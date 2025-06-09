## CoreFoundation

> `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

```diff

-3502.0.0.0.0
-  __TEXT.__text: 0x1b7a14
-  __TEXT.__auth_stubs: 0x31a0
+4030.1.101.0.0
+  __TEXT.__text: 0x1bda54
+  __TEXT.__auth_stubs: 0x31e0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x76ec
-  __TEXT.__const: 0x19b440
-  __TEXT.__oslogstring: 0x5679
-  __TEXT.__cstring: 0x14aceb
-  __TEXT.__gcc_except_tab: 0x44c0
+  __TEXT.__objc_methlist: 0x7a34
+  __TEXT.__const: 0x1a1710
+  __TEXT.__oslogstring: 0x5815
+  __TEXT.__cstring: 0x14b147
+  __TEXT.__gcc_except_tab: 0x44d4
   __TEXT.__ustring: 0x484
   __TEXT.__dof_CFRunLoop: 0x964
   __TEXT.__dof_Cocoa_Aut: 0x486
-  __TEXT.__unwind_info: 0x5dc0
-  __TEXT.__eh_frame: 0x59c
-  __TEXT.__objc_classname: 0xa7c
-  __TEXT.__objc_methname: 0x7fba
-  __TEXT.__objc_methtype: 0xb39a4
-  __TEXT.__objc_stubs: 0x5d00
-  __DATA_CONST.__const: 0x37d170
-  __DATA_CONST.__objc_classlist: 0x460
+  __TEXT.__unwind_info: 0x5800
+  __TEXT.__eh_frame: 0x588
+  __TEXT.__objc_classname: 0xa9a
+  __TEXT.__objc_methname: 0x8323
+  __TEXT.__objc_methtype: 0xb399d
+  __TEXT.__objc_stubs: 0x6060
+  __DATA_CONST.__got: 0x490
+  __DATA_CONST.__const: 0x37d600
+  __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_nlclslist: 0x58
-  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6158
-  __DATA_CONST.__objc_selrefs: 0x2610
+  __DATA_CONST.__objc_selrefs: 0x2738
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_classrefs: 0x278
-  __DATA_CONST.__objc_superrefs: 0x2c0
-  __DATA_CONST.__got: 0x380
-  __DATA_CONST.__objc_arraydata: 0x1620
+  __DATA_CONST.__objc_superrefs: 0x2c8
+  __DATA_CONST.__objc_arraydata: 0x16e0
+  __AUTH_CONST.__auth_got: 0x1908
+  __AUTH_CONST.__const: 0x4d48
+  __AUTH_CONST.__cfstring: 0x1412e0
+  __AUTH_CONST.__objc_const: 0x9ac8
   __AUTH_CONST.__const_cfobj2: 0x40
-  __AUTH_CONST.__const: 0x4838
-  __AUTH_CONST.__cfstring: 0x140f40
-  __AUTH_CONST.__objc_const: 0x3a88
   __AUTH_CONST.__objc_dictobj: 0x7f8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x18e8
+  __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xa50
   __AUTH.__data: 0x58
-  __DATA.__objc_ivar: 0x4f8
-  __DATA.__data: 0xb10
-  __DATA.__thread_vars: 0x18
+  __AUTH.__thread_vars: 0x18
+  __AUTH.__thread_data: 0x4
+  __DATA.__objc_ivar: 0x51c
+  __DATA.__data: 0x6ec
   __DATA.__cf_except_bt: 0x2000
   __DATA.__cf_except_pack: 0x410
-  __DATA.__crash_info: 0x40
-  __DATA.__thread_data: 0x4
-  __DATA.__bss: 0x528
-  __DATA.__common: 0x88
-  __DATA_DIRTY.__const: 0x6690
-  __DATA_DIRTY.__objc_data: 0x2170
-  __DATA_DIRTY.__data: 0x140
-  __DATA_DIRTY.__got: 0x8
-  __DATA_DIRTY.__bss: 0xe58
-  __DATA_DIRTY.__common: 0x380
+  __DATA.__crash_info: 0x148
+  __DATA.__bss: 0x9d8
+  __DATA.__common: 0x98
+  __DATA_DIRTY.__objc_data: 0x21c0
+  __DATA_DIRTY.__data: 0x170
+  __DATA_DIRTY.__bss: 0xe60
+  __DATA_DIRTY.__common: 0x388
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7821F73C-378B-3A10-BE90-EF526B7DBA93
-  Functions: 7865
-  Symbols:   20165
-  CStrings:  100823
+  UUID: D4B41978-0DE5-3D20-BF02-C4E2255BEB3F
+  Functions: 7984
+  Symbols:   20427
+  CStrings:  100935
 
