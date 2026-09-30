## libsystem_sanitizers.dylib

> `/usr/lib/system/libsystem_sanitizers.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`

```diff

   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__bss: 0x521
-  __DATA.__common: 0x8
-  __DATA_DIRTY.__data: 0x38
-  __DATA_DIRTY.__bss: 0x38
-  __DATA_DIRTY.__common: 0x18
+  __DATA.__data: 0x38
+  __DATA.__bss: 0x559
+  __DATA.__common: 0x28
   __TPRO_CONST.__data: 0x8
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libmacho.dylib
```
