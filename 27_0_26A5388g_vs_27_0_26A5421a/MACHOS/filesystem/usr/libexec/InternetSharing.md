## InternetSharing

> `/usr/libexec/InternetSharing`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-399.0.0.0.0
-  __TEXT.__text: 0x1bf58
+401.0.0.0.0
+  __TEXT.__text: 0x1c058
   __TEXT.__auth_stubs: 0x10c0
   __TEXT.__const: 0x150
   __TEXT.__cstring: 0x8044
   __TEXT.__oslogstring: 0x1e
-  __TEXT.__unwind_info: 0x3f0
+  __TEXT.__unwind_info: 0x3f8
   __DATA_CONST.__const: 0x510
   __DATA_CONST.__cfstring: 0x8e0
   __DATA_CONST.__auth_got: 0x860

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libmrc.dylib
-  Functions: 341
+  Functions: 342
   Symbols:   364
   CStrings:  1138
 
```
