## TVPlayback

> `/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-635.0.1.0.0
-  __TEXT.__text: 0x68498
-  __TEXT.__objc_methlist: 0x5f98
+635.0.4.0.0
+  __TEXT.__text: 0x68e44
+  __TEXT.__objc_methlist: 0x5fb0
   __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x6ad0
-  __TEXT.__oslogstring: 0x6d96
-  __TEXT.__gcc_except_tab: 0x1f9c
-  __TEXT.__unwind_info: 0x16c0
+  __TEXT.__cstring: 0x6b00
+  __TEXT.__oslogstring: 0x7016
+  __TEXT.__gcc_except_tab: 0x1fd8
+  __TEXT.__unwind_info: 0x16d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3df0
+  __DATA_CONST.__objc_selrefs: 0x3e08
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x8d8
   __AUTH_CONST.__const: 0x680
-  __AUTH_CONST.__cfstring: 0x6c40
-  __AUTH_CONST.__objc_const: 0x9a78
+  __AUTH_CONST.__cfstring: 0x6c60
+  __AUTH_CONST.__objc_const: 0x9aa8
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x430
   __AUTH.__objc_data: 0x870
-  __DATA.__objc_ivar: 0x7c8
-  __DATA.__data: 0xad8
+  __DATA.__objc_ivar: 0x7cc
+  __DATA.__data: 0xae0
   __DATA.__bss: 0xa8
   __DATA_DIRTY.__objc_data: 0xb40
   __DATA_DIRTY.__bss: 0x230

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2272
-  Symbols:   5670
-  CStrings:  1438
+  Functions: 2276
+  Symbols:   5676
+  CStrings:  1448
 
Symbols:
+ -[TVPPlayer setSubtitlesDisabled:]
+ -[TVPPlayer subtitlesDisabled]
+ GCC_except_table234
+ GCC_except_table240
+ GCC_except_table244
+ GCC_except_table247
+ GCC_except_table295
+ GCC_except_table325
+ GCC_except_table335
+ GCC_except_table357
+ GCC_except_table361
+ GCC_except_table370
+ GCC_except_table381
+ GCC_except_table400
+ GCC_except_table407
+ GCC_except_table410
+ GCC_except_table413
+ GCC_except_table416
+ GCC_except_table419
+ GCC_except_table420
+ GCC_except_table425
+ GCC_except_table428
+ GCC_except_table432
+ GCC_except_table436
+ GCC_except_table441
+ GCC_except_table450
+ GCC_except_table477
+ GCC_except_table479
+ GCC_except_table482
+ GCC_except_table488
+ GCC_except_table497
+ GCC_except_table499
+ GCC_except_table508
+ GCC_except_table514
+ GCC_except_table522
+ GCC_except_table525
+ GCC_except_table537
+ GCC_except_table539
+ GCC_except_table546
+ _OBJC_IVAR_$_TVPPlayer._subtitlesDisabled
+ ___AVInterstitialPlayerItemPresentationSizeKVOContext
+ ___AVPlayerItemHasVideoKVOContext
+ ___AVPlayerItemPresentationSizeKVOContent
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80r88w_e5_v8?0ls32l8r80l8s40l8s48l8s56l8s64l8s72l8w88l8
+ _objc_msgSend$presentationSize
+ _objc_msgSend$subtitlesDisabled
- GCC_except_table232
- GCC_except_table238
- GCC_except_table242
- GCC_except_table245
- GCC_except_table293
- GCC_except_table323
- GCC_except_table333
- GCC_except_table355
- GCC_except_table359
- GCC_except_table368
- GCC_except_table379
- GCC_except_table398
- GCC_except_table405
- GCC_except_table406
- GCC_except_table409
- GCC_except_table412
- GCC_except_table415
- GCC_except_table418
- GCC_except_table423
- GCC_except_table426
- GCC_except_table430
- GCC_except_table434
- GCC_except_table439
- GCC_except_table444
- GCC_except_table473
- GCC_except_table478
- GCC_except_table484
- GCC_except_table491
- GCC_except_table493
- GCC_except_table500
- GCC_except_table510
- GCC_except_table518
- GCC_except_table521
- GCC_except_table533
- GCC_except_table535
- GCC_except_table538
- ___60-[TVPPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke_2
- ___AVPlayerItemHasVideoContext
- ___AVPlayerItemPresentationSizeContent
- ___block_descriptor_88_e8_32s40s48s56s64s72r80w_e5_v8?0ls32l8r72l8s40l8s48l8s56l8s64l8w80l8
CStrings:
+ "Automatically selecting option in legible group"
+ "Interstitial player item presentationSize did change to %@"
+ "Not updating currentMediaItemPresentationSize since interstitial player is current player"
+ "Not updating currentMediaItemPresentationSize since main player is current player"
+ "Selecting nil media option in legible group"
+ "Setting nil media selection option in legible group since subtitlesDisabled is YES"
+ "Updating currentMediaItemPresentationSize since interstitial player is current player"
+ "Updating currentMediaItemPresentationSize since main player is current player"
+ "Updating currentMediaItemPresentationSize to value from %@ player: %@"
+ "interstitialPlayer.currentItem.presentationSize"
```
