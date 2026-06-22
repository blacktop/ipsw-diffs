## lockstat

> `/usr/bin/lockstat`

```diff

 415.0.0.0.0
-  __TEXT.__text: 0x3444 sha256:c59c6ec7ca0dd19a22c8c3c2ebcba204c4a02b46f22ec2893aaff4e9ab2a25b9
+  __TEXT.__text: 0x348c sha256:986d979755a89c39ac77dd2e34faef672161d709781269e7f65d6b2099bfbef9
   __TEXT.__auth_stubs: 0x430 sha256:2e75975725a27e07f434aaa4b4d8835b8dfebd7a4aa1fb2d49478bbb157da623
   __TEXT.__const: 0x8 sha256:3743e2520ce26efc75a9a9fb439f5a9363b9db858a88cc95bcf647236a86c012
   __TEXT.__cstring: 0x137d sha256:38dc2811fdbe56607441e4a7ecc01f0a16a40304ee7e2a51277967deac333657
-  __TEXT.__unwind_info: 0xc8 sha256:4dda3ce769b3c34437f09ea48dbd489f5cfdca826e714f968194b054ce65f7c7
+  __TEXT.__unwind_info: 0xc8 sha256:39a59c2189e785e728d399aaf72ac743fce54a267a7dc708297bc369495bc96f
   __DATA_CONST.__auth_got: 0x218 sha256:5f829b46505dc0792f72c55d0cbcecb2fc66a04099f10398e3e8898b1598f160
   __DATA_CONST.__got: 0x28 sha256:de5f8aaa9168ed0789058f8fc92204f3921310dcbc03c2e64c92de13dd80b50c
-  __DATA.__data: 0x3488 sha256:76d83ebcff0464c4922108d81e6540e1079dabb4397aae431ce3ecf442bdbb0d
+  __DATA.__data: 0x3488 sha256:9bc746bfa1b7c64895b98e134538206aa443fa17f2e17a19fd3f1e1afc98414d
   __DATA.__bss: 0x780 sha256:155e437b946ac82ae591ff382b8d19efda9397b2282672dbabd91ec31ce8a651
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/Versions/A/CoreSymbolication
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libdtrace.dylib
-  UUID: 1071E730-09E8-334E-8AE7-F05259AA7FAD
+  UUID: 3BADBC96-43E2-32B8-BCB2-B1C6DB51B029
   Functions: 29
   Symbols:   132
   CStrings:  161
Functions:
~ _dtrace_gethrtime : sha256 a509dbc69f581c10757fd9d1cad51312065c1eb298a070094064308fa4d9cdfa -> bdae337db60546c8420df81a7b85a5631881e5490ac7837d377f7927f2861b43
~ _main : 8760 -> 8852
~ _fail : sha256 73ba2e02b4e4565c834bd3b8cbcb0db0041d71ce7474662490eb66e31e5ade58 -> 2f261e52caf1628dd0fbbe5cea4f19852ee57b7e8644209ee480bb68930447de
~ _drophandler : sha256 7d887f818c8a9fab03aa8c17ab0d8074aefcffd348517f6e9ca83cdf7f4c82e6 -> f9542c21588eaee59fca052cb641c82c166bdd955c367b1d728fed0dc3a2ae3f
~ _filter_add : sha256 42d1daf0ed5d6f6ea57fd49d6c9fd05a2a7e531ccde002df047b46ee2eb1de99 -> f2c51f7509e45aa387d6cb972dd10bbf4cd46abf06434d5546a76d924e64b4b7
~ _predicate_add : sha256 bb3b903c99b0944ad87fb6f8cf7d6d16579cc098642639058502d70e1cf92fa7 -> 4cfeb1aa3f8e64322510f14908d735ce23b8cdfce9014385683e18c94619b333
~ _lockstat_mergesort : 336 -> 320
~ _lockcmp : 148 -> 140
~ _coalesce : 264 -> 268
~ _site_and_count_cmp_anylock : 136 -> 128
~ _sitecmp_anylock : 128 -> 120
~ _show_events : 268 -> 260
~ _dprog_add : sha256 bc544b969437b68ac3767529fd689b83fe73890799e0925252e16fac58cc7303 -> 5dfb6119f84e265fe2a4db9ed3c00d6819b67459e5113d4e9b1d1f3ec86dd903
~ _process_trace : sha256 e011eec65e29a30c8df1fdb3a64e386103ac595307a1d8fd48774b9bb0007345 -> d08f936c3140cf8557acba4be16c0b8948916a26f292bd53f823f18a71c15417
~ _process_aggregate : 324 -> 336
~ _lsrec_fill : 376 -> 388
~ _format_symbol : sha256 77ea6eccde54b8f85d4eb69ca804ccfbd92cc3015479166e893e1d72a762520d -> 3cba036de30ae4c91e0e8b6aabf2f500b028b217a5f49746a9443d08ca865ccc
~ sub_1000038c8 -> sub_100003910 : sha256 3975bd96831046941a39531cd4229e22c70d29a5a6661359e5d12bf218208e3e -> 4f28c777c1381828b646491775e0e2e8cd568c18e66d39cb5d7bed9504c3f210
~ _dfail : sha256 ea41b3722c555e5e16d8acca22cd90833c1b3f8b359ccc2a3eb9854347f35c9d -> 5bac507d348d8a26e95b48212b4419b27aed72e78f4286aeb94546bf0eab9411
~ _usage : sha256 3bacfc330af319f862f9e4f36eefa28b390a719f0ffa9bcced3bb4e83b2c457e -> a1266b54f51b3392171aabef718f23faf85b46cd83a8a11410f8b55e9e92dda7

```
