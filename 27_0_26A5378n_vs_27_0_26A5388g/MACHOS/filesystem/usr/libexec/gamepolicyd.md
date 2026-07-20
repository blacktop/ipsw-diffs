## gamepolicyd

> `/usr/libexec/gamepolicyd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

   __TEXT.__text: 0x70684
   __TEXT.__auth_stubs: 0x27c0
   __TEXT.__objc_stubs: 0x1320
-  __TEXT.__objc_methlist: 0xbd0
+  __TEXT.__objc_methlist: 0xbe8
   __TEXT.__const: 0x2000
   __TEXT.__cstring: 0x15c8
-  __TEXT.__objc_methname: 0x2dcd
+  __TEXT.__objc_methname: 0x2e0d
   __TEXT.__oslogstring: 0x1e6b
   __TEXT.__objc_classname: 0x92c
   __TEXT.__objc_methtype: 0xa43

   __DATA_CONST.__auth_got: 0x13f0
   __DATA_CONST.__got: 0x4f8
   __DATA_CONST.__auth_ptr: 0x478
-  __DATA.__objc_const: 0x34c0
-  __DATA.__objc_selrefs: 0x7c8
+  __DATA.__objc_const: 0x34d0
+  __DATA.__objc_selrefs: 0x7d8
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0xba0
   __DATA.__data: 0x3810

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1517
   Symbols:   881
-  CStrings:  860
+  CStrings:  862
 
CStrings:
+ "getDeviceOrientationMode:"
+ "setDeviceOrientationMode:error:"
```
