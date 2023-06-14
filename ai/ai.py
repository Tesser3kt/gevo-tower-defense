#najítí všech tras(path,start,end) ->trasy
#začít na startu a jít po barevnejch pixelech. každé rozdvojení vytváří novou cestu
#   pohyb enemáků(trasy) ->pohyb vektor

#může věž střílet(věž,enemak) ->bool
#vyslat fake projektil a zjistit jestli tam není zeď

#jakým směrem střílet(věž,enemak) ->vektor
#   jak dlouho to poletí na současnou polohu
#   posunout enemaka o ten čas vrátit jeho směr od věže
from pygame import Rect
from queue import Queue

class AI:
    """Class for moving enemies and firing towers"""
    def __init__(self,level:dict,enemies:list) -> None:
        self.level=level
        self.enemies=enemies
        self.available_paths = {}
        self.subsequent={}
        self.enemy_paths=[]
        self.paths_names = ["b","c","d","e"]


    #path finding methods
    def najdi_sousedy(self,vertex:Rect,visited:list[Rect]=[])->list[Rect]:
        """Returns not visited neighbours for a vertex"""
        path=self.level["path"]
        sousedi=[]
        for node in path:
            if node in visited:continue
            print(vertex)
            distance = (abs(vertex[0].x-node.x),abs(vertex[0].y-node.y))
            if distance[0]==1 or distance[1]==1:
                sousedi.append(node)
        return sousedi

    def find_paths(self,start:Rect,visited:list[Rect]=[])->None:
        """Arranges all the paths between different rozcestí"""
        vertex=start
        q = Queue()
        q.put((vertex,"a"))
        self.available_paths["a"]=[]
        while q.not_empty:
            node,cesta=q.get()
            self.available_paths[cesta].append(node)
            sousedi = self.najdi_sousedy(node,self.available_paths[cesta])
            
            if node == self.level["end"] or not len(sousedi):
                continue

            q.put((sousedi.pop(),cesta))
            for soused in sousedi:
                pathid = self.paths_names[len(list(self.available_paths))]
                self.available_paths[pathid] = [soused]
                q.put((soused,pathid))

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
    
    def get_next_step(self,enemy_index:int)->tuple:
        """Returns next step for the enemy"""
        return self.enemy_paths[enemy_index].pop(0)