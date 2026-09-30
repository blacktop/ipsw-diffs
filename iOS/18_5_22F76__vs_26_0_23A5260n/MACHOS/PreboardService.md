## PreboardService

> `/usr/libexec/PreboardService`

```diff

-28.0.0.0.0
-  __TEXT.__text: 0x1cdc
-  __TEXT.__auth_stubs: 0x350
+29.0.0.0.0
+  __TEXT.__text: 0x1d28
+  __TEXT.__auth_stubs: 0x360
   __TEXT.__objc_stubs: 0x2c0
-  __TEXT.__cstring: 0xcb2
+  __TEXT.__cstring: 0xcd9
   __TEXT.__const: 0x30
   __TEXT.__oslogstring: 0xe
-  __TEXT.__gcc_except_tab: 0x2c
+  __TEXT.__gcc_except_tab: 0x38
   __TEXT.__objc_methname: 0x1ae
   __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__auth_got: 0x1c0
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0xd0
-  __DATA_CONST.__cfstring: 0xb40
+  __DATA_CONST.__cfstring: 0xb60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA.__objc_selrefs: 0xb0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 673AD331-F116-3B0C-8CD2-8DEC17F9CBF7
+  UUID: EDB739F9-4EBE-3422-B156-8DB6DC04F791
   Functions: 30
-  Symbols:   77
-  CStrings:  232
+  Symbols:   78
+  CStrings:  234
 
Symbols:
+ _MKBVerifyPasswordWithContext
Functions:
~ sub_100001050 : 2252 -> 2328
CStrings:
+ "failed to verify provided passcode: %d"

```
