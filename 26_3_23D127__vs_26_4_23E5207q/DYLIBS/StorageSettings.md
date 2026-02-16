## StorageSettings

> `/System/Library/PrivateFrameworks/StorageSettings.framework/StorageSettings`

```diff

 156.0.0.0.0
-  __TEXT.__text: 0x7ec0
+  __TEXT.__text: 0x83f8
   __TEXT.__auth_stubs: 0x450
   __TEXT.__objc_methlist: 0x790
   __TEXT.__const: 0x80
   __TEXT.__cstring: 0xadb
   __TEXT.__ustring: 0x4
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__unwind_info: 0x278
+  __TEXT.__unwind_info: 0x268
   __TEXT.__objc_classname: 0xfa
   __TEXT.__objc_methname: 0x18e6
   __TEXT.__objc_methtype: 0x24b

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BD66D505-766A-336F-A313-26C53689FA20
+  UUID: 6522A8CB-9CC8-3DC3-A09B-F279ADC2818F
   Functions: 196
   Symbols:   949
   CStrings:  610
Symbols:
+ _objc_release_x28
+ _objc_retain_x23
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x27
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x4
Functions:
~ -[STStorageProgressView updateColors] : 220 -> 260
~ -[STStorageProgressView initWithFrame:] : 120 -> 124
~ -[STStorageProgressView drawRect:] : 424 -> 436
~ _STStorageDeviceKey : 68 -> 84
~ -[STStorageTableCell initWithStyle:reuseIdentifier:specifier:] : 1836 -> 1888
~ -[STStorageTableCell setupTitleAndInfoConstraints] : 860 -> 908
~ -[STStorageTableCell createNormalFontConstraints] : 848 -> 900
~ -[STStorageTableCell createLargeFontConstraints] : 964 -> 1024
~ -[STStorageTableCell updateConstraints] : 924 -> 908
~ -[STStorageTableCell setTitle:] : 100 -> 104
~ -[STStorageTableCell setInfo:] : 100 -> 104
~ -[STStorageTableCell setSizeString:] : 316 -> 332
~ -[STStorageTableCell sizeString] : 84 -> 100
~ -[STStorageTableCell setSize:] : 176 -> 180
~ -[STStorageTableCell setCloudIconHidden:] : 96 -> 100
~ -[STStoragePlugin setIdentifier:] : 12 -> 64
~ -[STStoragePlugin identifier] : 132 -> 136
~ -[STStoragePlugin setTips:] : 12 -> 64
~ -[STStoragePlugin tips] : 24 -> 72
~ -[STStoragePlugin notifyUsageChanged] : 76 -> 80
~ -[STStoragePlugin reloadTips] : 96 -> 100
~ -[STStoragePlugin reloadSpecifiersForApp:] : 184 -> 192
~ _STColorForCategoryKey : 140 -> 148
~ ___STColorForCategoryKey_block_invoke : 472 -> 508
~ _STColorForCategory : 76 -> 84
~ -[STStorageTip init] : 180 -> 184
~ -[STStorageTip propertyForKey:] : 108 -> 112
~ -[STStorageTip setSize:] : 104 -> 108
~ -[STStorageTip size] : 68 -> 72
~ -[STStorageTip _reload:] : 272 -> 288
~ -[STStorageOptionTip init] : 216 -> 220
~ -[STStorageOptionTip enableOption] : 120 -> 124
~ -[STStorageOptionTip setValue:specifier:] : 508 -> 552
~ -[STStorageOptionTip setActivationPercent:] : 152 -> 156
~ -[STStorageOptionTip activationPercent] : 76 -> 80
~ -[STStorageOptionTip immediateGain] : 92 -> 100
~ -[STStorageOptionTip setImmediateGain:] : 104 -> 108
~ -[STStorageOptionTip eventualGain] : 68 -> 72
~ -[STStorageOptionTip setEventualGain:] : 104 -> 108
~ +[STStorageAppCell specifierForStorageApp:] : 184 -> 188
~ +[STStorageAppCell specifierForChildApp:] : 264 -> 272
~ +[STStorageAppCell specifierForAppIdentifier:] : 128 -> 132
~ +[STStorageAppCell specifierForAppBundleURL:] : 124 -> 136
~ +[STStorageAppCell specifierForAppProxy:] : 96 -> 104
~ -[STStorageAppCell initWithStyle:reuseIdentifier:specifier:] : 240 -> 248
~ -[STStorageAppCell refreshCellContentsWithSpecifier:] : 768 -> 804
~ ___53-[STStorageAppCell refreshCellContentsWithSpecifier:]_block_invoke_2 : 236 -> 244
~ ___LastUsedFormatString_block_invoke : 64 -> 68
~ _STLoadHeaderIconForAppID : 100 -> 104
~ __STLoadHeaderIconForAppID : 356 -> 364
~ _AppIsClip : 108 -> 112
~ _STLoadHeaderIconForApp : 132 -> 136
~ _STLoadTableIconForAppID : 100 -> 104
~ __STLoadTableIconForAppID : 296 -> 300
~ _STLoadTableIconForApp : 132 -> 136
~ ____STLoadHeaderIconForAppID_block_invoke : 64 -> 68
~ __CachedIconForAppID : 152 -> 160
~ _getIconLoaderQueue : 68 -> 84
~ __LoadIconForAppID : 1156 -> 1196
~ ____STLoadHeaderIconForAppID_block_invoke_3 : 144 -> 148
~ ____STLoadTableIconForAppID_block_invoke : 64 -> 68
~ ____STLoadTableIconForAppID_block_invoke_3 : 144 -> 148
~ +[STStorageItemCell specifierForItemURL:] : 184 -> 188
~ -[STStorageItemCell refreshCellContentsWithSpecifier:] : 600 -> 620
~ ___54-[STStorageItemCell refreshCellContentsWithSpecifier:]_block_invoke : 204 -> 192
~ ___54-[STStorageItemCell refreshCellContentsWithSpecifier:]_block_invoke_2 : 112 -> 120
~ ___54-[STStorageItemCell refreshCellContentsWithSpecifier:]_block_invoke_3 : 464 -> 444
~ _STFrameworkLocStr : 108 -> 116
~ __FrameworkBundle : 68 -> 84
~ _STFrameworkImage : 116 -> 124
~ ____FrameworkBundle_block_invoke : 72 -> 76
~ +[STStorageAppHeaderCell specifierForStorageApp:] : 184 -> 188
~ +[STStorageAppHeaderCell specifierForAppIdentifier:] : 128 -> 132
~ +[STStorageAppHeaderCell specifierForAppProxy:] : 96 -> 104
~ +[STStorageAppHeaderCell specifierForAppBundleURL:] : 124 -> 136
~ -[STStorageAppHeaderCell initWithStyle:reuseIdentifier:specifier:] : 1288 -> 1316
~ -[STStorageAppHeaderCell updateConstraints] : 876 -> 920
~ -[STStorageAppHeaderCell refreshCellContentsWithSpecifier:] : 640 -> 672
~ -[STStorageAppHeaderCell setTitle:] : 100 -> 108
~ -[STStorageAppHeaderCell title] : 84 -> 100
~ -[STStorageAppHeaderCell vendor] : 84 -> 100
~ -[STStorageAppHeaderCell info] : 84 -> 100
~ -[PSSpecifier(STStorageAppHeaderCell) versionLabelEnabled] : 84 -> 88
~ -[STStorageActionTip init] : 212 -> 216
~ -[STStorageActionTip setDetailControllerClass:] : 80 -> 84
~ -[STStorageActionTip detailControllerClass] : 76 -> 84
~ -[STStorageTipCell initWithStyle:reuseIdentifier:specifier:] : 1500 -> 1536
~ -[STStorageTipCell updateConstraints] : 2184 -> 2256
~ -[STStorageTipCell refreshCellContentsWithSpecifier:] : 1328 -> 1384
~ -[STStorageTipCell _activateOption] : 108 -> 116
~ -[STStorageTipInfoCell initWithStyle:reuseIdentifier:specifier:] : 456 -> 472
~ -[STStorageTipInfoCell updateConstraints] : 312 -> 328
~ -[STStorageTipInfoCell refreshCellContentsWithSpecifier:] : 488 -> 520

```
