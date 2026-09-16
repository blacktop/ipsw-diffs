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

-118.0.0.0.0
+119.1.2.0.0
   __TEXT.__text: 0xbc7c
   __TEXT.__auth_stubs: 0x600
   __TEXT.__objc_stubs: 0x1f00
-  __TEXT.__objc_methlist: 0x231c
-  __TEXT.__objc_methname: 0x631f
+  __TEXT.__objc_methlist: 0x2334
+  __TEXT.__objc_methname: 0x6373
   __TEXT.__cstring: 0x788
   __TEXT.__objc_classname: 0x381
-  __TEXT.__objc_methtype: 0x2a4e
+  __TEXT.__objc_methtype: 0x2a6c
   __TEXT.__const: 0x88
   __TEXT.__oslogstring: 0x138f
   __TEXT.__gcc_except_tab: 0x1b4

   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__auth_got: 0x310
   __DATA_CONST.__got: 0x168
-  __DATA.__objc_const: 0x5728
-  __DATA.__objc_selrefs: 0x1780
+  __DATA.__objc_const: 0x5738
+  __DATA.__objc_selrefs: 0x1790
   __DATA.__objc_ivar: 0x104
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x840

   - /usr/lib/libobjc.A.dylib
   Functions: 341
   Symbols:   163
-  CStrings:  1407
+  CStrings:  1411
 
CStrings:
+ "@\"UIView\"20@0:8B16"
+ "@20@0:8B16"
+ "_hostViewForSelectionHandleWithTrailingHandle:"
+ "_selectedTextRangeWillChangeToRange:"
```
