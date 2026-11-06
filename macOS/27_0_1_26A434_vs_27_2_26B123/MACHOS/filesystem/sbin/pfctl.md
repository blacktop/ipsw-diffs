## pfctl

> `/sbin/pfctl`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-118.0.0.0.0
-  __TEXT.__text: 0x20ec4
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__cstring: 0x5ed0
+120.40.2.0.0
+  __TEXT.__text: 0x2139c
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__cstring: 0x5f1f
   __TEXT.__const: 0x25cc
   __TEXT.__unwind_info: 0x6e8
   __DATA_CONST.__const: 0x15e0
-  __DATA_CONST.__auth_got: 0x2f0
+  __DATA_CONST.__auth_got: 0x300
   __DATA_CONST.__got: 0x40
-  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__auth_ptr: 0x18
   __DATA.__data: 0xbac
   __DATA.__bss: 0xcc
   __DATA.__common: 0xc8c
   - /usr/lib/libSystem.B.dylib
   Functions: 415
-  Symbols:   105
-  CStrings:  1365
+  Symbols:   107
+  CStrings:  1368
 
Symbols:
+ ___memcpy_chk
+ _reallocf
Functions:
~ sub_100011a38 : 1328 -> 2520
~ sub_10001468c -> sub_100014b34 : 3400 -> 3448
CStrings:
+ "%s: max anchor stack depth exceeded for %s"
+ "anchor \"%s\" all {\n"
+ "pfctl_show_rules"
```
