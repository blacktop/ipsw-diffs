## NewDeviceOutreachExtension

> `/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/PlugIns/NewDeviceOutreachExtension.appex/NewDeviceOutreachExtension`

```diff

-432.0.0.0.0
-  __TEXT.__text: 0x17ac
-  __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_stubs: 0x540
-  __TEXT.__objc_methlist: 0x21c
-  __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0xdc
-  __TEXT.__oslogstring: 0x1c3
-  __TEXT.__cstring: 0x2bf
-  __TEXT.__objc_methname: 0x69b
+464.120.4.502.1
+  __TEXT.__text: 0x2220
+  __TEXT.__auth_stubs: 0x2e0
+  __TEXT.__objc_stubs: 0x600
+  __TEXT.__objc_methlist: 0x234
+  __TEXT.__const: 0x74
+  __TEXT.__gcc_except_tab: 0x1a8
+  __TEXT.__cstring: 0x49c
+  __TEXT.__oslogstring: 0x242
+  __TEXT.__objc_methname: 0x783
   __TEXT.__objc_classname: 0x6d
   __TEXT.__objc_methtype: 0x16f
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x148
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x158
-  __DATA_CONST.__cfstring: 0x1a0
+  __TEXT.__constg_swiftt: 0x28
+  __TEXT.__swift5_typeref: 0x6
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0x108
+  __DATA_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__const: 0x270
+  __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x2b0
-  __DATA.__objc_selrefs: 0x230
+  __DATA.__objc_selrefs: 0x260
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x120
+  __DATA.__bss: 0x8
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/CoreFollowUpUI.framework/CoreFollowUpUI
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/NDOAPI.framework/NDOAPI
   - /System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach
   - /System/Library/PrivateFrameworks/NewDeviceOutreachUI.framework/NewDeviceOutreachUI
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 31
-  Symbols:   67
-  CStrings:  142
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 46
+  Symbols:   89
+  CStrings:  164
 
Symbols:
+ _OBJC_CLASS_$_NDOAMSUIComposition
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_release_x28
+ _objc_retain_x20
+ _objc_retain_x23
+ _swift_once
+ _swift_slowAlloc
CStrings:
+ "%s: Processing new stack follow up item, %@"
+ "%s:Error creating AMS controller: %@"
+ "-[NDOAppleCareLandingViewController processNewStackFollowUpItem:selectedAction:completion:]"
+ "-[NDOAppleCareLandingViewController processNewStackFollowUpItem:selectedAction:completion:]_block_invoke_2"
+ "Failed to open url: %@, with error: %@"
+ "OPEN_PATH"
+ "START_WEB"
+ "boolValue"
+ "com.apple.NewDeviceOutreach"
+ "isNewStackFollowUpItem:"
+ "makeFollowUpAMSViewControllerWithAgent:url:presenter:headers:body:onDismiss:completion:"
+ "ndo-follow-up-accept-action-type"
+ "ndo-follow-up-additional-headers"
+ "ndo-follow-up-additional-payload"
+ "ndo-follow-up-new-stack"
+ "ndo-follow-up-url"
+ "objectForKey:"
+ "openURL:configuration:completionHandler:"
+ "processNewStackFollowUpItem:selectedAction:completion:"
+ "url:%@"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v24@?0@\"UIViewController\"8@\"NSError\"16"

```
