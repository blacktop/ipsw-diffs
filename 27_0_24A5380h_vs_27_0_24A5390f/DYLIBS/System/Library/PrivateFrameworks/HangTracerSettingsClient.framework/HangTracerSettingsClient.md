## HangTracerSettingsClient

> `/System/Library/PrivateFrameworks/HangTracerSettingsClient.framework/HangTracerSettingsClient`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-421.0.0.0.0
-  __TEXT.__text: 0x17278
-  __TEXT.__objc_methlist: 0xc94
-  __TEXT.__const: 0x20c2
-  __TEXT.__cstring: 0x31ce
+424.0.0.0.0
+  __TEXT.__text: 0x18c3c
+  __TEXT.__objc_methlist: 0xd8c
+  __TEXT.__const: 0x20e2
+  __TEXT.__cstring: 0x3372
   __TEXT.__gcc_except_tab: 0x1a8
-  __TEXT.__oslogstring: 0x60a
+  __TEXT.__oslogstring: 0xa2f
   __TEXT.__dlopen_cstrs: 0xaf
-  __TEXT.__ustring: 0x822
+  __TEXT.__ustring: 0x83c
   __TEXT.__swift5_typeref: 0x4c3
   __TEXT.__swift5_reflstr: 0x45
   __TEXT.__swift5_assocty: 0x6c0

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x194
   __TEXT.__swift5_types: 0x3c
-  __TEXT.__unwind_info: 0x670
+  __TEXT.__unwind_info: 0x6d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xdc8
-  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb60
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_selrefs: 0xbc8
+  __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x158
-  __DATA_CONST.__got: 0x380
+  __DATA_CONST.__got: 0x3d8
   __AUTH_CONST.__const: 0x608
-  __AUTH_CONST.__cfstring: 0x3980
-  __AUTH_CONST.__objc_const: 0x1670
+  __AUTH_CONST.__cfstring: 0x3900
+  __AUTH_CONST.__objc_const: 0x1960
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x4b0
-  __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0xdc
+  __AUTH_CONST.__auth_got: 0x4d0
+  __AUTH.__objc_data: 0x460
+  __DATA.__objc_ivar: 0x100
   __DATA.__data: 0x6f8
-  __DATA.__bss: 0x36b0
+  __DATA.__bss: 0x3710
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 806
-  Symbols:   1420
-  CStrings:  589
+  Functions: 851
+  Symbols:   1513
+  CStrings:  617
 
