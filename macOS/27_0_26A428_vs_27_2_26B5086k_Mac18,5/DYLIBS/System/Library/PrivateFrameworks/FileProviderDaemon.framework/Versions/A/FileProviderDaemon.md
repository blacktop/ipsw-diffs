## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/Versions/A/FileProviderDaemon`

```diff

-4838.0.125.0.0
-  __TEXT.__text: 0xa86300
-  __TEXT.__objc_methlist: 0x9cdc
-  __TEXT.__const: 0x2e080
-  __TEXT.__cstring: 0x4e545
-  __TEXT.__oslogstring: 0x20ab2
-  __TEXT.__gcc_except_tab: 0xd73c
-  __TEXT.__ustring: 0x171e
-  __TEXT.__dlopen_cstrs: 0xc3
-  __TEXT.__constg_swiftt: 0x1489c
-  __TEXT.__swift5_typeref: 0x14c5e
+4838.40.92.501.1
+  __TEXT.__text: 0xa993f4
+  __TEXT.__objc_methlist: 0x9e04
+  __TEXT.__const: 0x2e280
+  __TEXT.__cstring: 0x50765
+  __TEXT.__oslogstring: 0x21372
+  __TEXT.__gcc_except_tab: 0xd934
+  __TEXT.__ustring: 0x1830
+  __TEXT.__dlopen_cstrs: 0x114
+  __TEXT.__constg_swiftt: 0x14a7c
+  __TEXT.__swift5_typeref: 0x14d8e
   __TEXT.__swift5_builtin: 0x8fc
-  __TEXT.__swift5_reflstr: 0xf9cd
-  __TEXT.__swift5_fieldmd: 0xd198
+  __TEXT.__swift5_reflstr: 0xfb3d
+  __TEXT.__swift5_fieldmd: 0xd26c
   __TEXT.__swift5_mpenum: 0x144
   __TEXT.__swift5_assocty: 0x29c0
-  __TEXT.__swift5_capture: 0x1a830
-  __TEXT.__swift5_proto: 0x1c68
-  __TEXT.__swift5_types: 0xc58
+  __TEXT.__swift5_capture: 0x1aab8
+  __TEXT.__swift5_proto: 0x1c70
+  __TEXT.__swift5_types: 0xc60
   __TEXT.__swift5_types2: 0x8
   __TEXT.__swift_as_entry: 0x1d4
   __TEXT.__swift_as_ret: 0x190
   __TEXT.__swift_as_cont: 0x3d8
   __TEXT.__swift5_protos: 0xbc
-  __TEXT.__unwind_info: 0x1b638
-  __TEXT.__eh_frame: 0x2d848
+  __TEXT.__unwind_info: 0x1b900
+  __TEXT.__eh_frame: 0x2dae0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x998
-  __DATA_CONST.__objc_classlist: 0x5b8
+  __DATA_CONST.__const: 0x9d0
+  __DATA_CONST.__objc_classlist: 0x5d0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6280
+  __DATA_CONST.__objc_selrefs: 0x63f0
   __DATA_CONST.__objc_protorefs: 0x170
-  __DATA_CONST.__objc_superrefs: 0x2a8
+  __DATA_CONST.__objc_superrefs: 0x2b8
   __DATA_CONST.__objc_arraydata: 0x158
-  __DATA_CONST.__got: 0x19c8
-  __AUTH_CONST.__const: 0x4fb00
-  __AUTH_CONST.__cfstring: 0x7660
-  __AUTH_CONST.__objc_const: 0x28230
+  __DATA_CONST.__got: 0x1a28
+  __AUTH_CONST.__const: 0x503e8
+  __AUTH_CONST.__cfstring: 0x7a20
+  __AUTH_CONST.__objc_const: 0x286c8
   __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH_CONST.__objc_intobj: 0x150
+  __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x30a8
-  __AUTH.__objc_data: 0x1c30
-  __AUTH.__data: 0x2688
-  __DATA.__objc_ivar: 0xbb0
-  __DATA.__data: 0x7f90
-  __DATA.__common: 0x20b
-  __DATA_DIRTY.__objc_data: 0x3530
-  __DATA_DIRTY.__data: 0x10fe0
+  __AUTH_CONST.__auth_got: 0x30a0
+  __AUTH.__objc_data: 0x1d20
+  __AUTH.__data: 0x2698
+  __DATA.__objc_ivar: 0xbe4
+  __DATA.__data: 0x8110
+  __DATA.__common: 0x21b
+  __DATA_DIRTY.__objc_data: 0x3578
+  __DATA_DIRTY.__data: 0x11010
   __DATA_DIRTY.__bss: 0xfea0
   __DATA_DIRTY.__common: 0x938
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /System/Library/Frameworks/QuickLookThumbnailing.framework/Versions/A/QuickLookThumbnailing
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
+  - /System/Library/Frameworks/UserNotifications.framework/Versions/A/UserNotifications
   - /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
   - /System/Library/PrivateFrameworks/ApplePushService.framework/Versions/A/ApplePushService
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/Versions/A/BackgroundSystemTasks

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 31662
-  Symbols:   15771
-  CStrings:  8198
+  Functions: 31875
+  Symbols:   15928
+  CStrings:  8349
 
Symbols:
+ -[FPDClaimKnownFolderOperation postClaimNotification]
+ -[FPDConfigurationStore hardConcurrentBackgroundDownloadLimit]
+ -[FPDConfigurationStore hardConcurrentBackgroundUploadLimit]
+ -[FPDConfigurationStore softConcurrentBackgroundDownloadLimit]
+ -[FPDConfigurationStore softConcurrentBackgroundUploadLimit]
+ -[FPDDomain _makeDonationSearchableIndexWithResolvedName:]
+ -[FPDDomain deleteDonationProgressWithCompletionHandler:]
+ -[FPDDomain donateZeroIndexingProgressWithCompletionHandler:]
+ -[FPDKnownFolderClaimNotification .cxx_destruct]
+ -[FPDKnownFolderClaimNotification generateAndPostNotifications]
+ -[FPDKnownFolderClaimNotification initWithPreviousDomain:newDomain:knownFoldersPhysicalURLs:]
+ -[FPDKnownFolderNotification generateAndPostNotifications]
+ -[FPDKnownFolderNotification postNotificationWithTitle:subtitle:physicalURL:]
+ -[FPDKnownFolderReleaseNotification .cxx_destruct]
+ -[FPDKnownFolderReleaseNotification generateAndPostNotifications]
+ -[FPDKnownFolderReleaseNotification initWithPreviousDomain:knownFoldersPhysicalURLs:]
+ -[FPDProvider _flushDefaultDomainDonationProgress]
+ -[FPDProvider _updateDefaultDomainDonationProgress]
+ -[FPDProviderDescriptor backgroundDownloadPipelineDepth]
+ -[FPDProviderDescriptor backgroundUploadPipelineDepth]
+ -[FPDProviderDescriptor setBackgroundDownloadPipelineDepth:]
+ -[FPDProviderDescriptor setBackgroundUploadPipelineDepth:]
+ -[FPDXPCServicer dumpStaleSpotlightDomainsToDumper:providerFilter:]
+ -[FPFSChangeMonitor subscribeToEventsAtPath:sinceEventID:streamUUID:ignoreOwnEvents:delegate:purpose:]
+ -[FPFSChangeSubscription initWithPath:reader:sinceEventID:streamUUID:ignoreOwnEvents:delegate:purpose:]
+ CoreSpotlightLibrary
+ CoreSpotlightLibraryCore.frameworkLibrary
+ GCC_except_table292
+ GCC_except_table300
+ GCC_except_table309
+ GCC_except_table313
+ GCC_except_table317
+ GCC_except_table319
+ GCC_except_table320
+ GCC_except_table323
+ GCC_except_table338
+ GCC_except_table345
+ GCC_except_table346
+ GCC_except_table347
+ GCC_except_table349
+ GCC_except_table370
+ GCC_except_table396
+ GCC_except_table397
+ GCC_except_table398
+ GCC_except_table427
+ GCC_except_table452
+ GCC_except_table455
+ GCC_except_table459
+ GCC_except_table468
+ GCC_except_table469
+ GCC_except_table470
+ GCC_except_table476
+ GCC_except_table477
+ GCC_except_table478
+ GCC_except_table98
+ KnownFolderTransitionedCenter.center
+ KnownFolderTransitionedCenter.onceToken
+ OBJC_IVAR_$_FPDClaimKnownFolderOperation._previousProviderDomain
+ OBJC_IVAR_$_FPDConfigurationStore._hardConcurrentBackgroundDownloadLimit
+ OBJC_IVAR_$_FPDConfigurationStore._hardConcurrentBackgroundUploadLimit
+ OBJC_IVAR_$_FPDConfigurationStore._softConcurrentBackgroundDownloadLimit
+ OBJC_IVAR_$_FPDConfigurationStore._softConcurrentBackgroundUploadLimit
+ OBJC_IVAR_$_FPDKnownFolderClaimNotification._knownFolderURLs
+ OBJC_IVAR_$_FPDKnownFolderClaimNotification._newDomain
+ OBJC_IVAR_$_FPDKnownFolderClaimNotification._previousDomain
+ OBJC_IVAR_$_FPDKnownFolderReleaseNotification._knownFolderURLs
+ OBJC_IVAR_$_FPDKnownFolderReleaseNotification._previousDomain
+ OBJC_IVAR_$_FPDProvider._desiredDonationState
+ OBJC_IVAR_$_FPDProvider._donationUpdateInFlight
+ OBJC_IVAR_$_FPDProvider._lastDonationState
+ OBJC_IVAR_$_FPDProviderDescriptor._backgroundDownloadPipelineDepth
+ OBJC_IVAR_$_FPDProviderDescriptor._backgroundUploadPipelineDepth
+ _CoreSpotlightLibrary
+ _FPKnownFolderTransitionedCategoryIdentifier
+ _FPKnownFolderTransitionedPreviousPathKey
+ _FPKnownFolderTransitionedShowActionIdentifier
+ _FPSpotlightIndexNamePrefix
+ _OBJC_CLASS_$_CSDonationProgressFailure
+ _OBJC_CLASS_$_CSDonationProgressQueryResult
+ _OBJC_CLASS_$_FPDKnownFolderClaimNotification
+ _OBJC_CLASS_$_FPDKnownFolderNotification
+ _OBJC_CLASS_$_FPDKnownFolderReleaseNotification
+ _OBJC_CLASS_$_UNMutableNotificationContent
+ _OBJC_CLASS_$_UNNotificationAction
+ _OBJC_CLASS_$_UNNotificationCategory
+ _OBJC_CLASS_$_UNNotificationRequest
+ _OBJC_CLASS_$_UNUserNotificationCenter
+ _OBJC_METACLASS_$_FPDKnownFolderClaimNotification
+ _OBJC_METACLASS_$_FPDKnownFolderNotification
+ _OBJC_METACLASS_$_FPDKnownFolderReleaseNotification
+ __57-[FPDDomain deleteDonationProgressWithCompletionHandler:]_block_invoke
+ __61-[FPDDomain donateZeroIndexingProgressWithCompletionHandler:]_block_invoke
+ __67-[FPDXPCServicer dumpStaleSpotlightDomainsToDumper:providerFilter:]_block_invoke
+ __77-[FPDKnownFolderNotification postNotificationWithTitle:subtitle:physicalURL:]_block_invoke
+ __IVARS__TtCO18FileProviderDaemon11Maintenance22BackfillDonationStatus
+ __OBJC_$_INSTANCE_METHODS_FPDKnownFolderClaimNotification
+ __OBJC_$_INSTANCE_METHODS_FPDKnownFolderNotification
+ __OBJC_$_INSTANCE_METHODS_FPDKnownFolderReleaseNotification
+ __OBJC_$_INSTANCE_VARIABLES_FPDKnownFolderClaimNotification
+ __OBJC_$_INSTANCE_VARIABLES_FPDKnownFolderReleaseNotification
+ __OBJC_CLASS_RO_$_FPDKnownFolderClaimNotification
+ __OBJC_CLASS_RO_$_FPDKnownFolderNotification
+ __OBJC_CLASS_RO_$_FPDKnownFolderReleaseNotification
+ __OBJC_METACLASS_RO_$_FPDKnownFolderClaimNotification
+ __OBJC_METACLASS_RO_$_FPDKnownFolderNotification
+ __OBJC_METACLASS_RO_$_FPDKnownFolderReleaseNotification
+ ___50-[FPDProvider _flushDefaultDomainDonationProgress]_block_invoke
+ ___57-[FPDDomain deleteDonationProgressWithCompletionHandler:]_block_invoke
+ ___61-[FPDDomain donateZeroIndexingProgressWithCompletionHandler:]_block_invoke
+ ___67-[FPDXPCServicer dumpStaleSpotlightDomainsToDumper:providerFilter:]_block_invoke
+ ___77-[FPDKnownFolderNotification postNotificationWithTitle:subtitle:physicalURL:]_block_invoke
+ ___79-[FPDClaimKnownFolderOperation attachClaimedKnownFoldersWithCompletionHandler:]_block_invoke_2
+ ___CoreSpotlightLibraryCore_block_invoke
+ ___KnownFolderTransitionedCenter_block_invoke
+ ___block_descriptor_32_e73_q24?0"CSDonationProgressQueryResult"8"CSDonationProgressQueryResult"16l
+ ___block_descriptor_48_e8_32w_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32s40r48r_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0l
+ ___getCSDonationProgressClass_block_invoke
+ ___getCSSearchableIndexClass_block_invoke
+ ___unnamed_115
+ ___unnamed_58
+ __getCSDonationProgressClass_block_invoke
+ __getCSSearchableIndexClass_block_invoke
+ __swift_closure_destructor.1029Tm
+ __swift_closure_destructor.1032Tm
+ __swift_closure_destructor.1235Tm
+ __swift_closure_destructor.142Tm
+ __swift_closure_destructor.1644Tm
+ __swift_closure_destructor.1695Tm
+ __swift_closure_destructor.1698Tm
+ __swift_closure_destructor.1724Tm
+ __swift_closure_destructor.173Tm
+ __swift_closure_destructor.1747Tm
+ __swift_closure_destructor.1754Tm
+ __swift_closure_destructor.176Tm
+ __swift_closure_destructor.1770Tm
+ __swift_closure_destructor.1785Tm
+ __swift_closure_destructor.1884Tm
+ __swift_closure_destructor.190Tm
+ __swift_closure_destructor.1912Tm
+ __swift_closure_destructor.1952Tm
+ __swift_closure_destructor.202Tm
+ __swift_closure_destructor.2071Tm
+ __swift_closure_destructor.2500Tm
+ __swift_closure_destructor.2808Tm
+ __swift_closure_destructor.2921Tm
+ __swift_closure_destructor.3058Tm
+ __swift_closure_destructor.3065Tm
+ __swift_closure_destructor.3075Tm
+ __swift_closure_destructor.3078Tm
+ __swift_closure_destructor.3152Tm
+ __swift_closure_destructor.3183Tm
+ __swift_closure_destructor.3289Tm
+ __swift_closure_destructor.3427Tm
+ __swift_closure_destructor.3457Tm
+ __swift_closure_destructor.349Tm
+ __swift_closure_destructor.3533Tm
+ __swift_closure_destructor.3543Tm
+ __swift_closure_destructor.3546Tm
+ __swift_closure_destructor.3549Tm
+ __swift_closure_destructor.3625Tm
+ __swift_closure_destructor.3631Tm
+ __swift_closure_destructor.3640Tm
+ __swift_closure_destructor.366Tm
+ __swift_closure_destructor.4126Tm
+ __swift_closure_destructor.4170Tm
+ __swift_closure_destructor.4176Tm
+ __swift_closure_destructor.4270Tm
+ __swift_closure_destructor.4295Tm
+ __swift_closure_destructor.4502Tm
+ __swift_closure_destructor.4505Tm
+ __swift_closure_destructor.4509Tm
+ __swift_closure_destructor.4626Tm
+ __swift_closure_destructor.4652Tm
+ __swift_closure_destructor.4691Tm
+ __swift_closure_destructor.4808Tm
+ __swift_closure_destructor.4814Tm
+ __swift_closure_destructor.49Tm
+ __swift_closure_destructor.518Tm
+ __swift_closure_destructor.5217Tm
+ __swift_closure_destructor.535Tm
+ __swift_closure_destructor.5490Tm
+ __swift_closure_destructor.5522Tm
+ __swift_closure_destructor.5825Tm
+ __swift_closure_destructor.6036Tm
+ __swift_closure_destructor.6326Tm
+ __swift_closure_destructor.6340Tm
+ __swift_closure_destructor.6546Tm
+ __swift_closure_destructor.6553Tm
+ __swift_closure_destructor.6578Tm
+ __swift_closure_destructor.97Tm
+ _associated conformance 18FileProviderDaemon0A4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLVyx_GSHAASQ
+ _audit_stringCoreSpotlight
+ _objc_msgSend$_flushDefaultDomainDonationProgress
+ _objc_msgSend$_makeDonationSearchableIndexWithResolvedName:
+ _objc_msgSend$_updateDefaultDomainDonationProgress
+ _objc_msgSend$actionWithIdentifier:title:options:
+ _objc_msgSend$addNotificationRequest:withCompletionHandler:
+ _objc_msgSend$allKnownItems
+ _objc_msgSend$allKnownItemsIsPartial
+ _objc_msgSend$backgroundDownloadPipelineDepth
+ _objc_msgSend$backgroundUploadPipelineDepth
+ _objc_msgSend$categoryWithIdentifier:actions:intentIdentifiers:options:
+ _objc_msgSend$deleteDonationProgressWithCompletionHandler:
+ _objc_msgSend$donateZeroIndexingProgressWithCompletionHandler:
+ _objc_msgSend$donatedItems
+ _objc_msgSend$donationProgress
+ _objc_msgSend$dumpStaleSpotlightDomainsToDumper:providerFilter:
+ _objc_msgSend$failureReason
+ _objc_msgSend$fetchDonationProgressForBundles:completionHandler:
+ _objc_msgSend$fp_URLWithNoFollow
+ _objc_msgSend$fp_hasNoFollow
+ _objc_msgSend$generateAndPostNotifications
+ _objc_msgSend$hardConcurrentBackgroundDownloadLimit
+ _objc_msgSend$hardConcurrentBackgroundUploadLimit
+ _objc_msgSend$indexName
+ _objc_msgSend$initWithBundleIdentifier:
+ _objc_msgSend$initWithName:bundleIdentifier:
+ _objc_msgSend$initWithPath:reader:sinceEventID:streamUUID:ignoreOwnEvents:delegate:purpose:
+ _objc_msgSend$initWithPreviousDomain:knownFoldersPhysicalURLs:
+ _objc_msgSend$initWithPreviousDomain:newDomain:knownFoldersPhysicalURLs:
+ _objc_msgSend$itemsNeedingDonation
+ _objc_msgSend$itemsNeedingDonationForRedonationRequests
+ _objc_msgSend$notificationCategories
+ _objc_msgSend$partiallyDonatedItems
+ _objc_msgSend$postClaimNotification
+ _objc_msgSend$postNotificationWithTitle:subtitle:physicalURL:
+ _objc_msgSend$requestWithIdentifier:content:trigger:
+ _objc_msgSend$setBackgroundDownloadPipelineDepth:
+ _objc_msgSend$setBackgroundUploadPipelineDepth:
+ _objc_msgSend$setBody:
+ _objc_msgSend$setByAddingObject:
+ _objc_msgSend$setCategoryIdentifier:
+ _objc_msgSend$setNotificationCategories:
+ _objc_msgSend$softConcurrentBackgroundDownloadLimit
+ _objc_msgSend$softConcurrentBackgroundUploadLimit
+ _objc_msgSend$spotlightIndexName
+ _objc_msgSend$startStringForFgColor:bgColor:attr:
+ _objc_msgSend$status
+ _objc_msgSend$stringForReset
+ _objc_msgSend$subscribeToEventsAtPath:sinceEventID:streamUUID:ignoreOwnEvents:delegate:purpose:
+ _objc_msgSend$underlyingError
+ _symbolic SDy_____ySo6FPItemC_GACG 18FileProviderDaemon0A4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLV
+ _symbolic SDy_____y______GABG 18FileProviderDaemon0A4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLV AA7VFSItemV
+ _symbolic SDy_____yx_GxG 18FileProviderDaemon0A4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLV
+ _symbolic SDy_____yx_GxGz_x______RzlXX 18FileProviderDaemon0A4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLV AA0A4ItemP
+ _symbolic SaySo29CSDonationProgressQueryResultCGSg
+ _symbolic SaySo29CSDonationProgressQueryResultCGSgz_Xx
+ _symbolic _____ 18FileProviderDaemon0A4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLV
+ _symbolic _____ 18FileProviderDaemon11MaintenanceO22BackfillDonationStatusC
+ _symbolic _____Sg2at_t 18FileProviderDaemon8FilenameV
+ _symbolic _____XjSgSb______pSgIegnyg_ 18FileProviderDaemon26_DatabaseReadWriteAccessor_pRi0_s_XPXg s5ErrorP
+ _symbolic _____ySo6FPItemC_G 18FileProviderDaemon0A4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLV
+ _symbolic _____ySo6FPItemC______G 18FileProviderDaemon11MaintenanceO22BackfillDonationStatusC AA7VFSItemV
+ _symbolic _____y_____AB_G 18FileProviderDaemon11MaintenanceO22BackfillDonationStatusC AA7VFSItemV
+ _symbolic _____y_____So6FPItemC_G 18FileProviderDaemon11MaintenanceO22BackfillDonationStatusC AA7VFSItemV
+ _symbolic _____y______G 18FileProviderDaemon0A4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLV AA7VFSItemV
+ _symbolic _____y______pSgG 18FileProviderDaemon6LockedC s5ErrorP
+ _symbolic _____y_____ySo6FPItemC_GADG s18_DictionaryStorageC 18FileProviderDaemon0C4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLV
+ _symbolic _____y_____y______GACG s18_DictionaryStorageC 18FileProviderDaemon0C4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLV AC7VFSItemV
+ _symbolic yyyccSg
+ getCSDonationProgressClass.softClass
+ getCSSearchableIndexClass.softClass
- -[FPFSChangeMonitor subscribeToEventsAtPath:fd:sinceEventID:streamUUID:ignoreOwnEvents:delegate:purpose:]
- -[FPFSChangeSubscription initWithPath:fd:reader:sinceEventID:streamUUID:ignoreOwnEvents:delegate:purpose:]
- -[FPFSChangeSubscription rootfd]
- GCC_except_table288
- GCC_except_table289
- GCC_except_table295
- GCC_except_table297
- GCC_except_table310
- GCC_except_table311
- GCC_except_table314
- GCC_except_table318
- GCC_except_table324
- GCC_except_table325
- GCC_except_table327
- GCC_except_table333
- GCC_except_table343
- GCC_except_table355
- GCC_except_table357
- GCC_except_table359
- GCC_except_table361
- GCC_except_table375
- GCC_except_table401
- GCC_except_table402
- GCC_except_table403
- GCC_except_table432
- GCC_except_table457
- GCC_except_table460
- GCC_except_table464
- GCC_except_table473
- OBJC_IVAR_$_FPFSChangeSubscription._ownRootFD
- OBJC_IVAR_$_FPFSChangeSubscription._rootfd
- ___64-[FPDClaimKnownFolderOperation resolveKnownFolderURLsWithError:]_block_invoke
- ___unnamed_117
- __swift_closure_destructor.1017Tm
- __swift_closure_destructor.1020Tm
- __swift_closure_destructor.1229Tm
- __swift_closure_destructor.124Tm
- __swift_closure_destructor.126Tm
- __swift_closure_destructor.1632Tm
- __swift_closure_destructor.1680Tm
- __swift_closure_destructor.1683Tm
- __swift_closure_destructor.1723Tm
- __swift_closure_destructor.1746Tm
- __swift_closure_destructor.1753Tm
- __swift_closure_destructor.1768Tm
- __swift_closure_destructor.1769Tm
- __swift_closure_destructor.1852Tm
- __swift_closure_destructor.1880Tm
- __swift_closure_destructor.1951Tm
- __swift_closure_destructor.200Tm
- __swift_closure_destructor.2070Tm
- __swift_closure_destructor.2499Tm
- __swift_closure_destructor.2807Tm
- __swift_closure_destructor.2920Tm
- __swift_closure_destructor.3057Tm
- __swift_closure_destructor.3064Tm
- __swift_closure_destructor.3074Tm
- __swift_closure_destructor.3077Tm
- __swift_closure_destructor.3151Tm
- __swift_closure_destructor.3182Tm
- __swift_closure_destructor.3288Tm
- __swift_closure_destructor.3426Tm
- __swift_closure_destructor.3456Tm
- __swift_closure_destructor.34Tm
- __swift_closure_destructor.3532Tm
- __swift_closure_destructor.3542Tm
- __swift_closure_destructor.3545Tm
- __swift_closure_destructor.3548Tm
- __swift_closure_destructor.360Tm
- __swift_closure_destructor.3624Tm
- __swift_closure_destructor.3630Tm
- __swift_closure_destructor.3639Tm
- __swift_closure_destructor.4125Tm
- __swift_closure_destructor.4169Tm
- __swift_closure_destructor.4175Tm
- __swift_closure_destructor.4305Tm
- __swift_closure_destructor.4515Tm
- __swift_closure_destructor.4519Tm
- __swift_closure_destructor.4522Tm
- __swift_closure_destructor.4636Tm
- __swift_closure_destructor.4662Tm
- __swift_closure_destructor.46Tm
- __swift_closure_destructor.4701Tm
- __swift_closure_destructor.4818Tm
- __swift_closure_destructor.4824Tm
- __swift_closure_destructor.5039Tm
- __swift_closure_destructor.512Tm
- __swift_closure_destructor.5227Tm
- __swift_closure_destructor.529Tm
- __swift_closure_destructor.5500Tm
- __swift_closure_destructor.5532Tm
- __swift_closure_destructor.5835Tm
- __swift_closure_destructor.6046Tm
- __swift_closure_destructor.6336Tm
- __swift_closure_destructor.6350Tm
- __swift_closure_destructor.6556Tm
- __swift_closure_destructor.6563Tm
- __swift_closure_destructor.6588Tm
- __swift_closure_destructor.68Tm
- __swift_closure_destructor.81Tm
- _objc_msgSend$initWithPath:fd:reader:sinceEventID:streamUUID:ignoreOwnEvents:delegate:purpose:
- _objc_msgSend$subscribeToEventsAtPath:fd:sinceEventID:streamUUID:ignoreOwnEvents:delegate:purpose:
- _symbolic SDy2ID_____QzxG 18FileProviderDaemon0A4ItemP
- _symbolic SDy2ID_____QzxGz_x______RzlXX 18FileProviderDaemon0A4ItemP AC
- _symbolic SDy__________G 18FileProviderDaemon9VFSItemIDO AA0D0V
- _symbolic _____y__________G s18_DictionaryStorageC 18FileProviderDaemon9VFSItemIDO AC0F0V
- _symbolic _____y___________8genCounttSg______pGIegn_ s6ResultOsRi_zRi0_zrlE 10Foundation3URLV s6UInt32V s5ErrorP
CStrings:
+ "\n        END\n   WHERE rowID = NEW.rowID;\nEND"
+ "\n      AND parent_container.decoration_is_container = 1\n      AND parent_container.decoration_app_container_bundle_identifier IS NOT NULL\n      AND length(parent_container.decoration_app_container_bundle_identifier) > 0),\n  "
+ "\n   AND fp_id IS NOT NULL\n   AND (fs_deletion_status & "
+ "\n   AND fp_id IS NULL AND fs_id IS NOT NULL\n   AND (fs_deletion_status & "
+ "\n   WHERE fp_id = NEW.id;\nEND"
+ "\n   WHERE fp_id IN (SELECT documents_child.id\n                     FROM fp_snapshot AS documents_child\n                    WHERE documents_child.parent_id = NEW.id\n                      AND documents_child.filename = 'Documents' "
+ "\n   WHERE rowID = NEW.rowID;\nEND"
+ "\n  FROM fp_snapshot AS s WHERE s.id = "
+ "\n ORDER BY rowid\n LIMIT "
+ "\n WHERE rowid > "
+ "         allKnownItems: spotlight:"
+ "         allKnownItemsIsPartial: "
+ "         donatedItems: "
+ "         failure reason: "
+ "         indexedItems: <error: "
+ "         indexedItems: <timed out after 1s>\n"
+ "         indexedItems: spotlight-index:"
+ "         itemsNeedingDonation: spotlight:"
+ "         partiallyDonatedItems: "
+ "         progress type: "
+ "         redonationRequests: "
+ "         status: "
+ "         underlying error: "
+ "      + spotlight donation progress:\n"
+ "      + spotlight donation progress: <error: "
+ "      + spotlight donation progress: <none reported>\n"
+ "      + spotlight donation progress: <provider domain unavailable>\n"
+ "      + spotlight donation progress: <timed out after 1s>\n"
+ "      donation-status-backfill-in-progress: "
+ "     %@  bundle:%@"
+ "  allKnownItems:%lu"
+ "  allKnownItems:<failure reason:%lu>"
+ "  allKnownItems:<no progress reported, status:%lu>"
+ " (no progress stored)"
+ "%@⚠️  Found %lu stale spotlight domains (Spotlight tracks, FP has no live domain):%@\n"
+ "(nil)"
+ ")\n    OR OLD.parent_id != NEW.parent_id\nBEGIN\n  UPDATE reconciliation_table\n    SET donation_status = "
+ ")\nBEGIN\n  UPDATE reconciliation_table\n    SET donation_status = CASE\n          WHEN (NEW.fs_deletion_status & "
+ ") != 0 THEN 0\n          WHEN NEW.fp_id IS NULL AND NEW.fs_id IS NOT NULL THEN 1\n          ELSE "
+ ") != 0 THEN 0 ELSE "
+ ") IS NOT (NEW.decoration_capabilities & "
+ ") IS NOT (NEW.fs_deletion_status & "
+ "+ stale spotlight domains: <error: %@>\n"
+ "+ stale spotlight domains: <none>\n"
+ "+ stale spotlight domains: <timed out after 2s>\n"
+ "-[FPDKnownFolderNotification generateAndPostNotifications]"
+ ".decoration_capabilities, "
+ ".decoration_is_container, "
+ ".filename = 'Documents' "
+ ".metadata_is_hidden)"
+ ".parent_id\n      AND "
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/FileProvider_executables/fileproviderd/FPDKnownFolderNotification.m"
+ "/System/Library/Frameworks/CoreSpotlight.framework/Contents/MacOS/CoreSpotlight"
+ "<"
+ "ALTER TABLE reconciliation_table ADD COLUMN donation_status TINYINT NOT NULL DEFAULT 0"
+ "COALESCE(\n  (SELECT "
+ "COALESCE(\n  (SELECT parent_container.metadata_is_hidden\n     FROM fp_snapshot AS parent_container\n    WHERE parent_container.id = "
+ "CREATE INDEX reconciliation_donation_status ON reconciliation_table(donation_status) WHERE donation_status = 1"
+ "CREATE TRIGGER \"donation_status/fp_snapshot/app_container_insertion\"\n  AFTER INSERT ON fp_snapshot\n  WHEN NEW.decoration_is_container = 1\n    AND NEW.decoration_app_container_bundle_identifier IS NOT NULL\n    AND length(NEW.decoration_app_container_bundle_identifier) > 0\nBEGIN\n  UPDATE reconciliation_table\n    SET donation_status = "
+ "CREATE TRIGGER \"donation_status/fp_snapshot/app_container_visibility_change\"\n  AFTER UPDATE OF metadata_is_hidden ON fp_snapshot\n  WHEN OLD.metadata_is_hidden != NEW.metadata_is_hidden\n    AND NEW.decoration_is_container = 1\n    AND NEW.decoration_app_container_bundle_identifier IS NOT NULL\n    AND length(NEW.decoration_app_container_bundle_identifier) > 0\nBEGIN\n  UPDATE reconciliation_table\n    SET donation_status = "
+ "CREATE TRIGGER \"donation_status/fp_snapshot/eligibility_change\"\n  AFTER UPDATE OF decoration_is_container, metadata_is_hidden, decoration_capabilities, parent_id ON fp_snapshot\n  WHEN OLD.decoration_is_container != NEW.decoration_is_container\n    OR OLD.metadata_is_hidden != NEW.metadata_is_hidden\n    OR (OLD.decoration_capabilities & "
+ "CREATE TRIGGER \"donation_status/reconciliation_table/creation_with_binding\"\n  AFTER INSERT ON reconciliation_table\n  WHEN NEW.fp_id IS NOT NULL\nBEGIN\n  UPDATE reconciliation_table\n    SET donation_status = "
+ "CREATE TRIGGER \"donation_status/reconciliation_table/creation_without_binding\"\n  AFTER INSERT ON reconciliation_table\n  WHEN NEW.fs_id IS NOT NULL AND NEW.fp_id IS NULL\nBEGIN\n  UPDATE reconciliation_table\n    SET donation_status = "
+ "CREATE TRIGGER \"donation_status/reconciliation_table/deletion_change\"\n  AFTER UPDATE OF fs_deletion_status ON reconciliation_table\n  WHEN (OLD.fs_deletion_status & "
+ "CREATE TRIGGER \"donation_status/reconciliation_table/fp_id_binding\"\n  AFTER UPDATE OF fp_id ON reconciliation_table\n  WHEN NEW.fp_id IS NOT NULL AND (OLD.fp_id IS NULL OR OLD.fp_id != NEW.fp_id)\nBEGIN\n  UPDATE reconciliation_table\n    SET donation_status = "
+ "CREATE TRIGGER \"donation_status/reconciliation_table/fp_id_unbinding\"\n  AFTER UPDATE OF fp_id ON reconciliation_table\n  WHEN OLD.fp_id IS NOT NULL AND NEW.fp_id IS NULL\nBEGIN\n  UPDATE reconciliation_table\n    SET donation_status = "
+ "CSDonationProgress"
+ "CSSearchableIndex"
+ "Class getCSDonationProgressClass(void)_block_invoke"
+ "Class getCSSearchableIndexClass(void)_block_invoke"
+ "FPCK: parent lookup failed for %s: %@"
+ "FPDDomain.m"
+ "FPFSDownloader: there was an issue scanning the db: %{public}@"
+ "IS_DONATABLE: failed to decode item ID from sqlite value"
+ "KNOWNFOLDER_RELEASE_NOTIFICATION_ACTION_SHOW"
+ "KNOWNFOLDER_RELEASE_NOTIFICATION_SUBTITLE_DESKTOP_%@"
+ "KNOWNFOLDER_RELEASE_NOTIFICATION_SUBTITLE_DESKTOP_ICLOUDDRIVE"
+ "KNOWNFOLDER_RELEASE_NOTIFICATION_SUBTITLE_DOCUMENTS_%@"
+ "KNOWNFOLDER_RELEASE_NOTIFICATION_SUBTITLE_DOCUMENTS_ICLOUDDRIVE"
+ "KNOWNFOLDER_RELEASE_NOTIFICATION_TITLE_DESKTOP_%@"
+ "KNOWNFOLDER_RELEASE_NOTIFICATION_TITLE_DESKTOP_ICLOUDDRIVE"
+ "KNOWNFOLDER_RELEASE_NOTIFICATION_TITLE_DESKTOP_LOCAL"
+ "KNOWNFOLDER_RELEASE_NOTIFICATION_TITLE_DOCUMENTS_%@"
+ "KNOWNFOLDER_RELEASE_NOTIFICATION_TITLE_DOCUMENTS_ICLOUDDRIVE"
+ "KNOWNFOLDER_RELEASE_NOTIFICATION_TITLE_DOCUMENTS_LOCAL"
+ "NEW.fs_deletion_status"
+ "NSExtensionFileProviderBackgroundDownloadPipelineDepth"
+ "NSExtensionFileProviderBackgroundUploadPipelineDepth"
+ "PRAGMA table_info(reconciliation_table)"
+ "SEARCH reconciliation_table USING COVERING INDEX reconciliation_donation_status (donation_status=?)"
+ "SEARCH reconciliation_table USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=? AND rowid>? AND rowid<?)"
+ "SEARCH reconciliation_table USING INTEGER PRIMARY KEY (rowid>? AND rowid<?)\nCORRELATED SCALAR SUBQUERY 1\nSEARCH s USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nCORRELATED SCALAR SUBQUERY 2\nSEARCH parent_container USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)"
+ "SEARCH reconciliation_table USING INTEGER PRIMARY KEY (rowid>? AND rowid<?)\nCORRELATED SCALAR SUBQUERY 2\nSEARCH s USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nCORRELATED SCALAR SUBQUERY 1\nSEARCH parent_container USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)"
+ "SELECT COUNT(*) FROM reconciliation_table\nINDEXED BY reconciliation_donation_status\nWHERE donation_status = 1"
+ "SELECT rowid FROM reconciliation_table\n WHERE rowid > "
+ "SQLDB: Fetch donation counts"
+ "UPDATE reconciliation_table\n   SET donation_status = "
+ "UPDATE reconciliation_table\n   SET donation_status = 1\n WHERE rowid > "
+ "[DEBUG] 🔢 deleted donation progress for index %@"
+ "[DEBUG] 🔢 donation reconcile for %{public}@: desired=%{public}s lastDonated=%{public}s domains=%lu"
+ "[DEBUG] 🔢 donation reconcile skipped for %{public}@: no default domain in domainsByID (domains=%lu)"
+ "[DEBUG] 🔢 donation reconcile skipped for %{public}@: state unchanged (%{public}s)"
+ "[DEBUG] 🔢 recreate-default-domain for %{public}@: hasExistingDefault=%{bool}d domains=%lu volume=%@"
+ "[DEBUG] 🔢 reported 0/0 donation progress for index %@"
+ "[ERROR] 🔢 donation reconcile failed for %{public}@ (desired=%{public}s): %@"
+ "[ERROR] 🔢 failed to delete donation progress for index %@: %@"
+ "[ERROR] 🔢 failed to report 0/0 donation progress for index %@: %@"
+ "[ERROR] 🖥️ dropping known folder transitioned notification — nil argument: title=%{private}@, subtitle=%{private}@, physicalURL=%{private}@"
+ "[ERROR] 🖥️ failed to post known folder transitioned notification: %@"
+ "[INFO] 🔢 deleting donation progress for index %@ (provider=%{public}@)"
+ "[INFO] 🔢 donating empty (0/0) indexing progress for index %@ (provider=%{public}@)"
+ "[NOTICE] 🖥️ posting known folder transitioned notification"
+ "[WARNING] 🔢 can't resolve donation index (provider=%{public}@): no provider domain"
+ "_backgroundDownloadPipelineDepth"
+ "_backgroundUploadPipelineDepth"
+ "_vfs_fileid_idx (vfs_fileid=?)"
+ "applyDonationStatusBackfill(from:through:with:)"
+ "backfill-donation-status"
+ "backfillDonationStatusRange(from:limit:with:)"
+ "backgroundDownload"
+ "backgroundUpload"
+ "bootstrapDonationStatusTriggers(with:)"
+ "donatableItemCount(with:)"
+ "donation_status_mismatch"
+ "fpfs-allow-donation-container-exclusion."
+ "fpfs_fetch_url_for_ino: unexpected nil buffer"
+ "hardConcurrentBackgroundDownloadLimit"
+ "hardConcurrentBackgroundUploadLimit"
+ "has-real-domain"
+ "kMDItemFileProviderID == \""
+ "no-real-domain"
+ "onDonationBackfillComplete: indexer unavailable"
+ "q24@?0@\"CSDonationProgressQueryResult\"8@\"CSDonationProgressQueryResult\"16"
+ "reconciliation_table.fp_id"
+ "reconciliation_table.fs_deletion_status"
+ "reportDonationProgress(withAnchor:completionHandler:)"
+ "reportDonationProgress: spotlightIndexer unavailable"
+ "requestDonationProgressReport(completion:)"
+ "softConcurrentBackgroundDownloadLimit"
+ "softConcurrentBackgroundUploadLimit"
+ "softlink:r:path:/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight"
+ "unimplemented - value "
+ "update_v13_5_donationStatus(with:)"
+ "void *CoreSpotlightLibrary(void)"
+ "🔗 x-validation: %llu already tracked link at %{public}s/%{public}s has a different fileID %llu"
+ "🔗 x-validation: %llu already tracked link at %{public}s/%{public}s is not in the domain anymore"
+ "🔗 x-validation: %llu favorize link %llu/%{public}s over cached but hidden one %{public}s/%{public}s"
+ "🔗 x-validation: %llu hardlink no lookupCache available"
+ "🔗 x-validation: %llu hardlink resolution failed: %@"
+ "🔗 x-validation: %llu has multiple %u links and wasn't found in cache"
+ "🔗 x-validation: %llu resolved location is already the tracked link at %{public}s/%{public}s"
+ "🔗 x-validation: %llu rewriting from %llu/%{public}s to already tracked link at %{public}s/%{public}s"
+ "🔢 Pending indexing count: %ld, All known (donatable) count: %ld"
+ "🖥️ Notification should be implemented by subclass"
- "couldn't access hardlink for item %{public}s"
- "fpfs_fetch_url_for_handle: unexpected nil buffer"
- "🔢 Pending indexing count: %ld, Total indexing count: %ld"
```
