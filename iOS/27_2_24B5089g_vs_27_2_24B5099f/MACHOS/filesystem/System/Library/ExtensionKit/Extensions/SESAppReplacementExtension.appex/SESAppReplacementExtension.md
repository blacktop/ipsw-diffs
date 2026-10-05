## SESAppReplacementExtension

> `/System/Library/ExtensionKit/Extensions/SESAppReplacementExtension.appex/SESAppReplacementExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-71.8.0.0.0
-  __TEXT.__text: 0x19a4
-  __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_stubs: 0x160
+71.9.0.0.0
+  __TEXT.__text: 0x1b9c
+  __TEXT.__auth_stubs: 0x3f0
+  __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x13c
   __TEXT.__const: 0xcc
   __TEXT.__swift5_entry: 0x8

   __TEXT.__swift5_fieldmd: 0x20
   __TEXT.__swift5_reflstr: 0xe
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__oslogstring: 0x208
+  __TEXT.__oslogstring: 0x260
   __TEXT.__objc_methtype: 0xfb
   __TEXT.__cstring: 0x3f
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x8
   __TEXT.__objc_classname: 0x6f
-  __TEXT.__objc_methname: 0x21c
+  __TEXT.__objc_methname: 0x227
   __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__auth_got: 0x200
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x60
   __DATA.__objc_const: 0x170
-  __DATA.__objc_selrefs: 0x108
+  __DATA.__objc_selrefs: 0x110
   __DATA.__objc_data: 0xb0
   __DATA.__data: 0x140
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 38
-  Symbols:   70
-  CStrings:  67
+  Symbols:   73
+  CStrings:  69
 
Symbols:
+ _objc_release_x24
+ _objc_release_x26
+ _objc_release_x27
Functions:
~ sub_1000027f0 : 1308 -> 1812
CStrings:
+ "Skipping app extension replacement %{public}s -> %{public}s; nothing to migrate"
+ "entityType"
```
