## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-  __TEXT.__text: 0xc9208
+  __TEXT.__text: 0xc925c
   __TEXT.__auth_stubs: 0x1d20
-  __TEXT.__objc_stubs: 0xd400
+  __TEXT.__objc_stubs: 0xd420
   __TEXT.__objc_methlist: 0x29dc
   __TEXT.__const: 0x1040
   __TEXT.__gcc_except_tab: 0xa1f4
   __TEXT.__cstring: 0x33ad
   __TEXT.__oslogstring: 0x17c2b
   __TEXT.__objc_classname: 0x68f
-  __TEXT.__objc_methname: 0x12a9b
+  __TEXT.__objc_methname: 0x12ad7
   __TEXT.__objc_methtype: 0x2ca9
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x74e

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_const: 0x2ee0
-  __DATA.__objc_selrefs: 0x3b08
+  __DATA.__objc_selrefs: 0x3b10
   __DATA.__objc_ivar: 0x1c8
   __DATA.__objc_data: 0x9c8
   __DATA.__data: 0xb68

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1738
   Symbols:   905
-  CStrings:  4677
+  CStrings:  4678
 
Functions:
~ sub_97fc : 160 -> 164
~ sub_79134 -> sub_79138 : 2404 -> 2432
~ sub_79a98 -> sub_79ab8 : 316 -> 324
~ sub_79bd4 -> sub_79bfc : 1232 -> 1264
~ sub_8af24 -> sub_8af6c : 7780 -> 7792
CStrings:
+ "decisioningMetadata"
+ "supportsFaceTimeForSenderOrigin:"
+ "updateSpamModelMetadataWith:wasJunk:isJunk:"
- "setSpamModelMetadata:"
- "supportsFaceTime"
```
