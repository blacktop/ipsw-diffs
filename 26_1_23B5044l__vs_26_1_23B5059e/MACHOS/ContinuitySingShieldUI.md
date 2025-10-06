## ContinuitySingShieldUI

> `/Applications/ContinuitySingShieldUI.app/ContinuitySingShieldUI`

```diff

-664.40.10.122.3
-  __TEXT.__text: 0xa9e0
+664.40.15.122.3
+  __TEXT.__text: 0xade4
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_stubs: 0x2760
-  __TEXT.__objc_methlist: 0xe2c
-  __TEXT.__cstring: 0x1772
-  __TEXT.__objc_methname: 0x3593
-  __TEXT.__objc_classname: 0x32e
-  __TEXT.__objc_methtype: 0x1073
+  __TEXT.__objc_stubs: 0x2840
+  __TEXT.__objc_methlist: 0xeac
+  __TEXT.__cstring: 0x1842
+  __TEXT.__objc_methname: 0x3710
+  __TEXT.__objc_classname: 0x348
+  __TEXT.__objc_methtype: 0x1138
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x2c4
-  __TEXT.__oslogstring: 0xa89
-  __TEXT.__unwind_info: 0x330
+  __TEXT.__oslogstring: 0xb0b
+  __TEXT.__unwind_info: 0x348
   __DATA_CONST.__auth_got: 0x250
-  __DATA_CONST.__got: 0x280
+  __DATA_CONST.__got: 0x288
   __DATA_CONST.__const: 0x3f8
-  __DATA_CONST.__cfstring: 0xa00
+  __DATA_CONST.__cfstring: 0xa20
   __DATA_CONST.__objc_classlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x50
-  __DATA.__objc_const: 0x16b8
-  __DATA.__objc_selrefs: 0xe20
-  __DATA.__objc_ivar: 0xbc
+  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA.__objc_const: 0x1718
+  __DATA.__objc_selrefs: 0xe78
+  __DATA.__objc_ivar: 0xc0
   __DATA.__objc_data: 0x4b0
-  __DATA.__data: 0x2a0
+  __DATA.__data: 0x300
   __DATA.__bss: 0x30
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore
   - /System/Library/PrivateFrameworks/ContinuitySing.framework/ContinuitySing
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/IdleTimerServices.framework/IdleTimerServices
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus

   - /System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 861D7B45-4374-3732-B89F-883FCFABD9D1
-  Functions: 225
-  Symbols:   167
-  CStrings:  975
+  UUID: 1E951852-EF1E-36B3-9232-9128F78ED72A
+  Functions: 231
+  Symbols:   168
+  CStrings:  999
 
Symbols:
+ _OBJC_CLASS_$_ITIdleTimerState
CStrings:
+ "%s: <%p> Created backlight assertion to keep screen on with error: %@"
+ "%s: <%p> Released backlight assertion for screen management"
+ "-[ContinuitySingShieldUIBaseSceneDelegate _holdBacklightAssertion]"
+ "-[ContinuitySingShieldUIBaseSceneDelegate _releaseBacklightAssertion]"
+ "@\"<BSInvalidatable>\""
+ "CSShieldManagerObserver"
+ "ContinuitySingShieldUI - Keep screen on during Continuity Sing session"
+ "_holdBacklightAssertion"
+ "_idleTimerAssertion"
+ "_releaseBacklightAssertion"
+ "_startObservingMicrophoneState"
+ "_stopObservingMicrophoneState"
+ "_updateBacklightAssertion"
+ "isMicStreaming"
+ "newAssertionToDisableIdleTimerForReason:error:"
+ "shieldManager:didReceiveError:"
+ "shieldManager:didUpdateSessionState:"
+ "shieldManagerDidFinishLoading:withPlaybackManager:"
+ "shieldManagerDidReceiveDisconnectRequest:"
+ "v24@0:8@\"CSShieldManager\"16"
+ "v32@0:8@\"CSShieldManager\"16@\"CSErrorDetails\"24"
+ "v32@0:8@\"CSShieldManager\"16@\"CSPlaybackManager\"24"
+ "v32@0:8@\"CSShieldManager\"16@\"CSSingSessionState\"24"

```
