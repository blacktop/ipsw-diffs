## Diagnostic-8288

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8288.appex/Diagnostic-8288`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-58.0.0.0.0
-  __TEXT.__text: 0xda14
-  __TEXT.__auth_stubs: 0x6b0
+60.0.0.0.0
+  __TEXT.__text: 0xe04c
+  __TEXT.__auth_stubs: 0x6c0
   __TEXT.__objc_stubs: 0x3c0
   __TEXT.__objc_methlist: 0x50
-  __TEXT.__cstring: 0x3090
-  __TEXT.__gcc_except_tab: 0x1630
+  __TEXT.__cstring: 0x329d
+  __TEXT.__gcc_except_tab: 0x16fc
   __TEXT.__const: 0x18
   __TEXT.__oslogstring: 0x1d
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methname: 0x231
   __TEXT.__objc_methtype: 0xd4
-  __TEXT.__unwind_info: 0x408
+  __TEXT.__unwind_info: 0x430
   __DATA_CONST.__const: 0x4a0
-  __DATA_CONST.__cfstring: 0x21c0
+  __DATA_CONST.__cfstring: 0x2300
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA_CONST.__auth_got: 0x368
+  __DATA_CONST.__auth_got: 0x370
   __DATA_CONST.__got: 0x2f8
   __DATA.__objc_const: 0xd8
   __DATA.__objc_selrefs: 0x108

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 145
-  Symbols:   322
-  CStrings:  383
+  Functions: 148
+  Symbols:   326
+  CStrings:  393
 
Symbols:
+ _CFDictionaryGetTypeID
+ __ZN17DeviceCMInterface19getDiagnosticReportEPU15__autoreleasingP12NSDictionary
+ __ZN17DeviceCMInterface20getAntliaFaultStatusEPy
+ __ZN17DeviceCMInterface28getProjectorCalibratedValuesEPU15__autoreleasingP12NSDictionary
CStrings:
+ "DiagnosticReport"
+ "ProjectorAntliaFaultStatus"
+ "ProjectorCalibratedValues"
+ "getAntliaFaultStatus failed with OSStatus 0x%x for stream id %d (%@)"
+ "getAntliaFaultStatus failed, ir stream id invalid"
+ "getDiagnosticReport failed with OSStatus 0x%x for stream id %d (%@)"
+ "getDiagnosticReport failed, ir stream id invalid"
+ "getDiagnosticReport returned unexpected CF type (not a dictionary) for stream id %d"
+ "getProjectorCalibratedValues failed with OSStatus 0x%x for stream id %d (%@)"
+ "getProjectorCalibratedValues failed, ir stream id invalid"
```
