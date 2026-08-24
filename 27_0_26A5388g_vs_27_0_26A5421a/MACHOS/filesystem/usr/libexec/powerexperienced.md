## powerexperienced

> `/usr/libexec/powerexperienced`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-173.0.0.0.0
-  __TEXT.__text: 0x16800
+176.0.0.0.0
+  __TEXT.__text: 0x17078
   __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_stubs: 0x2e00
-  __TEXT.__objc_methlist: 0x1e64
-  __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x11c2
-  __TEXT.__objc_methname: 0x363a
-  __TEXT.__oslogstring: 0x2569
-  __TEXT.__objc_classname: 0x327
+  __TEXT.__objc_stubs: 0x2f00
+  __TEXT.__objc_methlist: 0x1f2c
+  __TEXT.__const: 0x140
+  __TEXT.__cstring: 0x11fa
+  __TEXT.__objc_methname: 0x372c
+  __TEXT.__oslogstring: 0x26b2
+  __TEXT.__objc_classname: 0x347
   __TEXT.__objc_methtype: 0x6cb
   __TEXT.__gcc_except_tab: 0x48
   __TEXT.__dlopen_cstrs: 0x8d
-  __TEXT.__unwind_info: 0x5b0
-  __DATA_CONST.__const: 0x8a0
-  __DATA_CONST.__cfstring: 0x1180
-  __DATA_CONST.__objc_classlist: 0xc8
+  __TEXT.__unwind_info: 0x5d8
+  __DATA_CONST.__const: 0x8c0
+  __DATA_CONST.__cfstring: 0x11a0
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0xb8
+  __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__auth_got: 0x2d0
   __DATA_CONST.__got: 0xd0
-  __DATA.__objc_const: 0x4690
-  __DATA.__objc_selrefs: 0xe78
-  __DATA.__objc_ivar: 0x214
-  __DATA.__objc_data: 0x7d0
+  __DATA.__objc_const: 0x47c0
+  __DATA.__objc_selrefs: 0xeb8
+  __DATA.__objc_ivar: 0x220
+  __DATA.__objc_data: 0x820
   __DATA.__data: 0x420
-  __DATA.__bss: 0x238
+  __DATA.__bss: 0x250
   __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 727
+  Functions: 744
   Symbols:   125
-  CStrings:  1203
+  CStrings:  1221
 
CStrings:
+ "DeviceExperienceState changing from %@ to %@ (secondaryDisplayActive=%d)"
+ "DeviceExperienceStateController"
+ "Failed to update CLPC with device orientation mode %@ (state %@). Error: %@"
+ "Failed to update CLPC with device thermal mode %@ (state %@). Error: %@"
+ "TC,V_currentState"
+ "Updated CLPC with device orientation mode %@ (state %@)"
+ "Updated CLPC with device thermal mode %@ (state %@)"
+ "_currentState"
+ "currentState"
+ "deviceexperiencestatecontroller"
+ "evaluateDeviceExperienceState"
+ "kWirelessChargerContext"
+ "setCurrentState:"
+ "setDeviceExperienceState:"
+ "setDeviceOrientationMode:error:"
+ "setDeviceThermalMode:error:"
+ "setDeviceThermalState:"
+ "significantBackgroundTaskBacklogPresent:"
```
