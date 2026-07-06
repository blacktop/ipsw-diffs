## uarphidd

> `/usr/libexec/uarphidd`

```diff

-  __TEXT.__text: 0x47c8
+  __TEXT.__text: 0x4844
   __TEXT.__auth_stubs: 0x560
   __TEXT.__objc_stubs: 0xb20
   __TEXT.__objc_methlist: 0x39c
   __TEXT.__const: 0x50
   __TEXT.__objc_methname: 0xd01
   __TEXT.__cstring: 0x6e2
-  __TEXT.__oslogstring: 0x777
+  __TEXT.__oslogstring: 0x79f
   __TEXT.__objc_classname: 0x6f
   __TEXT.__objc_methtype: 0x253
   __TEXT.__unwind_info: 0x178

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__auth_got: 0x2b8
-  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__got: 0xc0
   __DATA.__objc_const: 0x978
   __DATA.__objc_selrefs: 0x370
   __DATA.__objc_ivar: 0xbc

   - /usr/lib/libobjc.A.dylib
   Functions: 136
   Symbols:   117
-  CStrings:  407
+  CStrings:  408
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Functions:
~ sub_10000351c : 852 -> 976
CStrings:
+ "%s: Failed to create UARP HID Device %@"

```
