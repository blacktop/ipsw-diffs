## uarphidd

> `/usr/libexec/uarphidd`

```diff

-  __TEXT.__text: 0x511c
+  __TEXT.__text: 0x5198
   __TEXT.__auth_stubs: 0x460
   __TEXT.__objc_stubs: 0xb60
   __TEXT.__objc_methlist: 0x39c
   __TEXT.__const: 0x58
   __TEXT.__objc_methname: 0xd1d
   __TEXT.__cstring: 0x7e5
-  __TEXT.__oslogstring: 0x8ba
+  __TEXT.__oslogstring: 0x8e2
   __TEXT.__objc_classname: 0x6f
   __TEXT.__objc_methtype: 0x253
   __TEXT.__unwind_info: 0x198

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__auth_got: 0x238
-  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__got: 0xc8
   __DATA.__objc_const: 0x978
   __DATA.__objc_selrefs: 0x380
   __DATA.__objc_ivar: 0xbc

   - /usr/lib/libobjc.A.dylib
   Functions: 147
   Symbols:   102
-  CStrings:  428
+  CStrings:  429
 
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
~ sub_100003b08 : 880 -> 1004
CStrings:
+ "%s: Failed to create UARP HID Device %@"

```
