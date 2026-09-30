## mlhostd

> `/usr/libexec/mlhostd`

```diff

-3.2.14.0.0
-  __TEXT.__text: 0x3ddd0
-  __TEXT.__auth_stubs: 0x19b0
+3.2.17.0.0
+  __TEXT.__text: 0x3df20
+  __TEXT.__auth_stubs: 0x19c0
   __TEXT.__objc_methlist: 0x38
   __TEXT.__const: 0xbd4
   __TEXT.__cstring: 0x977b
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x2cc
-  __TEXT.__swift5_typeref: 0x657
+  __TEXT.__swift5_typeref: 0x655
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_reflstr: 0x2b5
   __TEXT.__swift5_fieldmd: 0x2e0

   __TEXT.__swift5_proto: 0x90
   __TEXT.__swift5_types: 0x40
   __TEXT.__objc_methname: 0xb03
-  __TEXT.__oslogstring: 0x1f5a
+  __TEXT.__oslogstring: 0x1faa
   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methtype: 0x342
   __TEXT.__swift5_capture: 0x110
   __TEXT.__unwind_info: 0x700
-  __TEXT.__eh_frame: 0xc98
-  __DATA_CONST.__auth_got: 0xcd8
+  __TEXT.__eh_frame: 0xc90
+  __DATA_CONST.__auth_got: 0xce0
   __DATA_CONST.__got: 0x498
-  __DATA_CONST.__auth_ptr: 0x428
-  __DATA_CONST.__const: 0x4d80
+  __DATA_CONST.__auth_ptr: 0x420
+  __DATA_CONST.__const: 0x4dc0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0xac8
   __DATA.__objc_selrefs: 0x2e8
   __DATA.__objc_data: 0x170
-  __DATA.__data: 0xa58
+  __DATA.__data: 0xa60
   __DATA.__bss: 0x1200
   __DATA.__common: 0x30
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

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
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 546
-  Symbols:   674
-  CStrings:  1531
+  Symbols:   683
+  CStrings:  1532
 
Symbols:
+ _$s20LighthouseBackground11TaskRequestV08asSystemD07requestyxz_tSo08BGSystemcD0CRbzlF
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "Decoded pushed message bundle: %!s(MISSING)"
+ "Task should use new style taskDefinition with taskRequest section."
+ "The push message body must be a JSON dictionary with key: %!s(MISSING)."
- "The push message body must be a json dictionary with key %!s(MISSING)."
- "decoded pushed message bundle: %!s(MISSING)"

```
