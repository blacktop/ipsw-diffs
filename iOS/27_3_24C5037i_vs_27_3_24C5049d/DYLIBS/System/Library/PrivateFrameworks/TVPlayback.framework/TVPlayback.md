## TVPlayback

> `/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback`

```diff

-635.20.5.0.0
-  __TEXT.__text: 0x69a58
-  __TEXT.__objc_methlist: 0x61c8
+635.20.7.0.0
+  __TEXT.__text: 0x6a25c
+  __TEXT.__objc_methlist: 0x6228
   __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x6cc1
-  __TEXT.__oslogstring: 0x75ab
+  __TEXT.__cstring: 0x6ce3
+  __TEXT.__oslogstring: 0x764a
   __TEXT.__gcc_except_tab: 0x1fd8
-  __TEXT.__unwind_info: 0x1bf0
+  __TEXT.__unwind_info: 0x1c00
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2500
+  __DATA_CONST.__const: 0x2550
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f38
+  __DATA_CONST.__objc_selrefs: 0x3f78
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x8f8
   __AUTH_CONST.__const: 0x6a0
-  __AUTH_CONST.__cfstring: 0x6e40
-  __AUTH_CONST.__objc_const: 0x9d40
+  __AUTH_CONST.__cfstring: 0x6e60
+  __AUTH_CONST.__objc_const: 0x9da0
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x450
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x7e8
+  __DATA.__objc_ivar: 0x7f0
   __DATA.__data: 0xae0
   __DATA_DIRTY.__objc_data: 0xb40
   __DATA_DIRTY.__bss: 0x230

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2328
-  Symbols:   4284
-  CStrings:  1483
+  Functions: 2337
+  Symbols:   4297
+  CStrings:  1486
 
Symbols:
+ -[TVPPlayer _elapsedTimeAdjustedForTrailingInterstitialSnapback:]
+ -[TVPPlayer _trailingInterstitialSnapbackWorkaroundEnabled]
+ -[TVPPlayer _updatePlayedThroughTrailingInterstitial]
+ -[TVPPlayer lastSeekTargetTime]
+ -[TVPPlayer playedThroughTrailingInterstitial]
+ -[TVPPlayer setLastSeekTargetTime:]
+ -[TVPPlayer setPlayedThroughTrailingInterstitial:]
+ -[TVPPlayer waitingForAVKitSeekAfterFinishingExternalImageScanning]
+ GCC_except_table129
+ GCC_except_table138
+ GCC_except_table243
+ GCC_except_table249
+ GCC_except_table253
+ GCC_except_table256
+ GCC_except_table305
+ GCC_except_table339
+ GCC_except_table355
+ GCC_except_table377
+ GCC_except_table381
+ GCC_except_table390
+ GCC_except_table402
+ GCC_except_table421
+ GCC_except_table428
+ GCC_except_table431
+ GCC_except_table434
+ GCC_except_table437
+ GCC_except_table438
+ GCC_except_table440
+ GCC_except_table446
+ GCC_except_table449
+ GCC_except_table453
+ GCC_except_table467
+ GCC_except_table469
+ GCC_except_table471
+ GCC_except_table496
+ GCC_except_table500
+ GCC_except_table503
+ GCC_except_table509
+ GCC_except_table516
+ GCC_except_table518
+ GCC_except_table525
+ GCC_except_table529
+ GCC_except_table535
+ GCC_except_table543
+ GCC_except_table546
+ GCC_except_table55
+ GCC_except_table560
+ GCC_except_table563
+ GCC_except_table567
+ GCC_except_table60
+ _OBJC_IVAR_$_TVPPlayer._lastSeekTargetTime
+ _OBJC_IVAR_$_TVPPlayer._playedThroughTrailingInterstitial
+ ___block_descriptor_56_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_72_e8_32s40s_e5_v8?0ls32l8s40l8
- GCC_except_table128
- GCC_except_table136
- GCC_except_table241
- GCC_except_table247
- GCC_except_table251
- GCC_except_table254
- GCC_except_table303
- GCC_except_table334
- GCC_except_table350
- GCC_except_table372
- GCC_except_table376
- GCC_except_table385
- GCC_except_table397
- GCC_except_table416
- GCC_except_table423
- GCC_except_table424
- GCC_except_table426
- GCC_except_table427
- GCC_except_table430
- GCC_except_table433
- GCC_except_table436
- GCC_except_table444
- GCC_except_table448
- GCC_except_table452
- GCC_except_table464
- GCC_except_table466
- GCC_except_table491
- GCC_except_table493
- GCC_except_table495
- GCC_except_table504
- GCC_except_table511
- GCC_except_table513
- GCC_except_table515
- GCC_except_table524
- GCC_except_table530
- GCC_except_table538
- GCC_except_table541
- GCC_except_table553
- GCC_except_table555
- GCC_except_table562
- GCC_except_table58
CStrings:
+ "DisablePostRollSnapbackWorkaround"
+ "Playing trailing interstitial of an item with external interstitials"
+ "Reporting duration %@ as elapsed time instead of %@ due to trailing interstitial snapback"
```
