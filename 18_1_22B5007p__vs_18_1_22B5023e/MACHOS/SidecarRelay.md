## SidecarRelay

> `/usr/libexec/SidecarRelay`

```diff

-340.0.0.0.0
-  __TEXT.__text: 0x77838
+342.1.2.0.0
+  __TEXT.__text: 0x774b0
   __TEXT.__auth_stubs: 0x1b30
   __TEXT.__objc_stubs: 0x420
   __TEXT.__objc_methlist: 0x69c
   __TEXT.__cstring: 0x3137
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x3f51
+  __TEXT.__const: 0x3f6e
   __TEXT.__constg_swiftt: 0x1f9c
   __TEXT.__swift5_typeref: 0x1b60
   __TEXT.__swift5_builtin: 0xa0

   __TEXT.__swift5_protos: 0x40
   __TEXT.__oslogstring: 0x24f2
   __TEXT.__swift5_capture: 0x97c
-  __TEXT.__info_plist: 0x545
+  __TEXT.__info_plist: 0x549
   __TEXT.__unwind_info: 0x1e58
   __TEXT.__eh_frame: 0x10f0
   __DATA_CONST.__auth_got: 0xda0
   __DATA_CONST.__got: 0x518
-  __DATA_CONST.__auth_ptr: 0x6b0
-  __DATA_CONST.__const: 0x3d50
+  __DATA_CONST.__auth_ptr: 0x6a8
+  __DATA_CONST.__const: 0x3e90
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_protolist: 0xf0

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
-  Functions: 3387
-  Symbols:   747
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 3384
+  Symbols:   755
   CStrings:  918
 
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
+ "342.1.2"
- "340"

```
