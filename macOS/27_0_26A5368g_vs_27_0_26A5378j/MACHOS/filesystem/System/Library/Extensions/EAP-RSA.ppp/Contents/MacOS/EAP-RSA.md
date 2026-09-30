## EAP-RSA

> `/System/Library/Extensions/EAP-RSA.ppp/Contents/MacOS/EAP-RSA`

```diff

-  __TEXT.__text: 0x26524
+  __TEXT.__text: 0x264e4
   __TEXT.__auth_stubs: 0x7c0
   __TEXT.__cstring: 0x5ad0
   __TEXT.__const: 0x13a8
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_d2c : 1448 -> 1472
~ _DoStateCheck : 372 -> 356
~ _ReadCfg : 5068 -> 5088
~ sub_5e0c -> sub_5e28 : 200 -> 204
~ sub_5ed4 -> sub_5ef4 : 688 -> 684
~ sub_6184 -> sub_61a0 : 772 -> 776
~ sub_6488 -> sub_64a8 : 620 -> 628
~ sub_66f4 -> sub_671c : 620 -> 628
~ _get_response_segs : 3144 -> 3152
~ sub_b384 -> sub_b3bc : 344 -> 352
~ sub_b870 -> sub_b8b0 : 472 -> 476
~ sub_13c1c -> sub_13c60 : 184 -> 176
~ _RC5EncryptECB : 176 -> 168
~ _sdi_setkey : 108 -> 104
~ _f_make_nibbles : 48 -> 40
~ _f_sdi : 484 -> 468
~ sub_18a38 -> sub_18a50 : 156 -> 136
~ sub_1b5ec -> sub_1b5f0 : 112 -> 128
~ sub_1c4f4 -> sub_1c508 : 468 -> 472
~ sub_1ce78 -> sub_1ce90 : 268 -> 284
~ sub_1e684 -> sub_1e6ac : 324 -> 312
~ sub_1edd0 -> sub_1edec : 212 -> 200
~ sub_1eea4 -> sub_1eeb4 : 216 -> 212
~ sub_21548 -> sub_21554 : 152 -> 148
~ sub_22f24 -> sub_22f2c : 140 -> 124
~ sub_231d4 -> sub_231cc : 244 -> 224
~ sub_232c8 -> sub_232ac : 160 -> 152
~ sub_23368 -> sub_23344 : 144 -> 136
~ sub_25088 -> sub_2505c : 312 -> 304
~ sub_25830 -> sub_257fc : 72 -> 76
~ sub_25e60 -> sub_25e30 : 124 -> 116
~ sub_261b0 -> sub_26178 : 140 -> 132
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CRlppt/Sources/eaprsa/ACEClient/acexport.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CRlppt/Sources/eaprsa/ACEClient/acinit.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CRlppt/Sources/eaprsa/ACEClient/acnetsub.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CRlppt/Sources/eaprsa/ACEClient/acprivate.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CRlppt/Sources/eaprsa/ACEClient/acutil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CRlppt/Sources/eaprsa/ACEClient/creadcfg.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CRlppt/Sources/eaprsa/ACEClient/loadbal.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CRlppt/Sources/eaprsa/ACEClient/newsd_api.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CRlppt/Sources/eaprsa/ACEClient/old_api.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CRlppt/Sources/eaprsa/ACEClient/sync_api.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CRlppt/Sources/eaprsa/ACEClient/udpmsg.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jrPibY/Sources/eaprsa/ACEClient/acexport.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jrPibY/Sources/eaprsa/ACEClient/acinit.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jrPibY/Sources/eaprsa/ACEClient/acnetsub.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jrPibY/Sources/eaprsa/ACEClient/acprivate.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jrPibY/Sources/eaprsa/ACEClient/acutil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jrPibY/Sources/eaprsa/ACEClient/creadcfg.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jrPibY/Sources/eaprsa/ACEClient/loadbal.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jrPibY/Sources/eaprsa/ACEClient/newsd_api.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jrPibY/Sources/eaprsa/ACEClient/old_api.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jrPibY/Sources/eaprsa/ACEClient/sync_api.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jrPibY/Sources/eaprsa/ACEClient/udpmsg.c"

```
