print("Imagine this: You're on a phone call with your friend who's at a racetrack.")
print("He just saw a car zoom past and he quickly shouts, 'That car’s going 80 km/h!'")
print("Now pause for a second...")

a = input("Do you think there might be a time lag between what he saw and what you heard? [y/n]: ")

while True:
    if a.lower() == "y":
        print("You're right. There *is* a time lag — even if it's just a fraction of a second.")
        break
    else:
        print("Hmm... think again. We're dealing with real-world signals and reaction time.")
        a = input("So, would there be a time lag? [y/n]: ")

print("Now, What if i wanted to reduce the time lag and get an instantaneous answer? Well let us talk mathematically now.")
print("Lets turn that situation into an equation. As we know that v=s/t. (velocity=displacement/time) But this equation holds true only for a time interval. \n"
          "Say i wanted the instantaneous velocity instead of an averaged out one. For that we will use limits. That is: \n"
          "v= lim(Δt→0) Δs/Δt")
b=input("Woah! What is that? Let me explain. Here 'lim' means we are limiting the value and Δt-->0 (read as delta t tends to 0) means the limiting value of t used is 0. Did you get it? [y/n]: ")

if a=="y":
    print("Great! Let's move on.")

else:
    input("Please read the definations again so you understand it better. (or just go and ask dhwanit) [Press ENTER when you are ready!] ")

print ("Now that we have the concept of limits with us, what if we dont want to write lim(Δt→0) Δs/Δt everytime? Well we turn them into diffrential terms.\n"
           "How? Simple, instead of writing lim(Δt→0) Δs/Δt, we simply remove the lim part and write ds/dt.\n"
           "These are differential terms and would give us the answer by limiting the value of 't' to 0 (in this equation)")

a=input("So, we have the formula now v=ds/dt (for instantaneous velocity). Are you able to follow? (if you have any questions ask dhwanit) [y/n]: ")

if a=="y":
    print("Great! Let's move on.")

else:
    input("Please read the definations again so you understand it better. (or just go and ask dhwanit) [Press ENTER when you are ready!] ")