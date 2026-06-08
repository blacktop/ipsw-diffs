## uarpassetmanagerd

> `/usr/libexec/uarpassetmanagerd`

```diff

-1345.120.5.0.0
-  __TEXT.__text: 0x28ba8
+1576.0.0.0.0
+  __TEXT.__text: 0x28d6c
   __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__objc_stubs: 0x2480
-  __TEXT.__objc_methlist: 0x126c
-  __TEXT.__cstring: 0x2aad
-  __TEXT.__oslogstring: 0x17bc
-  __TEXT.__objc_methname: 0x2b30
-  __TEXT.__objc_classname: 0x2fe
-  __TEXT.__objc_methtype: 0x829
-  __TEXT.__gcc_except_tab: 0x1ac
-  __TEXT.__unwind_info: 0x388
-  __DATA_CONST.__auth_got: 0x268
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0x2548
-  __DATA_CONST.__cfstring: 0x2a80
+  __TEXT.__objc_stubs: 0x2520
+  __TEXT.__objc_methlist: 0x12a4
+  __TEXT.__cstring: 0x2c41
+  __TEXT.__oslogstring: 0x1826
+  __TEXT.__objc_methname: 0x2c20
+  __TEXT.__objc_classname: 0x2e4
+  __TEXT.__objc_methtype: 0x837
+  __TEXT.__gcc_except_tab: 0x11c
+  __TEXT.__unwind_info: 0x390
+  __DATA_CONST.__const: 0x2710
+  __DATA_CONST.__cfstring: 0x2b80
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2d18
-  __DATA.__objc_selrefs: 0xb68
-  __DATA.__objc_ivar: 0x178
+  __DATA_CONST.__auth_got: 0x268
+  __DATA_CONST.__got: 0x198
+  __DATA.__objc_const: 0x2d48
+  __DATA.__objc_selrefs: 0xba0
+  __DATA.__objc_ivar: 0x17c
   __DATA.__objc_data: 0x500
   __DATA.__data: 0x480
   __DATA.__bss: 0x40

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 851AC022-F070-3D18-9C45-D086CE5E752B
-  Functions: 446
-  Symbols:   5499
-  CStrings:  1516
+  UUID: B9049489-6395-3CF3-B3BA-FC620B972C94
+  Functions: 453
+  Symbols:   5655
+  CStrings:  1547
 
Symbols:
+ +[NSUserDefaults(AUHelperExtend) AUDeveloperSettingsAccessoryDatabase]
+ -[AUDeveloperSettingsDatabase copyAccessoryWithSerialNumber:directMatchOnly:]
+ -[AUDeveloperSettingsDatabase remoteAccessoryList]
+ -[UARPSettingsAccessory parentSerialNumber]
+ -[UARPSettingsAccessory setParentSerialNumber:]
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUDPreferences.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUDeveloperSettingsDatabase.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUDeveloperSettingsUtils.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUHelperInstance.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUHelperStrings.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUInternalSettingsStrings.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUStrings.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/NSUserDefaults+AUHelper.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/SandboxingSupport.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetCacheRecord.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerController.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerListener.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceInstance-a71aca054c97db48723ddd9df5a05595.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceInstanceMobileAsset.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceManager.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceTypes.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerSettingsListener.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerStrings.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetSubscription.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetSubscriptionMobileAsset.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetSubscriptionMobileAssetSU.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAsyncAssetManagerUtils.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPDeploymentRule.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPDeploymentRuleConfig.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPError.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPSandboxExtension.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPSettingsAccessory.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/main.o
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Sources/AppleAccessoryManager/AUDeveloperSettings/
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Common/
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Common/Cache/
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Common/MobileAssetSubscriptions/
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Daemon/
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Daemon/ServiceManager/
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Sources/AppleAccessoryManager/CommonCode/
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Sources/AppleAccessoryManager/CoreUARP/
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Sources/AppleAccessoryManager/MobileAccessoryUpdater/AUHelper/
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Sources/AppleAccessoryManager/MobileAccessoryUpdater/AUHelper/helpers/
+ /Library/Caches/com.apple.xbs/6A1BB8B9-7DE7-4754-BED2-C1BBB80416BC/TemporaryDirectory.VEwxqz/Sources/AppleAccessoryManager/MobileAccessoryUpdater/fud/
+ GCC_except_table6
+ OBJC_IVAR_$_UARPSettingsAccessory._parentSerialNumber
+ _MA_PALLAS_AUDIENCE_NAME_DEMO_EXTERNAL
+ _MA_PALLAS_AUDIENCE_NAME_DEMO_INTERNAL
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_CARRIER
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_DEMO_EXTERNAL
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_DEMO_INTERNAL
+ _MA_SANDBOX_EXTENSION_SHORT_TERM_LOCKS_KEY
+ _MA_SANDBOX_EXTENSION_SHORT_TERM_LOCKS_PATH_KEY
+ __44-[UARPAssetManagerServiceInstance copyCache]_block_invoke.430
+ __46-[UARPAssetManagerServiceInstance primeCache:]_block_invoke.447
+ __46-[UARPAssetManagerServiceInstance queryIsBusy]_block_invoke.436
+ __50-[UARPAssetManagerServiceInstance checkForUpdate:]_block_invoke.435
+ __52-[UARPAssetManagerServiceInstance copySubscriptions]_block_invoke.432
+ __59-[UARPAssetManagerServiceInstance registerForSubscription:]_block_invoke.434
+ __60-[UARPAssetManagerServiceInstance clearAssetCacheForDomain:]_block_invoke.445
+ __61-[UARPAssetManagerServiceInstance checkCacheForSubscription:]_block_invoke.427
+ __70-[UARPAssetManagerServiceInstance listener:shouldAcceptNewConnection:]_block_invoke.401
+ ___50-[AUDeveloperSettingsDatabase remoteAccessoryList]_block_invoke
+ ___70+[NSUserDefaults(AUHelperExtend) AUDeveloperSettingsAccessoryDatabase]_block_invoke
+ ___kCFBooleanTrue
+ ___os_log_helper_16_2_3_8_32_8_34_8_66
+ _groupAccessoriesForPersonality
+ _kParentSerialNumberKey
+ _objc_msgSend$AUDeveloperSettingsAccessoryDatabase
+ _objc_msgSend$arrayWithObject:
+ _objc_msgSend$copyAccessoryWithSerialNumber:directMatchOnly:
+ _objc_msgSend$parentSerialNumber
+ _objc_msgSend$remoteAccessoryList
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$setParentSerialNumber:
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUDPreferences.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUDeveloperSettingsDatabase.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUDeveloperSettingsUtils.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUHelperInstance.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUHelperStrings.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUInternalSettingsStrings.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/AUStrings.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/NSUserDefaults+AUHelper.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/SandboxingSupport.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetCacheRecord.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerController.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerListener.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceInstance-8808789da1bce149497b44475beabb54.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceInstanceMobileAsset.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceManager.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerServiceTypes.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerSettingsListener.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetManagerStrings.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetSubscription.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetSubscriptionMobileAsset.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAssetSubscriptionMobileAssetSU.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPAsyncAssetManagerUtils.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPDeploymentRule.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPDeploymentRuleConfig.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPError.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPSandboxExtension.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/UARPSettingsAccessory.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Binaries/AppleAccessoryManager/install/TempContent/Objects/AppleAccessoryManager.build/uarpassetmanagerd.build/Objects-normal/arm64e/main.o
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Sources/AppleAccessoryManager/AUDeveloperSettings/
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Common/
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Common/Cache/
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Common/MobileAssetSubscriptions/
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Daemon/
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Sources/AppleAccessoryManager/AsyncAssetManager/uarpassetmanagerd/Daemon/ServiceManager/
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Sources/AppleAccessoryManager/CommonCode/
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Sources/AppleAccessoryManager/CoreUARP/
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Sources/AppleAccessoryManager/MobileAccessoryUpdater/AUHelper/
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Sources/AppleAccessoryManager/MobileAccessoryUpdater/AUHelper/helpers/
- /Library/Caches/com.apple.xbs/5892FB79-680E-4547-AAE0-346F39C5DD5C/TemporaryDirectory.rac7zB/Sources/AppleAccessoryManager/MobileAccessoryUpdater/fud/
- __44-[UARPAssetManagerServiceInstance copyCache]_block_invoke.409
- __46-[UARPAssetManagerServiceInstance primeCache:]_block_invoke.426
- __46-[UARPAssetManagerServiceInstance queryIsBusy]_block_invoke.415
- __50-[UARPAssetManagerServiceInstance checkForUpdate:]_block_invoke.414
- __52-[UARPAssetManagerServiceInstance copySubscriptions]_block_invoke.411
- __59-[UARPAssetManagerServiceInstance registerForSubscription:]_block_invoke.413
- __60-[UARPAssetManagerServiceInstance clearAssetCacheForDomain:]_block_invoke.424
- __61-[UARPAssetManagerServiceInstance checkCacheForSubscription:]_block_invoke.406
- __70-[UARPAssetManagerServiceInstance listener:shouldAcceptNewConnection:]_block_invoke.380
- ___kCFBooleanFalse
- ___os_log_helper_16_2_3_8_32_8_32_8_64
- __mergePartnerAccessoriesInAssetSettings
- _objc_msgSend$copyAccessoryForSignature:modelNumber:fusingType:partnerSerialNumbers:
- _objc_msgSend$removeAccessory:
CStrings:
+ "%s: Accessory with serial number %{public}@ does not exist"
+ "%s: Cannot group accessories without a serial number for %{public}@"
+ "%s: Missing entry for %{public}@"
+ "%s: Updating location = %{public}s for accessoryName = %{public}@"
+ "-[AUDeveloperSettingsDatabase remoteAccessoryList]"
+ "-[AUDeveloperSettingsDatabase remoteAccessoryList]_block_invoke"
+ "220d35fc-bc97-422e-8c96-7ea2785548a1"
+ "55b4b4f0-0ecd-4a85-a72f-3e5e6feeac4d"
+ "5f33eae7-f1e0-4811-9713-07dd879f16d5"
+ "63efd5fa-738b-4560-913f-49a55bc873f4"
+ "71b10ce9-15df-40be-bfca-49113fff8fcc"
+ "@28@0:8@16B24"
+ "AUDeveloperSettingsAccessoryDatabase"
+ "Cleaning up previous relationship between %@ and %@"
+ "RaveSeed"
+ "Setting %{public}@ as the new primary for %{public}@"
+ "Setting %{public}@ with final list  %{public}@"
+ "T@\"NSString\",R,V_parentSerialNumber"
+ "_parentSerialNumber"
+ "arrayWithObject:"
+ "b9e3c9f6-a252-481e-a9ab-0bd3beeae429"
+ "c1b5ebc2-72ff-44a5-a761-50502d26fc66"
+ "copyAccessoryWithSerialNumber:directMatchOnly:"
+ "demo-external"
+ "demo-internal"
+ "fc098402-04dd-45c5-86f8-50e36d846af1"
+ "groupAccessoriesForPersonality"
+ "parentSerialNumber"
+ "remoteAccessoryList"
+ "removeObjectAtIndex:"
+ "sandboxExtensionShortTermLocksKey"
+ "sandboxExtensionShortTermLocksPathKey"
+ "setParentSerialNumber:"
- "%s: Updating location = %s for accessoryName = %@"
- "245326d2-3ddb-4c46-a08e-aab8b6060a1b"
- "85ff7a90-361b-42d1-a420-97dee860f018"
- "97d68e5c-95bb-4136-9aa0-f08964fcc0e1"
- "LuckF"
- "Removing Entry from AUDeveloperSettingsDatabase with serialNumber %@"
- "Settings accessory found for personality %@"
- "Unexpected Accessory Entry for %@ with fusing %@"
- "Using reported Partner Serial Numbers %@ for personality %@"
- "ed5a1c1d-2a39-4993-8bcc-f260c4b42868"
- "fb333b76-b463-401f-8899-96d82fc4c598"

```
