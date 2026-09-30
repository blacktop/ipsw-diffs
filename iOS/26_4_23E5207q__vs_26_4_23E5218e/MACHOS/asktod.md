## asktod

> `/usr/libexec/asktod`

```diff

-67.475.9.0.0
+67.475.10.0.0
   __TEXT.__text: 0x4d0
   __TEXT.__auth_stubs: 0x130
   __TEXT.__objc_stubs: 0x40

   __DATA_CONST.__auth_got: 0xa0
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xe8
+  __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
   __DATA.__data: 0x10

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F9E07F65-8A7E-30E4-8B3D-AD0D067C4D67
+  UUID: 10B4B956-E550-36EE-A4B1-D853B04BD8A4
   Functions: 5
-  Symbols:   53
+  Symbols:   54
   CStrings:  4
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftSpatial

```
