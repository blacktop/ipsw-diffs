## inputanalyticsd

> `/usr/libexec/inputanalyticsd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`

```diff

-153.500.0.0.0
-  __TEXT.__text: 0x568
-  __TEXT.__auth_stubs: 0x1a0
+154.1.4.0.0
+  __TEXT.__text: 0x624
+  __TEXT.__auth_stubs: 0x1d0
   __TEXT.__objc_stubs: 0x40
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x95
-  __TEXT.__oslogstring: 0x190
+  __TEXT.__cstring: 0xdc
+  __TEXT.__oslogstring: 0x1c7
   __TEXT.__objc_methname: 0x15
   __TEXT.__unwind_info: 0x90
-  __DATA_CONST.__const: 0x40
+  __DATA_CONST.__const: 0x80
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xd8
-  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x40
   __DATA.__objc_selrefs: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/InputAnalyticsServer.framework/Versions/A/InputAnalyticsServer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 14
-  Symbols:   38
-  CStrings:  18
+  Functions: 15
+  Symbols:   42
+  CStrings:  22
 
Symbols:
+ __os_log_impl
+ __xpc_event_key_name
+ _xpc_dictionary_get_string
+ _xpc_set_event_stream_handler
Functions:
~ sub_100000a10 : 212 -> 248
+ sub_100000d78
CStrings:
+ "(unknown)"
+ "com.apple.notifyd.matching"
+ "inputanalyticsd received notification from: %{public}s"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
```
