## CardioHealth

> `/System/Library/PrivateFrameworks/CardioHealth.framework/Versions/A/CardioHealth`

```diff

-3185.0.6.0.0
-  __TEXT.__text: 0xcd24
-  __TEXT.__const: 0x550
-  __TEXT.__gcc_except_tab: 0x3b4
+3186.0.12.0.0
+  __TEXT.__text: 0xce1c
+  __TEXT.__const: 0x564
+  __TEXT.__gcc_except_tab: 0x3a4
   __TEXT.__cstring: 0xed
-  __TEXT.__oslogstring: 0x25ac
-  __TEXT.__unwind_info: 0x2d0
+  __TEXT.__oslogstring: 0x265a
+  __TEXT.__unwind_info: 0x2c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 101
-  Symbols:   86
-  CStrings:  94
+  Functions: 103
+  Symbols:   88
+  CStrings:  96
 
Symbols:
+ __ZN17CHVO2MaxEstimator20setHRConfidenceScaleE23VO2MaxHRConfidenceScale
+ __ZN17CHVO2MaxEstimator34setMinPointsToTrustClusterOverrideEd
CStrings:
+ "Overriding minPointsToTrustCluster,default,%f,override,%f"
+ "VO2Max HR confidence scale set: scale,%{public}d"
+ "VO2Max InsufficientSamplesForClustering, Only %{public}zu of %{public}zu samples usable, need %{public}zu minimum - clusteringMode=%{public}d"
+ "VO2Max deriveStageBasedClusters failed: inputSize=%zu, highConfidenceInputs=%zu, hrConfScale=%{public}d, hrConfThreshold=%{public}.4f"
- "VO2Max InsufficientSamplesForClustering, Only %{public}zu samples provided, need %{public}zu minimum - clusteringMode=%{public}d"
- "VO2Max deriveStageBasedClusters failed: inputSize=%zu, highConfidenceInputs=%zu"
```
