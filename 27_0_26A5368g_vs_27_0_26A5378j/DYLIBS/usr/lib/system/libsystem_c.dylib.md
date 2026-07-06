## libsystem_c.dylib

> `/usr/lib/system/libsystem_c.dylib`

```diff

-  __TEXT.__text: 0x7b52c
+  __TEXT.__text: 0x7ad78
   __TEXT.__const: 0x2978
   __TEXT.__cstring: 0x3127
   __TEXT.__oslogstring: 0x5c
-  __TEXT.__unwind_info: 0x1458
+  __TEXT.__unwind_info: 0x1460
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x1858
   __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__auth_got: 0x848
+  __AUTH_CONST.__auth_got: 0x830
   __AUTH.__data: 0x30
   __AUTH.__constrw: 0x80
   __DATA.__crash_info: 0x148
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH.__data : content changed
~ __AUTH.__constrw : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Functions:
~ _strtoll_l : 628 -> 612
~ _strnstr : 188 -> 192
~ ___vfprintf : 11940 -> 12184
~ ___sfvwrite : 968 -> 956
~ ___ultoa : 288 -> 296
~ ___ultoa : 288 -> 296
~ _uuid_copy : 36 -> 24
~ ___unsetenv_locked : 244 -> 240
~ _strtol_l : 628 -> 612
~ _tzparse : 1172 -> 1164
~ _getsecs : 308 -> 316
~ _getrule : 524 -> 532
~ _timesub : 1172 -> 1180
~ _setlocale : 980 -> 952
~ _strtoimax_l : 628 -> 612
~ _uuid_unparse_upper : 108 -> 104
~ _heapsort : 696 -> 644
~ __isort : 456 -> 404
~ __isort : 456 -> 420
~ _uuid_parse : 388 -> 376
~ _strtoul_l : 616 -> 600
~ ___heapsort_r : 744 -> 672
~ _strcasestr_l : 252 -> 244
~ ___dtoa : 3708 -> 3592
~ _strtoumax_l : 616 -> 600
~ ___sfp : 520 -> 504
~ ___multadd_D2A : 184 -> 176
~ __inet_aton_check : 532 -> 544
~ _strcspn : 188 -> 184
~ _strspn : 184 -> 180
~ _uuid_is_null : 44 -> 36
~ _uuid_unparse : 108 -> 104
~ ___rshift_D2A : 200 -> 180
~ _mergesort : 1972 -> 1924
~ _insertionsort : 196 -> 176
~ _insertionsort : 208 -> 196
~ _regncomp_l : 444 -> 436
~ _tre_parse : 5532 -> 5412
~ _tre_add_tags : 5740 -> 5760
~ _tre_make_trans : 868 -> 908
~ _tre_match : 448 -> 440
~ _tre_tnfa_run_parallel : 6272 -> 6276
~ _strtoull_l : 616 -> 600
~ _istrsenvisx : 1540 -> 1568
~ __UTF8_mbsnrtowcs : 428 -> 424
~ _wcslen : 32 -> 24
~ _mergesort_b : 2160 -> 2140
~ __strptime0 : 5664 -> 5668
~ __fwalk : 140 -> 132
~ _uuid_unparse_lower : 108 -> 104
~ _fnmatch : 1264 -> 1248
~ ___glob : 708 -> 712
~ _glob0 : 660 -> 628
~ _glob2 : 1308 -> 1288
~ ___errstr : 236 -> 244
~ ___sum_D2A : 320 -> 292
~ __qsort : 2368 -> 2252
~ __qsort : 2504 -> 2368
~ _heapsort_b : 756 -> 688
~ ___xprintf_domain_init : 332 -> 324
~ ___printf_comp : 1852 -> 1840
~ ___hdtoa : 944 -> 908
~ _fastParse64 : 3292 -> 3284
~ _generalSlowpath : 1820 -> 1796
~ _shiftRightMPWithRounding : 560 -> 568
~ _shiftLeftMP : 168 -> 160
~ ___crypt_des_cipher : 1140 -> 1136
~ _setkey : 100 -> 96
~ _encrypt : 204 -> 200
~ _getdiskbyname : 1684 -> 1664
~ _getttyent : 1664 -> 1684
~ _initshells : 536 -> 496
~ _strtofflags : 308 -> 312
~ _filter_utmpx : 916 -> 884
~ _acl_from_text : 1696 -> 1672
~ _acl_to_text : 1260 -> 1240
~ ___bt_defpfx : 88 -> 72
~ ___gdtoa : 4364 -> 4392
~ ___match_D2A : 68 -> 72
~ __e_visprintf : 312 -> 304
~ _getent : 1640 -> 1652
~ _cgetnext : 972 -> 944
~ _cgetustr : 280 -> 252
~ _getmode : 280 -> 272
~ _setmode : 1344 -> 1328
~ __sm_compress_mode : 228 -> 216
~ _strnunvisx : 344 -> 312
~ __ascii_mbsnrtowcs : 192 -> 188
~ __ascii_wcsnrtombs : 204 -> 200
~ ___collate_load_tables_legacy : 1996 -> 1964
~ __collate_wxfrm : 636 -> 624
~ __collate_sxfrm : 796 -> 784
~ __GB2312_mbrtowc : 296 -> 284
~ __none_mbsnrtowcs : 148 -> 144
~ __none_wcsnrtombs : 204 -> 200
~ ___wcsnrtombs_std : 524 -> 496
~ _wcstoimax_l : 596 -> 584
~ _wcstol_l : 596 -> 584
~ _wcstoll_l : 596 -> 584
~ _wcstoul_l : 592 -> 580
~ _wcstoull_l : 592 -> 580
~ _wcstoumax_l : 592 -> 580
~ _wctype_l : 276 -> 268
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
~ _strsignal_r : 348 -> 340
~ _swab : 116 -> 120
~ _wcscat : 68 -> 60
~ _wcscoll_l : 1132 -> 1108
~ _wcscpy : 32 -> 20
~ _wordexp : 2500 -> 2492
~ _wcsnlen : 52 -> 48
~ _wcsstr : 140 -> 136
~ __UTF2_mbsnrtowcs : 428 -> 424
~ _getsubopt : 384 -> 364
~ _r_sort_a : 1024 -> 1028
~ _r_sort_b : 928 -> 932
~ _gcvt : 684 -> 680
~ _getargs : 164 -> 160
~ __psort : 2424 -> 2296
~ __psort : 2620 -> 2488
~ _getargs : 164 -> 160
~ __psort : 2552 -> 2432
~ __strfmon : 3244 -> 3204
~ _tre_expand_macro : 140 -> 152
~ _tre_parse_bracket_items : 1564 -> 1548
~ _regerror : 392 -> 376

```
