## init_exclavekit

> `/usr/libexec/init_exclavekit`

```diff

-96.100.34.0.0
-  __TEXT.__text: 0x12c
+144.0.0.0.0
+  __TEXT.__text: 0x128
   __TEXT.__auth_stubs: 0x50
   __TEXT.__const: 0x1a
   __TEXT.__swift5_typeref: 0xa
   __TEXT.__cstring: 0x16
   __TEXT.__swift5_entry: 0x8
   __TEXT.__unwind_info: 0x58
+  __DATA_CONST.__const: 0x30
+  __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x28
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x30
-  __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x8
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: C66E0700-C49E-3BEC-84C2-A5E420DC7FD6
+  UUID: 2402E528-1665-34FE-BF25-C3E21189CC9C
   Functions: 2
   Symbols:   16
   CStrings:  1
Symbols:
+ _swift_release_x19
- _swift_release
Functions:
~ sub_100000998 : 216 -> 212

```
