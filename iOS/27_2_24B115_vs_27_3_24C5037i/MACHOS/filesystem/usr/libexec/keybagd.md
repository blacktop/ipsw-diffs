## keybagd

> `/usr/libexec/keybagd`

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

-697.40.5.0.0
-  __TEXT.__text: 0x216e0
+697.60.3.0.0
+  __TEXT.__text: 0x21734
   __TEXT.__auth_stubs: 0x1520
   __TEXT.__objc_stubs: 0x1040
   __TEXT.__objc_methlist: 0x814
-  __TEXT.__cstring: 0x9e1b
+  __TEXT.__cstring: 0x9e3e
   __TEXT.__const: 0x1a8
   __TEXT.__gcc_except_tab: 0x464
   __TEXT.__objc_methname: 0x182e

   - /usr/lib/libsqlite3.dylib
   Functions: 702
   Symbols:   411
-  CStrings:  1503
+  CStrings:  1505
 
Functions:
~ sub_100001290 : 788 -> 824
~ sub_100001d20 -> sub_100001d44 : 244 -> 292
CStrings:
+ "created_count"
+ "created_locked_count"
```
