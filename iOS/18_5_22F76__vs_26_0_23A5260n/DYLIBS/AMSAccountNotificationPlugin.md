## AMSAccountNotificationPlugin

> `/System/Library/Accounts/Notification/AMSAccountNotificationPlugin.bundle/AMSAccountNotificationPlugin`

```diff

-8.5.11.0.0
-  __TEXT.__text: 0xdc94
-  __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_methlist: 0x58c
-  __TEXT.__const: 0x14e
-  __TEXT.__cstring: 0x9fd
+9.0.54.2.1
+  __TEXT.__text: 0xd94c
+  __TEXT.__auth_stubs: 0x7a0
+  __TEXT.__objc_methlist: 0x57c
+  __TEXT.__const: 0x19a
+  __TEXT.__cstring: 0x9dd
   __TEXT.__gcc_except_tab: 0xec
-  __TEXT.__oslogstring: 0x25ed
+  __TEXT.__oslogstring: 0x2591
   __TEXT.__dlopen_cstrs: 0x1a6
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0xae

   __TEXT.__swift5_types: 0x4
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x20
-  __TEXT.__unwind_info: 0x320
+  __TEXT.__unwind_info: 0x328
   __TEXT.__eh_frame: 0x2a8
   __TEXT.__objc_classname: 0x5f
-  __TEXT.__objc_methname: 0x1e33
+  __TEXT.__objc_methname: 0x1dab
   __TEXT.__objc_methtype: 0x2f6
-  __TEXT.__objc_stubs: 0x1ec0
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x4a0
+  __TEXT.__objc_stubs: 0x1e00
+  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__const: 0x490
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8e8
+  __DATA_CONST.__objc_selrefs: 0x8c0
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x3e8
+  __AUTH_CONST.__auth_got: 0x3e0
   __AUTH_CONST.__const: 0x1b8
   __AUTH_CONST.__cfstring: 0x7a0
   __AUTH_CONST.__objc_const: 0x520

   __AUTH.__objc_data: 0x100
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x10
-  __DATA.__data: 0x138
+  __DATA.__data: 0xf0
   __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
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
-  UUID: 6807DC57-C0E7-3300-BE62-41043EF98E35
-  Functions: 194
-  Symbols:   197
-  CStrings:  618
+  UUID: 99D27CEA-8D89-3569-918F-193186D72F89
+  Functions: 188
+  Symbols:   193
+  CStrings:  610
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _OBJC_CLASS_$_AMSSyncAccountFlagsTask
- __os_feature_enabled_impl
- __swift_FORCE_LOAD_$_swiftCoreMIDI
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
CStrings:
- "%{public}@: [%{public}@] Not syncing account flags. Sync is disabled for this account save."
- "AccountFlagsV2Polus"
- "AppleMediaServices"
- "_processAccountFlagsForAccount:oldAccount:"
- "ams_disableAccountFlagsSync"
- "ams_setDisableAccountFlagsSync:"
- "initWithAccount:bag:"
- "performSync"

```
