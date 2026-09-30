## TactSwitchHIDServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/TactSwitchHIDServiceFilter.plugin/TactSwitchHIDServiceFilter`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-10100.40.0.0.0
-  __TEXT.__text: 0x29cc
-  __TEXT.__auth_stubs: 0x340
+10100.40.2.0.0
+  __TEXT.__text: 0x2b54
+  __TEXT.__auth_stubs: 0x350
   __TEXT.__objc_stubs: 0x720
   __TEXT.__objc_methlist: 0x488
-  __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x334
-  __TEXT.__cstring: 0x360
+  __TEXT.__const: 0xd0
+  __TEXT.__gcc_except_tab: 0x37c
+  __TEXT.__cstring: 0x38a
   __TEXT.__objc_methname: 0x99c
-  __TEXT.__oslogstring: 0x415
+  __TEXT.__oslogstring: 0x482
   __TEXT.__objc_classname: 0x69
   __TEXT.__objc_methtype: 0x65a
   __TEXT.__unwind_info: 0x1b0

   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__auth_got: 0x1c0
   __DATA_CONST.__got: 0x58
   __DATA.__objc_const: 0x928
   __DATA.__objc_selrefs: 0x328

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 71
-  Symbols:   275
-  CStrings:  266
+  Symbols:   276
+  CStrings:  269
 
Symbols:
+ _MGIsDeviceOfType
+ _MGIsDeviceOneOfType
+ _dispatch_queue_create
- _MGGetProductType
- _objc_release_x25
Functions:
~ +[TactSwitchHIDServiceFilter matchService:options:score:] : 204 -> 384
~ -[TouchSensitiveButtonHIDService initWithLog:usagePage:usage:streamCallback:algsInterface:] : 1676 -> 1888
CStrings:
+ "Matched TactSwitchServiceFilter successfully"
+ "TouchSensitiveButtonHIDService: Configured for async operations"
+ "com.apple.multitouch.touchSensitiveButton"
```
