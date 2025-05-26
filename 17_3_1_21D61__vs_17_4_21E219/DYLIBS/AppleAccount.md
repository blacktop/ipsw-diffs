## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-981.5.2.0.0
-  __TEXT.__text: 0xb8ba8
-  __TEXT.__auth_stubs: 0xab0
-  __TEXT.__objc_methlist: 0x8bbc
-  __TEXT.__const: 0x1100
-  __TEXT.__cstring: 0xb2d6
-  __TEXT.__oslogstring: 0xca5d
-  __TEXT.__gcc_except_tab: 0x1624
+981.12.0.0.0
+  __TEXT.__text: 0xb7bd4
+  __TEXT.__auth_stubs: 0xac0
+  __TEXT.__objc_methlist: 0x8ce4
+  __TEXT.__const: 0x1610
+  __TEXT.__cstring: 0xb564
+  __TEXT.__oslogstring: 0xd2ca
+  __TEXT.__gcc_except_tab: 0x1718
   __TEXT.__dlopen_cstrs: 0x241
-  __TEXT.__unwind_info: 0x23c8
-  __TEXT.__objc_classname: 0x1b6a
-  __TEXT.__objc_methname: 0x12d69
-  __TEXT.__objc_methtype: 0x2951
-  __TEXT.__objc_stubs: 0xaa00
+  __TEXT.__unwind_info: 0x2458
+  __TEXT.__objc_classname: 0x1bc8
+  __TEXT.__objc_methname: 0x1322d
+  __TEXT.__objc_methtype: 0x29df
+  __TEXT.__objc_stubs: 0xac60
   __DATA_CONST.__got: 0x508
-  __DATA_CONST.__const: 0x2eb8
-  __DATA_CONST.__objc_classlist: 0x718
+  __DATA_CONST.__const: 0x3028
+  __DATA_CONST.__objc_classlist: 0x720
   __DATA_CONST.__objc_catlist: 0x98
-  __DATA_CONST.__objc_protolist: 0x140
+  __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1ab78
-  __DATA_CONST.__objc_selrefs: 0x42e8
+  __DATA_CONST.__objc_const: 0x1add8
+  __DATA_CONST.__objc_selrefs: 0x43c8
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_classrefs: 0x710
+  __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__cfstring: 0xab00
+  __AUTH_CONST.__cfstring: 0xace0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_const: 0x118
+  __AUTH_CONST.__objc_const: 0x1a8
   __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH_CONST.__const: 0x48d0
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH_CONST.__const: 0x4e60
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x568
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_protorefs: 0x38
-  __DATA.__objc_classrefs: 0x710
-  __DATA.__objc_superrefs: 0x508
-  __DATA.__objc_ivar: 0xab8
-  __DATA.__data: 0x1210
+  __AUTH_CONST.__auth_got: 0x570
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0xac4
+  __DATA.__data: 0x12e8
   __DATA.__bss: 0x300
-  __DATA.__common: 0x64
-  __DATA_DIRTY.__const: 0x740
-  __DATA_DIRTY.__objc_const: 0x5bb0
-  __DATA_DIRTY.__objc_data: 0x4650
+  __DATA.__common: 0x6c
+  __DATA_DIRTY.__const: 0x680
+  __DATA_DIRTY.__objc_const: 0x5b68
+  __DATA_DIRTY.__objc_data: 0x4600
   __DATA_DIRTY.__data: 0x60
   __DATA_DIRTY.__bss: 0x1e8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libcompression.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3814
-  Symbols:   13511
-  CStrings:  6267
+  Functions: 3868
+  Symbols:   13687
+  CStrings:  6376
 
