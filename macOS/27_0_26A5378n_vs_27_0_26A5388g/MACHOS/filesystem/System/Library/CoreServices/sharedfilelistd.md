## sharedfilelistd

> `/System/Library/CoreServices/sharedfilelistd`

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

-365.0.0.0.0
-  __TEXT.__text: 0x17f84
+368.0.0.0.0
+  __TEXT.__text: 0x17fc8
   __TEXT.__auth_stubs: 0x730
   __TEXT.__objc_stubs: 0x2ce0
   __TEXT.__objc_methlist: 0x1714

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 578
+  Functions: 579
   Symbols:   250
   CStrings:  1043
 
Functions:
~ sub_10000e6b4 : 1024 -> 68
+ sub_10000e6f8
+ sub_1000188ac
- sub_1000188c8
```
