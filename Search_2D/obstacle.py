# Circle obstacle
middle_point_list = [(10, 12), (20, 20), (70, 70), (10, 70),
                     (30,80),(40,10),(50,70),(80,10), (90,20),
                     (20,40),(25,40),(28,5), (60,10),(60,30),
                     (50,50), (60,70), (90,80), (90,56), (60,60),
                     (70,55), (80,40),(40,40), (30,60),(70,85),
                     (80,75),(25,30)]
# middle_point_list = [(10, 80), (80, 10)]
# middle_point_list = [(10, 10), (80, 80)]
radius_list = [3, 5, 3, 5,4,3,4,5,3,2,3,3,2,5,3,2,3,4,3,3,7, 5,4,5,3,5]
# radius_list = [3, 3]

x_range = 100
y_range = 100

s_start = (0, 0)
s_goal = (100, 100)

motions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
           (1, 0), (1, -1), (0, -1), (-1, -1)]
