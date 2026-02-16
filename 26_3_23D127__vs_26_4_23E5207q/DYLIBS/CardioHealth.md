## CardioHealth

> `/System/Library/PrivateFrameworks/CardioHealth.framework/CardioHealth`

```diff

-3068.0.15.0.0
-  __TEXT.__text: 0xb334
-  __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__const: 0x4d8
-  __TEXT.__gcc_except_tab: 0x40c
-  __TEXT.__cstring: 0x1d1
-  __TEXT.__oslogstring: 0x14fd
-  __TEXT.__unwind_info: 0x260
+3072.0.40.0.1
+  __TEXT.__text: 0xd560
+  __TEXT.__auth_stubs: 0x1e0
+  __TEXT.__const: 0x530
+  __TEXT.__gcc_except_tab: 0x4c0
+  __TEXT.__cstring: 0x20f
+  __TEXT.__oslogstring: 0x2539
+  __TEXT.__unwind_info: 0x270
   __TEXT.__objc_methname: 0x66
   __TEXT.__objc_stubs: 0xa0
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x28
-  __AUTH_CONST.__auth_got: 0xf8
-  __AUTH_CONST.__const: 0x190
+  __AUTH_CONST.__auth_got: 0x100
+  __AUTH_CONST.__const: 0x130
   __AUTH_CONST.__cfstring: 0x40
-  __DATA_DIRTY.__data: 0x20
+  __DATA_DIRTY.__data: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D0B05FA6-1258-3E3C-B039-38E924C39A2F
-  Functions: 87
-  Symbols:   86
-  CStrings:  64
+  UUID: 2A61F8B5-C255-3372-A6C6-76FCA10D9E1B
+  Functions: 91
+  Symbols:   88
+  CStrings:  103
 
Symbols:
+ __ZN17CHVO2MaxEstimator19feedHrAndMetsUpdateEdddd
+ __ZN17CHVO2MaxEstimatorC1ENSt3__110shared_ptrI21CHVO2MaxInputDelegateEENS1_I22CHVO2MaxOutputDelegateEENS1_I30CHVO2MaxDataCollectionDelegateEENS_13ConfigurationE
+ __ZN17CHVO2MaxEstimatorC2ENSt3__110shared_ptrI21CHVO2MaxInputDelegateEENS1_I22CHVO2MaxOutputDelegateEENS1_I30CHVO2MaxDataCollectionDelegateEENS_13ConfigurationE
+ __ZNSt3__16__sortIRNS_6__lessIffEEPfEEvT0_S5_T_
- __ZN17CHVO2MaxEstimatorC1ENSt3__110shared_ptrI21CHVO2MaxInputDelegateEENS1_I22CHVO2MaxOutputDelegateEENS1_I30CHVO2MaxDataCollectionDelegateEENS_11CacheInputsEjbi
- __ZN17CHVO2MaxEstimatorC2ENSt3__110shared_ptrI21CHVO2MaxInputDelegateEENS1_I22CHVO2MaxOutputDelegateEENS1_I30CHVO2MaxDataCollectionDelegateEENS_11CacheInputsEjbi
CStrings:
+ " No fInputDelegate available for getPhoneBasedPriorDailyInputs"
+ "/Library/Caches/com.apple.xbs/B4C4B144-D2FF-48B2-9D70-FF39E21B4E6F/TemporaryDirectory.GWZWeF/Sources/CoreLocation/Framework/CardioHealth/Models/CHVO2MaxAdaptiveOutdoorPedestrianModel.mm"
+ "Attempting Retrocompute for phone/ipad estimate which is not supported, workoutEndTime:%{public}f"
+ "Calling adaptiveModel.estimateVO2Max with prior: %{private}.2f, clusteringInputs: %{public}zu, historicalSummary: %{public}zu"
+ "Completed insert of HR and Mets input record; duration: %{public}f"
+ "DB write rejected,reason,duplicateSession"
+ "DB write rejected,reason,extendedMode"
+ "DB write rejected,reason,insufficientDuration,duration,%{public}.1f,threshold,%{public}.1f,escalated,%{public}s"
+ "DB write rejected,reason,missingSessionEstimateForEscalation"
+ "DB write rejected,reason,stageBasedClustering"
+ "Data Pipeline: clusteringInputs,%{public}zu,historicalSummary,%{public}zu,prior,%{private}.2f,failingKinetics,%{public}d"
+ "DynamicsBypassed: vo2,%.2f,hr,%.2f,clusteringMode,%d"
+ "MetsCollected,mets,%{private}f,source,%d,metComputeTime,%f,hr,%{private}f,hrConfidence,%{public}f,hrTime,%{public}f"
+ "Output delegate not available"
+ "Overwriting meanMaxMets,calculated,%{private}f,overwrite,%{private}f"
+ "Phone-based prior result: %{private}.2f"
+ "Skipping dynamic filters: clusteringMode,%{public}d"
+ "Skipping historical cluster fetch - using session-only estimation: clusteringMode,%{public}d"
+ "Using phone-based prior calculation"
+ "Using phone-based prior: prior,%{private}.2f,clusteringMode,%{public}d"
+ "Using watch-based prior calculation with %{public}zu historical summaries, meanMaxMets: %{private}.2f"
+ "Using watch-based prior: prior,%.2f,clusteringMode,%d"
+ "VO2Max FAILURE: No clustering inputs after dynamics filtering - estimation will fail"
+ "VO2Max InsufficientSamplesForClustering, Only %{public}zu samples provided, need %{public}zu minimum - clusteringMode=%{public}d"
+ "VO2Max K-means deriveClusters failed: inputSize=%{public}zu, expected=%{public}u clusters"
+ "VO2Max K-means produced insufficient clusters: produced=%{public}zu, required=%{public}u, inputs=%{public}zu"
+ "VO2Max body metrics missing: isAgeSet=%{public}d, isHeightSet=%{public}d, isWeightSet=%{public}d, isBiologicalSexSet=%{public}d"
+ "VO2Max deriveStageBasedClusters failed: inputSize=%zu, highConfidenceInputs=%zu"
+ "VO2Max eligibility: shouldWriteToDB=%{public}d, historicalCount=%{public}zu, minRequired=%{public}d, isWatch=%{public}d, hasAge=%{public}d, eligibleForCalorimetry=%{public}d, eligibleForHealthKit=%{public}d"
+ "VO2Max estimation blocked by precondition: status=%{public}d, clusteringMode=%{public}d"
+ "VO2Max estimation failed for supported workout: workoutType=%{public}d, sessionStatus=%{public}d, longitudinalStatus=%{public}d, extendedMode=%{public}d, sessionType=%{public}d, duration=%{public}.1fs, hrAvailability=%{public}.1f%%, gpsAvailability=%{public}.1f%%, validHRMetsPairs=%{public}d, hrOutOfBounds=%{public}.1f%%, kinematicsFailureRate=%{public}.1f%%, historicalClusters=%{public}zu, strollerPct=%{public}.1f%%, medianVO2=%{private}.2f, median1FHR=%{private}.3f"
+ "VO2Max estimation not supported for workout type %{public}d, isEscalated: %{public}d"
+ "VO2Max estimation not supported for workout type %{public}d: Extended workout mode"
+ "VO2Max failed to calculate a prior due to invalid mean max METs: meanMaxMets=%{private}.2f, priorVO2Max=%{private}.2f, efficiency=%{private}.2f, currentClusters=%{public}zu, historicalClusters=%{public}zu, filteredClusters=%{public}zu"
+ "VO2Max filterClusters ENTRY: mode=%d, historical=%zu summaries"
+ "VO2Max filterClusters: using %.0f day lookback window"
+ "VO2Max insufficient clusters from session: clusters=%{public}zu, required=%{public}zu, clusteringMode=%{public}d, sessionStatus=%{public}d"
+ "VO2Max no input delegate available for getMeanMaxMetsInTimeRange"
+ "VO2Max,AdaptiveOutdoorPedestrianModel,Longitudinal Estimate,numClusters,%{public}lu,numClustersContr,%{public}u,numWorkoutsContr,%{public}u,medianResidual,%f,hrMin,%f,hrMax,%f,meanResidual,%f,clusterResidualBoundsMax,%{public}f"
+ "VO2Max,AdaptiveOutdoorPedestrianModel,Longitudinal Estimate,ts,%{public}.9f,size,%{public}lld,hrMin,%f,hrMax,%f,hrMean,%f,vo2Mean,%f,hrConfidenceMean,%{public}f,gradeMean,%{public}f,oneMinusFHR,%f,residual,%f,failHistResidCheck,%{public}d,confidence,%{public}f,sessionType,%{public}d,isLongitudinal,%{public}d"
+ "VO2Max,Estimate not written to database,status,%{public}d,workout duration,%{public}.3f,estimate,%f,workout mode,%{public}ld"
+ "VO2Max,HR Bounds,observedRestingHR,%{private}f,fhrHRMin,%{private}f,fhrHRMax,%{private}f"
+ "VO2Max,K-means clustering failed,inputs,%{public}zu,targetClusters,%{public}u,hrNorm,%{public}f,speedNorm,%{public}f,gradeNorm,%{public}f"
+ "VO2Max,vo2MaxEstimationStatus,%{public}d,priorVO2Max,%{private}f,longitudinalVO2Max,%{private}f,sessionVO2Max,%{private}f,clusteringMode,%{public}d"
+ "Watch-based prior result: %{private}.2f, efficiency: %{private}.3f"
+ "Will not retrocompute VO2Max due to absense of VO2MaxInputs, workoutEndTime:%{public}f"
+ "clusterIdx < maxNumClusters || inputIdx < inputsToCluster.size()"
+ "filterClusters: mode,%{public}d,lookback,%{public}.0f days,processed,%{public}u,sessionIdMismatch,%{public}u,modelSourceMismatch,%{public}u,timeWindowReject,%{public}u,filtered,%{public}zu"
+ "getPhoneBasedPriorDailyInputs returned %{public}zu entries"
+ "getSummarySince returned %{public}zu historical summaries"
+ "meanMaxMETs,%{private}.2f,dailyMaxMetsRecords,%{public}zu,priorSessionAttributes,%{public}d,usedSessionFallback,%{public}d"
+ "no"
+ "prior,%f,hrMin,%f,hrMax,%f,metsResponseRate,%f,metsRecoveryRate,%{public}f,numPairs,%{public}d"
+ "yes"
- "/Library/Caches/com.apple.xbs/Sources/CoreLocation/Framework/CardioHealth/Models/CHVO2MaxAdaptiveOutdoorPedestrianModel.mm"
- "Attempting Retrocompute for phone/ipad estimate which is not supported, workoutEndTime:%{private}f"
- "Calorimetry"
- "InsufficientSamplesForClustering,%{public}zu"
- "Overwriting meanMaxMets,calculated,%f,overwrite,%f"
- "VO2Max failed to calculate a prior due to invalid mean max METs."
- "VO2Max,AdaptiveOutdoorPedestrianModel,Longitudinal Estimate,numClusters,%lu,numClustersContr,%u,numWorkoutsContr,%u,medianResidual,%f,hrMin,%f,hrMax,%f,meanResidual,%f,clusterResidualBoundsMax,%f"
- "VO2Max,AdaptiveOutdoorPedestrianModel,Longitudinal Estimate,ts,%.9f,size,%lld,hrMin,%f,hrMax,%f,hrMean,%f,vo2Mean,%f,hrConfidenceMean,%f,gradeMean,%f,oneMinusFHR,%f,residual,%f,failHistResidCheck,%d,confidence,%f,sessionType,%d,isLongitudinal,%d"
- "VO2Max,Clustering failed"
- "VO2Max,GetMeanMaxMets,canCalculateMeanMaxMets,%{private}s,meanMaxMets,%{private}.3f"
- "VO2Max,HR Bounds,observedRestingHR,%f,fhrHRMin,%f,fhrHRMax,%f"
- "VO2Max,vo2MaxEstimationStatus,%{public}d,priorVO2Max,%{private}f,longitudinalVO2Max,%{private}f,sessionVO2Max,%{private}f"
- "Will not retrocompute VO2Max due to absense of VO2MaxInputs, workoutEndTime:%{private}f"
- "clusterIdx < kMaxNumClusters || inputIdx < modelInput.size()"
- "prior,%f,hrMin,%f,hrMax,%f,metsResponseRate,%f,metsRecoveryRate,%f,numPairs,%d"

```
