## neagent

> `/usr/libexec/neagent`

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
-  __TEXT.__text: 0x1ae4c
+2340.0.0.0.4
+  __TEXT.__text: 0x1af1c
   __TEXT.__auth_stubs: 0x950
   __TEXT.__objc_stubs: 0x25a0
   __TEXT.__objc_methlist: 0x1210
   __TEXT.__const: 0xf0
   __TEXT.__gcc_except_tab: 0x6bc
   __TEXT.__objc_methname: 0x2db5
-  __TEXT.__oslogstring: 0x3ebe
+  __TEXT.__oslogstring: 0x3efa
   __TEXT.__cstring: 0x18d3
   __TEXT.__objc_classname: 0x354
   __TEXT.__objc_methtype: 0xef8

   - /usr/lib/libobjc.A.dylib
   Functions: 362
   Symbols:   218
-  CStrings:  1174
+  CStrings:  1175
 
Functions:
~ sub_10000dc68 : 920 -> 1020
~ sub_10001a204 -> sub_10001a268 : 2404 -> 2512
CStrings:
+ "%@: %s - Filter not started, skipping reporting timer setup"
```
