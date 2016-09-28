#Week 2

###Active Shooter Exercise
- Do's
  - Call 911 (don't assume that someone else is calling) and inform the security. Be persistent; Lines may be jammed. Call only if the shooter isn't in front of you. In that call, camly and quickly the authorities where you are and what is happening.
  - Have an escape route in place if the shooting seems to be coming from a distant place. 
- Don't
  - Go out to see where the shots are being fired.  
  - Panic and make noise.

###ZeroR Classifier

The following is the modified lines in ninja.rc
```
# zeror() {
#         local learner=weka.classifiers.rules.ZeroR
# 	$Weka $learner -p 0 -t $1 -T $2
# }
zeror() {
    python -B $Here/zeror.py $1 $2
}
eg11() {
    local data="data/jedit-4.1.arff"         # edit this line to change the data
    local learners="j48 jrip nb rbfnet bnet zeror" # edit this line to change the leaners
    local goal=true                          # edit this line to hunt for another goal
    
    local i="$Tmp/eg11"
    if [ -f "$i.pd" ]; then
       report pd "$i"
       report pf "$i"
    else
        crossval 5 5 "$data" $Seed $learners | grep $goal >"$i"
        gawk  '{print $2,$10}' "$i" > "$i.pd"
        gawk  '{print $2,$11}' "$i" > "$i.pf"
        eg11
   fi
}
```
The output of eg11() running in ninja is:
```
pd

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 ,        zeror ,       0  ,     0 (*              |              ), 0.00,  0.00,  0.00,  0.00,  0.00
   2 ,           nb ,      45  ,    18 (        ---   *| --           ),25.00, 36.00, 45.00, 53.00, 60.00
   2 ,       rbfnet ,      47  ,    20 (        ------ *   ---        ),25.00, 43.00, 47.00, 60.00, 67.00
   3 ,         bnet ,      60  ,    17 (             --|-- *  -       ),40.00, 55.00, 60.00, 67.00, 71.00
   3 ,         jrip ,      60  ,    23 (          -----|   *   ---    ),33.00, 50.00, 60.00, 71.00, 80.00
   4 ,          j48 ,      72  ,    16 (               |-----  *  --  ),50.00, 65.00, 72.00, 81.00, 87.00
pf

rank ,         name ,    med   ,  iqr
----------------------------------------------------
   1 ,        zeror ,       0  ,     0 (*              |              ), 0.00,  0.00,  0.00,  0.00,  0.00
   2 ,          j48 ,       7  ,     6 (     --   *  --|---           ), 4.00,  5.00,  7.00,  9.00, 13.00
   2 ,           nb ,       7  ,     6 (     --   *   -|-             ), 4.00,  5.00,  7.00, 10.00, 12.00
   2 ,         jrip ,       9  ,    10 (  ---        * |------        ), 2.00,  4.00,  9.00, 11.00, 15.00
   2 ,       rbfnet ,       9  ,     5 (     -----   * |----          ), 4.00,  7.00,  9.00, 11.00, 14.00
   2 ,         bnet ,      11  ,     6 (        -----  |*   ------    ), 6.00,  9.00, 11.00, 14.00, 18.00
```

###Table Reader

The output of the results of reading weather.csv
```
outlook        Mode            sunny     Entropy:              1.577406
?temperature-  Mean        73.571429     Standard Deviation:   6.571667
<humidity      Mean        81.642857     Standard Deviation:  10.285218
windy          Mode            FALSE     Entropy:              0.985228
=play          Mean         1.071429     Standard Deviation:   0.997249
```