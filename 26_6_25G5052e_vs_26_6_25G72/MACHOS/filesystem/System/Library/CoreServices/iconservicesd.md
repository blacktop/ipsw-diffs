## iconservicesd

> `/System/Library/CoreServices/iconservicesd`

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

-743.5.2.400.0
-  __TEXT.__text: 0x1d60
+743.5.2.401.0
+  __TEXT.__text: 0x1dfc
   __TEXT.__auth_stubs: 0x260
   __TEXT.__objc_stubs: 0x600
   __TEXT.__objc_methlist: 0x1f4
-  __TEXT.__const: 0x28
+  __TEXT.__const: 0x30
   __TEXT.__gcc_except_tab: 0x80
   __TEXT.__cstring: 0x263
-  __TEXT.__oslogstring: 0x333
+  __TEXT.__oslogstring: 0x38a
   __TEXT.__objc_methname: 0x6e0
   __TEXT.__objc_classname: 0x50
   __TEXT.__objc_methtype: 0x21d

   - /usr/lib/libobjc.A.dylib
   Functions: 37
   Symbols:   63
-  CStrings:  162
+  CStrings:  163
 
Functions:
~ sub_10000179c : 520 -> 676
CStrings:
+ "Failed to remove store item at URL: %@ with error: %@"
+ "StoreService.removeAllData complete: removed %lu files, %lu failures at path: %@"
- "Failed to remove item at URL: %@ with error: %@"
```
