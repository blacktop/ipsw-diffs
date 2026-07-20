## Diagnostic-6002

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6002.appex/Diagnostic-6002`

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
-  __TEXT.__text: 0x1c830
-  __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_stubs: 0x1d60
+60.0.0.0.0
+  __TEXT.__text: 0x1cfe0
+  __TEXT.__auth_stubs: 0xb30
+  __TEXT.__objc_stubs: 0x1dc0
   __TEXT.__objc_methlist: 0x8e4
-  __TEXT.__gcc_except_tab: 0x3044
-  __TEXT.__const: 0x147
-  __TEXT.__objc_methname: 0x23bf
-  __TEXT.__cstring: 0x4683
+  __TEXT.__gcc_except_tab: 0x3154
+  __TEXT.__const: 0x123
+  __TEXT.__objc_methname: 0x2419
+  __TEXT.__cstring: 0x49dd
   __TEXT.__objc_classname: 0xaa
   __TEXT.__objc_methtype: 0xa81
   __TEXT.__oslogstring: 0x26
-  __TEXT.__unwind_info: 0x818
+  __TEXT.__unwind_info: 0x850
   __DATA_CONST.__const: 0x608
-  __DATA_CONST.__cfstring: 0x3600
+  __DATA_CONST.__cfstring: 0x37a0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x5c0
-  __DATA_CONST.__got: 0x428
+  __DATA_CONST.__auth_got: 0x5b0
+  __DATA_CONST.__got: 0x438
   __DATA.__objc_const: 0x12b8
-  __DATA.__objc_selrefs: 0xa30
+  __DATA.__objc_selrefs: 0xa48
   __DATA.__objc_ivar: 0x160
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/JasperDepth.framework/JasperDepth
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 354
-  Symbols:   466
-  CStrings:  1090
+  Functions: 359
+  Symbols:   470
+  CStrings:  1106
 
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
```
