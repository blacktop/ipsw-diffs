## CoreMotion

> `/System/Library/Frameworks/CoreMotion.framework/CoreMotion`

```diff

-2890.12.17.0.4
-  __TEXT.__text: 0x40aaf0
+2890.16.16.0.0
+  __TEXT.__text: 0x40e67c
   __TEXT.__auth_stubs: 0x2990
-  __TEXT.__objc_methlist: 0xaa84
-  __TEXT.__const: 0x9a10
+  __TEXT.__objc_methlist: 0xab8c
+  __TEXT.__const: 0x9b00
   __TEXT.__swift5_typeref: 0x247
   __TEXT.__swift5_reflstr: 0x26
   __TEXT.__swift5_assocty: 0x70
   __TEXT.__constg_swiftt: 0xb8
   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__cstring: 0x3c66d
+  __TEXT.__cstring: 0x3c91c
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x10
-  __TEXT.__gcc_except_tab: 0xb0bc
-  __TEXT.__oslogstring: 0x2362f
-  __TEXT.__unwind_info: 0xdb58
+  __TEXT.__gcc_except_tab: 0xb0d8
+  __TEXT.__oslogstring: 0x2382a
+  __TEXT.__unwind_info: 0xda90
   __TEXT.__eh_frame: 0x724
   __TEXT.__objc_classname: 0x17cd
-  __TEXT.__objc_methname: 0x17831
-  __TEXT.__objc_methtype: 0x7e9a
-  __TEXT.__objc_stubs: 0xc460
+  __TEXT.__objc_methname: 0x178d9
+  __TEXT.__objc_methtype: 0x7ec6
+  __TEXT.__objc_stubs: 0xc520
   __DATA_CONST.__got: 0x238
   __DATA_CONST.__const: 0x3460
   __DATA_CONST.__objc_classlist: 0x790
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1d6d8
-  __DATA_CONST.__objc_selrefs: 0x4778
+  __DATA_CONST.__objc_const: 0x1d750
+  __DATA_CONST.__objc_selrefs: 0x47a8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_classrefs: 0x730
   __DATA_CONST.__objc_superrefs: 0x6b0
   __DATA_CONST.__objc_arraydata: 0x220
-  __AUTH_CONST.__const: 0x12a98
-  __AUTH_CONST.__cfstring: 0x10c80
-  __AUTH_CONST.__objc_const: 0x6f60
+  __AUTH_CONST.__const: 0x12b40
+  __AUTH_CONST.__cfstring: 0x10ce0
+  __AUTH_CONST.__objc_const: 0x6fa8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__objc_intobj: 0x270

   __AUTH.__objc_data: 0x820
   __AUTH.__data: 0x210
   __DATA.__got_weak: 0x8
-  __DATA.__objc_ivar: 0x13fc
-  __DATA.__data: 0x1420
+  __DATA.__objc_ivar: 0x140c
+  __DATA.__data: 0x1430
   __DATA.__common: 0xc0
   __DATA.__bss: 0x458
   __DATA_DIRTY.__objc_ivar: 0x12c

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 1E51658A-881B-3BBB-95C2-6C7C9701E878
-  Functions: 16934
+  UUID: E4A6F107-B302-327C-A121-C9BEBACCA8F4
+  Functions: 16995
   Symbols:   1553
-  CStrings:  16184
+  CStrings:  16222
 
CStrings:
+ "%@, <recordId, %lu, startDate, %@, grade, %f>"
+ "%@, <recordId, %lu, startDate, %@, workoutType, %ld, sessionId, %@, estimatedVo2Max, %f, durationInSeconds, %f, hrMax, %f, hrMin, %f, variance, %f, filteredVo2Max, %f, sessionType, %ld, eligibleForHealthKit, %d, eligibleForCalorimetry, %d, numWorkoutsContrToEstimate, %lu, estimatedHRResponseParam, %f, estimatedHRRecoveryParam, %f, sessionVo2Max, %f>"
+ "%@, <version, %lu>"
+ "+[CMAltimeterInternal _bundleBeforeTCCCheck:]"
+ "-[CMAltimeter startRelativeAltitudeUpdatesToQueue:withHandler:]"
+ "-[CMAltimeter stopRelativeAltitudeUpdates]"
+ "-[CMHistoricalDataStore cacheAllCardioRecordIds]"
+ "-[CMHistoricalDataStore cacheAllMobilityRecordIds]"
+ "-[CMHistoricalDataStore getFirstRecordIdFrom:until:forTable:]"
+ "-[CMHistoricalDataStore getLastRecordIdFrom:until:forTable:]"
+ "-[CMHistoricalDataStore nextCardioFetchWithCount:withHandler:]"
+ "-[CMHistoricalDataStore nextMobilityFetchWithCount:withHandler:]"
+ "20:24:48"
+ "@144@0:8Q16@24q32@40d48d56d64d72d80d88q96B104B108Q112d120d128d136"
+ "@36@0:8Q16@24f32"
+ "@40@0:8{CLElevationGradeEntry=Qdd}16"
+ "App does not have NSMotionUsageDescription, do not vend relative altimeter"
+ "DTPlatformVersion"
+ "May  1 2024"
+ "NSMotionUsageDescription"
+ "Q40@0:8d16d24r*32"
+ "SELECT id FROM %s WHERE startTime >= %f AND startTime <= %f ORDER BY id ASC LIMIT 1"
+ "SELECT id FROM %s WHERE startTime >= %f AND startTime <= %f ORDER BY id DESC LIMIT 1"
+ "Td,N,V_endTime"
+ "Td,N,V_startTime"
+ "[HistoricalFetch] %s: Invalid rowId"
+ "[HistoricalFetch] %s: No records found"
+ "[HistoricalFetch] Cached all last cardio record ids from %f to %f"
+ "[HistoricalFetch] Cached all last mobility record ids from %f to %f"
+ "[HistoricalFetch] Caching first record id %lu for table %{private}s"
+ "[HistoricalFetch] Caching last record id %lu for table %{private}s"
+ "[HistoricalFetch] Error: invalid token timestamps, start:%{public}f end:%{public}f"
+ "[HistoricalFetch] Fetching cardio samples from: %f to: %f"
+ "[HistoricalFetch] Fetching mobility samples from: %f to: %f"
+ "_bundleBeforeTCCCheck"
+ "_bundleBeforeTCCCheck:"
+ "app sdk version, %s"
+ "avgRelOmegaRps"
+ "cacheAllCardioRecordIds"
+ "cacheAllMobilityRecordIds"
+ "componentsSeparatedByString:"
+ "fSessionVo2Max"
+ "firstRingSensorTimeStampMicroSeconds"
+ "getFirstRecordIdFrom:until:forTable:"
+ "getLastRecordIdFrom:until:forTable:"
+ "infoDictionary"
+ "initWithRecordId:startDate:grade:"
+ "initWithRecordId:startDate:workoutType:sessionId:estimatedVo2Max:durationInSeconds:hrMax:hrMin:variance:filteredVo2Max:sessionType:eligibleForHealthKit:eligibleForCalorimetry:numWorkoutsContrToEstimate:estimatedHRResponseParam:estimatedHRRecoveryParam:sessionVo2Max:"
+ "kCMCardioFitnessResultsCodingKeySessionVo2Max"
+ "medianBufferNumSamples"
+ "medianNorthAlignmentEstimateRad"
+ "newNorthAlignmentEstimateRad"
+ "nextCardioFetchWithCount:withHandler:"
+ "nextMobilityFetchWithCount:withHandler:"
+ "numRingSensorSamples"
+ "pencilFusionDMYawAlignmentUpdate"
+ "pencilFusionRingSensorTrustModelUpdate"
+ "ringSensorTrustModelMode"
+ "sessionVo2Max"
+ "timeElapsedSinceLastUpdateMicroSeconds"
+ "trustPencilRingSensorBool"
- "%@, <recordId, %lu, startDate, %@, grade, %f, gradeSource, %ld>"
- "%@, <recordId, %lu, startDate, %@, workoutType, %ld, sessionId, %@, estimatedVo2Max, %f, durationInSeconds, %f, hrMax, %f, hrMin, %f, variance, %f, filteredVo2Max, %f, sessionType, %ld, eligibleForHealthKit, %d, eligibleForCalorimetry, %d, numWorkoutsContrToEstimate, %lu, estimatedHRResponseParam, %f, estimatedHRRecoveryParam, %f>"
- "%@, <version, %lu, tables, %@>"
- "-[CMHistoricalDataStore getFirstRecordIdForTable:]"
- "-[CMHistoricalDataStore getLastRecordIdForTable:]"
- "-[CMHistoricalDataStore nextCardioFetchWithCount:AndResultHandler:]"
- "-[CMHistoricalDataStore nextMobilityFetchWithCount:AndResultHandler:]"
- "20:26:49"
- "@136@0:8Q16@24q32@40d48d56d64d72d80d88q96B104B108Q112d120d128"
- "@48@0:8Q16@24d32q40"
- "Mar 13 2024"
- "Q24@0:8r*16"
- "SELECT id FROM %s ORDER BY id DESC LIMIT 1"
- "SELECT id FROM %s WHERE startTime >= %f ORDER BY id ASC LIMIT 1"
- "[HistoricalFetch] Caching first record id %d for table %{private}s"
- "[HistoricalFetch] Caching last record id %d for table %{private}s"
- "fGradeSource"
- "getFirstRecordIdForTable:"
- "getLastRecordIdForTable:"
- "gradeSource"
- "initWithRecordId:startDate:grade:gradeSource:"
- "initWithRecordId:startDate:workoutType:sessionId:estimatedVo2Max:durationInSeconds:hrMax:hrMin:variance:filteredVo2Max:sessionType:eligibleForHealthKit:eligibleForCalorimetry:numWorkoutsContrToEstimate:estimatedHRResponseParam:estimatedHRRecoveryParam:"
- "internalDescription"
- "kCMPedestrianGradeCodingKeyGradeSource"
- "nextCardioFetchWithCount:AndResultHandler:"
- "nextMobilityFetchWithCount:AndResultHandler:"

```
