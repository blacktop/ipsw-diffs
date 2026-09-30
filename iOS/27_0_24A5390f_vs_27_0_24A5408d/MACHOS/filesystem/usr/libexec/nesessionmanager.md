## nesessionmanager

> `/usr/libexec/nesessionmanager`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-2331.0.0.0.1
-  __TEXT.__text: 0xb6e3c
+2340.0.0.0.4
+  __TEXT.__text: 0xb6ea0
   __TEXT.__auth_stubs: 0x1e10
   __TEXT.__objc_stubs: 0x8a20
   __TEXT.__objc_methlist: 0x3fc4
   __TEXT.__const: 0x198
   __TEXT.__gcc_except_tab: 0x2394
   __TEXT.__objc_methname: 0x9b2f
-  __TEXT.__oslogstring: 0x1138b
+  __TEXT.__oslogstring: 0x113c7
   __TEXT.__cstring: 0x5a93
   __TEXT.__objc_classname: 0xbc4
   __TEXT.__objc_methtype: 0x2270

   - /usr/lib/libobjc.A.dylib
   Functions: 1960
   Symbols:   711
-  CStrings:  4301
+  CStrings:  4302
 
Functions:
~ sub_1000a6c84 : 920 -> 1020
CStrings:
+ "%@: %s - Filter not started, skipping reporting timer setup"
```
