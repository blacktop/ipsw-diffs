## uarpassetmanagerd

> `/usr/libexec/uarpassetmanagerd`

```diff

-1338.60.22.0.0
-  __TEXT.__text: 0x25908
-  __TEXT.__auth_stubs: 0x490
-  __TEXT.__objc_stubs: 0x22a0
-  __TEXT.__objc_methlist: 0x1124
-  __TEXT.__cstring: 0x2830
-  __TEXT.__oslogstring: 0x1608
-  __TEXT.__objc_methname: 0x28aa
-  __TEXT.__objc_classname: 0x2db
-  __TEXT.__objc_methtype: 0x80f
-  __TEXT.__gcc_except_tab: 0x1a0
-  __TEXT.__unwind_info: 0x360
-  __DATA_CONST.__auth_got: 0x258
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x1f38
-  __DATA_CONST.__cfstring: 0x27c0
-  __DATA_CONST.__objc_classlist: 0x78
+1338.80.29.0.0
+  __TEXT.__text: 0x28abc
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__objc_stubs: 0x2480
+  __TEXT.__objc_methlist: 0x1284
+  __TEXT.__cstring: 0x29c7
+  __TEXT.__oslogstring: 0x1788
+  __TEXT.__objc_methname: 0x2b79
+  __TEXT.__objc_classname: 0x2fe
+  __TEXT.__objc_methtype: 0x829
+  __TEXT.__gcc_except_tab: 0x1ac
+  __TEXT.__unwind_info: 0x388
+  __DATA_CONST.__auth_got: 0x270
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__const: 0x21f8
+  __DATA_CONST.__cfstring: 0x2860
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2b50
-  __DATA.__objc_selrefs: 0xae0
-  __DATA.__objc_ivar: 0x160
-  __DATA.__objc_data: 0x4b0
+  __DATA.__objc_const: 0x2d18
+  __DATA.__objc_selrefs: 0xb68
+  __DATA.__objc_ivar: 0x178
+  __DATA.__objc_data: 0x500
   __DATA.__data: 0x480
   __DATA.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2C98DDA8-3C2B-32C9-A385-723E5798D15E
-  Functions: 416
-  Symbols:   4926
-  CStrings:  1431
+  UUID: C8833504-7E9F-3DA8-9FB6-472CE90FCDFF
+  Functions: 448
+  Symbols:   5297
+  CStrings:  1484
 
Symbols:
+ +[UARPAssetSubscriptionMobileAssetSU supportsSecureCoding]
+ -[UARPAssetManagerController handleNotification:]
+ -[UARPAssetManagerServiceInstance checkForUpdate:]
+ -[UARPAssetManagerServiceInstance createPersonality:]
+ -[UARPAssetManagerServiceInstance softwareUpdateAudienceChange]
+ -[UARPAssetManagerServiceInstance unregisterForSubscription:]
+ -[UARPAssetManagerServiceInstanceMobileAsset createPersonality:]
+ -[UARPAssetManagerServiceInstanceMobileAsset softwareUpdateAudienceChange]
+ -[UARPAssetManagerServiceManager checkForUpdate:]
+ -[UARPAssetManagerServiceManager softwareUpdateAudienceChange]
+ -[UARPAssetSubscriptionMobileAssetSU .cxx_destruct]
+ -[UARPAssetSubscriptionMobileAssetSU activeVersion]
+ -[UARPAssetSubscriptionMobileAssetSU copyWithZone:]
+ -[UARPAssetSubscriptionMobileAssetSU description]
+ -[UARPAssetSubscriptionMobileAssetSU encodeWithCoder:]
+ -[UARPAssetSubscriptionMobileAssetSU forceInstall]
+ -[UARPAssetSubscriptionMobileAssetSU hash]
+ -[UARPAssetSubscriptionMobileAssetSU initWithAppleModelNumber:hwFusing:domain:activeVersion:internalVersion:internalVariant:]
+ -[UARPAssetSubscriptionMobileAssetSU initWithCoder:]
+ -[UARPAssetSubscriptionMobileAssetSU internalVariant]
+ -[UARPAssetSubscriptionMobileAssetSU internalVersion]
+ -[UARPAssetSubscriptionMobileAssetSU isEqual:]
+ -[UARPAssetSubscriptionMobileAssetSU isEqualForAnyDomain:]
+ -[UARPAssetSubscriptionMobileAssetSU setForceInstall:]
+ -[UARPAssetSubscriptionMobileAssetSU setInternalVariant:]
+ -[UARPAssetSubscriptionMobileAssetSU setSoftwareUpdateDefaultAssetAudience:]
+ -[UARPAssetSubscriptionMobileAssetSU softwareUpdateDefaultAssetAudience]
+ -[UARPSettingsAccessory forceInstall]
+ -[UARPSettingsAccessory setForceInstall:]
+ -[UARPSettingsAccessory setSoftwareUpdateAssetType:]
+ -[UARPSettingsAccessory setSoftwareUpdateEraseInstall:]
+ -[UARPSettingsAccessory softwareUpdateAssetType]
+ -[UARPSettingsAccessory softwareUpdateEraseInstall]
+ /Library/Caches/com.apple.xbs/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetSubscriptionMobileAssetSU.o
+ /Library/Caches/com.apple.xbs/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Common/MobileAssetSubscriptions/
+ OBJC_IVAR_$_UARPAssetSubscriptionMobileAssetSU._activeVersion
+ OBJC_IVAR_$_UARPAssetSubscriptionMobileAssetSU._forceInstall
+ OBJC_IVAR_$_UARPAssetSubscriptionMobileAssetSU._internalVariant
+ OBJC_IVAR_$_UARPAssetSubscriptionMobileAssetSU._internalVersion
+ OBJC_IVAR_$_UARPAssetSubscriptionMobileAssetSU._softwareUpdateDefaultAssetAudience
+ OBJC_IVAR_$_UARPSettingsAccessory._forceInstall
+ OBJC_IVAR_$_UARPSettingsAccessory._softwareUpdateAssetType
+ OBJC_IVAR_$_UARPSettingsAccessory._softwareUpdateEraseInstall
+ UARPAssetSubscriptionMobileAssetSU.m
+ _MAGetPallasAudience
+ _OBJC_CLASS_$_UARPAssetSubscriptionMobileAssetSU
+ _OBJC_METACLASS_$_UARPAssetSubscriptionMobileAssetSU
+ __44-[UARPAssetManagerServiceInstance copyCache]_block_invoke.361
+ __46-[UARPAssetManagerServiceInstance primeCache:]_block_invoke.378
+ __46-[UARPAssetManagerServiceInstance queryIsBusy]_block_invoke.367
+ __50-[UARPAssetManagerServiceInstance checkForUpdate:]_block_invoke.366
+ __52-[UARPAssetManagerServiceInstance copySubscriptions]_block_invoke.363
+ __59-[UARPAssetManagerServiceInstance registerForSubscription:]_block_invoke.365
+ __60-[UARPAssetManagerServiceInstance clearAssetCacheForDomain:]_block_invoke.376
+ __61-[UARPAssetManagerServiceInstance checkCacheForSubscription:]_block_invoke.358
+ __70-[UARPAssetManagerServiceInstance listener:shouldAcceptNewConnection:]_block_invoke.332
+ __OBJC_$_CLASS_METHODS_UARPAssetSubscriptionMobileAssetSU
+ __OBJC_$_INSTANCE_METHODS_UARPAssetSubscriptionMobileAssetSU
+ __OBJC_$_INSTANCE_VARIABLES_UARPAssetSubscriptionMobileAssetSU
+ __OBJC_$_PROP_LIST_UARPAssetSubscriptionMobileAssetSU
+ __OBJC_CLASS_RO_$_UARPAssetSubscriptionMobileAssetSU
+ __OBJC_METACLASS_RO_$_UARPAssetSubscriptionMobileAssetSU
+ ___50-[UARPAssetManagerController initWithIdleTimeout:]_block_invoke_3
+ ___50-[UARPAssetManagerServiceInstance checkForUpdate:]_block_invoke
+ ___61-[UARPAssetManagerServiceInstance unregisterForSubscription:]_block_invoke
+ ___block_descriptor_40_e8_32w_e33_v16?0"NSObject<OS_xpc_object>"8lw32l8
+ ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
+ ___kCFBooleanTrue
+ ___os_log_helper_16_2_4_8_32_8_64_8_64_8_64
+ __xpc_event_key_name
+ _compareOSVersion
+ _kAUSettingsLocationPallasSUDefault
+ _kAccessoryForceInstallKey
+ _kPallasInternalAssetVariantKey
+ _kPallasSoftwareUpdateAssetTypeKey
+ _kPallasSoftwareUpdateEraseInstallKey
+ _kUARPAssetSubscriptionMobileAssetEncoderKeyActiveVersion
+ _kUARPAssetSubscriptionMobileAssetEncoderKeyForceInstall
+ _kUARPAssetSubscriptionMobileAssetEncoderKeyInternalVariant
+ _kUARPAssetSubscriptionMobileAssetEncoderKeyInternalVersion
+ _kUARPAssetSubscriptionMobileAssetEncoderKeySUDefaultAudience
+ _mobileAssetNewerThanRestoreVersion
+ _mobileAssetPrefixForSubscription
+ _notify_post
+ _objc_msgSend$assetManagerService
+ _objc_msgSend$checkForAssetUpdate:
+ _objc_msgSend$checkForUpdate:
+ _objc_msgSend$createPersonality:
+ _objc_msgSend$forceInstall
+ _objc_msgSend$handleNotification:
+ _objc_msgSend$initWithAppleModelNumber:hwFusing:domain:activeVersion:internalVersion:internalVariant:
+ _objc_msgSend$internalVariant
+ _objc_msgSend$internalVersion
+ _objc_msgSend$restoreVersion
+ _objc_msgSend$setForceInstall:
+ _objc_msgSend$setInternalVariant:
+ _objc_msgSend$setSoftwareUpdateAssetType:
+ _objc_msgSend$setSoftwareUpdateDefaultAssetAudience:
+ _objc_msgSend$setSoftwareUpdateEraseInstall:
+ _objc_msgSend$softwareUpdateAudienceChange
+ _objc_msgSend$softwareUpdateDefaultAssetAudience
+ _objc_msgSend$unsubscribeForAsset:
+ _setPallasAudienceForSubscription
+ _xpc_set_event_stream_handler
- -[UARPAssetManagerServiceInstance checkForUpdate]
- -[UARPAssetManagerServiceManager checkForUpdate]
- -[UARPAssetSubscriptionMobileAsset internalAsset]
- -[UARPAssetSubscriptionMobileAsset setInternalAsset:]
- -[UARPAssetSubscriptionMobileAsset setSoftwareUpdateAsset:]
- -[UARPAssetSubscriptionMobileAsset softwareUpdateAsset]
- OBJC_IVAR_$_UARPAssetSubscriptionMobileAsset._internalAsset
- OBJC_IVAR_$_UARPAssetSubscriptionMobileAsset._softwareUpdateAsset
- _INTERNAL_PALLAS_SERVER_URL_V2_AUTH
- _MA_PALLAS_AUDIENCE_CUSTOMER_SEASHIP
- _MA_PALLAS_AUDIENCE_INTERNAL_SEASHIP
- __44-[UARPAssetManagerServiceInstance copyCache]_block_invoke.369
- __46-[UARPAssetManagerServiceInstance primeCache:]_block_invoke.389
- __46-[UARPAssetManagerServiceInstance queryIsBusy]_block_invoke.375
- __49-[UARPAssetManagerServiceInstance checkForUpdate]_block_invoke.374
- __52-[UARPAssetManagerServiceInstance copySubscriptions]_block_invoke.371
- __59-[UARPAssetManagerServiceInstance registerForSubscription:]_block_invoke.373
- __60-[UARPAssetManagerServiceInstance clearAssetCacheForDomain:]_block_invoke.384
- __61-[UARPAssetManagerServiceInstance checkCacheForSubscription:]_block_invoke.366
- __70-[UARPAssetManagerServiceInstance listener:shouldAcceptNewConnection:]_block_invoke.341
- ___49-[UARPAssetManagerServiceInstance checkForUpdate]_block_invoke
- ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
- ___kCFBooleanFalse
- _getPallasAudienceForAccessory
- _kPallasInternalAssetVariant
- _kUARPAssetSubscriptionMobileAssetEncoderKeyInternalAsset
- _kUARPAssetSubscriptionMobileAssetEncoderKeySUAsset
- _mobileAssetPrefixForAppleModelNumber
- _objc_msgSend$checkForUpdate
- _objc_msgSend$internalAsset
- _objc_msgSend$setInternalAsset:
CStrings:
+ "%@ Unregistering for subscription:%{public}@"
+ "%s: Asset version %@ not comparable with %@"
+ "%s: Checking audience for subscription: %{public}@"
+ "%s: Error setting continue status for activity: %s"
+ "%s: Error setting done status for activity: %s"
+ "%s: OS Version check failed %@ <= %@ <= %@"
+ "%s: Updating audience for subscription: %{public}@"
+ "-[UARPAssetManagerServiceInstance createPersonality:]"
+ "-[UARPAssetManagerServiceInstance softwareUpdateAudienceChange]"
+ "-[UARPAssetManagerServiceInstanceMobileAsset softwareUpdateAudienceChange]"
+ "<%@: modelNumber=%@, hwFusing=%@ assetLocation=%@ domain=%@>"
+ "<%@: modelNumber=%@, hwFusing=%@ assetLocation=%@/%u activeVersion=%@/%u variant=%u force=%u domain=%@>"
+ "@56@0:8@16@24@32@40B48B52"
+ "LuckDSeed"
+ "Received notification %@"
+ "SU Default Audience"
+ "SU_DEFAULT"
+ "TB,R,V_forceInstall"
+ "TB,R,V_internalVersion"
+ "TB,R,V_softwareUpdateAssetType"
+ "TB,R,V_softwareUpdateEraseInstall"
+ "TB,V_forceInstall"
+ "TB,V_internalVariant"
+ "TB,V_softwareUpdateDefaultAssetAudience"
+ "UARPAssetSubscriptionMobileAssetSU"
+ "Unexpected notification %@"
+ "_forceInstall"
+ "_internalVariant"
+ "_internalVersion"
+ "_softwareUpdateAssetType"
+ "_softwareUpdateDefaultAssetAudience"
+ "_softwareUpdateEraseInstall"
+ "checkForAssetUpdate:"
+ "checkForUpdate:"
+ "com.apple.notifyd.matching"
+ "createPersonality:"
+ "forceInstall"
+ "handleNotification:"
+ "initWithAppleModelNumber:hwFusing:domain:activeVersion:internalVersion:internalVariant:"
+ "internalVariant"
+ "internalVersion"
+ "mobileAssetNewerThanRestoreVersion"
+ "restoreVersion"
+ "setForceInstall:"
+ "setInternalVariant:"
+ "setSoftwareUpdateAssetType:"
+ "setSoftwareUpdateDefaultAssetAudience:"
+ "setSoftwareUpdateEraseInstall:"
+ "softwareUpdateAssetType"
+ "softwareUpdateAudienceChange"
+ "softwareUpdateDefaultAssetAudience"
+ "softwareUpdateEraseInstall"
+ "softwareupdate.externalupdateschanged"
+ "softwareupdate.scantriggered"
+ "suAssetType"
+ "suDefaultAssetAudience"
+ "suEraseInstall"
+ "uarpdisplayd"
+ "unregisterForSubscription:"
+ "unsubscribeForAsset:"
- "<%@: modelNumber=%@, hwFusing=%@ assetLocation=%@ internal/su=%u/%u domain=%@>"
- "A2525"
- "LuckC"
- "TB,V_internalAsset"
- "TB,V_softwareUpdateAsset"
- "_internalAsset"
- "_softwareUpdateAsset"
- "cd060049-2465-43e3-bbb5-d769a66da2d7"
- "checkForUpdate"
- "ffc25f86-b83c-4139-b8ad-91131d0e5429"
- "https://gdmf-auth-stg.apple.com/v2/assets"
- "internalAsset"
- "setInternalAsset:"
- "suAsset"

```
