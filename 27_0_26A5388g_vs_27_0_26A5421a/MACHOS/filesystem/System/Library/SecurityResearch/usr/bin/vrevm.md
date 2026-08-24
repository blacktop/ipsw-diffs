## vrevm

> `/System/Library/SecurityResearch/usr/bin/vrevm`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__cstring`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-274.0.3.0.0
-  __TEXT.__text: 0x5ce6c
+274.1.3.0.0
+  __TEXT.__text: 0x5ceb0
   __TEXT.__auth_stubs: 0x1bc0
   __TEXT.__objc_stubs: 0xec0
   __TEXT.__objc_methlist: 0x18c
Functions:
~ sub_100018e30 : 1424 -> 1416
~ sub_1000193c0 -> sub_1000193b8 : 1424 -> 1416
~ sub_100019950 -> sub_100019940 : 1444 -> 1436
~ sub_10001a344 -> sub_10001a32c : 1208 -> 1200
~ sub_100020fdc -> sub_100020fbc : 2032 -> 2024
~ sub_1000253dc -> sub_1000253b4 : 404 -> 388
~ sub_10003ade8 -> sub_10003adb0 : 5284 -> 5416
~ sub_10003c28c -> sub_10003c2d8 : 1384 -> 1376
CStrings:
+ "e970bf252f65b7afc2163bc38fa742c92e443bfb47bc19fae694eb1c09535eae"
- "dd1b2a89cf5b230a02dc7534a457454495d562183203ddc0742274e5a1a2fbd3"
```
