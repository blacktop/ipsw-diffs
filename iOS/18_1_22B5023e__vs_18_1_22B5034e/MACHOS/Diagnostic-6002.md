## Diagnostic-6002

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6002.appex/Diagnostic-6002`

```diff

-45.0.0.0.0
-  __TEXT.__text: 0x1b06c
+49.0.0.0.0
+  __TEXT.__text: 0x1b02c
   __TEXT.__auth_stubs: 0xae0
   __TEXT.__objc_stubs: 0x1bc0
   __TEXT.__objc_methlist: 0x794
-  __TEXT.__gcc_except_tab: 0x2c1c
+  __TEXT.__gcc_except_tab: 0x2c08
   __TEXT.__const: 0x128
   __TEXT.__objc_methname: 0x22e5
-  __TEXT.__cstring: 0x417a
+  __TEXT.__cstring: 0x4157
   __TEXT.__objc_classname: 0xc0
   __TEXT.__objc_methtype: 0xcd0
   __TEXT.__oslogstring: 0xec
Symbols:
+ __ZN17DeviceCMInterface27getJasperProjectorWillFaultEPy
+ __ZN17DeviceCMInterface19getJasperResistanceEPy
+ __ZN17DeviceCMInterface23getJasperProjectorFaultEPyPU15__autoreleasingP12NSDictionary
- __ZN17DeviceCMInterface28getJasperRikerProjectorFaultEPy
- __ZN17DeviceCMInterface24getJasperRikerResistanceEPy
- __ZN17DeviceCMInterface32getJasperRikerProjectorWillFaultEPy
CStrings:
+ "getJasperProjectorFault %!@(MISSING) failed with OSStatus 0x%!x(MISSING) for stream id %!d(MISSING) (%!@(MISSING)) and property (%!@(MISSING))"
+ "ProjectorQuarkFaultStatus"
- "Null cfType detected for kFigCaptureStreamProperty_ProjectorRikerFaultStatus"
- "getJasperRikerProjectorFault failed with OSStatus 0x%!x(MISSING) for stream id %!d(MISSING) (%!@(MISSING))"

```
