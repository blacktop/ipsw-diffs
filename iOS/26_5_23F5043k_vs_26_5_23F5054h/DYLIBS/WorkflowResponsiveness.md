## WorkflowResponsiveness

> `/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness`

```diff

-419.9.0.0.0
-  __TEXT.__text: 0x279a8
-  __TEXT.__auth_stubs: 0x710
-  __TEXT.__objc_methlist: 0x7f0
-  __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0xcfc
-  __TEXT.__cstring: 0x2330
-  __TEXT.__oslogstring: 0x44a3
-  __TEXT.__unwind_info: 0x548
-  __TEXT.__objc_classname: 0x11e
-  __TEXT.__objc_methname: 0x2803
-  __TEXT.__objc_methtype: 0x293
-  __TEXT.__objc_stubs: 0x1da0
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x660
-  __DATA_CONST.__objc_classlist: 0x58
+419.10.0.0.0
+  __TEXT.__text: 0x2dcb4
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__objc_methlist: 0x8b8
+  __TEXT.__const: 0x118
+  __TEXT.__gcc_except_tab: 0x12f8
+  __TEXT.__cstring: 0x2952
+  __TEXT.__oslogstring: 0x47cb
+  __TEXT.__unwind_info: 0x5f0
+  __TEXT.__objc_classname: 0x135
+  __TEXT.__objc_methname: 0x2941
+  __TEXT.__objc_methtype: 0x2a2
+  __TEXT.__objc_stubs: 0x1ec0
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__const: 0x758
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x880
-  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_selrefs: 0x8d0
+  __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x398
-  __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x2120
-  __AUTH_CONST.__objc_const: 0x1730
+  __AUTH_CONST.__auth_got: 0x3a0
+  __AUTH_CONST.__const: 0x300
+  __AUTH_CONST.__cfstring: 0x2820
+  __AUTH_CONST.__objc_const: 0x1940
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x15c
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x178
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x18
+  __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 1A5FC9F4-A7A3-3AA5-87D6-6FEE2F5544C4
-  Functions: 551
-  Symbols:   1856
-  CStrings:  1290
+  UUID: C4122FF5-F94C-3FAD-9428-99A1C6DB5D07
+  Functions: 607
+  Symbols:   2034
+  CStrings:  1433
 
Symbols:
+ +[WREnvironmentMetadata environmentMetadataForWorkflowName:signpostName:environmentMetadataDicts:environmentFieldNames:checkForOverrides:error:]
+ -[WREnvironmentMetadata .cxx_destruct]
+ -[WREnvironmentMetadata applyDict:error:]
+ -[WREnvironmentMetadata copyWithZone:]
+ -[WREnvironmentMetadata debugDescription]
+ -[WREnvironmentMetadata encodedDict]
+ -[WREnvironmentMetadata encodedDict].cold.1
+ -[WREnvironmentMetadata encodedDict].cold.2
+ -[WREnvironmentMetadata fieldName]
+ -[WREnvironmentMetadata hash]
+ -[WREnvironmentMetadata initWithDict:error:]
+ -[WREnvironmentMetadata initWithEncodedDict:error:]
+ -[WREnvironmentMetadata initWithFieldName:]
+ -[WREnvironmentMetadata isEqual:]
+ -[WREnvironmentMetadata mergeStrategy]
+ -[WREnvironmentMetadata name]
+ -[WREnvironmentMetadata sharingOptions]
+ -[WREnvironmentMetadata shouldShareFrom:to:]
+ -[WREnvironmentMetadata valueAfterMergingExistingValue:withNewValue:]
+ -[WRSignpost environmentMetadataArray]
+ -[WRSignpost hasChangesRelativeTo:whatChanged:]
+ -[WRSignpost initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:environmentMetadataArray:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:requiredFieldNamesAndValues:requiredLogMessageContents:]
+ -[WRTimestampAndThread environment]
+ -[WRTimestampAndThread initWithPID:threadID:machContTimeNs:date:environment:]
+ -[WRWorkflow customEnvironmentCoreAnalyticsEventName]
+ -[WRWorkflow hasChangesRelativeTo:whatChanged:]
+ -[WRWorkflowEventTracker workflowEventCompleted]
+ GCC_except_table103
+ GCC_except_table106
+ GCC_except_table121
+ GCC_except_table124
+ GCC_except_table138
+ GCC_except_table177
+ GCC_except_table18
+ GCC_except_table180
+ GCC_except_table181
+ GCC_except_table184
+ GCC_except_table19
+ GCC_except_table20
+ GCC_except_table21
+ GCC_except_table221
+ GCC_except_table23
+ GCC_except_table41
+ GCC_except_table47
+ GCC_except_table88
+ _AllEnvironmentKeys
+ _AllEnvironmentKeys.allEnvironmentKeys
+ _AllEnvironmentKeys.cold.1
+ _AllEnvironmentKeys.onceToken
+ _AllEnvironmentMergeStrategyValues
+ _AllEnvironmentMergeStrategyValues.allowedValues
+ _AllEnvironmentMergeStrategyValues.cold.1
+ _AllEnvironmentMergeStrategyValues.onceToken
+ _AllEnvironmentSharingStrategyValues
+ _AllEnvironmentSharingStrategyValues.allowedValues
+ _AllEnvironmentSharingStrategyValues.cold.1
+ _AllEnvironmentSharingStrategyValues.onceToken
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_WREnvironmentMetadata
+ _OBJC_IVAR_$_WREnvironmentMetadata._fieldName
+ _OBJC_IVAR_$_WREnvironmentMetadata._mergeStrategy
+ _OBJC_IVAR_$_WREnvironmentMetadata._name
+ _OBJC_IVAR_$_WREnvironmentMetadata._sharingOptions
+ _OBJC_IVAR_$_WRSignpost._environmentMetadataArray
+ _OBJC_IVAR_$_WRSignpostTracker._environment
+ _OBJC_IVAR_$_WRTimestampAndThread._environment
+ _OBJC_IVAR_$_WRWorkflow._customEnvironmentCoreAnalyticsEventName
+ _OBJC_IVAR_$_WRWorkflowEventTracker._environment
+ _OBJC_METACLASS_$_WREnvironmentMetadata
+ _OUTLINED_FUNCTION_120
+ _OUTLINED_FUNCTION_121
+ _OUTLINED_FUNCTION_122
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _WRCheckForBadEnvironmentDict
+ _WREnvironmentDisabledKey
+ _WREnvironmentFieldNameKey
+ _WREnvironmentMergeStrategyConcatenateStr
+ _WREnvironmentMergeStrategyFirstStr
+ _WREnvironmentMergeStrategyKey
+ _WREnvironmentMergeStrategyLastStr
+ _WREnvironmentMergeStrategyMaxStr
+ _WREnvironmentMergeStrategyMinStr
+ _WREnvironmentMergeStrategySumStr
+ _WREnvironmentNameKey
+ _WREnvironmentSharingStrategyAllIncludingOtherIndividuationsStr
+ _WREnvironmentSharingStrategyAllStr
+ _WREnvironmentSharingStrategyKey
+ _WREnvironmentSharingStrategyNoneStr
+ _WREnvironmentSharingStrategyOverallWorkflowStr
+ _WRMergeStrategyFromString
+ _WROverrideEnvironmentForSignpost
+ _WRSharingOptionsFromString
+ _WRSignpostEnvironmentKey
+ _WRStringFromMergeStrategy
+ _WRStringFromSharingOptions
+ _WRTaskingKeyBaseForEnvironment
+ _WRWorkflowCustomEnvironmentCoreAnalyticsEventNameKey
+ __OBJC_$_INSTANCE_METHODS_WREnvironmentMetadata
+ __OBJC_$_INSTANCE_VARIABLES_WREnvironmentMetadata
+ __OBJC_$_PROP_LIST_WREnvironmentMetadata
+ __OBJC_CLASS_PROTOCOLS_$_WREnvironmentMetadata
+ __OBJC_CLASS_RO_$_WREnvironmentMetadata
+ __OBJC_METACLASS_RO_$_WREnvironmentMetadata
+ __WRTaskingEnvironmentRemovedDict
+ ___144+[WREnvironmentMetadata environmentMetadataForWorkflowName:signpostName:environmentMetadataDicts:environmentFieldNames:checkForOverrides:error:]_block_invoke
+ ___42-[WRWorkflowProvider registerNotification]_block_invoke.271
+ ___42-[WRWorkflowProvider registerNotification]_block_invoke.271.cold.1
+ ___48-[WRWorkflowEventTracker workflowEventCompleted]_block_invoke
+ ___48-[WRWorkflowEventTracker workflowEventCompleted]_block_invoke_2
+ ___48-[WRWorkflowEventTracker workflowEventCompleted]_block_invoke_3
+ ___48-[WRWorkflowEventTracker workflowEventCompleted]_block_invoke_4
+ ___52-[WRWorkflowEventTracker handleSignpost:wrsignpost:]_block_invoke.236
+ ___52-[WRWorkflowEventTracker initWithEncodedDict:error:]_block_invoke_2
+ ___88-[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:checkForOverrides:error:]_block_invoke.106
+ ___AllEnvironmentKeys_block_invoke
+ ___AllEnvironmentMergeStrategyValues_block_invoke
+ ___AllEnvironmentSharingStrategyValues_block_invoke
+ ___WRCheckForBadEnvironmentDict_block_invoke
+ ____WRTaskingDictAddEnvironment_block_invoke
+ ____WRTaskingFilteredEnvironment_block_invoke
+ ____WRTaskingFilteredEnvironment_block_invoke_2
+ ____WRTaskingFilteredSignposts_block_invoke.cold.1
+ ____WRTaskingFilteredSignposts_block_invoke.cold.2
+ ___block_descriptor_32_e57_q24?0"WREnvironmentMetadata"8"WREnvironmentMetadata"16l
+ ___block_descriptor_48_e8_32r40r_e56_v24?0"WRTimestampAndThread"8"WREnvironmentMetadata"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e15_v32?0816^B24lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e37_"NSDictionary"16?0"SignpostEvent"8ls32l8s40l8
+ ___block_literal_global.110
+ ___block_literal_global.157
+ ___block_literal_global.159
+ ___block_literal_global.161
+ ___block_literal_global.164
+ ___block_literal_global.166
+ ___block_literal_global.219
+ ___block_literal_global.221
+ ___block_literal_global.223
+ ___block_literal_global.244
+ ___block_literal_global.256
+ ___block_literal_global.397
+ ___block_literal_global.572
+ ___block_literal_global.578
+ ___block_literal_global.581
+ ___block_literal_global.87
+ _kWREnvironmentDefaultMergeStrategy
+ _kWREnvironmentDefaultSharingOptions
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$environmentMetadataArray
+ _objc_msgSend$fieldName
+ _objc_msgSend$hasChangesRelativeTo:whatChanged:
+ _objc_msgSend$initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:environmentMetadataArray:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:requiredFieldNamesAndValues:requiredLogMessageContents:
+ _objc_msgSend$mergeStrategy
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$sharingOptions
+ _objc_msgSend$strongToStrongObjectsMapTable
+ _objc_release_x3
- -[WRSignpost hasChangesRelativeTo:]
- -[WRSignpost initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:environmentFieldNames:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:requiredFieldNamesAndValues:requiredLogMessageContents:]
- -[WRTimestampAndThread initWithPID:threadID:machContTimeNs:date:]
- GCC_except_table100
- GCC_except_table117
- GCC_except_table119
- GCC_except_table13
- GCC_except_table133
- GCC_except_table169
- GCC_except_table172
- GCC_except_table175
- GCC_except_table176
- GCC_except_table216
- GCC_except_table42
- GCC_except_table45
- GCC_except_table8
- GCC_except_table97
- _OBJC_IVAR_$_WRSignpost._environmentFieldNames
- _OBJC_IVAR_$_WRSignpostTracker._environmentMutable
- _OUTLINED_FUNCTION_42
- _OUTLINED_FUNCTION_43
- ___37-[WRWorkflowEventTracker environment]_block_invoke
- ___42-[WRWorkflowProvider registerNotification]_block_invoke.228
- ___42-[WRWorkflowProvider registerNotification]_block_invoke.228.cold.1
- ___52-[WRWorkflowEventTracker handleSignpost:wrsignpost:]_block_invoke.215
- ___58-[WRWorkflowEventTracker applySignpost:toSignpostTracker:]_block_invoke.cold.1
- ___88-[WRWorkflow initWithPlist:telemetryEnabled:diagnosticsEnabled:checkForOverrides:error:]_block_invoke.105
- ___block_descriptor_48_e8_32s40s_e23_v16?0"SignpostEvent"8ls32l8s40l8
- ___block_literal_global.109
- ___block_literal_global.115
- ___block_literal_global.117
- ___block_literal_global.220
- ___block_literal_global.226
- ___block_literal_global.376
- ___block_literal_global.548
- ___block_literal_global.554
- ___block_literal_global.557
- ___block_literal_global.71
- _objc_msgSend$environmentFieldNames
- _objc_msgSend$initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:environmentFieldNames:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:requiredFieldNamesAndValues:requiredLogMessageContents:
CStrings:
+ "%@%@%@"
+ "%{public}@: %{public}@: applied environment override for %{public}@: %{public}@ + %{public}@ -> %{public}@"
+ "%{public}@: %{public}@: environment disabled for %{public}@"
+ "%{public}@: %{public}@: environment enabled for %{public}@"
+ "%{public}@: %{public}@: invalid environment disable bool for %{public}@: %{public}@"
+ "%{public}@: %{public}@: invalid environment override dict: %{public}@"
+ "%{public}@: %{public}@: invalid environment override settings for %{public}@: %{public}@"
+ "%{public}@: %{public}@: invalid new environment dict: %{public}@\n%{public}@"
+ "%{public}@: %{public}@: invalid new environment settings: %{public}@"
+ "(invalid)"
+ ", "
+ "@\"NSDictionary\"16@?0@\"SignpostEvent\"8"
+ "B32@0:8@16^@24"
+ "Environment %@ specified more than once"
+ "Environment disabled"
+ "Environment field name %@ specified more than once"
+ "Invalid merge strategy"
+ "Invalid sharing strategy string %@"
+ "Missing required field_name in environment dict: %@"
+ "Shared environment %@ is specified multiple times with conflicting merge strategies"
+ "T@\"NSArray\",R,V_environmentMetadataArray"
+ "T@\"NSDictionary\",R,V_environment"
+ "T@\"NSString\",R,V_fieldName"
+ "TQ,R,V_mergeStrategy"
+ "TQ,R,V_sharingOptions"
+ "Unable to convert sharing options 0x%llx to string"
+ "Unknown environment key \"%@\""
+ "Unknown environment leaf key %@"
+ "Unknown merge strategy 0x%llx"
+ "Unknown merge strategy string \"%@\""
+ "Unknown merge strategy string %@"
+ "Unknown sharing strategy \"%@\""
+ "WREnvironmentMetadata"
+ "WRTimestampAndThread: env key not string (%s)"
+ "WRTimestampAndThread: env value not string nor number (%s)"
+ "Wrong type for signpost environment dict: %s"
+ "Wrong value type for environment key \"%@\": %s, expected %@"
+ "_environment"
+ "_environmentMetadataArray"
+ "_fieldName"
+ "_mergeStrategy"
+ "_sharingOptions"
+ "addObjectsFromArray:"
+ "all"
+ "all_including_other_individuations"
+ "cat"
+ "contextualTelemetry"
+ "endSignpostName"
+ "environment %@ with numeric merge strategy max has non-numeric value %@, ignoring"
+ "environment %@ with numeric merge strategy sum has non-numeric value %@, ignoring"
+ "environmentMetadataArray"
+ "fieldName"
+ "fieldName:%@ name:%@ merge:%@ sharing:%@"
+ "field_name"
+ "first"
+ "hasChangesRelativeTo:whatChanged:"
+ "initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:environmentMetadataArray:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:requiredFieldNamesAndValues:requiredLogMessageContents:"
+ "last"
+ "max"
+ "mergeStrategy"
+ "merge_strategy"
+ "min"
+ "nil environment field_name"
+ "none"
+ "objectForKey:"
+ "overall_workflow"
+ "q24@?0@\"WREnvironmentMetadata\"8@\"WREnvironmentMetadata\"16"
+ "setObject:forKey:"
+ "setWithObjects:"
+ "sharingOptions"
+ "sharing_strategy"
+ "signpost [%lu] %@: %@"
+ "signpost [%lu] %@:%@:%@ -> %@:%@:%@"
+ "startSignpostName"
+ "strongToStrongObjectsMapTable"
+ "sum"
+ "tat_environment"
+ "v24@?0@\"WRTimestampAndThread\"8@\"WREnvironmentMetadata\"16"
+ "wt_environment"
- "!"
- "%@_%@"
- "T@\"NSArray\",R,V_environmentFieldNames"
- "T@\"NSMutableDictionary\",R"
- "_environmentFieldNames"
- "_environmentMutable"
- "initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:environmentFieldNames:networkBound:customEnvironmentCoreAnalyticsEventName:diagnostics:requiredFieldNamesAndValues:requiredLogMessageContents:"
- "v16@?0@\"SignpostEvent\"8"

```
