## PromotedContentPrediction

> `/System/Library/PrivateFrameworks/PromotedContentPrediction.framework/PromotedContentPrediction`

```diff

-91.0.0.0.0
-  __TEXT.__text: 0x2b3d4
+94.0.0.0.0
+  __TEXT.__text: 0x2c540
   __TEXT.__auth_stubs: 0xa10
-  __TEXT.__objc_methlist: 0x2844
-  __TEXT.__const: 0x478
-  __TEXT.__cstring: 0x165e
-  __TEXT.__oslogstring: 0x2f97
-  __TEXT.__gcc_except_tab: 0x10e0
+  __TEXT.__objc_methlist: 0x28a4
+  __TEXT.__const: 0x488
+  __TEXT.__cstring: 0x16fe
+  __TEXT.__oslogstring: 0x2fcf
+  __TEXT.__gcc_except_tab: 0x1130
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x9f0
+  __TEXT.__unwind_info: 0xa04
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x630
-  __TEXT.__objc_methname: 0x6e64
-  __TEXT.__objc_methtype: 0xd62
-  __TEXT.__objc_stubs: 0x5960
+  __TEXT.__objc_methname: 0x70b4
+  __TEXT.__objc_methtype: 0xd6a
+  __TEXT.__objc_stubs: 0x5aa0
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0xb28
+  __DATA_CONST.__const: 0xb40
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3e30
-  __DATA_CONST.__objc_selrefs: 0x1b90
+  __DATA_CONST.__objc_const: 0x3ec0
+  __DATA_CONST.__objc_selrefs: 0x1be0
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__cfstring: 0x2500
+  __AUTH_CONST.__cfstring: 0x25e0
   __AUTH_CONST.__objc_const: 0x17d0
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__objc_intobj: 0x90

   __AUTH.__objc_data: 0x640
   __DATA.__objc_classrefs: 0x348
   __DATA.__objc_superrefs: 0x140
-  __DATA.__objc_ivar: 0x324
+  __DATA.__objc_ivar: 0x330
   __DATA.__data: 0x240
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xd20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D689AED4-8342-3C66-B433-D0821705F2C1
-  Functions: 877
-  Symbols:   696
-  CStrings:  2433
+  UUID: 913392C4-C39A-39AF-8FE9-16F6AFB27B73
+  Functions: 888
+  Symbols:   701
+  CStrings:  2467
 
Symbols:
+ _kAPOdmlFeatureTypeAppVectorODMLKey
+ _kAPOdmlFeatureTypeQueryVectorKey
+ _kAPOdmlFeatureTypeUserQueryVectorKey
+ _kAPOdmlPredictionQueryVectorCalculationFailureError
+ _kAPOdmlPredictionQueryVectorRetrievalFailureError
CStrings:
+ "\x0f\x0e"
+ "@\"DESRecordSet\""
+ "Augmented records: %@"
+ "B40@0:8@16@24@32"
+ "Generated the following training rows: %@"
+ "Generating Training Set"
+ "Local records: %@"
+ "Sampling ratio: %@"
+ "T@\"DESRecordSet\",R,C,N,V_localRecords"
+ "T@\"MLFeatureValue\",&,N,V_userQueryVector"
+ "T@\"NSArray\",R,N,V_augmentedDESRecords"
+ "T@\"NSArray\",R,N,V_augmentedRecords"
+ "T@\"NSNumber\",R,N,V_augmentedDESRecordsLimit"
+ "T@\"NSNumber\",R,N,V_augmentedDESRecordsRatio"
+ "T@\"NSNumber\",R,N,V_augmentedDESRecordsTruePercentage"
+ "T@\"NSString\",R,N,V_augmentedDESRecordsTargetKey"
+ "[%@] Vector retrieval failed; CoreData failed to load with the following error: %@."
+ "_augmentedDESRecords"
+ "_augmentedDESRecordsLimit"
+ "_augmentedDESRecordsRatio"
+ "_augmentedDESRecordsTargetKey"
+ "_augmentedDESRecordsTruePercentage"
+ "_augmentedRecords"
+ "_combineRows:augmentedRows:"
+ "_extractFeaturesFromDataBlob:featuresRequired:andSaveTo:"
+ "_gatherFeaturesFromAdRecord:requiredFeatures:"
+ "_localRecords"
+ "_preprocessAugmentedDESRecords:andAddMetadataTo:addRecordIDsTo:"
+ "_trainingRowsFromDESRecord:isCounterfactual:"
+ "_userQueryVector"
+ "appVectorODML"
+ "arrayByAddingObjectsFromArray:"
+ "augmentedDESRecords"
+ "augmentedDESRecordsLimit"
+ "augmentedDESRecordsRatio"
+ "augmentedDESRecordsTargetKey"
+ "augmentedDESRecordsTruePercentage"
+ "augmentedRecords"
+ "computeUserQueryVectorWithResponses:"
+ "deleteExpiredFeaturesForName:lookbackWindow:"
+ "featuresForName:"
+ "localRecords"
+ "metricsForTrainingRow:withClientPttr:"
+ "parseRowsFromRecords:recordIDs:"
+ "queryVector"
+ "saveFeaturesFromResponse:"
+ "saveUserQueryVector"
+ "setUserQueryVector:"
+ "userQueryVector"
+ "v40@0:8@16@24@32"
+ "vectorsForName:lookbackWindow:"
- "\x0f\n"
- "@44@0:8@16@24B32^@36"
- "B48@0:8@16@24@32^@40"
- "IDs: %@"
- "Metadatas: %@"
- "Records: %@"
- "T@\"NSArray\",R,C,N,V_recordDictionaries"
- "T@\"NSArray\",R,C,N,V_recordIDs"
- "T@\"NSArray\",R,C,N,V_recordMetadatas"
- "T@\"NSArray\",R,N,V_mockDESRecords"
- "[%@]: Ad is neither tapped nor impressed."
- "[%@]: Ad is neither tapped nor impressed. We will not use this training row."
- "_additionalMetricsFromAdRecord:clientPttr:error:"
- "_extractFeaturesFromDataBlob:featuresRequired:andSaveTo:error:"
- "_gatherFeaturesFromAdRecord:requiredFeatures:forMetricsOnly:error:"
- "_mockDESRecords"
- "_recordDictionaries"
- "_recordIDs"
- "_recordMetadatas"
- "_trainingRowsFromDESRecord:isCounterfactual:error:"
- "deleteExpiredFeaturesForName:"
- "initWithRecipe:"
- "initWithRecipe:recordDictionaries:recordMetadatas:recordIDs:"
- "isDateInToday:"
- "metricsFromDESRecordWithClientPttr:error:"
- "mockDESRecords"
- "recordDictionaries"
- "recordIDs"
- "recordMetadatas"

```
