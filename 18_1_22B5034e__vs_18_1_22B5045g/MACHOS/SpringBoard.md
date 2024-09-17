## SpringBoard

> `/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard`

```diff

-4501.0.0.0.0
-  __TEXT.__text: 0xcf58
+4502.2.102.0.0
+  __TEXT.__text: 0xd3e8
   __TEXT.__auth_stubs: 0x5e0
   __TEXT.__objc_stubs: 0x1940
   __TEXT.__objc_methlist: 0x4e4
-  __TEXT.__cstring: 0x14de
+  __TEXT.__cstring: 0x158a
   __TEXT.__const: 0x70
   __TEXT.__objc_methname: 0x1945
-  __TEXT.__oslogstring: 0x1136
+  __TEXT.__oslogstring: 0x1193
   __TEXT.__objc_classname: 0x125
   __TEXT.__objc_methtype: 0x329
   __TEXT.__gcc_except_tab: 0x194
-  __TEXT.__unwind_info: 0x238
+  __TEXT.__unwind_info: 0x240
   __DATA_CONST.__auth_got: 0x300
-  __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0x1238
-  __DATA_CONST.__cfstring: 0xd00
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__const: 0x1338
+  __DATA_CONST.__cfstring: 0xce0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x128
-  __DATA.__bss: 0x270
+  __DATA.__bss: 0x2d0
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__bss: 0x590
+  __DATA_DIRTY.__bss: 0x5b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 405
-  Symbols:   346
-  CStrings:  646
+  Functions: 420
+  Symbols:   355
+  CStrings:  654
 
Symbols:
+ _SBLogCameraCaptureLaunchAnimation
+ _SBLogButtonsCapture
+ _SBLogCameraCaptureOverlay
+ _SBLogCameraCaptureSuppression
+ _SBLogCameraCaptureRestriction
+ _SBLogCameraCaptureStudyLogs
+ _SBLogCameraCaptureButtonScanMode
+ _SBLogCameraCaptureLaunch
+ _SBIconUserInterfaceStyleDefault
CStrings:
+ "[performPosterBoardMigration] home screen icon style migration migrating to %!{(MISSING)public}@"
+ "CameraCaptureOverlay"
+ "[performPosterBoardMigration] tint style migration is has occured; will not do again."
+ "[performPosterBoardMigration] checking if tint style migration is necessary..."
+ "Capture"
+ "CameraCaptureRestriction"
+ "CameraCaptureStudyLogs"
+ "CameraCaptureSuppression"
+ "CameraCaptureButtonScanMode"
+ "CameraCaptureLaunchAnimation"
+ "CameraCaptureLaunch"
+ "[performPosterBoardMigration] tint style migration is necessary!"
- "[performPosterBoardMigration] tint color migration is necessary!"
- "accent"
- "[performPosterBoardMigration] checking if tint color migration is necessary..."
- "[performPosterBoardMigration] skipping tint color migration; already performed."

```
