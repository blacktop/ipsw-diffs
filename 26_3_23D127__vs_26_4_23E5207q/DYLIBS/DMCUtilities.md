## DMCUtilities

> `/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities`

```diff

-55.80.4.0.0
-  __TEXT.__text: 0x34844
-  __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_methlist: 0x2df4
-  __TEXT.__const: 0x158
-  __TEXT.__gcc_except_tab: 0x7c4
-  __TEXT.__cstring: 0x3669
-  __TEXT.__oslogstring: 0x51e7
+59.100.16.0.0
+  __TEXT.__text: 0x38660
+  __TEXT.__auth_stubs: 0xe90
+  __TEXT.__objc_methlist: 0x2ecc
+  __TEXT.__const: 0x178
+  __TEXT.__gcc_except_tab: 0x810
+  __TEXT.__cstring: 0x3774
+  __TEXT.__oslogstring: 0x549e
   __TEXT.__dlopen_cstrs: 0x165
-  __TEXT.__unwind_info: 0xde8
+  __TEXT.__unwind_info: 0xe40
   __TEXT.__objc_classname: 0x4b9
-  __TEXT.__objc_methname: 0x9b4f
-  __TEXT.__objc_methtype: 0x1355
-  __TEXT.__objc_stubs: 0x62a0
+  __TEXT.__objc_methname: 0x9f09
+  __TEXT.__objc_methtype: 0x13b2
+  __TEXT.__objc_stubs: 0x64a0
   __DATA_CONST.__got: 0x6b0
-  __DATA_CONST.__const: 0x11e8
+  __DATA_CONST.__const: 0x12c0
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2578
+  __DATA_CONST.__objc_selrefs: 0x2618
   __DATA_CONST.__objc_superrefs: 0xc8
-  __AUTH_CONST.__auth_got: 0x778
-  __AUTH_CONST.__const: 0xc80
-  __AUTH_CONST.__cfstring: 0x3fc0
-  __AUTH_CONST.__objc_const: 0x43b0
+  __AUTH_CONST.__auth_got: 0x758
+  __AUTH_CONST.__const: 0xcc0
+  __AUTH_CONST.__cfstring: 0x4100
+  __AUTH_CONST.__objc_const: 0x4410
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH.__objc_data: 0xf00
-  __DATA.__objc_ivar: 0x210
+  __DATA.__objc_ivar: 0x214
   __DATA.__data: 0x300
-  __DATA.__bss: 0x910
+  __DATA.__bss: 0x920
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 52A8E7C1-B779-393B-87C6-6B2E63DB76D6
-  Functions: 1380
-  Symbols:   5060
-  CStrings:  3251
+  UUID: 5D43D985-82CD-3E04-B8C8-71C926D344A3
+  Functions: 1412
+  Symbols:   5154
+  CStrings:  3316
 
Symbols:
+ +[DMCFeatureFlags isAuthenticatedTemporarySessionEnabled]
+ +[DMCFeatureFlags isDirectUserSwitchEnabled]
+ +[DMCMultiUserModeUtilities _deleteAllUsersOtherThanCurrent]
+ +[DMCMultiUserModeUtilities _provisionDeviceWithProvisionDict:error:]
+ +[DMCMultiUserModeUtilities _updateMultiUserConfigurationFileAtPath:key:value:changed:]
+ +[DMCMultiUserModeUtilities _updateMultiUserDeviceConfigurationFileWithKey:value:changed:]
+ +[DMCMultiUserModeUtilities _updateMultiUserUserConfigurationFileWithKey:value:changed:]
+ +[DMCMultiUserModeUtilities authenticatedTemporarySession]
+ +[DMCMultiUserModeUtilities configureNoQuotaSizeSharedDevice]
+ +[DMCMultiUserModeUtilities configureTemporarySessionOnly:useDynamicQuotaSize:restoreQuotaSizeWhenDisabled:directUserSwitch:authenticatedTemporarySession:preferenceDomain:]
+ +[DMCMultiUserModeUtilities deviceNeedsReprovision]
+ +[DMCMultiUserModeUtilities directUserSwitch]
+ +[DMCMultiUserModeUtilities reprovisionDeviceIfNeeded]
+ -[DMCAccountUtilities _signIniCloudAccountWithAuthenticationResult:personaID:baseViewController:forceInlinePresentation:outError:]
+ -[DMCAccountUtilities signInAccountsWithTypes:authenticationResult:personaID:canMakeAccountActive:baseViewController:forceInlinePresentation:completionHandler:]
+ -[DMCObliterationShelter _generatePerformanceDictionary]
+ -[DMCObliterationShelter _performanceDirectoryPath]
+ -[DMCObliterationShelter _performanceFilePath]
+ -[DMCObliterationShelter performanceDictionary]
+ -[DMCObliterationShelter setShouldRetryEnrollment:]
+ -[DMCObliterationShelter shouldRetryEnrollment]
+ -[DMCObliterationShelter trackEndTime]
+ -[DMCSnapshotUtilities hasSystemVolumeSnapshotWithName:]
+ GCC_except_table42
+ GCC_except_table7
+ _DMCMCInstallationErrorDomain
+ _DMCSendSessionTimeoutChangedNotification
+ _DMCSessionTimeoutChangedNotification
+ _MDMDatabasePerformanceStorageDirectory
+ _MDMDatabasePerformanceStorageDirectory.cold.1
+ _MDMDatabasePerformanceStorageDirectory.once
+ _MDMDatabasePerformanceStorageDirectory.str
+ _OBJC_IVAR_$_DMCObliterationShelter._shouldRetryEnrollment
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ ___130-[DMCAccountUtilities _signIniCloudAccountWithAuthenticationResult:personaID:baseViewController:forceInlinePresentation:outError:]_block_invoke
+ ___130-[DMCAccountUtilities _signIniCloudAccountWithAuthenticationResult:personaID:baseViewController:forceInlinePresentation:outError:]_block_invoke.21
+ ___160-[DMCAccountUtilities signInAccountsWithTypes:authenticationResult:personaID:canMakeAccountActive:baseViewController:forceInlinePresentation:completionHandler:]_block_invoke
+ ___172+[DMCMultiUserModeUtilities configureTemporarySessionOnly:useDynamicQuotaSize:restoreQuotaSizeWhenDisabled:directUserSwitch:authenticatedTemporarySession:preferenceDomain:]_block_invoke
+ ___172+[DMCMultiUserModeUtilities configureTemporarySessionOnly:useDynamicQuotaSize:restoreQuotaSizeWhenDisabled:directUserSwitch:authenticatedTemporarySession:preferenceDomain:]_block_invoke.57
+ ___172+[DMCMultiUserModeUtilities configureTemporarySessionOnly:useDynamicQuotaSize:restoreQuotaSizeWhenDisabled:directUserSwitch:authenticatedTemporarySession:preferenceDomain:]_block_invoke.60
+ ___172+[DMCMultiUserModeUtilities configureTemporarySessionOnly:useDynamicQuotaSize:restoreQuotaSizeWhenDisabled:directUserSwitch:authenticatedTemporarySession:preferenceDomain:]_block_invoke_2
+ ___172+[DMCMultiUserModeUtilities configureTemporarySessionOnly:useDynamicQuotaSize:restoreQuotaSizeWhenDisabled:directUserSwitch:authenticatedTemporarySession:preferenceDomain:]_block_invoke_2.59
+ ___172+[DMCMultiUserModeUtilities configureTemporarySessionOnly:useDynamicQuotaSize:restoreQuotaSizeWhenDisabled:directUserSwitch:authenticatedTemporarySession:preferenceDomain:]_block_invoke_3
+ ___56-[DMCSnapshotUtilities hasSystemVolumeSnapshotWithName:]_block_invoke
+ ___60+[DMCMultiUserModeUtilities _deleteAllUsersOtherThanCurrent]_block_invoke
+ ___69+[DMCMultiUserModeUtilities _provisionDeviceWithProvisionDict:error:]_block_invoke
+ ___MDMDatabasePerformanceStorageDirectory_block_invoke
+ ___block_descriptor_40_e5_B8?0l
+ ___block_descriptor_48_e5_B8?0l
+ ___block_descriptor_48_e8_32s40r_e8_B12?0i8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_56_e5_B8?0l
+ ___block_descriptor_73_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8s48l8r56l8r64l8
+ ___block_descriptor_82_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s72l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.232
+ ___block_literal_global.234
+ ___block_literal_global.245
+ ___block_literal_global.256
+ ___block_literal_global.258
+ ___block_literal_global.62
+ _fs_snapshot_list
+ _kDMCPerformanceDurationKey
+ _kDMCPerformanceEndKey
+ _kDMCPerformanceStartKey
+ _objc_msgSend$_deleteAllUsersOtherThanCurrent
+ _objc_msgSend$_generatePerformanceDictionary
+ _objc_msgSend$_performanceDirectoryPath
+ _objc_msgSend$_performanceFilePath
+ _objc_msgSend$_provisionDeviceWithProvisionDict:error:
+ _objc_msgSend$_signIniCloudAccountWithAuthenticationResult:personaID:baseViewController:forceInlinePresentation:outError:
+ _objc_msgSend$_updateMultiUserConfigurationFileAtPath:key:value:changed:
+ _objc_msgSend$_updateMultiUserDeviceConfigurationFileWithKey:value:changed:
+ _objc_msgSend$authenticatedTemporarySession
+ _objc_msgSend$configureNoQuotaSizeSharedDevice
+ _objc_msgSend$deleteUser:completionHandler:
+ _objc_msgSend$deviceNeedsReprovision
+ _objc_msgSend$directUserSwitch
+ _objc_msgSend$isAuthenticatedTemporarySessionEnabled
+ _objc_msgSend$isDirectUserSwitchEnabled
+ _objc_msgSend$isEqualToUser:
+ _objc_msgSend$setShouldRetryEnrollment:
+ _objc_msgSend$shouldRetryEnrollment
+ _objc_msgSend$signInAccountsWithTypes:authenticationResult:personaID:canMakeAccountActive:baseViewController:forceInlinePresentation:completionHandler:
+ _objc_retain_x27
+ _objc_retain_x28
+ _reboot3
- +[DMCMultiUserModeUtilities _updateMultiUserConfigurationFileAtPath:key:value:]
- +[DMCMultiUserModeUtilities _updateMultiUserDeviceConfigurationFileWithKey:value:]
- +[DMCMultiUserModeUtilities _updateMultiUserUserConfigurationFileWithKey:value:]
- +[DMCMultiUserModeUtilities configureTemporarySessionOnly:useDynamicQuotaSize:restoreQuotaSizeWhenDisabled:preferenceDomain:]
- -[DMCAccountUtilities _signIniCloudAccountWithAuthenticationResult:personaID:baseViewController:outError:]
- GCC_except_table11
- GCC_except_table31
- ___106-[DMCAccountUtilities _signIniCloudAccountWithAuthenticationResult:personaID:baseViewController:outError:]_block_invoke
- ___106-[DMCAccountUtilities _signIniCloudAccountWithAuthenticationResult:personaID:baseViewController:outError:]_block_invoke.21
- ___136-[DMCAccountUtilities signInAccountsWithTypes:authenticationResult:personaID:canMakeAccountActive:baseViewController:completionHandler:]_block_invoke
- ___75+[DMCMultiUserModeUtilities _configureQuotaSizeForSharedDeviceImmediately:]_block_invoke
- ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8s48l8r56l8r64l8
- ___block_descriptor_81_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s72l8s40l8s48l8s56l8s64l8
- ___block_literal_global.229
- ___block_literal_global.240
- ___block_literal_global.246
- ___block_literal_global.253
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_signIniCloudAccountWithAuthenticationResult:personaID:baseViewController:outError:
- _objc_msgSend$_updateMultiUserConfigurationFileAtPath:key:value:
- _objc_msgSend$_updateMultiUserDeviceConfigurationFileWithKey:value:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x10
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "%s provision result %d..."
+ "%s won't be able to provision now, reboot so we can retry..."
+ "+[DMCMultiUserModeUtilities configureTemporarySessionOnly:useDynamicQuotaSize:restoreQuotaSizeWhenDisabled:directUserSwitch:authenticatedTemporarySession:preferenceDomain:]"
+ "-[DMCAccountUtilities _signIniCloudAccountWithAuthenticationResult:personaID:baseViewController:forceInlinePresentation:outError:]_block_invoke"
+ "/Performance"
+ "AuthenticatedTemporarySession"
+ "AuthenticatedTemporarySessionEnabled"
+ "B40@0:8@16@24^B32"
+ "B44@0:8B16B20B24B28B32^{__CFString=}36"
+ "B48@0:8@16@24@32^B40"
+ "B52@0:8@16@24@32B40^@44"
+ "B8@?0"
+ "Configuring no quota size Shared iPad"
+ "DMCObliterationShelter: start time is missing / malformed."
+ "Direct user switch can only be enabled when there's no user on the device."
+ "DirectUserSwitch"
+ "DirectUserSwitchEnabled"
+ "Duration"
+ "End"
+ "Failed to configure no quota size device with error: %{public}@"
+ "Failed to re-provision Shared iPad with error: %{public}@"
+ "Failed to remove user %@ with error: %{public}@"
+ "Failed to switch to persona %{public}@ for iCloud sign-in: %{public}@"
+ "Failed to switch to persona %{public}@ for iTunes sign-in: %{public}@"
+ "MCInstallationErrorDomain"
+ "NeedReprovision"
+ "Sending session timeout changed notification."
+ "ShouldRetryEnrollment"
+ "Start"
+ "T@\"NSDictionary\",R,N"
+ "TB,N,V_shouldRetryEnrollment"
+ "TB,R,N,GisAuthenticatedTemporarySessionEnabled"
+ "TB,R,N,GisDirectUserSwitchEnabled"
+ "_deleteAllUsersOtherThanCurrent"
+ "_generatePerformanceDictionary"
+ "_performanceDirectoryPath"
+ "_performanceFilePath"
+ "_provisionDeviceWithProvisionDict:error:"
+ "_shouldRetryEnrollment"
+ "_signIniCloudAccountWithAuthenticationResult:personaID:baseViewController:forceInlinePresentation:outError:"
+ "_updateMultiUserConfigurationFileAtPath:key:value:changed:"
+ "_updateMultiUserDeviceConfigurationFileWithKey:value:changed:"
+ "_updateMultiUserUserConfigurationFileWithKey:value:changed:"
+ "authenticatedTemporarySession"
+ "com.apple.devicemanagementclient.sessiontimeoutchanged"
+ "configureNoQuotaSizeSharedDevice"
+ "configureTemporarySessionOnly:useDynamicQuotaSize:restoreQuotaSizeWhenDisabled:directUserSwitch:authenticatedTemporarySession:preferenceDomain:"
+ "deleteUser:completionHandler:"
+ "deviceNeedsReprovision"
+ "directUserSwitch"
+ "fs_snapshot_list() failed with error: %{public}@"
+ "hasSystemVolumeSnapshotWithName:"
+ "isAuthenticatedTemporarySessionEnabled"
+ "isDirectUserSwitchEnabled"
+ "isEqualToUser:"
+ "performanceDictionary"
+ "reprovisionDeviceIfNeeded"
+ "rrts_performance.plist"
+ "setShouldRetryEnrollment:"
+ "shouldRetryEnrollment"
+ "signInAccountsWithTypes:authenticationResult:personaID:canMakeAccountActive:baseViewController:forceInlinePresentation:completionHandler:"
+ "trackEndTime"
+ "v32@0:8@16^@24"
+ "v64@0:8@16@24@32B40@44B52@?56"
- "+[DMCMultiUserModeUtilities configureTemporarySessionOnly:useDynamicQuotaSize:restoreQuotaSizeWhenDisabled:preferenceDomain:]"
- "-[DMCAccountUtilities _signIniCloudAccountWithAuthenticationResult:personaID:baseViewController:outError:]_block_invoke"
- "B36@0:8B16B20B24^{__CFString=}28"
- "B48@0:8@16@24@32^@40"
- "_signIniCloudAccountWithAuthenticationResult:personaID:baseViewController:outError:"
- "_updateMultiUserConfigurationFileAtPath:key:value:"
- "_updateMultiUserDeviceConfigurationFileWithKey:value:"
- "_updateMultiUserUserConfigurationFileWithKey:value:"
- "configureTemporarySessionOnly:useDynamicQuotaSize:restoreQuotaSizeWhenDisabled:preferenceDomain:"

```
