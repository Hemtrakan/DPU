import geometry

def main():
   need_cal = int(input("Enter Number 1 for start the program : "))
   while need_cal == 1:
      print("")
      print("<------------------------------------------------>")
      print("Enter number 1 for circle_area")
      print("Enter number 2 for circle_line")
      print("Enter number 3 for rectangle_area")
      print("Enter number 4 for rectangle_line")
      print("Enter number 5 for triangle_area")
      print("Enter number 6 for triangle_line")
      print("Enter number 0 for exit program")
      print("<------------------------------------------------>")
      number = int(input("Select the desired item. : "))
      
      # try:
      #    number = int(input("Select the desired item. : "))
      # except:
      #    continue
      # else:
      #    print("กรุณาใส่แต่ตัวเลขเท่านั้น")
      if number == 1:
         radius = float(input("Enter radius : "))
         res = geometry.circle_area(radius)
         print("<---------- Ans ---------->")
         print(f"circle_area = {res}")
         print("<---------- Ans ---------->")
         
      if number == 2:
         radius = float(input("Enter radius : "))
         res = geometry.circle_line(radius)
         print("<---------- Ans ---------->")
         print(f"circle_line = {res}")
         print("<---------- Ans ---------->")
         
      if number == 3:
         width  = float(input("Enter width : "))
         height = float(input("Enter height : "))
         res = geometry.rectangle_area(width, height)
         print("<---------- Ans ---------->")
         print(f"rectangle_area = {res}")
         print("<---------- Ans ---------->")
      
      if number == 4:
         width  = float(input("Enter width : "))
         height = float(input("Enter height : "))
         res = geometry.rectangle_line(width, height)
         print("<---------- Ans ---------->")
         print(f"rectangle_line = {res}")
         print("<---------- Ans ---------->")
         
      
      if number == 5:
         width  = float(input("Enter width : "))
         height = float(input("Enter height : "))
         res = geometry.triangle_area(width,height)
         print("<---------- Ans ---------->")
         print(f"triangle_area = {res}")
         print("<---------- Ans ---------->")
      
      if number == 6:
         side_a  = float(input("Enter side_a : "))
         side_b = float(input("Enter side_b : "))
         side_c = float(input("Enter side_c : "))
         res = geometry.triangle_line(side_a, side_b,side_c)
         print("<---------- Ans ---------->")
         print(f"triangle_line = {res}")
         print("<---------- Ans ---------->")
      
      if number == 0:
         print("Exit Programe")
         break
      
   if need_cal != 1:
         main()     

if __name__ == "__main__":
    main()