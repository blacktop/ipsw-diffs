## libncurses.5.4.dylib

> `/usr/lib/libncurses.5.4.dylib`

```diff

-79.0.0.0.0
-  __TEXT.__text: 0x2fd38
-  __TEXT.__auth_stubs: 0x5d0
+81.0.0.0.0
+  __TEXT.__text: 0x30380
   __TEXT.__const: 0x72e4
-  __TEXT.__cstring: 0x3bf9
-  __TEXT.__unwind_info: 0x770
-  __DATA_CONST.__got: 0x28
+  __TEXT.__cstring: 0x3c60
+  __TEXT.__unwind_info: 0x778
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x2f10
-  __AUTH_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__auth_got: 0x2e8
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_data: 0x4
-  __DATA.__data: 0x300
-  __DATA.__bss: 0x20b
-  __DATA.__common: 0x3d4
-  __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__common: 0x1f8
+  __DATA.__data: 0x10
+  __DATA.__bss: 0x203
+  __DATA.__common: 0x2c4
+  __DATA_DIRTY.__data: 0x308
+  __DATA_DIRTY.__bss: 0x8
+  __DATA_DIRTY.__common: 0x308
   - /usr/lib/libSystem.B.dylib
-  UUID: 4E74E9AB-D4BD-3C6F-8E59-034AA6EC36E2
+  UUID: 3211B715-9426-38B9-A2FC-F7ECEECF3793
   Functions: 1014
   Symbols:   1042
-  CStrings:  1677
+  CStrings:  1681
 
Functions:
~ __nc_wrap_entry : 816 -> 856
~ __nc_merge_entry : 284 -> 316
~ __nc_align_termtype : 620 -> 616
~ sub_2a3b268d4 -> sub_2be522968 : 260 -> 264
~ sub_2a3b269d8 -> sub_2be522a70 : 712 -> 840
~ sub_2a3b26de8 -> sub_2be522f00 : 144 -> 148
~ sub_2a3b27020 -> sub_2be52313c : 676 -> 688
~ sub_2a3b27a20 -> sub_2be523b48 : 156 -> 160
~ sub_2a3b288d0 -> sub_2be5249fc : 316 -> 320
~ sub_2a3b28ca8 -> sub_2be524dd8 : 164 -> 172
~ __nc_tic_expand : 1148 -> 1216
~ __nc_resolve_uses2 : 1652 -> 1660
~ sub_2a3b2a7ac -> sub_2be526930 : 116 -> 120
~ __nc_get_token : 2532 -> 2544
~ sub_2a3b2b260 -> sub_2be5273f4 : 788 -> 816
~ sub_2a3b2b5a8 -> sub_2be527758 : 168 -> 188
~ __nc_trans_string : 1148 -> 1160
~ __nc_first_db : 940 -> 952
~ __nc_scroll_optimize : 448 -> 544
~ __nc_hash_map : 1208 -> 1288
~ sub_2a3b2cb54 -> sub_2be528de0 : 624 -> 640
~ __nc_scroll_oldhash : 352 -> 360
~ __nc_init_keytry : 256 -> 260
~ __nc_init_acs : 652 -> 680
~ sub_2a3b2dd04 -> sub_2be529fc8 : 1300 -> 1308
~ sub_2a3b2e218 -> sub_2be52a4e4 : 132 -> 136
~ _waddch : 160 -> 156
~ _wechochar : 176 -> 172
~ sub_2a3b2eb10 -> sub_2be52add8 : 1040 -> 1048
~ sub_2a3b2ef20 -> sub_2be52b1f0 : 132 -> 136
~ _waddnstr : 160 -> 176
~ _wadd_wchnstr : 864 -> 888
~ _waddnwstr : 160 -> 176
~ _wbkgrnd : 528 -> 524
~ _wborder : 1728 -> 1736
~ _setcchar : 312 -> 316
~ _wchgat : 296 -> 300
~ _wclrtobot : 208 -> 216
~ _wclrtoeol : 208 -> 224
~ _start_color : 540 -> 556
~ _init_pair : 944 -> 952
~ _wdelch : 196 -> 204
~ _werase : 264 -> 252
~ _wget_wch : 456 -> 460
~ __nc_wgetch : 1732 -> 1740
~ _wgetnstr : 840 -> 844
~ _whline : 464 -> 404
~ _win_wch : 68 -> 72
~ _win_wchnstr : 188 -> 200
~ _winchnstr : 128 -> 144
~ __nc_insert_wch : 372 -> 392
~ __nc_insert_ch : 984 -> 1004
~ _winsnstr : 172 -> 176
~ _winnstr : 476 -> 480
~ _winnwstr : 208 -> 220
~ sub_2a3b3ae18 -> sub_2be53718c : 436 -> 444
~ sub_2a3b3b294 -> sub_2be537610 : 956 -> 964
~ sub_2a3b3c4b8 -> sub_2be53883c : 1800 -> 1784
~ sub_2a3b3cbd8 -> sub_2be538f4c : 1940 -> 1944
~ __nc_freewin : 332 -> 336
~ _newwin : 360 -> 368
~ _derwin : 268 -> 272
~ _meta : 136 -> 140
~ _copywin : 816 -> 852
~ _newpad : 292 -> 296
~ _wredrawln : 344 -> 340
~ _wnoutrefresh : 1236 -> 1252
~ _getwin : 456 -> 460
~ _putwin : 216 -> 220
~ __nc_scroll_window : 560 -> 576
~ _delscreen : 524 -> 528
~ __nc_setup_tinfo : 248 -> 252
~ __nc_tinfo_cmdch : 152 -> 156
~ __nc_format_slks : 408 -> 416
~ __nc_slk_initialize : 580 -> 584
~ sub_2a3b423d4 -> sub_2be53e7c4 : 716 -> 724
~ _slk_set : 812 -> 816
~ _tgetent : 1144 -> 1160
~ _tgoto : 1164 -> 1172
~ sub_2a3b43d38 -> sub_2be54014c : 5628 -> 5904
~ __nc_flush : 152 -> 156
~ __nc_timed_wait : 684 -> 700
~ _unget_wch : 264 -> 268
~ __nc_ungetch : 124 -> 128
~ _wvline : 420 -> 424
~ _wvline_set : 320 -> 324
~ __nc_init_wacs : 288 -> 320
~ _winch : 44 -> 48
~ _mvderwin : 212 -> 216
~ _dupwin : 356 -> 364
~ __nc_first_name : 192 -> 204
~ __nc_parse_entry : 6004 -> 6152
~ __nc_init_termtype : 244 -> 252
~ __nc_read_termtype : 2116 -> 2124
~ sub_2a3b4a73c -> sub_2be546d68 : 272 -> 276
~ __nc_remove_string : 132 -> 144
~ sub_2a3b4bca8 -> sub_2be5482e4 : 172 -> 180
~ _doupdate : 2152 -> 2168
~ sub_2a3b4c9c8 -> sub_2be54901c : 204 -> 208
~ sub_2a3b4ce08 -> sub_2be549460 : 5456 -> 5432
~ sub_2a3b4f46c -> sub_2be54baac : 580 -> 584
~ sub_2a3b4fe84 -> sub_2be54c4c8 : 520 -> 524
~ sub_2a3b5008c -> sub_2be54c6d4 : 1108 -> 1120
~ sub_2a3b50658 -> sub_2be54ccac : 544 -> 556
~ sub_2a3b50930 -> sub_2be54cf90 : 1360 -> 1368
~ sub_2a3b50fa4 -> sub_2be54d60c : 580 -> 588
~ _wresize : 900 -> 908
~ sub_2a3b515f4 -> sub_2be54dc6c : 236 -> 244
~ sub_2a3b51d60 -> sub_2be54e3e0 : 2056 -> 2068
~ __nc_keyname : 760 -> 772
CStrings:
+ "/\\|=,:"
+ "invalid name for use-clause \"%s\""
+ "missing name for use-clause"
+ "too many use-clauses, ignored \"%s\""

```
