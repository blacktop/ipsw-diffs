## TVAppServicesAccountNotificationPlugin

> `/System/Library/Accounts/Notification/TVAppServicesAccountNotificationPlugin.bundle/TVAppServicesAccountNotificationPlugin`

```diff

-65.50.6.0.0
-  __TEXT.__text: 0x6fc
-  __TEXT.__auth_stubs: 0x180
+117.0.0.0.0
+  __TEXT.__text: 0x167c
+  __TEXT.__auth_stubs: 0x310
   __TEXT.__objc_methlist: 0x18c
-  __TEXT.__const: 0xac
+  __TEXT.__const: 0xbc
   __TEXT.__cstring: 0xa2
-  __TEXT.__objc_methname: 0x297
+  __TEXT.__objc_methname: 0x2ae
   __TEXT.__constg_swiftt: 0x48
-  __TEXT.__swift5_typeref: 0x14
+  __TEXT.__swift5_typeref: 0x28
   __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__oslogstring: 0xaf
+  __TEXT.__oslogstring: 0x1ef
   __TEXT.__swift5_types: 0x4
   __TEXT.__objc_classname: 0x26
   __TEXT.__objc_methtype: 0x1f3
-  __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0xc0
-  __DATA_CONST.__got: 0x10
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xd8
+  __TEXT.__unwind_info: 0xb0
+  __DATA_CONST.__auth_got: 0x188
+  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0xb0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA.__objc_const: 0x1a8
-  __DATA.__objc_selrefs: 0x100
+  __DATA.__objc_selrefs: 0x110
   __DATA.__objc_data: 0xb8
-  __DATA.__data: 0xf0
-  __DATA.__bss: 0x20
+  __DATA.__data: 0x100
+  __DATA.__bss: 0x8
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
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
-  UUID: D8FC193D-BE70-3043-B22A-705D249725E5
-  Functions: 8
-  Symbols:   57
-  CStrings:  69
+  UUID: 7B56AAD9-E508-354F-B09B-D77AD486B80B
+  Functions: 22
+  Symbols:   67
+  CStrings:  76
 
Symbols:
+ _ACAccountTypeIdentifieriTunesStore
+ _ACAccountTypeIdentifieriTunesStoreSandbox
+ _OBJC_CLASS_$_NSString
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _bzero
+ _memmove
+ _objc_release_x21
+ _objc_release_x22
+ _objc_retainAutoreleasedReturnValue
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_getObjCClassMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release
+ _swift_setDeallocating
- ___chkstk_darwin
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_release_x26
CStrings:
+ "AccountNotificationPlugin:: account changed - will notify"
+ "AccountNotificationPlugin:: user logged in - will notify"
+ "AccountNotificationPlugin:: user logged out - will notify"
+ "AccountNotificationPlugin:: will not handle account update"
+ "AccountNotificationPlugin:: will not notify account update"
+ "accountType"
+ "identifier"

```
