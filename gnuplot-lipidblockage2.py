set term postscript color enhanced
set term postscript size 16cm, 10cm
set tics out
set ytics 2
set mytics 2
set xtics nomirror
set ytics nomirror
set xtics 200
set mxtics 2
set xlabel "Time (ns)"
set ylabel "xy-radius (A)"
set output "gnuplot-lipidblockage2.ps"
set yrange [8:0] reverse
unset key
set style line 1 pointtype 7 pointsize 0.3 lc rgb "#eb5d4d"  #waters OW red
set style line 2 pointtype 7 pointsize 0.3 lc rgb "#b1bab1"  #popc gray
set style line 3 pointtype 7 pointsize 0.3 lc rgb "#9a00db"  #Kions purple
plot for [col=3:100] "xxx3.xvg" u ($1*0.001):col w p ls 2, \
