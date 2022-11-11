def main():
    city_graph = {}

    while(True):
        option = str(input("Please enter [e] - to exit, or any character to continue entering city name: "))
        if option == "e":
            break
        city_1 = str(input("Please enter first city name: "))
        city_2 = str(input("Please enter second city name: "))

        distance = int(input("Please enter distance between cities: "))
        if city_1 in city_graph.keys():
            updated_map = city_graph[city_1]
        else:
            updated_map = {}
        updated_map[city_2] = distance
        city_graph[city_1] = updated_map

    print(city_graph)

if __name__ == "__main__":
    main()