## spindump

> `/usr/sbin/spindump`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

 448.0.0.0.0
-  __TEXT.__text: 0xb9eb4
+  __TEXT.__text: 0xb9ef4
   __TEXT.__auth_stubs: 0x13d0
   __TEXT.__objc_stubs: 0x41e0
   __TEXT.__objc_methlist: 0xa04
Functions:
~ sub_10002adfc : 6964 -> 6988
~ sub_100035978 -> sub_100035990 : 5988 -> 6020
~ sub_1000492f0 -> sub_100049328 : 11644 -> 11648
~ sub_100067370 -> sub_1000673ac : 32 -> 44
~ sub_100067390 -> sub_1000673d8 : 44 -> 32
~ sub_1000952b0 -> sub_1000952ec : 33896 -> 33900
```
