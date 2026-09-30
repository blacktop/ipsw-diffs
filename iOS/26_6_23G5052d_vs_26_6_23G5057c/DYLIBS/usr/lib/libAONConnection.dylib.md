## libAONConnection.dylib

> `/usr/lib/libAONConnection.dylib`

```diff

-  __TEXT.__text: 0x7fb4
+  __TEXT.__text: 0x7f78
   __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__const: 0x1a0
-  __TEXT.__cstring: 0x1a7a
+  __TEXT.__const: 0x198
+  __TEXT.__cstring: 0x1a6c
   __TEXT.__gcc_except_tab: 0x164
-  __TEXT.__oslogstring: 0x8de
+  __TEXT.__oslogstring: 0x909
   __TEXT.__unwind_info: 0x230
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x8c

   - /usr/lib/libobjc.A.dylib
   Functions: 122
   Symbols:   386
-  CStrings:  187
+  CStrings:  188
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
Functions:
~ _aon_net_service_init : 2376 -> 2436
~ ___aon_net_service_init_block_invoke_3 : 172 -> 52
CStrings:
+ "callbacks->disconnected_with_error is NULL"

```
