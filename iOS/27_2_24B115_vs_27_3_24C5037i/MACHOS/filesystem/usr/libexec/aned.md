## aned

> `/usr/libexec/aned`

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

-382.101.2.0.0
-  __TEXT.__text: 0x7c300
+382.102.2.0.0
+  __TEXT.__text: 0x7c30c
   __TEXT.__auth_stubs: 0xf80
   __TEXT.__objc_stubs: 0x3480
   __TEXT.__objc_methlist: 0x117c
Functions:
~ -[_ANEProgramForLoad prepareChainingRequest:qos:qIndex:statsMask:error:] : 2980 -> 2992
```
