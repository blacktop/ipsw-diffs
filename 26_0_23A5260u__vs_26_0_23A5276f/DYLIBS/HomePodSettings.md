## HomePodSettings

> `/System/Library/PrivateFrameworks/HomePodSettings.framework/HomePodSettings`

```diff

-270.0.0.0.0
-  __TEXT.__text: 0xe493c
+270.0.2.0.0
+  __TEXT.__text: 0xe4938
   __TEXT.__auth_stubs: 0x2690
   __TEXT.__objc_methlist: 0x2274
   __TEXT.__const: 0xda9a

   __TEXT.__objc_methtype: 0xb68
   __TEXT.__objc_stubs: 0x18e0
   __DATA_CONST.__got: 0x738
-  __DATA_CONST.__const: 0xb20
+  __DATA_CONST.__const: 0xb00
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xd8

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 25FBBCAF-17BD-3792-8303-942BE0FCBA74
+  UUID: 40786564-DC31-3CC2-9BA8-02FF8BAF5F49
   Functions: 7662
-  Symbols:   7447
+  Symbols:   7439
   CStrings:  1544
 
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
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_HomePodSettings
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_HomePodSettings
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_HomePodSettings
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_HomePodSettings
Functions:
~ sub_2443bdb28 -> sub_244a1f9f8 : 484 -> 480

```
