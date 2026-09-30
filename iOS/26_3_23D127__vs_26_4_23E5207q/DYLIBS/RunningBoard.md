## RunningBoard

> `/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard`

```diff

-1008.80.2.0.0
-  __TEXT.__text: 0x7dbc4
-  __TEXT.__auth_stubs: 0x14a0
-  __TEXT.__objc_methlist: 0x61c4
+1015.100.15.0.0
+  __TEXT.__text: 0x80968
+  __TEXT.__auth_stubs: 0x1450
+  __TEXT.__objc_methlist: 0x622c
   __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0x7c5b
-  __TEXT.__oslogstring: 0xb560
-  __TEXT.__gcc_except_tab: 0xcbc
-  __TEXT.__unwind_info: 0x1b48
+  __TEXT.__cstring: 0x7d36
+  __TEXT.__oslogstring: 0xb5f4
+  __TEXT.__gcc_except_tab: 0xca0
+  __TEXT.__unwind_info: 0x1e08
   __TEXT.__objc_classname: 0xf7c
-  __TEXT.__objc_methname: 0xd520
+  __TEXT.__objc_methname: 0xd645
   __TEXT.__objc_methtype: 0x2cd2
-  __TEXT.__objc_stubs: 0xa280
-  __DATA_CONST.__got: 0x770
-  __DATA_CONST.__const: 0x1770
+  __TEXT.__objc_stubs: 0xa3a0
+  __DATA_CONST.__got: 0x780
+  __DATA_CONST.__const: 0x1798
   __DATA_CONST.__objc_classlist: 0x378
-  __DATA_CONST.__objc_catlist: 0x170
+  __DATA_CONST.__objc_catlist: 0x178
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e18
+  __DATA_CONST.__objc_selrefs: 0x2e68
   __DATA_CONST.__objc_superrefs: 0x298
   __DATA_CONST.__objc_arraydata: 0x768
-  __AUTH_CONST.__auth_got: 0xa60
+  __AUTH_CONST.__auth_got: 0xa38
   __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0x6b60
-  __AUTH_CONST.__objc_const: 0xd570
+  __AUTH_CONST.__cfstring: 0x6c00
+  __AUTH_CONST.__objc_const: 0xd610
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0xa1c
+  __DATA.__objc_ivar: 0xa24
   __DATA.__data: 0x1320
   __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0x20d0

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
+  - /System/Library/PrivateFrameworks/DynamicPrefetching.framework/DynamicPrefetching
   - /System/Library/PrivateFrameworks/IOGPU.framework/IOGPU
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 7D21F6C6-397F-37A4-9DF1-12BF79B0A4ED
-  Functions: 2722
-  Symbols:   9489
-  CStrings:  5435
+  UUID: 50E4D528-DF23-3079-945F-DB83AC0C08E4
+  Functions: 2809
+  Symbols:   9808
+  CStrings:  5462
 
Symbols:
+ +[RBAttributeFactory _prefetchPageAttributeWithProperties:errors:]
+ +[RBAttributeFactory _prefetchPageAttributeWithProperties:errors:].cold.1
+ -[RBAssertionAcquisitionContext pagePrefetchLaunchScenario]
+ -[RBAssertionAcquisitionContext setPagePrefetchLaunchScenario:]
+ -[RBMutableProcessState addPrefetchPageScenario:]
+ -[RBMutableProcessState removePrefetchPageScenario:]
+ -[RBProcess _getBundleID]
+ -[RBProcess _lock_applyPrefetchPageScenarios]
+ -[RBProcessState prefetchPageScenarios]
+ -[RBSPrefetchPageAttribute(RBProcessState) applyToAcquisitionContext:]
+ -[RBSPrefetchPageAttribute(RBProcessState) applyToProcessState:attributePath:context:]
+ -[RBSPrefetchPageAttribute(RBProcessState) isValidForContext:withError:]
+ OBJC_IVAR_$_RBProcessState._prefetchPageScenarios
+ _OBJC_CLASS_$_RBSPrefetchPageAttribute
+ _OBJC_CLASS_$_RBSProcessPrefetchPageScenario
+ _OBJC_IVAR_$_RBAssertionAcquisitionContext._pagePrefetchLaunchScenario
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_RBSPrefetchPageAttribute_$_RBProcessState
+ __OBJC_$_CATEGORY_RBSPrefetchPageAttribute_$_RBProcessState
+ ___45-[RBProcess _lock_applyPrefetchPageScenarios]_block_invoke
+ ___45-[RBProcess _lock_applyPrefetchPageScenarios]_block_invoke_2
+ ___60-[RBLaunchdJobManager invokeOnProcessDeath:handler:onQueue:]_block_invoke.200
+ ___63-[RBLaunchdJobManager _createAndSubmitExtensionJob:UUID:error:]_block_invoke.152
+ ___88-[RBLaunchdJobManager _addAppPropertiesToData:forIdentity:context:actualIdentity:error:]_block_invoke.46
+ ___block_descriptor_40_e8_32s_e44_v24?0"RBSProcessPrefetchPageScenario"8^B16ls32l8
+ ___block_literal_global.266
+ ___block_literal_global.354
+ _end_scenario
+ _objc_msgSend$addPrefetchPageScenario:
+ _objc_msgSend$initWithScenario:
+ _objc_msgSend$pagePrefetchLaunchScenario
+ _objc_msgSend$prefetchPageScenarios
+ _objc_msgSend$psPageIn
+ _objc_msgSend$scenario
+ _objc_msgSend$setPagePrefetchLaunchScenario:
+ _objc_msgSend$setPrefetchPageScenarios:
+ _objc_msgSend$setPsPageIn:
+ _start_scenario
- -[RBSLegacyAttribute _maxCPUDuration]
- ___60-[RBLaunchdJobManager invokeOnProcessDeath:handler:onQueue:]_block_invoke.199
- ___63-[RBLaunchdJobManager _createAndSubmitExtensionJob:UUID:error:]_block_invoke.151
- ___88-[RBLaunchdJobManager _addAppPropertiesToData:forIdentity:context:actualIdentity:error:]_block_invoke.45
- ___block_literal_global.263
- ___block_literal_global.350
- _objc_claimAutoreleasedReturnValue
- _objc_release_x2
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x7
CStrings:
+ "\t13"
+ "\n%@: invalidation reason: %hhu"
+ " prefetchPageScenarios:[\n\t"
+ "%{public}@ Found locked file lock: %{public}@ with unknown owner"
+ "<%@| identity:%@ role:%@ gpuRole:%@ coalitionLevel:%llu explicitJetsamBand:%d memoryLimit:%@(%@) flags:%hx guaranteedRunning:%@ legacyFinishTaskReason:%lu%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@>"
+ "Assertions were invalidated, count = %lu."
+ "Detected misconfigured RBSPrefetchPageAttribute attribute with scenario %{public}@"
+ "RBSPrefetchPageAttribute"
+ "Scenario"
+ "TB,N,V_pagePrefetchLaunchScenario"
+ "_POSIXSpawnTelemetryPageIn"
+ "_pagePrefetchLaunchScenario"
+ "_prefetchPageScenarios"
+ "addPrefetchPageScenario:"
+ "com.apple.RemoteAlertTestUIService"
+ "initWithScenario:"
+ "pagePrefetchLaunchScenario"
+ "prefetchPageScenarios"
+ "psPageIn"
+ "removePrefetchPageScenario:"
+ "scenario"
+ "setPagePrefetchLaunchScenario:"
+ "setPrefetchPageScenarios:"
+ "setPsPageIn:"
+ "v24@?0@\"RBSProcessPrefetchPageScenario\"8^B16"
- "\t12"
- "<%@| identity:%@ role:%@ gpuRole:%@ coalitionLevel:%llu explicitJetsamBand:%d memoryLimit:%@(%@) flags:%hx guaranteedRunning:%@ legacyFinishTaskReason:%lu%@%@%@%@%@%@%@%@%@%@%@%@%@%@>"
- "Assertions were invalidated"

```
