## magicswitchd

> `/usr/libexec/magicswitchd`

```diff

 40.0.0.0.0
-  __TEXT.__text: 0xb6b4
-  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__text: 0xc124
+  __TEXT.__auth_stubs: 0x580
   __TEXT.__objc_stubs: 0x1560
   __TEXT.__objc_methlist: 0x13c0
   __TEXT.__const: 0x80

   __TEXT.__oslogstring: 0x1f5e
   __TEXT.__objc_classname: 0x2f1
   __TEXT.__objc_methtype: 0x9dc
-  __TEXT.__gcc_except_tab: 0x154
-  __TEXT.__unwind_info: 0x378
-  __DATA_CONST.__auth_got: 0x300
+  __TEXT.__gcc_except_tab: 0x14c
+  __TEXT.__unwind_info: 0x478
+  __DATA_CONST.__auth_got: 0x2d0
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__const: 0x2a8
   __DATA_CONST.__cfstring: 0x300

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 466DAD61-768C-333F-97CF-00A348BD07B9
+  UUID: 7C022758-EB12-3AD9-9AA0-524310EEC4B9
   Functions: 351
-  Symbols:   153
+  Symbols:   147
   CStrings:  878
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
Functions:
~ sub_100000ee8 : 112 -> 116
~ sub_100000f58 -> sub_100000f5c : 360 -> 368
~ sub_100001334 -> sub_100001340 : 648 -> 652
~ sub_1000015bc -> sub_1000015cc : 372 -> 368
~ sub_100001888 -> sub_100001894 : 632 -> 644
~ sub_100001b00 -> sub_100001b18 : 656 -> 664
~ sub_100001de0 -> sub_100001e00 : 12 -> 64
~ sub_100001e14 -> sub_100001e68 : 12 -> 64
~ sub_1000020c4 -> sub_10000214c : 320 -> 324
~ sub_10000228c -> sub_100002318 : 136 -> 144
~ sub_100002448 -> sub_1000024dc : 484 -> 492
~ sub_100002740 -> sub_1000027dc : 444 -> 460
~ sub_100002a80 -> sub_100002b2c : 12 -> 64
~ sub_100002adc -> sub_100002bbc : 12 -> 64
~ sub_100002af0 -> sub_100002c04 : 12 -> 64
~ sub_100002b04 -> sub_100002c4c : 12 -> 64
~ sub_100002b74 -> sub_100002cf0 : 444 -> 448
~ sub_100002d30 -> sub_100002eb0 : 420 -> 424
~ sub_100002ed4 -> sub_100003058 : 192 -> 196
~ sub_100002f94 -> sub_10000311c : 236 -> 244
~ sub_1000030fc -> sub_10000328c : 520 -> 544
~ sub_100003304 -> sub_1000034ac : 272 -> 284
~ sub_100003414 -> sub_1000035c8 : 260 -> 264
~ sub_100003518 -> sub_1000036d0 : 1556 -> 1604
~ sub_100003cf0 -> sub_100003ed8 : 700 -> 708
~ sub_100003fac -> sub_10000419c : 248 -> 256
~ sub_1000041e4 -> sub_1000043dc : 168 -> 176
~ sub_100004310 -> sub_100004510 : 20 -> 80
~ sub_100004334 -> sub_100004570 : 20 -> 80
~ sub_100004378 -> sub_1000045f0 : 20 -> 80
~ sub_10000465c -> sub_100004910 : 468 -> 456
~ sub_100004830 -> sub_100004ad8 : 452 -> 464
~ sub_100004a44 -> sub_100004cf8 : 484 -> 492
~ sub_100004efc -> sub_1000051b8 : 12 -> 64
~ sub_100004f10 -> sub_100005200 : 12 -> 64
~ sub_100004f24 -> sub_100005248 : 12 -> 64
~ sub_100004f38 -> sub_100005290 : 12 -> 64
~ sub_100004f4c -> sub_1000052d8 : 12 -> 64
~ sub_100004f60 -> sub_100005320 : 12 -> 64
~ sub_100004fe8 -> sub_1000053dc : 616 -> 636
~ sub_100005250 -> sub_100005658 : 224 -> 228
~ sub_100005330 -> sub_10000573c : 208 -> 216
~ sub_100005400 -> sub_100005814 : 180 -> 188
~ sub_1000054bc -> sub_1000058d8 : 144 -> 152
~ sub_1000056d4 -> sub_100005af8 : 256 -> 264
~ sub_100005a78 -> sub_100005ea4 : 588 -> 608
~ sub_100005cc4 -> sub_100006104 : 396 -> 404
~ sub_100005e50 -> sub_100006298 : 452 -> 472
~ sub_10000613c -> sub_100006598 : 244 -> 248
~ sub_100006230 -> sub_100006690 : 240 -> 248
~ sub_100006368 -> sub_1000067d0 : 12 -> 64
~ sub_10000637c -> sub_100006818 : 12 -> 64
~ sub_100006390 -> sub_100006860 : 12 -> 64
~ sub_1000063a4 -> sub_1000068a8 : 12 -> 64
~ sub_10000640c -> sub_100006944 : 996 -> 1012
~ sub_100006950 -> sub_100006e98 : 160 -> 176
~ sub_100006d28 -> sub_100007280 : 940 -> 944
~ sub_100007240 -> sub_10000779c : 336 -> 340
~ sub_1000073d8 -> sub_100007938 : 536 -> 552
~ sub_1000078e4 -> sub_100007e54 : 12 -> 64
~ sub_100007908 -> sub_100007eac : 12 -> 64
~ sub_10000792c -> sub_100007f04 : 12 -> 64
~ sub_1000079b8 -> sub_100007fc4 : 180 -> 176
~ sub_100007b28 -> sub_100008130 : 316 -> 320
~ sub_100007d0c -> sub_100008318 : 12 -> 64
~ sub_100007d50 -> sub_100008390 : 12 -> 64
~ sub_100007e34 -> sub_1000084a8 : 328 -> 336
~ sub_1000083b4 -> sub_100008a30 : 204 -> 208
~ sub_10000851c -> sub_100008b9c : 136 -> 144
~ sub_1000085a4 -> sub_100008c2c : 136 -> 144
~ sub_100008938 -> sub_100008fc8 : 272 -> 268
~ sub_100008a48 -> sub_1000090d4 : 484 -> 480
~ sub_100008c3c -> sub_1000092c4 : 12 -> 64
~ sub_100008c48 -> sub_100009304 : 12 -> 64
~ sub_100008c5c -> sub_10000934c : 12 -> 64
~ sub_100008cb8 -> sub_1000093dc : 12 -> 64
~ sub_100008d28 -> sub_100009480 : 452 -> 460
~ sub_1000090bc -> sub_10000981c : 108 -> 112
~ sub_10000919c -> sub_100009900 : 12 -> 64
~ sub_10000921c -> sub_1000099b4 : 268 -> 276
~ sub_100009328 -> sub_100009ac8 : 380 -> 396
~ sub_1000094ac -> sub_100009c5c : 352 -> 360
~ sub_10000960c -> sub_100009dc4 : 12 -> 60
~ sub_100009698 -> sub_100009e80 : 12 -> 64
~ sub_1000096b0 -> sub_100009ecc : 436 -> 444
~ sub_100009a5c -> sub_10000a280 : 672 -> 684
~ sub_100009cfc -> sub_10000a52c : 540 -> 544
~ sub_10000a78c -> sub_10000afc0 : 248 -> 252
~ sub_10000a9cc -> sub_10000b204 : 12 -> 64
~ sub_10000a9e0 -> sub_10000b24c : 12 -> 64
~ sub_10000a9f4 -> sub_10000b294 : 12 -> 64
~ sub_10000aa08 -> sub_10000b2dc : 12 -> 64
~ sub_10000aa94 -> sub_10000b39c : 536 -> 540
~ sub_10000acac -> sub_10000b5b8 : 304 -> 296
~ sub_10000af5c -> sub_10000b860 : 668 -> 692
~ sub_10000b220 -> sub_10000bb3c : 576 -> 572
~ sub_10000b460 -> sub_10000bd78 : 484 -> 480
~ sub_10000b6d8 -> sub_10000bfec : 12 -> 64
~ sub_10000b6fc -> sub_10000c044 : 12 -> 64
~ sub_10000b710 -> sub_10000c08c : 12 -> 64
~ sub_10000b7a4 -> sub_10000c154 : 160 -> 156
~ sub_10000bb28 -> sub_10000c4d4 : 156 -> 164
~ sub_10000bbf4 -> sub_10000c5a8 : 596 -> 608
~ sub_10000bf9c -> sub_10000c95c : 488 -> 496
~ sub_10000c2a8 -> sub_10000cc70 : 240 -> 252
~ sub_10000c49c -> sub_10000ce70 : 12 -> 64
~ sub_10000c4a8 -> sub_10000ceb0 : 12 -> 64
~ sub_10000c504 -> sub_10000cf40 : 12 -> 64
CStrings:
+ "B8365B0F-332F-481C-B7DE-7E80973B07BF"
+ "MagicSwitchEnabler --- Launching; \"MagicSwitch-40\" \"7383\""
- "B8365B0F-C979-491B-86E3-EBAE195F1755"
- "MagicSwitchEnabler --- Launching; \"MagicSwitch-40\" \"7059\""

```
