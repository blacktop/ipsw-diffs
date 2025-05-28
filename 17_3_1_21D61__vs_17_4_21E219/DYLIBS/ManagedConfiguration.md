## ManagedConfiguration

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`

```diff

-2261.0.0.0.0
-  __TEXT.__text: 0xd8f78
-  __TEXT.__auth_stubs: 0x1630
-  __TEXT.__objc_methlist: 0xa114
-  __TEXT.__cstring: 0x14430
-  __TEXT.__oslogstring: 0x7f54
-  __TEXT.__const: 0xfa4
-  __TEXT.__gcc_except_tab: 0xa78
+2288.0.1.0.0
+  __TEXT.__text: 0xd8674
+  __TEXT.__auth_stubs: 0x1600
+  __TEXT.__objc_methlist: 0xa214
+  __TEXT.__cstring: 0x14605
+  __TEXT.__oslogstring: 0x7d4b
+  __TEXT.__const: 0xfb4
+  __TEXT.__gcc_except_tab: 0xa48
   __TEXT.__ustring: 0x78
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x2c10
+  __TEXT.__unwind_info: 0x2be8
   __TEXT.__objc_classname: 0xc76
-  __TEXT.__objc_methname: 0x1bc43
-  __TEXT.__objc_methtype: 0x2146
-  __TEXT.__objc_stubs: 0xd100
-  __DATA_CONST.__got: 0x510
-  __DATA_CONST.__const: 0x4930
+  __TEXT.__objc_methname: 0x1be17
+  __TEXT.__objc_methtype: 0x217f
+  __TEXT.__objc_stubs: 0xd020
+  __DATA_CONST.__got: 0x500
+  __DATA_CONST.__const: 0x4908
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa480
-  __DATA_CONST.__objc_selrefs: 0x5610
+  __DATA_CONST.__objc_const: 0xa4b0
+  __DATA_CONST.__objc_selrefs: 0x5650
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x538
+  __DATA_CONST.__objc_superrefs: 0x2e0
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__cfstring: 0x17da0
+  __AUTH_CONST.__cfstring: 0x17fe0
   __AUTH_CONST.__objc_const: 0x3bf0
-  __AUTH_CONST.__const: 0x2200
+  __AUTH_CONST.__const: 0x2220
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__auth_got: 0xb28
+  __AUTH_CONST.__auth_got: 0xb10
   __AUTH.__objc_data: 0x1220
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x530
-  __DATA.__objc_superrefs: 0x2e0
-  __DATA.__objc_ivar: 0x950
-  __DATA.__data: 0xdc8
-  __DATA.__bss: 0x911
+  __DATA.__objc_ivar: 0x954
+  __DATA.__data: 0xde8
+  __DATA.__bss: 0x901
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x1400
   __DATA_DIRTY.__bss: 0x200

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4648
+  Functions: 4647
   Symbols:   15315
-  CStrings:  8209
+  CStrings:  8233
 
