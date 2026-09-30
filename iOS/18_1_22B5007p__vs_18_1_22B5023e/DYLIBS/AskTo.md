## AskTo

> `/System/Library/PrivateFrameworks/AskTo.framework/AskTo`

```diff

-37.1.0.0.0
-  __TEXT.__text: 0x480c
-  __TEXT.__auth_stubs: 0x770
+40.0.0.0.0
+  __TEXT.__text: 0x36d0
+  __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_methlist: 0x68
   __TEXT.__const: 0x19a
-  __TEXT.__swift5_typeref: 0x165
+  __TEXT.__swift5_typeref: 0x15c
   __TEXT.__swift5_fieldmd: 0x8c
-  __TEXT.__cstring: 0x4b2
+  __TEXT.__cstring: 0x472
   __TEXT.__constg_swiftt: 0xc0
-  __TEXT.__oslogstring: 0x12b
+  __TEXT.__oslogstring: 0x4b
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_reflstr: 0x46
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_capture: 0x54
-  __TEXT.__unwind_info: 0x1f8
-  __TEXT.__eh_frame: 0x3fc
-  __TEXT.__objc_methname: 0x11c
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x50
+  __TEXT.__unwind_info: 0x1d8
+  __TEXT.__eh_frame: 0x364
+  __TEXT.__objc_methname: 0xc8
+  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__const: 0x90
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x78
+  __DATA_CONST.__objc_selrefs: 0x60
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0x3b8
-  __AUTH_CONST.__auth_ptr: 0xc0
+  __AUTH_CONST.__auth_got: 0x328
+  __AUTH_CONST.__auth_ptr: 0xb8
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__objc_const: 0x1a0
   __AUTH.__objc_data: 0xe8
   __AUTH.__data: 0xc0
-  __DATA.__data: 0xe8
+  __DATA.__data: 0xc8
   __DATA.__bss: 0x180
   __DATA.__common: 0x18
-  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AskToCore.framework/AskToCore
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 114
-  Symbols:   106
-  CStrings:  53
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 105
+  Symbols:   104
+  CStrings:  46
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_retain_x28
+ _objc_retain_x8
- _OBJC_CLASS_$_LSApplicationRecord
- ___stack_chk_fail
- ___stack_chk_guard
- __swift_stdlib_bridgeErrorToNSError
- _objc_release_x24
- _objc_release_x25
- _objc_retain_x22
- _objc_retain_x25
- _swift_allocBox
- _swift_beginAccess
- _swift_bridgeObjectRetain_n
CStrings:
+ "Sending question to daemon: %!@(MISSING)"
+ "_send(_:to:destinationsNotSupportingLegacyAskViaMessages:)"
- "Error retrieving LSApplicationRecord for client with bundle ID %!s(MISSING): %!@(MISSING)"
- "ScreenTime question ID was not a valid UUID. Failing send. question.id: %!s(MISSING)"
- "Sending payload to daemon: %!@(MISSING)"
- "_send(_:to:destinationsNotSupportingLegacyAskViaMessages:canSendWithValidDestinations:)"
- "adamIdentifier for client with bundle ID %!s(MISSING) is %!s(MISSING)"
- "com.apple.ScreenTimeAgent"
- "iTunesMetadata"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "storeItemIdentifier"

```
