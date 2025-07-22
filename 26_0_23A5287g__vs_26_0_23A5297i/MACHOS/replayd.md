## replayd

> `/usr/libexec/replayd`

```diff

-650.45.2.0.0
-  __TEXT.__text: 0x60fec
-  __TEXT.__auth_stubs: 0x1080
-  __TEXT.__objc_stubs: 0x8640
-  __TEXT.__objc_methlist: 0x43fc
+650.49.1.0.0
+  __TEXT.__text: 0x61e48
+  __TEXT.__auth_stubs: 0x1090
+  __TEXT.__objc_stubs: 0x87a0
+  __TEXT.__objc_methlist: 0x445c
   __TEXT.__const: 0x1b4
-  __TEXT.__objc_methname: 0xc938
-  __TEXT.__cstring: 0xc753
-  __TEXT.__oslogstring: 0x9440
+  __TEXT.__objc_methname: 0xca5c
+  __TEXT.__cstring: 0xc91b
+  __TEXT.__oslogstring: 0x9688
   __TEXT.__objc_classname: 0x69b
-  __TEXT.__objc_methtype: 0x22b1
-  __TEXT.__gcc_except_tab: 0x7b4
-  __TEXT.__unwind_info: 0x12b8
-  __DATA_CONST.__auth_got: 0x850
-  __DATA_CONST.__got: 0x718
-  __DATA_CONST.__const: 0x1900
-  __DATA_CONST.__cfstring: 0x39e0
+  __TEXT.__objc_methtype: 0x22bb
+  __TEXT.__gcc_except_tab: 0x7c8
+  __TEXT.__unwind_info: 0x12e8
+  __DATA_CONST.__auth_got: 0x858
+  __DATA_CONST.__got: 0x750
+  __DATA_CONST.__const: 0x1928
+  __DATA_CONST.__cfstring: 0x3a20
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xe0

   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_intobj: 0x318
   __DATA_CONST.__objc_doubleobj: 0x30
-  __DATA.__objc_const: 0x9610
-  __DATA.__objc_selrefs: 0x2a60
-  __DATA.__objc_ivar: 0x5b4
+  __DATA.__objc_const: 0x9630
+  __DATA.__objc_selrefs: 0x2ac8
+  __DATA.__objc_ivar: 0x5b8
   __DATA.__objc_data: 0xe60
   __DATA.__data: 0xa98
   __DATA.__bss: 0x1d0

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/ScreenshotServices.framework/ScreenshotServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libCTGreenTeaLogger.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B9B7F37B-A428-3CEC-B7BB-98388B5EC48C
-  Functions: 1966
-  Symbols:   504
-  CStrings:  4496
+  UUID: 74AEBE2D-DC1C-3474-B7A3-506A810A31A5
+  Functions: 1980
+  Symbols:   512
+  CStrings:  4528
 
Symbols:
+ _AVAudioSessionMediaServicesWereResetNotification
+ _CGColorSpaceCreateWithPropertyList
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_TUCall
+ _OBJC_CLASS_$_TUCallCenter
+ _TUCallCenterCallConnectedNotification
+ _TUCallUpgradedToVideoNotification
+ _kIOSurfaceColorSpace
CStrings:
+ " [ERROR] %{public}s:%d Media services reset. Stopping and saving current recording"
+ " [INFO] %{public}s:%d Notifying client, stopped due to media services reset"
+ " [INFO] %{public}s:%d Received a TUCallCenter notification [%@], new call=%@ (isVideo=%@), previous call=%@ (isVideo=%@)"
+ " [INFO] %{public}s:%d Will stop HQLR session due to current call upgrading to video call"
+ " [INFO] %{public}s:%d Will stop HQLR session due to incoming call connected"
+ " [INFO] %{public}s:%d active call: %p"
+ " [INFO] %{public}s:%d using call from notification object"
+ " [INFO] %{public}s:%d using frontmost call"
+ "-[RPHighQualityLocalRecordingSession handleMediaServicesReset:]"
+ "-[RPHighQualityLocalRecordingSession handleMediaServicesReset:]_block_invoke"
+ "-[RPHighQualityLocalRecordingSession handleTUCallCenterNotification:]_block_invoke"
+ "-[RPHighQualityLocalRecordingSession removeCallStatusObservers]"
+ "-[RPHighQualityLocalRecordingSession updateFrontmostAudioOrVideoCall]_block_invoke"
+ "@\"TUCall\""
+ "LOCAL_CAPTURE_FAILED_ALERT_MESSAGE_FORMAT"
+ "LOCAL_CAPTURE_STATUSBAR_TAPPED_ALERT_TITLE"
+ "_activeCall"
+ "addCallStatusObservers"
+ "addMediaServicesResetObserver"
+ "callUUID"
+ "clearFrontmostAudioOrVideoCall"
+ "executeOnMainQueue:"
+ "frontmostAudioOrVideoCall"
+ "handleMediaServicesReset:"
+ "handleTUCallCenterNotification:"
+ "isMainThread"
+ "name"
+ "object"
+ "removeCallStatusObservers"
+ "updateFrontmostAudioOrVideoCall"

```
