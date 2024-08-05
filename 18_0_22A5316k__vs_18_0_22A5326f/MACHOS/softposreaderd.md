## softposreaderd

> `/usr/libexec/softposreaderd`

```diff

-30.32.3.0.0
-  __TEXT.__text: 0x17f1f0
-  __TEXT.__auth_stubs: 0x2950
+30.33.0.0.0
+  __TEXT.__text: 0x17e828
+  __TEXT.__auth_stubs: 0x2930
   __TEXT.__objc_methlist: 0x610
-  __TEXT.__const: 0xa07c
-  __TEXT.__cstring: 0xe925
-  __TEXT.__swift5_typeref: 0x1b34
-  __TEXT.__oslogstring: 0xb1ec
+  __TEXT.__const: 0xa08c
+  __TEXT.__cstring: 0xe935
+  __TEXT.__swift5_typeref: 0x1b26
   __TEXT.__objc_methname: 0x1e37
+  __TEXT.__oslogstring: 0xb1ac
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x4ce4
+  __TEXT.__constg_swiftt: 0x4cec
   __TEXT.__swift5_proto: 0x95c
   __TEXT.__swift5_types: 0x3a8
   __TEXT.__objc_classname: 0x186
   __TEXT.__objc_methtype: 0xb0c
   __TEXT.__swift5_protos: 0xa8
-  __TEXT.__info_plist: 0x510
-  __TEXT.__unwind_info: 0x3cc8
-  __TEXT.__eh_frame: 0x7c74
-  __DATA_CONST.__auth_got: 0x14a8
+  __TEXT.__info_plist: 0x50e
+  __TEXT.__unwind_info: 0x3cf8
+  __TEXT.__eh_frame: 0x7cb4
+  __DATA_CONST.__auth_got: 0x1498
   __DATA_CONST.__got: 0xa58
-  __DATA_CONST.__auth_ptr: 0xd98
-  __DATA_CONST.__const: 0xa040
+  __DATA_CONST.__auth_ptr: 0xd90
+  __DATA_CONST.__const: 0xa1a8
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_selrefs: 0x9c8
   __DATA.__objc_data: 0x1710
   __DATA.__data: 0x8450
-  __DATA.__common: 0x620
+  __DATA.__common: 0x5f8
   __DATA.__bss: 0xfe10
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5173
-  Symbols:   1138
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 5185
+  Symbols:   1143
   CStrings:  2801
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _$ss4Int8VMn
- _OSAtomicIncrement32
- _OSAtomicIncrement64
CStrings:
+ "Invalid platform: (%!s(MISSING))"
+ "pollingTimeVAS"
- "Invalid platform: NearField not supported (%!u(MISSING))"
- "Invalid platform: unsupported device (%!s(MISSING))"

```
