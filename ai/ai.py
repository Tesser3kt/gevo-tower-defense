#najítí všech tras(path,start,end) ->trasy
#začít na startu a jít po barevnejch pixelech. každé rozdvojení vytváří novou cestu
#   pohyb enemáků(trasy) ->pohyb vektor

#může věž střílet(věž,enemak) ->bool
#vyslat fake projektil a zjistit jestli tam není zeď

#jakým směrem střílet(věž,enemak) ->vektor
#   jak dlouho to poletí na současnou polohu
#   posunout enemaka o ten čas vrátit jeho směr od věže


from re import I


class AI:
    def __init__(self,level:dict,) -> None:
        self.level=level


    def najdi_sousedy(self,vertex:tuple[int],path,visited:list[tuple[int]]=[])->list[tuple[int]]:
        path=self.level["path"]
        sousedi=[]
        for node in path:
            if node in visited:continue
            distance = (abs(vertex[0]-node[0]),abs(vertex[1]-node[1]))
            if distance[0]==1 or distance[1]==1:
                sousedi.append(node)


    def find_paths(self,start:tuple[int],visited:list[tuple[int]]=[],cesty:list=[])->list[list[tuple[int]]]:
        vertex=start
        cesty=cesty
        heap = [vertex]
        while len(heap):
            node=heap.pop()
            visited.append(node)
            if node == self.level["end"][0]:break

            sousedi = self.najdi_sousedy(node,self.level["path"],visited)
            
            if len(sousedi)>1:
                for i in range(len(sousedi)-1):
                    self.find_paths(sousedi[i],visited,cesty)
            
            heap.append(sousedi[len(sousedi)-1])
        cesty.append(visited)