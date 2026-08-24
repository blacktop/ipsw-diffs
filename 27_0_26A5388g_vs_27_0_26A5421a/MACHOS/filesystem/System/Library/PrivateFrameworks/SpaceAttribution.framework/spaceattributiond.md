## spaceattributiond

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/spaceattributiond`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-493.0.0.0.0
-  __TEXT.__text: 0x42264
+496.0.1.0.0
+  __TEXT.__text: 0x421f8
   __TEXT.__auth_stubs: 0x760
   __TEXT.__objc_stubs: 0x72e0
   __TEXT.__objc_methlist: 0x2f38
   __TEXT.__const: 0x228
   __TEXT.__gcc_except_tab: 0x16c4
-  __TEXT.__cstring: 0x349e
-  __TEXT.__oslogstring: 0x523a
+  __TEXT.__cstring: 0x3457
+  __TEXT.__oslogstring: 0x5251
   __TEXT.__objc_classname: 0x2e8
   __TEXT.__objc_methname: 0x87d8
   __TEXT.__objc_methtype: 0x1192
   __TEXT.__unwind_info: 0xeb8
   __DATA_CONST.__const: 0x1aa8
-  __DATA_CONST.__cfstring: 0x2d00
+  __DATA_CONST.__cfstring: 0x2ce0
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 1500
   Symbols:   192
-  CStrings:  2712
+  CStrings:  2711
 
Functions:
~ sub_100010064 : 512 -> 556
~ sub_10001e5ac -> sub_10001e5d8 : 640 -> 488
CStrings:
+ "%s: Removing %@ - no registered paths remaining"
- "%s: Removing %@ app path"
- "bundleIDs %@ cache size: %llu is greater than existing data size: %llu"
```
