## CascadeSets

> `/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets`

```diff

-166.23.1.0.0
-  __TEXT.__text: 0x4d954
+192.0.0.0.0
+  __TEXT.__text: 0x4f4fc
   __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x44dc
+  __TEXT.__objc_methlist: 0x4694
   __TEXT.__const: 0x1b8
-  __TEXT.__gcc_except_tab: 0x1128
-  __TEXT.__cstring: 0x3968
-  __TEXT.__oslogstring: 0x4765
+  __TEXT.__gcc_except_tab: 0x1110
+  __TEXT.__cstring: 0x3ab6
+  __TEXT.__oslogstring: 0x4983
   __TEXT.__dlopen_cstrs: 0x278
-  __TEXT.__unwind_info: 0x1338
-  __TEXT.__objc_classname: 0xac2
-  __TEXT.__objc_methname: 0x9b18
-  __TEXT.__objc_methtype: 0x1da1
-  __TEXT.__objc_stubs: 0x6ac0
+  __TEXT.__unwind_info: 0x1358
+  __TEXT.__objc_classname: 0xade
+  __TEXT.__objc_methname: 0xa0f8
+  __TEXT.__objc_methtype: 0x1e4b
+  __TEXT.__objc_stubs: 0x6ce0
   __DATA_CONST.__got: 0x488
-  __DATA_CONST.__const: 0x1210
-  __DATA_CONST.__objc_classlist: 0x338
+  __DATA_CONST.__const: 0x1228
+  __DATA_CONST.__objc_classlist: 0x340
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2300
+  __DATA_CONST.__objc_selrefs: 0x23f0
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x2b8
-  __DATA_CONST.__objc_arraydata: 0x38
+  __DATA_CONST.__objc_superrefs: 0x2c0
+  __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x508
   __AUTH_CONST.__const: 0x190
-  __AUTH_CONST.__cfstring: 0x31e0
-  __AUTH_CONST.__objc_const: 0xa9e0
-  __AUTH_CONST.__objc_intobj: 0x3c0
+  __AUTH_CONST.__cfstring: 0x3400
+  __AUTH_CONST.__objc_const: 0xae38
+  __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH.__objc_data: 0xc8
-  __DATA.__objc_ivar: 0x498
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x4d0
   __DATA.__data: 0xaf8
   __DATA.__bss: 0x48
-  __DATA_DIRTY.__objc_data: 0x1f68
+  __DATA_DIRTY.__objc_data: 0x1f90
   __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 772B60B2-EFEE-39F5-91EA-C9277B195129
-  Functions: 1784
-  Symbols:   6295
-  CStrings:  3195
+  UUID: BFBB2A57-2631-3DFF-863E-880B2E0E121B
+  Functions: 1817
+  Symbols:   6408
+  CStrings:  3302
 
Symbols:
+ +[CCDataResourceWriter incrementRowsModified:database:].cold.1
+ +[CCDataResourceWriter incrementRowsModified:database:].cold.2
+ +[CCDatabaseUpdater _writeRecordWithKey:stringValue:integerValue:dataValue:onConflictType:database:error:]
+ +[CCDatabaseUpdater upsertLastMaintenanceDate:database:error:]
+ +[CCDatabaseUpdater upsertRowsModified:database:error:]
+ +[CCDonateServicePriors supportsSecureCoding]
+ +[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]
+ +[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:].cold.1
+ +[CCSetDonation donationWithName:itemType:service:errorCode:priors:]
+ +[CCSetDonation fullSetDonationWithItemType:completion:]
+ +[CCSetDonation incrementalSetDonationWithItemType:completion:]
+ +[CCSetDonation incrementalSetDonationWithItemType:descriptors:completion:]
+ +[CCSetDonation incrementalSetDonationWithItemType:descriptors:serviceProvider:completion:]
+ +[CCSetsAccessDaemonDelegate _loadResourceGenerationCounter:baseSystemPath:error:]
+ +[CCSetsAccessDaemonDelegate readDefaultLocalDeviceUUID:]
+ -[CCDatabaseDeviceMapping activeDeviceSiteWithDeviceUUID:]
+ -[CCDatabaseUpdater _incrementLocalDeltaGeneration]
+ -[CCDatabaseUpdater _incrementLocalDeltaGeneration].cold.1
+ -[CCDatabaseUpdater _persistDateWithDeltaProduced:isFullSet:]
+ -[CCDatabaseUpdater _persistRevisionTokenIfNotNil:]
+ -[CCDatabaseUpdater _selectLocalSourcePersistedValuesOutVersion:outValidityHash:outRevisionToken:outDonationDate:outFullSetDonationDate:]
+ -[CCDatabaseUpdater _selectPersistedValueForKey:outValue:valueClass:]
+ -[CCDatabaseUpdater _updateDeviceRowId:deltaGeneration:expirationDate:]
+ -[CCDatabaseUpdater _updateDeviceRowId:deltaGeneration:expirationDate:].cold.1
+ -[CCDatabaseUpdater _updateDeviceRowId:deltaGeneration:expirationDate:].cold.2
+ -[CCDatabaseUpdater _updateDeviceRowId:deltaGeneration:expirationDate:].cold.3
+ -[CCDatabaseUpdater _upsertInteger:forKey:]
+ -[CCDatabaseUpdater _upsertInteger:forKey:skipIfNil:]
+ -[CCDatabaseUpdater _writeRecordWithKey:stringValue:integerValue:dataValue:onConflictType:]
+ -[CCDatabaseUpdater finishAndDetectDelta:updateRevisionToken:isFullSet:]
+ -[CCDatabaseUpdater priorLocalDonationDate]
+ -[CCDatabaseUpdater priorLocalFullSetDonationDate]
+ -[CCDatabaseUpdater priorLocalSourceRevisionToken]
+ -[CCDatabaseUpdater registerRemoteDeviceSite:isPeer:hasDeltas:returningRowId:]
+ -[CCDeviceRecord deltaGeneration]
+ -[CCDeviceSite deltaGeneration]
+ -[CCDeviceSite initFromDictionary:].cold.1
+ -[CCDeviceSite initWithDevice:resourceGeneration:deltaGeneration:expirationDate:]
+ -[CCDeviceSite isEqualToDeviceSite:]
+ -[CCDonateServicePriors .cxx_destruct]
+ -[CCDonateServicePriors donationDate]
+ -[CCDonateServicePriors encodeWithCoder:]
+ -[CCDonateServicePriors fullSetDonationDate]
+ -[CCDonateServicePriors initWithCoder:]
+ -[CCDonateServicePriors initWithVersion:instanceCount:donationDate:fullSetDonationDate:revisionToken:options:]
+ -[CCDonateServicePriors instanceCount]
+ -[CCDonateServicePriors isAwaitingFullSet]
+ -[CCDonateServicePriors options]
+ -[CCDonateServicePriors revisionToken]
+ -[CCDonateServicePriors version]
+ -[CCDonateXPCClient endSetDonationWithOptions:revisionToken:completion:]
+ -[CCIncrementalSetDonation designateAsFullSet]
+ -[CCIncrementalSetDonation isAwaitingFullSet]
+ -[CCSet initWithSet:error:]
+ -[CCSetDonation _addFinishOptions:]
+ -[CCSetDonation _addItem:error:]
+ -[CCSetDonation _finishWithOptions:error:]
+ -[CCSetDonation _mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]
+ -[CCSetDonation _removeSourceItemIdentifier:error:]
+ -[CCSetDonation initWithName:itemType:service:errorCode:priors:flushThreshold:]
+ -[CCSetDonation initWithName:itemType:service:errorCode:priors:flushThreshold:].cold.1
+ -[CCSetDonation priorDonationDate]
+ -[CCSetDonation priorFullSetDonationDate]
+ -[CCSetDonation priorInstanceCount]
+ -[CCSetDonation priorRevisionToken]
+ -[CCSetDonation priors]
+ -[CCSetDonation updateRevisionToken:error:]
+ -[CCSetsAccessDaemonDelegate localDeviceUUID]
+ -[CCXPCClient servicePriorsRespondingRequest:completion:usingBlock:]
+ GCC_except_table149
+ GCC_except_table20
+ GCC_except_table40
+ GCC_except_table51
+ GCC_except_table56
+ GCC_except_table62
+ _CCDatabaseColumnDeltaGeneration
+ _CCNotificationDonateNow
+ _CCPersistedKeyValueKeyLastLocalDonationDate
+ _CCPersistedKeyValueKeyLastLocalFullSetDonationDate
+ _CCPersistedKeyValueKeyLocalSourceRevisionToken
+ _OBJC_CLASS_$_CCDonateServicePriors
+ _OBJC_IVAR_$_CCDatabaseUpdater._isLocalDonation
+ _OBJC_IVAR_$_CCDatabaseUpdater._priorLocalDonationDate
+ _OBJC_IVAR_$_CCDatabaseUpdater._priorLocalFullSetDonationDate
+ _OBJC_IVAR_$_CCDatabaseUpdater._priorLocalSourceRevisionToken
+ _OBJC_IVAR_$_CCDeviceRecord._deltaGeneration
+ _OBJC_IVAR_$_CCDeviceSite._deltaGeneration
+ _OBJC_IVAR_$_CCDonateServicePriors._donationDate
+ _OBJC_IVAR_$_CCDonateServicePriors._fullSetDonationDate
+ _OBJC_IVAR_$_CCDonateServicePriors._instanceCount
+ _OBJC_IVAR_$_CCDonateServicePriors._options
+ _OBJC_IVAR_$_CCDonateServicePriors._revisionToken
+ _OBJC_IVAR_$_CCDonateServicePriors._version
+ _OBJC_IVAR_$_CCSetDonation._finishOptions
+ _OBJC_IVAR_$_CCSetDonation._priors
+ _OBJC_IVAR_$_CCSetDonation._revisionToken
+ _OBJC_METACLASS_$_CCDonateServicePriors
+ __OBJC_$_CLASS_METHODS_CCDonateServicePriors
+ __OBJC_$_CLASS_PROP_LIST_CCDonateServicePriors
+ __OBJC_$_INSTANCE_METHODS_CCDonateServicePriors
+ __OBJC_$_INSTANCE_VARIABLES_CCDonateServicePriors
+ __OBJC_$_PROP_LIST_CCDonateServicePriors
+ __OBJC_$_PROP_LIST_CCFullSetDonation
+ __OBJC_CLASS_PROTOCOLS_$_CCDonateServicePriors
+ __OBJC_CLASS_RO_$_CCDonateServicePriors
+ __OBJC_METACLASS_RO_$_CCDonateServicePriors
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorItEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne200100Ev
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB8ne200100Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZnwmSt19__type_descriptor_t
+ ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke
+ ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.21
+ ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.26
+ ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2
+ ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2.22
+ ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2.22.cold.1
+ ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2.28
+ ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2.28.cold.1
+ ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_3
+ ___125+[CCSetDonation _setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_4
+ ___42-[CCSetDonation _finishWithOptions:error:]_block_invoke
+ ___51-[CCSetDonation _removeSourceItemIdentifier:error:]_block_invoke
+ ___52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.53
+ ___52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.53.cold.1
+ ___52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.53.cold.2
+ ___60-[CCDataResourceWriter _didCompleteMaintenance:shouldDefer:]_block_invoke.27.cold.1
+ ___68-[CCXPCClient servicePriorsRespondingRequest:completion:usingBlock:]_block_invoke
+ ___69-[CCSetDonation _mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke
+ ___71-[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:]_block_invoke.57
+ ___71-[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:]_block_invoke.57.cold.1
+ ___72-[CCDonateXPCClient endSetDonationWithOptions:revisionToken:completion:]_block_invoke
+ ___84+[CCSetDonation fullSetDonationWithItemType:descriptors:serviceProvider:completion:]_block_invoke
+ ___87-[CCDataResourceReadAccess _enumerateReadableSets:resourceOptions:itemType:usingBlock:]_block_invoke.17
+ ___87-[CCDataResourceReadAccess _enumerateReadableSets:resourceOptions:itemType:usingBlock:]_block_invoke.20
+ ___91+[CCSetDonation incrementalSetDonationWithItemType:descriptors:serviceProvider:completion:]_block_invoke
+ ___block_descriptor_48_e8_32s_e45_v24?0"NSObject<CCDonateService>"8?<v?S>16ls32l8
+ ___block_descriptor_66_e8_32s40s_e70_v24?0"NSObject<CCDonateService>"8?<v?Sq"CCDonateServicePriors">16ls32l8s40l8
+ ___block_descriptor_74_e8_32s40s48s56bs64r_e37_v28?0S8q12"CCDonateServicePriors"20ls32l8r64l8s40l8s48l8s56l8
+ ___block_descriptor_84_e8_32s40s48s56bs64r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.185
+ _objc_msgSend$_addFinishOptions:
+ _objc_msgSend$_addItem:error:
+ _objc_msgSend$_finishWithOptions:error:
+ _objc_msgSend$_incrementLocalDeltaGeneration
+ _objc_msgSend$_loadResourceGenerationCounter:baseSystemPath:error:
+ _objc_msgSend$_mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:
+ _objc_msgSend$_persistDateWithDeltaProduced:isFullSet:
+ _objc_msgSend$_persistRevisionTokenIfNotNil:
+ _objc_msgSend$_removeSourceItemIdentifier:error:
+ _objc_msgSend$_selectLocalSourcePersistedValuesOutVersion:outValidityHash:outRevisionToken:outDonationDate:outFullSetDonationDate:
+ _objc_msgSend$_selectPersistedValueForKey:outValue:valueClass:
+ _objc_msgSend$_setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:
+ _objc_msgSend$_updateDeviceRowId:deltaGeneration:expirationDate:
+ _objc_msgSend$_upsertInteger:forKey:
+ _objc_msgSend$_upsertInteger:forKey:skipIfNil:
+ _objc_msgSend$_writeRecordWithKey:stringValue:integerValue:dataValue:onConflictType:
+ _objc_msgSend$_writeRecordWithKey:stringValue:integerValue:dataValue:onConflictType:database:error:
+ _objc_msgSend$connectionToAccessServerInDomain:user:useCase:options:
+ _objc_msgSend$debugDescription
+ _objc_msgSend$deltaGeneration
+ _objc_msgSend$donationDate
+ _objc_msgSend$donationWithName:itemType:service:errorCode:priors:
+ _objc_msgSend$endSetDonationWithOptions:revisionToken:completion:
+ _objc_msgSend$fullSetDonationDate
+ _objc_msgSend$fullSetDonationWithItemType:descriptors:completion:
+ _objc_msgSend$incrementalSetDonationWithItemType:descriptors:completion:
+ _objc_msgSend$incrementalSetDonationWithItemType:descriptors:serviceProvider:completion:
+ _objc_msgSend$incrementalSetDonationWithItemType:descriptors:version:validity:serviceProvider:completion:
+ _objc_msgSend$initWithDevice:resourceGeneration:deltaGeneration:expirationDate:
+ _objc_msgSend$initWithFilename:protectionClass:directory:domain:readOnly:error:
+ _objc_msgSend$initWithName:itemType:service:errorCode:priors:flushThreshold:
+ _objc_msgSend$initWithVersion:instanceCount:donationDate:fullSetDonationDate:revisionToken:options:
+ _objc_msgSend$instanceCount
+ _objc_msgSend$isAwaitingFullSet
+ _objc_msgSend$isDeviceUnlocked
+ _objc_msgSend$isEqualToDeviceSite:
+ _objc_msgSend$priors
+ _objc_msgSend$revisionToken
+ _objc_msgSend$servicePriorsRespondingRequest:completion:usingBlock:
+ _objc_msgSend$upsertLastMaintenanceDate:database:error:
+ _objc_msgSend$upsertRowsModified:database:error:
+ _objc_msgSend$version
- +[CCDatabaseUpdater _writeRecordWithKey:stringValue:integerValue:dataValue:onConflictType:database:]
- +[CCDatabaseUpdater insertOrUpdateLastDeltaDate:database:]
- +[CCDatabaseUpdater insertOrUpdateLastMaintenanceDate:database:]
- +[CCDatabaseUpdater insertOrUpdateRowsModified:database:]
- +[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]
- +[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:].cold.1
- +[CCSetDonation donationWithName:itemType:service:errorCode:priorVersion:]
- +[CCSetDonation fullSetDonationWithItemType:forAccount:descriptors:completion:]
- +[CCSetDonation fullSetDonationWithItemType:forAccount:descriptors:serviceProvider:completion:]
- +[CCSetDonation incrementalSetDonationWithItemType:forAccount:descriptors:version:validity:completion:]
- +[CCSetDonation incrementalSetDonationWithItemType:forAccount:descriptors:version:validity:serviceProvider:completion:]
- -[CCDataResourceWriter _didCompleteMaintenance:shouldDefer:].cold.5
- -[CCDatabaseUpdater _persistIntegerWithKey:cachedValue:]
- -[CCDatabaseUpdater _updateDeviceRowId:expirationDate:]
- -[CCDatabaseUpdater _updateDeviceRowId:expirationDate:].cold.1
- -[CCDatabaseUpdater _updateDeviceRowId:expirationDate:].cold.2
- -[CCDatabaseUpdater _updateDeviceRowId:expirationDate:].cold.3
- -[CCDatabaseUpdater _updateLastDelta]
- -[CCDatabaseUpdater _updateLastDelta].cold.1
- -[CCDatabaseUpdater _updateLocalSourceVersion:localSourceValidityHash:].cold.1
- -[CCDatabaseUpdater _updateLocalSourceVersion:localSourceValidityHash:].cold.2
- -[CCDatabaseUpdater finish:]
- -[CCDatabaseUpdater initWithDatabase:request:].cold.2
- -[CCDatabaseUpdater initWithDatabase:request:].cold.3
- -[CCDatabaseUpdater registerRemoteDeviceSite:isAttestation:returningRowId:]
- -[CCDatabaseUpdater registerRemoteDeviceSite:isAttestation:returningRowId:].cold.1
- -[CCDatabaseUpdater registerRemoteDeviceSite:isAttestation:returningRowId:].cold.2
- -[CCDeviceSite initWithDevice:resourceGeneration:expirationDate:]
- -[CCDeviceSite isEqualToSetContributor:]
- -[CCDonateXPCClient endSetDonationWithOptions:completion:]
- -[CCSetDonation addItem:error:]
- -[CCSetDonation finishWithOptions:error:]
- -[CCSetDonation initWithName:itemType:service:errorCode:priorVersion:flushThreshold:]
- -[CCSetDonation mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]
- -[CCSetDonation removeSourceItemIdentifier:error:]
- -[CCXPCClient serviceVersionRespondingRequest:completion:usingBlock:]
- GCC_except_table145
- GCC_except_table35
- GCC_except_table36
- GCC_except_table42
- GCC_except_table60
- _OBJC_IVAR_$_CCSetDonation._priorVersion
- __ZNKSt3__16vectorItNS_9allocatorItEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorItEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke
- ___136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.21
- ___136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke.26
- ___136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2
- ___136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2.22
- ___136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2.22.cold.1
- ___136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2.28
- ___136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_2.28.cold.1
- ___136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_3
- ___136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_4
- ___136+[CCSetDonation _setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:]_block_invoke_5
- ___41-[CCSetDonation finishWithOptions:error:]_block_invoke
- ___50-[CCSetDonation removeSourceItemIdentifier:error:]_block_invoke
- ___52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.38
- ___52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.38.cold.1
- ___52-[CCDatabaseUpdater compactContiguousRunsOfDeletes:]_block_invoke.38.cold.2
- ___58-[CCDonateXPCClient endSetDonationWithOptions:completion:]_block_invoke
- ___68-[CCSetDonation mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:]_block_invoke
- ___69-[CCXPCClient serviceVersionRespondingRequest:completion:usingBlock:]_block_invoke
- ___71-[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:]_block_invoke.45
- ___71-[CCDatabaseUpdater deleteExpiredRemoteDeviceState:shouldTombstoneSet:]_block_invoke.45.cold.1
- ___87-[CCDataResourceReadAccess _enumerateReadableSets:resourceOptions:itemType:usingBlock:]_block_invoke.18
- ___87-[CCDataResourceReadAccess _enumerateReadableSets:resourceOptions:itemType:usingBlock:]_block_invoke.21
- ___95+[CCSetDonation fullSetDonationWithItemType:forAccount:descriptors:serviceProvider:completion:]_block_invoke
- ___block_descriptor_40_e45_v24?0"NSObject<CCDonateService>"8?<v?S>16l
- ___block_descriptor_66_e8_32s40s_e47_v24?0"NSObject<CCDonateService>"8?<v?SqQ>16ls32l8s40l8
- ___block_descriptor_74_e8_32s40s48s56bs64r_e14_v28?0S8q12Q20ls32l8r64l8s40l8s48l8s56l8
- ___block_descriptor_84_e8_32s40s48bs56r_e5_v8?0lr56l8s32l8s40l8s48l8
- ___block_literal_global.161
- _objc_msgSend$_persistIntegerWithKey:cachedValue:
- _objc_msgSend$_setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:
- _objc_msgSend$_updateDeviceRowId:expirationDate:
- _objc_msgSend$_updateLastDelta
- _objc_msgSend$_writeRecordWithKey:stringValue:integerValue:dataValue:onConflictType:database:
- _objc_msgSend$addItem:error:
- _objc_msgSend$connectionToAccessServerInDomain:user:useCase:
- _objc_msgSend$copyWithExpirationDate:
- _objc_msgSend$donationWithName:itemType:service:errorCode:priorVersion:
- _objc_msgSend$endSetDonationWithOptions:completion:
- _objc_msgSend$finishWithOptions:error:
- _objc_msgSend$fullSetDonationWithItemType:forAccount:descriptors:serviceProvider:completion:
- _objc_msgSend$incrementalSetDonationWithItemType:forAccount:descriptors:version:validity:serviceProvider:completion:
- _objc_msgSend$initWithDevice:resourceGeneration:expirationDate:
- _objc_msgSend$initWithFilename:protectionClass:directory:domain:error:
- _objc_msgSend$initWithName:itemType:service:errorCode:priorVersion:flushThreshold:
- _objc_msgSend$insertOrUpdateLastDeltaDate:database:
- _objc_msgSend$insertOrUpdateLastMaintenanceDate:database:
- _objc_msgSend$insertOrUpdateRowsModified:database:
- _objc_msgSend$isEqualToSetContributor:
- _objc_msgSend$isUnlocked
- _objc_msgSend$mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:
- _objc_msgSend$removeSourceItemIdentifier:error:
- _objc_msgSend$selectLocalSourceValidityHashInDatabase:error:
- _objc_msgSend$serviceVersionRespondingRequest:completion:usingBlock:
CStrings:
+ " device: %@ resourceGeneration: %@ deltaGeneration: %@%@"
+ " deviceRowId: %@, deviceId: %@ idsDeviceId: %@ platform: %@ recordOptions %X, resourceGeneration: %@, attestationGeneration: %@, deltaGeneration: %@, expiration: %@"
+ "#"
+ "(%@) Aborting maintenance after failing to record date"
+ "@\"CCDonateServicePriors\""
+ "@36@0:8B16@20^@28"
+ "@52@0:8@16S24@28q36@44"
+ "@60@0:8@16S24@28q36@44Q52"
+ "@64@0:8Q16Q24@32@40@48Q56"
+ "AwaitingFullSet"
+ "B24@0:8B16B20"
+ "B36@0:8@16@24B32"
+ "B36@0:8^B16@24B32"
+ "B40@0:8@16B24B28^@32"
+ "B40@0:8@16^@24#32"
+ "B40@0:8Q16@24^@32"
+ "B56@0:8@16@24@32@40q48"
+ "B56@0:8^@16^@24^@32^@40^@48"
+ "B72@0:8@16@24@32@40q48@56^@64"
+ "CCDonateServicePriors"
+ "CREATE TABLE IF NOT EXISTS \"%@\" (\"%@\" integer PRIMARY KEY, \"%@\" blob NOT NULL, \"%@\" varchar NULLABLE, \"%@\" integer NOT NULL, \"%@\" integer NOT NULL, \"%@\" integer NOT NULL, \"%@\" integer NOT NULL, \"%@\" integer NOT NULL, \"%@\" integer NULLABLE);"
+ "Cannot re-register local device record: %@ with site %@. %@"
+ "DesignateAsFullSet"
+ "Device site %@ already expired (compared to: %@). %@"
+ "Device site %@ matches local deviceUUID: %@. %@"
+ "Extending expiration date from %@ to %@ due to re-attestation of device site %@ compared to record: %@. %@"
+ "Failed to select persisted value for key: %@ error: %@ %@"
+ "Failed to select rows modified in database: %@"
+ "Failed to update last maintenance date: %@"
+ "Failed to update rows modified in database: %@"
+ "Failed to write persisted value: %@ for key: %@ error: %@ %@"
+ "FullSet"
+ "Ignoring re-attested expiration date of device site %@ which occurs sooner than the stored device record: %@. %@"
+ "Incrementing local delta generation from %@ to %@, %@"
+ "InlineFallback"
+ "Invalid donation subclass: %@"
+ "Posted notification \"%@\""
+ "Returning %@ for set: %@ - %@"
+ "Skipping new registration of device site %@. %@"
+ "Skipping registration - delta generation of record: %@ is more recent than device site %@. %@"
+ "Skipping registration - resource generation of record: %@ is more recent than device site %@. %@"
+ "Skipping unattested registration of device site %@ for expired record: %@. %@"
+ "Skipping unattested registration of device site %@ which would progress the deltaGeneration for record: %@. %@"
+ "Skipping unattested registration of device site %@. %@"
+ "Supplanting %@ for nil deltaGeneration"
+ "T@\"CCDonateServicePriors\",R,N,V_priors"
+ "T@\"NSDate\",R,D,N"
+ "T@\"NSDate\",R,N,V_donationDate"
+ "T@\"NSDate\",R,N,V_fullSetDonationDate"
+ "T@\"NSDate\",R,N,V_priorLocalDonationDate"
+ "T@\"NSDate\",R,N,V_priorLocalFullSetDonationDate"
+ "T@\"NSNumber\",R,N,V_deltaGeneration"
+ "T@\"NSString\",R,D,N"
+ "T@\"NSString\",R,N,V_priorLocalSourceRevisionToken"
+ "T@\"NSString\",R,N,V_revisionToken"
+ "T@\"NSUUID\",R,N,V_localDeviceUUID"
+ "TQ,R,D,N"
+ "TQ,R,N,V_instanceCount"
+ "TQ,R,N,V_options"
+ "TQ,R,N,V_version"
+ "Tq,R,D,N"
+ "Unexpected remote device site %@ has isLocal flag set. %@"
+ "Unexpected remote device site %@ missing expiration date. %@"
+ "Vv40@0:8Q16@\"NSString\"24@?<v@?S>32"
+ "Vv40@0:8Q16@24@?32"
+ "Vv60@0:8S16@\"NSString\"20Q28@\"NSString\"36Q44@?<v@?Sq@\"CCDonateServicePriors\">52"
+ "[%@ with%@ deltas] %@"
+ "_addFinishOptions:"
+ "_addItem:error:"
+ "_deltaGeneration"
+ "_donationDate"
+ "_finishOptions"
+ "_finishWithOptions:error:"
+ "_fullSetDonationDate"
+ "_incrementLocalDeltaGeneration"
+ "_instanceCount"
+ "_isLocalDonation"
+ "_loadResourceGenerationCounter:baseSystemPath:error:"
+ "_mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:"
+ "_persistDateWithDeltaProduced:isFullSet:"
+ "_persistRevisionTokenIfNotNil:"
+ "_priorLocalDonationDate"
+ "_priorLocalFullSetDonationDate"
+ "_priorLocalSourceRevisionToken"
+ "_priors"
+ "_removeSourceItemIdentifier:error:"
+ "_revisionToken"
+ "_selectLocalSourcePersistedValuesOutVersion:outValidityHash:outRevisionToken:outDonationDate:outFullSetDonationDate:"
+ "_selectPersistedValueForKey:outValue:valueClass:"
+ "_setDonationWithItemType:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:"
+ "_updateDeviceRowId:deltaGeneration:expirationDate:"
+ "_upsertInteger:forKey:"
+ "_upsertInteger:forKey:skipIfNil:"
+ "_version"
+ "_writeRecordWithKey:stringValue:integerValue:dataValue:onConflictType:"
+ "_writeRecordWithKey:stringValue:integerValue:dataValue:onConflictType:database:error:"
+ "activeDeviceSiteWithDeviceUUID:"
+ "connectionToAccessServerInDomain:user:useCase:options:"
+ "deltaGeneration"
+ "delta_generation"
+ "designateAsFullSet"
+ "device site %@ has regressed deltaGeneration compared with record: %@. %@"
+ "device site %@ has regressed resourceGeneration compared with record: %@. %@"
+ "device site %@ not expected to invalidate record: %@. %@"
+ "device site %@ not expected to progress deltaGeneration for record: %@. %@"
+ "donationDate"
+ "donationWithName:itemType:service:errorCode:priors:"
+ "endSetDonationWithOptions:revisionToken:completion:"
+ "f"
+ "finishAndDetectDelta:updateRevisionToken:isFullSet:"
+ "fullSetDonationDate"
+ "fullSetDonationWithItemType:completion:"
+ "incrementalSetDonationWithItemType:completion:"
+ "incrementalSetDonationWithItemType:descriptors:completion:"
+ "incrementalSetDonationWithItemType:descriptors:serviceProvider:completion:"
+ "initWithDevice:resourceGeneration:deltaGeneration:expirationDate:"
+ "initWithFilename:protectionClass:directory:domain:readOnly:error:"
+ "initWithName:itemType:service:errorCode:priors:flushThreshold:"
+ "initWithSet:error:"
+ "initWithVersion:instanceCount:donationDate:fullSetDonationDate:revisionToken:options:"
+ "instanceCount"
+ "isAwaitingFullSet"
+ "isDeviceUnlocked"
+ "isEqualToDeviceSite:"
+ "lastLocalDonationDate"
+ "lastLocalFullSetDonationDate"
+ "localSourceRevisionToken"
+ "out"
+ "peer"
+ "priorDonationDate"
+ "priorFullSetDonationDate"
+ "priorInstanceCount"
+ "priorLocalDonationDate"
+ "priorLocalFullSetDonationDate"
+ "priorLocalSourceRevisionToken"
+ "priorRevisionToken"
+ "priors"
+ "readDefaultLocalDeviceUUID:"
+ "registerRemoteDeviceSite:isPeer:hasDeltas:returningRowId:"
+ "relayed"
+ "revisionToken"
+ "servicePriorsRespondingRequest:completion:usingBlock:"
+ "updateRevisionToken:error:"
+ "upsertLastMaintenanceDate:database:error:"
+ "upsertRowsModified:database:error:"
+ "v"
+ "v24@?0@\"NSObject<CCDonateService>\"8@?<v@?Sq@\"CCDonateServicePriors\">16"
+ "v28@0:8S16@?20"
+ "v28@?0S8q12@\"CCDonateServicePriors\"20"
+ "v84@0:8S16@20Q28@36Q44@52@60Q68@?76"
+ "version"
- " device: %@ resourceGeneration: %@%@"
- " deviceRowId: %@, deviceId: %@ idsDeviceId: %@ platform: %@ recordOptions %X, resourceGeneration: %@, attestationGeneration: %@, expiration: %@"
- "(%@) Database has not been created at path: %@"
- "(%@) Failed to update last maintenance date"
- "@52@0:8@16S24@28q36Q44"
- "@60@0:8@16S24@28q36Q44Q52"
- "Attempting to obtain read access on a tombstoned set: %@"
- "B24@0:8^B16"
- "B36@0:8@16B24^@28"
- "B64@0:8@16@24@32@40q48@56"
- "CREATE TABLE IF NOT EXISTS \"%@\" (\"%@\" integer PRIMARY KEY, \"%@\" blob NOT NULL, \"%@\" varchar NULLABLE, \"%@\" integer NOT NULL, \"%@\" integer NOT NULL, \"%@\" integer NOT NULL, \"%@\" integer NOT NULL, \"%@\" integer NULLABLE);"
- "Cannot re-register local device record: %@ with site: %@. %@"
- "Could not update key: %@ with cached value: %@. %@"
- "Could not update last delta date - update failed. %@"
- "Could not update set validity hash - update failed. %@"
- "Could not update set version - update failed. %@"
- "Extending expiration date from %@ to %@ due to re-attestation of device site %@. %@"
- "Failed to select prior set validity hash with error: %@"
- "Failed to select prior set version with error: %@"
- "Ignoring re-attested expiration date of device site %@ which occurs sooner than the stored device record (%@). %@"
- "Not an attestation - inheriting expiration date from prior device record (%@) for device site: %@. %@"
- "Posted notification \"%s\""
- "Remote device site: %@ already expired (compared to: %@). %@"
- "Skipping registration - stored resource generation %@ in the databse is more recent than device site %@. %@"
- "Skipping unattested registration of new device site %@. %@"
- "TQ,R,N,V_priorVersion"
- "Unexpected remote device site: %@ has isLocal flag set. %@"
- "Unexpected remote device site: %@ missing expiration date for attestation. %@"
- "Vv32@0:8Q16@?24"
- "Vv32@0:8Q16@?<v@?S>24"
- "Vv60@0:8S16@\"NSString\"20Q28@\"NSString\"36Q44@?<v@?SqQ>52"
- "_persistIntegerWithKey:cachedValue:"
- "_priorVersion"
- "_setDonationWithItemType:forAccount:descriptors:version:validity:options:serviceProvider:queue:timeoutNanos:completion:"
- "_updateDeviceRowId:expirationDate:"
- "_updateLastDelta"
- "_writeRecordWithKey:stringValue:integerValue:dataValue:onConflictType:database:"
- "addItem:error:"
- "connectionToAccessServerInDomain:user:useCase:"
- "donationWithName:itemType:service:errorCode:priorVersion:"
- "endSetDonationWithOptions:completion:"
- "finishWithOptions:error:"
- "fullSetDonationWithItemType:forAccount:descriptors:completion:"
- "fullSetDonationWithItemType:forAccount:descriptors:serviceProvider:completion:"
- "incrementalSetDonationWithItemType:forAccount:descriptors:version:validity:completion:"
- "incrementalSetDonationWithItemType:forAccount:descriptors:version:validity:serviceProvider:completion:"
- "initWithDevice:resourceGeneration:expirationDate:"
- "initWithFilename:protectionClass:directory:domain:error:"
- "initWithName:itemType:service:errorCode:priorVersion:flushThreshold:"
- "insertOrUpdateLastDeltaDate:database:"
- "insertOrUpdateLastMaintenanceDate:database:"
- "insertOrUpdateRowsModified:database:"
- "isEqualToSetContributor:"
- "isUnlocked"
- "mergeRemoteDelta:peerDeviceSite:relayedDeviceSites:"
- "registerRemoteDeviceSite:isAttestation:returningRowId:"
- "removeSourceItemIdentifier:error:"
- "serviceVersionRespondingRequest:completion:usingBlock:"
- "v24@?0@\"NSObject<CCDonateService>\"8@?<v@?SqQ>16"
- "v28@?0S8q12Q20"
- "v52@0:8S16@20@28@36@?44"
- "v60@0:8S16@20@28Q36@44@?52"
- "v68@0:8S16@20@28Q36@44@52@?60"
- "v92@0:8S16@20@28Q36@44Q52@60@68Q76@?84"

```
