## ZoomTouch

> `/System/Library/SpringBoardPlugins/ZoomTouch.bundle/ZoomTouch`

```diff

-880.2.0.0.0
-  __TEXT.__text: 0x35f0
-  __TEXT.__auth_stubs: 0x480
+880.3.0.0.0
+  __TEXT.__text: 0x382c
+  __TEXT.__auth_stubs: 0x420
   __TEXT.__objc_stubs: 0xd80
   __TEXT.__objc_methlist: 0x434
   __TEXT.__const: 0x128

   __TEXT.__objc_methname: 0x107a
   __TEXT.__objc_classname: 0x6c
   __TEXT.__objc_methtype: 0x1c9
-  __TEXT.__unwind_info: 0x1c8
-  __DATA_CONST.__auth_got: 0x250
+  __TEXT.__unwind_info: 0x1d8
+  __DATA_CONST.__auth_got: 0x220
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x230
   __DATA_CONST.__cfstring: 0x560

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 05647347-A874-3FED-AED6-246C51A67811
+  UUID: 79783093-9EEB-3CCB-AA14-76AA2189744C
   Functions: 111
-  Symbols:   431
+  Symbols:   425
   CStrings:  332
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x22
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ +[ZOTWorkspace workspace] : 12 -> 60
~ -[ZOTWorkspace _runThread] : 240 -> 252
~ +[ZOTWorkspace enableZoom] : 116 -> 120
~ +[ZOTWorkspace disableZoom] : 72 -> 76
~ -[ZOTWorkspace init] : 420 -> 424
~ -[ZOTWorkspace _registerForZoomConflict] : 108 -> 112
~ -[ZOTWorkspace zoomConflictRegistered:] : 152 -> 160
~ -[ZOTWorkspace _conflictAlert:] : 300 -> 308
~ -[ZOTWorkspace tripleClickAlertDidDismissWithButtonIndex:] : 272 -> 296
~ -[ZOTWorkspace conflictAlertDidDismissWithButtonIndex:] : 844 -> 880
~ -[ZOTWorkspace _zoomConflictRegistered:] : 308 -> 332
~ __appTransitionOccurred : 132 -> 136
~ -[ZOTWorkspace _setCaptureEvents:] : 192 -> 204
~ ___34-[ZOTWorkspace _setCaptureEvents:]_block_invoke : 312 -> 320
~ -[ZOTWorkspace _voiceOverEnabled] : 124 -> 128
~ -[ZOTWorkspace _delayedHandleApplicationActivated] : 104 -> 108
~ -[ZOTWorkspace _setZoomEnabled:] : 256 -> 264
~ ___32-[ZOTWorkspace _setZoomEnabled:]_block_invoke : 324 -> 328
~ -[ZOTWorkspace _handleApplicationActivated] : 364 -> 384
~ -[ZOTWorkspace _showAppConflictAlertIfNecessary] : 212 -> 232
~ -[ZOTWorkspace setFollowCursorTimer:] : 12 -> 64
~ -[ZOTWorkspace setZoomServices:] : 12 -> 64
~ -[ZOTWorkspace setSpringboardActionHandlerIdentifer:] : 12 -> 64
~ +[ZOTConfiguration configurationManager] : 88 -> 96
~ -[ZOTConfiguration didStartForFirstTime] : 60 -> 64
~ -[ZOTConfiguration valueForKey:] : 160 -> 172
~ -[ZOTConfiguration setValue:forKey:] : 200 -> 204
~ -[ZOTConfiguration setZoomLevel:location:zoomed:forKey:] : 556 -> 580
~ -[ZOTConfiguration zoomLevelForKey:currentLevel:] : 280 -> 296
~ -[ZOTConfiguration zoomLocationForKey:currentLocation:] : 420 -> 432
~ -[ZOTConfiguration zoomedForKey:] : 188 -> 204
~ -[ZOTConfiguration perApplicationZoomLevelEnabled] : 80 -> 84
~ _LocString : 132 -> 140
~ _ZOTTimeSinceBoot : 72 -> 76
~ ___ZOTUpdateDeviceOrientation_block_invoke : 72 -> 76
~ _ZOTEventMeetsOrbThreshold : 200 -> 220
~ _ZOTEventRealFingerCount : 280 -> 288
~ _ZOTDispatchEventThreadWithDelay : 256 -> 248
~ +[ZOTSystemInterface initialize] : 124 -> 132
~ ___32+[ZOTSystemInterface initialize]_block_invoke : 328 -> 332
~ ___32+[ZOTSystemInterface initialize]_block_invoke_2 : 84 -> 88
~ +[ZOTSystemInterface sendUserEventOccurred] : 72 -> 76

```
