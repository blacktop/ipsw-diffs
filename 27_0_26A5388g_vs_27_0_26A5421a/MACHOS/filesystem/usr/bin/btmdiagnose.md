## btmdiagnose

> `/usr/bin/btmdiagnose`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-368.0.0.0.0
-  __TEXT.__text: 0x259fc
+371.0.0.0.0
+  __TEXT.__text: 0x25a20
   __TEXT.__auth_stubs: 0xa20
   __TEXT.__objc_stubs: 0x3620
   __TEXT.__objc_methlist: 0x171c

   __TEXT.__gcc_except_tab: 0x418
   __TEXT.__objc_methname: 0x4235
   __TEXT.__cstring: 0x17b3
-  __TEXT.__oslogstring: 0x1dbc
+  __TEXT.__oslogstring: 0x1db6
   __TEXT.__objc_classname: 0x176
   __TEXT.__objc_methtype: 0xfb1
   __TEXT.__swift5_entry: 0x8
Functions:
~ sub_10000ef58 : 1636 -> 1672
CStrings:
+ "%s: no app URL for BTMItem, uuid=%{public}@, item=%@, container=%@"
- "%s: no container URL for BTMItem, uuid=%{public}@, item=%@, container=%@"
```
