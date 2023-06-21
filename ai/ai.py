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
from pygame.sprite import RenderUpdates
class AI:
    """Class for moving enemies and firing towers"""
    def __init__(self,level:dict,enemies:RenderUpdates) -> None:
        self.level=level
        self.enemies = enemies
        self.enemypaths ={}
        self.available_paths = {}

        #this is silly needs to be done better
        for enemy in enemies:
            self.enemypaths[enemy]=["",0]

    #path finding methods
    def najdi_sousedy(self,vertex:Rect,visited:list[Rect]=[])->list[Rect]:
        """Returns not visited neighbours for a vertex"""
        path=self.level["path"]
        sousedi=[]
        #print(vertex)
        for node in path:
            if node in visited:continue
            distance = (abs(node.x-vertex.x),abs(node.y-vertex.y))
            if distance==(0,16) or distance==(16,0):
                #print(vertex.x,vertex.y,node.x,node.y)
                sousedi.append(node)
        return sousedi

    def find_paths(self,start:Rect)->None:
        """Finds all the paths in the level"""
        vertex=start[0]
        q = Queue()
        q.put((vertex,1))
        self.available_paths[1]=[]
        while not q.empty():
            node,cesta=q.get()
            print(self.available_paths[1])
            #print("current",node,cesta, self.available_paths[cesta])
            self.available_paths[cesta].append(node)
            sousedi = self.najdi_sousedy(node,self.available_paths[cesta])

            if node == self.level["end"][0] or not len(sousedi):
                continue
            
            q.put((sousedi.pop(),cesta))
            for soused in sousedi:
                pathid = len(list(self.available_paths))+1
                #print(pathid)
                self.available_paths[pathid] = [self.available_paths[cesta].copy()]
                q.put((soused,pathid))

    def get_next_step(self,enemy:object):
        """Returns next step in the apropriet path for the enemy"""
        pathid = self.enemypaths[enemy][0]
        self.enemypaths[enemy][1] +=1
        positionindex =self.enemypaths[enemy][1]
        return self.available_paths[pathid][positionindex]

    #not working do not use!!
    def assign_path_to_enemies(self)->None:
        """For every enemy in game it chooses the correct path"""
        for i,enemy in enumerate(list(self.enemies)):
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