Symbols:
+ +[AAPreferences repairWithoutTransparencyCFU]
+ +[AAUrlBagHelper canRepairCustodian]
+ +[AAUrlBagHelper maxRepairCount]
+ -[AAAppleIDRepairController .cxx_destruct]
+ -[AAAppleIDRepairController _fetchRepairState]
+ -[AAAppleIDRepairController _forceFetchUpdatedUserInformationWithCompletion:]
+ -[AAAppleIDRepairController init]
+ -[AAAppleIDRepairController offline_primaryAppleIDNeedsRepair]
+ -[AAAppleIDRepairController primaryAccount]
+ -[AAAppleIDRepairController primaryAppleIDRepairNeedsRepairCompletion:]
+ -[AAAppleIDRepairController setPrimaryAccount:]
+ -[AAContactsProvider fetchMyCachedCustodians:]
+ -[AACustodianController fetchCachedTrustedContactsWithCompletion:]
+ -[AACustodianController preflightCustodianRecoveryWithCompletion:]
+ -[AACustodianController repairCustodians:remove:completion:]
+ -[AAFollowUpController _custodianReviewNotification:]
+ -[AAFollowUpController _followUpItemForCustodianReview:]
+ -[AAFollowUpController _showAccountRecoveryPane]
+ -[AAFollowUpController(Convenience) _filterFollowUpItems:byIdentifier:byAccount:]
+ -[AAFollowUpController(Convenience) _filterFollowUpItems:byIdentifier:byAccount:].cold.1
+ -[AAFollowUpController(Convenience) _pendingFollowUpItemsWithIdentifier:forAccount:]
+ -[AAFollowUpController(Convenience) _pendingFollowUpItemsWithIdentifier:forAccount:].cold.1
+ -[AAFollowUpController(Convenience) _pendingFollowUpItemsWithIdentifier:forAccount:].cold.2
+ -[AAFollowUpController(Convenience) _pendingFollowUpItemsWithIdentifier:forAccount:completion:]
+ -[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:]
+ -[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:].cold.1
+ -[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:completion:]
+ -[AAProvisioningResponse ageCategory]
+ -[AATrustedContact initWithID:status:handle:firstName:lastName:displayName:isAcceptedAndShared:isIdMSConfirmed:preflightStatus:otCustodianID:keyCreatedOnBuild:repairDate:repairCount:]
+ -[AATrustedContact keyCreatedOnBuild]
+ -[AATrustedContact otCustodianID]
+ -[AATrustedContact repairCount]
+ -[AATrustedContact repairDate]
+ -[ACAccount(AppleAccount) aa_ageCategory]
+ GCC_except_table47
+ GCC_except_table50
+ GCC_except_table53
+ GCC_except_table56
+ GCC_except_table59
+ GCC_except_table67
+ GCC_except_table79
+ GCC_except_table88
+ GCC_except_table91
+ GCC_except_table95
+ GCC_except_table99
+ _AAFollowUpIdentifierCustodianReview
+ _AAFollowUpTrustedContactIDs
+ _OBJC_CLASS_$_AAAppleIDRepairController
+ _OBJC_CLASS_$_AAUrlBagHelper
+ _OBJC_IVAR_$_AAAppleIDRepairController.primaryAccount
+ _OBJC_IVAR_$_AATrustedContact._keyCreatedOnBuild
+ _OBJC_IVAR_$_AATrustedContact._otCustodianID
+ _OBJC_IVAR_$_AATrustedContact._repairCount
+ _OBJC_IVAR_$_AATrustedContact._repairDate
+ _OBJC_METACLASS_$_AAAppleIDRepairController
+ _OBJC_METACLASS_$_AAUrlBagHelper
+ _OUTLINED_FUNCTION_8
+ __AAUrlBagCanRepairCustodianKey
+ __AAUrlBagCustodianConfigKey
+ __AAUrlBagMaxRepairCountKey
+ __OBJC_$_CLASS_METHODS_AAUrlBagHelper
+ __OBJC_$_INSTANCE_METHODS_AAAppleIDRepairController
+ __OBJC_$_INSTANCE_VARIABLES_AAAppleIDRepairController
+ __OBJC_$_PROP_LIST_AAAppleIDRepairController
+ __OBJC_$_PROP_LIST_AAAppleIDRepairControllerProtocol_Internal
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AAAppleIDRepairControllerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AAAppleIDRepairControllerProtocol_Internal
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AAAppleIDRepairControllerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AAAppleIDRepairControllerProtocol_Internal
+ __OBJC_CLASS_PROTOCOLS_$_AAAppleIDRepairController
+ __OBJC_CLASS_RO_$_AAAppleIDRepairController
+ __OBJC_CLASS_RO_$_AAUrlBagHelper
+ __OBJC_LABEL_PROTOCOL_$_AAAppleIDRepairControllerProtocol
+ __OBJC_LABEL_PROTOCOL_$_AAAppleIDRepairControllerProtocol_Internal
+ __OBJC_METACLASS_RO_$_AAAppleIDRepairController
+ __OBJC_METACLASS_RO_$_AAUrlBagHelper
+ __OBJC_PROTOCOL_$_AAAppleIDRepairControllerProtocol
+ __OBJC_PROTOCOL_$_AAAppleIDRepairControllerProtocol_Internal
+ ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.379
+ ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.379.cold.1
+ ___46-[AAContactsProvider fetchMyCachedCustodians:]_block_invoke
+ ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.51
+ ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.51.cold.1
+ ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.52
+ ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.52.cold.1
+ ___60-[AACustodianController fetchTrustedContactsWithCompletion:]_block_invoke.29
+ ___60-[AACustodianController fetchTrustedContactsWithCompletion:]_block_invoke.29.cold.1
+ ___60-[AACustodianController fetchTrustedContactsWithCompletion:]_block_invoke.30
+ ___60-[AACustodianController fetchTrustedContactsWithCompletion:]_block_invoke.30.cold.1
+ ___60-[AACustodianController repairCustodians:remove:completion:]_block_invoke
+ ___60-[AACustodianController repairCustodians:remove:completion:]_block_invoke.76
+ ___60-[AACustodianController repairCustodians:remove:completion:]_block_invoke.76.cold.1
+ ___60-[AACustodianController repairCustodians:remove:completion:]_block_invoke.77
+ ___60-[AACustodianController repairCustodians:remove:completion:]_block_invoke.77.cold.1
+ ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.55
+ ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.55.cold.1
+ ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.56
+ ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.56.cold.1
+ ___62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.31
+ ___62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.31.cold.1
+ ___62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.32
+ ___62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.32.cold.1
+ ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.74
+ ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.74.cold.1
+ ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.75
+ ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.75.cold.1
+ ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.61
+ ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.61.cold.1
+ ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.62
+ ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.62.cold.1
+ ___64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.36
+ ___64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.36.cold.1
+ ___64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.37
+ ___64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.37.cold.1
+ ___65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.326
+ ___65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.326.cold.1
+ ___65-[AAFollowUpController pendingFollowUpWithIdentifier:completion:]_block_invoke.323
+ ___66-[AACustodianController fetchCachedTrustedContactsWithCompletion:]_block_invoke
+ ___66-[AACustodianController fetchCachedTrustedContactsWithCompletion:]_block_invoke.27
+ ___66-[AACustodianController fetchCachedTrustedContactsWithCompletion:]_block_invoke.27.cold.1
+ ___66-[AACustodianController fetchCachedTrustedContactsWithCompletion:]_block_invoke.28
+ ___66-[AACustodianController fetchCachedTrustedContactsWithCompletion:]_block_invoke.28.cold.1
+ ___66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.38
+ ___66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.38.cold.1
+ ___66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.39
+ ___66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.39.cold.1
+ ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke
+ ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.78
+ ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.78.cold.1
+ ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.79
+ ___66-[AACustodianController preflightCustodianRecoveryWithCompletion:]_block_invoke.79.cold.1
+ ___67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.34
+ ___67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.34.cold.1
+ ___67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.35
+ ___67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.35.cold.1
+ ___70-[AACustodianController performTrustedContactsDataSyncWithCompletion:]_block_invoke.53
+ ___70-[AACustodianController performTrustedContactsDataSyncWithCompletion:]_block_invoke.53.cold.1
+ ___70-[AACustodianController performTrustedContactsDataSyncWithCompletion:]_block_invoke.54
+ ___70-[AACustodianController performTrustedContactsDataSyncWithCompletion:]_block_invoke.54.cold.1
+ ___70-[AACustodianController startCustodianRecoveryWithContext:completion:]_block_invoke.41
+ ___70-[AACustodianController startCustodianRecoveryWithContext:completion:]_block_invoke.41.cold.1
+ ___71-[AAAppleIDRepairController primaryAppleIDRepairNeedsRepairCompletion:]_block_invoke
+ ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.59
+ ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.59.cold.1
+ ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.60
+ ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.60.cold.1
+ ___71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.57
+ ___71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.57.cold.1
+ ___71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.58
+ ___71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.319
+ ___71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.319.cold.1
+ ___75-[AACustodianController fetchCustodianRecoveryConfigurationWithCompletion:]_block_invoke.43
+ ___75-[AACustodianController fetchCustodianRecoveryConfigurationWithCompletion:]_block_invoke.43.cold.1
+ ___75-[AAFollowUpController(Convenience) pendingFollowUpsForAccount:completion:]_block_invoke.380
+ ___76-[AACustodianController fetchCustodianRecoveryKeysWithSessionID:completion:]_block_invoke.48
+ ___76-[AACustodianController fetchCustodianRecoveryKeysWithSessionID:completion:]_block_invoke.48.cold.1
+ ___77-[AAAppleIDRepairController _forceFetchUpdatedUserInformationWithCompletion:]_block_invoke
+ ___77-[AAAppleIDRepairController _forceFetchUpdatedUserInformationWithCompletion:]_block_invoke.cold.1
+ ___77-[AACustodianController generateCustodianRecoveryCodeWithContext:completion:]_block_invoke.44
+ ___77-[AACustodianController generateCustodianRecoveryCodeWithContext:completion:]_block_invoke.44.cold.1
+ ___77-[AACustodianController validateCustodianRecoveryCodeWithContext:completion:]_block_invoke.46
+ ___77-[AACustodianController validateCustodianRecoveryCodeWithContext:completion:]_block_invoke.46.cold.1
+ ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.384
+ ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.384.cold.1
+ ___80-[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:]_block_invoke
+ ___80-[AARemoteServer(Deprecated) _startRequest:responseClass:mainThread:completion:]_block_invoke.204
+ ___81-[AAFollowUpController(Convenience) _filterFollowUpItems:byIdentifier:byAccount:]_block_invoke
+ ___81-[AAFollowUpController(Convenience) _filterFollowUpItems:byIdentifier:byAccount:]_block_invoke_2
+ ___87-[AAFollowUpController(Convenience) dismissFollowUpsForAccount:identifiers:completion:]_block_invoke.378
+ ___88-[AACustodianController fetchCustodianPasswordResetInformationWithSessionID:completion:]_block_invoke.50
+ ___88-[AACustodianController fetchCustodianPasswordResetInformationWithSessionID:completion:]_block_invoke.50.cold.1
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.376
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.376.cold.1
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.376.cold.2
+ ___91-[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:completion:]_block_invoke
+ ___91-[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:completion:]_block_invoke.387
+ ___91-[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:completion:]_block_invoke.cold.1
+ ___95-[AAFollowUpController(Convenience) _pendingFollowUpItemsWithIdentifier:forAccount:completion:]_block_invoke
+ ___95-[AAFollowUpController(Convenience) _pendingFollowUpItemsWithIdentifier:forAccount:completion:]_block_invoke.cold.1
+ ____AAFollowUpControllerHandleSetupAssistantExited_block_invoke.426
+ ___block_descriptor_32_e24_16?0"FLFollowUpItem"8l
+ ___block_descriptor_40_e8_32bs_e39_v24?0"AKUserInformation"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e8_v16?0Q8ls32l8
+ ___block_descriptor_40_e8_32s_e27_B24?0"FLFollowUpItem"8Q16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e29_v24?0"NSArray"8"NSError"16lr64l8s56l8s32l8s40l8s48l8
+ ___block_literal_global.125
+ ___block_literal_global.127
+ ___block_literal_global.129
+ ___block_literal_global.131
+ ___block_literal_global.186
+ ___block_literal_global.190
+ ___block_literal_global.192
+ ___block_literal_global.242
+ ___block_literal_global.390
+ ___block_literal_global.428
+ ___block_literal_global.702
+ ___block_literal_global.707
+ __unnamed_array_storage.202
+ _kAAAccountAgeCategory
+ _kAACustodianPostRepairCFUEvent
+ _kAACustodianPreflightEvent
+ _kAACustodianRemoveEvent
+ _kAACustodianRepairCFUActionBeginEvent
+ _kAACustodianRepairCFUActionEndEvent
+ _kAACustodianRepairEvent
+ _kAAProtocolAgeCategoryKey
+ _kAAProtocolPrefRepairWithoutTransparencyCFUKey
+ _kAATrustedContactsPreflightBeginEvent
+ _kAATrustedContactsPreflightEndEvent
+ _kInheritancePreflightCheckEventName
+ _objc_msgSend$_custodianReviewNotification:
+ _objc_msgSend$_fetchRepairState
+ _objc_msgSend$_filterFollowUpItems:byIdentifier:byAccount:
+ _objc_msgSend$_followUpItemForCustodianReview:
+ _objc_msgSend$_forceFetchUpdatedUserInformationWithCompletion:
+ _objc_msgSend$_pendingFollowUpItemsWithIdentifier:forAccount:
+ _objc_msgSend$_pendingFollowUpItemsWithIdentifier:forAccount:completion:
+ _objc_msgSend$_showAccountRecoveryPane
+ _objc_msgSend$ageCategory
+ _objc_msgSend$configurationAtKey:
+ _objc_msgSend$fetchCachedTrustedContactsWithCompletion:
+ _objc_msgSend$getUserInformationForAltDSID:completion:
+ _objc_msgSend$preflightCustodianRecoveryWithCompletion:
+ _objc_msgSend$repairCustodians:remove:completion:
+ _objc_msgSend$repairState
+ _objc_msgSend$repairStateForAccount:
+ _objc_msgSend$setPrimaryAccount:
+ _objc_msgSend$setTimeoutIntervalForResource:
+ _objc_msgSend$setWaitsForConnectivity:
+ _objc_setProperty_atomic
- -[AASpyglassSpecifierModel .cxx_destruct]
- -[AASpyglassSpecifierModel iconName]
- -[AASpyglassSpecifierModel initForSpecifierType:]
- -[AASpyglassSpecifierModel setIconName:]
- -[AASpyglassSpecifierModel setTitle:]
- -[AASpyglassSpecifierModel title]
- -[AATrustedContact initWithID:status:handle:firstName:lastName:displayName:isAcceptedAndShared:isIdMSConfirmed:preflightStatus:]
- GCC_except_table57
- GCC_except_table60
- GCC_except_table87
- _OBJC_CLASS_$_AASpyglassSpecifierModel
- _OBJC_IVAR_$_AASpyglassSpecifierModel._iconName
- _OBJC_IVAR_$_AASpyglassSpecifierModel._title
- _OBJC_METACLASS_$_AASpyglassSpecifierModel
- __OBJC_$_INSTANCE_METHODS_AASpyglassSpecifierModel
- __OBJC_$_INSTANCE_VARIABLES_AASpyglassSpecifierModel
- __OBJC_$_PROP_LIST_AASpyglassSpecifierModel
- __OBJC_CLASS_RO_$_AASpyglassSpecifierModel
- __OBJC_METACLASS_RO_$_AASpyglassSpecifierModel
- ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.367
- ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.367.cold.1
- ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.49
- ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.49.cold.1
- ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.50
- ___56-[AACustodianController startHealthCheckWithCompletion:]_block_invoke.50.cold.1
- ___60-[AACustodianController fetchTrustedContactsWithCompletion:]_block_invoke.27
- ___60-[AACustodianController fetchTrustedContactsWithCompletion:]_block_invoke.27.cold.1
- ___60-[AACustodianController fetchTrustedContactsWithCompletion:]_block_invoke.28
- ___60-[AACustodianController fetchTrustedContactsWithCompletion:]_block_invoke.28.cold.1
- ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.53
- ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.53.cold.1
- ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.54
- ___61-[AACustodianController startManateeMigrationWithCompletion:]_block_invoke.54.cold.1
- ___62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.29
- ___62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.29.cold.1
- ___62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.30
- ___62-[AACustodianController fetchCustodianshipInfoWithCompletion:]_block_invoke.30.cold.1
- ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.72
- ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.72.cold.1
- ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.73
- ___64-[AACustodianController availableRecoveryFactorsWithCompletion:]_block_invoke.73.cold.1
- ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.59
- ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.59.cold.1
- ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.60
- ___64-[AACustodianController displayInvitationUIWithUUID:completion:]_block_invoke.60.cold.1
- ___64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.34
- ___64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.34.cold.1
- ___64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.35
- ___64-[AACustodianController fetchSuggestedCustodiansWithCompletion:]_block_invoke.35.cold.1
- ___65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.317
- ___65-[AAFollowUpController dismissFollowUpWithIdentifier:completion:]_block_invoke.317.cold.1
- ___65-[AAFollowUpController pendingFollowUpWithIdentifier:completion:]_block_invoke.314
- ___66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.36
- ___66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.36.cold.1
- ___66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.37
- ___66-[AACustodianController fetchCustodianHealthStatusWithCompletion:]_block_invoke.37.cold.1
- ___67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.32
- ___67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.32.cold.1
- ___67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.33
- ___67-[AACustodianController fetchCustodianshipInfoWithUUID:completion:]_block_invoke.33.cold.1
- ___70-[AACustodianController performTrustedContactsDataSyncWithCompletion:]_block_invoke.51
- ___70-[AACustodianController performTrustedContactsDataSyncWithCompletion:]_block_invoke.51.cold.1
- ___70-[AACustodianController performTrustedContactsDataSyncWithCompletion:]_block_invoke.52
- ___70-[AACustodianController performTrustedContactsDataSyncWithCompletion:]_block_invoke.52.cold.1
- ___70-[AACustodianController startCustodianRecoveryWithContext:completion:]_block_invoke.39
- ___70-[AACustodianController startCustodianRecoveryWithContext:completion:]_block_invoke.39.cold.1
- ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.57
- ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.57.cold.1
- ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.58
- ___71-[AACustodianController displayTrustedContactFlowWithModel:completion:]_block_invoke.58.cold.1
- ___71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.55
- ___71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.55.cold.1
- ___71-[AACustodianController pullTrustedContactsFromCloudKitWithCompletion:]_block_invoke.56
- ___71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.310
- ___71-[AAFollowUpController postFollowUpWithIdentifier:userInfo:completion:]_block_invoke.310.cold.1
- ___75-[AACustodianController fetchCustodianRecoveryConfigurationWithCompletion:]_block_invoke.41
- ___75-[AACustodianController fetchCustodianRecoveryConfigurationWithCompletion:]_block_invoke.41.cold.1
- ___75-[AAFollowUpController(Convenience) pendingFollowUpsForAccount:completion:]_block_invoke.368
- ___76-[AACustodianController fetchCustodianRecoveryKeysWithSessionID:completion:]_block_invoke.46
- ___76-[AACustodianController fetchCustodianRecoveryKeysWithSessionID:completion:]_block_invoke.46.cold.1
- ___77-[AACustodianController generateCustodianRecoveryCodeWithContext:completion:]_block_invoke.42
- ___77-[AACustodianController generateCustodianRecoveryCodeWithContext:completion:]_block_invoke.42.cold.1
- ___77-[AACustodianController validateCustodianRecoveryCodeWithContext:completion:]_block_invoke.44
- ___77-[AACustodianController validateCustodianRecoveryCodeWithContext:completion:]_block_invoke.44.cold.1
- ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.372
- ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.372.cold.1
- ___80-[AARemoteServer(Deprecated) _startRequest:responseClass:mainThread:completion:]_block_invoke.203
- ___87-[AAFollowUpController(Convenience) dismissFollowUpsForAccount:identifiers:completion:]_block_invoke.366
- ___88-[AACustodianController fetchCustodianPasswordResetInformationWithSessionID:completion:]_block_invoke.48
- ___88-[AACustodianController fetchCustodianPasswordResetInformationWithSessionID:completion:]_block_invoke.48.cold.1
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.364
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.364.cold.1
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.364.cold.2
- ____AAFollowUpControllerHandleSetupAssistantExited_block_invoke.403
- ___block_literal_global.124
- ___block_literal_global.126
- ___block_literal_global.128
- ___block_literal_global.130
- ___block_literal_global.185
- ___block_literal_global.189
- ___block_literal_global.191
- ___block_literal_global.241
- ___block_literal_global.700
- ___block_literal_global.705
- __unnamed_array_storage.201
- _malloc
CStrings:
+ "\x11\x14\x13"
+ "@\"ACAccount\"16@0:8"
+ "@112@0:8@16q24@32@40@48@56B64B68q72@80@88@96Q104"
+ "@16@?0@\"FLFollowUpItem\"8"
+ "AAAppleIDRepairController"
+ "AAAppleIDRepairControllerProtocol"
+ "AAAppleIDRepairControllerProtocol_Internal"
+ "AARepairWithoutTransparencyCFU"
+ "AAUrlBagHelper"
+ "AppleAccount daemon connection for Preflighting custodian returned an error: %@"
+ "AppleAccount daemon connection for fetching cached trusted contacts returned an error: %@"
+ "AppleAccount daemon connection for removing custodian returned an error: %@"
+ "AppleAccount daemon connection for repairing custodian returned an error: %@"
+ "Attempting to fetch follow up items with identifier: %{public}@"
+ "Attempting to fetch pending CFUs"
+ "Attempting to fetch user info of follow up item with identifier: %{public}@"
+ "Authentication Header after Base64: %@"
+ "Authentication Header before Base64: %@"
+ "B24@?0@\"FLFollowUpItem\"8Q16"
+ "BEGIN [%lld]: FetchCachedTrustedContacts  enableTelemetry=YES "
+ "BEGIN [%lld]: PreflightCustodianRecovery  enableTelemetry=YES "
+ "BEGIN [%lld]: RepairCustodians  enableTelemetry=YES "
+ "Custodians repaired/removed successfully."
+ "DecoupleOTPeerID"
+ "END [%lld] %fs: FetchCachedTrustedContacts  Error=%{public,signpost.telemetry:number2,name=Error}d "
+ "END [%lld] %fs: PreflightCustodianRecovery  Error=%{public,signpost.telemetry:number2,name=Error}d "
+ "END [%lld] %fs: RepairCustodians  Error=%{public,signpost.telemetry:number2,name=Error}d "
+ "Error fetching cached trusted contacts: %@"
+ "Error fetching user information: %@"
+ "Error repairing/removing error: %@"
+ "FOLLOWUP_CUSTODIAN_REVIEW_BUTTON_PRIMARY"
+ "FOLLOWUP_CUSTODIAN_REVIEW_MESSAGE"
+ "FOLLOWUP_CUSTODIAN_REVIEW_TITLE"
+ "Failed to fetch pending CFUs"
+ "Failed to fetch pending follow ups with Identifieer: %{public}@"
+ "FetchCachedTrustedContacts"
+ "Fetched cached trusted contacts: %@"
+ "Fetching cached trusted contacts."
+ "Final repair state %@"
+ "Preflight custodian recovery failed: %@"
+ "Preflight custodian recovery successfully."
+ "PreflightCustodianRecovery"
+ "RepairCustodians"
+ "Repairing custodians %@ and removing custodians %@"
+ "Returning canRepairCustodian based on feature flag: %d"
+ "Returning canRepairCustodian from urlbag: %@"
+ "Returning maxRepairCount default value: 1"
+ "Returning maxRepairCount from urlbag: %@"
+ "Starting Preflight custodian recovery in CustodianController"
+ "Successfully fetched follow ups: %{private}@"
+ "Successfully fetched user infos of pending follow ups: %{private}@"
+ "T@\"AACustodianshipInfo\",?,C,N"
+ "T@\"AACustodianshipInfo\",?,C,N,V_custodianshipInfo"
+ "T@\"ACAccount\",&"
+ "T@\"ACAccount\",&,VprimaryAccount"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,C,N,V_detailText"
+ "T@\"NSString\",?,C,N,V_helpLinkTitle"
+ "T@\"NSString\",?,C,N,V_helpLinkURL"
+ "T@\"NSString\",?,C,N,V_imageName"
+ "T@\"NSString\",?,C,N,V_leftBarButton"
+ "T@\"NSString\",?,C,N,V_ownerHandle"
+ "T@\"NSString\",?,C,N,V_primaryButton"
+ "T@\"NSString\",?,C,N,V_recipientHandle"
+ "T@\"NSString\",?,C,N,V_secondaryButton"
+ "T@\"NSString\",?,C,N,V_title"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,N,V_keyCreatedOnBuild"
+ "T@\"NSString\",R,N,V_repairDate"
+ "T@\"NSUUID\",R,N,V_otCustodianID"
+ "TQ,?,N"
+ "TQ,?,N,V_currentVersion"
+ "TQ,R,N,V_repairCount"
+ "User information returned state: %@"
+ "_custodianReviewNotification:"
+ "_fetchRepairState"
+ "_filterFollowUpItems:byIdentifier:byAccount:"
+ "_followUpItemForCustodianReview:"
+ "_forceFetchUpdatedUserInformationWithCompletion:"
+ "_keyCreatedOnBuild"
+ "_otCustodianID"
+ "_pendingFollowUpItemsWithIdentifier:forAccount:"
+ "_pendingFollowUpItemsWithIdentifier:forAccount:completion:"
+ "_repairCount"
+ "_repairDate"
+ "_showAccountRecoveryPane"
+ "aa_ageCategory"
+ "ageCategory"
+ "canRepairCustodian"
+ "com.apple.AAFollowUpIdentifier.custodianReview"
+ "com.apple.appleaccount.custodian.postRepairCFU"
+ "com.apple.appleaccount.custodian.preflight"
+ "com.apple.appleaccount.custodian.remove"
+ "com.apple.appleaccount.custodian.repair"
+ "com.apple.appleaccount.custodian.repairCFU.action.begin"
+ "com.apple.appleaccount.custodian.repairCFU.action.end"
+ "com.apple.appleaccount.inheritance.preflightCheckEvent"
+ "com.apple.appleaccount.trustedContacts.preflight.begin"
+ "com.apple.appleaccount.trustedContacts.preflight.end"
+ "configurationAtKey:"
+ "custodian-appleaccount/custodian-repair"
+ "custodian-appleaccount/fetch-cached-trusted-contacts"
+ "custodian-appleaccount/preflight-custodian-recovery"
+ "custodianCfgs"
+ "custodianCfgs from urlbag: %@"
+ "fetchCachedTrustedContactsWithCompletion:"
+ "fetchMyCachedCustodians:"
+ "getUserInformationForAltDSID:completion:"
+ "initWithID:status:handle:firstName:lastName:displayName:isAcceptedAndShared:isIdMSConfirmed:preflightStatus:otCustodianID:keyCreatedOnBuild:repairDate:repairCount:"
+ "keyCreatedOnBuild"
+ "maxRepairCount"
+ "offline_primaryAppleIDNeedsRepair"
+ "otCustodianID"
+ "pendingFollowUpItemUserInfosWithIdentifier:"
+ "pendingFollowUpItemUserInfosWithIdentifier:completion:"
+ "preflightCustodianRecoveryWithCompletion:"
+ "primaryAppleIDRepairNeedsRepairCompletion:"
+ "repairCount"
+ "repairCustodians:remove:completion:"
+ "repairDate"
+ "repairStateForAccount:"
+ "repairWithoutTransparencyCFU"
+ "setTimeoutIntervalForResource:"
+ "setWaitsForConnectivity:"
+ "trustedContactIDs"
+ "v16@?0Q8"
+ "v24@0:8@\"ACAccount\"16"
+ "v24@0:8@?<v@?B>16"
+ "v24@0:8@?<v@?Q>16"
+ "v24@?0@\"AKUserInformation\"8@\"NSError\"16"
+ "v40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?@\"NSError\">32"
- "\x11\x14"
- "@80@0:8@16q24@32@40@48@56B64B68q72"
- "AASpyglassSpecifierModel"
- "SPYGLASS_SPECIFIER_PAYMENT_AND_SHIPPING"
- "SPYGLASS_SPECIFIER_PERSONAL_INFORMATION"
- "SPYGLASS_SPECIFIER_SIGNIN_AND_SECURITY"
- "SPYGLASS_SPECIFIER_SUBSCRIPTIONS"
- "T@\"AACustodianshipInfo\",C,N"
- "T@\"AACustodianshipInfo\",C,N,V_custodianshipInfo"
- "T@\"NSString\",C,N,V_detailText"
- "T@\"NSString\",C,N,V_helpLinkTitle"
- "T@\"NSString\",C,N,V_helpLinkURL"
- "T@\"NSString\",C,N,V_iconName"
- "T@\"NSString\",C,N,V_imageName"
- "T@\"NSString\",C,N,V_leftBarButton"
- "T@\"NSString\",C,N,V_ownerHandle"
- "T@\"NSString\",C,N,V_primaryButton"
- "T@\"NSString\",C,N,V_recipientHandle"
- "T@\"NSString\",C,N,V_secondaryButton"
- "TQ,N"
- "TQ,N,V_currentVersion"
- "_iconName"
- "creditcard.fill"
- "goforward.plus"
- "iconName"
- "initForSpecifierType:"
- "initWithID:status:handle:firstName:lastName:displayName:isAcceptedAndShared:isIdMSConfirmed:preflightStatus:"
- "key.horizontal.fill"
- "person.text.rectangle.fill"
- "setIconName:"

```
