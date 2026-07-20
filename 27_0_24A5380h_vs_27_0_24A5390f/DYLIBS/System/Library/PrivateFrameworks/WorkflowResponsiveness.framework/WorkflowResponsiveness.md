## WorkflowResponsiveness

> `/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-443.0.0.0.0
-  __TEXT.__text: 0x3f128
-  __TEXT.__objc_methlist: 0xa08
+445.0.0.0.0
+  __TEXT.__text: 0x40c68
+  __TEXT.__objc_methlist: 0xa30
   __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x182c
-  __TEXT.__cstring: 0x89f9
-  __TEXT.__oslogstring: 0x5ba2
-  __TEXT.__unwind_info: 0x628
+  __TEXT.__gcc_except_tab: 0x18e4
+  __TEXT.__cstring: 0x8dff
+  __TEXT.__oslogstring: 0x5e6f
+  __TEXT.__unwind_info: 0x648
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x890
+  __DATA_CONST.__const: 0x8c0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9a0
+  __DATA_CONST.__objc_selrefs: 0x9d0
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x1f8
+  __DATA_CONST.__got: 0x1f0
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x52a0
-  __AUTH_CONST.__objc_const: 0x1cc0
+  __AUTH_CONST.__cfstring: 0x54a0
+  __AUTH_CONST.__objc_const: 0x1d20
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0x3d8
+  __AUTH_CONST.__auth_got: 0x3e8
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x1b8
+  __DATA.__objc_ivar: 0x1c0
   __DATA.__data: 0xc0
   __DATA.__common: 0x4
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 730
-  Symbols:   1434
-  CStrings:  703
+  Functions: 749
+  Symbols:   1460
+  CStrings:  720
 
Symbols:
+ +[WRWorkflow additionalPlistDirectory]
+ -[WRDisabledWorkflow disabledViaAllowList]
+ -[WRDisabledWorkflow setDisabledViaAllowList:]
+ -[WRSignpost individuatedBySignpostId]
+ -[WRSignpost initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:individuatedBySignpostId:incidentUUIDFieldName:environmentMetadataArray:networkBound:networkBoundIndeterminate:customEnvironmentCoreAnalyticsEventName:diagnostics:requiredFieldNamesAndValues:requiredLogMessageContents:earlyAllowance:]
+ -[WRWorkflowEventTracker individuationIdentifierForSignpostObject:wrSignpost:]
+ -[WRWorkflowEventTracker scopeQualifiedSignpostIdForSignpostObject:]
+ GCC_except_table113
+ GCC_except_table118
+ GCC_except_table134
+ GCC_except_table137
+ GCC_except_table144
+ GCC_except_table153
+ GCC_except_table64
+ GCC_except_table94
+ _OBJC_IVAR_$_WRDisabledWorkflow._disabledViaAllowList
+ _OBJC_IVAR_$_WRSignpost._individuatedBySignpostId
+ _OUTLINED_FUNCTION_191
+ _OUTLINED_FUNCTION_192
+ _OUTLINED_FUNCTION_193
+ _OUTLINED_FUNCTION_194
+ _OUTLINED_FUNCTION_195
+ _OUTLINED_FUNCTION_196
+ _OUTLINED_FUNCTION_77
+ _WRFindOriginalPlistPath
+ _WRSignpostIndividuatedBySignpostIdKey
+ _WRWorkflowIsAllowed
+ __WRAllowedAdditionalWorkflowNames.allowedNames
+ __WRAllowedAdditionalWorkflowNames.onceToken
+ ____WRAllowedAdditionalWorkflowNames_block_invoke
+ ____directoryEnumerator_block_invoke
+ ___block_descriptor_146_e8_32s40s48s56s64s72s80s88s96s104r112r120r128r136r_e48_"NSError"24?0"NSDictionary"8"NSDictionary"16lr104l8s32l8r112l8r120l8s40l8r128l8s48l8s56l8s64l8r136l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_48_e8_32s40bs_e32_v32?0"NSString"8"NSURL"16^B24ls40l8s32l8
+ __directoryEnumerator
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend$addAllowlist:
+ _objc_msgSend$additionalPlistDirectory
+ _objc_msgSend$dataWithContentsOfURL:options:error:
+ _objc_msgSend$individuatedBySignpostId
+ _objc_msgSend$initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:individuatedBySignpostId:incidentUUIDFieldName:environmentMetadataArray:networkBound:networkBoundIndeterminate:customEnvironmentCoreAnalyticsEventName:diagnostics:requiredFieldNamesAndValues:requiredLogMessageContents:earlyAllowance:
+ _objc_msgSend$set
+ _objc_msgSend$setDisabledViaAllowList:
- -[WRSignpost initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:incidentUUIDFieldName:environmentMetadataArray:networkBound:networkBoundIndeterminate:customEnvironmentCoreAnalyticsEventName:diagnostics:requiredFieldNamesAndValues:requiredLogMessageContents:earlyAllowance:]
- -[WRWorkflowEventTracker individuationIdentifierForSignpostObject:individuationFieldName:]
- GCC_except_table112
- GCC_except_table117
- GCC_except_table133
- GCC_except_table136
- GCC_except_table14
- GCC_except_table143
- GCC_except_table152
- GCC_except_table61
- GCC_except_table93
- _NSURLFileSizeKey
- _OUTLINED_FUNCTION_73
- ___26+[WRWorkflow allWorkflows]_block_invoke_2
- ___block_descriptor_130_e8_32s40s48s56s64s72s80s88s96r104r112r120r_e48_"NSError"24?0"NSDictionary"8"NSDictionary"16lr96l8s32l8r104l8s40l8r112l8s48l8s56l8r120l8s64l8s72l8s80l8s88l8
- _objc_msgSend$dictionaryWithContentsOfURL:error:
- _objc_msgSend$initWithSubsystem:category:name:eventIdentifierFieldName:eventIdentifierIsSignpostId:individuationFieldName:incidentUUIDFieldName:environmentMetadataArray:networkBound:networkBoundIndeterminate:customEnvironmentCoreAnalyticsEventName:diagnostics:requiredFieldNamesAndValues:requiredLogMessageContents:earlyAllowance:
CStrings:
+ "%{public}@: Plist is of unexpected class: %{public}s for url: %{public}@"
+ "%{public}@: Skipping additional-directory workflow not in allow list"
+ "%{public}@: Unable to read in data %{public}@ for url: %{public}@"
+ "%{public}@: Unable to read plist from data in %{public}@: %{public}@"
+ "/System/Library/WorkflowResponsiveness/WorkflowAllowList.plist"
+ "/System/Library/WorkflowResponsiveness/WorkflowPlists"
+ "Allow list at %{public}@ is not a dictionary (root is %{public}s)"
+ "Allow list plist at %{public}@ has non-array %{public}@ key (value is %{public}s)"
+ "Allow list plist at %{public}@ is missing %{public}@ key"
+ "AllowedWorkflows"
+ "Cannot specify both individuation_field_name and individuated_by_signpost_id for signpost %@"
+ "Failed to create directory enumerator for '%{public}@'. This is properly a permissions issue. Check access to the URL."
+ "Non-string entry in allow list %{public}@ (entry is %{public}s)"
+ "Unable to parse allow list at %{public}@: %{public}@"
+ "Unable to read allow list at %{public}@: %{public}@"
+ "individuatedBySignpostId"
+ "individuated_by_signpost_id"
+ "v32@?0@\"NSString\"8@\"NSURL\"16^B24"
- "%{public}@: Unable to read in %{public}@: %{public}@"
```
