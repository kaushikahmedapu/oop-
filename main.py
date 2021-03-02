import bird
import datetime
import penguin
import parrot
today_time = datetime.datetime.now()
print(today_time)
bird1 = bird.Bird()
print(bird1.get_attribute())

bird2 = penguin.Penguin("Apu vai")
print(bird2.get_attribute())
bird3 = parrot.Parrot("Tipu")
print(bird3.get_attribute())
