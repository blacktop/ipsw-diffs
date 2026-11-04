## mlhostd

> `/usr/libexec/mlhostd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3.7.24.0.0
-  __TEXT.__text: 0x6ea0c
+3.9.1.0.0
+  __TEXT.__text: 0x6ec98
   __TEXT.__auth_stubs: 0x26b0
   __TEXT.__objc_stubs: 0xd20
   __TEXT.__objc_methlist: 0x290

   __TEXT.__objc_methname: 0x1189
   __TEXT.__objc_methtype: 0x53e
   __TEXT.__cstring: 0x938e
-  __TEXT.__oslogstring: 0x309a
+  __TEXT.__oslogstring: 0x30ea
   __TEXT.__swift5_capture: 0x3cc
   __TEXT.__swift_as_entry: 0x74
   __TEXT.__swift_as_ret: 0x44

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 848
   Symbols:   972
-  CStrings:  1660
+  CStrings:  1661
 
Functions:
~ sub_10002eea0 : 25492 -> 25516
~ sub_100035360 -> sub_100035378 : 5112 -> 5128
~ sub_100036758 -> sub_100036780 : 4876 -> 4884
~ sub_100037b80 -> sub_100037bb0 : 7908 -> 7932
~ sub_10003b914 -> sub_10003b95c : 13816 -> 13840
~ sub_10003ef0c -> sub_10003ef6c : 13344 -> 13368
~ sub_1000450a0 -> sub_100045118 : 552 -> 564
~ sub_100045578 -> sub_1000455fc : 4020 -> 4540
CStrings:
+ "Task %s is on-demand and cannot be retried, marking DAS task as completed."
```
