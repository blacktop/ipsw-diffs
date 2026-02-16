## merchantd

> `/usr/libexec/merchantd`

```diff

-142.1.0.0.0
-  __TEXT.__text: 0x1c8
-  __TEXT.__auth_stubs: 0x150
+144.4.0.0.0
+  __TEXT.__text: 0x1bc
+  __TEXT.__auth_stubs: 0x140
+  __TEXT.__objc_stubs: 0x40
   __TEXT.__const: 0x4a
-  __TEXT.__cstring: 0x7
-  __TEXT.__objc_methname: 0x13
+  __TEXT.__objc_methtype: 0x6
+  __TEXT.__cstring: 0x1
   __TEXT.__swift5_entry: 0x8
+  __TEXT.__objc_methname: 0x13
   __TEXT.__unwind_info: 0x68
   __DATA_CONST.__auth_got: 0xa8
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0x90
+  __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DC402542-7818-3D8C-BFA7-CCC8C7FF779A
+  UUID: 79400341-9C8A-36E9-AF13-A14EB3383252
   Functions: 5
-  Symbols:   38
+  Symbols:   39
   CStrings:  3
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreImage
Functions:
~ sub_100000c00 -> sub_100000ce8 : 280 -> 264
~ sub_100000db0 -> sub_100000e88 : 16 -> 20

```
