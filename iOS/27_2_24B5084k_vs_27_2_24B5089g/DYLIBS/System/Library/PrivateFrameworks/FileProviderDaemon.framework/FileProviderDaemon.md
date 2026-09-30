## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-4838.40.53.502.1
-  __TEXT.__text: 0xa45214
-  __TEXT.__objc_methlist: 0x9914
-  __TEXT.__const: 0x2e480
-  __TEXT.__cstring: 0x4dd45
-  __TEXT.__oslogstring: 0x207f2
-  __TEXT.__gcc_except_tab: 0xd70c
-  __TEXT.__ustring: 0x181a
-  __TEXT.__dlopen_cstrs: 0xc3
-  __TEXT.__constg_swiftt: 0x14710
-  __TEXT.__swift5_typeref: 0x14c6e
+4838.40.92.502.1
+  __TEXT.__text: 0xa545e0
+  __TEXT.__objc_methlist: 0x99c4
+  __TEXT.__const: 0x2e570
+  __TEXT.__cstring: 0x4f8b5
+  __TEXT.__oslogstring: 0x210c2
+  __TEXT.__gcc_except_tab: 0xd80c
+  __TEXT.__ustring: 0x1880
+  __TEXT.__dlopen_cstrs: 0x114
+  __TEXT.__constg_swiftt: 0x14900
+  __TEXT.__swift5_typeref: 0x14d0e
   __TEXT.__swift5_builtin: 0x8e8
-  __TEXT.__swift5_reflstr: 0xf8fd
-  __TEXT.__swift5_fieldmd: 0xd1bc
+  __TEXT.__swift5_reflstr: 0xfa2d
+  __TEXT.__swift5_fieldmd: 0xd278
   __TEXT.__swift5_mpenum: 0x144
   __TEXT.__swift5_assocty: 0x29f0
-  __TEXT.__swift5_capture: 0x1a918
-  __TEXT.__swift5_proto: 0x1cbc
-  __TEXT.__swift5_types: 0xc54
+  __TEXT.__swift5_capture: 0x1aaa8
+  __TEXT.__swift5_proto: 0x1cc4
+  __TEXT.__swift5_types: 0xc5c
   __TEXT.__swift5_types2: 0x8
   __TEXT.__swift_as_entry: 0x1b4
   __TEXT.__swift_as_ret: 0x188
   __TEXT.__swift_as_cont: 0x36c
   __TEXT.__swift5_protos: 0xbc
-  __TEXT.__unwind_info: 0x1b810
-  __TEXT.__eh_frame: 0x2d2c8
+  __TEXT.__unwind_info: 0x1b7b8
+  __TEXT.__eh_frame: 0x2dab0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4740
-  __DATA_CONST.__objc_classlist: 0x5a0
+  __DATA_CONST.__const: 0x47a8
+  __DATA_CONST.__objc_classlist: 0x5b8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x2e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x62c0
+  __DATA_CONST.__objc_selrefs: 0x6368
   __DATA_CONST.__objc_protorefs: 0x150
-  __DATA_CONST.__objc_superrefs: 0x298
+  __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x118
-  __DATA_CONST.__got: 0x1940
-  __AUTH_CONST.__const: 0x4c3f8
-  __AUTH_CONST.__cfstring: 0x7540
-  __AUTH_CONST.__objc_const: 0x27dd8
+  __DATA_CONST.__got: 0x1980
+  __AUTH_CONST.__const: 0x4c998
+  __AUTH_CONST.__cfstring: 0x7720
+  __AUTH_CONST.__objc_const: 0x28150
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__objc_intobj: 0x138
+  __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x3158
-  __AUTH.__objc_data: 0x1b58
-  __AUTH.__data: 0x28a8
-  __DATA.__objc_ivar: 0xbcc
-  __DATA.__data: 0x80a0
+  __AUTH_CONST.__auth_got: 0x3150
+  __AUTH.__objc_data: 0x1b90
+  __AUTH.__data: 0x2878
+  __DATA.__objc_ivar: 0xbe8
+  __DATA.__data: 0x81f0
   __DATA.__common: 0x21b
