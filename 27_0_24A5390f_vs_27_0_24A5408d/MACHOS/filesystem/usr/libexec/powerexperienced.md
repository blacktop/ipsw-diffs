## powerexperienced

> `/usr/libexec/powerexperienced`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-173.0.0.0.0
-  __TEXT.__text: 0x1ad74
+176.0.0.0.0
+  __TEXT.__text: 0x1b58c
   __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_stubs: 0x39c0
-  __TEXT.__objc_methlist: 0x23bc
-  __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x1341
-  __TEXT.__objc_methname: 0x41f5
-  __TEXT.__oslogstring: 0x31b3
-  __TEXT.__objc_classname: 0x400
+  __TEXT.__objc_stubs: 0x3ac0
+  __TEXT.__objc_methlist: 0x2484
+  __TEXT.__const: 0x150
+  __TEXT.__cstring: 0x1361
+  __TEXT.__objc_methname: 0x42e7
+  __TEXT.__oslogstring: 0x32fc
+  __TEXT.__objc_classname: 0x420
   __TEXT.__objc_methtype: 0x8a6
   __TEXT.__gcc_except_tab: 0x48
   __TEXT.__dlopen_cstrs: 0x8d
-  __TEXT.__unwind_info: 0x758
-  __DATA_CONST.__const: 0x8f8
+  __TEXT.__unwind_info: 0x780
+  __DATA_CONST.__const: 0x918
   __DATA_CONST.__cfstring: 0x13e0
-  __DATA_CONST.__objc_classlist: 0xe0
+  __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0xd0
+  __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__auth_got: 0x3a8
   __DATA_CONST.__got: 0x188
-  __DATA.__objc_const: 0x5710
-  __DATA.__objc_selrefs: 0x1180
-  __DATA.__objc_ivar: 0x26c
-  __DATA.__objc_data: 0x8c0
+  __DATA.__objc_const: 0x5840
+  __DATA.__objc_selrefs: 0x11c0
+  __DATA.__objc_ivar: 0x278
+  __DATA.__objc_data: 0x910
   __DATA.__data: 0x600
-  __DATA.__bss: 0x268
+  __DATA.__bss: 0x280
   __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 843
+  Functions: 860
   Symbols:   175
-  CStrings:  1440
+  CStrings:  1457
 
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
+ "setCurrentState:"
+ "setDeviceExperienceState:"
+ "setDeviceOrientationMode:error:"
+ "setDeviceThermalMode:error:"
+ "setDeviceThermalState:"
+ "significantBackgroundTaskBacklogPresent:"
```
