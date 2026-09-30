## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1119.0.0.0.0
-  __TEXT.__text: 0x6bd79c
+1122.0.0.0.0
+  __TEXT.__text: 0x6be004
   __TEXT.__objc_methlist: 0x34e30
   __TEXT.__const: 0x4bd8
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__swift5_typeref: 0x41b
-  __TEXT.__oslogstring: 0x89e8d
-  __TEXT.__cstring: 0x4ae89
+  __TEXT.__oslogstring: 0x89da2
+  __TEXT.__cstring: 0x4aed2
   __TEXT.__swift5_capture: 0xdc
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x38

   __TEXT.__swift5_reflstr: 0x14
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_types: 0x8
-  __TEXT.__gcc_except_tab: 0x2ef98
+  __TEXT.__gcc_except_tab: 0x2effc
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0xf268
+  __TEXT.__unwind_info: 0xf260
   __TEXT.__eh_frame: 0x6d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x10658
+  __DATA_CONST.__const: 0x10680
   __DATA_CONST.__objc_classlist: 0x1688
   __DATA_CONST.__objc_catlist: 0x3f0
   __DATA_CONST.__objc_protolist: 0x370

   __DATA_CONST.__objc_selrefs: 0x1b4a8
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x1280
-  __DATA_CONST.__objc_arraydata: 0x2e58
-  __DATA_CONST.__got: 0x3510
+  __DATA_CONST.__objc_arraydata: 0x2dd8
+  __DATA_CONST.__got: 0x3518
   __AUTH_CONST.__const: 0x3738
-  __AUTH_CONST.__cfstring: 0x2c300
+  __AUTH_CONST.__cfstring: 0x2c340
   __AUTH_CONST.__objc_const: 0x56920
-  __AUTH_CONST.__objc_intobj: 0x4bc0
+  __AUTH_CONST.__objc_intobj: 0x4c08
   __AUTH_CONST.__objc_arrayobj: 0xfc0
   __AUTH_CONST.__objc_doubleobj: 0xbe0
-  __AUTH_CONST.__objc_dictobj: 0x348
+  __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x12f0
   __AUTH.__objc_data: 0x1b20

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 22020
-  Symbols:   45813
-  CStrings:  16421
+  Functions: 22022
+  Symbols:   45816
+  CStrings:  16419
 
