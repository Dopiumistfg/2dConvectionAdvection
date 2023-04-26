# 2d Convection Advection

This case study involved discretization and coding for 2d Natural convection and Advection

The problem statement involved a hollow 2d plate with one wall at a temperature T and the others at room temperature or 0.

The governing equations are as follows:

![](https://drive.google.com/file/d/1Zx9Kj7cxk9OrllrvLnxn54OACVSO5hsY/view?usp=share_link)
![](https://drive.google.com/file/d/1zlKz6XYhIuPPGrhgZOrik2JU7Rncveal/view?usp=share_link)
![](https://drive.google.com/file/d/1XBWQIcUzfbJ5dIwHAdS1cyjQZLTQwK7r/view?usp=share_link)
![](https://drive.google.com/file/d/1igjQKHUCI5s2xd96MjX6MnI9wHlBGt4D/view?usp=share_link)

However the pressure gradient is unkown to us and hence we will be using the Stream function and Vorticity approach where

![](https://drive.google.com/file/d/1qzdp7owaQTe_B7OXBkPga7JKFJLyL8kQ/view?usp=share_link)
![](https://drive.google.com/file/d/1Fry9Wh6l-iWhPDDd8b4LecYyh6vMaYmp/view?usp=share_link)

So the new Governing equations will look like

![](https://drive.google.com/file/d/1h3e-4sy5PHevvMEpF7VK0wSMUdFZvZ_N/view?usp=share_link)
![](https://drive.google.com/file/d/1NsHaNPkeZSlfvXdN-wzX_8bcqfreusKM/view?usp=share_link)
![](https://drive.google.com/file/d/1fBcNRtU7En5dwMZUjFV3zkwhY_Pqpkbi/view?usp=share_link)

After discretization, the equations will finally look like

![](https://drive.google.com/file/d/1Btgmc4DJGOxKz95qNY2dh6c51_3Ae8na/view?usp=share_link)
![](https://drive.google.com/file/d/1BlRQuqfjG3YJWIVVWUZ-h-uVbX1vtNpt/view?usp=share_link)
![](https://drive.google.com/file/d/1gMehbaF8CDhggBlLygYf5FFeP6fK55wg/view?usp=share_link)

Advection:
![](https://drive.google.com/file/d/18e5Oy37b4a2Rv8WD5O1idk-DJFhv8fen/view?usp=share_link)

Convection:
![](https://drive.google.com/file/d/1cO9EEmDF6TDLm5CsKJQeSw4DrKo_ppg3/view?usp=share_link)
