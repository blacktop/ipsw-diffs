## kmutil

> `/usr/bin/kmutil`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__cstring`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-514.0.2.0.0
-  __TEXT.__text: 0x151b20
+514.40.8.0.0
+  __TEXT.__text: 0x151b2c
   __TEXT.__auth_stubs: 0x37a0
   __TEXT.__objc_stubs: 0x1200
   __TEXT.__objc_methlist: 0x274
Functions:
~ sub_1000be640 : 10580 -> 10576
~ sub_1000eeb88 -> sub_1000eeb84 : 792 -> 800
~ sub_1000ef10c -> sub_1000ef110 : 608 -> 616
CStrings:
+ "KernelManagement_executables-514.40.8"
+ "kmutil: KernelManagement Utility (KernelManagement_executables-514.40.8)"
- "KernelManagement_executables-514.0.2"
- "kmutil: KernelManagement Utility (KernelManagement_executables-514.0.2)"
```
