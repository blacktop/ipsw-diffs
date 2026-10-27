## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/Versions/A/PowerlogHelperdOperators`

```diff

-3486.1.2.0.0
-  __TEXT.__text: 0x113354
-  __TEXT.__objc_methlist: 0xa718
-  __TEXT.__const: 0x4b0
-  __TEXT.__cstring: 0x167e3
-  __TEXT.__oslogstring: 0xb06e
+3486.41.1.0.0
+  __TEXT.__text: 0x11452c
+  __TEXT.__objc_methlist: 0xa808
+  __TEXT.__const: 0x4c0
+  __TEXT.__cstring: 0x16a94
+  __TEXT.__oslogstring: 0xb40e
   __TEXT.__gcc_except_tab: 0x1cf0
-  __TEXT.__unwind_info: 0x2580
+  __TEXT.__unwind_info: 0x25a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2260
-  __DATA_CONST.__objc_classlist: 0x230
+  __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_nlclslist: 0xb0
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x72f0
+  __DATA_CONST.__objc_selrefs: 0x7390
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1d0
-  __DATA_CONST.__objc_arraydata: 0x2af8
+  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_arraydata: 0x2ba8
   __DATA_CONST.__got: 0xac0
-  __AUTH_CONST.__const: 0x2bc8
-  __AUTH_CONST.__cfstring: 0x20840
-  __AUTH_CONST.__objc_const: 0xd578
+  __AUTH_CONST.__const: 0x2c38
+  __AUTH_CONST.__cfstring: 0x20d00
+  __AUTH_CONST.__objc_const: 0xd758
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_doubleobj: 0x640
-  __AUTH_CONST.__objc_intobj: 0x1428
-  __AUTH_CONST.__objc_dictobj: 0x1e78
-  __AUTH_CONST.__objc_arrayobj: 0xc90
-  __AUTH_CONST.__auth_got: 0xb78
+  __AUTH_CONST.__objc_doubleobj: 0x650
+  __AUTH_CONST.__objc_intobj: 0x1440
+  __AUTH_CONST.__objc_dictobj: 0x1ef0
+  __AUTH_CONST.__objc_arrayobj: 0xd50
+  __AUTH_CONST.__auth_got: 0xb80
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x9b0
-  __DATA.__objc_ivar: 0xd94
+  __AUTH.__objc_data: 0x9d8
+  __DATA.__objc_ivar: 0xdb0
   __DATA.__data: 0x3a0
-  __DATA.__bss: 0xe50
+  __DATA.__bss: 0xe60
   __DATA.__common: 0x74
-  __DATA_DIRTY.__objc_data: 0xc30
-  __DATA_DIRTY.__bss: 0x2b8
+  __DATA_DIRTY.__objc_data: 0xc58
+  __DATA_DIRTY.__bss: 0x2c0
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5303
-  Symbols:   10662
-  CStrings:  5470
+  Functions: 5330
+  Symbols:   10715
+  CStrings:  5518
 
Symbols:
+ +[PLUrsaUtilities diagnosticExtensionIDsForProcess:]
+ +[PLUrsaUtilities generateTTRURLWithRadarParams:context:metadataPath:]
+ +[PLUrsaUtilities remoteDiagnosticParamsForProcess:]
+ +[PLUrsaUtilities writeMetadata:toDirectory:]
+ -[PLAggregateSummarizationService getQueryForDisplayAPL:]
+ -[PLCoalitionAgent buildPLEntryDiffForObject:withNewUsage:hasPrevSample:withStartDate:withEndDate:]
+ -[PLCoalitionAgent logOSMetrics:withNewUsage:hasPrevSample:]
+ -[PLCoalitionAgent shouldLogCoalitionObject:withNewUsage:hasPrevSample:]
+ -[PLCoalitionAgent shouldProcessCoalitionID:seenCoalitionIDs:]
+ -[PLMetricsFormatterJSON addDisplayAPL:userData:forIndex:]
+ -[PLSleepWakeAgent kaIDMax]
+ -[PLSleepWakeAgent kaIDMin]
+ -[PLSleepWakeAgent setKaIDMax:]
+ -[PLSleepWakeAgent setKaIDMin:]
+ -[PLUrsaViolationContext .cxx_destruct]
+ -[PLUrsaViolationContext init]
+ -[PLUrsaViolationContext internalOnlyRule]
+ -[PLUrsaViolationContext issueType]
+ -[PLUrsaViolationContext mitigationsEnabled]
+ -[PLUrsaViolationContext procName]
+ -[PLUrsaViolationContext ruleID]
+ -[PLUrsaViolationContext setInternalOnlyRule:]
+ -[PLUrsaViolationContext setIssueType:]
+ -[PLUrsaViolationContext setMitigationsEnabled:]
+ -[PLUrsaViolationContext setProcName:]
+ -[PLUrsaViolationContext setRuleID:]
+ -[PLUrsaViolationContext setViolationTime:]
+ -[PLUrsaViolationContext violationTime]
+ OBJC_IVAR_$_PLMetricsFormatterJSON.appDisplayXAPLMapping
+ OBJC_IVAR_$_PLSleepWakeAgent._kaIDMax
+ OBJC_IVAR_$_PLSleepWakeAgent._kaIDMin
+ OBJC_IVAR_$_PLUrsaViolationContext._internalOnlyRule
+ OBJC_IVAR_$_PLUrsaViolationContext._issueType
+ OBJC_IVAR_$_PLUrsaViolationContext._mitigationsEnabled
+ OBJC_IVAR_$_PLUrsaViolationContext._procName
+ OBJC_IVAR_$_PLUrsaViolationContext._ruleID
+ OBJC_IVAR_$_PLUrsaViolationContext._violationTime
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_PLUrsaViolationContext
+ _OBJC_METACLASS_$_PLUrsaViolationContext
+ __OBJC_$_INSTANCE_METHODS_PLUrsaViolationContext
+ __OBJC_$_INSTANCE_VARIABLES_PLUrsaViolationContext
+ __OBJC_$_PROP_LIST_PLUrsaViolationContext
+ __OBJC_CLASS_RO_$_PLUrsaViolationContext
+ __OBJC_METACLASS_RO_$_PLUrsaViolationContext
+ ___52+[PLUrsaUtilities diagnosticExtensionIDsForProcess:]_block_invoke
+ ___52+[PLUrsaUtilities remoteDiagnosticParamsForProcess:]_block_invoke
+ ___57-[PLAggregateSummarizationService getQueryForDisplayAPL:]_block_invoke
+ ___block_descriptor_41_e8_32s_e17_"NSArray"16?0d8l
+ _normalizedProcessName
+ _objc_msgSend$addDisplayAPL:userData:forIndex:
+ _objc_msgSend$buildPLEntryDiffForObject:withNewUsage:hasPrevSample:withStartDate:withEndDate:
+ _objc_msgSend$code
+ _objc_msgSend$diagnosticExtensionIDsForProcess:
+ _objc_msgSend$getQueryForDisplayAPL:
+ _objc_msgSend$internalOnlyRule
+ _objc_msgSend$issueType
+ _objc_msgSend$kaIDMax
+ _objc_msgSend$kaIDMin
+ _objc_msgSend$logOSMetrics:withNewUsage:hasPrevSample:
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$mitigationsEnabled
+ _objc_msgSend$procName
+ _objc_msgSend$remoteDiagnosticParamsForProcess:
+ _objc_msgSend$ruleID
+ _objc_msgSend$setKaIDMax:
+ _objc_msgSend$setKaIDMin:
+ _objc_msgSend$shouldLogCoalitionObject:withNewUsage:hasPrevSample:
+ _objc_msgSend$shouldProcessCoalitionID:seenCoalitionIDs:
+ _objc_msgSend$violationTime
+ _objc_msgSend$whitespaceCharacterSet
+ _objc_msgSend$writeMetadata:toDirectory:
+ _objc_msgSend$writeToURL:options:error:
+ diagnosticExtensionIDsForProcess:.mapping
+ diagnosticExtensionIDsForProcess:.onceToken
+ remoteDiagnosticParamsForProcess:.mapping
+ remoteDiagnosticParamsForProcess:.onceToken
- +[PLUrsaUtilities generateTTRURLWithRadarParams:procName:mitigationsEnabled:violationTime:metadataPath:issueType:]
- -[PLAggregateSummarizationService getQueryForDisplayAPL]
- -[PLCoalitionAgent buildPLEntryDiffForObject:withStartDate:withEndDate:]
- -[PLCoalitionAgent logCoalitionObjectDifference]
- -[PLCoalitionAgent logOSMetrics:]
- -[PLCoalitionAgent shouldLogCoalitionObject:]
- -[PLCoalitionDataObject hasPrevSample]
- -[PLCoalitionDataObject prevCoalResourceUsage]
- -[PLMetricsFormatterJSON addDisplayAPL:userData:]
- OBJC_IVAR_$_PLCoalitionDataObject._hasPrevSample
- OBJC_IVAR_$_PLCoalitionDataObject._prevCoalResourceUsage
- ___48-[PLCoalitionAgent logCoalitionObjectDifference]_block_invoke
- ___56-[PLAggregateSummarizationService getQueryForDisplayAPL]_block_invoke
- _objc_msgSend$addDisplayAPL:userData:
- _objc_msgSend$buildPLEntryDiffForObject:withStartDate:withEndDate:
- _objc_msgSend$createFileAtPath:contents:attributes:
- _objc_msgSend$getQueryForDisplayAPL
- _objc_msgSend$hasPrevSample
- _objc_msgSend$logCoalitionObjectDifference
- _objc_msgSend$logOSMetrics:
- _objc_msgSend$prevCoalResourceUsage
- _objc_msgSend$shouldLogCoalitionObject:
- logCoalitionObjectDifference.classDebugEnabled
- logCoalitionObjectDifference.defaultOnce
CStrings:
+ "\n\nNOTE: This issue was caught by a detection rule that is enabled on internal builds only. Mitigations for this rule are not applied on customer devices."
+ "                           SELECT bundleID AS %@, SUM(%f * Frames * (%f*AvgRed + %f*AvgGreen + %f*AvgBlue))/SUM(Frames) %@, SUM(Frames) %@ FROM %@                            WHERE timestamp >= %f AND timestamp < %f                           GROUP BY %@;"
+ "\""
+ "$rulePolicy"
+ "2033894"
+ "AveragePictureLevelX"
+ "ComponentID"
+ "ComponentName"
+ "ComponentVersion"
+ "DeviceClasses"
+ "DisplayXAPL"
+ "Drop Box (Multi-device)"
+ "ExtensionIdentifiers"
+ "HomeKitPrimaryResident"
+ "Kernel assertions entry: kaID=%llu, duration=%f, count=%zu"
+ "Nearby"
+ "PLDisplayAgent_EventBackward_APLStats"
+ "PLDisplayAgent_EventBackward_APLStatsX"
+ "PLUrsaUtilities: %{public}@ exists but is not a directory"
+ "PLUrsaUtilities: could not remove existing metadata at %{public}@, overwriting in place: %{public}@"
+ "PLUrsaUtilities: could not set permissions on %{public}@, continuing: %{public}@"
+ "PLUrsaUtilities: could not write metadata to %{public}@, falling back to %{public}@"
+ "PLUrsaUtilities: created directory at: %{public}@"
+ "PLUrsaUtilities: failed to create directory %{public}@: errno=%d (%{public}s) error=%{public}@"
+ "PLUrsaUtilities: failed to create metadata file URL in %{public}@"
+ "PLUrsaUtilities: failed to write metadata to %{public}@: errno=%d (%{public}s) error=%{public}@"
+ "PLUrsaUtilities: failed to write metadata to both %{public}@ and %{public}@"
+ "PLUrsaUtilities: invalid metadata directory"
+ "PLUrsaUtilities: nil violation context"
+ "PLUrsaUtilities: requesting diagnostic extensions %{public}@ for %{public}@"
+ "PLUrsaUtilities: requesting remote device diagnostics for %{public}@: %{public}@ (component %{public}@ -> %{public}@)"
+ "PowerExceptions"
+ "RemoteDeviceSelections"
+ "TotalFrameCountX"
+ "Watch"
+ "Watch,Mac,iPad"
+ "apsd"
+ "assetsd"
+ "atc"
+ "cloudd"
+ "cloudphotod"
+ "com.apple.DiagnosticExtensions.IMDiagnosticExtension"
+ "com.apple.PhotoLibraryServices.PhotosDiagnostics"
+ "deferredmediad"
+ "devicesharingd"
+ "displayX_apl"
+ "generateTTRURL: called with issueType = %d, ruleID = %d, internalOnlyRule = %d"
+ "getSignpostMetricsWithStartDate returned launchDurations=%lu extendedLaunchDurations=%lu launchesTimeSeries=%lu bundleIDs(launchDurations)=%@"
+ "homed"
+ "identityservicesd"
+ "imagent"
+ "imdpersistence.imdpersistenceagent"
+ "imdpersistenceagent"
+ "mediastream.mstreamd"
+ "mstreamd"
+ "nanomapscd"
+ "sharingd"
- "                           SELECT bundleID AS %@, SUM(%f * Frames * (%f*AvgRed + %f*AvgGreen + %f*AvgBlue))/SUM(Frames) %@, SUM(Frames) %@ FROM PLDisplayAgent_EventBackward_APLStats                           WHERE timestamp >= %f AND timestamp < %f                           GROUP BY %@;"
- "-[PLCoalitionAgent logCoalitionObjectDifference]"
- "Kernel assertions entry: paID=%llu, duration=%f, count=%zu"
- "PLUrsaUtilities: created Ursa directory at: %{public}@"
- "PLUrsaUtilities: failed to create Ursa directory: %{public}@"
- "PLUrsaUtilities: failed to create metadata file URL"
- "PLUrsaUtilities: failed to create metadata file with permissions"
- "generateTTRURL: called with issueType = %d"
- "self.lastCoalitionObjectDictionary=%@"
```
