## libSecureMAHelper.dylib

> `/usr/lib/libSecureMAHelper.dylib`

```diff

-1837.40.40.0.0
-  __TEXT.__text: 0x1046c
-  __TEXT.__auth_stubs: 0x9a0
-  __TEXT.__objc_methlist: 0x614
-  __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x2699
-  __TEXT.__oslogstring: 0x1bc6
-  __TEXT.__gcc_except_tab: 0x758
-  __TEXT.__unwind_info: 0x2e0
-  __TEXT.__objc_classname: 0xca
-  __TEXT.__objc_methname: 0x11fe
-  __TEXT.__objc_methtype: 0x3f3
-  __TEXT.__objc_stubs: 0x13c0
-  __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x3b0
-  __DATA_CONST.__objc_classlist: 0x18
+1837.40.63.0.0
+  __TEXT.__text: 0x201f4
+  __TEXT.__auth_stubs: 0xcb0
+  __TEXT.__objc_methlist: 0x74c
+  __TEXT.__const: 0x530
+  __TEXT.__cstring: 0x7643
+  __TEXT.__oslogstring: 0x31ce
+  __TEXT.__gcc_except_tab: 0xb4c
+  __TEXT.__unwind_info: 0x568
+  __TEXT.__objc_classname: 0x106
+  __TEXT.__objc_methname: 0x1c7c
+  __TEXT.__objc_methtype: 0x4ea
+  __TEXT.__objc_stubs: 0x1fa0
+  __DATA_CONST.__got: 0x298
+  __DATA_CONST.__const: 0xea8
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x608
+  __DATA_CONST.__objc_selrefs: 0x918
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x4e0
-  __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x2d00
-  __AUTH_CONST.__objc_const: 0x620
-  __AUTH_CONST.__objc_intobj: 0x4f8
-  __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x24
-  __DATA.__data: 0x180
-  __DATA.__bss: 0xa8
+  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_arraydata: 0x2e8
+  __AUTH_CONST.__auth_got: 0x668
+  __AUTH_CONST.__const: 0x4f0
+  __AUTH_CONST.__cfstring: 0x7fe0
+  __AUTH_CONST.__objc_const: 0x840
+  __AUTH_CONST.__objc_intobj: 0x8a0
+  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x34
+  __DATA.__data: 0x238
+  __DATA.__bss: 0x258
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 925245EB-074F-34FA-8C0B-5D87A3205699
-  Functions: 170
-  Symbols:   894
-  CStrings:  1149
+  UUID: BB88236C-C8D9-31DF-AAA0-5B0C894674C0
+  Functions: 448
+  Symbols:   1566
+  CStrings:  2710
 
Symbols:
+ +[SecureMobileAssetBundle clearBootTaskPlist:]
+ +[SecureMobileAssetBundle getBootTaskPlistLock]
+ +[SecureMobileAssetBundle getBootTaskPlistLock].cold.1
+ +[SecureMobileAssetBundle isErrorDueToDeviceBeingLocked:]
+ +[SecureMobileAssetBundle readBootTaskPlist:]
+ +[SecureMobileAssetManifestVerifier sharedInstance]
+ +[SecureMobileAssetManifestVerifier sharedInstance].cold.1
+ -[MASecureMobileAssetTypes supportsLoadableTrustCache:]
+ -[SMABundleAccessOptions .cxx_destruct]
+ -[SMABundleAccessOptions flags]
+ -[SMABundleAccessOptions init]
+ -[SMABundleAccessOptions pathsToPurgeOnGraftFailureInEarlyBootTask]
+ -[SMABundleAccessOptions setFlags:]
+ -[SMABundleAccessOptions setPathsToPurgeOnGraftFailureInEarlyBootTask:]
+ -[SecureMAHelper clearBootTaskPlist]
+ -[SecureMAHelper copyBootTaskPlist:]
+ -[SecureMobileAssetBundle _beginAccessWithOptions_nowait:accessMechanismPtr:errorPtr:]
+ -[SecureMobileAssetBundle _manifestDataFromStoredTicket:manifestType:]
+ -[SecureMobileAssetBundle _queryNonceForHandle:domain:digest:error:]
+ -[SecureMobileAssetBundle _storeManifest:manifestType:stage:error:]
+ -[SecureMobileAssetBundle beginAccessWithOptions:accessMechanismPtr:errorPtr:]
+ -[SecureMobileAssetBundle endAccessWithOptions:accessMechanismPtr:errorPtr:]
+ -[SecureMobileAssetBundle endAccessWithOptions_nowait:accessMechanismPtr:errorPtr:]
+ -[SecureMobileAssetBundle graftOrMount:graftingError:]
+ -[SecureMobileAssetBundle graftOrMount:graftingError:].cold.1
+ -[SecureMobileAssetBundle loadTrustCache:]
+ -[SecureMobileAssetBundle manifestType]
+ -[SecureMobileAssetBundle manifestVerifier]
+ -[SecureMobileAssetBundle recordAssetGraftStateForEarlyBootTask:options:]
+ -[SecureMobileAssetBundle recordAssetGraftStateForEarlyBootTask:options:].cold.1
+ -[SecureMobileAssetBundle secureMountAuthType]
+ -[SecureMobileAssetBundle setManifestVerifier:]
+ -[SecureMobileAssetBundle ungraftOrUnmount:ungraftingError:]
+ -[SecureMobileAssetManifestVerifier .cxx_destruct]
+ -[SecureMobileAssetManifestVerifier _logBase64Data:description:]
+ -[SecureMobileAssetManifestVerifier _manifestDigest:]
+ -[SecureMobileAssetManifestVerifier _verifyPlist:manifest:manifestType:result:]
+ -[SecureMobileAssetManifestVerifier cachedManifestVerificationResults]
+ -[SecureMobileAssetManifestVerifier init]
+ -[SecureMobileAssetManifestVerifier setCachedManifestVerificationResults:]
+ -[SecureMobileAssetManifestVerifier verifyManifest:manifestType:]
+ -[SecureMobileAssetManifestVerifier verifyPlist:manifest:manifestType:result:error:]
+ GCC_except_table111
+ GCC_except_table116
+ GCC_except_table19
+ GCC_except_table3
+ GCC_except_table33
+ GCC_except_table4
+ GCC_except_table42
+ GCC_except_table46
+ GCC_except_table51
+ GCC_except_table53
+ GCC_except_table56
+ GCC_except_table57
+ GCC_except_table58
+ GCC_except_table61
+ GCC_except_table63
+ GCC_except_table76
+ GCC_except_table79
+ GCC_except_table94
+ GCC_except_table95
+ GCC_except_table96
+ _BootSessionUUID
+ _BootSessionUUID.cold.1
+ _BootSessionUUID.onceSessionBootUUID
+ _BootSessionUUID.stringValue
+ _CC_SHA1
+ _CC_SHA1_Final
+ _CC_SHA1_Init
+ _CC_SHA1_Update
+ _CC_SHA256
+ _CC_SHA256_Final
+ _CC_SHA256_Init
+ _CC_SHA256_Update
+ _CC_SHA384
+ _CFArrayGetCount
+ _CFArrayGetCountOfValue
+ _CFArrayGetTypeID
+ _CFArrayGetValueAtIndex
+ _CFDateGetAbsoluteTime
+ _CFDateGetTypeID
+ _CFDictionaryGetCount
+ _CFDictionaryGetKeysAndValues
+ _CFDictionaryGetTypeID
+ _CFDictionaryGetValue
+ _CFNumberGetValue
+ _CFStringGetCString
+ _CFStringGetLength
+ _CFStringGetMaximumSizeForEncoding
+ _MAError
+ _MAErrorForCancelDownloadResultWithUnderlying
+ _MAErrorForDownloadResultWithUnderlying
+ _MAErrorWithUnderlying
+ _MAErrorWithUnderlyingAndString
+ _MAErrorWithUnderlyingUserInfoAndString
+ _MAMeasurementHashAlgorithmSHA1
+ _MKBDeviceLockAssertion
+ _NSFilePathErrorKey
+ _NSKeyedArchiveRootObjectKey
+ _NSLocalizedDescriptionKey
+ _NSURLErrorDomain
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateComponents
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_NSTimeZone
+ _OBJC_CLASS_$_SMABundleAccessOptions
+ _OBJC_CLASS_$_SecureMobileAssetManifestVerifier
+ _OBJC_IVAR_$_SMABundleAccessOptions._flags
+ _OBJC_IVAR_$_SMABundleAccessOptions._pathsToPurgeOnGraftFailureInEarlyBootTask
+ _OBJC_IVAR_$_SecureMobileAssetBundle._manifestVerifier
+ _OBJC_IVAR_$_SecureMobileAssetManifestVerifier._cachedManifestVerificationResults
+ _OBJC_METACLASS_$_SMABundleAccessOptions
+ _OBJC_METACLASS_$_SecureMobileAssetManifestVerifier
+ __MABufferToHexString
+ __MAPreferencesIsCentralizedCacheDeleteEnabled
+ __MAPreferencesIsCentralizedCacheDeleteEnabled._centralizedCacheDeleteEnabled
+ __MAPreferencesIsCentralizedCacheDeleteEnabled.cold.1
+ __MAPreferencesIsCentralizedCacheDeleteEnabled.onceToken
+ __MAPreferencesIsVerboseLoggingEnabled
+ __MAPreferencesIsVerboseLoggingEnabled._verboseLoggingEnabled
+ __MAPreferencesIsVerboseLoggingEnabled.cold.1
+ __MAPreferencesIsVerboseLoggingEnabled.onceToken
+ __MobileAssetHashAssetData
+ __MobileAssetHashAssetDataNoLegacy
+ __MobileAssetHashAssetDataOptCompatibility
+ __OBJC_$_CLASS_METHODS_SecureMobileAssetManifestVerifier
+ __OBJC_$_INSTANCE_METHODS_SMABundleAccessOptions
+ __OBJC_$_INSTANCE_METHODS_SecureMobileAssetManifestVerifier
+ __OBJC_$_INSTANCE_VARIABLES_SMABundleAccessOptions
+ __OBJC_$_INSTANCE_VARIABLES_SecureMobileAssetManifestVerifier
+ __OBJC_$_PROP_LIST_SMABundleAccessOptions
+ __OBJC_$_PROP_LIST_SecureMobileAssetManifestVerifier
+ __OBJC_CLASS_RO_$_SMABundleAccessOptions
+ __OBJC_CLASS_RO_$_SecureMobileAssetManifestVerifier
+ __OBJC_METACLASS_RO_$_SMABundleAccessOptions
+ __OBJC_METACLASS_RO_$_SecureMobileAssetManifestVerifier
+ ___47+[SecureMobileAssetBundle getBootTaskPlistLock]_block_invoke
+ ___51+[SecureMobileAssetManifestVerifier sharedInstance]_block_invoke
+ ___54-[SecureMAHelper graftSecureAssetsFromLastBootSession]_block_invoke
+ ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1269
+ ___BootSessionUUID_block_invoke
+ ___NSArray0__struct
+ ____MAPreferencesIsCentralizedCacheDeleteEnabled_block_invoke
+ ____MAPreferencesIsCentralizedCacheDeleteEnabled_block_invoke.cold.1
+ ____MAPreferencesIsVerboseLoggingEnabled_block_invoke
+ ____MAPreferencesIsVerboseLoggingEnabled_block_invoke.cold.1
+ ___assetIdDisallowedCharacterSet_block_invoke
+ ___assetTypeDisallowedCharacterSet_block_invoke
+ ___attributesInAssetIdWithUnderscore_block_invoke
+ ___attributesInDownloadContent_block_invoke
+ ___attributesInDownloadPolicy_block_invoke
+ ___attributesInDownloadUrl_block_invoke
+ ___attributesInPallasDynamicAssetId_block_invoke
+ ___block_descriptor_160_e8_32s40s48s56s64s72r80r88r96r104r112r120r128r136r144r152r_e25_B24?08"NSDictionary"16ls32l8r72l8r80l8s40l8r88l8r96l8r104l8r112l8s48l8s56l8r120l8r128l8s64l8r136l8r144l8r152l8
+ ___block_descriptor_48_e8_32s40r_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8r40l8
+ ___block_literal_global.1125
+ ___block_literal_global.1131
+ ___block_literal_global.1169
+ ___block_literal_global.1175
+ ___block_literal_global.1180
+ ___block_literal_global.1185
+ ___block_literal_global.1190
+ ___block_literal_global.1195
+ ___block_literal_global.1214
+ ___block_literal_global.1255
+ ___block_literal_global.1264
+ ___block_literal_global.1307
+ ___block_literal_global.1378
+ ___block_literal_global.1383
+ ___block_literal_global.1385
+ ___block_literal_global.1432
+ ___block_literal_global.1438
+ ___block_literal_global.1443
+ ___block_literal_global.1454
+ ___block_literal_global.1459
+ ___block_literal_global.1481
+ ___block_literal_global.1712
+ ___block_literal_global.2268
+ ___block_literal_global.2822
+ ___block_literal_global.2824
+ ___block_literal_global.2826
+ ___block_literal_global.2828
+ ___block_literal_global.2830
+ ___block_literal_global.2869
+ ___block_literal_global.2872
+ ___filterPMV_block_invoke
+ ___getPreallocatedSpaceAllowedTypes_block_invoke
+ ___getSoftwareUpdateBrainTypes_block_invoke
+ ___getSoftwareUpdateTypes_block_invoke
+ ___getSupportedAnalyticsEventFields_block_invoke
+ ___isSSONeededForURL_block_invoke
+ ___plistDecodeClasses_block_invoke
+ ___plistMutableDecodeClasses_block_invoke
+ ___purposeDisallowedCharacterSet_block_invoke
+ ___purposeIgnoredCharacterSet_block_invoke
+ ___runningInDeviceRecoveryEnvironment_block_invoke
+ ___suAssetTypes_block_invoke
+ ___supportedAssetFormatsArray_block_invoke
+ ___supportedAssetFormats_block_invoke
+ ___tokenFileDisallowedCharacterSet_block_invoke
+ ___urlSupportsAuthenticatedPallas_block_invoke
+ ___usingCentralizedCachedelete_block_invoke
+ __hashCFArray
+ __hashCFDictionary
+ __hashCFNumber
+ __hashCFString
+ __hashCFString.cold.1
+ __hashCFString.cold.2
+ __hashCFString.cold.3
+ __hashCFType
+ __hashCFType.cold.1
+ __image4_trust_evaluation_preflight
+ __manifest_trust_callback
+ __query_nonce_callback
+ _abort
+ _allocStringForBytes
+ _amfi_load_trust_cache
+ _applyCatalogTransforms
+ _assembleTaskDescriptorWithPurpose
+ _assembleTaskDescriptorWithPurposeAndAutoAssetJobID
+ _assetIdDisallowedCharacterSet
+ _assetIdDisallowedCharacterSet.cold.1
+ _assetIdDisallowedCharacterSet.disallowedSet
+ _assetIdDisallowedCharacterSet.once
+ _assetPathDirectory
+ _assetTypeDisallowedCharacterSet
+ _assetTypeDisallowedCharacterSet.cold.1
+ _assetTypeDisallowedCharacterSet.disallowedSet
+ _assetTypeDisallowedCharacterSet.once
+ _assetTypeFromAssetDirectory
+ _assetTypeFromNormalized
+ _attributesInAssetIdWithUnderscore
+ _attributesInAssetIdWithUnderscore._underscoreAssetIdAttributes
+ _attributesInAssetIdWithUnderscore.cold.1
+ _attributesInAssetIdWithUnderscore.once
+ _attributesInDownloadContent
+ _attributesInDownloadContent._downloadContentAttributes
+ _attributesInDownloadContent.cold.1
+ _attributesInDownloadContent.once
+ _attributesInDownloadPolicy
+ _attributesInDownloadPolicy._downloadPolicyAttributes
+ _attributesInDownloadPolicy.cold.1
+ _attributesInDownloadPolicy.once
+ _attributesInDownloadUrl
+ _attributesInDownloadUrl._downloadUrlAttributes
+ _attributesInDownloadUrl.cold.1
+ _attributesInDownloadUrl.once
+ _attributesInPallasDynamicAssetId
+ _attributesInPallasDynamicAssetId._pallasDynamicAssetIdAttributes
+ _attributesInPallasDynamicAssetId.cold.1
+ _attributesInPallasDynamicAssetId.once
+ _cacheDeleteLevelForPolicyValue
+ _calculateTimeout
+ _categoryAssessDiffAndMask
+ _categoryClean
+ _categoryCompoundName
+ _categoryIntersection
+ _categoryInverse
+ _categoryRemoveLatter
+ _categorySimpleName
+ _categoryUnion
+ _categoryUnion3
+ _categoryXor
+ _clock_gettime_nsec_np
+ _convertGarbageCollectionOperationToString
+ _dateAfterTimeTravel
+ _deepMergeDictionaries
+ _determineUnarchiveSizeFromAttributes
+ _determineUnarchiveSizeFromMessage
+ _disassembleTaskDescriptor
+ _downloadResultForFailureGivenPreliminaryAndFurtherInformation
+ _downloadResultForNetworkFailure
+ _downloadTypeForTaskDescriptor
+ _enableDirStatsForDirectory
+ _ensureAndIncrementNumberAtKey
+ _errorStringForMACancelDownloadResult
+ _errorStringForMADownloadResult
+ _errorStringForMAPurgeResult
+ _errorStringForMAQueryResult
+ _errorStringForPurgeResult
+ _fcntl
+ _filterPMV
+ _fsync
+ _getAssetDirectoryName
+ _getAssetIdFromDict
+ _getAssetTypeFromTaskDescriptor
+ _getAutoAssetJobIDFromTaskDescriptor
+ _getAutoLocalUrlFromTypeAndIdGivenDefaultRepoWithPurpose
+ _getAutoLocalUrlFromTypeGivenDefaultRepoWithPurpose
+ _getBootTaskPlistLock.lock
+ _getBootTaskPlistLock.onceToken
+ _getHashFromAssetIdAttributes
+ _getHashFromAttributesInSet
+ _getHashFromNonAssetIdAttributes
+ _getIsKnoxSupportedFromPallasURL
+ _getLocalUrlFromTypeAndIdGivenDefaultRepo
+ _getLocalUrlFromTypeAndIdGivenDefaultRepoWithPurpose
+ _getObjectFromMessage
+ _getObjectFromMessageLogIfDesired
+ _getObjectFromMessageWithFailureReason
+ _getPathToAsset
+ _getPathToAssetWithPurpose
+ _getPathToPmvFile
+ _getPlistArray
+ _getPlistData
+ _getPlistDictionary
+ _getPlistEntryOfClass
+ _getPlistNumber
+ _getPlistNumberAsBool
+ _getPlistString
+ _getPreallocatedSpaceAllowedTypes
+ _getPreallocatedSpaceAllowedTypes.allowedAssetTypes
+ _getPreallocatedSpaceAllowedTypes.allowedTypesOnce
+ _getPreallocatedSpaceAllowedTypes.cold.1
+ _getPreferenceLong
+ _getPurposeFromTaskDescriptor
+ _getRepositoryPath
+ _getSoftwareUpdateBrainTypes
+ _getSoftwareUpdateBrainTypes.cold.1
+ _getSoftwareUpdateBrainTypes.softwareUpdateBrainAssetTypes
+ _getSoftwareUpdateBrainTypes.softwareUpdateBrainTypesOnce
+ _getSoftwareUpdateTypes
+ _getSoftwareUpdateTypes.cold.1
+ _getSoftwareUpdateTypes.softwareUpdateAssetTypes
+ _getSoftwareUpdateTypes.softwareUpdateTypesOnce
+ _getSupportedAnalyticsEventFields
+ _getSupportedAnalyticsEventFields.cold.1
+ _getSupportedAnalyticsEventFields.supportedAnalyticsEventsFields
+ _getSupportedAnalyticsEventFields.supportedAnalyticsEventsFieldsOnce
+ _image4_environment_copy_nonce_digest
+ _image4_environment_set_callbacks
+ _image4_environment_set_nonce_domain
+ _image4_trust_destroy
+ _image4_trust_evaluate
+ _image4_trust_new
+ _image4_trust_set_payload
+ _isAssetTaskDescriptor
+ _isAttributePartOfAssetIdHash
+ _isBuildAlignedType
+ _isCancelDownloadResultFailure
+ _isCatalogTaskDescriptor
+ _isCategoryAllKnown
+ _isCategoryAnyIn
+ _isCategoryClean
+ _isCategoryIn
+ _isCategoryNone
+ _isCategorySame
+ _isCategorySameExcepting
+ _isDirStatsEnabledForDirectory
+ _isDisallowedFromContentCaching
+ _isDownloadResultFailure
+ _isDownloadResultGeneric
+ _isDownloadResultSSO
+ _isDownloadResultSuggestingCheckClient
+ _isDownloadResultSuggestingCheckClockAndCerts
+ _isDownloadResultSuggestingCheckConfiguration
+ _isDownloadResultSuggestingCheckFilesystemState
+ _isDownloadResultSuggestingCheckNetwork
+ _isDownloadResultSuggestingCheckServer
+ _isDownloadResultSuggestingCheckSpaceNeeded
+ _isDownloadResultSuggestingCheckTimeoutConditions
+ _isDownloadResultSuggestingRequeryIsHelpful
+ _isDownloadResultSuggestingRetryWithBackoff
+ _isDownloadResultSuggestingTimeoutWithDetail
+ _isDownloadResultSuggestingTryAgainLater
+ _isDownloadResultSuggestingUsable
+ _isPallasNoBuildVersionMatchFound
+ _isPallasNoPMVMatchFound
+ _isPlistArray
+ _isPlistDictionary
+ _isPmvTaskDescriptor
+ _isPreallocateSpaceAllowedType
+ _isQueryResultFailure
+ _isReboot
+ _isSSONeededForURL
+ _isSSONeededForURL.cold.1
+ _isSSONeededForURL.domainsNeedingSSO
+ _isSSONeededForURL.domainsNeedingSSODispatchOnce
+ _isSoftwareUpdateBrainType
+ _isSoftwareUpdateType
+ _isSupportedMAAnalyticsEventFieldName
+ _isSystemAppType
+ _isTypeDescriptorOfType
+ _isUserInteractionAllowedType
+ _isValidPlistObject
+ _isWellFormedAssetId
+ _isWellFormedAssetType
+ _isWellFormedNormalizedAssetType
+ _isWellFormedPurpose
+ _isWellFormedSystemBuildId
+ _isWellFormedTokenFileName
+ _kMADiffCategoryName_All
+ _kMADiffCategoryName_AnyAttribute
+ _kMADiffCategoryName_AssetId
+ _kMADiffCategoryName_AssetIdAttributes
+ _kMADiffCategoryName_AssetType
+ _kMADiffCategoryName_DownloadContent
+ _kMADiffCategoryName_DownloadPolicy
+ _kMADiffCategoryName_DownloadUrl
+ _kMADiffCategoryName_NonAssetId
+ _kMADiffCategoryName_None
+ _kMADiffCategoryName_PallasDynamicAssetId
+ _kMADiffCategoryName_Some
+ _kMADiffCategoryName_Unknown
+ _kMADiffCategory_BaseCount
+ _kMADiffCategory_Bases
+ _kMobileAssetPreferencesAutoAssetSecureSimulateGraftFailure
+ _malloc_type_malloc
+ _mapMABrainErrorIndications
+ _mapV2ErrorIndications
+ _markAssetPurgeable
+ _markItemPurgeableWithFlagsAndStartTime
+ _markItemPurgeableWithUrgencyAndGarbageCollectionPolicy
+ _markLockedAssetPurgeable
+ _markPreciousAssetPurgeable
+ _markPreciousLockedAssetPurgeable
+ _memcpy
+ _mergeDictionaries
+ _normalizePurpose
+ _normalizePurposeFromUtf8
+ _normalizedAssetType
+ _objc_msgSend$URLByAppendingPathComponent:
+ _objc_msgSend$URLByAppendingPathComponent:isDirectory:
+ _objc_msgSend$_beginAccessWithOptions_nowait:accessMechanismPtr:errorPtr:
+ _objc_msgSend$_logBase64Data:description:
+ _objc_msgSend$_manifestDataFromStoredTicket:manifestType:
+ _objc_msgSend$_manifestDigest:
+ _objc_msgSend$_queryNonceForHandle:domain:digest:error:
+ _objc_msgSend$_storeManifest:manifestType:stage:error:
+ _objc_msgSend$_verifyPlist:manifest:manifestType:result:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$allKeys
+ _objc_msgSend$allObjects
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$base64EncodedStringWithOptions:
+ _objc_msgSend$beginAccessWithOptions:accessMechanismPtr:errorPtr:
+ _objc_msgSend$cachedManifestVerificationResults
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$clearBootTaskPlist
+ _objc_msgSend$clearBootTaskPlist:
+ _objc_msgSend$code
+ _objc_msgSend$compare:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$componentsSeparatedByCharactersInSet:
+ _objc_msgSend$containsString:
+ _objc_msgSend$copy
+ _objc_msgSend$copyBootTaskPlist:
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$currentTotalWritten
+ _objc_msgSend$dataWithContentsOfURL:options:error:
+ _objc_msgSend$dateByAddingComponents:toDate:options:
+ _objc_msgSend$dateFromString:
+ _objc_msgSend$decodeObjectOfClasses:forKey:
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$domain
+ _objc_msgSend$endAccessWithOptions:accessMechanismPtr:errorPtr:
+ _objc_msgSend$endAccessWithOptions_nowait:accessMechanismPtr:errorPtr:
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$filterUsingPredicate:
+ _objc_msgSend$finishDecoding
+ _objc_msgSend$flags
+ _objc_msgSend$getBootTaskPlistLock
+ _objc_msgSend$graftOrMount:graftingError:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$host
+ _objc_msgSend$initForReadingFromData:error:
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithBase64EncodedString:options:
+ _objc_msgSend$initWithBytesNoCopy:length:encoding:freeWhenDone:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$initWithFormat:arguments:
+ _objc_msgSend$initWithLocaleIdentifier:
+ _objc_msgSend$initWithLong:
+ _objc_msgSend$initWithString:
+ _objc_msgSend$insertObject:atIndex:
+ _objc_msgSend$invertedSet
+ _objc_msgSend$keyEnumerator
+ _objc_msgSend$loadTrustCache:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$longLongValue
+ _objc_msgSend$longValue
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$manifestType
+ _objc_msgSend$manifestVerifier
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$numNoLongerStalled
+ _objc_msgSend$numStalled
+ _objc_msgSend$pathComponents
+ _objc_msgSend$pathExtension
+ _objc_msgSend$pathWithComponents:
+ _objc_msgSend$pathsToPurgeOnGraftFailureInEarlyBootTask
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$propertyListWithData:options:format:error:
+ _objc_msgSend$rangeOfCharacterFromSet:
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$readBootTaskPlist:
+ _objc_msgSend$recordAssetGraftStateForEarlyBootTask:options:
+ _objc_msgSend$replaceOccurrencesOfString:withString:options:range:
+ _objc_msgSend$scheme
+ _objc_msgSend$secureMountAuthType
+ _objc_msgSend$set
+ _objc_msgSend$setByAddingObjectsFromSet:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setDay:
+ _objc_msgSend$setFlags:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$setPathsToPurgeOnGraftFailureInEarlyBootTask:
+ _objc_msgSend$setTimeZone:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$storeManifest:manifestType:infoPlist:stage:error:
+ _objc_msgSend$string
+ _objc_msgSend$stringByTrimmingCharactersInSet:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$stringIsEqual:to:
+ _objc_msgSend$stringWithCapacity:
+ _objc_msgSend$stringWithContentsOfFile:encoding:error:
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$supportsLoadableTrustCache:
+ _objc_msgSend$timeZoneWithAbbreviation:
+ _objc_msgSend$trustCachePath
+ _objc_msgSend$ungraftOrUnmount:ungraftingError:
+ _objc_msgSend$userInfo
+ _objc_msgSend$verifyManifest:manifestType:
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
+ _objc_msgSend$writeToFile:atomically:
+ _objc_msgSend$writeToFile:atomically:encoding:error:
+ _objc_retain_x1
+ _objc_retain_x27
+ _objc_retain_x3
+ _plistDecodeClasses
+ _plistDecodeClasses._plistDecodeClasses
+ _plistDecodeClasses.cold.1
+ _plistDecodeClasses.once
+ _plistMutableDecodeClasses
+ _plistMutableDecodeClasses._plistDecodeClasses
+ _plistMutableDecodeClasses.cold.1
+ _plistMutableDecodeClasses.once
+ _purposeDirectoryName
+ _purposeDisallowedCharacterSet
+ _purposeDisallowedCharacterSet.cold.1
+ _purposeDisallowedCharacterSet.disallowedSet
+ _purposeDisallowedCharacterSet.once
+ _purposeIgnoredCharacterSet
+ _purposeIgnoredCharacterSet.cold.1
+ _purposeIgnoredCharacterSet.ignoredSet
+ _purposeIgnoredCharacterSet.once
+ _removefile
+ _rename
+ _runningInDeviceRecoveryEnvironment
+ _runningInDeviceRecoveryEnvironment.cold.1
+ _runningInDeviceRecoveryEnvironment.isRunningInDeviceRecoveryEnvironment
+ _runningInDeviceRecoveryEnvironment.onceToken
+ _safeAtomicWriteToPath
+ _sendClientResponse
+ _sendReply
+ _simplifySetIdentifier
+ _snprintf
+ _stringForAnalyticsReportingLevel
+ _stringForCacheDeleteUrgency
+ _stringForMAAssetState
+ _stringForMACancelDownloadResult
+ _stringForMADownloadResult
+ _stringForMAOperationResult
+ _stringForMAPurgeResult
+ _stringForMAQueryResult
+ _stringForMAQueryReturnTypes
+ _stringForMAXpcCommand
+ _stringForMAXpcError
+ _stringForSecureMABundleCommand
+ _stringForSecureOperation
+ _stringWithoutNewlines
+ _strncmp
+ _strtoll
+ _suAssetTypes
+ _suAssetTypes.cold.1
+ _suAssetTypes.once
+ _suAssetTypes.suAssetTypes
+ _supportedAssetFormats
+ _supportedAssetFormats.cold.1
+ _supportedAssetFormats.compressionTypes
+ _supportedAssetFormats.onceToken
+ _supportedAssetFormatsArray
+ _supportedAssetFormatsArray.__orderedCompressionTypes
+ _supportedAssetFormatsArray.cold.1
+ _supportedAssetFormatsArray.orderedOnceToken
+ _sysctlbyname
+ _tokenFileDisallowedCharacterSet
+ _tokenFileDisallowedCharacterSet.cold.1
+ _tokenFileDisallowedCharacterSet.disallowedSet
+ _tokenFileDisallowedCharacterSet.once
+ _urlSupportsAuthenticatedPallas
+ _urlSupportsAuthenticatedPallas.cold.1
+ _urlSupportsAuthenticatedPallas.domainsSupportingAuthenticatedPallas
+ _urlSupportsAuthenticatedPallas.domainsSupportingAuthenticatedPallasDispatchOnce
+ _usingCentralizedCachedelete
+ _usingCentralizedCachedelete.cold.1
+ _usingCentralizedCachedelete.eapfsEnabled
+ _usingCentralizedCachedelete.onceToken
+ _write
+ _xpcRequestFieldsOptional
+ _xpcRequestFieldsRequired
+ _xpc_connection_send_message
+ _xpc_dictionary_create_reply
+ _xpc_dictionary_get_data
+ _xpc_dictionary_get_double
+ _xpc_dictionary_get_string
+ _xpc_dictionary_set_int64
- +[SecureMobileAssetBundle clearGraftList:]
- +[SecureMobileAssetBundle copyGraftList:]
- +[SecureMobileAssetBundle getGraftListLock]
- +[SecureMobileAssetBundle getGraftListLock].cold.1
- -[SecureMAHelper clearGraftList]
- -[SecureMAHelper copyGraftList:]
- -[SecureMobileAssetBundle _manifestDataFromFullyFormedTicket:]
- -[SecureMobileAssetBundle _storeManifest:stage:error:]
- -[SecureMobileAssetBundle beginAccess:error:]
- -[SecureMobileAssetBundle beginAccess_nowait:error:]
- -[SecureMobileAssetBundle endAccess:error:]
- -[SecureMobileAssetBundle endAccess_nowait:error:]
- -[SecureMobileAssetBundle graftOrMount:]
- -[SecureMobileAssetBundle graftOrMount:].cold.1
- -[SecureMobileAssetBundle recordAssetGraftStateForEarlyBootTask:]
- -[SecureMobileAssetBundle ungraftOrUnmount:]
- GCC_except_table103
- GCC_except_table26
- GCC_except_table34
- GCC_except_table43
- GCC_except_table44
- GCC_except_table45
- GCC_except_table48
- GCC_except_table49
- GCC_except_table50
- GCC_except_table54
- GCC_except_table67
- GCC_except_table7
- GCC_except_table70
- GCC_except_table83
- GCC_except_table84
- GCC_except_table85
- ___43+[SecureMobileAssetBundle getGraftListLock]_block_invoke
- ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1214
- ___block_literal_global.1201
- ___block_literal_global.1209
- ___block_literal_global.1342
- ___block_literal_global.1605
- ___block_literal_global.2065
- _getGraftListLock.lock
- _getGraftListLock.onceToken
- _objc_msgSend$_manifestDataFromFullyFormedTicket:
- _objc_msgSend$_storeManifest:stage:error:
- _objc_msgSend$beginAccess:error:
- _objc_msgSend$beginAccess_nowait:error:
- _objc_msgSend$clearGraftList
- _objc_msgSend$clearGraftList:
- _objc_msgSend$copyGraftList:
- _objc_msgSend$endAccess:error:
- _objc_msgSend$endAccess_nowait:error:
- _objc_msgSend$getGraftListLock
- _objc_msgSend$graftOrMount:
- _objc_msgSend$initWithContentsOfURL:error:
- _objc_msgSend$recordAssetGraftStateForEarlyBootTask:
- _objc_msgSend$ungraftOrUnmount:
- _objc_msgSend$writeToURL:error:
- _objc_retain_x24
CStrings:
+ "\n"
+ " "
+ " %lld bytes"
+ " -- ISSUES: "
+ " -- Some entries missed potential filtering due to"
+ " -- filtering saw a total of %ld individual SupportedDevices that were nil or not strings"
+ " 1 byte"
+ " ExpirationDate: %ld"
+ " Filtered out %ld due to"
+ " PostingDate: %ld"
+ " ProductVersion: %ld"
+ " SupportedDevices: %ld"
+ " emptySupportedDevices: %ld"
+ " missingAllPlatforms"
+ " missingExpirationDate: %ld"
+ " missingPlatform: %@"
+ " missingPostingDate: %ld"
+ " missingProductVersion: %ld"
+ " missingSet: %@"
+ " missingSupportedDevices: %ld"
+ " notExpiredBefore: %@"
+ " platformExactMatch: %@"
+ " postedBefore: %@"
+ " supportedDevicePrefix: %@"
+ " versionPrefix: %@"
+ "%02hhX"
+ "%02x"
+ "%0lx/%0lx %@%@%@"
+ "%@%@"
+ "%@%@%@"
+ "%@%ld"
+ "%@%lld bytes"
+ "%@%lldGB %lldMB %lldKB%@"
+ "%@%lldKB%@"
+ "%@%lldMB %lldKB%@"
+ "%@.%@"
+ "%@:\ndescendants: %llu\nphysical size: %llu\ngen-count: %llu\n"
+ "%s failed with error %d (%@)"
+ "%{public}s: Atomic write to path failed and failed to remove temp path(%{public}@): %{public}@"
+ "%{public}s: Extracted object for key %{public}@ is invalid/not a dictionary"
+ "%{public}s: Failed to write item to path %{public}@"
+ "%{public}s: Field is invalid"
+ "%{public}s: Invalid options"
+ "%{public}s: Unable to extract plist object for key %{public}@ from dict"
+ "("
+ "(from newer)"
+ "(from newer, subset)"
+ "(from older)"
+ ")"
+ "+"
+ ", "
+ "."
+ ".tok"
+ "/.nofollow/private/var/run/bootSessionMA.txt"
+ "/System/Library/PreinstalledAssetsV2/RequiredByOs"
+ "/private/var/MobileAsset/AssetsV2"
+ "/private/var/MobileAsset/PreinstalledAssetsV2/InstallWithOs"
+ "/private/var/MobileSoftwareUpdate/.MAAMigrated.plist"
+ "0 bytes"
+ "0123456789-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
+ "0123456789.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"
+ "0123456789.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-/"
+ "0123456789abcdefABCDEF"
+ "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
+ ";'\"\\/@?%*|<>.{}"
+ "<operation>"
+ "<reason>"
+ "<undefined-level>"
+ "@\"NSMutableDictionary\""
+ "@\"NSSet\""
+ "@\"SecureMobileAssetManifestVerifier\""
+ "@32@0:8@16Q24"
+ "AAError"
+ "AMAuthInstallUpdaterCryptex1CopyTicket()"
+ "AMAuthInstallUpdaterCryptex1MobileAssetCopyImg4WithRestoreInfo()"
+ "API MISUSE: markItemPurgeableWithUrgencyAndGarbageCollectionPolicy called with NeverCollected policy"
+ "AdditionalAuthenticatedPallasServer"
+ "AdditionalSSOServer"
+ "AppleArchive"
+ "AppleConnect"
+ "AppleEncryptedArchive"
+ "AppleSoftwareLookup.json"
+ "AssetBundlePath"
+ "AssetFormat"
+ "AssetNotInstalled"
+ "AssetPatchingFailureError"
+ "AssetPatchingFailureReason"
+ "AssetPatchingPallasResult"
+ "AssetSets"
+ "AssetTargetBuildVersion"
+ "AssetTargetOSVersion"
+ "AssetVersion"
+ "Attempting to get local URL with asset-type that could not be normalized"
+ "Attempting to get local URL with nil asset-type"
+ "Attempting to get local url with nil asset id"
+ "Attempting to get local url with nil asset type"
+ "Attempting to get local url with nil default repo for a non preinstalled asset"
+ "AuthInstall"
+ "AutoAssetJob"
+ "AutoAssetSecureSimulateGraftFailure"
+ "AvailableFreeSpace"
+ "B24@?0@8@\"NSDictionary\"16"
+ "B32@0:8@16Q24"
+ "B32@0:8^q16^@24"
+ "B40@0:8@16^q24^@32"
+ "B44@0:8@16Q24B32^@36"
+ "B44@0:8Q16I24^@28^@36"
+ "B56@0:8@16@24Q32^@40^@48"
+ "BEYOND-EMERGENCY"
+ "BaseAssetVersion"
+ "BaseURL"
+ "Boot plist from previous boot contains no graft operations. Skipping grafting..."
+ "Boot plist successfully loaded. Deleting list\n"
+ "Boot session UUID has an invalid length (%zu)"
+ "Boot session file does not exist at path: %@"
+ "BrainVersion"
+ "BytesTransferredEst"
+ "BytesWritten"
+ "COMMIT"
+ "CacheDeleteLevel"
+ "Calculated the download timeout to be %ld hrs %ld mins %ld secs (%ld) for size %lld"
+ "Cancel of download failed."
+ "Cancel of download had XPC error."
+ "Cancel of download not needed because it was not downloading."
+ "Cancel of download not needed because the asset is part of the OS."
+ "Cancel of download not needed because the asset is preinstalled with the OS."
+ "Cancel of download not possible as client was not entitled."
+ "Cancel of download request sent but XPC connection interrupted."
+ "Cancel of download was successful."
+ "Canceled"
+ "CellularAccessRequest"
+ "CellularAccessResponse"
+ "Cleaning up path: %@"
+ "Clearing previous boot-task plist\n"
+ "ClientCommunication"
+ "ClientName"
+ "ConstrainedNetworkAccessRequest"
+ "ConstrainedNetworkAccessResponse"
+ "Could not allocate buffer to copy boot session UUID"
+ "Could not copy boot session UUID: %d (%s)"
+ "Could not create normalized asset type"
+ "Could not decode object for key:%s error:%@"
+ "Could not look up boot session UUID: %d (%s)"
+ "Could not send XPC reply with result %lld, because there was no xpc reply dictionary"
+ "DEPERSONALIZATION"
+ "Default"
+ "DetermineReclaimable"
+ "DictionaryEnumerationFailure"
+ "DiscretionaryBreakdown"
+ "DiscretionaryConfigChanged"
+ "DomainsNeedingSSO not initialized"
+ "Downlaod failed due to a server redirect to a nonexistent location."
+ "Download"
+ "Download failed as an AssetVersion downgrade was detected"
+ "Download failed as the asset is no longer in the catalog. A requery is likely needed."
+ "Download failed as the downloaded asset was not well-formed."
+ "Download failed as the server said authentication failed."
+ "Download failed as the server said it encountered an error."
+ "Download failed as the server said it had an internal error."
+ "Download failed as the server said it was a bad request."
+ "Download failed as the server said the file was not found (or access was denied)."
+ "Download failed as the server said the file was not found."
+ "Download failed due to Data not being allowed."
+ "Download failed due to Error %lld (%@)."
+ "Download failed due to XPC message creation failure."
+ "Download failed due to a DNS lookup failure."
+ "Download failed due to a bad URL."
+ "Download failed due to a bad server response."
+ "Download failed due to a connection not being established for a request attempt in the time NSURLSession allows."
+ "Download failed due to a general networking error."
+ "Download failed due to a secure connection not being established. A common cause is the device time not being set correctly."
+ "Download failed due to an error obtaining the SSO token."
+ "Download failed due to an error while copying the data to it's final location."
+ "Download failed due to an error while determining the final location for the download"
+ "Download failed due to an unsupported URL."
+ "Download failed due to bad metadata on asset."
+ "Download failed due to being out of space. Check for storage space before retrying download."
+ "Download failed due to being unable to replace the existing asset."
+ "Download failed due to client requesting Live Asset only, but the device was configured to disable Live Asset server. No XML fallback was allowed."
+ "Download failed due to client requesting Live Asset only, but the live asset server gave an error. No XML fallback was allowed."
+ "Download failed due to international roaming being off."
+ "Download failed due to invalid asset reciepts in response from live asset server."
+ "Download failed due to losing the network connection."
+ "Download failed due to no XML server URL being configured."
+ "Download failed due to no XML server URL being provided for fallback."
+ "Download failed due to no live asset server URL being configured."
+ "Download failed due to not being able to connect to the host."
+ "Download failed due to not being able to determine a staging directory."
+ "Download failed due to not being able to find the host."
+ "Download failed due to not being able to get a TCP connection in the time NSURLSession allows."
+ "Download failed due to not being able to load from network."
+ "Download failed due to not being scheduled or the download of the whole resource was not able to complete in the time allowed."
+ "Download failed due to not getting a response within the time allowed."
+ "Download failed due to not having an extractor."
+ "Download failed due to the asset type being invalid and not being well-formed."
+ "Download failed due to the download taking longer than the time allowed."
+ "Download failed due to the download taking longer than the time allowed. Fluctuating between stalled and not stalled."
+ "Download failed due to the download taking longer than the time allowed. Never downloaded a single byte."
+ "Download failed due to the download taking longer than the time allowed. Slow download yet never stalled."
+ "Download failed due to the download taking longer than the time allowed. Was downloading then stalled once and remained stalled from that point."
+ "Download failed due to the live asset server providing invalid transforms."
+ "Download failed due to the purpose being invalid and not being well-formed."
+ "Download failed due to the resource being unavailable."
+ "Download failed due to the server not responding during the time allowed for the stream watchdog."
+ "Download failed due to there being an active call."
+ "Download failed due to there being no Internet connection."
+ "Download failed due to too many HTTP redirects."
+ "Download failed."
+ "Download failure due to unknown result."
+ "Download finished but could not be installed."
+ "Download finished but could not be moved into repository."
+ "Download finished but could not be moved to staging location."
+ "Download finished but the metadata in the download was corrupted."
+ "Download from live asset server could not get an asset matching the requested one."
+ "Download is not allowed as mobileassetd was starting up."
+ "Download is not allowed as the requesting client is not entitled."
+ "Download is not needed for preinstalled asset (installed with OS)."
+ "Download is not needed for preinstalled asset (required by OS)."
+ "Download is not possible as the task could not be created for the session."
+ "Download not allowed as the asset already appears to be in the repository."
+ "Download not allowed as the given extractor is invalid."
+ "Download not possible as the asset doesn't support streaming zip."
+ "Download not possible due to invalid options."
+ "Download not possible due to missing decryption key"
+ "Download not possible for invalid asset identifier."
+ "Download not possible for invalid asset type."
+ "Download request had XPC error."
+ "Download request had gotten a response but it was incomplete."
+ "Download request sent but XPC connection interrupted."
+ "Download request sent but mobileassetd exited."
+ "Download request was sent and while processing a failure happened."
+ "Download successful."
+ "Download tracking was abandoned as the task was no longer found in NSURLSession."
+ "Download unzip failed."
+ "Download was cancelled."
+ "Download was not needed as the server indicated the file was unchanged."
+ "DownloadAssetFailed"
+ "DownloadTime"
+ "Downloads not allowed at this time."
+ "EMERGENCY"
+ "ERROR: Invalid string passed to %{public}s"
+ "EarlyBootTaskInfo-Temp.plist"
+ "EarlyBootTaskInfo.plist"
+ "Error reading boot UUID: %@"
+ "Error writing boot session UUID to path:%@ | err:%@"
+ "ExpensiveNetworkAccessRequest"
+ "ExpensiveNetworkAccessResponse"
+ "ExpirationDate"
+ "Failed to cleanup: %@. %s"
+ "Failed to clear previous boot task plist: %@\n"
+ "Failed to clear purgability, errno:%d"
+ "Failed to decode object for key:%s"
+ "Failed to get NSData object from message for key:%s length:%lld bytes"
+ "Failed to get key: %{public}s"
+ "Failed to get key: %{public}s due to not beinng present"
+ "Failed to get key:%s (length:%lld bytes too small)"
+ "Failed to get object from message since key:%s is not present"
+ "Failed to mark purgeable with label, errno:%d"
+ "Failing to hash due to duplicate array entries"
+ "FailureErrorCode"
+ "FailureErrorDomain"
+ "FailureErrorMessage"
+ "FailureErrorUnderlying"
+ "FileType"
+ "Filtered PMV to %ld/%ld entries (from %@: %ld iOS, %ld macOS) using ["
+ "Filtered PMV to 0/0 entries. PMV was not a dictionary."
+ "GRAFTING"
+ "GetBrainInfo"
+ "Graft operation for (%@) did not contain paths for cleanup, it will be skipped: %@."
+ "Graft operation for (%@) is not a dictionary, it will be skipped: %@"
+ "GraftInfo"
+ "GraftOperations"
+ "GraftTicketVerificationFailed"
+ "HIGH"
+ "Hash duplicate found at index %i (%li duplicates found) with entry %@"
+ "IODeviceTree:/filesystems"
+ "InstallCreateBrainDirFailed"
+ "InstallFailed"
+ "InstallWriteBrainPlistFailed"
+ "InstallWriteStageFileFailed"
+ "Invalid data passed to %{public}s"
+ "Invalid path passed to %{public}s"
+ "Invalid transform, skipping: %{public}@"
+ "Invalid url passed to %{public}s"
+ "InvalidDictionaryType"
+ "IsAssetPatch"
+ "IsAutoDownload"
+ "IsDiscretionary"
+ "IsMAAutoAsset"
+ "IsPallas"
+ "IsUserPriority"
+ "LOW"
+ "MA repo path does not exist."
+ "MAAssetState%llu"
+ "MACancelConnectionInterupted"
+ "MACancelDownloadResult%llu"
+ "MACancelFailed"
+ "MACancelNotApplicableForInstalledWithOs"
+ "MACancelNotApplicableForRequireByOs"
+ "MACancelNotEntitled"
+ "MACancelSucceeded"
+ "MACancelWasNotDownloading"
+ "MACatalogButNotInstalledOnly"
+ "MACatalogOnly"
+ "MADAnalyticsLevelDoNotSave"
+ "MADAnalyticsLevelDoNotSend"
+ "MADAnalyticsLevelImmediate"
+ "MADAnalyticsLevelUnchanged"
+ "MADownloadAssetAlreadyInstalled"
+ "MADownloadAssetBadMetaData"
+ "MADownloadAssetMissingDecryptionKey"
+ "MADownloadAssetNoLongerInCatalog"
+ "MADownloadBadOptions"
+ "MADownloadBadServerResponse"
+ "MADownloadBadUrl"
+ "MADownloadCallIsActive"
+ "MADownloadCancelled"
+ "MADownloadCannotConnectToHost"
+ "MADownloadCannotFindHost"
+ "MADownloadCannotLoadFromNetwork"
+ "MADownloadConflict"
+ "MADownloadConnectionInterrupted"
+ "MADownloadContentDecryptionFailed"
+ "MADownloadCopyFailed"
+ "MADownloadCouldNotReplace"
+ "MADownloadDNSLookupFailed"
+ "MADownloadDaemonExit"
+ "MADownloadDaemonNotReady"
+ "MADownloadDataNotAllowed"
+ "MADownloadFailed"
+ "MADownloadFailedNoFallBackUrl"
+ "MADownloadFailedNoFallbackAllowed"
+ "MADownloadFailedNoPallasUrl"
+ "MADownloadFailedNoStandardUrl"
+ "MADownloadHTTPTooManyRedirects"
+ "MADownloadIncompatibleBrain"
+ "MADownloadIncomplete"
+ "MADownloadInstallFailed"
+ "MADownloadInternationalRoamingOff"
+ "MADownloadInvalidPaths"
+ "MADownloadInvalidReceipts"
+ "MADownloadInvalidSZExtractor"
+ "MADownloadLiveServerDisabledNoFallback"
+ "MADownloadLostTask"
+ "MADownloadMalformedAssetData"
+ "MADownloadMalformedAssetType"
+ "MADownloadMalformedPurpose"
+ "MADownloadMetaDataProcessFailed"
+ "MADownloadMoveFailed"
+ "MADownloadNetworkConnectionLost"
+ "MADownloadNetworkingError"
+ "MADownloadNewBrainRequired"
+ "MADownloadNilAssetId"
+ "MADownloadNilAssetType"
+ "MADownloadNoChange"
+ "MADownloadNoExtractorFailure"
+ "MADownloadNoMatchFound"
+ "MADownloadNoSpaceLeft"
+ "MADownloadNoStagingDir"
+ "MADownloadNoValidSession"
+ "MADownloadNotAllowed"
+ "MADownloadNotApplicableForInstalledWithOs"
+ "MADownloadNotApplicableForRequireByOs"
+ "MADownloadNotConnectedToInternet"
+ "MADownloadNotEntitled"
+ "MADownloadNotFound"
+ "MADownloadNotFoundOrDenied"
+ "MADownloadRedirectToNonExistentLocation"
+ "MADownloadResourceUnavailable"
+ "MADownloadResponseDeferred"
+ "MADownloadResult%llu"
+ "MADownloadSSOFailure"
+ "MADownloadSecureConnectionFailed"
+ "MADownloadServerAuthFailure"
+ "MADownloadServerBadRequest"
+ "MADownloadServerError"
+ "MADownloadServerInternalError"
+ "MADownloadStagingFailed"
+ "MADownloadStreamingZipNotSupported"
+ "MADownloadSuccessful"
+ "MADownloadTimedOut"
+ "MADownloadTimedOutBecameStalled"
+ "MADownloadTimedOutConnection"
+ "MADownloadTimedOutFrequentStalls"
+ "MADownloadTimedOutRequest"
+ "MADownloadTimedOutResource"
+ "MADownloadTimedOutSlowDownload"
+ "MADownloadTimedOutStart"
+ "MADownloadTimedOutWatchdog"
+ "MADownloadTimeoutNoContent"
+ "MADownloadTransformFailure"
+ "MADownloadUnableToCreateMessage"
+ "MADownloadUnknownResult"
+ "MADownloadUnsupportedURL"
+ "MADownloadUnzipFailed"
+ "MADownloadXpcError"
+ "MADownloading"
+ "MAInstalled"
+ "MAInstalledNotInCatalog"
+ "MAInstalledOnly"
+ "MAInstalledWithOs"
+ "MANotPresent"
+ "MAOperationFailed"
+ "MAOperationInvalid"
+ "MAOperationNotEntitled"
+ "MAOperationResult%llu"
+ "MAOperationSuccessful"
+ "MAOperationUnknownResult"
+ "MAOperationXpcError"
+ "MAP_TO_EXCLAVE"
+ "MAPreinstalledOnly"
+ "MAPurgeAssetCouldntPurge"
+ "MAPurgeAssetDidntExist"
+ "MAPurgeCannotCreateMessage"
+ "MAPurgeConnectionInterrupted"
+ "MAPurgeCouldNotCancelAllDownloads"
+ "MAPurgeEncodingFailure"
+ "MAPurgeFailed"
+ "MAPurgeFailedBeforeFirstUnlock"
+ "MAPurgeNotApplicableForRequireByOs"
+ "MAPurgeNotEntitled"
+ "MAPurgePartiallyComplete"
+ "MAPurgeResult%llu"
+ "MAPurgeSucceeded"
+ "MAPurgeXpcError"
+ "MAQueryBeforeFirstUnlock"
+ "MAQueryCannotCreateMessage"
+ "MAQueryCatalogNotDownloaded"
+ "MAQueryCouldNotEncodeResults"
+ "MAQueryDaemonExit"
+ "MAQueryFailed"
+ "MAQueryHasAllowedDifferences"
+ "MAQueryNilAssetType"
+ "MAQueryNotEntitled"
+ "MAQueryParamsEncodeFailure"
+ "MAQueryResult%llu"
+ "MAQueryReturnTypes%llu"
+ "MAQuerySuccessful"
+ "MAQueryTooManyResults"
+ "MAQueryUnknownResult"
+ "MAQueryXpcError"
+ "MAQueryXpcLengthError"
+ "MARequiredByOs"
+ "MASecureManifestStorage does not support SMAC"
+ "MAStrictlyCatalogOnly"
+ "MAStrictlyObsoleteOnly"
+ "MAUnionOfCatalogInstalled"
+ "MAUnknown"
+ "MAXpcCommand%llu"
+ "MAXpcError%llu"
+ "MAXpcErrorConnectionTerminated"
+ "MAXpcErrorDataMismatch"
+ "MAXpcErrorEmptyData"
+ "MAXpcErrorLengthMismatch"
+ "MAXpcErrorLengthMissing"
+ "MAXpcErrorLengthZero"
+ "MAXpcErrorNone"
+ "MAXpcErrorParamMissing"
+ "MAXpcErrorUnableToReply"
+ "MA_CANCEL_CATALOG_DOWNLOAD"
+ "MA_CANCEL_DOWNLOAD"
+ "MA_CANCEL_PMV_DOWNLOAD"
+ "MA_CLEAN_V1_ASSETS"
+ "MA_CLEAR_PREFERENCES"
+ "MA_CONFIG_DOWNLOAD"
+ "MA_DATA_MIGRATOR"
+ "MA_DOWNLOAD_ASSET"
+ "MA_DOWNLOAD_METADATA"
+ "MA_DOWNLOAD_PMV"
+ "MA_DUMP_CLIENT_USAGE"
+ "MA_DUMP_CODE_COVERAGE"
+ "MA_ENSURE_DATA_VAULT"
+ "MA_GARBAGE_COLLECT"
+ "MA_GET_ALLOW_NON_USER_INIT"
+ "MA_GET_MABRAIN_INFO"
+ "MA_GET_PALLAS_AUDIENCE"
+ "MA_GET_PALLAS_ENABLED"
+ "MA_GET_PALLAS_URL"
+ "MA_GET_SANDBOX_EXTENSION"
+ "MA_GET_SERVER_URL"
+ "MA_INSTALL_ASSET"
+ "MA_INVALID_MESSAGE"
+ "MA_LOAD_ASSET_BY_ID"
+ "MA_MIGRATE_ASSETS"
+ "MA_NSURL_STATE_DUMP"
+ "MA_OVERRIDE_GC"
+ "MA_PURGE_ALL"
+ "MA_PURGE_ASSET"
+ "MA_PURGE_CATALOGS"
+ "MA_QUERY_ASSET_TYPE"
+ "MA_QUERY_INSTALLED_IDS"
+ "MA_QUERY_PMV"
+ "MA_REFRESH_ASSET_STATE"
+ "MA_REPAIR_STATE"
+ "MA_REPORTING_REQUEST"
+ "MA_SECUREMABUNDLE_COMMAND_KEY"
+ "MA_SERVER_URL_OVERRIDE"
+ "MA_SET_DAW_TOKEN_PATH"
+ "MA_SET_DAW_TOKEN_VALUE"
+ "MA_SET_PALLAS_AUDIENCE"
+ "MA_SET_PALLAS_ENABLED"
+ "MA_SET_PALLAS_URL"
+ "MA_SET_PREFERENCES"
+ "MA_SPACE_CHECK"
+ "MA_UPDATE_CLIENT_USAGE"
+ "MA_UPDATE_DOWNLOAD_PROGRESS"
+ "MA_UPDATE_MABRAIN"
+ "MEDIUM"
+ "MKBAssertionKey"
+ "MKBAssertionTimeout"
+ "MOUNTING"
+ "MSCancelXpcError"
+ "MapToExclavesTicketVerificationFailed"
+ "MobileAssetBrainErrorDomain"
+ "MountTicketVerificationFailed"
+ "MultipathRequest"
+ "MultipathResponse"
+ "NEGATIVE "
+ "NO-OPERATION"
+ "NONE"
+ "NULL"
+ "NeverCollected"
+ "Other"
+ "PERSONALIZATION"
+ "PallasAssetAudience"
+ "PathsToDeleteOnGraftFailure"
+ "PerformGraft"
+ "Personalized manifest failed to verify (nonce rolled?)"
+ "PostingDate"
+ "Precious"
+ "PrerollNonce"
+ "ProductVersion"
+ "PublicAssetSets"
+ "Purge attempt failed due to daemon jetsam/crash."
+ "Purge failed as all inflight downloads could not be cancelled."
+ "Purge failed as the asset was not present locally."
+ "Purge failed as the attempt to delete the directory failed."
+ "Purge failed as the device is before first unlock."
+ "Purge failed due to error %llu"
+ "Purge failed due to the calling process not being entitled."
+ "Purpose"
+ "Q"
+ "Query failed due an XPC failure confirming the length of the field."
+ "Query failed due to Error %lld (%@)."
+ "Query failed due to XPC error."
+ "Query failed due to being unable to create an XPC message."
+ "Query failed due to having too many results."
+ "Query failed due to mobileassetd exiting, the system may be under load."
+ "Query failed due to not being able to encode the parameters provided by the client."
+ "Query failed due to not being able to encode the results to give to the client."
+ "Query failed due to the asset type being invalid."
+ "Query failed due to the client not having a required entitlement."
+ "Query failed due to the device not yet providing access to user data, usually due to the device being locked."
+ "Query failed unexpectedly."
+ "Query failed."
+ "Query found a matching item, but the asset found has some differences from the request which were allowable by the client."
+ "Query may be incomplete as there was no catalog."
+ "Query successful."
+ "Ramp"
+ "Received a request to hash a multibyte value that is too large, possible malicious behavior - aborting"
+ "Received a request to hash a value but could not get a C string. Possible malicious behavior - aborting"
+ "Received a request to hash a value that is too large, possible malicious behavior - aborting"
+ "ReclaimSpace"
+ "RelativePath"
+ "RequiredByOS assets are in the system partition and cannot be collected."
+ "Result"
+ "RollNonce"
+ "SECUREMABUNDLE_COMMAND_BEGINACCESS"
+ "SECUREMABUNDLE_COMMAND_COMMIT_MANIFESTS"
+ "SECUREMABUNDLE_COMMAND_DEPERSONALIZE"
+ "SECUREMABUNDLE_COMMAND_ENDACCESS"
+ "SECUREMABUNDLE_COMMAND_IS_PERSONALIZED"
+ "SECUREMABUNDLE_COMMAND_MAPTOEXCLAVES"
+ "SECUREMABUNDLE_COMMAND_PERSONALIZE"
+ "SECUREMABUNDLE_COMMAND_UNMAPFROMEXCLAVES"
+ "SHA-1"
+ "SHA-256"
+ "SMABundleAccessOptions"
+ "ScanCatalogDownloadFailed"
+ "ScanFailed"
+ "ScanNoUpdateFound"
+ "SecureMobileAssetManifestVerifier"
+ "Skipping transformation (key: \"%@\" value: \"%@\"): Value cannot be base64 decoded."
+ "Skipping transformation, as asset isn't a dict"
+ "StillNeededSpace"
+ "StreamingZip"
+ "SupportedAssetFormats"
+ "SupportedAssetFormats: Found unexpected non-array type in SupportedAssetFormats preferences, dropping preference"
+ "SupportedAssetFormats: Found unexpected non-string item in SupportedAssetFormats preferences, dropping entry"
+ "SupportedAssetFormats: Using default supported asset format types: [%@]"
+ "SupportedAssetFormats: Using preferences override supported asset format types: [%@]"
+ "SupportedDevices"
+ "SupportsLoadableTrustCache"
+ "T@\"NSMutableDictionary\",&,V_cachedManifestVerificationResults"
+ "T@\"NSSet\",&,N,V_pathsToPurgeOnGraftFailureInEarlyBootTask"
+ "T@\"SecureMobileAssetManifestVerifier\",&,V_manifestVerifier"
+ "TQ,N,V_flags"
+ "TQ,R,D,N"
+ "The path already does not exist: %@"
+ "TimeoutIntervalForRequest"
+ "TokenFileName passed in contains invalid characters in string"
+ "TokenFileName passed in has an invalid file suffix"
+ "TokenFileName passed in has an invalid length"
+ "TokenFileName passed in is not a string"
+ "TokenFileName passed in was null"
+ "TotalRequiredSpace"
+ "TriggeringLayer"
+ "Trust cache and/or ticket is empty."
+ "TrustCache"
+ "TrustCacheAMFILoadDeviceLocked"
+ "TrustCacheAMFILoadError"
+ "TrustCacheCommittedTicketDataNil"
+ "TrustCacheDataOrTicketEmpty"
+ "TrustCacheNotPersonalizedForExclaves"
+ "TrustCachePersonalizedBundleTicketDataNil"
+ "TrustCacheReadError"
+ "TrustCacheTicketMismatch"
+ "TrustCacheTicketReadError"
+ "TrustCacheTicketVerificationFailed"
+ "UNDEFINED"
+ "UNGRAFTING"
+ "UNMAP_FORM_EXCLAVE"
+ "UNMOUNTING"
+ "URL %{public}@ requires SSO"
+ "URL to asset: %@"
+ "URLByAppendingPathComponent:"
+ "URLByAppendingPathComponent:isDirectory:"
+ "UTC"
+ "Unable to check dirstats for directory %{public}@, error %i"
+ "Unable to decrypt asset content"
+ "Unable to determine boot plist from previous boot. Skipping grafting: %@\n"
+ "Unable to download asset due to brain being incompatible with the asset requirements and no available brain that meets the requirements"
+ "Unable to enable dirstats for directory %{public}@, error %i"
+ "Unable to get MA repo path"
+ "Unable to immediately download asset due to current brain being incompatible with the asset requirements - a new brain will be installed and the download will begin when it relaunches"
+ "Unable to parse boot task plist data into dictionary."
+ "Unknown"
+ "Unknown MACancelDownloadResult: %ld (%{public}@)"
+ "WasAssetPatchingAttempted"
+ "[AuthenticatedPallas]: Invalid url passed to %{public}s"
+ "[AuthenticatedPallas]: URL %{public}@ supports authenticated pallas"
+ "[AuthenticatedPallas]: domainsSupportingAuthenticatedPallas not initialized"
+ "[AuthenticatedPallas]: {urlSupportsAuthenticatedPallas} Adding %{public}@ to set of domains supporting authenticated pallas"
+ "[DeepMergeDictionaries]: Invalid source/target dictionaries passed"
+ "[DeepMergeDictionaries]: No object exists in source dict for key %{public}@"
+ "[DetectDeviceRecoveryMode]: Failed to allocate buffer to read OS environment value. Assuming regular OS"
+ "[DetectDeviceRecoveryMode]: Returning RunningInDeviceRecoveryMode as true due to override"
+ "[DetectDeviceRecoveryMode]: Running in DeviceRecovery environment"
+ "[DetectDeviceRecoveryMode]: Running in regular OS environment"
+ "[DetectDeviceRecoveryMode]: Unable to determine OS environment(%s). Assuming regular OS"
+ "[DetectDeviceRecoveryMode]: Unable to determine size of OS environment variable(%s). Assuming regular OS"
+ "[SMA] %@ manifest for %@ (type = %s)"
+ "[SMA] %{public}@:<<<<<<<<<<\n%{public}@\n%{public}@:>>>>>>>>>>"
+ "[SMA] Cached manifest verification result: %i"
+ "[SMA] Error loading Cryptex1 ticket at %@: %@"
+ "[SMA] Error loading trust cache at %@: %@"
+ "[SMA] Failed to deserialize info plist: %{public}@"
+ "[SMA] Failed to instantiate environment"
+ "[SMA] Failed to load trust cache for asset bundle %@. (%s)"
+ "[SMA] Failed to query nonce domain %d: %d (%s)"
+ "[SMA] Info plist verification failed: %d (%s)"
+ "[SMA] Info plist verification succeeded"
+ "[SMA] Loading trustcache for %@"
+ "[SMA] Manifest is empty"
+ "[SMA] Manifest verification failed: %d (%s)"
+ "[SMA] Manifest verification succeeded"
+ "[SMA] Queried nonce digest for domain %d: %@"
+ "[SMA] Querying nonce digests for darwin"
+ "[SMA] Successfully loaded trust cache for Secure Asset bundle: %@"
+ "[SMA] Trust cache and/or ticket for %@ are invalid\ntrustCache=%@\nticket=%@"
+ "[SMA] Unable to acquiring unlock assertion %@: %@"
+ "[SMA] [SecureMAHelper]: Boot task plist does not exist at %@"
+ "[SMA] [SecureMAHelper]: Creating new boot task plist for tracking assets"
+ "[SMA] [SecureMAHelper]: Failed to delete boot plist file at path %@. Error: %@"
+ "[SMA] [SecureMAHelper]: Failed to load existing boot plist at path %@. Error: %@"
+ "[SMA] [SecureMAHelper]: Failed to record %@ entry for asset of type %@ into a property list. %@"
+ "[SMA] [SecureMAHelper]: Failed to record %@ entry for asset of type %@. Opening %@ for writing failed. %s"
+ "[SMA] [SecureMAHelper]: Failed to record %@ entry for asset of type %@. Renaming file from (%@) -> (%@) failed. %s"
+ "[SMA] [SecureMAHelper]: Failed to record %@ entry for asset of type %@. Taking a write barrier failed. %s"
+ "[SMA] [SecureMAHelper]: Failed to record %@ entry for asset of type %@. Writing (expected:%zd, actual:%zd) failed. %s"
+ "[SMA] [SecureMAHelper]: Unable to get MA repository path."
+ "]."
+ "_"
+ "_CompatibilityVersion"
+ "_CompressionAlgorithm"
+ "_ContentVersion"
+ "_DownloadSize"
+ "_IsZipStreamable"
+ "_MasteredVersion"
+ "_Measurement"
+ "_Measurement-SHA256"
+ "_MeasurementAlgorithm"
+ "_UnarchivedSize"
+ "__AssetDefaultGarbageCollectionBehavior"
+ "__BaseURL"
+ "__CanUseLocalCacheServer"
+ "__RelativePath"
+ "_beginAccessWithOptions_nowait:accessMechanismPtr:errorPtr:"
+ "_cachedManifestVerificationResults"
+ "_flags"
+ "_kCFStreamErrorCodeKey"
+ "_kCFStreamErrorDomainKey"
+ "_logBase64Data:description:"
+ "_manifestDataFromStoredTicket:manifestType:"
+ "_manifestDigest:"
+ "_manifestVerifier"
+ "_pathsToPurgeOnGraftFailureInEarlyBootTask"
+ "_queryNonceForHandle:domain:digest:error:"
+ "_storeManifest:manifestType:stage:error:"
+ "_verifyPlist:manifest:manifestType:result:"
+ "aar"
+ "addObjectsFromArray:"
+ "aea"
+ "all"
+ "allKeys"
+ "allObjects"
+ "amfi_load_trust_cache() returned an error."
+ "anyAttribute"
+ "appendFormat:"
+ "appendString:"
+ "asset"
+ "assetId"
+ "assetIdAttributes"
+ "assetIdentifier"
+ "base64EncodedStringWithOptions:"
+ "beginAccessWithOptions:accessMechanismPtr:errorPtr:"
+ "cachedManifestVerificationResults"
+ "cannot load trustcache for an unpersonalized cryptex"
+ "carrier-updates.cdn-apple.com"
+ "characterSetWithCharactersInString:"
+ "checkClient"
+ "checkClockAndCerts"
+ "checkConfiguration"
+ "checkFilesystemState"
+ "checkNetwork"
+ "checkSSO"
+ "checkServer"
+ "checkSpaceNeeded"
+ "checkTimeoutConditions"
+ "classic"
+ "clearBootTaskPlist"
+ "clearBootTaskPlist:"
+ "code"
+ "com.apple.MobileAsset."
+ "com.apple.MobileAsset.DeviceRecoveryBrain"
+ "com.apple.MobileAsset.MacRecoveryOSUpdate"
+ "com.apple.MobileAsset.MacSoftwareUpdate"
+ "com.apple.MobileAsset.MacSplatSoftwareUpdate"
+ "com.apple.MobileAsset.MobileSoftwareUpdate.MacUpdateBrain"
+ "com.apple.MobileAsset.MobileSoftwareUpdate.UpdateBrain"
+ "com.apple.MobileAsset.RecoveryOSUpdate"
+ "com.apple.MobileAsset.RecoveryOSUpdateBrain"
+ "com.apple.MobileAsset.SFRSoftwareUpdate"
+ "com.apple.MobileAsset.SoftwareUpdate"
+ "com.apple.MobileAsset.SoftwareUpdateDocumentation"
+ "com.apple.MobileAsset.SplatSoftwareUpdate"
+ "com.apple.MobileAsset.SystemApp"
+ "com.apple.MobileAsset.WatchSoftwareUpdateDocumentation"
+ "com.apple.MobileAssetError.CancelDownload"
+ "com.apple.MobileAssetError.Download"
+ "com.apple.MobileAssetError.Purge"
+ "com.apple.MobileAssetError.Query"
+ "com.apple.MobileAssetError.Xpc"
+ "com.apple.MobileAssetSSO"
+ "com_apple_MobileAsset"
+ "com_apple_MobileAsset_"
+ "compare:"
+ "componentsJoinedByString:"
+ "componentsSeparatedByCharactersInSet:"
+ "containsString:"
+ "copy"
+ "copyBootTaskPlist:"
+ "currentCalendar"
+ "currentTotalWritten"
+ "data"
+ "dataWithContentsOfURL:options:error:"
+ "dateByAddingComponents:toDate:options:"
+ "dateFromString:"
+ "decodeObjectOfClasses:forKey:"
+ "device-recovery"
+ "dictionaryWithCapacity:"
+ "domain"
+ "downloadContent"
+ "downloadPolicy"
+ "downloadUrl"
+ "e-apfs"
+ "en_US_POSIX"
+ "endAccessWithOptions:accessMechanismPtr:errorPtr:"
+ "endAccessWithOptions_nowait:accessMechanismPtr:errorPtr:"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "failed to %s %s manifest"
+ "failing manifest"
+ "failing payload"
+ "false"
+ "filterUsingPredicate:"
+ "finishDecoding"
+ "flags"
+ "gdmf-auth-stg.apple.com"
+ "gdmf-auth-uat.apple.com"
+ "gdmf-auth.apple.com"
+ "gdmf.apple.com"
+ "generic"
+ "getBootTaskPlistLock"
+ "getObjectFromMessage: could not decode object for key: %{public}s error: %{public}@"
+ "getPlistDictionary"
+ "getRepositoryPath"
+ "graftOrMount:graftingError:"
+ "hasPrefix:"
+ "hasSuffix:"
+ "host"
+ "https"
+ "hw.osenvironment"
+ "i48@0:8@16@24Q32^@40"
+ "iOS"
+ "image4_environment_copy_nonce_digest() failed"
+ "in ensureAndIncrementNumberAtKey nil dict or key value, skipped"
+ "includeSupervised: %@ "
+ "initForReadingFromData:error:"
+ "initWithArray:"
+ "initWithBase64EncodedString:options:"
+ "initWithBytesNoCopy:length:encoding:freeWhenDone:"
+ "initWithCapacity:"
+ "initWithFormat:"
+ "initWithFormat:arguments:"
+ "initWithLocaleIdentifier:"
+ "initWithLong:"
+ "initWithString:"
+ "insertObject:atIndex:"
+ "invertedSet"
+ "isErrorDueToDeviceBeingLocked:"
+ "isSSONeededForURL"
+ "isSupportedMAAnalyticsEventFieldName"
+ "isXml"
+ "kern.bootsessionuuid"
+ "keyEnumerator"
+ "loadTrustCache:"
+ "localizedDescription"
+ "longLongValue"
+ "longValue"
+ "lowercaseString"
+ "macOS"
+ "manifestType"
+ "manifestVerifier"
+ "mutableCopy"
+ "nonAssetIdAttributes"
+ "none"
+ "normalizedAssetType"
+ "numNoLongerStalled"
+ "numStalled"
+ "pallasDynamicAssetId"
+ "pallasNoBuildVersionMatchFound"
+ "pallasNoPMVMatchFound"
+ "pathComponents"
+ "pathExtension"
+ "pathWithComponents:"
+ "pathsToPurgeOnGraftFailureInEarlyBootTask"
+ "pmv"
+ "predicateWithBlock:"
+ "propertyListWithData:options:format:error:"
+ "public"
+ "purpose_"
+ "purpose_%@"
+ "rangeOfCharacterFromSet:"
+ "rangeOfString:"
+ "readBootTaskPlist:"
+ "recordAssetGraftStateForEarlyBootTask:options:"
+ "replaceOccurrencesOfString:withString:options:range:"
+ "requeryIsHelpful"
+ "retryWithBackoff"
+ "safeAtomicWriteToPath"
+ "scheme"
+ "secureMountAuthType"
+ "set"
+ "setByAddingObjectsFromSet:"
+ "setCachedManifestVerificationResults:"
+ "setDateFormat:"
+ "setDay:"
+ "setFlags:"
+ "setLocale:"
+ "setManifestVerifier:"
+ "setPathsToPurgeOnGraftFailureInEarlyBootTask:"
+ "setTimeZone:"
+ "setValue:forKey:"
+ "some"
+ "stage"
+ "store"
+ "storeManifest:manifestType:infoPlist:stage:error:"
+ "string"
+ "stringByTrimmingCharactersInSet:"
+ "stringFromDate:"
+ "stringIsEqual:to:"
+ "stringWithCapacity:"
+ "stringWithContentsOfFile:encoding:error:"
+ "stringWithString:"
+ "substringFromIndex:"
+ "substringWithRange:"
+ "supervised"
+ "supportsLoadableTrustCache:"
+ "ticketPath is nil"
+ "ticketpath"
+ "timeZoneWithAbbreviation:"
+ "timeoutWithDetail"
+ "true"
+ "trustCachePath is nil"
+ "tryAgainLater"
+ "ungraftOrUnmount:ungraftingError:"
+ "unknown"
+ "urlSupportsAuthenticatedPallas"
+ "usableDownload"
+ "userInfo"
+ "v24@0:8Q16"
+ "v28@0:8B16@20"
+ "v32@0:8@16@24"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
+ "verifyManifest:manifestType:"
+ "verifyPlist:manifest:manifestType:result:error:"
+ "whitespaceAndNewlineCharacterSet"
+ "woolyjumper.apple.com"
+ "woolyjumper.sd.apple.com"
+ "writeToFile:atomically:"
+ "writeToFile:atomically:encoding:error:"
+ "xml"
+ "yyyy-MM-dd"
+ "yyyy-MM-dd HH:mm:ss Z"
+ "zip"
+ "{assembleTaskDescriptorWithPurposeAndAutoAssetJobID} invalid autoAssetJobID(ignored):%{public}@"
+ "{isSSONeededForURL} Adding %{public}@ to set of domains needing SSO"
- "%@/%@"
- "/private/var/MobileSoftwareUpdate/Controller/MobileAsset"
- "AMAuthInstallUpdaterCryptex1MobileAssetCopyImg4WithRestoreInfo() failed with error %d (%@)"
- "B32@0:8q16^@24"
- "Clearing previously grafted asset list\n"
- "Failed to clear previously grafted asset list: %@\n"
- "Graft list successfully loaded. Deleting list\n"
- "Unable to create folder for graft list"
- "Unable to determine graft list from previous boot. Skipping grafting: %@\n"
- "[SMA] %@ manifest for %@"
- "[SMA] [SecureMAHelper]: Creating new graft list for tracking grafted assets"
- "[SMA] [SecureMAHelper]: Failed to create folder(%@) for grafted list file: %@"
- "[SMA] [SecureMAHelper]: Failed to delete graft list file at path %@. Error: %@"
- "[SMA] [SecureMAHelper]: Failed to load existing graft list at path %@. Error: %@"
- "[SMA] [SecureMAHelper]: Failed to record %@ entry for asset of type %@ to file %@: %@"
- "[SMA] [SecureMAHelper]: Graft list does not exist at %@"
- "[SMA] [SecureMAHelper]: Successfully created folder(%@) for grafted list file"
- "_manifestDataFromFullyFormedTicket:"
- "_storeManifest:stage:error:"
- "beginAccess:error:"
- "beginAccess_nowait:error:"
- "clearGraftList"
- "clearGraftList:"
- "copyGraftList:"
- "endAccess:error:"
- "endAccess_nowait:error:"
- "getGraftListLock"
- "graftList.plist"
- "graftOrMount:"
- "initWithContentsOfURL:error:"
- "recordAssetGraftStateForEarlyBootTask:"
- "ungraftOrUnmount:"
- "writeToURL:error:"

```
