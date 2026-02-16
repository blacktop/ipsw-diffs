## SilexVideo

> `/System/Library/PrivateFrameworks/SilexVideo.framework/SilexVideo`

```diff

-5805.0.0.0.0
-  __TEXT.__text: 0x103b4
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x2030
-  __TEXT.__const: 0x1c4
-  __TEXT.__cstring: 0x56a
-  __TEXT.__gcc_except_tab: 0x420
+5861.1.0.0.0
+  __TEXT.__text: 0x11910
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_methlist: 0x2068
+  __TEXT.__const: 0x1a4
+  __TEXT.__cstring: 0x483
+  __TEXT.__gcc_except_tab: 0x440
   __TEXT.__oslogstring: 0x44
   __TEXT.__swift5_typeref: 0x2c
   __TEXT.__constg_swiftt: 0x88

   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x658
+  __TEXT.__unwind_info: 0x768
   __TEXT.__eh_frame: 0x40
-  __TEXT.__objc_classname: 0x4ba
-  __TEXT.__objc_methname: 0x5b79
-  __TEXT.__objc_methtype: 0x133d
-  __TEXT.__objc_stubs: 0x4260
-  __DATA_CONST.__got: 0x318
-  __DATA_CONST.__const: 0x4e8
+  __TEXT.__objc_classname: 0x52a
+  __TEXT.__objc_methname: 0x5c62
+  __TEXT.__objc_methtype: 0x1368
+  __TEXT.__objc_stubs: 0x4300
+  __DATA_CONST.__got: 0x310
+  __DATA_CONST.__const: 0x4e0
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1600
+  __DATA_CONST.__objc_selrefs: 0x1618
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x3a8
+  __AUTH_CONST.__auth_got: 0x378
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x440
-  __AUTH_CONST.__objc_const: 0x3c70
+  __AUTH_CONST.__objc_const: 0x3c80
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x668

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 07F63E39-D122-37EB-B682-47F2FBA66673
-  Functions: 573
-  Symbols:   2414
-  CStrings:  1314
+  UUID: F18142E0-9557-34C0-BBDC-BC7BCB3FBD23
+  Functions: 577
+  Symbols:   2421
+  CStrings:  1312
 
Symbols:
+ -[SVPlaybackCoordinator seekLive]
+ -[SVVideoPlayerViewController isMuted]
+ -[SVVideoPlayerViewController playWithButtonTapped:muted:]
+ -[SVVideoPlayerViewController playWithButtonTapped:muted:seekLive:]
+ -[SVVideoPlayerViewController setMuted:]
+ GCC_except_table13
+ GCC_except_table20
+ GCC_except_table22
+ GCC_except_table39
+ GCC_except_table42
+ GCC_except_table45
+ GCC_except_table48
+ GCC_except_table51
+ GCC_except_table57
+ ___block_descriptor_48_e8_32s40w_e34_v16?0"<SVVideoVolumeObserving>"8ls32l8w40l8
+ ___block_literal_global.19
+ _objc_msgSend$init
+ _objc_msgSend$playWithButtonTapped:muted:seekLive:
+ _objc_msgSend$seekLive
+ _objc_msgSend$seekToTime:
+ _objc_msgSend$seekableTimeRanges
+ _objc_msgSend$setOverrideUserInterfaceStyle:
+ _objc_msgSend$sv_setPlayerButtonBackground
+ _objc_msgSend$videoPlayerViewController:muteStateDidChangeOfVideo:
- -[SVVideoPlayButton updateBackgroundColor]
- GCC_except_table19
- GCC_except_table21
- GCC_except_table38
- GCC_except_table41
- GCC_except_table44
- GCC_except_table47
- GCC_except_table50
- GCC_except_table9
- _UIAccessibilityIsReduceTransparencyEnabled
- ___block_descriptor_40_e8_32s_e34_v16?0"<SVVideoVolumeObserving>"8ls32l8
- ___block_literal_global.21
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftAccelerate_$_SilexVideo
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$backgroundColor
- _objc_msgSend$colorWithAlphaComponent:
- _objc_msgSend$sv_setPlayButtonBackgroundWithFallback:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x22
CStrings:
+ "/Library/Caches/com.apple.xbs/64DD935D-D224-4135-8630-EE6E7194BD2F/TemporaryDirectory.7n6nAy/Sources/FeldsparServicesUI/Modules/silex/SilexVideo/Playback/Layer/SVPlayerLayer.m"
+ "B20@0:8B16"
+ "TB,N,GisMuted"
+ "playWithButtonTapped:muted:"
+ "playWithButtonTapped:muted:seekLive:"
+ "seekLive"
+ "seekToTime:"
+ "seekableTimeRanges"
+ "sv_setPlayerButtonBackground"
+ "v24@0:8B16B20"
+ "v28@0:8B16B20B24"
+ "videoPlayerViewController:muteStateDidChangeOfVideo:"
- "/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/SilexVideo/Playback/Layer/SVPlayerLayer.m"
- "backgroundColor"
- "colorWithAlphaComponent:"
- "sv_setPlayButtonBackgroundWithFallback:"
- "updateBackgroundColor"

```
