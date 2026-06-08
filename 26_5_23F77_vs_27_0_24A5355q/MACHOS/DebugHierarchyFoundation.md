## DebugHierarchyFoundation

> `/System/Library/PrivateFrameworks/DebugHierarchyFoundation.framework/DebugHierarchyFoundation`

```diff

-73.0.0.0.0
-  __TEXT.__text: 0x14384
-  __TEXT.__auth_stubs: 0x750
+74.0.0.0.0
+  __TEXT.__text: 0x13478
   __TEXT.__objc_methlist: 0x17c4
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x151c
-  __TEXT.__gcc_except_tab: 0x4bc
+  __TEXT.__cstring: 0x1542
+  __TEXT.__gcc_except_tab: 0x4c4
   __TEXT.__oslogstring: 0x136
-  __TEXT.__unwind_info: 0x4d0
-  __TEXT.__objc_classname: 0x470
+  __TEXT.__unwind_info: 0x480
+  __TEXT.__objc_stubs: 0x34e0
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__objc_classname: 0x449
   __TEXT.__objc_methname: 0x466f
   __TEXT.__objc_methtype: 0x6b3
-  __TEXT.__objc_stubs: 0x34e0
-  __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__const: 0x348
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x38

   __DATA_CONST.__objc_selrefs: 0x10b0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x3b8
+  __DATA_CONST.__got: 0x1c8
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x1880
   __AUTH_CONST.__objc_const: 0x3e00
   __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__auth_got: 0x3e8
   __AUTH.__objc_data: 0x7d0
   __DATA.__objc_ivar: 0x17c
   __DATA.__data: 0x328

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 6102BEFA-7C3F-3495-BDC2-FE8922AF4377
+  UUID: D73B5D85-224C-3988-954C-6842CD7ED0B5
   Functions: 499
-  Symbols:   1570
+  Symbols:   1576
   CStrings:  1303
 
Symbols:
+ __block_literal_global.137
+ __block_literal_global.148
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
- __block_literal_global.138
- __block_literal_global.149
Functions:
~ -[DebugHierarchyProperty initWithPropertyDescription:] : 384 -> 348
~ -[DebugHierarchyProperty initWithName:runtimeTypeName:] : 152 -> 160
~ -[DebugHierarchyProperty dictionaryRepresentation] : 376 -> 392
~ -[DebugHierarchyProperty debugDescription] : 192 -> 176
~ _DBHIsInstanceOverridingNSObjectSelector : 124 -> 120
~ +[DebugHierarchyEntryPointProtocolHelper debugHierarchyGroupingIDsOnClass:] : 132 -> 124
~ +[DebugHierarchyEntryPointProtocolHelper debugHierarchyObjectsInGroupWithID:outOptions:onEntryPointClass:] : 240 -> 228
~ +[DebugHierarchyObjectProtocolHelper objectImplements_debugHierarchyVisibility:] : 92 -> 88
~ +[DebugHierarchyObjectProtocolHelper debugHierarchyVisibilityOfObject:] : 116 -> 112
~ +[DebugHierarchyObjectProtocolHelper debugHierarchyChildGroupingIDOfClass:] : 132 -> 124
~ +[DebugHierarchyObjectProtocolHelper debugHierarchyAdditionalGroupingIDsOfClass:] : 132 -> 124
~ +[DebugHierarchyObjectProtocolHelper debugHierarchyObjectsInGroupWithID:outOptions:vendingClass:onObject:] : 348 -> 328
~ +[DebugHierarchyObjectProtocolHelper debugHierarchyPropertyDescriptionsOfClass:] : 132 -> 124
~ +[DebugHierarchyObjectProtocolHelper debugHierarchyValueForPropertyWithName:onObject:vendingClass:outOptions:outError:] : 384 -> 376
~ +[DebugHierarchyObjectProtocolHelper childObjectsForObject:withType:outGroupingID:outOptions:] : 448 -> 436
~ +[DebugHierarchyObjectProtocolHelper enumerateAdditionalGroupsAndObjectsOfObject:withType:withBlock:] : 848 -> 828
~ +[DebugHierarchyObjectProtocolHelper v1_objectImplementsRequiredChildGroupMethods:] : 92 -> 88
~ +[DebugHierarchyObjectProtocolHelper v1_objectImplementsRequiredAdditionalGroupMethods:] : 92 -> 88
~ +[DebugHierarchyValueProtocolHelper objectImplementsRequiredDebugHierarchyValueMethods:] : 92 -> 88
~ +[DebugHierarchyValueProtocolHelper debugHierarchyValueWithOutOptions:outError:onObject:] : 296 -> 280
~ +[DebugHierarchyMetaDataProviderProtocolHelper debugHierarchyEnumDescriptionsOnClass:] : 132 -> 124
~ +[DebugHierarchyMetaDataProviderProtocolHelper debugHierarchyOptionDescriptionsOnClass:] : 132 -> 124
~ -[DebugHierarchyMetaDataAction keysToArchiveViaKVC] : 156 -> 152
~ -[DebugHierarchyMetaDataAction performInContext:] : 1112 -> 1056
~ -[DebugHierarchyMetaDataAction matchesEnumsForProviderClass:] : 156 -> 144
~ -[DebugHierarchyMetaDataAction matchesOptionsForProviderClass:] : 156 -> 144
~ -[DebugHierarchyMetaDataAction metaDataProviderClassesForEnumsAreExclusive] : 20 -> 24
~ -[DebugHierarchyMetaDataAction setMetaDataProviderClassesForEnumsAreExclusive:] : 16 -> 20
~ -[DebugHierarchyMetaDataAction metaDataProviderClassesForOptionsAreExclusive] : 20 -> 24
~ -[DebugHierarchyMetaDataAction setMetaDataProviderClassesForOptionsAreExclusive:] : 16 -> 20
~ +[DebugHierarchyRequestFailureReason failureReasonWithErrorMessage:] : 172 -> 160
~ +[DebugHierarchyRequestFailureReason _failureReasonWithReasonString:] : 348 -> 328
~ +[DebugHierarchyRequestFailureReason _wordStartingAtIndex:inString:] : 200 -> 184
~ +[DebugHierarchyRequestFailureReason _wordStartingAfterSubstring:inString:] : 156 -> 152
~ -[NSNumber(DBGNumberEncoding) dbgStringForType:error:] : 836 -> 816
~ _DebugHierarchyClassesConformingToProtocol : 272 -> 268
~ _DebugHierarchyEntryPointClasses : 192 -> 172
~ _DebugHierarchyMetaDataProviderClasses : 192 -> 172
~ -[DebugHierarchyAbstractRequestAction dictionaryRepresentation] : 300 -> 284
~ -[DebugHierarchyPropertyActionLegacyV1 performInContext:withObject:] : 992 -> 964
~ -[DebugHierarchyPropertyActionLegacyV1 _serializePropertyDescription:] : 476 -> 456
~ -[DebugHierarchyRequest initWithDictionary:] : 1036 -> 1000
~ +[DebugHierarchyRequest requestWithDiscoveryType:actions:completion:] : 116 -> 120
~ +[DebugHierarchyRequest requestWithName:discoveryType:actions:completion:] : 148 -> 156
~ -[DebugHierarchyRequest initWithWithDiscoveryType:actions:completion:] : 212 -> 208
~ -[DebugHierarchyRequest isEqual:] : 156 -> 148
~ -[DebugHierarchyRequest cancel] : 148 -> 140
~ -[DebugHierarchyRequest dictionaryRepresentation] : 1288 -> 1208
~ -[DebugHierarchyRequest addLogEntry:] : 316 -> 300
~ -[DebugHierarchyRequest base64Encoded] : 120 -> 108
~ -[DebugHierarchyRequest humanReadableStatusMessage] : 212 -> 200
~ -[DebugHierarchyRequest debugDescription] : 128 -> 120
~ -[DebugHierarchyCrawlerOptions initWithDictionary:] : 372 -> 348
~ -[DebugHierarchyCrawlerOptions dictionaryRepresentation] : 504 -> 468
~ -[DebugHierarchyCrawlerOptions shouldCrawlGroupWithID:] : 184 -> 172
~ -[NSPointerArray(DBGAdditions) dbg_removeObject:] : 132 -> 128
~ -[NSPointerArray(DBGAdditions) dbg_indexOfObjectIdenticalTo:] : 284 -> 288
~ -[DebugHierarchyRuntimeInfo initWithSerializedRepresentation:] : 312 -> 320
~ -[DebugHierarchyRuntimeInfo init] : 108 -> 104
~ -[DebugHierarchyRuntimeInfo addType:toParentType:] : 168 -> 160
~ -[DebugHierarchyRuntimeInfo typeWithName:] : 128 -> 120
~ -[DebugHierarchyRuntimeInfo typeOfObject:] : 184 -> 172
~ -[DebugHierarchyRuntimeInfo _recursivelyIndexRuntimeType:] : 336 -> 328
~ -[DebugHierarchyRuntimeInfo serializedRepresentation] : 360 -> 352
~ -[DebugHierarchyRuntimeInfo _topLevelTypes] : 376 -> 364
~ -[DebugHierarchyRuntimeInfo _recursivelyMergeInRuntimeType:] : 468 -> 440
~ -[DebugHierarchyRuntimeInfo clearData] : 68 -> 64
~ -[DebugHierarchyRuntimeInfo debugDescription] : 532 -> 508
~ -[DebugHierarchyRuntimeInfo _describeTreeWithRoot:depth:description:] : 460 -> 448
~ -[DebugHierarchyRequestExecutionContext initWithRequest:] : 256 -> 240
~ -[DebugHierarchyRequestExecutionContext hasAlreadyFetchedDebugHierarchyObject:] : 148 -> 140
~ -[DebugHierarchyRequestExecutionContext addDebugHierarchyObject:withVisibility:fetchStatus:toGroupWithID:asDirectChild:belowParent:] : 628 -> 612
~ -[DebugHierarchyRequestExecutionContext addReferencedDebugHierarchyObject:withVisibility:toGroupWithID:asDirectChild:belowParent:] : 324 -> 320
~ -[DebugHierarchyRequestExecutionContext _addDebugHierarchyObject:withDict:toTopLevelGroupWithID:] : 1356 -> 1264
~ -[DebugHierarchyRequestExecutionContext _addDebugHierarchyObjectDict:toGroupWithID:asDirectChild:belowParent:] : 1400 -> 1320
~ -[DebugHierarchyRequestExecutionContext addProperties:toObject:] : 628 -> 608
~ -[DebugHierarchyRequestExecutionContext logRequestErrorWithTitle:message:fromMethod:] : 216 -> 208
~ -[DebugHierarchyRequestExecutionContext requestResponse] : 492 -> 456
~ -[DebugHierarchyRequestExecutionContext recursiveDescription] : 204 -> 192
~ -[DebugHierarchyRequestExecutionContext globalRuntimeInfo] : 92 -> 84
~ -[DebugHierarchyRequestExecutionContext runtimeTypeWithName:] : 164 -> 148
~ -[DebugHierarchyRequestExecutionContext _collectRuntimeInformationForObjectType:] : 1064 -> 1016
~ -[DebugHierarchyRequestExecutionContext setRequest:] : 64 -> 12
~ -[DebugHierarchyRequestExecutionContext setTopLevelGroups:] : 64 -> 12
~ -[DebugHierarchyRequestExecutionContext setTopLevelPropertyDescriptions:] : 64 -> 12
~ -[DebugHierarchyRequestExecutionContext setIdentifierToObjectDescriptionMap:] : 64 -> 12
~ -[DebugHierarchyRequestExecutionContext setContextRuntimeInfo:] : 64 -> 12
~ -[DebugHierarchyRequestExecutionContext setMetaData:] : 64 -> 12
~ +[DebugHierarchyCrawler crawlerWithRequestContext:knownObjectsMap:] : 108 -> 112
~ -[DebugHierarchyCrawler initWithRequestContext:knownObjectsMap:] : 144 -> 152
~ -[DebugHierarchyCrawler crawlEntryPointClasses] : 820 -> 796
~ -[DebugHierarchyCrawler options] : 112 -> 100
~ -[DebugHierarchyCrawler enumerateDebugHierarchyObjects:inGroupWithID:options:asDirectChildren:belowParent:] : 424 -> 416
~ -[DebugHierarchyCrawler crawlDebugHierarchyObject:inGroupWithID:asDirectChild:belowParent:withParentDefinedVisibility:] : 844 -> 816
~ -[DebugHierarchyCrawler _entryPointClasses] : 360 -> 356
~ -[DebugHierarchyCrawler setKnownObjectsMap:] : 64 -> 12
~ -[DebugHierarchyCrawler setRequestContext:] : 64 -> 12
~ -[DebugHierarchyRequestExecutor initWithRequest:] : 164 -> 156
~ -[DebugHierarchyRequestExecutor runWithError:] : 2524 -> 2392
~ -[DebugHierarchyRequestExecutor _v1CompatibleRequestResponseFromResponse:] : 620 -> 596
~ ___74-[DebugHierarchyRequestExecutor _v1CompatibleRequestResponseFromResponse:]_block_invoke_2 : 256 -> 244
~ -[DebugHierarchyRequestExecutor _v1RecursivelyMakePropertyDescriptionCompatibleWithGroup:] : 1200 -> 1152
~ ___90-[DebugHierarchyRequestExecutor _v1RecursivelyMakePropertyDescriptionCompatibleWithGroup:]_block_invoke : 484 -> 456
~ -[DebugHierarchyRequestExecutor _v1MakePropertyDescriptionCompatible:withRuntimeType:] : 808 -> 744
~ -[DebugHierarchyRequestExecutor _executeRequestActionsWithCrawler] : 224 -> 204
~ -[DebugHierarchyRequestExecutor _executeRequestActionsWithKnownObjects] : 632 -> 604
~ -[DebugHierarchyRequestExecutor _performanceMetricsDictionaryRequestActionDuration:] : 184 -> 176
~ -[DebugHierarchyRequestExecutor setActionExecutor:] : 64 -> 12
~ -[DebugHierarchyRequestExecutor setRequestContext:] : 64 -> 12
~ _DebugHierarchyRequestsOSLog : 84 -> 68
~ _DebugHierarchyResponseDataForException : 204 -> 192
~ _DebugHierarchyResponseDataForGenericError : 520 -> 500
~ +[NSError(DebugHierarchyAdditions) debugHierarchyErrorFromException:caughtDuringRequest:forMethodSignature:] : 404 -> 384
~ -[NSError(DebugHierarchyAdditions) debugHierarchyResponseDataForRequest:] : 152 -> 140
~ -[DebugHierarchyPropertyAction init] : 88 -> 96
~ -[DebugHierarchyPropertyAction addPropertyNames:] : 136 -> 128
~ -[DebugHierarchyPropertyAction keysToArchiveViaKVC] : 228 -> 224
~ -[DebugHierarchyPropertyAction performInContext:withObject:] : 852 -> 812
~ -[DebugHierarchyPropertyAction targetsObjectIdentifiers:] : 128 -> 120
~ -[DebugHierarchyPropertyAction isTargetingObject:] : 1044 -> 1028
~ -[DebugHierarchyPropertyAction _isTargetingProperty:] : 272 -> 256
~ -[DebugHierarchyPropertyAction debugDescription] : 236 -> 216
~ -[DebugHierarchyPropertyAction objectIdentifiersAreExclusive] : 20 -> 24
~ -[DebugHierarchyPropertyAction setObjectIdentifiersAreExclusive:] : 16 -> 20
~ -[DebugHierarchyPropertyAction propertyNamesAreExclusive] : 20 -> 24
~ -[DebugHierarchyPropertyAction setPropertyNamesAreExclusive:] : 16 -> 20
~ -[DebugHierarchyPropertyAction typesAreExclusive] : 20 -> 24
~ -[DebugHierarchyPropertyAction setTypesAreExclusive:] : 16 -> 20
~ -[DebugHierarchyPropertyAction exactTypesAreExclusive] : 20 -> 24
~ -[DebugHierarchyPropertyAction setExactTypesAreExclusive:] : 16 -> 20
~ -[DebugHierarchyPropertyAction visibility] : 16 -> 20
~ -[DebugHierarchyPropertyAction setVisibility:] : 16 -> 20
~ -[DebugHierarchyPropertyAction options] : 16 -> 20
~ -[DebugHierarchyPropertyAction setOptions:] : 16 -> 20
~ -[DebugHierarchyPropertyAction optionsComparisonStyle] : 16 -> 20
~ -[DebugHierarchyPropertyAction setOptionsComparisonStyle:] : 16 -> 20
~ +[NSDictionary(DBGAdditions) dictionaryWithJSONData:error:] : 492 -> 444
~ -[NSDictionary(DBGAdditions) generateJSONDataWithError:] : 404 -> 356
~ -[NSDictionary(DBGAdditions) generateJSONStringWithError:] : 360 -> 364
~ _DebugHierarchyJSONProcessingOSLog : 84 -> 68
~ _DebugHierarchyRequestActionForDictionary : 100 -> 92
~ +[DebugHierarchyObjectInterface valueAndOptionsForProperty:onObject:inContext:] : 836 -> 808
~ +[DebugHierarchyObjectInterface valueForProperty:withOutOptions:onObject:inContext:error:] : 1948 -> 1896
~ +[DebugHierarchyObjectInterface propertyDescriptionsForClass:inContext:] : 340 -> 328
~ -[DebugHierarchyRuntimeType initWithDictionaryRepresentation:] : 660 -> 648
~ -[DebugHierarchyRuntimeType initWithName:] : 108 -> 116
~ -[DebugHierarchyRuntimeType addSubtype:] : 196 -> 180
~ -[DebugHierarchyRuntimeType isKindOfTypeWithName:] : 148 -> 144
~ -[DebugHierarchyRuntimeType propertyWithName:] : 172 -> 164
~ -[DebugHierarchyRuntimeType namesOfInheritanceChain] : 176 -> 164
~ -[DebugHierarchyRuntimeType closestTypeVendingAChildGroupingID] : 148 -> 132
~ -[DebugHierarchyRuntimeType instanceProperties] : 100 -> 88
~ -[DebugHierarchyRuntimeType addInstanceProperty:] : 132 -> 124
~ -[DebugHierarchyRuntimeType sourceLanguage] : 128 -> 120
~ -[DebugHierarchyRuntimeType dictionaryRepresentation] : 976 -> 920
~ -[DebugHierarchyRuntimeType isEqual:] : 312 -> 292
~ -[DebugHierarchyRuntimeType debugDescription] : 196 -> 180
~ -[DebugHierarchyRequest(Utilities) formattedResponseDataForRawRequestResultData:] : 160 -> 164
~ +[DebugHierarchyRequest(TargetHubAdditions) requestWithBase64Data:error:] : 384 -> 376
~ +[DebugHierarchyRequest(TargetHubAdditions) _compatibleRequestWithDictionary:] : 180 -> 164
~ +[DebugHierarchyRequest(TargetHubAdditions) _requestWithV1RequestDictionary:] : 648 -> 608
~ ___77+[DebugHierarchyRequest(TargetHubAdditions) _requestWithV1RequestDictionary:]_block_invoke : 488 -> 484
~ -[DebugHierarchyRunLoopAction performInContext:] : 120 -> 112
~ -[DebugHierarchyRequestActionExecutor initWithContext:] : 108 -> 116
~ -[DebugHierarchyRequestActionExecutor initialActions] : 184 -> 164
~ -[DebugHierarchyRequestActionExecutor finalActions] : 184 -> 164
~ -[DebugHierarchyRequestActionExecutor objectActions] : 184 -> 164
~ +[DebugHierarchyRequestActionExecutor initialActionsFromActions:] : 216 -> 204
~ +[DebugHierarchyRequestActionExecutor finalActionsFromActions:] : 256 -> 248
~ -[DebugHierarchyRequestActionExecutor executeInitialStandaloneActions] : 124 -> 116
~ -[DebugHierarchyRequestActionExecutor executeFinalStandaloneActions] : 124 -> 116
~ -[DebugHierarchyRequestActionExecutor executeActionsWithObject:] : 152 -> 144
~ +[DebugHierarchyRequestActionExecutor _executeStandaloneActions:inContext:] : 252 -> 260
~ +[DebugHierarchyRequestActionExecutor _executeObjectActions:withObject:inContext:] : 276 -> 288
~ -[NSData(Gzip) dbg_gzipInflateIfCompressed] : 88 -> 76
~ -[NSData(Gzip) dbg_gzipInflate] : 264 -> 216
~ -[NSData(Gzip) dbg_gzipInflateWithWindowBits:] : 924 -> 880
~ -[NSData(Gzip) dbg_gzipDeflate] : 272 -> 224
~ -[NSData(Gzip) dbg_gzipDeflateWithLevel:windowBits:memLevel:] : 820 -> 776
~ _DebugHierarchyGzipOSLog : 84 -> 68
~ +[DebugHierarchyLogEntry errorLogEntryWithTitle:message:methodSignature:environmentInfo:] : 152 -> 164
~ +[DebugHierarchyLogEntry warningLogEntryWithTitle:message:methodSignature:environmentInfo:] : 152 -> 164
~ +[DebugHierarchyLogEntry errorLogEntryWithTitle:message:methodSignature:] : 132 -> 140
~ +[DebugHierarchyLogEntry warningLogEntryWithTitle:message:methodSignature:] : 132 -> 140
~ +[DebugHierarchyLogEntry formattedSummaryOfLogs:] : 372 -> 360
~ -[DebugHierarchyLogEntry initWithSeverity:title:message:methodSignature:environmentInfo:] : 248 -> 260
~ -[DebugHierarchyLogEntry initWithDictionary:] : 384 -> 356
~ -[DebugHierarchyLogEntry dictionaryRepresentation] : 596 -> 548
~ -[DebugHierarchyLogEntry formattedSummary] : 180 -> 164
~ +[DBGTargetHub sharedHub] : 176 -> 160
~ -[DBGTargetHub performRequest:] : 120 -> 112
~ -[DBGTargetHub performRequestWithRequestInBase64:] : 120 -> 112
~ -[DBGTargetHub clearAllRequestsAndData] : 76 -> 72
~ +[DebugHierarchyTargetHub sharedHub] : 176 -> 160
~ -[DebugHierarchyTargetHub init] : 160 -> 156
~ -[DebugHierarchyTargetHub knownObjectsMap] : 100 -> 88
~ -[DebugHierarchyTargetHub additionalKnownObjects] : 92 -> 84
~ -[DebugHierarchyTargetHub runtimeInfo] : 92 -> 84
~ -[DebugHierarchyTargetHub performRequestWithRequestInBase64:] : 284 -> 272
~ -[DebugHierarchyTargetHub performRequest:error:] : 704 -> 664
~ ___48-[DebugHierarchyTargetHub performRequest:error:]_block_invoke : 136 -> 132
~ -[DebugHierarchyTargetHub performRequestInPlaceWithRequestInBase64:] : 60 -> 56
~ -[DebugHierarchyTargetHub performRequestAndWriteResponseToFileDescriptorWithRequestInBase64:fileDescriptor:] : 176 -> 164
~ -[DebugHierarchyTargetHub registerForDarwinNotifications] : 220 -> 216
~ -[DebugHierarchyTargetHub openXPCConnection] : 312 -> 324
~ ___44-[DebugHierarchyTargetHub openXPCConnection]_block_invoke_2 : 224 -> 212
~ -[DebugHierarchyTargetHub handleXPCEvent:] : 296 -> 292
~ -[DebugHierarchyTargetHub setCurrentRequest:responseFileDescriptor:reply:] : 124 -> 120
~ +[DebugHierarchyTargetHub performDebugRequest:] : 336 -> 320
~ -[DebugHierarchyTargetHub setAdditionalKnownObjects:] : 64 -> 12
~ -[DebugHierarchyTargetHub setCurrentRequestInBase64:] : 64 -> 12
~ -[DebugHierarchyTargetHub setCurrentReply:] : 64 -> 12
~ __DBGViewHierarchyInitialize : 76 -> 72
~ _DebugHierarchyRequestsOSLog : 84 -> 68
~ +[DebugHierarchyResetAction resetRequest] : 228 -> 220
~ -[DebugHierarchyResetAction performInContext:] : 76 -> 72
~ __DBGStructureOfDictionaryDescriptionWithFormat : 696 -> 676
~ +[DebugHierarchyFormatSpecifier specifierWithFormat:label:] : 108 -> 112
~ -[DebugHierarchyFormatSpecifier initWithFormat:label:] : 144 -> 152
~ _DBGClearCachedFormatSpecifiers : 68 -> 64
~ _DBGCachedFormatSpecifiers : 84 -> 68
~ _DBGSpecifiersFromFormatString : 1040 -> 976
~ _DBGEncodeDictionaryAsJSONCompatibleDictionary : 268 -> 276
~ ___DBGEncodeDictionaryAsJSONCompatibleDictionary_block_invoke : 296 -> 280
~ _DBGEncodeValueAsJSONCompatibleValue : 1416 -> 1340
~ _DBGDecodeDictionaryFromJSONCompatibleDictionary : 268 -> 276
~ ___DBGDecodeDictionaryFromJSONCompatibleDictionary_block_invoke : 296 -> 280
~ _DBGDecodeValueFromJSONCompatibleValue : 2416 -> 2212
~ _DBGSerializePropertyDescriptionAsJSON : 612 -> 584
~ _DBGSerializePropertyDescriptionsAsJSON : 428 -> 424
~ _DBGDeserializePropertyDictionaryFromJSON : 300 -> 296
~ _DBGDeserializePropertyDictionariesFromJSON : 428 -> 424
~ ___DBGCachedFormatSpecifiers_block_invoke : 68 -> 64

```
