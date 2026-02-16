## WorkflowResponsiveness

> `/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness`

```diff

-412.0.0.0.0
-  __TEXT.__text: 0x25ef8
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x798
+419.1.0.0.0
+  __TEXT.__text: 0x26754
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_methlist: 0x7b0
   __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0xbd0
-  __TEXT.__cstring: 0x2074
-  __TEXT.__oslogstring: 0x4014
-  __TEXT.__unwind_info: 0x530
+  __TEXT.__gcc_except_tab: 0xaa4
+  __TEXT.__cstring: 0x2213
+  __TEXT.__oslogstring: 0x4289
+  __TEXT.__unwind_info: 0x4f0
   __TEXT.__objc_classname: 0x11a
-  __TEXT.__objc_methname: 0x24e8
-  __TEXT.__objc_methtype: 0x26d
-  __TEXT.__objc_stubs: 0x1ca0
+  __TEXT.__objc_methname: 0x25f3
+  __TEXT.__objc_methtype: 0x270
+  __TEXT.__objc_stubs: 0x1cc0
   __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x5e8
+  __DATA_CONST.__const: 0x600
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x838
+  __DATA_CONST.__objc_selrefs: 0x840
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x3b8
+  __AUTH_CONST.__auth_got: 0x390
   __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x1fa0
-  __AUTH_CONST.__objc_const: 0x1620
+  __AUTH_CONST.__cfstring: 0x2060
+  __AUTH_CONST.__objc_const: 0x16a0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x144
+  __DATA.__objc_ivar: 0x150
   __DATA.__data: 0xc0
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x2d0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 915E6321-7745-3BA0-BEE0-D21E3D1DDDBF
-  Functions: 525
-  Symbols:   1784
-  CStrings:  1224
+  UUID: D67DD8C5-5B3A-3C7C-A6E0-6CDD614FE3A0
+  Functions: 540
+  Symbols:   1814
+  CStrings:  1254
 
Symbols:
+ -[WRSignpost initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:environmentFieldNames:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:]
+ -[WRWorkflow endSignpostsUsingIntervalBegin]
+ -[WRWorkflow startSignpostsUsingIntervalEnd]
+ -[WRWorkflowEventTracker individuationIdentifierForSignpostObject:individuationFieldName:].cold.1
+ -[WRWorkflowEventTracker individuationIdentifierForSignpostObject:individuationFieldName:].cold.2
+ -[WRWorkflowEventTracker isEndSignpost:inEndGroupIndex:wrsignpost:usesIntervalStart:]
+ -[WRWorkflowEventTracker isStartSignpost:wrsignpost:usesIntervalEnd:]
+ -[WRWorkflowEventTracker shouldIgnoreStartOrEndSignpost:wrsignpost:]
+ GCC_except_table116
+ GCC_except_table130
+ GCC_except_table174
+ GCC_except_table211
+ GCC_except_table45
+ GCC_except_table9
+ GCC_except_table97
+ _OBJC_IVAR_$_WRWorkflow._endSignpostsUsingIntervalBegin
+ _OBJC_IVAR_$_WRWorkflow._startSignpostsUsingIntervalEnd
+ _OBJC_IVAR_$_WRWorkflowEventTracker._startOrEndSignpostsWithIntervals
+ _OUTLINED_FUNCTION_101
+ _OUTLINED_FUNCTION_102
+ _OUTLINED_FUNCTION_103
+ _OUTLINED_FUNCTION_104
+ _OUTLINED_FUNCTION_105
+ _OUTLINED_FUNCTION_106
+ _OUTLINED_FUNCTION_107
+ _OUTLINED_FUNCTION_108
+ _OUTLINED_FUNCTION_109
+ _OUTLINED_FUNCTION_110
+ _OUTLINED_FUNCTION_111
+ _OUTLINED_FUNCTION_112
+ _OUTLINED_FUNCTION_113
+ _OUTLINED_FUNCTION_114
+ _OUTLINED_FUNCTION_115
+ _OUTLINED_FUNCTION_116
+ _OUTLINED_FUNCTION_117
+ _OUTLINED_FUNCTION_118
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _WRSignpostEventIdentifierIsSignpostIdKey
+ _WRSignpostIntervalBeginIsEventEndKey
+ _WRSignpostIntervalEndIsEventStartKey
+ ___42-[WRWorkflowProvider registerNotification]_block_invoke.228
+ ___42-[WRWorkflowProvider registerNotification]_block_invoke.228.cold.1
+ ___52-[WRWorkflowEventTracker handleSignpost:wrsignpost:]_block_invoke.214
+ ___88-[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:checkForOverrides:error:]_block_invoke.105
+ ___block_descriptor_130_e8_32s40s48s56s64s72s80s88s96r104r112r120r_e48_"NSError"24?0"NSDictionary"8"NSDictionary"16lr96l8s32l8r104l8s40l8r112l8s48l8s56l8r120l8s64l8s72l8s80l8s88l8
+ ___block_literal_global.109
+ ___block_literal_global.111
+ ___block_literal_global.220
+ ___block_literal_global.226
+ ___block_literal_global.238
+ ___block_literal_global.376
+ ___block_literal_global.550
+ ___block_literal_global.553
+ _objc_msgSend$endSignpostsUsingIntervalBegin
+ _objc_msgSend$initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:environmentFieldNames:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:
+ _objc_msgSend$startSignpostsUsingIntervalEnd
- -[WRSignpost initWithSubsystem:category:name:eventIdentifierFieldName:individuationFieldName:environmentFieldNames:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:]
- -[WRWorkflowEventTracker handleSignpost:].cold.10
- -[WRWorkflowEventTracker handleSignpost:].cold.11
- -[WRWorkflowEventTracker handleSignpost:].cold.12
- -[WRWorkflowEventTracker handleSignpost:].cold.9
- -[WRWorkflowEventTracker handleSignpost:wrsignpost:].cold.4
- -[WRWorkflowEventTracker handleSignpost:wrsignpost:].cold.5
- -[WRWorkflowEventTracker handleSignpost:wrsignpost:].cold.6
- -[WRWorkflowEventTracker handleSignpost:wrsignpost:].cold.7
- -[WRWorkflowEventTracker individuationIdentifierForSignpostEvent:individuationFieldName:]
- -[WRWorkflowEventTracker reportCoreAnalyticsEventForSignpost:allCount:allDurationUnionSec:allDurationSumSec:allDurationLongestSec:allDurationUntrackedSec:allDurationNonNetworkBoundSec:allTimeUntilFirstSignpost:allTimeAfterLastSignpost:incompleteCount:completeDurationUnionSec:completeDurationSumSec:completeDurationLongestSec:completeTimeUntilFirstSignpost:environment:].cold.2
- -[WRWorkflowEventTracker valueForFieldName:inSignpostObject:].cold.1
- -[WRWorkflowEventTracker valueForFieldName:inSignpostObject:].cold.2
- GCC_except_table10
- GCC_except_table112
- GCC_except_table128
- GCC_except_table176
- GCC_except_table177
- GCC_except_table179
- GCC_except_table180
- GCC_except_table220
- GCC_except_table221
- GCC_except_table43
- GCC_except_table95
- _OUTLINED_FUNCTION_40
- _OUTLINED_FUNCTION_41
- _OUTLINED_FUNCTION_42
- _OUTLINED_FUNCTION_43
- _PlaceholderNameMatches
- ___42-[WRWorkflowProvider registerNotification]_block_invoke.214
- ___42-[WRWorkflowProvider registerNotification]_block_invoke.214.cold.1
- ___43-[WRWorkflowEventTracker generateTelemetry]_block_invoke.cold.2
- ___52-[WRWorkflowEventTracker handleSignpost:wrsignpost:]_block_invoke.209
- ___78-[WRWorkflowEventTracker gatherDiagnosticsWithTailspin:tailspinIncludeOSLogs:]_block_invoke.cold.4
- ___78-[WRWorkflowEventTracker gatherDiagnosticsWithTailspin:tailspinIncludeOSLogs:]_block_invoke.cold.5
- ___78-[WRWorkflowEventTracker gatherDiagnosticsWithTailspin:tailspinIncludeOSLogs:]_block_invoke.cold.6
- ___88-[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:checkForOverrides:error:]_block_invoke.99
- ___block_descriptor_114_e8_32s40s48s56s64s72s80r88r96r104r_e48_"NSError"24?0"NSDictionary"8"NSDictionary"16lr80l8s32l8r88l8s40l8r96l8s48l8s56l8r104l8s64l8s72l8
- ___block_literal_global.100
- ___block_literal_global.102
- ___block_literal_global.103
- ___block_literal_global.215
- ___block_literal_global.221
- ___block_literal_global.233
- ___block_literal_global.371
- ___block_literal_global.538
- ___block_literal_global.547
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$indexOfObject:
- _objc_msgSend$initWithSubsystem:category:name:eventIdentifierFieldName:individuationFieldName:environmentFieldNames:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
CStrings:
+ "%llu"
+ "%{public}@: %{public}@: %{public}sevent start @ %@ (%llu)"
+ "%{public}@: %{public}@: %{public}sevent start @%llu (%+.3fs in previous event)"
+ "%{public}@: %{public}@: Handling interval end event as SignpostEvent, not SignpostInterval"
+ "%{public}@: %{public}@: No individuation field name for identifier %@"
+ "%{public}@: %{public}@: Saw new individuation identifier with field name %@ needed for end signpost %@"
+ "%{public}@: %{public}@: Unable to get event identifier for field %@, ignoring signpost"
+ "%{public}@: %{public}@: contains environment %{public}@ of unsupported type %{public}s"
+ "%{public}@: %{public}@: contains environment %{public}@->%{public}@"
+ "%{public}@: %{public}@: environment %{public}@ missing"
+ "%{public}@: %{public}@: event identifier invalid"
+ "%{public}@: %{public}@: event identifier missing"
+ "%{public}@: %{public}@: event identifier not provided"
+ "%{public}@: %{public}@: found field %@ with data (unsupported)"
+ "%{public}@: %{public}@: found field %@ with invalid type %@"
+ "%{public}@: %{public}@: found field %@ with missing value"
+ "%{public}@: %{public}@: found field %@ with number %@"
+ "%{public}@: %{public}@: found field %@ with string %@"
+ "%{public}@: %{public}@: individuation identifier invalid"
+ "%{public}@: %{public}@: individuation identifier missing"
+ "%{public}@: %{public}@: individuation identifier not provided"
+ "%{public}@: %{public}@<%{public}@>: Both begin and end times are overridden - assuming they occurred on [%d] thread 0x%#llx and [%d] thread 0x%#llx"
+ "%{public}@: %{public}@<%{public}@>: End signpost with individuation, set as candidate for group"
+ "%{public}@: %{public}@<%{public}@>: End signpost with individuation, still needs %@"
+ "%{public}@: %{public}@<%{public}@>: Handling interval end event as SignpostEvent, not SignpostInterval"
+ "%{public}@: %{public}@<%{public}@>: Handling synthetic event as SignpostEvent, not SignpostInterval"
+ "%{public}@: %{public}@<%{public}@>: Interval start after event end (%.3f later)"
+ "%{public}@: %{public}@<%{public}@>: No missing end signposts, but didn't find an end signpost tracker"
+ "%{public}@: %{public}@<%{public}@>: Saw new individuation identifier with field name %@ needed for end signpost %@"
+ "%{public}@: %{public}@<%{public}@>: candidateEndSignpostTracker is bad class %s"
+ "%{public}@: %{public}@<%{public}@>: contains environment %{public}@ of unsupported type %{public}s"
+ "%{public}@: %{public}@<%{public}@>: contains environment %{public}@->%{public}@"
+ "%{public}@: %{public}@<%{public}@>: environment %{public}@ missing"
+ "%{public}@: %{public}@<%{public}@>: event end %+.3fs @%llu"
+ "%{public}@: %{public}@<%{public}@>: event middle %+.3fs - %+.3fs (%.3fs) @%llu-%llu"
+ "%{public}@: %{public}@<%{public}@>: event middle %+.3fs @%llu"
+ "%{public}@: %{public}@<%{public}@>: fill non-diagnostic signposts: event middle %+.3fs - %+.3fs (%.3fs) @%llu-%llu"
+ "%{public}@: %{public}@<%{public}@>: fill non-diagnostic signposts: event middle %+.3fs @%llu"
+ "%{public}@: %{public}@<%{public}@>: found individuation identifier"
+ "%{public}@: Have %lu open individuated intervals with corresponding end signposts"
+ "%{public}@<%{public}@>: %{public}@: %{public}sevent start @ %@ (%llu)"
+ "%{public}@<%{public}@>: %{public}@: %{public}sevent start @%llu (%+.3fs in previous event)"
+ "%{public}@<%{public}@>: %{public}@: Handling interval end event as SignpostEvent, not SignpostInterval"
+ "%{public}@<%{public}@>: %{public}@: No individuation field name for identifier %@"
+ "%{public}@<%{public}@>: %{public}@: Saw new individuation identifier with field name %@ needed for end signpost %@"
+ "%{public}@<%{public}@>: %{public}@: contains environment %{public}@ of unsupported type %{public}s"
+ "%{public}@<%{public}@>: %{public}@: contains environment %{public}@->%{public}@"
+ "%{public}@<%{public}@>: %{public}@: environment %{public}@ missing"
+ "%{public}@<%{public}@>: %{public}@: found event identifier"
+ "%{public}@<%{public}@>: %{public}@: found field %@ with data (unsupported)"
+ "%{public}@<%{public}@>: %{public}@: found field %@ with invalid type %@"
+ "%{public}@<%{public}@>: %{public}@: found field %@ with missing value"
+ "%{public}@<%{public}@>: %{public}@: found field %@ with number %@"
+ "%{public}@<%{public}@>: %{public}@: found field %@ with string %@"
+ "%{public}@<%{public}@>: %{public}@: individuation identifier invalid"
+ "%{public}@<%{public}@>: %{public}@: individuation identifier missing"
+ "%{public}@<%{public}@>: %{public}@: individuation identifier not provided"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: Both begin and end times are overridden - assuming they occurred on [%d] thread 0x%#llx and [%d] thread 0x%#llx"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: End signpost with individuation, set as candidate for group"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: End signpost with individuation, still needs %@"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: Handling interval end event as SignpostEvent, not SignpostInterval"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: Handling synthetic event as SignpostEvent, not SignpostInterval"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: No missing end signposts, but didn't find an end signpost tracker"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: Saw new individuation identifier with field name %@ needed for end signpost %@"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: candidateEndSignpostTracker is bad class %s"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: contains environment %{public}@ of unsupported type %{public}s"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: contains environment %{public}@->%{public}@"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: environment %{public}@ missing"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: event end %+.3fs @%llu"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: event middle %+.3fs - %+.3fs (%.3fs) @%llu-%llu"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: event middle %+.3fs @%llu"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: fill non-diagnostic signposts: event middle %+.3fs - %+.3fs (%.3fs) @%llu-%llu"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: fill non-diagnostic signposts: event middle %+.3fs @%llu"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: found individuation identifier"
+ "%{public}@<%{public}@>: Have %lu open individuated intervals with corresponding end signposts"
+ "(interval end) "
+ "@88@0:8@16@24@32@40B48@52@60B68@72@80"
+ "Cannot specify both event_identifier_field_name and event_identifier_is_signpost_id for signpost %@"
+ "T@\"NSArray\",R,V_endSignpostsUsingIntervalBegin"
+ "T@\"NSArray\",R,V_startSignpostsUsingIntervalEnd"
+ "Workflow supports concurrent events, but start signpost %@ has no event identifier field name and doesn't use the signpost ID"
+ "_endSignpostsUsingIntervalBegin"
+ "_startOrEndSignpostsWithIntervals"
+ "_startSignpostsUsingIntervalEnd"
+ "endSignpostsUsingIntervalBegin"
+ "end_is_signpost_interval_begin"
+ "event_identifier_is_signpost_id"
+ "event_identifier_is_signpost_id not supported for single-signpost workflows (concurrency support is implicit for all single-signpost workflows with a maximum duration)"
+ "initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:environmentFieldNames:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:"
+ "startSignpostsUsingIntervalEnd"
+ "start_is_signpost_interval_end"
- "%{public}@: %{public}@: %{public}@->%@: Both begin and end times are overridden - assuming they occurred on [%d] thread 0x%#llx and [%d] thread 0x%#llx"
- "%{public}@: %{public}@: %{public}@->%@: End signpost group candidate"
- "%{public}@: %{public}@: %{public}@->%@: End signpost with individuation, set as candidate for group"
- "%{public}@: %{public}@: %{public}@->%@: End signpost with individuation, still needs %@"
- "%{public}@: %{public}@: %{public}@->%@: Handling synthetic event as SignpostEvent, not SignpostInterval"
- "%{public}@: %{public}@: %{public}@->%@: Interval start after event end (%.3f later)"
- "%{public}@: %{public}@: %{public}@->%@: No field value"
- "%{public}@: %{public}@: %{public}@->%@: No missing end signposts, but didn't find an end signpost tracker"
- "%{public}@: %{public}@: %{public}@->%@: Saw new individuation identifier needed for end signpost %@"
- "%{public}@: %{public}@: %{public}@->%@: Unable to get event identifier for start signpost, throwing out all current events in case they were incomplete events"
- "%{public}@: %{public}@: %{public}@->%@: Unable to get event identifier, ignoring signpost"
- "%{public}@: %{public}@: %{public}@->%@: candidateEndSignpostTracker is bad class %s"
- "%{public}@: %{public}@: %{public}@->%@: contained environment %{public}@ not a number/string"
- "%{public}@: %{public}@: %{public}@->%@: contained environment %{public}@->%{public}@"
- "%{public}@: %{public}@: %{public}@->%@: event end %+.3fs @%llu"
- "%{public}@: %{public}@: %{public}@->%@: event middle %+.3fs - %+.3fs (%.3fs) @%llu-%llu"
- "%{public}@: %{public}@: %{public}@->%@: event middle %+.3fs @%llu"
- "%{public}@: %{public}@: %{public}@->%@: fill non-diagnostic signposts: event middle %+.3fs - %+.3fs (%.3fs) @%llu-%llu"
- "%{public}@: %{public}@: %{public}@->%@: fill non-diagnostic signposts: event middle %+.3fs @%llu"
- "%{public}@: %{public}@: %{public}@->%@: found missing individuation identifier"
- "%{public}@: %{public}@: %{public}@->%@: metadata is data type"
- "%{public}@: %{public}@: %{public}@->%@: missing environment %{public}@"
- "%{public}@: %{public}@: %{public}@->%@: outside any workflow event (%llu)"
- "%{public}@: %{public}@: End signpost with individuation, set as candidate for group"
- "%{public}@: %{public}@: End signpost with individuation, still needs %@"
- "%{public}@: %{public}@: No indivudation field name for identifier %@"
- "%{public}@: %{public}@: Saw new individuation identifier needed for end signpost %@"
- "%{public}@: %{public}@: Unable to get event identifier, ignoring signpost"
- "%{public}@: %{public}@: candidateEndSignpostTracker is bad class %s"
- "%{public}@: %{public}@: contained environment %{public}@ not a number/string"
- "%{public}@: %{public}@: contained environment %{public}@->%{public}@"
- "%{public}@: %{public}@: event start @ %@ (%llu)"
- "%{public}@: %{public}@: event start @%llu (%+.3fs in previous event)"
- "%{public}@: %{public}@: missing environment %{public}@"
- "%{public}@<%{public}@>: %{public}@: %{public}@->%@: Both begin and end times are overridden - assuming they occurred on [%d] thread 0x%#llx and [%d] thread 0x%#llx"
- "%{public}@<%{public}@>: %{public}@: %{public}@->%@: End signpost group candidate"
- "%{public}@<%{public}@>: %{public}@: %{public}@->%@: End signpost with individuation, set as candidate for group"
- "%{public}@<%{public}@>: %{public}@: %{public}@->%@: End signpost with individuation, still needs %@"
- "%{public}@<%{public}@>: %{public}@: %{public}@->%@: Handling synthetic event as SignpostEvent, not SignpostInterval"
- "%{public}@<%{public}@>: %{public}@: %{public}@->%@: No field value"
- "%{public}@<%{public}@>: %{public}@: %{public}@->%@: No missing end signposts, but didn't find an end signpost tracker"
- "%{public}@<%{public}@>: %{public}@: %{public}@->%@: Saw new individuation identifier needed for end signpost %@"
- "%{public}@<%{public}@>: %{public}@: %{public}@->%@: candidateEndSignpostTracker is bad class %s"
- "%{public}@<%{public}@>: %{public}@: %{public}@->%@: contained environment %{public}@ not a number/string"
- "%{public}@<%{public}@>: %{public}@: %{public}@->%@: contained environment %{public}@->%{public}@"
- "%{public}@<%{public}@>: %{public}@: %{public}@->%@: event end %+.3fs @%llu"
- "%{public}@<%{public}@>: %{public}@: %{public}@->%@: event middle %+.3fs - %+.3fs (%.3fs) @%llu-%llu"
- "%{public}@<%{public}@>: %{public}@: %{public}@->%@: event middle %+.3fs @%llu"
- "%{public}@<%{public}@>: %{public}@: %{public}@->%@: fill non-diagnostic signposts: event middle %+.3fs - %+.3fs (%.3fs) @%llu-%llu"
- "%{public}@<%{public}@>: %{public}@: %{public}@->%@: fill non-diagnostic signposts: event middle %+.3fs @%llu"
- "%{public}@<%{public}@>: %{public}@: %{public}@->%@: found missing individuation identifier"
- "%{public}@<%{public}@>: %{public}@: %{public}@->%@: metadata is data type"
- "%{public}@<%{public}@>: %{public}@: %{public}@->%@: missing environment %{public}@"
- "%{public}@<%{public}@>: %{public}@: End signpost with individuation, set as candidate for group"
- "%{public}@<%{public}@>: %{public}@: End signpost with individuation, still needs %@"
- "%{public}@<%{public}@>: %{public}@: No indivudation field name for identifier %@"
- "%{public}@<%{public}@>: %{public}@: Saw new individuation identifier needed for end signpost %@"
- "%{public}@<%{public}@>: %{public}@: candidateEndSignpostTracker is bad class %s"
- "%{public}@<%{public}@>: %{public}@: contained environment %{public}@ not a number/string"
- "%{public}@<%{public}@>: %{public}@: contained environment %{public}@->%{public}@"
- "%{public}@<%{public}@>: %{public}@: event start @ %@ (%llu)"
- "%{public}@<%{public}@>: %{public}@: event start @%llu (%+.3fs in previous event)"
- "%{public}@<%{public}@>: %{public}@: missing environment %{public}@"
- "@84@0:8@16@24@32@40@48@56B64@68@76"
- "Workflow supports concurrent events, but start signpost %@ has no event identifier field name"
- "indexOfObject:"
- "initWithSubsystem:category:name:eventIdentifierFieldName:individuationFieldName:environmentFieldNames:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:"

```
