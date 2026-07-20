## DistributedEvaluation

> `/System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

 111.1.0.0.0
-  __TEXT.__text: 0x20058
-  __TEXT.__auth_stubs: 0x870
+  __TEXT.__text: 0x20080
+  __TEXT.__auth_stubs: 0x880
   __TEXT.__objc_methlist: 0x1bc4
   __TEXT.__const: 0x238
   __TEXT.__cstring: 0x2370

   __DATA_CONST.__objc_selrefs: 0x10e8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xd8
-  __AUTH_CONST.__auth_got: 0x450
+  __AUTH_CONST.__auth_got: 0x458
   __AUTH_CONST.__const: 0x2b0
   __AUTH_CONST.__cfstring: 0x2c80
   __AUTH_CONST.__objc_const: 0x35b0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 733
-  Symbols:   1813
+  Symbols:   1814
   CStrings:  1399
 
Symbols:
+ _MGGetProductType
Functions:
~ _DESServiceAvailable : 64 -> 104
```