Symbols:
+ -[RTBGSystemTaskScheduler _reportTaskFinishedWithIdentifier:stimulationDate:error:didDefer:systemRequestedDeferral:]
+ -[RTFloorTransitionExtractor _largeTransitionExistsInGapFrom:to:transitions:]
+ -[RTFloorTransitionExtractor findLabeledDataForTime:labeledData:lookingForEnd:transitions:]
+ _RPOptionStatusFlags
+ ___61-[RTXPCActivityManager unregisterTaskWithIdentifier:handler:]_block_invoke
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80s88r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r88l8s72l8s80l8
+ ___block_descriptor_80_e8_32s40s48s56bs64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80r_e20_v20?0"NSError"8B16ls32l8s40l8s48l8s56l8r80l8s64l8s72l8
+ _objc_msgSend$_largeTransitionExistsInGapFrom:to:transitions:
+ _objc_msgSend$_reportTaskFinishedWithIdentifier:stimulationDate:error:didDefer:systemRequestedDeferral:
+ _objc_msgSend$findLabeledDataForTime:labeledData:lookingForEnd:transitions:
- -[RTBGSystemTaskScheduler _reportTaskFinishedWithIdentifier:stimulationDate:error:isDeferred:]
- -[RTFloorTransitionExtractor findLabeledDataForTime:labeledData:lookingForEnd:]
- -[RTVisitFloorMap assignFloorLabelsToSimplifiedData:groupedAltitudeData:clusteringResult:]
- ___block_descriptor_105_e8_32s40s48s56s64s72s80s88r_e5_v8?0ls32l8s40l8r88l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80r_e20_v20?0"NSError"8B16ls32l8s40l8r80l8s48l8s56l8s64l8s72l8
- _objc_msgSend$_reportTaskFinishedWithIdentifier:stimulationDate:error:isDeferred:
- _objc_msgSend$assignFloorLabelsToSimplifiedData:groupedAltitudeData:clusteringResult:
- _objc_msgSend$findLabeledDataForTime:labeledData:lookingForEnd:
CStrings:
+ "#altimeter,%{public}@,floor_count_histogram,k,%lu,visits,%lu,fraction,%.3f,loiUUID,%{private}@"
+ "#altimeter,%{public}@,selected_cluster_count,%lu,visits_with_count,%lu,fraction,%.3f,loiUUID,%{private}@"
+ "#altimeter,built labeled grouped data,validCount,%lu,totalGrouped,%lu,visitUUID,%{private}@"
+ "#altimeter,findLabeledDataForTime,dropping feature,backwardCandidateIdx,%lu,reason,largeTransitionInGap,visitUUID,%{private}@"
+ "#altimeter,findLabeledDataForTime,dropping feature,forwardCandidateIdx,%lu,reason,largeTransitionInGap,visitUUID,%{private}@"
+ "#altimeter,initial k-mean clustering group number guess for LOI learning,clusterCount,%d,qualifyingVisitsCount,%lu,totalVisits,%lu"
+ "#altimeter,initial loi floor map guess,floorIdx,%d,initialCenter,%.3f,qualifyingVisitCount,%lu"
+ "#altimeter,invalid clustering result for labeled data construction,assignmentsCount,%lu,groupedCount,%lu,floorCount,%lu,visitUUID,%{private}@"
+ "%@, %@, scheduler, %@, run finished, identifier, %@, group, %@, error, %@, latency, %.2f, system requested deferral, %d, did defer, %d"
+ "%@, ignoring provider error and labeling visit with remaining placeInferences, error, %@"
+ "%@.%@.BGSTRegisterLaunchHandler.%@"
+ "%@.%@.BGSTSubmitTaskRequest.%@"
+ "ignoring provider error and labeling visit with remaining placeInferences, error, %@"
+ "systemRequestedDeferral"
- "#altimeter,added grouped segment,floorIndex,%d,startTime,%.3f,endTime,%.3f,altitude,%.3f,visitUUID,%{private}@"
- "#altimeter,added simplified point,floorIndex,%d,pointAltitude,%.3f,floorAltitude,%.3f,distance,%.3f,visitUUID,%{private}@"
- "#altimeter,assignFloorLabelsToSimplifiedData,empty grouped data,visitUUID,%{private}@"
- "#altimeter,assignFloorLabelsToSimplifiedData,empty simplified data,visitUUID,%{private}@"
- "#altimeter,assignFloorLabelsToSimplifiedData,invalid clustering result data,visitUUID,%{private}@"
- "#altimeter,assignFloorLabelsToSimplifiedData,no clustering result,visitUUID,%{private}@"
- "#altimeter,completed floor label assignment,totalAssignedPoints,%lu,groupedSegmentsUsed,%lu,additionalSimplifiedPoints,%lu,visitUUID,%{private}@"
- "#altimeter,excluded simplified point without floor assignment,pointAltitude,%.3f,timestamp,%.3f,visitUUID,%{private}@"
- "#altimeter,no labeled Simplified Data found, skipped floor transition extraction,visitUUID,%{private}@"
- "#altimeter,skipping simplified point that overlaps with already used grouped segment,pointTime,%.3f,visitUUID,%{private}@"
- "#altimeter,starting floor label assignment,simplifiedDataCount,%lu,groupedDataCount,%lu,floorCount,%lu,visitUUID,%{private}@"
- "%@, %@, scheduler, %@, run finished, identifier, %@, group, %@, error, %@, latency, %.2f, is deferred, %d"
- "%@, %@, task deferred by client, identifier: %@"
- "%@, %@, task expired by system, identifier: %@"
- "%@, %@, task failed, identifier: %@, error: %@"
- "@min.doubleValue"
```
