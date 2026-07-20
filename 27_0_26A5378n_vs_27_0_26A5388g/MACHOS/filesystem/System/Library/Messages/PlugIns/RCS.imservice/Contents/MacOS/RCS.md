## RCS

> `/System/Library/Messages/PlugIns/RCS.imservice/Contents/MacOS/RCS`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1485.100.12.1.1
-  __TEXT.__text: 0x60528
+1487.100.6.1.2
+  __TEXT.__text: 0x60540
   __TEXT.__auth_stubs: 0x1540
-  __TEXT.__objc_stubs: 0x22a0
+  __TEXT.__objc_stubs: 0x22c0
   __TEXT.__objc_methlist: 0x3f8
   __TEXT.__const: 0x3148
   __TEXT.__objc_classname: 0x3bf
-  __TEXT.__objc_methname: 0x275d
+  __TEXT.__objc_methname: 0x277d
   __TEXT.__objc_methtype: 0x46f
   __TEXT.__constg_swiftt: 0x14a8
   __TEXT.__swift5_typeref: 0x10bb

   __DATA_CONST.__got: 0x538
   __DATA_CONST.__auth_ptr: 0xd80
   __DATA.__objc_const: 0x13a8
-  __DATA.__objc_selrefs: 0xa08
+  __DATA.__objc_selrefs: 0xa10
   __DATA.__objc_data: 0x4e0
   __DATA.__data: 0x2308
   __DATA.__bss: 0x3300

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1855
   Symbols:   279
-  CStrings:  654
+  CStrings:  655
 
Functions:
~ sub_b98c : 3916 -> 3940
CStrings:
+ "isFiltered"
+ "updateSpamModelMetadataWith:wasJunk:isJunk:"
- "setSpamModelMetadata:"
```
