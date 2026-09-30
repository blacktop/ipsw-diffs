## DebugHierarchyFoundation

> `/System/Library/PrivateFrameworks/DebugHierarchyFoundation.framework/DebugHierarchyFoundation`

```diff

 73.0.0.0.0
-  __TEXT.__text: 0x134c4
-  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__text: 0x14384
+  __TEXT.__auth_stubs: 0x750
   __TEXT.__objc_methlist: 0x17c4
   __TEXT.__const: 0x88
   __TEXT.__cstring: 0x151c
-  __TEXT.__gcc_except_tab: 0x4f0
+  __TEXT.__gcc_except_tab: 0x4bc
   __TEXT.__oslogstring: 0x136
-  __TEXT.__unwind_info: 0x480
+  __TEXT.__unwind_info: 0x4d0
   __TEXT.__objc_classname: 0x470
   __TEXT.__objc_methname: 0x466f
   __TEXT.__objc_methtype: 0x6b3

   __DATA_CONST.__objc_selrefs: 0x10b0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x3e8
+  __AUTH_CONST.__auth_got: 0x3b8
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x1880
   __AUTH_CONST.__objc_const: 0x3e00

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 16140422-8AE6-33DB-9E0B-A51C6CB7E2C6
+  UUID: 49F4B442-EDE9-3AD3-B138-A0E3BC63F981
   Functions: 499
-  Symbols:   1576
+  Symbols:   1570
   CStrings:  1303
 
Symbols:
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
Functions:
~ -[DebugHierarchyProperty initWithPropertyDescription:] : 348 -> 384
~ -[DebugHierarchyProperty initWithName:runtimeTypeName:] : 160 -> 152
~ -[DebugHierarchyProperty dictionaryRepresentation] : 392 -> 376
~ -[DebugHierarchyProperty debugDescription] : 176 -> 192
~ _DBHIsInstanceOverridingNSObjectSelector : 120 -> 124
~ +[DebugHierarchyEntryPointProtocolHelper debugHierarchyGroupingIDsOnClass:] : 124 -> 132
~ +[DebugHierarchyEntryPointProtocolHelper debugHierarchyObjectsInGroupWithID:outOptions:onEntryPointClass:] : 228 -> 240
~ +[DebugHierarchyObjectProtocolHelper objectImplements_debugHierarchyVisibility:] : 88 -> 92
~ +[DebugHierarchyObjectProtocolHelper debugHierarchyVisibilityOfObject:] : 112 -> 116
~ +[DebugHierarchyObjectProtocolHelper debugHierarchyChildGroupingIDOfClass:] : 124 -> 132
~ +[DebugHierarchyObjectProtocolHelper debugHierarchyAdditionalGroupingIDsOfClass:] : 124 -> 132
~ +[DebugHierarchyObjectProtocolHelper debugHierarchyObjectsInGroupWithID:outOptions:vendingClass:onObject:] : 328 -> 348
~ +[DebugHierarchyObjectProtocolHelper debugHierarchyPropertyDescriptionsOfClass:] : 124 -> 132
~ +[DebugHierarchyObjectProtocolHelper debugHierarchyValueForPropertyWithName:onObject:vendingClass:outOptions:outError:] : 376 -> 384
~ +[DebugHierarchyObjectProtocolHelper childObjectsForObject:withType:outGroupingID:outOptions:] : 436 -> 448
~ +[DebugHierarchyObjectProtocolHelper enumerateAdditionalGroupsAndObjectsOfObject:withType:withBlock:] : 820 -> 848
~ +[DebugHierarchyObjectProtocolHelper v1_objectImplementsRequiredChildGroupMethods:] : 88 -> 92
~ +[DebugHierarchyObjectProtocolHelper v1_objectImplementsRequiredAdditionalGroupMethods:] : 88 -> 92
~ +[DebugHierarchyValueProtocolHelper objectImplementsRequiredDebugHierarchyValueMethods:] : 88 -> 92
~ +[DebugHierarchyValueProtocolHelper debugHierarchyValueWithOutOptions:outError:onObject:] : 280 -> 296
~ +[DebugHierarchyMetaDataProviderProtocolHelper debugHierarchyEnumDescriptionsOnClass:] : 124 -> 132
~ +[DebugHierarchyMetaDataProviderProtocolHelper debugHierarchyOptionDescriptionsOnClass:] : 124 -> 132
~ -[DebugHierarchyMetaDataAction keysToArchiveViaKVC] : 152 -> 156
~ -[DebugHierarchyMetaDataAction performInContext:] : 1052 -> 1112
~ -[DebugHierarchyMetaDataAction matchesEnumsForProviderClass:] : 144 -> 156
~ -[DebugHierarchyMetaDataAction matchesOptionsForProviderClass:] : 144 -> 156
~ +[DebugHierarchyRequestFailureReason failureReasonWithErrorMessage:] : 160 -> 172
~ +[DebugHierarchyRequestFailureReason _failureReasonWithReasonString:] : 328 -> 348
~ +[DebugHierarchyRequestFailureReason _wordStartingAtIndex:inString:] : 184 -> 200
~ +[DebugHierarchyRequestFailureReason _wordStartingAfterSubstring:inString:] : 152 -> 156
~ -[NSNumber(DBGNumberEncoding) dbgStringForType:error:] : 816 -> 836
~ _DebugHierarchyClassesConformingToProtocol : 268 -> 272
~ _DebugHierarchyEntryPointClasses : 172 -> 192
~ _DebugHierarchyMetaDataProviderClasses : 172 -> 192
~ -[DebugHierarchyAbstractRequestAction dictionaryRepresentation] : 284 -> 300
~ -[DebugHierarchyPropertyActionLegacyV1 performInContext:withObject:] : 960 -> 992
~ -[DebugHierarchyPropertyActionLegacyV1 _serializePropertyDescription:] : 456 -> 476
~ -[DebugHierarchyRequest initWithDictionary:] : 992 -> 1036
~ +[DebugHierarchyRequest requestWithDiscoveryType:actions:completion:] : 120 -> 116
~ +[DebugHierarchyRequest requestWithName:discoveryType:actions:completion:] : 156 -> 148
~ -[DebugHierarchyRequest initWithWithDiscoveryType:actions:completion:] : 208 -> 212
~ -[DebugHierarchyRequest isEqual:] : 148 -> 156
~ -[DebugHierarchyRequest cancel] : 140 -> 148
~ -[DebugHierarchyRequest dictionaryRepresentation] : 1200 -> 1288
~ -[DebugHierarchyRequest addLogEntry:] : 300 -> 316
~ -[DebugHierarchyRequest base64Encoded] : 108 -> 120
~ -[DebugHierarchyRequest humanReadableStatusMessage] : 200 -> 212
~ -[DebugHierarchyRequest debugDescription] : 120 -> 128
~ -[DebugHierarchyCrawlerOptions initWithDictionary:] : 348 -> 372
~ -[DebugHierarchyCrawlerOptions dictionaryRepresentation] : 468 -> 504
~ -[DebugHierarchyCrawlerOptions shouldCrawlGroupWithID:] : 172 -> 184
~ -[NSPointerArray(DBGAdditions) dbg_removeObject:] : 128 -> 132
~ -[DebugHierarchyRuntimeInfo initWithSerializedRepresentation:] : 316 -> 312
~ -[DebugHierarchyRuntimeInfo init] : 104 -> 108
~ -[DebugHierarchyRuntimeInfo addType:toParentType:] : 160 -> 168
~ -[DebugHierarchyRuntimeInfo typeWithName:] : 120 -> 128
~ -[DebugHierarchyRuntimeInfo typeOfObject:] : 172 -> 184
~ -[DebugHierarchyRuntimeInfo _reindexAllTypes] : 244 -> 248
~ -[DebugHierarchyRuntimeInfo _recursivelyIndexRuntimeType:] : 324 -> 336
~ -[DebugHierarchyRuntimeInfo serializedRepresentation] : 348 -> 360
~ -[DebugHierarchyRuntimeInfo _topLevelTypes] : 360 -> 376
~ -[DebugHierarchyRuntimeInfo mergeWith:] : 260 -> 264
~ -[DebugHierarchyRuntimeInfo _recursivelyMergeInRuntimeType:] : 436 -> 468
~ -[DebugHierarchyRuntimeInfo clearData] : 64 -> 68
~ -[DebugHierarchyRuntimeInfo debugDescription] : 504 -> 532
~ -[DebugHierarchyRuntimeInfo _describeTreeWithRoot:depth:description:] : 444 -> 460
~ -[DebugHierarchyRequestExecutionContext initWithRequest:] : 240 -> 256
~ -[DebugHierarchyRequestExecutionContext hasAlreadyFetchedDebugHierarchyObject:] : 140 -> 148
~ -[DebugHierarchyRequestExecutionContext addDebugHierarchyObject:withVisibility:fetchStatus:toGroupWithID:asDirectChild:belowParent:] : 612 -> 628
~ -[DebugHierarchyRequestExecutionContext addReferencedDebugHierarchyObject:withVisibility:toGroupWithID:asDirectChild:belowParent:] : 320 -> 324
~ -[DebugHierarchyRequestExecutionContext _addDebugHierarchyObject:withDict:toTopLevelGroupWithID:] : 1264 -> 1356
~ -[DebugHierarchyRequestExecutionContext _addDebugHierarchyObjectDict:toGroupWithID:asDirectChild:belowParent:] : 1316 -> 1400
~ -[DebugHierarchyRequestExecutionContext addProperties:toObject:] : 604 -> 628
~ -[DebugHierarchyRequestExecutionContext logRequestErrorWithTitle:message:fromMethod:] : 208 -> 216
~ -[DebugHierarchyRequestExecutionContext requestResponse] : 456 -> 492
~ -[DebugHierarchyRequestExecutionContext recursiveDescription] : 192 -> 204
~ -[DebugHierarchyRequestExecutionContext globalRuntimeInfo] : 84 -> 92
~ -[DebugHierarchyRequestExecutionContext runtimeTypeWithName:] : 148 -> 164
~ -[DebugHierarchyRequestExecutionContext _collectRuntimeInformationForObjectType:] : 1016 -> 1064
~ -[DebugHierarchyRequestExecutionContext setRequest:] : 12 -> 64
~ -[DebugHierarchyRequestExecutionContext setTopLevelGroups:] : 12 -> 64
~ -[DebugHierarchyRequestExecutionContext setTopLevelPropertyDescriptions:] : 12 -> 64
~ -[DebugHierarchyRequestExecutionContext setIdentifierToObjectDescriptionMap:] : 12 -> 64
~ -[DebugHierarchyRequestExecutionContext setContextRuntimeInfo:] : 12 -> 64
~ -[DebugHierarchyRequestExecutionContext setMetaData:] : 12 -> 64
~ +[DebugHierarchyCrawler crawlerWithRequestContext:knownObjectsMap:] : 112 -> 108
~ -[DebugHierarchyCrawler initWithRequestContext:knownObjectsMap:] : 152 -> 144
~ -[DebugHierarchyCrawler crawlEntryPointClasses] : 792 -> 820
~ -[DebugHierarchyCrawler options] : 100 -> 112
~ -[DebugHierarchyCrawler enumerateDebugHierarchyObjects:inGroupWithID:options:asDirectChildren:belowParent:] : 416 -> 424
~ -[DebugHierarchyCrawler crawlDebugHierarchyObject:inGroupWithID:asDirectChild:belowParent:withParentDefinedVisibility:] : 816 -> 844
~ -[DebugHierarchyCrawler _entryPointClasses] : 352 -> 360
~ -[DebugHierarchyCrawler setKnownObjectsMap:] : 12 -> 64
~ -[DebugHierarchyCrawler setRequestContext:] : 12 -> 64
~ -[DebugHierarchyRequestExecutor initWithRequest:] : 156 -> 164
~ -[DebugHierarchyRequestExecutor runWithError:] : 2392 -> 2524
~ -[DebugHierarchyRequestExecutor _v1CompatibleRequestResponseFromResponse:] : 596 -> 620
~ ___74-[DebugHierarchyRequestExecutor _v1CompatibleRequestResponseFromResponse:]_block_invoke_2 : 244 -> 256
~ -[DebugHierarchyRequestExecutor _v1RecursivelyMakePropertyDescriptionCompatibleWithGroup:] : 1148 -> 1200
~ ___90-[DebugHierarchyRequestExecutor _v1RecursivelyMakePropertyDescriptionCompatibleWithGroup:]_block_invoke : 456 -> 484
~ -[DebugHierarchyRequestExecutor _v1MakePropertyDescriptionCompatible:withRuntimeType:] : 744 -> 808
~ -[DebugHierarchyRequestExecutor _executeRequestActionsWithCrawler] : 204 -> 224
~ -[DebugHierarchyRequestExecutor _executeRequestActionsWithKnownObjects] : 596 -> 632
~ -[DebugHierarchyRequestExecutor _performanceMetricsDictionaryRequestActionDuration:] : 176 -> 184
~ -[DebugHierarchyRequestExecutor setActionExecutor:] : 12 -> 64
~ -[DebugHierarchyRequestExecutor setRequestContext:] : 12 -> 64
~ _DebugHierarchyRequestsOSLog : 68 -> 84
~ _DebugHierarchyResponseDataForException : 192 -> 204
~ _DebugHierarchyResponseDataForGenericError : 500 -> 520
~ +[NSError(DebugHierarchyAdditions) debugHierarchyErrorFromException:caughtDuringRequest:forMethodSignature:] : 384 -> 404
~ -[NSError(DebugHierarchyAdditions) debugHierarchyResponseDataForRequest:] : 140 -> 152
~ -[DebugHierarchyPropertyAction addPropertyNames:] : 128 -> 136
~ -[DebugHierarchyPropertyAction keysToArchiveViaKVC] : 224 -> 228
~ -[DebugHierarchyPropertyAction performInContext:withObject:] : 808 -> 852
~ -[DebugHierarchyPropertyAction targetsObjectIdentifiers:] : 120 -> 128
~ -[DebugHierarchyPropertyAction isTargetingObject:] : 1020 -> 1044
~ -[DebugHierarchyPropertyAction _isTargetingProperty:] : 256 -> 272
~ -[DebugHierarchyPropertyAction _fetchValuesForPropertiesWithNames:onObject:inContext:] : 544 -> 548
~ -[DebugHierarchyPropertyAction debugDescription] : 216 -> 236
~ +[NSDictionary(DBGAdditions) dictionaryWithJSONData:error:] : 488 -> 492
~ -[NSDictionary(DBGAdditions) generateJSONDataWithError:] : 400 -> 404
~ -[NSDictionary(DBGAdditions) generateJSONStringWithError:] : 364 -> 360
~ _DebugHierarchyJSONProcessingOSLog : 68 -> 84
~ _DebugHierarchyRequestActionForDictionary : 92 -> 100
~ +[DebugHierarchyObjectInterface valueAndOptionsForProperty:onObject:inContext:] : 808 -> 836
~ +[DebugHierarchyObjectInterface valueForProperty:withOutOptions:onObject:inContext:error:] : 1912 -> 1948
~ +[DebugHierarchyObjectInterface propertyDescriptionsForClass:inContext:] : 328 -> 340
~ -[DebugHierarchyRuntimeType initWithDictionaryRepresentation:] : 640 -> 660
~ -[DebugHierarchyRuntimeType initWithName:] : 116 -> 108
~ -[DebugHierarchyRuntimeType addSubtype:] : 180 -> 196
~ -[DebugHierarchyRuntimeType isKindOfTypeWithName:] : 144 -> 148
~ -[DebugHierarchyRuntimeType propertyWithName:] : 164 -> 172
~ -[DebugHierarchyRuntimeType namesOfInheritanceChain] : 164 -> 176
~ -[DebugHierarchyRuntimeType closestTypeVendingAChildGroupingID] : 132 -> 148
~ -[DebugHierarchyRuntimeType instanceProperties] : 88 -> 100
~ -[DebugHierarchyRuntimeType addInstanceProperty:] : 124 -> 132
~ -[DebugHierarchyRuntimeType sourceLanguage] : 120 -> 128
~ -[DebugHierarchyRuntimeType dictionaryRepresentation] : 912 -> 976
~ -[DebugHierarchyRuntimeType isEqual:] : 292 -> 312
~ -[DebugHierarchyRuntimeType debugDescription] : 180 -> 196
~ -[DebugHierarchyRequest(Utilities) formattedResponseDataForRawRequestResultData:] : 164 -> 160
~ +[DebugHierarchyRequest(TargetHubAdditions) requestWithBase64Data:error:] : 376 -> 384
~ +[DebugHierarchyRequest(TargetHubAdditions) _compatibleRequestWithDictionary:] : 164 -> 180
~ +[DebugHierarchyRequest(TargetHubAdditions) _requestWithV1RequestDictionary:] : 608 -> 648
~ ___77+[DebugHierarchyRequest(TargetHubAdditions) _requestWithV1RequestDictionary:]_block_invoke : 480 -> 488
~ -[DebugHierarchyRunLoopAction performInContext:] : 112 -> 120
~ -[DebugHierarchyRequestActionExecutor initWithContext:] : 116 -> 108
~ -[DebugHierarchyRequestActionExecutor initialActions] : 164 -> 184
~ -[DebugHierarchyRequestActionExecutor finalActions] : 164 -> 184
~ -[DebugHierarchyRequestActionExecutor objectActions] : 164 -> 184
~ +[DebugHierarchyRequestActionExecutor initialActionsFromActions:] : 204 -> 216
~ +[DebugHierarchyRequestActionExecutor finalActionsFromActions:] : 248 -> 256
~ +[DebugHierarchyRequestActionExecutor objectTargetedActionsFromActions:] : 336 -> 340
~ -[DebugHierarchyRequestActionExecutor executeInitialStandaloneActions] : 116 -> 124
~ -[DebugHierarchyRequestActionExecutor executeFinalStandaloneActions] : 116 -> 124
~ -[DebugHierarchyRequestActionExecutor executeActionsWithObject:] : 144 -> 152
~ +[DebugHierarchyRequestActionExecutor _executeStandaloneActions:inContext:] : 256 -> 252
~ +[DebugHierarchyRequestActionExecutor _executeObjectActions:withObject:inContext:] : 284 -> 276
~ -[DebugHierarchyRequestActionExecutor allObjectActionsTargetIdentifiers:] : 372 -> 376
~ -[NSData(Gzip) dbg_gzipInflateIfCompressed] : 76 -> 88
~ -[NSData(Gzip) dbg_gzipInflate] : 260 -> 264
~ -[NSData(Gzip) dbg_gzipInflateWithWindowBits:] : 920 -> 924
~ -[NSData(Gzip) dbg_gzipDeflate] : 268 -> 272
~ _DebugHierarchyGzipOSLog : 68 -> 84
~ +[DebugHierarchyLogEntry errorLogEntryWithTitle:message:methodSignature:environmentInfo:] : 164 -> 152
~ +[DebugHierarchyLogEntry warningLogEntryWithTitle:message:methodSignature:environmentInfo:] : 164 -> 152
~ +[DebugHierarchyLogEntry errorLogEntryWithTitle:message:methodSignature:] : 140 -> 132
~ +[DebugHierarchyLogEntry warningLogEntryWithTitle:message:methodSignature:] : 140 -> 132
~ +[DebugHierarchyLogEntry formattedSummaryOfLogs:] : 356 -> 372
~ -[DebugHierarchyLogEntry initWithSeverity:title:message:methodSignature:environmentInfo:] : 260 -> 248
~ -[DebugHierarchyLogEntry initWithDictionary:] : 356 -> 384
~ -[DebugHierarchyLogEntry dictionaryRepresentation] : 548 -> 596
~ -[DebugHierarchyLogEntry formattedSummary] : 164 -> 180
~ +[DBGTargetHub sharedHub] : 160 -> 176
~ -[DBGTargetHub performRequest:] : 112 -> 120
~ -[DBGTargetHub performRequestWithRequestInBase64:] : 112 -> 120
~ -[DBGTargetHub clearAllRequestsAndData] : 72 -> 76
~ +[DebugHierarchyTargetHub sharedHub] : 160 -> 176
~ -[DebugHierarchyTargetHub init] : 156 -> 160
~ -[DebugHierarchyTargetHub knownObjectsMap] : 88 -> 100
~ -[DebugHierarchyTargetHub additionalKnownObjects] : 84 -> 92
~ -[DebugHierarchyTargetHub runtimeInfo] : 84 -> 92
~ -[DebugHierarchyTargetHub performRequestWithRequestInBase64:] : 272 -> 284
~ -[DebugHierarchyTargetHub performRequest:error:] : 716 -> 704
~ ___48-[DebugHierarchyTargetHub performRequest:error:]_block_invoke : 132 -> 136
~ -[DebugHierarchyTargetHub performRequestInPlaceWithRequestInBase64:] : 56 -> 60
~ -[DebugHierarchyTargetHub performRequestAndWriteResponseToFileDescriptorWithRequestInBase64:fileDescriptor:] : 164 -> 176
~ -[DebugHierarchyTargetHub registerForDarwinNotifications] : 216 -> 220
~ -[DebugHierarchyTargetHub openXPCConnection] : 324 -> 312
~ ___44-[DebugHierarchyTargetHub openXPCConnection]_block_invoke_2 : 212 -> 224
~ -[DebugHierarchyTargetHub handleXPCEvent:] : 292 -> 296
~ -[DebugHierarchyTargetHub setCurrentRequest:responseFileDescriptor:reply:] : 120 -> 124
~ +[DebugHierarchyTargetHub performDebugRequest:] : 320 -> 336
~ -[DebugHierarchyTargetHub setAdditionalKnownObjects:] : 12 -> 64
~ -[DebugHierarchyTargetHub setCurrentRequestInBase64:] : 12 -> 64
~ -[DebugHierarchyTargetHub setCurrentReply:] : 12 -> 64
~ __DBGViewHierarchyInitialize : 72 -> 76
~ _DebugHierarchyRequestsOSLog : 68 -> 84
~ +[DebugHierarchyResetAction resetRequest] : 220 -> 228
~ -[DebugHierarchyResetAction performInContext:] : 72 -> 76
~ __DBGStructureOfDictionaryDescriptionWithFormat : 676 -> 696
~ +[DebugHierarchyFormatSpecifier specifierWithFormat:label:] : 112 -> 108
~ -[DebugHierarchyFormatSpecifier initWithFormat:label:] : 152 -> 144
~ _DBGClearCachedFormatSpecifiers : 64 -> 68
~ _DBGCachedFormatSpecifiers : 68 -> 84
~ _DBGSpecifiersFromFormatString : 976 -> 1040
~ _DBGEncodeDictionaryAsJSONCompatibleDictionary : 276 -> 268
~ ___DBGEncodeDictionaryAsJSONCompatibleDictionary_block_invoke : 280 -> 296
~ _DBGEncodeValueAsJSONCompatibleValue : 1340 -> 1416
~ _DBGDecodeDictionaryFromJSONCompatibleDictionary : 276 -> 268
~ ___DBGDecodeDictionaryFromJSONCompatibleDictionary_block_invoke : 280 -> 296
~ _DBGDecodeValueFromJSONCompatibleValue : 2212 -> 2416
~ _DBGSerializePropertyDescriptionAsJSON : 584 -> 612
~ _DBGSerializePropertyDescriptionsAsJSON : 420 -> 428
~ _DBGDeserializePropertyDictionaryFromJSON : 288 -> 300
~ _DBGDeserializePropertyDictionariesFromJSON : 420 -> 428
~ ___DBGCachedFormatSpecifiers_block_invoke : 64 -> 68

```
