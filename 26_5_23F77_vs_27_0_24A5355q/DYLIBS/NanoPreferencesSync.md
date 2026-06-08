## NanoPreferencesSync

> `/System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync`

```diff

-323.0.0.0.0
-  __TEXT.__text: 0xa7f4
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_methlist: 0xc34
-  __TEXT.__cstring: 0xab2
+331.0.0.0.0
+  __TEXT.__text: 0x9e1c
+  __TEXT.__objc_methlist: 0x75c
+  __TEXT.__cstring: 0xacc
   __TEXT.__const: 0xa0
-  __TEXT.__oslogstring: 0xae7
-  __TEXT.__gcc_except_tab: 0xfc
-  __TEXT.__unwind_info: 0x3a0
-  __TEXT.__objc_classname: 0x12e
-  __TEXT.__objc_methname: 0x1fa9
-  __TEXT.__objc_methtype: 0x52f
-  __TEXT.__objc_stubs: 0x1860
-  __DATA_CONST.__got: 0x190
+  __TEXT.__oslogstring: 0xb4c
+  __TEXT.__gcc_except_tab: 0xd8
+  __TEXT.__unwind_info: 0x380
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x4d8
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8f0
+  __DATA_CONST.__objc_selrefs: 0x718
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x290
+  __DATA_CONST.__got: 0x198
   __AUTH_CONST.__const: 0x200
   __AUTH_CONST.__cfstring: 0x720
-  __AUTH_CONST.__objc_const: 0xef8
+  __AUTH_CONST.__objc_const: 0xd98
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x5c
+  __DATA.__objc_ivar: 0x60
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x70
+  __DATA.__bss: 0x30
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__data: 0x4
-  __DATA_DIRTY.__bss: 0x18
+  __DATA_DIRTY.__bss: 0x58
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5CFB3866-FA26-3052-AD78-C10524C04CB2
-  Functions: 291
-  Symbols:   1092
-  CStrings:  644
+  UUID: BEA66DBF-3445-3F4A-9BF6-E805DE22EE70
+  Functions: 292
+  Symbols:   1074
+  CStrings:  219
 
Symbols:
+ -[NPSDomainAccessorFilePresenter initWithDelegate:domainURL:].cold.1
+ -[NPSDomainAccessorInternal lastDiskReadDate]
+ -[NPSDomainAccessorInternal objectForKey:completionHandler:].cold.1
+ -[NPSDomainAccessorInternal setLastDiskReadDate:]
+ GCC_except_table3
+ GCC_except_table43
+ GCC_except_table53
+ _NSFileModificationDate
+ _OBJC_IVAR_$_NPSDomainAccessorInternal._lastDiskReadDate
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ ___82+[NPSDomainAccessorInternal internalAccessorForPairingID:pairingDataStore:domain:]_block_invoke.cold.1
+ ___82+[NPSDomainAccessorInternal internalAccessorForPairingID:pairingDataStore:domain:]_block_invoke_2.cold.1
+ ___82+[NPSDomainAccessorInternal internalAccessorForPairingID:pairingDataStore:domain:]_block_invoke_2.cold.2
+ ___block_literal_global.187
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$compare:
+ _objc_msgSend$date
+ _objc_opt_self
+ _objc_release_x2
+ _objc_release_x27
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x8
- GCC_except_table127
- GCC_except_table20
- GCC_except_table36
- GCC_except_table39
- __OBJC_$_CLASS_METHODS_NPSDomainAccessorUtils
- __OBJC_$_PROP_LIST_NPSDomainAccessorInternal
- __OBJC_$_PROP_LIST_NPSManager
- ___block_literal_global.294
- _objc_msgSend$URLForKey:
- _objc_msgSend$URLForObject:
- _objc_msgSend$_invalidatePresenter
- _objc_msgSend$arrayForKey:
- _objc_msgSend$arrayForObject:
- _objc_msgSend$boolForKey:keyExistsAndHasValidFormat:
- _objc_msgSend$boolForObject:existsAndHasValidFormat:
- _objc_msgSend$copyDomainListForPairingDataStore:
- _objc_msgSend$copyKeyList
- _objc_msgSend$createNanoSettingsDirectory
- _objc_msgSend$dataForKey:
- _objc_msgSend$dataForObject:
- _objc_msgSend$decrementInternalAccessorReferenceCount:
- _objc_msgSend$dictionaryForKey:
- _objc_msgSend$dictionaryForObject:
- _objc_msgSend$dictionaryRepresentation
- _objc_msgSend$domainIsValid:
- _objc_msgSend$domainSize
- _objc_msgSend$doubleForKey:
- _objc_msgSend$doubleForKey:keyExistsAndHasValidFormat:
- _objc_msgSend$doubleForObject:existsAndHasValidFormat:
- _objc_msgSend$filePresenter
- _objc_msgSend$floatForKey:
- _objc_msgSend$floatForKey:keyExistsAndHasValidFormat:
- _objc_msgSend$floatForObject:existsAndHasValidFormat:
- _objc_msgSend$initWithDelegate:domainURL:
- _objc_msgSend$integerForKey:
- _objc_msgSend$integerForKey:keyExistsAndHasValidFormat:
- _objc_msgSend$integerForObject:existsAndHasValidFormat:
- _objc_msgSend$internalAccessor
- _objc_msgSend$internalAccessorForPairingID:pairingDataStore:domain:
- _objc_msgSend$internalQueue
- _objc_msgSend$invalidateAndReleaseUnreferencedAccessors
- _objc_msgSend$invalidatePresenter
- _objc_msgSend$isCurrent
- _objc_msgSend$longForKey:
- _objc_msgSend$longForKey:keyExistsAndHasValidFormat:
- _objc_msgSend$longForObject:existsAndHasValidFormat:
- _objc_msgSend$objectForKey:completionHandler:
- _objc_msgSend$objectForURL:
- _objc_msgSend$readDomainURL:withError:
- _objc_msgSend$referenceCounter
- _objc_msgSend$requiresDeviceUnlockedSinceBoot
- _objc_msgSend$setBool:forKey:
- _objc_msgSend$setDouble:forKey:
- _objc_msgSend$setFloat:forKey:
- _objc_msgSend$setHasReadFromDisk:
- _objc_msgSend$setInteger:forKey:
- _objc_msgSend$setObject:forKey:completionHandler:
- _objc_msgSend$setReferenceCounter:
- _objc_msgSend$setURL:forKey:
- _objc_msgSend$setXpcConnection:
- _objc_msgSend$stringArrayForObject:
- _objc_msgSend$stringForKey:
- _objc_msgSend$stringForObject:
- _objc_msgSend$synchronizeForReadingOnly:handler:
- _objc_msgSend$synchronizeWithCompletionHandler:
- _objc_msgSend$urlForDomain:pairingDataStore:
- _objc_msgSend$writeDomain:toURL:
CStrings:
+ "Stale cache for domain %{public}@: file mtime (%{public}@) > last read (%{public}@); forcing re-read"
+ "[NPSDomainAccessorInternal domainIsValid:domain]"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<NPSDomainAccessorFilePresenterDelegate>\""
- "@\"NPSDomainAccessorFilePresenter\""
- "@\"NPSDomainAccessorInternal\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSOperationQueue\""
- "@\"NSOperationQueue\"16@0:8"
- "@\"NSSet\"16@0:8"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSURL\"16@0:8"
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^v16"
- "@28@0:8@16B24"
- "@28@0:8B16@?20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@48@0:8@16@24@32@40"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16^B24"
- "NPSCompanionServerProtocol"
- "NPSDomainAccessorFilePresenter"
- "NPSDomainAccessorFilePresenterDelegate"
- "NPSDomainAccessorUtils"
- "NPSManager"
- "NPSPairedDeviceRegistry"
- "NPSPrefPlistSizeUtil"
- "NPSServerProtocol"
- "NSFilePresenter"
- "NSObject"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "Q32@0:8@16@24"
- "T#,R"
- "T@\"<NPSDomainAccessorFilePresenterDelegate>\",R,W,N,V_delegate"
- "T@\"NPSDomainAccessorFilePresenter\",&,N,V_filePresenter"
- "T@\"NPSDomainAccessorInternal\",&,N,V_internalAccessor"
- "T@\"NSMutableDictionary\",&,N,V_map"
- "T@\"NSMutableSet\",&,N,V_dirtyKeysForWriting"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_externalQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_internalQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_invalidationQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_presenterUnderlyingQueue"
- "T@\"NSOperationQueue\",&,N,V_presenterOperationQueue"
- "T@\"NSOperationQueue\",R,&"
- "T@\"NSSet\",?,R"
- "T@\"NSString\",&,N,V_domain"
- "T@\"NSString\",&,N,V_pairingStorePath"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSURL\",&,N,V_domainURL"
- "T@\"NSURL\",?,R,C"
- "T@\"NSURL\",R,C"
- "T@\"NSUUID\",&,N,V_pairingID"
- "T@\"NSUUID\",R,N"
- "T@\"NSXPCConnection\",&,N,V_xpcConnection"
- "TB,N,GisCurrent,V_current"
- "TB,N,V_hasReadFromDisk"
- "TB,N,V_initializedWithActiveDevice"
- "TB,N,V_nanoSettingsDirectoryExists"
- "TQ,N,V_referenceCounter"
- "TQ,R"
- "URLForKey:"
- "URLForObject:"
- "UTF8String"
- "UUIDString"
- "Vv16@0:8"
- "[[self class] domainIsValid:domain]"
- "^{_NSZone=}16@0:8"
- "_copyKeyList"
- "_current"
- "_delegate"
- "_dictionaryRepresentation"
- "_dirtyKeysForWriting"
- "_domain"
- "_domainPlistPathFor:inContainer:"
- "_domainURL"
- "_externalQueue"
- "_filePresenter"
- "_hasReadFromDisk"
- "_initializedWithActiveDevice"
- "_internalAccessor"
- "_internalQueue"
- "_invalidatePresenter"
- "_invalidationQueue"
- "_map"
- "_nanoSettingsDirectoryExists"
- "_objectForKey:error:"
- "_pairingID"
- "_pairingStorePath"
- "_presenterOperationQueue"
- "_presenterUnderlyingQueue"
- "_referenceCounter"
- "_setObject:forKey:"
- "_synchronizeReadOnly:"
- "_xpcConnection"
- "absoluteString"
- "absoluteURL"
- "accommodatePresentedItemDeletionWithCompletionHandler:"
- "accommodatePresentedItemEvictionWithCompletionHandler:"
- "accommodatePresentedSubitemDeletionAtURL:completionHandler:"
- "activeDevice"
- "activeDeviceChanged"
- "addFilePresenter:"
- "addObject:"
- "addObserver:selector:name:object:"
- "addOperations:waitUntilFinished:"
- "allKeys"
- "applicationDidEnterBackground"
- "applicationDidResume"
- "applicationState"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "arrayForKey:"
- "arrayForObject:"
- "arrayWithObjects:count:"
- "attributesOfItemAtPath:error:"
- "autorelease"
- "beginBackgroundTaskWithName:expirationHandler:"
- "blockOperationWithBlock:"
- "boolForKey:"
- "boolForKey:keyExistsAndHasValidFormat:"
- "boolForObject:existsAndHasValidFormat:"
- "boolValue"
- "callStackSymbols"
- "canSynchronizeForReadingURL:"
- "canSynchronizeForWritingURL:readFirst:"
- "cfTypeNameForCFPropertyListRef:"
- "class"
- "code"
- "compare:options:range:"
- "conformsToProtocol:"
- "connection"
- "containsObject:"
- "contentsOfDirectoryAtPath:error:"
- "coordinateReadingItemAtURL:options:error:byAccessor:"
- "coordinateWritingItemAtURL:options:error:byAccessor:"
- "copy"
- "copyDomainList"
- "copyDomainListForPairingDataStore:"
- "copyDomainListForPairingID:pairingDataStore:"
- "copyKeyList"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createNanoSettingsDirectory"
- "current"
- "d24@0:8@16"
- "d32@0:8@16^B24"
- "dataForKey:"
- "dataForObject:"
- "dataWithContentsOfURL:options:error:"
- "dataWithPropertyList:format:options:error:"
- "dealloc"
- "debugDescription"
- "decrementInternalAccessorReferenceCount:"
- "defaultCenter"
- "defaultManager"
- "delegate"
- "description"
- "dictionaryForKey:"
- "dictionaryForObject:"
- "dictionaryRepresentation"
- "dictionaryWithObjects:forKeys:count:"
- "dirtyKeysForWriting"
- "domain"
- "domainIsValid:"
- "domainSize"
- "domainURL"
- "doubleForKey:"
- "doubleForKey:keyExistsAndHasValidFormat:"
- "doubleForObject:existsAndHasValidFormat:"
- "doubleValue"
- "endBackgroundTask:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "exceptionWithName:reason:userInfo:"
- "extensionDidBecomeActive"
- "extensionWillResignActive"
- "externalQueue"
- "f24@0:8@16"
- "f32@0:8@16^B24"
- "fileExistsAtPath:"
- "filePresenter"
- "filePresenterDidBecomeNonCurrent:"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "floatForKey:"
- "floatForKey:keyExistsAndHasValidFormat:"
- "floatForObject:existsAndHasValidFormat:"
- "floatValue"
- "getActiveDevice"
- "hasReadFromDisk"
- "hash"
- "infoDictionary"
- "init"
- "initWithDelegate:domainURL:"
- "initWithDomain:"
- "initWithDomain:pairedDevice:"
- "initWithDomain:pairingID:pairingDataStore:"
- "initWithDomain:pdrDevice:"
- "initWithDomain:queue:"
- "initWithDomain:queue:pairingID:pairingDataStore:"
- "initWithFilePresenter:"
- "initWithInternalDomainAccessor:queue:"
- "initWithMachServiceName:options:"
- "initWithObjectsAndKeys:"
- "initWithPairingID:pairingDataStore:domain:"
- "initialize"
- "initializedWithActiveDevice"
- "integerForKey:"
- "integerForKey:keyExistsAndHasValidFormat:"
- "integerForObject:existsAndHasValidFormat:"
- "integerValue"
- "interfaceWithProtocol:"
- "internalAccessor"
- "internalAccessorForPairingID:pairingDataStore:domain:"
- "internalQueue"
- "invalidate"
- "invalidateAndReleaseUnreferencedAccessors"
- "invalidatePresenter"
- "invalidationQueue"
- "isCurrent"
- "isEqual:"
- "isEqualToString:"
- "isFileReferenceURL"
- "isFileURL"
- "isKindOfClass:"
- "isMainThread"
- "isMemberOfClass:"
- "isPlistProtectedAtPath:"
- "isProxy"
- "length"
- "localizedDescription"
- "longForKey:"
- "longForKey:keyExistsAndHasValidFormat:"
- "longForObject:existsAndHasValidFormat:"
- "longLongValue"
- "mainBundle"
- "map"
- "mergeDirtyKeys:fromDictionary:toDictionary:"
- "mutableCopy"
- "nanoSettingsDirectoryExists"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInteger:"
- "numberWithLongLong:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "objectForKey:completionHandler:"
- "objectForKeyedSubscript:"
- "objectForURL:"
- "observedPresentedItemUbiquityAttributes"
- "pairingStorePath"
- "path"
- "performExpiringActivityWithReason:usingBlock:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "prefSizeFor:inContainer:"
- "presentedItemDidChange"
- "presentedItemDidChangeUbiquityAttributes:"
- "presentedItemDidGainVersion:"
- "presentedItemDidLoseVersion:"
- "presentedItemDidMoveToURL:"
- "presentedItemDidResolveConflictVersion:"
- "presentedItemNeedsWatching"
- "presentedItemOperationQueue"
- "presentedItemURL"
- "presentedSubitemAtURL:didGainVersion:"
- "presentedSubitemAtURL:didLoseVersion:"
- "presentedSubitemAtURL:didMoveToURL:"
- "presentedSubitemAtURL:didResolveConflictVersion:"
- "presentedSubitemDidAppearAtURL:"
- "presentedSubitemDidChangeAtURL:"
- "presenterOperationQueue"
- "presenterUnderlyingQueue"
- "primaryPresentedItemURL"
- "processInfo"
- "propertyListWithData:options:format:error:"
- "q24@0:8@16"
- "q32@0:8@16^B24"
- "queue"
- "rangeOfString:"
- "readDomainURL:withError:"
- "referenceCounter"
- "registry"
- "release"
- "relinquishPresentedItemToReader:"
- "relinquishPresentedItemToWriter:"
- "removeFilePresenter:"
- "removeItemAtURL:error:"
- "removeObjectForKey:"
- "removeObjectsForKeys:"
- "requiresDeviceUnlockedSinceBoot"
- "resolveActivePairedDevicePairingID:pairingDataStore:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "savePresentedItemChangesWithCompletionHandler:"
- "self"
- "setBool:forKey:"
- "setCurrent:"
- "setDirtyKeysForWriting:"
- "setDomain:"
- "setDomainURL:"
- "setDouble:forKey:"
- "setExternalQueue:"
- "setFilePresenter:"
- "setFloat:forKey:"
- "setHasReadFromDisk:"
- "setInitializedWithActiveDevice:"
- "setInteger:forKey:"
- "setInternalAccessor:"
- "setInternalQueue:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setInvalidationQueue:"
- "setLong:forKey:"
- "setMap:"
- "setMaxConcurrentOperationCount:"
- "setNanoSettingsDirectoryExists:"
- "setObject:forKey:"
- "setObject:forKey:completionHandler:"
- "setObject:forKeyedSubscript:"
- "setPairingID:"
- "setPairingStorePath:"
- "setPresenterOperationQueue:"
- "setPresenterUnderlyingQueue:"
- "setReferenceCounter:"
- "setRemoteObjectInterface:"
- "setURL:forKey:"
- "setUnderlyingQueue:"
- "setWithArray:"
- "setXpcConnection:"
- "sharedApplication"
- "sharedInstance"
- "shouldNotDoWork"
- "sizeForPlistAtPath:"
- "start"
- "stringArrayForKey:"
- "stringArrayForObject:"
- "stringByAbbreviatingWithTildeInPath"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringByExpandingTildeInPath"
- "stringForKey:"
- "stringForObject:"
- "stringValue"
- "stringWithFormat:"
- "superclass"
- "supportsWatch"
- "synchronize"
- "synchronizeForReadingOnly:handler:"
- "synchronizeNanoDomain:keys:"
- "synchronizeNanoDomain:keys:cloudEnabled:"
- "synchronizeUserDefaultsDomain:keys:"
- "synchronizeUserDefaultsDomain:keys:cloudEnabled:"
- "synchronizeUserDefaultsDomain:keys:container:"
- "synchronizeUserDefaultsDomain:keys:container:appGroupContainer:"
- "synchronizeUserDefaultsDomain:keys:container:appGroupContainer:cloudEnabled:"
- "synchronizeWithCompletionHandler:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "unarchivedObjectOfClass:fromData:error:"
- "unsafe_invalidate"
- "unsignedLongLongValue"
- "urlForDomain:pairingDataStore:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NPSDomainAccessorFilePresenter\"16"
- "v24@0:8@\"NSFileVersion\"16"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@\"NSURL\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@?<v@?>>16"
- "v24@0:8Q16"
- "v28@0:8B16@20"
- "v28@0:8f16@20"
- "v32@0:8@\"NSURL\"16@\"NSFileVersion\"24"
- "v32@0:8@\"NSURL\"16@\"NSURL\"24"
- "v32@0:8@\"NSURL\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8^@16^@24"
- "v32@0:8d16@24"
- "v32@0:8q16@24"
- "v36@0:8@\"NSString\"16@\"NSSet\"24B32"
- "v36@0:8@16@24B32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v48@0:8@16@24@32@40"
- "v52@0:8@\"NSString\"16@\"NSSet\"24@\"NSString\"32@\"NSString\"40B48"
- "v52@0:8@16@24@32@40B48"
- "valueForProperty:"
- "valueIsValid:"
- "watchDidBecomeActive"
- "writeDomain:toURL:"
- "writeToURL:options:error:"
- "xpcConnection"
- "zone"

```
