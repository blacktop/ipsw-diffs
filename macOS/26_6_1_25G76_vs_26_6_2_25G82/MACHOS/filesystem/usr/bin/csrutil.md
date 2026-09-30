## csrutil

> `/usr/bin/csrutil`

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

 85.0.0.0.0
-  __TEXT.__text: 0x17040
+  __TEXT.__text: 0x170a4
   __TEXT.__auth_stubs: 0x810
   __TEXT.__objc_stubs: 0xe60
   __TEXT.__objc_methlist: 0x304

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 614
+  Functions: 613
   Symbols:   175
   CStrings:  649
 
```
