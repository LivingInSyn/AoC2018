extern crate threadpool;
use std::sync::{Arc, Mutex, RwLock};
use std::thread;
use std::sync::mpsc::channel;
use threadpool::ThreadPool;

fn get_pvalue(serial_num: i32, x: i32, y: i32) -> i32 {
    let rack_id = x + 10;
    let mut plevel = ((rack_id * y) + serial_num) * rack_id;
    plevel = plevel / 100;
    if plevel > 10 {
        plevel = plevel % 10;
    } 
    else if plevel == 0 {
        return plevel;
    }
    return plevel - 5;
}

struct Answer {
    tsum: i32,
    topx: usize,
    topy: usize,
    tsize: usize,
}

fn main() {
    println!("in main");
    let serial_num = 9221;
    const gridsize: usize = 300;
    //build the grid
    let mut fuel_cell = vec![vec![0i32; gridsize]; gridsize];
    for xval in 1..gridsize+1 {
        for yval in 1..gridsize+1 {
            fuel_cell[xval-1][yval-1] = get_pvalue(serial_num, xval as i32, yval as i32);
        }
    }
    //put the grid into an rwlock
    let fclock = Arc::new(RwLock::new(fuel_cell));
    //
    let pool = ThreadPool::new(8);
    let tops = Answer {
        tsum: 0,
        topx: 0,
        topy: 0,
        tsize: 0,
    };
    let tops = Arc::new(Mutex::new(tops));
    // let tsum = Arc::new(Mutex::new(0));
    // let topx = Arc::new(Mutex::new(0));
    // let topy = Arc::new(Mutex::new(0));
    // let tsize = Arc::new(Mutex::new(0));
    
    let (tx, rx) = channel();
    println!("created arc mutexes");

    // let mut topsum = 0;
    // let mut topx = 0;
    // let mut topy = 0;
    // let mut topsize = 0;
    for xval in 1..gridsize+1 {
        println!("{}", xval);
        let blocks_processed = Arc::new(Mutex::new(0));
        for yval in 1..gridsize+1 {
            let (tops, blocks_processed, tx, fuel_cell) = (
                tops.clone(), blocks_processed.clone(), tx.clone(), fclock.clone()
            );
            // thread::spawn(move || {
            pool.execute(move || {
                let fuel_cell = fuel_cell.read().unwrap();
                for size in 1..gridsize - xval + 2 {
                    let mut blocksum = 0;
                    for x in xval..xval+size {
                        if x-1 >= gridsize {
                            break;
                        }
                        for y in yval..yval+size {
                            if y-1 >= gridsize {
                                break;
                            }
                            blocksum = blocksum + fuel_cell[x-1][y-1]
                        }
                    }
                    let mut tops = tops.lock().unwrap();
                    //let mut tsum = tsum.lock().unwrap();
                    if blocksum > tops.tsum {
                        tops.tsum = blocksum;
                        tops.topx = xval;
                        tops.topy = yval;
                        tops.tsize = size;
                    }
                    //println!("{},{} increasing bproc", xval, yval);
                    //let mut bproc = blocks_processed.lock().unwrap();
                    let mut bproc = blocks_processed.try_lock();
                    //println!("{},{} tlock", xval, yval);
                    if let Ok(ref mut b) = bproc {
                        **b += 1; 
                        if **b == gridsize {
                            tx.send(()).unwrap();
                        }
                    } else {
                        println!("ERROR LOCKING BPROC");
                    }
                }
            });
        }
        rx.recv().unwrap();
    }    
    let tops = tops.lock().unwrap();
    //println!("{} {} {} {}", tsum.lock().unwrap(), topx.lock().unwrap(), topy.lock().unwrap(), tsize.lock().unwrap());
    println!("{} {} {} {}", tops.tsum, tops.topx, tops.topy, tops.tsize);
}
