## Diagnostic-4009

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4009.appex/Diagnostic-4009`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1374.42.1.0.0
-  __TEXT.__text: 0x76a0
+1374.60.20.0.0
+  __TEXT.__text: 0x7798
   __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_stubs: 0x1880
-  __TEXT.__objc_methlist: 0xd64
+  __TEXT.__objc_stubs: 0x1960
+  __TEXT.__objc_methlist: 0xdbc
   __TEXT.__cstring: 0xb33
   __TEXT.__const: 0x50
   __TEXT.__gcc_except_tab: 0x168
   __TEXT.__objc_classname: 0x153
-  __TEXT.__objc_methname: 0x1b0d
+  __TEXT.__objc_methname: 0x1c73
   __TEXT.__objc_methtype: 0x777
   __TEXT.__oslogstring: 0x46d
   __TEXT.__unwind_info: 0x370

   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__auth_got: 0x368
   __DATA_CONST.__got: 0x1e8
-  __DATA.__objc_const: 0x13d0
-  __DATA.__objc_selrefs: 0x768
-  __DATA.__objc_ivar: 0xb8
+  __DATA.__objc_const: 0x1460
+  __DATA.__objc_selrefs: 0x7a0
+  __DATA.__objc_ivar: 0xc4
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x300
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 244
+  Functions: 251
   Symbols:   210
-  CStrings:  578
+  CStrings:  591
 
CStrings:
+ "T@\"OSDCamera\",&,N,V_frontSuperWideCamera"
+ "T@\"OSDCamera\",&,N,V_innerFrontSuperWideCamera"
+ "T@\"OSDCamera\",&,N,V_rearSuperWideCamera"
+ "_frontSuperWideCamera"
+ "_innerFrontSuperWideCamera"
+ "_rearSuperWideCamera"
+ "frontSuperWideCamera"
+ "innerFrontSuperWideCamera"
+ "rearSuperWideCamera"
+ "releaseCameras"
+ "setFrontSuperWideCamera:"
+ "setInnerFrontSuperWideCamera:"
+ "setRearSuperWideCamera:"
```
