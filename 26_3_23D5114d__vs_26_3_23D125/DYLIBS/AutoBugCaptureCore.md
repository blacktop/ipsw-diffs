## AutoBugCaptureCore

> `/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore`

```diff

 411.80.3.0.0
-  __TEXT.__text: 0x791a4
+  __TEXT.__text: 0x792ec
   __TEXT.__auth_stubs: 0xff0
   __TEXT.__objc_methlist: 0x5f7c
-  __TEXT.__cstring: 0x50ab
+  __TEXT.__cstring: 0x510c
   __TEXT.__const: 0x290
   __TEXT.__oslogstring: 0xef8e
   __TEXT.__gcc_except_tab: 0x10c0
   __TEXT.__ustring: 0x8
   __TEXT.diag_actions: 0x59ac
-  __TEXT.__unwind_info: 0x1578
+  __TEXT.__unwind_info: 0x1570
   __TEXT.__objc_classname: 0xa08
   __TEXT.__objc_methname: 0xe702
   __TEXT.__objc_methtype: 0x23cb

   __DATA_CONST.__objc_selrefs: 0x3700
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f0
-  __DATA_CONST.__objc_arraydata: 0x5d8
+  __DATA_CONST.__objc_arraydata: 0x668
   __AUTH_CONST.__auth_got: 0x808
   __AUTH_CONST.__const: 0x620
-  __AUTH_CONST.__cfstring: 0x6a40
+  __AUTH_CONST.__cfstring: 0x6b00
   __AUTH_CONST.__objc_const: 0xc888
-  __AUTH_CONST.__objc_dictobj: 0x500
+  __AUTH_CONST.__objc_dictobj: 0x5f0
   __AUTH_CONST.__objc_intobj: 0x2d0
-  __AUTH_CONST.__objc_arrayobj: 0x420
+  __AUTH_CONST.__objc_arrayobj: 0x480
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x1400
   __DATA.__objc_ivar: 0x68c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C4209155-805B-3CA2-BD46-264B0A45C492
+  UUID: 581C4B63-75E6-3672-A091-3BE08B482D82
   Functions: 2251
   Symbols:   8166
-  CStrings:  5917
+  CStrings:  5929
 
Symbols:
+ ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.269
+ ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.270
+ ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.272
+ ___74-[DiagnosticsController consolidateLoggingLevelsIntoSet:withCurrentState:]_block_invoke.198
+ ___83-[DiagnosticsController diagnosticExtensionsForDiagnosticCase:enableCommonActions:]_block_invoke.235
+ ___block_literal_global.175
- ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.226
- ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.227
- ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.229
- ___74-[DiagnosticsController consolidateLoggingLevelsIntoSet:withCurrentState:]_block_invoke.155
- ___83-[DiagnosticsController diagnosticExtensionsForDiagnosticCase:enableCommonActions:]_block_invoke.192
- ___block_literal_global.132
Functions:
~ +[CaseDampeningExceptions allowDampeningExceptionFor:] : 1880 -> 1932
~ -[SystemProperties init] : 1476 -> 1472
~ -[DiagnosticsController addSpecialProjectsDiagnosticActions:] : 8 -> 288
CStrings:
+ "Proxima"
+ "Thread"
+ "WiFi Watchdog"
+ "com.apple.DiagnosticExtensions.ConnectivityDE"
+ "proxima"
+ "proxima-diags"

```
