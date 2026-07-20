## libcups.2.dylib

> `/usr/lib/libcups.2.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__data`

```diff

-530.0.0.0.0
-  __TEXT.__text: 0x4af80
-  __TEXT.__const: 0x330
-  __TEXT.__cstring: 0x1122f
+531.1.0.0.0
+  __TEXT.__text: 0x4b11c
+  __TEXT.__const: 0x340
+  __TEXT.__cstring: 0x11250
+  __TEXT.__oslogstring: 0xae
   __TEXT.__unwind_info: 0xa18
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x7a80
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xb0
   __AUTH_CONST.__cfstring: 0x400
-  __AUTH_CONST.__auth_got: 0xa40
+  __AUTH_CONST.__auth_got: 0xa50
   __AUTH.__data: 0x28
   __DATA.__data: 0x58
   __DATA_DIRTY.__data: 0x178

   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
   Functions: 811
-  Symbols:   979
-  CStrings:  3819
+  Symbols:   982
+  CStrings:  3824
 
Symbols:
+ __os_log_default
+ __os_log_impl
+ _os_log_type_enabled
Functions:
~ sub_196066264 -> sub_1961ac2b4 : 2324 -> 2604
~ __cupsSetError : 172 -> 304
CStrings:
+ "%s: IPP value for %s, tag %d, was sanitized."
+ "%{public}s: last_error=%d last_status_message=%{public}s"
+ "%{public}s: warning, tag: 0x%x string value too long. len %d > max (%d)"
+ "_cupsSetError"
+ "ippReadIOWithDepth"
```
