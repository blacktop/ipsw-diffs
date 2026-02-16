## CloudSettings

> `/System/Library/PrivateFrameworks/CloudSettings.framework/CloudSettings`

```diff

 113.0.0.0.0
-  __TEXT.__text: 0x6a74
-  __TEXT.__auth_stubs: 0x350
+  __TEXT.__text: 0x6d30
+  __TEXT.__auth_stubs: 0x300
   __TEXT.__objc_methlist: 0x53c
   __TEXT.__const: 0x98
   __TEXT.__cstring: 0x335
   __TEXT.__oslogstring: 0x2456
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__unwind_info: 0x110
+  __TEXT.__unwind_info: 0x128
   __TEXT.__objc_classname: 0xd5
   __TEXT.__objc_methname: 0xa45
   __TEXT.__objc_methtype: 0x2ea

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x200
-  __AUTH_CONST.__auth_got: 0x1b8
+  __AUTH_CONST.__auth_got: 0x190
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x340
   __AUTH_CONST.__objc_const: 0x808

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 49E2A062-1B2E-353A-B06D-67612F48BD6A
+  UUID: 84B460A3-E751-3CF5-B26C-CCC8EC8A656E
   Functions: 77
-  Symbols:   390
+  Symbols:   385
   CStrings:  388
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ +[CloudSettingsManager sharedCloudSettingsManager] : 68 -> 84
~ -[CloudSettingsManager setEnabled:forStore:] : 688 -> 696
~ -[CloudSettingsManager isEnabledForStore:] : 652 -> 660
~ -[CloudSettingsManager setConflict:forStore:] : 464 -> 472
~ -[CloudSettingsManager conflictStateForStore:] : 540 -> 548
~ -[CloudSettingsManager isServiceKnownForStore:] : 340 -> 348
~ -[CloudSettingsManager performFirstTimeSetup:] : 1124 -> 1140
~ -[CloudSettingsManager applyCloudSettingsToDevice:forStore:] : 628 -> 636
~ -[CloudSettingsManager writeToCloudSettings:forStore:] : 628 -> 636
~ -[CloudSettingsManager deviceSettingsForStore:] : 800 -> 816
~ -[CloudSettingsManager applySettingsToDevice:forStore:] : 736 -> 744
~ -[CloudSettingsManager defaultSettingsDictionary] : 388 -> 400
~ -[CloudSettingsManager currentStateDictionary] : 536 -> 548
~ -[CloudSettingsManager activeXPCConnectionForStore:] : 280 -> 284
~ -[CloudSettingsManager currentConflictDictionary] : 536 -> 548
~ -[CloudSettingsStore initWithStoreIdentifier:] : 508 -> 500
~ -[CloudSettingsStore keyExists:andIsOfType:] : 1016 -> 1020
~ -[CloudSettingsStore setBool:forKey:] : 556 -> 568
~ -[CloudSettingsStore boolForKey:] : 532 -> 540
~ -[CloudSettingsStore setNumber:forKey:] : 540 -> 544
~ -[CloudSettingsStore numberForKey:] : 760 -> 772
~ -[CloudSettingsStore setString:forKey:] : 540 -> 544
~ -[CloudSettingsStore stringForKey:] : 760 -> 772
~ -[CloudSettingsStore setArray:forKey:] : 540 -> 544
~ -[CloudSettingsStore arrayForKey:] : 760 -> 772
~ -[CloudSettingsStore setData:forKey:] : 540 -> 544
~ -[CloudSettingsStore dataForKey:] : 760 -> 772
~ -[CloudSettingsStore setDictionary:forKey:] : 632 -> 640
~ -[CloudSettingsStore dictionaryForKey:] : 552 -> 564
~ -[CloudSettingsStore removeObjectForKey:] : 612 -> 624
~ -[CloudSettingsStore syncNow:] : 488 -> 496
~ -[CloudSettingsStore setObject:forKey:] : 500 -> 504
~ -[CloudSettingsStore objectForKey:] : 452 -> 460
~ -[CloudSettingsService initWithStoreIdentifier:settingsMediator:] : 180 -> 176
~ -[CloudSettingsService performFirstTimeSetupForStore:newDevice:] : 580 -> 596
~ -[CloudSettingsService applyCloudSettingsToDevice:forStore:] : 908 -> 952
~ -[CloudSettingsService writeToCloudSettingsDict:forStore:] : 720 -> 756
~ -[CloudSettingsService writeToCloudSettings:forStore:] : 148 -> 152
~ -[CloudSettingsService performSmartMergeWithStoreSettings:] : 1380 -> 1444
~ -[CloudSettingsService setIdentifier:] : 12 -> 64
~ -[CloudSettingsService setStore:] : 12 -> 64
~ -[CloudSettingsService setMediator:] : 12 -> 64
~ -[CloudSettingsServiceDelegate initWithStoreIdentifier:settingsMediator:] : 160 -> 156
~ -[CloudSettingsServiceDelegate listener:shouldAcceptNewConnection:] : 148 -> 156
~ -[CloudSettingsDispatchingMediator registerKey:getter:setter:merger:type:] : 372 -> 388
~ -[CloudSettingsDispatchingMediator deviceSettingsForKeys:] : 556 -> 580
~ -[CloudSettingsDispatchingMediator mergeSettings:] : 1172 -> 1216
~ ___50-[CloudSettingsDispatchingMediator mergeSettings:]_block_invoke : 108 -> 112
~ ___50-[CloudSettingsDispatchingMediator mergeSettings:]_block_invoke.3 : 132 -> 140

```
