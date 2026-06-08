## CognitiveHealth

> `/System/Library/PrivateFrameworks/CognitiveHealth.framework/CognitiveHealth`

```diff

-26.0.0.0.0
-  __TEXT.__text: 0x4098
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_methlist: 0x3f8
+27.0.0.0.0
+  __TEXT.__text: 0x3e40
+  __TEXT.__objc_methlist: 0x400
   __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0xec
+  __TEXT.__gcc_except_tab: 0xd8
   __TEXT.__oslogstring: 0x240
-  __TEXT.__cstring: 0xa91
+  __TEXT.__cstring: 0xa13
   __TEXT.__unwind_info: 0x198
-  __TEXT.__objc_classname: 0x13d
-  __TEXT.__objc_methname: 0xf83
-  __TEXT.__objc_methtype: 0x29f
-  __TEXT.__objc_stubs: 0xb00
-  __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x1a0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1c0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x390
+  __DATA_CONST.__objc_selrefs: 0x3a8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x1e8
-  __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x880
+  __DATA_CONST.__got: 0x138
+  __AUTH_CONST.__const: 0x160
+  __AUTH_CONST.__cfstring: 0x8a0
   __AUTH_CONST.__objc_const: 0xb80
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x3c0
   __DATA.__objc_ivar: 0x54
   __DATA.__data: 0x180

   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C85F2421-9A78-3662-ADB5-1591EFC1BC4A
-  Functions: 96
-  Symbols:   530
-  CStrings:  355
+  UUID: 80AC42FB-9D3C-3D43-BB91-07F400EC8CFE
+  Functions: 99
+  Symbols:   549
+  CStrings:  160
 
Symbols:
+ -[CHMobileAssetBridge autoAssetEndAllAtomicLocks:]
+ GCC_except_table73
+ GCC_except_table92
+ GCC_except_table96
+ _OBJC_CLASS_$_MAAutoAssetSet
+ _OBJC_CLASS_$_MAAutoAssetSetEntry
+ _OBJC_CLASS_$_MAAutoAssetSetPolicy
+ ___26-[CHSensorDataClient init]_block_invoke.19
+ ___48-[CHXPCClientHelper _locked_establishConnection]_block_invoke.3
+ ___50-[CHMobileAssetBridge autoAssetEndAllAtomicLocks:]_block_invoke
+ ___93-[CHMobileAssetBridge autoAssetLockContentForAssetType:assetSpecifier:lockReason:completion:]_block_invoke_2
+ ___Block_byref_object_copy_.183
+ ___Block_byref_object_dispose_.184
+ ___block_descriptor_32_e42_v24?0"MAAutoAssetSetStatus"8"NSError"16l
+ ___block_descriptor_40_e8_32bs_e30_v24?0"NSString"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e42_v24?0"MAAutoAssetSetStatus"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e42_v32?0"NSString"8"NSArray"16"NSError"24ls32l8
+ ___block_literal_global.110
+ ___block_literal_global.142
+ ___block_literal_global.207
+ ___block_literal_global.21
+ ___block_literal_global.41
+ ___block_literal_global.74
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$autoAssetEndAllAtomicLocks:
+ _objc_msgSend$currentSetStatus:
+ _objc_msgSend$endAtomicLocks:usingClientDomain:forClientName:forAssetSetIdentifier:ofAtomicInstance:removingLockCount:completion:
+ _objc_msgSend$initUsingClientDomain:forClientName:forAssetSetIdentifier:comprisedOfEntries:error:
+ _objc_msgSend$localContentURL
+ _objc_msgSend$lockAtomic:forAtomicInstance:withNeedPolicy:withTimeout:reportingProgress:completion:
+ _objc_msgSend$needForAtomic:withNeedPolicy:completion:
+ _objc_msgSend$setUserInitiated:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
- GCC_except_table70
- GCC_except_table89
- GCC_except_table93
- _OBJC_CLASS_$_MAAutoAsset
- _OBJC_CLASS_$_MAAutoAssetSelector
- ___26-[CHSensorDataClient init]_block_invoke.25
- ___48-[CHXPCClientHelper _locked_establishConnection]_block_invoke.7
- ___Block_byref_object_copy_.176
- ___Block_byref_object_dispose_.177
- ___block_descriptor_40_e8_32bs_e39_v24?0"MAAutoAssetStatus"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e41_v24?0"MAAutoAssetSelector"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e76_v44?0"MAAutoAssetSelector"8B16"NSURL"20"MAAutoAssetStatus"28"NSError"36ls32l8
- ___block_literal_global.128
- ___block_literal_global.193
- ___block_literal_global.27
- ___block_literal_global.39
- ___block_literal_global.71
- _objc_msgSend$autoAssetEndAllLocksForAssetType:assetSpecifier:completion:
- _objc_msgSend$currentStatus:
- _objc_msgSend$endAllPreviousLocksOfSelector:forClientName:completion:
- _objc_msgSend$endLockUsage:completion:
- _objc_msgSend$initForClientName:selectingAsset:error:
- _objc_msgSend$interestInContent:completion:
- _objc_msgSend$lockContent:withTimeout:completion:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
CStrings:
+ "ALL_INSTANCES"
+ "Asset download progress - Status: %@, Error: %@"
+ "Attempting ending all atomic locks."
+ "CognitiveHealthAssetSet"
+ "Content locked. Entry Summary %@"
+ "Core Data fetch count %lu. Categories count %lu."
+ "Error ending all locks; Asset Set identifier: %@, Operation Error: %@"
+ "Error indicating need for atomic-instance; assetSetIdentifier:%@, error:%@"
+ "Success ending all locks; Asset Set identifier: %@"
+ "Success registerring for atomic instance. Asset Set identifier: %@"
+ "Successfully received auto asset set status with error %@"
+ "com.apple.CognitiveHealth"
+ "initial need for atomic-instance"
+ "v24@?0@\"MAAutoAssetSetStatus\"8@\"NSError\"16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
- ".cxx_destruct"
- "@"
- "@\"CHCoreDataController\""
- "@\"CHXPCClientHelper\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSObject<CHIntegrationTestProtocol>\""
- "@\"NSObject<CHSensorDataProtocol>\""
- "@\"NSPersistentContainer\""
- "@\"NSString\""
- "@\"NSXPCConnection\""
- "@\"NSXPCInterface\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@32@0:8@16@24"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8@16@24@32@?40@?48"
- "@?"
- "Auto-asset content locked and ready to use. Asset selector: %@, local content URL: %@"
- "B16@0:8"
- "CHAppLaunchSensorData"
- "CHCoreDataController"
- "CHCustomCategories"
- "CHCustomCategory"
- "CHIntegrationTest"
- "CHIntegrationTestClient"
- "CHIntegrationTestProtocol"
- "CHMobileAssetBridge"
- "CHSensorData"
- "CHSensorDataClient"
- "CHSensorDataProtocol"
- "CHVersion"
- "CHXPCClientHelper"
- "Content locked but newer version in progress %@"
- "Content locked; no newer version download in progress"
- "CoreDataProperties"
- "Download Custom Categories file"
- "Error ending all locks; Asset selector: %@, Operation Error: %@"
- "Error indicating interest in content; assetSelector:%@, error:%@"
- "Error unlocking asset; Asset selector: %@, Operation Error: %@"
- "Errror creating auto asset instance %@"
- "NSCoding"
- "NSSecureCoding"
- "Success ending all locks; Asset selector: %@"
- "Success locking asset; Asset selector: %@"
- "Success unlocking asset; Asset selector: %@"
- "Successfully received auto asset status with error %@"
- "T@\"CHCoreDataController\",&,N,V_coreDataController"
- "T@\"NSArray\",R,N,V_embeddingVector"
- "T@\"NSDate\",R,N,V_trainingDate"
- "T@\"NSDictionary\",&,N,V_intToUUIDMapping"
- "T@\"NSError\",&,N,V_fetchError"
- "T@\"NSPersistentContainer\",&,N,V_persistentContainer"
- "T@\"NSPersistentContainer\",R,V_persistentContainer"
- "T@\"NSString\",&,D,N"
- "T@\"NSString\",C,D,N"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_algorithmType"
- "T@\"NSString\",R,N,V_bundleId"
- "T@\"NSString\",R,N,V_modelVersion"
- "TB,R"
- "URLByAppendingPathComponent:"
- "URLForResource:withExtension:"
- "_algorithmType"
- "_bundleId"
- "_clientExportedObject"
- "_clientHelper"
- "_conn"
- "_connLock"
- "_coreDataController"
- "_embeddingVector"
- "_fetchError"
- "_intToUUIDMapping"
- "_interruptionHandler"
- "_invalidationHandler"
- "_locked_establishConnection"
- "_modelVersion"
- "_persistentContainer"
- "_serviceName"
- "_trainingDate"
- "_whitelistedServerInterface"
- "_xpcClient"
- "addObject:"
- "addPersistentStoreFromDatabase"
- "addPersistentStoreWithType:configuration:URL:options:error:"
- "aggregatedMotionAndAppLaunchDataFromDate:toDate:completion:"
- "array"
- "autoAssetAvailableForUseForAssetType:assetSpecifier:completion:"
- "autoAssetEndAllLocksForAssetType:assetSpecifier:completion:"
- "autoAssetEndLockContentForAssetType:assetSpecifier:endLockReason:completion:"
- "autoAssetInterestInContentForAssetType:assetSpecifier:completion:"
- "autoAssetLockContentForAssetType:assetSpecifier:lockReason:completion:"
- "bundleForClass:"
- "categoriesForBundleId:completion:"
- "categoriesForBundleIdSet:completion:"
- "category"
- "categoryForBundleId:"
- "code"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "contentsOfDirectoryAtPath:error:"
- "coreDataController"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentHandler"
- "currentStatus:"
- "customCategoryVersion"
- "databaseAssetAvailableStatusWithCompletion:"
- "dealloc"
- "defaultManager"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "downloadDatabaseAssetIfNeeded"
- "downloadDatabaseAssetIfNeededWithCompletion:"
- "embeddingVectorForBundleId:completion:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endAllPreviousLocksOfSelector:forClientName:completion:"
- "endLockUsage:completion:"
- "entityForName:inManagedObjectContext:"
- "executeFetchRequest:error:"
- "extractDataFromCoreDataResult:"
- "fetchCategoriesForBundleId:"
- "fetchError"
- "fetchRequest"
- "fetchRequestWithEntityName:"
- "fileURLWithPath:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "init"
- "initForAssetType:withAssetSpecifier:"
- "initForClientName:selectingAsset:error:"
- "initWithBundleId:embeddingVector:modelVersion:algorithmType:trainingDate:"
- "initWithCoder:"
- "initWithContentsOfURL:"
- "initWithMachServiceName:options:"
- "initWithName:managedObjectModel:"
- "initWithObjects:"
- "initWithServiceName:whitelistedServerInterface:clientExportedObject:interruptionHandler:invalidationHandler:"
- "intToUUIDMapping"
- "interestInContent:completion:"
- "interfaceWithProtocol:"
- "invalidate"
- "loadMappingFromFile"
- "loadPersistentStoresWithCompletionHandler:"
- "localizedDescription"
- "lockAssetAndReturnAssetPathForFile:withLockReason:"
- "lockAssetWithLockReason:"
- "lockContent:withTimeout:completion:"
- "newerVersionError"
- "objectAtIndex:"
- "objectForKey:"
- "path"
- "persistentContainer"
- "persistentStoreCoordinator"
- "persistentStoreForURL:"
- "populateSampleAppLaunchEmbeddingWithCompletion:"
- "predicateWithFormat:"
- "remoteObjectProxyWithErrorHandler:"
- "resetTimer"
- "resume"
- "robustDecodeObjectOfClass:forKey:withCoder:expectNonNull:errorDomain:errorCode:logHandle:"
- "robustDecodeObjectOfClasses:forKey:withCoder:expectNonNull:errorDomain:errorCode:logHandle:"
- "scheduledTimerWithTimeInterval:repeats:block:"
- "semanticVersion"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCoreDataController:"
- "setDateFormat:"
- "setEntity:"
- "setExportedObject:"
- "setFetchError:"
- "setIntToUUIDMapping:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setPersistentContainer:"
- "setPredicate:"
- "setRemoteObjectInterface:"
- "setValue:forKey:"
- "stringByAppendingPathComponent:"
- "stringFromDate:"
- "stringWithContentsOfFile:encoding:error:"
- "stringWithFormat:"
- "summary"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "userInfo"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@?0@\"MAAutoAssetSelector\"8@\"NSError\"16"
- "v24@?0@\"MAAutoAssetStatus\"8@\"NSError\"16"
- "v32@0:8@\"NSString\"16@?<v@?@\"CHAppLaunchSensorData\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSDate\"16@\"NSDate\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v44@?0@\"MAAutoAssetSelector\"8B16@\"NSURL\"20@\"MAAutoAssetStatus\"28@\"NSError\"36"
- "v48@0:8@16@24@32@?40"
- "viewContext"
- "{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}"

```
