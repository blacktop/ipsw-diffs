## visioncompaniond

> `/usr/libexec/visioncompaniond`

```diff

-17.100.11.0.1
+17.100.12.0.0
   __TEXT.__text: 0x1228
   __TEXT.__auth_stubs: 0x1d0
   __TEXT.__objc_stubs: 0x40

   __DATA_CONST.__auth_got: 0xf0
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x108
+  __DATA_CONST.__const: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
   __DATA.__data: 0x18

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BB158741-3F78-3426-8C0C-10089CB5EAC3
+  UUID: 1E691A7E-9117-3FA6-8144-562B473B8A45
   Functions: 23
-  Symbols:   54
+  Symbols:   55
   CStrings:  2
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftSpatial

```
