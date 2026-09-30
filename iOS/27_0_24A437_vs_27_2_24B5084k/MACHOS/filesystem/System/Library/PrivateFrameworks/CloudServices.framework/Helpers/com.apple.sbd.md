## com.apple.sbd

> `/System/Library/PrivateFrameworks/CloudServices.framework/Helpers/com.apple.sbd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-747.0.6.0.0
-  __TEXT.__text: 0x4e0f0
+747.40.7.0.0
+  __TEXT.__text: 0x4e0b8
   __TEXT.__auth_stubs: 0x1000
   __TEXT.__objc_stubs: 0x7080
   __TEXT.__objc_methlist: 0x30b8
   __TEXT.__const: 0x150
   __TEXT.__gcc_except_tab: 0x1adc
-  __TEXT.__cstring: 0x43ff
+  __TEXT.__cstring: 0x43fb
   __TEXT.__objc_methname: 0x7bf4
-  __TEXT.__oslogstring: 0x836f
+  __TEXT.__oslogstring: 0x836b
   __TEXT.__objc_classname: 0x757
   __TEXT.__objc_methtype: 0x1176
   __TEXT.__unwind_info: 0x12e8
Functions:
~ sub_100014d24 : 432 -> 384
~ sub_10004bd0c -> sub_10004bcdc : 60 -> 52
CStrings:
+ "attempt to enable backup with non-decimal digits in SMS target"
- "attempt to enable backup with non-decimal digits in SMS target: %@"
```
