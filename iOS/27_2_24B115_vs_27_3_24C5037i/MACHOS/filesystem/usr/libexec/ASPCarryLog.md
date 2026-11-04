## ASPCarryLog

> `/usr/libexec/ASPCarryLog`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-849.40.17.0.0
-  __TEXT.__text: 0x29d1c
+849.60.3.0.0
+  __TEXT.__text: 0x29fec
   __TEXT.__auth_stubs: 0xbf0
   __TEXT.__objc_stubs: 0x2fa0
   __TEXT.__objc_methlist: 0x14d8
   __TEXT.__gcc_except_tab: 0x4b0
-  __TEXT.__cstring: 0x943a
+  __TEXT.__cstring: 0x9518
   __TEXT.__const: 0x2d4
   __TEXT.__objc_methname: 0x324e
   __TEXT.__oslogstring: 0x1b12

   - /usr/local/lib/libNVMeCTL.dylib
   Functions: 556
   Symbols:   261
-  CStrings:  2642
+  CStrings:  2656
 
Functions:
~ sub_100015c78 : 68968 -> 69688
CStrings:
+ "alignFastValidSectors"
+ "alignRegularValidSectors"
+ "hpBatchDropped"
+ "hpBatchHandoffs"
+ "hpEntriesByRunLen"
+ "hpHotUnits"
+ "hpMulEvictHot"
+ "hpMulInserts"
+ "hpMulLive"
+ "hpOtoInserts"
+ "hpOtoLive"
+ "hpUnits"
+ "hpUnitsByHitAlignFast"
+ "hpUnitsByHitAlignRegular"
```
