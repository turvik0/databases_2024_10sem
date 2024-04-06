1)Возьмем датасет на 20 мб (data.json)
2)Запустим контейнер с Redis, прокинув порт 6379. (Dockerfile)
![alt text](image.png)
3)Используя библиотеку redis и питон, будем переводить наш JSON в различные форматы и закидывать их в контейнер. (main.py)
4)Наш контейнер
![alt text](image-1.png)
5)Для мастер создадим redis_master.config и Dockerfile.master, для реплик redis_replica.conf и dockerfile.replica
![alt text](image-2.png)
6)В итоге наш кластер:
![alt text](image-3.png)
А также мастер и слэйвы:
![alt text](image-4.png)
![alt text](image-5.png)
7)Добавим ключ в мастер и удостоверимся что он появился в реплике:
мастер:
![alt text](image-6.png)
реплика:
![alt text](image-7.png)