## DiagnosticsKit

> `/System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit`

```diff

-63.120.2.0.0
-  __TEXT.__text: 0x1d1b4
-  __TEXT.__auth_stubs: 0x620
-  __TEXT.__objc_methlist: 0x2d34
-  __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x1a63
-  __TEXT.__oslogstring: 0x11b2
-  __TEXT.__gcc_except_tab: 0x90c
+70.0.0.0.0
+  __TEXT.__text: 0x1ebc0
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_methlist: 0x2eac
+  __TEXT.__const: 0xe8
+  __TEXT.__cstring: 0x1ac9
+  __TEXT.__oslogstring: 0x12ea
+  __TEXT.__gcc_except_tab: 0xbc4
   __TEXT.__dlopen_cstrs: 0x173
-  __TEXT.__unwind_info: 0x8e0
-  __TEXT.__objc_classname: 0x69d
-  __TEXT.__objc_methname: 0x566d
-  __TEXT.__objc_methtype: 0x105c
-  __TEXT.__objc_stubs: 0x4260
-  __DATA_CONST.__got: 0x2a0
-  __DATA_CONST.__const: 0x688
-  __DATA_CONST.__objc_classlist: 0x150
+  __TEXT.__unwind_info: 0x960
+  __TEXT.__objc_classname: 0x6ca
+  __TEXT.__objc_methname: 0x5970
+  __TEXT.__objc_methtype: 0x1080
+  __TEXT.__objc_stubs: 0x4540
+  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__const: 0x700
+  __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1480
+  __DATA_CONST.__objc_selrefs: 0x1538
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x320
+  __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0xe00
-  __AUTH_CONST.__objc_const: 0x4f00
+  __AUTH_CONST.__cfstring: 0xe20
+  __AUTH_CONST.__objc_const: 0x5190
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0xd20
-  __DATA.__objc_ivar: 0x2b4
+  __AUTH.__objc_data: 0xdc0
+  __DATA.__objc_ivar: 0x2d0
   __DATA.__data: 0xe00
   __DATA.__bss: 0x150
   - /System/Library/Frameworks/CallKit.framework/CallKit

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
-  - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2F0E4274-C5C9-3A63-A490-EDAF507FC635
-  Functions: 891
-  Symbols:   3381
-  CStrings:  1607
+  UUID: 8885A61B-CEAF-3B52-9680-A9452C89D769
+  Functions: 925
+  Symbols:   3504
+  CStrings:  1657
 
Symbols:
+ +[DKReportingConcurrentRequestGroup initWithResources:]
+ -[DKReport mergeWithReport:]
+ -[DKReportManager getRequests:]
+ -[DKReportManager requestsToRetry]
+ -[DKReportManager resourceUsage]
+ -[DKReportManager retryInterruptedRequests:andWithError:]
+ -[DKReportManager sendRequests:serialRequests:failOnError:completion:]
+ -[DKReportManager sendRequests:serialRequests:failOnError:completion:].cold.1
+ -[DKReportManager setRequestsToRetry:]
+ -[DKReportManager setResourceUsage:]
+ -[DKResourceMonitor .cxx_destruct]
+ -[DKResourceMonitor canProceedWithResources:]
+ -[DKResourceMonitor cancelAndResetReservations]
+ -[DKResourceMonitor executeWhenSafe:withCompletion:]
+ -[DKResourceMonitor executionQueue]
+ -[DKResourceMonitor init]
+ -[DKResourceMonitor isExecutingBlocks]
+ -[DKResourceMonitor proceedWithAllSafeExectuions]
+ -[DKResourceMonitor releaseResources:]
+ -[DKResourceMonitor reserveIfAvailable:]
+ -[DKResourceMonitor reserveResources:]
+ -[DKResourceMonitor resourceUsage]
+ -[DKResourceMonitor setExecutionQueue:]
+ -[DKResourceMonitor setIsExecutingBlocks:]
+ -[DKResourceMonitor setResourceUsage:]
+ -[DKResourceMonitorQueueItem .cxx_destruct]
+ -[DKResourceMonitorQueueItem completion]
+ -[DKResourceMonitorQueueItem resources]
+ -[DKResourceMonitorQueueItem setCompletion:]
+ -[DKResourceMonitorQueueItem setResources:]
+ GCC_except_table10
+ GCC_except_table23
+ GCC_except_table27
+ GCC_except_table30
+ GCC_except_table31
+ GCC_except_table8
+ _OBJC_CLASS_$_DKResourceMonitor
+ _OBJC_CLASS_$_DKResourceMonitorQueueItem
+ _OBJC_IVAR_$_DKReportManager._requestsToRetry
+ _OBJC_IVAR_$_DKReportManager._resourceUsage
+ _OBJC_IVAR_$_DKResourceMonitor._executionQueue
+ _OBJC_IVAR_$_DKResourceMonitor._isExecutingBlocks
+ _OBJC_IVAR_$_DKResourceMonitor._resourceUsage
+ _OBJC_IVAR_$_DKResourceMonitorQueueItem._completion
+ _OBJC_IVAR_$_DKResourceMonitorQueueItem._resources
+ _OBJC_METACLASS_$_DKResourceMonitor
+ _OBJC_METACLASS_$_DKResourceMonitorQueueItem
+ __OBJC_$_CLASS_METHODS_DKReportingConcurrentRequestGroup
+ __OBJC_$_INSTANCE_METHODS_DKResourceMonitor
+ __OBJC_$_INSTANCE_METHODS_DKResourceMonitorQueueItem
+ __OBJC_$_INSTANCE_VARIABLES_DKResourceMonitor
+ __OBJC_$_INSTANCE_VARIABLES_DKResourceMonitorQueueItem
+ __OBJC_$_PROP_LIST_DKResourceMonitor
+ __OBJC_$_PROP_LIST_DKResourceMonitorQueueItem
+ __OBJC_CLASS_RO_$_DKResourceMonitor
+ __OBJC_CLASS_RO_$_DKResourceMonitorQueueItem
+ __OBJC_METACLASS_RO_$_DKResourceMonitor
+ __OBJC_METACLASS_RO_$_DKResourceMonitorQueueItem
+ ___57-[DKReportManager retryInterruptedRequests:andWithError:]_block_invoke
+ ___57-[DKReportManager retryInterruptedRequests:andWithError:]_block_invoke.cold.1
+ ___67-[DKReportManager reportWithComponentPredicateManifest:completion:]_block_invoke.64
+ ___70-[DKReportManager sendRequests:serialRequests:failOnError:completion:]_block_invoke
+ ___70-[DKReportManager sendRequests:serialRequests:failOnError:completion:]_block_invoke.80
+ ___70-[DKReportManager sendRequests:serialRequests:failOnError:completion:]_block_invoke_2
+ ___block_descriptor_121_e8_32s40s48s56s64s72r80r88r96r104r112r_e20_v24?08"NSError"16lr72l8r80l8r88l8s32l8s40l8r96l8r104l8s48l8r112l8s56l8s64l8
+ ___block_descriptor_56_e8_32s40bs48r_e30_v24?0"DKReport"8"NSError"16ls32l8r48l8s40l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e30_v24?0"DKReport"8"NSError"16ls32l8r48l8r56l8r64l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8
+ __os_feature_enabled_impl
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$canProceedWithResources:
+ _objc_msgSend$componentPredicateWithType:identifier:
+ _objc_msgSend$executeWhenSafe:withCompletion:
+ _objc_msgSend$executionQueue
+ _objc_msgSend$getRequests:
+ _objc_msgSend$initWithResources:
+ _objc_msgSend$isEqualToSet:
+ _objc_msgSend$isExecutingBlocks
+ _objc_msgSend$mergeWithReport:
+ _objc_msgSend$proceedWithAllSafeExectuions
+ _objc_msgSend$releaseResources:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeObjectsInArray:
+ _objc_msgSend$requestsToRetry
+ _objc_msgSend$reserveIfAvailable:
+ _objc_msgSend$reserveResources:
+ _objc_msgSend$resourceUsage
+ _objc_msgSend$retryInterruptedRequests:andWithError:
+ _objc_msgSend$sendRequests:serialRequests:failOnError:completion:
+ _objc_msgSend$setExecutionQueue:
+ _objc_msgSend$setIsExecutingBlocks:
+ _objc_msgSend$setResourceUsage:
+ _objc_msgSend$setResources:
+ _objc_msgSend$setValue:forKey:
+ _objc_retain_x28
- -[DKReportManager sendRequestsForGroup:concurrent:failOnError:error:]
- ___69-[DKReportManager sendRequestsForGroup:concurrent:failOnError:error:]_block_invoke
- ___block_descriptor_97_e8_32s40s48s56s64r72r80r88r_e20_v24?08"NSError"16lr64l8r72l8r80l8s32l8r88l8s40l8s48l8s56l8
- _objc_msgSend$intersectsSet:
- _objc_msgSend$sendRequestsForGroup:concurrent:failOnError:error:
CStrings:
+ "@\"DKResourceMonitor\""
+ "@28@0:8B16^@20"
+ "Calling resource reservation callback for %@"
+ "Component execution failed; count: %@"
+ "ConcurrentSystemReportGeneration"
+ "Could not start report request; count: %d"
+ "DKResourceMonitor"
+ "DKResourceMonitorQueueItem"
+ "DKResourceUsageMonitor"
+ "DiagnosticsKit"
+ "Dispatch group timed out waiting on all system report component requests to complete"
+ "Finished executing interrupted report components"
+ "Queue %@ for execution"
+ "Releasing these resources: %@"
+ "Rerunning interrupted report components in serial order"
+ "Reserving these component resources %@"
+ "T@\"DKResourceMonitor\",&,N,V_resourceUsage"
+ "T@\"NSMutableArray\",&,N,V_executionQueue"
+ "T@\"NSMutableArray\",&,N,V_requestsToRetry"
+ "T@\"NSMutableDictionary\",&,N,V_resourceUsage"
+ "T@\"NSSet\",C,N,V_resources"
+ "TB,N,V_isExecutingBlocks"
+ "[RID: %@] Finished; count: %d; Report: %@, error: %@; request: %@"
+ "[RID: %@] Starting; count: %d, %@ < %@ < %@; request: %@"
+ "_executionQueue"
+ "_isExecutingBlocks"
+ "_requestsToRetry"
+ "_resourceUsage"
+ "arrayByAddingObjectsFromArray:"
+ "canProceedWithResources:"
+ "cancelAndResetReservations"
+ "executeWhenSafe:withCompletion:"
+ "executionQueue"
+ "getRequests:"
+ "initWithResources:"
+ "isEqualToSet:"
+ "isExecutingBlocks"
+ "mergeWithReport:"
+ "proceedWithAllSafeExectuions"
+ "releaseResources:"
+ "removeAllObjects"
+ "removeObjectsInArray:"
+ "requestsToRetry"
+ "reserveIfAvailable:"
+ "reserveResources:"
+ "resourceUsage"
+ "retryInterruptedRequests:andWithError:"
+ "sendRequests:serialRequests:failOnError:completion:"
+ "setExecutionQueue:"
+ "setIsExecutingBlocks:"
+ "setRequestsToRetry:"
+ "setResourceUsage:"
+ "setValue:forKey:"
+ "v24@?0@\"DKReport\"8@\"NSError\"16"
+ "v40@0:8@16B24B28@?32"
- "@40@0:8@16B24B28^@32"
- "Could not start report request; count: %d, concurrent: %d"
- "[RID: %@] Finished; count: %d, concurrent: %d; Report: %@, error: %@; request: %@"
- "[RID: %@] Starting; count: %d, concurrent: %d; %@ < %@ < %@ < %@; request: %@"
- "intersectsSet:"
- "sendRequestsForGroup:concurrent:failOnError:error:"

```
