## CoreLocation

> `/System/Library/Frameworks/CoreLocation.framework/CoreLocation`

```diff

-2953.0.19.0.0
-  __TEXT.__text: 0x1b99d4
-  __TEXT.__auth_stubs: 0x19e0
+2953.0.25.0.0
+  __TEXT.__text: 0x1bcf34
+  __TEXT.__auth_stubs: 0x1a10
   __TEXT.__objc_methlist: 0x9524
-  __TEXT.__const: 0x49e5
-  __TEXT.__gcc_except_tab: 0xcc88
-  __TEXT.__oslogstring: 0x333b7
-  __TEXT.__cstring: 0x1ff8c
+  __TEXT.__const: 0x4a05
+  __TEXT.__gcc_except_tab: 0xcdf4
+  __TEXT.__oslogstring: 0x33c14
+  __TEXT.__cstring: 0x201d1
   __TEXT.__ustring: 0x750
-  __TEXT.__unwind_info: 0x5370
+  __TEXT.__unwind_info: 0x53e0
   __TEXT.__objc_classname: 0x1397
-  __TEXT.__objc_methname: 0x1af39
+  __TEXT.__objc_methname: 0x1af5e
   __TEXT.__objc_methtype: 0x616d
-  __TEXT.__objc_stubs: 0xdc00
+  __TEXT.__objc_stubs: 0xdc40
   __DATA_CONST.__got: 0x6e8
-  __DATA_CONST.__const: 0x1d18
+  __DATA_CONST.__const: 0x1d38
   __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5028
+  __DATA_CONST.__objc_selrefs: 0x5038
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0xd08
+  __AUTH_CONST.__auth_got: 0xd20
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x3ae0
   __AUTH_CONST.__cfstring: 0xab20

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5045
-  Symbols:   1087
-  CStrings:  9744
+  Functions: 5057
+  Symbols:   1090
+  CStrings:  9769
 
Symbols:
+ _arc4random_uniform
+ _log10
+ _pow
CStrings:
+ "03:09:20"
+ "NSIndexSet *CLTrajectorySmoother::chooseRandomLocationIndices()"
+ "Oct 27 2024"
+ "[CLTrajectorySmoother]:[chooseRandomLocationIndices] insufficient location samplers for random selection, %!{(MISSING)publuc}zu."
+ "[CLTrajectorySmoother]:[computeScenarioSpecificMetrics] number of iteration,%!l(MISSING)u, number of intermediate points, %!l(MISSING)u."
+ "[CLTrajectorySmoother]:[runPedestrianTrajectorySmoothingWithRANSAC] Disgard model, %!{(MISSING)public}zu, isDisplacementRatio, %!{(MISSING)public}d, isCourseOffset, %!{(MISSING)public}d, isDistance, %!{(MISSING)public}d."
+ "[CLTrajectorySmoother]:[runPedestrianTrajectorySmoothingWithRANSAC] Disgarding model, areInliersTooSparse, %!{(MISSING)public}d, isRatioOfInliersLow, %!{(MISSING)public}d."
+ "[CLTrajectorySmoother]:[runPedestrianTrajectorySmoothingWithRANSAC] Number of selected models, %!{(MISSING)public}zu."
+ "[CLTrajectorySmoother]:[runPedestrianTrajectorySmoothingWithRANSAC] RANSAC is called with insufficient locations samples, %!{(MISSING)publuc}zu."
+ "[CLTrajectorySmoother]:[runPedestrianTrajectorySmoothingWithRANSAC] RTS failed while evaluating model, %!{(MISSING)public}zu."
+ "[CLTrajectorySmoother]:[runPedestrianTrajectorySmoothingWithRANSAC] RTS failed while generating models with randomly selected location samples."
+ "[CLTrajectorySmoother]:[runPedestrianTrajectorySmoothingWithRANSAC] Selection of inliers failed."
+ "[CLTrajectorySmoother]:[runPedestrianTrajectorySmoothingWithRANSAC] computation of scenario specific metrics failed."
+ "[CLTrajectorySmoother]:[runPedestrianTrajectorySmoothingWithRANSAC] random location selection failed."
+ "[CLTrajectorySmoother]:[runPedestrianTrajectorySmoothingWithRANSAC] selected model, %!{(MISSING)public}zu."
+ "[CLTrajectorySmoother]:[runPedestrianTrajectorySmoothing] RANSAC failed. Fall back to non-RANSAC."
+ "[CLTrajectorySmoother]:[runPedestrianTrajectorySmoothing] RANSAC succeeded."
+ "[CLTrajectorySmoother]:[runPedestrianTrajectorySmoothing] Returned false. Number of hunc based selected locations %!{(MISSING)public}zu."
+ "[CLTrajectorySmoother]:[runPedestrianTrajectorySmoothing] ratioOfDenseUrbanLocation, %!{(MISSING)private}.2f, durationOfSession_inSec, %!{(MISSING)public}.2f, shouldRunRANSAC, %!{(MISSING)public}d."
+ "[CLTrajectorySmoother]:[runRTSOnly] RTS is called with insufficient locations samples, %!{(MISSING)publuc}zu."
+ "[CLTrajectorySmoother]:[selectInliers] first estimated location is later than first measured locaton, timestampFirstEstimated, %!f(MISSING), timestampFirstMeasured, %!f(MISSING)"
+ "[CLTrajectorySmoother]:[selectInliers] projection is greater than 1, fromPrevToMeas, %!f(MISSING), fromPrevToEvaluate, %!f(MISSING)"
+ "bool CLTrajectorySmoother::computeScenarioSpecificMetrics(NSArray<CLTripSegmentLocation *> * _Nonnull)"
+ "bool CLTrajectorySmoother::runPedestrianTrajectorySmoothingWithRANSAC(NSArray<CLTripSegmentLocation *> * _Nonnull, NSArray<CLBackgroundInertialOdometrySample *> * _Nullable, NSMutableArray<CLTripSegmentLocation *> * _Nonnull)"
+ "bool CLTrajectorySmoother::runRTSOnly(NSArray<CLTripSegmentLocation *> * _Nonnull, NSArray<CLBackgroundInertialOdometrySample *> * _Nullable, NSMutableArray<CLTripSegmentLocation *> * _Nonnull)"
+ "bool CLTrajectorySmoother::selectInliers(RTSModel &, NSMutableArray<CLTripSegmentLocation *> * _Nonnull, NSArray<CLTripSegmentLocation *> * _Nonnull)"
+ "enumerateIndexesUsingBlock:"
+ "tearDown"
+ "v24@?0Q8^B16"
- "13:36:52"
- "Oct 16 2024"
- "[CLTrajectorySmoother]:[runPedestrianTrajectorySmoothing] Returned false. tripLocation array count, %!{(MISSING)public}zu, selected tripLocation count, %!{(MISSING)public}zu expected minimum count, %!{(MISSING)public}zu."
- "std::vector<size_t> CLTrajectorySmoother::selectLocationSamplesBasedOnUncertainty(NSArray<CLTripSegmentLocation *> * _Nonnull, const double, const double, const size_t)"

```
