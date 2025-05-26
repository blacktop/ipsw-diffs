## restoreserviced

> `/usr/libexec/restoreserviced`

```diff

 24.0.0.0.0
-  __TEXT.__text: 0xcb30
+  __TEXT.__text: 0xcb18
   __TEXT.__auth_stubs: 0xb10
   __TEXT.__objc_stubs: 0x1540
-  __TEXT.__objc_methlist: 0xa8c
+  __TEXT.__objc_methlist: 0xa7c
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x5217
+  __TEXT.__cstring: 0x5235
   __TEXT.__oslogstring: 0x28e
-  __TEXT.__objc_methname: 0x1660
+  __TEXT.__objc_methname: 0x163c
   __TEXT.__objc_classname: 0xbd
   __TEXT.__objc_methtype: 0x5ae
   __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__unwind_info: 0x320
+  __TEXT.__unwind_info: 0x328
   __DATA_CONST.__auth_got: 0x598
   __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0x310
-  __DATA_CONST.__cfstring: 0x2940
+  __DATA_CONST.__const: 0x340
+  __DATA_CONST.__cfstring: 0x2980
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0xb8
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0xf20
   __DATA.__objc_selrefs: 0x678
-  __DATA.__objc_classrefs: 0xb8
-  __DATA.__objc_superrefs: 0x50
   __DATA.__objc_ivar: 0xac
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x81

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
-  - /usr/lib/libimg4.dylib
+  - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 322
+  Functions: 323
   Symbols:   222
-  CStrings:  933
+  CStrings:  934
 
Symbols:
+ _AMAuthInstallUpdaterTwoStageEnabled
- _strncmp
CStrings:
+ "/usr/lib/updaters/libTconUpdaterUARP.dylib"
+ "AppleTconUARP"
+ "Committing valid header via flash as: %@"
+ "DeferredCommit"
+ "Skipping checking AppleTconUARP for booted update\n"
+ "TI,N,V_headerSignature"
+ "_ramrod_update_supported"
+ "array"
+ "update_appletconuarp"
- "-[IODualSPIWriter _commitBytes:atOffset:ofLength:withError:]"
- "0000"
- "Committing valid header as: %@"
- "HUFA"
- "T*,N,V_headerSignature"
- "_commitBytes: Failed to commit %d bytes with error %d"
- "_commitBytes:atOffset:ofLength:withError:"
- "ramrod_update_supported"

```
