## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-111.4.5.0.0
-  __TEXT.__text: 0x6aba4
+111.4.6.0.0
+  __TEXT.__text: 0x6b738
   __TEXT.__auth_stubs: 0x1320
-  __TEXT.__objc_methlist: 0x5164
+  __TEXT.__objc_methlist: 0x51b4
   __TEXT.__const: 0x580
-  __TEXT.__cstring: 0x4a17
-  __TEXT.__oslogstring: 0x6703
-  __TEXT.__gcc_except_tab: 0xc94
+  __TEXT.__cstring: 0x4ad7
+  __TEXT.__oslogstring: 0x6853
+  __TEXT.__gcc_except_tab: 0xc98
   __TEXT.__swift5_typeref: 0x1b7
   __TEXT.__constg_swiftt: 0xec
   __TEXT.__swift5_fieldmd: 0x40

   __TEXT.__swift5_capture: 0x98
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x1718
+  __TEXT.__unwind_info: 0x1748
   __TEXT.__eh_frame: 0x358
   __TEXT.__objc_classname: 0xcca
-  __TEXT.__objc_methname: 0xc450
-  __TEXT.__objc_methtype: 0x11ad
-  __TEXT.__objc_stubs: 0x9b80
-  __DATA_CONST.__got: 0x1288
-  __DATA_CONST.__const: 0x1290
+  __TEXT.__objc_methname: 0xc67b
+  __TEXT.__objc_methtype: 0x11bd
+  __TEXT.__objc_stubs: 0x9ca0
+  __DATA_CONST.__got: 0x12a0
+  __DATA_CONST.__const: 0x12b0
   __DATA_CONST.__objc_classlist: 0x340
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a50
+  __DATA_CONST.__objc_selrefs: 0x2a98
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_arraydata: 0x1d0
   __AUTH_CONST.__auth_got: 0x9a0
   __AUTH_CONST.__const: 0xf98
-  __AUTH_CONST.__cfstring: 0x53c0
-  __AUTH_CONST.__objc_const: 0x8ca8
+  __AUTH_CONST.__cfstring: 0x54c0
+  __AUTH_CONST.__objc_const: 0x8d38
   __AUTH_CONST.__objc_intobj: 0xfc0
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH.__objc_data: 0xbe0
   __AUTH.__data: 0xa0
-  __DATA.__objc_ivar: 0x618
+  __DATA.__objc_ivar: 0x624
   __DATA.__data: 0x578
   __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0x1608

   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/Frameworks/Vision.framework/Vision
   - /System/Library/PrivateFrameworks/Anvil.framework/Anvil
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BA00CCD5-DBA1-3B8D-884B-8B03EF77F030
-  Functions: 2289
-  Symbols:   777
-  CStrings:  4196
+  UUID: 26884391-6934-36F1-BE57-C9715FAE03BC
+  Functions: 2298
+  Symbols:   780
+  CStrings:  4233
 
Symbols:
+ _IAPayloadKeyMissingKeyboardIsCustomInputView
+ _IASignalMissingKeyboardDictationDidBegin
+ _OBJC_CLASS_$_VNSession
CStrings:
+ "Cancelled: Custom Input View"
+ "Cancelled: Dictation Started"
+ "DictationStarted"
+ "Event publishing scheduled. Retroactive cancel cutoff: %f"
+ "Ignoring a custom inputView."
+ "IsCustomInputView"
+ "Potential retroactive-cancellation signal made (-) or missed (+) cutoff by: %+.2f. (Missing cutoff by up to %.2f second(s) allowed.)"
+ "Q32@0:8@16^@24"
+ "T@\"NSDate\",&,N,V_detectionEndTimestamp"
+ "T@\"NSDate\",&,N,V_detectionStartTimestamp"
+ "T@\"NSDate\",&,N,V_keyboardRequestedReceivedTimestamp"
+ "T@\"NSDate\",&,N,V_retroactiveCancellationCutoffTime"
+ "T@\"NSDate\",&,N,V_screenshotEndTimestamp"
+ "We're not eligible to start a timer cycle yet."
+ "WritingToolsPanelUp"
+ "_detectionEndTimestamp"
+ "_detectionStartTimestamp"
+ "_keyboardRequestedReceivedTimestamp"
+ "_retroactiveCancellationCutoffTime"
+ "_screenshotEndTimestamp"
+ "detectionEndTimestamp"
+ "detectionStartTimestamp"
+ "globalSession"
+ "kbdProcessLatencyMs"
+ "kbdSignalLatencyMs"
+ "keyboardPresenceDetectionResultForOrientation:screenshotEndTime:"
+ "keyboardRequestedReceivedTimestamp"
+ "publishTimerInfo exists but retroactiveCancellationCutoffTime is nil"
+ "releaseCachedResources"
+ "retroactiveCancellationCutoffTime"
+ "screenshotEndTimestamp"
+ "setDetectionEndTimestamp:"
+ "setDetectionStartTimestamp:"
+ "setKeyboardRequestedReceivedTimestamp:"
+ "setRetroactiveCancellationCutoffTime:"
+ "setScreenshotEndTimestamp:"
- "EarlyExpireDismissTimer"
- "T@\"NSDate\",&,N,V_snapshotEndTimestamp"
- "T@\"NSDate\",&,N,V_snapshotStartTimestamp"
- "_snapshotEndTimestamp"
- "_snapshotStartTimestamp"
- "setSnapshotEndTimestamp:"
- "setSnapshotStartTimestamp:"
- "snapshotEndTimestamp"
- "snapshotStartTimestamp"

```
