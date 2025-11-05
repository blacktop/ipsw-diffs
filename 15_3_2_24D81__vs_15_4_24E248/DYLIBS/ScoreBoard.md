## ScoreBoard

> `/System/Library/PrivateFrameworks/ScoreBoard.framework/Versions/A/ScoreBoard`

```diff

 13.0.0.0.0
-  __TEXT.__text: 0xb40c
+  __TEXT.__text: 0xc724
   __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_methlist: 0xc08
+  __TEXT.__objc_methlist: 0xe0c
   __TEXT.__const: 0x78
   __TEXT.__cstring: 0xeb9
   __TEXT.__oslogstring: 0x62a
-  __TEXT.__gcc_except_tab: 0x108
-  __TEXT.__unwind_info: 0x370
+  __TEXT.__gcc_except_tab: 0xfc
+  __TEXT.__unwind_info: 0x3b0
   __TEXT.__objc_classname: 0x244
   __TEXT.__objc_methname: 0x1b58
   __TEXT.__objc_methtype: 0x619

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a0
+  __DATA_CONST.__objc_selrefs: 0x718
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0x190
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0xf20
-  __AUTH_CONST.__objc_const: 0x3ab0
+  __AUTH_CONST.__objc_const: 0x3730
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH.__objc_data: 0x5f0

   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/Versions/A/DuetActivityScheduler
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 426C3B5C-5555-31F5-A8B7-AF9F07637EC4
-  Functions: 267
-  Symbols:   870
+  UUID: 16956CC7-28BB-3F8F-AB9A-4E96D1FC7430
+  Functions: 349
+  Symbols:   969
   CStrings:  717
 
Symbols:
+ +[SCRSchedulingConfiguration immediateConfiguration].cold.1
+ -[SCRActivity initWithName:earliestStartDate:schedulingWindow:activationBlock:].cold.1
+ -[SCRActivity initWithName:earliestStartDate:schedulingWindow:activationBlock:].cold.2
+ -[SCRActivity initWithName:earliestStartDate:schedulingWindow:activationBlock:].cold.3
+ -[SCRActivity initWithName:earliestStartDate:schedulingWindow:activationBlock:].cold.4
+ -[SCRActivityScheduler init].cold.1
+ -[SCRApprovalCoordinator getApprovalForTask:error:].cold.1
+ -[SCRApprovalCoordinator getApprovalForTask:error:].cold.2
+ -[SCRApprovalCoordinator getApprovalForTask:error:].cold.3
+ -[SCRCompositeGovernor addGovernor:].cold.1
+ -[SCRCompositeGovernor addGovernor:].cold.2
+ -[SCRCompositeGovernor removeGovernor:].cold.1
+ -[SCRCompositeGovernor removeGovernor:].cold.2
+ -[SCRCompositeGovernor taskAdministrator:didCompleteTask:withError:].cold.1
+ -[SCRCompositeGovernor taskAdministrator:isEligibleToPerformTask:eligiblityError:].cold.1
+ -[SCRCompositeGovernor taskAdministrator:isEligibleToPerformTask:eligiblityError:].cold.2
+ -[SCRCompositeGovernor taskAdministrator:isEligibleToPerformTask:eligiblityError:].cold.3
+ -[SCRCompositeGovernor taskAdministrator:willPerformTask:].cold.1
+ -[SCRDASActivityScheduler _activityWithIdentifierDidBegin:].cold.2
+ -[SCRDASActivityScheduler _enqueueActivityWithMetadata:].cold.1
+ -[SCRDASActivityScheduler _enqueueActivityWithMetadata:].cold.2
+ -[SCRDASActivityScheduler _enqueueActivityWithMetadata:].cold.3
+ -[SCRDASActivityScheduler _enqueueActivityWithMetadata:].cold.4
+ -[SCRDASActivityScheduler _popActivityWithIdentifier:].cold.1
+ -[SCRIsolatedActivityScheduler completeActivityWithIdentifier:].cold.1
+ -[SCRIsolatedActivityScheduler submitActivity:].cold.1
+ -[SCRMutableSchedulingConfiguration setLatestStartDate:].cold.1
+ -[SCRSchedulingConfiguration _isSatisfiedBy:strictly:].cold.1
+ -[SCRSchedulingConfiguration intersectionWith:minimumWindow:].cold.1
+ -[SCRSchedulingConfiguration intersectionWith:minimumWindow:].cold.2
+ -[SCRSchedulingConfiguration intersectionWith:minimumWindow:].cold.3
+ -[SCRSchedulingConfiguration intersectionWith:minimumWindow:].cold.4
+ -[SCRSchedulingConfiguration intersectionWith:minimumWindow:].cold.5
+ -[SCRSchedulingConfiguration setEarliestStartDate:].cold.1
+ -[SCRSchedulingConfiguration setRequiresClassAAccess:].cold.1
+ -[SCRSchedulingConfiguration setRequiresNetworkAccess:].cold.1
+ -[SCRSchedulingConfiguration setSchedulingWindow:].cold.1
+ -[SCRSchedulingConfiguration setSchedulingWindow:].cold.2
+ -[SCRSchedulingConfiguration setWakeDeviceForDeadline:].cold.1
+ -[SCRStateMachine _assertNextStateTransitionIsValid].cold.1
+ -[SCRStateMachine _assertNextStateTransitionIsValid].cold.2
+ -[SCRStateMachine _assertNextStateTransitionIsValid].cold.3
+ -[SCRStateMachine _performStateTransition].cold.1
+ -[SCRStateMachine _stringForState:].cold.1
+ -[SCRTask addAttribute:withKey:].cold.1
+ -[SCRTask addAttribute:withKey:].cold.2
+ -[SCRTask attributeForKey:].cold.1
+ -[SCRTask removeAttributeWithKey:].cold.1
+ -[SCRTaskAdministrator cancelTaskWithIdentifier:].cold.1
+ -[SCRTaskAdministrator registerGovernor:].cold.1
+ -[SCRTaskAdministrator registerGovernor:].cold.2
+ -[SCRTaskAdministrator submitTask:].cold.1
+ -[SCRTaskAdministrator submitTask:].cold.2
+ -[SCRTaskAdministrator unregisterGovernor:].cold.1
+ -[SCRTaskAdministrator unregisterGovernor:].cold.2
+ -[SCRTaskHandler _initWithSyncBlock:asyncBlock:].cold.1
+ -[SCRTaskHandler performWithContext:completion:].cold.1
+ -[SCRTaskSession _requestApproval].cold.1
+ -[SCRTaskSession _setupSharedContext].cold.1
+ -[SCRTaskSession _start].cold.1
+ -[SCRTaskSession _teardownSharedContext].cold.1
+ -[SCRTaskSession _teardownSharedContext].cold.2
+ -[SCRTaskSession initWithTask:approvalCoordinator:].cold.1
+ -[SCRTaskSession initWithTask:approvalCoordinator:].cold.2
+ -[SCRTaskTargetConfiguration _initWithTarget:syncProvider:asyncProvider:].cold.1
+ -[SCRTaskTargetConfiguration _initWithTarget:syncProvider:asyncProvider:].cold.2
+ -[SCRTaskTargetConfiguration _validateContext:].cold.1
+ -[SCRTaskTargetConfiguration contextProvider].cold.1
+ -[SCRTokenBucketBudget _locked_updateTokenCountForTimeElapsed].cold.1
+ -[SCRTokenBucketBudget _locked_updateTokenCountForTimeElapsed].cold.2
+ -[SCRTokenBucketBudget taskAdministrator:isEligibleToPerformTask:eligiblityError:].cold.1
+ -[SCRTokenBucketBudget taskAdministrator:isEligibleToPerformTask:eligiblityError:].cold.2
+ -[SCRTokenBucketBudget taskAdministrator:willPerformTask:].cold.1
+ SCRGenerateRandomIdentifier.cold.1
+ SCRLogCommon.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ __30-[SCRTaskSession _performTask]_block_invoke.cold.1
+ __37-[SCRTaskSession _setupSharedContext]_block_invoke.cold.2
+ __37-[SCRTaskSession _setupSharedContext]_block_invoke.cold.3
+ __40-[SCRTaskSession _teardownSharedContext]_block_invoke.cold.1
+ __58-[SCRTaskTargetConfiguration createContextWithCompletion:]_block_invoke.cold.1

```
