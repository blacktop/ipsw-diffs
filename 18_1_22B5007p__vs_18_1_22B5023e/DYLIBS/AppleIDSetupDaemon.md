## AppleIDSetupDaemon

> `/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/AppleIDSetupDaemon`

```diff

-45.1.0.0.0
-  __TEXT.__text: 0xde10c
+48.1.1.0.0
+  __TEXT.__text: 0xc4d30
   __TEXT.__auth_stubs: 0x21d0
   __TEXT.__objc_methlist: 0x2d0
-  __TEXT.__const: 0x1a50
-  __TEXT.__cstring: 0x16bc
-  __TEXT.__oslogstring: 0x4cb6
-  __TEXT.__constg_swiftt: 0x12e0
-  __TEXT.__swift5_typeref: 0x159a
-  __TEXT.__swift5_reflstr: 0xa24
-  __TEXT.__swift5_fieldmd: 0xad8
+  __TEXT.__const: 0x1ad0
+  __TEXT.__cstring: 0x175c
+  __TEXT.__oslogstring: 0x4cf6
+  __TEXT.__constg_swiftt: 0x13a8
+  __TEXT.__swift5_typeref: 0x1774
+  __TEXT.__swift5_reflstr: 0xa64
+  __TEXT.__swift5_fieldmd: 0xaf4
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_assocty: 0x170
-  __TEXT.__swift5_capture: 0x5b4
-  __TEXT.__swift5_proto: 0x11c
+  __TEXT.__swift5_capture: 0x82c
+  __TEXT.__swift5_proto: 0x120
   __TEXT.__swift5_types: 0xcc
-  __TEXT.__swift5_protos: 0x2c
+  __TEXT.__swift5_protos: 0x30
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x3710
-  __TEXT.__eh_frame: 0xd800
+  __TEXT.__unwind_info: 0x3628
+  __TEXT.__eh_frame: 0xb178
   __TEXT.__objc_classname: 0xe3
   __TEXT.__objc_methname: 0x11cf
   __TEXT.__objc_methtype: 0x7d5
   __TEXT.__objc_stubs: 0xc0
-  __DATA_CONST.__got: 0x9a8
-  __DATA_CONST.__const: 0x2c8
-  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__got: 0x998
+  __DATA_CONST.__const: 0x278
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3b0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x10f0
-  __AUTH_CONST.__auth_ptr: 0x640
-  __AUTH_CONST.__const: 0x1c00
+  __AUTH_CONST.__auth_ptr: 0x6d8
+  __AUTH_CONST.__const: 0x1ec8
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x2f20
+  __AUTH_CONST.__objc_const: 0x3098
   __AUTH.__objc_data: 0x4b8
-  __AUTH.__data: 0x810
+  __AUTH.__data: 0x930
   __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x1c58
-  __DATA.__bss: 0x2000
+  __DATA.__data: 0x1b88
+  __DATA.__bss: 0x1f00
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x138
-  __DATA_DIRTY.__data: 0x540
-  __DATA_DIRTY.__common: 0x20
-  __DATA_DIRTY.__bss: 0x80
+  __DATA_DIRTY.__data: 0x568
+  __DATA_DIRTY.__bss: 0x180
+  __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

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
-  Functions: 2424
-  Symbols:   284
-  CStrings:  783
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 2179
+  Symbols:   298
+  CStrings:  792
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "Cleaning up RepairModel"
+ "Cleaning up RepairService"
+ "Failed to perform magic auth for account with error: %!@(MISSING)"
+ "Ignoring error during auth: %!s(MISSING)"
+ "LocalSetupService caught overall setup skipped"
+ "Model is not available for remote repair, Cancelling"
+ "Received auth report: %!{(MISSING)sensitive}s"
+ "Remote repair is not available. Cannot continue"
+ "Removing the connector before removing RemoteRepairService."
+ "Throwing CommandRouter.Failure.userCancelled"
+ "_TtC18AppleIDSetupDaemon17MachRepairService"
+ "auditReport"
+ "authStreamContinuation"
+ "receive(_:from:)"
+ "requiredEntitlements"
+ "session"
- "Connector is not available to invalidate"
- "Not invalidating connector or throwing HaltingTapError"
- "Pairing was cancelled, invalidating proximity connection if available"
- "Repair flow is ending with %!@(MISSING)"
- "Shutting down repair flow, starting with invalidation of connector"
- "Throwing halting error for cancel or skip"
- "Unablet to convert to a repair or not a cancel error"

```
