## init_exclavekit

> `/usr/libexec/init_exclavekit`

```diff

-25.0.0.0.0
-  __TEXT.__text: 0xd0
-  __TEXT.__auth_stubs: 0x40
+27.120.10.0.0
+  __TEXT.__text: 0x110
+  __TEXT.__auth_stubs: 0x50
   __TEXT.__const: 0x12
   __TEXT.__swift5_typeref: 0xa
-  __TEXT.__cstring: 0x24
+  __TEXT.__cstring: 0x16
   __TEXT.__swift5_entry: 0x8
   __TEXT.__unwind_info: 0x48
-  __DATA_CONST.__auth_got: 0x20
-  __DATA_CONST.__got: 0x8
+  __DATA_CONST.__auth_got: 0x28
+  __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x8
+  __DATA.__common: 0x8
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
-  UUID: 5F4B5308-CAFA-3F2A-8408-DEAAA6730FB2
+  UUID: 9E96DFC5-A18E-3B8D-ABD5-26A3AE820D5E
   Functions: 2
-  Symbols:   14
+  Symbols:   16
   CStrings:  1
 
Symbols:
+ _$ss5Int32VN
+ _exclaves_boot
CStrings:
+ "exclaves_boot failed:"
- "init_exclavekit - nothing to do yet"

```
