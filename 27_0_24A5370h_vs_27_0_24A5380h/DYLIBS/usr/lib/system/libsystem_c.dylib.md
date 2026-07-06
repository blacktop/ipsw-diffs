## libsystem_c.dylib

> `/usr/lib/system/libsystem_c.dylib`

```diff

-  __TEXT.__text: 0x798d0
+  __TEXT.__text: 0x7911c
   __TEXT.__const: 0x27a0
   __TEXT.__cstring: 0x3280
   __TEXT.__oslogstring: 0x5c
-  __TEXT.__unwind_info: 0x1480
+  __TEXT.__unwind_info: 0x1488
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x1910
   __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__auth_got: 0x810
+  __AUTH_CONST.__auth_got: 0x7f8
   __AUTH.__data: 0x30
   __AUTH.__constrw: 0x80
   __DATA.__crash_info: 0x148
-  __DATA.__data: 0x4d5
+  __DATA.__data: 0x57d
   __DATA.__constrw: 0xc88
-  __DATA.__bss: 0xcb0
+  __DATA.__bss: 0xca8
   __DATA.__common: 0x88
-  __DATA_DIRTY.__data: 0x12f8
-  __DATA_DIRTY.__bss: 0x2d8
+  __DATA_DIRTY.__data: 0x1248
+  __DATA_DIRTY.__bss: 0x2e0
   __DATA_DIRTY.__common: 0x90
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libcorecrypto.dylib
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH.__data : content changed
~ __AUTH.__constrw : content changed
Functions:
~ ___vfprintf : 12160 -> 12252
~ ___sfvwrite : 968 -> 956
~ ___ultoa : 288 -> 296
~ ___ultoa : 288 -> 296
~ ___dtoa : 3704 -> 3588
~ ___multadd_D2A : 184 -> 176
~ _uuid_parse : 388 -> 376
~ _strtoul_l : 616 -> 612
~ _uuid_is_null : 44 -> 36
~ _timesub : 1172 -> 1180
~ _strtol_l : 628 -> 624
~ __qsort : 2364 -> 2276
~ __qsort : 2504 -> 2380
~ _heapsort : 696 -> 644
~ __isort : 456 -> 404
~ __isort : 456 -> 420
~ ___sfp : 520 -> 504
~ _fastParse64 : 3272 -> 3264
~ _strnstr : 188 -> 192
~ _strtoull_l : 616 -> 612
~ _strtoumax_l : 616 -> 612
~ _uuid_copy : 36 -> 24
~ _strtoimax_l : 628 -> 624
~ _strtoll_l : 628 -> 624
~ _uuid_unparse_upper : 108 -> 104
~ _strcasestr_l : 252 -> 244
~ _tzparse : 1172 -> 1164
~ _getsecs : 308 -> 316
~ _getrule : 524 -> 532
~ _uuid_unparse : 108 -> 104
~ ___heapsort_r : 744 -> 672
~ __inet_aton_check : 532 -> 540
~ _setmode : 1344 -> 1328
~ ___unsetenv_locked : 244 -> 240
~ __sm_compress_mode : 228 -> 216
~ ___errstr : 236 -> 244
~ _fnmatch : 1264 -> 1248
~ _tre_match : 448 -> 440
~ _tre_tnfa_run_parallel : 6248 -> 6252
~ _strsignal_r : 348 -> 340
~ _mergesort_b : 2160 -> 2140
~ _insertionsort : 196 -> 176
~ _insertionsort : 208 -> 196
~ _regncomp_l : 444 -> 436
~ _tre_parse : 5528 -> 5428
~ _tre_expand_macro : 140 -> 152
~ _tre_parse_bracket_items : 1564 -> 1548
~ __none_wcsnrtombs : 204 -> 200
~ _wctype_l : 276 -> 268
~ _tre_add_tags : 5640 -> 5664
~ _tre_make_trans : 868 -> 908
~ __fwalk : 140 -> 132
~ _uuid_unparse_lower : 108 -> 104
~ _istrsenvisx : 1540 -> 1568
~ _wcslen : 32 -> 24
~ __none_mbsnrtowcs : 148 -> 144
~ _strcspn : 188 -> 184
~ __UTF8_mbsnrtowcs : 428 -> 424
~ _generalSlowpath : 1800 -> 1776
~ _shiftLeftMP : 168 -> 160
~ _shiftRightMPWithRounding : 560 -> 568
~ ___printf_comp : 1572 -> 1576
~ _setlocale : 980 -> 952
~ __strptime0 : 5668 -> 5672
~ __e_visprintf : 312 -> 304
~ ___crypt_des_cipher : 1116 -> 1132
~ _setkey : 100 -> 96
~ _encrypt : 204 -> 200
~ _getdiskbyname : 1684 -> 1664
~ _getttyent : 1664 -> 1680
~ _initshells : 536 -> 496
~ _strtofflags : 308 -> 312
~ _filter_utmpx : 916 -> 884
~ _acl_from_text : 1696 -> 1672
~ _acl_to_text : 1260 -> 1240
~ ___xprintf_domain_init : 332 -> 324
~ ___bt_defpfx : 88 -> 72
~ ___hdtoa : 944 -> 908
~ ___gdtoa : 4368 -> 4360
~ ___rshift_D2A : 200 -> 180
~ ___match_D2A : 68 -> 72
~ ___sum_D2A : 320 -> 292
~ _getent : 1632 -> 1644
~ _cgetnext : 964 -> 936
~ _cgetustr : 280 -> 252
~ ___glob : 708 -> 712
~ _glob0 : 660 -> 628
~ _glob2 : 1308 -> 1288
~ _getmode : 280 -> 272
~ _strnunvisx : 344 -> 312
~ __ascii_mbsnrtowcs : 192 -> 188
~ __ascii_wcsnrtombs : 204 -> 200
~ ___collate_load_tables_legacy : 1996 -> 1964
~ __collate_wxfrm : 632 -> 620
~ __collate_sxfrm : 792 -> 780
~ __GB2312_mbrtowc : 296 -> 284
~ ___wcsnrtombs_std : 524 -> 496
~ _wcstoimax_l : 596 -> 584
~ _wcstol_l : 596 -> 584
~ _wcstoll_l : 596 -> 584
~ _wcstoul_l : 592 -> 580
~ _wcstoull_l : 592 -> 580
~ _wcstoumax_l : 592 -> 580
~ _inet_net_ntop : 1260 -> 1248
~ _inet_net_pton : 1748 -> 1720
~ _getbits : 152 -> 148
~ _inet_nsap_ntoa : 244 -> 224
~ _setipv4sourcefilter : 440 -> 424
~ _gets : 240 -> 232
~ ___find_arguments : 3332 -> 3316
~ ___find_warguments : 3312 -> 3296
~ ___vfwscanf : 5732 -> 5720
~ _time2posix : 120 -> 128
~ _posix2time : 376 -> 416
~ _strchrnul : 300 -> 296
~ _strspn : 184 -> 180
~ _swab : 116 -> 120
~ _wcscat : 68 -> 60
~ _wcscoll_l : 1132 -> 1108
~ _wcscpy : 32 -> 20
~ _wcsnlen : 52 -> 48
~ _wcsstr : 140 -> 136
~ __UTF2_mbsnrtowcs : 428 -> 424
~ _getsubopt : 384 -> 364
~ _mergesort : 1972 -> 1924
~ _r_sort_a : 1024 -> 1028
~ _r_sort_b : 928 -> 932
~ _gcvt : 684 -> 680
~ _heapsort_b : 756 -> 688
~ _getargs : 164 -> 160
~ __psort : 2424 -> 2300
~ __psort : 2620 -> 2492
~ _getargs : 164 -> 160
~ __psort : 2544 -> 2432
~ __strfmon : 3240 -> 3200
~ _regerror : 388 -> 372

```
