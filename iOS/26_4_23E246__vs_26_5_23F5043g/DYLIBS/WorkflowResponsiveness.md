## WorkflowResponsiveness

> `/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness`

```diff

-419.2.4.0.0
-  __TEXT.__text: 0x26808
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x7b0
+419.9.0.0.0
+  __TEXT.__text: 0x279a8
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_methlist: 0x7f0
   __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0xaa4
-  __TEXT.__cstring: 0x2213
-  __TEXT.__oslogstring: 0x4289
-  __TEXT.__unwind_info: 0x4f8
-  __TEXT.__objc_classname: 0x11a
-  __TEXT.__objc_methname: 0x25f3
-  __TEXT.__objc_methtype: 0x270
-  __TEXT.__objc_stubs: 0x1cc0
+  __TEXT.__gcc_except_tab: 0xcfc
+  __TEXT.__cstring: 0x2330
+  __TEXT.__oslogstring: 0x44a3
+  __TEXT.__unwind_info: 0x548
+  __TEXT.__objc_classname: 0x11e
+  __TEXT.__objc_methname: 0x2803
+  __TEXT.__objc_methtype: 0x293
+  __TEXT.__objc_stubs: 0x1da0
   __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x600
+  __DATA_CONST.__const: 0x660
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x840
+  __DATA_CONST.__objc_selrefs: 0x880
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x2060
-  __AUTH_CONST.__objc_const: 0x16a0
+  __AUTH_CONST.__cfstring: 0x2120
+  __AUTH_CONST.__objc_const: 0x1730
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x150
+  __DATA.__objc_ivar: 0x15c
   __DATA.__data: 0xc0
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x2d0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 144FF333-6DA8-3257-95C6-A01843383CAD
-  Functions: 538
-  Symbols:   1809
-  CStrings:  1254
+  UUID: 1A5FC9F4-A7A3-3AA5-87D6-6FEE2F5544C4
+  Functions: 551
+  Symbols:   1856
+  CStrings:  1290
 
Symbols:
+ -[WRDiagnostic isValid:]
+ -[WRDiagnostic isValidForSignpost:]
+ -[WRDiagnostic isValidForWorkflow:]
+ -[WRSignpost initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:environmentFieldNames:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:requiredFieldNamesAndValues:requiredLogMessageContents:]
+ -[WRSignpost requiredFieldNamesAndValues]
+ -[WRSignpost requiredLogMessageContents]
+ -[WRWorkflowEventTracker handleSignpost:].cold.9
+ -[WRWorkflowEventTracker numSignpostsContributingToEvents]
+ -[WRWorkflowEventTracker numSignpostsFilteredOut]
+ -[WRWorkflowEventTracker numSignpostsNotInWorkflow]
+ -[WRWorkflowEventTracker numSignpostsOutsideEventTimeRange]
+ GCC_except_table100
+ GCC_except_table119
+ GCC_except_table133
+ GCC_except_table14
+ GCC_except_table169
+ GCC_except_table172
+ GCC_except_table174
+ GCC_except_table176
+ GCC_except_table179
+ GCC_except_table216
+ GCC_except_table97
+ _IndexOfSubstringNotContainedInString
+ _OBJC_IVAR_$_WRSignpost._requiredFieldNamesAndValues
+ _OBJC_IVAR_$_WRSignpost._requiredLogMessageContents
+ _OBJC_IVAR_$_WRWorkflowEventTracker._numSignpostsContributingToEvents
+ _OBJC_IVAR_$_WRWorkflowEventTracker._numSignpostsFilteredOut
+ _OBJC_IVAR_$_WRWorkflowEventTracker._numSignpostsNotInWorkflow
+ _OBJC_IVAR_$_WRWorkflowEventTracker._numSignpostsOutsideEventTimeRange
+ _OUTLINED_FUNCTION_116
+ _OUTLINED_FUNCTION_117
+ _OUTLINED_FUNCTION_118
+ _OUTLINED_FUNCTION_119
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _WRIsEqualNullable
+ _WRSignpostRequiredFieldNamesAndValuesKey
+ _WRSignpostRequiredLogMessageContentsKey
+ ___41-[WRWorkflowEventTracker handleSignpost:]_block_invoke
+ ___52-[WRWorkflowEventTracker handleSignpost:wrsignpost:]_block_invoke.215
+ ___WRCheckForBadSignpostDict_block_invoke.cold.2
+ ___WRValidateDict_block_invoke
+ ___block_descriptor_56_e8_32s40s48r_e25_v32?0"NSString"816^B24ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48r_e15_v32?0816^B24lu56l8r48l8s32l8s40l8
+ ___block_literal_global.115
+ ___block_literal_global.117
+ ___block_literal_global.548
+ ___block_literal_global.554
+ ___block_literal_global.557
+ _objc_msgSend$containsString:
+ _objc_msgSend$initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:environmentFieldNames:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:requiredFieldNamesAndValues:requiredLogMessageContents:
+ _objc_msgSend$isValidForSignpost:
+ _objc_msgSend$isValidForWorkflow:
+ _objc_msgSend$metadata
+ _objc_msgSend$requiredFieldNamesAndValues
+ _objc_msgSend$requiredLogMessageContents
+ _objc_msgSend$timeRecordedMachContinuousTime
+ _objc_retain_x2
- -[WRDiagnostic isValidForSignpost]
- -[WRDiagnostic isValidForWorkflow]
- -[WRDiagnostic validate]
- -[WRSignpost initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:environmentFieldNames:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:]
- -[WRWorkflowEventTracker numHandledSignposts]
- -[WRWorkflowEventTracker numOutsideSignposts]
- -[WRWorkflowEventTracker numUnhandledSignposts]
- GCC_except_table115
- GCC_except_table131
- GCC_except_table212
- GCC_except_table98
- _OBJC_IVAR_$_WRWorkflowEventTracker._numHandledSignposts
- _OBJC_IVAR_$_WRWorkflowEventTracker._numOutsideSignposts
- _OBJC_IVAR_$_WRWorkflowEventTracker._numUnhandledSignposts
- _OUTLINED_FUNCTION_44
- _OUTLINED_FUNCTION_45
- _OUTLINED_FUNCTION_46
- _OUTLINED_FUNCTION_47
- ___52-[WRWorkflowEventTracker handleSignpost:wrsignpost:]_block_invoke.214
- ___block_literal_global.111
- ___block_literal_global.544
- ___block_literal_global.550
- ___block_literal_global.553
- _objc_msgSend$initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:environmentFieldNames:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:
CStrings:
+ "%@:%@:%@ (event:%@ indiv:%@ env:%@ caEventName:%@ requiredFields:%lu requiredLogMessageContents:%lu thresholds:%lu)"
+ "%{public}@: %{public}@: filtered out by required field/value %@=%@ (mismatched value %@) (%llu)"
+ "%{public}@: %{public}@: filtered out by required field/value %@=%@ (no such field) (%llu)"
+ "%{public}@: %{public}@: filtered out by required log message contents \"%@\" (%llu)"
+ "%{public}@: %{public}@: have intervals, not using emit as start/end of workflow event"
+ "%{public}@: Bad SignpostObject class: %s"
+ "%{public}@<%{public}@>: %{public}@: have intervals, not using emit as start/end of workflow event"
+ "1@`"
+ "@\"NSDictionary\""
+ "@104@0:8@16@24@32@40B48@52@60B68@72@80@88@96"
+ "B24@0:8^@16"
+ "T@\"NSArray\",R,V_requiredLogMessageContents"
+ "T@\"NSDictionary\",R,V_requiredFieldNamesAndValues"
+ "TQ,R,V_numSignpostsContributingToEvents"
+ "TQ,R,V_numSignpostsFilteredOut"
+ "TQ,R,V_numSignpostsNotInWorkflow"
+ "TQ,R,V_numSignpostsOutsideEventTimeRange"
+ "Wrong key type under %@: %s, expected %@"
+ "Wrong type for signpost required log message contents: %s"
+ "Wrong value type for %@ key \"%@\": %s"
+ "_numSignpostsContributingToEvents"
+ "_numSignpostsFilteredOut"
+ "_numSignpostsNotInWorkflow"
+ "_numSignpostsOutsideEventTimeRange"
+ "_requiredFieldNamesAndValues"
+ "_requiredLogMessageContents"
+ "containsString:"
+ "initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:environmentFieldNames:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:requiredFieldNamesAndValues:requiredLogMessageContents:"
+ "isValidForSignpost:"
+ "isValidForWorkflow:"
+ "metadata"
+ "numSignpostsContributingToEvents"
+ "numSignpostsFilteredOut"
+ "numSignpostsNotInWorkflow"
+ "numSignpostsOutsideEventTimeRange"
+ "requiredFieldNamesAndValues"
+ "requiredLogMessageContents"
+ "required_field_names_and_values"
+ "required_log_message_contents"
+ "timeRecordedMachContinuousTime"
+ "unhandled signpost dictionary key %@"
+ "unhandled signpost dictionary key %{public}@"
- "%@:%@:%@ (event:%@ indiv:%@ env:%@ caEventName:%@ thresholds:%lu)"
- "@88@0:8@16@24@32@40B48@52@60B68@72@80"
- "TQ,R,V_numHandledSignposts"
- "TQ,R,V_numOutsideSignposts"
- "TQ,R,V_numUnhandledSignposts"
- "_numHandledSignposts"
- "_numOutsideSignposts"
- "_numUnhandledSignposts"
- "initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:environmentFieldNames:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:"
- "numHandledSignposts"
- "numOutsideSignposts"
- "numUnhandledSignposts"

```
