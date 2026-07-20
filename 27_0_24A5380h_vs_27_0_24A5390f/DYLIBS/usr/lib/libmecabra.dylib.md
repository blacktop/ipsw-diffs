## libmecabra.dylib

> `/usr/lib/libmecabra.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__lazy_load_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1151.0.0.0.0
-  __TEXT.__text: 0x26b9f4
+1154.0.0.0.0
+  __TEXT.__text: 0x26b520
   __TEXT.__lazy_helpers: 0xfc
   __TEXT.__objc_methlist: 0x3e4
   __TEXT.__const: 0x3001c
   __TEXT.__dlopen_cstrs: 0x152
-  __TEXT.__cstring: 0x16af0
-  __TEXT.__gcc_except_tab: 0x1a7b0
+  __TEXT.__cstring: 0x16aab
+  __TEXT.__gcc_except_tab: 0x1a790
   __TEXT.__ustring: 0x32ae
   __TEXT.__oslogstring: 0x4a0e
-  __TEXT.__unwind_info: 0xce80
+  __TEXT.__unwind_info: 0xce60
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x16898
+  __DATA_CONST.__const: 0x16860
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8

   __AUTH_CONST.__lazy_load_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x13e0
+  __AUTH_CONST.__auth_got: 0x13f8
   __AUTH.__data: 0x1e0
   __AUTH.__thread_vars: 0x438
   __AUTH.__thread_bss: 0x618

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 11152
-  Symbols:   1094
-  CStrings:  4425
+  Functions: 11145
+  Symbols:   1095
+  CStrings:  4423
 
Symbols:
+ _dispatch_block_cancel
+ _dispatch_block_create
+ _dispatch_block_wait
- _MecabraContextAddStringContext
- _MecabraContextSetRightContextFromString
CStrings:
- "unique_lock::lock: already locked"
- "unique_lock::lock: references null mutex"
```
