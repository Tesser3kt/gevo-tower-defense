#najítí všech tras(path,start,end) ->trasy
#začít na startu a jít po barevnejch pixelech. každé rozdvojení vytváří novou cestu
#   pohyb enemáků(trasy) ->pohyb vektor

#může věž střílet(věž,enemak) ->bool
#vyslat fake projektil a zjistit jestli tam není zeď

#jakým směrem střílet(věž,enemak) ->vektor
#   jak dlouho to poletí na současnou polohu
#   posunout enemaka o ten čas vrátit jeho směr od věže


class AI:
    def __init__(self,level:dict,enemies:list) -> None:
        self.level=level
        self.enemies=enemies
        self.available_paths = []
        self.subsequent={}
        self.enemy_paths=[]

    def najdi_sousedy(self,vertex:tuple[int],path,visited:list[tuple[int]]=[])->list[tuple[int]]:
        """Returns not visited neighbours for a vertex"""
        path=self.level["path"]
        sousedi=[]
        for node in path:
            if node in visited:continue
            distance = (abs(vertex[0]-node[0]),abs(vertex[1]-node[1]))
            if distance[0]==1 or distance[1]==1:
                sousedi.append(node)
        return sousedi

    def find_paths(self,start:tuple[int],visited:list[tuple[int]]=[])->None:
        """Arranges all the paths between different rozcestí"""
        vertex=start
        heap = [vertex]
        while True:
            node=heap.pop()
            visited.append(node)
            if node == self.level["end"][0]:break

            sousedi = self.najdi_sousedy(node,self.level["path"],visited)
            
            if len(sousedi)>1:
                for i in range(len(sousedi)):
                    self.find_paths(sousedi[i],[node])
            else:
                visited.append(sousedi[0])
                heap.append(sousedi[0])

        self.available_paths.append(visited)

    def subsequent_paths(self)->None:
        """For every rozcesti writes the indexes for the paths that come after it"""
        for path1 in enumerate(self.available_paths):
            self.subsequent[path1[len(path1)]]=[]
            for i,path2 in enumerate(self.available_paths):
                if path1[len(path1)]==path2[0]:
                    self.subsequent[path1[len(path1)]].append(i)

    def sort_paths(self)->None:
        """Sorts indexes for paths by their length"""
        for rozcesti in self.subsequent:
            self.subsequent[rozcesti]=sorted(self.subsequent[rozcesti], key=lambda x: len(self.available_paths[x]))
    
    def assign_path_to_enemies(self)->None:
        """For every enemy in game it chooses the correct path"""
        for i,enemy in enumerate(self.enemies):
            preference = "long" #this will be assigned depending on the enemytype and their preferency
            path = [x for x in self.available_paths[0]]
            rozcesti = path[len(path)]
            while rozcesti!=self.level["end"]:
                if preference=="long": #chooses the last element of the rozcesti->longest path
                    subpath=self.available_paths[self.subsequent[rozcesti][len(self.subsequent[rozcesti])]]
                    path.append([x for x in subpath])
                    rozcesti = path[len(path)]
                elif preference=="short": #chooses the first->shortest path
                    subpath = self.available_paths[self.subsequent[rozcesti][0]]
                    path.append([x for x in subpath])
                    rozcesti = path[len(path)]
                elif preference=="middle": #chooses something aproximetly in the middle
                    subpath = self.available_paths[self.subsequent[rozcesti][len(self.subsequent[rozcesti])//2]]
                    path.append([x for x in subpath])
                    rozcesti = path[len(path)]
            self.enemy_paths[i]=path