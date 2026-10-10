#wap to mine a log file and find out
#whether it contains 'python'.
with open( "log.txt") as f:
    content = f.read()

    if ("python" in content):
        print ( "present ")
    else :
        print ( "not present ")
        