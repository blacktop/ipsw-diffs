## DeviceRecovery

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/DeviceRecovery`

```diff

-103.40.3.0.0
-  __TEXT.__text: 0x1f4dc
+103.40.3.0.5
+  __TEXT.__text: 0x1fe0c
   __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x5dc
+  __TEXT.__objc_methlist: 0x5e8
   __TEXT.__const: 0x188
   __TEXT.__gcc_except_tab: 0x2d4
-  __TEXT.__cstring: 0x3b1b
-  __TEXT.__oslogstring: 0xcf4
-  __TEXT.__unwind_info: 0x5a0
+  __TEXT.__cstring: 0x3c07
+  __TEXT.__oslogstring: 0xe90
+  __TEXT.__unwind_info: 0x5c0
   __TEXT.__objc_classname: 0xa2
-  __TEXT.__objc_methname: 0x103f
-  __TEXT.__objc_methtype: 0x28a
-  __TEXT.__objc_stubs: 0xa00
+  __TEXT.__objc_methname: 0x1074
+  __TEXT.__objc_methtype: 0x2d5
+  __TEXT.__objc_stubs: 0xa20
   __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x4b8
+  __DATA_CONST.__const: 0x4e0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x480
+  __DATA_CONST.__objc_selrefs: 0x488
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__auth_got: 0x330
-  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0xea0
-  __AUTH_CONST.__objc_const: 0x780
+  __AUTH_CONST.__objc_const: 0x788
   __AUTH_CONST.__objc_intobj: 0x48
   __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0xca

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7AA40059-6C93-354A-A0B8-C3DA8BDF5A95
-  Functions: 735
-  Symbols:   1642
-  CStrings:  829
+  UUID: CB8C598B-54ED-3780-9265-089FB88C5C23
+  Functions: 747
+  Symbols:   1675
+  CStrings:  841
 
