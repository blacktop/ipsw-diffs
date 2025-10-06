## MobileTimer

> `/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer`

```diff

-2303.1.2.0.0
-  __TEXT.__text: 0x106894
-  __TEXT.__auth_stubs: 0x1800
-  __TEXT.__objc_methlist: 0xd744
+2303.1.7.0.0
+  __TEXT.__text: 0x107b7c
+  __TEXT.__auth_stubs: 0x1830
+  __TEXT.__objc_methlist: 0xd7cc
   __TEXT.__const: 0x1310
-  __TEXT.__oslogstring: 0x10f73
+  __TEXT.__oslogstring: 0x10ff3
   __TEXT.__cstring: 0x9656
-  __TEXT.__gcc_except_tab: 0x147c
+  __TEXT.__gcc_except_tab: 0x148c
   __TEXT.__dlopen_cstrs: 0x837
   __TEXT.__ustring: 0x1a
-  __TEXT.__swift5_typeref: 0x86a
+  __TEXT.__swift5_typeref: 0x904
   __TEXT.__swift5_reflstr: 0x2ad
   __TEXT.__swift5_assocty: 0xd8
   __TEXT.__constg_swiftt: 0x548
   __TEXT.__swift5_fieldmd: 0x334
   __TEXT.__swift5_proto: 0x68
   __TEXT.__swift5_types: 0x64
-  __TEXT.__swift5_capture: 0xf74
+  __TEXT.__swift5_capture: 0xf88
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift_as_entry: 0x104
   __TEXT.__swift_as_ret: 0x108
-  __TEXT.__unwind_info: 0x4910
+  __TEXT.__unwind_info: 0x4948
   __TEXT.__eh_frame: 0x3150
   __TEXT.__objc_classname: 0x1955
-  __TEXT.__objc_methname: 0x17e37
+  __TEXT.__objc_methname: 0x17f3a
   __TEXT.__objc_methtype: 0x4248
-  __TEXT.__objc_stubs: 0x11c80
-  __DATA_CONST.__got: 0xc58
-  __DATA_CONST.__const: 0x4240
+  __TEXT.__objc_stubs: 0x11d80
+  __DATA_CONST.__got: 0xc60
+  __DATA_CONST.__const: 0x42b8
   __DATA_CONST.__objc_classlist: 0x688
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6028
+  __DATA_CONST.__objc_selrefs: 0x6068
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x420
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0xc10
-  __AUTH_CONST.__const: 0x39b8
+  __AUTH_CONST.__auth_got: 0xc28
+  __AUTH_CONST.__const: 0x39e0
   __AUTH_CONST.__cfstring: 0x7000
-  __AUTH_CONST.__objc_const: 0x28d60
+  __AUTH_CONST.__objc_const: 0x28d90
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x2da0
   __AUTH.__data: 0x3c8
-  __DATA.__objc_ivar: 0x95c
-  __DATA.__data: 0x2b28
+  __DATA.__objc_ivar: 0x960
+  __DATA.__data: 0x2b48
   __DATA.__common: 0x68
-  __DATA.__bss: 0x1190
+  __DATA.__bss: 0x11a0
   __DATA_DIRTY.__objc_data: 0x18b0
   __DATA_DIRTY.__bss: 0x288
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 5C6E64A2-15F7-3A94-A200-40E60CCC0AA8
-  Functions: 6578
-  Symbols:   18288
-  CStrings:  8382
+  UUID: CD22BA67-60FE-3644-9B0C-C68BA8F9D5BE
+  Functions: 6603
+  Symbols:   18351
+  CStrings:  8391
 
Symbols:
+ -[MTTimerDurationManager _withLock:]
+ -[MTTimerDurationManager clearAllDurationsWithCompletion:]
+ -[MTTimerDurationManager lock]
+ -[MTTimerDurationManager restoreFromDataStoreSync]
+ -[MTTimerDurationManager restoreFromDataStoreWithCompletion:]
+ -[MTTimerDurationManager setLock:]
+ -[MTTimerStorage durationFromCD:]
+ -[MTTimerStorage durationsFromCD:]
+ -[MTTimerStorage store_addDurations:isFavorite:completion:]
+ -[MTTimerStorage store_deleteDuration:isFavorite:completion:]
+ -[MTTimerStorage store_getAllDurations:completion:]
+ -[MTTimerStorage store_getRecentsFavoritesLatest:]
+ _OBJC_IVAR_$_MTTimerDurationManager._lock
+ __OBJC_$_PROP_LIST_MTTimerStorage.361
+ ___34-[MTTimerStorage durationsFromCD:]_block_invoke
+ ___41-[MTTimerDurationManager recentDurations]_block_invoke
+ ___45-[MTTimerDurationManager restoreFromDefaults]_block_invoke
+ ___50-[MTTimerDurationManager restoreFromDataStoreSync]_block_invoke
+ ___50-[MTTimerStorage store_getRecentsFavoritesLatest:]_block_invoke
+ ___51-[MTTimerDurationManager clearPersistenceDurations]_block_invoke
+ ___51-[MTTimerStorage store_getAllDurations:completion:]_block_invoke
+ ___55-[MTTimerDurationManager migrateFromDefaultsToCoreData]_block_invoke
+ ___61-[MTTimerDurationManager restoreFromDataStoreWithCompletion:]_block_invoke
+ ___61-[MTTimerDurationManager restoreFromDataStoreWithCompletion:]_block_invoke_2
+ ___61-[MTTimerDurationManager restoreFromDataStoreWithCompletion:]_block_invoke_3
+ ___61-[MTTimerDurationManager restoreFromDataStoreWithCompletion:]_block_invoke_4
+ ___65-[MTTimerDurationManager addDuration:toCollection:withKey:limit:]_block_invoke
+ ___76-[MTTimerDurationManager removeDuration:fromCollection:withKey:synchronize:]_block_invoke
+ ___block_descriptor_40_e8_32s_e27_16?0"MTCDTimerDuration"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e51_v32?0"NSArray"8"NSArray"16"MTCDTimerDuration"24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e51_v32?0"NSArray"8"NSArray"16"MTCDTimerDuration"24ls40l8s32l8
+ ___block_descriptor_65_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.10
+ _objc_msgSend$addDurations:isFavorite:completion:
+ _objc_msgSend$clearAllDurationsWithCompletion:
+ _objc_msgSend$deleteDuration:isFavorite:completion:
+ _objc_msgSend$durationFromCD:
+ _objc_msgSend$durationsFromCD:
+ _objc_msgSend$getAllDurationsWithCompletion:
+ _objc_msgSend$restoreFromDataStoreSync
+ _objc_msgSend$restoreFromDataStoreWithCompletion:
+ _objc_msgSend$setCoreDataStore:
+ _symbolic _____ySSSg_____G 7Combine19CurrentValueSubjectC s5NeverO
+ _symbolic _____y______ySSSg_____GG 7Combine10PublishersO5ShareC AA19CurrentValueSubjectC s5NeverO
+ _symbolic _____y______y______ySSSg_____GGSSG 7Combine10PublishersO10CompactMapV AC5ShareC AA19CurrentValueSubjectC s5NeverO
+ _symbolic _____y______y______y______ySSSg_____GGSSG_____G 7Combine10PublishersO14SetFailureTypeV AC10CompactMapV AC5ShareC AA19CurrentValueSubjectC s5NeverO 11MobileTimer15ConductorStatusO
+ _symbolic _____y______y______y______y______ySSSg_____GGSSG_____GG 7Combine10PublishersO10FirstWhereV AC14SetFailureTypeV AC10CompactMapV AC5ShareC AA19CurrentValueSubjectC s5NeverO 11MobileTimer15ConductorStatusO
+ _symbolic _____y______y______y______y______y______ySSSg_____GGSSG_____GGSo17OS_dispatch_queueCG 7Combine10PublishersO7TimeoutV AC10FirstWhereV AC14SetFailureTypeV AC10CompactMapV AC5ShareC AA19CurrentValueSubjectC s5NeverO 11MobileTimer15ConductorStatusO
+ _symbolic _____y______y______y______y______y______yytSg_____GGytG_____GGSo17OS_dispatch_queueCG 7Combine10PublishersO7TimeoutV AC5FirstV AC14SetFailureTypeV AC10CompactMapV AC5ShareC AA19CurrentValueSubjectC s5NeverO 11MobileTimer15ConductorStatusO
+ _symbolic _____y______y______y______y______yytSg_____GGytG_____GG 7Combine10PublishersO5FirstV AC14SetFailureTypeV AC10CompactMapV AC5ShareC AA19CurrentValueSubjectC s5NeverO 11MobileTimer15ConductorStatusO
+ _symbolic _____y______y______y______yytSg_____GGytG_____G 7Combine10PublishersO14SetFailureTypeV AC10CompactMapV AC5ShareC AA19CurrentValueSubjectC s5NeverO 11MobileTimer15ConductorStatusO
+ _symbolic _____y______y______yytSg_____GGytG 7Combine10PublishersO10CompactMapV AC5ShareC AA19CurrentValueSubjectC s5NeverO
+ _symbolic _____y______yytSg_____GG 7Combine10PublishersO5ShareC AA19CurrentValueSubjectC s5NeverO
+ _symbolic _____yxSg_____G 7Combine19CurrentValueSubjectC s5NeverO
+ _symbolic _____yytSg_____G 7Combine19CurrentValueSubjectC s5NeverO
- -[MTTimerDurationManager restoreFromDataStore]
- __OBJC_$_PROP_LIST_MTTimerStorage.351
- ___46-[MTTimerDurationManager restoreFromDataStore]_block_invoke
- ___46-[MTTimerDurationManager restoreFromDataStore]_block_invoke_2
- ___46-[MTTimerDurationManager restoreFromDataStore]_block_invoke_3
- ___block_descriptor_40_e8_32s_e51_v32?0"NSArray"8"NSArray"16"MTCDTimerDuration"24ls32l8
- _objc_msgSend$restoreFromDataStore
- _symbolic _____ySS_____G 7Combine18PassthroughSubjectC s5NeverO
- _symbolic _____y______ySS_____GG 7Combine10PublishersO5ShareC AA18PassthroughSubjectC s5NeverO
- _symbolic _____y______y______ySS_____GG_____G 7Combine10PublishersO14SetFailureTypeV AC5ShareC AA18PassthroughSubjectC s5NeverO 11MobileTimer15ConductorStatusO
- _symbolic _____y______y______y______ySS_____GG_____GG 7Combine10PublishersO10FirstWhereV AC14SetFailureTypeV AC5ShareC AA18PassthroughSubjectC s5NeverO 11MobileTimer15ConductorStatusO
- _symbolic _____y______y______y______y______ySS_____GG_____GGSo17OS_dispatch_queueCG 7Combine10PublishersO7TimeoutV AC10FirstWhereV AC14SetFailureTypeV AC5ShareC AA18PassthroughSubjectC s5NeverO 11MobileTimer15ConductorStatusO
- _symbolic _____y______y______y______y______yyt_____GG_____GGSo17OS_dispatch_queueCG 7Combine10PublishersO7TimeoutV AC5FirstV AC14SetFailureTypeV AC5ShareC AA18PassthroughSubjectC s5NeverO 11MobileTimer15ConductorStatusO
- _symbolic _____y______y______y______yyt_____GG_____GG 7Combine10PublishersO5FirstV AC14SetFailureTypeV AC5ShareC AA18PassthroughSubjectC s5NeverO 11MobileTimer15ConductorStatusO
- _symbolic _____y______y______yyt_____GG_____G 7Combine10PublishersO14SetFailureTypeV AC5ShareC AA18PassthroughSubjectC s5NeverO 11MobileTimer15ConductorStatusO
- _symbolic _____y______yyt_____GG 7Combine10PublishersO5ShareC AA18PassthroughSubjectC s5NeverO
- _symbolic _____yx_____G 7Combine18PassthroughSubjectC s5NeverO
- _symbolic _____yyt_____G 7Combine18PassthroughSubjectC s5NeverO
CStrings:
+ "%{public}@ restoreFromDataStoreSync"
+ "%{public}@ restoreFromDataStoreWithCompletion"
+ "%{public}@ returning timer duration query, recents:%{public}@ favorites:%{public}@ default:%{public}@ latest:%{public}@"
+ "clearAllDurationsWithCompletion:"
+ "durationFromCD:"
+ "durationsFromCD:"
+ "restoreFromDataStoreSync"
+ "restoreFromDataStoreWithCompletion:"
+ "store_addDurations:isFavorite:completion:"
+ "store_deleteDuration:isFavorite:completion:"
+ "store_getAllDurations:completion:"
+ "store_getRecentsFavoritesLatest:"
- "%{public}@ restoreFromDataStore"
- "%{public}@ returning timer duration query"
- "restoreFromDataStore"

```
