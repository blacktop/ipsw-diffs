## SoftwareUpdateSubscriber

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/SoftwareUpdateSubscriber.xpc/Contents/MacOS/SoftwareUpdateSubscriber`

```diff

-2082.80.5.0.0
-  __TEXT.__text: 0x5fd4
+2171.101.1.0.0
+  __TEXT.__text: 0x6154
   __TEXT.__auth_stubs: 0x170
-  __TEXT.__objc_stubs: 0xc00
-  __TEXT.__objc_methlist: 0x25c
+  __TEXT.__objc_stubs: 0xc20
+  __TEXT.__objc_methlist: 0x568
   __TEXT.__objc_classname: 0x17f
   __TEXT.__const: 0x28
   __TEXT.__cstring: 0xa13
-  __TEXT.__objc_methname: 0xe86
+  __TEXT.__objc_methname: 0xe8d
   __TEXT.__oslogstring: 0x745
   __TEXT.__objc_methtype: 0x531
-  __TEXT.__unwind_info: 0xc8
+  __TEXT.__unwind_info: 0xd0
   __DATA_CONST.__auth_got: 0xc0
-  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__const: 0x30
   __DATA_CONST.__cfstring: 0x6e0
   __DATA_CONST.__objc_classlist: 0x40

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x108
-  __DATA_CONST.__objc_arraydata: 0x70
-  __DATA_CONST.__objc_arrayobj: 0x120
-  __DATA.__objc_const: 0xec0
-  __DATA.__objc_selrefs: 0x3a8
+  __DATA_CONST.__objc_arraydata: 0x88
+  __DATA_CONST.__objc_arrayobj: 0x150
+  __DATA.__objc_const: 0x960
+  __DATA.__objc_selrefs: 0x4a8
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x240

   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/Versions/A/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 047CDF9A-8F2E-3AAA-8245-BA9B00208B1F
-  Functions: 44
-  Symbols:   627
-  CStrings:  373
+  UUID: F3A98BBE-3364-33B2-9FD6-B7AD84930998
+  Functions: 47
+  Symbols:   631
+  CStrings:  374
 
