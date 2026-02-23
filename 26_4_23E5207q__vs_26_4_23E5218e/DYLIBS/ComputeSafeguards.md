## ComputeSafeguards

> `/System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards`

```diff

-4.100.40.502.2
-  __TEXT.__text: 0x3f1b0
-  __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_methlist: 0x3074
+4.100.48.0.0
+  __TEXT.__text: 0x3f51c
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_methlist: 0x3084
   __TEXT.__const: 0x260
-  __TEXT.__cstring: 0x40e1
-  __TEXT.__oslogstring: 0x8cbe
+  __TEXT.__cstring: 0x4163
+  __TEXT.__oslogstring: 0x8c73
   __TEXT.__gcc_except_tab: 0x86c
-  __TEXT.__unwind_info: 0xc58
+  __TEXT.__unwind_info: 0xc60
   __TEXT.__objc_classname: 0x3a1
-  __TEXT.__objc_methname: 0x8c1b
-  __TEXT.__objc_methtype: 0x1574
-  __TEXT.__objc_stubs: 0x4ee0
+  __TEXT.__objc_methname: 0x8c84
+  __TEXT.__objc_methtype: 0x1588
+  __TEXT.__objc_stubs: 0x4f20
   __DATA_CONST.__got: 0x250
-  __DATA_CONST.__const: 0x7c8
+  __DATA_CONST.__const: 0x818
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d28
+  __DATA_CONST.__objc_selrefs: 0x1d38
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xa8
-  __DATA_CONST.__objc_arraydata: 0x1120
-  __AUTH_CONST.__auth_got: 0x418
+  __DATA_CONST.__objc_arraydata: 0x11a0
+  __AUTH_CONST.__auth_got: 0x420
   __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x43a0
+  __AUTH_CONST.__cfstring: 0x4420
   __AUTH_CONST.__objc_const: 0x4698
-  __AUTH_CONST.__objc_intobj: 0x3a8
+  __AUTH_CONST.__objc_intobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x5c8
-  __AUTH_CONST.__objc_arrayobj: 0x240
+  __AUTH_CONST.__objc_arrayobj: 0x270
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x39c

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/PowerExceptions_ClientFramework.framework/PowerExceptions_ClientFramework
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
-  UUID: 5E2D94F2-307A-3311-A82A-6DA717C14FD4
-  Functions: 1431
-  Symbols:   4491
-  CStrings:  3334
+  UUID: 51BC7A95-0BCF-3565-B8B4-FBFE0281F7C8
+  Functions: 1434
+  Symbols:   4502
+  CStrings:  3345
 
Symbols:
+ -[CSIssueDetector logDetectionToCoreAnalytics:]
+ -[CSIssueDetector logDetectionToPowerlog:]
+ -[CSIssueDetector logDetectionToPowerlog:].cold.1
+ -[CSIssueDetector logDetectionToPowerlog:].cold.2
+ -[CSMitigationManager logMitigationToCoreAnalytics:withIssueType:withMitigationType:withReason:]
+ GCC_except_table48
+ GCC_except_table98
+ GCC_except_table99
+ _AnalyticsSendEventLazy
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.198
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.211
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.212
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.213
+ ___42-[CSIssueDetector logDetectionToPowerlog:]_block_invoke
+ ___47-[CSIssueDetector logDetectionToCoreAnalytics:]_block_invoke
+ ___96-[CSMitigationManager logMitigationToCoreAnalytics:withIssueType:withMitigationType:withReason:]_block_invoke
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_43_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_literal_global.179
+ ___block_literal_global.325
+ ___block_literal_global.737
+ _logDetectionToPowerlog:.onceToken
+ _logDetectionToPowerlog:.streamID
+ _objc_msgSend$initWithFilePath:withFlags:
+ _objc_msgSend$logDetectionToCoreAnalytics:
+ _objc_msgSend$logDetectionToPowerlog:
+ _objc_msgSend$logMitigationToCoreAnalytics:withIssueType:withMitigationType:withReason:
- -[CSIssueDetector logIssuesToPowerLogWithPayload:]
- -[CSIssueDetector logIssuesToPowerLogWithPayload:].cold.1
- -[CSIssueDetector logIssuesToPowerLogWithPayload:].cold.2
- -[CSMitigationManager logCPUViolationToPowerLog:pid:coalitionID:coalitionName:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:mitigationType:mitigationReason:withError:].cold.3
- GCC_except_table44
- GCC_except_table94
- GCC_except_table95
- ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.191
- ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.204
- ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.205
- ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.206
- ___50-[CSIssueDetector logIssuesToPowerLogWithPayload:]_block_invoke
- ___block_literal_global.178
- ___block_literal_global.318
- ___block_literal_global.734
- _logIssuesToPowerLogWithPayload:.onceToken
- _logIssuesToPowerLogWithPayload:.streamID
- _objc_msgSend$initWithFilePath:
- _objc_msgSend$logIssuesToPowerLogWithPayload:
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "Reason"
+ "com.apple.intelligencetasksd"
+ "com.apple.powerexceptions.detection"
+ "com.apple.powerexceptions.mitigations"
+ "initWithFilePath:withFlags:"
+ "logDetectionToCoreAnalytics:"
+ "logDetectionToPowerlog:"
+ "logMitigationToCoreAnalytics:withIssueType:withMitigationType:withReason:"
+ "v36@0:8@16C24C28C32"
- "initWithFilePath:"
- "logCPUViolationToPowerLog: timestampEnd is before timestampStart, skipping"
- "logIssuesToPowerLogWithPayload:"

```
