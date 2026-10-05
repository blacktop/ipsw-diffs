## TouchSensitiveButtonHIDService

> `/System/Library/HIDPlugins/ServicePlugins/TouchSensitiveButtonHIDService.plugin/TouchSensitiveButtonHIDService`

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
-  __TEXT.__text: 0x2f28
+10110.3.0.0.0
+  __TEXT.__text: 0x2fa4
   __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_stubs: 0x6e0
+  __TEXT.__objc_stubs: 0x700
   __TEXT.__objc_methlist: 0x470
   __TEXT.__const: 0xf8
   __TEXT.__gcc_except_tab: 0x384
-  __TEXT.__cstring: 0x336
-  __TEXT.__oslogstring: 0x4a9
-  __TEXT.__objc_methname: 0x96d
+  __TEXT.__cstring: 0x34f
+  __TEXT.__oslogstring: 0x4ef
+  __TEXT.__objc_methname: 0x979
   __TEXT.__objc_classname: 0x73
   __TEXT.__objc_methtype: 0x5b8
   __TEXT.__unwind_info: 0x210
   __DATA_CONST.__const: 0x240
-  __DATA_CONST.__cfstring: 0x2a0
+  __DATA_CONST.__cfstring: 0x2e0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0x200
   __DATA_CONST.__got: 0x68
   __DATA.__objc_const: 0x918
-  __DATA.__objc_selrefs: 0x318
+  __DATA.__objc_selrefs: 0x320
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 83
-  Symbols:   289
-  CStrings:  265
+  Symbols:   290
+  CStrings:  268
 
Symbols:
+ _objc_msgSend$boolForKey:
Functions:
~ -[TouchSensitiveButtonHIDServicePlugin createUserDevice] : 476 -> 600
CStrings:
+ "MTDisableDebugUserDevice"
+ "MTDisableDebugUserDevice set; skipping debug HID user device creation"
+ "boolForKey:"
```
