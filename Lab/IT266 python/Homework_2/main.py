import geometry
import func_average
import func_min
import func_max

def main():
    list_items = []
    while True:
         try:
            item = input("Enter Number and Type 'done' for Calculate : ")
            if item.lower() != "done":
                  list_items.append(item)
         
            if item.lower() == "done":
               circle_area = geometry.circle_area(list_items)
               circle_line = geometry.circle_line(list_items)
               average = func_average.average(circle_area)
               min = func_min.min(circle_area)
               max = func_max.max(circle_area)
               print()
               print(f"CircleArea : {circle_area}")
               print(f"CircleLine : {circle_line}")
               print(f"Average : {average}")
               print(f"Min : {min} , Max : {max}")
               print()
               break
         except:
            print("<-------------------------------------->")
            print()
            print(f"Input Error {list_items}")
            print()
            print("<-------------------------------------->")
            main()
            break

if __name__ == "__main__":
    main()