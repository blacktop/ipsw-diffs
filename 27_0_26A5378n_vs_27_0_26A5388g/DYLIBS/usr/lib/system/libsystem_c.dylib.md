## libsystem_c.dylib

> `/usr/lib/system/libsystem_c.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__AUTH.__constrw`

```diff

   __AUTH.__data: 0x30
   __AUTH.__constrw: 0x80
   __DATA.__crash_info: 0x148
-  __DATA.__data: 0x61c
+  __DATA.__data: 0x604
   __DATA.__constrw: 0xc88
-  __DATA.__bss: 0xc78
+  __DATA.__bss: 0xc68
   __DATA.__common: 0x88
-  __DATA_DIRTY.__data: 0x1238
-  __DATA_DIRTY.__bss: 0x1ad0
+  __DATA_DIRTY.__data: 0x1250
+  __DATA_DIRTY.__bss: 0x1ad8
   __DATA_DIRTY.__common: 0x9c
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libcorecrypto.dylib
```
