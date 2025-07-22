## PredictedContextAlgorithms

> `/System/Library/PrivateFrameworks/PredictedContextAlgorithms.framework/PredictedContextAlgorithms`

```diff

-27.0.0.0.0
-  __TEXT.__text: 0x8aac4
+29.0.0.0.0
+  __TEXT.__text: 0x8ad8c
   __TEXT.__auth_stubs: 0x1090
-  __TEXT.__objc_methlist: 0x6a0c
-  __TEXT.__const: 0xb64
-  __TEXT.__cstring: 0x3301
-  __TEXT.__oslogstring: 0x5b90
+  __TEXT.__objc_methlist: 0x6a34
+  __TEXT.__const: 0xbd4
+  __TEXT.__cstring: 0x32db
+  __TEXT.__oslogstring: 0x5d17
   __TEXT.__swift5_typeref: 0x2d0
   __TEXT.__swift5_reflstr: 0x14d
   __TEXT.__swift5_assocty: 0x30

   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x860
   __AUTH_CONST.__const: 0x810
-  __AUTH_CONST.__cfstring: 0x4260
-  __AUTH_CONST.__objc_const: 0xabe8
-  __AUTH_CONST.__objc_doubleobj: 0x1b0
+  __AUTH_CONST.__cfstring: 0x4200
+  __AUTH_CONST.__objc_const: 0xac28
+  __AUTH_CONST.__objc_doubleobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0xb28
   __AUTH.__data: 0x1b0
-  __DATA.__objc_ivar: 0x728
+  __DATA.__objc_ivar: 0x72c
   __DATA.__data: 0x258
   __DATA.__bss: 0x4a0
   __DATA.__common: 0x10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 983F9CC9-B615-3E7B-A9F5-F73DB98D3FF5
-  Functions: 2809
-  Symbols:   9087
-  CStrings:  4028
+  UUID: 1E0ADE0E-4EC1-34BE-8FD5-719403FD000F
+  Functions: 2813
+  Symbols:   9094
+  CStrings:  4015
 
Symbols:
+ -[PCPMapsActiveNavigation hasLoiIdentifier]
+ -[PCPMapsActiveNavigation loiIdentifier]
+ -[PCPMapsActiveNavigation setLoiIdentifier:]
+ OBJC_IVAR_$_PCPMapsActiveNavigation._loiIdentifier
CStrings:
+ "%{public}@ (visits=%{public}lu, loi=%{public}lu, workouts=%{public}lu, currentTime=%{public}.2f)"
+ "--- Workout Predictions (%{public}lu) ---"
+ "Before De-duping: cluster=%{public}@, activityType='%{public}@', isAlreadyPredicted=%{public}d"
+ "Capping outdoor walk probability to 0.89 from %f"
+ "Cluster %{public}@ (%{public}@), meanProbability=%{public}.3f, meanScore=%{public}.3f, numWorkouts=%{public}lu, location=%{public}@"
+ "Cluster %{public}@ has no activity type"
+ "Comparing with existing prediction: workoutType=%{public}llu, locationType=%{public}d (looking for workoutType=%{public}llu, locationType=%{public}d)"
+ "Converted '%{public}@' to workout type %{public}llu"
+ "Created prediction for activity type: %{public}@, total predictions now: %{public}lu"
+ "EventBundle has no associated visit, using HealthKit workout location=%{sensitive}@, workout=%{public}@"
+ "Failed to create prediction for cluster %{public}@"
+ "Location type '%{public}@' is %{public}@"
+ "LogisticRegression,%{public}@,output,%{public}.3f,logit,%{public}.3f,FeaturesRawAndWeighted,combinedPlaceType,%{public}.3f,%.3f,placeName,%{public}.3f,%.3f,geographicalProximity,%{public}.3f,%.3f,timeOfDay,%{public}.3f,%.3f,dayOfWeek,%{public}.3f,%.3f,isWeekend,%{public}.3f,%.3f,timeOfDayCircularStd,%{public}.3f,%.3f,latLongCircularStd,%{public}.3f,%.3f"
+ "Mapped %lu Clusters to UUIDs (totalClusters=%lu, numClusterProbabilities=%lu)"
+ "Prediction completed with %{public}lu predictions from %{public}lu clusters"
+ "Selected cluster %{public}@, workoutType: %{public}@, probability: %{public}.4f"
+ "Successfully decoded outOfPatternLogic!"
+ "Successfully decoded workoutPrediction!"
+ "Workout %@ (workoutType=%{public}llu, locationType=%{public}d) is already predicted, skipping"
+ "Workout '%{public}@' is NOT already predicted"
+ "Workout Prediction: %{public}@"
+ "WorkoutAnnotation: annotateEventBundle, contextEventsCount, %{public}lu, visitsCount, %{public}lu, majorVisitsCount, %{public}lu"
+ "WorkoutPrediction: Bundling - startDate, %{public}@, endDate, %{public}@, eventCount, %{public}lu, bundleCount, %{public}lu"
+ "WorkoutPrediction: Clustering final count %{public}lu"
+ "WorkoutPrediction: Compute Workout Clusters BEGIN. (visits=%{public}lu, loi=%{public}lu, workouts=%{public}lu)"
+ "WorkoutPrediction: Created a cluster ID=%{public}@, bundleCount=%{public}lu, phenotype=%{public}@, dateRange=%{public}@-%{public}@"
+ "WorkoutPrediction: Found more than one LOI for UUID=%@. First=%{sensitive}@, Second=%{sensitive}@"
+ "WorkoutPrediction: No matching Visit LOI found - visitID, %{public}@, loiID, %{public}@, startDate, %{public}@, endDate, %{public}@"
+ "WorkoutPrediction: Real-Time Visit: startDate, %{public}@, endDate, %{public}@, poiCategory, %{public}@, placeUserType, %{public}d, placeName, %{sensitive}@, location, %{sensitive}@"
+ "WorkoutPrediction: Total %{public}lu embeddings and %{public}lu clusters coded"
+ "WorkoutPrediction: Total %{public}lu embeddings and %{public}lu clusters decoded"
- "%@ (visits=%lu, loi=%lu, workouts=%lu, currentTime=%.2f)"
- "--- Workout Predictions (%lu) ---"
- "Applied home/work mapping: %.4f -> %.4f"
- "Applied out-of-home/work mapping: %.4f -> %.4f"
- "Before deduping: Cluster %@: activityType='%@' (length=%lu)"
- "Cluster %@ (%@), mapped probability,%.4f, location,%@"
- "Cluster %@ calculated: timeStd=%.6f, locationStd=%.6f"
- "Cluster %@ has no activity type"
- "Cluster %@: workoutType=%@, meanProbability=%.3f, meanScore=%.3f, numWorkouts=%lu"
- "Comparing with existing prediction: workoutType=%llu, locationType=%d (looking for workoutType=%llu, locationType=%d)"
- "Computing circular std for cluster %@"
- "Converted '%@' to workout type %llu"
- "Created cluster map with %lu clusters"
- "Created prediction for activity type: %@, total predictions now: %lu"
- "EventBundle has no associated visit, using HealthKit workout location=%{sensitive}@"
- "Failed to create prediction for cluster %@"
- "Generating predictions from %lu clusters with %lu probability entries"
- "Location type '%@' is %@home/work"
- "LogisticRegression,%@,output,%.3f,logit,%.3f,FeaturesRawAndWeighted,combinedPlaceType,%.3f,%.3f,placeName,%.3f,%.3f,geographicalProximity,%.3f,%.3f,timeOfDay,%.3f,%.3f,dayOfWeek,%.3f,%.3f,isWeekend,%.3f,%.3f,timeOfDayCircularStd,%.3f,%.3f,latLongCircularStd,%.3f,%.3f"
- "Prediction completed with %lu predictions"
- "Selected cluster %@, workoutType: %@ , probability: %.4f"
- "Sorted cluster UUIDs (%lu): %@"
- "Succesfully decoded outOfPatternLogic!"
- "Succesfully decoded workoutPrediction!"
- "Workout %@ (workoutType=%llu, locationType=%d) is already predicted, skipping"
- "Workout '%@' is NOT already predicted"
- "Workout Prediction: %@"
- "Workout type %@ already predicted, skipping cluster %@"
- "WorkoutAnnotation: annotateEventBundle, visit Events count, %lu, valid visits count, %lu, majorVisits count, %lu"
- "WorkoutPrediction: Bundling - startDate, %@, endDate, %@, bundle count,%lu"
- "WorkoutPrediction: Bundling - there are %lu event(s) to bundle.(%@ - %@)"
- "WorkoutPrediction: Clustering final count %lu"
- "WorkoutPrediction: Compute Workout Clusters BEGIN. (visits=%lu, loi=%lu, workouts=%lu)"
- "WorkoutPrediction: Created a cluster ID=%@,bundleCount=%lu,phenotype=%@, dateRange=%@-%@"
- "WorkoutPrediction: No matching Visit LOI found, visit, id,%@, startDate, %@ endDate, %@"
- "WorkoutPrediction: Real-Time Visit: startDate, %@, endDate, %@, poiCategory, %@, placeUserType, %d, placeName, %{sensitive}@, location, %{sensitive}@"
- "WorkoutPrediction: Total %lu embeddings and %lu clusters coded"
- "WorkoutPrediction: Total %lu embeddings and %lu clusters decoded"
- "not "
- "thresholdHomeWork"
- "thresholdOther"

```
