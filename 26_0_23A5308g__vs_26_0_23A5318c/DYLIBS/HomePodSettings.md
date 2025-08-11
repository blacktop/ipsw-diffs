## HomePodSettings

> `/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings`

```diff

   __TEXT.__objc_methtype: 0xb68
   __TEXT.__objc_stubs: 0x18e0
   __DATA_CONST.__got: 0x738
-  __DATA_CONST.__const: 0xb00
+  __DATA_CONST.__const: 0xb08
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xd8

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FF03252C-2A39-3BE2-B7EA-22229A545829
+  UUID: DDD06AB0-1D69-3C79-A23F-71D58907E922
   Functions: 7715
-  Symbols:   7479
+  Symbols:   7481
   CStrings:  1545
 
Symbols:
+ ___102-[HPSAccessorySettingService updateSettingWithoutSynchronizationForKeyPath:setting:completionHandler:]_block_invoke.426
+ ___37-[HPSHomeInterface initWithDelegate:]_block_invoke.356
+ ___37-[HPSHomeInterface initWithDelegate:]_block_invoke.356.cold.1
+ ___38-[HPSAccessorySettingService keyPaths]_block_invoke.443
+ ___39-[HPSHomeInterface getAirPlaySettings:]_block_invoke.361
+ ___42-[HPSHomeInterface isHomeKitSyncComplete:]_block_invoke.364
+ ___44-[HPSAccessorySettingService heldAssertions]_block_invoke.444
+ ___45-[HPSHomeInterface getHomeKitCachedSettings:]_block_invoke.363
+ ___48-[HPSAccessorySettingService settingForKeyPath:]_block_invoke.434
+ ___48-[HPSAccessorySettingService settingForKeyPath:]_block_invoke.434.cold.1
+ ___50-[HPSAccessorySettingService keyPathsAvailability]_block_invoke.445
+ ___53-[HPSHomeInterface isAutomaticSoftwareUpdateEnabled:]_block_invoke.366
+ ___54-[HPSHomeAccessorySettingsInterface initWithDelegate:]_block_invoke.348
+ ___54-[HPSHomeAccessorySettingsInterface initWithDelegate:]_block_invoke.348.cold.1
+ ___55-[HPSHomeInterface getCurrentHomeAttribute:completion:]_block_invoke.367
+ ___57-[HPSHomeInterface getHomeAccessoryAttribute:completion:]_block_invoke.359
+ ___62-[HPSAccessorySettingService updateSettingForKeyPath:setting:]_block_invoke.427
+ ___66-[HPSAccessorySettingService initWithConnectionProvider:delegate:]_block_invoke.407
+ ___66-[HPSAccessorySettingService initWithConnectionProvider:delegate:]_block_invoke.407.cold.1
+ ___66-[HPSAccessorySettingService initWithConnectionProvider:delegate:]_block_invoke.409
+ ___66-[HPSAccessorySettingService settingForKeyPath:completionHandler:]_block_invoke.431
+ ___68-[HPSAccessorySettingService fetchAllSettingsWithCompletionHandler:]_block_invoke.438
+ ___68-[HPSAccessorySettingService settingsForKeyPaths:completionHandler:]_block_invoke.429
+ ___80-[HPSAccessorySettingService aggregateAllSettingsInScope:withCompletionHandler:]_block_invoke.441
+ ___80-[HPSAccessorySettingService updateSettingForKeyPath:setting:completionHandler:]_block_invoke.424
+ ___84-[HPSAccessorySettingService updateSettingWithoutSynchronizationForKeyPath:setting:]_block_invoke.428
+ ___block_literal_global.304
+ ___block_literal_global.354
+ ___block_literal_global.356
+ ___block_literal_global.433
+ ___block_literal_global.448
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_HomePodSettings
- ___102-[HPSAccessorySettingService updateSettingWithoutSynchronizationForKeyPath:setting:completionHandler:]_block_invoke.423
- ___37-[HPSHomeInterface initWithDelegate:]_block_invoke.353
- ___37-[HPSHomeInterface initWithDelegate:]_block_invoke.353.cold.1
- ___38-[HPSAccessorySettingService keyPaths]_block_invoke.440
- ___39-[HPSHomeInterface getAirPlaySettings:]_block_invoke.358
- ___42-[HPSHomeInterface isHomeKitSyncComplete:]_block_invoke.361
- ___44-[HPSAccessorySettingService heldAssertions]_block_invoke.441
- ___45-[HPSHomeInterface getHomeKitCachedSettings:]_block_invoke.360
- ___48-[HPSAccessorySettingService settingForKeyPath:]_block_invoke.431
- ___48-[HPSAccessorySettingService settingForKeyPath:]_block_invoke.431.cold.1
- ___50-[HPSAccessorySettingService keyPathsAvailability]_block_invoke.442
- ___53-[HPSHomeInterface isAutomaticSoftwareUpdateEnabled:]_block_invoke.363
- ___54-[HPSHomeAccessorySettingsInterface initWithDelegate:]_block_invoke.345
- ___54-[HPSHomeAccessorySettingsInterface initWithDelegate:]_block_invoke.345.cold.1
- ___55-[HPSHomeInterface getCurrentHomeAttribute:completion:]_block_invoke.364
- ___57-[HPSHomeInterface getHomeAccessoryAttribute:completion:]_block_invoke.356
- ___62-[HPSAccessorySettingService updateSettingForKeyPath:setting:]_block_invoke.424
- ___66-[HPSAccessorySettingService initWithConnectionProvider:delegate:]_block_invoke.404
- ___66-[HPSAccessorySettingService initWithConnectionProvider:delegate:]_block_invoke.404.cold.1
- ___66-[HPSAccessorySettingService initWithConnectionProvider:delegate:]_block_invoke.406
- ___66-[HPSAccessorySettingService settingForKeyPath:completionHandler:]_block_invoke.428
- ___68-[HPSAccessorySettingService fetchAllSettingsWithCompletionHandler:]_block_invoke.435
- ___68-[HPSAccessorySettingService settingsForKeyPaths:completionHandler:]_block_invoke.426
- ___80-[HPSAccessorySettingService aggregateAllSettingsInScope:withCompletionHandler:]_block_invoke.438
- ___80-[HPSAccessorySettingService updateSettingForKeyPath:setting:completionHandler:]_block_invoke.421
- ___84-[HPSAccessorySettingService updateSettingWithoutSynchronizationForKeyPath:setting:]_block_invoke.425
- ___block_literal_global.301
- ___block_literal_global.351
- ___block_literal_global.353
- ___block_literal_global.430
- ___block_literal_global.445

```