Symbols:
+ -[SoftwareUpdateCombinedAdapter applyCombinedConfiguration:declarationKeys:scope:returningReasons:error:].cold.1
+ -[SoftwareUpdateCombinedAdapter removeCombinedConfigurationForScope:error:].cold.1
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate_SUCore/install/TempContent/Objects/MobileSoftwareUpdate.build/SoftwareUpdateSubscriber.build/Objects-normal/arm64e/DDMSoftwareUpdateConstants.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate_SUCore/install/TempContent/Objects/MobileSoftwareUpdate.build/SoftwareUpdateSubscriber.build/Objects-normal/arm64e/RMModelStatusSoftwareUpdateBetaEnrollment.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate_SUCore/install/TempContent/Objects/MobileSoftwareUpdate.build/SoftwareUpdateSubscriber.build/Objects-normal/arm64e/RMModelStatusSoftwareUpdateDeviceID.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate_SUCore/install/TempContent/Objects/MobileSoftwareUpdate.build/SoftwareUpdateSubscriber.build/Objects-normal/arm64e/SoftwareUpdateAdapter.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate_SUCore/install/TempContent/Objects/MobileSoftwareUpdate.build/SoftwareUpdateSubscriber.build/Objects-normal/arm64e/SoftwareUpdateApplicator.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate_SUCore/install/TempContent/Objects/MobileSoftwareUpdate.build/SoftwareUpdateSubscriber.build/Objects-normal/arm64e/SoftwareUpdateCombinedAdapter.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate_SUCore/install/TempContent/Objects/MobileSoftwareUpdate.build/SoftwareUpdateSubscriber.build/Objects-normal/arm64e/SoftwareUpdateSettingsApplicator.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate_SUCore/install/TempContent/Objects/MobileSoftwareUpdate.build/SoftwareUpdateSubscriber.build/Objects-normal/arm64e/SoftwareUpdateStatus.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate_SUCore/install/TempContent/Objects/MobileSoftwareUpdate.build/SoftwareUpdateSubscriber.build/Objects-normal/arm64e/main.o
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate_SUCore/SoftwareUpdateSubscriber/
+ /AppleInternal/Library/BuildRoots/218d6505-03da-11f0-8896-122ba06eff56/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate_SUCore/SoftwareUpdateSubscriber/Models/Status/
+ _OBJC_CLASS_$_SUCoreDevice
+ _OUTLINED_FUNCTION_0
+ _SUCorePolicyDDMGlobalSettingSystemUpdatesDeferralPeriodKey
+ _objc_msgSend$hwModelString
+ _objc_msgSend$sharedDevice
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate_SUCore/install/TempContent/Objects/MobileSoftwareUpdate.build/SoftwareUpdateSubscriber.build/Objects-normal/arm64e/DDMSoftwareUpdateConstants.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate_SUCore/install/TempContent/Objects/MobileSoftwareUpdate.build/SoftwareUpdateSubscriber.build/Objects-normal/arm64e/RMModelStatusSoftwareUpdateBetaEnrollment.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate_SUCore/install/TempContent/Objects/MobileSoftwareUpdate.build/SoftwareUpdateSubscriber.build/Objects-normal/arm64e/RMModelStatusSoftwareUpdateDeviceID.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate_SUCore/install/TempContent/Objects/MobileSoftwareUpdate.build/SoftwareUpdateSubscriber.build/Objects-normal/arm64e/SoftwareUpdateAdapter.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate_SUCore/install/TempContent/Objects/MobileSoftwareUpdate.build/SoftwareUpdateSubscriber.build/Objects-normal/arm64e/SoftwareUpdateApplicator.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate_SUCore/install/TempContent/Objects/MobileSoftwareUpdate.build/SoftwareUpdateSubscriber.build/Objects-normal/arm64e/SoftwareUpdateCombinedAdapter.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate_SUCore/install/TempContent/Objects/MobileSoftwareUpdate.build/SoftwareUpdateSubscriber.build/Objects-normal/arm64e/SoftwareUpdateSettingsApplicator.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate_SUCore/install/TempContent/Objects/MobileSoftwareUpdate.build/SoftwareUpdateSubscriber.build/Objects-normal/arm64e/SoftwareUpdateStatus.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/MobileSoftwareUpdate_SUCore/install/TempContent/Objects/MobileSoftwareUpdate.build/SoftwareUpdateSubscriber.build/Objects-normal/arm64e/main.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate_SUCore/SoftwareUpdateSubscriber/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/MobileSoftwareUpdate_SUCore/SoftwareUpdateSubscriber/Models/Status/
- _OBJC_CLASS_$_SUOSUMDMController
- _objc_msgSend$hardwareModelString
Functions:
~ -[SoftwareUpdateAdapter removeDeclarationKey:scope:error:] : 1840 -> 1836
~ -[SoftwareUpdateAdapter configurationUIForConfiguration:scope:completionHandler:] : 1892 -> 1920
~ -[SoftwareUpdateCombinedAdapter applyCombinedConfiguration:declarationKeys:scope:returningReasons:error:] : 3956 -> 3988
~ -[SoftwareUpdateCombinedAdapter _recommendationCadenceLocalizedStringForString:] : 356 -> 272
~ -[SoftwareUpdateCombinedAdapter removeCombinedConfigurationForScope:error:] : 1144 -> 1104
~ -[SoftwareUpdateCombinedAdapter configurationUIForConfiguration:scope:completionHandler:] : 4536 -> 4620
~ -[SoftwareUpdateCombinedAdapter _localizedStringForRMModelSettingsState:] : 356 -> 272
+ _OUTLINED_FUNCTION_0
~ -[SoftwareUpdateApplicator init] : 104 -> 108
~ -[SoftwareUpdateStatus queryForStatusWithKeyPaths:store:completionHandler:] : 1172 -> 1212
~ +[RMModelStatusSoftwareUpdateDeviceID supportedOS] : 572 -> 704
CStrings:
+ "hwModelString"
+ "sharedDevice"
- "hardwareModelString"

```
