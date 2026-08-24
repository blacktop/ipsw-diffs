## securityd

> `/usr/sbin/securityd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__dof_security_`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-62460.0.55.0.1
-  __TEXT.__text: 0x6ddb0
+62460.1.2.0.0
+  __TEXT.__text: 0x6e370
   __TEXT.__auth_stubs: 0x19b0
   __TEXT.__objc_stubs: 0x1c0
   __TEXT.__init_offsets: 0x18
   __TEXT.__objc_methlist: 0x20
   __TEXT.__const: 0x25dd
-  __TEXT.__gcc_except_tab: 0x841c
+  __TEXT.__gcc_except_tab: 0x8458
   __TEXT.__cstring: 0x1be5
   __TEXT.__oslogstring: 0x4a86
   __TEXT.__objc_classname: 0x18

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxar.1.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1774
+  Functions: 1776
   Symbols:   487
   CStrings:  838
 
```
