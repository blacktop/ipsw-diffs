## devicerecoveryd

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/Support/devicerecoveryd`

```diff

-103.40.3.0.0
-  __TEXT.__text: 0x21388
+103.40.3.0.5
+  __TEXT.__text: 0x21c0c
   __TEXT.__auth_stubs: 0xe80
-  __TEXT.__objc_stubs: 0x2140
-  __TEXT.__objc_methlist: 0xba4
-  __TEXT.__cstring: 0x67a0
+  __TEXT.__objc_stubs: 0x21c0
+  __TEXT.__objc_methlist: 0xbbc
+  __TEXT.__cstring: 0x68db
   __TEXT.__const: 0x58
-  __TEXT.__objc_methname: 0x2348
-  __TEXT.__oslogstring: 0x30ec
+  __TEXT.__objc_methname: 0x23d9
+  __TEXT.__oslogstring: 0x32b6
   __TEXT.__objc_classname: 0x125
-  __TEXT.__objc_methtype: 0x4d7
-  __TEXT.__gcc_except_tab: 0x6f0
-  __TEXT.__unwind_info: 0x620
+  __TEXT.__objc_methtype: 0x522
+  __TEXT.__gcc_except_tab: 0x704
+  __TEXT.__unwind_info: 0x638
   __DATA_CONST.__auth_got: 0x750
-  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xbd0
-  __DATA_CONST.__cfstring: 0x2300
+  __DATA_CONST.__const: 0xbd8
+  __DATA_CONST.__cfstring: 0x2460
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x13a0
-  __DATA.__objc_selrefs: 0xa38
+  __DATA_CONST.__objc_arraydata: 0x58
+  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA.__objc_const: 0x13a8
+  __DATA.__objc_selrefs: 0xa68
   __DATA.__objc_ivar: 0xb4
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x220

   - /System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DE5A6D6C-EC25-3F20-BBE9-D1A72FF0809C
-  Functions: 643
-  Symbols:   301
-  CStrings:  1718
+  UUID: DEB0EB0C-FDB7-39B2-A193-7D25D82F08DD
+  Functions: 650
+  Symbols:   302
+  CStrings:  1757
 
Symbols:
+ _OBJC_CLASS_$_OSASystemConfiguration
+ _objc_retain_x26
- _objc_retain_x25
CStrings:
+ "%{public}s: %{public}d"
+ "%{public}s: DRE entry reason cookie is not a number: %{public}s"
+ "%{public}s: Diagnostics Submission %{public}@"
+ "%{public}s: Got error fetching DT:/chosen entry %{public}@: %{public}@"
+ "%{public}s: No %{public}@ entry in the DT:/chosen node, the %{public}@ NVRAM var is not set and we don't have an entry reason cookie set"
+ "%{public}s: User %{public}@ opted in to sharing diagnostics"
+ "%{public}s: We have a DRE entry reason cookie, but it is not RECOVERY_REASON_CRITICAL_PROCESS_CRASH_LOOP (%u)"
+ "%{public}s: [DownloadRecoveryBrain]: Starting catalog download for DeviceRecoveryBrain | Options:%{public}@"
+ "%{public}s: failedOperation: %{public}@ - description: %{public}@ - diagnosticsSubmissionApproved: %{public}d"
+ "-[DeviceRecoveryService setDiagnosticsSubmissionApproved:completion:]"
+ "01:42:44"
+ "AppleArchive"
+ "AppleEncryptedArchive"
+ "AssetSpecifier"
+ "DeviceRecoveryBrain"
+ "DiagnosticsSubmissionApproved"
+ "OSVersion"
+ "Oct  6 2025"
+ "RequestingMAAutoAsset"
+ "StreamingZip"
+ "SupportedAssetFormats"
+ "TB,N,V_userApprovedDiagnosticsSubmission"
+ "[entry isKindOfClass:[NSNumber class]]"
+ "[entry unsignedIntValue] == RECOVERY_REASON_CRITICAL_PROCESS_CRASH_LOOP"
+ "_userApprovedDiagnosticsSubmission"
+ "entry != nil"
+ "err == nil"
+ "has"
+ "has not"
+ "productVersion"
+ "setAdditionalServerParams:"
+ "setDREOptIn:"
+ "setDiagnosticsSubmissionApproved:completion:"
+ "setSafeObject:forKey:"
+ "setUserApprovedDiagnosticsSubmission:"
+ "sharedInstance"
+ "true"
+ "userApprovedDiagnosticsSubmission"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?@\"NSError\"@\"NSDictionary\"@\"NSDictionary\">20"
- "%{public}s: Analytics Submission %@"
- "%{public}s: No entry reason: %{public}@"
- "%{public}s: [DownloadRecoveryBrain]: Starting catalog download for DeviceRecoveryBrain"
- "%{public}s: failedOperation: %{public}@ - description: %{public}@ - analyticsSubmissionApproved: %{public}d"
- "(dtRecoveryReasonData != nil) && (err == nil)"
- "22:12:17"
- "AnalyticsSubmissionApproved"
- "Sep 28 2025"
- "TB,N,V_userApprovedAnalyticsSubmission"
- "_userApprovedAnalyticsSubmission"
- "setUserApprovedAnalyticsSubmission:"
- "userApprovedAnalyticsSubmission"

```
