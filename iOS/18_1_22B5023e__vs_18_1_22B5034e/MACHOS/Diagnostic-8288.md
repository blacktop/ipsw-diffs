## Diagnostic-8288

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8288.appex/Diagnostic-8288`

```diff

-45.0.0.0.0
-  __TEXT.__text: 0xdb44
-  __TEXT.__auth_stubs: 0x6d0
+49.0.0.0.0
+  __TEXT.__text: 0xdb04
+  __TEXT.__auth_stubs: 0x6e0
   __TEXT.__objc_stubs: 0x3c0
   __TEXT.__objc_methlist: 0x50
-  __TEXT.__cstring: 0x2f77
-  __TEXT.__gcc_except_tab: 0x161c
+  __TEXT.__cstring: 0x2f54
+  __TEXT.__gcc_except_tab: 0x1608
   __TEXT.__const: 0x18
   __TEXT.__oslogstring: 0x1d
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methname: 0x231
   __TEXT.__objc_methtype: 0xd4
   __TEXT.__unwind_info: 0x418
-  __DATA_CONST.__auth_got: 0x378
+  __DATA_CONST.__auth_got: 0x380
   __DATA_CONST.__got: 0x2f8
   __DATA_CONST.__const: 0x480
   __DATA_CONST.__cfstring: 0x2080

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 148
-  Symbols:   324
+  Symbols:   325
   CStrings:  370
 
Symbols:
+ __ZN17DeviceCMInterface27getJasperProjectorWillFaultEPy
+ __ZN17DeviceCMInterface23getJasperProjectorFaultEPyPU15__autoreleasingP12NSDictionary
+ __ZN17DeviceCMInterface19getJasperResistanceEPy
+ _objc_retainAutorelease
- __ZN17DeviceCMInterface28getJasperRikerProjectorFaultEPy
- __ZN17DeviceCMInterface24getJasperRikerResistanceEPy
- __ZN17DeviceCMInterface32getJasperRikerProjectorWillFaultEPy
CStrings:
+ "getJasperProjectorFault %!@(MISSING) failed with OSStatus 0x%!x(MISSING) for stream id %!d(MISSING) (%!@(MISSING)) and property (%!@(MISSING))"
+ "ProjectorQuarkFaultStatus"
- "Null cfType detected for kFigCaptureStreamProperty_ProjectorRikerFaultStatus"
- "getJasperRikerProjectorFault failed with OSStatus 0x%!x(MISSING) for stream id %!d(MISSING) (%!@(MISSING))"

```
