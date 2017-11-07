

class JSONLevels():
    # cstruct =["""{"name":"Generated level72","size":[4,4],"walls":[[0,3],[1,0],[2,0]],"levels":[{"id":0,"start":[0,0],"complexity":4,"minLength":14,"maxLength":14}]}""",
    #           """{"name":"Generated level160","size":[5,5],"walls":[[0,0],[2,1],[4,3],[4,4]],"levels":[{"id":0,"start":[2,3],"complexity":22,"minLength":23,"maxLength":23}]}""",
    #           """{"name":"Generated level20","size":[6,6],"walls":[[0,5],[2,0],[2,3],[3,3],[5,4],[5,5]],"levels":[{"id":0,"start":[2,2],"complexity":52,"minLength":32,"maxLength":32}]}""",
    #           """{"name":"Generated level160","size":[5,5],"walls":[[2,1],[4,3],[4,4],[0,0]],"levels":[{"id":1,"start":[2,3],"complexity":44,"minLength":22,"maxLength":22}]}"""]

    cstruct = []

    def load_levels_from_file(self, file_name):
        f = open(file_name)
        for line in f.readlines():
            self.cstruct.append(line)