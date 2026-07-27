## libsystem_containermanager.dylib

> `/usr/lib/system/libsystem_containermanager.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-725.160.2.0.0
-  __TEXT.__text: 0x2da38
+725.160.3.0.0
+  __TEXT.__text: 0x2db04
   __TEXT.__auth_stubs: 0xaf0
   __TEXT.__const: 0x290
   __TEXT.__cstring: 0x38df
-  __TEXT.__oslogstring: 0x4f7a
+  __TEXT.__oslogstring: 0x4fe8
   __TEXT.__unwind_info: 0x6a0
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0xc98

   - /usr/lib/system/libxpc.dylib
   Functions: 590
   Symbols:   971
-  CStrings:  830
+  CStrings:  831
 
Functions:
~ _container_traverse_directory : 4296 -> 4312
~ __container_traverse_parse_attr_buf : 3556 -> 3744
CStrings:
+ "@(#)VERSION:Container Manager: Jul 11 2026 14:43:51; MobileContainerManager_system-725.160.3~30/arm64e"
+ "Malformed attrlist on entry in [%s]; length (%u) exceeds remaining buffer (%zu); buffer = %p, buffer_end = %p"
- "@(#)VERSION:Container Manager: Jun 17 2026 01:17:51; MobileContainerManager_system-725.160.2~34/arm64e"
```