Symbols:
+ +[HTPerformanceInformation informationWithExtendedAttribute:]
+ +[HTPerformanceInformation parseLostPerfIntervalsFromObject:]
+ -[HTHangExtendedAttributes getMATUExtendedAttributeNamed:forFileAtPath:]
+ -[HTHangExtendedAttributes hangWindow]
+ -[HTHangExtendedAttributes performanceInformation]
+ -[HTHangExtendedAttributes sampleWindow]
+ -[HTHangsDataEntry hangWindow]
+ -[HTHangsDataEntry initWithPath:hangID:creationDate:duration:processBundleID:processPath:processRecord:isBoosted:isBeingProcessed:performanceInformation:hangWindow:sampleWindow:]
+ -[HTHangsDataEntry performanceInformation]
+ -[HTHangsDataEntry sampleWindow]
+ -[HTPerformanceInformation .cxx_destruct]
+ -[HTPerformanceInformation initWithLostPerfIntervals:]
+ -[HTPerformanceInformation lostPerfIntervals]
+ -[HTPerformanceInformation percentActiveDuringHangWindow:]
+ -[HTPerformanceInformation percentActiveForReason:duringHangWindow:]
+ -[HTPerformanceLostPerfInterval .cxx_destruct]
+ -[HTPerformanceLostPerfInterval initWithIntervalWindow:reason:]
+ -[HTPerformanceLostPerfInterval intervalWindow]
+ -[HTPerformanceLostPerfInterval reason]
+ _HTUIInternalInsightLowPowerModeBody
+ _HTUIInternalInsightLowPowerModeBody.str
+ _HTUIInternalInsightLowPowerModeHeadline
+ _HTUIInternalInsightScreenOffThrottlingBody
+ _HTUIInternalInsightScreenOffThrottlingBody.str
+ _HTUIInternalInsightScreenOffThrottlingHeadline
+ _HTUIInternalInsightThermalThrottlingBody
+ _HTUIInternalInsightThermalThrottlingBody.str
+ _HTUIInternalInsightThermalThrottlingHeadline
+ _HTUIInternalInsightsPlacardLabel
+ _HTUIInternalInsightsPlacardLabel.str
+ _HTUIInternalInsightsSectionTitle
+ _HTUIInternalInsightsSectionTitle.str
+ _HTUIInternalNoClientIssuesDetectedFormat
+ _HTUIInternalNoIssuesDetected
+ _HTUIInternalNoIssuesDetected.str
+ _HTUIInternalSystemConditionsCalloutDurationFormat
+ _HTUIInternalSystemConditionsHUDDisabledStatus
+ _HTUIInternalSystemConditionsHUDDisabledStatus.str
+ _HTUIInternalSystemConditionsHUDEnableLink
+ _HTUIInternalSystemConditionsHUDEnableLink.str
+ _HTUIInternalSystemConditionsLostPerfActiveFormat
+ _HTUIInternalSystemConditionsNoneActive
+ _HTUIInternalSystemConditionsNoneActive.str
+ _HTUIInternalSystemConditionsPlacardLabel
+ _HTUIInternalSystemConditionsPlacardLabel.str
+ _HTUIInternalSystemConditionsSectionTitle
+ _HTUIInternalSystemConditionsSectionTitle.str
+ _HTUIInternalSystemConditionsTraceCoverageNotice
+ _HTUIInternalSystemConditionsTraceCoverageNotice.str
+ _MATU_TO_MS
+ _NSStringFromClass
+ _OBJC_CLASS_$_HTPerformanceInformation
+ _OBJC_CLASS_$_HTPerformanceLostPerfInterval
+ _OBJC_IVAR_$_HTHangExtendedAttributes._hangWindow
+ _OBJC_IVAR_$_HTHangExtendedAttributes._performanceInformation
+ _OBJC_IVAR_$_HTHangExtendedAttributes._sampleWindow
+ _OBJC_IVAR_$_HTHangsDataEntry._hangWindow
+ _OBJC_IVAR_$_HTHangsDataEntry._performanceInformation
+ _OBJC_IVAR_$_HTHangsDataEntry._sampleWindow
+ _OBJC_IVAR_$_HTPerformanceInformation._lostPerfIntervals
+ _OBJC_IVAR_$_HTPerformanceLostPerfInterval._intervalWindow
+ _OBJC_IVAR_$_HTPerformanceLostPerfInterval._reason
+ _OBJC_METACLASS_$_HTPerformanceInformation
+ _OBJC_METACLASS_$_HTPerformanceLostPerfInterval
+ __OBJC_$_CLASS_METHODS_HTPerformanceInformation
+ __OBJC_$_INSTANCE_METHODS_HTPerformanceInformation
+ __OBJC_$_INSTANCE_METHODS_HTPerformanceLostPerfInterval
+ __OBJC_$_INSTANCE_VARIABLES_HTPerformanceInformation
+ __OBJC_$_INSTANCE_VARIABLES_HTPerformanceLostPerfInterval
+ __OBJC_$_PROP_LIST_HTPerformanceInformation
+ __OBJC_$_PROP_LIST_HTPerformanceLostPerfInterval
+ __OBJC_CLASS_RO_$_HTPerformanceInformation
+ __OBJC_CLASS_RO_$_HTPerformanceLostPerfInterval
+ __OBJC_METACLASS_RO_$_HTPerformanceInformation
+ __OBJC_METACLASS_RO_$_HTPerformanceLostPerfInterval
+ _kHTExtendedAttributeHangEnd
+ _kHTExtendedAttributeHangStart
+ _kHTExtendedAttributeSampleEnd
+ _kHTExtendedAttributeSampleStart
+ _kHTLostPerfJSONKeyEndMATU
+ _kHTLostPerfJSONKeyIntervals
+ _kHTLostPerfJSONKeyReason
+ _kHTLostPerfJSONKeyStartMATU
+ _objc_msgSend$getMATUExtendedAttributeNamed:forFileAtPath:
+ _objc_msgSend$hangWindow
+ _objc_msgSend$informationWithExtendedAttribute:
+ _objc_msgSend$initWithIntervalWindow:reason:
+ _objc_msgSend$initWithLostPerfIntervals:
+ _objc_msgSend$initWithPath:hangID:creationDate:duration:processBundleID:processPath:processRecord:isBoosted:isBeingProcessed:performanceInformation:hangWindow:sampleWindow:
+ _objc_msgSend$intervalWindow
+ _objc_msgSend$lostPerfIntervals
+ _objc_msgSend$parseLostPerfIntervalsFromObject:
+ _objc_msgSend$performanceInformation
+ _objc_msgSend$reason
+ _objc_msgSend$sampleWindow
+ _objc_retain_x26
+ _objc_retain_x28
+ _objc_retain_x4
+ _strtoull
- -[HTHangsDataEntry initWithPath:hangID:creationDate:duration:processBundleID:processPath:processRecord:isBoosted:isBeingProcessed:]
- ___72-[HTHangsDataFinder findEventsFilteringDeveloperApps:completionHandler:]_block_invoke_2
- ___90-[HTHangsDataFinder initWithLogUpdateCallback:tailspinSavedCallback:tailspinDoneCallback:]_block_invoke_2
- ___90-[HTHangsDataFinder initWithLogUpdateCallback:tailspinSavedCallback:tailspinDoneCallback:]_block_invoke_3
- _objc_msgSend$initWithPath:hangID:creationDate:duration:processBundleID:processPath:processRecord:isBoosted:isBeingProcessed:
- _objc_retain_x27
CStrings:
+ "%@ – %@ (%@)"
+ "(nil)"
+ "HTHangExtendedAttributes: hangID=%{public}@ perfXattr=%{public}s length=%lu intervalCount=%lu"
+ "HTHangsDataFinder: URL %{public}@ does not have extended attributes, skipping"
+ "HTHangsDataFinder: adding %lu entries to list of results"
+ "HTHangsDataFinder: assembled entry hangID=%{public}@ path=%{public}@ performanceInformation=%{public}s lostPerfIntervalCount=%lu"
+ "HTHangsDataFinder: entry at path %{public}@ is missing bundle id or hang id: skipping."
+ "HTHangsDataFinder: error finding entries for type: %lu"
+ "HTHangsDataFinder: error looking for hang logs at path %{public}@ error: %{public}@"
+ "HTHangsDataFinder: finding hang events (filtering on developer apps: %d)"
+ "HTHangsDataFinder: found %lu pending hangs entries"
+ "HTHangsDataFinder: getting pending hangs list (filtering on developer apps: %d)"
+ "HTHangsDataFinder: looking for data entries at path %{public}@"
+ "HTHangsDataFinder: unable to retrieve information about app with bundle id %{public}@ (Error: %{public}@)"
+ "HTPerformanceInformation: parsed xattr payload (length=%lu intervalCount=%lu)"
+ "HTPerformanceInformation: xattr payload failed to parse as JSON: %{public}@"
+ "HTPerformanceInformation: xattr payload was not a JSON object (class=%{public}@)"
+ "HTUIInternalInsightLowPowerModeBody"
+ "HTUIInternalInsightLowPowerModeHeadline"
+ "HTUIInternalInsightScreenOffThrottlingBody"
+ "HTUIInternalInsightScreenOffThrottlingHeadline"
+ "HTUIInternalInsightThermalThrottlingBody"
+ "HTUIInternalInsightThermalThrottlingHeadline"
+ "HTUIInternalInsightsPlacardLabel"
+ "HTUIInternalInsightsSectionTitle"
+ "HTUIInternalNoClientIssuesDetectedFormat"
+ "HTUIInternalNoIssuesDetected"
+ "HTUIInternalSystemConditionsCalloutDurationFormat"
+ "HTUIInternalSystemConditionsHUDDisabledStatus"
+ "HTUIInternalSystemConditionsHUDEnableLink"
+ "HTUIInternalSystemConditionsLostPerfActiveFormat"
+ "HTUIInternalSystemConditionsNoneActive"
+ "HTUIInternalSystemConditionsPlacardLabel"
+ "HTUIInternalSystemConditionsSectionTitle"
+ "HTUIInternalSystemConditionsTraceCoverageNotice"
+ "No %@ issues detected."
+ "absent"
+ "present"
- "Adding %lu entries to list of results"
- "Entry at path %@ is missing bundle id or hang id: skipping."
- "Error looking for hang logs at path %@ error: %@"
- "Finding hang events (filtering on developer apps: %d)"
- "Found %lu pending hangs entries"
- "Getting pending hangs list (filtering on developer apps: %d)"
- "Looking for data entries at path %@"
- "There was an error finding entries for type: %lu"
- "URL %@ does not have extended attributes, skipping"
- "Unable to retrieve information about app with bundle id %@ (Error: %@)"
```
