## Heimdal

> `/System/Library/PrivateFrameworks/Heimdal.framework/Heimdal`

```diff

-  __TEXT.__text: 0x620a4
-  __TEXT.__const: 0x1090
-  __TEXT.__cstring: 0xf299
+  __TEXT.__text: 0x629e0
+  __TEXT.__const: 0x10a0
+  __TEXT.__cstring: 0xf30d
   __TEXT.__oslogstring: 0xb
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__unwind_info: 0x1608
+  __TEXT.__unwind_info: 0x1620
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0

   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x1e70
   __AUTH_CONST.__cfstring: 0xc20
-  __AUTH_CONST.__auth_got: 0xcc0
-  __DATA.__data: 0x2c38
+  __AUTH_CONST.__auth_got: 0xcd0
+  __AUTH.__data: 0x1410
+  __DATA.__data: 0x2c50
   __DATA.__bss: 0x6f1
   __DATA.__common: 0x18
-  __DATA_DIRTY.__data: 0x1320
+  __DATA_DIRTY.__data: 0x90
   __DATA_DIRTY.__bss: 0x48
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
-  Functions: 2504
-  Symbols:   1881
-  CStrings:  2340
+  Functions: 2511
+  Symbols:   1884
+  CStrings:  2345
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
Symbols:
+ _CCDesIsWeakKey
+ _CCDesSetOddParity
+ _krb5_string_to_key_derived
CStrings:
+ "KRB-CRED tickets count (%lu) does not match ticket-info count (%lu)"
+ "des3"
+ "des3-cbc-none"
+ "des3-cbc-sha1"
+ "hmac-sha1-des3"

```
