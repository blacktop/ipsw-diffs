## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`

```diff

-3486.2.4.0.0
-  __TEXT.__text: 0x1e17e8
-  __TEXT.__objc_methlist: 0x111c8
+3486.40.92.0.0
+  __TEXT.__text: 0x1e1ff8
+  __TEXT.__objc_methlist: 0x11270
   __TEXT.__const: 0x700
-  __TEXT.__cstring: 0x2694b
-  __TEXT.__oslogstring: 0x15b6e
+  __TEXT.__cstring: 0x26a1b
+  __TEXT.__oslogstring: 0x15dbe
   __TEXT.__gcc_except_tab: 0x2598
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x6060
+  __TEXT.__unwind_info: 0x6070
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4580
-  __DATA_CONST.__objc_classlist: 0x3a0
+  __DATA_CONST.__const: 0x45a8
+  __DATA_CONST.__objc_classlist: 0x3a8
   __DATA_CONST.__objc_nlclslist: 0x108
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb208
+  __DATA_CONST.__objc_selrefs: 0xb260
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2d8
-  __DATA_CONST.__objc_arraydata: 0x163c8
-  __DATA_CONST.__got: 0xf80
+  __DATA_CONST.__objc_superrefs: 0x2e0
+  __DATA_CONST.__objc_arraydata: 0x16428
+  __DATA_CONST.__got: 0xf88
   __AUTH_CONST.__const: 0x1a40
-  __AUTH_CONST.__cfstring: 0x33f80
-  __AUTH_CONST.__objc_const: 0x168c0
+  __AUTH_CONST.__cfstring: 0x340a0
+  __AUTH_CONST.__objc_const: 0x16a40
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_intobj: 0x28c8
+  __AUTH_CONST.__objc_intobj: 0x28e0
   __AUTH_CONST.__objc_dictobj: 0x3ac0
   __AUTH_CONST.__objc_doubleobj: 0xb90
-  __AUTH_CONST.__objc_arrayobj: 0x2fa0
-  __AUTH_CONST.__auth_got: 0xe00
-  __AUTH.__objc_data: 0xbe0
-  __DATA.__objc_ivar: 0x16c8
+  __AUTH_CONST.__objc_arrayobj: 0x3030
+  __AUTH_CONST.__auth_got: 0xe08
+  __AUTH.__objc_data: 0xc30
+  __DATA.__objc_ivar: 0x16dc
   __DATA.__data: 0x580
   __DATA.__common: 0x74
   __DATA_DIRTY.__objc_data: 0x1860

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 8831
-  Symbols:   16484
-  CStrings:  9088
+  Functions: 8845
+  Symbols:   16518
+  CStrings:  9104
 
Symbols:
+ +[PLUrsaUtilities generateTTRURLWithRadarParams:context:metadataPath:]
+ +[PLUrsaUtilities writeMetadata:toDirectory:]
+ -[PLAggregateSummarizationService getQueryForDisplayAPL:]
+ -[PLCoalitionAgent buildPLEntryDiffForObject:withNewUsage:hasPrevSample:withStartDate:withEndDate:]
+ -[PLCoalitionAgent logOSMetrics:withNewUsage:hasPrevSample:]
+ -[PLCoalitionAgent shouldLogCoalitionObject:withNewUsage:hasPrevSample:]
+ -[PLCoalitionAgent shouldProcessCoalitionID:seenCoalitionIDs:]
+ -[PLMetricsFormatterJSON addDisplayAPL:userData:forIndex:]
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
+ GCC_except_table216
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_PLUrsaViolationContext
+ _OBJC_IVAR_$_PLMetricsFormatterJSON.appDisplayXAPLMapping
+ _OBJC_IVAR_$_PLUrsaViolationContext._internalOnlyRule
+ _OBJC_IVAR_$_PLUrsaViolationContext._issueType
+ _OBJC_IVAR_$_PLUrsaViolationContext._mitigationsEnabled
+ _OBJC_IVAR_$_PLUrsaViolationContext._procName
+ _OBJC_IVAR_$_PLUrsaViolationContext._ruleID
+ _OBJC_IVAR_$_PLUrsaViolationContext._violationTime
+ _OBJC_METACLASS_$_PLUrsaViolationContext
+ __OBJC_$_INSTANCE_METHODS_PLUrsaViolationContext
+ __OBJC_$_INSTANCE_VARIABLES_PLUrsaViolationContext
+ __OBJC_$_PROP_LIST_PLUrsaViolationContext
+ __OBJC_CLASS_RO_$_PLUrsaViolationContext
+ __OBJC_METACLASS_RO_$_PLUrsaViolationContext
+ ___57-[PLAggregateSummarizationService getQueryForDisplayAPL:]_block_invoke
+ ___block_descriptor_41_e8_32s_e17_"NSArray"16?0d8ls32l8
+ _objc_msgSend$addDisplayAPL:userData:forIndex:
+ _objc_msgSend$buildPLEntryDiffForObject:withNewUsage:hasPrevSample:withStartDate:withEndDate:
+ _objc_msgSend$generateTTRURLWithRadarParams:context:metadataPath:
+ _objc_msgSend$getQueryForDisplayAPL:
+ _objc_msgSend$internalOnlyRule
+ _objc_msgSend$issueType
+ _objc_msgSend$logOSMetrics:withNewUsage:hasPrevSample:
+ _objc_msgSend$mitigationsEnabled
+ _objc_msgSend$procName
+ _objc_msgSend$ruleID
+ _objc_msgSend$setInternalOnlyRule:
+ _objc_msgSend$setIssueType:
+ _objc_msgSend$setMitigationsEnabled:
+ _objc_msgSend$setProcName:
+ _objc_msgSend$setRuleID:
+ _objc_msgSend$setViolationTime:
+ _objc_msgSend$shouldLogCoalitionObject:withNewUsage:hasPrevSample:
+ _objc_msgSend$shouldProcessCoalitionID:seenCoalitionIDs:
+ _objc_msgSend$violationTime
+ _objc_msgSend$writeMetadata:toDirectory:
+ _objc_msgSend$writeToURL:options:error:
- +[PLUrsaUtilities generateTTRURLWithRadarParams:procName:mitigationsEnabled:violationTime:metadataPath:issueType:]
- -[PLAggregateSummarizationService getQueryForDisplayAPL]
- -[PLCoalitionAgent buildPLEntryDiffForObject:withStartDate:withEndDate:]
- -[PLCoalitionAgent logCoalitionObjectDifference]
- -[PLCoalitionAgent logOSMetrics:]
- -[PLCoalitionAgent shouldLogCoalitionObject:]
- -[PLCoalitionDataObject hasPrevSample]
- -[PLCoalitionDataObject prevCoalResourceUsage]
- -[PLMetricsFormatterJSON addDisplayAPL:userData:]
- GCC_except_table173
- GCC_except_table219
- _OBJC_IVAR_$_PLCoalitionDataObject._hasPrevSample
- _OBJC_IVAR_$_PLCoalitionDataObject._prevCoalResourceUsage
- ___48-[PLCoalitionAgent logCoalitionObjectDifference]_block_invoke
- ___56-[PLAggregateSummarizationService getQueryForDisplayAPL]_block_invoke
- _logCoalitionObjectDifference.classDebugEnabled
- _logCoalitionObjectDifference.defaultOnce
- _objc_msgSend$addDisplayAPL:userData:
- _objc_msgSend$buildPLEntryDiffForObject:withStartDate:withEndDate:
- _objc_msgSend$createFileAtPath:contents:attributes:
- _objc_msgSend$generateTTRURLWithRadarParams:procName:mitigationsEnabled:violationTime:metadataPath:issueType:
- _objc_msgSend$getQueryForDisplayAPL
- _objc_msgSend$hasPrevSample
- _objc_msgSend$logCoalitionObjectDifference
- _objc_msgSend$logOSMetrics:
- _objc_msgSend$prevCoalResourceUsage
- _objc_msgSend$shouldLogCoalitionObject:
CStrings:
+ "\n\nNOTE: This issue was caught by a detection rule that is enabled on internal builds only. Mitigations for this rule are not applied on customer devices."
+ "                           SELECT bundleID AS %@, SUM(%f * Frames * (%f*AvgRed + %f*AvgGreen + %f*AvgBlue))/SUM(Frames) %@, SUM(Frames) %@ FROM %@                            WHERE timestamp >= %f AND timestamp < %f                           GROUP BY %@;"
+ "\""
+ "$rulePolicy"
+ "AveragePictureLevelX"
+ "DisplayXAPL"
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
+ "TotalFrameCountX"
+ "displayX_apl"
+ "generateTTRURL: called with issueType = %d, ruleID = %d, internalOnlyRule = %d"
+ "internalOnlyRule"
+ "ruleID"
- "                           SELECT bundleID AS %@, SUM(%f * Frames * (%f*AvgRed + %f*AvgGreen + %f*AvgBlue))/SUM(Frames) %@, SUM(Frames) %@ FROM PLDisplayAgent_EventBackward_APLStats                           WHERE timestamp >= %f AND timestamp < %f                           GROUP BY %@;"
- "-[PLCoalitionAgent logCoalitionObjectDifference]"
- "PLUrsaUtilities: created Ursa directory at: %{public}@"
- "PLUrsaUtilities: failed to create Ursa directory: %{public}@"
- "PLUrsaUtilities: failed to create metadata file URL"
- "PLUrsaUtilities: failed to create metadata file with permissions"
- "generateTTRURL: called with issueType = %d"
- "self.lastCoalitionObjectDictionary=%@"
```
