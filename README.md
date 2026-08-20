# 9siliconcs3

## Project Links
* [Click here to view my main code file](README.md)
* [Click here to view the Live Website](https://github.io)

Annex A
Computational Thinking Exercise: "Smart School Canteen Queue"

Section: 9 - Silicon                        Score:_________

C# / Name: Jeb Francis M. Climaco            Date: 08/18/26


Scenario

The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:

Some students take too long to decide what to order.
The cashier has to manually calculate totals and give change.
There is no system to track which food items are running out.
Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

Step 1: Identify the Big Problem

Main Problem: The PSHS school canteen suffers from severe overcrowding and long lunch break queues due to slow ordering, manual cash processing, and lack of real-time inventory tracking.


Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

1. Ordering Delay: Students take a long time to view the menu and decide what food to buy while already standing at the counter.

2. Manual Checkout Bottleneck: The cashier spends excessive time manually calculating total order costs and physical cash change.

3. Inventory Tracking: The canteen staff lack a system to monitor stock levels, leading to stockouts of popular items during peak service.

4. Queue Disorganization: Physical lines become chaotic without a digital call system or pickup queue.

Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

Sub-Problem
1.) Ordering Delay
2.)Manual Checkout Bottleneck
3.)Inventory Tracking
4.)Queue Disorganization

CT Skill
1.)Decomposition
2.)Abstraction
3.)Pattern Recognition
4.)Algorithm Design

Example Solution
1.)Install a pre-order mobile app or digital menu boards in the line so students choose their meals before reaching the counter.
2.)Implement a simple POS touchscreen system that automatically calculates the total bill and change when items are selected.
3.)Use a digital barcode scanner system that automatically deducts sold items from stock and sends low-inventory alerts to staff.
4.)Create an automated order-token system (like a digital board displaying ticket numbers) to split the ordering and pickup stations.



 Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem

START
    DISPLAY digital_menu
    
    REPEAT
        INPUT selected_items
        SET items_available = TRUE
        
        FOR EACH item IN selected_items DO
            IF item.stock == 0 THEN
                DISPLAY item.name + " is currently out of stock."
                SET items_available = FALSE
            ENDIF
        ENDFOR
        
    UNTIL items_available == TRUE
    
    CREATE pre_order_cart WITH selected_items
    SET order_token = GENERATE_UNIQUE_ID()
    
    DISPLAY "Pre-order confirmed!"
    DISPLAY "Your Order Token: " + order_token
    DISPLAY "Show this token to the cashier to pay."



