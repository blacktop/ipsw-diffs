## Heimdal

> `/System/Library/PrivateFrameworks/Heimdal.framework/Heimdal`

```diff

-  __TEXT.__text: 0x621f0
+  __TEXT.__text: 0x62220
   __TEXT.__auth_stubs: 0x1980
   __TEXT.__const: 0x10a0
-  __TEXT.__cstring: 0xf298
+  __TEXT.__cstring: 0xf2dc
   __TEXT.__oslogstring: 0xb
   __TEXT.__gcc_except_tab: 0x28
   __TEXT.__unwind_info: 0x1600

   - /usr/lib/libresolv.9.dylib
   Functions: 2510
   Symbols:   1785
-  CStrings:  2362
+  CStrings:  2363
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Functions:
~ _krb5_rd_cred : 1540 -> 1588
CStrings:
+ "KRB-CRED tickets count (%lu) does not match ticket-info count (%lu)"

```
