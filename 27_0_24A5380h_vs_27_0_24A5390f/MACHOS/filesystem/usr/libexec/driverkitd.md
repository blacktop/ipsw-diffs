## driverkitd

> `/usr/libexec/driverkitd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`

```diff

-511.0.0.0.0
-  __TEXT.__text: 0xe9650
+514.0.0.0.0
+  __TEXT.__text: 0xe96bc
   __TEXT.__auth_stubs: 0x2480
   __TEXT.__objc_stubs: 0x860
   __TEXT.__objc_methlist: 0x1f8

   __TEXT.__objc_methtype: 0x39a
   __TEXT.__const: 0xf3f5
   __TEXT.__oslogstring: 0x11d9
-  __TEXT.__cstring: 0x8d04
+  __TEXT.__cstring: 0x8ce4
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x40bc
   __TEXT.__swift5_typeref: 0x35f4

   - /usr/lib/swift/libswiftos.dylib
   Functions: 3610
   Symbols:   877
-  CStrings:  1206
+  CStrings:  1205
 
Functions:
~ sub_10006f0a0 : 3204 -> 3212
~ sub_10006fed0 -> sub_10006fed8 : 344 -> 408
~ sub_100072f14 -> sub_100072f5c : 2984 -> 3020
CStrings:
+ "%{public}s is marked as LPN agent but is not a platform dext"
+ "KernelManagement_executables-514"
- "%{public}s is marked as LPN agent but is not a first-party dext"
- "EnableNetworkCapability"
- "KernelManagement_executables-511"
```
