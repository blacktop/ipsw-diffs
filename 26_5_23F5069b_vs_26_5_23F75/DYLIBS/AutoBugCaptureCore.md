## AutoBugCaptureCore

> `/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore`

```diff

 411.120.4.0.0
-  __TEXT.__text: 0x7eeb4
+  __TEXT.__text: 0x7f008
   __TEXT.__auth_stubs: 0xfc0
   __TEXT.__objc_methlist: 0x5f7c
-  __TEXT.__cstring: 0x517b
+  __TEXT.__cstring: 0x51dc
   __TEXT.__const: 0x290
   __TEXT.__oslogstring: 0xf086
   __TEXT.__gcc_except_tab: 0x11b4
   __TEXT.__ustring: 0x8
   __TEXT.diag_actions: 0x5dcf
-  __TEXT.__unwind_info: 0x1950
+  __TEXT.__unwind_info: 0x1948
   __TEXT.__objc_classname: 0xa08
   __TEXT.__objc_methname: 0xe71d
   __TEXT.__objc_methtype: 0x23cb

   __DATA_CONST.__objc_selrefs: 0x3710
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f0
-  __DATA_CONST.__objc_arraydata: 0x628
+  __DATA_CONST.__objc_arraydata: 0x6b8
   __AUTH_CONST.__auth_got: 0x7f0
   __AUTH_CONST.__const: 0x620
-  __AUTH_CONST.__cfstring: 0x6b80
+  __AUTH_CONST.__cfstring: 0x6c40
   __AUTH_CONST.__objc_const: 0xc888
-  __AUTH_CONST.__objc_dictobj: 0x5a0
+  __AUTH_CONST.__objc_dictobj: 0x690
   __AUTH_CONST.__objc_intobj: 0x2d0
-  __AUTH_CONST.__objc_arrayobj: 0x450
+  __AUTH_CONST.__objc_arrayobj: 0x4b0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x1400
   __DATA.__objc_ivar: 0x68c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4D67053F-29C0-349F-85DC-752BB4EBADEB
+  UUID: AC608CCA-DEDB-3E2F-A5B9-C80AC9375557
   Functions: 2258
   Symbols:   8187
-  CStrings:  5945
+  CStrings:  5957
 
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
~ +[CaseDampeningExceptions allowDampeningExceptionFor:] : 1876 -> 1964
~ -[SystemProperties init] : 1520 -> 1516
~ -[DiagnosticsController addSpecialProjectsDiagnosticActions:] : 56 -> 312
CStrings:
+ "Proxima"
+ "Thread"
+ "WiFi Watchdog"
+ "com.apple.DiagnosticExtensions.ConnectivityDE"
+ "proxima"
+ "proxima-diags"

```
