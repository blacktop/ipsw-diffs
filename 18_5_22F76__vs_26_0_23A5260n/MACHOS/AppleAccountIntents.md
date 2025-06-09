## AppleAccountIntents

> `/System/Library/ExtensionKit/Extensions/AppleAccountIntents.appex/AppleAccountIntents`

```diff

-520.480.0.0.0
-  __TEXT.__text: 0xe264
-  __TEXT.__auth_stubs: 0x8d0
+540.1.0.0.0
+  __TEXT.__text: 0xe690
+  __TEXT.__auth_stubs: 0x920
   __TEXT.__objc_methlist: 0x14c
-  __TEXT.__const: 0xd2e
-  __TEXT.__cstring: 0x27e8
+  __TEXT.__const: 0xdbe
+  __TEXT.__cstring: 0x29f8
   __TEXT.__swift5_typeref: 0x4d4
-  __TEXT.__swift5_reflstr: 0x2f5
+  __TEXT.__swift5_reflstr: 0x345
   __TEXT.__swift5_assocty: 0x178
   __TEXT.__constg_swiftt: 0x208
-  __TEXT.__swift5_fieldmd: 0x1dc
+  __TEXT.__swift5_fieldmd: 0x20c
   __TEXT.__swift5_proto: 0x9c
   __TEXT.__swift5_types: 0x20
   __TEXT.__swift_as_entry: 0x3c

   __TEXT.__objc_classname: 0x24
   __TEXT.__objc_methtype: 0xe5
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x4a8
-  __TEXT.__eh_frame: 0x2c0
-  __DATA_CONST.__auth_got: 0x468
-  __DATA_CONST.__got: 0x120
+  __TEXT.__unwind_info: 0x488
+  __TEXT.__eh_frame: 0x270
+  __DATA_CONST.__auth_got: 0x490
+  __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x570
-  __DATA_CONST.__const: 0x520
+  __DATA_CONST.__const: 0x560
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0x238
   __DATA.__objc_selrefs: 0x100
   __DATA.__objc_data: 0x1d0
-  __DATA.__data: 0x380
+  __DATA.__data: 0x300
   __DATA.__bss: 0x1450
   __DATA.__common: 0x58
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

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
-  UUID: 649A101F-4971-3179-9049-E7A8BBF354FC
-  Functions: 363
-  Symbols:   115
-  CStrings:  278
+  UUID: 28EFEE32-C689-3C09-96A5-CB641A184917
+  Functions: 362
+  Symbols:   113
+  CStrings:  286
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_release_x1
+ _objc_retain_x1
+ _objc_retain_x26
+ _objc_retain_x9
+ _swift_coroFrameAlloc
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_release_x22
- _objc_retain_x27
- _objc_retain_x8
CStrings:
+ "Custom Email Domain"
+ "Settings → Apple Account → iCloud → Hide My Email"
+ "Settings → Apple Account → iCloud → Mail → Custom Email Domain"
+ "Settings → Apple Account → iCloud → Private Relay"
+ "Sign in with Apple"
+ "prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/INTERNET_PRIVACY"
+ "prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/PRIVATE_EMAIL_MANAGE"
+ "prefs:root=APPLE_ACCOUNT&path=ICLOUD_SERVICE/com.apple.Dataclass.Mail/BYOD_SETTING_SPECIFIER_ID"
+ "prefs:root=APPLE_ACCOUNT&path=SIWA_SERVICE"
- "Settings → Apple Account"

```
