## inputanalyticsd

> `/usr/libexec/inputanalyticsd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`

```diff

-153.0.0.0.0
-  __TEXT.__text: 0x3d0
-  __TEXT.__auth_stubs: 0x1a0
+154.1.4.0.0
+  __TEXT.__text: 0x488
+  __TEXT.__auth_stubs: 0x1e0
   __TEXT.__objc_stubs: 0x40
-  __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x7d
-  __TEXT.__oslogstring: 0x101
+  __TEXT.__const: 0x58
+  __TEXT.__cstring: 0xc4
+  __TEXT.__oslogstring: 0x138
   __TEXT.__objc_methname: 0x15
-  __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__const: 0x40
+  __TEXT.__unwind_info: 0x88
+  __DATA_CONST.__const: 0x80
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xd8
-  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__auth_got: 0xf8
+  __DATA_CONST.__got: 0x40
   __DATA.__objc_selrefs: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 10
-  Symbols:   38
-  CStrings:  13
+  Functions: 11
+  Symbols:   43
+  CStrings:  17
 
Symbols:
+ __os_log_impl
+ __xpc_event_key_name
+ _objc_release_x19
+ _xpc_dictionary_get_string
+ _xpc_set_event_stream_handler
Functions:
~ sub_1000009d8 : 204 -> 236
+ sub_100000c5c
CStrings:
+ "(unknown)"
+ "com.apple.notifyd.matching"
+ "inputanalyticsd received notification from: %{public}s"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
```
