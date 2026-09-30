## RestorePostProcess

> `/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess`

```diff

-2349.0.31.0.2
+2349.0.42.0.0
   __TEXT.__text: 0x122e8
   __TEXT.__auth_stubs: 0xce0
   __TEXT.__objc_stubs: 0x2060
   __TEXT.__objc_methlist: 0x7a0
-  __TEXT.__const: 0x410
+  __TEXT.__const: 0x400
   __TEXT.__gcc_except_tab: 0x384
   __TEXT.__objc_methname: 0x26e3
   __TEXT.__cstring: 0x3725

   __DATA_CONST.__auth_got: 0x680
   __DATA_CONST.__got: 0x288
   __DATA_CONST.__auth_ptr: 0x128
-  __DATA_CONST.__const: 0x650
+  __DATA_CONST.__const: 0x690
   __DATA_CONST.__cfstring: 0xb40
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x18

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 298
-  Symbols:   275
+  Symbols:   283
   CStrings:  1025
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd

```