Symbols:
+ -[DeviceRecoveryController setUserApprovedDiagnosticsSubmission:]
+ -[DeviceRecoveryController setUserApprovedDiagnosticsSubmission:].cold.1
+ -[DeviceRecoveryController setUserApprovedDiagnosticsSubmission:].cold.2
+ -[DeviceRecoveryController userApprovedDiagnosticsSubmission]
+ -[DeviceRecoveryEnvironmentWorker populateDREReason].cold.5
+ -[DeviceRecoveryEnvironmentWorker populateDREReason].cold.6
+ -[DeviceRecoveryEnvironmentWorker populateDREReason].cold.7
+ -[DeviceRecoveryEnvironmentWorker populateDREReason].cold.8
+ -[DeviceRecoveryEnvironmentWorker populateDREReason].cold.9
+ GCC_except_table112
+ GCC_except_table113
+ GCC_except_table114
+ GCC_except_table18
+ GCC_except_table84
+ _DRServiceAttributeDiagnosticsSubmissionApproved
+ _DRUserAuthParamDiagnosticsSubmissionApproved
+ _OBJC_IVAR_$_DeviceRecoveryController._userApprovedDiagnosticsSubmission
+ ___32-[DeviceRecoveryController init]_block_invoke.32
+ ___32-[DeviceRecoveryController init]_block_invoke.33
+ ___32-[DeviceRecoveryController init]_block_invoke.33.cold.1
+ ___32-[DeviceRecoveryController init]_block_invoke.38
+ ___32-[DeviceRecoveryController init]_block_invoke.38.cold.1
+ ___32-[DeviceRecoveryController init]_block_invoke.38.cold.2
+ ___32-[DeviceRecoveryController init]_block_invoke.38.cold.3
+ ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.63
+ ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.63.cold.1
+ ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.63.cold.2
+ ___52-[DeviceRecoveryController disableRecoveryAutoBoot:]_block_invoke.94
+ ___52-[DeviceRecoveryController disableRecoveryAutoBoot:]_block_invoke.94.cold.1
+ ___54-[DeviceRecoveryController recoverDeviceFromBootedOS:]_block_invoke.93
+ ___54-[DeviceRecoveryController recoverDeviceFromBootedOS:]_block_invoke.93.cold.1
+ ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.91
+ ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.91.cold.1
+ ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.91.cold.2
+ ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.90
+ ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.90.cold.1
+ ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.90.cold.2
+ ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.62
+ ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.62.cold.1
+ ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.62.cold.2
+ ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.86
+ ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.86.cold.1
+ ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.87
+ ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.87.cold.1
+ ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.87.cold.2
+ ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.89
+ ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.89.cold.1
+ ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.89.cold.2
+ ___65-[DeviceRecoveryController setUserApprovedDiagnosticsSubmission:]_block_invoke
+ ___65-[DeviceRecoveryController setUserApprovedDiagnosticsSubmission:]_block_invoke.47
+ ___65-[DeviceRecoveryController setUserApprovedDiagnosticsSubmission:]_block_invoke.47.cold.1
+ ___65-[DeviceRecoveryController setUserApprovedDiagnosticsSubmission:]_block_invoke.cold.1
+ ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.88
+ ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.88.cold.1
+ ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.88.cold.2
+ ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.92
+ ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.92.cold.1
+ ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.92.cold.2
+ ___78-[DeviceRecoveryController loadAccessibilitySettingsToDefaultsWithCompletion:]_block_invoke.95
+ ___78-[DeviceRecoveryController loadAccessibilitySettingsToDefaultsWithCompletion:]_block_invoke.95.cold.1
+ ___block_descriptor_32_e51_v32?0"NSError"8"NSDictionary"16"NSDictionary"24l
+ ___block_literal_global.31
+ ___block_literal_global.36
+ ___block_literal_global.45
+ ___block_literal_global.49
+ _objc_msgSend$setDiagnosticsSubmissionApproved:completion:
+ _objc_msgSend$userApprovedDiagnosticsSubmission
- -[DeviceRecoveryController setUserApprovedAnalyticsSubmission:]
- -[DeviceRecoveryController userApprovedAnalyticsSubmission]
- GCC_except_table106
- GCC_except_table107
- GCC_except_table108
- GCC_except_table15
- GCC_except_table82
- _DRUserAuthParamAnalyticsSubmissionApproved
- _OBJC_IVAR_$_DeviceRecoveryController._userApprovedAnalyticsSubmission
- ___32-[DeviceRecoveryController init]_block_invoke.29
- ___32-[DeviceRecoveryController init]_block_invoke.30
- ___32-[DeviceRecoveryController init]_block_invoke.30.cold.1
- ___32-[DeviceRecoveryController init]_block_invoke.35
- ___32-[DeviceRecoveryController init]_block_invoke.35.cold.1
- ___32-[DeviceRecoveryController init]_block_invoke.35.cold.2
- ___32-[DeviceRecoveryController init]_block_invoke.35.cold.3
- ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.53
- ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.53.cold.1
- ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.53.cold.2
- ___52-[DeviceRecoveryController disableRecoveryAutoBoot:]_block_invoke.84
- ___52-[DeviceRecoveryController disableRecoveryAutoBoot:]_block_invoke.84.cold.1
- ___54-[DeviceRecoveryController recoverDeviceFromBootedOS:]_block_invoke.83
- ___54-[DeviceRecoveryController recoverDeviceFromBootedOS:]_block_invoke.83.cold.1
- ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.81
- ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.81.cold.1
- ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.81.cold.2
- ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.80
- ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.80.cold.1
- ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.80.cold.2
- ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.52
- ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.52.cold.1
- ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.52.cold.2
- ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.76
- ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.76.cold.1
- ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.77
- ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.77.cold.1
- ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.77.cold.2
- ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.79
- ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.79.cold.1
- ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.79.cold.2
- ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.78
- ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.78.cold.1
- ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.78.cold.2
- ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.82
- ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.82.cold.1
- ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.82.cold.2
- ___78-[DeviceRecoveryController loadAccessibilitySettingsToDefaultsWithCompletion:]_block_invoke.85
- ___78-[DeviceRecoveryController loadAccessibilitySettingsToDefaultsWithCompletion:]_block_invoke.85.cold.1
- ___block_literal_global.28
- _objc_msgSend$userApprovedAnalyticsSubmission
CStrings:
+ "%{public}s: DRE entry reason cookie is not a number: %{public}s"
+ "%{public}s: Failed to set diagnostics submission approval: %{public}@"
+ "%{public}s: Got error fetching DT:/chosen entry %{public}@: %{public}@"
+ "%{public}s: No %{public}@ entry in the DT:/chosen node, the %{public}@ NVRAM var is not set and we don't have an entry reason cookie set"
+ "%{public}s: We have a DRE entry reason cookie, but it is not RECOVERY_REASON_CRITICAL_PROCESS_CRASH_LOOP (%u)"
+ "-[DeviceRecoveryController setUserApprovedDiagnosticsSubmission:]"
+ "-[DeviceRecoveryController setUserApprovedDiagnosticsSubmission:]_block_invoke"
+ "DiagnosticsSubmissionApproved"
+ "TB,N,V_userApprovedDiagnosticsSubmission"
+ "[entry isKindOfClass:[NSNumber class]]"
+ "[entry unsignedIntValue] == RECOVERY_REASON_CRITICAL_PROCESS_CRASH_LOOP"
+ "_userApprovedDiagnosticsSubmission"
+ "entry != nil"
+ "err == nil"
+ "setDiagnosticsSubmissionApproved:completion:"
+ "setUserApprovedDiagnosticsSubmission:"
+ "userApprovedDiagnosticsSubmission"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?@\"NSError\"@\"NSDictionary\"@\"NSDictionary\">20"
- "%{public}s: No entry reason: %{public}@"
- "(dtRecoveryReasonData != nil) && (err == nil)"
- "AnalyticsSubmissionApproved"
- "TB,N,V_userApprovedAnalyticsSubmission"
- "_userApprovedAnalyticsSubmission"
- "setUserApprovedAnalyticsSubmission:"
- "userApprovedAnalyticsSubmission"

```
