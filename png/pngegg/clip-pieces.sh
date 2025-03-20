#!/bin/sh
set -e

# Clip chess pieces out of the source image.

HGT=312
convert pngegg.png -crop 1200x$HGT+0+325 +repage black-row.png
convert black-row.png -crop 160x$HGT+35+0 +repage bk.png
convert black-row.png -crop 170x$HGT+225+0 +repage bq.png
convert black-row.png -crop 148x$HGT+432+0 +repage bb.png
convert black-row.png -crop 165x$HGT+617+0 +repage bn.png
convert black-row.png -crop 148x$HGT+821+0 +repage br.png
convert black-row.png -crop 148x$HGT+1016+0 +repage bp.png
rm -f black-row.png


convert pngegg.png -crop 1200x$HGT+0+10 +repage white-row.png
convert white-row.png -crop 160x$HGT+1002+0 +repage wk.png
convert white-row.png -crop 170x$HGT+802+0 +repage wq.png
convert white-row.png -crop 148x$HGT+618+0 +repage wb.png
convert white-row.png -crop 165x$HGT+415+0 +repage wn.png
convert white-row.png -crop 148x$HGT+228+0 +repage wr.png
convert white-row.png -crop 148x$HGT+34+0 +repage wp.png
rm -f white-row.png
