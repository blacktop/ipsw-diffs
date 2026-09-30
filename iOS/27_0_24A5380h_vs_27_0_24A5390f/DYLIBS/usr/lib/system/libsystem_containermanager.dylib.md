## libsystem_containermanager.dylib

> `/usr/lib/system/libsystem_containermanager.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-833.0.0.0.0
-  __TEXT.__text: 0x2ffd0
-  __TEXT.__const: 0x414
-  __TEXT.__cstring: 0x3c41
-  __TEXT.__oslogstring: 0x5939
+833.0.3.0.0
+  __TEXT.__text: 0x300a8
+  __TEXT.__const: 0x424
+  __TEXT.__cstring: 0x3c45
+  __TEXT.__oslogstring: 0x59a7
   __TEXT.__unwind_info: 0x708
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x1d08

   - /usr/lib/system/libxpc.dylib
   Functions: 626
   Symbols:   1008
-  CStrings:  904
+  CStrings:  905
 
Functions:
~ _container_persona_copy_from_voucher_proximate : 644 -> 636
~ _container_traverse_directory : 4156 -> 4188
~ __container_traverse_parse_attr_buf : 3512 -> 3700
~ _container_audit_token_get_launch_persona : 524 -> 528
CStrings:
+ "@(#)VERSION:Container Manager: Jul  8 2026 00:24:25; MobileContainerManager_system-833.0.3~133/arm64e"
+ "Malformed attrlist on entry in [%s]; length (%u) exceeds remaining buffer (%zu); buffer = %p, buffer_end = %p"
- "@(#)VERSION:Container Manager: Jun 23 2026 01:24:57; MobileContainerManager_system-833~403/arm64e"
```
