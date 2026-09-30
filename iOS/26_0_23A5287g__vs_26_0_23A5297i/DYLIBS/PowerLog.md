## PowerLog

> `/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`

```diff

-2964.0.64.0.0
-  __TEXT.__text: 0x26e3c
+2964.0.107.502.1
+  __TEXT.__text: 0x273dc
   __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_methlist: 0x1924
-  __TEXT.__const: 0xcf8
-  __TEXT.__gcc_except_tab: 0xc1c
-  __TEXT.__cstring: 0x23f5
-  __TEXT.__oslogstring: 0x403f
-  __TEXT.__unwind_info: 0xa68
+  __TEXT.__objc_methlist: 0x193c
+  __TEXT.__const: 0xd40
+  __TEXT.__gcc_except_tab: 0xc48
+  __TEXT.__cstring: 0x23d7
+  __TEXT.__oslogstring: 0x40e4
+  __TEXT.__unwind_info: 0xa98
   __TEXT.__objc_classname: 0x298
-  __TEXT.__objc_methname: 0x4d9c
-  __TEXT.__objc_methtype: 0xc57
-  __TEXT.__objc_stubs: 0x3a20
+  __TEXT.__objc_methname: 0x4e66
+  __TEXT.__objc_methtype: 0xd24
+  __TEXT.__objc_stubs: 0x3a40
   __DATA_CONST.__got: 0x1b0
-  __DATA_CONST.__const: 0x880
+  __DATA_CONST.__const: 0x7e8
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12b8
+  __DATA_CONST.__objc_selrefs: 0x12c8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__objc_arraydata: 0x170
+  __DATA_CONST.__objc_arraydata: 0x198
   __AUTH_CONST.__auth_got: 0x4d0
-  __AUTH_CONST.__const: 0x540
-  __AUTH_CONST.__cfstring: 0x2980
-  __AUTH_CONST.__objc_const: 0x25f8
-  __AUTH_CONST.__objc_intobj: 0x420
-  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__const: 0x560
+  __AUTH_CONST.__cfstring: 0x2920
+  __AUTH_CONST.__objc_const: 0x2608
+  __AUTH_CONST.__objc_intobj: 0x498
+  __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH.__objc_data: 0x320
   __DATA.__objc_ivar: 0x1c0
   __DATA.__data: 0x2b0
-  __DATA.__bss: 0x160
+  __DATA.__bss: 0x170
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__bss: 0x78

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: CEDE87B4-0ECB-357B-AE49-E558493156C0
-  Functions: 972
-  Symbols:   3112
-  CStrings:  2032
+  UUID: B614FCDE-FBF2-3329-A5A0-08D4642C62DC
+  Functions: 982
+  Symbols:   3139
+  CStrings:  2038
 
Symbols:
+ -[SafeguardsManagingClient resetRuleParameters:error:]
+ -[SafeguardsManagingClient setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:error:]
+ -[SafeguardsManagingClient setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:error:]
+ GCC_except_table121
+ GCC_except_table124
+ GCC_except_table139
+ GCC_except_table142
+ _PLBatteryBreakdownResponseTypes
+ _PLBatteryBreakdownResponseTypes.breakdownTypes
+ _PLBatteryBreakdownResponseTypes.cold.1
+ _PLBatteryBreakdownResponseTypes.onceToken
+ ___111-[SafeguardsManagingClient forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke.80
+ ___111-[SafeguardsManagingClient forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke.80.cold.1
+ ___111-[SafeguardsManagingClient setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:error:]_block_invoke
+ ___111-[SafeguardsManagingClient setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:error:]_block_invoke.78
+ ___111-[SafeguardsManagingClient setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:error:]_block_invoke.78.cold.1
+ ___111-[SafeguardsManagingClient setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:error:]_block_invoke.cold.1
+ ___131-[SafeguardsManagingClient setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:error:]_block_invoke
+ ___131-[SafeguardsManagingClient setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:error:]_block_invoke.74
+ ___131-[SafeguardsManagingClient setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:error:]_block_invoke.cold.1
+ ___49-[SafeguardsManagingClient forceMidnightRoutine:]_block_invoke.81
+ ___54-[SafeguardsManagingClient resetRuleParameters:error:]_block_invoke
+ ___54-[SafeguardsManagingClient resetRuleParameters:error:]_block_invoke.79
+ ___54-[SafeguardsManagingClient resetRuleParameters:error:]_block_invoke.79.cold.1
+ ___54-[SafeguardsManagingClient resetRuleParameters:error:]_block_invoke.cold.1
+ ___55-[SafeguardsManagingClient sendCoalitionEntries:error:]_block_invoke.85
+ ___55-[SafeguardsManagingClient sendCoalitionEntries:error:]_block_invoke.85.cold.1
+ ___62-[SafeguardsManagingClient forceCPUViolationForProcess:error:]_block_invoke.82
+ ___62-[SafeguardsManagingClient forceCPUViolationForProcess:error:]_block_invoke.82.cold.1
+ ___67-[SafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke.83
+ ___67-[SafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke.83.cold.1
+ ___70-[SafeguardsManagingClient forceDetectionWithStartTime:endTime:error:]_block_invoke.84
+ ___70-[SafeguardsManagingClient forceDetectionWithStartTime:endTime:error:]_block_invoke.84.cold.1
+ ___PLBatteryBreakdownResponseTypes_block_invoke
+ ___block_literal_global.161
+ ___block_literal_global.174
+ ___block_literal_global.184
+ ___block_literal_global.188
+ ___block_literal_global.189
+ ___block_literal_global.27
+ _objc_msgSend$modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:withHandler:
+ _objc_msgSend$resetRuleParameters:withHandler:
+ _objc_msgSend$setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:withHandler:
+ _objc_retain_x27
- +[PLModelingUtilities alsCurveHigherThanDefault]
- +[PLModelingUtilities getDefaultL0bThresholdForDeviceType]
- -[SafeguardsManagingClient setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:error:]
- GCC_except_table133
- GCC_except_table136
- _CFPreferencesCopyValue
- ___111-[SafeguardsManagingClient forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke.78
- ___111-[SafeguardsManagingClient forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke.78.cold.1
- ___116-[SafeguardsManagingClient setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:error:]_block_invoke
- ___116-[SafeguardsManagingClient setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:error:]_block_invoke.74
- ___116-[SafeguardsManagingClient setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:error:]_block_invoke.cold.1
- ___49-[SafeguardsManagingClient forceMidnightRoutine:]_block_invoke.79
- ___55-[SafeguardsManagingClient sendCoalitionEntries:error:]_block_invoke.83
- ___55-[SafeguardsManagingClient sendCoalitionEntries:error:]_block_invoke.83.cold.1
- ___62-[SafeguardsManagingClient forceCPUViolationForProcess:error:]_block_invoke.80
- ___62-[SafeguardsManagingClient forceCPUViolationForProcess:error:]_block_invoke.80.cold.1
- ___67-[SafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke.81
- ___67-[SafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke.81.cold.1
- ___70-[SafeguardsManagingClient forceDetectionWithStartTime:endTime:error:]_block_invoke.82
- ___70-[SafeguardsManagingClient forceDetectionWithStartTime:endTime:error:]_block_invoke.82.cold.1
- ___block_literal_global.157
- ___block_literal_global.183
- ___block_literal_global.198
- ___block_literal_global.205
- ___block_literal_global.215
- ___block_literal_global.220
- _objc_msgSend$getDefaultL0bThresholdForDeviceType
- _objc_msgSend$modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withHandler:
CStrings:
+ "B72@0:8@16@24@32@40@48@56^@64"
+ "Failed to reset rule parameters %@"
+ "Failed to set rule parameters %@"
+ "IOSUISOCDrain"
+ "modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:withHandler:"
+ "q"
+ "resetRuleParameters:error:"
+ "resetRuleParameters:withHandler:"
+ "setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:error:"
+ "setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:error:"
+ "setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:withHandler:"
+ "v32@0:8@\"NSNumber\"16@?<v@?@\"NSError\">24"
+ "v64@0:8@\"NSNumber\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@?<v@?@\"NSError\">56"
+ "v72@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@\"NSNumber\"56@?<v@?@\"NSError\">64"
+ "v72@0:8@16@24@32@40@48@56@?64"
+ "xpcSendMessage: xpc connection is not valid"
+ "xpcSendMessageWithReply: xpc connection is not valid"
- "BKALSUserPreferences"
- "L0b"
- "alsCurveHigherThanDefault"
- "com.apple.backboardd"
- "getDefaultL0bThresholdForDeviceType"
- "modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withHandler:"
- "setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:error:"
- "v64@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@?<v@?@\"NSError\">56"

```
