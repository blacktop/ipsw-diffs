## InviteMessageBubbleExtension

> `/System/Applications/Family/InviteMessageBubbleExtension.appex/InviteMessageBubbleExtension`

```diff

-221.1.0.0.0
-  __TEXT.__text: 0x2db70
-  __TEXT.__auth_stubs: 0x11b0
+223.0.0.0.0
+  __TEXT.__text: 0x2d2c0
+  __TEXT.__auth_stubs: 0x1220
   __TEXT.__objc_stubs: 0x40
   __TEXT.__objc_methlist: 0xa4
-  __TEXT.__objc_methname: 0x79b
+  __TEXT.__objc_methname: 0x7ba
   __TEXT.__objc_classname: 0x23
   __TEXT.__objc_methtype: 0x18
   __TEXT.__const: 0xa14
-  __TEXT.__cstring: 0xbcc
+  __TEXT.__cstring: 0xbfc
   __TEXT.__constg_swiftt: 0x59c
-  __TEXT.__swift5_typeref: 0x1890
-  __TEXT.__swift5_reflstr: 0x6e3
-  __TEXT.__swift5_fieldmd: 0x5f0
+  __TEXT.__swift5_typeref: 0x188c
+  __TEXT.__swift5_reflstr: 0x6ff
+  __TEXT.__swift5_fieldmd: 0x5c0
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_capture: 0x228
-  __TEXT.__oslogstring: 0x783
+  __TEXT.__swift5_capture: 0x1e8
+  __TEXT.__oslogstring: 0x803
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_assocty: 0x120
-  __TEXT.__unwind_info: 0x750
-  __TEXT.__eh_frame: 0xbb8
-  __DATA_CONST.__auth_got: 0x8e0
-  __DATA_CONST.__got: 0x2a0
-  __DATA_CONST.__auth_ptr: 0x2f0
-  __DATA_CONST.__const: 0xf78
+  __TEXT.__unwind_info: 0x790
+  __TEXT.__eh_frame: 0xd68
+  __DATA_CONST.__auth_got: 0x918
+  __DATA_CONST.__got: 0x2c0
+  __DATA_CONST.__auth_ptr: 0x2f8
+  __DATA_CONST.__const: 0xf30
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x2c0
-  __DATA.__objc_selrefs: 0x2d0
+  __DATA.__objc_selrefs: 0x2d8
   __DATA.__objc_data: 0x1d0
-  __DATA.__data: 0xab0
+  __DATA.__data: 0xaa8
   __DATA.__common: 0x20
   __DATA.__bss: 0x8a0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
-  - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 536
-  Symbols:   173
-  CStrings:  239
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 537
+  Symbols:   185
+  CStrings:  242
 
Symbols:
+ _FAURLEndpointPendingInviteActionFromMessagesV1
+ _OBJC_CLASS_$_FAURLConfiguration
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ __swift_stdlib_bridgeErrorToNSError
+ _objc_retain_x25
- __swift_FORCE_LOAD_$_swiftMapKit
CStrings:
+ "FAMILY_INVITATION_ACCEPT_BUTTON"
+ "FAMILY_INVITATION_DECLINE_BUTTON"
+ "Failed to retrieve PendingInviteActionFromMessagesV1 from config bag. Falling back to url from messages payload. Error: %!@(MISSING)"
+ "URLForEndpoint:withCompletion:"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"
- "Can't construct Array with count < 0"
- "Swift/Array.swift"

```
