## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/Versions/A/PowerlogCore`

```diff

-3486.1.2.0.0
-  __TEXT.__text: 0xd230c
-  __TEXT.__objc_methlist: 0x8ad0
-  __TEXT.__const: 0x668
-  __TEXT.__cstring: 0x406a5
-  __TEXT.__oslogstring: 0x7220
-  __TEXT.__gcc_except_tab: 0x2140
-  __TEXT.__unwind_info: 0x3c40
+3486.40.92.0.0
+  __TEXT.__text: 0xd2f78
+  __TEXT.__objc_methlist: 0x8b50
+  __TEXT.__const: 0x660
+  __TEXT.__cstring: 0x407d6
+  __TEXT.__oslogstring: 0x73c4
+  __TEXT.__gcc_except_tab: 0x2160
+  __TEXT.__unwind_info: 0x3c80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xe28
+  __DATA_CONST.__const: 0xe68
   __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_nlclslist: 0x80
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x51c8
+  __DATA_CONST.__objc_selrefs: 0x5218
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2b0
-  __DATA_CONST.__objc_arraydata: 0x44360
+  __DATA_CONST.__objc_arraydata: 0x444b0
   __DATA_CONST.__got: 0x618
   __AUTH_CONST.__const: 0x37a0
-  __AUTH_CONST.__cfstring: 0x68d00
+  __AUTH_CONST.__cfstring: 0x68f60
   __AUTH_CONST.__objc_const: 0x9cc8
-  __AUTH_CONST.__objc_intobj: 0x4c08
+  __AUTH_CONST.__objc_intobj: 0x4c20
   __AUTH_CONST.__objc_doubleobj: 0x14d0
   __AUTH_CONST.__objc_arrayobj: 0x1008
-  __AUTH_CONST.__objc_dictobj: 0xf410
+  __AUTH_CONST.__objc_dictobj: 0xf4b0
   __AUTH_CONST.__auth_got: 0xb20
   __AUTH.__objc_data: 0x460
   __DATA.__objc_ivar: 0x708

   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1c70
   __DATA_DIRTY.__data: 0x14
-  __DATA_DIRTY.__bss: 0xf88
+  __DATA_DIRTY.__bss: 0xf78
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4514
-  Symbols:   8647
-  CStrings:  14555
+  Functions: 4527
+  Symbols:   8667
+  CStrings:  14583
 
Symbols:
+ +[PLDefaults(Submission) addActiveTaskingRequest:]
+ +[PLDefaults(Submission) removeActiveTaskingRequest:]
+ +[PLDefaults(Submission) removeAllActiveTaskingRequests]
+ +[PLDefaults(Submission) setLastUploadDate:ForSubmitReason:]
+ -[PLSubmissionConfig getSubmitReasonTypeToDefaultsKey]
+ -[PLSubmissionFilePLL declaredRetentionIsExactly24HoursForLegacyEntryKeyConfig:]
+ -[PLSubmissionFilePLL declaredRetentionIsExactly24HoursForTimeToLiveInDays:]
+ -[PLSubmissionFilePLL tableHas24HourRetention:]
+ -[PLSubmissionFilePLL trialsTaskingTrimFiltersForTables:beforeDate:]
+ -[PLSubmissions shouldNotifyTaskingReceivedAndCompletedForConfig:]
+ GCC_except_table78
+ __OBJC_$_CLASS_METHODS_PLDefaults(Submission)
+ _objc_msgSend$addActiveTaskingRequest:
+ _objc_msgSend$declaredRetentionIsExactly24HoursForLegacyEntryKeyConfig:
+ _objc_msgSend$declaredRetentionIsExactly24HoursForTimeToLiveInDays:
+ _objc_msgSend$getSubmitReasonTypeToDefaultsKey
+ _objc_msgSend$removeActiveTaskingRequest:
+ _objc_msgSend$removeAllActiveTaskingRequests
+ _objc_msgSend$setLastUploadDate:ForSubmitReason:
+ _objc_msgSend$shouldNotifyTaskingReceivedAndCompletedForConfig:
+ _objc_msgSend$tableHas24HourRetention:
+ _objc_msgSend$trialsTaskingTrimFiltersForTables:beforeDate:
- GCC_except_table77
- __OBJC_$_CLASS_METHODS_PLDefaults
CStrings:
+ "Abandoning '%@' task after %lu stalled retries with no progress..."
+ "CollectionSummary"
+ "DistinctCategoryCount"
+ "Indexing"
+ "InternalOTA"
+ "InternalSafeguardOTA"
+ "Notify of powerlog tasking request received: %@"
+ "PLDefaults: Attempted to add duplicate tasking request: %@"
+ "PLLastUploadDate"
+ "PLTaskingRequests"
+ "PPSSignpostControllerStalledRetryCount"
+ "Powerlog tasking completed: %@"
+ "Powerlog tasking request received: %@"
+ "Powerlog tasking submit reason: (%d) %@"
+ "RunDuration"
+ "Send notification of tasking completed (%@)"
+ "SignpostServiceMetrics"
+ "SiriTools"
+ "TaskedOTA"
+ "TaskedUpgradeOTA"
+ "TotalSignpostCount"
+ "Trimming %lu trials tasking tables to 24h window (cutoff=%@)"
+ "Updated last upload date for %@"
+ "com.apple.powerlog.tasking_completed"
+ "com.apple.powerlog.tasking_received"
+ "entityCount"
+ "enumCount"
+ "intentCount"
+ "timestamp is NULL OR timestamp < (SELECT max(timestamp) FROM '%@' WHERE timestamp < %f)"
+ "totalItemCount"
- "timestamp is NULL OR timestamp < %f"
- "timestamp is NULL OR timestamp < (SELECT max(timestamp) FROM 'PLConfigAgent_EventNone_Config' WHERE timestamp < %f)"
```
