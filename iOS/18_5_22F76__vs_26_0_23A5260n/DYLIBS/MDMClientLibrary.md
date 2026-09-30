## MDMClientLibrary

> `/System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary`

```diff

-20.5.1.2.0
-  __TEXT.__text: 0x19d08
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x17fc
+43.0.0.0.0
+  __TEXT.__text: 0x1e9c4
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__objc_methlist: 0x1d14
   __TEXT.__const: 0xd1
-  __TEXT.__gcc_except_tab: 0x450
-  __TEXT.__cstring: 0x207b
-  __TEXT.__oslogstring: 0x2aa0
+  __TEXT.__gcc_except_tab: 0x538
+  __TEXT.__cstring: 0x22b2
+  __TEXT.__oslogstring: 0x2e98
   __TEXT.__dlopen_cstrs: 0xb7
-  __TEXT.__unwind_info: 0x610
-  __TEXT.__objc_classname: 0x303
-  __TEXT.__objc_methname: 0x488a
-  __TEXT.__objc_methtype: 0x8b0
-  __TEXT.__objc_stubs: 0x32c0
+  __TEXT.__unwind_info: 0x808
+  __TEXT.__objc_classname: 0x336
+  __TEXT.__objc_methname: 0x5388
+  __TEXT.__objc_methtype: 0xba2
+  __TEXT.__objc_stubs: 0x3800
   __DATA_CONST.__got: 0x398
-  __DATA_CONST.__const: 0x1078
-  __DATA_CONST.__objc_classlist: 0xc0
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__const: 0x1168
+  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1198
+  __DATA_CONST.__objc_selrefs: 0x1358
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x468
-  __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x3080
-  __AUTH_CONST.__objc_const: 0x3438
+  __DATA_CONST.__objc_superrefs: 0x78
+  __AUTH_CONST.__auth_got: 0x470
+  __AUTH_CONST.__const: 0x3c0
+  __AUTH_CONST.__cfstring: 0x31e0
+  __AUTH_CONST.__objc_const: 0x39e8
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x114
-  __DATA.__data: 0x4e0
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x124
+  __DATA.__data: 0x540
   __DATA.__bss: 0x110
-  __DATA_DIRTY.__objc_data: 0x6e0
-  __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__objc_data: 0x690
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D867CE18-55B0-3C6D-BF66-07A7F70169E1
-  Functions: 549
-  Symbols:   2550
-  CStrings:  1818
+  UUID: 933069E5-276D-3F44-8690-0F23E59DA162
+  Functions: 668
+  Symbols:   2888
+  CStrings:  1949
 
Symbols:
+ +[MDMCheckInRequest _checkInRequestAtURL:identity:pinnedSecCertificateRefs:pinningRevocationCheckRequired:signMessage:isUserEnrollment:enrollmentID:topic:pushMagic:rmAccountID:messageType:requestDict:channelType:isCheckout:isShortTransaction:completionHandler:]
+ +[MDMCheckInRequest _requestDataWithRequestDict:enrollmentID:topic:pushMagic:isUserEnrollment:messageType:channelType:error:]
+ +[MDMCheckInRequest _userFieldsForRequest]
+ +[MDMCheckInRequest executeRequestForMessageType:channelType:requestDict:isCheckout:shouldIncludeTopic:shouldIncludePushMagic:isEnrollmentRequired:isShortTransaction:completionHandler:]
+ +[MDMConfiguration _failedToConvertTokenDataError]
+ +[MDMConfiguration getOrgTokenForMAIDWithCompletionHandler:]
+ +[MDMConfiguration getWatchPairingTokenForPhoneID:watchID:securityToken:completionHandler:]
+ +[MDMConfigurationBase sharedConfigurationForChannel:]
+ +[MDMProvisioningProfileTrust appSignerIdentityForBundleID:]
+ +[MDMProvisioningProfileTrust manualTrustSignerIdentities:]
+ +[MDMProvisioningProfileTrust untrustProvisioningProfileUUID:]
+ +[MDMUserConfiguration sharedConfiguration]
+ +[MDMUserConfiguration sharedConfiguration].cold.1
+ -[MDMClientCore _debug_nagForMigrationWithCompletion:]
+ -[MDMClientCore _debug_stopNaggingForMigration]
+ -[MDMClientCore blockMDMCommandsWithCompletion:]
+ -[MDMClientCore deleteBootstrapTokenWithToken:devicePasscode:completionHandler:]
+ -[MDMClientCore disablePushWakeWithCompletion:]
+ -[MDMClientCore enablePushWakeWithCompletion:]
+ -[MDMClientCore evaluateMigrationStatusWithPollFromServer:completionHandler:]
+ -[MDMClientCore generateBootstrapTokenWithDevicePasscode:completionHandler:]
+ -[MDMClientCore getOrgTokenForMAIDWithCompletionHandler:]
+ -[MDMClientCore getWatchPairingTokenForPhoneID:watchID:securityToken:completionHandler:]
+ -[MDMClientCore nagWithID:clientID:schedule:title:message:notificationTitle:notificationMessage:actionTitle:actionURL:dismissTitle:dismissURL:deadlineURL:completion:]
+ -[MDMClientCore preserveAppsWithCompletion:]
+ -[MDMClientCore removeUnusedPreservedAppsWithCompletion:]
+ -[MDMClientCore requestDeviceObliterationWithPreserveDataPlan:disallowProximitySetup:completionHandler:]
+ -[MDMClientCore requestRRTSCheckInAndValidationWithCompletionHandler:]
+ -[MDMClientCore requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:]
+ -[MDMClientCore sendMDMAuthenticationRequestWithCompletionHandler:]
+ -[MDMClientCore sendMDMCheckOutRequestWithCompletionHandler:]
+ -[MDMClientCore syncBootstrapTokenToMDMWithToken:completionHandler:]
+ -[MDMClientCore unblockMDMCommandsWithCompletion:]
+ -[MDMCloudConfiguration migrationDeadline]
+ -[MDMCloudConfiguration shouldIgnoreMDMFromBackup]
+ -[MDMConfiguration accessRights]
+ -[MDMConfiguration channelType]
+ -[MDMConfiguration checkInPinnedSecCertificateRefs]
+ -[MDMConfiguration checkInURL]
+ -[MDMConfiguration isADEProfile]
+ -[MDMConfiguration managingProfileIdentifier]
+ -[MDMConfiguration memberQueueEASEnrollmentID]
+ -[MDMConfiguration memberQueueEnrollmentID]
+ -[MDMConfiguration memberQueueEnrollmentMode]
+ -[MDMConfiguration memberQueueIdentityPersistentID]
+ -[MDMConfiguration memberQueueIsADEProfile]
+ -[MDMConfiguration memberQueueIsProfileLocked]
+ -[MDMConfiguration memberQueueIsUserEnrollment]
+ -[MDMConfiguration memberQueuePersonaID]
+ -[MDMConfiguration memberQueueRMAccountID]
+ -[MDMConfiguration memberQueueReadConfigurationOutError:]
+ -[MDMConfiguration memberQueueSupportUserChannel]
+ -[MDMConfiguration organizationInfo]
+ -[MDMConfiguration pinningRevocationCheckRequired]
+ -[MDMConfiguration pushMagic]
+ -[MDMConfiguration serverCapabilities]
+ -[MDMConfiguration serverURL]
+ -[MDMConfiguration setMemberQueueEASEnrollmentID:]
+ -[MDMConfiguration setMemberQueueEnrollmentID:]
+ -[MDMConfiguration setMemberQueueEnrollmentMode:]
+ -[MDMConfiguration setMemberQueueIdentityPersistentID:]
+ -[MDMConfiguration setMemberQueueIsADEProfile:]
+ -[MDMConfiguration setMemberQueueIsProfileLocked:]
+ -[MDMConfiguration setMemberQueueIsUserEnrollment:]
+ -[MDMConfiguration setMemberQueuePersonaID:]
+ -[MDMConfiguration setMemberQueueRMAccountID:]
+ -[MDMConfiguration setMemberQueueSupportUserChannel:]
+ -[MDMConfiguration signMessage]
+ -[MDMConfiguration topic]
+ -[MDMConfigurationBase .cxx_destruct]
+ -[MDMConfigurationBase _mdmFilePathForChannelType:]
+ -[MDMConfigurationBase _mdmPropertiesFilePathForChannelType:]
+ -[MDMConfigurationBase _memberQueueReadPropertiesForChannelType:createIfMissingFile:error:]
+ -[MDMConfigurationBase _memberQueueWriteProperties:channelType:error:]
+ -[MDMConfigurationBase channelType]
+ -[MDMConfigurationBase details]
+ -[MDMConfigurationBase getPropertyForKey:channelType:error:]
+ -[MDMConfigurationBase getPropertyForKey:error:]
+ -[MDMConfigurationBase init]
+ -[MDMConfigurationBase lastPushTokenHash]
+ -[MDMConfigurationBase memberQueueForgetCurrentConfiguration]
+ -[MDMConfigurationBase memberQueueLastPushTokenHash]
+ -[MDMConfigurationBase memberQueueMDMDictionary]
+ -[MDMConfigurationBase memberQueuePushMagicMismatchDateMarker]
+ -[MDMConfigurationBase memberQueueReadConfigurationOutError:]
+ -[MDMConfigurationBase memberQueue]
+ -[MDMConfigurationBase pushMagicMismatchDateMarker]
+ -[MDMConfigurationBase refreshDetailsFromDisk]
+ -[MDMConfigurationBase removeMDMConfigurationForChannel:error:]
+ -[MDMConfigurationBase removeMDMConfigurationWithError:]
+ -[MDMConfigurationBase retrieveMDMDictionaryWithError:]
+ -[MDMConfigurationBase setMemberQueue:]
+ -[MDMConfigurationBase setMemberQueueLastPushTokenHash:]
+ -[MDMConfigurationBase setMemberQueueMDMDictionary:]
+ -[MDMConfigurationBase setMemberQueuePushMagicMismatchDateMarker:]
+ -[MDMConfigurationBase setPropertyForKey:value:channelType:error:]
+ -[MDMConfigurationBase setPropertyForKey:value:error:]
+ -[MDMConfigurationBase updateMDMConfigurationForChannel:createIfNeeded:error:updateBlock:]
+ -[MDMConfigurationBase updateMDMConfigurationWithCreateIfNeeded:updateBlock:error:]
+ -[MDMConfigurationBase updateMDMConfigurationWithUpdateBlock:error:]
+ -[MDMProvisioningProfileTrust didEnrollInMDMWithPasscode:duringMigration:]
+ -[MDMProvisioningProfileTrust didUnenrollFromMDM]
+ -[MDMProvisioningProfileTrust isUnenrollingFromMDM]
+ -[MDMProvisioningProfileTrust setIsUnenrollingFromMDM:]
+ -[MDMProvisioningProfileTrust untrustSignerIdentities:]
+ -[MDMUserConfiguration channelType]
+ GCC_except_table102
+ GCC_except_table11
+ GCC_except_table13
+ GCC_except_table19
+ GCC_except_table2
+ GCC_except_table20
+ GCC_except_table21
+ GCC_except_table24
+ GCC_except_table26
+ GCC_except_table28
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table36
+ GCC_except_table38
+ GCC_except_table42
+ GCC_except_table44
+ GCC_except_table46
+ GCC_except_table48
+ GCC_except_table50
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table7
+ GCC_except_table87
+ GCC_except_table98
+ _MDMFileChangedNotification
+ _MDMSendMDMFileChangedNotification
+ _MDMSendSkipkeyChangedNotification
+ _MDMSkipKeyChangedNotification
+ _MDMUserFilePath
+ _NSStringFromClass
+ _OBJC_CLASS_$_DMCDateFormatterFactory
+ _OBJC_CLASS_$_MDMConfigurationBase
+ _OBJC_CLASS_$_MDMUserConfiguration
+ _OBJC_CLASS_$_MISProfileDBClient
+ _OBJC_IVAR_$_MDMConfiguration._memberQueueEASEnrollmentID
+ _OBJC_IVAR_$_MDMConfiguration._memberQueueEnrollmentID
+ _OBJC_IVAR_$_MDMConfiguration._memberQueueEnrollmentMode
+ _OBJC_IVAR_$_MDMConfiguration._memberQueueIdentityPersistentID
+ _OBJC_IVAR_$_MDMConfiguration._memberQueueIsADEProfile
+ _OBJC_IVAR_$_MDMConfiguration._memberQueueIsProfileLocked
+ _OBJC_IVAR_$_MDMConfiguration._memberQueueIsUserEnrollment
+ _OBJC_IVAR_$_MDMConfiguration._memberQueuePersonaID
+ _OBJC_IVAR_$_MDMConfiguration._memberQueueRMAccountID
+ _OBJC_IVAR_$_MDMConfiguration._memberQueueSupportUserChannel
+ _OBJC_IVAR_$_MDMConfigurationBase._memberQueue
+ _OBJC_IVAR_$_MDMConfigurationBase._memberQueueLastPushTokenHash
+ _OBJC_IVAR_$_MDMConfigurationBase._memberQueueMDMDictionary
+ _OBJC_IVAR_$_MDMConfigurationBase._memberQueuePushMagicMismatchDateMarker
+ _OBJC_IVAR_$_MDMProvisioningProfileTrust._isUnenrollingFromMDM
+ _OBJC_METACLASS_$_MDMConfigurationBase
+ _OBJC_METACLASS_$_MDMUserConfiguration
+ __OBJC_$_CLASS_METHODS_MDMConfigurationBase
+ __OBJC_$_CLASS_METHODS_MDMUserConfiguration
+ __OBJC_$_INSTANCE_METHODS_MDMConfigurationBase
+ __OBJC_$_INSTANCE_METHODS_MDMUserConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_MDMConfigurationBase
+ __OBJC_$_PROP_LIST_MDMConfigurationBase
+ __OBJC_$_PROP_LIST_MDMConfigurationCommonProperties
+ __OBJC_$_PROP_LIST_MDMConfigurationProperties
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MDMConfigurationCommonProperties
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MDMConfigurationProperties
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MDMConfigurationCommonProperties
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MDMConfigurationProperties
+ __OBJC_CLASS_PROTOCOLS_$_MDMConfigurationBase
+ __OBJC_CLASS_RO_$_MDMConfigurationBase
+ __OBJC_CLASS_RO_$_MDMUserConfiguration
+ __OBJC_LABEL_PROTOCOL_$_MDMConfigurationCommonProperties
+ __OBJC_LABEL_PROTOCOL_$_MDMConfigurationProperties
+ __OBJC_METACLASS_RO_$_MDMConfigurationBase
+ __OBJC_METACLASS_RO_$_MDMUserConfiguration
+ __OBJC_PROTOCOL_$_MDMConfigurationCommonProperties
+ __OBJC_PROTOCOL_$_MDMConfigurationProperties
+ ___104-[MDMClientCore requestDeviceObliterationWithPreserveDataPlan:disallowProximitySetup:completionHandler:]_block_invoke
+ ___166-[MDMClientCore nagWithID:clientID:schedule:title:message:notificationTitle:notificationMessage:actionTitle:actionURL:dismissTitle:dismissURL:deadlineURL:completion:]_block_invoke
+ ___180-[MDMClientCore requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:]_block_invoke
+ ___25-[MDMConfiguration topic]_block_invoke
+ ___26-[MDMClientCore pushToken]_block_invoke.14
+ ___261+[MDMCheckInRequest _checkInRequestAtURL:identity:pinnedSecCertificateRefs:pinningRevocationCheckRequired:signMessage:isUserEnrollment:enrollmentID:topic:pushMagic:rmAccountID:messageType:requestDict:channelType:isCheckout:isShortTransaction:completionHandler:]_block_invoke
+ ___29-[MDMConfiguration personaID]_block_invoke
+ ___29-[MDMConfiguration pushMagic]_block_invoke
+ ___29-[MDMConfiguration serverURL]_block_invoke
+ ___30-[MDMConfiguration checkInURL]_block_invoke
+ ___31-[MDMConfiguration rmAccountID]_block_invoke
+ ___31-[MDMConfiguration signMessage]_block_invoke
+ ___31-[MDMConfigurationBase details]_block_invoke
+ ___32-[MDMConfiguration accessRights]_block_invoke
+ ___32-[MDMConfiguration enrollmentID]_block_invoke
+ ___32-[MDMConfiguration isADEProfile]_block_invoke
+ ___34-[MDMConfiguration enrollmentMode]_block_invoke
+ ___35-[MDMConfiguration easEnrollmentID]_block_invoke
+ ___35-[MDMConfiguration isProfileLocked]_block_invoke
+ ___36-[MDMConfiguration isUserEnrollment]_block_invoke
+ ___36-[MDMConfiguration organizationInfo]_block_invoke
+ ___37-[MDMClientCore touchWithCompletion:]_block_invoke.16
+ ___38-[MDMConfiguration serverCapabilities]_block_invoke
+ ___38-[MDMConfiguration supportUserChannel]_block_invoke
+ ___39+[MDMConfiguration sharedConfiguration]_block_invoke_2
+ ___39+[MDMConfiguration sharedConfiguration]_block_invoke_3
+ ___41-[MDMClientCore isAwaitingUserConfigured]_block_invoke.26
+ ___41-[MDMConfigurationBase lastPushTokenHash]_block_invoke
+ ___43+[MDMUserConfiguration sharedConfiguration]_block_invoke
+ ___44-[MDMClientCore preserveAppsWithCompletion:]_block_invoke
+ ___45-[MDMConfiguration managingProfileIdentifier]_block_invoke
+ ___46-[MDMClientCore enablePushWakeWithCompletion:]_block_invoke
+ ___46-[MDMConfigurationBase refreshDetailsFromDisk]_block_invoke
+ ___47-[MDMClientCore _debug_stopNaggingForMigration]_block_invoke
+ ___47-[MDMClientCore disablePushWakeWithCompletion:]_block_invoke
+ ___48-[MDMClientCore blockMDMCommandsWithCompletion:]_block_invoke
+ ___50-[MDMClientCore unblockMDMCommandsWithCompletion:]_block_invoke
+ ___50-[MDMConfiguration pinningRevocationCheckRequired]_block_invoke
+ ___51-[MDMConfiguration checkInPinnedSecCertificateRefs]_block_invoke
+ ___51-[MDMConfigurationBase pushMagicMismatchDateMarker]_block_invoke
+ ___54-[MDMClientCore _debug_nagForMigrationWithCompletion:]_block_invoke
+ ___54-[MDMClientCore _queue_createAndStartMDMXPCConnection]_block_invoke.145
+ ___55-[MDMProvisioningProfileTrust untrustSignerIdentities:]_block_invoke
+ ___57-[MDMClientCore getOrgTokenForMAIDWithCompletionHandler:]_block_invoke
+ ___57-[MDMClientCore removeUnusedPreservedAppsWithCompletion:]_block_invoke
+ ___59+[MDMProvisioningProfileTrust manualTrustSignerIdentities:]_block_invoke
+ ___60+[MDMConfiguration getOrgTokenForMAIDWithCompletionHandler:]_block_invoke
+ ___60-[MDMConfigurationBase getPropertyForKey:channelType:error:]_block_invoke
+ ___61-[MDMClientCore sendMDMCheckOutRequestWithCompletionHandler:]_block_invoke
+ ___63-[MDMConfigurationBase removeMDMConfigurationForChannel:error:]_block_invoke
+ ___66-[MDMConfigurationBase setPropertyForKey:value:channelType:error:]_block_invoke
+ ___67-[MDMClientCore sendMDMAuthenticationRequestWithCompletionHandler:]_block_invoke
+ ___68-[MDMClientCore syncBootstrapTokenToMDMWithToken:completionHandler:]_block_invoke
+ ___70-[MDMClientCore requestRRTSCheckInAndValidationWithCompletionHandler:]_block_invoke
+ ___76-[MDMClientCore generateBootstrapTokenWithDevicePasscode:completionHandler:]_block_invoke
+ ___77-[MDMClientCore evaluateMigrationStatusWithPollFromServer:completionHandler:]_block_invoke
+ ___80-[MDMClientCore deleteBootstrapTokenWithToken:devicePasscode:completionHandler:]_block_invoke
+ ___88-[MDMClientCore getWatchPairingTokenForPhoneID:watchID:securityToken:completionHandler:]_block_invoke
+ ___90-[MDMConfigurationBase updateMDMConfigurationForChannel:createIfNeeded:error:updateBlock:]_block_invoke
+ ___91+[MDMConfiguration getWatchPairingTokenForPhoneID:watchID:securityToken:completionHandler:]_block_invoke
+ ___96+[MDMDeclarativeManagement executeRequestForEndpoint:channelType:requestData:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSData"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e57_v32?0"MDMHTTPTransaction"8"NSDictionary"16"NSError"24ls32l8
+ ___block_descriptor_40_e8_32s_e22_v24?0^v8"NSString"16ls32l8
+ ___block_descriptor_48_e8_32s40s_e21_v16?0^{__CFString=}8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e30_v24?0"NSString"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_65_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_72_e8_32s40s48r56r_e5_v8?0ls32l8r48l8r56l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8r56l8s48l8r64l8
+ ___block_literal_global.18
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _kCCIgnoreMDMFromBackupKey
+ _kCCMDMMigrationDeadlineKey
+ _kMDMActivityIdleTimeout
+ _kMDMBootstrapTokenCapability
+ _kMDMBootstrapTokenKey
+ _kMDMEndMigrationSuccessStatuskey
+ _kMDMMessageTypeGetBootstrapToken
+ _kMDMMessageTypeRRTS
+ _kMDMMessageTypeSetBootstrapToken
+ _kMDMSettingsURLMDMMigration
+ _kMDMSettingsURLProfilesUI
+ _objc_msgSend$_checkInRequestAtURL:identity:pinnedSecCertificateRefs:pinningRevocationCheckRequired:signMessage:isUserEnrollment:enrollmentID:topic:pushMagic:rmAccountID:messageType:requestDict:channelType:isCheckout:isShortTransaction:completionHandler:
+ _objc_msgSend$_failedToConvertTokenDataError
+ _objc_msgSend$_mdmFilePathForChannelType:
+ _objc_msgSend$_memberQueueReadPropertiesForChannelType:createIfMissingFile:error:
+ _objc_msgSend$_memberQueueWriteProperties:channelType:error:
+ _objc_msgSend$_requestDataWithRequestDict:enrollmentID:topic:pushMagic:isUserEnrollment:messageType:channelType:error:
+ _objc_msgSend$_userFieldsForRequest
+ _objc_msgSend$appSignerIdentityForBundleID:
+ _objc_msgSend$blockMDMCommandsWithCompletion:
+ _objc_msgSend$checkInPinnedSecCertificateRefs
+ _objc_msgSend$checkInURL
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$deleteBootstrapTokenWithToken:devicePasscode:completionHandler:
+ _objc_msgSend$disablePushWakeWithCompletion:
+ _objc_msgSend$enablePushWakeWithCompletion:
+ _objc_msgSend$evaluateMigrationStatusWithPollFromServer:completionHandler:
+ _objc_msgSend$executeRequestForMessageType:channelType:requestDict:isCheckout:shouldIncludeTopic:shouldIncludePushMagic:isEnrollmentRequired:isShortTransaction:completionHandler:
+ _objc_msgSend$generateBootstrapTokenWithDevicePasscode:completionHandler:
+ _objc_msgSend$getOrgTokenForMAIDWithCompletionHandler:
+ _objc_msgSend$getPropertyForKey:channelType:error:
+ _objc_msgSend$getPropertyForKey:error:
+ _objc_msgSend$getWatchPairingTokenForPhoneID:watchID:securityToken:completionHandler:
+ _objc_msgSend$isoDateFormatter
+ _objc_msgSend$managingProfileIdentifier
+ _objc_msgSend$memberQueueAccessRights
+ _objc_msgSend$memberQueueEASEnrollmentID
+ _objc_msgSend$memberQueueEnrollmentID
+ _objc_msgSend$memberQueueEnrollmentMode
+ _objc_msgSend$memberQueueIdentityPersistentID
+ _objc_msgSend$memberQueueIsADEProfile
+ _objc_msgSend$memberQueueIsProfileLocked
+ _objc_msgSend$memberQueueIsUserEnrollment
+ _objc_msgSend$memberQueueLastPushTokenHash
+ _objc_msgSend$memberQueueMDMDictionary
+ _objc_msgSend$memberQueuePersonaID
+ _objc_msgSend$memberQueuePushMagicMismatchDateMarker
+ _objc_msgSend$memberQueueRMAccountID
+ _objc_msgSend$memberQueueReadConfigurationOutError:
+ _objc_msgSend$memberQueueSupportUserChannel
+ _objc_msgSend$nagForMigrationWithHardCodedValuesWithCompletion:
+ _objc_msgSend$nagWithID:clientID:schedule:title:message:notificationTitle:notificationMessage:actionTitle:actionURL:dismissTitle:dismissURL:deadlineURL:completion:
+ _objc_msgSend$pinningRevocationCheckRequired
+ _objc_msgSend$preserveAppsWithCompletion:
+ _objc_msgSend$profileIsForLocalProvisioning:
+ _objc_msgSend$profileProvisionsAllDevices:
+ _objc_msgSend$pushMagic
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$removeMDMConfigurationForChannel:error:
+ _objc_msgSend$removeUnusedPreservedAppsWithCompletion:
+ _objc_msgSend$requestDeviceObliterationWithPreserveDataPlan:disallowProximitySetup:completionHandler:
+ _objc_msgSend$requestRRTSCheckInAndValidationWithCompletionHandler:
+ _objc_msgSend$requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:
+ _objc_msgSend$retrieveMDMDictionaryWithError:
+ _objc_msgSend$sendMDMAuthenticationRequestWithCompletionHandler:
+ _objc_msgSend$sendMDMCheckOutRequestWithCompletionHandler:
+ _objc_msgSend$setMemberQueueEASEnrollmentID:
+ _objc_msgSend$setMemberQueueEnrollmentID:
+ _objc_msgSend$setMemberQueueEnrollmentMode:
+ _objc_msgSend$setMemberQueueIdentityPersistentID:
+ _objc_msgSend$setMemberQueueIsADEProfile:
+ _objc_msgSend$setMemberQueueIsProfileLocked:
+ _objc_msgSend$setMemberQueueIsUserEnrollment:
+ _objc_msgSend$setMemberQueueLastPushTokenHash:
+ _objc_msgSend$setMemberQueueMDMDictionary:
+ _objc_msgSend$setMemberQueuePersonaID:
+ _objc_msgSend$setMemberQueuePushMagicMismatchDateMarker:
+ _objc_msgSend$setMemberQueueRMAccountID:
+ _objc_msgSend$setMemberQueueSupportUserChannel:
+ _objc_msgSend$setPropertyForKey:value:channelType:error:
+ _objc_msgSend$setPropertyForKey:value:error:
+ _objc_msgSend$sharedClient
+ _objc_msgSend$signMessage
+ _objc_msgSend$stopNaggingForMigrationWithCompletion:
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$syncBootstrapTokenToMDMWithToken:completionHandler:
+ _objc_msgSend$teamIDWithProfileUUID:
+ _objc_msgSend$teamIDsWithSigningIdentity:
+ _objc_msgSend$topic
+ _objc_msgSend$unblockMDMCommandsWithCompletion:
+ _objc_msgSend$untrustProvisioningProfileUUID:
+ _objc_msgSend$untrustSignerIdentities:
+ _objc_msgSend$updateMDMConfigurationForChannel:createIfNeeded:error:updateBlock:
+ _objc_msgSend$updateMDMConfigurationWithCreateIfNeeded:updateBlock:error:
- +[MDMCheckInRequest _createUnsupportedFeatureError]
- +[MDMConfiguration _emptyTokenErrorWithUnderlayingError:]
- +[MDMConfiguration getTokenUnsupportedError]
- +[MDMConfiguration getWatchPairingTokenForPhoneID:watchID:securityToken:outError:]
- +[MDMConfiguration isGetTokenSupportedByServer]
- +[MDMDeclarativeManagement _createUnsupportedFeatureError]
- +[MDMProvisioningProfileTrust _appSignerIdentityForBundleID:]
- +[MDMProvisioningProfileTrust _untrustProvisioningProfileUUID:]
- +[MDMProvisioningProfileTrust didEnrollInMDMWithPasscode:duringMigration:]
- +[MDMProvisioningProfileTrust didUnenrollFromMDM]
- -[MDMClientConcreteDataProvider mdmDictionary]
- -[MDMClientCore _deviceEnrollmentAuthenticationDict]
- -[MDMClientCore _userEnrollmentAuthenticationDictWithEnrollmentID:]
- -[MDMClientCore _userFieldsForResponse]
- -[MDMClientCore accessRights]
- -[MDMClientCore authenticateWithCheckInURL:identity:pinnedSecCertificateRefs:pinningRevocationCheckRequired:topic:useDevelopmentAPNS:signMessage:isUserEnrollment:enrollmentID:outError:]
- -[MDMClientCore checkInRequestAtURL:identity:pinnedSecCertificateRefs:pinningRevocationCheckRequired:signMessage:isUserEnrollment:enrollmentID:messageType:requestDict:outResponse:outError:]
- -[MDMClientCore checkOutCheckInURL:identity:pinnedSecCertificateRefs:pinningRevocationCheckRequired:topic:signMessage:isUserEnrollment:enrollmentID:outError:]
- -[MDMClientCore dataProvider]
- -[MDMClientCore initWithChannelType:dataProvider:]
- -[MDMClientCore isActivationLockAllowedWhileSupervised]
- -[MDMClientCore remoteManagementCheckInURL:identity:pinnedSecCertificateRefs:pinningRevocationCheckRequired:signMessage:isUserEnrollment:enrollmentID:endpoint:requestData:outResponse:outError:]
- -[MDMClientCore setDataProvider:]
- -[MDMConfiguration _mdmPropertiesFilePathForChannelType:]
- -[MDMConfiguration _readPropertiesForChannelType:createIfMissingFile:error:]
- -[MDMConfiguration _writeProperties:channelType:error:]
- -[MDMConfiguration getPropertyForKey:channelType:]
- -[MDMConfiguration identityPersistentID]
- -[MDMConfiguration init]
- -[MDMConfiguration memberQueue]
- -[MDMConfiguration readConfigurationOutError:]
- -[MDMConfiguration refreshDetailsFromDisk]
- -[MDMConfiguration setEasEnrollmentID:]
- -[MDMConfiguration setEnrollmentID:]
- -[MDMConfiguration setEnrollmentMode:]
- -[MDMConfiguration setIdentityPersistentID:]
- -[MDMConfiguration setIsUserEnrollment:]
- -[MDMConfiguration setMemberQueue:]
- -[MDMConfiguration setPersonaID:]
- -[MDMConfiguration setPropertyForKey:value:channelType:]
- -[MDMConfiguration setRmAccountID:]
- -[MDMConfiguration setSupportUserChannel:]
- GCC_except_table5
- GCC_except_table58
- GCC_except_table66
- GCC_except_table70
- _DMCCTIMEI
- _DMCCTMEID
- _DMCEventsTopicOrgToken
- _DMCIOSerialString
- _OBJC_CLASS_$_DMCEvents
- _OBJC_CLASS_$_MDMClientConcreteDataProvider
- _OBJC_IVAR_$_MDMClientCore._dataProvider
- _OBJC_IVAR_$_MDMConfiguration._easEnrollmentID
- _OBJC_IVAR_$_MDMConfiguration._enrollmentID
- _OBJC_IVAR_$_MDMConfiguration._enrollmentMode
- _OBJC_IVAR_$_MDMConfiguration._identityPersistentID
- _OBJC_IVAR_$_MDMConfiguration._isProfileLocked
- _OBJC_IVAR_$_MDMConfiguration._isUserEnrollment
- _OBJC_IVAR_$_MDMConfiguration._memberQueue
- _OBJC_IVAR_$_MDMConfiguration._personaID
- _OBJC_IVAR_$_MDMConfiguration._rmAccountID
- _OBJC_IVAR_$_MDMConfiguration._supportUserChannel
- _OBJC_METACLASS_$_MDMClientConcreteDataProvider
- __OBJC_$_INSTANCE_METHODS_MDMClientConcreteDataProvider
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MDMClientDataProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_MDMClientDataProvider
- __OBJC_CLASS_PROTOCOLS_$_MDMClientConcreteDataProvider
- __OBJC_CLASS_RO_$_MDMClientConcreteDataProvider
- __OBJC_LABEL_PROTOCOL_$_MDMClientDataProvider
- __OBJC_METACLASS_RO_$_MDMClientConcreteDataProvider
- __OBJC_PROTOCOL_$_MDMClientDataProvider
- ___26-[MDMClientCore pushToken]_block_invoke.16
- ___37-[MDMClientCore touchWithCompletion:]_block_invoke.18
- ___41-[MDMClientCore isAwaitingUserConfigured]_block_invoke.36
- ___46-[MDMConfiguration readConfigurationOutError:]_block_invoke
- ___47+[MDMConfiguration isGetTokenSupportedByServer]_block_invoke
- ___49+[MDMProvisioningProfileTrust didUnenrollFromMDM]_block_invoke
- ___50-[MDMConfiguration getPropertyForKey:channelType:]_block_invoke
- ___54-[MDMClientCore _queue_createAndStartMDMXPCConnection]_block_invoke.128
- ___56-[MDMConfiguration setPropertyForKey:value:channelType:]_block_invoke
- ___82+[MDMConfiguration getWatchPairingTokenForPhoneID:watchID:securityToken:outError:]_block_invoke
- ___block_descriptor_40_e8_32s_e21_v16?0^{__CFString=}8ls32l8
- ___block_descriptor_48_e8_32r40r_e34_v24?0"NSDictionary"8"NSError"16lr32l8r40l8
- ___block_descriptor_56_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
- ___block_descriptor_64_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
- ___block_descriptor_72_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
- ___block_literal_global.15
- ___block_literal_global.27
- ___block_literal_global.29
- ___block_literal_global.31
- ___block_literal_global.33
- ___block_literal_global.35
- _kMDMPQuerySIMCarrierNetwork
- _objc_msgSend$DMCDictionaryFromFile:
- _objc_msgSend$DMCSetObjectIfNotNil:forKey:
- _objc_msgSend$_appSignerIdentityForBundleID:
- _objc_msgSend$_createUnsupportedFeatureError
- _objc_msgSend$_deviceEnrollmentAuthenticationDict
- _objc_msgSend$_emptyTokenErrorWithUnderlayingError:
- _objc_msgSend$_readPropertiesForChannelType:createIfMissingFile:error:
- _objc_msgSend$_untrustProvisioningProfileUUID:
- _objc_msgSend$_userEnrollmentAuthenticationDictWithEnrollmentID:
- _objc_msgSend$_userFieldsForResponse
- _objc_msgSend$_writeProperties:channelType:error:
- _objc_msgSend$accessRights
- _objc_msgSend$allowedDeviceQueriesForAccessRights:isDataSeparated:
- _objc_msgSend$buildVersion
- _objc_msgSend$checkInRequestAtURL:identity:pinnedSecCertificateRefs:pinningRevocationCheckRequired:signMessage:isUserEnrollment:enrollmentID:messageType:requestDict:outResponse:outError:
- _objc_msgSend$clientWithChannelType:
- _objc_msgSend$dataProvider
- _objc_msgSend$defaultMDMOptions
- _objc_msgSend$dictionaryWithObject:forKey:
- _objc_msgSend$getPropertyForKey:channelType:
- _objc_msgSend$getTokenUnsupportedError
- _objc_msgSend$identityPersistentID
- _objc_msgSend$initWithChannelType:dataProvider:
- _objc_msgSend$integerValue
- _objc_msgSend$isGetTokenSupportedByServer
- _objc_msgSend$logErrorEventForTopic:reason:error:details:
- _objc_msgSend$marketingVersion
- _objc_msgSend$mdmDictionary
- _objc_msgSend$performSynchronously
- _objc_msgSend$productNameWithDefaultValue:
- _objc_msgSend$productType
- _objc_msgSend$readConfigurationOutError:
- _objc_msgSend$remoteManagementCheckInURL:identity:pinnedSecCertificateRefs:pinningRevocationCheckRequired:signMessage:isUserEnrollment:enrollmentID:endpoint:requestData:outResponse:outError:
- _objc_msgSend$setEasEnrollmentID:
- _objc_msgSend$setEnrollmentID:
- _objc_msgSend$setEnrollmentMode:
- _objc_msgSend$setIdentityPersistentID:
- _objc_msgSend$setIsUserEnrollment:
- _objc_msgSend$setPersonaID:
- _objc_msgSend$setPropertyForKey:value:channelType:
- _objc_msgSend$setSupportUserChannel:
- _objc_retain_x9
CStrings:
+ "%@ member queue"
+ "%s Failed to get wallpaper config UUID with error: %{public}@"
+ "%s Failed to set wallpaper config UUID with error: %{public}@"
+ "-[MDMConfiguration(Wallpaper) setWallpaperConfigurationUUID:]"
+ "-[MDMConfiguration(Wallpaper) wallpaperConfigurationUUID]"
+ "@\"NSData\"16@0:8"
+ "@\"NSDate\""
+ "@\"NSDate\"16@0:8"
+ "@\"NSURL\"16@0:8"
+ "@40@0:8@16Q24^@32"
+ "@76@0:8@16@24@32@40B48@52Q60^@68"
+ "B32@0:8@?16^@24"
+ "B32@0:8Q16^@24"
+ "B36@0:8B16@?20^@28"
+ "B40@0:8@16@24^@32"
+ "B44@0:8Q16B24^@28@?36"
+ "B48@0:8@16@24Q32^@40"
+ "BootstrapToken"
+ "Calling executeRequestForMessageType - channel type: %lu"
+ "CheckIn Request failed with error: %{public}@"
+ "CheckIn Request finished with status: %ld"
+ "Could not register for MDM file change notification."
+ "DMC_SERVER_RESPONSE_INVALID_TOKEN_VALUE"
+ "Error in _debug_nagForMigrationWithCompletion XPC reply. Error: %{public}@"
+ "Error in _debug_stopNaggingForMigration XPC reply. Error: %{public}@"
+ "Error in preserveApps XPC reply. Error: %{public}@. Not attempting a retry."
+ "Error in removeUnusedPreservedAppsWithCompletion XPC reply. Error: %{public}@. Not attempting a retry."
+ "Failed to create MDM directory: %{public}@"
+ "Failed to read MDM.plist with error: %{public}@"
+ "Failed to remove MDM.plist at path %{public}@ with error: %{public}@"
+ "Failed to save MDM.plist file"
+ "Failed to save MDM.plist to filePath: %{public}@"
+ "GetBootstrapToken"
+ "IdleTimeout"
+ "MDM.plist file doesn't exist"
+ "MDMCheckInRequest: Creating request data with dictionary with keys: %{public}@"
+ "MDMClientCore XPC failed to nag with error: %{public}@"
+ "MDMConfiguration: Failed to get Watch pairing token with error: %{public}@"
+ "MDMConfiguration: Failed to get org token with error: %{public}@"
+ "MDMConfiguration: Forgetting Current Configuration!"
+ "MDMConfiguration: getWatchPairingTokenForPhoneID finished"
+ "MDMConfiguration: memberQueueReadConfigurationOutError:"
+ "MDMConfiguration: memberQueueReadConfigurationOutError: Invalid MDM installation found. Error: %{public}@"
+ "MDMConfiguration: memberQueueReadConfigurationOutError: Valid MDM installation found."
+ "MDMConfiguration: memberQueueReadConfigurationOutError: doneblock"
+ "MDMConfiguration: memberQueueReadConfigurationOutError: doneblock: Configuration not valid!"
+ "MDMConfigurationBase"
+ "MDMConfigurationBase: Forgetting Current Configuration!"
+ "MDMConfigurationBase: getPropertyForKey: %{public}@ value: %{public}@"
+ "MDMConfigurationBase: getPropertyForKey: cannot get property without plist"
+ "MDMConfigurationBase: memberQueueReadConfigurationOutError:"
+ "MDMConfigurationBase: memberQueueReadConfigurationOutError: Invalid MDM installation found. Error: %{public}@"
+ "MDMConfigurationBase: memberQueueReadConfigurationOutError: No MDM installation found!"
+ "MDMConfigurationBase: memberQueueReadConfigurationOutError: Valid MDM installation found."
+ "MDMConfigurationBase: memberQueueReadConfigurationOutError: doneblock"
+ "MDMConfigurationBase: memberQueueReadConfigurationOutError: doneblock: Configuration not valid!"
+ "MDMConfigurationBase: setPropertyForKey: %{public}@ value: %{public}@"
+ "MDMConfigurationBase: setPropertyForKey: cannot set property for key %{public}@. Error: %{public}@"
+ "MDMConfigurationBase: setPropertyForKey: failed to write plist"
+ "MDMConfigurationCommonProperties"
+ "MDMConfigurationProperties"
+ "MDMProvisioningProfileTrust failed to manually trust signer identities: %{public}@"
+ "MDMProvisioningProfileTrust ignoring MDM trust because we are unenrolling from MDM"
+ "MDMProvisioningProfileTrust skipping non-orphaned profile UUID %{public}@ because it is trusted by Team ID: %{public}@"
+ "MDMUserConfiguration"
+ "ReturnToService"
+ "Sending MDM file changed notification."
+ "Sending skip key changed notification."
+ "SetBootstrapToken"
+ "T@\"NSArray\",R"
+ "T@\"NSData\",&,N,V_memberQueueIdentityPersistentID"
+ "T@\"NSData\",&,N,V_memberQueueLastPushTokenHash"
+ "T@\"NSData\",R"
+ "T@\"NSDate\",&,N,V_memberQueuePushMagicMismatchDateMarker"
+ "T@\"NSDate\",R"
+ "T@\"NSDictionary\",&,N,V_memberQueueMDMDictionary"
+ "T@\"NSDictionary\",R"
+ "T@\"NSString\",&,N,V_memberQueueEASEnrollmentID"
+ "T@\"NSString\",&,N,V_memberQueueEnrollmentID"
+ "T@\"NSString\",&,N,V_memberQueueEnrollmentMode"
+ "T@\"NSString\",&,N,V_memberQueuePersonaID"
+ "T@\"NSString\",&,N,V_memberQueueRMAccountID"
+ "T@\"NSURL\",R"
+ "TB,N,V_isUnenrollingFromMDM"
+ "TB,N,V_memberQueueIsADEProfile"
+ "TB,N,V_memberQueueIsProfileLocked"
+ "TB,N,V_memberQueueIsUserEnrollment"
+ "TB,N,V_memberQueueSupportUserChannel"
+ "_checkInRequestAtURL:identity:pinnedSecCertificateRefs:pinningRevocationCheckRequired:signMessage:isUserEnrollment:enrollmentID:topic:pushMagic:rmAccountID:messageType:requestDict:channelType:isCheckout:isShortTransaction:completionHandler:"
+ "_debug_nagForMigrationWithCompletion:"
+ "_debug_stopNaggingForMigration"
+ "_failedToConvertTokenDataError"
+ "_isUnenrollingFromMDM"
+ "_mdmFilePathForChannelType:"
+ "_memberQueueEASEnrollmentID"
+ "_memberQueueEnrollmentID"
+ "_memberQueueEnrollmentMode"
+ "_memberQueueIdentityPersistentID"
+ "_memberQueueIsADEProfile"
+ "_memberQueueIsProfileLocked"
+ "_memberQueueIsUserEnrollment"
+ "_memberQueueLastPushTokenHash"
+ "_memberQueueMDMDictionary"
+ "_memberQueuePersonaID"
+ "_memberQueuePushMagicMismatchDateMarker"
+ "_memberQueueRMAccountID"
+ "_memberQueueReadPropertiesForChannelType:createIfMissingFile:error:"
+ "_memberQueueSupportUserChannel"
+ "_memberQueueWriteProperties:channelType:error:"
+ "_requestDataWithRequestDict:enrollmentID:topic:pushMagic:isUserEnrollment:messageType:channelType:error:"
+ "_userFieldsForRequest"
+ "appSignerIdentityForBundleID:"
+ "blockMDMCommandsWithCompletion:"
+ "checkInPinnedSecCertificateRefs"
+ "checkInURL"
+ "com.apple.devicemanagementclient.mdmFileChanged"
+ "com.apple.devicemanagementclient.skipKeyChanged"
+ "com.apple.mdm.bootstraptoken"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "deleteBootstrapTokenWithToken:devicePasscode:completionHandler:"
+ "disablePushWakeWithCompletion:"
+ "enablePushWakeWithCompletion:"
+ "evaluateMigrationStatusWithPollFromServer:completionHandler:"
+ "executeRequestForMessageType:channelType:requestDict:isCheckout:shouldIncludeTopic:shouldIncludePushMagic:isEnrollmentRequired:isShortTransaction:completionHandler:"
+ "generateBootstrapTokenWithDevicePasscode:completionHandler:"
+ "getOrgTokenForMAIDWithCompletionHandler:"
+ "getPropertyForKey:channelType:error:"
+ "getPropertyForKey:error:"
+ "getWatchPairingTokenForPhoneID:watchID:securityToken:completionHandler:"
+ "isADEProfile"
+ "isUnenrollingFromMDM"
+ "isoDateFormatter"
+ "lastPushTokenHash"
+ "managingProfileIdentifier"
+ "manualTrustSignerIdentities:"
+ "memberQueueEASEnrollmentID"
+ "memberQueueEnrollmentID"
+ "memberQueueEnrollmentMode"
+ "memberQueueIdentityPersistentID"
+ "memberQueueIsADEProfile"
+ "memberQueueIsProfileLocked"
+ "memberQueueIsUserEnrollment"
+ "memberQueueLastPushTokenHash"
+ "memberQueueMDMDictionary"
+ "memberQueuePersonaID"
+ "memberQueuePushMagicMismatchDateMarker"
+ "memberQueueRMAccountID"
+ "memberQueueReadConfigurationOutError:"
+ "memberQueueSupportUserChannel"
+ "migrationDeadline"
+ "nagForMigrationWithHardCodedValuesWithCompletion:"
+ "nagWithID:clientID:schedule:title:message:notificationTitle:notificationMessage:actionTitle:actionURL:dismissTitle:dismissURL:deadlineURL:completion:"
+ "organizationInfo"
+ "pinningRevocationCheckRequired"
+ "preserveAppsWithCompletion:"
+ "profileIsForLocalProvisioning:"
+ "profileProvisionsAllDevices:"
+ "pushMagic"
+ "pushMagicMismatchDateMarker"
+ "removeItemAtPath:error:"
+ "removeMDMConfigurationForChannel:error:"
+ "removeMDMConfigurationWithError:"
+ "removeUnusedPreservedAppsWithCompletion:"
+ "requestDeviceObliterationWithPreserveDataPlan:disallowProximitySetup:completionHandler:"
+ "requestRRTSCheckInAndValidationWithCompletionHandler:"
+ "requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:"
+ "retrieveMDMDictionaryWithError:"
+ "sendMDMAuthenticationRequestWithCompletionHandler:"
+ "sendMDMCheckOutRequestWithCompletionHandler:"
+ "serverCapabilities"
+ "serverURL"
+ "setIsUnenrollingFromMDM:"
+ "setMemberQueueEASEnrollmentID:"
+ "setMemberQueueEnrollmentID:"
+ "setMemberQueueEnrollmentMode:"
+ "setMemberQueueIdentityPersistentID:"
+ "setMemberQueueIsADEProfile:"
+ "setMemberQueueIsProfileLocked:"
+ "setMemberQueueIsUserEnrollment:"
+ "setMemberQueueLastPushTokenHash:"
+ "setMemberQueueMDMDictionary:"
+ "setMemberQueuePersonaID:"
+ "setMemberQueuePushMagicMismatchDateMarker:"
+ "setMemberQueueRMAccountID:"
+ "setMemberQueueSupportUserChannel:"
+ "setPropertyForKey:value:channelType:error:"
+ "setPropertyForKey:value:error:"
+ "settings-navigation://com.apple.Settings.General/ManagedConfigurationList"
+ "settings-navigation://com.apple.Settings.General/ManagedConfigurationList/MDMMigration"
+ "sharedConfigurationForChannel:"
+ "shouldIgnoreMDMFromBackup"
+ "signMessage"
+ "stopNaggingForMigrationWithCompletion:"
+ "stringByDeletingLastPathComponent"
+ "success"
+ "syncBootstrapTokenToMDMWithToken:completionHandler:"
+ "teamIDWithProfileUUID:"
+ "teamIDsWithSigningIdentity:"
+ "topic"
+ "unblockMDMCommandsWithCompletion:"
+ "untrustProvisioningProfileUUID:"
+ "untrustSignerIdentities:"
+ "updateMDMConfigurationForChannel:createIfNeeded:error:updateBlock:"
+ "updateMDMConfigurationWithCreateIfNeeded:updateBlock:error:"
+ "updateMDMConfigurationWithUpdateBlock:error:"
+ "v120@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"NSURL\"80@\"NSString\"88@\"NSURL\"96@\"NSURL\"104@?<v@?@\"NSError\">112"
+ "v120@0:8@16@24@32@40@48@56@64@72@80@88@96@104@?112"
+ "v124@0:8@16^{__SecIdentity=}24@32B40B44B48@52@60@68@76@84@92Q100B108B112@?116"
+ "v24@0:8@?<v@?@\"NSData\"@\"NSData\"@\"NSData\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSString\"@\"NSError\">16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?B@\"NSError\">20"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
+ "v32@0:8B16B20@?24"
+ "v32@0:8B16B20@?<v@?@\"NSError\">24"
+ "v32@?0@\"MDMHTTPTransaction\"8@\"NSDictionary\"16@\"NSError\"24"
+ "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSError\">32"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSError\">40"
+ "v64@0:8B16B20@\"NSData\"24@\"NSData\"32@\"NSString\"40@\"NSData\"48@?<v@?@\"NSError\">56"
+ "v64@0:8B16B20@24@32@40@48@?56"
+ "v68@0:8@16Q24@32B40B44B48B52B56@?60"
- "@\"<MDMClientDataProvider>\""
- "@\"NSData\"48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32^@40"
- "@32@0:8@16Q24"
- "@32@0:8Q16@24"
- "@40@0:8@16@24Q32"
- "@48@0:8@16@24@32^@40"
- "Authenticating with MDM"
- "Authentication with MDM finished."
- "B76@0:8@16^{__SecIdentity=}24@32B40@44B52B56@60^@68"
- "B80@0:8@16^{__SecIdentity=}24@32B40@44B52B56B60@64^@72"
- "B92@0:8@16^{__SecIdentity=}24@32B40B44B48@52@60@68^@76^@84"
- "Calling remoteManagementCheckInURL - channel type: %lu"
- "Cannot Authenticate. Error: %{public}@"
- "Cannot Check Out. Error: %{public}@"
- "Check out finished."
- "Checking out of MDM service"
- "Could Not Check In for MessageType: %{public}@ with Error: %{public}@"
- "DMCDictionaryFromFile:"
- "DMCSetObjectIfNotNil:forKey:"
- "DMC_SERVER_RESPONSE_EMPTY_TOKEN_VALUE"
- "Failed to get org token"
- "Finished running CheckIn Request on MDM service"
- "MDMClientConcreteDataProvider"
- "MDMClientDataProvider"
- "MDMConfiguration member queue"
- "MDMConfiguration: Forgetting Current APNS Config, clearing push topics!"
- "MDMConfiguration: GetToken request not supported by MDM server"
- "MDMConfiguration: Org Token request failed with Non 200 response from the server. Response code: %ld Error: %{public}@"
- "MDMConfiguration: Pairing Token request failed with Non 200 response from the server. Response code: %ld Error: %{public}@"
- "MDMConfiguration: TokenData for pairing is empty in response dict from request, with error: %{public}@"
- "MDMConfiguration: TokenData for pairing was received with accompanying error: %{public}@"
- "MDMConfiguration: TokenData is empty in response dict from request, with error: %{public}@"
- "MDMConfiguration: TokenData was received with accompanying error: %{public}@"
- "MDMConfiguration: getPropertyForKey: %{public}@ value: %{public}@"
- "MDMConfiguration: getPropertyForKey: cannot get property without plist"
- "MDMConfiguration: readConfigurationOutError:"
- "MDMConfiguration: readConfigurationOutError: Invalid MDM installation found. Error: %{public}@"
- "MDMConfiguration: readConfigurationOutError: No MDM installation found!"
- "MDMConfiguration: readConfigurationOutError: Valid MDM installation found."
- "MDMConfiguration: readConfigurationOutError: doneblock"
- "MDMConfiguration: readConfigurationOutError: doneblock: Configuration not valid!"
- "MDMConfiguration: setPropertyForKey: %{public}@ value: %{public}@"
- "MDMConfiguration: setPropertyForKey: cannot set property for key %{public}@. Error: %{public}@"
- "MDMConfiguration: setPropertyForKey: failed to write plist"
- "SIMCarrierNetwork"
- "T@\"<MDMClientDataProvider>\",&,N,V_dataProvider"
- "T@\"NSData\",&,N,V_identityPersistentID"
- "T@\"NSString\",&,N,V_easEnrollmentID"
- "T@\"NSString\",&,N,V_enrollmentID"
- "T@\"NSString\",&,N,V_enrollmentMode"
- "T@\"NSString\",&,N,V_personaID"
- "TB,N,V_isUserEnrollment"
- "TB,N,V_supportUserChannel"
- "TB,R,V_isProfileLocked"
- "This checkin channel does not support the messageType: %{public}@"
- "UNSUPPORTED_FEATURE"
- "_appSignerIdentityForBundleID:"
- "_createUnsupportedFeatureError"
- "_dataProvider"
- "_deviceEnrollmentAuthenticationDict"
- "_easEnrollmentID"
- "_emptyTokenErrorWithUnderlayingError:"
- "_enrollmentID"
- "_enrollmentMode"
- "_identityPersistentID"
- "_isProfileLocked"
- "_isUserEnrollment"
- "_readPropertiesForChannelType:createIfMissingFile:error:"
- "_supportUserChannel"
- "_untrustProvisioningProfileUUID:"
- "_userEnrollmentAuthenticationDictWithEnrollmentID:"
- "_userFieldsForResponse"
- "_writeProperties:channelType:error:"
- "authenticateWithCheckInURL:identity:pinnedSecCertificateRefs:pinningRevocationCheckRequired:topic:useDevelopmentAPNS:signMessage:isUserEnrollment:enrollmentID:outError:"
- "buildVersion"
- "checkInRequestAtURL:identity:pinnedSecCertificateRefs:pinningRevocationCheckRequired:signMessage:isUserEnrollment:enrollmentID:messageType:requestDict:outResponse:outError:"
- "checkOutCheckInURL:identity:pinnedSecCertificateRefs:pinningRevocationCheckRequired:topic:signMessage:isUserEnrollment:enrollmentID:outError:"
- "dataProvider"
- "dictionaryWithObject:forKey:"
- "getPropertyForKey:channelType:"
- "getTokenUnsupportedError"
- "getWatchPairingTokenForPhoneID:watchID:securityToken:outError:"
- "identityPersistentID"
- "initWithChannelType:dataProvider:"
- "integerValue"
- "isActivationLockAllowedWhileSupervised"
- "isGetTokenSupportedByServer"
- "logErrorEventForTopic:reason:error:details:"
- "marketingVersion"
- "mdmDictionary"
- "performSynchronously"
- "productNameWithDefaultValue:"
- "productType"
- "readConfigurationOutError:"
- "remoteManagementCheckInURL:identity:pinnedSecCertificateRefs:pinningRevocationCheckRequired:signMessage:isUserEnrollment:enrollmentID:endpoint:requestData:outResponse:outError:"
- "setDataProvider:"
- "setEasEnrollmentID:"
- "setEnrollmentID:"
- "setEnrollmentMode:"
- "setIdentityPersistentID:"
- "setIsUserEnrollment:"
- "setPropertyForKey:value:channelType:"
- "setSupportUserChannel:"

```
