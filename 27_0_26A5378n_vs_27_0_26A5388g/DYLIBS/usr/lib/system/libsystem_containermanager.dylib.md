## libsystem_containermanager.dylib

> `/usr/lib/system/libsystem_containermanager.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-833.0.0.501.1
-  __TEXT.__text: 0x2fda8
-  __TEXT.__const: 0x434
-  __TEXT.__cstring: 0x3af2
-  __TEXT.__oslogstring: 0x57c0
+833.0.3.0.0
+  __TEXT.__text: 0x2fe84
+  __TEXT.__const: 0x424
+  __TEXT.__cstring: 0x3aee
+  __TEXT.__oslogstring: 0x582e
   __TEXT.__unwind_info: 0x710
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xca0

   - /usr/lib/system/libxpc.dylib
   Functions: 625
   Symbols:   1012
-  CStrings:  889
+  CStrings:  890
 
Functions:
~ _container_traverse_directory : 4152 -> 4184
~ __container_traverse_parse_attr_buf : 3512 -> 3700
CStrings:
+ "@(#)VERSION:Container Manager: Jul  7 2026 18:28:11; MobileContainerManager_system-833.0.3~122/arm64e"
+ "Malformed attrlist on entry in [%s]; length (%u) exceeds remaining buffer (%zu); buffer = %p, buffer_end = %p"
- "@(#)VERSION:Container Manager: Jun 29 2026 21:04:39; MobileContainerManager_system-833.0.0.501.1~1/arm64e"
```
