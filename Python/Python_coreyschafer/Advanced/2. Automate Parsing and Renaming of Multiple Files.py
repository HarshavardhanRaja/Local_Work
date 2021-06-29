"""

imort os

os.chdir('path')
print(os.getcwd())


for f in os.lisdir():
    print(f)
    f_name, f_ext = os.path.splittext(f)            # returns tuple with two elements: first elemnt as file name with out extension, 2nd element as extension
    print(f_name.split('-'))
    f_title, f_course, f_num = f_name.split('-')
   
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)

    print('{}-{}-{}.{}'.format(f_num, f_course, f_title, f_ext))

    new_name = '{}-{}-{}.{}'.format(f_num, f_course, f_title, f_ext
    os.rename(f, new_name)

"""