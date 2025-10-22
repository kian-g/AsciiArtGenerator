# ASCII Art Generator
Convert any image into colorful ASCII art right in your terminal!
This Python script uses the Pillow (PIL) library to process images and print a text-based representation using ANSI color codes.

## Requirements
- Python 3.8+
- Pillow (PIL)

Install: `pip install pillow`

## Example
Given an input image `image.png`, you’ll see ASCII art printed directly in your console, such as:
```
++++++++++++++++++++==+++
+++++++++****++++++++#$$#
+++++++*++=====+++*x#&X@&
++++***+=.. ...-+*x###$XX
++****+-.....--=+*xx##$X@
```

If we were to use this input image of an elephant and have it use 50 characters per line, this is the output:<br>
<img src="elephant.png" alt="elephant" width="250">
```
xxxxxxx#x##x+++*x**x#####################$$$$$$$$$
#########x=.=+==***+++++*****x##$$##$$$$$$$$$$$$$$
########x-.=+++=-=*x*+=-=+++++++*#$$$$$$$$$$$$$$$$
#######x--=+++++=.-**+==+*******=-+#$$$$$$$$$$$$$$
#######x--=++**x+==+=+=+=+*****++--=#$$$$$$$$$$$$$
#######=--=+*++*x+=-*===+****+*++=+x$$$$$$$$$$$$$$
######x----=++***+=-++=+++****++=++xx#$$$$$$$$$$$$
#x***+-.-----.- -==.+=+++*+x=++++***+++x$$$$$$$$&&
###xxx+.-=+++=++-   *-=+=+=*+++====++++=#&$$$&&&&&
###$$$+--=+*=.#$#=  .. .=+****+===-==+++#&$$&&&&&&
$####$+-=++*+*###$=..  =***xxx+=----=+++*&$&&&&&&&
$$$$$$=-=++*$$$$#$#-- -*****x+==-.-++*+=+&&&&&&&&&
$$$$$#=-=++x$$$$$$$x-.+***+====-..-=+*+=*&&&&&&&&&
$$$$$#-==++#$$$$$$$#..*xx*+. ------=++=+x&&&&&&&&&
$$$$$x-=++*$$$$$$$$*.=+**+-   ...--=+-++$&&&&&&&&&
$$$$$x.--=*$$$$$$$$--=+**++ ..      -=+*&$&&&&&&&&
$$$$$* .--x$$$$$$$#--=+*-+*-    -*x.-++#&$$$&&&&&&
$$$$$* .--x$$$$$$$*.-+++ .+*x...*$$+.=x$$$$$$$$$$$
#####x .--*$###$#$=.-++x= -=x$-.-*$*.=#$$$$$$$$$$$
######= --=#######=.-++x$-.-=x#-..x* =x$$$$$$$$$$$
####x##= .-=######- .==*##..-+#*  .-.=x$#######$#x
***++***+...-****-...==**+. -=++....-=+*++**+++*++
+++++++++++--+++. .---==*+==+++*+**++*+*****+**+++
*************++**+*******xx*xx****x***xx*********+
```

Or, of this rainbow to view how transparent pixels are taken care of:<br>
<img src="rainbow.png" alt="rainbow" width="250">
```
         ++*    -================-    *++ 
       ++   ====+**xxxxxxxxxxxx**+====   ++       
     ++  ===+*xxxxx*****++*****xxxxx*+===  ++     
    +  ==+*x#x*+++++++======+++++++*x#x*+==  +    
   + ==+*##*++++==--------------==++++*##*+== +   
  + ==*x#*+*+==--==+          +==--==+*+*#x*== +  
 + =+*#x=**=--=+     --------     +=--=**=x#*+= + 
+ =+x#x=*+--=+  .-++          ++-.  +=--+*=x#x+= +
 ==*#x=x+-==  -+                  +-  ==-+x=x#*== 
&=*x#=**.== =+                      += ==.**=#x*=&
==*#x=x--= =                          = =--x=x#*==
=+x#++x-==.-                          +.==-x++#x+=
```

## How it works
<ul>
  <li>Image Preprocessing
    <ul>
      <li>Converts any image to RGBA (adds alpha if missing).</li>
      <li>Optionally squashes height to correct the text’s aspect ratio.</li>
      <li>Resizes image width to fit within a given number of characters.</li>
    </ul>
  </li>

  <li>Brightness to ASCII Mapping
    <ul>
      <li>Each pixel’s brightness is mapped to one of 12 ASCII characters:</li>
      <li><code> .-=+*x#$&X@</code></li>
      <li>Darker pixels → “ ” (space), lighter pixels → “@”.</li>
    </ul>
  </li>
</ul>
