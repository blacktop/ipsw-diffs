## Diagnostic-8276

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8276.appex/Diagnostic-8276`

```diff

-45.0.0.0.0
-  __TEXT.__text: 0x1a9f0
+49.0.0.0.0
+  __TEXT.__text: 0x1a9b0
   __TEXT.__auth_stubs: 0xad0
   __TEXT.__objc_stubs: 0x1a40
   __TEXT.__objc_methlist: 0x754
-  __TEXT.__gcc_except_tab: 0x2b5c
+  __TEXT.__gcc_except_tab: 0x2b48
   __TEXT.__const: 0x128
   __TEXT.__objc_methname: 0x21a0
-  __TEXT.__cstring: 0x4026
+  __TEXT.__cstring: 0x4003
   __TEXT.__objc_classname: 0xca
   __TEXT.__objc_methtype: 0xc61
   __TEXT.__oslogstring: 0x11d
Symbols:
+ __ZN17DeviceCMInterface19getJasperResistanceEPy
+ __ZN17DeviceCMInterface23getJasperProjectorFaultEPyPU15__autoreleasingP12NSDictionary
+ __ZN17DeviceCMInterface27getJasperProjectorWillFaultEPy
- __ZN17DeviceCMInterface24getJasperRikerResistanceEPy
- __ZN17DeviceCMInterface32getJasperRikerProjectorWillFaultEPy
- __ZN17DeviceCMInterface28getJasperRikerProjectorFaultEPy
CStrings:
+ "ProjectorQuarkFaultStatus"
+ "getJasperProjectorFault %!@(MISSING) failed with OSStatus 0x%!x(MISSING) for stream id %!d(MISSING) (%!@(MISSING)) and property (%!@(MISSING))"
- "Null cfType detected for kFigCaptureStreamProperty_ProjectorRikerFaultStatus"
- "getJasperRikerProjectorFault failed with OSStatus 0x%!x(MISSING) for stream id %!d(MISSING) (%!@(MISSING))"

```
