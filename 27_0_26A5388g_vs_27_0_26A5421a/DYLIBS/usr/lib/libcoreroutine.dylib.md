## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1119.0.0.0.0
-  __TEXT.__text: 0x68de2c
+1122.0.0.0.0
+  __TEXT.__text: 0x68e6b0
   __TEXT.__objc_methlist: 0x32010
   __TEXT.__const: 0x45e8
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__swift5_typeref: 0x18a
-  __TEXT.__oslogstring: 0x7e298
-  __TEXT.__cstring: 0x459e0
+  __TEXT.__oslogstring: 0x7e1ad
+  __TEXT.__cstring: 0x45a29
   __TEXT.__swift5_capture: 0x7c
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x20

   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x27d7c
+  __TEXT.__gcc_except_tab: 0x27de0
   __TEXT.__ustring: 0x3e
-  __TEXT.__unwind_info: 0xde48
+  __TEXT.__unwind_info: 0xde40
   __TEXT.__eh_frame: 0x3a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0x19688
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x11d0
-  __DATA_CONST.__objc_arraydata: 0x2d28
-  __DATA_CONST.__got: 0x2f38
-  __AUTH_CONST.__const: 0xf510
-  __AUTH_CONST.__cfstring: 0x28680
+  __DATA_CONST.__objc_arraydata: 0x2ca8
+  __DATA_CONST.__got: 0x2f40
+  __AUTH_CONST.__const: 0xf540
+  __AUTH_CONST.__cfstring: 0x286c0
   __AUTH_CONST.__objc_const: 0x53ae8
-  __AUTH_CONST.__objc_intobj: 0x4818
+  __AUTH_CONST.__objc_intobj: 0x4860
   __AUTH_CONST.__objc_arrayobj: 0xeb8
   __AUTH_CONST.__objc_doubleobj: 0xbe0
-  __AUTH_CONST.__objc_dictobj: 0x320
+  __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0xde0
   __AUTH.__objc_data: 0x25e8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 20820
-  Symbols:   43206
-  CStrings:  15139
+  Functions: 20822
+  Symbols:   43210
+  CStrings:  15137
 
Symbols:
+ -[RTBGSystemTaskScheduler _reportTaskFinishedWithIdentifier:stimulationDate:error:didDefer:systemRequestedDeferral:]
+ -[RTFloorTransitionExtractor _largeTransitionExistsInGapFrom:to:transitions:]
+ -[RTFloorTransitionExtractor findLabeledDataForTime:labeledData:lookingForEnd:transitions:]
+ _RPOptionStatusFlags
+ __81-[RTXPCActivityManager registerTaskWithIdentifier:criteria:handler:deferHandler:]_block_invoke
+ ___61-[RTXPCActivityManager unregisterTaskWithIdentifier:handler:]_block_invoke
+ ___block_descriptor_80_e8_32s40s48s56bs64bs_e5_v8?0l
+ _objc_msgSend$_largeTransitionExistsInGapFrom:to:transitions:
+ _objc_msgSend$_reportTaskFinishedWithIdentifier:stimulationDate:error:didDefer:systemRequestedDeferral:
+ _objc_msgSend$findLabeledDataForTime:labeledData:lookingForEnd:transitions:
- -[RTBGSystemTaskScheduler _reportTaskFinishedWithIdentifier:stimulationDate:error:isDeferred:]
- -[RTFloorTransitionExtractor findLabeledDataForTime:labeledData:lookingForEnd:]
- -[RTVisitFloorMap assignFloorLabelsToSimplifiedData:groupedAltitudeData:clusteringResult:]
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
+ "03:38:11"
+ "Aug 10 2026"
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
- "02:05:56"
- "@min.doubleValue"
- "Jul 11 2026"
```
