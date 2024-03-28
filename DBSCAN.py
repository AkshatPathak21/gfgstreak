# City With the Smallest Number of Neighbors at a Threshold Distance

#solution using dijkstra algorithm
from heapq import *
from typing import List
class Solution:
    
    def findCity(self, n : int, m : int, edges : List[List[int]], distanceThreshold : int) -> int:
        adj={}
        
        for i in edges:
            src=i[0]
            des=i[1]
            cost=i[2]
            if src in adj:
                adj[src].append([des,cost])
            else:
                adj[src]=[[des,cost]]
            if des in adj:
                adj[des].append([src,cost])
            else:
                adj[des]=[[src,cost]]
        for i in range(n):
            if i not in adj:
                adj[i]=[]
        ans=[]
        for i in range(n):
            heap=[]
            heappush(heap,[0,i])
            dis=[float("inf")]*n
            dis[i]=0
            while heap:
                a=heappop(heap)
                cost=a[0]
                node=a[1]
                for i in adj[node]:
                    n1=i[0]
                    c1=i[1]
                    if c1+cost<dis[n1]:
                        dis[n1]=c1+cost
                        heappush(heap,[dis[n1],n1])
            ans.append(dis[:])
                
       
        
        mini=n+1
        city=-1
        for i in range(n):
            c=0
            for j in range(n):
                if ans[i][j]<=distanceThreshold:
                    c+=1
            if c<=mini:
                mini=c
                city=i
        return city
        
                    


#solution using floyd warshall algorithm
class Solution1:
    
    def findCity(self, n : int, m : int, edges : List[List[int]], distanceThreshold : int) -> int:
        adj=[[float("inf") for i in range(n)]for j in range(n)]
        for i in edges:
            src=i[0]
            des=i[1]
            cost=i[2]
            adj[src][des]=cost
            adj[des][src]=cost
        for i in range(n):
            
            adj[i][i]=0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if adj[i][k]==float("inf") or adj[k][j]==float("inf"):
                        continue
                    adj[i][j]=min(adj[i][j],adj[i][k]+adj[k][j])
        
        mini=n+1
        city=-1
        for i in range(n):
            c=0
            for j in range(n):
                if adj[i][j]<=distanceThreshold:
                    c+=1
            if c<=mini:
                mini=c
                city=i
        return city