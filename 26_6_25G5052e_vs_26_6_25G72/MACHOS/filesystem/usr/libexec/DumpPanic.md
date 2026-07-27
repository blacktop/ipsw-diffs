## DumpPanic

> `/usr/libexec/DumpPanic`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`

```diff

-6.100.8.0.0
+6.160.2.0.0
   __TEXT.__text: 0x2f748
   __TEXT.__auth_stubs: 0x1050
   __TEXT.__objc_stubs: 0x2240

   __TEXT.__swift5_reflstr: 0x27
   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x7f0
+  __TEXT.__unwind_info: 0x7f8
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__auth_got: 0x838
   __DATA_CONST.__got: 0x268
Functions:
~ sub_100002e7c : 3140 -> 3228
~ sub_10001b44c -> sub_10001b4a4 : 68 -> 20
~ sub_1000208fc -> sub_100020924 : 84 -> 76
~ sub_1000233f0 -> sub_100023410 : 144 -> 112
```
