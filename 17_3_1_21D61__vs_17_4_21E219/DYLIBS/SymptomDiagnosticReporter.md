## SymptomDiagnosticReporter

> `/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter`

```diff

-308.80.4.0.0
-  __TEXT.__text: 0x6920
-  __TEXT.__auth_stubs: 0x400
+316.100.13.0.0
+  __TEXT.__text: 0x6924
+  __TEXT.__auth_stubs: 0x410
   __TEXT.__objc_methlist: 0x268
-  __TEXT.__const: 0x58
+  __TEXT.__const: 0x5c
   __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__cstring: 0xbc4
+  __TEXT.__cstring: 0xc15
   __TEXT.__oslogstring: 0x8c4
-  __TEXT.__unwind_info: 0x250
+  __TEXT.__unwind_info: 0x244
   __TEXT.__objc_classname: 0x3f
-  __TEXT.__objc_methname: 0x1047
-  __TEXT.__objc_methtype: 0x664
+  __TEXT.__objc_methname: 0x105f
+  __TEXT.__objc_methtype: 0x66f
   __TEXT.__objc_stubs: 0x7a0
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x7f0
+  __DATA_CONST.__const: 0x968
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x6c8
   __DATA_CONST.__objc_selrefs: 0x2c8
-  __AUTH_CONST.__cfstring: 0x1580
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x58
+  __DATA_CONST.__objc_superrefs: 0x8
+  __AUTH_CONST.__cfstring: 0x15a0
+  __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__auth_got: 0x210
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x58
-  __DATA.__objc_superrefs: 0x8
+  __AUTH_CONST.__auth_got: 0x218
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0xc0
-  __DATA_DIRTY.__const: 0x60
+  __DATA_DIRTY.__const: 0x20
   __DATA_DIRTY.__objc_const: 0x90
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x20

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 164
-  Symbols:   703
-  CStrings:  407
+  Functions: 163
+  Symbols:   706
+  CStrings:  410
 
Symbols:
+ -[SDRDiagnosticReporter checkSignatureValidity:]
+ ___105-[SDRDiagnosticReporter startSessionWithSignature:duration:events:payload:actions:wantsRemoteCase:reply:]_block_invoke.132
+ ___105-[SDRDiagnosticReporter startSessionWithSignature:duration:events:payload:actions:wantsRemoteCase:reply:]_block_invoke_2.133
+ ___105-[SDRDiagnosticReporter startSessionWithSignature:duration:events:payload:actions:wantsRemoteCase:reply:]_block_invoke_3.134
+ ___42-[SDRDiagnosticReporter setupXPCInterface]_block_invoke.120
+ ___42-[SDRDiagnosticReporter setupXPCInterface]_block_invoke.123
+ ___56-[SDRDiagnosticReporter getAllDiagnosticCasesWithReply:]_block_invoke.146
+ ___56-[SDRDiagnosticReporter getAutoBugCaptureConfiguration:]_block_invoke.156
+ ___59-[SDRDiagnosticReporter addToSession:events:payload:reply:]_block_invoke.139
+ ___63-[SDRDiagnosticReporter groupCaseIdentifierForSignature:reply:]_block_invoke.126
+ ___64-[SDRDiagnosticReporter getDiagnosticCaseSummariesOfType:reply:]_block_invoke.151
+ ___66-[SDRDiagnosticReporter getDiagnosticPayloadsForSignatures:reply:]_block_invoke.141
+ ___68-[SDRDiagnosticReporter purgeAutoBugCaptureFilesWithSubPaths:reply:]_block_invoke.153
+ ___73-[SDRDiagnosticReporter addSignatureContentForSession:key:content:reply:]_block_invoke.140
+ ___73-[SDRDiagnosticReporter getDiagnosticCaseSummariesWithIdentifiers:reply:]_block_invoke.152
+ ___76-[SDRDiagnosticReporter triggerRemoteSessionForSignature:caseGroupID:reply:]_block_invoke.144
+ ___98-[SDRDiagnosticReporter snapshotWithSignature:delay:events:payload:actions:wantsRemoteCase:reply:]_block_invoke.130
+ ___block_descriptor_44_e8_32bs_e5_v8?0ls32l8
+ ___block_literal_global.136
+ ___block_literal_global.138
+ _kSymptomDiagnosticErrorInvalidSignature
+ _objc_msgSend$checkSignatureValidity:
+ _objc_release_x28
- -[SDRDiagnosticReporter isSignatureValid:]
- ___105-[SDRDiagnosticReporter startSessionWithSignature:duration:events:payload:actions:wantsRemoteCase:reply:]_block_invoke.130
- ___105-[SDRDiagnosticReporter startSessionWithSignature:duration:events:payload:actions:wantsRemoteCase:reply:]_block_invoke_2.132
- ___105-[SDRDiagnosticReporter startSessionWithSignature:duration:events:payload:actions:wantsRemoteCase:reply:]_block_invoke_3.133
- ___42-[SDRDiagnosticReporter setupXPCInterface]_block_invoke.119
- ___42-[SDRDiagnosticReporter setupXPCInterface]_block_invoke.122
- ___56-[SDRDiagnosticReporter getAllDiagnosticCasesWithReply:]_block_invoke.145
- ___56-[SDRDiagnosticReporter getAutoBugCaptureConfiguration:]_block_invoke.155
- ___59-[SDRDiagnosticReporter addToSession:events:payload:reply:]_block_invoke.138
- ___63-[SDRDiagnosticReporter groupCaseIdentifierForSignature:reply:]_block_invoke.125
- ___64-[SDRDiagnosticReporter getDiagnosticCaseSummariesOfType:reply:]_block_invoke.150
- ___66-[SDRDiagnosticReporter getDiagnosticPayloadsForSignatures:reply:]_block_invoke.140
- ___68-[SDRDiagnosticReporter purgeAutoBugCaptureFilesWithSubPaths:reply:]_block_invoke.152
- ___73-[SDRDiagnosticReporter addSignatureContentForSession:key:content:reply:]_block_invoke.139
- ___73-[SDRDiagnosticReporter getDiagnosticCaseSummariesWithIdentifiers:reply:]_block_invoke.151
- ___76-[SDRDiagnosticReporter triggerRemoteSessionForSignature:caseGroupID:reply:]_block_invoke.143
- ___98-[SDRDiagnosticReporter snapshotWithSignature:delay:events:payload:actions:wantsRemoteCase:reply:]_block_invoke.129
- ___block_literal_global.135
- ___block_literal_global.137
- _objc_msgSend$isSignatureValid:
CStrings:
+ "API was called with an invalid signature (signature fields exceed length limits)"
+ "T@\"NSString\",?,R,C"
+ "checkSignatureValidity:"
+ "i24@0:8@16"
- "isSignatureValid:"

```
