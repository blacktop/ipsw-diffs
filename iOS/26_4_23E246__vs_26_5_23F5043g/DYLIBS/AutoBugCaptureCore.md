## AutoBugCaptureCore

> `/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore`

```diff

-411.100.14.0.0
-  __TEXT.__text: 0x7ef80
+411.120.3.0.0
+  __TEXT.__text: 0x7eeb4
   __TEXT.__auth_stubs: 0xfc0
   __TEXT.__objc_methlist: 0x5f7c
-  __TEXT.__cstring: 0x519c
+  __TEXT.__cstring: 0x515e
   __TEXT.__const: 0x290
   __TEXT.__oslogstring: 0xf086
   __TEXT.__gcc_except_tab: 0x11b4
   __TEXT.__ustring: 0x8
-  __TEXT.diag_actions: 0x5d43
-  __TEXT.__unwind_info: 0x1948
+  __TEXT.diag_actions: 0x5dcf
+  __TEXT.__unwind_info: 0x1950
   __TEXT.__objc_classname: 0xa08
   __TEXT.__objc_methname: 0xe71d
   __TEXT.__objc_methtype: 0x23cb

   __DATA_CONST.__objc_selrefs: 0x3710
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f0
-  __DATA_CONST.__objc_arraydata: 0x668
+  __DATA_CONST.__objc_arraydata: 0x600
   __AUTH_CONST.__auth_got: 0x7f0
   __AUTH_CONST.__const: 0x620
-  __AUTH_CONST.__cfstring: 0x6b80
+  __AUTH_CONST.__cfstring: 0x6b20
   __AUTH_CONST.__objc_const: 0xc888
-  __AUTH_CONST.__objc_dictobj: 0x5f0
+  __AUTH_CONST.__objc_dictobj: 0x550
   __AUTH_CONST.__objc_intobj: 0x2d0
-  __AUTH_CONST.__objc_arrayobj: 0x480
+  __AUTH_CONST.__objc_arrayobj: 0x438
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x1400
   __DATA.__objc_ivar: 0x68c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5AF69AA8-140B-354B-907E-7F4C54C9A851
+  UUID: D7B560A2-1968-3D9B-8AC5-933ECACA49E6
   Functions: 2258
   Symbols:   8187
-  CStrings:  5945
+  CStrings:  5939
 
Symbols:
+ ___103-[DiagnosticCaseManager startSessionWithSignature:flags:preferredTimeout:events:payload:actions:reply:]_block_invoke.267
+ ___103-[DiagnosticCaseManager startSessionWithSignature:flags:preferredTimeout:events:payload:actions:reply:]_block_invoke.268
+ ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.226
+ ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.227
+ ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.229
+ ___49-[DiagnosticCaseManager isAdmissible:dampenedBy:]_block_invoke.196
+ ___53-[DiagnosticCaseManager payloadsForSignatures:reply:]_block_invoke.283
+ ___55-[DiagnosticCaseManager _updateCaseStatisticsWithCase:]_block_invoke.205
+ ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.246
+ ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.248
+ ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.256
+ ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.260
+ ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.262
+ ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke_2.257
+ ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke_2.261
+ ___70-[DiagnosticCaseManager requestGroupCaseIdentifierForSignature:reply:]_block_invoke.197
+ ___74-[DiagnosticsController consolidateLoggingLevelsIntoSet:withCurrentState:]_block_invoke.155
+ ___83-[DiagnosticsController diagnosticExtensionsForDiagnosticCase:enableCommonActions:]_block_invoke.192
+ ___86-[DiagnosticCaseManager _processRemoteIDSTriggers:validFor:signature:sessionID:reply:]_block_invoke.224
+ ___86-[DiagnosticCaseManager _processRemoteIDSTriggers:validFor:signature:sessionID:reply:]_block_invoke.225
+ ___86-[DiagnosticCaseManager _processRemoteIDSTriggers:validFor:signature:sessionID:reply:]_block_invoke.228
+ ___block_literal_global.132
+ ___block_literal_global.265
- ___103-[DiagnosticCaseManager startSessionWithSignature:flags:preferredTimeout:events:payload:actions:reply:]_block_invoke.258
- ___103-[DiagnosticCaseManager startSessionWithSignature:flags:preferredTimeout:events:payload:actions:reply:]_block_invoke.259
- ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.269
- ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.270
- ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.272
- ___49-[DiagnosticCaseManager isAdmissible:dampenedBy:]_block_invoke.187
- ___53-[DiagnosticCaseManager payloadsForSignatures:reply:]_block_invoke.274
- ___55-[DiagnosticCaseManager _updateCaseStatisticsWithCase:]_block_invoke.196
- ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.237
- ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.239
- ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.247
- ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.251
- ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.253
- ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke_2.248
- ___63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke_2.252
- ___70-[DiagnosticCaseManager requestGroupCaseIdentifierForSignature:reply:]_block_invoke.188
- ___74-[DiagnosticsController consolidateLoggingLevelsIntoSet:withCurrentState:]_block_invoke.198
- ___83-[DiagnosticsController diagnosticExtensionsForDiagnosticCase:enableCommonActions:]_block_invoke.235
- ___86-[DiagnosticCaseManager _processRemoteIDSTriggers:validFor:signature:sessionID:reply:]_block_invoke.215
- ___86-[DiagnosticCaseManager _processRemoteIDSTriggers:validFor:signature:sessionID:reply:]_block_invoke.216
- ___86-[DiagnosticCaseManager _processRemoteIDSTriggers:validFor:signature:sessionID:reply:]_block_invoke.219
- ___block_literal_global.175
- ___block_literal_global.256
Functions:
~ +[CaseDampeningExceptions allowDampeningExceptionFor:] : 1888 -> 1876
~ -[SystemProperties init] : 1516 -> 1520
~ -[DiagnosticsController addSpecialProjectsDiagnosticActions:] : 312 -> 56
~ -[DiagnosticCaseManager buildSpecificRestrictionsForSignature:result:] : 1856 -> 1916
CStrings:
+ "Heuristics"
+ "NetifBufferTimeout"
+ "ULPN"
- "Proxima"
- "Thread"
- "WiFi Watchdog"
- "com.apple.DiagnosticExtensions.ConnectivityDE"
- "proxima"
- "proxima-diags"

```