-  __DATA_DIRTY.__objc_data: 0x33c0
-  __DATA_DIRTY.__data: 0x10e30
-  __DATA_DIRTY.__bss: 0xfe98
-  __DATA_DIRTY.__common: 0x8f0
+  __DATA_DIRTY.__objc_data: 0x34b0
+  __DATA_DIRTY.__data: 0x10e80
+  __DATA_DIRTY.__bss: 0x10198
+  __DATA_DIRTY.__common: 0x900
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/Frameworks/QuickLookThumbnailing.framework/QuickLookThumbnailing
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 31574
-  Symbols:   15345
-  CStrings:  8181
+  Functions: 31773
+  Symbols:   15445
+  CStrings:  8293
 
Symbols:
+ -[FPDClaimKnownFolderOperation postClaimNotification]
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
+ -[FPFSChangeMonitor subscribeToEventsAtPath:sinceEventID:streamUUID:ignoreOwnEvents:delegate:purpose:]
+ -[FPFSChangeSubscription initWithPath:reader:sinceEventID:streamUUID:ignoreOwnEvents:delegate:purpose:]
+ GCC_except_table97
+ _CoreSpotlightLibrary
+ _CoreSpotlightLibraryCore.frameworkLibrary
+ _FPKnownFolderTransitionedCategoryIdentifier
+ _FPKnownFolderTransitionedPreviousPathKey
+ _FPKnownFolderTransitionedShowActionIdentifier
+ _KnownFolderTransitionedCenter.center
+ _KnownFolderTransitionedCenter.onceToken
+ _OBJC_CLASS_$_FPDKnownFolderClaimNotification
+ _OBJC_CLASS_$_FPDKnownFolderNotification
+ _OBJC_CLASS_$_FPDKnownFolderReleaseNotification
+ _OBJC_CLASS_$_UNMutableNotificationContent
+ _OBJC_CLASS_$_UNNotificationAction
+ _OBJC_CLASS_$_UNNotificationCategory
+ _OBJC_CLASS_$_UNNotificationRequest
+ _OBJC_CLASS_$_UNUserNotificationCenter
+ _OBJC_IVAR_$_FPDClaimKnownFolderOperation._previousProviderDomain
+ _OBJC_IVAR_$_FPDKnownFolderClaimNotification._knownFolderURLs
+ _OBJC_IVAR_$_FPDKnownFolderClaimNotification._newDomain
+ _OBJC_IVAR_$_FPDKnownFolderClaimNotification._previousDomain
+ _OBJC_IVAR_$_FPDKnownFolderReleaseNotification._knownFolderURLs
+ _OBJC_IVAR_$_FPDKnownFolderReleaseNotification._previousDomain
+ _OBJC_IVAR_$_FPDProvider._desiredDonationState
+ _OBJC_IVAR_$_FPDProvider._donationUpdateInFlight
+ _OBJC_IVAR_$_FPDProvider._lastDonationState
+ _OBJC_METACLASS_$_FPDKnownFolderClaimNotification
+ _OBJC_METACLASS_$_FPDKnownFolderNotification
+ _OBJC_METACLASS_$_FPDKnownFolderReleaseNotification
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
+ ___77-[FPDKnownFolderNotification postNotificationWithTitle:subtitle:physicalURL:]_block_invoke
+ ___79-[FPDClaimKnownFolderOperation attachClaimedKnownFoldersWithCompletionHandler:]_block_invoke_2
+ ___CoreSpotlightLibraryCore_block_invoke
+ ___KnownFolderTransitionedCenter_block_invoke
+ ___block_descriptor_48_e8_32w_e17_v16?0"NSError"8lw32l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___getCSDonationProgressClass_block_invoke
+ ___getCSSearchableIndexClass_block_invoke
+ ___swift_closure_destructor.1029Tm
+ ___swift_closure_destructor.1032Tm
+ ___swift_closure_destructor.1235Tm
+ ___swift_closure_destructor.154Tm
+ ___swift_closure_destructor.1641Tm
+ ___swift_closure_destructor.1692Tm
+ ___swift_closure_destructor.1695Tm
+ ___swift_closure_destructor.1710Tm
+ ___swift_closure_destructor.171Tm
+ ___swift_closure_destructor.1730Tm
+ ___swift_closure_destructor.1737Tm
+ ___swift_closure_destructor.174Tm
+ ___swift_closure_destructor.1753Tm
+ ___swift_closure_destructor.1782Tm
+ ___swift_closure_destructor.1881Tm
+ ___swift_closure_destructor.188Tm
+ ___swift_closure_destructor.1909Tm
+ ___swift_closure_destructor.1935Tm
+ ___swift_closure_destructor.202Tm
+ ___swift_closure_destructor.206Tm
+ ___swift_closure_destructor.2457Tm
+ ___swift_closure_destructor.2764Tm
+ ___swift_closure_destructor.2877Tm
+ ___swift_closure_destructor.3014Tm
+ ___swift_closure_destructor.3021Tm
+ ___swift_closure_destructor.3031Tm
+ ___swift_closure_destructor.3034Tm
+ ___swift_closure_destructor.3108Tm
+ ___swift_closure_destructor.3139Tm
+ ___swift_closure_destructor.3245Tm
+ ___swift_closure_destructor.3383Tm
+ ___swift_closure_destructor.3413Tm
+ ___swift_closure_destructor.3489Tm
+ ___swift_closure_destructor.3499Tm
+ ___swift_closure_destructor.349Tm
+ ___swift_closure_destructor.3502Tm
+ ___swift_closure_destructor.3505Tm
+ ___swift_closure_destructor.3581Tm
+ ___swift_closure_destructor.3587Tm
+ ___swift_closure_destructor.3596Tm
+ ___swift_closure_destructor.366Tm
+ ___swift_closure_destructor.4082Tm
+ ___swift_closure_destructor.4126Tm
+ ___swift_closure_destructor.4132Tm
+ ___swift_closure_destructor.4244Tm
+ ___swift_closure_destructor.4451Tm
+ ___swift_closure_destructor.4454Tm
+ ___swift_closure_destructor.4458Tm
+ ___swift_closure_destructor.4461Tm
+ ___swift_closure_destructor.4541Tm
+ ___swift_closure_destructor.4567Tm
+ ___swift_closure_destructor.4606Tm
+ ___swift_closure_destructor.4722Tm
+ ___swift_closure_destructor.4728Tm
+ ___swift_closure_destructor.4943Tm
+ ___swift_closure_destructor.5131Tm
+ ___swift_closure_destructor.518Tm
+ ___swift_closure_destructor.535Tm
+ ___swift_closure_destructor.5404Tm
+ ___swift_closure_destructor.5436Tm
+ ___swift_closure_destructor.5739Tm
+ ___swift_closure_destructor.5950Tm
+ ___swift_closure_destructor.6252Tm
+ ___swift_closure_destructor.6266Tm
+ ___swift_closure_destructor.6472Tm
+ ___swift_closure_destructor.6479Tm
+ ___swift_closure_destructor.6504Tm
+ ___swift_closure_destructor.65Tm
+ ___swift_closure_destructor.6630Tm
+ ___unnamed_116
+ ___unnamed_58
+ ___unnamed_60
+ _associated conformance 18FileProviderDaemon0A4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLVyx_GSHAASQ
+ _audit_stringCoreSpotlight
+ _getCSDonationProgressClass.softClass
+ _getCSSearchableIndexClass.softClass
+ _objc_msgSend$_flushDefaultDomainDonationProgress
+ _objc_msgSend$_makeDonationSearchableIndexWithResolvedName:
+ _objc_msgSend$_updateDefaultDomainDonationProgress
+ _objc_msgSend$actionWithIdentifier:title:options:
+ _objc_msgSend$addNotificationRequest:withCompletionHandler:
+ _objc_msgSend$categoryWithIdentifier:actions:intentIdentifiers:options:
+ _objc_msgSend$deleteDonationProgressWithCompletionHandler:
+ _objc_msgSend$donateZeroIndexingProgressWithCompletionHandler:
+ _objc_msgSend$fp_hasNoFollow
+ _objc_msgSend$generateAndPostNotifications
+ _objc_msgSend$initWithBundleIdentifier:
+ _objc_msgSend$initWithName:protectionClass:bundleIdentifier:
+ _objc_msgSend$initWithPath:reader:sinceEventID:streamUUID:ignoreOwnEvents:delegate:purpose:
+ _objc_msgSend$initWithPreviousDomain:knownFoldersPhysicalURLs:
+ _objc_msgSend$initWithPreviousDomain:newDomain:knownFoldersPhysicalURLs:
+ _objc_msgSend$notificationCategories
+ _objc_msgSend$postClaimNotification
+ _objc_msgSend$postNotificationWithTitle:subtitle:physicalURL:
+ _objc_msgSend$requestWithIdentifier:content:trigger:
+ _objc_msgSend$setBody:
+ _objc_msgSend$setByAddingObject:
+ _objc_msgSend$setCategoryIdentifier:
+ _objc_msgSend$setNotificationCategories:
+ _objc_msgSend$subscribeToEventsAtPath:sinceEventID:streamUUID:ignoreOwnEvents:delegate:purpose:
+ _objc_retain_x13
+ _symbolic SDy_____ySo6FPItemC_GACG 18FileProviderDaemon0A4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLV
+ _symbolic SDy_____y______GABG 18FileProviderDaemon0A4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLV AA7VFSItemV
+ _symbolic SDy_____yx_GxG 18FileProviderDaemon0A4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLV
+ _symbolic SDy_____yx_GxGz_x______RzlXX 18FileProviderDaemon0A4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLV AA0A4ItemP
+ _symbolic _____ 18FileProviderDaemon0A4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLV
+ _symbolic _____ 18FileProviderDaemon11MaintenanceO22BackfillDonationStatusC
+ _symbolic _____Sg2at_t 18FileProviderDaemon8FilenameV
+ _symbolic _____ySo6FPItemC_G 18FileProviderDaemon0A4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLV
+ _symbolic _____ySo6FPItemC______G 18FileProviderDaemon11MaintenanceO22BackfillDonationStatusC AA7VFSItemV
+ _symbolic _____y_____AB_G 18FileProviderDaemon11MaintenanceO22BackfillDonationStatusC AA7VFSItemV
+ _symbolic _____y_____So6FPItemC_G 18FileProviderDaemon11MaintenanceO22BackfillDonationStatusC AA7VFSItemV
+ _symbolic _____y______G 18FileProviderDaemon0A4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLV AA7VFSItemV
+ _symbolic _____y______pSgG 18FileProviderDaemon6LockedC s5ErrorP
+ _symbolic _____y_____ySo6FPItemC_GADG s18_DictionaryStorageC 18FileProviderDaemon0C4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLV
+ _symbolic _____y_____y______GACG s18_DictionaryStorageC 18FileProviderDaemon0C4TreeC9IDAndName33_E336761B4F808522882A9750FAF16EE1LLV AC7VFSItemV
+ _symbolic yyyccSg
- -[FPFSChangeMonitor subscribeToEventsAtPath:fd:sinceEventID:streamUUID:ignoreOwnEvents:delegate:purpose:]
- -[FPFSChangeSubscription initWithPath:fd:reader:sinceEventID:streamUUID:ignoreOwnEvents:delegate:purpose:]
- -[FPFSChangeSubscription rootfd]
- _OBJC_IVAR_$_FPFSChangeSubscription._ownRootFD
- _OBJC_IVAR_$_FPFSChangeSubscription._rootfd
- ___64-[FPDClaimKnownFolderOperation resolveKnownFolderURLsWithError:]_block_invoke
- ___swift_closure_destructor.1017Tm
- ___swift_closure_destructor.101Tm
- ___swift_closure_destructor.1020Tm
- ___swift_closure_destructor.120Tm
- ___swift_closure_destructor.1229Tm
- ___swift_closure_destructor.124Tm
- ___swift_closure_destructor.137Tm
- ___swift_closure_destructor.1629Tm
- ___swift_closure_destructor.1677Tm
- ___swift_closure_destructor.1680Tm
- ___swift_closure_destructor.1709Tm
- ___swift_closure_destructor.1729Tm
- ___swift_closure_destructor.1736Tm
- ___swift_closure_destructor.1752Tm
- ___swift_closure_destructor.1767Tm
- ___swift_closure_destructor.1865Tm
- ___swift_closure_destructor.1893Tm
- ___swift_closure_destructor.1934Tm
- ___swift_closure_destructor.196Tm
- ___swift_closure_destructor.2456Tm
- ___swift_closure_destructor.2763Tm
- ___swift_closure_destructor.2876Tm
- ___swift_closure_destructor.3013Tm
- ___swift_closure_destructor.3020Tm
- ___swift_closure_destructor.3030Tm
- ___swift_closure_destructor.3033Tm
- ___swift_closure_destructor.3107Tm
- ___swift_closure_destructor.3138Tm
- ___swift_closure_destructor.3244Tm
- ___swift_closure_destructor.3382Tm
- ___swift_closure_destructor.3412Tm
- ___swift_closure_destructor.3488Tm
- ___swift_closure_destructor.3498Tm
- ___swift_closure_destructor.3501Tm
- ___swift_closure_destructor.3504Tm
- ___swift_closure_destructor.3580Tm
- ___swift_closure_destructor.3586Tm
- ___swift_closure_destructor.3595Tm
- ___swift_closure_destructor.360Tm
- ___swift_closure_destructor.4081Tm
- ___swift_closure_destructor.4125Tm
- ___swift_closure_destructor.4131Tm
- ___swift_closure_destructor.4261Tm
- ___swift_closure_destructor.42Tm
- ___swift_closure_destructor.4468Tm
- ___swift_closure_destructor.4471Tm
- ___swift_closure_destructor.4475Tm
- ___swift_closure_destructor.4478Tm
- ___swift_closure_destructor.4558Tm
- ___swift_closure_destructor.4584Tm
- ___swift_closure_destructor.4623Tm
- ___swift_closure_destructor.4739Tm
- ___swift_closure_destructor.4745Tm
- ___swift_closure_destructor.4960Tm
- ___swift_closure_destructor.512Tm
- ___swift_closure_destructor.5148Tm
- ___swift_closure_destructor.529Tm
- ___swift_closure_destructor.5421Tm
- ___swift_closure_destructor.5453Tm
- ___swift_closure_destructor.5756Tm
- ___swift_closure_destructor.57Tm
- ___swift_closure_destructor.5967Tm
- ___swift_closure_destructor.6269Tm
- ___swift_closure_destructor.6283Tm
- ___swift_closure_destructor.6489Tm
- ___swift_closure_destructor.6496Tm
- ___swift_closure_destructor.6521Tm
- ___swift_closure_destructor.6647Tm
- ___swift_closure_destructor.98Tm
- ___unnamed_114
- _objc_msgSend$initWithPath:fd:reader:sinceEventID:streamUUID:ignoreOwnEvents:delegate:purpose:
- _objc_msgSend$subscribeToEventsAtPath:fd:sinceEventID:streamUUID:ignoreOwnEvents:delegate:purpose:
- _objc_retain_x12
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
+ "      donation-status-backfill-in-progress: "
+ "(nil)"
+ ")\n    OR OLD.parent_id != NEW.parent_id\nBEGIN\n  UPDATE reconciliation_table\n    SET donation_status = "
+ ")\nBEGIN\n  UPDATE reconciliation_table\n    SET donation_status = CASE\n          WHEN (NEW.fs_deletion_status & "
+ ") != 0 THEN 0\n          WHEN NEW.fp_id IS NULL AND NEW.fs_id IS NOT NULL THEN 1\n          ELSE "
+ ") != 0 THEN 0 ELSE "
+ ") IS NOT (NEW.decoration_capabilities & "
+ ") IS NOT (NEW.fs_deletion_status & "
+ "-[FPDKnownFolderNotification generateAndPostNotifications]"
+ ".decoration_capabilities, "
+ ".decoration_is_container, "
+ ".filename = 'Documents' "
+ ".metadata_is_hidden)"
+ ".parent_id\n      AND "
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/FileProviderTools/fileproviderd/FPDKnownFolderNotification.m"
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
+ "IS_DONATABLE: failed to decode or empty item ID from sqlite value"
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
+ "_vfs_fileid_idx (vfs_fileid=?)"
+ "applyDonationStatusBackfill(from:through:with:)"
+ "backfill-donation-status"
+ "backfillDonationStatusRange(from:limit:with:)"
+ "bootstrapDonationStatusTriggers(with:)"
+ "com.apple.finder"
+ "donatableItemCount(with:)"
+ "donation_status_mismatch"
+ "fpfs-allow-donation-container-exclusion."
+ "fpfs_fetch_url_for_ino: unexpected nil buffer"
+ "has-real-domain"
+ "no-real-domain"
+ "onDonationBackfillComplete: indexer unavailable"
+ "reconciliation_table.fp_id"
+ "reconciliation_table.fs_deletion_status"
+ "reportDonationProgress(withAnchor:completionHandler:)"
+ "reportDonationProgress: spotlightIndexer unavailable"
+ "requestDonationProgressReport(completion:)"
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
