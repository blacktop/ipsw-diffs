## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-622.1.18.10.3
-  __TEXT.__text: 0x118b94
+622.1.19.10.4
+  __TEXT.__text: 0x11912c
   __TEXT.__auth_stubs: 0x2d90
-  __TEXT.__objc_methlist: 0xb50c
+  __TEXT.__objc_methlist: 0xb564
   __TEXT.__const: 0x29a4
-  __TEXT.__gcc_except_tab: 0x6560
-  __TEXT.__cstring: 0x11a65
-  __TEXT.__ustring: 0x2786
-  __TEXT.__oslogstring: 0x9f4d
+  __TEXT.__gcc_except_tab: 0x6554
+  __TEXT.__cstring: 0x11b95
+  __TEXT.__ustring: 0x2810
+  __TEXT.__oslogstring: 0xa05d
   __TEXT.__dlopen_cstrs: 0x19b
   __TEXT.__swift5_typeref: 0xd30
   __TEXT.__swift5_fieldmd: 0x804

   __TEXT.__swift_as_entry: 0xd0
   __TEXT.__swift_as_ret: 0xbc
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x5f70
+  __TEXT.__unwind_info: 0x5f88
   __TEXT.__eh_frame: 0x2cf0
   __TEXT.__objc_classname: 0x19b3
-  __TEXT.__objc_methname: 0x23983
+  __TEXT.__objc_methname: 0x23a5a
   __TEXT.__objc_methtype: 0x3d7e
-  __TEXT.__objc_stubs: 0x11420
-  __DATA_CONST.__got: 0xde0
-  __DATA_CONST.__const: 0x4e08
+  __TEXT.__objc_stubs: 0x11460
+  __DATA_CONST.__got: 0xde8
+  __DATA_CONST.__const: 0x4df8
   __DATA_CONST.__objc_classlist: 0x5c8
   __DATA_CONST.__objc_catlist: 0x168
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68a0
+  __DATA_CONST.__objc_selrefs: 0x68e0
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x478
   __DATA_CONST.__objc_arraydata: 0x2790
   __AUTH_CONST.__auth_got: 0x16e0
   __AUTH_CONST.__const: 0x4b18
-  __AUTH_CONST.__cfstring: 0x18440
-  __AUTH_CONST.__objc_const: 0x12a20
+  __AUTH_CONST.__cfstring: 0x18540
+  __AUTH_CONST.__objc_const: 0x12a30
   __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x5a0

   __AUTH.__data: 0x480
   __DATA.__objc_ivar: 0xbb8
   __DATA.__data: 0x1670
-  __DATA.__bss: 0x3e90
+  __DATA.__bss: 0x3ea0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1730
   __DATA_DIRTY.__data: 0x1c8
-  __DATA_DIRTY.__bss: 0x498
+  __DATA_DIRTY.__bss: 0x488
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy
   - /System/Library/PrivateFrameworks/Lexicon.framework/Lexicon
+  - /System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/ManagedSettingsObjC.framework/ManagedSettingsObjC
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8C8387DF-BAF5-3F37-AE48-F377DEEDA767
-  Functions: 6730
-  Symbols:   18479
-  CStrings:  12432
+  UUID: ED8EB501-8FF3-39FA-9AB6-B19566C66F23
+  Functions: 6738
+  Symbols:   18494
+  CStrings:  12460
 
