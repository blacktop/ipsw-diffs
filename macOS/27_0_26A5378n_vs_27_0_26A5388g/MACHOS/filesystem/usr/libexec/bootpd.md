## bootpd

> `/usr/libexec/bootpd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-554.0.0.0.0
-  __TEXT.__text: 0x1db18
+555.0.0.0.0
+  __TEXT.__text: 0x1dc78
   __TEXT.__auth_stubs: 0xdd0
   __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x2cf5
+  __TEXT.__cstring: 0x2d38
   __TEXT.__oslogstring: 0x20f7
   __TEXT.__unwind_info: 0x450
   __DATA_CONST.__const: 0x14d8
-  __DATA_CONST.__cfstring: 0x1260
+  __DATA_CONST.__cfstring: 0x12e0
   __DATA_CONST.__auth_got: 0x6e8
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__auth_ptr: 0x50

   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libresolv.9.dylib
-  Functions: 306
-  Symbols:   290
-  CStrings:  947
+  Functions: 308
+  Symbols:   292
+  CStrings:  950
 
Symbols:
+ _SubnetAllSubnetsAreLocal
+ _SubnetUseServerConfig
CStrings:
+ "\tAll Subnets Local: yes\n"
+ "\tUse Server Config: %s\n"
+ "use_server_config"
```
