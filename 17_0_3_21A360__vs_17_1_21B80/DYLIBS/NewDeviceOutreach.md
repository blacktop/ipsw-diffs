## NewDeviceOutreach

> `/System/Library/PrivateFrameworks/NewDeviceOutreach.framework/NewDeviceOutreach`

```diff

-252.0.0.0.0
-  __TEXT.__text: 0xa3ac
-  __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_methlist: 0xc90
-  __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x2a0
-  __TEXT.__oslogstring: 0x76c
-  __TEXT.__cstring: 0xec5
-  __TEXT.__unwind_info: 0x2dc
-  __TEXT.__objc_classname: 0x8e
-  __TEXT.__objc_methname: 0x3680
-  __TEXT.__objc_methtype: 0x3fe
-  __TEXT.__objc_stubs: 0x1bc0
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x440
-  __DATA_CONST.__objc_classlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x18
+405.0.0.0.0
+  __TEXT.__text: 0x110dc
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_methlist: 0x1000
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x15e8
+  __TEXT.__oslogstring: 0x13ab
+  __TEXT.__gcc_except_tab: 0x314
+  __TEXT.__unwind_info: 0x3dc
+  __TEXT.__objc_classname: 0xfb
+  __TEXT.__objc_methname: 0x4901
+  __TEXT.__objc_methtype: 0x5b3
+  __TEXT.__objc_stubs: 0x2dc0
+  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__const: 0x5b8
+  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1688
-  __DATA_CONST.__objc_selrefs: 0xa58
-  __AUTH_CONST.__cfstring: 0x10e0
+  __DATA_CONST.__objc_const: 0x1da0
+  __DATA_CONST.__objc_selrefs: 0xf18
+  __DATA_CONST.__objc_arraydata: 0x10
+  __AUTH_CONST.__objc_const: 0x470
+  __AUTH_CONST.__cfstring: 0x1940
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH_CONST.__objc_const: 0x2d0
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__auth_got: 0x260
-  __AUTH.__objc_data: 0x1e0
+  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__auth_got: 0x290
+  __AUTH.__objc_data: 0x2d0
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0xd8
-  __DATA.__objc_superrefs: 0x20
-  __DATA.__objc_ivar: 0x168
-  __DATA.__data: 0x120
+  __DATA.__objc_classrefs: 0x160
+  __DATA.__objc_superrefs: 0x28
+  __DATA.__objc_ivar: 0x190
+  __DATA.__data: 0x1e0
   __DATA.__bss: 0x10
+  - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
+  - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
-  - /System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 357546B5-770F-38C0-9616-567990EC7ED6
-  Functions: 361
-  Symbols:   1282
-  CStrings:  931
+  UUID: 86B9B95B-6F63-313A-BB42-A41D92D0A6BA
+  Functions: 479
+  Symbols:   1759
+  CStrings:  1363
 
Symbols:
+ +[NDODevice deviceWithName:serialNumber:activationDate:deviceType:productID:productName:]
+ +[NDODevice deviceWithName:serialNumber:activationDate:deviceType:productID:productName:isICloudDevice:]
+ +[NDODevice deviceWithName:serialNumber:activationDate:deviceType:productID:productName:isVisibleInCC:]
+ +[NDOFollowUp uniqueIdentfierForSerialNumber:]
+ +[NDOServerVersionUtilities readAPSSupportedOverride]
+ +[NDOServerVersionUtilities readAPSSupportedOverride].cold.1
+ +[NDOUtilities isInternal]
+ -[NDODefaultFolllowUpProvider clearPendingFollowUpItemsWithUniqueIdentifiers:error:]
+ -[NDODefaultFolllowUpProvider pendingFollowUpItems:]
+ -[NDODefaultFolllowUpProvider postFollowUpItem:error:]
+ -[NDODevice initWithName:serialNumber:activationDate:deviceType:productID:productName:isICloudDevice:isVisibleInCC:]
+ -[NDODevice isICloudDevice]
+ -[NDODevice isVisibleInCC]
+ -[NDODevice productName]
+ -[NDODevice setIsICloudDevice:]
+ -[NDODevice setIsVisibleInCC:]
+ -[NDODevice setProductName:]
+ -[NDOFollowUp .cxx_destruct]
+ -[NDOFollowUp _checkConversionEligibilityForDevice:]
+ -[NDOFollowUp _checkConversionEligibilityForDevice:].cold.1
+ -[NDOFollowUp _clearFollowUpForSerialNumber:]
+ -[NDOFollowUp _clearFollowUpWithDevices:]
+ -[NDOFollowUp _postFollowUpWithDevicesInfo:repostAllowed:]
+ -[NDOFollowUp _setupFollowUpItem:withDeviceInfo:]
+ -[NDOFollowUp _setupFollowUpItem:withDeviceInfo:].cold.1
+ -[NDOFollowUp _setupFollowUpItem:withDeviceInfo:].cold.2
+ -[NDOFollowUp _setupFollowUpNotificationWithDeviceInfo:]
+ -[NDOFollowUp _setupFollowUpNotificationWithDeviceInfo:].cold.1
+ -[NDOFollowUp _setupFollowUpNotificationWithDeviceInfo:].cold.2
+ -[NDOFollowUp dismissFollowUpForSerialNumber:]
+ -[NDOFollowUp dismissNotificationForSerialNumber:]
+ -[NDOFollowUp followUpProvider]
+ -[NDOFollowUp initWithFollowUpProvider:]
+ -[NDOFollowUp init]
+ -[NDOFollowUp migrateLegacyFollowUpIfNeededWithDeviceInfo:]
+ -[NDOFollowUp migrateLegacyFollowUpIfNeededWithDeviceInfo:].cold.1
+ -[NDOFollowUp migrateLegacyFollowUpIfNeededWithDeviceInfo:].cold.2
+ -[NDOFollowUp migrateLegacyFollowUpIfNeededWithDeviceInfo:].cold.3
+ -[NDOFollowUp pendingFollowUpCount]
+ -[NDOFollowUp pendingFollowUpCount].cold.1
+ -[NDOFollowUp postFollowUpWithDeviceInfo:]
+ -[NDOFollowUp postFollowUpWithDeviceInfo:].cold.1
+ -[NDOFollowUp postFollowUpWithDeviceInfo:].cold.2
+ -[NDOFollowUp postFollowUpWithDeviceInfo:].cold.3
+ -[NDOFollowUp postFollowUpWithDevicesInfo:]
+ -[NDOFollowUp refreshALLFollowupsWithDeviceInfos:andForcePostFollowup:]
+ -[NDOFollowUp refreshFollowupWithDeviceInfo:andForcePostFollowup:]
+ -[NDOFollowUp refreshFollowupWithDeviceInfos:andForcePostFollowup:]
+ -[NDOFollowUp refreshFollowupWithDeviceInfos:clearUntrackedDeviceFollowups:andForcePostFollowup:]
+ -[NDOFollowUp refreshFollowupWithDeviceInfos:clearUntrackedDeviceFollowups:andForcePostFollowup:].cold.1
+ -[NDOFollowUp setFollowUpProvider:]
+ -[NDOManager apsSupportedOverride:]
+ -[NDOManager getBTDeviceInfosUsingPolicy:updateFollowUps:withReply:]
+ -[NDOManager getBTPioneerDeviceInfosUsingPolicy:updateFollowUps:withReply:]
+ -[NDOManager getPrimaryFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:]
+ -[NDOManager isAPSSupportedOverrideWithServerValue:]
+ -[NDOManager isAPSSupportedOverrideWithServerValue:].cold.1
+ -[NDOWarranty acLocalizedGroupedOfferCTA]
+ -[NDOWarranty acLocalizedGroupedOfferFooterLabel]
+ -[NDOWarranty acLocalizedOfferLongLabel]
+ -[NDOWarranty cacheValidityDuration]
+ -[NDOWarranty getSupportURL]
+ -[NDOWarranty isAPSSupported]
+ -[NDOWarranty mySupportURL]
+ -[NDOWarranty setAcLocalizedGroupedOfferCTA:]
+ -[NDOWarranty setAcLocalizedGroupedOfferFooterLabel:]
+ -[NDOWarranty setAcLocalizedOfferLongLabel:]
+ -[NDOWarranty setCacheValidityDuration:]
+ -[NDOWarranty setGetSupportURL:]
+ -[NDOWarranty setIsAPSSupported:]
+ -[NDOWarranty setMySupportURL:]
+ -[NSMutableURLRequest(AccountHeaders) _addGSHeadersForAccount:withStore:forceReprovisioning:avoidUI:]
+ -[NSMutableURLRequest(AccountHeaders) _addGSHeadersForAccount:withStore:forceReprovisioning:avoidUI:].cold.1
+ -[NSMutableURLRequest(AccountHeaders) _deviceProductType]
+ -[NSMutableURLRequest(AccountHeaders) _osVersion]
+ -[NSMutableURLRequest(AccountHeaders) _userAgentWithBundleID:]
+ -[NSMutableURLRequest(AccountHeaders) _userAgent]
+ -[NSMutableURLRequest(AccountHeaders) addBAAAuthenticationHeadersWithBody:]
+ -[NSMutableURLRequest(AccountHeaders) addBAAAuthenticationHeadersWithBody:].cold.1
+ -[NSMutableURLRequest(AccountHeaders) addBAAAuthenticationHeadersWithSerialNumber:]
+ -[NSMutableURLRequest(AccountHeaders) addStoreLocaleHeaderIfNeededForAccount:]
+ -[NSMutableURLRequest(AccountHeaders) addStoreLocaleHeaderIfNeededForAccount:].cold.1
+ -[NSMutableURLRequest(AccountHeaders) bodyDescription]
+ -[NSMutableURLRequest(AccountHeaders) headerDescription]
+ -[NSMutableURLRequest(AccountHeaders) ndo_addBasicHeadersWithBundleID:]
+ -[NSMutableURLRequest(AccountHeaders) ndo_addOASHeadersWithOfferID:serialNumber:primarySerialNumber:]
+ -[NSMutableURLRequest(AccountHeaders) ndo_addOASHeadersWithOfferID:serialNumber:primarySerialNumber:].cold.1
+ -[NSMutableURLRequest(AccountHeaders) ndo_setCoverageRequestBodyWithSerialNumber:primarySerialNumber:displayedEvents:]
+ -[NSMutableURLRequest(AccountHeaders) ndo_signWithAccountHeaders:avoidUI:]
+ -[NSString(SHA256Hash) sha256Hash]
+ GCC_except_table20
+ GCC_except_table30
+ GCC_except_table33
+ GCC_except_table36
+ GCC_except_table39
+ GCC_except_table45
+ GCC_except_table7
+ _CC_SHA256
+ _CFPreferencesCopyAppValue
+ _FLFollowUpBridgeBundleIdentifier
+ _FLFollowUpNDOBundleIdentifier
+ _FLFollowUpNotifyingAppIdKey
+ _FLFollowUpPreferencesBundleIdentifier
+ _FLGroupIdentifierNewDeviceOutreach
+ _FLNotificationOptionExtensionActions
+ _FLNotificationOptionExtensionForNotification
+ _FLNotificationOptionLockscreen
+ _FLNotificationOptionNotificationCenter
+ _FLUserInfoPropertyCoalescedGroupFooterText
+ _FLUserInfoPropertyCoalescedLongerTitle
+ _FLUserInfoPropertyRelativeIsCeilingKey
+ _FLUserInfoPropertyRelativePluralDaysFormatKey
+ _FLUserInfoPropertyRelativeSingleDayKey
+ _MGCopyAnswer
+ _OBJC_CLASS_$_ACAccountStore
+ _OBJC_CLASS_$_AKAppleIDSession
+ _OBJC_CLASS_$_AMSAuthenticateOptions
+ _OBJC_CLASS_$_AMSAuthenticateTask
+ _OBJC_CLASS_$_FLFollowUpAction
+ _OBJC_CLASS_$_FLFollowUpController
+ _OBJC_CLASS_$_FLFollowUpItem
+ _OBJC_CLASS_$_FLFollowUpNotification
+ _OBJC_CLASS_$_NDODefaultFolllowUpProvider
+ _OBJC_CLASS_$_NDOFollowUp
+ _OBJC_CLASS_$_NDOUtilities
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSMutableURLRequest
+ _OBJC_CLASS_$_NSTimeZone
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_IVAR_$_NDODevice._isICloudDevice
+ _OBJC_IVAR_$_NDODevice._isVisibleInCC
+ _OBJC_IVAR_$_NDODevice._productName
+ _OBJC_IVAR_$_NDOFollowUp._followUpProvider
+ _OBJC_IVAR_$_NDOWarranty._acLocalizedGroupedOfferCTA
+ _OBJC_IVAR_$_NDOWarranty._acLocalizedGroupedOfferFooterLabel
+ _OBJC_IVAR_$_NDOWarranty._acLocalizedOfferLongLabel
+ _OBJC_IVAR_$_NDOWarranty._cacheValidityDuration
+ _OBJC_IVAR_$_NDOWarranty._getSupportURL
+ _OBJC_IVAR_$_NDOWarranty._isAPSSupported
+ _OBJC_IVAR_$_NDOWarranty._mySupportURL
+ _OBJC_METACLASS_$_NDODefaultFolllowUpProvider
+ _OBJC_METACLASS_$_NDOFollowUp
+ _OBJC_METACLASS_$_NDOUtilities
+ __OBJC_$_CATEGORY_NSMutableURLRequest_$_AccountHeaders
+ __OBJC_$_CATEGORY_NSString_$_SHA256Hash
+ __OBJC_$_CLASS_METHODS_NDOFollowUp
+ __OBJC_$_CLASS_METHODS_NDOUtilities
+ __OBJC_$_INSTANCE_METHODS_NDODefaultFolllowUpProvider
+ __OBJC_$_INSTANCE_METHODS_NDOFollowUp
+ __OBJC_$_INSTANCE_METHODS_NSMutableURLRequest(AccountHeaders)
+ __OBJC_$_INSTANCE_METHODS_NSString(SHA256Hash)
+ __OBJC_$_INSTANCE_VARIABLES_NDOFollowUp
+ __OBJC_$_PROP_LIST_NDODefaultFolllowUpProvider
+ __OBJC_$_PROP_LIST_NDOFollowUp
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NDOFollowUpProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NDOFollowUpProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_NDOFollowUpProvider
+ __OBJC_CLASS_PROTOCOLS_$_NDODefaultFolllowUpProvider
+ __OBJC_CLASS_RO_$_NDODefaultFolllowUpProvider
+ __OBJC_CLASS_RO_$_NDOFollowUp
+ __OBJC_CLASS_RO_$_NDOUtilities
+ __OBJC_LABEL_PROTOCOL_$_NDOFollowUpProvider
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_NDODefaultFolllowUpProvider
+ __OBJC_METACLASS_RO_$_NDOFollowUp
+ __OBJC_METACLASS_RO_$_NDOUtilities
+ __OBJC_PROTOCOL_$_NDOFollowUpProvider
+ __OBJC_PROTOCOL_$_NSObject
+ ___101-[NSMutableURLRequest(AccountHeaders) _addGSHeadersForAccount:withStore:forceReprovisioning:avoidUI:]_block_invoke
+ ___101-[NSMutableURLRequest(AccountHeaders) _addGSHeadersForAccount:withStore:forceReprovisioning:avoidUI:]_block_invoke.cold.1
+ ___103-[NDOManager getDeviceInfoForSerialNumber:usingPolicy:sessionID:params:andForcePostFollowup:withReply:]_block_invoke.36
+ ___27-[NDOManager defaultDevice]_block_invoke.28
+ ___27-[NDOManager pairedWatches]_block_invoke.30
+ ___29-[NDOManager pairedBTDevices]_block_invoke.32
+ ___35-[NDOManager apsSupportedOverride:]_block_invoke
+ ___35-[NDOManager apsSupportedOverride:]_block_invoke.13
+ ___35-[NDOManager apsSupportedOverride:]_block_invoke.cold.1
+ ___41-[NDOFollowUp _clearFollowUpWithDevices:]_block_invoke
+ ___42-[NDOFollowUp postFollowUpWithDeviceInfo:]_block_invoke
+ ___48-[NDOManager getDecodedParamsForPath:withReply:]_block_invoke.27
+ ___52-[NDOManager isAPSSupportedOverrideWithServerValue:]_block_invoke
+ ___56-[NDOManager dismissFollowUpForSerialNumber:completion:]_block_invoke.41
+ ___56-[NDOManager getDefaultDeviceInfoUsingForceCachedPolicy]_block_invoke.33
+ ___56-[NDOManager getDefaultDeviceInfoUsingPolicy:withReply:]_block_invoke.34
+ ___58-[NDOFollowUp _postFollowUpWithDevicesInfo:repostAllowed:]_block_invoke
+ ___58-[NDOFollowUp _postFollowUpWithDevicesInfo:repostAllowed:]_block_invoke.61
+ ___60-[NDOManager dismissNotificationForSerialNumber:completion:]_block_invoke.42
+ ___65-[NDOManager getDeviceInfoUsingForceCachedPolicyForSerialNumber:]_block_invoke.35
+ ___68-[NDOManager getBTDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke
+ ___68-[NDOManager getBTDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.39
+ ___68-[NDOManager getBTDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.cold.1
+ ___75-[NDOManager getBTPioneerDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke
+ ___75-[NDOManager getBTPioneerDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.40
+ ___75-[NDOManager getBTPioneerDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.cold.1
+ ___75-[NSMutableURLRequest(AccountHeaders) addBAAAuthenticationHeadersWithBody:]_block_invoke
+ ___75-[NSMutableURLRequest(AccountHeaders) addBAAAuthenticationHeadersWithBody:]_block_invoke.cold.1
+ ___80-[NDOManager getAllFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.38
+ ___84-[NDOManager getPrimaryFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke
+ ___84-[NDOManager getPrimaryFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.37
+ ___84-[NDOManager getPrimaryFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.cold.1
+ ___97-[NDOFollowUp refreshFollowupWithDeviceInfos:clearUntrackedDeviceFollowups:andForcePostFollowup:]_block_invoke
+ ___97-[NDOFollowUp refreshFollowupWithDeviceInfos:clearUntrackedDeviceFollowups:andForcePostFollowup:]_block_invoke.105
+ ___97-[NDOFollowUp refreshFollowupWithDeviceInfos:clearUntrackedDeviceFollowups:andForcePostFollowup:]_block_invoke.cold.1
+ ___NSArray0__struct
+ ___block_descriptor_32_e32_v32?0"NSArray"816"NSError"24l
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e26_v32?0"NDODevice"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e30_v32?0"NDODeviceInfo"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s40r_e18_v16?0"NSString"8lr40l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e30_v32?0"NDODeviceInfo"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e30_v32?0"NDODeviceInfo"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e20_v24?0q8"NSError"16ls32l8s40l8r56l8s48l8
+ ___block_descriptor_73_e8_32s40s48s56s64s_e30_v32?0"NDODeviceInfo"8Q16^B24ls32l8s40l8s48l8s56l8s64l8
+ __unnamed_array_storage
+ _kACRenewCredentialsServicesKey
+ _kACRenewCredentialsShouldAvoidUIKey
+ _objc_msgSend$HTTPBody
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_addGSHeadersForAccount:withStore:forceReprovisioning:avoidUI:
+ _objc_msgSend$_checkConversionEligibilityForDevice:
+ _objc_msgSend$_clearFollowUpWithDevices:
+ _objc_msgSend$_deviceProductType
+ _objc_msgSend$_osVersion
+ _objc_msgSend$_postFollowUpWithDevicesInfo:repostAllowed:
+ _objc_msgSend$_setupFollowUpItem:withDeviceInfo:
+ _objc_msgSend$_setupFollowUpNotificationWithDeviceInfo:
+ _objc_msgSend$_userAgentWithBundleID:
+ _objc_msgSend$aa_altDSID
+ _objc_msgSend$acLocalizedGroupedOfferCTA
+ _objc_msgSend$acLocalizedGroupedOfferFooterLabel
+ _objc_msgSend$acLocalizedNotificationOfferDesc
+ _objc_msgSend$acLocalizedOfferCTA
+ _objc_msgSend$acLocalizedOfferDesc
+ _objc_msgSend$acLocalizedOfferLabel
+ _objc_msgSend$acLocalizedOfferLongLabel
+ _objc_msgSend$acNotificationLocalizedOfferLabel
+ _objc_msgSend$acOfferBadgeDurationBeforeEndDate
+ _objc_msgSend$acOfferDurationBeforeEndDate
+ _objc_msgSend$acOfferFollowupDisplayDate
+ _objc_msgSend$acOfferSettingsRowBadge
+ _objc_msgSend$account
+ _objc_msgSend$actionWithLabel:url:
+ _objc_msgSend$addBAAAuthenticationHeadersToRequest:withBody:error:
+ _objc_msgSend$addBAAAuthenticationHeadersWithBody:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addStoreLocaleHeaderIfNeededForAccount:
+ _objc_msgSend$aida_accountForPrimaryiCloudAccount
+ _objc_msgSend$aida_accountForiCloudAccount:
+ _objc_msgSend$aida_alternateDSID
+ _objc_msgSend$ak_addClientInfoHeader
+ _objc_msgSend$ak_addDeviceUDIDHeader
+ _objc_msgSend$allHTTPHeaderFields
+ _objc_msgSend$allKeys
+ _objc_msgSend$allObjects
+ _objc_msgSend$ams_iTunesAccountForAccount:
+ _objc_msgSend$ams_sharedAccountStore
+ _objc_msgSend$ams_storefront
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appleIDHeadersForRequest:
+ _objc_msgSend$apsSupportedOverride:
+ _objc_msgSend$array
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$clearNotificationForItem:error:
+ _objc_msgSend$clearPendingFollowUpItemsWithUniqueIdentifiers:error:
+ _objc_msgSend$compare:
+ _objc_msgSend$credentialForAccount:serviceID:
+ _objc_msgSend$date
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$deviceWithName:serialNumber:activationDate:deviceType:
+ _objc_msgSend$dictionaryForKey:
+ _objc_msgSend$displayStyle
+ _objc_msgSend$eligibilityEventId
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$firstObject
+ _objc_msgSend$followUpProvider
+ _objc_msgSend$generateBAACertficate:
+ _objc_msgSend$getBTDeviceInfosUsingPolicy:updateFollowUps:withReply:
+ _objc_msgSend$getBTPioneerDeviceInfosUsingPolicy:updateFollowUps:withReply:
+ _objc_msgSend$getPrimaryFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:
+ _objc_msgSend$initWithAccount:options:
+ _objc_msgSend$initWithClientIdentifier:
+ _objc_msgSend$initWithFollowUpProvider:
+ _objc_msgSend$initWithName:serialNumber:activationDate:deviceType:productID:productName:isICloudDevice:isVisibleInCC:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isICloudDevice
+ _objc_msgSend$isInternal
+ _objc_msgSend$isVisibleInCC
+ _objc_msgSend$localTimeZone
+ _objc_msgSend$localeIdentifier
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$mainBundle
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$options
+ _objc_msgSend$pendingFollowUpItems:
+ _objc_msgSend$performAuthentication
+ _objc_msgSend$postFollowUpItem:error:
+ _objc_msgSend$postFollowUpWithDeviceInfo:
+ _objc_msgSend$preferredLocale
+ _objc_msgSend$productName
+ _objc_msgSend$readAPSSupportedOverride:
+ _objc_msgSend$refreshFollowupWithDeviceInfos:clearUntrackedDeviceFollowups:andForcePostFollowup:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$renewCredentialsForAccount:options:completion:
+ _objc_msgSend$resultWithError:
+ _objc_msgSend$scIntervalFollowupEligible
+ _objc_msgSend$secondsFromGMT
+ _objc_msgSend$set
+ _objc_msgSend$setAcLocalizedGroupedOfferCTA:
+ _objc_msgSend$setAcLocalizedGroupedOfferFooterLabel:
+ _objc_msgSend$setAcLocalizedOfferLongLabel:
+ _objc_msgSend$setActions:
+ _objc_msgSend$setActivateAction:
+ _objc_msgSend$setAuthenticationType:
+ _objc_msgSend$setByAddingObjectsFromArray:
+ _objc_msgSend$setCacheValidityDuration:
+ _objc_msgSend$setClearAction:
+ _objc_msgSend$setDebugReason:
+ _objc_msgSend$setDisplayStyle:
+ _objc_msgSend$setDouble:forKey:
+ _objc_msgSend$setExpirationDate:
+ _objc_msgSend$setExtensionIdentifier:
+ _objc_msgSend$setFollowUpProvider:
+ _objc_msgSend$setFrequency:
+ _objc_msgSend$setGetSupportURL:
+ _objc_msgSend$setGroupIdentifier:
+ _objc_msgSend$setHTTPBody:
+ _objc_msgSend$setHTTPMethod:
+ _objc_msgSend$setIdentifier:
+ _objc_msgSend$setInformativeFooterText:
+ _objc_msgSend$setInformativeText:
+ _objc_msgSend$setIsAPSSupported:
+ _objc_msgSend$setIsICloudDevice:
+ _objc_msgSend$setIsVisibleInCC:
+ _objc_msgSend$setLabel:
+ _objc_msgSend$setMySupportURL:
+ _objc_msgSend$setNotification:
+ _objc_msgSend$setOptions:
+ _objc_msgSend$setProductName:
+ _objc_msgSend$setTargetBundleIdentifier:
+ _objc_msgSend$setTitle:
+ _objc_msgSend$setUniqueIdentifier:
+ _objc_msgSend$setUserInfo:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$setWithCapacity:
+ _objc_msgSend$setWithSet:
+ _objc_msgSend$sf_isInternalInstall
+ _objc_msgSend$showNotificationBeforeEndDate
+ _objc_msgSend$showNotificationToggle
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringWithCapacity:
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$token
+ _objc_msgSend$uniqueIdentfierForSerialNumber:
+ _objc_msgSend$uniqueIdentifier
+ _objc_msgSend$userInfo
+ _objc_msgSend$valueForHTTPHeaderField:
+ _objc_opt_new
+ _objc_retain_x26
+ _objc_retain_x27
+ _strlen
- +[NDODevice deviceWithName:serialNumber:activationDate:deviceType:productID:]
- -[NDODevice initWithName:serialNumber:activationDate:deviceType:productID:]
- -[NDOWarranty acOfferBadgeDaysBeforeEndDate]
- -[NDOWarranty setAcOfferBadgeDaysBeforeEndDate:]
- GCC_except_table19
- GCC_except_table28
- GCC_except_table31
- GCC_except_table34
- GCC_except_table40
- _OBJC_IVAR_$_NDOWarranty._acOfferBadgeDaysBeforeEndDate
- ___103-[NDOManager getDeviceInfoForSerialNumber:usingPolicy:sessionID:params:andForcePostFollowup:withReply:]_block_invoke.25
- ___27-[NDOManager defaultDevice]_block_invoke.17
- ___27-[NDOManager pairedWatches]_block_invoke.19
- ___29-[NDOManager pairedBTDevices]_block_invoke.21
- ___48-[NDOManager getDecodedParamsForPath:withReply:]_block_invoke.16
- ___56-[NDOManager dismissFollowUpForSerialNumber:completion:]_block_invoke.27
- ___56-[NDOManager getDefaultDeviceInfoUsingForceCachedPolicy]_block_invoke.22
- ___56-[NDOManager getDefaultDeviceInfoUsingPolicy:withReply:]_block_invoke.23
- ___60-[NDOManager dismissNotificationForSerialNumber:completion:]_block_invoke.28
- ___65-[NDOManager getDeviceInfoUsingForceCachedPolicyForSerialNumber:]_block_invoke.24
- ___80-[NDOManager getAllFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:]_block_invoke.26
- _objc_msgSend$initWithName:serialNumber:activationDate:deviceType:productID:
- _objc_msgSend$setAcOfferBadgeDaysBeforeEndDate:
- _objc_retain_x6
CStrings:
+ "\x13\x12"
+ "#16@0:8"
+ "%02x"
+ "%@ :: (%@) :: (%@) :: %@ - %@ :: (%@) :: %d :: %d"
+ "%@: %@ %@"
+ "%@_CachedWarrantyValidityDuration"
+ "%{public}s: %{private}@"
+ "%{public}s: BAA (UCRT) failed due to missing UCRT with error: %@, falling back to BAA (SCRT)"
+ "%{public}s: Device NOT eligible. Don't post a followup for %{private}@"
+ "%{public}s: Device NOT eligible. Remove the followup for %{private}@"
+ "%{public}s: Device eligible for re-post due to eligible event. Re-post the followup for %{private}@"
+ "%{public}s: Device eligible for re-post. Re-post the followup for %{private}@"
+ "%{public}s: Device eligible with future post date. Cannot post followup for %{private}@ on: %@"
+ "%{public}s: Device eligible. Post new  followup for %{private}@"
+ "%{public}s: Device eligible. Update the followup for %{private}@"
+ "%{public}s: Device no longer eligible. Don't post a followup for %{private}@"
+ "%{public}s: Device no longer eligible. Remove the followup for %{private}@"
+ "%{public}s: Error serializing plist file from URL '%@': %@"
+ "%{public}s: Failed to add Baa Headers with error: %@"
+ "%{public}s: Failed to convert: %{public}@"
+ "%{public}s: Failed to get reference key or cert!"
+ "%{public}s: Followup already dismissed for %{private}@, leaving unposted"
+ "%{public}s: Followup already dismissed/not present for %{private}@, leaving unposted"
+ "%{public}s: Followup already dismissed/not present/no eligible events found for %{private}@, leaving unposted"
+ "%{public}s: Found NULL attestation data!!"
+ "%{public}s: Initiating device authentication"
+ "%{public}s: Installation timed out after %d seconds"
+ "%{public}s: No warranty downloaded for device. Don't post a followup for %{private}@"
+ "%{public}s: No warranty downloaded for device. Remove the followup for %{private}@"
+ "%{public}s: NotificationDate: %@"
+ "%{public}s: Override isAPSSupported nil"
+ "%{public}s: Serial number is nil"
+ "%{public}s: Using initial postdate as it is later than FollowupDisplay Date"
+ "%{public}s: deviceIdentitySupported on this device:%d"
+ "%{public}s: error: %@"
+ "%{public}s: saving for event: %@ with events: %@"
+ "%{public}s: shouldShowNotification: %d"
+ "%{public}s: shouldShowRowBadge: %d"
+ "%{public}s: signatureDataString: %@\n certificateString: %@"
+ "+[NDOServerVersionUtilities readAPSSupportedOverride]"
+ "-[NDOFollowUp _postFollowUpWithDevicesInfo:repostAllowed:]_block_invoke"
+ "-[NDOFollowUp _setupFollowUpItem:withDeviceInfo:]"
+ "-[NDOFollowUp postFollowUpWithDeviceInfo:]"
+ "-[NDOFollowUp refreshFollowupWithDeviceInfos:clearUntrackedDeviceFollowups:andForcePostFollowup:]_block_invoke"
+ "-[NSMutableURLRequest(AccountHeaders) addBAAAuthenticationHeadersWithBody:]"
+ ".%@"
+ ".dismissed"
+ "/\x0f\x02\x13\x1f\v)"
+ "1"
+ "<%@/%@/%@>"
+ "<Missing serial number>"
+ "<Missing warranty>"
+ "@\"<NDOFollowUpProvider>\""
+ "@\"NSArray\"24@0:8^@16"
+ "@\"NSString\"16@0:8"
+ "@24@0:8:16"
+ "@24@0:8^@16"
+ "@28@0:8@16B24"
+ "@32@0:8:16@24"
+ "@32@0:8@16B24B28"
+ "@40@0:8:16@24@32"
+ "@64@0:8@16@24@32Q40@48@56"
+ "@68@0:8@16@24@32Q40@48@56B64"
+ "@72@0:8@16@24@32Q40@48@56B64B68"
+ "AccountHeaders"
+ "B20@0:8B16"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8B16B20"
+ "B28@0:8@16B24"
+ "B32@0:8@\"FLFollowUpItem\"16^@24"
+ "B32@0:8@\"NSArray\"16^@24"
+ "B32@0:8@16^@24"
+ "B40@0:8@16@24B32B36"
+ "BAA certificate generation success: %@"
+ "CLEAR_NOTIFICATION"
+ "CachedWarrantyValidityDuration"
+ "Cleared follow-up notification: %@ for item: %@"
+ "Cleared follow-up: %@"
+ "Clearing legacy followup, no legacy warranty was found.."
+ "Content-Type"
+ "Couldn't find an iTunesAccount"
+ "Couldn't find an iTunesAccount with error: %@"
+ "DETAILS"
+ "Device authentication failed while generating certificate with error: %@"
+ "Device authentication failed with error: %@"
+ "Device authentication successful"
+ "Device not eligible for conversion. %{private}@, followup dismissed date: %@, fup display date: %@"
+ "Dismissed follow-up: %@"
+ "Error clearing legacy follow-up: %@"
+ "Error loading pending follow-ups: %@"
+ "Error posting migrated follow-up: %@"
+ "Error: still no GS token even after calling renewCredentialsForAccount."
+ "FUP_ACTION_LABEL"
+ "Failed to add GS headers, can't sign this request"
+ "Failed to alloc clear action"
+ "Failed to alloc open action"
+ "Failed to post follow-up:%@%@"
+ "FollowupDismissedSerialNumberHashes"
+ "FollowupDisplayedSerialNumberHashesWithEvents"
+ "FollowupPostedSerialNumberHashes"
+ "FollowupSerialNumber"
+ "FollowupWarranty"
+ "GrandSlam signing failed because no GS account was provided."
+ "GrandSlam signing failed because no there's no altDSID on the account."
+ "HTTPBody"
+ "Localizable"
+ "Migrating legacy followup.."
+ "Missing acLocalizedOfferPluralDescFormat value"
+ "Missing acLocalizedOfferSingularDesc value"
+ "Missing eventID"
+ "NDODefaultFolllowUpProvider"
+ "NDOFollowUp"
+ "NDOFollowUpProvider"
+ "NDOUtilities"
+ "NSObject"
+ "No"
+ "No longer tracking device %{private}@, clearing"
+ "No primary iCloud account, can't sign this request"
+ "No way to sign request with GS token because renewal of GS credential failed: %ld, %@"
+ "Offer-ID"
+ "POST"
+ "Posted follow-up: serialNumber:%@ -> %@"
+ "Primary iCloud Account is nil!"
+ "ProductType"
+ "ProductVersion"
+ "Reposted follow-up: %@"
+ "Reprovision GS tokens"
+ "Retrying with silent authentication to get the itunes store account."
+ "SHA256Hash"
+ "T#,R"
+ "T@\"<NDOFollowUpProvider>\",&,V_followUpProvider"
+ "T@\"NSString\",&,V_acLocalizedGroupedOfferCTA"
+ "T@\"NSString\",&,V_acLocalizedGroupedOfferFooterLabel"
+ "T@\"NSString\",&,V_acLocalizedOfferLongLabel"
+ "T@\"NSString\",&,V_getSupportURL"
+ "T@\"NSString\",&,V_mySupportURL"
+ "T@\"NSString\",&,V_productName"
+ "T@\"NSString\",R,C"
+ "TB,V_isAPSSupported"
+ "TB,V_isICloudDevice"
+ "TB,V_isVisibleInCC"
+ "TQ,R"
+ "Td,V_cacheValidityDuration"
+ "UIPreferredContentSizeCategoryName"
+ "UUID"
+ "UUIDString"
+ "Updated follow-up: %@"
+ "User-Agent"
+ "Using overriden value %@"
+ "Vv16@0:8"
+ "X-Apple-Content-Size"
+ "X-Apple-DM"
+ "X-Apple-GS-Token"
+ "X-Apple-SN"
+ "X-Apple-Txn-ID"
+ "^{_NSZone=}16@0:8"
+ "_acLocalizedGroupedOfferCTA"
+ "_acLocalizedGroupedOfferFooterLabel"
+ "_acLocalizedOfferLongLabel"
+ "_addGSHeadersForAccount:withStore:forceReprovisioning:avoidUI:"
+ "_cacheValidityDuration"
+ "_checkConversionEligibilityForDevice:"
+ "_clearFollowUpForSerialNumber:"
+ "_clearFollowUpWithDevices:"
+ "_deviceProductType"
+ "_followUpProvider"
+ "_getSupportURL"
+ "_isAPSSupported"
+ "_isICloudDevice"
+ "_isVisibleInCC"
+ "_mySupportURL"
+ "_osVersion"
+ "_postFollowUpWithDevicesInfo:repostAllowed:"
+ "_productName"
+ "_setupFollowUpItem:withDeviceInfo:"
+ "_setupFollowUpNotificationWithDeviceInfo:"
+ "_userAgent"
+ "_userAgentWithBundleID:"
+ "aa_altDSID"
+ "acLocalizedGroupedOfferCTA"
+ "acLocalizedGroupedOfferFooterLabel"
+ "acLocalizedOfferLongLabel"
+ "account"
+ "actionWithLabel:url:"
+ "addBAAAuthenticationHeadersWithBody:"
+ "addBAAAuthenticationHeadersWithSerialNumber:"
+ "addObjectsFromArray:"
+ "addStoreLocaleHeaderIfNeededForAccount:"
+ "aida_accountForPrimaryiCloudAccount"
+ "aida_accountForiCloudAccount:"
+ "aida_alternateDSID"
+ "ak_addClientInfoHeader"
+ "ak_addDeviceUDIDHeader"
+ "allFUPEligibleDevices:"
+ "allHTTPHeaderFields"
+ "allKeys"
+ "allObjects"
+ "altDSID"
+ "ams_iTunesAccountForAccount:"
+ "ams_sharedAccountStore"
+ "ams_storefront"
+ "appendFormat:"
+ "appleIDHeadersForRequest:"
+ "application/json"
+ "apsSupportedOverride : %@"
+ "apsSupportedOverride:"
+ "array"
+ "arrayWithArray:"
+ "autorelease"
+ "bodyDescription"
+ "bundleIdentifier"
+ "cacheTtlMinutes"
+ "cacheValidityDuration"
+ "class"
+ "clearNotificationForItem:error:"
+ "clearPendingFollowUpItemsWithUniqueIdentifiers:error:"
+ "com.apple.NewDeviceOutreach.Extension"
+ "com.apple.UIKit"
+ "com.apple.gs.supportapp.auth"
+ "com.apple.newdeviceoutreach.followupDisplayCount"
+ "com.followup.ndo_followup_open_action"
+ "com.followup.ndo_notification_clear_action"
+ "com.followup.ndo_notification_open_action"
+ "compare:"
+ "conformsToProtocol:"
+ "credentialForAccount:serviceID:"
+ "date"
+ "debugDescription"
+ "decodeBoolForKey:"
+ "deviceWithName:serialNumber:activationDate:deviceType:productID:productName:"
+ "deviceWithName:serialNumber:activationDate:deviceType:productID:productName:isICloudDevice:"
+ "deviceWithName:serialNumber:activationDate:deviceType:productID:productName:isVisibleInCC:"
+ "devicetype"
+ "dictionaryForKey:"
+ "dismissFollowUpForSerialNumber:"
+ "dismissNotificationForSerialNumber:"
+ "displayStyle"
+ "displayedEvents"
+ "eligible until %@"
+ "empty"
+ "encodeBool:forKey:"
+ "enumerateObjectsUsingBlock:"
+ "firstObject"
+ "followUpProvider"
+ "getBTDeviceInfosUsingPolicy:updateFollowUps:withReply:"
+ "getBTPioneerDeviceInfosUsingPolicy:updateFollowUps:withReply:"
+ "getPrimaryFUPEligibleDeviceInfosUsingPolicy:updateFollowUps:withReply:"
+ "getSupportURL"
+ "has warranty"
+ "hash"
+ "headerDescription"
+ "initWithAccount:options:"
+ "initWithClientIdentifier:"
+ "initWithFollowUpProvider:"
+ "initWithName:serialNumber:activationDate:deviceType:productID:productName:isICloudDevice:isVisibleInCC:"
+ "isAPSSupported"
+ "isAPSSupportedOverrideWithServerValue:"
+ "isEqualToString:"
+ "isICloudDevice"
+ "isInternal"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "isVisibleInCC"
+ "localTimeZone"
+ "locale"
+ "localeIdentifier"
+ "localizedStringForKey:value:table:"
+ "mainBundle"
+ "migrateLegacyFollowUpIfNeededWithDeviceInfo:"
+ "missing warranty"
+ "mySupportURL"
+ "ndo_addBasicHeadersWithBundleID:"
+ "ndo_addOASHeadersWithOfferID:serialNumber:primarySerialNumber:"
+ "ndo_setCoverageRequestBodyWithSerialNumber:primarySerialNumber:displayedEvents:"
+ "ndo_signWithAccountHeaders:avoidUI:"
+ "numberWithInt:"
+ "numberWithUnsignedLongLong:"
+ "options"
+ "paired BTDevices : %{private}@"
+ "pairedBTPioneerDevices:"
+ "pendingFollowUpCount"
+ "pendingFollowUpItems:"
+ "performAuthentication"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "postFollowUpItem:error:"
+ "postFollowUpWithDeviceInfo:"
+ "postFollowUpWithDevicesInfo:"
+ "preferredLocale"
+ "primaryFUPEligibleDevices:"
+ "productName"
+ "readAPSSupportedOverride"
+ "readAPSSupportedOverride:"
+ "refreshALLFollowupsWithDeviceInfos:andForcePostFollowup:"
+ "refreshFollowupWithDeviceInfo:andForcePostFollowup:"
+ "refreshFollowupWithDeviceInfos:andForcePostFollowup:"
+ "refreshFollowupWithDeviceInfos:clearUntrackedDeviceFollowups:andForcePostFollowup:"
+ "release"
+ "removeObject:"
+ "renewCredentialsForAccount:options:completion:"
+ "requestTimestamp"
+ "requestTimezone"
+ "respondsToSelector:"
+ "resultWithError:"
+ "retain"
+ "retainCount"
+ "secondsFromGMT"
+ "self"
+ "set"
+ "setAcLocalizedGroupedOfferCTA:"
+ "setAcLocalizedGroupedOfferFooterLabel:"
+ "setAcLocalizedOfferLongLabel:"
+ "setActions:"
+ "setActivateAction:"
+ "setAuthenticationType:"
+ "setByAddingObjectsFromArray:"
+ "setCacheValidityDuration:"
+ "setClearAction:"
+ "setDebugReason:"
+ "setDisplayStyle:"
+ "setDouble:forKey:"
+ "setExpirationDate:"
+ "setExtensionIdentifier:"
+ "setFollowUpProvider:"
+ "setFrequency:"
+ "setGetSupportURL:"
+ "setGroupIdentifier:"
+ "setHTTPBody:"
+ "setHTTPMethod:"
+ "setIdentifier:"
+ "setInformativeFooterText:"
+ "setInformativeText:"
+ "setIsAPSSupported:"
+ "setIsICloudDevice:"
+ "setIsVisibleInCC:"
+ "setLabel:"
+ "setMySupportURL:"
+ "setNotification:"
+ "setOptions:"
+ "setProductName:"
+ "setTargetBundleIdentifier:"
+ "setTitle:"
+ "setUniqueIdentifier:"
+ "setUserInfo:"
+ "setWithArray:"
+ "setWithCapacity:"
+ "setWithSet:"
+ "sf_isInternalInstall"
+ "storeLocale %@"
+ "storeLocale already set to %@"
+ "storefrontLocale"
+ "stringByAppendingFormat:"
+ "stringByAppendingString:"
+ "stringWithCapacity:"
+ "stringWithString:"
+ "success"
+ "superclass"
+ "timeIntervalSince1970"
+ "token"
+ "uniqueIdentfierForSerialNumber:"
+ "uniqueIdentifier"
+ "userInfo"
+ "v24@?0q8@\"NSError\"16"
+ "v32@?0@\"NDODevice\"8Q16^B24"
+ "v32@?0@\"NDODeviceInfo\"8Q16^B24"
+ "v32@?0@\"NSArray\"8@16@\"NSError\"24"
+ "v40@0:8@16@24@32"
+ "valueForHTTPHeaderField:"
+ "visonpro"
+ "x-apple-bundle-id"
+ "x-apple-os-version"
+ "x-apple-primary-device-model"
+ "x-apple-primary-sn"
+ "zone"
- "\x03\x11"
- "%@ :: (%@) :: (%@) :: %@ - %@"
- "%@: %@"
- "%s: BAA (UCRT) failed due to missing UCRT with error: %@, falling back to BAA (SCRT)"
- "%s: Error serializing plist file from URL '%@': %@"
- "%s: Failed to add Baa Headers with error: %@"
- "%s: Failed to convert: %{public}@"
- "%s: Failed to get reference key or cert!"
- "%s: Found NULL attestation data!!"
- "%s: Installation timed out after %d seconds"
- "%s: deviceIdentitySupported on this device:%d"
- "%s: error: %@"
- "%s: signatureDataString: %@\n certificateString: %@"
- "/\x0e\x13\x1f\f\x17"
- "@56@0:8@16@24@32Q40@48"
- "Eligible until %@"
- "T@\"NSNumber\",&,V_acOfferBadgeDaysBeforeEndDate"
- "_acOfferBadgeDaysBeforeEndDate"
- "acOfferBadgeDaysBeforeEndDate"
- "deviceWithName:serialNumber:activationDate:deviceType:productID:"
- "initWithName:serialNumber:activationDate:deviceType:productID:"
- "setAcOfferBadgeDaysBeforeEndDate:"

```
