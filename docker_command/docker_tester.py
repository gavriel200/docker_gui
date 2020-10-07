from dockercom import Images
from dockercom import Container

# (a b c d e f g h i j k l m n o p)

# a = Images.just_images()
# print(a)

# b = Images.list_images()
# print(b)

# c = Images.load_image("C:/Users/gabi_r/Desktop/vsftpd_server.tar")
# print(c)

# d = Images.run_image('ubuntua', ["5672:5672","-p","100:100","-p"], ["C://Users//gabi_r//Desktop//test2:/app/", "-v"], False)
# print(d)

# e = Images.save_image("rabbitmq:3", "C:/Users/gabi_r/Desktop/test3/rabbit.tar")
# print(e)

# f = Images.change_image_tag("rabbitmq:3", "rabbitmq")
# print(f)

# g = Container.list_containers()
# print(g)

# h = Container.save_container("29b243538d6f", "vsftpd:blabla")
# print(h)

# i = Container.start_or_stop_containers("29b243538d6e")
# print(i)

# # j = Container.start_container_in_bash("29b243538d6e")
# # print(j)

# k = Container.running_containers()
# print(k)

# l = Container.remove_container("745f2530a7d7")
# print(l)