## 🛗Offline algorithm for smart elevator🛗
Waiting for an elevator is a situation with which we are all familiar. We press a button and then wait for an elevator to arrive traveling in the right direction. We may have to wait a long time if there are too many passengers or not enough elevators. Just how long we wait depends on the dispatching strategy the elevators use to decide where to go.Elevator dispatching is a good example of a stochastic optimal control problem of economic importance that is too large to solve by classical techniques such as dynamic programming.

## 💡INTRODUCTION💡:
Elevators have been built throughout history but the first modern passenger elevators were developed
no more than about 150 years ago. Steam and hydraulic elevators had already been introduced by
1852, when Elisha Otis made one of the most important elevator inventions, the clutch, which
prevented the elevator from falling. Following this, in 1857, the first passenger elevator was installed
in the store of E. Haughwout&Company, New York.The development of elevator technology was fast.

## ❓What is the difference between an on-line and off-line algorithm?❓:
In computer science, an online algorithm is one that can process its input piece-by-piece in a serial fashion, i.e., in the order that the input is fed to the algorithm, without having the entire input available from the start. In contrast, an offline algorithm is given the whole problem data from the beginning and is required to output an answer which solves the problem at hand

## 🔎What does a smart elevator mean🔎:
Smart elevators are designed to transform the simple act of traveling between floors. Instead of pushing a button to go up or down, passengers first select the floor they want. Then they are directed to the elevator that will take them to their destination with the fewest number of stops.

## 💡My algorithm💡:
Given a csv file and json files, the algorithm will read the files and perform a number of operations:
1. The algorithm will calculate the location of each elevator in relation to the time of each reading and will be entered in another field in the elevator class called pos_and_time
2. The algorithm will go through all the requests and place the elevator for each request which will perform its purpose in the shortest time of all the elevators (taking into account the given times, the location of the elevator, the time it takes for the elevator to go one floor, the number of elevators, up / down elevator mode and end previous readings)
3. In some cases the elevator will make several requests simultaneously depending on the situation. As for example the elevator goes up from floor x to floor y the elevator will take all requests between x and y (as long as the elevator has not passed the source of the additional request)


## ✨Diagram class✨
![](https://imagizer.imageshack.com/img924/9083/g3rQkP.png)






## 🔗Links🔗:
- [Showcase of Elevator Simulator](https://www.youtube.com/watch?v=LZauW_Zfepk)

- [Elevator call logic, the old OTIS system](https://www.youtube.com/watch?v=BCN9mQOT3RQ)

- [DUPLEX elevator call logic - how does THAT work?](https://www.youtube.com/watch?v=oY1QlCqWOss)

- [Planning and Control Models for Elevators in High-Rise Buildings](https://drive.google.com/file/d/1-8bHEAO5y-wUhEXrZxPwiLVHvs287JvW/view?usp=sharing)

- [Exemplar-based Control of Multi-Car Elevators and its Multi-Objective Optimization using Genetic Algorithm ](https://drive.google.com/file/d/1Ij0-IkqT8ht1cI2r4OyS4Wl7XofV7d0a/view?usp=sharing)




## ✨ Illustration✨ :

![](https://web.eecs.umich.edu/~baveja/RLMasses/img1.gif)
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnbdlelnb4xti3KRgMk7hx7Hlaey2VQCr1ig&usqp=CAU)
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnyILq_pWPFHNPQqc1pfvAFe-RXYsJnMZtWw&usqp=CAU)


## 💡Reported results💡

![](https://github.com/nivk99/OOP_Ex1/blob/main/offline_algo_page-0001.jpg)

## ©️license & copyright©️:

**© Kotek Niv** 
📧 <niv.kotek@msmail.ariel.ac.il >



