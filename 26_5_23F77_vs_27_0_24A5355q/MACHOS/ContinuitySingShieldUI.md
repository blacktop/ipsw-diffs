## ContinuitySingShieldUI

> `/Applications/ContinuitySingShieldUI.app/ContinuitySingShieldUI`

```diff

-665.120.8.0.0
-  __TEXT.__text: 0xb700
-  __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_stubs: 0x2840
-  __TEXT.__objc_methlist: 0xeac
-  __TEXT.__cstring: 0x1842
-  __TEXT.__objc_methname: 0x3710
-  __TEXT.__objc_classname: 0x348
-  __TEXT.__objc_methtype: 0x1138
+748.0.0.122.2
+  __TEXT.__text: 0xae30
+  __TEXT.__auth_stubs: 0x470
+  __TEXT.__objc_stubs: 0x27e0
+  __TEXT.__objc_methlist: 0xec4
+  __TEXT.__cstring: 0x17da
+  __TEXT.__objc_methname: 0x3743
+  __TEXT.__objc_classname: 0x333
+  __TEXT.__objc_methtype: 0x1185
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x2c4
-  __TEXT.__oslogstring: 0xb0b
-  __TEXT.__unwind_info: 0x370
-  __DATA_CONST.__auth_got: 0x240
-  __DATA_CONST.__got: 0x288
+  __TEXT.__oslogstring: 0xab7
+  __TEXT.__unwind_info: 0x348
   __DATA_CONST.__const: 0x3f8
   __DATA_CONST.__cfstring: 0xa20
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA.__objc_const: 0x1718
+  __DATA_CONST.__auth_got: 0x248
+  __DATA_CONST.__got: 0x280
+  __DATA.__objc_const: 0x1730
   __DATA.__objc_selrefs: 0xe78
   __DATA.__objc_ivar: 0xc0
   __DATA.__objc_data: 0x4b0

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/_GroupActivities_UIKit.framework/_GroupActivities_UIKit
+  - /System/Library/Frameworks/_MusicKit_SwiftUI.framework/_MusicKit_SwiftUI
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
-  - /System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore
+  - /System/Library/PrivateFrameworks/CMContinuityCaptureRemote.framework/CMContinuityCaptureRemote
   - /System/Library/PrivateFrameworks/ContinuitySing.framework/ContinuitySing
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/IdleTimerServices.framework/IdleTimerServices

   - /System/Library/PrivateFrameworks/_MusicKitInternal_SwiftUI.framework/_MusicKitInternal_SwiftUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 27CC478F-84E4-3468-9799-3F2326EE5110
-  Functions: 232
+  UUID: A162961C-F4E7-3FE6-B96E-D066CB020ACD
+  Functions: 231
   Symbols:   166
-  CStrings:  999
+  CStrings:  997
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _OBJC_CLASS_$_CSShieldConnectionManager
- __os_feature_enabled_impl
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x26
CStrings:
+ "%s: <%p> Called event:%zu. Ignoring event: %d. supportsCCMultitasking:%d"
+ "-[ContinuityCaptureShieldUIBackgroundPauseManager requestDefaultScreenEvent:]"
+ "Q24@0:8@\"UIWindowScene\"16"
+ "Q24@0:8@16"
+ "handlePauseStateEvent:"
+ "requestDefaultScreenEvent:"
+ "shieldManager:didRequestTeardownShieldWithError:"
+ "shieldManager:didUpdatePresentationError:"
+ "supportedInterfaceOrientationsForWindowScene:"
+ "v32@0:8@\"CSShieldManager\"16@\"NSError\"24"
- "%s: <%p> Called pauseEvent:%zu. Ignoring event: %d. supportsCCMultitasking:%d"
- "%s: <%p> Called resumeEvent:%zu. Ignoring event: %d. supportsCCMultitasking:%d"
- "-[ContinuityCaptureShieldUIBackgroundPauseManager requestDefaultScreenPauseEvent:]"
- "-[ContinuityCaptureShieldUIBackgroundPauseManager requestDefaultScreenResumeEvent:]"
- "Music"
- "atv_sing"
- "atv_sing_quick_setup"
- "pauseSessionForEvent:"
- "requestDefaultScreenPauseEvent:"
- "requestDefaultScreenResumeEvent:"
- "requestGroupSessionURL:"
- "resumeStreamingForEvent:"

```
