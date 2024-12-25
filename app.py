import pandas as pd

FILE_NAME = "diamonds.csv"

def higher_cost(diamonds_mat):
    higher_price = 0
    index = 0
    index_of_high = 0
    for diamond in diamonds_mat:
        if diamond[6] > higher_price:
            higher_price = diamond[6]
            index_of_high = index
        index += 1
    print(f"{higher_price} in line {index_of_high+2} in {FILE_NAME}")

def average(diamonds_mat):
    sum_prices = 0
    count = 0
    # index_of_high = 0
    for diamond in diamonds_mat:
        sum_prices += diamond[6]
        count += 1
    print(f"The average is: {sum_prices/count}")

def count_ideal(diamonds_mat):
    count = 0
    for diamond in diamonds_mat:
        if diamond[1]=="Ideal": count += 1
    print(f"There are {count} Ideal diamonds")

def print_colors(colors):
    colors_str = ""
    for color in colors:
        colors_str += f"{color}, "
    return colors_str

def find_colors(diamonds_mat):
    colors = set()
    for diamond in diamonds_mat:
        colors.add(diamond[2])
    print(f"There are {len(colors)} colors: {print_colors(colors)}")

def find_median_primeum_carat(diamonds_mat):
    primeum_carat = []
    for diamond in diamonds_mat:
        if diamond[1] == "Premium": primeum_carat.append(diamond[0])
    primeum_carat.sort()
    print(f"The median is: {primeum_carat[int(len(primeum_carat)/2)]}")

def average_carats(diamonds_mat):
    #find the different types of cut
    cuts_set = set()
    for diamond in diamonds_mat:
        cuts_set.add(diamond[1])

    cuts_list = []
    for cut in cuts_set:
        # gets the count of spesific cut and its sum of carats
        cut_data = {"cut":cut, "count":0, "carats_sum":0}
        for diamond in diamonds_mat:
            if diamond[1]==cut:
                cut_data["count"] +=1
                cut_data["carats_sum"] += diamond[0]
        cuts_list.append(cut_data)
    for cut in cuts_list:
        print(f"The average of {cut["cut"]} is: {cut["carats_sum"]/cut["count"]}")

def average_price_for_color(diamonds_mat):
    #find the different types of colors
    color_set = set()
    for diamond in diamonds_mat:
        color_set.add(diamond[2])

    color_list = []
    for color in color_set:
        # gets the count of spesific color and its sum of price
        color_data = {"color":color, "count":0, "price_sum":0}
        for diamond in diamonds_mat:
            if diamond[2]==color:
                color_data["count"] +=1
                color_data["price_sum"] += diamond[6]
        color_list.append(color_data)
    for color in color_list:
        print(f"The average of {color["color"]} price is: {color["price_sum"]/color["count"]}")

if __name__ == "__main__":
    df = pd.read_csv(FILE_NAME)
    diamonds = df.values.tolist() # convert the data frame to mat
    print("\nQ.1: What the higher cost of diamond?")
    higher_cost(diamonds)
    print("\nQ.2: What the average price of diamond?")
    average(diamonds)
    print("\nQ.3 How many Ideal diamonds are exist?")
    count_ideal(diamonds)
    print("\nQ.4 How many and which color there are?")
    find_colors(diamonds)
    print("\nQ.5 What is the median of Primeum diamonds carat?")
    find_median_primeum_carat(diamonds)
    print("\nQ.6 What is the carat average of the dfferent cuts?")
    average_carats(diamonds)
    print("\nQ.7 What is the price average of the different colors?")
    average_price_for_color(diamonds)