## Home

> `/System/Library/PrivateFrameworks/Home.framework/Home`

```diff

-825.2.8.1.1
-  __TEXT.__text: 0x2ee5d8
-  __TEXT.__auth_stubs: 0x20f0
-  __TEXT.__objc_methlist: 0x26c7c
-  __TEXT.__const: 0x2238
-  __TEXT.__cstring: 0x347ce
-  __TEXT.__swift5_typeref: 0x117c
-  __TEXT.__swift5_reflstr: 0x53a
+841.3.9.1.1
+  __TEXT.__text: 0x2edad0
+  __TEXT.__auth_stubs: 0x2100
+  __TEXT.__objc_methlist: 0x26d5c
+  __TEXT.__const: 0x2188
+  __TEXT.__cstring: 0x34712
+  __TEXT.__swift5_typeref: 0x1184
+  __TEXT.__swift5_reflstr: 0x52a
   __TEXT.__swift5_assocty: 0x210
-  __TEXT.__constg_swiftt: 0xef0
+  __TEXT.__constg_swiftt: 0xea8
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_fieldmd: 0x644
-  __TEXT.__swift5_proto: 0x150
-  __TEXT.__swift5_types: 0x94
+  __TEXT.__swift5_fieldmd: 0x634
+  __TEXT.__swift5_proto: 0x148
+  __TEXT.__swift5_types: 0x8c
   __TEXT.__swift5_capture: 0x3d4
-  __TEXT.__swift5_protos: 0x28
-  __TEXT.__oslogstring: 0x183db
-  __TEXT.__gcc_except_tab: 0x3ed0
+  __TEXT.__swift5_protos: 0x2c
+  __TEXT.__oslogstring: 0x18401
+  __TEXT.__gcc_except_tab: 0x3ed4
   __TEXT.__ustring: 0x88
   __TEXT.__dlopen_cstrs: 0x4b
-  __TEXT.__unwind_info: 0xce6c
+  __TEXT.__unwind_info: 0xce78
   __TEXT.__eh_frame: 0x1dd8
-  __TEXT.__objc_classname: 0x68ac
-  __TEXT.__objc_methname: 0x552a8
-  __TEXT.__objc_methtype: 0x756e
-  __TEXT.__objc_stubs: 0x376a0
+  __TEXT.__objc_classname: 0x68cb
+  __TEXT.__objc_methname: 0x55474
+  __TEXT.__objc_methtype: 0x7586
+  __TEXT.__objc_stubs: 0x37720
   __DATA_CONST.__got: 0xdf0
-  __DATA_CONST.__const: 0x10450
-  __DATA_CONST.__objc_classlist: 0x16c8
+  __DATA_CONST.__const: 0x10478
+  __DATA_CONST.__objc_classlist: 0x16d0
   __DATA_CONST.__objc_catlist: 0x3f0
   __DATA_CONST.__objc_protolist: 0x818
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x38f58
-  __DATA_CONST.__objc_selrefs: 0x114b8
-  __DATA_CONST.__objc_arraydata: 0x348
-  __AUTH_CONST.__const: 0xcaf0
-  __AUTH_CONST.__objc_const: 0x142a8
+  __DATA_CONST.__objc_const: 0x390e8
+  __DATA_CONST.__objc_selrefs: 0x114f8
+  __DATA_CONST.__objc_arraydata: 0x340
+  __AUTH_CONST.__const: 0xca90
+  __AUTH_CONST.__objc_const: 0x142f0
   __AUTH_CONST.__cfstring: 0x255a0
   __AUTH_CONST.__objc_intobj: 0x2070
   __AUTH_CONST.__objc_doubleobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_floatobj: 0x50
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1088
-  __AUTH.__objc_data: 0xa298
+  __AUTH_CONST.__auth_got: 0x1090
+  __AUTH.__objc_data: 0xa320
   __AUTH.__data: 0x4f8
   __DATA.__objc_protorefs: 0x320
-  __DATA.__objc_classrefs: 0x1b58
-  __DATA.__objc_superrefs: 0x12b0
-  __DATA.__objc_ivar: 0x1480
+  __DATA.__objc_classrefs: 0x1b68
+  __DATA.__objc_superrefs: 0x12b8
+  __DATA.__objc_ivar: 0x1490
   __DATA.__objc_data: 0x20
-  __DATA.__data: 0x74c8
+  __DATA.__data: 0x7510
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x20d8
+  __DATA.__bss: 0x1f50
   __DATA.__common: 0x68
-  __DATA_DIRTY.__objc_ivar: 0xc38
-  __DATA_DIRTY.__objc_data: 0x4ee8
-  __DATA_DIRTY.__data: 0x240
+  __DATA_DIRTY.__objc_ivar: 0xc3c
+  __DATA_DIRTY.__objc_data: 0x4e60
+  __DATA_DIRTY.__data: 0x220
   __DATA_DIRTY.__common: 0x10
   __DATA_DIRTY.__bss: 0x1898
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HomeKit.framework/HomeKit
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
+  - /System/Library/Frameworks/Matter.framework/Matter
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4B3DF18B-1D27-3662-87FC-40F808B6C8A5
-  Functions: 18177
-  Symbols:   54606
-  CStrings:  27291
+  UUID: F0A72700-9D93-3CE4-BDFE-9CEBD0A76297
+  Functions: 18180
+  Symbols:   54670
+  CStrings:  27306
 
Symbols:
+ -[HFHomePropertyCacheManager _clearRoomOrderValues]
+ -[HFHomePropertyCacheManager _testing_disableCaching]
+ -[HFHomePropertyCacheManager home:didAddRoom:]
+ -[HFHomePropertyCacheManager home:didRemoveRoom:]
+ -[HFHomePropertyCacheManager homeDidUpdateApplicationData:]
+ -[HFHomePropertyCacheManager keysForRoomOrder]
+ -[HFHomePropertyCacheManager roomOrderKeysLock]
+ -[HFHomePropertyCacheManager setKeysForRoomOrder:]
+ -[HFHomePropertyCacheManager setRoomOrderKeysLock:]
+ -[HFHomePropertyCacheManager set_testing_disableCaching:]
+ -[HFHomePropertyCacheManager valueForObject:home:key:invalidationReasons:recalculationBlock:]
+ -[HFUserItemProvider filter]
+ -[HFUserItemProvider setFilter:]
+ -[HMHome(Additions) hf_allHomePodsSupportRemoteProfileInstallation]
+ -[_HFHomePropertyCacheManagerKey .cxx_destruct]
+ -[_HFHomePropertyCacheManagerKey copyWithZone:]
+ -[_HFHomePropertyCacheManagerKey hash]
+ -[_HFHomePropertyCacheManagerKey initWithObjectID:key:]
+ -[_HFHomePropertyCacheManagerKey isEqual:]
+ -[_HFHomePropertyCacheManagerKey key]
+ -[_HFHomePropertyCacheManagerKey objectID]
+ GCC_except_table286
+ GCC_except_table358
+ GCC_except_table374
+ GCC_except_table381
+ GCC_except_table382
+ GCC_except_table390
+ GCC_except_table392
+ GCC_except_table403
+ GCC_except_table404
+ GCC_except_table409
+ GCC_except_table414
+ GCC_except_table421
+ GCC_except_table422
+ GCC_except_table45
+ _OBJC_CLASS_$_NSRecursiveLock
+ _OBJC_CLASS_$__HFHomePropertyCacheManagerKey
+ _OBJC_IVAR_$_HFHomePropertyCacheManager.__testing_disableCaching
+ _OBJC_IVAR_$_HFHomePropertyCacheManager._keysForRoomOrder
+ _OBJC_IVAR_$_HFHomePropertyCacheManager._roomOrderKeysLock
+ _OBJC_IVAR_$__HFHomePropertyCacheManagerKey._key
+ _OBJC_IVAR_$__HFHomePropertyCacheManagerKey._objectID
+ _OBJC_METACLASS_$__HFHomePropertyCacheManagerKey
+ __OBJC_$_INSTANCE_METHODS__HFHomePropertyCacheManagerKey
+ __OBJC_$_INSTANCE_VARIABLES__HFHomePropertyCacheManagerKey
+ __OBJC_$_PROP_LIST__HFHomePropertyCacheManagerKey
+ __OBJC_CLASS_PROTOCOLS_$__HFHomePropertyCacheManagerKey
+ __OBJC_CLASS_RO_$__HFHomePropertyCacheManagerKey
+ __OBJC_METACLASS_RO_$__HFHomePropertyCacheManagerKey
+ ___101-[HMHome(Additions) hf_setPhotosLibrarySettingsForUser:importPhotosLibraryEnabled:shareFacesEnabled:]_block_invoke.233
+ ___127-[HFItemManager _reloadItemProviders:updateItems:shouldUpdateExistingItems:senderSelector:readPolicy:fastInitialUpdatePromise:]_block_invoke.247
+ ___127-[HFItemManager _reloadItemProviders:updateItems:shouldUpdateExistingItems:senderSelector:readPolicy:fastInitialUpdatePromise:]_block_invoke_2.248
+ ___127-[HFItemManager _reloadItemProviders:updateItems:shouldUpdateExistingItems:senderSelector:readPolicy:fastInitialUpdatePromise:]_block_invoke_3.251
+ ___36-[HMHome(Additions) hf_orderedRooms]_block_invoke
+ ___47-[HFCharacteristicValueManager executeActions:]_block_invoke.141
+ ___47-[HFCharacteristicValueManager executeActions:]_block_invoke.143
+ ___47-[HFCharacteristicValueManager executeActions:]_block_invoke_2.142
+ ___47-[HFCharacteristicValueManager executeActions:]_block_invoke_2.144
+ ___47-[HMHome(Additions) hf_walletKeyInWalletAppURL]_block_invoke.402
+ ___48-[HMHome(Additions) hf_addWalletKeyWithOptions:]_block_invoke.410
+ ___48-[HMHome(Additions) hf_updateNetworkProtection:]_block_invoke.68
+ ___49-[HFCharacteristicValueManager executeActionSet:]_block_invoke.129
+ ___49-[HFCharacteristicValueManager executeActionSet:]_block_invoke.130
+ ___50-[HMHome(Additions) hf_setFaceRecognitionEnabled:]_block_invoke.200
+ ___50-[HMHome(Additions) hf_setFaceRecognitionEnabled:]_block_invoke_2.198
+ ___51-[HFHomePropertyCacheManager _clearRoomOrderValues]_block_invoke
+ ___54-[HMHome(Additions) hf_updateAccessControlDescriptor:]_block_invoke.376
+ ___54-[HMHome(Additions) hf_updateAccessControlDescriptor:]_block_invoke.378
+ ___54-[HMHome(Additions) hf_updateAccessControlDescriptor:]_block_invoke_2.382
+ ___57-[HFAccessorySettingManagedConfigurationAdapter profiles]_block_invoke.29
+ ___59-[HFCharacteristicValueManager readValueForCharacteristic:]_block_invoke.103
+ ___59-[HFCharacteristicValueManager readValueForCharacteristic:]_block_invoke.108
+ ___59-[HFCharacteristicValueManager readValueForCharacteristic:]_block_invoke.109
+ ___60-[HFCharacteristicValueManager commitTransactionWithReason:]_block_invoke.157
+ ___60-[HFCharacteristicValueManager commitTransactionWithReason:]_block_invoke.158
+ ___60-[HFCharacteristicValueManager commitTransactionWithReason:]_block_invoke.159
+ ___60-[HFCharacteristicValueManager commitTransactionWithReason:]_block_invoke.160
+ ___61-[HFCharacteristicValueManager writeValue:forCharacteristic:]_block_invoke.118
+ ___61-[HFCharacteristicValueManager writeValue:forCharacteristic:]_block_invoke.121
+ ___65-[HMHome(Additions) hf_fetchWalletKeyDeviceStateForCurrentDevice]_block_invoke.389
+ ___67-[HMHome(Additions) hf_allHomePodsSupportRemoteProfileInstallation]_block_invoke
+ ___70-[HFItemManager _performUpdateForItem:withContext:isInternal:isChild:]_block_invoke.349
+ ___70-[HMHome(Additions) hf_walletKeyDeviceStatesOfCompatiblePairedWatches]_block_invoke.448
+ ___75-[HFItemManager _updateResultsForItems:removedItems:context:allowDelaying:]_block_invoke.301
+ ___75-[HFItemManager _updateResultsForItems:removedItems:context:allowDelaying:]_block_invoke.313
+ ___75-[HFItemManager _updateResultsForItems:removedItems:context:allowDelaying:]_block_invoke.325
+ ___75-[HFItemManager _updateResultsForItems:removedItems:context:allowDelaying:]_block_invoke_2.316
+ ___90-[HFAccessorySettingManagedConfigurationAdapter _synchronizeHomeKitToManagedConfiguration]_block_invoke.59
+ ___90-[HFAccessorySettingManagedConfigurationAdapter _synchronizeManagedConfigurationToHomeKit]_block_invoke.45
+ ___90-[HFAccessorySettingManagedConfigurationAdapter _synchronizeManagedConfigurationToHomeKit]_block_invoke.49
+ ___90-[HFCharacteristicValueManager _transactionLock_executeReadTransaction:completionHandler:]_block_invoke.200
+ ___90-[HFCharacteristicValueManager _transactionLock_executeReadTransaction:completionHandler:]_block_invoke.211
+ ___90-[HFCharacteristicValueManager _transactionLock_executeReadTransaction:completionHandler:]_block_invoke.218
+ ___90-[HFCharacteristicValueManager _transactionLock_executeReadTransaction:completionHandler:]_block_invoke.220
+ ___90-[HFCharacteristicValueManager _transactionLock_executeReadTransaction:completionHandler:]_block_invoke_2.203
+ ___90-[HFCharacteristicValueManager _transactionLock_executeReadTransaction:completionHandler:]_block_invoke_2.214
+ ___90-[HFCharacteristicValueManager _transactionLock_executeReadTransaction:completionHandler:]_block_invoke_2.219
+ ___90-[HFCharacteristicValueManager _transactionLock_executeReadTransaction:completionHandler:]_block_invoke_2.221
+ ___90-[HFCharacteristicValueManager _transactionLock_executeReadTransaction:completionHandler:]_block_invoke_3.215
+ ___91-[HFCharacteristicValueManager _transactionLock_executeWriteTransaction:completionHandler:]_block_invoke.179
+ ___91-[HFCharacteristicValueManager _transactionLock_executeWriteTransaction:completionHandler:]_block_invoke.180
+ ___91-[HFCharacteristicValueManager _transactionLock_executeWriteTransaction:completionHandler:]_block_invoke_2.185
+ ___93-[HFCharacteristicValueManager _transactionLock_executeActionsTransaction:completionHandler:]_block_invoke.229
+ ___93-[HFHomePropertyCacheManager valueForObject:home:key:invalidationReasons:recalculationBlock:]_block_invoke
+ ___95-[HFCharacteristicValueManager _transactionLock_executeActionSetTransaction:completionHandler:]_block_invoke.224
+ ___95-[HFCharacteristicValueManager _transactionLock_executeActionSetTransaction:completionHandler:]_block_invoke_2.225
+ ___95-[HFCharacteristicValueManager _transactionLock_executeActionSetTransaction:completionHandler:]_block_invoke_3.228
+ ___block_descriptor_40_e8_32w_e5_8?0lw32l8
+ ___block_literal_global.147
+ ___block_literal_global.153
+ ___block_literal_global.167
+ ___block_literal_global.169
+ ___block_literal_global.178
+ ___block_literal_global.180
+ ___block_literal_global.208
+ ___block_literal_global.220
+ ___block_literal_global.225
+ ___block_literal_global.230
+ ___block_literal_global.248
+ ___block_literal_global.252
+ ___block_literal_global.258
+ ___block_literal_global.260
+ ___block_literal_global.277
+ ___block_literal_global.329
+ ___block_literal_global.333
+ ___block_literal_global.335
+ ___block_literal_global.341
+ ___block_literal_global.343
+ ___block_literal_global.354
+ ___block_literal_global.362
+ ___block_literal_global.365
+ ___block_literal_global.381
+ ___block_literal_global.386
+ ___block_literal_global.396
+ ___block_literal_global.405
+ ___block_literal_global.409
+ ___block_literal_global.427
+ ___block_literal_global.432
+ ___block_literal_global.441
+ ___block_literal_global.443
+ ___block_literal_global.450
+ ___block_literal_global.458
+ ___block_literal_global.460
+ ___block_literal_global.469
+ ___block_literal_global.470
+ ___block_literal_global.475
+ ___block_literal_global.481
+ ___block_literal_global.483
+ ___block_literal_global.494
+ ___block_literal_global.520
+ ___block_literal_global.522
+ ___block_literal_global.93
+ ___swift_mutable_project_boxed_opaque_existential_1
+ _objc_msgSend$_clearRoomOrderValues
+ _objc_msgSend$_testing_disableCaching
+ _objc_msgSend$initWithObjectID:key:
+ _objc_msgSend$keysForRoomOrder
+ _objc_msgSend$objectID
+ _objc_msgSend$roomOrderKeysLock
+ _objc_msgSend$setTransactionLock:
+ _objc_msgSend$valueForObject:home:key:invalidationReasons:recalculationBlock:
+ _swift_makeBoxUnique
+ _symbolic $s4Home9GeocodingP
+ _symbolic ______p 4Home9GeocodingP
- -[HFCharacteristicValueManager _errorLock_lock]
- -[HFCharacteristicValueManager _errorLock_unlock]
- GCC_except_table285
- GCC_except_table355
- GCC_except_table365
- GCC_except_table369
- GCC_except_table376
- GCC_except_table386
- GCC_except_table387
- GCC_except_table400
- GCC_except_table401
- GCC_except_table405
- GCC_except_table406
- GCC_except_table415
- GCC_except_table416
- _OBJC_IVAR_$_HFCharacteristicValueManager._errorLock
- ___101-[HMHome(Additions) hf_setPhotosLibrarySettingsForUser:importPhotosLibraryEnabled:shareFacesEnabled:]_block_invoke.228
- ___127-[HFItemManager _reloadItemProviders:updateItems:shouldUpdateExistingItems:senderSelector:readPolicy:fastInitialUpdatePromise:]_block_invoke.250
- ___127-[HFItemManager _reloadItemProviders:updateItems:shouldUpdateExistingItems:senderSelector:readPolicy:fastInitialUpdatePromise:]_block_invoke_2.251
- ___127-[HFItemManager _reloadItemProviders:updateItems:shouldUpdateExistingItems:senderSelector:readPolicy:fastInitialUpdatePromise:]_block_invoke_3.254
- ___47-[HFCharacteristicValueManager executeActions:]_block_invoke.137
- ___47-[HFCharacteristicValueManager executeActions:]_block_invoke.139
- ___47-[HFCharacteristicValueManager executeActions:]_block_invoke_2.138
- ___47-[HFCharacteristicValueManager executeActions:]_block_invoke_2.140
- ___47-[HMHome(Additions) hf_walletKeyInWalletAppURL]_block_invoke.395
- ___48-[HMHome(Additions) hf_addWalletKeyWithOptions:]_block_invoke.403
- ___48-[HMHome(Additions) hf_updateNetworkProtection:]_block_invoke.63
- ___49-[HFCharacteristicValueManager executeActionSet:]_block_invoke.125
- ___49-[HFCharacteristicValueManager executeActionSet:]_block_invoke.126
- ___50-[HMHome(Additions) hf_setFaceRecognitionEnabled:]_block_invoke.190
- ___50-[HMHome(Additions) hf_setFaceRecognitionEnabled:]_block_invoke_2.193
- ___54-[HMHome(Additions) hf_updateAccessControlDescriptor:]_block_invoke.369
- ___54-[HMHome(Additions) hf_updateAccessControlDescriptor:]_block_invoke.371
- ___54-[HMHome(Additions) hf_updateAccessControlDescriptor:]_block_invoke_2.375
- ___57-[HFAccessorySettingManagedConfigurationAdapter profiles]_block_invoke.31
- ___59-[HFCharacteristicValueManager readValueForCharacteristic:]_block_invoke.104
- ___59-[HFCharacteristicValueManager readValueForCharacteristic:]_block_invoke.105
- ___59-[HFCharacteristicValueManager readValueForCharacteristic:]_block_invoke.99
- ___60-[HFCharacteristicValueManager commitTransactionWithReason:]_block_invoke.153
- ___60-[HFCharacteristicValueManager commitTransactionWithReason:]_block_invoke.154
- ___60-[HFCharacteristicValueManager commitTransactionWithReason:]_block_invoke.155
- ___60-[HFCharacteristicValueManager commitTransactionWithReason:]_block_invoke.156
- ___61-[HFCharacteristicValueManager writeValue:forCharacteristic:]_block_invoke.114
- ___61-[HFCharacteristicValueManager writeValue:forCharacteristic:]_block_invoke.117
- ___65-[HMHome(Additions) hf_fetchWalletKeyDeviceStateForCurrentDevice]_block_invoke.382
- ___70-[HFItemManager _performUpdateForItem:withContext:isInternal:isChild:]_block_invoke.352
- ___70-[HMHome(Additions) hf_walletKeyDeviceStatesOfCompatiblePairedWatches]_block_invoke.441
- ___75-[HFItemManager _updateResultsForItems:removedItems:context:allowDelaying:]_block_invoke.304
- ___75-[HFItemManager _updateResultsForItems:removedItems:context:allowDelaying:]_block_invoke.316
- ___75-[HFItemManager _updateResultsForItems:removedItems:context:allowDelaying:]_block_invoke.328
- ___75-[HFItemManager _updateResultsForItems:removedItems:context:allowDelaying:]_block_invoke_2.319
- ___80-[HFAccessorySettingManagedConfigurationAdapter homeKitSettingWasUpdated:value:]_block_invoke
- ___90-[HFAccessorySettingManagedConfigurationAdapter _synchronizeHomeKitToManagedConfiguration]_block_invoke.63
- ___90-[HFAccessorySettingManagedConfigurationAdapter _synchronizeManagedConfigurationToHomeKit]_block_invoke.47
- ___90-[HFAccessorySettingManagedConfigurationAdapter _synchronizeManagedConfigurationToHomeKit]_block_invoke.51
- ___90-[HFCharacteristicValueManager _transactionLock_executeReadTransaction:completionHandler:]_block_invoke.196
- ___90-[HFCharacteristicValueManager _transactionLock_executeReadTransaction:completionHandler:]_block_invoke.207
- ___90-[HFCharacteristicValueManager _transactionLock_executeReadTransaction:completionHandler:]_block_invoke.214
- ___90-[HFCharacteristicValueManager _transactionLock_executeReadTransaction:completionHandler:]_block_invoke.216
- ___90-[HFCharacteristicValueManager _transactionLock_executeReadTransaction:completionHandler:]_block_invoke_2.199
- ___90-[HFCharacteristicValueManager _transactionLock_executeReadTransaction:completionHandler:]_block_invoke_2.210
- ___90-[HFCharacteristicValueManager _transactionLock_executeReadTransaction:completionHandler:]_block_invoke_2.215
- ___90-[HFCharacteristicValueManager _transactionLock_executeReadTransaction:completionHandler:]_block_invoke_2.217
- ___90-[HFCharacteristicValueManager _transactionLock_executeReadTransaction:completionHandler:]_block_invoke_3.211
- ___91-[HFCharacteristicValueManager _transactionLock_executeWriteTransaction:completionHandler:]_block_invoke.171
- ___91-[HFCharacteristicValueManager _transactionLock_executeWriteTransaction:completionHandler:]_block_invoke.176
- ___91-[HFCharacteristicValueManager _transactionLock_executeWriteTransaction:completionHandler:]_block_invoke_2.181
- ___93-[HFCharacteristicValueManager _transactionLock_executeActionsTransaction:completionHandler:]_block_invoke.225
- ___95-[HFCharacteristicValueManager _transactionLock_executeActionSetTransaction:completionHandler:]_block_invoke.220
- ___95-[HFCharacteristicValueManager _transactionLock_executeActionSetTransaction:completionHandler:]_block_invoke_2.221
- ___95-[HFCharacteristicValueManager _transactionLock_executeActionSetTransaction:completionHandler:]_block_invoke_3.224
- ___block_literal_global.115
- ___block_literal_global.138
- ___block_literal_global.151
- ___block_literal_global.164
- ___block_literal_global.175
- ___block_literal_global.195
- ___block_literal_global.202
- ___block_literal_global.203
- ___block_literal_global.209
- ___block_literal_global.228
- ___block_literal_global.234
- ___block_literal_global.237
- ___block_literal_global.238
- ___block_literal_global.257
- ___block_literal_global.289
- ___block_literal_global.306
- ___block_literal_global.308
- ___block_literal_global.317
- ___block_literal_global.324
- ___block_literal_global.326
- ___block_literal_global.330
- ___block_literal_global.332
- ___block_literal_global.336
- ___block_literal_global.340
- ___block_literal_global.355
- ___block_literal_global.357
- ___block_literal_global.368
- ___block_literal_global.379
- ___block_literal_global.384
- ___block_literal_global.389
- ___block_literal_global.408
- ___block_literal_global.412
- ___block_literal_global.414
- ___block_literal_global.425
- ___block_literal_global.429
- ___block_literal_global.430
- ___block_literal_global.431
- ___block_literal_global.434
- ___block_literal_global.448
- ___block_literal_global.451
- ___block_literal_global.461
- ___block_literal_global.463
- ___block_literal_global.465
- ___block_literal_global.486
- ___block_literal_global.497
- ___block_literal_global.506
- ___block_literal_global.523
- ___block_literal_global.525
- _associated conformance 4Home0A11KitFeaturesOSHAASQ
- _objc_msgSend$_dispatchWasUpdated
- _objc_msgSend$_errorLock_lock
- _objc_msgSend$_errorLock_unlock
- _objc_msgSend$_synchronizeHomeKitToManagedConfiguration
- _requestStatus:.onceToken
- _symbolic _____ 4Home0A11KitFeaturesO
- _symbolic _____ 4Home22AccessoryListUtilitiesC
CStrings:
+ "\x02\x1f"
+ "%@:(DU-D1.1) Duplicate request to disable updates for reason \"%@\""
+ "/Library/Caches/com.apple.xbs/Sources/Home/HomeFramework/Utilities/HFAccessoryListUtilities.swift"
+ "@56@0:8@16@24@32Q40@?48"
+ "HFHomePropertyCacheManager: Clearing room order cache"
+ "T@\"HMFUnfairLock\",&,N,V_roomOrderKeysLock"
+ "T@\"NSMutableSet\",&,N,V_keysForRoomOrder"
+ "T@\"NSString\",R,N,V_key"
+ "T@\"NSUUID\",R,N,V_objectID"
+ "TB,N,V__testing_disableCaching"
+ "_HFHomePropertyCacheManagerKey"
+ "__testing_disableCaching"
+ "_clearRoomOrderValues"
+ "_keysForRoomOrder"
+ "_objectID"
+ "_roomOrderKeysLock"
+ "_testing_disableCaching"
+ "com.apple.Home.valueManager.transactionLock"
+ "geocoder"
+ "hf_allHomePodsSupportRemoteProfileInstallation"
+ "initWithObjectID:key:"
+ "keysForRoomOrder"
+ "objectID"
+ "roomOrderKeysLock"
+ "setKeysForRoomOrder:"
+ "setRoomOrderKeysLock:"
+ "set_testing_disableCaching:"
+ "thirdrail"
+ "valueForObject:home:key:invalidationReasons:recalculationBlock:"
- "\x12\x1f"
- "%s accessoryReachableOverRapport ..%@"
- "(%s) Camera accessories are not favoritable"
- "-[HFAccessorySettingDeviceOptionsAdapter accessoryReachableOverRapport:]"
- "-[HMAccessory(HFIncludedContextProtocol) hf_isOnForContextType:]"
- "/Library/Caches/com.apple.xbs/Sources/Home/HomeFramework/Utilities/AccessoryListUtilities.swift"
- "Duplicate request to disable updates for reason \"%@\""
- "HFSensitiveStrings-Hindsight"
- "Hindsight"
- "ManagedConfigurationProfile"
- "_errorLock"
- "_errorLock_lock"
- "_errorLock_unlock"
- "d0d2700c4dee4686a15d55"
- "sortedRoomsForHome:"

```
