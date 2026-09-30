## libsandbox.1.dylib

> `/usr/lib/libsandbox.1.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`

```diff

-3051.0.30.0.0
+3051.0.42.0.2
   __TEXT.__text: 0x31eb4
-  __TEXT.__const: 0x15501
-  __TEXT.__cstring: 0x1f3a4
+  __TEXT.__const: 0x15611
+  __TEXT.__cstring: 0x1f3e7
   __TEXT.__oslogstring: 0x4f1
   __TEXT.__unwind_info: 0x8c8
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__const: 0x27d0
   __AUTH_CONST.__auth_got: 0x418
   __DATA.__crash_info: 0x148
-  __DATA.__data: 0xe670
+  __DATA.__data: 0xe690
   __DATA_DIRTY.__bss: 0x38
   - /usr/lib/libMatch.1.dylib
   - /usr/lib/libSystem.B.dylib
   Functions: 725
   Symbols:   942
-  CStrings:  5288
+  CStrings:  5290
 
CStrings:
+ "3763840C-43E0-49EA-8647-847EAC83F3BB"
+ "CISP_CMD_CH_LED_STROBE_IVFM_SET"
+ "CISP_CMD_SET_SECURE_ISP_DEBUG_MODE"
- "1E6E9E4D-48D5-4ECF-9960-348479364C5B"
```
