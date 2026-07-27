## DumpPanicRecoveryOS

> `/usr/libexec/DumpPanicRecoveryOS`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-6.100.8.0.0
-  __TEXT.__text: 0x2a1ac
+6.160.2.0.0
+  __TEXT.__text: 0x2a1ec
   __TEXT.__auth_stubs: 0xbc0
   __TEXT.__objc_stubs: 0x1dc0
   __TEXT.__objc_methlist: 0x5d8
Functions:
~ sub_100003a18 : 3140 -> 3228
~ sub_100019c84 -> sub_100019cdc : 68 -> 20
~ sub_10001b0c4 -> sub_10001b0ec : 12 -> 20
~ sub_10001db70 -> sub_10001dba0 : 144 -> 160
```
