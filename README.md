# thesis-code-2025
My code I used/created under my thesis for creating my "fake" sensors.

<-------------------------------------------------------------------------------------------------------------------------------------------------------------------------->

Quick Step-By-Step

1. Started by creating an 'Installation' in IoT-Open with the company's information, such as name, address, users, etc.

2. Here I set up the necessary tools I will need to get everything working properly. I am using Docker Desktop for this.
I have created three containers:

    - An Edge client for IoT-Open.

    - A Grafana instance to transfer data from IoT-Open to Grafana.

    - A Node-RED instance to create various "rules" if necessary.

![image](https://github.com/user-attachments/assets/530ccc25-4d37-4b0e-9de6-e21d138091ca)

3. In step three, it is simply a matter of sitting down and starting to write code for each sensor the customer wishes to simulate. I am using Visual Studio Code for this.
In my case, I had the following sensors to simulate data for:

    - Noise / Noise Warning = Noise level measurement with warnings. (Environment)

    - Presence = Information about whether someone is present in a specific room. (Environment)

    - Temperature / Temperature Warning = Temperature measurement with warnings. (Environment)

    - Vibration / Vibration Warning = Vibration measurement with warnings. (Machine)
  
4. After the code is completed for all sensors, the final step is to create each device in the platform and configure its functions.

5. You can now see in the "MQTT-Realtime" window how the data starts streaming into IoT-Open. This indicates that everything is correctly configured and working as expected.

![image](https://github.com/user-attachments/assets/c9afcf38-0cf4-4a0b-8c04-be9acb336669)

6. The final step of the project was to create an interactive dashboard for the customer, where they could experiment with the data and get a concrete understanding of how everything works. This also provides a better insight into how our services function in practice.
