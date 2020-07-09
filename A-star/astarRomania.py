#
#   Created by PyCharm.
#   User: Rizky Andre Wibisono
#   Date: 17/03/2019
#   Time: 20:59
#

import heapq


class priorityQueue:
    def __init__(self):
        self.cities = []

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))

    def pop(self):
        return heapq.heappop(self.cities)[1]

    def isEmpty(self):
        if (self.cities == []):
            return True
        else:
            return False

    def check(self):
        print(self.cities)


class ctNode:
    def __init__(self, city, distance,roadState,danger):
        self.city = str(city)
        self.distance = str(distance)
        self.roadState = str(roadState)
        self.danger = str(danger)


romania = {}


def makedict():
    file = open("romania.txt", 'r')
    for string in file:
        line = string.split(',')
        ct1 = line[0]
        ct2 = line[1]
        dist = int(line[2])
        rdState = int(line[3])
        dger = int(line[4])
        romania.setdefault(ct1, []).append(ctNode(ct2, dist, rdState, dger))
        romania.setdefault(ct2, []).append(ctNode(ct1, dist, rdState, dger))


def makehuristikdict():
    h = {}
    with open("romania_sld.txt", 'r') as file:
        for line in file:
            line = line.strip().split(",")
            node = line[0].strip()
            sld = int(line[1].strip())
            h[node] = sld
    return h

def variante(estado, seguridad, distancia):

    return (pow(seguridad, 2) * distancia)/estado;

def heuristic(node, values):
    print ("Valor Nodo: "+str(values[node]))
    return values[node]


def astar(start, end):
    path = {}
    distance = {}
    q = priorityQueue()
    h = makehuristikdict()

    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []

    while (q.isEmpty() == False):
        current = q.pop()
        expandedList.append(current)

        if (current == end):
            break

        for new in romania[current]:
            g_cost = distance[current] + int(new.distance)

            #print("Costo Actual \n")
            #print(new.city, new.distance, "now : " + str(distance[current]), g_cost)
            #variante(new.roadState, new.danger, int(new.distance))
            if (new.city not in distance or g_cost < distance[new.city]):
                distance[new.city] = g_cost
                f_cost = g_cost + heuristic(new.city, h) + variante(int(new.roadState), int(new.danger), int(new.distance))
                q.push(new.city, f_cost)
                path[new.city] = current

    printoutput(start, end, path, distance, expandedList)


def printoutput(start, end, path, distance, expandedlist):
    finalpath = []
    i = end

    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()
    print("Programa A* Rumania")
    print("\tArad => Bucharest")
    print("=======================================================")
    print("Ciudades que pueden ser exploradas \t\t: " + str(expandedlist))
    print("Posible numero de ciudades \t\t: " + str(len(expandedlist)))
    print("=======================================================")
    print("La ciudad que se recorre con la distancia más corta.\t: " + str(finalpath))
    print("Número de ciudades atravesadas \t\t\t: " + str(len(finalpath)))
    print("Distancia total \t\t\t\t\t\t: " + str(distance[end]))


def main():
    src = "Mehadia"
    dst = "Bucharest"
    makedict()
    astar(src, dst)


if __name__ == "__main__":
    main()
