## uarpassetmanagerd

> `/usr/libexec/uarpassetmanagerd`

```diff

-  __TEXT.__text: 0x2b210
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_stubs: 0x26a0
-  __TEXT.__objc_methlist: 0x12bc
-  __TEXT.__cstring: 0x2d25
-  __TEXT.__oslogstring: 0x1969
-  __TEXT.__objc_methname: 0x2c0a
-  __TEXT.__objc_classname: 0x2e4
-  __TEXT.__objc_methtype: 0x837
+  __TEXT.__text: 0x2ebbc
+  __TEXT.__auth_stubs: 0x520
+  __TEXT.__objc_stubs: 0x2800
+  __TEXT.__objc_methlist: 0x1494
+  __TEXT.__cstring: 0x308a
+  __TEXT.__oslogstring: 0x1acc
+  __TEXT.__objc_methname: 0x2ee8
+  __TEXT.__objc_classname: 0x341
+  __TEXT.__objc_methtype: 0x894
   __TEXT.__gcc_except_tab: 0x11c
-  __TEXT.__unwind_info: 0x3b8
-  __DATA_CONST.__const: 0x2870
-  __DATA_CONST.__cfstring: 0x2c20
-  __DATA_CONST.__objc_classlist: 0x80
+  __TEXT.__unwind_info: 0x3f8
+  __DATA_CONST.__const: 0x2ce8
+  __DATA_CONST.__cfstring: 0x2fa0
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x290
-  __DATA_CONST.__got: 0x190
-  __DATA.__objc_const: 0x2d48
-  __DATA.__objc_selrefs: 0xba0
-  __DATA.__objc_ivar: 0x17c
-  __DATA.__objc_data: 0x500
+  __DATA_CONST.__auth_got: 0x2a0
+  __DATA_CONST.__got: 0x1a0
+  __DATA.__objc_const: 0x3090
+  __DATA.__objc_selrefs: 0xc08
+  __DATA.__objc_ivar: 0x19c
+  __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x480
   __DATA.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 473
-  Symbols:   5807
-  CStrings:  1570
+  Functions: 516
+  Symbols:   6371
+  CStrings:  1668
 
Sections:
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
Symbols:
+ +[UARPAssetCacheRecordiCloud supportsSecureCoding]
+ +[UARPAssetSubscriptioniCloud supportsSecureCoding]
+ -[UARPAssetCacheRecordiCloud .cxx_destruct]
+ -[UARPAssetCacheRecordiCloud assetHash]
+ -[UARPAssetCacheRecordiCloud containerID]
+ -[UARPAssetCacheRecordiCloud copyWithZone:]
+ -[UARPAssetCacheRecordiCloud description]
+ -[UARPAssetCacheRecordiCloud encodeWithCoder:]
+ -[UARPAssetCacheRecordiCloud hash]
+ -[UARPAssetCacheRecordiCloud initWithAssetVersion:containerID:assetURL:assetHash:deploymentRules:]
+ -[UARPAssetCacheRecordiCloud initWithCoder:]
+ -[UARPAssetCacheRecordiCloud isEqual:]
+ -[UARPAssetManagerController getAssetURLForPersonality:releaseNotes:]
+ -[UARPAssetManagerListener getAssetURLForPersonality:releaseNotes:reply:]
+ -[UARPAssetManagerServiceInstance checkCacheForPersonality:releaseNotes:]
+ -[UARPAssetManagerServiceInstance createSubscriptionForPrimeCache:]
+ -[UARPAssetManagerServiceInstanceMobileAsset checkCacheForPersonality:releaseNotes:]
+ -[UARPAssetManagerServiceInstanceiCloud .cxx_destruct]
+ -[UARPAssetManagerServiceInstanceiCloud assetAvailabilityUpdateForPersonality:assetVersion:creationDate:status:]
+ -[UARPAssetManagerServiceInstanceiCloud assetAvailabilityUpdateForSubscription:cacheRecord:asyncUpdate:]
+ -[UARPAssetManagerServiceInstanceiCloud assetType]
+ -[UARPAssetManagerServiceInstanceiCloud checkCacheForPersonality:releaseNotes:]
+ -[UARPAssetManagerServiceInstanceiCloud createPersonality:]
+ -[UARPAssetManagerServiceInstanceiCloud createSubscriptionForPrimeCache:]
+ -[UARPAssetManagerServiceInstanceiCloud encodedClasses]
+ -[UARPAssetManagerServiceInstanceiCloud initWithServiceName:delegate:]
+ -[UARPAssetManagerServiceInstanceiCloud isSubscriptionSupported:]
+ -[UARPAssetManagerServiceInstanceiCloud subscribeForPersonality:]
+ -[UARPAssetManagerServiceManager checkCacheForPersonality:releaseNotes:]
+ -[UARPAssetSubscriptioniCloud .cxx_destruct]
+ -[UARPAssetSubscriptioniCloud containerID]
+ -[UARPAssetSubscriptioniCloud copyWithZone:]
+ -[UARPAssetSubscriptioniCloud description]
+ -[UARPAssetSubscriptioniCloud downloadOnCellularAllowed]
+ -[UARPAssetSubscriptioniCloud encodeWithCoder:]
+ -[UARPAssetSubscriptioniCloud hash]
+ -[UARPAssetSubscriptioniCloud initWithCoder:]
+ -[UARPAssetSubscriptioniCloud initWithProductGroup:productNumber:containerID:releaseNotesAsset:downloadOnCellularAllowed:domain:]
+ -[UARPAssetSubscriptioniCloud isEqual:]
+ -[UARPAssetSubscriptioniCloud productGroup]
+ -[UARPAssetSubscriptioniCloud productNumber]
+ -[UARPAssetSubscriptioniCloud releaseNotesAsset]
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUDPreferences.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUDeveloperSettingsDatabase.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUDeveloperSettingsUtils.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUHelperInstance.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUHelperStrings.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUInternalSettingsStrings.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUStrings.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/NSUserDefaults+AUHelper.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/SandboxingSupport.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetCacheRecord.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetCacheRecordiCloud.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerController.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerListener.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceInstance-e10280a33acbb8b27d6f0c20fcde95e0.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceInstanceMobileAsset.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceInstanceiCloud.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceManager.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceTypes.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerSettingsListener.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerStrings.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetSubscription.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetSubscriptionMobileAsset.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetSubscriptionMobileAssetSU.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetSubscriptioniCloud.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAsyncAssetManagerUtils.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPDeploymentRule.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPDeploymentRuleConfig.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPError.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPSandboxExtension.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPSettingsAccessory.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/main.o
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Sources/AppleAccessoryManager/AUDeveloperSettings/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Common/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Common/Cache/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Common/MobileAssetSubscriptions/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Daemon/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Daemon/ServiceManager/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Sources/AppleAccessoryManager/CommonCode/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Sources/AppleAccessoryManager/CoreUARP/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Sources/AppleAccessoryManager/MobileAccessoryUpdater/AUHelper/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Sources/AppleAccessoryManager/MobileAccessoryUpdater/AUHelper/helpers/
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xqrN9K/Sources/AppleAccessoryManager/MobileAccessoryUpdater/fud/
+ GCC_except_table18
+ OBJC_IVAR_$_UARPAssetCacheRecordiCloud._assetHash
+ OBJC_IVAR_$_UARPAssetCacheRecordiCloud._containerID
+ OBJC_IVAR_$_UARPAssetManagerServiceInstanceiCloud._log
+ OBJC_IVAR_$_UARPAssetSubscriptioniCloud._containerID
+ OBJC_IVAR_$_UARPAssetSubscriptioniCloud._downloadOnCellularAllowed
+ OBJC_IVAR_$_UARPAssetSubscriptioniCloud._productGroup
+ OBJC_IVAR_$_UARPAssetSubscriptioniCloud._productNumber
+ OBJC_IVAR_$_UARPAssetSubscriptioniCloud._releaseNotesAsset
+ UARPAssetCacheRecordiCloud.m
+ UARPAssetManagerServiceInstanceiCloud.m
+ UARPAssetSubscriptioniCloud.m
+ _CFPreferencesCopyAppValue
+ _OBJC_CLASS_$_UARPAssetCacheRecordiCloud
+ _OBJC_CLASS_$_UARPAssetManagerServiceInstanceiCloud
+ _OBJC_CLASS_$_UARPAssetSubscriptioniCloud
+ _OBJC_CLASS_$_UARPEndpointPersonalityiCloud
+ _OBJC_METACLASS_$_UARPAssetCacheRecordiCloud
+ _OBJC_METACLASS_$_UARPAssetManagerServiceInstanceiCloud
+ _OBJC_METACLASS_$_UARPAssetSubscriptioniCloud
+ _UARPiCloudPublicContainerBetaKey
+ _UARPiCloudPublicContainerKey
+ _UARPiCloudPublicContainerUATKey
+ _UARPiCloudStagingContainerBetaKey
+ _UARPiCloudStagingContainerKey
+ _UARPiCloudStagingContainerUATKey
+ __61-[UARPAssetManagerServiceInstance unregisterForSubscription:]_block_invoke
+ __OBJC_$_CLASS_METHODS_UARPAssetCacheRecordiCloud
+ __OBJC_$_CLASS_METHODS_UARPAssetSubscriptioniCloud
+ __OBJC_$_INSTANCE_METHODS_UARPAssetCacheRecordiCloud
+ __OBJC_$_INSTANCE_METHODS_UARPAssetManagerServiceInstanceiCloud
+ __OBJC_$_INSTANCE_METHODS_UARPAssetSubscriptioniCloud
+ __OBJC_$_INSTANCE_VARIABLES_UARPAssetCacheRecordiCloud
+ __OBJC_$_INSTANCE_VARIABLES_UARPAssetManagerServiceInstanceiCloud
+ __OBJC_$_INSTANCE_VARIABLES_UARPAssetSubscriptioniCloud
+ __OBJC_$_PROP_LIST_UARPAssetCacheRecordiCloud
+ __OBJC_$_PROP_LIST_UARPAssetSubscriptioniCloud
+ __OBJC_CLASS_RO_$_UARPAssetCacheRecordiCloud
+ __OBJC_CLASS_RO_$_UARPAssetManagerServiceInstanceiCloud
+ __OBJC_CLASS_RO_$_UARPAssetSubscriptioniCloud
+ __OBJC_METACLASS_RO_$_UARPAssetCacheRecordiCloud
+ __OBJC_METACLASS_RO_$_UARPAssetManagerServiceInstanceiCloud
+ __OBJC_METACLASS_RO_$_UARPAssetSubscriptioniCloud
+ ___55-[UARPAssetManagerServiceInstance releaseXPCConnection]_block_invoke
+ ___block_descriptor_40_e8_32s_e5_v8?0l
+ ___os_log_helper_16_0_1_8_2
+ ___os_log_helper_16_2_4_8_32_8_64_8_64_4_0
+ _containerIDForAssetContainerType
+ _createPersonalityForiCloudSubscription
+ _createiCloudEndpointPersonality
+ _createiCloudSubscriptionForPersonality
+ _getContainerIDFromCFPrefs
+ _kUARPAssetCacheRecordEncoderKeyAssetHash
+ _kUARPAssetCacheRecordEncoderKeyContainerID
+ _kUARPAssetManagerServiceCacheRegistryFileExtension
+ _kUARPAssetManagerServiceCacheVerificationCertsFileName
+ _kUARPAssetManagerServiceReleaseNotesFileName
+ _kUARPAssetManagerServiceiCloudCertificateFileName
+ _kUARPAssetManagerServiceiCloudTokenFileName
+ _kUARPAssetSubscriptionMobileAssetEncoderKeyCellDownload
+ _kUARPAssetSubscriptionMobileAssetEncoderKeyReleaseNotes
+ _kUARPAssetSubscriptionUARPiCloudEncoderKeyContainerID
+ _kUARPAssetSubscriptionUARPiCloudEncoderKeyProductGroup
+ _kUARPAssetSubscriptionUARPiCloudEncoderKeyProductNumber
+ _objc_msgSend$assetAvailabilityUpdateForPersonality:assetVersion:creationDate:status:
+ _objc_msgSend$assetHash
+ _objc_msgSend$checkCacheForPersonality:releaseNotes:
+ _objc_msgSend$containerID
+ _objc_msgSend$createSubscriptionForPrimeCache:
+ _objc_msgSend$getAssetURLForPersonality:releaseNotes:
+ _objc_msgSend$initWithAssetVersion:containerID:assetURL:assetHash:deploymentRules:
+ _objc_msgSend$initWithProductGroup:productNumber:containerID:releaseNotesAsset:downloadOnCellularAllowed:domain:
+ _objc_msgSend$initWithProductGroup:productNumber:domain:
+ _objc_msgSend$model
+ _objc_msgSend$productGroup
+ _objc_msgSend$productNumber
+ _objc_msgSend$releaseNotesAsset
+ _objc_msgSend$setContainerID:
+ _objc_msgSend$useiCloud
- -[UARPAssetManagerController getAssetURLForPersonality:]
- -[UARPAssetManagerListener getAssetURLForPersonality:reply:]
- -[UARPAssetManagerServiceInstance assetManagerService]
- -[UARPAssetManagerServiceInstance checkCacheForPersonality:]
- -[UARPAssetManagerServiceInstanceMobileAsset assetManagerService]
- -[UARPAssetManagerServiceInstanceMobileAsset checkCacheForPersonality:]
- -[UARPAssetManagerServiceManager checkCacheForPersonality:]
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUDPreferences.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUDeveloperSettingsDatabase.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUDeveloperSettingsUtils.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUHelperInstance.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUHelperStrings.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUInternalSettingsStrings.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUStrings.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/NSUserDefaults+AUHelper.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/SandboxingSupport.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetCacheRecord.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerController.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerListener.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceInstance-fd161e77cb24e0c536d45b4041be005e.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceInstanceMobileAsset.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceManager.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceTypes.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerSettingsListener.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerStrings.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetSubscription.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetSubscriptionMobileAsset.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetSubscriptionMobileAssetSU.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAsyncAssetManagerUtils.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPDeploymentRule.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPDeploymentRuleConfig.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPError.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPSandboxExtension.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPSettingsAccessory.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/main.o
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Sources/AppleAccessoryManager/AUDeveloperSettings/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Common/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Common/Cache/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Common/MobileAssetSubscriptions/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Daemon/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Daemon/ServiceManager/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Sources/AppleAccessoryManager/CommonCode/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Sources/AppleAccessoryManager/CoreUARP/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Sources/AppleAccessoryManager/MobileAccessoryUpdater/AUHelper/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Sources/AppleAccessoryManager/MobileAccessoryUpdater/AUHelper/helpers/
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.a7oU5Z/Sources/AppleAccessoryManager/MobileAccessoryUpdater/fud/
- GCC_except_table17
- _objc_msgSend$assetManagerService
- _objc_msgSend$checkCacheForPersonality:
- _objc_msgSend$getAssetURLForPersonality:
- _objc_msgSend$usePallas
CStrings:
+ "%@-%@"
+ "%s Could not create valid iCloud subscription for %{public}@"
+ "%s: ContainerID override found for %@: %@"
+ "-"
+ "-[UARPAssetManagerListener getAssetURLForPersonality:releaseNotes:reply:]"
+ "-[UARPAssetManagerServiceInstance checkCacheForPersonality:releaseNotes:]"
+ "-[UARPAssetManagerServiceInstance createSubscriptionForPrimeCache:]"
+ "-[UARPAssetManagerServiceInstanceMobileAsset checkCacheForPersonality:releaseNotes:]"
+ "-[UARPAssetManagerServiceInstanceiCloud assetAvailabilityUpdateForSubscription:cacheRecord:asyncUpdate:]"
+ "-[UARPAssetManagerServiceInstanceiCloud checkCacheForPersonality:releaseNotes:]"
+ "<%@: assetVersion=%@, assetURL=%@ containerID=%@ assetHash=%@>"
+ "<%@: pgpn=%@-%@, containerID=%@ releaseNotes=%@ domain=%@>"
+ "@\"NSURL\"28@0:8@\"UARPEndpointPersonality\"16B24"
+ "@56@0:8@16@24@32@40@48"
+ "@56@0:8@16@24@32B40B44@48"
+ "Could not create valid iCloud subscription for %{public}@"
+ "NO"
+ "Only iCloud accessory personalities are currently supported"
+ "Only iCloud accessory subscriptions are currently supported"
+ "RECEIVED %s: %@, returning %@ / %d"
+ "T@\"NSString\",R,V_assetHash"
+ "T@\"NSString\",R,V_containerID"
+ "T@\"NSString\",R,V_productGroup"
+ "T@\"NSString\",R,V_productNumber"
+ "TB,R,V_downloadOnCellularAllowed"
+ "TB,R,V_releaseNotesAsset"
+ "UARPAssetCacheRecordiCloud"
+ "UARPAssetManagerServiceInstanceiCloud"
+ "UARPAssetSubscriptioniCloud"
+ "UARPVerificationCertificates.plist"
+ "UARPiCloudPublicContainer"
+ "UARPiCloudPublicContainerBeta"
+ "UARPiCloudPublicContainerUAT"
+ "UARPiCloudStagingContainer"
+ "UARPiCloudStagingContainerBeta"
+ "UARPiCloudStagingContainerUAT"
+ "UARPiCloudTokens.plist"
+ "Unsupported container type %{public}ld"
+ "YES"
+ "_assetHash"
+ "_containerID"
+ "_downloadOnCellularAllowed"
+ "_productGroup"
+ "_productNumber"
+ "_releaseNotesAsset"
+ "assetAvailabilityUpdateForPersonality:assetVersion:creationDate:status:"
+ "assetHash"
+ "assetType"
+ "cellularDownload"
+ "checkCacheForPersonality:releaseNotes:"
+ "com.apple.uarp.beta"
+ "com.apple.uarp.staging"
+ "com.apple.uarp.staging.beta"
+ "com.apple.uarp.staging.uat"
+ "com.apple.uarp.uat"
+ "containerID"
+ "createSubscriptionForPrimeCache:"
+ "downloadOnCellularAllowed"
+ "getAssetURLForPersonality:releaseNotes:"
+ "getAssetURLForPersonality:releaseNotes:reply:"
+ "getContainerIDFromCFPrefs"
+ "initWithAssetVersion:containerID:assetURL:assetHash:deploymentRules:"
+ "initWithProductGroup:productNumber:containerID:releaseNotesAsset:downloadOnCellularAllowed:domain:"
+ "initWithProductGroup:productNumber:domain:"
+ "model"
+ "plist"
+ "productGroup"
+ "productNumber"
+ "releaseNotes"
+ "releaseNotesAsset"
+ "releasenotes"
+ "setContainerID:"
+ "useiCloud"
+ "v36@0:8@\"UARPEndpointPersonality\"16B24@?<v@?@\"NSURL\">28"
+ "v36@0:8@16B24@?28"
+ "v48@0:8@16@24@32q40"
+ "vid0x%04lXpid0x%04lX"
- "-[UARPAssetManagerListener getAssetURLForPersonality:reply:]"
- "-[UARPAssetManagerServiceInstance assetManagerService]"
- "-[UARPAssetManagerServiceInstance checkCacheForPersonality:]"
- "-[UARPAssetManagerServiceInstanceMobileAsset checkCacheForPersonality:]"
- "@\"NSURL\"24@0:8@\"UARPEndpointPersonality\"16"
- "assetManagerService"
- "checkCacheForPersonality:"
- "getAssetURLForPersonality:"
- "getAssetURLForPersonality:reply:"
- "usePallas"
- "v32@0:8@\"UARPEndpointPersonality\"16@?<v@?@\"NSURL\">24"

```
