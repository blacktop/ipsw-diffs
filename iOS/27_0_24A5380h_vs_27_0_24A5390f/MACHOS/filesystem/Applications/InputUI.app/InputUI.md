## InputUI

> `/Applications/InputUI.app/InputUI`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-111.0.0.0.0
+114.0.0.0.0
   __TEXT.__text: 0xbff4
   __TEXT.__auth_stubs: 0x600
   __TEXT.__objc_stubs: 0x1f00
-  __TEXT.__objc_methlist: 0x22d4
-  __TEXT.__objc_methname: 0x627f
+  __TEXT.__objc_methlist: 0x2304
+  __TEXT.__objc_methname: 0x62d7
   __TEXT.__cstring: 0x788
   __TEXT.__objc_classname: 0x381
   __TEXT.__objc_methtype: 0x2a4e

   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__auth_got: 0x310
   __DATA_CONST.__got: 0x168
-  __DATA.__objc_const: 0x5678
-  __DATA.__objc_selrefs: 0x1750
+  __DATA.__objc_const: 0x5708
+  __DATA.__objc_selrefs: 0x1770
   __DATA.__objc_ivar: 0x104
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x840

   - /usr/lib/libobjc.A.dylib
   Functions: 341
   Symbols:   163
-  CStrings:  1401
+  CStrings:  1405
 
CStrings:
+ "grammarCheckingType"
+ "preferKeyboardInput"
+ "setGrammarCheckingType:"
+ "setPreferKeyboardInput:"
```
