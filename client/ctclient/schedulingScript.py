import subprocess
import time

def main () :
    startTime = time.time()
    start = 1
    end = 1000
    MAX_LOGS = 3000
    #MAX_LOGS = 1102363703
    filename = "testFile.txt"

    for index in range(1,MAX_LOGS,1000):
        start = index
        end = start + 1000
        process = subprocess.run([f"./ctclient -first {start} -last {end} getentries >> {filename}"], shell=True)
    
    print("Total Time:", time.time()-startTime)

if __name__ == "__main__":
    main()