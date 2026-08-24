## TVPlayback

> `/System/Library/PrivateFrameworks/TVPlayback.framework/Versions/A/TVPlayback`

```diff

-635.0.4.0.0
-  __TEXT.__text: 0x147fc0
-  __TEXT.__objc_methlist: 0x58b8
+635.0.7.0.0
+  __TEXT.__text: 0x14829c
+  __TEXT.__objc_methlist: 0x58d0
   __TEXT.__const: 0x22e90
-  __TEXT.__cstring: 0x6748
-  __TEXT.__oslogstring: 0x5739
+  __TEXT.__cstring: 0x6768
+  __TEXT.__oslogstring: 0x572b
   __TEXT.__gcc_except_tab: 0x1d58
-  __TEXT.__unwind_info: 0x16b8
+  __TEXT.__unwind_info: 0x16c0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b68
+  __DATA_CONST.__objc_selrefs: 0x3b80
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x738
   __AUTH_CONST.__const: 0xba70
-  __AUTH_CONST.__cfstring: 0x65e0
+  __AUTH_CONST.__cfstring: 0x6600
   __AUTH_CONST.__objc_const: 0x89d0
   __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x398
+  __AUTH_CONST.__auth_got: 0x388
   __AUTH.__objc_data: 0x780
   __DATA.__objc_ivar: 0x6cc
   __DATA.__data: 0x1040

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2325
-  Symbols:   5382
-  CStrings:  1287
+  Functions: 2330
+  Symbols:   5384
+  CStrings:  1288
 
Symbols:
+ -[TVPPlayer displaysUsedForPlayback]
+ -[TVPPlayer setDisplaysUsedForPlayback:]
+ GCC_except_table248
+ GCC_except_table254
+ GCC_except_table258
+ GCC_except_table261
+ GCC_except_table309
+ GCC_except_table341
+ GCC_except_table353
+ GCC_except_table380
+ GCC_except_table384
+ GCC_except_table399
+ GCC_except_table423
+ GCC_except_table430
+ GCC_except_table431
+ GCC_except_table435
+ GCC_except_table436
+ GCC_except_table440
+ GCC_except_table443
+ GCC_except_table446
+ GCC_except_table447
+ GCC_except_table453
+ GCC_except_table457
+ GCC_except_table462
+ GCC_except_table466
+ GCC_except_table471
+ GCC_except_table483
+ GCC_except_table514
+ GCC_except_table517
+ GCC_except_table523
+ GCC_except_table534
+ GCC_except_table537
+ GCC_except_table542
+ GCC_except_table546
+ GCC_except_table552
+ GCC_except_table560
+ GCC_except_table563
+ GCC_except_table577
+ GCC_except_table580
+ GCC_except_table584
+ OBJC_IVAR_$_TVPPlayer._displaysUsedForPlayback
+ _CGDisplayIsInMirrorSet
+ _CGDisplayMirrorsDisplay
+ _TVPPlaybackNeedsMachineAuthKey
+ _objc_msgSend$displaysUsedForPlayback
+ _objc_msgSend$unsignedIntValue
- GCC_except_table246
- GCC_except_table252
- GCC_except_table256
- GCC_except_table259
- GCC_except_table307
- GCC_except_table339
- GCC_except_table351
- GCC_except_table378
- GCC_except_table382
- GCC_except_table397
- GCC_except_table421
- GCC_except_table428
- GCC_except_table429
- GCC_except_table433
- GCC_except_table434
- GCC_except_table438
- GCC_except_table439
- GCC_except_table442
- GCC_except_table445
- GCC_except_table451
- GCC_except_table455
- GCC_except_table460
- GCC_except_table464
- GCC_except_table469
- GCC_except_table477
- GCC_except_table508
- GCC_except_table515
- GCC_except_table521
- GCC_except_table530
- GCC_except_table535
- GCC_except_table540
- GCC_except_table544
- GCC_except_table550
- GCC_except_table558
- GCC_except_table561
- GCC_except_table573
- GCC_except_table578
- GCC_except_table582
- OBJC_IVAR_$_TVPPlayer._playbackFrameRelativeToScreen
- _CGDisplayBounds
- _CGGetDisplaysWithRect
- _CGRectIsEmpty
- _NSStringFromRect
- _objc_msgSend$playbackFrameRelativeToScreen
CStrings:
+ "Adding primary display %u to display list"
+ "Display %u is in mirror set. Primary display is %u"
+ "Found secondary display %u. Adding to display list"
+ "TVPPlaybackNeedsMachineAuthKey"
+ "displaysUsedForPlayback is empty, adding all displays"
+ "displaysUsedForPlayback set to %@"
+ "setPlaybackFrameRelativeToScreen is unimplemented"
- "Display bounds for display ID %lu: %@"
- "No displays intersect playback frame, falling back to all displays"
- "Playback frame: %@"
- "playbackFrameRelativeToScreen is empty, adding all displays"
- "playbackFrameRelativeToScreen is non-nil, adding intersecting displays"
- "playbackFrameRelativeToScreen set to: %@"
```
