## BlackPowderInferenceExtension

> `/System/Library/ExtensionKit/Extensions/BlackPowderInferenceExtension.appex/BlackPowderInferenceExtension`

```diff

-92.6.0.0.0
+104.0.0.0.0
   __TEXT.__text: 0x1b0
   __TEXT.__auth_stubs: 0xa0
   __TEXT.__const: 0xaa

   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x70
+  __DATA_CONST.__const: 0x70
+  __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x50
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x68
-  __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x48
   __DATA.__objc_data: 0x48
   __DATA.__data: 0x48

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A8294FB4-1B7C-3FD4-B03D-9652FBB4965F
+  UUID: 6D2959AB-0C7D-304E-82AD-9713C337872A
   Functions: 7
-  Symbols:   27
+  Symbols:   28
   CStrings:  1
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio

```
