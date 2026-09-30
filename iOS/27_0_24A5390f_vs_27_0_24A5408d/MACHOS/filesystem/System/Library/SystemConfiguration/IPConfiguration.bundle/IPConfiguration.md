## IPConfiguration

> `/System/Library/SystemConfiguration/IPConfiguration.bundle/IPConfiguration`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-555.0.0.0.0
-  __TEXT.__text: 0x5ca48
+557.0.0.0.0
+  __TEXT.__text: 0x5cd9c
   __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__const: 0x300
-  __TEXT.__oslogstring: 0x61dc
-  __TEXT.__cstring: 0x424b
+  __TEXT.__const: 0x308
+  __TEXT.__oslogstring: 0x623e
+  __TEXT.__cstring: 0x425e
   __TEXT.__unwind_info: 0xc48
   __DATA_CONST.__const: 0x1db0
   __DATA_CONST.__cfstring: 0x2b40

   - /usr/lib/libbsm.0.dylib
   Functions: 1030
   Symbols:   494
-  CStrings:  1740
+  CStrings:  1744
 
CStrings:
+ "%s: %s present in new list"
+ "%s: can't find %s, building new list"
+ "add_or_set_service"
+ "frame_length %zu > sendbuf_len %u"
```
