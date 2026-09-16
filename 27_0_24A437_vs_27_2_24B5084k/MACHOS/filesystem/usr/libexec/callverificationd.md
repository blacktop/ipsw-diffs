## callverificationd

> `/usr/libexec/callverificationd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 10.0.0.0.0
-  __TEXT.__text: 0x12220
+  __TEXT.__text: 0x122a8
   __TEXT.__auth_stubs: 0xe60
-  __TEXT.__objc_stubs: 0x520
+  __TEXT.__objc_stubs: 0x540
   __TEXT.__objc_methlist: 0x2c4
   __TEXT.__const: 0x126c
   __TEXT.__constg_swiftt: 0x3f0

   __TEXT.__swift5_proto: 0x10c
   __TEXT.__swift5_types: 0x68
   __TEXT.__objc_classname: 0x103
-  __TEXT.__objc_methname: 0x87f
+  __TEXT.__objc_methname: 0x899
   __TEXT.__objc_methtype: 0x4f8
   __TEXT.__swift5_capture: 0x1b8
   __TEXT.__oslogstring: 0x52a

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__auth_got: 0x738
-  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x1a0
   __DATA.__objc_const: 0x4f0
-  __DATA.__objc_selrefs: 0x2a0
+  __DATA.__objc_selrefs: 0x2a8
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x7f0
   __DATA.__common: 0x80

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 705
-  Symbols:   363
-  CStrings:  213
+  Functions: 706
+  Symbols:   364
+  CStrings:  214
 
Symbols:
+ _AKSeedBuildHeaderKey
Functions:
~ sub_10000a4a8 : 1104 -> 1208
+ sub_10000c928
CStrings:
+ "shouldHideSeedBuildHeader"
```
