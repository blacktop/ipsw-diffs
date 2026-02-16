## JetEngine

> `/System/Library/PrivateFrameworks/JetEngine.framework/JetEngine`

```diff

-9.3.4.0.0
-  __TEXT.__text: 0x45dd4c
-  __TEXT.__auth_stubs: 0x5050
+9.4.15.0.0
+  __TEXT.__text: 0x45f74c
+  __TEXT.__auth_stubs: 0x5170
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x1da4
-  __TEXT.__const: 0x98ab0
-  __TEXT.__cstring: 0x13846
-  __TEXT.__oslogstring: 0x6cc
-  __TEXT.__gcc_except_tab: 0x128
+  __TEXT.__objc_methlist: 0x1dd4
+  __TEXT.__const: 0x991a0
+  __TEXT.__gcc_except_tab: 0x154
+  __TEXT.__cstring: 0x10dd6
+  __TEXT.__oslogstring: 0x71c
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__swift5_typeref: 0xe4dc
-  __TEXT.__swift5_fieldmd: 0xb418
-  __TEXT.__constg_swiftt: 0xcec8
+  __TEXT.__swift5_typeref: 0xe858
+  __TEXT.__swift5_fieldmd: 0xb6f0
+  __TEXT.__constg_swiftt: 0xd114
   __TEXT.__swift5_builtin: 0x438
-  __TEXT.__swift5_reflstr: 0x6f7b
-  __TEXT.__swift5_assocty: 0x1778
-  __TEXT.__swift5_protos: 0x2a0
-  __TEXT.__swift5_proto: 0x1f34
-  __TEXT.__swift5_types: 0xf70
-  __TEXT.__swift5_capture: 0x6c78
-  __TEXT.__swift_as_entry: 0x8fc
-  __TEXT.__swift_as_ret: 0x970
+  __TEXT.__swift5_reflstr: 0x71eb
+  __TEXT.__swift5_assocty: 0x17a8
+  __TEXT.__swift5_protos: 0x2a8
+  __TEXT.__swift5_proto: 0x1f74
+  __TEXT.__swift5_types: 0xfa0
+  __TEXT.__swift5_capture: 0x6c68
+  __TEXT.__swift_as_entry: 0x914
+  __TEXT.__swift_as_ret: 0x99c
   __TEXT.__swift5_mpenum: 0x280
-  __TEXT.__unwind_info: 0x10b10
-  __TEXT.__eh_frame: 0x248c4
-  __TEXT.__objc_classname: 0x38b
-  __TEXT.__objc_methname: 0x4add
-  __TEXT.__objc_methtype: 0xad5
-  __TEXT.__objc_stubs: 0x19a0
-  __DATA_CONST.__got: 0xea8
-  __DATA_CONST.__const: 0xe90
-  __DATA_CONST.__objc_classlist: 0x478
+  __TEXT.__unwind_info: 0x10b78
+  __TEXT.__eh_frame: 0x24af8
+  __TEXT.__objc_classname: 0x1fca
+  __TEXT.__objc_methname: 0x624d
+  __TEXT.__objc_methtype: 0x12e9
+  __TEXT.__objc_stubs: 0x4ec0
+  __DATA_CONST.__got: 0xe48
+  __DATA_CONST.__const: 0x1160
+  __DATA_CONST.__objc_classlist: 0x498
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18a8
+  __DATA_CONST.__objc_selrefs: 0x18c8
   __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_superrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x2838
-  __AUTH_CONST.__const: 0x2c8a8
-  __AUTH_CONST.__cfstring: 0x1320
-  __AUTH_CONST.__objc_const: 0x9af0
+  __DATA_CONST.__objc_superrefs: 0xb0
+  __AUTH_CONST.__auth_got: 0x28c8
+  __AUTH_CONST.__const: 0x2ca08
+  __AUTH_CONST.__cfstring: 0x1360
+  __AUTH_CONST.__objc_const: 0x9e08
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x1f30
-  __AUTH.__data: 0x5878
-  __DATA.__objc_ivar: 0xdc
-  __DATA.__data: 0xbb90
-  __DATA.__bss: 0x30a30
-  __DATA.__common: 0x5f0
+  __AUTH.__objc_data: 0x1fd0
+  __AUTH.__data: 0x5a68
+  __DATA.__objc_ivar: 0xe0
+  __DATA.__data: 0xb780
+  __DATA.__bss: 0x310b0
+  __DATA.__common: 0x370
   __DATA_DIRTY.__objc_data: 0x618
-  __DATA_DIRTY.__data: 0x36d8
+  __DATA_DIRTY.__data: 0x3650
   __DATA_DIRTY.__bss: 0x1a88
-  __DATA_DIRTY.__common: 0x1f8
+  __DATA_DIRTY.__common: 0x1e0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BABA6159-6D84-3EF0-866D-A063AC2709B1
-  Functions: 21080
-  Symbols:   9229
-  CStrings:  3393
+  UUID: 5EB4DD2E-BB5E-3FDA-B164-58B930901D0D
+  Functions: 21043
+  Symbols:   9752
+  CStrings:  3422
 
Symbols:
+ -[JEURLSessionPreconnecter .cxx_destruct]
+ -[JEURLSessionPreconnecter initWithURLSession:]
+ -[JEURLSessionPreconnecter preconnectWithRequest:completionHandler:error:]
+ _BrotliAllocate.cold.1
+ _NSLocalizedFailureReasonErrorKey
+ _OBJC_CLASS_$_JEURLSessionPreconnecter
+ _OBJC_IVAR_$_JEURLSessionPreconnecter._session
+ _OBJC_METACLASS_$_JEURLSessionPreconnecter
+ __DATA__TtC9JetEngine21JetPackReloadObserver
+ __DATA__TtC9JetEngine21NotificationsListener
+ __DATA__TtCC9JetEngine21JetPackReloadObserver13ListenerToken
+ __IVARS__TtC9JetEngine21JetPackReloadObserver
+ __IVARS__TtC9JetEngine21NotificationsListener
+ __IVARS__TtCC9JetEngine21JetPackReloadObserver13ListenerToken
+ __METACLASS_DATA__TtC9JetEngine21JetPackReloadObserver
+ __METACLASS_DATA__TtC9JetEngine21NotificationsListener
+ __METACLASS_DATA__TtCC9JetEngine21JetPackReloadObserver13ListenerToken
+ __OBJC_$_INSTANCE_METHODS_JEURLSessionPreconnecter
+ __OBJC_$_INSTANCE_VARIABLES_JEURLSessionPreconnecter
+ __OBJC_CLASS_RO_$_JEURLSessionPreconnecter
+ __OBJC_METACLASS_RO_$_JEURLSessionPreconnecter
+ ___swift_memcpy146_8
+ _associated conformance 9JetEngine22PushChannelStateRecordV10CodingKeys33_7674369818C74462B0012F4D78C73DD4LLOSHAASQ
+ _associated conformance 9JetEngine22PushChannelStateRecordV10CodingKeys33_7674369818C74462B0012F4D78C73DD4LLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 9JetEngine22PushChannelStateRecordV10CodingKeys33_7674369818C74462B0012F4D78C73DD4LLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 9JetEngine22ReloadNotificationTypeOSHAASQ
+ _associated conformance 9JetEngine3BagV0C15SoftwareVersionOSHAASQ
+ _associated conformance 9JetEngine7JSErrorV4KindOSHAASQ
+ _block_copy_helper.20
+ _block_copy_helper.21
+ _block_copy_helper.264
+ _block_copy_helper.273
+ _block_copy_helper.282
+ _block_copy_helper.290
+ _block_copy_helper.298
+ _block_copy_helper.304
+ _block_copy_helper.312
+ _block_copy_helper.319
+ _block_copy_helper.350
+ _block_copy_helper.358
+ _block_copy_helper.366
+ _block_copy_helper.374
+ _block_copy_helper.381
+ _block_copy_helper.389
+ _block_copy_helper.399
+ _block_copy_helper.414
+ _block_copy_helper.436
+ _block_copy_helper.448
+ _block_copy_helper.45
+ _block_copy_helper.456
+ _block_copy_helper.464
+ _block_copy_helper.472
+ _block_copy_helper.480
+ _block_copy_helper.488
+ _block_copy_helper.496
+ _block_copy_helper.504
+ _block_copy_helper.512
+ _block_copy_helper.520
+ _block_copy_helper.523
+ _block_copy_helper.70
+ _block_copy_helper.76
+ _block_copy_helper.93
+ _block_copy_helper.99
+ _block_descriptor.101
+ _block_descriptor.22
+ _block_descriptor.23
+ _block_descriptor.266
+ _block_descriptor.275
+ _block_descriptor.284
+ _block_descriptor.292
+ _block_descriptor.300
+ _block_descriptor.306
+ _block_descriptor.314
+ _block_descriptor.321
+ _block_descriptor.352
+ _block_descriptor.360
+ _block_descriptor.368
+ _block_descriptor.376
+ _block_descriptor.383
+ _block_descriptor.391
+ _block_descriptor.401
+ _block_descriptor.416
+ _block_descriptor.438
+ _block_descriptor.450
+ _block_descriptor.458
+ _block_descriptor.466
+ _block_descriptor.47
+ _block_descriptor.474
+ _block_descriptor.482
+ _block_descriptor.490
+ _block_descriptor.498
+ _block_descriptor.506
+ _block_descriptor.514
+ _block_descriptor.522
+ _block_descriptor.525
+ _block_descriptor.72
+ _block_descriptor.78
+ _block_descriptor.95
+ _block_destroy_helper.100
+ _block_destroy_helper.21
+ _block_destroy_helper.22
+ _block_destroy_helper.265
+ _block_destroy_helper.274
+ _block_destroy_helper.283
+ _block_destroy_helper.291
+ _block_destroy_helper.299
+ _block_destroy_helper.305
+ _block_destroy_helper.313
+ _block_destroy_helper.320
+ _block_destroy_helper.351
+ _block_destroy_helper.359
+ _block_destroy_helper.367
+ _block_destroy_helper.375
+ _block_destroy_helper.382
+ _block_destroy_helper.390
+ _block_destroy_helper.400
+ _block_destroy_helper.415
+ _block_destroy_helper.437
+ _block_destroy_helper.449
+ _block_destroy_helper.457
+ _block_destroy_helper.46
+ _block_destroy_helper.465
+ _block_destroy_helper.473
+ _block_destroy_helper.481
+ _block_destroy_helper.489
+ _block_destroy_helper.497
+ _block_destroy_helper.505
+ _block_destroy_helper.513
+ _block_destroy_helper.521
+ _block_destroy_helper.524
+ _block_destroy_helper.71
+ _block_destroy_helper.77
+ _block_destroy_helper.94
+ _get_type_metadata 15Synchronization5MutexVySDy9JetEngine12DiskPropertyOAD06CachedeF033_3D988632E755F3184F7A0396680788AELLVGG noncopyable.2
+ _notify_post
+ _objc_msgSend$JSGlobalContextRef
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$JSValueRef
+ _objc_msgSend$URL
+ _objc_msgSend$URLForDirectory:inDomain:appropriateForURL:create:error:
+ _objc_msgSend$URLForKey:
+ _objc_msgSend$URLForResource:withExtension:
+ _objc_msgSend$URLWithSize:
+ _objc_msgSend$URLWithSize:cropStyle:format:
+ _objc_msgSend$URLWithSize:cropStyle:format:quality:
+ _objc_msgSend$__swift_objectForKeyedSubscript:
+ _objc_msgSend$__swift_setObject:forKeyedSubscript:
+ _objc_msgSend$_calculatedExpiration
+ _objc_msgSend$_incompleteTaskMetrics
+ _objc_msgSend$_setDebuggerRunLoop:
+ _objc_msgSend$_setIdentifier:withStartedDate:forKey:
+ _objc_msgSend$_timingDataOptions
+ _objc_msgSend$account
+ _objc_msgSend$acquireWithError:
+ _objc_msgSend$addBagKey:valueType:
+ _objc_msgSend$addFinishBlock:
+ _objc_msgSend$addObserver:forKeyPath:options:context:
+ _objc_msgSend$addObserver:selector:name:object:
+ _objc_msgSend$addOperation:
+ _objc_msgSend$addPropertiesWithDictionary:
+ _objc_msgSend$addSubsystem:category:
+ _objc_msgSend$allItems
+ _objc_msgSend$allObjects
+ _objc_msgSend$ams_DSID
+ _objc_msgSend$ams_accountFlagValueForAccountFlag:
+ _objc_msgSend$ams_activeiTunesAccount
+ _objc_msgSend$ams_configurationWithProcessInfo:bag:
+ _objc_msgSend$ams_configureWithClientInfo:bag:
+ _objc_msgSend$ams_cookiesForURL:
+ _objc_msgSend$ams_iTunesAccountWithDSID:
+ _objc_msgSend$ams_localiTunesAccount
+ _objc_msgSend$ams_setAccountFlagValue:forAccountFlag:
+ _objc_msgSend$ams_sharedAccountStore
+ _objc_msgSend$ams_sharedAccountStoreForMediaType:
+ _objc_msgSend$ams_storefront
+ _objc_msgSend$ams_storefrontForMediaType:
+ _objc_msgSend$arrayForKey:
+ _objc_msgSend$artworkDictionary
+ _objc_msgSend$artworkSize
+ _objc_msgSend$attributeWithDomain:name:
+ _objc_msgSend$attributesOfItemAtPath:error:
+ _objc_msgSend$bag
+ _objc_msgSend$bagForProfile:profileVersion:
+ _objc_msgSend$bagForProfile:profileVersion:processInfo:
+ _objc_msgSend$bagValueWithKey:valueType:valuePromise:
+ _objc_msgSend$beginDate
+ _objc_msgSend$blockOperationWithBlock:
+ _objc_msgSend$boolForEntitlement:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$buildWithError:
+ _objc_msgSend$cacheBytecodeWithError:
+ _objc_msgSend$cachedValuesForKeys:observationToken:updateHandler:
+ _objc_msgSend$callWithArguments:
+ _objc_msgSend$charValue
+ _objc_msgSend$clientInfo
+ _objc_msgSend$code
+ _objc_msgSend$colorWithKind:
+ _objc_msgSend$compareWithValue:andExchangeWithValue:
+ _objc_msgSend$compressStreamWithOperation:availableIn:nextIn:availableOut:nextOut:
+ _objc_msgSend$connectEndDate
+ _objc_msgSend$connectStartDate
+ _objc_msgSend$constructWithArguments:
+ _objc_msgSend$containerId
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _objc_msgSend$context
+ _objc_msgSend$copyItemAtPath:toPath:error:
+ _objc_msgSend$countOfRequestBodyBytesSent
+ _objc_msgSend$countOfRequestHeaderBytesSent
+ _objc_msgSend$countOfResponseBodyBytesReceived
+ _objc_msgSend$countOfResponseHeaderBytesReceived
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$createFileAtPath:contents:attributes:
+ _objc_msgSend$createSnapshotWithCompletion:
+ _objc_msgSend$currentArguments
+ _objc_msgSend$currentContext
+ _objc_msgSend$currentProcess
+ _objc_msgSend$currentRequest
+ _objc_msgSend$currentThis
+ _objc_msgSend$currentThread
+ _objc_msgSend$data
+ _objc_msgSend$dataTaskPromiseWithRequest:
+ _objc_msgSend$dataTaskPromiseWithRequest:activity:
+ _objc_msgSend$dataTaskWithRequest:completionHandler:
+ _objc_msgSend$dataWithJSONObject:options:error:
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$dateFromString:
+ _objc_msgSend$decimalValue
+ _objc_msgSend$decompressStreamWithAvailableIn:nextIn:availableOut:nextOut:
+ _objc_msgSend$decrement
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$defaultManager
+ _objc_msgSend$defaultSessionConfiguration
+ _objc_msgSend$defaultSignatureVerifier
+ _objc_msgSend$defineProperty:descriptor:
+ _objc_msgSend$deleteProperty:
+ _objc_msgSend$diagnosticsSubmissionAllowed
+ _objc_msgSend$dictionaryForKey:
+ _objc_msgSend$dictionaryForPosting
+ _objc_msgSend$domain
+ _objc_msgSend$domainLookupEndDate
+ _objc_msgSend$domainLookupStartDate
+ _objc_msgSend$doubleForKey:
+ _objc_msgSend$downloadTaskWithRequest:completionHandler:
+ _objc_msgSend$durationNanoseconds
+ _objc_msgSend$endDate
+ _objc_msgSend$endEvent
+ _objc_msgSend$enqueueEvent:
+ _objc_msgSend$environment
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$escapedPatternForString:
+ _objc_msgSend$evaluateJSScript:
+ _objc_msgSend$exception
+ _objc_msgSend$exceptionHandler
+ _objc_msgSend$executableURL
+ _objc_msgSend$expiresDate
+ _objc_msgSend$failingBagValueWithKey:valueType:error:
+ _objc_msgSend$fetchStartDate
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$fileHandleForWritingToURL:error:
+ _objc_msgSend$fileURLWithPathComponents:
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$floatValue
+ _objc_msgSend$flush
+ _objc_msgSend$flushEvents:
+ _objc_msgSend$frozenBagValueWithKey:value:valueType:
+ _objc_msgSend$generateEventFieldsForKeys:
+ _objc_msgSend$generateEventFieldsForKeys:date:
+ _objc_msgSend$globalObject
+ _objc_msgSend$hasProperty:
+ _objc_msgSend$hostName
+ _objc_msgSend$hours
+ _objc_msgSend$iTunesStoreIdentifier
+ _objc_msgSend$idFieldsForTopic:options:
+ _objc_msgSend$identifier
+ _objc_msgSend$identifierForKey:
+ _objc_msgSend$identifierIfExistsForKey:
+ _objc_msgSend$identifierStoreWithAccount:bagNamespace:bag:
+ _objc_msgSend$increment
+ _objc_msgSend$infoDictionary
+ _objc_msgSend$init
+ _objc_msgSend$initWithBag:
+ _objc_msgSend$initWithBag:caller:keyProfile:
+ _objc_msgSend$initWithBlock:
+ _objc_msgSend$initWithBool:
+ _objc_msgSend$initWithCharactersNoCopy:length:deallocator:
+ _objc_msgSend$initWithClientIdentifier:bag:
+ _objc_msgSend$initWithClientIdentifier:keychainAccessGroup:bag:
+ _objc_msgSend$initWithConfiguration:
+ _objc_msgSend$initWithContainerID:bag:
+ _objc_msgSend$initWithData:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$initWithDouble:
+ _objc_msgSend$initWithExplanation:target:attributes:
+ _objc_msgSend$initWithInitialValue:
+ _objc_msgSend$initWithInteger:
+ _objc_msgSend$initWithLongLong:
+ _objc_msgSend$initWithPath:
+ _objc_msgSend$initWithPattern:options:error:
+ _objc_msgSend$initWithRequest:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$initWithTask:metrics:
+ _objc_msgSend$initWithTokenService:
+ _objc_msgSend$initWithTokenService:bag:
+ _objc_msgSend$initWithTopic:
+ _objc_msgSend$initWithURL:
+ _objc_msgSend$initWithURLSession:
+ _objc_msgSend$initWithUnderlyingDictionary:
+ _objc_msgSend$initWithUnsignedInteger:
+ _objc_msgSend$initWithUnsignedLongLong:
+ _objc_msgSend$initWithVirtualMachine:
+ _objc_msgSend$intValue
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$internalInstanceUsingBag:
+ _objc_msgSend$invalidate
+ _objc_msgSend$invalidateSyncWithError:
+ _objc_msgSend$invokeMethod:withArguments:
+ _objc_msgSend$isActiveITunesAccountRequired
+ _objc_msgSend$isArray
+ _objc_msgSend$isBoolean
+ _objc_msgSend$isConstrained
+ _objc_msgSend$isDate
+ _objc_msgSend$isEqualToDictionary:
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$isEqualToObject:
+ _objc_msgSend$isExpired
+ _objc_msgSend$isFinished
+ _objc_msgSend$isInstanceOf:
+ _objc_msgSend$isNull
+ _objc_msgSend$isNumber
+ _objc_msgSend$isObject
+ _objc_msgSend$isOperatingSystemAtLeastVersion:
+ _objc_msgSend$isReusedConnection
+ _objc_msgSend$isString
+ _objc_msgSend$isUndefined
+ _objc_msgSend$isUsingBytecodeCache
+ _objc_msgSend$isValid
+ _objc_msgSend$isValidJSONObject:
+ _objc_msgSend$itemDictionary
+ _objc_msgSend$keyEnumerator
+ _objc_msgSend$loadURLEventPromiseWithContext:
+ _objc_msgSend$localizations
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$localizedStringForKey:value:table:localization:
+ _objc_msgSend$localizedStringForStatusCode:
+ _objc_msgSend$localizedStringsForTable:localization:
+ _objc_msgSend$lock
+ _objc_msgSend$longLongValue
+ _objc_msgSend$mainRunLoop
+ _objc_msgSend$managedValueWithValue:andOwner:
+ _objc_msgSend$monitorsLifecycleEvents
+ _objc_msgSend$moveItemAtURL:toURL:error:
+ _objc_msgSend$mutableCopyWithZone:
+ _objc_msgSend$networkType
+ _objc_msgSend$nonretainedObjectValue
+ _objc_msgSend$numberOfRanges
+ _objc_msgSend$objCType
+ _objc_msgSend$objectForInfoDictionaryKey:
+ _objc_msgSend$originalRequest
+ _objc_msgSend$path
+ _objc_msgSend$pathname
+ _objc_msgSend$pattern
+ _objc_msgSend$performLookupWithBundleIdentifiers:itemIdentifiers:
+ _objc_msgSend$performSelector:withObject:
+ _objc_msgSend$performTreatments:
+ _objc_msgSend$port
+ _objc_msgSend$postNotificationName:object:
+ _objc_msgSend$postNotificationName:object:userInfo:
+ _objc_msgSend$preconnectWithRequest:completionHandler:error:
+ _objc_msgSend$preferredLocalizationsFromArray:forPreferences:
+ _objc_msgSend$processLogArchiveWithPath:startDate:endDate:errorOut:
+ _objc_msgSend$processStream:signatureVerifier:options:error:
+ _objc_msgSend$profile
+ _objc_msgSend$profileVersion
+ _objc_msgSend$promiseForEnqueueingEvents:
+ _objc_msgSend$promiseWithResult:
+ _objc_msgSend$promiseWithTimeout:
+ _objc_msgSend$propertyForBodyKey:
+ _objc_msgSend$propertyListWithData:options:format:error:
+ _objc_msgSend$protocolHandler
+ _objc_msgSend$rangeAtIndex:
+ _objc_msgSend$rangeOfFirstMatchInString:options:range:
+ _objc_msgSend$rangeWithName:
+ _objc_msgSend$readData
+ _objc_msgSend$reason
+ _objc_msgSend$registerBagKeySet:forProfile:profileVersion:
+ _objc_msgSend$removeFromRunLoop:forMode:
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$removeObserver:forKeyPath:context:
+ _objc_msgSend$removeObserver:name:object:
+ _objc_msgSend$removeObserverWithToken:
+ _objc_msgSend$removePropertiesForKeys:
+ _objc_msgSend$replacingSnapshotIfNeeded
+ _objc_msgSend$request
+ _objc_msgSend$requestByEncodingRequest:parameters:
+ _objc_msgSend$requestStartDate
+ _objc_msgSend$reset
+ _objc_msgSend$resetIDForTopics:
+ _objc_msgSend$resetInterval
+ _objc_msgSend$resolveWithTimeout:
+ _objc_msgSend$resourceFetchType
+ _objc_msgSend$response
+ _objc_msgSend$responseCorrelationId
+ _objc_msgSend$responseEndDate
+ _objc_msgSend$responseHeaders
+ _objc_msgSend$responseStartDate
+ _objc_msgSend$responseStatusCode
+ _objc_msgSend$resultWithCompletion:
+ _objc_msgSend$resume
+ _objc_msgSend$scheduleInRunLoop:forMode:
+ _objc_msgSend$scriptOfType:memoryMappedFromASCIIFile:withSourceURL:andBytecodeCache:inVirtualMachine:error:
+ _objc_msgSend$searchForServicesOfType:inDomain:
+ _objc_msgSend$seconds
+ _objc_msgSend$secureConnectionStartDate
+ _objc_msgSend$serverTimeFromDate:
+ _objc_msgSend$serverTimeFromTimeInterval:
+ _objc_msgSend$session
+ _objc_msgSend$sessionWithConfiguration:
+ _objc_msgSend$setAccount:
+ _objc_msgSend$setAlwaysIncludeAuthKitHeaders:
+ _objc_msgSend$setAlwaysIncludeMMeClientInfoAndDeviceHeaders:
+ _objc_msgSend$setAnisetteType:
+ _objc_msgSend$setAnonymous:
+ _objc_msgSend$setAttributes:ofItemAtPath:error:
+ _objc_msgSend$setBag:
+ _objc_msgSend$setBeginEventProcessingBlock:
+ _objc_msgSend$setCalendar:
+ _objc_msgSend$setClientInfo:
+ _objc_msgSend$setData:
+ _objc_msgSend$setDataSegmentFound:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setDateStyle:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setDialogOptions:
+ _objc_msgSend$setDisableResponseDecoding:
+ _objc_msgSend$setDoesRelativeDateFormatting:
+ _objc_msgSend$setDomain:
+ _objc_msgSend$setEndEventProcessingBlock:
+ _objc_msgSend$setError:
+ _objc_msgSend$setException:
+ _objc_msgSend$setExceptionHandler:
+ _objc_msgSend$setExcludeIdentifierHeadersForAccount:
+ _objc_msgSend$setExpirationDate:
+ _objc_msgSend$setFileEntryFound:
+ _objc_msgSend$setFormatterBehavior:
+ _objc_msgSend$setFormattingContext:
+ _objc_msgSend$setGsTokenIdentifier:
+ _objc_msgSend$setIdentifier:forKey:
+ _objc_msgSend$setIncludeClientVersions:
+ _objc_msgSend$setInspectable:
+ _objc_msgSend$setIntervalCompletionProcessingBlock:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setIsActiveITunesAccountRequired:
+ _objc_msgSend$setKeyForIdentifier:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$setLocalizedDateFormatFromTemplate:
+ _objc_msgSend$setMaximumFractionDigits:
+ _objc_msgSend$setMescalType:
+ _objc_msgSend$setMinimumFractionDigits:
+ _objc_msgSend$setMonitorsLifecycleEvents:
+ _objc_msgSend$setName:
+ _objc_msgSend$setNumberStyle:
+ _objc_msgSend$setPlatform:
+ _objc_msgSend$setPreventSampling:
+ _objc_msgSend$setProcessInfo:
+ _objc_msgSend$setProfile:
+ _objc_msgSend$setProfileVersion:
+ _objc_msgSend$setProtocolHandler:
+ _objc_msgSend$setQuality:
+ _objc_msgSend$setQualityOfService:
+ _objc_msgSend$setRequestEncoding:
+ _objc_msgSend$setResetInterval:
+ _objc_msgSend$setResponseBody:
+ _objc_msgSend$setResponseDecoder:
+ _objc_msgSend$setSession:
+ _objc_msgSend$setSizeHint:
+ _objc_msgSend$setSubsystemCategoryFilter:
+ _objc_msgSend$setTimeStyle:
+ _objc_msgSend$setTimeZone:
+ _objc_msgSend$setUrlKnownToBeTrusted:
+ _objc_msgSend$setValue:atIndex:
+ _objc_msgSend$setValue:forProperty:
+ _objc_msgSend$setVersion:
+ _objc_msgSend$set_maxCacheableEntrySizeRatio:
+ _objc_msgSend$set_preconnect:
+ _objc_msgSend$set_timingDataOptions:
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$sharedSession
+ _objc_msgSend$sharedURLCache
+ _objc_msgSend$shortValue
+ _objc_msgSend$shouldCollectMetricsPromiseForContext:
+ _objc_msgSend$signatureVerifierWithCertificate:
+ _objc_msgSend$signpostId
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$statusCode
+ _objc_msgSend$stop
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$stringFromByteCount:countStyle:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$stringFromNumber:
+ _objc_msgSend$task
+ _objc_msgSend$taskMetrics
+ _objc_msgSend$temporaryDirectory
+ _objc_msgSend$threadDictionary
+ _objc_msgSend$toBool
+ _objc_msgSend$toDate
+ _objc_msgSend$toDictionary
+ _objc_msgSend$toDouble
+ _objc_msgSend$toInt32
+ _objc_msgSend$toNumber
+ _objc_msgSend$toObject
+ _objc_msgSend$toPoint
+ _objc_msgSend$toRange
+ _objc_msgSend$toRect
+ _objc_msgSend$toSize
+ _objc_msgSend$toString
+ _objc_msgSend$toUInt32
+ _objc_msgSend$tokenService
+ _objc_msgSend$transactionMetrics
+ _objc_msgSend$underlyingDictionary
+ _objc_msgSend$underlyingErrors
+ _objc_msgSend$uninitializedToken
+ _objc_msgSend$unionBagKeySet:
+ _objc_msgSend$unlock
+ _objc_msgSend$unsafeIgnoreSignatureVerifier
+ _objc_msgSend$unsignedCharValue
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$unsignedShortValue
+ _objc_msgSend$userAgentForProcessInfo:
+ _objc_msgSend$valueAtIndex:
+ _objc_msgSend$valueForHTTPHeaderField:
+ _objc_msgSend$valueForProperty:
+ _objc_msgSend$valuePromise
+ _objc_msgSend$valueWithBool:inContext:
+ _objc_msgSend$valueWithDouble:inContext:
+ _objc_msgSend$valueWithError:
+ _objc_msgSend$valueWithInt32:inContext:
+ _objc_msgSend$valueWithJSValueRef:inContext:
+ _objc_msgSend$valueWithNewErrorFromMessage:inContext:
+ _objc_msgSend$valueWithNewObjectInContext:
+ _objc_msgSend$valueWithNewPromiseInContext:fromExecutor:
+ _objc_msgSend$valueWithNonretainedObject:
+ _objc_msgSend$valueWithNullInContext:
+ _objc_msgSend$valueWithObject:inContext:
+ _objc_msgSend$valueWithPoint:inContext:
+ _objc_msgSend$valueWithRange:inContext:
+ _objc_msgSend$valueWithRect:inContext:
+ _objc_msgSend$valueWithSize:inContext:
+ _objc_msgSend$valueWithUInt32:inContext:
+ _objc_msgSend$valueWithUndefinedInContext:
+ _objc_msgSend$virtualMachine
+ _objc_msgSend$weakObjectsHashTable
+ _objc_msgSend$writeStream:toDirectory:error:
+ _objc_msgSend$writeToFile:blockSize:error:
+ _objectdestroy.123Tm
+ _objectdestroy.195Tm
+ _objectdestroy.202Tm
+ _objectdestroy.208Tm
+ _objectdestroy.211Tm
+ _objectdestroy.24Tm
+ _objectdestroy.253Tm
+ _objectdestroy.256Tm
+ _objectdestroy.259Tm
+ _objectdestroy.263Tm
+ _objectdestroy.285Tm
+ _objectdestroy.306Tm
+ _objectdestroy.313Tm
+ _objectdestroy.317Tm
+ _objectdestroy.369Tm
+ _objectdestroy.383Tm
+ _objectdestroy.393Tm
+ _objectdestroy.410Tm
+ _objectdestroy.424Tm
+ _objectdestroy.452Tm
+ _objectdestroy.50Tm
+ _objectdestroy.73Tm
+ _swift_task_immediate
+ _swift_task_isCurrentExecutorWithFlags
+ _symbolic $s9JetEngine11BagProviderP
+ _symbolic $s9JetEngine21PushChannelStateStoreP
+ _symbolic S2SIeghgg_
+ _symbolic S2SytIeghnnr_
+ _symbolic SDySS_____G 9JetEngine21NotificationsListenerC
+ _symbolic SDy__________G 10Foundation4UUIDV 9JetEngine0C18PackReloadObserverC13ListenerEntry33_5061A21CB35A734507373825AFBA7679LLV
+ _symbolic SS8fileName_SS8cacheKeyt
+ _symbolic SSSgIegn_
+ _symbolic SS_____Ieggy_ s5Int32V
+ _symbolic Say_____GSg 10Foundation3URLV
+ _symbolic So13AMSURLSessionCSg
+ _symbolic So24JEURLSessionPreconnecterC
+ _symbolic _____ 10Foundation4UUIDV
+ _symbolic _____ 9JetEngine0A18PackReloadObserverC
+ _symbolic _____ 9JetEngine0A18PackReloadObserverC0E5State33_5061A21CB35A734507373825AFBA7679LLV
+ _symbolic _____ 9JetEngine0A18PackReloadObserverC13ListenerEntry33_5061A21CB35A734507373825AFBA7679LLV
+ _symbolic _____ 9JetEngine0A18PackReloadObserverC13ListenerTokenC
+ _symbolic _____ 9JetEngine0A22PackReloadNotificationV
+ _symbolic _____ 9JetEngine21NotificationsListenerC
+ _symbolic _____ 9JetEngine22PushChannelStateRecordV
+ _symbolic _____ 9JetEngine22PushChannelStateRecordV10CodingKeys33_7674369818C74462B0012F4D78C73DD4LLO
+ _symbolic _____ 9JetEngine22ReloadNotificationTypeO
+ _symbolic _____ 9JetEngine27PushChannelStateSQLiteStoreV
+ _symbolic _____ 9JetEngine3BagV0C15SoftwareVersionO
+ _symbolic _____ 9JetEngine7JSErrorV4KindO
+ _symbolic _____11columnIndex_t s5Int32V
+ _symbolic _____Sg 9JetEngine0A36PackSandboxExtensionFileStreamSourceV
+ _symbolic _____SgXw 9JetEngine0A18PackReloadObserverC
+ _symbolic _____SgXwz_Xx 9JetEngine0A18PackReloadObserverC
+ _symbolic _____Sg_ABt s6MirrorV12DisplayStyleO
+ _symbolic _____Sg______p______pIegnrzo_ 9JetEngine10JSONObjectV AA39MetricsEventLinterConfigurationProviderP s5ErrorP
+ _symbolic ___________t 10Foundation4UUIDV 9JetEngine0C18PackReloadObserverC13ListenerEntry33_5061A21CB35A734507373825AFBA7679LLV
+ _symbolic ______pSg 9JetEngine11BagProviderP
+ _symbolic _____ySDySS_____GG 2os21OSAllocatedUnfairLockV s5Int32V
+ _symbolic _____ySDySS_____G_____G s13ManagedBufferCsRi__rlE s5Int32V So16os_unfair_lock_sV
+ _symbolic _____ySS8fileName_SS8cacheKeytG s23_ContiguousArrayStorageC
+ _symbolic _____ySSSg_G 9JetEngine7PromiseC8Observer029_379DCD89C1164EFF4D1BDB8B7B92K1ALLO
+ _symbolic _____ySS_____G s18_DictionaryStorageC 9JetEngine21NotificationsListenerC
+ _symbolic _____ySS_______ptG s23_ContiguousArrayStorageC 9JetEngine23InspectableMetricsEventP
+ _symbolic _____ySaySS8fileName_SS8cacheKeytGG 2os21OSAllocatedUnfairLockV
+ _symbolic _____ySaySS8fileName_SS8cacheKeytG_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic _____y_____G 2os21OSAllocatedUnfairLockV 9JetEngine0E18PackReloadObserverC0I5State33_5061A21CB35A734507373825AFBA7679LLV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 9JetEngine22PushChannelStateRecordV10CodingKeys33_7674369818C74462B0012F4D78C73DD4LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 9JetEngine22PushChannelStateRecordV10CodingKeys33_7674369818C74462B0012F4D78C73DD4LLO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 9JetEngine0D18PackReloadObserverC13ListenerEntry33_5061A21CB35A734507373825AFBA7679LLV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 9JetEngine22PushChannelStateRecordV
+ _symbolic _____y__________G s13ManagedBufferCsRi__rlE 9JetEngine0C18PackReloadObserverC0G5State33_5061A21CB35A734507373825AFBA7679LLV So16os_unfair_lock_sV
+ _symbolic _____y__________G s18_DictionaryStorageC 10Foundation4UUIDV 9JetEngine0E18PackReloadObserverC13ListenerEntry33_5061A21CB35A734507373825AFBA7679LLV
+ _symbolic _____y_____ySSSg_GG s23_ContiguousArrayStorageC 9JetEngine7PromiseC8Observer029_379DCD89C1164EFF4D1BDB8B7B92N1ALLO
+ _symbolic _____y_____y_____Sg_GG s23_ContiguousArrayStorageC 9JetEngine7PromiseC8Observer029_379DCD89C1164EFF4D1BDB8B7B92N1ALLO AC10JSONObjectV
+ _symbolic _____yySSYbcG s23_ContiguousArrayStorageC
+ _symbolic _____yySS_SStYbcSgG 2os21OSAllocatedUnfairLockV
+ _symbolic _____yySS_SStYbcSg_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic xq_Ri_zRi0_zRi__Ri0__r0_lySSytIseghnr_Sg
+ _symbolic ySSYbc
+ _symbolic yt_____y______pGIegno_ 9JetEngine7PromiseC AA39MetricsEventLinterConfigurationProviderP
+ _type_layout_string 9JetEngine0A18PackReloadObserverC0E5State33_5061A21CB35A734507373825AFBA7679LLV
+ _type_layout_string 9JetEngine0A18PackReloadObserverC13ListenerEntry33_5061A21CB35A734507373825AFBA7679LLV
+ _type_layout_string 9JetEngine22PushChannelStateRecordV
+ _type_layout_string 9JetEngine27PushChannelStateSQLiteStoreV
- ___swift_memcpy104_8
- ___swift_memcpy145_8
- __swift_FORCE_LOAD_$_swiftCompression
- __swift_FORCE_LOAD_$_swiftCompression_$_JetEngine
- _associated conformance 9JetEngine20SQLiteStatementErrorOSHAASQ
- _block_copy_helper.281
- _block_copy_helper.289
- _block_copy_helper.297
- _block_copy_helper.303
- _block_copy_helper.311
- _block_copy_helper.318
- _block_copy_helper.345
- _block_copy_helper.349
- _block_copy_helper.354
- _block_copy_helper.357
- _block_copy_helper.365
- _block_copy_helper.373
- _block_copy_helper.380
- _block_copy_helper.388
- _block_copy_helper.398
- _block_copy_helper.41
- _block_copy_helper.413
- _block_copy_helper.435
- _block_copy_helper.44
- _block_copy_helper.447
- _block_copy_helper.455
- _block_copy_helper.463
- _block_copy_helper.471
- _block_copy_helper.479
- _block_copy_helper.487
- _block_copy_helper.495
- _block_copy_helper.503
- _block_copy_helper.511
- _block_copy_helper.519
- _block_copy_helper.533
- _block_copy_helper.69
- _block_copy_helper.75
- _block_copy_helper.92
- _block_copy_helper.98
- _block_descriptor.100
- _block_descriptor.283
- _block_descriptor.291
- _block_descriptor.299
- _block_descriptor.305
- _block_descriptor.313
- _block_descriptor.320
- _block_descriptor.347
- _block_descriptor.351
- _block_descriptor.356
- _block_descriptor.359
- _block_descriptor.367
- _block_descriptor.375
- _block_descriptor.382
- _block_descriptor.390
- _block_descriptor.400
- _block_descriptor.415
- _block_descriptor.43
- _block_descriptor.437
- _block_descriptor.449
- _block_descriptor.457
- _block_descriptor.46
- _block_descriptor.465
- _block_descriptor.473
- _block_descriptor.481
- _block_descriptor.489
- _block_descriptor.497
- _block_descriptor.505
- _block_descriptor.513
- _block_descriptor.521
- _block_descriptor.535
- _block_descriptor.71
- _block_descriptor.77
- _block_descriptor.94
- _block_destroy_helper.282
- _block_destroy_helper.290
- _block_destroy_helper.298
- _block_destroy_helper.304
- _block_destroy_helper.312
- _block_destroy_helper.319
- _block_destroy_helper.346
- _block_destroy_helper.350
- _block_destroy_helper.355
- _block_destroy_helper.358
- _block_destroy_helper.366
- _block_destroy_helper.374
- _block_destroy_helper.381
- _block_destroy_helper.389
- _block_destroy_helper.399
- _block_destroy_helper.414
- _block_destroy_helper.42
- _block_destroy_helper.436
- _block_destroy_helper.448
- _block_destroy_helper.45
- _block_destroy_helper.456
- _block_destroy_helper.464
- _block_destroy_helper.472
- _block_destroy_helper.480
- _block_destroy_helper.488
- _block_destroy_helper.496
- _block_destroy_helper.504
- _block_destroy_helper.512
- _block_destroy_helper.520
- _block_destroy_helper.534
- _block_destroy_helper.70
- _block_destroy_helper.76
- _block_destroy_helper.93
- _block_destroy_helper.99
- _get_type_metadata 15Synchronization5MutexVySDy9JetEngine12DiskPropertyOAD06CachedeF033_3D988632E755F3184F7A0396680788AELLVGG.2
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_release_x10
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x7
- _objectdestroy.13Tm
- _objectdestroy.153Tm
- _objectdestroy.181Tm
- _objectdestroy.188Tm
- _objectdestroy.194Tm
- _objectdestroy.197Tm
- _objectdestroy.236Tm
- _objectdestroy.239Tm
- _objectdestroy.246Tm
- _objectdestroy.268Tm
- _objectdestroy.26Tm
- _objectdestroy.289Tm
- _objectdestroy.296Tm
- _objectdestroy.303Tm
- _objectdestroy.316Tm
- _objectdestroy.337Tm
- _objectdestroy.340Tm
- _objectdestroy.34Tm
- _objectdestroy.35Tm
- _objectdestroy.375Tm
- _objectdestroy.385Tm
- _objectdestroy.402Tm
- _objectdestroy.40Tm
- _objectdestroy.416Tm
- _objectdestroy.441Tm
- _objectdestroy.62Tm
- _objectdestroy.85Tm
- _swift_deallocBox
- _symbolic SSSg______pIegHozo_ s5ErrorP
- _symbolic ____________pt s11AnyHashableV 9JetEngine15PipelineBackoffP
- _symbolic ______pIegHzo_ s5ErrorP
- _symbolic _____z_Xx 9JetEngine0A9PackAssetV
- _symbolic ySSYbcSg
CStrings:
+ " already had is_system_client column"
+ " but no cacheKey mapping found"
+ " eviction listeners of evicted assets"
+ " reload listener with ID: "
+ " reload listeners for cacheKey: "
+ " reload notification for UUID: "
+ " reload notification received for UUID: "
+ ", listening for both override and regular notifications"
+ ", skipping duplicate setup"
+ "@\"NSURLSession\""
+ "ALTER TABLE push_subscription ADD COLUMN is_system_client INTEGER NOT NULL DEFAULT(0) CHECK (is_system_client IN (0, 1))"
+ "Already observing UUID: "
+ "Asset was not retrieved from daemon (streamSource is not JetPackSandboxExtensionFileStreamSource), skipping eviction observation"
+ "AssetPushSubscriptionSQLiteStore DB migration to v3"
+ "AssetPushSubscriptionSQLiteStore DB migration to v3 - additional UPDATE for internal builds"
+ "Automatically setting up eviction observation for UUID: "
+ "B40@0:8@16@?24^@32"
+ "CREATE TABLE IF NOT EXISTS push_channel_state (\n    channel_id TEXT PRIMARY KEY NOT NULL,\n    checkpoint INTEGER NOT NULL,\n    last_push_received_at INTEGER,\n    modified_at INTEGER NOT NULL DEFAULT(STRFTIME('%s', 'now'))\n)"
+ "Cache eviction listener called for: "
+ "Canceled notifications for "
+ "Cannot observe asset eviction: unable to extract UUID from file path: "
+ "DELETE FROM push_channel_state WHERE channel_id = "
+ "Expected `Function`, but got `"
+ "Expected `JSON`, but got `"
+ "Expected `Promise`, but got `"
+ "Expected `Service`, but got `"
+ "Failed to cancel notifications for "
+ "Failed to subscribe to notifications for "
+ "Failed to update is_system_client flag for known system clients: "
+ "INSERT INTO push_subscription (asset_url, channel_id, bundle_id, usage_id, is_system_client) VALUES ("
+ "INSERT OR REPLACE INTO push_channel_state (channel_id, checkpoint, last_push_received_at, modified_at) VALUES ("
+ "JEErrorDomain"
+ "JEURLSessionPreconnecter"
+ "JetEarlyBootstrap error: "
+ "JetEngine"
+ "JetPackAssetDiskCache.notifyEvictions() called"
+ "JetPackAssetDiskCache.notifyEvictions(): Evictions are empty, nothing to notify"
+ "JetPackAssetDiskCache.notifyEvictions(): Listener not found, early return"
+ "Received JetPack reload notification for UUID "
+ "Received notification for "
+ "Removed reload listener with ID: "
+ "SELECT * FROM push_channel_state ORDER BY channel_id"
+ "SELECT * FROM push_subscription WHERE channel_id IN "
+ "SELECT checkpoint FROM push_channel_state WHERE channel_id = "
+ "Setting up observer for UUID: "
+ "Stopped observing JetPack reload for UUID: "
+ "Stopped observing JetPack reload for all assets, removed "
+ "Successfully subscribed to notifications for "
+ "Tracked eviction of UUID: "
+ "UPDATE push_channel_state SET checkpoint = "
+ "UPDATE push_subscription SET is_system_client = 1 WHERE bundle_id IN ('com.apple.jetpackctl', 'com.apple.appstorecomponentsd')"
+ "Unknown error"
+ "[URLSessionPreconnecter] preconnect threw error: url="
+ "[URLSessionPreconnecter] preconnectV3 failed: "
+ "[URLSessionPreconnecter] preconnectV3 falling back to default hosts"
+ "[URLSessionPreconnecter] preconnectV3 fetching network bag"
+ "[URLSessionPreconnecter] preconnectV3 found no hosts"
+ "[URLSessionPreconnecter] preconnectV3 using default hosts"
+ "[URLSessionPreconnecter] preconnectV3 using disk bag"
+ "[URLSessionPreconnecter] preconnectV3 using network bag"
+ "_TtC9JetEngine21JetPackReloadObserver"
+ "_TtC9JetEngine21NotificationsListener"
+ "_TtCC9JetEngine21JetPackReloadObserver13ListenerToken"
+ "_session"
+ "com.apple.JetEngine.JetPackReloadObserver"
+ "com.apple.jetpackassetd.reload."
+ "com.apple.jetpackassetd.reload.override."
+ "errorWithDomain:code:userInfo:"
+ "evictedUUIDs"
+ "evictionListenerLock"
+ "initWithURLSession:"
+ "is_system_client"
+ "lastPushReceivedAt"
+ "last_push_received_at"
+ "notificationQueue"
+ "observer"
+ "override"
+ "preconnectWithRequest:completionHandler:error:"
+ "reason"
+ "regular"
+ "source=defaults"
+ "source=disk"
+ "source=error"
+ "source=network"
+ "source=none"
+ "stackReplaceWithoutAnimation"
+ "tokenLookup"
- "' must be provided lazily in object graph."
- "' which are not present in object graph."
- "Cannot eagerly load types '"
- "Error getting personality for "
- "INSERT INTO push_subscription (asset_url, channel_id, bundle_id, usage_id) VALUES ("
- "JetEngine/JetEarlyBootstrap.swift"

```
