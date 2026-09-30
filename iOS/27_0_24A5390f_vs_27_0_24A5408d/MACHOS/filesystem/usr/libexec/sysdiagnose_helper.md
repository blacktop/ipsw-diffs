## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1598.0.4.0.0
-  __TEXT.__text: 0x2523c
+1598.0.6.0.0
+  __TEXT.__text: 0x252f4
   __TEXT.__auth_stubs: 0xfe0
-  __TEXT.__objc_stubs: 0x17e0
+  __TEXT.__objc_stubs: 0x17c0
   __TEXT.__objc_methlist: 0x5e4
   __TEXT.__const: 0x490
   __TEXT.__gcc_except_tab: 0x7c4
   __TEXT.__oslogstring: 0x2781
-  __TEXT.__cstring: 0x97dd
+  __TEXT.__cstring: 0x9861
   __TEXT.__objc_classname: 0xfc
   __TEXT.__objc_methtype: 0x2a9
-  __TEXT.__objc_methname: 0x1744
+  __TEXT.__objc_methname: 0x1735
   __TEXT.__swift5_typeref: 0x91
   __TEXT.__swift5_capture: 0x30
   __TEXT.__constg_swiftt: 0x64

   __TEXT.__unwind_info: 0x650
   __TEXT.__eh_frame: 0x130
   __DATA_CONST.__const: 0x898
-  __DATA_CONST.__cfstring: 0x1da0
+  __DATA_CONST.__cfstring: 0x1e00
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_arraydata: 0x110
-  __DATA_CONST.__objc_arrayobj: 0x78
+  __DATA_CONST.__objc_arraydata: 0x170
+  __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__auth_got: 0x800
   __DATA_CONST.__got: 0x230
   __DATA_CONST.__auth_ptr: 0xe0
   __DATA.__objc_const: 0x700
-  __DATA.__objc_selrefs: 0x660
+  __DATA.__objc_selrefs: 0x658
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0x290
   __DATA.__data: 0x5c0

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 365
   Symbols:   357
-  CStrings:  2190
+  CStrings:  2194
 
Functions:
~ sub_10000852c : 880 -> 992
~ sub_1000120a8 -> sub_100012118 : 68076 -> 68148
CStrings:
+ "BatteryHealth"
+ "BatteryPacks"
+ "Power source %d health info:\n%@\n"
+ "Power source %u pack %u health info:\n%@\n"
+ "arrayByAddingObjectsFromArray:"
+ "dictionaryWithValuesForKeys:"
+ "gcSlowInlineWritesMigration"
+ "gcSlowInlineWritesTotal"
+ "objectAtIndexedSubscript:"
- "Battery %d health info:\n%@\n"
- "addObjectsFromArray:"
- "arrayWithObjects:"
- "dictionaryWithObjects:forKeys:"
- "objectsForKeys:notFoundMarker:"
```
