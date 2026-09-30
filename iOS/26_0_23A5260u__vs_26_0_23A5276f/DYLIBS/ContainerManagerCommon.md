## ContainerManagerCommon

> `/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon`

```diff

-725.0.3.0.1
-  __TEXT.__text: 0xe4e80
+725.0.8.0.0
+  __TEXT.__text: 0xe3f50
   __TEXT.__auth_stubs: 0x2090
-  __TEXT.__objc_methlist: 0xa2b4
-  __TEXT.__const: 0xc10
-  __TEXT.__cstring: 0x8d6b
+  __TEXT.__objc_methlist: 0xa3a4
+  __TEXT.__const: 0xc00
+  __TEXT.__cstring: 0x9025
   __TEXT.__swift5_typeref: 0x330
-  __TEXT.__oslogstring: 0xe54d
+  __TEXT.__oslogstring: 0xe38f
   __TEXT.__constg_swiftt: 0x2ec
   __TEXT.__swift5_reflstr: 0x113
   __TEXT.__swift5_fieldmd: 0x18c

   __TEXT.__swift5_proto: 0x70
   __TEXT.__swift5_types: 0x58
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x2ae4
+  __TEXT.__gcc_except_tab: 0x2b0c
   __TEXT.__ustring: 0x16c
-  __TEXT.__unwind_info: 0x2000
+  __TEXT.__unwind_info: 0x2018
   __TEXT.__eh_frame: 0x160
-  __TEXT.__objc_classname: 0x1dd1
-  __TEXT.__objc_methname: 0x13014
-  __TEXT.__objc_methtype: 0x4102
-  __TEXT.__objc_stubs: 0xb840
-  __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0x1a78
+  __TEXT.__objc_classname: 0x1dd2
+  __TEXT.__objc_methname: 0x135a7
+  __TEXT.__objc_methtype: 0x40f9
+  __TEXT.__objc_stubs: 0xb9c0
+  __DATA_CONST.__got: 0x340
+  __DATA_CONST.__const: 0x1a58
   __DATA_CONST.__objc_classlist: 0x5c0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x4a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3470
+  __DATA_CONST.__objc_selrefs: 0x34e8
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x4e8
   __DATA_CONST.__objc_arraydata: 0x2a8
   __AUTH_CONST.__auth_got: 0x1058
-  __AUTH_CONST.__const: 0xbe0
-  __AUTH_CONST.__cfstring: 0x4500
-  __AUTH_CONST.__objc_const: 0x16000
+  __AUTH_CONST.__const: 0xb80
+  __AUTH_CONST.__cfstring: 0x45a0
+  __AUTH_CONST.__objc_const: 0x16188
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH_CONST.__objc_intobj: 0x1410
+  __AUTH_CONST.__objc_intobj: 0x1458
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH.__objc_data: 0xa90
   __AUTH.__data: 0xe0
-  __DATA.__objc_ivar: 0xbd0
+  __DATA.__objc_ivar: 0xbcc
   __DATA.__data: 0x3838
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xda8
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x30c0
   __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0x390
+  __DATA_DIRTY.__bss: 0x360
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0EF6A7AB-D437-3531-B556-FBF284ED0CC8
-  Functions: 3298
-  Symbols:   11485
-  CStrings:  6055
+  UUID: 752544A9-99CF-39C6-80B7-9B31CCCE105E
+  Functions: 3304
+  Symbols:   11492
+  CStrings:  6091
 
Symbols:
+ +[MCMXPCMessageBase(Helpers) _userIdentityDisambiguatedFromUserIdentities:error:]
+ +[MCMXPCMessageBase(Helpers) legacySetOfUserIdentitiesForIdentifiers:targetUserIdentity:containerConfig:clientIdentity:userIdentityCache:warnings:error:]
+ +[MCMXPCMessageBase(Helpers) legacyUserIdentityForIdentifier:targetUserIdentity:containerConfig:clientIdentity:userIdentityCache:warnings:error:]
+ +[MCMXPCMessageBase(Helpers) userIdentitiesAssociatedWithContainerIdentifier:containerConfig:userIdentityCache:error:]
+ -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier _finalizeWithRealPathWithReason:containerIdentity:clientNegatesReference:error:]
+ -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier _finalizeWithSynthesizedPathWithReason:containerIdentity:error:]
+ -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier _recordAnalyticsEventWithAuthResult:clientIsAllowed:]
+ -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier _recordAnalyticsEventWithSandboxExtensionIssueReason:clientIsAllowed:alwaysReturnPath:]
+ -[MCMCommandCreateOrLookupWithBundle _containerIdentityWithError:]
+ -[MCMCommandQuery _checkIfSecureContainer:prefixes:error:]
+ -[MCMCommandQuery _checkIfSecureContainers:error:]
+ -[MCMCommandQuery _checkIfSecureURL:error:]
+ -[MCMCommandQuery _legacySetOfUserIdentitiesForIdentifiers:targetUserIdentity:containerConfig:error:]
+ -[MCMCommandQuery _queryPlanWithIdentifiers:containerConfig:clientIdentity:error:]
+ -[MCMCommandQuery _setOfAvailableUserIdentitiesWithError:]
+ -[MCMCommandQuery requireSecureByPlatformPolicy]
+ -[MCMContainerCacheEntry verifyWithError:]
+ -[MCMContainerConfiguration _identifierPrefixesExemptFromAutomaticProtectionFromPlistValue:error:]
+ -[MCMContainerConfiguration associatedWithParent]
+ -[MCMContainerConfiguration enforceBasedOnDynamicProtectionState]
+ -[MCMContainerConfiguration enforceBasedOnStrictSignatureScrutiny]
+ -[MCMContainerConfiguration hasDynamicProtection]
+ -[MCMContainerConfiguration identifierPrefixesExemptFromAutomaticProtection]
+ -[MCMContainerConfiguration registerDynamicProtectionWithRestrictedEntitlement]
+ -[MCMContainerConfiguration securedByPlatformPolicy]
+ -[MCMFileManager mountPointForURL:error:]
+ -[MCMStaticConfiguration requireDataBackedPersona]
+ -[MCMStaticConfiguration supportPersonasIfAvailable]
+ -[MCMStaticConfiguration warnIfNotDataBackedPersona]
+ -[MCMXPCMessageBase warnings]
+ -[MCMXPCMessageQuery requireSecureByPlatformPolicy]
+ GCC_except_table1033
+ GCC_except_table1042
+ GCC_except_table1046
+ GCC_except_table1084
+ GCC_except_table1085
+ GCC_except_table1097
+ GCC_except_table1099
+ GCC_except_table1108
+ GCC_except_table1119
+ GCC_except_table1121
+ GCC_except_table1123
+ GCC_except_table1125
+ GCC_except_table1128
+ GCC_except_table1130
+ GCC_except_table1134
+ GCC_except_table1139
+ GCC_except_table1145
+ GCC_except_table1148
+ GCC_except_table1158
+ GCC_except_table1174
+ GCC_except_table1184
+ GCC_except_table1189
+ GCC_except_table1193
+ GCC_except_table1195
+ GCC_except_table1247
+ GCC_except_table1257
+ GCC_except_table1288
+ GCC_except_table1336
+ GCC_except_table1338
+ GCC_except_table1342
+ GCC_except_table1343
+ GCC_except_table1556
+ GCC_except_table1605
+ GCC_except_table1694
+ GCC_except_table1839
+ GCC_except_table1877
+ GCC_except_table1884
+ GCC_except_table1887
+ GCC_except_table1902
+ GCC_except_table1906
+ GCC_except_table1941
+ GCC_except_table1947
+ GCC_except_table2019
+ GCC_except_table2022
+ GCC_except_table2133
+ GCC_except_table2270
+ GCC_except_table2287
+ GCC_except_table2288
+ GCC_except_table2364
+ GCC_except_table2421
+ GCC_except_table2436
+ GCC_except_table2496
+ GCC_except_table2508
+ GCC_except_table2568
+ GCC_except_table2578
+ GCC_except_table2603
+ GCC_except_table2632
+ GCC_except_table2654
+ GCC_except_table2658
+ GCC_except_table2661
+ GCC_except_table2665
+ GCC_except_table2721
+ GCC_except_table2810
+ GCC_except_table2858
+ GCC_except_table2861
+ GCC_except_table2932
+ GCC_except_table310
+ GCC_except_table328
+ GCC_except_table348
+ GCC_except_table367
+ GCC_except_table393
+ GCC_except_table396
+ GCC_except_table488
+ GCC_except_table676
+ GCC_except_table752
+ GCC_except_table763
+ GCC_except_table825
+ GCC_except_table901
+ GCC_except_table946
+ GCC_except_table977
+ GCC_except_table979
+ _OBJC_IVAR_$_MCMCommandQuery._requireSecureByPlatformPolicy
+ _OBJC_IVAR_$_MCMContainerConfiguration._associatedWithParent
+ _OBJC_IVAR_$_MCMContainerConfiguration._enforceBasedOnDynamicProtectionState
+ _OBJC_IVAR_$_MCMContainerConfiguration._enforceBasedOnStrictSignatureScrutiny
+ _OBJC_IVAR_$_MCMContainerConfiguration._hasDynamicProtection
+ _OBJC_IVAR_$_MCMContainerConfiguration._identifierPrefixesExemptFromAutomaticProtection
+ _OBJC_IVAR_$_MCMContainerConfiguration._registerDynamicProtectionWithRestrictedEntitlement
+ _OBJC_IVAR_$_MCMContainerConfiguration._securedByPlatformPolicy
+ _OBJC_IVAR_$_MCMStaticConfiguration._requireDataBackedPersona
+ _OBJC_IVAR_$_MCMStaticConfiguration._supportPersonasIfAvailable
+ _OBJC_IVAR_$_MCMStaticConfiguration._warnIfNotDataBackedPersona
+ _OBJC_IVAR_$_MCMXPCMessageBase._warnings
+ _OBJC_IVAR_$_MCMXPCMessageQuery._requireSecureByPlatformPolicy
+ __OBJC_$_PROP_LIST_MCMClientIdentity.197
+ __OBJC_$_PROP_LIST_MCMContainerConfiguration.267
+ __OBJC_$_PROP_LIST_MCMFileHandle.240
+ __OBJC_$_PROP_LIST_MCMUserIdentityCache.192
+ ___40-[MCMFileManager stripACLFromURL:error:]_block_invoke.481
+ ___41-[MCMFileManager mountPointForURL:error:]_block_invoke
+ ___42-[MCMContainerCacheEntry verifyWithError:]_block_invoke
+ ___51-[MCMFileHandle checkAppContainerProtection:error:]_block_invoke
+ ___55-[MCMFileManager _fixPOSIXPermsOnFD:FTSENT:stat:error:]_block_invoke.621
+ ___60-[MCMFileHandle registerAppContainerForProtectionWithError:]_block_invoke
+ ___63-[MCMFileManager repairPermissionsAtURL:uid:gid:options:error:]_block_invoke.547
+ ___63-[MCMFileManager repairPermissionsAtURL:uid:gid:options:error:]_block_invoke.553
+ ___63-[MCMFileManager repairPermissionsAtURL:uid:gid:options:error:]_block_invoke.559
+ ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.393
+ ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.396
+ ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.402
+ ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.408
+ ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.411
+ ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.414
+ ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.417
+ ___67-[MCMFileManager fixUserPermissionsAtURL:limitToTopLevelURL:error:]_block_invoke.494
+ ___68-[MCMFileManager _enumeratePOSIX1eACLEntriesAtURL:error:usingBlock:]_block_invoke.443
+ ___68-[MCMFileManager _enumeratePOSIX1eACLEntriesAtURL:error:usingBlock:]_block_invoke.449
+ ___75-[MCMFileManager checkFileSystemAtURL:isCaseSensitive:canAtomicSwap:error:]_block_invoke.425
+ ___75-[MCMFileManager checkFileSystemAtURL:isCaseSensitive:canAtomicSwap:error:]_block_invoke.428
+ ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.586
+ ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.592
+ ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.598
+ ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.604
+ ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.610
+ ___95-[MCMFileManager setDataProtectionAtURL:toDataProtectionClass:directoriesOnly:recursive:error:]_block_invoke.572
+ ___Block_byref_object_copy_.1060
+ ___Block_byref_object_copy_.1132
+ ___Block_byref_object_copy_.11783
+ ___Block_byref_object_copy_.12473
+ ___Block_byref_object_copy_.12819
+ ___Block_byref_object_copy_.13378
+ ___Block_byref_object_copy_.14231
+ ___Block_byref_object_copy_.14587
+ ___Block_byref_object_copy_.14845
+ ___Block_byref_object_copy_.2505
+ ___Block_byref_object_copy_.3276
+ ___Block_byref_object_copy_.3943
+ ___Block_byref_object_copy_.4342
+ ___Block_byref_object_copy_.5075
+ ___Block_byref_object_copy_.5347
+ ___Block_byref_object_copy_.7280
+ ___Block_byref_object_copy_.7813
+ ___Block_byref_object_copy_.8964
+ ___Block_byref_object_copy_.9156
+ ___Block_byref_object_copy_.9290
+ ___Block_byref_object_copy_.9758
+ ___Block_byref_object_copy_.9987
+ ___Block_byref_object_dispose_.1061
+ ___Block_byref_object_dispose_.1133
+ ___Block_byref_object_dispose_.11784
+ ___Block_byref_object_dispose_.12474
+ ___Block_byref_object_dispose_.12820
+ ___Block_byref_object_dispose_.13379
+ ___Block_byref_object_dispose_.14232
+ ___Block_byref_object_dispose_.14588
+ ___Block_byref_object_dispose_.14846
+ ___Block_byref_object_dispose_.2506
+ ___Block_byref_object_dispose_.3277
+ ___Block_byref_object_dispose_.3944
+ ___Block_byref_object_dispose_.4343
+ ___Block_byref_object_dispose_.5076
+ ___Block_byref_object_dispose_.5348
+ ___Block_byref_object_dispose_.7281
+ ___Block_byref_object_dispose_.7814
+ ___Block_byref_object_dispose_.8965
+ ___Block_byref_object_dispose_.9157
+ ___Block_byref_object_dispose_.9291
+ ___Block_byref_object_dispose_.9759
+ ___Block_byref_object_dispose_.9988
+ ___block_literal_global.1063
+ ___block_literal_global.10884
+ ___block_literal_global.11821
+ ___block_literal_global.12026
+ ___block_literal_global.1208
+ ___block_literal_global.1270
+ ___block_literal_global.12828
+ ___block_literal_global.1293
+ ___block_literal_global.13177
+ ___block_literal_global.13360
+ ___block_literal_global.13640
+ ___block_literal_global.13842
+ ___block_literal_global.1399
+ ___block_literal_global.14579
+ ___block_literal_global.14668
+ ___block_literal_global.14688
+ ___block_literal_global.1758
+ ___block_literal_global.2627
+ ___block_literal_global.457
+ ___block_literal_global.5051
+ ___block_literal_global.533
+ ___block_literal_global.5393
+ ___block_literal_global.6548
+ ___block_literal_global.7172
+ ___block_literal_global.7716
+ ___block_literal_global.8326
+ ___block_literal_global.8596
+ ___block_literal_global.9415
+ ___block_literal_global.9512
+ ___block_literal_global.977
+ _container_error_get_message
+ _defaultManager.onceToken.9404
+ _gCMSandboxSeam
+ _objc_msgSend$_checkIfSecureContainer:prefixes:error:
+ _objc_msgSend$_checkIfSecureContainers:error:
+ _objc_msgSend$_checkIfSecureURL:error:
+ _objc_msgSend$_containerIdentityWithError:
+ _objc_msgSend$_finalizeWithRealPathWithReason:containerIdentity:clientNegatesReference:error:
+ _objc_msgSend$_identifierPrefixesExemptFromAutomaticProtectionFromPlistValue:error:
+ _objc_msgSend$_legacySetOfUserIdentitiesForIdentifiers:targetUserIdentity:containerConfig:error:
+ _objc_msgSend$_queryPlanWithIdentifiers:containerConfig:clientIdentity:error:
+ _objc_msgSend$_recordAnalyticsEventWithAuthResult:clientIsAllowed:
+ _objc_msgSend$_recordAnalyticsEventWithSandboxExtensionIssueReason:clientIsAllowed:alwaysReturnPath:
+ _objc_msgSend$_setOfAvailableUserIdentitiesWithError:
+ _objc_msgSend$_userIdentityDisambiguatedFromUserIdentities:error:
+ _objc_msgSend$associatedWithParent
+ _objc_msgSend$checkAppContainerProtection:error:
+ _objc_msgSend$hasDynamicProtection
+ _objc_msgSend$identifierPrefixesExemptFromAutomaticProtection
+ _objc_msgSend$initWithErrorType:category:message:
+ _objc_msgSend$legacySetOfUserIdentitiesForIdentifiers:targetUserIdentity:containerConfig:clientIdentity:userIdentityCache:warnings:error:
+ _objc_msgSend$legacyUserIdentityForIdentifier:targetUserIdentity:containerConfig:clientIdentity:userIdentityCache:warnings:error:
+ _objc_msgSend$mountPointForURL:error:
+ _objc_msgSend$registerDynamicProtectionWithRestrictedEntitlement
+ _objc_msgSend$requireDataBackedPersona
+ _objc_msgSend$requireSecureByPlatformPolicy
+ _objc_msgSend$securedByPlatformPolicy
+ _objc_msgSend$userIdentitiesAssociatedWithContainerIdentifier:containerConfig:userIdentityCache:error:
+ _objc_msgSend$userInfo
+ _objc_msgSend$warnIfNotDataBackedPersona
+ _sharedInstance.instance.12337
+ _sharedInstance.onceToken.10289
+ _sharedInstance.onceToken.12336
- +[MCMXPCMessageBase(Helpers) userIdentityForContainerIdentifier:clientIdentity:containerClass:error:]
- -[MCMClientIdentity isAllowedToAccessContainerIdentity:error:]
- -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier _commonInit:]
- -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier _finalizeWithFabricatedPathWithReason:error:]
- -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier _finalizeWithRealPathWithReason:clientNegatesReference:error:]
- -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier _recordAnalyticsEventWithAuthResult:]
- -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier _recordAnalyticsEventWithSandboxExtensionIssueReason:]
- -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier alwaysReturnPath]
- -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier clientIsAllowed]
- -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier containerConfig]
- -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier containerIdentity]
- -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier error]
- -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier userIdentity]
- -[MCMCommandCreateOrLookupWithBundle _commonInit:]
- -[MCMCommandCreateOrLookupWithBundle containerClass]
- -[MCMCommandCreateOrLookupWithBundle containerIdentity]
- -[MCMCommandCreateOrLookupWithBundle error]
- -[MCMCommandCreateOrLookupWithBundle info]
- -[MCMCommandCreateOrLookupWithBundle userIdentity]
- -[MCMCommandQuery _queryPlanWithIdentifiers:isGroupClass:clientIdentity:error:]
- -[MCMCommandQuery _setOfUserIdentitiesForIdentifiers:isGroupClass:]
- -[MCMContainerCacheEntry metadata]
- -[MCMContainerCacheEntry setMetadata:]
- -[MCMContainerCacheEntry verify]
- -[MCMContainerConfiguration supportsProtectedContainerWithRestrictedEntitlement]
- GCC_except_table1025
- GCC_except_table1034
- GCC_except_table1038
- GCC_except_table1076
- GCC_except_table1077
- GCC_except_table1089
- GCC_except_table1091
- GCC_except_table1095
- GCC_except_table1100
- GCC_except_table1105
- GCC_except_table1115
- GCC_except_table1117
- GCC_except_table1120
- GCC_except_table1122
- GCC_except_table1126
- GCC_except_table1129
- GCC_except_table1131
- GCC_except_table1140
- GCC_except_table1142
- GCC_except_table1166
- GCC_except_table1176
- GCC_except_table1181
- GCC_except_table1185
- GCC_except_table1187
- GCC_except_table1239
- GCC_except_table1249
- GCC_except_table1280
- GCC_except_table1328
- GCC_except_table1330
- GCC_except_table1334
- GCC_except_table1335
- GCC_except_table1546
- GCC_except_table1592
- GCC_except_table1681
- GCC_except_table1833
- GCC_except_table1871
- GCC_except_table1875
- GCC_except_table1878
- GCC_except_table1896
- GCC_except_table1900
- GCC_except_table1938
- GCC_except_table1944
- GCC_except_table2007
- GCC_except_table2010
- GCC_except_table2120
- GCC_except_table2262
- GCC_except_table2279
- GCC_except_table2280
- GCC_except_table2356
- GCC_except_table2413
- GCC_except_table2428
- GCC_except_table2488
- GCC_except_table2500
- GCC_except_table2560
- GCC_except_table2570
- GCC_except_table2595
- GCC_except_table2624
- GCC_except_table2646
- GCC_except_table2650
- GCC_except_table2653
- GCC_except_table2657
- GCC_except_table2713
- GCC_except_table2802
- GCC_except_table2850
- GCC_except_table2853
- GCC_except_table2926
- GCC_except_table311
- GCC_except_table329
- GCC_except_table349
- GCC_except_table368
- GCC_except_table394
- GCC_except_table397
- GCC_except_table487
- GCC_except_table674
- GCC_except_table751
- GCC_except_table762
- GCC_except_table817
- GCC_except_table893
- GCC_except_table938
- GCC_except_table969
- GCC_except_table971
- _MCMRequirePersona.onceToken
- _MCMRequirePersona.result
- _MCMRequirePersonaAndConvertSystemToPersonal.onceToken
- _MCMRequirePersonaAndConvertSystemToPersonal.result
- _MCMRequirePersonaTelemetryOnly.onceToken
- _MCMRequirePersonaTelemetryOnly.result
- _OBJC_IVAR_$_MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier._alwaysReturnPath
- _OBJC_IVAR_$_MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier._clientIsAllowed
- _OBJC_IVAR_$_MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier._containerConfig
- _OBJC_IVAR_$_MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier._containerIdentity
- _OBJC_IVAR_$_MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier._error
- _OBJC_IVAR_$_MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier._userIdentity
- _OBJC_IVAR_$_MCMCommandCreateOrLookupWithBundle._containerClass
- _OBJC_IVAR_$_MCMCommandCreateOrLookupWithBundle._containerIdentity
- _OBJC_IVAR_$_MCMCommandCreateOrLookupWithBundle._error
- _OBJC_IVAR_$_MCMCommandCreateOrLookupWithBundle._info
- _OBJC_IVAR_$_MCMCommandCreateOrLookupWithBundle._userIdentity
- _OBJC_IVAR_$_MCMContainerCacheEntry._metadata
- _OBJC_IVAR_$_MCMContainerCacheEntry._metadataLock
- _OBJC_IVAR_$_MCMContainerConfiguration._supportsProtectedContainerWithRestrictedEntitlement
- __OBJC_$_PROP_LIST_MCMClientIdentity.199
- __OBJC_$_PROP_LIST_MCMContainerConfiguration.239
- __OBJC_$_PROP_LIST_MCMFileHandle.230
- __OBJC_$_PROP_LIST_MCMUserIdentityCache.191
- ___32-[MCMContainerCacheEntry verify]_block_invoke
- ___40-[MCMFileManager stripACLFromURL:error:]_block_invoke.479
- ___55-[MCMFileManager _fixPOSIXPermsOnFD:FTSENT:stat:error:]_block_invoke.619
- ___63-[MCMFileManager repairPermissionsAtURL:uid:gid:options:error:]_block_invoke.545
- ___63-[MCMFileManager repairPermissionsAtURL:uid:gid:options:error:]_block_invoke.551
- ___63-[MCMFileManager repairPermissionsAtURL:uid:gid:options:error:]_block_invoke.557
- ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.388
- ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.391
- ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.397
- ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.403
- ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.406
- ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.409
- ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.412
- ___67-[MCMFileManager fixUserPermissionsAtURL:limitToTopLevelURL:error:]_block_invoke.492
- ___68-[MCMFileManager _enumeratePOSIX1eACLEntriesAtURL:error:usingBlock:]_block_invoke.441
- ___68-[MCMFileManager _enumeratePOSIX1eACLEntriesAtURL:error:usingBlock:]_block_invoke.447
- ___75-[MCMFileManager checkFileSystemAtURL:isCaseSensitive:canAtomicSwap:error:]_block_invoke.420
- ___75-[MCMFileManager checkFileSystemAtURL:isCaseSensitive:canAtomicSwap:error:]_block_invoke.423
- ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.584
- ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.590
- ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.596
- ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.602
- ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.608
- ___95-[MCMFileManager setDataProtectionAtURL:toDataProtectionClass:directoriesOnly:recursive:error:]_block_invoke.570
- ___Block_byref_object_copy_.1064
- ___Block_byref_object_copy_.1136
- ___Block_byref_object_copy_.11765
- ___Block_byref_object_copy_.12456
- ___Block_byref_object_copy_.12806
- ___Block_byref_object_copy_.13371
- ___Block_byref_object_copy_.14222
- ___Block_byref_object_copy_.14578
- ___Block_byref_object_copy_.14829
- ___Block_byref_object_copy_.2491
- ___Block_byref_object_copy_.3264
- ___Block_byref_object_copy_.3927
- ___Block_byref_object_copy_.4322
- ___Block_byref_object_copy_.5052
- ___Block_byref_object_copy_.5324
- ___Block_byref_object_copy_.7231
- ___Block_byref_object_copy_.7758
- ___Block_byref_object_copy_.8941
- ___Block_byref_object_copy_.9133
- ___Block_byref_object_copy_.9267
- ___Block_byref_object_copy_.9723
- ___Block_byref_object_copy_.9949
- ___Block_byref_object_dispose_.1065
- ___Block_byref_object_dispose_.1137
- ___Block_byref_object_dispose_.11766
- ___Block_byref_object_dispose_.12457
- ___Block_byref_object_dispose_.12807
- ___Block_byref_object_dispose_.13372
- ___Block_byref_object_dispose_.14223
- ___Block_byref_object_dispose_.14579
- ___Block_byref_object_dispose_.14830
- ___Block_byref_object_dispose_.2492
- ___Block_byref_object_dispose_.3265
- ___Block_byref_object_dispose_.3928
- ___Block_byref_object_dispose_.4323
- ___Block_byref_object_dispose_.5053
- ___Block_byref_object_dispose_.5325
- ___Block_byref_object_dispose_.7232
- ___Block_byref_object_dispose_.7759
- ___Block_byref_object_dispose_.8942
- ___Block_byref_object_dispose_.9134
- ___Block_byref_object_dispose_.9268
- ___Block_byref_object_dispose_.9724
- ___Block_byref_object_dispose_.9950
- ___MCMRequirePersonaAndConvertSystemToPersonal_block_invoke
- ___MCMRequirePersonaTelemetryOnly_block_invoke
- ___MCMRequirePersona_block_invoke
- ___block_literal_global.1067
- ___block_literal_global.10840
- ___block_literal_global.11803
- ___block_literal_global.12008
- ___block_literal_global.1214
- ___block_literal_global.1279
- ___block_literal_global.12815
- ___block_literal_global.1302
- ___block_literal_global.13170
- ___block_literal_global.13353
- ___block_literal_global.13632
- ___block_literal_global.13834
- ___block_literal_global.14
- ___block_literal_global.1408
- ___block_literal_global.14570
- ___block_literal_global.14659
- ___block_literal_global.14679
- ___block_literal_global.1757
- ___block_literal_global.18
- ___block_literal_global.21
- ___block_literal_global.2614
- ___block_literal_global.455
- ___block_literal_global.5028
- ___block_literal_global.531
- ___block_literal_global.5370
- ___block_literal_global.6521
- ___block_literal_global.7122
- ___block_literal_global.7662
- ___block_literal_global.8269
- ___block_literal_global.8540
- ___block_literal_global.9395
- ___block_literal_global.9502
- ___block_literal_global.981
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_ContainerManagerCommon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_ContainerManagerCommon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_ContainerManagerCommon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_ContainerManagerCommon
- _container_error_create
- _defaultManager.onceToken.9384
- _objc_msgSend$_commonInit:
- _objc_msgSend$_finalizeWithFabricatedPathWithReason:error:
- _objc_msgSend$_finalizeWithRealPathWithReason:clientNegatesReference:error:
- _objc_msgSend$_queryPlanWithIdentifiers:isGroupClass:clientIdentity:error:
- _objc_msgSend$_recordAnalyticsEventWithAuthResult:
- _objc_msgSend$_recordAnalyticsEventWithSandboxExtensionIssueReason:
- _objc_msgSend$_setOfUserIdentitiesForIdentifiers:isGroupClass:
- _objc_msgSend$alwaysReturnPath
- _objc_msgSend$clientIsAllowed
- _objc_msgSend$isAllowedToAccessContainerIdentity:error:
- _objc_msgSend$isExplicitlyPersonal
- _objc_msgSend$personaIdentifier
- _objc_msgSend$supportsProtectedContainerWithRestrictedEntitlement
- _objc_msgSend$userIdentityForContainerIdentifier:clientIdentity:containerClass:error:
- _objc_msgSend$verify
- _sharedInstance.instance.12320
- _sharedInstance.onceToken.10245
- _sharedInstance.onceToken.12319
CStrings:
+ "(%@|%llu|%@|%@|%@|%@%s%s)"
+ "(%llu|%llu|%d|[%@]%@)"
+ "-[MCMFileHandle checkAppContainerProtection:error:]_block_invoke"
+ "-[MCMFileHandle registerAppContainerForProtectionWithError:]_block_invoke"
+ "-[MCMFileManager mountPointForURL:error:]_block_invoke"
+ "00:54:12"
+ "<%@: %p; identifier = %@, generation = %llu, containerPath = %@, schemaVersion = %@, uuid = %@, fsNode = %@%s%s>"
+ "@40@0:8^Q16@24^@32"
+ "@44@0:8^Q16@24B32^@36"
+ "@72@0:8@16@24@32@40@48@56^@64"
+ "Attempted to create error with uninitialized error type."
+ "Attempted to recover, but verification failed; identifier = [%@], uuid = %@, schemaVersion = %@, error = %@"
+ "Client has not adopted an unambiguous persona; client = %@"
+ "Client ineligible for the requested persona; client = %@, requested = %@"
+ "Client requested an ambiguous persona; target = %@"
+ "Could not resolve user identities; client = %@, class = %@"
+ "Could not resolve user identities; identifier = %@, class = %@"
+ "Evaluating requested target userIdentity: %@"
+ "Failed to check mount point at [%@]: %@"
+ "Failed to verify container while looking up [%@]. FATAL; error = %@"
+ "Identifier prefixes is not in a valid format; expected = NSArray, got = %@, value = %@"
+ "Identifier prefixes value is not in a valid format; expected = NSArray<NSString>, got = NSArray<%@>, value = %@"
+ "It is undefined behavior to look up a container with a persona other than personal or data separated. Please adopt a persona first. Assuming personal. given persona = (%@)"
+ "Jun 17 2025"
+ "MobileContainerManager-725.0.8~334"
+ "Not expected to use legacy user identity resolution with modern persona policy."
+ "Not expected to use modern user identity resolution with legacy persona policy."
+ "Persona [%@] volume not mounted at [%@]"
+ "Query's explicit userIdentity: %@"
+ "Requested container has multiple persona; client = %@, class = %@, personas = %@"
+ "Requested owned container has multiple persona; client = %@, class = %@"
+ "T@\"NSSet\",R,N,V_identifierPrefixesExemptFromAutomaticProtection"
+ "TB,R,N,V_associatedWithParent"
+ "TB,R,N,V_enforceBasedOnDynamicProtectionState"
+ "TB,R,N,V_enforceBasedOnStrictSignatureScrutiny"
+ "TB,R,N,V_hasDynamicProtection"
+ "TB,R,N,V_registerDynamicProtectionWithRestrictedEntitlement"
+ "TB,R,N,V_requireDataBackedPersona"
+ "TB,R,N,V_requireSecureByPlatformPolicy"
+ "TB,R,N,V_securedByPlatformPolicy"
+ "TB,R,N,V_supportPersonasIfAvailable"
+ "TB,R,N,V_warnIfNotDataBackedPersona"
+ "Using client-based userIdentity: %@"
+ "_associatedWithParent"
+ "_checkIfSecureContainer:prefixes:error:"
+ "_checkIfSecureContainers:error:"
+ "_checkIfSecureURL:error:"
+ "_containerIdentityWithError:"
+ "_enforceBasedOnDynamicProtectionState"
+ "_enforceBasedOnStrictSignatureScrutiny"
+ "_finalizeWithRealPathWithReason:containerIdentity:clientNegatesReference:error:"
+ "_finalizeWithSynthesizedPathWithReason:containerIdentity:error:"
+ "_hasDynamicProtection"
+ "_identifierPrefixesExemptFromAutomaticProtection"
+ "_identifierPrefixesExemptFromAutomaticProtectionFromPlistValue:error:"
+ "_legacySetOfUserIdentitiesForIdentifiers:targetUserIdentity:containerConfig:error:"
+ "_queryPlanWithIdentifiers:containerConfig:clientIdentity:error:"
+ "_recordAnalyticsEventWithAuthResult:clientIsAllowed:"
+ "_recordAnalyticsEventWithSandboxExtensionIssueReason:clientIsAllowed:alwaysReturnPath:"
+ "_registerDynamicProtectionWithRestrictedEntitlement"
+ "_requireDataBackedPersona"
+ "_requireSecureByPlatformPolicy"
+ "_securedByPlatformPolicy"
+ "_setOfAvailableUserIdentitiesWithError:"
+ "_supportPersonasIfAvailable"
+ "_userIdentityDisambiguatedFromUserIdentities:error:"
+ "_warnIfNotDataBackedPersona"
+ "associatedWithParent"
+ "enforceBasedOnDynamicProtectionState"
+ "enforceBasedOnStrictSignatureScrutiny"
+ "hasDynamicProtection"
+ "identifierPrefixesExemptFromAutomaticProtection"
+ "legacySetOfUserIdentitiesForIdentifiers:targetUserIdentity:containerConfig:clientIdentity:userIdentityCache:warnings:error:"
+ "legacyUserIdentityForIdentifier:targetUserIdentity:containerConfig:clientIdentity:userIdentityCache:warnings:error:"
+ "mountPointForURL:error:"
+ "registerDynamicProtectionWithRestrictedEntitlement"
+ "requireDataBackedPersona"
+ "requireSecureByPlatformPolicy"
+ "sandbox_check_protected_app_container() failed on path [%s]: error = %{darwin.errno}d"
+ "sandbox_register_app_container() failed on path [%s]: error = (%d) %s"
+ "securedByPlatformPolicy"
+ "supportPersonasIfAvailable"
+ "userIdentitiesAssociatedWithContainerIdentifier:containerConfig:userIdentityCache:error:"
+ "userInfo"
+ "v28@0:8Q16B24"
+ "v32@0:8Q16B24B28"
+ "warnIfNotDataBackedPersona"
- " NOT"
- "(%@|%llu|%@|%@|%@|%@|%s metadata%s%s)"
- "(%llu|%llu|%d|[%@])"
- "20:50:38"
- "<%@: %p; identifier = %@, generation = %llu, containerPath = %@, schemaVersion = %@, uuid = %@, fsNode = %@, metadata = %@%s%s>"
- "@\"MCMCodeSignInfo\""
- "@32@0:8^Q16^@24"
- "@36@0:8^Q16B24^@28"
- "@44@0:8@16B24@28^@36"
- "@48@0:8@16@24Q32^Q40"
- "Ambiguous user identity from [%@]. Expected one of [%@], got %@"
- "Attempted to recover, but verification failed; identifier = [%@], uuid = %@, schemaVersion = %@"
- "B32@0:8@16^Q24"
- "Chose bundleIdentifier: %@, userIdentities: %@ for identifier: %@, class: %llu"
- "Client %{public}@ failed trying to look up persona for %llu:%@"
- "Client %{public}@ is not allowed to access container identity %{public}@: error %llu"
- "Client %{public}@ trying to look up container %@:%{public}@ while in one of the System personas or no persona (%{public}@ / %{public}@)"
- "Client %{public}@ trying to look up container %@:%{public}@ while in one of the System personas or no persona - converting to Personal"
- "Client %{public}@ trying to look up container %llu:%{public}@ while in one of the System personas or no persona"
- "Client %{public}@ trying to look up container %llu:%{public}@ while in one of the System personas or no persona (%{public}@)"
- "Client %{public}@ trying to look up container %llu:%{public}@ while in one of the System personas or no persona - converting to Personal"
- "Client %{public}@ trying to look up container %llu:%{public}@ with ambiguous user identity (client: %{public}@; container: %{public}@)"
- "Client %{public}@ user identity does not match container user identity (client: %{public}@; container: %{public}@)"
- "E"
- "For %{public}@ ,%s substituting user identity %{public}@ for client identity %{public}@ for container %llu:%@"
- "Jun  1 2025"
- "MobileContainerManager-725.0.3.0.1~176"
- "T@\"<MCMMetadata>\",&,N,V_metadata"
- "T@\"MCMCodeSignInfo\",R,N,V_info"
- "TB,R,N,V_alwaysReturnPath"
- "TB,R,N,V_clientIsAllowed"
- "TB,R,N,V_supportsProtectedContainerWithRestrictedEntitlement"
- "_alwaysReturnPath"
- "_clientIsAllowed"
- "_commonInit:"
- "_finalizeWithFabricatedPathWithReason:error:"
- "_finalizeWithRealPathWithReason:clientNegatesReference:error:"
- "_metadataLock"
- "_queryPlanWithIdentifiers:isGroupClass:clientIdentity:error:"
- "_recordAnalyticsEventWithAuthResult:"
- "_recordAnalyticsEventWithSandboxExtensionIssueReason:"
- "_setOfUserIdentitiesForIdentifiers:isGroupClass:"
- "_supportsProtectedContainerWithRestrictedEntitlement"
- "alwaysReturnPath"
- "clientIsAllowed"
- "convert_system_persona_to_personal"
- "isAllowedToAccessContainerIdentity:error:"
- "message userIdentity: %@"
- "require_persona"
- "require_persona_telemetry_only"
- "setMetadata:"
- "supportsProtectedContainerWithRestrictedEntitlement"
- "userIdentity: %@"
- "userIdentityForContainerIdentifier:clientIdentity:containerClass:error:"
- "verify"
- "with"
- "without"
- "\x81"

```
