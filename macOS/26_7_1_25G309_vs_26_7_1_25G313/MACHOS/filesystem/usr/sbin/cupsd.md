## cupsd

> `usr/sbin/cupsd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`

```diff

-522.9.1.0.0
-  __TEXT.__text: 0x4187c
+522.9.2.0.0
+  __TEXT.__text: 0x41b1c
   __TEXT.__auth_stubs: 0x1f20
-  __TEXT.__cstring: 0x11410
-  __TEXT.__const: 0x340
+  __TEXT.__cstring: 0x11496
+  __TEXT.__const: 0x338
   __TEXT.__oslogstring: 0x24
   __TEXT.__unwind_info: 0x568
   __DATA_CONST.__auth_got: 0xf90

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 404
+  Functions: 406
   Symbols:   532
-  CStrings:  2674
+  CStrings:  2679
 
Symbols:
+ _removefileat
- _rmdir
CStrings:
+ "%s: device_uri is missing."
+ "Failed to get directory fd \"%s\" - %s"
+ "Printer name is missing."
+ "Skipping \"%s/%s\" - %s"
+ "The printer is in use."
```
