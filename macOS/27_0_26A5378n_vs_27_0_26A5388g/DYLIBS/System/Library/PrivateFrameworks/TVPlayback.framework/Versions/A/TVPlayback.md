## TVPlayback

> `/System/Library/PrivateFrameworks/TVPlayback.framework/Versions/A/TVPlayback`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
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
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-635.0.1.0.0
-  __TEXT.__text: 0x1475e4
-  __TEXT.__objc_methlist: 0x58a0
+635.0.4.0.0
+  __TEXT.__text: 0x147fc0
+  __TEXT.__objc_methlist: 0x58b8
   __TEXT.__const: 0x22e90
-  __TEXT.__cstring: 0x6718
-  __TEXT.__oslogstring: 0x54b9
-  __TEXT.__gcc_except_tab: 0x1d24
-  __TEXT.__unwind_info: 0x16a8
+  __TEXT.__cstring: 0x6748
+  __TEXT.__oslogstring: 0x5739
+  __TEXT.__gcc_except_tab: 0x1d58
+  __TEXT.__unwind_info: 0x16b8
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b50
+  __DATA_CONST.__objc_selrefs: 0x3b68
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x738
   __AUTH_CONST.__const: 0xba70
-  __AUTH_CONST.__cfstring: 0x65c0
-  __AUTH_CONST.__objc_const: 0x89a0
+  __AUTH_CONST.__cfstring: 0x65e0
+  __AUTH_CONST.__objc_const: 0x89d0
   __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x398
   __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x6c8
+  __DATA.__objc_ivar: 0x6cc
   __DATA.__data: 0x1040
   __DATA.__bss: 0x100
   __DATA.__common: 0x9f0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2321
-  Symbols:   5376
-  CStrings:  1277
+  Functions: 2325
+  Symbols:   5382
+  CStrings:  1287
 
Symbols:
+ -[TVPPlayer setSubtitlesDisabled:]
+ -[TVPPlayer subtitlesDisabled]
+ GCC_except_table246
+ GCC_except_table252
+ GCC_except_table256
+ GCC_except_table259
+ GCC_except_table307
+ GCC_except_table339
+ GCC_except_table351
+ GCC_except_table378
+ GCC_except_table382
+ GCC_except_table397
+ GCC_except_table421
+ GCC_except_table428
+ GCC_except_table429
+ GCC_except_table433
+ GCC_except_table434
+ GCC_except_table438
+ GCC_except_table441
+ GCC_except_table444
+ GCC_except_table445
+ GCC_except_table451
+ GCC_except_table455
+ GCC_except_table460
+ GCC_except_table464
+ GCC_except_table469
+ GCC_except_table481
+ GCC_except_table510
+ GCC_except_table512
+ GCC_except_table515
+ GCC_except_table521
+ GCC_except_table530
+ GCC_except_table532
+ GCC_except_table535
+ GCC_except_table544
+ GCC_except_table550
+ GCC_except_table558
+ GCC_except_table561
+ GCC_except_table573
+ GCC_except_table575
+ GCC_except_table582
+ OBJC_IVAR_$_TVPPlayer._subtitlesDisabled
+ ___AVInterstitialPlayerItemPresentationSizeKVOContext
+ ___AVPlayerItemHasVideoKVOContext
+ ___AVPlayerItemPresentationSizeKVOContent
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80r88w_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64s72s80r88w
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80r88w
+ _objc_msgSend$presentationSize
+ _objc_msgSend$subtitlesDisabled
- GCC_except_table244
- GCC_except_table250
- GCC_except_table254
- GCC_except_table257
- GCC_except_table305
- GCC_except_table337
- GCC_except_table349
- GCC_except_table376
- GCC_except_table380
- GCC_except_table395
- GCC_except_table419
- GCC_except_table426
- GCC_except_table427
- GCC_except_table431
- GCC_except_table432
- GCC_except_table436
- GCC_except_table437
- GCC_except_table440
- GCC_except_table443
- GCC_except_table449
- GCC_except_table453
- GCC_except_table458
- GCC_except_table462
- GCC_except_table467
- GCC_except_table475
- GCC_except_table506
- GCC_except_table511
- GCC_except_table517
- GCC_except_table526
- GCC_except_table528
- GCC_except_table531
- GCC_except_table536
- GCC_except_table546
- GCC_except_table554
- GCC_except_table557
- GCC_except_table569
- GCC_except_table571
- GCC_except_table574
- ___60-[TVPPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke_2
- ___AVPlayerItemHasVideoContext
- ___AVPlayerItemPresentationSizeContent
- ___block_descriptor_88_e8_32s40s48s56s64s72r80w_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56s64s72r80w
- ___destroy_helper_block_e8_32s40s48s56s64s72r80w
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
