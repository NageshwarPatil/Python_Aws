#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import pyttsx3
import subprocess
while True:
    print ('hey I am here to Help you  From Amazon web Services......Please Give me a Instruction')

    pyttsx3.speak('hey I am here to Help you ,From Amazon web Services.......Please Give me a Instruction'
                  )

    user_instruction = input()
    pyttsx3.speak('Your Request is under Process Please be patience')

    if((('launch' in user_instruction) or ('run' in user_instruction) or ('give' in user_instruction)) and (('os' in user_instruction) or ('instance' in user_instruction) or ('operating system' in user_instruction)) and ('aws' in user_instruction)):
        print()
        print('Please Be Patience we are launching an Redhat version 8  operating system for Developer')
        print()
        print ('For Development Environment we are launching a ,AWS platform which include, Created a New Key Pairs ,And Security Group Which enables port number 80 for HTTP ,port number 22 for ssh')
        pyttsx3.speak('For Development Environment we are launching a ,AWS platform which include, Created a New Key Pairs ,And Security Group Which enables port number 80 for Http ,port number 22 for ssh')
	
                      
        subprocess.getoutput('terraform apply --auto-approve')
	
        print()
        
        
                      
        print ('For Developer An Instance has been Launched Successfully')
        pyttsx3.speak('For Developer An Instance has been Launched Successfully')	
                      
    elif((('stop' in user_instruction) or ('hold' in user_instruction) or ('terminate') in user_instruction) and (('instance' in user_instruction) or ('os') in user_instruction) and ('aws') in user_instruction):
        print('An aws Instance is Terminated Now, Thank You For using')
        pyttsx3.speak('An aws Instance is Terminated Now, Thank You For using')
        subprocess.getoutput('terraform destroy --auto-approve')
