## ProactiveML

> `/System/Library/PrivateFrameworks/ProactiveML.framework/Versions/A/ProactiveML`

```diff

-1271.10.0.0.0
-  __TEXT.__text: 0x478c4
-  __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_methlist: 0x429c
-  __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x7b0
+1276.10.4.0.0
+  __TEXT.__text: 0x4780c
+  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__objc_methlist: 0x45ec
+  __TEXT.__const: 0x128
+  __TEXT.__dlopen_cstrs: 0x6e
+  __TEXT.__gcc_except_tab: 0x7b8
   __TEXT.__cstring: 0x7a2f
   __TEXT.__oslogstring: 0x23dd
-  __TEXT.__dlopen_cstrs: 0x6e
-  __TEXT.__unwind_info: 0x1128
+  __TEXT.__unwind_info: 0x10d8
   __TEXT.__objc_classname: 0xacd
   __TEXT.__objc_methname: 0x803f
   __TEXT.__objc_methtype: 0x1b12
   __TEXT.__objc_stubs: 0x5060
   __DATA_CONST.__got: 0x3e8
-  __DATA_CONST.__const: 0x208
+  __DATA_CONST.__const: 0x220
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ca8
+  __DATA_CONST.__objc_selrefs: 0x1d20
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_arraydata: 0x3e0
-  __AUTH_CONST.__auth_got: 0x5e0
+  __AUTH_CONST.__auth_got: 0x5d8
   __AUTH_CONST.__const: 0x12b0
   __AUTH_CONST.__cfstring: 0x42a0
-  __AUTH_CONST.__objc_const: 0x8630
+  __AUTH_CONST.__objc_const: 0x8098
   __AUTH_CONST.__objc_intobj: 0x3a8
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0x28

   - /System/Library/PrivateFrameworks/WirelessDiagnostics.framework/Versions/A/WirelessDiagnostics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 910EBF66-973A-3D45-885C-3EB376E6FDB8
-  Functions: 1575
-  Symbols:   3734
+  UUID: CE677920-A029-3550-B184-B9A53F83699A
+  Functions: 1559
+  Symbols:   3733
   CStrings:  3021
 
Symbols:
+ __101-[PMLTrainingStore _loadDataFromLabelAndTuples:model:numberOfRows:numberOfColumns:lastUsedMax:block:]_block_invoke.129
+ __101-[PMLTrainingStore _loadDataFromLabelAndTuples:model:numberOfRows:numberOfColumns:lastUsedMax:block:]_block_invoke.149
+ __101-[PMLTrainingStore _loadDataFromLabelAndTuples:model:numberOfRows:numberOfColumns:lastUsedMax:block:]_block_invoke_2.133
+ __115-[PMLTrainingStore _loadDataForModel:privacyBudgetRefreshPeriod:labelAndStartRows:batchSize:supportPerLabel:block:]_block_invoke.179
+ __30-[PMLTrainingStore getSchema:]_block_invoke.367
+ __32-[PMLTrainingStore sessionStats]_block_invoke.258
+ __38-[PMLLogRegTrainingPlan runWithError:]_block_invoke.31
+ __40-[PMLLogRegEvaluationPlan runWithError:]_block_invoke.19
+ __68-[PMLTrainingStore lastTrainingFeaturizationForModelName:andLocale:]_block_invoke.314
+ __68-[PMLTrainingStore updateLastTrainingFeaturizationForModel:andData:]_block_invoke.331
+ __71-[PMLTrainingStore limitSessionsWithSessionDescriptor:withLabel:limit:]_block_invoke.223
+ __71-[PMLTrainingStore limitSessionsWithSessionDescriptor:withLabel:limit:]_block_invoke.227
+ __71-[PMLTrainingStore limitSessionsWithSessionDescriptor:withLabel:limit:]_block_invoke.234
+ __71-[PMLTrainingStore limitSessionsWithSessionDescriptor:withLabel:limit:]_block_invoke_2.224
+ __71-[PMLTrainingStore limitSessionsWithSessionDescriptor:withLabel:limit:]_block_invoke_2.231
+ __85-[PMLTrainingStore limitSessionsForEachLabelWithSessionDescriptor:totalSessionLimit:]_block_invoke.186
+ __85-[PMLTrainingStore limitSessionsForEachLabelWithSessionDescriptor:totalSessionLimit:]_block_invoke.187
+ __85-[PMLTrainingStore limitSessionsForEachLabelWithSessionDescriptor:totalSessionLimit:]_block_invoke.194
+ __85-[PMLTrainingStore limitSessionsForEachLabelWithSessionDescriptor:totalSessionLimit:]_block_invoke_2.195
+ __89-[PMLTrainingStore _loadBatchForModel:privacyBudgetRefreshPeriod:labels:batchSize:block:]_block_invoke.170
+ __89-[PMLTrainingStore _loadBatchForModel:privacyBudgetRefreshPeriod:labels:batchSize:block:]_block_invoke.174
+ __90-[PMLTrainingStore sessionDimensionsForModel:startingRowId:onlyAppleInternal:labelFilter:]_block_invoke.112
+ __94+[PMLEspressoTrainingPlan _getModelParametersForTask:globalNames:weightNames:biasNames:error:]_block_invoke.255
+ __Block_byref_object_copy_.1040
+ __Block_byref_object_copy_.2062
+ __Block_byref_object_copy_.2896
+ __Block_byref_object_copy_.297
+ __Block_byref_object_copy_.5885
+ __Block_byref_object_copy_.693
+ __Block_byref_object_dispose_.1041
+ __Block_byref_object_dispose_.2063
+ __Block_byref_object_dispose_.2897
+ __Block_byref_object_dispose_.298
+ __Block_byref_object_dispose_.5886
+ __Block_byref_object_dispose_.694
+ __block_literal_global.172
+ __block_literal_global.189
+ __block_literal_global.197
+ __block_literal_global.204
+ __block_literal_global.2064
+ __block_literal_global.212
+ __block_literal_global.226
+ __block_literal_global.236
+ __block_literal_global.260
+ __block_literal_global.265
+ __block_literal_global.294
+ __block_literal_global.316
+ __block_literal_global.321
+ __block_literal_global.333
+ __block_literal_global.343
+ __block_literal_global.345
+ __block_literal_global.3476
+ __block_literal_global.352
+ __block_literal_global.403
+ __block_literal_global.406
+ __block_literal_global.4138
+ __block_literal_global.4287
+ __block_literal_global.4813
+ __migrateSessionsToFloats_block_invoke.395
+ __migrateSessionsToFloats_block_invoke.399
+ __migrateSessionsToFloats_block_invoke.404
- __101-[PMLTrainingStore _loadDataFromLabelAndTuples:model:numberOfRows:numberOfColumns:lastUsedMax:block:]_block_invoke.123
- __101-[PMLTrainingStore _loadDataFromLabelAndTuples:model:numberOfRows:numberOfColumns:lastUsedMax:block:]_block_invoke.143
- __101-[PMLTrainingStore _loadDataFromLabelAndTuples:model:numberOfRows:numberOfColumns:lastUsedMax:block:]_block_invoke_2.127
- __115-[PMLTrainingStore _loadDataForModel:privacyBudgetRefreshPeriod:labelAndStartRows:batchSize:supportPerLabel:block:]_block_invoke.173
- __30-[PMLTrainingStore getSchema:]_block_invoke.361
- __32-[PMLTrainingStore sessionStats]_block_invoke.252
- __38-[PMLLogRegTrainingPlan runWithError:]_block_invoke.25
- __40-[PMLLogRegEvaluationPlan runWithError:]_block_invoke.13
- __68-[PMLTrainingStore lastTrainingFeaturizationForModelName:andLocale:]_block_invoke.308
- __68-[PMLTrainingStore updateLastTrainingFeaturizationForModel:andData:]_block_invoke.325
- __71-[PMLTrainingStore limitSessionsWithSessionDescriptor:withLabel:limit:]_block_invoke.217
- __71-[PMLTrainingStore limitSessionsWithSessionDescriptor:withLabel:limit:]_block_invoke.221
- __71-[PMLTrainingStore limitSessionsWithSessionDescriptor:withLabel:limit:]_block_invoke.228
- __71-[PMLTrainingStore limitSessionsWithSessionDescriptor:withLabel:limit:]_block_invoke_2.218
- __71-[PMLTrainingStore limitSessionsWithSessionDescriptor:withLabel:limit:]_block_invoke_2.225
- __85-[PMLTrainingStore limitSessionsForEachLabelWithSessionDescriptor:totalSessionLimit:]_block_invoke.180
- __85-[PMLTrainingStore limitSessionsForEachLabelWithSessionDescriptor:totalSessionLimit:]_block_invoke.181
- __85-[PMLTrainingStore limitSessionsForEachLabelWithSessionDescriptor:totalSessionLimit:]_block_invoke.188
- __85-[PMLTrainingStore limitSessionsForEachLabelWithSessionDescriptor:totalSessionLimit:]_block_invoke_2.189
- __89-[PMLTrainingStore _loadBatchForModel:privacyBudgetRefreshPeriod:labels:batchSize:block:]_block_invoke.164
- __89-[PMLTrainingStore _loadBatchForModel:privacyBudgetRefreshPeriod:labels:batchSize:block:]_block_invoke.168
- __90-[PMLTrainingStore sessionDimensionsForModel:startingRowId:onlyAppleInternal:labelFilter:]_block_invoke.106
- __94+[PMLEspressoTrainingPlan _getModelParametersForTask:globalNames:weightNames:biasNames:error:]_block_invoke.249
- __Block_byref_object_copy_.1062
- __Block_byref_object_copy_.2092
- __Block_byref_object_copy_.2929
- __Block_byref_object_copy_.314
- __Block_byref_object_copy_.5921
- __Block_byref_object_copy_.708
- __Block_byref_object_dispose_.1063
- __Block_byref_object_dispose_.2093
- __Block_byref_object_dispose_.2930
- __Block_byref_object_dispose_.315
- __Block_byref_object_dispose_.5922
- __Block_byref_object_dispose_.709
- __block_literal_global.166
- __block_literal_global.183
- __block_literal_global.191
- __block_literal_global.198
- __block_literal_global.206
- __block_literal_global.2094
- __block_literal_global.220
- __block_literal_global.230
- __block_literal_global.254
- __block_literal_global.259
- __block_literal_global.288
- __block_literal_global.310
- __block_literal_global.315
- __block_literal_global.327
- __block_literal_global.337
- __block_literal_global.339
- __block_literal_global.346
- __block_literal_global.3511
- __block_literal_global.397
- __block_literal_global.400
- __block_literal_global.4158
- __block_literal_global.4313
- __block_literal_global.4837
- __migrateSessionsToFloats_block_invoke.389
- __migrateSessionsToFloats_block_invoke.393
- __migrateSessionsToFloats_block_invoke.398
- _fmod

```
