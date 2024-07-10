## SymptomDiagnosticReporter

> `/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/Versions/A/SymptomDiagnosticReporter`

```diff

-358.0.0.0.0
-  __TEXT.__text: 0x90a0
-  __TEXT.__auth_stubs: 0x290
+362.0.0.0.0
+  __TEXT.__text: 0x8fd4
+  __TEXT.__auth_stubs: 0x2a0
   __TEXT.__objc_methlist: 0x308
-  __TEXT.__const: 0xa4
-  __TEXT.__gcc_except_tab: 0x9c
+  __TEXT.__const: 0xac
+  __TEXT.__gcc_except_tab: 0x88
   __TEXT.__cstring: 0x12e6
-  __TEXT.__oslogstring: 0xe45
-  __TEXT.__unwind_info: 0x2d0
+  __TEXT.__oslogstring: 0xf2a
+  __TEXT.__unwind_info: 0x2c0
   __TEXT.__objc_classname: 0x57
   __TEXT.__objc_methname: 0x12c4
   __TEXT.__objc_methtype: 0x6b0

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x480
-  __AUTH_CONST.__auth_got: 0x158
-  __AUTH_CONST.__const: 0x420
+  __AUTH_CONST.__auth_got: 0x160
+  __AUTH_CONST.__const: 0x3f0
   __AUTH_CONST.__cfstring: 0x2100
   __AUTH_CONST.__objc_const: 0x7c8
   __AUTH_CONST.__objc_arrayobj: 0x390

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 206
-  Symbols:   615
+  Functions: 204
+  Symbols:   612
   CStrings:  275
 
Symbols:
+ -[SDRDiagnosticReporter commonPreflightChecksForSignature:payload:callback:].cold.1
+ -[SDRDiagnosticReporter commonPreflightChecksForSignature:payload:callback:].cold.2
+ GCC_except_table134
+ GCC_except_table56
+ GCC_except_table73
+ __105-[SDRDiagnosticReporter startSessionWithSignature:duration:events:payload:actions:wantsRemoteCase:reply:]_block_invoke.176
+ __105-[SDRDiagnosticReporter startSessionWithSignature:duration:events:payload:actions:wantsRemoteCase:reply:]_block_invoke_2.177
+ __56-[SDRDiagnosticReporter getAllDiagnosticCasesWithReply:]_block_invoke.194
+ __56-[SDRDiagnosticReporter getAllDiagnosticCasesWithReply:]_block_invoke.196
+ __56-[SDRDiagnosticReporter getAllDiagnosticCasesWithReply:]_block_invoke_2.197
+ __56-[SDRDiagnosticReporter getAutoBugCaptureConfiguration:]_block_invoke.216
+ __59-[SDRDiagnosticReporter addToSession:events:payload:reply:]_block_invoke.182
+ __64-[SDRDiagnosticReporter getDiagnosticCaseSummariesOfType:reply:]_block_invoke.202
+ __64-[SDRDiagnosticReporter getDiagnosticCaseSummariesOfType:reply:]_block_invoke_2.203
+ __66-[SDRDiagnosticReporter getDiagnosticPayloadsForSignatures:reply:]_block_invoke.184
+ __66-[SDRDiagnosticReporter getDiagnosticPayloadsForSignatures:reply:]_block_invoke.189
+ __66-[SDRDiagnosticReporter getDiagnosticPayloadsForSignatures:reply:]_block_invoke_2.190
+ __68-[SDRDiagnosticReporter purgeAutoBugCaptureFilesWithSubPaths:reply:]_block_invoke.211
+ __73-[SDRDiagnosticReporter addSignatureContentForSession:key:content:reply:]_block_invoke.183
+ __73-[SDRDiagnosticReporter getDiagnosticCaseSummariesWithIdentifiers:reply:]_block_invoke.204
+ __73-[SDRDiagnosticReporter getDiagnosticCaseSummariesWithIdentifiers:reply:]_block_invoke.207
+ __73-[SDRDiagnosticReporter getDiagnosticCaseSummariesWithIdentifiers:reply:]_block_invoke_2.208
+ __76-[SDRDiagnosticReporter triggerRemoteSessionForSignature:caseGroupID:reply:]_block_invoke.191
+ __94-[SDRDiagnosticReporter casesListCallbackWithResult:service:identifier:count:container:reply:]_block_invoke.193
+ __98-[SDRDiagnosticReporter snapshotWithSignature:delay:events:payload:actions:wantsRemoteCase:reply:]_block_invoke.173
+ ___98-[SDRDiagnosticReporter snapshotWithSignature:delay:events:payload:actions:wantsRemoteCase:reply:]_block_invoke_4
+ ___block_descriptor_48_e8_32s40s_e19_"NSDictionary"8?0l
+ __block_literal_global.179
+ __block_literal_global.181
+ _objc_retainAutoreleaseReturnValue
- GCC_except_table138
- GCC_except_table44
- GCC_except_table58
- GCC_except_table77
- __105-[SDRDiagnosticReporter startSessionWithSignature:duration:events:payload:actions:wantsRemoteCase:reply:]_block_invoke.174
- __105-[SDRDiagnosticReporter startSessionWithSignature:duration:events:payload:actions:wantsRemoteCase:reply:]_block_invoke_2.176
- __56-[SDRDiagnosticReporter getAllDiagnosticCasesWithReply:]_block_invoke.193
- __56-[SDRDiagnosticReporter getAllDiagnosticCasesWithReply:]_block_invoke.195
- __56-[SDRDiagnosticReporter getAllDiagnosticCasesWithReply:]_block_invoke_2.196
- __56-[SDRDiagnosticReporter getAutoBugCaptureConfiguration:]_block_invoke.215
- __59-[SDRDiagnosticReporter addToSession:events:payload:reply:]_block_invoke.181
- __64-[SDRDiagnosticReporter getDiagnosticCaseSummariesOfType:reply:]_block_invoke.200
- __64-[SDRDiagnosticReporter getDiagnosticCaseSummariesOfType:reply:]_block_invoke_2.202
- __66-[SDRDiagnosticReporter getDiagnosticPayloadsForSignatures:reply:]_block_invoke.183
- __66-[SDRDiagnosticReporter getDiagnosticPayloadsForSignatures:reply:]_block_invoke.188
- __66-[SDRDiagnosticReporter getDiagnosticPayloadsForSignatures:reply:]_block_invoke_2.189
- __68-[SDRDiagnosticReporter purgeAutoBugCaptureFilesWithSubPaths:reply:]_block_invoke.210
- __73-[SDRDiagnosticReporter addSignatureContentForSession:key:content:reply:]_block_invoke.182
- __73-[SDRDiagnosticReporter getDiagnosticCaseSummariesWithIdentifiers:reply:]_block_invoke.203
- __73-[SDRDiagnosticReporter getDiagnosticCaseSummariesWithIdentifiers:reply:]_block_invoke.206
- __73-[SDRDiagnosticReporter getDiagnosticCaseSummariesWithIdentifiers:reply:]_block_invoke_2.207
- __76-[SDRDiagnosticReporter triggerRemoteSessionForSignature:caseGroupID:reply:]_block_invoke.190
- __94-[SDRDiagnosticReporter casesListCallbackWithResult:service:identifier:count:container:reply:]_block_invoke.192
- __98-[SDRDiagnosticReporter snapshotWithSignature:delay:events:payload:actions:wantsRemoteCase:reply:]_block_invoke.171
- __98-[SDRDiagnosticReporter snapshotWithSignature:delay:events:payload:actions:wantsRemoteCase:reply:]_block_invoke.172
- ___block_descriptor_56_e8_32s40bs48r_e22_v16?0"NSDictionary"8l
- ___block_descriptor_72_e8_32s40w_e19_"NSDictionary"8?0l
- ___copy_helper_block_e8_32s40b48r
- ___copy_helper_block_e8_32s40w
- ___destroy_helper_block_e8_32s40s48r
- ___destroy_helper_block_e8_32s40w
- __block_literal_global.178
- __block_literal_global.180

```
