## powerexperienced

> `/usr/libexec/powerexperienced`

```diff

-118.40.12.0.0
-  __TEXT.__text: 0x18788
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_stubs: 0x3400
-  __TEXT.__objc_methlist: 0x1fe4
+118.40.15.0.0
+  __TEXT.__text: 0x189f4
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_stubs: 0x3420
+  __TEXT.__objc_methlist: 0x1ff4
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x10da
-  __TEXT.__objc_methname: 0x3b7e
-  __TEXT.__oslogstring: 0x27f7
+  __TEXT.__cstring: 0x1137
+  __TEXT.__objc_methname: 0x3b8f
+  __TEXT.__oslogstring: 0x28e4
   __TEXT.__objc_classname: 0x3df
-  __TEXT.__objc_methtype: 0x80e
+  __TEXT.__objc_methtype: 0x819
   __TEXT.__gcc_except_tab: 0x48
   __TEXT.__dlopen_cstrs: 0x8d
-  __TEXT.__unwind_info: 0x638
-  __DATA_CONST.__auth_got: 0x378
+  __TEXT.__unwind_info: 0x630
+  __DATA_CONST.__auth_got: 0x370
   __DATA_CONST.__got: 0x178
   __DATA_CONST.__const: 0x850
-  __DATA_CONST.__cfstring: 0x1100
+  __DATA_CONST.__cfstring: 0x1220
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA.__objc_const: 0x4ae8
-  __DATA.__objc_selrefs: 0xfe8
+  __DATA.__objc_selrefs: 0xff0
   __DATA.__objc_ivar: 0x224
   __DATA.__objc_data: 0x7d0
   __DATA.__data: 0x600
-  __DATA.__bss: 0x210
+  __DATA.__bss: 0x218
   __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C5A8EC7E-EF8C-3E98-8BA7-04011A9B3249
-  Functions: 745
-  Symbols:   169
-  CStrings:  1442
+  UUID: CC676B0A-63AC-376B-BE85-17830D14BC6E
+  Functions: 748
+  Symbols:   168
+  CStrings:  1466
 
Symbols:
- _objc_retain_x4
CStrings:
+ "%@ is now : %@"
+ "CLPC_LPMOption"
+ "Evaluating power modes on DeviceContext change"
+ "Evaluating power targets on DeviceContext change"
+ "HardwarePlatform"
+ "Trial: Device/Platform not expected for LPM Trial."
+ "Trial: Setting TrialID: %lld with CLPC"
+ "Trial: Setting TrialID: %lld with CLPCInternal"
+ "Trial:CLPC LPMOption %lld adjusted to %lld"
+ "Trial:CLPC LPMOption factor %lld"
+ "Trial:CLPC_TuningOption and CLPC_LPMOption are both zero. Resetting to default"
+ "Trial:CLPC_TuningOption and CLPC_LPMOption both have non-zero values. Resetting to default"
+ "Trial:Error setting clpc trial value %@"
+ "adjustLPMOption:"
+ "kHardwarePlatformContext"
+ "q24@0:8q16"
+ "t8101"
+ "t8110"
+ "t8120"
+ "t8130"
+ "t8140"
+ "t8150"
- "Error setting clpc trial value %@"
- "Evaluating power modes for device context change %@"
- "Evaluating power targets for device context change %@"
- "Power source update. AC powered %d"
- "Received early thermal notification %@"
- "Trial:No trial value for CLPC tuning option. Resetting to default"
- "battery level %@"

```
