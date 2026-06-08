## ZoomTouch

> `/System/Library/SpringBoardPlugins/ZoomTouch.bundle/ZoomTouch`

```diff

-880.3.0.0.0
-  __TEXT.__text: 0x382c
-  __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_stubs: 0xd80
+899.0.0.0.0
+  __TEXT.__text: 0x406c
+  __TEXT.__auth_stubs: 0x490
+  __TEXT.__objc_stubs: 0xda0
   __TEXT.__objc_methlist: 0x434
-  __TEXT.__const: 0x128
+  __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__cstring: 0x386
-  __TEXT.__objc_methname: 0x107a
-  __TEXT.__objc_classname: 0x6c
+  __TEXT.__cstring: 0x38f
+  __TEXT.__objc_methname: 0x108a
+  __TEXT.__objc_classname: 0x63
   __TEXT.__objc_methtype: 0x1c9
   __TEXT.__unwind_info: 0x1d8
-  __DATA_CONST.__auth_got: 0x220
-  __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x230
   __DATA_CONST.__cfstring: 0x560
   __DATA_CONST.__objc_classlist: 0x18

   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0x100
   __DATA.__objc_const: 0x738
-  __DATA.__objc_selrefs: 0x4f8
+  __DATA.__objc_selrefs: 0x500
   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0xe0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2F54DB30-BEC3-384A-9002-D5AA510D0161
-  Functions: 111
-  Symbols:   425
-  CStrings:  332
+  UUID: 7BB1A59C-1601-36E2-AEE9-C6FF0F0556D2
+  Functions: 109
+  Symbols:   431
+  CStrings:  333
 
Symbols:
+ GCC_except_table22
+ GCC_except_table38
+ GCC_except_table41
+ _ZOTIndexOfDelegateInPointerArray
+ __block_literal_global.367
+ __block_literal_global.37
+ __block_literal_global.371
+ __block_literal_global.373
+ __block_literal_global.389
+ __block_literal_global.58
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$pointerAtIndex:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x8
- GCC_except_table10
- GCC_except_table13
- GCC_except_table28
- ZOTGutterDistance.cold.1
- ZOTMainScreenScaleFactor.cold.1
- ZOTNotGutterFrame.cold.1
- __block_literal_global.346
- __block_literal_global.350
- __block_literal_global.352
- __block_literal_global.368
- _objc_retainAutoreleasedReturnValue
Functions:
~ +[ZOTWorkspace workspace] : 60 -> 12
~ +[ZOTWorkspace initialize] : 80 -> 64
~ -[ZOTWorkspace _runThread] : 252 -> 240
~ +[ZOTWorkspace enableZoom] : 120 -> 116
~ +[ZOTWorkspace disableZoom] : 76 -> 72
~ -[ZOTWorkspace init] : 424 -> 476
~ -[ZOTWorkspace _registerForZoomConflict] : 112 -> 108
~ -[ZOTWorkspace zoomConflictRegistered:] : 160 -> 208
~ -[ZOTWorkspace _conflictAlert:] : 308 -> 300
~ -[ZOTWorkspace tripleClickAlertDidDismissWithButtonIndex:] : 296 -> 272
~ -[ZOTWorkspace conflictAlertDidDismissWithButtonIndex:] : 880 -> 844
~ -[ZOTWorkspace _zoomConflictRegistered:] : 332 -> 308
~ __appTransitionOccurred : 136 -> 132
~ -[ZOTWorkspace _setCaptureEvents:] : 204 -> 192
~ ___34-[ZOTWorkspace _setCaptureEvents:]_block_invoke : 320 -> 312
~ -[ZOTWorkspace _voiceOverEnabled] : 128 -> 124
~ -[ZOTWorkspace _delayedHandleApplicationActivated] : 108 -> 104
~ -[ZOTWorkspace _updateDeviceOrientationOffMainThread] : 4 -> 20
~ -[ZOTWorkspace _setZoomEnabled:] : 264 -> 256
~ ___32-[ZOTWorkspace _setZoomEnabled:]_block_invoke : 328 -> 324
~ -[ZOTWorkspace _handleApplicationActivated] : 384 -> 364
~ -[ZOTWorkspace _showAppConflictAlertIfNecessary] : 232 -> 212
~ -[ZOTWorkspace setFollowCursorTimer:] : 64 -> 12
~ -[ZOTWorkspace setZoomServices:] : 64 -> 12
~ -[ZOTWorkspace setSpringboardActionHandlerIdentifer:] : 64 -> 12
~ +[ZOTConfiguration configurationManager] : 96 -> 88
~ -[ZOTConfiguration didStartForFirstTime] : 64 -> 60
~ -[ZOTConfiguration valueForKey:] : 172 -> 160
~ -[ZOTConfiguration setValue:forKey:] : 204 -> 200
~ -[ZOTConfiguration setZoomLevel:location:zoomed:forKey:] : 580 -> 556
~ -[ZOTConfiguration zoomLevelForKey:currentLevel:] : 296 -> 280
~ -[ZOTConfiguration zoomLocationForKey:currentLocation:] : 432 -> 404
~ -[ZOTConfiguration zoomedForKey:] : 204 -> 188
~ -[ZOTConfiguration perApplicationZoomLevelEnabled] : 84 -> 80
~ _LocString : 140 -> 132
~ _ZOTTimeSinceBoot : 76 -> 216
~ _ZOTMainScreenScaleFactor : 120 -> 136
~ ___ZOTUpdateDeviceOrientation_block_invoke : 76 -> 72
~ _ZOTEventMeetsOrbThreshold : 220 -> 200
~ _ZOTEventRealFingerCount : 288 -> 292
+ _ZOTIndexOfDelegateInPointerArray
~ _ZOTDispatchEventThreadWithDelay : 248 -> 256
~ _ZOTConvertVectorToScreenStandard : 140 -> 172
~ _ZOTAlignDistanceAlongAngle : 224 -> 336
~ _ZOTCalculateDistanceForAngle : 140 -> 680
~ _ZOTNormalizeVelocity : 56 -> 68
~ _ZOTDistanceForTimeAndVelocityWithMaxDistance : 280 -> 288
~ _ZOTGutterDistance : 76 -> 92
~ ___ZOTGutterDistance_block_invoke : 84 -> 192
~ _ZOTNotGutterFrame : 80 -> 96
~ ___ZOTNotGutterFrame_block_invoke : 96 -> 160
~ _ZOTShouldStartAutopan : 672 -> 1756
~ _ZOTScreenRegionForPoint : 184 -> 456
~ _ZOTScreenRegionForRelativePushPan : 668 -> 744
~ +[ZOTSystemInterface initialize] : 132 -> 124
~ ___32+[ZOTSystemInterface initialize]_block_invoke : 332 -> 328
~ ___32+[ZOTSystemInterface initialize]_block_invoke_2 : 88 -> 84
~ +[ZOTSystemInterface sendUserEventOccurred] : 76 -> 72
CStrings:
+ "pointerAtIndex:"

```
