import matplotlib.pyplot as plt
d1={"Main Entrance":[0],'Entrance/Exit2':[2], "TT Gallery1/Shakespeare Gallery":[3],"Lift1":[5],"Entrance/Exit1":[8],"Gents Washroom":[6],"Ladies Washroom":[8],"Room: 38,37":[0,1],"Room: 35,36":[1,2],"Room: 30-32":[3,4],"Room: 33,34":[2,3],"Room: 25-27":[3,4],'CTS':[7],"Room: 15,14":[7,8],"Room: 12,13":[8,9],"Room: 10,11":[9,10],"Room: 6-9":[10,12], "Room: 3-5":[12,13],"Room: 1,2,20":[13,0],"Room: 18,19,21,22":[8,13],"Lift2 & Stairs":[7,0],"Room: 39-43":[6,1],"Nescafe":[4],'Amphitheatre':[11]}
distance=[]
w=[]
class Graph: 
    
    def minDistance(self,dist,queue): 
        minimum = float("Inf") 
        min_index = -1 
        for i in range(len(dist)): 
            if dist[i] < minimum and i in queue: 
                minimum = dist[i] 
                min_index = i 
        return min_index 
  
    def printPath(self, parent, j): 
          
        if parent[j] == -1 :  
            w.append(j)
            print(j), 
            return
        self.printPath(parent , parent[j]) 
        w.append(j)
        print(j) 
    
    def printSolution(self, dist, parent): 
        #print("Vertex \t\tDistance from Source\tPath") 
        '''for i in range(1, len(dist)): 
            print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])), 
            self.printPath(parent,i)'''

        self.printPath(parent,p)
        distance.append(dist[p])
  
  
    '''Dijkstra's single source shortest path 
    algorithm'''
    def dijkstra(self, graph, src,p): 
  
        row = len(graph) 
        col = len(graph[0])
        #print(row,col)
  
        dist = [float("Inf")] * row 
  
        parent = [-1] * row 

        dist[src] = 0
      
        queue = [] 
        for i in range(row): 
            queue.append(i) 
        
        while queue: 
  
            u = self.minDistance(dist,queue)  
       
            queue.remove(u) 
  
            for i in range(col): 
                if graph[u][i] and i in queue: 
                    if dist[u] + graph[u][i] < dist[i]: 
                        dist[i] = dist[u] + graph[u][i] 
                        parent[i] = u 
                
  
        self.printSolution(dist,parent) 
        return dist[p]
  
g= Graph() 
  
graph = [[0,25,0,0,0,0,0,0,0,0,0,0,0,25,0,25,0], 
        [25,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,25], 
        [0,25,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0], 
        [0,0,25,0,12,25,0,0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,12,0,0,0,0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,25,0,0,25,0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,25,0,25,0,0,0,0,0,0,0,0,25], 
        [0,0,0,0,0,0,25,0,25,0,0,0,0,0,0,25,0], 
        [0,0,0,0,0,0,0,25,0,25,0,0,0,0,25,0,0],
        [0,0,0,0,0,0,0,0,25,0,25,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,25,0,12,25,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,12,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,25,0,0,25,0,0,0],
        [25,0,0,0,0,0,0,0,0,0,0,0,25,0,25,0,0],
        [0,0,0,0,0,0,0,0,25,0,0,0,0,25,0,0,0],
        [25,0,0,0,0,0,0,25,0,0,0,0,0,0,0,0,0],
        [0,25,0,0,0,0,25,0,0,0,0,0,0,0,0,0,0]
        ] 

src=int(input("Enter source location: "))

print('Choose your destination:')
a=list(d1.keys())
for i in range(0,len(d1)):
    print(str(i),a[i])
dest=int(input('Enter your Destination:'))  
if(len(d1[a[dest]])==1):
    p=d1[a[dest]][0]
    k=00
    
else:
    k=1
    if(g.dijkstra(graph,src,d1[a[dest]][0])<g.dijkstra(graph,src,d1[a[dest]][1])):
        w=[]
        p=d1[a[dest]][0]
    else:
        p=d1[a[dest]][1]
        w=[]
g.dijkstra(graph,src,p) 
print(w)
if(k==1):
    w.append(d1[a[dest]][0])
fig,ax=plt.subplots()
x=[0,-25,-50,-50,-38,-50,-25,0,25,50,50,38,50,25,25,0]
y=[0,0,0,25,25,50,50,50,50,50,25,25,0,0,25,25]
xnav=[]
ynav=[]
img=plt.imread("Map.jpg")
imgu=plt.imread("up.png")
imgd=plt.imread("down.png")
imgl=plt.imread("left.png")
imgr=plt.imread("right.png")

for i in range(0,len(w)):
    xnav.append(x[w[i]])
    ynav.append(y[w[i]])
ax.imshow(img,extent=[-55,55,-5,55])

for i in range(0,len(xnav)-1):
    if(xnav[i+1]>xnav[i]):
        ax.imshow(imgr,extent=[(xnav[i+1]+xnav[i])/2-1,(xnav[i+1]+xnav[i])/2+1,ynav[i]-1,ynav[i]+1])
    if(xnav[i+1]<xnav[i]):
        ax.imshow(imgl,extent=[(xnav[i+1]+xnav[i])/2-1,(xnav[i+1]+xnav[i])/2+1,ynav[i]-1,ynav[i]+1])
    if(ynav[i+1]>ynav[i]):
        ax.imshow(imgu,extent=[(xnav[i+1]+xnav[i])/2-1,(xnav[i+1]+xnav[i])/2+1,(ynav[i+1]+ynav[i])/2-1,(ynav[i]+ynav[i+1])/2+1])
    if(ynav[i+1]<ynav[i]):
        ax.imshow(imgd,extent=[(xnav[i+1]+xnav[i])/2-1,(xnav[i+1]+xnav[i])/2+1,(ynav[i+1]+ynav[i])/2-1,(ynav[i]+ynav[i+1])/2+1])
plt.scatter(x,y)
plt.plot(xnav,ynav,color='red')
if(k==1):
    plt.plot((xnav[-2],xnav[-1]),(ynav[-2],ynav[-1]),color='green')
plt.savefig('Path.png')
plt.close('all')