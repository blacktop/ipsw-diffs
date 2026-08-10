## tvremoted

> `/usr/libexec/tvremoted`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-627.0.19.0.0
-  __TEXT.__text: 0x110bc
+627.0.28.0.0
+  __TEXT.__text: 0x110d4
   __TEXT.__auth_stubs: 0x510
   __TEXT.__objc_stubs: 0x2620
   __TEXT.__objc_methlist: 0xf44

   __TEXT.__gcc_except_tab: 0x1a4
   __TEXT.__cstring: 0xb5d
   __TEXT.__objc_methname: 0x32b7
-  __TEXT.__oslogstring: 0x26cb
+  __TEXT.__oslogstring: 0x26d7
   __TEXT.__objc_classname: 0x13d
   __TEXT.__objc_methtype: 0xf7a
   __TEXT.__unwind_info: 0x340
Functions:
~ sub_10000ca00 : 936 -> 960
CStrings:
+ "Device disconnected: %@ reason: %ld"
- "Device disconnected: %@"
```
