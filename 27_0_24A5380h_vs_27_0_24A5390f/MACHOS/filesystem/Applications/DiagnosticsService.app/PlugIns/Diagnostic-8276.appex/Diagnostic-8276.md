## Diagnostic-8276

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8276.appex/Diagnostic-8276`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-58.0.0.0.0
-  __TEXT.__text: 0x1ba14
-  __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_stubs: 0x1bc0
+60.0.0.0.0
+  __TEXT.__text: 0x1c1c4
+  __TEXT.__auth_stubs: 0xb20
+  __TEXT.__objc_stubs: 0x1c00
   __TEXT.__objc_methlist: 0x8a4
-  __TEXT.__gcc_except_tab: 0x2d64
-  __TEXT.__const: 0x147
-  __TEXT.__objc_methname: 0x225d
-  __TEXT.__cstring: 0x43ca
+  __TEXT.__gcc_except_tab: 0x2e74
+  __TEXT.__const: 0x123
+  __TEXT.__objc_methname: 0x229b
+  __TEXT.__cstring: 0x4724
   __TEXT.__objc_classname: 0xb4
   __TEXT.__objc_methtype: 0xa12
   __TEXT.__oslogstring: 0x11d
-  __TEXT.__unwind_info: 0x7f0
+  __TEXT.__unwind_info: 0x828
   __DATA_CONST.__const: 0x608
-  __DATA_CONST.__cfstring: 0x3480
+  __DATA_CONST.__cfstring: 0x3620
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x5b8
-  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__auth_got: 0x5a8
+  __DATA_CONST.__got: 0x428
   __DATA.__objc_const: 0x1288
-  __DATA.__objc_selrefs: 0x9c8
+  __DATA.__objc_selrefs: 0x9d8
   __DATA.__objc_ivar: 0x15c
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/JasperDepth.framework/JasperDepth
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 349
-  Symbols:   463
-  CStrings:  1064
+  Functions: 354
+  Symbols:   467
+  CStrings:  1079
 
Symbols:
+ _CFDictionaryGetTypeID
+ _MGCopyAnswer
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_PDPeridotCameraSystemCalibrationData
+ __Z20getCurrentIOSVersionv
+ __ZN17DeviceCMInterface19getDiagnosticReportEPU15__autoreleasingP12NSDictionary
+ __ZN17DeviceCMInterface20getAntliaFaultStatusEPy
+ __ZN17DeviceCMInterface28getProjectorCalibratedValuesEPU15__autoreleasingP12NSDictionary
- __ZdaPvSt19__type_descriptor_t
- __ZnamSt19__type_descriptor_t
- _bzero
- _sysctlbyname
CStrings:
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/DepthDiagnostics/RGBJ/ViewController.mm"
+ "DiagnosticReport"
+ "HWModelStr"
+ "PeridotDepth has no nominal Wide->Peridot extrinsics for %@; refusing to write fallback (would be 180 deg wrong, rdar://155526786)"
+ "ProjectorAntliaFaultStatus"
+ "ProjectorCalibratedValues"
+ "getAntliaFaultStatus failed with OSStatus 0x%x for stream id %d (%@)"
+ "getAntliaFaultStatus failed, ir stream id invalid"
+ "getDiagnosticReport failed with OSStatus 0x%x for stream id %d (%@)"
+ "getDiagnosticReport failed, ir stream id invalid"
+ "getDiagnosticReport returned unexpected CF type (not a dictionary) for stream id %d"
+ "getNominalWideToPeridotExtrinsics:forDeviceName:"
+ "getProjectorCalibratedValues failed with OSStatus 0x%x for stream id %d (%@)"
+ "getProjectorCalibratedValues failed, ir stream id invalid"
+ "operatingSystemVersionString"
+ "processInfo"
+ "set wide jasper extrinsics from PeridotDepth nominal"
+ "unknown device for nominal extrinsics"
- "hw.model"
- "set wide jasper extrinsics to 0"
- "stringWithCString:encoding:"
```
