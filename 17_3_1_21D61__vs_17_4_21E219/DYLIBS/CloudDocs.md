## CloudDocs

> `/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs`

```diff

-2461.80.8.0.0
-  __TEXT.__text: 0x8c34c
-  __TEXT.__auth_stubs: 0x1390
-  __TEXT.__objc_methlist: 0x4fc0
-  __TEXT.__const: 0x108
-  __TEXT.__gcc_except_tab: 0x4244
-  __TEXT.__cstring: 0xb071
-  __TEXT.__oslogstring: 0x94c6
+2720.100.117.0.0
+  __TEXT.__text: 0x8e908
+  __TEXT.__auth_stubs: 0x13a0
+  __TEXT.__objc_methlist: 0x5178
+  __TEXT.__const: 0x118
+  __TEXT.__gcc_except_tab: 0x42f8
+  __TEXT.__cstring: 0xb216
+  __TEXT.__oslogstring: 0x9757
+  __TEXT.__dlopen_cstrs: 0x4c
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2390
-  __TEXT.__objc_classname: 0xd5a
-  __TEXT.__objc_methname: 0x10361
-  __TEXT.__objc_methtype: 0x3f07
-  __TEXT.__objc_stubs: 0xad00
-  __DATA_CONST.__got: 0x510
-  __DATA_CONST.__const: 0x26a8
-  __DATA_CONST.__objc_classlist: 0x2c8
+  __TEXT.__unwind_info: 0x2474
+  __TEXT.__objc_classname: 0xdb3
+  __TEXT.__objc_methname: 0x10957
+  __TEXT.__objc_methtype: 0x4136
+  __TEXT.__objc_stubs: 0xb080
+  __DATA_CONST.__got: 0x528
+  __DATA_CONST.__const: 0x27a8
+  __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0xd0
-  __DATA_CONST.__objc_protolist: 0x138
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xe0a0
-  __DATA_CONST.__objc_selrefs: 0x3a30
+  __DATA_CONST.__objc_const: 0xe248
+  __DATA_CONST.__objc_selrefs: 0x3b78
+  __DATA_CONST.__objc_protorefs: 0x98
+  __DATA_CONST.__objc_classrefs: 0x420
+  __DATA_CONST.__objc_superrefs: 0x248
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__cfstring: 0x5a00
-  __AUTH_CONST.__const: 0xfe0
-  __AUTH_CONST.__objc_const: 0x2720
+  __AUTH_CONST.__cfstring: 0x5940
+  __AUTH_CONST.__const: 0x10c0
+  __AUTH_CONST.__objc_const: 0x2840
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__objc_intobj: 0x438
+  __AUTH_CONST.__objc_intobj: 0x450
   __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__auth_got: 0x9d8
-  __AUTH.__objc_data: 0x11d0
+  __AUTH_CONST.__auth_got: 0x9e0
+  __AUTH.__objc_data: 0x1270
   __AUTH.__data: 0x98
-  __DATA.__objc_protorefs: 0x90
-  __DATA.__objc_classrefs: 0x408
-  __DATA.__objc_superrefs: 0x240
-  __DATA.__objc_ivar: 0x610
-  __DATA.__data: 0x1160
-  __DATA.__bss: 0x200
+  __DATA.__objc_ivar: 0x624
+  __DATA.__data: 0x11d8
+  __DATA.__bss: 0x240
   __DATA.__common: 0x0
   __DATA_DIRTY.__objc_data: 0xa00
   __DATA_DIRTY.__data: 0x38
-  __DATA_DIRTY.__bss: 0x2a8
+  __DATA_DIRTY.__bss: 0x298
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3128
-  Symbols:   10432
-  CStrings:  5379
+  Functions: 3190
+  Symbols:   10649
+  CStrings:  5468
 
Symbols:
+ +[BRFileProviderServicesFactory clientSideServiceSyncProxyForURL:]
+ +[BRPosixOperationsWrapper closeFD:]
+ +[BRPosixOperationsWrapper open:flags:]
+ +[BRRuntimeBehavior isInternalBuild]
+ +[BRRuntimeBehavior isRunningOnIOS]
+ +[BRRuntimeBehavior isRunningOnMacOS]
+ +[BRRuntimeBehavior isSeedBuild]
+ +[BRScreenLockMonitor sharedScreenLockMonitor]
+ +[ICDCollaborationVersion supportsSecureCoding]
+ +[NSError(BRAdditions) brc_errorAcceptShareFailedForItem:]
+ +[NSString(BRCPathAdditions) br_badFilenameAlternativeName]
+ +[NSURL(BRAdditions_Private) br_isURL:syncRootOwnedByICloudDrive:withError:]
+ +[UMUserManager(BRAdditions) br_isInSyncBubble]
+ -[BRFrameworkCloudDocsHelper _queryFastPathsForPrimaryPersona:]
+ -[BRScreenLockMonitor .cxx_destruct]
+ -[BRScreenLockMonitor _getScreenLockedStateFromToken]
+ -[BRScreenLockMonitor _getScreenLockedStateFromToken].cold.1
+ -[BRScreenLockMonitor _invalidateScreenLockManager]
+ -[BRScreenLockMonitor _setScreenLocked:]
+ -[BRScreenLockMonitor addObserver:]
+ -[BRScreenLockMonitor init]
+ -[BRScreenLockMonitor init].cold.1
+ -[BRScreenLockMonitor removeObserver:]
+ -[BRScreenLockMonitor screenLockedUnlockedNotifyToken]
+ -[ICDCollaborationVersion .cxx_destruct]
+ -[ICDCollaborationVersion collaborationSignature]
+ -[ICDCollaborationVersion description]
+ -[ICDCollaborationVersion encodeWithCoder:]
+ -[ICDCollaborationVersion initWithCoder:]
+ -[ICDCollaborationVersion initWithCollaborationSignature:]
+ -[NSArray(BRAdditions) _br_minMaxWithMax:comperator:]
+ -[NSArray(BRAdditions) br_count_if:]
+ -[NSArray(BRAdditions) br_maxWithComparator:]
+ -[NSArray(BRAdditions) br_minWithComparator:]
+ -[NSError(BRAdditions) br_isCKErrorCode:]
+ -[NSError(BRAdditions) br_isCKErrorCode:underlyingErrorCode:]
+ -[NSError(BRFPAdditions) _br_populateErrorMessageOnUserInfo:]
+ -[NSPersonNameComponents(BRAdditions) br_shouldOverwriteExistingName]
+ -[NSURL(BRAdditions) _br_isParentOfURL:strictly:ignoreHomeDirectoryCheck:]
+ -[NSURL(BRAdditions) _br_isParentOfURL:strictly:ignoreHomeDirectoryCheck:].cold.1
+ -[NSURL(BRAdditions) _br_isParentOfURL:strictly:withNonMateralizingIOPolicy:ignoreHomeDirectoryCheck:]
+ -[NSURL(BRAdditions) br_getSyncRootWithError:]
+ -[NSURL(BRAdditions) br_isExistWithNonMateralizingIOPolicy:]
+ -[NSURL(BRAdditions) br_isParentOfURL:ignoreHomeDirectoryCheck:]
+ -[NSURL(BRServiceAdditions) _br_clientSideCollaborationServiceSyncProxy]
+ GCC_except_table153
+ GCC_except_table34
+ GCC_except_table58
+ GCC_except_table64
+ GCC_except_table70
+ GCC_except_table96
+ _BRCXPCICDFileProviderClientSideCollaborationProtocolInterface
+ _BRCXPCICDFileProviderClientSideCollaborationProtocolInterface.iface
+ _BRCXPCICDFileProviderClientSideCollaborationProtocolInterface.once
+ _BREntitlementSyncBubbleClient
+ _BRSpringBoardDeviceLockStateNotification
+ _CFBundleCopyResourceURL
+ _CKUnderlyingErrorDomain
+ _ICDClientSideCollaborationServiceName
+ _NSLocalizedDescriptionKey
+ _NSLocalizedFailureReasonErrorKey
+ _OBJC_CLASS_$_AATermsStringsProvider
+ _OBJC_CLASS_$_BRRuntimeBehavior
+ _OBJC_CLASS_$_BRScreenLockMonitor
+ _OBJC_CLASS_$_ICDCollaborationVersion
+ _OBJC_IVAR_$_BRScreenLockMonitor._notificationQueue
+ _OBJC_IVAR_$_BRScreenLockMonitor._screenLockObservers
+ _OBJC_IVAR_$_BRScreenLockMonitor._screenLocked
+ _OBJC_IVAR_$_BRScreenLockMonitor._screenLockedUnlockedNotifyToken
+ _OBJC_IVAR_$_BRShareOperation._fetchServiceError
+ _OBJC_IVAR_$_ICDCollaborationVersion._collaborationSignature
+ _OBJC_METACLASS_$_BRRuntimeBehavior
+ _OBJC_METACLASS_$_BRScreenLockMonitor
+ _OBJC_METACLASS_$_ICDCollaborationVersion
+ _SeedingLibraryCore.frameworkLibrary
+ __OBJC_$_CLASS_METHODS_BRRuntimeBehavior
+ __OBJC_$_CLASS_METHODS_BRScreenLockMonitor
+ __OBJC_$_CLASS_METHODS_ICDCollaborationVersion
+ __OBJC_$_CLASS_METHODS_UMUserManager(BRAdditions)
+ __OBJC_$_CLASS_PROP_LIST_ICDCollaborationVersion
+ __OBJC_$_INSTANCE_METHODS_BRScreenLockMonitor
+ __OBJC_$_INSTANCE_METHODS_ICDCollaborationVersion
+ __OBJC_$_INSTANCE_VARIABLES_BRScreenLockMonitor
+ __OBJC_$_INSTANCE_VARIABLES_ICDCollaborationVersion
+ __OBJC_$_PROP_LIST_BRScreenLockMonitor
+ __OBJC_$_PROP_LIST_ICDCollaborationVersion
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ICDFileProviderClientSideCollaborationProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ICDFileProviderClientSideCollaborationProtocol
+ __OBJC_$_PROTOCOL_REFS_ICDFileProviderClientSideCollaborationProtocol
+ __OBJC_CLASS_PROTOCOLS_$_ICDCollaborationVersion
+ __OBJC_CLASS_RO_$_BRRuntimeBehavior
+ __OBJC_CLASS_RO_$_BRScreenLockMonitor
+ __OBJC_CLASS_RO_$_ICDCollaborationVersion
+ __OBJC_LABEL_PROTOCOL_$_ICDFileProviderClientSideCollaborationProtocol
+ __OBJC_METACLASS_RO_$_BRRuntimeBehavior
+ __OBJC_METACLASS_RO_$_BRScreenLockMonitor
+ __OBJC_METACLASS_RO_$_ICDCollaborationVersion
+ __OBJC_PROTOCOL_$_ICDFileProviderClientSideCollaborationProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_ICDFileProviderClientSideCollaborationProtocol
+ ___102-[NSURL(BRAdditions) _br_isParentOfURL:strictly:withNonMateralizingIOPolicy:ignoreHomeDirectoryCheck:]_block_invoke
+ ___27-[BRScreenLockMonitor init]_block_invoke
+ ___32+[BRRuntimeBehavior isSeedBuild]_block_invoke
+ ___32-[BRShareOperation initWithURL:]_block_invoke.50
+ ___32-[BRShareOperation initWithURL:]_block_invoke.50.cold.1
+ ___35-[BRScreenLockMonitor addObserver:]_block_invoke
+ ___36+[BRRuntimeBehavior isInternalBuild]_block_invoke
+ ___36-[NSArray(BRAdditions) br_count_if:]_block_invoke
+ ___38-[BRScreenLockMonitor removeObserver:]_block_invoke
+ ___40-[BRScreenLockMonitor _setScreenLocked:]_block_invoke
+ ___46+[BRScreenLockMonitor sharedScreenLockMonitor]_block_invoke
+ ___46-[NSURL(BRAdditions) br_getSyncRootWithError:]_block_invoke
+ ___47+[UMUserManager(BRAdditions) br_isInSyncBubble]_block_invoke
+ ___53-[BRItemCollectionGatherer _addItemCollectionOnItem:]_block_invoke.cold.2
+ ___53-[NSArray(BRAdditions) _br_minMaxWithMax:comperator:]_block_invoke
+ ___60-[NSFileProviderManager(BRAdditions) getFPDomainsWithError:]_block_invoke_2
+ ___60-[NSFileProviderManager(BRAdditions) getFPDomainsWithError:]_block_invoke_2.cold.1
+ ___60-[NSFileProviderManager(BRAdditions) getFPDomainsWithError:]_block_invoke_2.cold.2
+ ___60-[NSURL(BRAdditions) br_isExistWithNonMateralizingIOPolicy:]_block_invoke
+ ___61-[NSError(BRFPAdditions) _br_populateErrorMessageOnUserInfo:]_block_invoke
+ ___61-[NSURL(BRAdditions) br_containerIDIfIsDocumentsContainerURL]_block_invoke_2
+ ___BRCXPCICDFileProviderClientSideCollaborationProtocolInterface_block_invoke
+ ___BRCXPCICDFileProviderClientSideCollaborationProtocolInterface_block_invoke.cold.1
+ ___SeedingLibraryCore_block_invoke
+ ____fetchServiceAutomaticErrorProxyFromURL_block_invoke.9
+ ____preComputeURLSForPersona_block_invoke.cold.2
+ ___block_descriptor_32_e17_B16?0"NSError"8l
+ ___block_descriptor_32_e18_24?0"FPTag"8Q16l
+ ___block_descriptor_32_e21_24?0"NSString"8Q16l
+ ___block_descriptor_32_e25_B32?0"NSString"8Q16^B24l
+ ___block_descriptor_41_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_e8_32r40r_e34_v24?0"NSDictionary"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e9_B16?0^8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e38_"NSString"24?0"NSNumber"8"NSURL"16ls32l8s40l8
+ ___block_descriptor_56_e8_32bs40r_e15_v32?08Q16^B24lr40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e36_v32?0"NSString"8B16B20"NSError"24lr48l8s40l8s32l8
+ ___block_descriptor_58_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_literal_global.12
+ ___block_literal_global.175
+ ___block_literal_global.20
+ ___block_literal_global.3
+ ___block_literal_global.514
+ ___block_literal_global.526
+ ___block_literal_global.557
+ ___block_literal_global.569
+ ___block_literal_global.726
+ ___getSDBuildInfoClass_block_invoke
+ __fetchSynchronousAutomaticErrorProxyFromURL
+ __sl_dlopen
+ _audit_stringSeeding
+ _br_NSNumberComparatorBlock
+ _br_NSNumberComparatorBlock_block_invoke
+ _br_NSNumberComparatorBlock_block_invoke.cold.1
+ _br_NSNumberComparatorBlock_block_invoke.cold.2
+ _br_isInSyncBubble.onceToken
+ _br_isInSyncBubble.res
+ _getSDBuildInfoClass.softClass
+ _isInternalBuild.isInternalBuild
+ _isInternalBuild.onceToken
+ _isSeedBuild.isSeedBuild
+ _isSeedBuild.onceToken
+ _objc_msgSend$_br_isParentOfURL:strictly:ignoreHomeDirectoryCheck:
+ _objc_msgSend$_br_isParentOfURL:strictly:withNonMateralizingIOPolicy:ignoreHomeDirectoryCheck:
+ _objc_msgSend$_br_minMaxWithMax:comperator:
+ _objc_msgSend$_br_populateErrorMessageOnUserInfo:
+ _objc_msgSend$_getScreenLockedStateFromToken
+ _objc_msgSend$_queryFastPathsForPrimaryPersona:
+ _objc_msgSend$_setScreenLocked:
+ _objc_msgSend$br_isCKErrorCode:
+ _objc_msgSend$br_isParentOfURL:ignoreHomeDirectoryCheck:
+ _objc_msgSend$br_isURL:syncRootOwnedByICloudDrive:withError:
+ _objc_msgSend$br_realpathURL
+ _objc_msgSend$clientSideServiceSyncProxyForURL:
+ _objc_msgSend$currentBuildIsSeed
+ _objc_msgSend$currentUser
+ _objc_msgSend$dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:
+ _objc_msgSend$executeXPCWithMaxRetries:error:block:
+ _objc_msgSend$familyName
+ _objc_msgSend$fileURLWithPathComponents:
+ _objc_msgSend$fp_fpfsProviderDomainID:error:
+ _objc_msgSend$fp_homeDirectory
+ _objc_msgSend$fp_lmdURL
+ _objc_msgSend$givenName
+ _objc_msgSend$indexOfObjectWithOptions:passingTest:
+ _objc_msgSend$isSharedIPad
+ _objc_msgSend$neediCloudTermsAcceptanceDeviceSpecificMessage
+ _objc_msgSend$neediCloudTermsAcceptanceTitle
+ _objc_msgSend$screenLockChanged:
+ _objc_msgSend$stringByTrimmingCharactersInSet:
+ _objc_msgSend$uid
+ _objc_msgSend$underlyingErrors
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
+ _sharedScreenLockMonitor.monitor
+ _sharedScreenLockMonitor.onceToken
- +[NSError(BRAdditions) brc_errorCiconiaAborted:]
- +[NSError(BRAdditions) brc_errorCiconiaCannotDefer]
- +[NSError(BRAdditions) brc_errorCiconiaFailed:]
- +[NSError(BRAdditions) brc_errorCiconiaTimedout]
- -[BRDeviceConfiguration .cxx_destruct]
- -[BRDeviceConfiguration configuration]
- -[BRDeviceConfiguration getDeviceConfigurationString]
- -[BRDeviceConfiguration initForTestingDevice:]
- -[NSURL(BRAdditions) _br_isParentOfURL:strictly:]
- -[NSURL(BRAdditions) _br_isParentOfURL:strictly:].cold.1
- -[NSURL(BRAdditions) br_isParentOfURL:strictly:withNonMateralizingIOPolicy:]
- GCC_except_table155
- GCC_except_table35
- GCC_except_table43
- GCC_except_table51
- GCC_except_table53
- GCC_except_table55
- _BRCIsInternalBuild
- _BRCIsInternalBuild.isInternalBuild
- _BRCIsInternalBuild.onceToken
- _BRCiconiaIgnoredItemsErrorDomain
- _BRCiconiaServiceName
- _BREnableCiconiaContext
- _BREntitlementCiconia
- _BRIsFPFSCiconiaOnly
- _BRIsInTheCiconiaContext
- _CFBundleCopyResourceURLForLocalization
- _OBJC_CLASS_$_BRDeviceConfiguration
- _OBJC_IVAR_$_BRDeviceConfiguration._configuration
- _OBJC_METACLASS_$_BRDeviceConfiguration
- __OBJC_$_INSTANCE_METHODS_BRDeviceConfiguration
- __OBJC_$_INSTANCE_VARIABLES_BRDeviceConfiguration
- __OBJC_$_PROP_LIST_BRDeviceConfiguration
- __OBJC_CLASS_RO_$_BRDeviceConfiguration
- __OBJC_METACLASS_RO_$_BRDeviceConfiguration
- ___32-[BRShareOperation initWithURL:]_block_invoke.49
- ___32-[BRShareOperation initWithURL:]_block_invoke.49.cold.1
- ___53-[BRDeviceConfiguration getDeviceConfigurationString]_block_invoke
- ___60-[NSFileProviderManager(BRAdditions) getFPDomainsWithError:]_block_invoke.cold.1
- ___60-[NSFileProviderManager(BRAdditions) getFPDomainsWithError:]_block_invoke.cold.2
- ___76-[NSURL(BRAdditions) br_isParentOfURL:strictly:withNonMateralizingIOPolicy:]_block_invoke
- ___BRCIsInternalBuild_block_invoke
- ____fetchServiceAutomaticErrorProxyFromURL_block_invoke.7
- ___block_descriptor_32_e15_16?0"FPTag"8l
- ___block_descriptor_32_e18_16?0"NSString"8l
- ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"NSString"16^B24ls32l8
- ___block_descriptor_56_e8_32s40s48r_e36_v32?0"NSString"8B16B20"NSError"24ls32l8s40l8r48l8
- ___block_descriptor_57_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- ___block_literal_global.174
- ___block_literal_global.18
- ___block_literal_global.39
- ___block_literal_global.516
- ___block_literal_global.528
- ___block_literal_global.62
- ___block_literal_global.725
- ___block_literal_global.9
- _objc_msgSend$_br_isParentOfURL:strictly:
- _objc_msgSend$br_isParentOfURL:strictly:withNonMateralizingIOPolicy:
- _objc_msgSend$dumpDatabaseTo:containerID:personaID:includeAllItems:reply:
CStrings:
+ "\x06"
+ "-[BRScreenLockMonitor _getScreenLockedStateFromToken]"
+ "-[BRScreenLockMonitor _invalidateScreenLockManager]"
+ "-[BRScreenLockMonitor init]"
+ "-[NSFileProviderManager(BRAdditions) getFPDomainsWithError:]_block_invoke_2"
+ "-[NSURL(BRAdditions) _br_isParentOfURL:strictly:ignoreHomeDirectoryCheck:]"
+ "2720.100.117"
+ "<%@ sig:%@>"
+ "@\"NSProgress\"40@0:8@\"NSSecurityScopedURLWrapper\"16@\"NSFileProviderItemVersion\"24@?<v@?@\"NSFileProviderItemVersion\"@\"NSError\">32"
+ "@\"NSString\"24@?0@\"NSNumber\"8@\"NSURL\"16"
+ "@24@?0@\"FPTag\"8Q16"
+ "@24@?0@\"NSString\"8Q16"
+ "@28@0:8B16@?20"
+ "@40@0:8@16@24@?32"
+ "Accept share failed for item %@"
+ "B16@?0@\"NSError\"8"
+ "B16@?0^@8"
+ "B32@0:8q16q24"
+ "B32@?0@\"NSString\"8Q16^B24"
+ "B36@0:8@16B24B28B32"
+ "B40@0:8@16^B24^@32"
+ "BRCXPCICDFileProviderClientSideCollaborationProtocolInterface_block_invoke"
+ "BRRuntimeBehavior"
+ "BRScreenLockMonitor"
+ "ICDCollaborationVersion"
+ "ICDFileProviderClientSideCollaborationProtocol"
+ "NSUnderlyingError"
+ "Q24@0:8@?16"
+ "SDBuildInfo"
+ "T@\"NSArray\",?,R,C"
+ "T@\"NSData\",?,R,C,N"
+ "T@\"NSData\",?,R,N"
+ "T@\"NSData\",R,N,V_collaborationSignature"
+ "T@\"NSDate\",?,R,C,N"
+ "T@\"NSDictionary\",?,R,N"
+ "T@\"NSError\",?,R,C,N"
+ "T@\"NSFileProviderItemVersion\",?,R,N"
+ "T@\"NSNumber\",?,R,C"
+ "T@\"NSNumber\",?,R,C,GisDownloadRequested"
+ "T@\"NSNumber\",?,R,C,N"
+ "T@\"NSPersonNameComponents\",?,R,N"
+ "T@\"NSSet\",?,R,C"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"NSString\",?,R,N"
+ "T@\"NSURL\",?,R,C"
+ "T@\"UTType\",?,R,C,N"
+ "TB,?,GisSyncRoot"
+ "TB,?,R"
+ "TB,?,R,Gfp_isUbiquitous"
+ "TB,?,R,GisHidden"
+ "TB,?,R,N,Gfp_isAddedByCurrentUser"
+ "TB,?,R,N,Gfp_isLastModifiedByCurrentUser"
+ "TB,?,R,N,GisDownloaded"
+ "TB,?,R,N,GisDownloading"
+ "TB,?,R,N,GisExcludedFromSync"
+ "TB,?,R,N,GisMostRecentVersionDownloaded"
+ "TB,?,R,N,GisShared"
+ "TB,?,R,N,GisSharedByCurrentUser"
+ "TB,?,R,N,GisTopLevelSharedItem"
+ "TB,?,R,N,GisTrashed"
+ "TB,?,R,N,GisUploaded"
+ "TB,?,R,N,GisUploading"
+ "TQ,?,R,N"
+ "Ti,R,N,V_screenLockedUnlockedNotifyToken"
+ "Tq,?,R,N"
+ "T{NSFileProviderTypeAndCreator=II},?,R,N"
+ "[CRIT] Assertion failed: [obj1 isKindOfClass:NSNumber.class]%@"
+ "[CRIT] Assertion failed: [obj2 isKindOfClass:NSNumber.class]%@"
+ "[CRIT] UNREACHABLE: Using client side collaboration service protocol from legacy%@"
+ "[CRIT] UNREACHABLE: fp items should always have a parentItemID set on it - %@%@"
+ "[DEBUG] %@ - received token change notification%@"
+ "[DEBUG] Running in a ICD File Provider, optimizing flow for URL cache based on home directory. Home Directory: %@%@"
+ "[ERROR] %@ - Looks like we don't have permission to view %@%@"
+ "[ERROR] Failed to query whether screen is locked%@"
+ "[ERROR] can't register to screen lock/unlock changes. error: %d%@"
+ "[ERROR] failed to get services for url %@ (%@)%@"
+ "[NOTICE] Unregister for %s%@"
+ "_br_clientSideCollaborationServiceSyncProxy"
+ "_br_isParentOfURL:strictly:ignoreHomeDirectoryCheck:"
+ "_br_isParentOfURL:strictly:withNonMateralizingIOPolicy:ignoreHomeDirectoryCheck:"
+ "_br_minMaxWithMax:comperator:"
+ "_br_populateErrorMessageOnUserInfo:"
+ "_collaborationSignature"
+ "_fetchServiceError"
+ "_getScreenLockedStateFromToken"
+ "_invalidateScreenLockManager"
+ "_notificationQueue"
+ "_queryFastPathsForPrimaryPersona:"
+ "_screenLockObservers"
+ "_screenLocked"
+ "_screenLockedUnlockedNotifyToken"
+ "_setScreenLocked:"
+ "backupDatabaseWithURLWrapper:reply:"
+ "br_NSNumberComparatorBlock_block_invoke"
+ "br_badFilenameAlternativeName"
+ "br_count_if:"
+ "br_getSyncRootWithError:"
+ "br_isCKErrorCode:"
+ "br_isCKErrorCode:underlyingErrorCode:"
+ "br_isExistWithNonMateralizingIOPolicy:"
+ "br_isInSyncBubble"
+ "br_isParentOfURL:ignoreHomeDirectoryCheck:"
+ "br_isURL:syncRootOwnedByICloudDrive:withError:"
+ "br_maxWithComparator:"
+ "br_minWithComparator:"
+ "br_shouldOverwriteExistingName"
+ "brc_errorAcceptShareFailedForItem:"
+ "calculateCollaborationVersionForContents:reply:"
+ "clientSideServiceSyncProxyForURL:"
+ "cloneLatestContentRevisionForItemIdentifier:reply:"
+ "closeFD:"
+ "collaborationSignature"
+ "com.apple.CloudDocs.private.ClientSideCollaboration"
+ "com.apple.br.screen-lock-monitor"
+ "com.apple.private.clouddocs.sync-bubble-client"
+ "com.apple.springboard.lockstate"
+ "currentBuildIsSeed"
+ "currentUser"
+ "dumpDatabaseTo:containerID:personaID:includeAllItems:verbose:reply:"
+ "familyName"
+ "fetchLatestRevisionIntoURL:reply:"
+ "fetchLatestRevisionWithReply:"
+ "fileURLWithPathComponents:"
+ "fp_fpfsProviderDomainID:error:"
+ "fp_homeDirectory"
+ "fp_lmdURL"
+ "generateSmallItemThumbnailForFileObject:reply:"
+ "getSaltingVerificationKeys:"
+ "getSaltingVerificationKeysAtItemIdentifier:reply:"
+ "givenName"
+ "i28@0:8@16i24"
+ "indexOfObjectWithOptions:passingTest:"
+ "initWithCollaborationSignature:"
+ "isInternalBuild"
+ "isRunningOnIOS"
+ "isRunningOnMacOS"
+ "isSeedBuild"
+ "isSharedIPad"
+ "loctable"
+ "n/a"
+ "neediCloudTermsAcceptanceDeviceSpecificMessage"
+ "neediCloudTermsAcceptanceTitle"
+ "open:flags:"
+ "refreshSharingState:"
+ "screenLockChanged:"
+ "screenLockedUnlockedNotifyToken"
+ "setAdvancedDataProtectionEnabled:forContainer:reply:"
+ "sharedScreenLockMonitor"
+ "signature"
+ "softlink:o:path:/System/Library/PrivateFrameworks/Seeding.framework/Seeding"
+ "stringByTrimmingCharactersInSet:"
+ "tmp-bad-filename-"
+ "uid"
+ "underlyingErrors"
+ "uploadContents:baseVersion:reply:"
+ "v24@0:8@?<v@?@\"ICDCollaborationVersion\"@\"NSFileProviderItemVersion\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSData\"@\"NSData\"@\"NSData\"I@\"NSError\">16"
+ "v32@0:8@\"BRFileObjectID\"16@?<v@?@\"NSURL\"@\"NSData\"@\"NSError\">24"
+ "v32@0:8@\"FPSandboxingURLWrapper\"16@?<v@?@\"NSURL\"@\"NSError\">24"
+ "v32@0:8@\"NSSecurityScopedURLWrapper\"16@?<v@?@\"ICDCollaborationVersion\"@\"NSError\">24"
+ "v32@0:8@\"NSSecurityScopedURLWrapper\"16@?<v@?@\"NSURL\"@\"NSFileProviderItemVersion\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSData\"@\"NSData\"I@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSFileProviderItemVersion\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSURL\"@\"NSFileProviderItemVersion\"@\"NSError\">24"
+ "v36@0:8B16@\"NSString\"20@?<v@?@\"NSError\">28"
+ "v36@0:8B16@20@?28"
+ "v56@0:8@\"NSFileHandle\"16@\"NSString\"24@\"NSString\"32B40B44@?<v@?B@\"NSError\">48"
+ "v56@0:8@16@24@32B40B44@?48"
+ "waitForStabilizationWithReply:"
+ "whitespaceAndNewlineCharacterSet"
- "%@:%@;"
- "%@::"
- "-[NSURL(BRAdditions) _br_isParentOfURL:strictly:]"
- "0"
- "1"
- "1.1"
- "2461.80.8"
- "@16@?0@\"FPTag\"8"
- "@16@?0@\"NSString\"8"
- "BRCiconiaIgnoredItemsErrorDomain"
- "BRDeviceConfiguration"
- "EDS"
- "FPFS"
- "T@\"NSArray\",R,C"
- "T@\"NSData\",R,C,N"
- "T@\"NSData\",R,N"
- "T@\"NSDate\",R,C,N"
- "T@\"NSDictionary\",R,N"
- "T@\"NSDictionary\",R,N,V_configuration"
- "T@\"NSError\",R,C,N"
- "T@\"NSFileProviderItemVersion\",R,N"
- "T@\"NSNumber\",R,C"
- "T@\"NSNumber\",R,C,GisDownloadRequested"
- "T@\"NSNumber\",R,C,N"
- "T@\"NSSet\",R,C"
- "T@\"NSURL\",R,C"
- "T@\"UTType\",R,C,N"
- "TB,GisSyncRoot"
- "TB,R,Gfp_isUbiquitous"
- "TB,R,GisHidden"
- "TB,R,N,Gfp_isAddedByCurrentUser"
- "TB,R,N,Gfp_isLastModifiedByCurrentUser"
- "TB,R,N,GisDownloaded"
- "TB,R,N,GisDownloading"
- "TB,R,N,GisExcludedFromSync"
- "TB,R,N,GisMostRecentVersionDownloaded"
- "TB,R,N,GisShared"
- "TB,R,N,GisSharedByCurrentUser"
- "TB,R,N,GisTopLevelSharedItem"
- "TB,R,N,GisTrashed"
- "TB,R,N,GisUploaded"
- "TB,R,N,GisUploading"
- "TESTING"
- "T{NSFileProviderTypeAndCreator=II},R,N"
- "[DEBUG] %@ - [%@] received token change notification%@"
- "_br_isParentOfURL:strictly:"
- "_configuration"
- "backupDatabaseWithURLWrapper:forCiconia:reply:"
- "br_isParentOfURL:strictly:withNonMateralizingIOPolicy:"
- "brc_errorCiconiaAborted:"
- "brc_errorCiconiaCannotDefer"
- "brc_errorCiconiaFailed:"
- "brc_errorCiconiaTimedout"
- "com.apple.CloudDocs.private.Ciconia"
- "com.apple.private.clouddocs.ciconia"
- "configuration"
- "dumpDatabaseTo:containerID:personaID:includeAllItems:reply:"
- "getDeviceConfigurationString"
- "initForTestingDevice:"
- "launchItemCountMismatchChecksAtURL:reply:"
- "migration aborted due to: '%@'"
- "migration could not defer but was asked to"
- "migration failed due to: '%@'"
- "migration timed out"
- "queryLastCiconiaVersion:"
- "reportCleanupFailureDuringSilentMigration:operationType:uuid:version:reply:"
- "reportDummyCiconiaMigration:reply:"
- "reportFinishedMigration:uuid:reply:"
- "reportItemMismatchDuringSilentMigration:information:uuid:reply:"
- "signalStartOfSilentTelemetry:uuid:manual:version:reply:"
- "strings"
- "v32@0:8@\"BRCMigrationReport\"16@?<v@?@\"NSError\">24"
- "v32@?0@\"NSString\"8@\"NSString\"16^B24"
- "v36@0:8@\"FPSandboxingURLWrapper\"16B24@?<v@?@\"NSURL\"@\"NSError\">28"
- "v40@0:8@\"BRCMigrationReport\"16@\"NSUUID\"24@?<v@?@\"NSError\">32"
- "v48@0:8@\"NSError\"16@\"NSString\"24@\"NSUUID\"32@?<v@?@\"NSError\">40"
- "v52@0:8@\"NSDate\"16@\"NSUUID\"24B32Q36@?<v@?@\"NSError\">44"
- "v52@0:8@\"NSFileHandle\"16@\"NSString\"24@\"NSString\"32B40@?<v@?B@\"NSError\">44"
- "v52@0:8@16@24@32B40@?44"
- "v52@0:8@16@24B32Q36@?44"
- "v56@0:8@\"NSError\"16@\"NSString\"24@\"NSUUID\"32Q40@?<v@?@\"NSError\">48"
- "v56@0:8@16@24@32Q40@?48"

```
