import Build_Adj_matrix
import International_Nw_build
import buildNet
import neighborCalc
import shortest_paths

"Prerequisite files  (Can be found in Network_Databases):"
"our worldcities.csv file,"
"neighbours.csv (you can only use this sim with european cities,  neighbours was created by bruteforce, reading a map)"
"varuhus.csv- a file which contains on each row, the desired city, it's nation and the continent it is on, feel free to add cities"

def runMe1st():
    International_Nw_build.Nw_Build()

def runMe2nd():
    neighborCalc.buildNet()
    
def runMe3rd():
    Build_Adj_matrix.buildAdjMatrix()
    
def runMeLast():
    shortest_paths.build_shortest_path()
    

runMe1st()
runMe2nd()
runMe3rd()
runMeLast()
        
    
    