Symbols:
+ +[NSIndirectTaggedPointerString allocWithZone:]
+ +[NSIndirectTaggedPointerString automaticallyNotifiesObserversForKey:]
+ +[NSIndirectTaggedPointerString newIndirectTaggedNSStringWithConstantNullTerminatedASCIIBytes_:length_:]
+ +[NSObject(NSObject) load].cold.1
+ -[CFPDSource validateSandboxForRead:containerPath:].cold.6
+ -[CFPDSource validateSandboxForWrite:containerPath:].cold.3
+ -[NSIndirectTaggedPointerString UTF8String]
+ -[NSIndirectTaggedPointerString _fastCStringContents:]
+ -[NSIndirectTaggedPointerString _fastCharacterContents]
+ -[NSIndirectTaggedPointerString _getCString:maxLength:encoding:]
+ -[NSIndirectTaggedPointerString autorelease]
+ -[NSIndirectTaggedPointerString cStringUsingEncoding:]
+ -[NSIndirectTaggedPointerString characterAtIndex:]
+ -[NSIndirectTaggedPointerString compare:options:range:locale:]
+ -[NSIndirectTaggedPointerString copyWithZone:]
+ -[NSIndirectTaggedPointerString copy]
+ -[NSIndirectTaggedPointerString fastestEncoding]
+ -[NSIndirectTaggedPointerString getBytes:maxLength:usedLength:encoding:options:range:remainingRange:]
+ -[NSIndirectTaggedPointerString getCharacters:range:]
+ -[NSIndirectTaggedPointerString hash]
+ -[NSIndirectTaggedPointerString isEqual:]
+ -[NSIndirectTaggedPointerString isEqualToString:]
+ -[NSIndirectTaggedPointerString isNSString__]
+ -[NSIndirectTaggedPointerString length]
+ -[NSIndirectTaggedPointerString release]
+ -[NSIndirectTaggedPointerString retainCount]
+ -[NSIndirectTaggedPointerString retain]
+ -[NSIndirectTaggedPointerString smallestEncoding]
+ -[NSIndirectTaggedPointerString substringWithRange:]
+ -[_CFXPreferences nonLaunchPersonaUID]
+ -[_CFXPreferencesHandle copyPrefs].cold.1
+ -[_CFXPreferencesHandle forEachPrefsPerformBlock:]
+ -[_CFXPreferencesHandle setNonLaunchPersonaOverride:]
+ GCC_except_table101
+ GCC_except_table109
+ GCC_except_table112
+ GCC_except_table116
+ GCC_except_table119
+ GCC_except_table123
+ GCC_except_table124
+ GCC_except_table128
+ GCC_except_table132
+ GCC_except_table138
+ GCC_except_table146
+ GCC_except_table147
+ GCC_except_table148
+ GCC_except_table151
+ GCC_except_table156
+ GCC_except_table158
+ GCC_except_table159
+ GCC_except_table169
+ GCC_except_table176
+ GCC_except_table178
+ GCC_except_table198
+ GCC_except_table205
+ GCC_except_table237
+ GCC_except_table240
+ GCC_except_table263
+ GCC_except_table46
+ GCC_except_table65
+ GCC_except_table75
+ GCC_except_table93
+ GCC_except_table99
+ _CFAllocatorCreateWithZone
+ _CFAttributedStringGetStatisticalWritingDirections
+ _CFGetDirectionalOverridesStrategyForStatisticalWritingDirections
+ _CFRunLoopGetRunOptions
+ _CFRunLoopRunInModeWithOptions
+ _CFSetDirectionalOverridesStrategyForStatisticalWritingDirections
+ _CFShowURL.cold.1
+ _CFURLCanBeDecomposed.cold.1
+ _CFURLCopyAbsoluteURL.cold.1
+ _CFURLCopyFileSystemPath.cold.1
+ _CFURLCopyFragment.cold.1
+ _CFURLCopyLastPathComponent.cold.1
+ _CFURLCopyNetLocation.cold.1
+ _CFURLCopyParameterString.cold.1
+ _CFURLCopyParameterString.onceToken.34
+ _CFURLCopyPath.cold.1
+ _CFURLCopyPathExtension.cold.1
+ _CFURLCopyQueryString.cold.1
+ _CFURLCopyResourceSpecifier.cold.1
+ _CFURLCopyScheme.cold.1
+ _CFURLCreateAbsoluteURLWithBytes.cold.1
+ _CFURLCreateCopyAppendingPathComponent.cold.1
+ _CFURLCreateCopyAppendingPathExtension.cold.1
+ _CFURLCreateCopyAppendingPathExtension.cold.2
+ _CFURLCreateCopyDeletingLastPathComponent.cold.1
+ _CFURLCreateCopyDeletingPathExtension.cold.1
+ _CFURLCreateStringWithFileSystemPath.cold.1
+ _CFURLCreateStringWithFileSystemPath.cold.2
+ _CFURLCreateWithBytes.cold.1
+ _CFURLCreateWithString.cold.1
+ _CFURLGetBaseURL.cold.1
+ _CFURLGetByteRangeForComponent.cold.1
+ _CFURLGetBytes.cold.1
+ _CFURLGetBytesUsingEncoding.cold.1
+ _CFURLGetFileSystemRepresentation.cold.1
+ _CFURLGetPortNumber.cold.2
+ _CFURLGetString.cold.1
+ _CFURLHasDirectoryPath.cold.1
+ _CFURLIsFileReferenceURL.cold.1
+ _NSCalendarIdentifierBangla
+ _NSCalendarIdentifierDangi
+ _NSCalendarIdentifierGujarati
+ _NSCalendarIdentifierKannada
+ _NSCalendarIdentifierMalayalam
+ _NSCalendarIdentifierMarathi
+ _NSCalendarIdentifierOdia
+ _NSCalendarIdentifierTamil
+ _NSCalendarIdentifierTelugu
+ _NSCalendarIdentifierVietnamese
+ _NSCalendarIdentifierVikram
+ _NSURLUbiquitousItemIsSyncPausedKey
+ _NSURLUbiquitousItemSupportedSyncControlsKey
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSIndirectTaggedPointerString
+ _OBJC_CLASS_$_NSMutableAttributedString
+ _OBJC_CLASS_$_NSMutableCharacterSet
+ _OBJC_CLASS_$_NSNotification
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSString
+ _OBJC_IVAR_$_NSCache._notificationLock
+ _OBJC_IVAR_$_NSCache._notificationToken
+ _OBJC_IVAR_$_NSCache._observesNotification
+ _OBJC_IVAR_$__CFXPreferences._nonLaunchPersonaUID
+ _OBJC_IVAR_$__CFXPreferencesHandle.checkedProcessCanHaveMultiplePersonas
+ _OBJC_IVAR_$__CFXPreferencesHandle.nonLaunchPersonaID
+ _OBJC_IVAR_$__CFXPreferencesHandle.nonLaunchPersonaPrefs
+ _OBJC_IVAR_$__CFXPreferencesHandle.processCanHaveMultiplePersonas
+ _OBJC_IVAR_$___NSArrayI.list
+ _OBJC_IVAR_$___NSArrayI.used
+ _OBJC_METACLASS_$_NSError
+ _OBJC_METACLASS_$_NSIndirectTaggedPointerString
+ _OBJC_METACLASS_$_NSMutableAttributedString
+ _OBJC_METACLASS_$_NSMutableCharacterSet
+ _OBJC_METACLASS_$_NSMutableString
+ _OBJC_METACLASS_$_NSNotification
+ _OBJC_METACLASS_$_NSNumber
+ _OBJC_METACLASS_$_NSString
+ __CFBytesInASCII
+ __CFIndirectTaggedPointerStringGetContents
+ __CFLookupDiskArbitrationFunction
+ __CFLookupDiskArbitrationFunction.cold.1
+ __CFLookupDiskArbitrationFunction.image
+ __CFLookupDiskArbitrationFunction.onceToken
+ __CFPNLPO
+ __CFPNLPO_block_invoke.observationCallBackQueue
+ __CFPNLPO_block_invoke.onceToken
+ __CFRunLoopObserverSetRecursive
+ __CFRunLoopRunCleanup
+ __CFRunLoopRunCleanup.cold.1
+ __CFRunLoopRunSpecificWithOptions
+ __CFRunLoopRunSpecificWithOptions.cold.1
+ __CFRunLoopRunSpecificWithOptions.cold.2
+ __CFRunLoopRunSpecificWithOptions.onceToken
+ __CFRunLoopRunSpecificWithOptions.runloopNestingLevel
+ __CFRunLoopRunSpecificWithOptions.runloopNestingLevel$tlv$init
+ __CFStringCreateIndirectASCIITaggedPointerString
+ __CFStringCreateStringWithValidatedFormatAuxWithDesc
+ __CFStringCreateWithASCIIBytesNoCopyOrIndirectTagged
+ __CFStringCreateWithASCIICStringNoCopyOrIndirectTagged
+ __CFStringSaveUserDefaultEncoding.cold.1
+ __CFURLCopyComponents.cold.1
+ __CFURLCopyFileURL.cold.1
+ __CFURLCopyFragment.cold.1
+ __CFURLCopyHostName.cold.2
+ __CFURLCopyPassword.cold.2
+ __CFURLCopyPath.cold.1
+ __CFURLCopyQueryString.cold.1
+ __CFURLCopyUserName.cold.2
+ __CFURLCreateCopyAppendingPathComponent.cold.1
+ __CFURLCreateWithArbitraryString
+ __CFURLCreateWithArbitraryString.cold.1
+ __CFURLCreateWithFileSystemPath.cold.1
+ __CFURLCreateWithFileSystemPathCachingResourcePropertiesForKeys.cold.1
+ __CFURLCreateWithFileSystemRepresentation.cold.1
+ __CFURLGetEncoding.cold.1
+ __CFURLHasFileURLScheme.cold.1
+ __CFVolumeObserverCreate
+ __CFVolumeObserverGetTypeID
+ __CFVolumeObserverGetTypeID.cold.1
+ __CFVolumeObserverGetUnmountDissenterForDisk
+ __CFVolumeObserverInvalidate
+ __CFVolumeObserverInvalidateWithCompletionHandler
+ __CFVolumeObserverSetUnmountDissenterForDisk
+ __MergedGlobals.58
+ __NSIndirectTaggedPointerStringIsEqualToCFString
+ __NSIndirectTaggedPointerStringIsEqualToTaggedPointer
+ __NSInlineTaggedPointerStringIsEqualToTaggedPointer
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSObject_$_NSObject
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSObject_$_NSKindOfAdditions
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSObject_$_NSObject
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSObject_$___NSCFType
+ __OBJC_$_CATEGORY_NSObject_$___NSCFType
+ __OBJC_$_CLASS_METHODS_NSIndirectTaggedPointerString
+ __OBJC_$_CLASS_METHODS__CFXPreferences
+ __OBJC_$_INSTANCE_METHODS_NSDictionary
+ __OBJC_$_INSTANCE_METHODS_NSIndirectTaggedPointerString
+ __OBJC_$_INSTANCE_METHODS_NSMutableDictionary
+ __OBJC_CLASS_RO_$_NSIndirectTaggedPointerString
+ __OBJC_METACLASS_RO_$_NSIndirectTaggedPointerString
+ __VolumeIsAutomounted
+ __VolumeObserverCopyDebugDesc
+ __VolumeObserverDiskAppearedCallback
+ __VolumeObserverDiskDescriptionChangedCallback
+ __VolumeObserverDiskDisappearedCallback
+ __VolumeObserverDiskUnmountApprovalCallback
+ __VolumeObserverFinalize
+ __VolumeObserverIdleCallback
+ __VolumeObserverInvalidate
+ ___112-[_CFXPreferences(SearchListAdditions) with23930198HackSourceForIdentifier:user:byHost:container:cloud:perform:]_block_invoke.135
+ ___26+[NSObject(NSObject) load]_block_invoke
+ ___38-[_CFXPreferences flushManagedSources]_block_invoke.66
+ ___65-[_CFXPreferences _setupNewDaemonConnection:invalidationHandler:]_block_invoke.100
+ ___65-[_CFXPreferences _setupNewDaemonConnection:invalidationHandler:]_block_invoke.107
+ ___CFDataSetDontDeallocate
+ ___CFDiskArbitration_DADiskCopyDescription
+ ___CFDiskArbitration_DADiskCopyDescription.cold.1
+ ___CFDiskArbitration_DADiskCopyDescription.dyfunc
+ ___CFDiskArbitration_DADiskCopyDescription.onceToken
+ ___CFDiskArbitration_DASessionSetDispatchQueue
+ ___CFDiskArbitration_DASessionSetDispatchQueue.cold.1
+ ___CFDiskArbitration_DASessionSetDispatchQueue.dyfunc
+ ___CFDiskArbitration_DASessionSetDispatchQueue.onceToken
+ ___CFDiskArbitration_kDADiskDescriptionVolumeNameKey
+ ___CFDiskArbitration_kDADiskDescriptionVolumePathKey
+ ___CFStringAppendFormatCore.cold.1
+ ___CFStringAppendFormatCore.warnOnce
+ ___CFStringCreateImmutableFunnel3.cold.3
+ ___CFStringEncodingGetNameAsCF
+ ___CFStringFindTypeAndSizeForArgumentIndex
+ ___CFToBig5Core
+ ___CFToGB2312
+ ___CFURLCopyDescription.cold.1
+ ___CFURLCopyFormattingDescription.cold.1
+ ___CFURLCopyParameterString_block_invoke
+ ___CFURLCopyParameterString_block_invoke.35
+ ___CFURLCopyParameterString_block_invoke.35.cold.1
+ ___CFURLCopyParameterString_block_invoke.cold.1
+ ___CFURLCreateCopyAppendingPathComponent.cold.1
+ ___CFURLCreatePathForFileID
+ ___CFURLDeallocate.cold.1
+ ___CFURLEqual.cold.1
+ ___CFURLHash.cold.1
+ ___CFURLReservedPtr.cold.1
+ ___CFURLResourceInfoPtr.cold.1
+ ___CFURLResourceInfoPtr.cold.2
+ ___CFURLSetReservedPtr.cold.1
+ ___CFURLSetResourceInfoPtr.cold.1
+ ___CFURLSetResourceInfoPtr.cold.2
+ ___CFVolumeObserverClass
+ ____CFLookupDiskArbitrationFunction_block_invoke
+ ____CFPrefsGetSuiteContainer_block_invoke_2.cold.2
+ ____CFPrefsGetSuiteContainer_block_invoke_2.cold.3
+ ____CFPrefsResetPreferences_block_invoke
+ ____CFPrefsResetUserSessionPreferences_block_invoke
+ ____CFRunLoopRunSpecificWithOptions_block_invoke
+ ____CFVolumeObserverGetTypeID_block_invoke
+ ____CFVolumeObserverInvalidateWithCompletionHandler_block_invoke
+ ____InitializeDiskArbitrationKeys_block_invoke
+ ____VolumeObserverFinalize_block_invoke
+ ____VolumeObserverInstallIdleTimer_block_invoke
+ ____VolumeObserverInvalidate_block_invoke
+ _____CFDiskArbitration_DADiskCopyDescription_block_invoke
+ _____CFDiskArbitration_DARegisterDiskAppearedCallback_block_invoke
+ _____CFDiskArbitration_DARegisterDiskDescriptionChangedCallback_block_invoke
+ _____CFDiskArbitration_DARegisterDiskDisappearedCallback_block_invoke
+ _____CFDiskArbitration_DARegisterDiskUnmountApprovalCallback_block_invoke
+ _____CFDiskArbitration_DARegisterIdleCallback_block_invoke
+ _____CFDiskArbitration_DASessionCreate_block_invoke
+ _____CFDiskArbitration_DASessionSetDispatchQueue_block_invoke
+ _____CFStringAppendFormatCore_block_invoke
+ ____foundation_swift_nsurl_feature_enabled_block_invoke
+ ___block_descriptor_32_e25_v16?0"_CFXPreferences"8l
+ ___block_descriptor_33_e25_v16?0"_CFXPreferences"8l
+ ___block_descriptor_91_e8_32o40o48o_e22_^{__CFDictionary=}8?0ls32l8s40l8s48l8
+ ___block_descriptor_tmp.25
+ ___block_descriptor_tmp.32
+ ___block_descriptor_tmp.40
+ ___block_descriptor_tmp.44
+ ___block_descriptor_tmp.48
+ ___block_descriptor_tmp.52
+ ___block_descriptor_tmp.56
+ ___block_descriptor_tmp.57
+ ___block_literal_global.109
+ ___block_literal_global.120
+ ___block_literal_global.123
+ ___block_literal_global.132
+ ___block_literal_global.160
+ ___block_literal_global.170
+ ___block_literal_global.176
+ ___block_literal_global.189
+ ___block_literal_global.193
+ ___block_literal_global.195
+ ___block_literal_global.23
+ ___block_literal_global.243
+ ___block_literal_global.247
+ ___block_literal_global.255
+ ___block_literal_global.27
+ ___block_literal_global.30
+ ___block_literal_global.34
+ ___block_literal_global.46
+ ___block_literal_global.50
+ ___block_literal_global.54
+ ___block_literal_global.56
+ ___sharedPreferencesHandle_block_invoke
+ __foundation_swift_nsurl_feature_enabled
+ __foundation_swift_nsurl_feature_enabled.cold.1
+ __foundation_swift_nsurl_feature_enabled.featureEnabled
+ __foundation_swift_nsurl_feature_enabled.onceToken
+ _countByEnumeratingWithState:objects:count:.const_mu.45
+ _decomposeToRFC1808.cold.1
+ _dispatch_barrier_sync
+ _isEqualToTaggedPointer
+ _kCFBanglaCalendar
+ _kCFCalendarIdentifierBangla
+ _kCFCalendarIdentifierDangi
+ _kCFCalendarIdentifierGujarati
+ _kCFCalendarIdentifierKannada
+ _kCFCalendarIdentifierMalayalam
+ _kCFCalendarIdentifierMarathi
+ _kCFCalendarIdentifierOdia
+ _kCFCalendarIdentifierTamil
+ _kCFCalendarIdentifierTelugu
+ _kCFCalendarIdentifierVietnamese
+ _kCFCalendarIdentifierVikram
+ _kCFDangiCalendar
+ _kCFGujaratiCalendar
+ _kCFKannadaCalendar
+ _kCFMalayalamCalendar
+ _kCFMarathiCalendar
+ _kCFOdiaCalendar
+ _kCFTamilCalendar
+ _kCFTeluguCalendar
+ _kCFURLUbiquitousItemIsSyncPausedKey
+ _kCFURLUbiquitousItemSupportedSyncControlsKey
+ _kCFVietnameseCalendar
+ _kCFVikramCalendar
+ _kpersona_pidinfo
+ _load.once
+ _notFoundRange
+ _objc_msgSend$URLByAppendingPathExtension:
+ _objc_msgSend$URLByDeletingLastPathComponent
+ _objc_msgSend$URLByDeletingPathExtension
+ _objc_msgSend$_URLByAppendingPathComponent:isDirectory:encodingSlashes:
+ _objc_msgSend$_cfurlResourceSpecifier
+ _objc_msgSend$_cfurlWithString:encoding:relativeToURL:encodingInvalidCharacters:forceBaseURL:
+ _objc_msgSend$_compatibilityAbsoluteURL
+ _objc_msgSend$_encoding
+ _objc_msgSend$_fileSystemPath:resolveAgainstBase:
+ _objc_msgSend$_fileURLWithPath:isDirectory:relativeToURL:
+ _objc_msgSend$_fileURLWithPath:pathStyle:isDirectory:relativeToURL:
+ _objc_msgSend$_fragment:
+ _objc_msgSend$_host:
+ _objc_msgSend$_isDecomposable
+ _objc_msgSend$_lastPathComponent
+ _objc_msgSend$_netLocation
+ _objc_msgSend$_originalString
+ _objc_msgSend$_password:
+ _objc_msgSend$_query:
+ _objc_msgSend$_rangeForComponent:rangeIncludingSeparators:
+ _objc_msgSend$_relativePath:
+ _objc_msgSend$_resourceInfoPtr
+ _objc_msgSend$_user:
+ _objc_msgSend$forEachPrefsPerformBlock:
+ _objc_msgSend$hasDirectoryPath
+ _objc_msgSend$pathExtension
+ _objc_msgSend$set_resourceInfoPtr:
+ _os_log_shim_with_CFString_4NSLog
+ _processParagraph
+ _sUseOuterDirectionalOverride
+ _u_charDirection
+ _u_charType
- GCC_except_table113
- GCC_except_table115
- GCC_except_table120
- GCC_except_table127
- GCC_except_table129
- GCC_except_table135
- GCC_except_table143
- GCC_except_table144
- GCC_except_table145
- GCC_except_table149
- GCC_except_table152
- GCC_except_table153
- GCC_except_table155
- GCC_except_table160
- GCC_except_table170
- GCC_except_table173
- GCC_except_table174
- GCC_except_table199
- GCC_except_table206
- GCC_except_table239
- GCC_except_table241
- GCC_except_table254
- GCC_except_table45
- GCC_except_table68
- GCC_except_table90
- GCC_except_table91
- GCC_except_table96
- _CFCopyDescription.cold.1
- _CFCopyDescription.cold.2
- _CFCopyDescription.cold.3
- _CFCopyFullUserName
- _CFEqual.cold.3
- _CFEqual.cold.4
- _CFEqual.cold.5
- _CFEqual.cold.6
- _CFEqual.cold.7
- _CFGetTypeID.cold.1
- _CFHash.cold.2
- _CFHash.cold.3
- _CFHash.cold.4
- _CFRunLoopRunSpecific.cold.1
- _CFRunLoopRunSpecific.cold.2
- _CFRunLoopRunSpecific.cold.3
- _CFRunLoopRunSpecific.onceToken
- _CFRunLoopRunSpecific.runloopNestingLevel
- _CFRunLoopRunSpecific.runloopNestingLevel$tlv$init
- _OBJC_IVAR_$___NSArrayI.storage
- __CFBundleCopyLanguageAbbreviationForLanguageCode
- __CFBundleCopyLoadedImagePathForAddress
- __CFBundleSupportsFHSBundles
- __CFBundleSupportsFreestandingBundles
- __CFCharacterSetCreateCopy
- __CFCharacterSetCreateMutableCopy
- __CFCharacterSetInitCopyingSet
- __CFCharacterSetIsLongCharacterMember
- __CFDataInit
- __CFGetNonObjCTypeID.cold.1
- __CFIsMainThread
- __CFNonObjCEqual.cold.2
- __CFNonObjCEqual.cold.3
- __CFNonObjCEqual.cold.4
- __CFNonObjCEqual.cold.5
- __CFNonObjCHash.cold.1
- __CFNumberInitBool
- __CFNumberInitDouble
- __CFNumberInitFloat
- __CFNumberInitInt
- __CFNumberInitInt16
- __CFNumberInitInt32
- __CFNumberInitInt64
- __CFNumberInitInt8
- __CFNumberInitUInt
- __CFNumberInitUInt16
- __CFNumberInitUInt32
- __CFNumberInitUInt64
- __CFNumberInitUInt8
- __CFPrefsMessageSenderIsSandboxed
- __CFPrefsMessageSenderIsSandboxed.cold.1
- __CFURLInitAbsoluteURLWithBytes
- __CFURLInitWithFileSystemPathRelativeToBase
- __CFURLInitWithURLString
- __OBJC_$_CLASS_METHODS_NSObject(NSObject)
- __OBJC_$_CLASS_METHODS__CFXPreferences(SourceAdditions|SearchListAdditions)
- __OBJC_$_INSTANCE_METHODS_NSDictionary(NSSharedKeySetDictionary)
- __OBJC_$_INSTANCE_METHODS_NSMutableDictionary(NSSharedKeySetDictionary)
- __OBJC_$_INSTANCE_METHODS_NSObject(NSKindOfAdditions|__NSCFType)
- __OBJC_$_INSTANCE_METHODS_NSObject(NSObject)
- ___112-[_CFXPreferences(SearchListAdditions) with23930198HackSourceForIdentifier:user:byHost:container:cloud:perform:]_block_invoke.132
- ___38-[_CFXPreferences flushManagedSources]_block_invoke.57
- ___65-[_CFXPreferences _setupNewDaemonConnection:invalidationHandler:]_block_invoke.91
- ___65-[_CFXPreferences _setupNewDaemonConnection:invalidationHandler:]_block_invoke.98
- ___CFAttributedLocalizedStringDictionaryApplyFunction
- ___CFCopyFormattingDescription.cold.1
- ___CFCopyFormattingDescription.cold.2
- ___CFCopyFormattingDescription.cold.3
- ___CFGenericTypeID.cold.1
- ___CFNumberInit
- ___CFRunLoopRunSpecific_block_invoke
- ___CFURLCopyParameterString_block_invoke.30
- ___CFURLCopyParameterString_block_invoke.30.cold.1
- ___CFVariableWidthStringApplyFunction
- ____CFICURemoveVariableNameForHeapPointer
- ____CFPrefsCopyDefaultPreferences_block_invoke
- ____forwarding___.cold.7
- ____postProcessStringsDict_block_invoke
- ___block_descriptor_73_e34_^{__CFString=}16?0^{__CFString=}8l
- ___block_descriptor_83_e8_32o40o48o_e22_^{__CFDictionary=}8?0ls32l8s40l8s48l8
- ___block_literal_global.100
- ___block_literal_global.124
- ___block_literal_global.157
- ___block_literal_global.167
- ___block_literal_global.173
- ___block_literal_global.179
- ___block_literal_global.181
- ___block_literal_global.229
- ___block_literal_global.232
- ___block_literal_global.236
- ___block_literal_global.60
- __block_invoke.observationCallBackQueue
- __block_invoke.onceToken
- __initializeClient
- __loadStringsInOrder
- __unnamed_array_storage
- __unnamed_array_storage.100
- __unnamed_array_storage.101
- __unnamed_array_storage.103
- __unnamed_array_storage.104
- __unnamed_array_storage.105
- __unnamed_array_storage.107
- __unnamed_array_storage.108
- __unnamed_array_storage.109
- __unnamed_array_storage.111
- __unnamed_array_storage.112
- __unnamed_array_storage.115
- __unnamed_array_storage.116
- __unnamed_array_storage.118
- __unnamed_array_storage.119
- __unnamed_array_storage.120
- __unnamed_array_storage.122
- __unnamed_array_storage.123
- __unnamed_array_storage.124
- __unnamed_array_storage.127
- __unnamed_array_storage.128
- __unnamed_array_storage.131
- __unnamed_array_storage.132
- __unnamed_array_storage.133
- __unnamed_array_storage.136
- __unnamed_array_storage.137
- __unnamed_array_storage.138
- __unnamed_array_storage.139
- __unnamed_array_storage.140
- __unnamed_array_storage.141
- __unnamed_array_storage.144
- __unnamed_array_storage.145
- __unnamed_array_storage.151
- __unnamed_array_storage.152
- __unnamed_array_storage.155
- __unnamed_array_storage.156
- __unnamed_array_storage.165
- __unnamed_array_storage.166
- __unnamed_array_storage.169
- __unnamed_array_storage.170
- __unnamed_array_storage.173
- __unnamed_array_storage.174
- __unnamed_array_storage.189
- __unnamed_array_storage.190
- __unnamed_array_storage.196
- __unnamed_array_storage.197
- __unnamed_array_storage.200
- __unnamed_array_storage.201
- __unnamed_array_storage.204
- __unnamed_array_storage.205
- __unnamed_array_storage.208
- __unnamed_array_storage.209
- __unnamed_array_storage.215
- __unnamed_array_storage.216
- __unnamed_array_storage.219
- __unnamed_array_storage.220
- __unnamed_array_storage.223
- __unnamed_array_storage.224
- __unnamed_array_storage.295
- __unnamed_array_storage.31
- __unnamed_array_storage.48
- __unnamed_array_storage.49
- __unnamed_array_storage.52
- __unnamed_array_storage.53
- __unnamed_array_storage.539
- __unnamed_array_storage.540
- __unnamed_array_storage.62
- __unnamed_array_storage.63
- __unnamed_array_storage.69
- __unnamed_array_storage.70
- __unnamed_array_storage.76
- __unnamed_array_storage.77
- __unnamed_array_storage.79
- __unnamed_array_storage.80
- __unnamed_array_storage.81
- __unnamed_array_storage.819
- __unnamed_array_storage.820
- __unnamed_array_storage.823
- __unnamed_array_storage.824
- __unnamed_array_storage.827
- __unnamed_array_storage.828
- __unnamed_array_storage.831
- __unnamed_array_storage.832
- __unnamed_array_storage.835
- __unnamed_array_storage.836
- __unnamed_array_storage.839
- __unnamed_array_storage.84
- __unnamed_array_storage.840
- __unnamed_array_storage.85
- __unnamed_array_storage.91
- __unnamed_array_storage.92
- __unnamed_array_storage.95
- __unnamed_array_storage.96
- __unnamed_array_storage.99
- _countByEnumeratingWithState:objects:count:.const_mu.43
- _createErrorReply
- _os_log_shim_with_CFString
CStrings:
+ "%@-fakePersona(%d)"
+ "%s<%p> (Domain: %@, Container: %@ Non-launch persona: %d)"
+ "/System/Library/Frameworks/DiskArbitration.framework/DiskArbitration"
+ "<CFVolumeObserver %p> { INVALIDATED }"
+ "<CFVolumeObserver %p> {queue = %p, eventsToObserve = 0x%lx, options = 0x%lx, observer = %p}"
+ "@32@0:8r*16Q24"
+ "CFStringCreateWithCString can only be called with an c-string compatible encoding"
+ "CFVolumeObserver"
+ "CFVolumeObserver: Notifying client about disk %{public}@ (%{private}@) because it's path changed to NULL."
+ "CFVolumeObserver: Notifying client about disk %{public}@ (%{private}@) being unmounted because it disappeared."
+ "DADiskCopyDescription"
+ "DARegisterDiskAppearedCallback"
+ "DARegisterDiskDescriptionChangedCallback"
+ "DARegisterDiskDisappearedCallback"
+ "DARegisterDiskUnmountApprovalCallback"
+ "DARegisterIdleCallback"
+ "DASessionCreate"
+ "DASessionSetDispatchQueue"
+ "NSIndirectTaggedPointerString"
+ "NSIndirectTaggedPointerString cannot be allocated"
+ "NSSwiftURL"
+ "NSURLUbiquitousItemIsSyncPausedKey"
+ "NSURLUbiquitousItemSupportedSyncControlsKey"
+ "NSURLUseSwift"
+ "Passing an object as the argument to a %%s format string is invalid, and will crash in a future release of the operating system. Call it with a char * as the argument instead. This warning is displayed only once."
+ "Process %{public}s (%{public}d) running as root is attempting to look up an app group container. That's not supported"
+ "Replacing preferences for non-launch persona UID change: %u -> %u %{public}@"
+ "URLByAppendingPathExtension:"
+ "URLByDeletingLastPathComponent"
+ "URLByDeletingPathExtension"
+ "Unknown value for considerWordDirectionality: %d"
+ "User default encoding must be c-string compatible"
+ "_URLByAppendingPathComponent:isDirectory:encodingSlashes:"
+ "_cfurlResourceSpecifier"
+ "_cfurlWithString:encoding:relativeToURL:encodingInvalidCharacters:forceBaseURL:"
+ "_compatibilityAbsoluteURL"
+ "_encoding"
+ "_fileSystemPath:resolveAgainstBase:"
+ "_fileURLWithPath:isDirectory:relativeToURL:"
+ "_fileURLWithPath:pathStyle:isDirectory:relativeToURL:"
+ "_fragment:"
+ "_host:"
+ "_isDecomposable"
+ "_kCFVolumeObserverDissenterKey"
+ "_lastPathComponent"
+ "_mutableArrayValueForKeyPath:ofObjectAtIndex:"
+ "_mutableOrderedSetValueForKeyPath:ofObjectAtIndex:"
+ "_mutableSetValueForKeyPath:ofObjectAtIndex:"
+ "_netLocation"
+ "_nonLaunchPersonaUID"
+ "_notificationLock"
+ "_notificationToken"
+ "_observesNotification"
+ "_originalString"
+ "_password:"
+ "_query:"
+ "_rangeForComponent:rangeIncludingSeparators:"
+ "_relativePath:"
+ "_requestFromResumeData"
+ "_resourceInfoPtr"
+ "_setValue:forKeyPath:ofObjectAtIndex:"
+ "_user:"
+ "_validateValue:forKeyPath:ofObjectAtIndex:error:"
+ "_valueForKeyPath:ofObjectAtIndex:"
+ "bangla"
+ "cfTrimWS"
+ "checkedProcessCanHaveMultiplePersonas"
+ "com.apple.CFVolumeObserver.%p"
+ "dangi"
+ "forEachPrefsPerformBlock:"
+ "groupConcat:"
+ "groupConcat:separator:"
+ "intents_decodeFromProto"
+ "kDADiskDescriptionVolumeNameKey"
+ "kDADiskDescriptionVolumePathKey"
+ "list"
+ "marathi"
+ "newIndirectTaggedNSStringWithConstantNullTerminatedASCIIBytes_:length_:"
+ "nonLaunchPersonaID"
+ "nonLaunchPersonaPrefs"
+ "odia"
+ "processCanHaveMultiplePersonas"
+ "requestFromResumeData"
+ "setNonLaunchPersonaOverride:"
+ "setSelectorName:"
+ "set_resourceInfoPtr:"
+ "used"
+ "v16@?0@\"_CFXPreferences\"8"
+ "vikram"
- "-[__NSArrayI objectAtIndexedSubscript:]"
- "Attempting to address object pointer with invalid tag"
- "CFPropertyListCreateFromXMLData(): Old-style plist parser: missing semicolon in dictionary on line %d. Parsing will be abandoned. Break on _CFPropertyListMissingSemicolon to debug."
- "CFPropertyListCreateFromXMLData(): Old-style plist parser: missing semicolon or value in dictionary on line %d. Parsing will be abandoned. Break on _CFPropertyListMissingSemicolonOrValue to debug."
- "Expected format '%@' is invalid"
- "^{__CFString=}16@?0^{__CFString=}8"
- "_requestFromResumeData:"
- "{?=\"used\"Q\"list\"[0@]}"

```
