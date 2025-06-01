## PromotedContentPrediction

> `/System/Library/PrivateFrameworks/PromotedContentPrediction.framework/PromotedContentPrediction`

```diff

-94.0.0.0.0
-  __TEXT.__text: 0x2c540
+95.0.0.0.0
+  __TEXT.__text: 0x2bf64
   __TEXT.__auth_stubs: 0xa10
-  __TEXT.__objc_methlist: 0x28a4
-  __TEXT.__const: 0x488
-  __TEXT.__cstring: 0x16fe
-  __TEXT.__oslogstring: 0x2fcf
-  __TEXT.__gcc_except_tab: 0x1130
+  __TEXT.__objc_methlist: 0x28bc
+  __TEXT.__const: 0x480
+  __TEXT.__cstring: 0x170e
+  __TEXT.__oslogstring: 0x2f38
+  __TEXT.__gcc_except_tab: 0x111c
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0xa04
+  __TEXT.__unwind_info: 0x9f0
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x630
-  __TEXT.__objc_methname: 0x70b4
-  __TEXT.__objc_methtype: 0xd6a
-  __TEXT.__objc_stubs: 0x5aa0
+  __TEXT.__objc_classname: 0x63b
+  __TEXT.__objc_methname: 0x6f12
+  __TEXT.__objc_methtype: 0xd55
+  __TEXT.__objc_stubs: 0x5960
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0xb40
-  __DATA_CONST.__objc_classlist: 0x1f0
+  __DATA_CONST.__const: 0xb00
+  __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3ec0
-  __DATA_CONST.__objc_selrefs: 0x1be0
+  __DATA_CONST.__objc_const: 0x3ee8
+  __DATA_CONST.__objc_selrefs: 0x1b80
+  __DATA_CONST.__objc_classrefs: 0x320
+  __DATA_CONST.__objc_superrefs: 0x148
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__cfstring: 0x25e0
-  __AUTH_CONST.__objc_const: 0x17d0
+  __AUTH_CONST.__cfstring: 0x2660
+  __AUTH_CONST.__objc_const: 0x1818
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x520
   __AUTH.__objc_data: 0x640
-  __DATA.__objc_classrefs: 0x348
-  __DATA.__objc_superrefs: 0x140
-  __DATA.__objc_ivar: 0x330
+  __DATA.__objc_ivar: 0x32c
   __DATA.__data: 0x240
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0xd20
+  __DATA_DIRTY.__objc_data: 0xd70
   __DATA_DIRTY.__bss: 0x128
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/PrivateFrameworks/BiomeStorage.framework/BiomeStorage
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
-  - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation
   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7AEDFF98-914B-3CDA-B783-681BB76C3172
-  Functions: 888
-  Symbols:   701
-  CStrings:  2467
+  UUID: D2978EFD-11D7-3239-BA8B-73A1BFE41559
+  Functions: 885
+  Symbols:   698
+  CStrings:  2457
 
Symbols:
+ _OBJC_CLASS_$_APOdmlBiomeSQLQuery
+ _OBJC_CLASS_$_BMSQLDatabase
+ _OBJC_METACLASS_$_APOdmlBiomeSQLQuery
+ _kAPOdmlAppInstallBiomeEventKey
+ _kAPOdmlAppUsageBiomeEventKey
- _OBJC_CLASS_$_BMStreams
- _OBJC_CLASS_$_NSCompoundPredicate
- _OBJC_CLASS_$__DKEvent
- _OBJC_CLASS_$__DKEventQuery
- _OBJC_CLASS_$__DKKnowledgeStore
- _OBJC_CLASS_$__DKQuery
- _OBJC_CLASS_$__DKSystemEventStreams
- _kAPOdmlCoreDuetFailure
CStrings:
+ "\x12\x131"
+ "\"%@\""
+ "@\"BMSQLDatabase\""
+ "APOdmlBiomeSQLQuery"
+ "App.InFocus"
+ "App.Install"
+ "Biome SQL query error: %@"
+ "SELECT * FROM %@"
+ "SELECT * FROM %@ WHERE eventTimestamp > %f AND eventTimestamp < %f"
+ "T@\"BMSQLDatabase\",&,N,V_database"
+ "T@\"NSString\",?,R,C"
+ "_database"
+ "absoluteTimestamp"
+ "database"
+ "duration"
+ "eventsBetween:and:"
+ "formatEventName:"
+ "getRowsFromResults:"
+ "next"
+ "query:startDate:endDate:"
+ "row"
+ "setDatabase:"
- "\x12\x133"
- "%@(adamid=%@, mins_ago=%f, duration=%f)"
- "%@(adamid=%llu)"
- "@\"_DKKnowledgeStore\""
- "@40@0:8@16@24Q32"
- "CoreDuet"
- "T@\"NSMutableArray\",&,N,V_consumedEvents"
- "T@\"_DKKnowledgeStore\",&,N,V_knowledgeStore"
- "[%@]: Querying CoreDuet for usage events between %@ and %@"
- "[%{private}@]: Failed to get events. Error : %{private}@"
- "[%{private}@]: Fetched %{private}lu results."
- "_DKAppInstallMetadataKey-isInstall"
- "_consumedEvents"
- "_knowledgeStore"
- "andPredicateWithSubpredicates:"
- "appInstallStream"
- "appUsageStream"
- "collect"
- "consumedEvents"
- "coreDuetStream"
- "descriptionForEvent:"
- "eventsBetween:and:withLimit:"
- "filteredArrayUsingPredicate:"
- "knowledgeStore"
- "predicateForEventsWithStartAndEndInDateRangeFrom:to:"
- "predicateForObjectsWithMetadataKey:andIntegerValue:"
- "publisherForQuery:"
- "setConsumedEvents:"
- "setEventStreams:"
- "setKnowledgeStore:"
- "setLimit:"
- "sinkWithCompletion:receiveInput:"
- "startDateSortDescriptorAscending:"
- "test_events: %@"
- "timeIntervalSinceNow"
- "v16@?0@\"NSArray\"8"
- "value.stringValue == %@"

```
