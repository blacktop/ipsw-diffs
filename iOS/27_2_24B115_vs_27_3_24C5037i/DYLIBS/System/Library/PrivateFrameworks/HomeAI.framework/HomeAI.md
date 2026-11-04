## HomeAI

> `/System/Library/PrivateFrameworks/HomeAI.framework/HomeAI`

```diff

-382.0.0.0.0
-  __TEXT.__text: 0x17b2d4
+386.0.0.0.0
+  __TEXT.__text: 0x17b5cc
   __TEXT.__init_offsets: 0x10
-  __TEXT.__objc_methlist: 0xa6e4
+  __TEXT.__objc_methlist: 0xa6ec
   __TEXT.__const: 0x496d
-  __TEXT.__cstring: 0xdb67
+  __TEXT.__cstring: 0xdb94
   __TEXT.__gcc_except_tab: 0xc240
-  __TEXT.__oslogstring: 0xe915
+  __TEXT.__oslogstring: 0xe9d2
   __TEXT.__dlopen_cstrs: 0x16e
   __TEXT.__swift5_typeref: 0x21
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_reflstr: 0x74
   __TEXT.__swift5_fieldmd: 0x4c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x5ba0
+  __TEXT.__unwind_info: 0x5ba8
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x39c8
+  __DATA_CONST.__const: 0x39e8
   __DATA_CONST.__objc_classlist: 0x718
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x4868
+  __DATA_CONST.__objc_selrefs: 0x4870
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x610
   __DATA_CONST.__objc_arraydata: 0x6e8
   __DATA_CONST.__got: 0xc48
-  __AUTH_CONST.__const: 0x48d0
+  __AUTH_CONST.__const: 0x48f0
   __AUTH_CONST.__cfstring: 0x8c40
   __AUTH_CONST.__objc_const: 0x164c0
   __AUTH_CONST.__weak_auth_got: 0x28

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5532
-  Symbols:   10280
-  CStrings:  3233
+  Functions: 5534
+  Symbols:   10283
+  CStrings:  3236
 
Symbols:
+ +[HMITorsoClassifier predictedLinkedEntityUUIDsForPrediction:homeUUID:]
+ +[HMIVideoAnalyzerMutableReport silhouetteScoreForMatches:previousMatches:truePositiveScores:falsePositiveScores:falseNegativeScores:]
+ -[HMICameraActivityZone jsonRepresentationOfDetectedObject:motionDetection:eventClass:]
+ -[HMICameraActivityZone overlapsWithEllipseInsideRect:]
+ -[HMICameraActivityZone overlapsWithEllipseInsideRect:withInsetPercentage:]
+ _HMILineSegmentsIntersect
+ ___134+[HMIVideoAnalyzerMutableReport silhouetteScoreForMatches:previousMatches:truePositiveScores:falsePositiveScores:falseNegativeScores:]_block_invoke
+ ___134+[HMIVideoAnalyzerMutableReport silhouetteScoreForMatches:previousMatches:truePositiveScores:falsePositiveScores:falseNegativeScores:]_block_invoke_2
+ ___71+[HMITorsoClassifier predictedLinkedEntityUUIDsForPrediction:homeUUID:]_block_invoke
+ ___block_descriptor_32_e43_"NSUUID"16?0"HMIPersonsModelPrediction"8l
- +[HMIVideoAnalyzerMutableReport sihouetteScoreForMatches:previousMatches:truePositiveScores:falsePositiveScores:falseNegativeScores:]
- -[HMICameraActivityZone jsonReperesentaionOfDetectedObject:motionDetection:eventClass:]
- -[HMICameraActivityZone overlapsWithElipseInsideRect:]
- -[HMICameraActivityZone overlapsWithElipseInsideRect:withInsetPercentage:]
- _HMILineSgementsIntersect
- ___133+[HMIVideoAnalyzerMutableReport sihouetteScoreForMatches:previousMatches:truePositiveScores:falsePositiveScores:falseNegativeScores:]_block_invoke
- ___133+[HMIVideoAnalyzerMutableReport sihouetteScoreForMatches:previousMatches:truePositiveScores:falsePositiveScores:falseNegativeScores:]_block_invoke_2
CStrings:
+ "@\"NSUUID\"16@?0@\"HMIPersonsModelPrediction\"8"
+ "Couldn't retrieve linked predictions for torso personUUID: %@ homeUUID: %@ error: %@"
+ "Face removed from unknown and uncertain bucket, SSD confidence = %f, entropy of laplacian = %f, Face yaw = %f, box size: %f"
+ "Named person %@ with at least 1 personLink has %lu clusters, treating as impure"
+ "Successfully associated face crops (num UUIDs %lu) to person UUID: %@ for source: %@"
+ "Successfully removed persons %@"
+ "Unknown server error"
+ "[%{public}@] Couldn't retrieve linked predictions for torso personUUID: %@ homeUUID: %@ error: %@"
+ "[%{public}@] Face removed from unknown and uncertain bucket, SSD confidence = %f, entropy of laplacian = %f, Face yaw = %f, box size: %f"
+ "[%{public}@] Named person %@ with at least 1 personLink has %lu clusters, treating as impure"
+ "[%{public}@] Successfully associated face crops (num UUIDs %lu) to person UUID: %@ for source: %@"
+ "[%{public}@] Successfully removed persons %@"
- "Face removed from unknown and uncertian bucket, SSD confidence = %f, entropy of laplacian = %f, Face yaw = %f, box size: %f"
- "Named person %@ with atleast 1 personLink has %lu clusters, treating as impure"
- "Succesfully associated face crops (num UUIDs %lu) to person UUID: %@ for source: %@"
- "Succesfully removed persons %@"
- "Unkown server error"
- "[%{public}@] Face removed from unknown and uncertian bucket, SSD confidence = %f, entropy of laplacian = %f, Face yaw = %f, box size: %f"
- "[%{public}@] Named person %@ with atleast 1 personLink has %lu clusters, treating as impure"
- "[%{public}@] Succesfully associated face crops (num UUIDs %lu) to person UUID: %@ for source: %@"
- "[%{public}@] Succesfully removed persons %@"
```
