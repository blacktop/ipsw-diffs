## mds

> `/System/Library/Frameworks/CoreServices.framework/Versions/Current/Frameworks/Metadata.framework/Versions/A/Support/mds`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__objc_classname`
- `__TEXT.__objc_methtype`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__dof_mds`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2459.405.0.0.0
-  __TEXT.__text: 0x1699a4
+2465.1.9.0.0
+  __TEXT.__text: 0x1699f0
   __TEXT.__auth_stubs: 0x3d20
   __TEXT.__objc_stubs: 0xd2c0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x8154
-  __TEXT.__const: 0x5f30
-  __TEXT.__cstring: 0x196da
+  __TEXT.__const: 0x5f20
+  __TEXT.__cstring: 0x196d1
   __TEXT.__objc_methname: 0x1174d
   __TEXT.__objc_classname: 0xcdf
   __TEXT.__objc_methtype: 0x5c56
   __TEXT.__gcc_except_tab: 0x1bb4
-  __TEXT.__oslogstring: 0x13b03
+  __TEXT.__oslogstring: 0x13af2
   __TEXT.__ustring: 0x1f0
   __TEXT.__dof_mds: 0x58d5
-  __TEXT.__unwind_info: 0x7960
+  __TEXT.__unwind_info: 0x7968
   __DATA_CONST.__const: 0x19b48
   __DATA_CONST.__cfstring: 0xf3e0
   __DATA_CONST.__objc_classlist: 0x460

   __DATA.__objc_data: 0x2bc0
   __DATA.__data: 0x3ba0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xb9a0
+  __DATA.__bss: 0xb998
   __DATA.__common: 0x8c54
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libfakelink.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9858
+  Functions: 9860
   Symbols:   1317
-  CStrings:  9361
+  CStrings:  9360
 
CStrings:
+ "Could not activate sandbox profile at '%s'. sandbox_init() error %d: error:%s, home:%s, extra:%s, lib:%s, mail:%s, plugin:%s"
+ "sandbox profile activated time:%g uid:%d profile:%s cache:%s temp:%s home:%s lib:%s M:%s typeExtension:%d bundleId:%s"
- "Could not activate sandbox profile at '%s'. sandbox_init() error %d: error:%s, home:%s, extra:%s, lib:%s, mail:%s, mail2:%s, plugin:%s"
- "_MAIL_V2"
- "sandbox profile activated time:%g uid:%d profile:%s cache:%s temp:%s home:%s lib:%s M:%s MV2:%s typeExtension:%d bundleId:%s"
```
