## PowerlogLiteOperators

> `/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/Versions/A/PowerlogLiteOperators`

```diff

-3486.1.2.0.0
-  __TEXT.__text: 0x1fa29c
-  __TEXT.__objc_methlist: 0xd904
-  __TEXT.__const: 0x21a0
+3486.41.1.0.0
+  __TEXT.__text: 0x1fb904
+  __TEXT.__objc_methlist: 0xd9f4
+  __TEXT.__const: 0x21b0
   __TEXT.__swift5_typeref: 0x4f9
   __TEXT.__constg_swiftt: 0x36c
   __TEXT.__swift5_reflstr: 0x3f1

   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__cstring: 0x383ed
+  __TEXT.__cstring: 0x387b5
   __TEXT.__swift5_capture: 0xb8
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift_as_cont: 0x44
-  __TEXT.__oslogstring: 0xca6e
+  __TEXT.__oslogstring: 0xcd55
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__gcc_except_tab: 0x1d9c
   __TEXT.__ustring: 0x12
-  __TEXT.__unwind_info: 0x33a8
+  __TEXT.__unwind_info: 0x33c8
   __TEXT.__eh_frame: 0xdb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3708
-  __DATA_CONST.__objc_classlist: 0x2d0
+  __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_nlclslist: 0x198
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8bf8
+  __DATA_CONST.__objc_selrefs: 0x8ca0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x390
-  __DATA_CONST.__objc_arraydata: 0x5ff0
+  __DATA_CONST.__objc_superrefs: 0x398
+  __DATA_CONST.__objc_arraydata: 0x6090
   __DATA_CONST.__got: 0xbe8
-  __AUTH_CONST.__const: 0x33b8
-  __AUTH_CONST.__cfstring: 0x4d4a0
-  __AUTH_CONST.__objc_const: 0xfc48
+  __AUTH_CONST.__const: 0x33f8
+  __AUTH_CONST.__cfstring: 0x4d900
+  __AUTH_CONST.__objc_const: 0xfe08
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_intobj: 0x4f20
-  __AUTH_CONST.__objc_dictobj: 0x25a8
-  __AUTH_CONST.__objc_arrayobj: 0xf30
-  __AUTH_CONST.__objc_doubleobj: 0xbf0
-  __AUTH_CONST.__auth_got: 0x1348
+  __AUTH_CONST.__objc_intobj: 0x4f38
+  __AUTH_CONST.__objc_dictobj: 0x2620
+  __AUTH_CONST.__objc_arrayobj: 0xfd8
+  __AUTH_CONST.__objc_doubleobj: 0xc00
+  __AUTH_CONST.__auth_got: 0x1350
   __AUTH_CONST.__auth_ptr: 0x258
-  __AUTH.__objc_data: 0x328
+  __AUTH.__objc_data: 0x378
   __AUTH.__data: 0xcf8
-  __DATA.__objc_ivar: 0x47c
+  __DATA.__objc_ivar: 0x494
   __DATA.__data: 0x618
   __DATA.__common: 0x1e8
   __DATA.__bss: 0x24e0
   __DATA_DIRTY.__objc_ivar: 0xb68
   __DATA_DIRTY.__objc_data: 0x1a20
   __DATA_DIRTY.__data: 0x698
-  __DATA_DIRTY.__bss: 0x19f0
+  __DATA_DIRTY.__bss: 0x1a10
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6477
-  Symbols:   12585
-  CStrings:  13003
+  Functions: 6499
+  Symbols:   12636
+  CStrings:  13063
 
Symbols:
+ +[PLUrsaUtilities diagnosticExtensionIDsForProcess:]
+ +[PLUrsaUtilities generateTTRURLWithRadarParams:context:metadataPath:]
+ +[PLUrsaUtilities remoteDiagnosticParamsForProcess:]
+ +[PLUrsaUtilities writeMetadata:toDirectory:]
+ -[PLCoalitionAgent buildPLEntryDiffForObject:withNewUsage:hasPrevSample:withStartDate:withEndDate:]
+ -[PLCoalitionAgent logOSMetrics:withNewUsage:hasPrevSample:]
+ -[PLCoalitionAgent shouldLogCoalitionObject:withNewUsage:hasPrevSample:]
+ -[PLCoalitionAgent shouldProcessCoalitionID:seenCoalitionIDs:]
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
+ GCC_except_table39
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
+ __41-[PLSMCMetricsAgent logPowerDeliveryKeys]_block_invoke
+ __OBJC_$_INSTANCE_METHODS_PLUrsaViolationContext
+ __OBJC_$_INSTANCE_VARIABLES_PLUrsaViolationContext
+ __OBJC_$_PROP_LIST_PLUrsaViolationContext
+ __OBJC_CLASS_RO_$_PLUrsaViolationContext
+ __OBJC_METACLASS_RO_$_PLUrsaViolationContext
+ ___52+[PLUrsaUtilities diagnosticExtensionIDsForProcess:]_block_invoke
+ ___52+[PLUrsaUtilities remoteDiagnosticParamsForProcess:]_block_invoke
+ ___block_descriptor_57_e8_32s40s48s_e25_v32?0"NSString"8Q16^B24l
+ _normalizedProcessName
+ _objc_msgSend$buildPLEntryDiffForObject:withNewUsage:hasPrevSample:withStartDate:withEndDate:
+ _objc_msgSend$code
+ _objc_msgSend$diagnosticExtensionIDsForProcess:
+ _objc_msgSend$fileExistsAtPath:isDirectory:
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
+ _objc_msgSend$setAttributes:ofItemAtPath:error:
+ _objc_msgSend$setKaIDMax:
+ _objc_msgSend$setKaIDMin:
+ _objc_msgSend$shouldLogCoalitionObject:withNewUsage:hasPrevSample:
+ _objc_msgSend$shouldProcessCoalitionID:seenCoalitionIDs:
+ _objc_msgSend$violationTime
+ _objc_msgSend$whitespaceCharacterSet
+ _objc_msgSend$writeMetadata:toDirectory:
+ _objc_msgSend$writeToURL:options:error:
- +[PLUrsaUtilities generateTTRURLWithRadarParams:procName:mitigationsEnabled:violationTime:metadataPath:issueType:]
- -[PLCoalitionAgent buildPLEntryDiffForObject:withStartDate:withEndDate:]
- -[PLCoalitionAgent logCoalitionObjectDifference]
- -[PLCoalitionAgent logOSMetrics:]
- -[PLCoalitionAgent shouldLogCoalitionObject:]
- -[PLCoalitionDataObject hasPrevSample]
- -[PLCoalitionDataObject prevCoalResourceUsage]
- GCC_except_table38
- OBJC_IVAR_$_PLCoalitionDataObject._hasPrevSample
- OBJC_IVAR_$_PLCoalitionDataObject._prevCoalResourceUsage
- ___48-[PLCoalitionAgent logCoalitionObjectDifference]_block_invoke
- ___block_descriptor_49_e8_32s40s_e25_v32?0"NSString"8Q16^B24l
- _objc_msgSend$buildPLEntryDiffForObject:withStartDate:withEndDate:
- _objc_msgSend$createFileAtPath:contents:attributes:
- _objc_msgSend$fileExistsAtPath:
- _objc_msgSend$hasPrevSample
- _objc_msgSend$logCoalitionObjectDifference
- _objc_msgSend$logOSMetrics:
- _objc_msgSend$prevCoalResourceUsage
- _objc_msgSend$shouldLogCoalitionObject:
CStrings:
+ "\n\nNOTE: This issue was caught by a detection rule that is enabled on internal builds only. Mitigations for this rule are not applied on customer devices."
+ "\""
+ "$rulePolicy"
+ "%@: rail is OFF, timestamp=%u, entry=%d"
+ "%@: reached end of buffer, timestamp=%u, entry=%d"
+ "2033894"
+ "ComponentID"
+ "ComponentName"
+ "ComponentVersion"
+ "DeviceClasses"
+ "Drop Box (Multi-device)"
+ "ExtensionIdentifiers"
+ "HomeKitPrimaryResident"
+ "J775d"
+ "Kernel assertions entry: kaID=%llu, duration=%f, count=%zu"
+ "Log Power Delivery Keys to CA, payload=%@"
+ "Nearby"
+ "OpenBandExtraSensesOnLastWLPerMode"
+ "OpenBandExtraSensesPerMode"
+ "OpenBandReadsPerMode"
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
+ "Watch"
+ "Watch,Mac,iPad"
+ "apsd"
+ "assetsd"
+ "atc"
+ "cloudd"
+ "cloudphotod"
+ "com.apple."
+ "com.apple.DiagnosticExtensions.IMDiagnosticExtension"
+ "com.apple.PhotoLibraryServices.PhotosDiagnostics"
+ "com.apple.power.powerDeliveryKeys"
+ "debugDataCompressionFailed"
+ "debugDataDumpSuccess"
+ "debugDataGetFail"
+ "debugDataGetSuccess"
+ "debugDataHandoffToRxBurn"
+ "debugDataRequestDropped"
+ "debugDataRequestDump"
+ "debugDataTrimCalled"
+ "deferredmediad"
+ "devicesharingd"
+ "generateTTRURL: called with issueType = %d, ruleID = %d, internalOnlyRule = %d"
+ "homed"
+ "identityservicesd"
+ "idleStackFlowVCurveCDPAtSlowGC"
+ "imagent"
+ "imdpersistence.imdpersistenceagent"
+ "imdpersistenceagent"
+ "mediastream.mstreamd"
+ "mstreamd"
+ "nanomapscd"
+ "rail = %@, payload = %@"
+ "sanitizeDoneTime"
+ "sanitizeReject"
+ "sanitizeStartTime"
+ "sanitizeStatus"
+ "sharingd"
+ "timer_read64_synced"
- "%@: manually increment timestamp %u at entry %d"
- "%@: reached the end of buffer at entry %d"
- "%@: reached the end of buffer at entry %d due to timestamp jump %u"
- "-[PLCoalitionAgent logCoalitionObjectDifference]"
- "Kernel assertions entry: paID=%llu, duration=%f, count=%zu"
- "PLUrsaUtilities: created Ursa directory at: %{public}@"
- "PLUrsaUtilities: failed to create Ursa directory: %{public}@"
- "PLUrsaUtilities: failed to create metadata file URL"
- "PLUrsaUtilities: failed to create metadata file with permissions"
- "PMUMetricsStatic: rail = %@, payload = %@"
- "generateTTRURL: called with issueType = %d"
- "idleStackPurgeableValidityCurveAtSlowGC"
- "self.lastCoalitionObjectDictionary=%@"
```
