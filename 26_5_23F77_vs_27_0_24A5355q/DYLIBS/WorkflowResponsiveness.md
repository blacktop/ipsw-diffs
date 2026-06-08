## WorkflowResponsiveness

> `/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness`

```diff

-419.10.0.0.0
-  __TEXT.__text: 0x2dcb4
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0x8b8
+435.0.0.0.0
+  __TEXT.__text: 0x3d740
+  __TEXT.__objc_methlist: 0x900
   __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x12f8
-  __TEXT.__cstring: 0x2952
-  __TEXT.__oslogstring: 0x47cb
-  __TEXT.__unwind_info: 0x5f0
-  __TEXT.__objc_classname: 0x135
-  __TEXT.__objc_methname: 0x2941
-  __TEXT.__objc_methtype: 0x2a2
-  __TEXT.__objc_stubs: 0x1ec0
-  __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__const: 0x758
+  __TEXT.__gcc_except_tab: 0x14dc
+  __TEXT.__cstring: 0x86f6
+  __TEXT.__oslogstring: 0x5bce
+  __TEXT.__unwind_info: 0x5e8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x7e0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8d0
+  __DATA_CONST.__objc_selrefs: 0x918
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x3a0
-  __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x2820
-  __AUTH_CONST.__objc_const: 0x1940
+  __DATA_CONST.__got: 0x1e0
+  __AUTH_CONST.__const: 0x360
+  __AUTH_CONST.__cfstring: 0x5140
+  __AUTH_CONST.__objc_const: 0x1a40
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x178
+  __AUTH_CONST.__auth_got: 0x3d8
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x190
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x48
-  __DATA_DIRTY.__objc_data: 0x2d0
-  __DATA_DIRTY.__bss: 0x88
+  __DATA.__bss: 0x58
+  __DATA.__common: 0x4
+  __DATA_DIRTY.__objc_data: 0x320
+  __DATA_DIRTY.__bss: 0xa8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: DF2F73EB-FA5E-3DF3-B870-79106B06DD54
-  Functions: 607
-  Symbols:   2034
-  CStrings:  1433
+  UUID: 1B53496B-A5CA-3DA5-BEA9-27BB2A544BDF
+  Functions: 698
+  Symbols:   2247
+  CStrings:  1656
 
Symbols:
+ -[WRSignpost earlyAllowance]
+ -[WRSignpost incidentUUIDFieldName]
+ -[WRSignpost initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:incidentUUIDFieldName:environmentMetadataArray:networkBound:networkBoundIndeterminate:customEnvironmentCoreAnalyticsEventName:diagnostics:requiredFieldNamesAndValues:requiredLogMessageContents:earlyAllowance:]
+ -[WRSignpost networkBoundIndeterminate]
+ -[WRWorkflowEventTracker eventIdentifierForSignpostObject:wrSignpost:]
+ -[WRWorkflowEventTracker generateTelemetry].cold.7
+ -[WRWorkflowEventTracker generateTelemetry].cold.8
+ -[WRWorkflowEventTracker handleEarlySignpost:allowance:]
+ -[WRWorkflowEventTracker handleReboot]
+ -[WRWorkflowEventTracker handleSignpost:].cold.10
+ -[WRWorkflowEventTracker handleSignpost:].cold.11
+ -[WRWorkflowEventTracker handleSignpost:wrsignpost:].cold.4
+ -[WRWorkflowEventTracker handleSignpost:wrsignpost:].cold.5
+ -[WRWorkflowEventTracker handleSignpost:wrsignpost:].cold.6
+ -[WRWorkflowEventTracker incidentUUID]
+ -[WRWorkflowEventTracker removeStaleEarlySignposts:allowance:currentTimeNs:]
+ GCC_except_table112
+ GCC_except_table117
+ GCC_except_table133
+ GCC_except_table136
+ GCC_except_table150
+ GCC_except_table16
+ GCC_except_table22
+ GCC_except_table93
+ _AllNetworkBoundValues
+ _AllNetworkBoundValues.allowedValues
+ _AllNetworkBoundValues.cold.1
+ _AllNetworkBoundValues.onceToken
+ _DictGetUUID
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_IVAR_$_WRSignpost._earlyAllowance
+ _OBJC_IVAR_$_WRSignpost._incidentUUIDFieldName
+ _OBJC_IVAR_$_WRSignpost._networkBoundIndeterminate
+ _OBJC_IVAR_$_WRWorkflowEventTracker._earlySignposts
+ _OBJC_IVAR_$_WRWorkflowEventTracker._incidentUUID
+ _OBJC_IVAR_$_WRWorkflowEventTracker._mostRecentEndTimeRecordedMachContNs
+ _OUTLINED_FUNCTION_123
+ _OUTLINED_FUNCTION_124
+ _OUTLINED_FUNCTION_125
+ _OUTLINED_FUNCTION_126
+ _OUTLINED_FUNCTION_127
+ _OUTLINED_FUNCTION_128
+ _OUTLINED_FUNCTION_129
+ _OUTLINED_FUNCTION_130
+ _OUTLINED_FUNCTION_131
+ _OUTLINED_FUNCTION_132
+ _OUTLINED_FUNCTION_133
+ _OUTLINED_FUNCTION_134
+ _OUTLINED_FUNCTION_135
+ _OUTLINED_FUNCTION_136
+ _OUTLINED_FUNCTION_137
+ _OUTLINED_FUNCTION_138
+ _OUTLINED_FUNCTION_139
+ _OUTLINED_FUNCTION_140
+ _OUTLINED_FUNCTION_141
+ _OUTLINED_FUNCTION_142
+ _OUTLINED_FUNCTION_143
+ _OUTLINED_FUNCTION_144
+ _OUTLINED_FUNCTION_145
+ _OUTLINED_FUNCTION_146
+ _OUTLINED_FUNCTION_147
+ _OUTLINED_FUNCTION_148
+ _OUTLINED_FUNCTION_149
+ _OUTLINED_FUNCTION_150
+ _OUTLINED_FUNCTION_151
+ _OUTLINED_FUNCTION_152
+ _OUTLINED_FUNCTION_153
+ _OUTLINED_FUNCTION_154
+ _OUTLINED_FUNCTION_155
+ _OUTLINED_FUNCTION_156
+ _OUTLINED_FUNCTION_157
+ _OUTLINED_FUNCTION_158
+ _OUTLINED_FUNCTION_159
+ _OUTLINED_FUNCTION_160
+ _OUTLINED_FUNCTION_161
+ _OUTLINED_FUNCTION_162
+ _OUTLINED_FUNCTION_163
+ _OUTLINED_FUNCTION_164
+ _OUTLINED_FUNCTION_165
+ _OUTLINED_FUNCTION_166
+ _OUTLINED_FUNCTION_167
+ _OUTLINED_FUNCTION_168
+ _OUTLINED_FUNCTION_169
+ _OUTLINED_FUNCTION_170
+ _OUTLINED_FUNCTION_171
+ _OUTLINED_FUNCTION_172
+ _OUTLINED_FUNCTION_173
+ _OUTLINED_FUNCTION_174
+ _OUTLINED_FUNCTION_175
+ _OUTLINED_FUNCTION_176
+ _OUTLINED_FUNCTION_177
+ _OUTLINED_FUNCTION_178
+ _OUTLINED_FUNCTION_179
+ _OUTLINED_FUNCTION_180
+ _OUTLINED_FUNCTION_181
+ _OUTLINED_FUNCTION_182
+ _OUTLINED_FUNCTION_183
+ _OUTLINED_FUNCTION_184
+ _OUTLINED_FUNCTION_185
+ _OUTLINED_FUNCTION_186
+ _OUTLINED_FUNCTION_187
+ _OUTLINED_FUNCTION_188
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _WRNanosecondsFromMachTimeUsingLiveTimebase
+ _WRNanosecondsFromMachTimeUsingLiveTimebase.cold.1
+ _WRNetworkBoundIndeterminateStr
+ _WRSetTelemetryCallback
+ _WRSignpostEarlyAllowanceKey
+ _WRSignpostIncidentUUIDFieldNameKey
+ ___26+[WRWorkflow allWorkflows]_block_invoke.63
+ ___26+[WRWorkflow allWorkflows]_block_invoke.63.cold.1
+ ___42-[WRWorkflowProvider registerNotification]_block_invoke.494
+ ___42-[WRWorkflowProvider registerNotification]_block_invoke.494.cold.1
+ ___52-[WRWorkflowEventTracker handleSignpost:wrsignpost:]_block_invoke.900
+ ___52-[WRWorkflowEventTracker handleSignpost:wrsignpost:]_block_invoke_2
+ ___52-[WRWorkflowEventTracker handleSignpost:wrsignpost:]_block_invoke_2.cold.1
+ ___52-[WRWorkflowEventTracker handleSignpost:wrsignpost:]_block_invoke_2.cold.2
+ ___56-[WRWorkflowEventTracker handleEarlySignpost:allowance:]_block_invoke
+ ___58-[WRWorkflowEventTracker applySignpost:toSignpostTracker:]_block_invoke.490
+ ___88-[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:checkForOverrides:error:]_block_invoke.323
+ ___AllNetworkBoundValues_block_invoke
+ ____wr_sanitize_os_log_format_block_invoke
+ ___block_descriptor_32_e43_q24?0"SignpostObject"8"SignpostObject"16l
+ ___block_descriptor_48_e8_32s40s_e23_v16?0"SignpostEvent"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e41_v32?0"NSString"8"NSMutableArray"16^B24ls32l8
+ ___block_literal_global.1031
+ ___block_literal_global.1381
+ ___block_literal_global.1621
+ ___block_literal_global.1627
+ ___block_literal_global.1633
+ ___block_literal_global.169
+ ___block_literal_global.172
+ ___block_literal_global.174
+ ___block_literal_global.176
+ ___block_literal_global.178
+ ___block_literal_global.24
+ ___block_literal_global.327
+ ___block_literal_global.4
+ ___block_literal_global.567
+ ___block_literal_global.569
+ ___block_literal_global.571
+ ___block_literal_global.605
+ ___block_literal_global.86
+ ___block_literal_global.986
+ ___block_literal_global.992
+ ___stdoutp
+ __wr_sanitize_os_log_format
+ __wr_sanitize_os_log_format.cold.1
+ __wr_sanitize_os_log_format.onceToken
+ __wr_sanitize_os_log_format.regex
+ _fprintf
+ _gWRLogToStdOutLevel
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$UUIDString
+ _objc_msgSend$bytes
+ _objc_msgSend$diagnosticsExceedingThresholds
+ _objc_msgSend$diagnosticsExceedingThresholdsWithEventStartNs:eventEndNs:
+ _objc_msgSend$earlyAllowance
+ _objc_msgSend$incidentUUID
+ _objc_msgSend$incidentUUIDFieldName
+ _objc_msgSend$initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:incidentUUIDFieldName:environmentMetadataArray:networkBound:networkBoundIndeterminate:customEnvironmentCoreAnalyticsEventName:diagnostics:requiredFieldNamesAndValues:requiredLogMessageContents:earlyAllowance:
+ _objc_msgSend$initWithUUIDBytes:
+ _objc_msgSend$initWithUUIDString:
+ _objc_msgSend$networkBoundIndeterminate
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$stringByReplacingMatchesInString:options:range:withTemplate:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- -[WRSignpost initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:environmentMetadataArray:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:requiredFieldNamesAndValues:requiredLogMessageContents:]
- -[WRWorkflowEventTracker eventIdentifierForSignpostObject:wrSignopst:]
- GCC_except_table103
- GCC_except_table106
- GCC_except_table121
- GCC_except_table124
- GCC_except_table138
- GCC_except_table14
- GCC_except_table174
- GCC_except_table177
- GCC_except_table179
- GCC_except_table18
- GCC_except_table180
- GCC_except_table181
- GCC_except_table184
- GCC_except_table19
- GCC_except_table221
- GCC_except_table88
- _OUTLINED_FUNCTION_72
- _OUTLINED_FUNCTION_73
- _OUTLINED_FUNCTION_74
- _OUTLINED_FUNCTION_75
- ___26+[WRWorkflow allWorkflows]_block_invoke.13
- ___26+[WRWorkflow allWorkflows]_block_invoke.13.cold.1
- ___42-[WRWorkflowProvider registerNotification]_block_invoke.271
- ___42-[WRWorkflowProvider registerNotification]_block_invoke.271.cold.1
- ___52-[WRWorkflowEventTracker handleSignpost:wrsignpost:]_block_invoke.236
- ___88-[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:checkForOverrides:error:]_block_invoke.106
- ___block_literal_global.11
- ___block_literal_global.110
- ___block_literal_global.157
- ___block_literal_global.159
- ___block_literal_global.161
- ___block_literal_global.164
- ___block_literal_global.219
- ___block_literal_global.221
- ___block_literal_global.223
- ___block_literal_global.238
- ___block_literal_global.244
- ___block_literal_global.256
- ___block_literal_global.397
- ___block_literal_global.572
- ___block_literal_global.578
- ___block_literal_global.581
- ___block_literal_global.87
- _objc_msgSend$endMachContinuousTime
- _objc_msgSend$initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:environmentMetadataArray:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:requiredFieldNamesAndValues:requiredLogMessageContents:
- _objc_msgSend$startMachContinuousTime
- _objc_msgSend$timeRecordedMachContinuousTime
CStrings:
+ "%"
+ "%@-%@-%@-%@-%@"
+ "%@:%@:%@ (event:%@ indiv:%@ incident:%@ env:%@ caEventName:%@ requiredFields:%lu requiredLogMessageContents:%lu thresholds:%lu early:%.0fs)"
+ "%\\{[^}]*\\}"
+ "%s\n"
+ "%{public}@: %{public}@: Ignoring end signpost %.3fs before start signpost"
+ "%{public}@: %{public}@: No wrsignpost for early signpost"
+ "%{public}@: %{public}@: Not logging %@ to CA: %@"
+ "%{public}@: %{public}@: Start signpost received out of order with end signpost (%.3fs), ignoring and throwing out all current events"
+ "%{public}@: %{public}@: contains incident UUID %@"
+ "%{public}@: %{public}@: contains invalid incident UUID (data length %lu)"
+ "%{public}@: %{public}@: contains invalid incident UUID string (%@)"
+ "%{public}@: %{public}@: contains multiple incident UUIDs, ignoring %@ and using %@"
+ "%{public}@: %{public}@: contains number, not incident UUID (%@)"
+ "%{public}@: %{public}@: dropping early signpost recorded at %llu, %.1fs before now (%llu) (%.1f allowance)"
+ "%{public}@: %{public}@: early signpost interval %llu-%llu outside event time range %llu-%llu, ignoring in stats"
+ "%{public}@: %{public}@: found field %@ with data of %lu bytes"
+ "%{public}@: %{public}@: handling early signpost at %llu, %.1fs before event start (%llu) (%.1f allowance)"
+ "%{public}@: %{public}@: has timestamp %.2fs before workflow event (%llu), ignoring"
+ "%{public}@: %{public}@: holding onto signpost with early allowance recorded at %llu"
+ "%{public}@: %{public}@: holding onto signpost with early allowance recorded at %llu (with overridden timestamp %llu)"
+ "%{public}@: %{public}@: ignoring early signpost ending at %llu, %.1fs before event start (%llu) (%.1f allowance)"
+ "%{public}@: %{public}@: incident UUID missing"
+ "%{public}@: %{public}@: incomplete interval %llu after event end %llu"
+ "%{public}@: %{public}@: signpost interval %llu-%llu outside event time range %llu-%llu"
+ "%{public}@: %{public}@<%{public}@>: Ignoring end signpost %.3fs before start signpost"
+ "%{public}@: %{public}@<%{public}@>: contains incident UUID %@"
+ "%{public}@: %{public}@<%{public}@>: contains invalid incident UUID (data length %lu)"
+ "%{public}@: %{public}@<%{public}@>: contains invalid incident UUID string (%@)"
+ "%{public}@: %{public}@<%{public}@>: contains multiple incident UUIDs, ignoring %@ and using %@"
+ "%{public}@: %{public}@<%{public}@>: contains number, not incident UUID (%@)"
+ "%{public}@: %{public}@<%{public}@>: early signpost interval %llu-%llu outside event time range %llu-%llu, ignoring in stats"
+ "%{public}@: %{public}@<%{public}@>: has timestamp %.2fs before workflow event (%llu), ignoring"
+ "%{public}@: %{public}@<%{public}@>: incident UUID missing"
+ "%{public}@: %{public}@<%{public}@>: incomplete interval %llu after event end %llu"
+ "%{public}@: %{public}@<%{public}@>: signpost interval %llu-%llu outside event time range %llu-%llu"
+ "%{public}@: Not logging %@ to CA: %@"
+ "%{public}@<%{public}@>: %{public}@: Ignoring end signpost %.3fs before start signpost"
+ "%{public}@<%{public}@>: %{public}@: No wrsignpost for early signpost"
+ "%{public}@<%{public}@>: %{public}@: Not logging %@ to CA: %@"
+ "%{public}@<%{public}@>: %{public}@: contains incident UUID %@"
+ "%{public}@<%{public}@>: %{public}@: contains invalid incident UUID (data length %lu)"
+ "%{public}@<%{public}@>: %{public}@: contains invalid incident UUID string (%@)"
+ "%{public}@<%{public}@>: %{public}@: contains multiple incident UUIDs, ignoring %@ and using %@"
+ "%{public}@<%{public}@>: %{public}@: contains number, not incident UUID (%@)"
+ "%{public}@<%{public}@>: %{public}@: dropping early signpost recorded at %llu, %.1fs before now (%llu) (%.1f allowance)"
+ "%{public}@<%{public}@>: %{public}@: early signpost interval %llu-%llu outside event time range %llu-%llu, ignoring in stats"
+ "%{public}@<%{public}@>: %{public}@: found field %@ with data of %lu bytes"
+ "%{public}@<%{public}@>: %{public}@: handling early signpost at %llu, %.1fs before event start (%llu) (%.1f allowance)"
+ "%{public}@<%{public}@>: %{public}@: has timestamp %.2fs before workflow event (%llu), ignoring"
+ "%{public}@<%{public}@>: %{public}@: holding onto signpost with early allowance recorded at %llu"
+ "%{public}@<%{public}@>: %{public}@: holding onto signpost with early allowance recorded at %llu (with overridden timestamp %llu)"
+ "%{public}@<%{public}@>: %{public}@: ignoring early signpost ending at %llu, %.1fs before event start (%llu) (%.1f allowance)"
+ "%{public}@<%{public}@>: %{public}@: incident UUID missing"
+ "%{public}@<%{public}@>: %{public}@: incomplete interval %llu after event end %llu"
+ "%{public}@<%{public}@>: %{public}@: signpost interval %llu-%llu outside event time range %llu-%llu"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: Ignoring end signpost %.3fs before start signpost"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: contains incident UUID %@"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: contains invalid incident UUID (data length %lu)"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: contains invalid incident UUID string (%@)"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: contains multiple incident UUIDs, ignoring %@ and using %@"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: contains number, not incident UUID (%@)"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: early signpost interval %llu-%llu outside event time range %llu-%llu, ignoring in stats"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: has timestamp %.2fs before workflow event (%llu), ignoring"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: incident UUID missing"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: incomplete interval %llu after event end %llu"
+ "%{public}@<%{public}@>: %{public}@<%{public}@>: signpost interval %llu-%llu outside event time range %llu-%llu"
+ "%{public}@<%{public}@>: Not logging %@ to CA: %@"
+ "Cannot specify early_allowance for start/end signpost %@"
+ "Key %@: value is non-UUID string \"%@\""
+ "Unknown network bound value \"%@\""
+ "Wrong value type for signpost key \"%@\": %s, expected NSNumber or NSString"
+ "early_allowance"
+ "environment %@ with numeric merge strategy min has non-numeric value %@, ignoring"
+ "incidentUUIDFieldName"
+ "incident_uuid_field_name"
+ "indeterminate"
+ "networkBoundIndeterminate"
+ "q24@?0@\"SignpostObject\"8@\"SignpostObject\"16"
+ "v16@?0@\"SignpostEvent\"8"
+ "wt_incident_uuid"
- "%@:%@:%@ (event:%@ indiv:%@ env:%@ caEventName:%@ requiredFields:%lu requiredLogMessageContents:%lu thresholds:%lu)"
- "%{public}@: %{public}@: found field %@ with data (unsupported)"
- "%{public}@: incomplete interval %llu after event end %llu"
- "%{public}@: signpost interval %llu-%llu outside event time range %llu-%llu"
- "%{public}@<%{public}@>: %{public}@: found field %@ with data (unsupported)"
- "%{public}@<%{public}@>: incomplete interval %llu after event end %llu"
- "%{public}@<%{public}@>: signpost interval %llu-%llu outside event time range %llu-%llu"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSError\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSString\""
- "@\"SignpostSupportSubsystemCategoryAllowlist\""
- "@\"WRSignpost\""
- "@\"WRTimestampAndThread\""
- "@\"WRWorkflow\""
- "@104@0:8@16@24@32@40B48@52@60B68@72@80@88@96"
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8@\"NSDictionary\"16^@24"
- "@32@0:8@16@?24"
- "@32@0:8@16^@24"
- "@36@0:8@16B24^@28"
- "@40@0:8@16@24@?32"
- "@?"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B32@0:8@16^@24"
- "I16@0:8"
- "JSONObjectWithData:options:error:"
- "NSCopying"
- "Q"
- "Q16@0:8"
- "T@\"NSArray\",R"
- "T@\"NSArray\",R,V_allSignposts"
- "T@\"NSArray\",R,V_diagnostics"
- "T@\"NSArray\",R,V_endSignpostGroups"
- "T@\"NSArray\",R,V_endSignpostsUsingIntervalBegin"
- "T@\"NSArray\",R,V_environmentMetadataArray"
- "T@\"NSArray\",R,V_requiredLogMessageContents"
- "T@\"NSArray\",R,V_startSignposts"
- "T@\"NSArray\",R,V_startSignpostsUsingIntervalEnd"
- "T@\"NSArray\",R,V_workflowDiagnostics"
- "T@\"NSDate\",R,V_date"
- "T@\"NSDictionary\",R"
- "T@\"NSDictionary\",R,V_environment"
- "T@\"NSDictionary\",R,V_requiredFieldNamesAndValues"
- "T@\"NSError\",R"
- "T@\"NSMutableDictionary\",&,V_nonPublicFields"
- "T@\"NSString\",R"
- "T@\"NSString\",R,V_category"
- "T@\"NSString\",R,V_contextualTelemetryRawValue"
- "T@\"NSString\",R,V_customEnvironmentCoreAnalyticsEventName"
- "T@\"NSString\",R,V_eventIdentifierFieldName"
- "T@\"NSString\",R,V_fieldName"
- "T@\"NSString\",R,V_individuationFieldName"
- "T@\"NSString\",R,V_individuationIdentifier"
- "T@\"NSString\",R,V_name"
- "T@\"NSString\",R,V_reportOtherSignpostWithName"
- "T@\"NSString\",R,V_reportProcessesWithName"
- "T@\"NSString\",R,V_reportSpindumpForDispatchQueueWithLabel"
- "T@\"NSString\",R,V_reportSpindumpForThreadWithName"
- "T@\"NSString\",R,V_subsystem"
- "T@\"SignpostSupportSubsystemCategoryAllowlist\",R"
- "T@\"SignpostSupportSubsystemCategoryAllowlist\",R,V_allowListForAllSignposts"
- "T@\"SignpostSupportSubsystemCategoryAllowlist\",R,V_allowListForDiagnostics"
- "T@\"WRSignpost\",R"
- "T@\"WRSignpost\",R,V_signpost"
- "T@\"WRTimestampAndThread\",R"
- "T@\"WRTimestampAndThread\",R,V_end"
- "T@\"WRTimestampAndThread\",R,V_start"
- "T@\"WRWorkflow\",R,V_workflow"
- "TB,R"
- "TB,R,V_contextualTelemetryEnabled"
- "TB,R,V_gatherTailspin"
- "TB,R,V_hasDiagnosticThresholdInterval"
- "TB,R,V_networkBound"
- "TB,R,V_reportOmittingNetworkBoundIntervals"
- "TB,R,V_reportSpindumpForMainThread"
- "TB,R,V_reportSpindumpForThisDispatchQueue"
- "TB,R,V_reportSpindumpForThisThread"
- "TB,R,V_tailspinIncludeOSLogs"
- "TB,R,V_triggerEventTimeout"
- "TB,R,V_workflowSupportsConcurrentEvents"
- "TB,V_ignoreEventTimeouts"
- "TI,R,V_triggerThresholdCount"
- "TQ,R"
- "TQ,R,V_machContTimeNs"
- "TQ,R,V_mergeStrategy"
- "TQ,R,V_numSignpostsContributingToEvents"
- "TQ,R,V_numSignpostsFilteredOut"
- "TQ,R,V_numSignpostsNotInWorkflow"
- "TQ,R,V_numSignpostsOutsideEventTimeRange"
- "TQ,R,V_sharingOptions"
- "TQ,R,V_threadID"
- "Td,R"
- "Td,R,V_maximumEventDuration"
- "Td,R,V_triggerThresholdDurationSingle"
- "Td,R,V_triggerThresholdDurationSum"
- "Td,R,V_triggerThresholdDurationUnion"
- "Ti,R"
- "Ti,R,V_pid"
- "Tq,R"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathExtension:"
- "URLByStandardizingPath"
- "UTF8String"
- "WRDiagnostic"
- "WRDictEncoding"
- "WREnvironmentMetadata"
- "WRIntervalAndThreads"
- "WROpenIndividuatedSignpostInterval"
- "WRSignpost"
- "WRSignpostTracker"
- "WRTimestampAndThread"
- "WRWorkflow"
- "WRWorkflowEventTracker"
- "WRWorkflowProvider"
- "WRWorkflowProviderAllWorkflows"
- "WRWorkflowProviderSingleWorkflow"
- "_allSignpostTrackersMutable"
- "_allSignposts"
- "_allowListForAllSignposts"
- "_allowListForDiagnostics"
- "_callback"
- "_callbackQueue"
- "_candidateEndSignpostTrackers"
- "_category"
- "_concurrentEvents"
- "_contextualTelemetryEnabled"
- "_contextualTelemetryRawValue"
- "_customEnvironmentCoreAnalyticsEventName"
- "_date"
- "_diagnostics"
- "_emitsMutable"
- "_end"
- "_endSignpost"
- "_endSignpostGroups"
- "_endSignpostsUsingIntervalBegin"
- "_environment"
- "_environmentMetadataArray"
- "_error"
- "_eventCompletionCallback"
- "_eventEnd"
- "_eventIdentifier"
- "_eventIdentifierFieldName"
- "_eventIdentifierIsSignpostID"
- "_eventStart"
- "_fieldName"
- "_gatherTailspin"
- "_hasDiagnosticThresholdInterval"
- "_ignoreEventTimeouts"
- "_incompleteIntervalStartsMutable"
- "_individuationFieldName"
- "_individuationIdentifier"
- "_intervalsMutable"
- "_isMiddleOfInterval"
- "_machContTimeNs"
- "_maximumEventDuration"
- "_mergeStrategy"
- "_name"
- "_networkBound"
- "_nonPublicFields"
- "_numSignpostsContributingToEvents"
- "_numSignpostsFilteredOut"
- "_numSignpostsNotInWorkflow"
- "_numSignpostsOutsideEventTimeRange"
- "_openIndividuatedIntervalsWithFieldNameMatchingAnEndSignpostFromBeforeEventStart"
- "_pid"
- "_reportOmittingNetworkBoundIntervals"
- "_reportOtherSignpostWithName"
- "_reportProcessesWithName"
- "_reportSpindumpForDispatchQueueWithLabel"
- "_reportSpindumpForMainThread"
- "_reportSpindumpForThisDispatchQueue"
- "_reportSpindumpForThisThread"
- "_reportSpindumpForThreadWithName"
- "_requiredFieldNamesAndValues"
- "_requiredLogMessageContents"
- "_sharingOptions"
- "_signpost"
- "_start"
- "_startOrEndSignpostsWithIntervals"
- "_startSignpost"
- "_startSignposts"
- "_startSignpostsUsingIntervalEnd"
- "_subsystem"
- "_tailspinIncludeOSLogs"
- "_taskingNotifyToken"
- "_threadID"
- "_timeoutQueue"
- "_timeoutSource"
- "_timestampAndThread"
- "_triggerEventTimeout"
- "_triggerThresholdCount"
- "_triggerThresholdDurationSingle"
- "_triggerThresholdDurationSum"
- "_triggerThresholdDurationUnion"
- "_workflow"
- "_workflowDiagnostics"
- "_workflowName"
- "_workflowSupportsConcurrentEvents"
- "_workflows"
- "_wrSettingsChangedNotifyToken"
- "addCharactersInString:"
- "addObject:"
- "addObjectsFromArray:"
- "addSubsystem:category:"
- "allKeys"
- "allSignpostTrackers"
- "allSignposts"
- "allWorkflows"
- "allocWithZone:"
- "allowList"
- "allowListForAllSignposts"
- "allowListForDiagnostics"
- "alphanumericCharacterSet"
- "argument"
- "argumentObject"
- "array"
- "arrayWithObjects:count:"
- "attributesOfItemAtPath:error:"
- "beginDate"
- "beginEvent"
- "boolValue"
- "bundleForClass:"
- "cleanupWorkflowResponsivenessDiagnosticsDirectory"
- "code"
- "compare:"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "componentsSeparatedByString:"
- "containsObject:"
- "containsString:"
- "contextualTelemetryEnabled"
- "contextualTelemetryRawValue"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "d"
- "d16@0:8"
- "dataUsingEncoding:"
- "dataWithJSONObject:options:error:"
- "date"
- "dateByAddingTimeInterval:"
- "dealloc"
- "debugDescription"
- "defaultManager"
- "description"
- "diagnosticThresholdCount"
- "diagnosticThresholdIntervalSeconds"
- "dictionaryWithContentsOfURL:error:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "domain"
- "doneHandlingSignpostsWithEndTimeMachContNs:"
- "doubleValue"
- "emits"
- "encodedDict"
- "encodedStringWithError:"
- "endDate"
- "endEvent"
- "endMachContinuousTime"
- "endNanoseconds"
- "endSignpost"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
- "environmentFieldNames"
- "errorWithDomain:code:userInfo:"
- "eventEnd"
- "eventIdentifier"
- "eventStart"
- "eventType"
- "exceededDiagnosticThreshold"
- "fieldName"
- "fileExistsAtPath:"
- "fileSize"
- "fileSystemRepresentation"
- "fileType"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "fileURLWithPath:relativeToURL:"
- "firstObject"
- "formUnionWithCharacterSet:"
- "gatherDiagnosticsIfNeeded"
- "gatherTailspin"
- "generateTelemetry"
- "handleSettingsChanged:"
- "handleSignpost:"
- "hasAnySpindumpReports"
- "hasChangesRelativeTo:"
- "hasChangesRelativeTo:whatChanged:"
- "hasDiagnosticThresholdCount"
- "hasDiagnosticThresholdInterval"
- "hasMaximumEventDuration"
- "hasOverallDiagnosticThresholdInterval"
- "hasPrefix:"
- "hasSuffix:"
- "hasTriggerThresholdCount"
- "hasTriggerThresholdDurationSingle"
- "hasTriggerThresholdDurationSum"
- "hasTriggerThresholdDurationUnion"
- "hash"
- "i16@0:8"
- "ignoreEventTimeouts"
- "inMiddleOfEvent"
- "incompleteIntervalStarts"
- "indexOfObject:inSortedRange:options:usingComparator:"
- "indexOfObjectIdenticalTo:"
- "individuationIdentifier"
- "init"
- "initFileURLWithPath:isDirectory:"
- "initForLiveStreamingWithWorkflow:timeoutQueue:eventCompletionCallback:"
- "initForReadbackWithWorkflow:eventCompletionCallback:"
- "initWithBytes:length:encoding:"
- "initWithBytesNoCopy:length:freeWhenDone:"
- "initWithCapacity:"
- "initWithContentsOfURL:error:"
- "initWithData:encoding:"
- "initWithDomain:code:userInfo:"
- "initWithEncodedDict:error:"
- "initWithEncodedString:error:"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "initWithObjects:"
- "initWithObjectsAndKeys:"
- "initWithPattern:options:error:"
- "initWithQueue:"
- "initWithQueue:callback:"
- "initWithSpindump:error:"
- "initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:environmentMetadataArray:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:requiredFieldNamesAndValues:requiredLogMessageContents:"
- "initWithTailspin:error:"
- "initWithTimeIntervalSince1970:"
- "initWithTimeIntervalSinceReferenceDate:"
- "initWithWorkflow:eventCompletionCallback:"
- "initWithWorkflowName:queue:callback:"
- "insertObject:atIndex:"
- "intValue"
- "integerValue"
- "intervals"
- "invert"
- "invertedSet"
- "isEqual:"
- "isEqualToString:"
- "isSyntheticIntervalEvent"
- "isValidForSignpost:"
- "isValidForWorkflow:"
- "lastPathComponent"
- "length"
- "longLongValue"
- "machContTimeNs"
- "makeOverridePlistDirectoryWithError:"
- "mergeStrategy"
- "metadata"
- "metadataSegments"
- "mutableCopy"
- "nonPublicFields"
- "null"
- "numSignpostsContributingToEvents"
- "numSignpostsFilteredOut"
- "numSignpostsNotInWorkflow"
- "numSignpostsOutsideEventTimeRange"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "overallDiagnosticThresholdIntervalSeconds"
- "overridePlistDirectory"
- "overridesBeginTime"
- "overridesEndTime"
- "passesSubsystem:category:"
- "path"
- "pid"
- "placeholderTokens"
- "privacyLevel"
- "processID"
- "processTraceFileWithPath:startDate:endDate:errorOut:"
- "propertyListWithData:options:format:error:"
- "providerForAllWorkflowsWithQueue:callback:"
- "providerForWorkflowWithName:queue:callback:"
- "punctuationCharacterSet"
- "q16@0:8"
- "q24@0:8@16"
- "rangeOfCharacterFromSet:"
- "rangeOfString:options:range:"
- "removeAllObjects"
- "removeCharactersInString:"
- "removeItemAtURL:error:"
- "removeObjectAtIndex:"
- "removeObjectIdenticalTo:"
- "reportOmittingNetworkBoundIntervals"
- "reportOtherSignpostWithName"
- "reportProcessesWithName"
- "reportSpindumpForDispatchQueueWithLabel"
- "reportSpindumpForMainThread"
- "reportSpindumpForThisDispatchQueue"
- "reportSpindumpForThisThread"
- "reportSpindumpForThreadWithName"
- "reset"
- "resourceURL"
- "resourceValuesForKeys:error:"
- "scope"
- "setBeginEventProcessingBlock:"
- "setDateFormat:"
- "setEmitEventProcessingBlock:"
- "setIgnoreEventTimeouts:"
- "setIntervalCompletionProcessingBlock:"
- "setNonPublicFields:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setSubsystemCategoryFilter:"
- "setWithObjects:"
- "sharingOptions"
- "signpost"
- "signpostId"
- "sortUsingComparator:"
- "sortUsingSelector:"
- "sortedArrayUsingSelector:"
- "startMachContinuousTime"
- "startNanoseconds"
- "startSignpost"
- "stats"
- "statsWithEventEndNs:"
- "stringByAppendingFormat:"
- "stringByAppendingString:"
- "stringByDeletingPathExtension"
- "stringFromDate:"
- "stringPrefix"
- "stringValue"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "strongToStrongObjectsMapTable"
- "substringWithRange:"
- "tailspinIncludeOSLogs"
- "threadID"
- "timeIntervalSinceNow"
- "timeIntervalSinceReferenceDate"
- "timeRecordedMachContinuousTime"
- "timeRecordedNanoseconds"
- "timeUntilFirstSignpostNanoseconds"
- "totalDurationNanoseconds"
- "triggerEventTimeout"
- "triggerThresholdCount"
- "triggerThresholdDurationSingle"
- "triggerThresholdDurationSum"
- "triggerThresholdDurationUnion"
- "type"
- "unsignedIntValue"
- "unsignedLongLongValue"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "whitespaceAndNewlineCharacterSet"
- "workflow"
- "workflowSupportsConcurrentEvents"
- "workflowWithName:"
- "workflowWithPlist:checkForOverrides:error:"
- "{?=QQQ}16@0:8"
- "{?={?=QQQQQQ}{?=QQQQQQ}}24@0:8Q16"

```
