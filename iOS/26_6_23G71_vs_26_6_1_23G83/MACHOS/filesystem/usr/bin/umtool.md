## umtool

> `/usr/bin/umtool`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

 463.0.0.0.0
-  __TEXT.__text: 0x1596c
+  __TEXT.__text: 0x159d0
   __TEXT.__auth_stubs: 0x4d0
   __TEXT.__objc_stubs: 0x10e0
   __TEXT.__objc_methlist: 0x358

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 502
+  Functions: 501
   Symbols:   109
   CStrings:  568
 
```
