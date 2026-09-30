## AutoBugCaptureCore

> `/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/AutoBugCaptureCore`

```diff

-411.2.1.0.0
-  __TEXT.__text: 0x791c0
+411.40.3.0.0
+  __TEXT.__text: 0x79140
   __TEXT.__auth_stubs: 0xff0
   __TEXT.__objc_methlist: 0x5f5c
-  __TEXT.__cstring: 0x5082
+  __TEXT.__cstring: 0x508f
   __TEXT.__const: 0x290
-  __TEXT.__oslogstring: 0xefb7
+  __TEXT.__oslogstring: 0xef8e
   __TEXT.__gcc_except_tab: 0x10c0
   __TEXT.__ustring: 0x8
-  __TEXT.diag_actions: 0x5553
+  __TEXT.diag_actions: 0x587e
   __TEXT.__unwind_info: 0x1570
   __TEXT.__objc_classname: 0xa08
   __TEXT.__objc_methname: 0xe65d

   __DATA_CONST.__objc_selrefs: 0x36e8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f0
-  __DATA_CONST.__objc_arraydata: 0x5c8
+  __DATA_CONST.__objc_arraydata: 0x5b0
   __AUTH_CONST.__auth_got: 0x808
   __AUTH_CONST.__const: 0x620
-  __AUTH_CONST.__cfstring: 0x6a40
+  __AUTH_CONST.__cfstring: 0x6a00
   __AUTH_CONST.__objc_const: 0xc878
-  __AUTH_CONST.__objc_dictobj: 0x4d8
+  __AUTH_CONST.__objc_dictobj: 0x4b0
   __AUTH_CONST.__objc_intobj: 0x2d0
-  __AUTH_CONST.__objc_arrayobj: 0x420
+  __AUTH_CONST.__objc_arrayobj: 0x408
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x1400
   __DATA.__objc_ivar: 0x68c
-  __DATA.__data: 0xce8
+  __DATA.__data: 0xd20
   __DATA.__bss: 0x238
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x4b0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9F2234E5-3184-31D4-8E17-D1C02F07706D
+  UUID: C3EA08CB-0CBD-32E3-87BE-EE04DB1B5E63
   Functions: 2250
-  Symbols:   8159
-  CStrings:  5909
+  Symbols:   8162
+  CStrings:  5907
 
Symbols:
+ ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.226
+ ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.227
+ ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.229
+ ___112-[DiagnosticExtensionController collectDEPayloadsWithIdentifier:diagnosticExtensionsWithParameters:queue:reply:]_block_invoke.101
+ ___112-[DiagnosticExtensionController collectDEPayloadsWithIdentifier:diagnosticExtensionsWithParameters:queue:reply:]_block_invoke.105
+ ___112-[DiagnosticExtensionController collectDEPayloadsWithIdentifier:diagnosticExtensionsWithParameters:queue:reply:]_block_invoke.92
+ ___112-[DiagnosticExtensionController collectDEPayloadsWithIdentifier:diagnosticExtensionsWithParameters:queue:reply:]_block_invoke.94
+ ___59-[DiagnosticExtensionCaller _getDEExtensionWithIdentifier:]_block_invoke.74
+ ___74-[DiagnosticsController consolidateLoggingLevelsIntoSet:withCurrentState:]_block_invoke.155
+ ___83-[DiagnosticsController diagnosticExtensionsForDiagnosticCase:enableCommonActions:]_block_invoke.192
+ ___88-[DiagnosticExtensionCaller _getAttachmentsFrom:forBundleID:withParameters:queue:reply:]_block_invoke.79
+ ___block_literal_global.132
+ _kNetDiagAlwaysOnDroptap
+ _kNetDiagCmdTaskSnapshot
+ _kNetDiagOptNoTLSKeys
- ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.220
- ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.221
- ___105-[DiagnosticsController collectDiagnosticExtensionFilesForDiagnosticCase:parameters:options:queue:reply:]_block_invoke.223
- ___112-[DiagnosticExtensionController collectDEPayloadsWithIdentifier:diagnosticExtensionsWithParameters:queue:reply:]_block_invoke.86
- ___112-[DiagnosticExtensionController collectDEPayloadsWithIdentifier:diagnosticExtensionsWithParameters:queue:reply:]_block_invoke.88
- ___112-[DiagnosticExtensionController collectDEPayloadsWithIdentifier:diagnosticExtensionsWithParameters:queue:reply:]_block_invoke.95
- ___112-[DiagnosticExtensionController collectDEPayloadsWithIdentifier:diagnosticExtensionsWithParameters:queue:reply:]_block_invoke.99
- ___59-[DiagnosticExtensionCaller _getDEExtensionWithIdentifier:]_block_invoke.68
- ___74-[DiagnosticsController consolidateLoggingLevelsIntoSet:withCurrentState:]_block_invoke.149
- ___83-[DiagnosticsController diagnosticExtensionsForDiagnosticCase:enableCommonActions:]_block_invoke.186
- ___88-[DiagnosticExtensionCaller _getAttachmentsFrom:forBundleID:withParameters:queue:reply:]_block_invoke.73
- ___block_literal_global.126
Functions:
~ +[CaseDampeningExceptions allowDampeningExceptionFor:] : 1964 -> 1832
~ -[SystemProperties init] : 1472 -> 1476
CStrings:
+ "alwaysondroptap"
+ "notlskeys"
- "Added WiFi exceptions to exceptions list"
- "WiFi Watchdog"
- "proxima"

```
