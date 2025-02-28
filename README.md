# Warehouse_Robot_Navigation
In a modern warehouse, autonomous robots are responsible for transporting packages from  designated pickup zones to drop‐off zones while navigating around fixed obstacles  (shelves).

- Simulates one or multiple robots moving within the warehouse.
- Prevents robots from going out of bounds or passing through shelves.
- Properly handles package pickup and delivery.
- Allows multiple robots and their commands to be entered in a single execution.

---

## 🔧 Installation  
Ensure you have Python **Python** installed.  

1️⃣ Clone this repository:  
```bash
git clone https://github.com/tuusuario/Mars-Rover-Solution.git
```
2️⃣ Run the program:  
```bash
python WarehouseRobot.py
```
---

### **Example Input**  
- Warehouse Grid: The grid extends from (0,0) to (7,7). 
- Shelves: There are 2 shelves at positions (3,3) and (3,4). 
- Pickup Zone: There is 1 pickup zone at (0,0). 
- Drop‐Off Zone: There is 1 drop‐off zone at (7,7). 
- Robots: There is 1 robot. 
    - The robot starts at (0,0) facing North. 
    - It receives the command string: PMMMMMMMRMMMMMMD 
-  Command Breakdown: 
    - P: Pick up a package (succeeds because the robot is in a pickup zone). 
    - MMMMMMM: Move north 7 times, reaching (0,7). 
    - R: Turn right (now facing East). 
    - MMMMMMM: Move east 7 times, reaching (7,7). 
    - D: Drop off the package (succeeds because the robot is at the drop‐off zone).

```plaintext
7 7 
2 
3 3 
3 4 
1 
0 0 
1 
7 7 
1 
0 0 N 
PMMMMMMMRMMMMMMMD 
```

### **Example Output**  
```plaintext
Posiciones finales de los robots:
7 7 E EMPTY
```
---

