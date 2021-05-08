from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# Build your program below:
landmark_string = ""
for letter, landmark in landmark_choices.items():
  landmark_string += "{0} - {1}\n".format(letter, landmark)

def greet():
  print("Hi there and wilcome to SkyRoute!")
  print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

def skyroute():
  greet()
  new_route()
  goodbye()
 
def set_start_and_end(start_point, end_point):
  if(start_point != None):
    change_point  = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
    if change_point == 'b':
      start_point = get_start()
      end_point = get_end()
    elif change_point == 'o':
      start_point = get_start()
    elif change_point == 'd':
      end_point = get_end()
    else:
      print("Oops, that isn't 'o', 'd', or 'b'...")
      set_start_and_end(start_point, end_point)
  else:
    #print("else statement")
    start_point = get_start()
    end_point = get_end()
  return start_point, end_point

def get_start():
  start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
  if start_point_letter in landmark_choices:
    start_point = landmark_choices[start_point_letter]
    return start_point
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    get_start()

def get_end():
   end_point_letter = input("Ok, where are you headed? Type in the corresponding letter:" )
   if end_point_letter in landmark_choices:
     end_point = landmark_choices[end_point_letter]
     return end_point
   else:
     print("Sorry, that's not a landmark we have data on. Let's try this again...")
     get_end()

def new_route(start_point = None, end_point = None):
  start_point, end_point = set_start_and_end(start_point, end_point)
  shortest_route = get_route(start_point, end_point)
  shortest_route_string = '\n'.join(shortest_route)
  print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
  again = input("Would you like to see another route? Enter y/n: ")
  if again == 'y':
    show_landmarks()
    new_route(start_point, end_point)
def show_landmarks():
  see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")
  if see_landmarks == 'y':
    print(landmark_string)


def get_route(start_point, end_point):
  start_stations = vc_landmarks[start_point]
  end_stations = vc_landmarks[end_point]
  routes = []
  for start_station in start_stations:
    for end_station in end_stations:
      route = bfs(vc_metro, start_station, end_station)
      if route:
        routes.append(route)
  shortest_route = min(routes, key=len)
  return shortest_route

#print(get_route('Marine Building','Central Park' ))

def goodbye():
  print("Thanks for using SkyRoute!")
skyroute()



