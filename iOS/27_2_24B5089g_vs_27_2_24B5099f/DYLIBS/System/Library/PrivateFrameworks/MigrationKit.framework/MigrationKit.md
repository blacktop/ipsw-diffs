## MigrationKit

> `/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit`

```diff

-1439.0.0.0.0
-  __TEXT.__text: 0x761b70
-  __TEXT.__objc_methlist: 0x6fcc
-  __TEXT.__const: 0x3c648
-  __TEXT.__oslogstring: 0x10b5c
-  __TEXT.__cstring: 0x1b4f1
-  __TEXT.__gcc_except_tab: 0x16b8
-  __TEXT.__constg_swiftt: 0x100dc
-  __TEXT.__swift5_typeref: 0xcdbd
-  __TEXT.__swift5_builtin: 0x370
-  __TEXT.__swift5_reflstr: 0xd8b2
-  __TEXT.__swift5_fieldmd: 0xeb90
-  __TEXT.__swift5_assocty: 0x2488
-  __TEXT.__swift5_proto: 0x2518
-  __TEXT.__swift5_types: 0xdd0
-  __TEXT.__swift_as_entry: 0x1864
-  __TEXT.__swift_as_ret: 0x1da8
-  __TEXT.__swift_as_cont: 0x43f4
-  __TEXT.__swift5_capture: 0x434c
+1441.40.1.0.0
+  __TEXT.__text: 0x77975c
+  __TEXT.__objc_methlist: 0x712c
+  __TEXT.__const: 0x3ced8
+  __TEXT.__oslogstring: 0x110dc
+  __TEXT.__cstring: 0x1bb91
+  __TEXT.__gcc_except_tab: 0x16f8
+  __TEXT.__constg_swiftt: 0x10264
+  __TEXT.__swift5_typeref: 0xcf21
+  __TEXT.__swift5_builtin: 0x384
+  __TEXT.__swift5_reflstr: 0xdd62
+  __TEXT.__swift5_fieldmd: 0xeee4
+  __TEXT.__swift5_assocty: 0x2500
+  __TEXT.__swift5_proto: 0x2560
+  __TEXT.__swift5_types: 0xdec
+  __TEXT.__swift_as_entry: 0x18ec
+  __TEXT.__swift_as_ret: 0x1e20
+  __TEXT.__swift_as_cont: 0x44bc
+  __TEXT.__swift5_capture: 0x44cc
   __TEXT.__swift5_protos: 0x160
   __TEXT.__swift5_mpenum: 0xdc
   __TEXT.__swift5_types2: 0x8
-  __TEXT.__unwind_info: 0x1eca8
-  __TEXT.__eh_frame: 0x4c280
+  __TEXT.__unwind_info: 0x1eb50
+  __TEXT.__eh_frame: 0x4d028
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xbb0
+  __DATA_CONST.__const: 0xc18
   __DATA_CONST.__objc_classlist: 0xc80
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x2b8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4d60
+  __DATA_CONST.__objc_selrefs: 0x4eb0
   __DATA_CONST.__objc_protorefs: 0x120
   __DATA_CONST.__objc_superrefs: 0x340
   __DATA_CONST.__objc_arraydata: 0x488
-  __DATA_CONST.__got: 0x2418
-  __AUTH_CONST.__const: 0x1d428
-  __AUTH_CONST.__cfstring: 0x5780
-  __AUTH_CONST.__objc_const: 0x1cc28
+  __DATA_CONST.__got: 0x2440
+  __AUTH_CONST.__const: 0x1db68
+  __AUTH_CONST.__cfstring: 0x57e0
+  __AUTH_CONST.__objc_const: 0x1ce80
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0xcc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x210
-  __AUTH_CONST.__auth_got: 0x35a8
-  __AUTH.__objc_data: 0x7d80
-  __AUTH.__data: 0x18228
-  __DATA.__objc_ivar: 0x7ec
-  __DATA.__data: 0xec28
+  __AUTH_CONST.__auth_got: 0x35a0
+  __AUTH.__objc_data: 0x7d98
+  __AUTH.__data: 0x18368
+  __DATA.__objc_ivar: 0x80c
+  __DATA.__data: 0xed20
   __DATA.__common: 0x1bb8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal
   - /System/Library/PrivateFrameworks/AsyncAlgorithmsInternal.framework/AsyncAlgorithmsInternal
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CallHistory.framework/CallHistory

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 26559
-  Symbols:   10484
-  CStrings:  4486
+  Functions: 26827
+  Symbols:   10575
+  CStrings:  4534
 
Symbols:
+ -[MKAPIServer migrator:didImportItemCount:]
+ -[MKAPIServer migrator:willImportItemCount:]
+ -[MKAPIServer migratorDidFinishImportingItems:]
+ -[MKAPIServer progress]
+ -[MKAPIServer resetImportState]
+ -[MKAPIServer updateItemCounts:coalesce:]
+ -[MKMessage isAccountDeclared]
+ -[MKMessage rcsGroupID]
+ -[MKMessage rcsGroupName]
+ -[MKMessage rcsGroupURI]
+ -[MKMessage setIsAccountDeclared:]
+ -[MKMessage setRcsGroupID:]
+ -[MKMessage setRcsGroupName:]
+ -[MKMessage setRcsGroupURI:]
+ -[MKMigrator migratorDidFinishImportingItems]
+ -[MKMigrator migratorDidImportItemCount:]
+ -[MKMigrator migratorWillImportItemCount:]
+ -[MKProgress addCompletedItemCount:]
+ -[MKProgress addCompletedOperationCount:]
+ -[MKProgress addTotalItemCount:]
+ -[MKProgress completedItemCount]
+ -[MKProgress resetItemCounts]
+ -[MKProgress snapCompletedItemCountToTotal]
+ -[MKProgress totalItemCount]
+ GCC_except_table20
+ GCC_except_table37
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table43
+ GCC_except_table45
+ GCC_except_table50
+ _AVFoundationErrorDomain
+ _BGSystemTaskSchedulerErrorDomain
+ _NSOSStatusErrorDomain
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_IVAR_$_MKAPIServer._itemCountNotificationTime
+ _OBJC_IVAR_$_MKMessage._isAccountDeclared
+ _OBJC_IVAR_$_MKMessage._rcsGroupID
+ _OBJC_IVAR_$_MKMessage._rcsGroupName
+ _OBJC_IVAR_$_MKMessage._rcsGroupURI
+ _OBJC_IVAR_$_MKProgress._completedItemCount
+ _OBJC_IVAR_$_MKProgress._didLogItemCountOvershoot
+ _OBJC_IVAR_$_MKProgress._totalItemCount
+ __PROPERTIES__TtC12MigrationKit18MessageTransformer
+ __PROTOCOL_INSTANCE_METHODS_OPT__TtP12MigrationKit9XPCClient_
+ ___27-[MKMessageMigrator import]_block_invoke_2
+ ___43-[MKAPIServer migrator:didImportItemCount:]_block_invoke
+ ___44-[MKAPIServer migrator:willImportItemCount:]_block_invoke
+ ___47-[MKAPIServer migratorDidFinishImportingItems:]_block_invoke
+ ___block_descriptor_32_e20_v16?0"MKProgress"8l
+ ___block_descriptor_40_e20_v16?0"MKProgress"8l
+ ___block_descriptor_40_e8_32s_e8_v16?0Q8ls32l8
+ ___swift_closure_destructor.142Tm
+ ___swift_closure_destructor.234Tm
+ ___swift_closure_destructor.23Tm
+ ___swift_closure_destructor.42Tm
+ ___swift_closure_destructor.4Tm
+ ___swift_get_extra_inhabitant_index.42Tm
+ ___swift_memcpy168_8
+ ___swift_memcpy18_8
+ ___swift_memcpy224_8
+ ___swift_memcpy73_8
+ ___swift_store_extra_inhabitant_index.43Tm
+ _associated conformance 12MigrationKit16TransferEndPhaseOSHAASQ
+ _associated conformance 12MigrationKit16TransferEndPhaseOSLAASQ
+ _associated conformance 12MigrationKit20TransferCancelOriginOSHAASQ
+ _associated conformance 12MigrationKit9FinalPaneOSHAASQ
+ _associated conformance SC30BGSystemTaskSchedulerErrorCodeLeV10Foundation021_ObjectiveCBridgeableD0SCs0D0
+ _associated conformance SC30BGSystemTaskSchedulerErrorCodeLeV10Foundation13CustomNSErrorSCs0D0
+ _associated conformance SC30BGSystemTaskSchedulerErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0E0AcDP_8RawValueSYs17FixedWidthInteger
+ _associated conformance SC30BGSystemTaskSchedulerErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0E0AcDP_AC01_dE8Protocol
+ _associated conformance SC30BGSystemTaskSchedulerErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0E0AcDP_SY
+ _associated conformance SC30BGSystemTaskSchedulerErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC021_ObjectiveCBridgeableD0
+ _associated conformance SC30BGSystemTaskSchedulerErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC06CustomI0
+ _associated conformance SC30BGSystemTaskSchedulerErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCSH
+ _associated conformance SC30BGSystemTaskSchedulerErrorCodeLeVSHSCSQ
+ _associated conformance So30BGSystemTaskSchedulerErrorCodeV10Foundation01_dE8ProtocolSC01_D4TypeAcDP_AC21_BridgedStoredNSError
+ _associated conformance So30BGSystemTaskSchedulerErrorCodeV10Foundation01_dE8ProtocolSCSQ
+ _nw_parameters_set_prohibit_parallel_connection_attempts
+ _symbolic SS_ShySiGt
+ _symbolic SS______pIeghHrzo_ s5ErrorP
+ _symbolic ScTySS______pG s5ErrorP
+ _symbolic SiSS______pIeghHyrzo_ s5ErrorP
+ _symbolic So12BGSystemTaskC
+ _symbolic _____ 12MigrationKit16TransferEndPhaseO
+ _symbolic _____ 12MigrationKit20TransferCancelOriginO
+ _symbolic _____ 12MigrationKit21TransferCancelContextV
+ _symbolic _____ 12MigrationKit27AppContentTelemetryBackstopO
+ _symbolic _____ 12MigrationKit9FinalPaneO
+ _symbolic _____ SC30BGSystemTaskSchedulerErrorCodeLeV
+ _symbolic _____ So30BGSystemTaskSchedulerErrorCodeV
+ _symbolic _____Ieghy_Sg s6UInt64V
+ _symbolic _____IeyBhy_ s6UInt64V
+ _symbolic _____Sg 12MigrationKit21TransferCancelContextV
+ _symbolic _____Sg 12MigrationKit9FinalPaneO
+ _symbolic _____ySSShySiGG s18_DictionaryStorageC
+ _symbolic _____ySS______p_G Scg8IteratorV s5ErrorP
+ _symbolic _____ySbG 2os21OSAllocatedUnfairLockV
+ _symbolic _____ySb_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic _____ySiG s11_SetStorageC
+ _symbolic _____y______G 12MigrationKit16AnalyticsPayload33_703A8D8B92D72B2764A7A61BBD4D883ELLC5FieldV AA9FinalPaneO
+ _symbolic y_____cSg s6UInt16V
+ _type_layout_string 12MigrationKit21TransferCancelContextV
+ _type_layout_string SC30BGSystemTaskSchedulerErrorCodeLeV
- -[MKProgress addCompletedOerationCount:]
- GCC_except_table22
- GCC_except_table23
- GCC_except_table24
- GCC_except_table34
- ___swift_closure_destructor.133Tm
- ___swift_closure_destructor.228Tm
- ___swift_closure_destructor.36Tm
- ___swift_get_extra_inhabitant_index.46Tm
- ___swift_memcpy192_8
- ___swift_store_extra_inhabitant_index.47Tm
- _symbolic _____y_____G 2os21OSAllocatedUnfairLockV s5Int64V
- _symbolic _____y__________G s13ManagedBufferCsRi__rlE s5Int64V So16os_unfair_lock_sV
- _type_layout_string SC7DCErrorLeV
CStrings:
+ " was not shared."
+ "%@ finished importing short of its staged total; snapping the displayed count. completedItemCount=%llu, totalItemCount=%llu, shortfall=%llu"
+ "%@ imported more items than it staged; clamping the displayed count. completedItemCount=%llu, count=%llu, totalItemCount=%llu"
+ ", is_tester_host="
+ "A backstop wake is already running. Leaving the schedule to it."
+ "AMS request encoding timed out"
+ "API request timed out"
+ "Armed the app content telemetry backstop"
+ "Cancelled the app content telemetry backstop"
+ "Deadline for a single Media API encode or request step, in seconds"
+ "Failed to arm the app content telemetry backstop"
+ "Failed to cancel the app content telemetry backstop"
+ "Failed to fetch unresolved app bundle identifiers"
+ "Failed to register the app content telemetry backstop handler"
+ "Failed to report the backstop pass as expired"
+ "Failed to resolve the App Store storefront; deferring every app to the static mappings"
+ "Maximum attempts to resolve the App Store storefront from the AMS bag before deferring every app to the static mappings"
+ "MigrationKit/AppContentTelemetryBackstop.swift"
+ "No pending import telemetry. Cancelling any schedule."
+ "Peer cancelled: "
+ "Re-arming the app content telemetry backstop for another deadline"
+ "Registered the app content telemetry backstop handler"
+ "Resolving app content rows that never completed. count=%{public}ld"
+ "Seconds before the app content telemetry backstop wakes to send whatever is pending. Lower it to test the wake."
+ "TEST ONLY. Skips recording app content import successes, so metrics rows stay unresolved and only the telemetry backstop can send the batch. Does not affect the real data import."
+ "The app content telemetry backstop is already armed"
+ "The app content telemetry backstop woke"
+ "The backstop could not open the import metrics store"
+ "The backstop could not send the batch. It will retry on the next wake. remainingRows=%{public}ld"
+ "The backstop expired before it could run"
+ "The backstop found no pending import metrics"
+ "The backstop sent the pending batch"
+ "The batch was already sent. Cleaning up the leftover state."
+ "_run(estimation:contexts:onImported:)"
+ "appContentTelemetryBackstopInterval"
+ "appStoreStorefrontMaxAttempts"
+ "asPeerCancelContext"
+ "com.apple.brm.Android-OS-Migration-Tester"
+ "com.apple.migrationd.appcontent-telemetry-flush"
+ "encodeAMSRequest() timed out after %{public}s for %{public}s"
+ "final_pane"
+ "leaveAppContentMetricsUnresolved"
+ "leaveAppContentMetricsUnresolved is set. Not resolving metrics for %{private}s"
+ "mediaAPIRequestTimeoutSeconds"
+ "performAPIRequest() timed out after %{public}s for %{public}s"
+ "phase → %{public}s"
+ "rcs_group_id"
+ "rcs_group_name"
+ "rcs_group_uri"
+ "resolveAppsAPIPath(_:)"
+ "resolved the host app. bundle_id="
+ "shutdown(state:error:notify:updateState:cancelContext:)"
+ "the eSIM exporter did not implement didUpdateTelemetrySessionID(sessionID:). "
+ "the eSIM importer did not implement didUpdateTelemetrySessionID(sessionID:). "
+ "the host is the Android OS Migration Tester app and will skip eSIM data transfer and complete the current migration."
+ "v16@?0@\"MKProgress\"8"
+ "v16@?0Q8"
+ "\xf0\xe1"
- "<"
- "AMS request encoding timed out after 3 seconds"
- "API request timed out after 3 seconds"
- "User cancelled migration"
- "_run(estimation:contexts:)"
- "encodeAMSRequest() timed out for %{public}s"
- "lastActivityMillis"
- "performAPIRequest() timed out for %{public}s"
- "shutdown(state:error:notify:updateState:)"
- "\xf0\xd1"
```
