## Diagnostic-8253

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253`

```diff

-45.0.0.0.0
-  __TEXT.__text: 0x12888
-  __TEXT.__auth_stubs: 0x6a0
+49.0.0.0.0
+  __TEXT.__text: 0x1291c
+  __TEXT.__auth_stubs: 0x6b0
   __TEXT.__objc_stubs: 0x740
   __TEXT.__objc_methlist: 0xe0
-  __TEXT.__gcc_except_tab: 0x2078
+  __TEXT.__gcc_except_tab: 0x206c
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x39b7
+  __TEXT.__cstring: 0x39ad
   __TEXT.__objc_classname: 0x20
   __TEXT.__objc_methname: 0x585
   __TEXT.__objc_methtype: 0x992
   __TEXT.__unwind_info: 0x590
-  __DATA_CONST.__auth_got: 0x360
+  __DATA_CONST.__auth_got: 0x368
   __DATA_CONST.__got: 0x318
   __DATA_CONST.__const: 0x4d8
-  __DATA_CONST.__cfstring: 0x2e60
+  __DATA_CONST.__cfstring: 0x2ea0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x120

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 202
-  Symbols:   344
-  CStrings:  528
+  Symbols:   345
+  CStrings:  530
 
Symbols:
+ __ZN17DeviceCMInterface23getJasperProjectorFaultEPyPU15__autoreleasingP12NSDictionary
+ _objc_retainAutorelease
+ __ZN17DeviceCMInterface19getJasperResistanceEPy
+ __ZN17DeviceCMInterface27getJasperProjectorWillFaultEPy
- __ZN17DeviceCMInterface24getJasperRikerResistanceEPy
- __ZN17DeviceCMInterface28getJasperRikerProjectorFaultEPy
- __ZN17DeviceCMInterface32getJasperRikerProjectorWillFaultEPy
CStrings:
+ "getJasperProjectorFault %!@(MISSING) failed with OSStatus 0x%!x(MISSING) for stream id %!d(MISSING) (%!@(MISSING)) and property (%!@(MISSING))"
+ "v5"
+ "PROJECTOR_QUARK_FAULT"
+ "ProjectorQuarkFaultStatus"
- "getJasperRikerProjectorFault failed with OSStatus 0x%!x(MISSING) for stream id %!d(MISSING) (%!@(MISSING))"
- "Null cfType detected for kFigCaptureStreamProperty_ProjectorRikerFaultStatus"

```
