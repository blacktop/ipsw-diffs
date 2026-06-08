## ContinuityCaptureShieldUI

> `/Applications/ContinuityCaptureShieldUI.app/ContinuityCaptureShieldUI`

```diff

-665.120.8.0.0
-  __TEXT.__text: 0xa30c
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_stubs: 0x24c0
+748.0.0.122.2
+  __TEXT.__text: 0x9b2c
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_stubs: 0x2480
   __TEXT.__objc_methlist: 0xdac
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x264
-  __TEXT.__objc_methname: 0x3352
-  __TEXT.__cstring: 0x16c1
-  __TEXT.__objc_classname: 0x313
-  __TEXT.__objc_methtype: 0x1031
-  __TEXT.__oslogstring: 0x946
-  __TEXT.__unwind_info: 0x308
-  __DATA_CONST.__auth_got: 0x230
-  __DATA_CONST.__got: 0x248
+  __TEXT.__objc_methname: 0x3342
+  __TEXT.__cstring: 0x1679
+  __TEXT.__objc_classname: 0x302
+  __TEXT.__objc_methtype: 0x1056
+  __TEXT.__oslogstring: 0x8f2
+  __TEXT.__unwind_info: 0x2e8
   __DATA_CONST.__const: 0x3a8
   __DATA_CONST.__cfstring: 0xa00
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x48
-  __DATA.__objc_const: 0x15a8
-  __DATA.__objc_selrefs: 0xd78
+  __DATA_CONST.__auth_got: 0x238
+  __DATA_CONST.__got: 0x248
+  __DATA.__objc_const: 0x15b0
+  __DATA.__objc_selrefs: 0xd70
   __DATA.__objc_ivar: 0xb0
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x2a0

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
-  - /System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore
+  - /System/Library/PrivateFrameworks/CMContinuityCaptureRemote.framework/CMContinuityCaptureRemote
   - /System/Library/PrivateFrameworks/ContinuitySing.framework/ContinuitySing
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 11AC537E-71A1-39F9-9609-CE2E7A49078B
-  Functions: 205
-  Symbols:   156
-  CStrings:  933
+  UUID: AC546590-F09B-36C0-B9A0-A1CBAC8A6932
+  Functions: 204
+  Symbols:   157
+  CStrings:  932
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
- _objc_retain_x26
CStrings:
+ "%s: <%p> Called event:%zu. Ignoring event: %d. supportsCCMultitasking:%d"
+ "-[ContinuityCaptureShieldUIBackgroundPauseManager requestDefaultScreenEvent:]"
+ "Q24@0:8@\"UIWindowScene\"16"
+ "Q24@0:8@16"
+ "handlePauseStateEvent:"
+ "requestDefaultScreenEvent:"
+ "supportedInterfaceOrientationsForWindowScene:"
- "%s: <%p> Called pauseEvent:%zu. Ignoring event: %d. supportsCCMultitasking:%d"
- "%s: <%p> Called resumeEvent:%zu. Ignoring event: %d. supportsCCMultitasking:%d"
- "-[ContinuityCaptureShieldUIBackgroundPauseManager requestDefaultScreenPauseEvent:]"
- "-[ContinuityCaptureShieldUIBackgroundPauseManager requestDefaultScreenResumeEvent:]"
- "pauseSessionForEvent:"
- "requestDefaultScreenPauseEvent:"
- "requestDefaultScreenResumeEvent:"
- "resumeStreamingForEvent:"

```
