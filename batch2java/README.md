# Batch to Java
My AP Computer Science teacher did work for Google, Xilinx, and I believe Intel, so she was nothing short of brilliant at programming. Unfortunately, this made her very good at pushing several of the students in the class who had prior experience or were picking up things much more quickly than the rest of the class. And well, I guess we're lazy. One of my friends in the class was rather unfond of her and wanted to send her some form of malware. His prior programming experience was Windows batch scripting, so he wanted to see if there was a way to run his small script that just constantly opens command prompt windows until RAM runs out.

## Task
Create a Java file that runs malicious batch script. This file will then be turned in via [dropittome](https://dropitto.me/) as is expected for all class assignments. Class assignments are run in batch, with stdout (or whatever it's called in Java) being the initial criterion for grading. The malicious file would then run alongside assignments and theoretically crash the PC.

The Java program would generate the batch script and run it. This was Windows-specific, but since all of the computers used by the school district ran Windows it was not a concern. However, I was concerned I may be caught. So I then took the code and added another layer, creating a Java program that generates a Java wrapper for any batch script. If I was caught, I could say that all I did was give a tool to my friend that he requested, and that I had no part in creating the malicious program that he made. This program was what was given to my friend, who actually never used it due to a misunderstanding or chickening out or waning of interest or whatever reason it was.

## Learning Outcomes
- Writing files with Java
- Executing Windows commands with Java

## Code Considerations
- There's no reason to want to run batch scripts with Java. Stop it.
- There are far better ways of writing malicious Java than using a batch script.
- Don't prank your teacher. That's dumb.
