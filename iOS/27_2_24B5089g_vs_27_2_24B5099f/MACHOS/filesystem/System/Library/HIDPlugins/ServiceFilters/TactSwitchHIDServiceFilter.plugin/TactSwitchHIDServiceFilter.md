## TactSwitchHIDServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/TactSwitchHIDServiceFilter.plugin/TactSwitchHIDServiceFilter`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-10100.44.0.0.0
-  __TEXT.__text: 0x2ab8
+10110.3.0.0.0
+  __TEXT.__text: 0x2b3c
   __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_stubs: 0x720
+  __TEXT.__objc_stubs: 0x740
   __TEXT.__objc_methlist: 0x488
   __TEXT.__const: 0xe0
   __TEXT.__gcc_except_tab: 0x37c
-  __TEXT.__cstring: 0x38a
-  __TEXT.__objc_methname: 0x99c
-  __TEXT.__oslogstring: 0x482
+  __TEXT.__cstring: 0x3a3
+  __TEXT.__objc_methname: 0x9a8
+  __TEXT.__oslogstring: 0x4c8
   __TEXT.__objc_classname: 0x69
   __TEXT.__objc_methtype: 0x65a
   __TEXT.__unwind_info: 0x1f0
   __DATA_CONST.__const: 0x240
-  __DATA_CONST.__cfstring: 0x360
+  __DATA_CONST.__cfstring: 0x3a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0x1c0
   __DATA_CONST.__got: 0x58
   __DATA.__objc_const: 0x928
-  __DATA.__objc_selrefs: 0x328
+  __DATA.__objc_selrefs: 0x330
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 71
-  Symbols:   276
-  CStrings:  269
+  Symbols:   277
+  CStrings:  272
 
Symbols:
+ _objc_msgSend$boolForKey:
Functions:
~ -[TactSwitchHIDServiceFilter createUserDevice] : 476 -> 608
CStrings:
+ "MTDisableDebugUserDevice"
+ "MTDisableDebugUserDevice set; skipping debug HID user device creation"
+ "boolForKey:"
```
