## AutoBugCaptureCore

> `/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/Versions/A/AutoBugCaptureCore`

```diff

-358.0.0.0.0
-  __TEXT.__text: 0x7cd48
+362.0.0.0.0
+  __TEXT.__text: 0x7ce7c
   __TEXT.__auth_stubs: 0xd70
   __TEXT.__objc_methlist: 0x54b0
-  __TEXT.__cstring: 0x4b31
+  __TEXT.__cstring: 0x4b30
   __TEXT.__const: 0x268
-  __TEXT.__oslogstring: 0xdf02
-  __TEXT.__gcc_except_tab: 0x1090
+  __TEXT.__oslogstring: 0xdfaf
+  __TEXT.__gcc_except_tab: 0x108c
   __TEXT.__ustring: 0x8
-  __TEXT.diag_actions: 0x49b8
+  __TEXT.diag_actions: 0x4f9d
   __TEXT.__unwind_info: 0x1598
   __TEXT.__objc_classname: 0x989
   __TEXT.__objc_methname: 0xd6a1
Symbols:
+ __103-[DiagnosticCaseManager startSessionWithSignature:flags:preferredTimeout:events:payload:actions:reply:]_block_invoke.733
+ __103-[DiagnosticCaseManager startSessionWithSignature:flags:preferredTimeout:events:payload:actions:reply:]_block_invoke.736
+ __49-[DiagnosticCaseManager isAdmissible:dampenedBy:]_block_invoke.625
+ __53-[DiagnosticCaseManager payloadsForSignatures:reply:]_block_invoke.756
+ __55-[DiagnosticCaseManager _updateCaseStatisticsWithCase:]_block_invoke.638
+ __63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.693
+ __63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.697
+ __63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.703
+ __63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.707
+ __63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.714
+ __63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.716
+ __63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke_2.715
+ __65-[DiagnosticCaseManager addToSession:events:payload:queue:reply:]_block_invoke.732
+ __68-[DiagnosticCaseManager dampeningFactorForSignature:caseTime:limit:]_block_invoke.588
+ __70-[DiagnosticCaseManager requestGroupCaseIdentifierForSignature:reply:]_block_invoke.628
+ __86-[DiagnosticCaseManager _processRemoteIDSTriggers:validFor:signature:sessionID:reply:]_block_invoke.668
+ __86-[DiagnosticCaseManager _processRemoteIDSTriggers:validFor:signature:sessionID:reply:]_block_invoke.673
+ __block_literal_global.723
- __103-[DiagnosticCaseManager startSessionWithSignature:flags:preferredTimeout:events:payload:actions:reply:]_block_invoke.732
- __103-[DiagnosticCaseManager startSessionWithSignature:flags:preferredTimeout:events:payload:actions:reply:]_block_invoke.735
- __49-[DiagnosticCaseManager isAdmissible:dampenedBy:]_block_invoke.624
- __53-[DiagnosticCaseManager payloadsForSignatures:reply:]_block_invoke.755
- __55-[DiagnosticCaseManager _updateCaseStatisticsWithCase:]_block_invoke.637
- __63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.692
- __63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.696
- __63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.702
- __63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.706
- __63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.713
- __63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke.715
- __63-[DiagnosticCaseManager startPacketCaptureForSession:duration:]_block_invoke_2.714
- __65-[DiagnosticCaseManager addToSession:events:payload:queue:reply:]_block_invoke.731
- __70-[DiagnosticCaseManager requestGroupCaseIdentifierForSignature:reply:]_block_invoke.627
- __86-[DiagnosticCaseManager _processRemoteIDSTriggers:validFor:signature:sessionID:reply:]_block_invoke.666
- __86-[DiagnosticCaseManager _processRemoteIDSTriggers:validFor:signature:sessionID:reply:]_block_invoke.672
- ___68-[DiagnosticCaseManager dampeningFactorForSignature:caseTime:limit:]_block_invoke_2
- __block_literal_global.722
CStrings:
+ "AutoBugCapture case for %!@(MISSING), type:%!@(MISSING) subtype:%!@(MISSING)"
- "AutoBugCapture case for %!@(MISSING), type: %!@(MISSING) subtype:%!@(MISSING)"

```