Symbols:
+ +[MCPayload(Private) _installableVisionConfigurationPayloadClasses]
+ +[MCPayload(Private) payloadsRequiringRatchetWithStolenDeviceProtection]
+ +[MCProfile(Private) thisDeviceType]
+ +[MCRestrictionsPayload _platformSpecificKeyFilter]
+ +[MCRestrictionsPayload _supervisedAllowedKeys]
+ +[MCRestrictionsPayload _unsupervisedAllowedKeys]
+ +[MCRestrictionsPayload userEnrollmentAllowedKeysFilter]
+ -[MCHacks _applyHeuristicsToRestrictions:forProfile:ignoresUnrestrictableApps:]
+ -[MCHoldingTankManifest addPurgatoryProfileData:identifier:targetDevice:outError:]
+ -[MCProfileConnection(Misc) allMarketplacesAllowed]
+ -[MCProfileConnection(Misc) allowedMarketplaces]
+ -[MCProfileConnection(Misc) anyMarketplaceAllowed]
+ -[MCProfileConnection(Misc) deniedMarketplaces]
+ -[MCProfileConnection(Misc) isAutoDimAllowed]
+ -[MCProfileConnection(Misc) isCommandTabAllowed]
+ -[MCProfileConnection(Misc) isControlCenterAllowed]
+ -[MCProfileConnection(Misc) isCoverSheetAllowed]
+ -[MCProfileConnection(Misc) isExternalDisplayStageManagerAllowed]
+ -[MCProfileConnection(Misc) isHomeScreenEditingAllowed]
+ -[MCProfileConnection(Misc) isMarketplaceAllowed:]
+ -[MCProfileConnection(Misc) isMarketplaceAppInstallationAllowed]
+ -[MCProfileConnection(Misc) isSpotlightAllowed]
+ -[MCProfileConnection(Misc) isWallpaperAllowed]
+ -[MCProfileConnection(Misc) isWebDistributionAppInstallationAllowed]
+ -[MCProfileConnection(Restrictions) applyRestrictionDictionary:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:]
+ -[MCProfileConnection(Restrictions) applyRestrictionDictionary:overrideRestrictions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:]
+ -[MCRestrictionManager memberQueueOverridingRestrictionClientUUID]
+ -[MCRestrictionManager setMemberQueueOverridingRestrictionClientUUID:]
+ GCC_except_table100
+ GCC_except_table104
+ GCC_except_table126
+ GCC_except_table235
+ GCC_except_table68
+ GCC_except_table98
+ _AKS_FV_MDM_RECOVERY_KEY_UUID
+ _MCClientRestrictionsErrorDomain
+ _MCFeatureAllowedMarketplaceApps
+ _MCFeatureCommandTabAllowed
+ _MCFeatureControlCenterAllowed
+ _MCFeatureCoverSheetAllowed
+ _MCFeatureDeniedMarketplaceApps
+ _MCFeatureExternalDisplayStageManagerAllowed
+ _MCFeatureHomeScreenEditingAllowed
+ _MCFeatureMarketplaceAppInstallationAllowed
+ _MCFeatureSpotlightAllowed
+ _MCFeatureWallpaperAllowed
+ _MCFeatureWebDistributionAppInstallationAllowed
+ _MCGestaltGetDeviceName
+ _MCTelephonyUtilitiesBundleIdentifier
+ _OBJC_CLASS_$_DMCFeatureFlags
+ _OBJC_IVAR_$_MCRestrictionManager._memberQueueOverridingRestrictionClientUUID
+ __VisionProAllowedKeysFilter.dict
+ __VisionProAllowedKeysFilter.onceToken
+ ___100-[MCProfileConnection(Misc) defaultAppBundleIDForCommunicationServiceType:forAccountWithIdentifier:]_block_invoke.45
+ ___232-[MCProfileConnection(Restrictions) applyRestrictionDictionary:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:]_block_invoke
+ ___232-[MCProfileConnection(Restrictions) applyRestrictionDictionary:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:]_block_invoke.2
+ ___47+[MCRestrictionsPayload _supervisedAllowedKeys]_block_invoke
+ ___49+[MCRestrictionsPayload _unsupervisedAllowedKeys]_block_invoke
+ ___56+[MCRestrictionsPayload userEnrollmentAllowedKeysFilter]_block_invoke
+ ___72+[MCPayload(Private) payloadsRequiringRatchetWithStolenDeviceProtection]_block_invoke
+ ____VisionProAllowedKeysFilter_block_invoke
+ ___block_literal_global.107
+ ___block_literal_global.1285
+ ___block_literal_global.1292
+ ___block_literal_global.1294
+ ___block_literal_global.1296
+ ___block_literal_global.15
+ ___block_literal_global.243
+ ___block_literal_global.248
+ ___block_literal_global.254
+ ___block_literal_global.263
+ ___block_literal_global.336
+ ___block_literal_global.455
+ ___block_literal_global.55
+ ___block_literal_global.550
+ ___block_literal_global.572
+ ___block_literal_global.621
+ ___block_literal_global.656
+ ___block_literal_global.661
+ ___block_literal_global.666
+ ___block_literal_global.671
+ ___block_literal_global.676
+ ___block_literal_global.78
+ ___block_literal_global.90
+ _calloc
+ _firebloom_ccpbkdf2_hmac
+ _kMCClientRestrictionsOverrideRestrictions
+ _malloc
+ _objc_msgSend$_applyHeuristicsToRestrictions:forProfile:ignoresUnrestrictableApps:
+ _objc_msgSend$_installableVisionConfigurationPayloadClasses
+ _objc_msgSend$_platformSpecificKeyFilter
+ _objc_msgSend$_supervisedAllowedKeys
+ _objc_msgSend$_unsupervisedAllowedKeys
+ _objc_msgSend$allowedMarketplaces
+ _objc_msgSend$applyRestrictionDictionary:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:completion:
+ _objc_msgSend$applyRestrictionDictionary:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:
+ _objc_msgSend$deniedMarketplaces
+ _objc_msgSend$effectiveValuesForUnionSetting:
+ _objc_msgSend$isMarketplaceAppInstallationAllowed
+ _objc_msgSend$isVisionMDMEnabled
+ _objc_msgSend$userEnrollmentAllowedKeysFilter
+ _payloadsRequiringRatchetWithStolenDeviceProtection.onceToken
+ _payloadsRequiringRatchetWithStolenDeviceProtection.payloads
- +[MCPayload(Private) unavailablePayloadsWithStolenDeviceProtection]
- +[MCRestrictionManager restrictionsWithCurrentRestrictions:defaultRestrictions:profileRestrictions:clientRestrictions:outRestrictionsChanged:outError:]
- -[MCAccountUtilities _signIniCloudAccountWithAuthenticationResult:personaID:baseViewController:outError:]
- -[MCAccountUtilities _signIniTunesAccountWithAuthenticationResult:personaID:baseViewController:outError:]
- -[MCAccountUtilities signInAccountsWithTypes:authenticationResult:personaID:baseViewController:completionHandler:]
- -[MCHacks _applyHeuristicsToRestrictions:forProfile:outError:]
- -[MCHoldingTankManifest addProfileData:withIdentifier:toHoldingTankForDevice:outError:]
- GCC_except_table101
- GCC_except_table105
- GCC_except_table127
- GCC_except_table220
- GCC_except_table67
- GCC_except_table69
- GCC_except_table82
- GCC_except_table97
- GCC_except_table99
- _ACAccountTypeIdentifierAppleAccount
- _ACErrorDomain
- ___100-[MCProfileConnection(Misc) defaultAppBundleIDForCommunicationServiceType:forAccountWithIdentifier:]_block_invoke.44
- ___105-[MCAccountUtilities _signIniCloudAccountWithAuthenticationResult:personaID:baseViewController:outError:]_block_invoke
- ___105-[MCAccountUtilities _signIniCloudAccountWithAuthenticationResult:personaID:baseViewController:outError:]_block_invoke.77
- ___105-[MCAccountUtilities _signIniTunesAccountWithAuthenticationResult:personaID:baseViewController:outError:]_block_invoke
- ___114-[MCAccountUtilities signInAccountsWithTypes:authenticationResult:personaID:baseViewController:completionHandler:]_block_invoke
- ___211-[MCProfileConnection(Restrictions) applyRestrictionDictionary:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:]_block_invoke
- ___211-[MCProfileConnection(Restrictions) applyRestrictionDictionary:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:]_block_invoke.2
- ___67+[MCPayload(Private) unavailablePayloadsWithStolenDeviceProtection]_block_invoke
- ____supervisedAllowedKeys_block_invoke
- ____unsupervisedAllowedKeys_block_invoke
- ___block_descriptor_56_e8_32s40r48r_e20_v20?0B8"NSError"12lr40l8r48l8s32l8
- ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
- ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8r72l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s72l8s40l8s48l8s56l8s64l8
- ___block_literal_global.101
- ___block_literal_global.112
- ___block_literal_global.1279
- ___block_literal_global.1282
- ___block_literal_global.1284
- ___block_literal_global.1286
- ___block_literal_global.14
- ___block_literal_global.240
- ___block_literal_global.242
- ___block_literal_global.245
- ___block_literal_global.247
- ___block_literal_global.255
- ___block_literal_global.260
- ___block_literal_global.43
- ___block_literal_global.441
- ___block_literal_global.536
- ___block_literal_global.544
- ___block_literal_global.607
- ___block_literal_global.638
- ___block_literal_global.643
- ___block_literal_global.648
- ___block_literal_global.653
- ___block_literal_global.658
- ___block_literal_global.663
- ___userEnrollmentAllowedKeysFilter_block_invoke
- __supervisedAllowedKeys
- _aks_remote_peer_register
- _cccurve25519_make_key_pair
- _ccder_encode_body
- _ccder_encode_tl
- _cced25519_make_key_pair
- _decode_fv_data
- _decode_fv_key
- _decode_fv_params
- _decode_implicit_raw_octet_string
- _decode_implicit_raw_octet_string_copy
- _decode_implicit_uint64
- _der_decode_any
- _encode_fv_data
- _encode_fv_key
- _encode_fv_params
- _firebloom_cccurve25519
- _firebloom_curve25519_make_key_pair
- _firebloom_ed25519_make_key_pair
- _firebloom_get_sized_copy
- _firebloom_get_sized_len
- _firebloom_ipc_copy_out
- _malloc_type_malloc
- _objc_msgSend$_applyHeuristicsToRestrictions:forProfile:outError:
- _objc_msgSend$_signIniCloudAccountWithAuthenticationResult:personaID:baseViewController:outError:
- _objc_msgSend$_signIniTunesAccountWithAuthenticationResult:personaID:baseViewController:outError:
- _objc_msgSend$aa_altDSID
- _objc_msgSend$ams_activeiTunesAccount
- _objc_msgSend$ams_sharedAccountStore
- _objc_msgSend$applyRestrictionDictionary:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:completion:
- _objc_msgSend$currentPersonaID
- _objc_msgSend$initWithAccount:presentingViewController:options:
- _objc_msgSend$initWithAccountStore:
- _objc_msgSend$performAuthentication
- _objc_msgSend$performBlockUnderPersona:block:
- _objc_msgSend$restrictionsWithCurrentRestrictions:defaultRestrictions:systemProfileRestrictions:userProfileRestrictions:systemClientRestrictions:userClientRestrictions:outRestrictionsChanged:outError:
- _objc_msgSend$resultWithError:
- _objc_msgSend$setAltDSID:
- _objc_msgSend$setAuthenticationResults:
- _objc_msgSend$setAuthenticationType:
- _objc_msgSend$setCanMakeAccountActive:
- _objc_msgSend$setViewController:
- _objc_msgSend$signInService:withContext:completion:
- _unavailablePayloadsWithStolenDeviceProtection.onceToken
- _unavailablePayloadsWithStolenDeviceProtection.payloads
- _userEnrollmentAllowedKeysFilter
CStrings:
+ "\x0e"
+ "AssertMacros: %s, %s file: %s, line: %d, value: %lld\n"
+ "B84@0:8@16B24@28@36@44@52^B60^B68^@76"
+ "B92@0:8@16B24@28@36@44@52@60^B68^B76^@84"
+ "ERROR_PROFILE_DRIVEN_ENROLLMENT_BLOCKED"
+ "FEATURE_MARKETPLACE_APP_INSTALLATION"
+ "INSTALL_PROFILE_MESSAGE_HOME_APP"
+ "INSTALL_PROFILE_MESSAGE_SETTINGS_APP"
+ "INSTALL_PROFILE_MESSAGE_WATCH_APP"
+ "INSTALL_WARNING_TARGET_INVALID_MESSAGE_REALITYDEVICE"
+ "MCClientRestrictionsErrorDomain"
+ "T@\"NSArray\",?,R,&,N"
+ "T@\"NSString\",&,N,V_memberQueueOverridingRestrictionClientUUID"
+ "T@\"NSString\",?,R,C"
+ "VisionProRestrictionPayloadKeysFilter.plist"
+ "_applyHeuristicsToRestrictions:forProfile:ignoresUnrestrictableApps:"
+ "_installableVisionConfigurationPayloadClasses"
+ "_memberQueueOverridingRestrictionClientUUID"
+ "_platformSpecificKeyFilter"
+ "_supervisedAllowedKeys"
+ "_unsupervisedAllowedKeys"
+ "addPurgatoryProfileData:identifier:targetDevice:outError:"
+ "allMarketplacesAllowed"
+ "allowCommandTab"
+ "allowControlCenter"
+ "allowCoverSheet"
+ "allowExternalDisplayStageManager"
+ "allowHomeScreenEditing"
+ "allowMarketplaceAppInstallation"
+ "allowSpotlight"
+ "allowWallpaper"
+ "allowWebDistributionAppInstallation"
+ "allowedMarketplaceApps"
+ "allowedMarketplaces"
+ "anyMarketplaceAllowed"
+ "applyRestrictionDictionary:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:completion:"
+ "applyRestrictionDictionary:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:"
+ "applyRestrictionDictionary:overrideRestrictions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:outRestrictionChanged:outEffectiveSettingsChanged:outError:"
+ "com.apple.TelephonyUtilities"
+ "deniedMarketplaceApps"
+ "deniedMarketplaces"
+ "iDevice"
+ "isAutoDimAllowed"
+ "isCommandTabAllowed"
+ "isControlCenterAllowed"
+ "isCoverSheetAllowed"
+ "isExternalDisplayStageManagerAllowed"
+ "isHomeScreenEditingAllowed"
+ "isMarketplaceAllowed:"
+ "isMarketplaceAppInstallationAllowed"
+ "isSpotlightAllowed"
+ "isVisionMDMEnabled"
+ "isWallpaperAllowed"
+ "isWebDistributionAppInstallationAllowed"
+ "memberQueueOverridingRestrictionClientUUID"
+ "overrideRestrictions"
+ "payloadsRequiringRatchetWithStolenDeviceProtection"
+ "setMemberQueueOverridingRestrictionClientUUID:"
+ "thisDeviceType"
+ "userEnrollmentAllowedKeysFilter"
+ "v76@0:8@\"NSDictionary\"16B24@\"NSArray\"28@\"NSString\"36@\"NSString\"44@\"NSString\"52@\"NSString\"60@?<v@?BB@\"NSError\">68"
+ "v76@0:8@16B24@28@36@44@52@60@?68"
+ "vision"
- "\r"
- "@64@0:8@16@24@32@40^B48^@56"
- "AssertMacros: %s, %s file: %s, line: %d, value: %ld\n"
- "INSTALL_PROFILE_DISABLED_MESSAGE_STOLEN_DEVICE_PROTECTION_MODE"
- "INSTALL_PROFILE_MESSAGE_HOMEPOD"
- "INSTALL_PROFILE_MESSAGE_PHONE"
- "INSTALL_PROFILE_MESSAGE_WATCH"
- "MCAccountUtilities: Has enterprise persona, will sign in iCloud under enterprise persona"
- "MCAccountUtilities: Has enterprise persona, will sign in iTunes under enterprise persona"
- "MCAccountUtilities: Signing in iCloud account finished with result: %d, error: %@"
- "MCAccountUtilities: Signing in iCloud account with personaID: %@"
- "MCAccountUtilities: Signing in iTunes account finished with result: %d, error: %@"
- "MCAccountUtilities: Signing in iTunes account with personaID: %@"
- "MCAccountUtilities: Unsupported account type: %@"
- "_applyHeuristicsToRestrictions:forProfile:outError:"
- "_signIniCloudAccountWithAuthenticationResult:personaID:baseViewController:outError:"
- "_signIniTunesAccountWithAuthenticationResult:personaID:baseViewController:outError:"
- "aa_altDSID"
- "addProfileData:withIdentifier:toHoldingTankForDevice:outError:"
- "ams_activeiTunesAccount"
- "ams_sharedAccountStore"
- "applyRestrictionDictionary:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:completion:"
- "currentPersonaID"
- "initWithAccount:presentingViewController:options:"
- "initWithAccountStore:"
- "performAuthentication"
- "performBlockUnderPersona:block:"
- "r"
- "restrictionsWithCurrentRestrictions:defaultRestrictions:profileRestrictions:clientRestrictions:outRestrictionsChanged:outError:"
- "resultWithError:"
- "setAltDSID:"
- "setAuthenticationResults:"
- "setCanMakeAccountActive:"
- "setViewController:"
- "signInAccountsWithTypes:authenticationResult:personaID:baseViewController:completionHandler:"
- "signInService:withContext:completion:"
- "unavailablePayloadsWithStolenDeviceProtection"
- "v72@0:8@\"NSDictionary\"16@\"NSArray\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@?<v@?BB@\"NSError\">64"
- "v72@0:8@16@24@32@40@48@56@?64"

```