Symbols:
+ +[WBSFeatureAvailability _isLockdownModeEnabled]
+ +[WBSFeatureAvailability isNetworkFetchingForPasswordsEnabled]
+ +[WBSFeatureAvailability setIsNetworkFetchingForPasswordsEnabled:]
+ -[NSString(SafariCoreExtras) safari_containsDotOrHomoglyphForDot]
+ -[NSString(SafariCoreExtras) safari_containsDotOrHomoglyphForDot].cold.1
+ -[WBSAnalyticsLogger didClickRecentlySavedBookmark]
+ -[WBSAnalyticsLogger didInteractWithOnboardingItem:userClosedCard:]
+ -[WBSAnalyticsLogger didOpenRecentlySavedSection]
+ -[WBSAnalyticsLogger reportFolderOnTopModePreference:]
+ GCC_except_table113
+ GCC_except_table116
+ GCC_except_table119
+ GCC_except_table122
+ GCC_except_table125
+ GCC_except_table126
+ GCC_except_table129
+ GCC_except_table143
+ GCC_except_table154
+ GCC_except_table168
+ GCC_except_table173
+ GCC_except_table194
+ GCC_except_table212
+ GCC_except_table215
+ GCC_except_table218
+ GCC_except_table223
+ GCC_except_table228
+ GCC_except_table231
+ GCC_except_table234
+ GCC_except_table239
+ GCC_except_table244
+ GCC_except_table248
+ GCC_except_table253
+ GCC_except_table259
+ GCC_except_table266
+ GCC_except_table269
+ GCC_except_table272
+ GCC_except_table275
+ GCC_except_table281
+ GCC_except_table305
+ GCC_except_table310
+ GCC_except_table311
+ GCC_except_table318
+ GCC_except_table325
+ GCC_except_table330
+ GCC_except_table333
+ GCC_except_table338
+ GCC_except_table341
+ GCC_except_table342
+ GCC_except_table362
+ GCC_except_table367
+ GCC_except_table376
+ GCC_except_table386
+ GCC_except_table391
+ GCC_except_table392
+ GCC_except_table395
+ GCC_except_table406
+ GCC_except_table409
+ GCC_except_table414
+ GCC_except_table419
+ GCC_except_table425
+ GCC_except_table428
+ GCC_except_table431
+ GCC_except_table438
+ GCC_except_table439
+ GCC_except_table440
+ _OBJC_CLASS_$_LockdownModeManager
+ _WBSExpirationDateWithMonthYear
+ _WBSPasswordsAppBackgroundNetworkingEnabledDefaultsKey
+ __ZZ65-[NSString(SafariCoreExtras) safari_containsDotOrHomoglyphForDot]E22dotAndHomoglyphsForDot
+ __ZZ65-[NSString(SafariCoreExtras) safari_containsDotOrHomoglyphForDot]E4once
+ ___54-[WBSAnalyticsLogger reportFolderOnTopModePreference:]_block_invoke
+ ___61-[WBSOngoingSharingGroupProvider _fetchGroupsWithCompletion:]_block_invoke.41
+ ___65-[NSString(SafariCoreExtras) safari_containsDotOrHomoglyphForDot]_block_invoke
+ ___67-[WBSAnalyticsLogger didInteractWithOnboardingItem:userClosedCard:]_block_invoke
+ ___block_literal_global.1032
+ ___block_literal_global.1098
+ ___block_literal_global.1235
+ ___block_literal_global.1237
+ ___block_literal_global.1248
+ ___block_literal_global.1250
+ ___block_literal_global.1252
+ ___block_literal_global.1254
+ ___block_literal_global.1256
+ ___block_literal_global.1258
+ ___block_literal_global.1260
+ ___block_literal_global.1262
+ ___block_literal_global.1264
+ ___block_literal_global.1328
+ ___block_literal_global.1330
+ ___block_literal_global.1332
+ ___block_literal_global.1334
+ ___block_literal_global.1336
+ ___block_literal_global.1338
+ ___block_literal_global.3150
+ ___block_literal_global.630
+ ___block_literal_global.766
+ ___block_literal_global.771
+ ___block_literal_global.798
+ ___block_literal_global.807
+ ___block_literal_global.816
+ ___block_literal_global.841
+ ___block_literal_global.910
+ ___block_literal_global.996
+ ___block_literal_global.998
+ _objc_msgSend$_isLockdownModeEnabled
+ _objc_msgSend$exportedObject
+ _objc_msgSend$shared
- -[NSString(SafariCoreExtras) safari_containsPeriodOrHomoglyphForPeriod]
- -[NSString(SafariCoreExtras) safari_containsPeriodOrHomoglyphForPeriod].cold.1
- GCC_except_table121
- GCC_except_table124
- GCC_except_table127
- GCC_except_table130
- GCC_except_table139
- GCC_except_table158
- GCC_except_table170
- GCC_except_table171
- GCC_except_table196
- GCC_except_table211
- GCC_except_table216
- GCC_except_table219
- GCC_except_table224
- GCC_except_table229
- GCC_except_table232
- GCC_except_table233
- GCC_except_table236
- GCC_except_table246
- GCC_except_table250
- GCC_except_table255
- GCC_except_table260
- GCC_except_table267
- GCC_except_table270
- GCC_except_table273
- GCC_except_table279
- GCC_except_table303
- GCC_except_table307
- GCC_except_table308
- GCC_except_table312
- GCC_except_table313
- GCC_except_table322
- GCC_except_table331
- GCC_except_table332
- GCC_except_table335
- GCC_except_table340
- GCC_except_table354
- GCC_except_table363
- GCC_except_table368
- GCC_except_table384
- GCC_except_table389
- GCC_except_table390
- GCC_except_table393
- GCC_except_table402
- GCC_except_table403
- GCC_except_table408
- GCC_except_table413
- GCC_except_table418
- GCC_except_table423
- GCC_except_table427
- GCC_except_table432
- GCC_except_table433
- _WBSExpirationDateWithDayMonthYear
- __ZL22gregorianDateFromPartslll
- __ZZ71-[NSString(SafariCoreExtras) safari_containsPeriodOrHomoglyphForPeriod]E28periodAndHomoglyphsForPeriod
- __ZZ71-[NSString(SafariCoreExtras) safari_containsPeriodOrHomoglyphForPeriod]E4once
- ___61-[WBSOngoingSharingGroupProvider _fetchGroupsWithCompletion:]_block_invoke_3.41
- ___71-[NSString(SafariCoreExtras) safari_containsPeriodOrHomoglyphForPeriod]_block_invoke
- ___block_literal_global.1014
- ___block_literal_global.1080
- ___block_literal_global.1217
- ___block_literal_global.1219
- ___block_literal_global.1224
- ___block_literal_global.1226
- ___block_literal_global.1228
- ___block_literal_global.1230
- ___block_literal_global.1232
- ___block_literal_global.1234
- ___block_literal_global.1236
- ___block_literal_global.1238
- ___block_literal_global.1240
- ___block_literal_global.1310
- ___block_literal_global.1312
- ___block_literal_global.1314
- ___block_literal_global.1316
- ___block_literal_global.1318
- ___block_literal_global.132
- ___block_literal_global.1320
- ___block_literal_global.3147
- ___block_literal_global.618
- ___block_literal_global.754
- ___block_literal_global.759
- ___block_literal_global.774
- ___block_literal_global.795
- ___block_literal_global.804
- ___block_literal_global.823
- ___block_literal_global.892
- ___block_literal_global.978
- ___block_literal_global.980
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftAVFoundation_$_SafariCore
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftCoreAudio_$_SafariCore
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_SafariCore
- _objc_msgSend$dateByAddingComponents:toDate:options:
CStrings:
+ "%ld cached groups, %ld cached invitations"
+ "%ld groups after filtering by invite status"
+ "%ld invitations after filtering by invite status"
+ "Fetched %ld groups from Keychain"
+ "Skip fetching passkey availability as network fetching for passwords is not enabled."
+ "WBSPasswordsAppBackgroundNetworkingEnabled"
+ "_isLockdownModeEnabled"
+ "cardType"
+ "com.apple.Safari.OnBoarding.OnBoardingItemSelected"
+ "com.apple.Safari.Sidebar.ClickedRecentlySavedBookmark"
+ "com.apple.Safari.Sidebar.FolderOnTopModePreference"
+ "com.apple.Safari.Sidebar.OpenedRecentlySavedSection"
+ "didClickRecentlySavedBookmark"
+ "didInteractWithOnboardingItem:userClosedCard:"
+ "didOpenRecentlySavedSection"
+ "exportedObject"
+ "interactionType"
+ "isNetworkFetchingForPasswordsEnabled"
+ "prefersFoldersOnTop"
+ "reportFolderOnTopModePreference:"
+ "safari_containsDotOrHomoglyphForDot"
+ "setIsNetworkFetchingForPasswordsEnabled:"
- "dateByAddingComponents:toDate:options:"
- "en_US"
- "safari_containsPeriodOrHomoglyphForPeriod"

```
