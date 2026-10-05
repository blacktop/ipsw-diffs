## sharereportingd

> `/usr/libexec/sharereportingd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_assocty`
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

-104.0.0.0.0
-  __TEXT.__text: 0x415bc
+106.0.0.0.0
+  __TEXT.__text: 0x415b4
   __TEXT.__auth_stubs: 0x14d0
   __TEXT.__objc_stubs: 0x7a0
   __TEXT.__objc_methlist: 0x2e4

   __TEXT.__swift5_typeref: 0xbde
   __TEXT.__swift5_capture: 0x40c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x2485
+  __TEXT.__cstring: 0x2475
   __TEXT.__constg_swiftt: 0xc2c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x8f1
Functions:
~ sub_10000d29c : 1000 -> 992
CStrings:
+ "Failed to fetch share metadata object."
- "More than one share metadata object was fetched."
```
