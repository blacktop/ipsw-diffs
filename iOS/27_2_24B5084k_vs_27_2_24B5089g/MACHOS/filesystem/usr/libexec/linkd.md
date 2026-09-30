## linkd

> `/usr/libexec/linkd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-301.1.9.1.101
-  __TEXT.__text: 0xbf0c8
+301.1.10.2.101
+  __TEXT.__text: 0xbf100
   __TEXT.__auth_stubs: 0x2a50
   __TEXT.__objc_stubs: 0x27a0
   __TEXT.__objc_methlist: 0xe0c

   __TEXT.__swift5_types: 0x1cc
   __TEXT.__swift5_capture: 0x3148
   __TEXT.__oslogstring: 0x4e23
-  __TEXT.__cstring: 0x1bb5
+  __TEXT.__cstring: 0x1c15
   __TEXT.__swift_as_entry: 0x590
   __TEXT.__swift_as_ret: 0x55c
   __TEXT.__swift_as_cont: 0x754

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 5602
   Symbols:   1198
-  CStrings:  1229
+  CStrings:  1232
 
Functions:
~ sub_100015940 : 20 -> 32
~ sub_1000b9f64 -> sub_1000b9f70 : 120 -> 164
CStrings:
+ "preConfirmationClientHydration"
+ "preConfirmationEntityHydration"
+ "preConfirmationEntityQuery"
```
