## managedappsd

> `/usr/libexec/managedappsd`

```diff

-43.0.0.0.0
+46.0.0.0.0
   __TEXT.__text: 0x6d8
   __TEXT.__auth_stubs: 0x200
   __TEXT.__const: 0x42

   __DATA_CONST.__auth_got: 0x100
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x58
+  __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
   __DATA.__data: 0x8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E33F9C3A-D6D1-3B04-A110-60BE96864CAA
+  UUID: A370E1FF-EBE4-345E-BA99-D11090604BC6
   Functions: 6
-  Symbols:   47
+  Symbols:   43
   CStrings:  10
 
Symbols:
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3

```
