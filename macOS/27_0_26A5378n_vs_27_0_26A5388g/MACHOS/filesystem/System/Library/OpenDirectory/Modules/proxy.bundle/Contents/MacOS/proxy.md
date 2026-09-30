## proxy

> `/System/Library/OpenDirectory/Modules/proxy.bundle/Contents/MacOS/proxy`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`

```diff

-30.0.0.0.0
-  __TEXT.__text: 0x232c
+31.0.0.0.0
+  __TEXT.__text: 0x2398
   __TEXT.__auth_stubs: 0x520
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x2ae
+  __TEXT.__cstring: 0x2f4
   __TEXT.__unwind_info: 0x108
-  __DATA_CONST.__const: 0x258
-  __DATA_CONST.__cfstring: 0x1e0
+  __DATA_CONST.__const: 0x238
+  __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__auth_got: 0x290
   __DATA_CONST.__got: 0x68
   __DATA.__data: 0x98

   - /usr/lib/libSystem.B.dylib
   Functions: 53
   Symbols:   127
-  CStrings:  40
+  CStrings:  41
 
Functions:
~ sub_228c : 208 -> 252
~ sub_255c -> sub_2588 : 232 -> 296
CStrings:
+ "Dropping proxy reply for request %lld not bound to this proxy session"
```
