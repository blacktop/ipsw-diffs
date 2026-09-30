## TouchSensitiveButtonHIDService

> `/System/Library/HIDPlugins/ServicePlugins/TouchSensitiveButtonHIDService.plugin/TouchSensitiveButtonHIDService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-10100.40.0.0.0
-  __TEXT.__text: 0x2ef0
+10100.40.2.0.0
+  __TEXT.__text: 0x2fc4
   __TEXT.__auth_stubs: 0x3d0
   __TEXT.__objc_stubs: 0x6e0
   __TEXT.__objc_methlist: 0x470
-  __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x33c
-  __TEXT.__cstring: 0x30c
-  __TEXT.__oslogstring: 0x469
+  __TEXT.__const: 0xe4
+  __TEXT.__gcc_except_tab: 0x384
+  __TEXT.__cstring: 0x336
+  __TEXT.__oslogstring: 0x4a9
   __TEXT.__objc_methname: 0x96d
   __TEXT.__objc_classname: 0x73
   __TEXT.__objc_methtype: 0x5b8

   - /usr/lib/libobjc.A.dylib
   Functions: 83
   Symbols:   289
-  CStrings:  263
+  CStrings:  265
 
Symbols:
+ _MGIsDeviceOfType
+ _dispatch_queue_create
- _MGGetProductType
- _objc_release_x25
Functions:
~ -[TouchSensitiveButtonHIDService initWithLog:usagePage:usage:streamCallback:algsInterface:] : 1676 -> 1888
CStrings:
+ "TouchSensitiveButtonHIDService: Configured for async operations"
+ "com.apple.multitouch.touchSensitiveButton"
```
