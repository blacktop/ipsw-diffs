## Diagnostic-8253

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-58.0.0.0.0
-  __TEXT.__text: 0x13160
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_stubs: 0x820
+60.0.0.0.0
+  __TEXT.__text: 0x13828
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_stubs: 0x860
   __TEXT.__objc_methlist: 0xf8
-  __TEXT.__gcc_except_tab: 0x226c
+  __TEXT.__gcc_except_tab: 0x2358
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x3d03
+  __TEXT.__cstring: 0x3f1c
   __TEXT.__objc_classname: 0x1c
-  __TEXT.__objc_methname: 0x60a
+  __TEXT.__objc_methname: 0x633
   __TEXT.__objc_methtype: 0x7d1
-  __TEXT.__unwind_info: 0x600
+  __TEXT.__unwind_info: 0x630
   __DATA_CONST.__const: 0x518
-  __DATA_CONST.__cfstring: 0x3240
+  __DATA_CONST.__cfstring: 0x33a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x120
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA_CONST.__auth_got: 0x390
-  __DATA_CONST.__got: 0x320
+  __DATA_CONST.__auth_got: 0x398
+  __DATA_CONST.__got: 0x328
   __DATA.__objc_const: 0x278
-  __DATA.__objc_selrefs: 0x230
+  __DATA.__objc_selrefs: 0x240
   __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 213
-  Symbols:   355
-  CStrings:  570
+  Functions: 217
+  Symbols:   361
+  CStrings:  583
 
Symbols:
+ _CFDictionaryGetTypeID
+ _OBJC_CLASS_$_NSProcessInfo
+ __Z20getCurrentIOSVersionv
+ __ZN17DeviceCMInterface19getDiagnosticReportEPU15__autoreleasingP12NSDictionary
+ __ZN17DeviceCMInterface20getAntliaFaultStatusEPy
+ __ZN17DeviceCMInterface28getProjectorCalibratedValuesEPU15__autoreleasingP12NSDictionary
CStrings:
+ "DiagnosticReport"
+ "IOS_VERSION"
+ "ProjectorAntliaFaultStatus"
+ "ProjectorCalibratedValues"
+ "getAntliaFaultStatus failed with OSStatus 0x%x for stream id %d (%@)"
+ "getAntliaFaultStatus failed, ir stream id invalid"
+ "getDiagnosticReport failed with OSStatus 0x%x for stream id %d (%@)"
+ "getDiagnosticReport failed, ir stream id invalid"
+ "getDiagnosticReport returned unexpected CF type (not a dictionary) for stream id %d"
+ "getProjectorCalibratedValues failed with OSStatus 0x%x for stream id %d (%@)"
+ "getProjectorCalibratedValues failed, ir stream id invalid"
+ "operatingSystemVersionString"
+ "processInfo"
```
