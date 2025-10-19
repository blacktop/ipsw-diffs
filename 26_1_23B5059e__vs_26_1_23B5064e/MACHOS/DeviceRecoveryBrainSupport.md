## DeviceRecoveryBrainSupport

> `/System/Library/PrivateFrameworks/DeviceRecoveryBrainSupport.framework/DeviceRecoveryBrainSupport`

```diff

-103.40.3.0.0
-  __TEXT.__text: 0x1d35c
+103.40.3.0.5
+  __TEXT.__text: 0x1d860
   __TEXT.__auth_stubs: 0xbd0
   __TEXT.__objc_methlist: 0xd1c
   __TEXT.__const: 0x150
-  __TEXT.__oslogstring: 0x2a9b
-  __TEXT.__cstring: 0x3d12
+  __TEXT.__oslogstring: 0x2bf1
+  __TEXT.__cstring: 0x3d6d
   __TEXT.__gcc_except_tab: 0x5bc
-  __TEXT.__unwind_info: 0x550
+  __TEXT.__unwind_info: 0x560
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_classname: 0x16b
   __TEXT.__objc_methname: 0x209d
   __TEXT.__objc_methtype: 0x490
   __TEXT.__objc_stubs: 0x1bc0
   __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x8f8
+  __DATA_CONST.__const: 0x900
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20

   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 248977A7-1F86-3ED3-8041-54127CA6A817
-  Functions: 524
-  Symbols:   1319
-  CStrings:  1464
+  UUID: 8D9CD6A2-73F3-3E27-8ABF-F2AC6C8B57B4
+  Functions: 529
+  Symbols:   1328
+  CStrings:  1470
 
Symbols:
+ -[DeviceRecoveryEnvironmentWorker populateDREReason].cold.5
+ -[DeviceRecoveryEnvironmentWorker populateDREReason].cold.6
+ -[DeviceRecoveryEnvironmentWorker populateDREReason].cold.7
+ -[DeviceRecoveryEnvironmentWorker populateDREReason].cold.8
+ -[DeviceRecoveryEnvironmentWorker populateDREReason].cold.9
+ _DRServiceAttributeDiagnosticsSubmissionApproved
+ _DRUserAuthParamDiagnosticsSubmissionApproved
- _DRUserAuthParamAnalyticsSubmissionApproved
CStrings:
+ "%{public}s: DRE entry reason cookie is not a number: %{public}s"
+ "%{public}s: Got error fetching DT:/chosen entry %{public}@: %{public}@"
+ "%{public}s: No %{public}@ entry in the DT:/chosen node, the %{public}@ NVRAM var is not set and we don't have an entry reason cookie set"
+ "%{public}s: We have a DRE entry reason cookie, but it is not RECOVERY_REASON_CRITICAL_PROCESS_CRASH_LOOP (%u)"
+ "DiagnosticsSubmissionApproved"
+ "[entry isKindOfClass:[NSNumber class]]"
+ "[entry unsignedIntValue] == RECOVERY_REASON_CRITICAL_PROCESS_CRASH_LOOP"
+ "entry != nil"
+ "err == nil"
- "%{public}s: No entry reason: %{public}@"
- "(dtRecoveryReasonData != nil) && (err == nil)"
- "AnalyticsSubmissionApproved"

```
