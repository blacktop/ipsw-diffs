## DebugHierarchyKit

> `/System/Library/PrivateFrameworks/DebugHierarchyKit.framework/DebugHierarchyKit`

```diff

 73.0.0.0.0
-  __TEXT.__text: 0x13bc8
-  __TEXT.__auth_stubs: 0x640
+  __TEXT.__text: 0x14a60
+  __TEXT.__auth_stubs: 0x600
   __TEXT.__objc_methlist: 0x20e4
   __TEXT.__const: 0x80
   __TEXT.__cstring: 0x1313
   __TEXT.__oslogstring: 0x5b
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x698
+  __TEXT.__unwind_info: 0x688
   __TEXT.__objc_classname: 0x394
   __TEXT.__objc_methname: 0x3825
   __TEXT.__objc_methtype: 0x9b7

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x330
-  __AUTH_CONST.__auth_got: 0x330
+  __AUTH_CONST.__auth_got: 0x310
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x1b80
   __AUTH_CONST.__objc_const: 0x57c8

   - /System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0F41235A-109F-387B-B6A1-DCD7DA33EB42
+  UUID: 2FCFF9A0-B330-3D1C-9DCE-7C8AB3CB77CE
   Functions: 609
-  Symbols:   1753
+  Symbols:   1749
   CStrings:  1364
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x27
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
Functions:
~ -[DBGDataCoordinatorTargetHub _decompressedDataForRequestResponseData:] : 144 -> 156
~ -[DBGDataCoordinatorTargetHub _processFetchResults:forRequest:] : 1596 -> 1644
~ -[DBGDataCoordinatorTargetHub _processRequestLogs:forRequest:] : 412 -> 424
~ -[DBGDataCoordinatorTargetHub _updateSnapshotWithResponse:forRequest:] : 1032 -> 1100
~ -[DBGDataCoordinatorTargetHub processGroupDict:isDirectChildGroup:parentNode:] : 580 -> 608
~ -[DBGDataCoordinatorTargetHub processDebugHierarchyObjectDict:inGroup:isDirectChildGroup:] : 680 -> 724
~ -[DBGDataCoordinatorTargetHub _addNodeToMatchingRootLevelGroup:] : 184 -> 208
~ -[DBGDataCoordinatorTargetHub _createNodeWithDict:] : 192 -> 212
~ -[DBGDataCoordinatorTargetHub _updateGroup:withDict:] : 112 -> 116
~ -[DBGDataCoordinatorTargetHub _updateNode:withDict:] : 308 -> 332
~ __DBGDictionaryDescribesDebugHierarchyObjectReference : 72 -> 76
~ -[DBGDataCoordinatorTargetHub _updatePropertiesWithDicts:onNode:] : 416 -> 424
~ -[DBGDataCoordinatorTargetHub _updateProperty:withDict:] : 256 -> 272
~ -[DBGDataCoordinatorTargetHub _updateSubpropertiesWithDicts:onProperty:] : 380 -> 388
~ -[DBGDataCoordinatorTargetHub _updateSubHierarchyOfProperty:] : 344 -> 364
~ -[DBGDataCoordinatorTargetHub _updateComputedPropertiesOfNode:] : 260 -> 264
~ -[DBGDataCoordinatorTargetHub _writeRequestResponseToDiskIfNecessary:request:compressedSize:] : 788 -> 844
~ -[DBGDataCoordinatorTargetHub compatibility_modernizedPropertyDescription:targetVersion:] : 368 -> 384
~ _DebugHierarchySnapshotModelOSLog : 68 -> 84
~ -[DebugHierarchyRequest(DebugHierarchyTargetHub) lldbExpressionReturningNSDataOutError:] : 260 -> 280
~ -[DebugHierarchyRequest(DebugHierarchyTargetHub) lldbExpressionInPlaceOutError:] : 260 -> 280
~ +[DBGSnapshotNode nodeWithUniqueIdentifier] : 120 -> 128
~ -[DBGSnapshotNode displayName] : 156 -> 172
~ -[DBGSnapshotNode childGroup] : 8 -> 56
~ -[DBGSnapshotNode setChildGroup:] : 128 -> 144
~ -[DBGSnapshotNode addAdditonalGroup:] : 272 -> 292
~ -[DBGSnapshotNode groupWithID:] : 408 -> 428
~ -[DBGSnapshotNode allProperties] : 448 -> 484
~ -[DBGSnapshotNode hasPropertyWithName:] : 160 -> 176
~ -[DBGSnapshotNode propertyWithName:] : 200 -> 220
~ -[DBGSnapshotNode propertiesMatchingPredicate:] : 108 -> 116
~ -[DBGSnapshotNode addProperty:] : 132 -> 144
~ -[DBGSnapshotNode addProperties:] : 240 -> 244
~ -[DBGSnapshotNode valueForUndefinedKey:] : 76 -> 84
~ -[DBGSnapshotNode didUpdateProperty:] : 272 -> 276
~ -[DBGSnapshotNode addPropertyObserver:] : 156 -> 172
~ -[DBGSnapshotNode removePropertyObserver:] : 196 -> 208
~ -[DBGSnapshotNode debugDescription] : 240 -> 260
~ -[DBGSnapshotNode debugDescriptionWithIndentationDepth:prefix:includeProperties:] : 560 -> 596
~ -[DBGSnapshotNode _describeTreeWithRoot:depth:] : 480 -> 504
~ -[DBGSnapshotNode rootLevelGroup] : 100 -> 112
~ _DBGValueClassForPropertyWith : 1240 -> 1248
~ -[DBGCustomValue initWithCustomValue:] : 116 -> 108
~ -[DBGCustomValue description] : 148 -> 160
~ -[DBGClass initWithClassName:] : 116 -> 108
~ -[DBGClass description] : 76 -> 84
~ -[DBGClass debugDescription] : 148 -> 160
~ -[DBGObjectInfo initWithInfo:] : 116 -> 108
~ -[DBGObjectInfo displayString] : 180 -> 196
~ -[DBGObjectInfo objectClassName] : 84 -> 92
~ -[DBGObjectInfo objectPointer] : 84 -> 92
~ -[DBGObjectInfo description] : 76 -> 84
~ -[DBGObjectInfo debugDescription] : 148 -> 160
~ -[DBGObjectPointer initWithAddress:] : 116 -> 108
~ -[DBGObjectPointer description] : 76 -> 84
~ -[DBGObjectPointer debugDescription] : 148 -> 160
~ -[DBGEnumValue initWithCustomValue:] : 116 -> 108
~ -[DBGEnumValue integerValue] : 136 -> 148
~ -[DBGEnumValue setIntegerValue:] : 176 -> 188
~ -[DBGEnumValue unsignedIntegerValue] : 136 -> 148
~ -[DBGEnumValue setUnsignedIntegerValue:] : 176 -> 188
~ -[DBGEnumValue stringValue] : 124 -> 132
~ -[DBGEnumValue setStringValue:] : 156 -> 164
~ -[DBGEnumValue description] : 76 -> 84
~ -[DBGEnumValue debugDescription] : 148 -> 160
~ -[DBGData initWithData:] : 116 -> 108
~ -[DBGData description] : 76 -> 84
~ -[DBGData debugDescription] : 148 -> 160
~ -[DBGBool description] : 76 -> 84
~ -[DBGBool debugDescription] : 148 -> 160
~ -[DBGInt description] : 76 -> 84
~ -[DBGInt debugDescription] : 148 -> 160
~ -[DBGUnsignedInt description] : 76 -> 84
~ -[DBGUnsignedInt debugDescription] : 148 -> 160
~ -[DBGLong description] : 76 -> 84
~ -[DBGLong debugDescription] : 148 -> 160
~ -[DBGUnsignedLong description] : 76 -> 84
~ -[DBGUnsignedLong debugDescription] : 148 -> 160
~ -[DBGLongLong description] : 76 -> 84
~ -[DBGLongLong debugDescription] : 148 -> 160
~ -[DBGUnsignedLongLong description] : 76 -> 84
~ -[DBGUnsignedLongLong debugDescription] : 148 -> 160
~ -[DBGInteger description] : 76 -> 84
~ -[DBGInteger debugDescription] : 148 -> 160
~ -[DBGUnsignedInteger description] : 76 -> 84
~ -[DBGUnsignedInteger debugDescription] : 148 -> 160
~ -[DBGFloat description] : 76 -> 84
~ -[DBGFloat debugDescription] : 148 -> 160
~ -[DBGDouble description] : 76 -> 84
~ -[DBGDouble debugDescription] : 148 -> 160
~ -[DBGCGFloat description] : 76 -> 84
~ -[DBGCGFloat debugDescription] : 148 -> 160
~ -[DBGString initWithString:] : 116 -> 108
~ -[DBGString description] : 76 -> 84
~ -[DBGString debugDescription] : 148 -> 160
~ -[DBGAttributedString initWithAttributedString:] : 116 -> 108
~ -[DBGAttributedString description] : 76 -> 84
~ -[DBGAttributedString debugDescription] : 148 -> 160
~ +[DBGColor withCGColor:colorName:catalogName:] : 120 -> 116
~ -[DBGColor initWithCGColor:colorName:catalogName:] : 168 -> 160
~ +[DBGImage withImageData:type:metadata:] : 120 -> 116
~ -[DBGImage initWithImageData:type:metadata:] : 160 -> 152
~ -[DBGImage description] : 76 -> 84
~ -[DBGImage debugDescription] : 148 -> 160
~ -[DBGFont initWithDescription:] : 116 -> 108
~ -[DBGFont displayString] : 248 -> 272
~ -[DBGFont objectValue] : 168 -> 188
~ -[DBGFont description] : 76 -> 84
~ -[DBGFont debugDescription] : 148 -> 160
~ -[DBGPoint description] : 76 -> 84
~ -[DBGPoint debugDescription] : 148 -> 160
~ -[DBGSize description] : 76 -> 84
~ -[DBGSize debugDescription] : 148 -> 160
~ -[DBGRect description] : 76 -> 84
~ -[DBGRect debugDescription] : 148 -> 160
~ -[DBGOffset description] : 76 -> 84
~ -[DBGOffset debugDescription] : 148 -> 160
~ -[DBGInsets objectValue] : 288 -> 308
~ -[DBGInsets description] : 76 -> 84
~ -[DBGInsets debugDescription] : 148 -> 160
~ -[DBGVector2 objectValue] : 216 -> 228
~ -[DBGVector2 description] : 76 -> 84
~ -[DBGVector2 debugDescription] : 148 -> 160
~ -[DBGVector3 objectValue] : 272 -> 288
~ -[DBGVector3 description] : 76 -> 84
~ -[DBGVector3 debugDescription] : 148 -> 160
~ -[DBGVector4 objectValue] : 324 -> 344
~ -[DBGVector4 description] : 76 -> 84
~ -[DBGVector4 debugDescription] : 148 -> 160
~ -[DBGMatrix2 objectValue] : 304 -> 324
~ -[DBGMatrix2 description] : 76 -> 84
~ -[DBGMatrix2 debugDescription] : 148 -> 160
~ -[DBGMatrix3 objectValue] : 560 -> 600
~ -[DBGMatrix3 description] : 76 -> 84
~ -[DBGMatrix3 debugDescription] : 148 -> 160
~ -[DBGMatrix4 description] : 76 -> 84
~ -[DBGMatrix4 debugDescription] : 148 -> 160
~ -[DBGDataSourceConnectionDocument initWithDirectoryURL:] : 168 -> 176
~ -[DBGDataSourceConnectionDocument dateOrdererdContentsOfDirectory:] : 168 -> 184
~ ___67-[DBGDataSourceConnectionDocument dateOrdererdContentsOfDirectory:]_block_invoke : 304 -> 308
~ ___67-[DBGDataSourceConnectionDocument dateOrdererdContentsOfDirectory:]_block_invoke_2 : 200 -> 212
~ -[DBGDataSourceConnectionDocument dataForFetchAtIndex:] : 224 -> 252
~ -[DBGDataSourceConnectionDocument simulateInitialDataFetch] : 108 -> 116
~ -[DBGDataSourceConnectionDocument simulateSecondaryDataFetch] : 108 -> 116
~ -[DBGDataSourceConnectionDocument simulateTertiaryDataFetch] : 108 -> 116
~ -[DBGDataSourceConnectionDocument simulateTotalDataFetchForRequest:] : 208 -> 224
~ +[DBGSnapshotManager snapshotManagerWithSnapshot:primaryDataCoordinator:] : 112 -> 108
~ -[DBGSnapshotManager initWithSnapshot:primaryDataCoordinator:] : 232 -> 224
~ -[DBGSnapshotManager clearData] : 100 -> 108
~ -[DBGSnapshotManager cancelAllRequests] : 64 -> 68
~ -[DBGSnapshotManager setPrimaryDataCoordinator:] : 72 -> 76
~ +[RequestFactory initialRequestForPlatform:] : 204 -> 216
~ +[RequestFactory additionalRequestsWithSnapshot:] : 336 -> 360
~ +[RequestFactory requestForRemainingLazyPropertiesWithSnapshot:] : 240 -> 248
~ +[RequestFactory _requestForEncodedLayersWithSnapshot:] : 596 -> 632
~ +[RequestFactory _requestForRenderedEffectViewsWithSnapshot:] : 744 -> 764
~ +[RequestFactory _requestForRenderedMultiLayerViewsWithSnapshot:] : 604 -> 628
~ ___65+[RequestFactory _requestForRenderedMultiLayerViewsWithSnapshot:]_block_invoke : 84 -> 88
~ +[RequestFactory _requestForRenderedViewsWithSnapshot:] : 1248 -> 1320
~ +[RequestFactory _requestForRenderedSpriteKitTexturesWithSnapshot:] : 560 -> 572
~ +[RequestFactory _requestForEncodedSceneKitScenesWithSnapshot:] : 948 -> 980
~ +[RequestFactory _crossPlatformPropertyActions] : 400 -> 404
~ +[RequestFactory _propertyActionsForPlatform:] : 92 -> 96
~ +[RequestFactory _propertyActionsForiOS] : 652 -> 656
~ -[ViewHierarchyService initWithDataSourceConnection:runnablePid:] : 264 -> 272
~ -[ViewHierarchyService captureTo:completionBlock:] : 216 -> 208
~ ___50-[ViewHierarchyService captureTo:completionBlock:]_block_invoke : 264 -> 276
~ -[ViewHierarchyService _enqueueInitialRequest] : 248 -> 272
~ ___46-[ViewHierarchyService _enqueueInitialRequest]_block_invoke : 80 -> 84
~ -[ViewHierarchyService _enqueueAdditionalRequests] : 200 -> 216
~ ___50-[ViewHierarchyService _enqueueAdditionalRequests]_block_invoke : 264 -> 280
~ -[ViewHierarchyService _enqueueRemainingUnfetchedPropertyValuesRequest] : 232 -> 252
~ ___71-[ViewHierarchyService _enqueueRemainingUnfetchedPropertyValuesRequest]_block_invoke : 116 -> 120
~ -[ViewHierarchyService _requestFailed:] : 208 -> 216
~ -[ViewHierarchyService finishWithError:] : 140 -> 148
~ -[ViewHierarchyService _saveCompletedRequests] : 520 -> 540
~ ___46-[ViewHierarchyService _saveCompletedRequests]_block_invoke : 216 -> 224
~ -[ViewHierarchyService _metadata] : 348 -> 372
~ -[ViewHierarchyService setPlatform:] : 12 -> 64
~ -[DBGSnapshot init] : 176 -> 192
~ -[DBGSnapshot addRootLevelGroup:] : 396 -> 412
~ -[DBGSnapshot clearData] : 104 -> 108
~ -[DBGSnapshot nodesMatchingPredicate:] : 364 -> 376
~ -[DBGSnapshot nodesKindOfRuntimeClass:] : 392 -> 408
~ -[DBGSnapshot rootLevelSnapshotGroupWithIdentifier:] : 356 -> 360
~ -[DBGSnapshot rootLevelSnapshotGroups] : 72 -> 76
~ -[DBGSnapshot recursiveDescriptionIncludingProperties:] : 384 -> 396
~ -[DBGSnapshot _recursivelyDescribeGroup:withIndentation:isAdditonalGroup:includeProperties:] : 548 -> 576
~ -[DBGSnapshot _recursivelyDescribeNode:withIndentation:includeProperties:] : 580 -> 620
~ -[DBGLocalDataSourceConnection initWithPid:agentConnection:] : 204 -> 212
~ -[DBGLocalDataSourceConnection performRequest:] : 552 -> 576
~ ___47-[DBGLocalDataSourceConnection performRequest:]_block_invoke : 348 -> 368
~ ___47-[DBGLocalDataSourceConnection performRequest:]_block_invoke_2 : 160 -> 172
~ -[DBGLocalDataSourceConnection setCaptureQueue:] : 12 -> 64
~ +[DBGSnapshotProperty propertyWithName:runtimeTypeName:value:] : 136 -> 128
~ +[DBGSnapshotProperty propertyWithDebugHierarchyProperty:] : 164 -> 172
~ -[DBGSnapshotProperty allSubproperties] : 76 -> 84
~ -[DBGSnapshotProperty subpropertyWithName:] : 108 -> 116
~ -[DBGSnapshotProperty addSubproperty:] : 252 -> 280
~ -[DBGSnapshotProperty addSubproperties:] : 240 -> 244
~ -[DBGSnapshotProperty logicalTypeEquals:] : 120 -> 128
~ -[DBGSnapshotProperty logicalType] : 132 -> 144
~ -[DBGSnapshotProperty format] : 132 -> 144
~ -[DBGSnapshotProperty visibility] : 108 -> 112
~ -[DBGSnapshotProperty options] : 108 -> 112
~ -[DBGSnapshotProperty backingRuntimeTypeProperty] : 168 -> 188
~ -[DBGSnapshotProperty boolValue] : 136 -> 148
~ -[DBGSnapshotProperty setBoolValue:] : 160 -> 172
~ -[DBGSnapshotProperty integerValue] : 196 -> 212
~ -[DBGSnapshotProperty setIntegerValue:] : 304 -> 328
~ -[DBGSnapshotProperty CGFloatValue] : 144 -> 156
~ -[DBGSnapshotProperty setCGFloatValue:] : 168 -> 180
~ -[DBGSnapshotProperty pointValue] : 152 -> 164
~ -[DBGSnapshotProperty setPointValue:] : 176 -> 188
~ -[DBGSnapshotProperty sizeValue] : 152 -> 164
~ -[DBGSnapshotProperty setSizeValue:] : 176 -> 188
~ -[DBGSnapshotProperty rectValue] : 176 -> 188
~ -[DBGSnapshotProperty setRectValue:] : 200 -> 212
~ -[DBGSnapshotProperty floatValue] : 144 -> 156
~ -[DBGSnapshotProperty stringValue] : 156 -> 172
~ -[DBGSnapshotProperty dataValue] : 156 -> 172
~ -[DBGSnapshotProperty debugDescription] : 244 -> 264
~ -[DBGSnapshotProperty description] : 176 -> 192
~ -[DBGSnapshotProperty setBackingRuntimeTypeProperty:] : 20 -> 80
~ -[DBGSnapshotGroup initWithIdentifier:usingStrongChildNodeReferences:] : 164 -> 172
~ -[DBGSnapshotGroup addObject:] : 316 -> 352
~ -[DBGSnapshotGroup allObjects] : 76 -> 84
~ -[DBGSnapshotGroup displayName] : 132 -> 148
~ -[DBGSnapshotGroup debugDescription] : 140 -> 152
~ -[DBGSnapshotGroup rootLevelGroup] : 116 -> 124
~ -[DBGSnapshotProperty(JSONSerialization) updateWithJSONPropertyDescription:] : 724 -> 784
~ -[DBGSnapshotProperty(JSONSerialization) JSONPropertyDescription] : 596 -> 588
~ +[DBGCustomValue(JSONSerialization) valueWithEncodedValue:format:error:] : 180 -> 184
~ +[DBGClass(JSONSerialization) valueWithEncodedValue:format:error:] : 172 -> 176
~ +[DBGObjectInfo(JSONSerialization) valueWithEncodedValue:format:error:] : 172 -> 176
~ +[DBGObjectPointer(JSONSerialization) valueWithEncodedValue:format:error:] : 172 -> 176
~ +[DBGEnumValue(JSONSerialization) valueWithEncodedValue:format:error:] : 180 -> 184
~ +[DBGData(JSONSerialization) valueWithEncodedValue:format:error:] : 192 -> 200
~ -[DBGData(JSONSerialization) JSONCompatibleRepresentation] : 80 -> 88
~ +[DBGBool(JSONSerialization) valueWithEncodedValue:format:error:] : 220 -> 224
~ -[DBGBool(JSONSerialization) JSONCompatibleRepresentation] : 108 -> 116
~ +[DBGInt(JSONSerialization) valueWithEncodedValue:format:error:] : 220 -> 224
~ -[DBGInt(JSONSerialization) JSONCompatibleRepresentation] : 108 -> 116
~ +[DBGUnsignedInt(JSONSerialization) valueWithEncodedValue:format:error:] : 220 -> 224
~ -[DBGUnsignedInt(JSONSerialization) JSONCompatibleRepresentation] : 108 -> 116
~ +[DBGLong(JSONSerialization) valueWithEncodedValue:format:error:] : 220 -> 224
~ -[DBGLong(JSONSerialization) JSONCompatibleRepresentation] : 108 -> 116
~ +[DBGUnsignedLong(JSONSerialization) valueWithEncodedValue:format:error:] : 220 -> 224
~ -[DBGUnsignedLong(JSONSerialization) JSONCompatibleRepresentation] : 108 -> 116
~ +[DBGLongLong(JSONSerialization) valueWithEncodedValue:format:error:] : 220 -> 224
~ -[DBGLongLong(JSONSerialization) JSONCompatibleRepresentation] : 108 -> 116
~ +[DBGUnsignedLongLong(JSONSerialization) valueWithEncodedValue:format:error:] : 220 -> 224
~ -[DBGUnsignedLongLong(JSONSerialization) JSONCompatibleRepresentation] : 108 -> 116
~ +[DBGInteger(JSONSerialization) valueWithEncodedValue:format:error:] : 220 -> 224
~ -[DBGInteger(JSONSerialization) JSONCompatibleRepresentation] : 108 -> 116
~ +[DBGUnsignedInteger(JSONSerialization) valueWithEncodedValue:format:error:] : 220 -> 224
~ -[DBGUnsignedInteger(JSONSerialization) JSONCompatibleRepresentation] : 108 -> 116
~ +[DBGFloat(JSONSerialization) valueWithEncodedValue:format:error:] : 212 -> 216
~ -[DBGFloat(JSONSerialization) JSONCompatibleRepresentation] : 104 -> 112
~ +[DBGDouble(JSONSerialization) valueWithEncodedValue:format:error:] : 212 -> 216
~ -[DBGDouble(JSONSerialization) JSONCompatibleRepresentation] : 104 -> 112
~ +[DBGCGFloat(JSONSerialization) valueWithEncodedValue:format:error:] : 212 -> 216
~ -[DBGCGFloat(JSONSerialization) JSONCompatibleRepresentation] : 104 -> 112
~ +[DBGString(JSONSerialization) valueWithEncodedValue:format:error:] : 172 -> 176
~ +[DBGAttributedString(JSONSerialization) valueWithEncodedValue:format:error:] : 200 -> 204
~ +[DBGColor(JSONSerialization) valueWithEncodedValue:format:error:] : 632 -> 640
~ -[DBGColor(JSONSerialization) JSONCompatibleRepresentation] : 716 -> 692
~ +[DBGImage(JSONSerialization) valueWithEncodedValue:format:error:] : 608 -> 640
~ -[DBGFont(JSONSerialization) JSONCompatibleRepresentation] : 180 -> 188
~ +[DBGPoint(JSONSerialization) valueWithEncodedValue:format:error:] : 304 -> 296
~ +[DBGSize(JSONSerialization) valueWithEncodedValue:format:error:] : 304 -> 296
~ +[DBGRect(JSONSerialization) valueWithEncodedValue:format:error:] : 400 -> 392
~ +[DBGOffset(JSONSerialization) valueWithEncodedValue:format:error:] : 304 -> 296
~ +[DBGInsets(JSONSerialization) valueWithEncodedValue:format:error:] : 356 -> 376
~ -[DBGInsets(JSONSerialization) JSONCompatibleRepresentation] : 288 -> 308
~ +[DBGVector2(JSONSerialization) valueWithEncodedValue:format:error:] : 248 -> 260
~ -[DBGVector2(JSONSerialization) JSONCompatibleRepresentation] : 216 -> 228
~ +[DBGVector3(JSONSerialization) valueWithEncodedValue:format:error:] : 296 -> 304
~ -[DBGVector3(JSONSerialization) JSONCompatibleRepresentation] : 272 -> 288
~ +[DBGVector4(JSONSerialization) valueWithEncodedValue:format:error:] : 336 -> 356
~ -[DBGVector4(JSONSerialization) JSONCompatibleRepresentation] : 324 -> 344
~ +[DBGMatrix2(JSONSerialization) valueWithEncodedValue:format:error:] : 332 -> 352
~ -[DBGMatrix2(JSONSerialization) JSONCompatibleRepresentation] : 304 -> 324
~ +[DBGMatrix3(JSONSerialization) valueWithEncodedValue:format:error:] : 644 -> 684
~ -[DBGMatrix3(JSONSerialization) JSONCompatibleRepresentation] : 560 -> 600
~ +[DBGMatrix4(JSONSerialization) valueWithEncodedValue:format:error:] : 872 -> 940
~ -[DBGMatrix4(JSONSerialization) JSONCompatibleRepresentation] : 896 -> 964
~ -[DBGDataCoordinator initWithDataSourceConnection:] : 184 -> 192
~ -[DBGDataCoordinator performRequest:] : 620 -> 656
~ -[DBGDataCoordinator _performNextRequest] : 204 -> 220
~ -[DBGDataCoordinator cancelRequest:] : 220 -> 236
~ -[DBGDataCoordinator cancelAllRequests] : 300 -> 308
~ -[DBGDataCoordinator addSnapshotTransformer:] : 168 -> 180
~ -[DBGDataCoordinator snapshotTransformers] : 72 -> 76
~ -[DBGDataCoordinator didReceiveData:forRequest:] : 184 -> 196

```
