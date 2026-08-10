## libsystem_darwin.dylib

> `/usr/lib/system/libsystem_darwin.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__DATA.__data`

```diff

-1786.0.1.0.0
+1786.0.3.0.0
   __TEXT.__text: 0x65d8
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x1ebc
+  __TEXT.__cstring: 0x1ec3
   __TEXT.__oslogstring: 0x8d4
   __TEXT.__unwind_info: 0x1d8
   __TEXT.__auth_stubs: 0x0
CStrings:
+ "security.mac.lockdown_mode_state_public"
- "security.mac.lockdown_mode_state"
```
