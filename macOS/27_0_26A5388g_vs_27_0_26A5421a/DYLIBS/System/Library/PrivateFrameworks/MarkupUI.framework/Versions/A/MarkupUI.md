## MarkupUI

> `/System/Library/PrivateFrameworks/MarkupUI.framework/Versions/A/MarkupUI`

```diff

-581.0.0.0.0
-  __TEXT.__text: 0x1870c
+582.0.0.0.0
+  __TEXT.__text: 0x1875c
   __TEXT.__objc_methlist: 0x206c
   __TEXT.__const: 0xd8
   __TEXT.__gcc_except_tab: 0x3a0
-  __TEXT.__cstring: 0x1ef8
+  __TEXT.__cstring: 0x1fac
   __TEXT.__ustring: 0x1b8
   __TEXT.__dlopen_cstrs: 0xb6
   __TEXT.__unwind_info: 0x658

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__got: 0x590
   __AUTH_CONST.__const: 0x430
-  __AUTH_CONST.__cfstring: 0x1d60
+  __AUTH_CONST.__cfstring: 0x1da0
   __AUTH_CONST.__objc_const: 0x27e8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x18

   - /usr/lib/libobjc.A.dylib
   Functions: 528
   Symbols:   1993
-  CStrings:  303
+  CStrings:  305
 
Functions:
~ -[MUPayloadEncryption decryptData:] : 400 -> 480
CStrings:
+ "MUPayloadEncryption: %lu bytes is not a valid encrypted payload length. Returning nil."
+ "MUPayloadEncryption: decrypted %lu bytes, too few to contain the salt prefix. Returning nil."
```
