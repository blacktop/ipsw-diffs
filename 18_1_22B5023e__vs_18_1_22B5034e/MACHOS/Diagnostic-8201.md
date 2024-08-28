## Diagnostic-8201

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201`

```diff

-45.0.0.0.0
-  __TEXT.__text: 0x1f840
+49.0.0.0.0
+  __TEXT.__text: 0x1f800
   __TEXT.__auth_stubs: 0x7f0
   __TEXT.__objc_stubs: 0x9a0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x1d8
-  __TEXT.__gcc_except_tab: 0x24d8
+  __TEXT.__gcc_except_tab: 0x24c4
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x54da
+  __TEXT.__cstring: 0x54b7
   __TEXT.__objc_classname: 0x55
   __TEXT.__objc_methname: 0xb35
   __TEXT.__objc_methtype: 0x6b3
Symbols:
+ __ZN17DeviceCMInterface27getJasperProjectorWillFaultEPy
+ __ZN17DeviceCMInterface19getJasperResistanceEPy
+ __ZN17DeviceCMInterface23getJasperProjectorFaultEPyPU15__autoreleasingP12NSDictionary
- __ZN17DeviceCMInterface32getJasperRikerProjectorWillFaultEPy
- __ZN17DeviceCMInterface24getJasperRikerResistanceEPy
- __ZN17DeviceCMInterface28getJasperRikerProjectorFaultEPy
CStrings:
+ "getJasperProjectorFault %!@(MISSING) failed with OSStatus 0x%!x(MISSING) for stream id %!d(MISSING) (%!@(MISSING)) and property (%!@(MISSING))"
+ "ProjectorQuarkFaultStatus"
- "getJasperRikerProjectorFault failed with OSStatus 0x%!x(MISSING) for stream id %!d(MISSING) (%!@(MISSING))"
- "Null cfType detected for kFigCaptureStreamProperty_ProjectorRikerFaultStatus"

```
