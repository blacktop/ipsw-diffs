## kernelmanagerd

> `/usr/libexec/kernelmanagerd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-514.0.2.0.0
-  __TEXT.__text: 0x133760
+514.40.8.0.0
+  __TEXT.__text: 0x133770
   __TEXT.__auth_stubs: 0x3370
   __TEXT.__objc_stubs: 0x1600
   __TEXT.__objc_methlist: 0x8e8
Functions:
~ sub_100085598 : 784 -> 792
~ sub_100085ae0 -> sub_100085ae8 : 588 -> 596
CStrings:
+ "KernelManagement_executables-514.40.8"
- "KernelManagement_executables-514.0.2"
```
