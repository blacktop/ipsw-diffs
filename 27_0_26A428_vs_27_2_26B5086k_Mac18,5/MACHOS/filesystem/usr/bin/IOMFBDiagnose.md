## IOMFBDiagnose

> `/usr/bin/IOMFBDiagnose`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__objc_selrefs`

```diff

-700.50.97.9.0
-  __TEXT.__text: 0x10860
+700.50.103.0.0
+  __TEXT.__text: 0x10838
   __TEXT.__auth_stubs: 0x2b0
   __TEXT.__objc_stubs: 0xe0
   __TEXT.__const: 0xb74
-  __TEXT.__cstring: 0x837b
+  __TEXT.__cstring: 0x8369
   __TEXT.__objc_methname: 0x62
   __TEXT.__unwind_info: 0x250
   __DATA_CONST.__const: 0xd50
-  __DATA_CONST.__cfstring: 0xc00
+  __DATA_CONST.__cfstring: 0xbe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x160
   __DATA_CONST.__got: 0x40

   - /usr/lib/libobjc.A.dylib
   Functions: 121
   Symbols:   56
-  CStrings:  1346
+  CStrings:  1345
 
Functions:
~ sub_10000a6b0 : 1180 -> 1140
CStrings:
+ "\tNo scan plan set, or SWS data not ready"
- "\tNot in normal mode/SWS block disabled"
- "ProxCurrentScanPlan"
```
