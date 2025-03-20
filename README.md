# piece-packager

`piece-packager` is a collection of over 80 chess piece sets in SVG format.
If color-variants are included, the total exceeds 280 sets.

The chess piece sets can be [viewed online](./viewer.html).

Pre-packaged chess-piece sets can be found in the `out` directory.

`piece-packager` combines individual SVG and/or PNG files into a single SVG
file. The drawing data for each file can be retrieved from the generated SVG
using a two-letter SVG id. (e.g. `bp` for black pawn) See the
[Building](#building) section below for more details.

The chess piece sets have been copied from various places on the web. I am not
the author of any of the sets. I believe all sets are allowed to be used
for non-commercial purposes, but check their license if you have questions.

#### PNG sets

Each chess piece is a PNG image whose image data has been embedded in the
generated SVG.

* [standard](https://commons.wikimedia.org/wiki/Category:PNG_chess_pieces/Standard_transparent)
* [pngegg](https://www.pngegg.com/en/png-ynnvf)


#### SVG sets

Each chess piece is SVG data that has been included in the generated SVG file.
Some sets (e.g. qootee) contain embedded raster data.

* adventurer [font](http://www.enpassant.dk/chess/downl/adventur.zip)
  [by Armando H. Marroquin]
* [alfarishy](https://dribbble.com/shots/5261883-Chess-Icons-in-filled-line-style)
  [by Jordan Alfarishy]
* alfonso-x [font](http://www.enpassant.dk/chess/downl/alfonso.zip)
  [by Armando H. Marroquin]
* [alpha](http://www.enpassant.dk/chess/fontimg/alpha.htm)
  [by Eric Bentzen]
* [anarchy](https://github.com/lichess-org/lichobile/pull/210)
  [by caderek]
* [ansuz](https://github.com/quotepilgrim/ansuz)
  [by quotepilgrim]
* [bagnall](https://github.com/douglasbagnall/p4wn/tree/master/src/images)
  [by Douglas Bagnall]
* berlin [font](http://www.enpassant.dk/chess/downl/berlin.zip)
  [by Eric Bentzen]
* [caliente](https://github.com/avi-0/caliente/tree/master/caliente)
  [by Lena avi-0]
* [california](https://sites.google.com/view/jerrychess/home)
  [by Jerry S.]
* [cardinal](https://github.com/lichess-org/lila/issues/5534#issuecomment-540562460)
  [by sadsnake1]
* cases [font](http://www.enpassant.dk/chess/downl/cases.zip)
  [by Matthieu Leschemelle]
* [cburnett](https://en.wikipedia.org/wiki/User:Cburnett/GFDL_images/Chess)
  [by Colin Burnett]
* [celtic](https://github.com/maurimo/chess-art/tree/main/celtic)
  [by Maurizio Monge]
* checkers
* [chess7](https://luc.devroye.org/fonts-49518.html)
  [by Alexander Sizenko]
* [chessnut](https://github.com/LexLuengas/chessnut-pieces)
  [by Alexis Luengas]
* [chicago](https://github.com/benjfriedrich/chess-foundry-pack/tree/master/Chicago)
  [by Benjamin Friedrich]
* companion [font](https://www.enpassant.dk/chess/fontimg/gc.htm)
  [by David L. Brown]
* condal [font](http://www.enpassant.dk/chess/downl/condal.zip)
  [by Armando H. Marroquin]
* [cooke](https://github.com/lichess-org/lila/issues/15440)
  [by fefjar]
* disguised
* dmuysi [k](https://thenounproject.com/icon/king-4744565/)
  [q](https://thenounproject.com/icon/queen-4744562/)
  [b](https://thenounproject.com/icon/queen-4744562/)
  [n](https://thenounproject.com/icon/knight-4744560/)
  [r](https://thenounproject.com/icon/rook-4744575/)
  [p](https://thenounproject.com/icon/pawn-4744580/)
  [by Zach Bogart]
* [dubrovny](https://github.com/lichess-org/lila/issues/5705)
  [by sadsnake1]
* [echiquier](https://userstyles.org/styles/272094/chess-set-echiquier)
  [by Bryan]
* [fantasy](https://github.com/maurimo/chess-art/tree/main/fantasy)
  [by Maurizio Monge]
* [fresca](https://github.com/Deltaspace0/monomer-widgets/commit/937e137bc78520be6ad065c9faef31e9b1bd7cd8)
  [by sadsnake1]
* [gioco](https://github.com/lichess-org/lila/issues/5534#issuecomment-533173385)
  [by sadsnake1]
* [governor](https://github.com/lichess-org/lila/issues/6556)
  [by sadsnake1]
* [green](https://greenchess.net/info.php?item=downloads)
  [by Green Chess]
* harlequin [font](http://www.enpassant.dk/chess/downl/harlequi.zip)
  [by Armando H. Marroquin]
* [horsey](https://lichess.org/team/cham)
  [svg](https://github.com/marcobuontempo/tonnetto/tree/main/gui/chess-pieces/horsey)
  [by cham]
* [icon54](https://thenounproject.com/icon/chess-board-535267/)
  [by icon 54]
* icpieces [by sadsnake1]
* kingdom [font](http://www.enpassant.dk/chess/downl/kingdom.zip)
  [by Armando H. Marroquin]
* [kiwen-suwi](https://github.com/neverRare/kiwen-suwi)
  [by neverRare]
* [kosal](https://github.com/philatype/kosal/)
  [by Philatype]
* leipzig [font](http://www.enpassant.dk/chess/downl/leipzig.zip)
  [by Armando H. Marroquin]
* letter
* letters
* [libra](https://github.com/lichess-org/lila/issues/5707#issuecomment-562879751)
  [by sadsnake1]
* [libra_v0](https://github.com/lichess-org/lila/issues/5707#issuecomment-561782349)
  [by sadsnake1]
* line [font](http://www.enpassant.dk/chess/downl/chesline.zip)
  [by Armando H. Marroquin]
* lucena [font](http://www.enpassant.dk/chess/downl/lucena.zip)
  [by Armando H. Marroquin]
* [maestro](https://github.com/lichess-org/lila/issues/15365)
  [by sadsnake1]
* [maestro_v6](https://github.com/lichess-org/lila/issues/5488)
  [by sadsnake1]
* magnetic [font](http://www.enpassant.dk/chess/downl/magnetic.zip)
  [by Armando H. Marroquin]
* mark [font](http://www.enpassant.dk/chess/downl/chesmark.zip)
  [by Armando H. Marroquin]
* marroquin [font](http://www.enpassant.dk/chess/downl/marroqui.zip)
  [by Armando H. Marroquin]
* maya [font](http://www.enpassant.dk/chess/downl/chesmaya.zip)
  [by Armando H. Marroquin]
* mediaeval [font](http://www.enpassant.dk/chess/downl/medie_tt.zip)
  [by Armando H. Marroquin]
* [merida](https://codeberg.org/FelixKling/chess_pieces/src/branch/main/Merida_shaded)
  [by Armando H. Marroquin]
* millennia [font](http://www.enpassant.dk/chess/downl/millenia.zip)
  [by Armando H. Marroquin]
* [monarchy](https://github.com/lichess-org/lila/issues/15506)
  [by slither77]
* mono [by Thibault Duplessis and Colin M.L. Burnett]
* motif [font](http://www.enpassant.dk/chess/downl/motif.zip)
  [by Armando H. Marroquin]
* [mpchess](https://github.com/chupinmaxime/mpchess-pieces)
  [by Maxime Chupin]
* [oldstyle](https://www.reddit.com/r/sharechess/comments/voidfg/sharechess_new_piece_set_oldstyle_by_monika_berger/) [font](https://www.reddit.com/r/sharechess/comments/voidfg/sharechess_new_piece_set_oldstyle_by_monika_berger/) [by Monika Berger]
* [oslo](https://github.com/benjfriedrich/chess-foundry-pack/tree/master/Oslo)
  [by Benjamin Friedrich]
* [pirat](http://www.enpassant.dk/chess/fontimg/pirat.htm)
  [font](http://www.enpassant.dk/chess/downl/pirat.zip)
  [by Klaus Wolf]
* pirouetti [by pirouetti]
* [pixel](https://opengameart.org/content/pixel-chess-pieces)
  [by Lucas312]
* [qootee](https://www.reddit.com/r/chess/comments/wbfeks/my_new_chess_set_is_available/)
  [by TangentialElephant]
* [regular](https://www.enpassant.dk/chess/fontimg/usual.htm)
  [Alastair Scott] 
* [reillycraig](https://www.chess.com/forum/view/suggestions/new-chess-set-design)
  [by Reilly Craig]
* [rhosgfx](https://rhosgfx.itch.io/vector-chess-pieces)
  [by rhosgfx]
* riohacha 
* saakyan [k](https://thenounproject.com/icon/king-316314/)
  [q](https://thenounproject.com/icon/queen-316317/)
  [b](https://thenounproject.com/icon/bishop-316316/)
  [n](https://thenounproject.com/icon/knight-316315/)
  [r](https://thenounproject.com/icon/rook-316318/)
  [p](https://thenounproject.com/icon/pawn-316319/)
  [by Sergey Saakyan]
* [shapes](https://github.com/flugsio/chess_shapes)
  [by Jimmie Elvenmark]
* smart [font](https://www.enpassant.dk/chess/fontimg/smart.htm)
  [by Christoph Wirth]
* [spatial](https://github.com/maurimo/chess-art/tree/main/spatial)
  [by Maurizio Mongo]
* [staunty](https://github.com/lichess-org/lila/issues/5647)
  [by sadsnake1]
* [symmetric](https://github.com/lichess-org/lichobile/issues/215)
  [by Arcticpenguins]
* tagged 
* [tatiana](https://github.com/lichess-org/lila/issues/5534)
  [by sadsnake1]
* tfb [font](https://font.download/font/chess-tfb)
  [by kaiserzharkhan]
* [traveller](https://www.chessvariants.com/index/zipfile.php?itemid=FontTravel)
  [by Alan Cowderoy]
* [trendy](https://thenounproject.com/browse/collection-icon/trendy-chess-161956/)
  [by Benjamin Kinard]
* utrect [font](ftp://ftp.pitt.edu/group/student-activities/chess/DTP/utrecht.zip)
  [by Hans Bodlaender]
* vecon [k](https://thenounproject.com/icon/chess-2741972/)
  [q](https://thenounproject.com/icon/chess-2741970/)
  [b](https://thenounproject.com/icon/chess-2741971/)
  [n](https://thenounproject.com/icon/chess-2741973/)
  [r](https://thenounproject.com/icon/chess-2741969/)
  [p](https://thenounproject.com/icon/chess-2741968/)
  [by vecon]
* wisdom [font](https://www.dafont.com/wisdom-chess.font)
  [by Vladimir Nikolic]
* [xkcd](https://www.reddit.com/r/chess/comments/1j7gr3g/the_xkcd_piece_set_is_now_available_on_lichess/)
  [by detroyejr]



### Building
To build all chess-sets in the `svg` and `png` directories:
```
    ./build.sh
```

To build an individual chess-set, supply its directory:
```
    ./build.sh ./svg/staunty
```

Generated files are created in the `out` directory.

The intended purpose of `piece-packager` is to combine individual files, each
of which contains a single chess piece, into a single SVG file, but it need not
be limited to chess pieces. A maximum of twelve images can be combined. If more
than twelve images need to be combined, `piece-packager` will need to be
modified.

When combining a PNG file, the PNG data is simply embedded in the SVG file. The
embedded data, can be retrieved and manipulated as if it were an SVG image.
 
`piece-packager` is not smart enough to handle *every* SVG file, but handling
'simple' SVG files should not be a problem.

To build your own chess-set package, place all files in a directory and then
supply the directory path to `./build.sh`. e.g. `./build.sh ./path/to/set`.
The directory will be processed as follows:
* Subdirectories are ignored.
* Only SVG and PNG files are examined; all other file types are ignored.
* SVG files are processed before PNG files.
* The first file found for each piece is used; any subsequent matching piece
  files are ignored.
* When generating a two-letter id, the case of the filename is ignored,
  however, the case of the filename affects its retrieval-order.
* One-letter filenames (excluding the extension) are ignored.
* The generated SVG file will be placed in the `out` directory.


`piece-packager` does not enforce any naming conventions. It searches the
beginning and ending of each filename for anything that matches a 'color' or a
'piece-type'. The color can be `white`, `black`, `w`, `b`. The piece-type can be
`bishop`, `king`, `knight`, `pawn`, `queen`, `rook`, `b`, `k`, `n`, `p`, `q`,
`r`. (Note that `b` matches both `bishop` and `black`.) Any matches it finds
are used to generate a two-letter piece-id (e.g. `wk`). If a two-letter
piece-id cannot be created, the file is ignored. Each chess piece in the
generated SVG file is assigned its corresponding two-letter piece-id. 


Examples:
* If `Black_Knight.svg` and `bn.svg` exist (both are presumed to contain the
  piece for the black knight), `Black_Knight.svg` will be used because
  `Black_Knight` sorts before `bn`.
* If `wp.png` and `wp.svg` exist (both are presumed to contain the piece for
  the white pawn), the `wp.svg` will be chosen because SVG files have priority
  over PNG files.
* If `wk.svg` and `kw.svg` exist (both are presumed to contain the piece for
  the white king), the `kw.svg` will be chosen because `kw` sorts before `wk`.
* The filename `black.svg` will generate the two-leter id `bk` (black king)
  because of the `black` at the beginning and the `k` and the end.
* The filename `blackn.svg` will generate the two-letter id `bn` (black knight)
  because of the `black` at the beginning and the `n` and the end.
* The filename `kapow.svg` will generate the two-letter id `wk` (white king)
  because of the `k` at the beginning and the `w` and the end.


Assuming a file exists for each chess piece type, the generated SVG file will
contain the following twelve SVG ids which may be used to retrieve their
corresponding piece data:
* `bb` Black bishop
* `bk` Black king
* `bn` Black knight
* `bp` Black pawn
* `bq` Black queen
* `br` Black rook
* `wb` White bishop
* `wk` White king
* `wn` White knight
* `wp` White pawn
* `wq` White queen
* `wr` White rook

If a file does not exist for a chess piece type, its corresponding SVG id will
not exist in the generated SVG file.


### Misc

The chess piece sets were collected from various places such as
[lichess-org](https://github.com/lichess-org/lila/tree/master/public/piece),
[supertorpe](https://github.com/supertorpe/chessendgametraining/tree/master/code/public/assets/pieces)
and
[sharechess](https://github.com/sharechess/sharechess.github.io/tree/main/pieces).

supertorpe has a [half-black/half-white king](https://github.com/supertorpe/chessendgametraining/blob/master/code/public/assets/pieces/cburnett/wbK.svg)
as well as a 'full' black and white king.

The [alfarie site](https://www.chessvariants.com/graphics.dir/alfaerieSVG/index.html)
has over 170 chess piece variants.

http://mirrors.mit.edu/CTAN/macros/latex/contrib/chessfss/chessfonts_gallery.pdf

https://github.com/lichess-org/lila/blob/master/COPYING.md

https://www.chessvariants.com/d.font/

https://ajedreztipografia.wordpress.com/

https://www.enpassant.dk/chess/fonteng.htm

https://www.chessdiagrammer.com/download/zip/chessfonts_samples.pdf
