## IPConfiguration

> `/System/Library/SystemConfiguration/IPConfiguration.bundle/Contents/MacOS/IPConfiguration`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-555.0.0.0.0
-  __TEXT.__text: 0x5dbb0
+557.0.0.0.0
+  __TEXT.__text: 0x5df04
   __TEXT.__auth_stubs: 0x11c0
-  __TEXT.__const: 0x310
-  __TEXT.__cstring: 0x4336
-  __TEXT.__oslogstring: 0x633f
-  __TEXT.__unwind_info: 0xc20
+  __TEXT.__const: 0x320
+  __TEXT.__cstring: 0x4349
+  __TEXT.__oslogstring: 0x63a1
+  __TEXT.__unwind_info: 0xc18
   __DATA_CONST.__const: 0x1e58
   __DATA_CONST.__cfstring: 0x2ca0
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   Functions: 1046
   Symbols:   528
-  CStrings:  1762
+  CStrings:  1766
 
CStrings:
+ "%s: %s present in new list"
+ "%s: can't find %s, building new list"
+ "add_or_set_service"
+ "frame_length %zu > sendbuf_len %u"
```
