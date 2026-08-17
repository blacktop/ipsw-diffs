## proxy

> `System/Library/OpenDirectory/Modules/proxy.bundle/Contents/MacOS/proxy`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`

```diff

-28.0.0.0.0
-  __TEXT.__text: 0x2080
+28.0.0.700.1
+  __TEXT.__text: 0x20ec
   __TEXT.__auth_stubs: 0x500
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x2ae
+  __TEXT.__const: 0x68
+  __TEXT.__cstring: 0x2f4
   __TEXT.__unwind_info: 0xf8
   __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x238
-  __DATA_CONST.__cfstring: 0x1e0
+  __DATA_CONST.__const: 0x218
+  __DATA_CONST.__cfstring: 0x200
   __DATA.__data: 0x98
   __DATA.__bss: 0x21
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   Functions: 51
   Symbols:   125
-  CStrings:  40
+  CStrings:  41
 
Functions:
~ sub_1fe0 : 208 -> 252
~ sub_22b0 -> sub_22dc : 232 -> 296
CStrings:
+ "Dropping proxy reply for request %lld not bound to this proxy session"
```
