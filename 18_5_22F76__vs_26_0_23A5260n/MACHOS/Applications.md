## Applications

> `/System/Library/Assistant/Plugins/Applications.assistantBundle/Applications`

```diff

-115.5.1.0.0
-  __TEXT.__text: 0x107cc
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__objc_stubs: 0x2260
-  __TEXT.__objc_methlist: 0x974
-  __TEXT.__const: 0x96
-  __TEXT.__oslogstring: 0x2684
-  __TEXT.__cstring: 0x203b
+119.0.0.0.0
+  __TEXT.__text: 0x1051c
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_stubs: 0x21c0
+  __TEXT.__objc_methlist: 0x964
+  __TEXT.__const: 0xba
+  __TEXT.__oslogstring: 0x2674
+  __TEXT.__cstring: 0x205b
   __TEXT.__objc_classname: 0x217
-  __TEXT.__objc_methname: 0x1ea5
+  __TEXT.__objc_methname: 0x1e7b
   __TEXT.__objc_methtype: 0x780
-  __TEXT.__gcc_except_tab: 0x180
+  __TEXT.__gcc_except_tab: 0x170
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_typeref: 0x7d
   __TEXT.__swift5_reflstr: 0x14

   __TEXT.__swift5_types: 0x4
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x410
+  __TEXT.__unwind_info: 0x3f0
   __TEXT.__eh_frame: 0x120
-  __DATA_CONST.__auth_got: 0x388
-  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__auth_got: 0x398
+  __DATA_CONST.__got: 0x388
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x5f8
+  __DATA_CONST.__const: 0x580
   __DATA_CONST.__cfstring: 0x11a0
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x3c30
-  __DATA.__objc_selrefs: 0xa98
+  __DATA.__objc_selrefs: 0xa78
   __DATA.__objc_ivar: 0x94
   __DATA.__objc_data: 0x670
-  __DATA.__data: 0x378
+  __DATA.__data: 0x358
   __DATA.__bss: 0x10
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CarPlayServices.framework/CarPlayServices

   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
   - /System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: D37EECA4-6144-3CEF-8043-84FA9FDCC2DA
-  Functions: 347
-  Symbols:   316
-  CStrings:  973
+  UUID: 1CF524D2-3438-3C52-9060-DB68E3DD815A
+  Functions: 342
+  Symbols:   312
+  CStrings:  971
 
Symbols:
+ _AFDeviceSupportsSystemAssistantExperience
+ __os_feature_enabled_impl
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_release_x26
- _AFIsPersistentSiriAvailable
- _OBJC_CLASS_$_AFSyncSnapshot
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "%s com.apple.siri.applications: Setting doNotDismissSiri to YES since SAE is enabled"
+ "SiriUI"
+ "persistent_siri"
- "%s com.apple.siri.applications: Setting doNotDismissSiri to YES since Persistent Siri is available"
- "setAnchor:"
- "setCount:"
- "setKey:"
- "setValidity:"

```
