## WorkflowResponsiveness

> `/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness`

```diff

-383.14.0.0.0
-  __TEXT.__text: 0x26150
+404.0.0.0.0
+  __TEXT.__text: 0x25d78
   __TEXT.__auth_stubs: 0x750
   __TEXT.__objc_methlist: 0x790
-  __TEXT.__const: 0xf0
+  __TEXT.__const: 0xe8
   __TEXT.__gcc_except_tab: 0xba8
   __TEXT.__cstring: 0x2030
   __TEXT.__oslogstring: 0x4014
-  __TEXT.__unwind_info: 0x588
+  __TEXT.__unwind_info: 0x528
   __TEXT.__objc_classname: 0x11a
-  __TEXT.__objc_methname: 0x241c
+  __TEXT.__objc_methname: 0x2436
   __TEXT.__objc_methtype: 0x26a
-  __TEXT.__objc_stubs: 0x1c60
+  __TEXT.__objc_stubs: 0x1c80
   __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__const: 0x5e0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x828
+  __DATA_CONST.__objc_selrefs: 0x830
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x3b8
   __AUTH_CONST.__const: 0x220
   __AUTH_CONST.__cfstring: 0x1f60
-  __AUTH_CONST.__objc_const: 0x1638
+  __AUTH_CONST.__objc_const: 0x15f0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x140
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x2d0
-  __DATA_DIRTY.__bss: 0x78
+  __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 514C8F6D-127F-33A1-972A-E1336425890C
-  Functions: 568
-  Symbols:   1881
-  CStrings:  1216
+  UUID: 757CA114-FE95-3820-AAFF-E36C83DFFB51
+  Functions: 524
+  Symbols:   1779
+  CStrings:  1217
 
Symbols:
+ _WRSanitizeForCA.removedCharactersExcludingUnderscore
+ _WRSanitizeForCA.removedCharactersIncludingUnderscore
+ ___block_literal_global.538
+ ___block_literal_global.547
+ _objc_msgSend$removeCharactersInString:
- -[WROpenIndividuatedSignpostInterval individuationIdentifier]
- -[WROpenIndividuatedSignpostInterval signpost]
- -[WROpenIndividuatedSignpostInterval timestampAndThread]
- -[WRSignpost hasDiagnosticThresholdIntervalSeconds]
- -[WRSignpostTracker emitsMutable]
- -[WRSignpostTracker environmentMutable]
- -[WRSignpostTracker incompleteIntervalStartsMutable]
- -[WRSignpostTracker intervalsMutable]
- -[WRSignpostTracker isMiddleOfInterval]
- -[WRSignpostTracker reset]
- -[WRSignpostTracker setEmitsMutable:]
- -[WRSignpostTracker setEnvironmentMutable:]
- -[WRSignpostTracker setIncompleteIntervalStartsMutable:]
- -[WRSignpostTracker setIntervalsMutable:]
- -[WRSignpostTracker setIsMiddleOfInterval:]
- -[WRWorkflowEventTracker allSignpostTrackersMutable]
- -[WRWorkflowEventTracker candidateEndSignpostTrackers]
- -[WRWorkflowEventTracker concurrentEvents]
- -[WRWorkflowEventTracker eventCompletionCallback]
- -[WRWorkflowEventTracker openIndividuatedIntervalsWithFieldNameMatchingAnEndSignpostFromBeforeEventStart]
- -[WRWorkflowEventTracker setAllSignpostTrackersMutable:]
- -[WRWorkflowEventTracker setCandidateEndSignpostTrackers:]
- -[WRWorkflowEventTracker setConcurrentEvents:]
- -[WRWorkflowEventTracker setEndSignpost:]
- -[WRWorkflowEventTracker setError:]
- -[WRWorkflowEventTracker setEventEnd:]
- -[WRWorkflowEventTracker setEventIdentifier:]
- -[WRWorkflowEventTracker setEventStart:]
- -[WRWorkflowEventTracker setOpenIndividuatedIntervalsWithFieldNameMatchingAnEndSignpostFromBeforeEventStart:]
- -[WRWorkflowEventTracker setStartSignpost:]
- -[WRWorkflowEventTracker setTimeoutQueue:]
- -[WRWorkflowEventTracker setTimeoutSource:]
- -[WRWorkflowEventTracker timeoutQueue]
- -[WRWorkflowEventTracker timeoutSource]
- -[WRWorkflowProvider callbackQueue]
- -[WRWorkflowProvider taskingNotifyToken]
- -[WRWorkflowProvider wrSettingsChangedNotifyToken]
- -[WRWorkflowProviderAllWorkflows callback]
- -[WRWorkflowProviderAllWorkflows setWorkflows:]
- -[WRWorkflowProviderAllWorkflows workflows]
- -[WRWorkflowProviderSingleWorkflow callback]
- -[WRWorkflowProviderSingleWorkflow setWorkflow:]
- -[WRWorkflowProviderSingleWorkflow workflowName]
- -[WRWorkflowProviderSingleWorkflow workflow]
- _OUTLINED_FUNCTION_29
- _OUTLINED_FUNCTION_30
- _OUTLINED_FUNCTION_31
- _OUTLINED_FUNCTION_32
- _WRSanitizeForCA.removedCharacters
- ___block_literal_global.535
- ___block_literal_global.541
CStrings:
+ "removeCharactersInString:"

```
