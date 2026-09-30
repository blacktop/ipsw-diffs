## bootpd

> `/usr/libexec/bootpd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-554.0.0.0.0
-  __TEXT.__text: 0x10f8c
+555.0.0.0.0
+  __TEXT.__text: 0x110f4
   __TEXT.__auth_stubs: 0x970
   __TEXT.__const: 0xe8
-  __TEXT.__cstring: 0x1ed1
+  __TEXT.__cstring: 0x1f14
   __TEXT.__oslogstring: 0x11a2
   __TEXT.__unwind_info: 0x2f8
   __DATA_CONST.__const: 0x1318
-  __DATA_CONST.__cfstring: 0xc40
+  __DATA_CONST.__cfstring: 0xcc0
   __DATA_CONST.__auth_got: 0x4b8
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x18

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libresolv.9.dylib
-  Functions: 211
-  Symbols:   197
-  CStrings:  648
+  Functions: 213
+  Symbols:   199
+  CStrings:  651
 
Symbols:
+ _SubnetAllSubnetsAreLocal
+ _SubnetUseServerConfig
CStrings:
+ "\tAll Subnets Local: yes\n"
+ "\tUse Server Config: %s\n"
+ "use_server_config"
```
