## libBKDM2.dylib

> `/usr/lib/libBKDM2.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__TEXT.__objc_classname`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-  __TEXT.__text: 0x7b018
+  __TEXT.__text: 0x7b130
   __TEXT.__auth_stubs: 0xe30
-  __TEXT.__objc_methlist: 0x5c94
+  __TEXT.__objc_methlist: 0x5cd4
   __TEXT.__const: 0x8e07
   __TEXT.__cstring: 0x6caf
   __TEXT.__oslogstring: 0x4372

   __TEXT.__unwind_info: 0xde0
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x37d
-  __TEXT.__objc_methname: 0x14a9b
+  __TEXT.__objc_methname: 0x14b16
   __TEXT.__objc_methtype: 0x29a7
-  __TEXT.__objc_stubs: 0x7ea0
-  __DATA_CONST.__got: 0x468
+  __TEXT.__objc_stubs: 0x7f20
+  __DATA_CONST.__got: 0x470
   __DATA_CONST.__const: 0x1538
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3cb0
+  __DATA_CONST.__objc_selrefs: 0x3cd0
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x360
   __AUTH_CONST.__auth_got: 0x728
   __AUTH_CONST.__const: 0x968
   __AUTH_CONST.__cfstring: 0x60c0
-  __AUTH_CONST.__objc_const: 0x9448
+  __AUTH_CONST.__objc_const: 0x94a8
   __AUTH_CONST.__objc_intobj: 0x3a8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0xa48
+  __DATA.__objc_ivar: 0xa50
   __DATA.__data: 0x890
   __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x410

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 2831
-  Symbols:   5253
-  CStrings:  4452
+  Functions: 2836
+  Symbols:   5265
+  CStrings:  4457
 
Symbols:
+ -[PearlCoreAnalytics deviceThermalState]
+ -[PearlCoreAnalyticsEnrollEvent deviceThermalState]
+ -[PearlCoreAnalyticsEnrollEvent setDeviceThermalState:]
+ -[PearlCoreAnalyticsMatchEvent deviceThermalState]
+ -[PearlCoreAnalyticsMatchEvent setDeviceThermalState:]
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_IVAR_$_PearlCoreAnalyticsEnrollEvent._deviceThermalState
+ _OBJC_IVAR_$_PearlCoreAnalyticsMatchEvent._deviceThermalState
+ _objc_msgSend$deviceThermalState
+ _objc_msgSend$processInfo
+ _objc_msgSend$setDeviceThermalState:
+ _objc_msgSend$thermalState
CStrings:
+ "T@\"NSNumber\",&,V_deviceThermalState"
+ "_deviceThermalState"
+ "deviceThermalState"
+ "processInfo"
+ "setDeviceThermalState:"
+ "thermalState"
- "\t"
```
