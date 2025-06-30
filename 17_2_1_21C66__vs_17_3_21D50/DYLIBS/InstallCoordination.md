## InstallCoordination

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination`

```diff

-554.40.9.0.0
-  __TEXT.__text: 0x5b8e4
-  __TEXT.__auth_stubs: 0xab0
-  __TEXT.__objc_methlist: 0x2b50
+554.80.2.0.0
+  __TEXT.__text: 0x5d904
+  __TEXT.__auth_stubs: 0xad0
+  __TEXT.__objc_methlist: 0x2c88
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0xcf7f
-  __TEXT.__oslogstring: 0x6d80
-  __TEXT.__gcc_except_tab: 0x1684
-  __TEXT.__unwind_info: 0x14bc
-  __TEXT.__objc_classname: 0x80b
-  __TEXT.__objc_methname: 0x93d2
-  __TEXT.__objc_methtype: 0x1f6c
-  __TEXT.__objc_stubs: 0x5380
+  __TEXT.__cstring: 0xd131
+  __TEXT.__oslogstring: 0x7097
+  __TEXT.__gcc_except_tab: 0x16a0
+  __TEXT.__unwind_info: 0x151c
+  __TEXT.__objc_classname: 0x81c
+  __TEXT.__objc_methname: 0x957c
+  __TEXT.__objc_methtype: 0x1fc7
+  __TEXT.__objc_stubs: 0x5500
   __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x17d8
-  __DATA_CONST.__objc_classlist: 0x170
+  __DATA_CONST.__const: 0x1830
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9ce8
-  __DATA_CONST.__objc_selrefs: 0x1b88
+  __DATA_CONST.__objc_const: 0x9f20
+  __DATA_CONST.__objc_selrefs: 0x1c08
   __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__cfstring: 0x4f80
-  __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__cfstring: 0x5060
+  __AUTH_CONST.__objc_const: 0xd8
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH_CONST.__auth_got: 0x568
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__auth_got: 0x578
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x2c8
-  __DATA.__objc_superrefs: 0x108
-  __DATA.__objc_ivar: 0x1a0
+  __DATA.__objc_classrefs: 0x2d0
+  __DATA.__objc_superrefs: 0x110
+  __DATA.__objc_ivar: 0x1a8
   __DATA.__data: 0x8a8
-  __DATA.__bss: 0x50
-  __DATA_DIRTY.__const: 0x360
+  __DATA.__bss: 0x58
+  __DATA_DIRTY.__const: 0x300
   __DATA_DIRTY.__objc_const: 0x18b0
   __DATA_DIRTY.__objc_data: 0xe60
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x88
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F92D48FC-1264-30E7-8C6A-E15955818822
-  Functions: 1752
-  Symbols:   5705
-  CStrings:  3672
+  UUID: E26678B3-F726-3A3F-8A57-60833B852559
+  Functions: 1789
+  Symbols:   5829
+  CStrings:  3728
 
Symbols:
+ +[IXAppInstallCoordinator removabilityDataWithChangeClock:error:]
+ +[IXAppInstallCoordinator removabilityDataWithCompletion:]
+ +[IXAppRemovabilityMetadata supportsSecureCoding]
+ +[IXDataStoreClock newClockWithDictionary:]
+ +[IXDataStoreClock newClock]
+ +[IXDataStoreClock supportsSecureCoding]
+ -[IXAppRemovabilityMetadata encodeWithCoder:]
+ -[IXAppRemovabilityMetadata initWithCoder:]
+ -[IXDataStoreClock .cxx_destruct]
+ -[IXDataStoreClock copyWithZone:]
+ -[IXDataStoreClock description]
+ -[IXDataStoreClock dictionaryRepresentation]
+ -[IXDataStoreClock encodeWithCoder:]
+ -[IXDataStoreClock guid]
+ -[IXDataStoreClock hash]
+ -[IXDataStoreClock increment]
+ -[IXDataStoreClock initWithCoder:]
+ -[IXDataStoreClock initWithGUID:sequenceNumber:]
+ -[IXDataStoreClock isEqual:]
+ -[IXDataStoreClock notificationDictionary]
+ -[IXDataStoreClock sequenceNumber]
+ -[IXDataStoreClock setGuid:]
+ -[IXDataStoreClock setSequenceNumber:]
+ GCC_except_table132
+ GCC_except_table139
+ GCC_except_table143
+ GCC_except_table148
+ GCC_except_table152
+ GCC_except_table243
+ GCC_except_table246
+ GCC_except_table281
+ GCC_except_table284
+ GCC_except_table291
+ GCC_except_table298
+ GCC_except_table312
+ GCC_except_table315
+ GCC_except_table323
+ GCC_except_table326
+ GCC_except_table333
+ GCC_except_table370
+ GCC_except_table373
+ GCC_except_table378
+ GCC_except_table381
+ GCC_except_table388
+ GCC_except_table391
+ GCC_except_table395
+ GCC_except_table398
+ _IXGetUncachedRemovabilityDataStore
+ _IXGetUncachedRemovabilityMetadataForApp.cold.6
+ _IXNotificationPayloadRemovabilityStoreClockKey
+ _IXNotificationPayloadRemovabilityValueKey
+ _OBJC_CLASS_$_IXDataStoreClock
+ _OBJC_IVAR_$_IXDataStoreClock._guid
+ _OBJC_IVAR_$_IXDataStoreClock._sequenceNumber
+ _OBJC_METACLASS_$_IXDataStoreClock
+ __CopyRemovabilityDataFromURL
+ __CopyRemovabilityDataFromURL.cold.1
+ __CopyRemovabilityDataFromURL.cold.2
+ __CopyRemovabilityDataFromURL.cold.3
+ __IXValidateObject
+ __OBJC_$_CLASS_METHODS_IXAppRemovabilityMetadata
+ __OBJC_$_CLASS_METHODS_IXDataStoreClock
+ __OBJC_$_CLASS_PROP_LIST_IXAppRemovabilityMetadata
+ __OBJC_$_CLASS_PROP_LIST_IXDataStoreClock
+ __OBJC_$_INSTANCE_METHODS_IXDataStoreClock
+ __OBJC_$_INSTANCE_VARIABLES_IXDataStoreClock
+ __OBJC_$_PROP_LIST_IXDataStoreClock
+ __OBJC_CLASS_PROTOCOLS_$_IXDataStoreClock
+ __OBJC_CLASS_RO_$_IXDataStoreClock
+ __OBJC_METACLASS_RO_$_IXDataStoreClock
+ __RemovabilityPListToMetadata
+ ___105+[IXAppInstallCoordinator(IXTesting) setTestModeForIdentifierPrefix:testMode:testSpecificValidationData:]_block_invoke.667
+ ___32-[IXAppInstallCoordinator error]_block_invoke.272
+ ___32-[IXAppInstallCoordinator error]_block_invoke_2.273
+ ___37-[IXAppInstallCoordinator isComplete]_block_invoke.276
+ ___37-[IXAppInstallCoordinator isComplete]_block_invoke.277
+ ___39-[IXAppInstallCoordinator setObserver:]_block_invoke.288
+ ___39-[IXAppInstallCoordinator setObserver:]_block_invoke.289
+ ___42-[IXAppInstallCoordinator pauseWithError:]_block_invoke.290
+ ___43-[IXAppInstallCoordinator resumeWithError:]_block_invoke.291
+ ___44-[IXAppInstallCoordinator coordinationState]_block_invoke.300
+ ___44-[IXAppInstallCoordinator hasInstallOptions]_block_invoke.210
+ ___45-[IXAppInstallCoordinator hasAppAssetPromise]_block_invoke.188
+ ___45-[IXAppInstallCoordinator hasUserDataPromise]_block_invoke.240
+ ___46-[IXAppInstallCoordinator isPaused:withError:]_block_invoke.292
+ ___47+[IXAppInstallCoordinator(IXTesting) daemonPid]_block_invoke.660
+ ___47-[IXAppInstallCoordinator importanceWithError:]_block_invoke.212
+ ___47-[IXAppInstallCoordinator prioritizeWithError:]_block_invoke.293
+ ___47-[IXAppInstallCoordinator setImportance:error:]_block_invoke.211
+ ___48-[IXAppInstallCoordinator errorSourceIdentifier]_block_invoke.274
+ ___48-[IXAppInstallCoordinator errorSourceIdentifier]_block_invoke_2.275
+ ___48-[IXAppInstallCoordinator hasPlaceholderPromise]_block_invoke.178
+ ___49-[IXAppInstallCoordinator progressHintWithError:]_block_invoke.269
+ ___49-[IXAppInstallCoordinator removabilityWithError:]_block_invoke.263
+ ___51-[IXAppInstallCoordinator setInstallOptions:error:]_block_invoke.209
+ ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.180
+ ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.180.cold.1
+ ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.180.cold.2
+ ___52-[IXAppInstallCoordinator setAppAssetPromise:error:]_block_invoke.179
+ ___52-[IXAppInstallCoordinator setUserDataPromise:error:]_block_invoke.231
+ ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.232
+ ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.232.cold.1
+ ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.232.cold.2
+ ___53-[IXAppInstallCoordinator coordinatorScopeWithError:]_block_invoke.266
+ ___53-[IXAppInstallCoordinator hasInitialODRAssetPromises]_block_invoke.230
+ ___53-[IXAppInstallCoordinator setProgressHint:withError:]_block_invoke.271
+ ___54-[IXAppInstallCoordinator userDataRestoreShouldBegin:]_block_invoke.241
+ ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.166
+ ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.166.cold.1
+ ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.166.cold.2
+ ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.242
+ ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.242.cold.1
+ ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.242.cold.2
+ ___55-[IXAppInstallCoordinator setPlaceholderPromise:error:]_block_invoke.165
+ ___56+[IXAppInstallCoordinator(IXTesting) setTestingEnabled:]_block_invoke.664
+ ___56-[IXAppInstallCoordinator cancelForReason:client:error:]_block_invoke.150
+ ___56-[IXAppInstallCoordinator cancelForReason:client:error:]_block_invoke.151
+ ___56-[IXAppInstallCoordinator getNeedsPostProcessing:error:]_block_invoke.254
+ ___56-[IXAppInstallCoordinator setNeedsPostProcessing:error:]_block_invoke.253
+ ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.668
+ ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.669
+ ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.670
+ ___58+[IXAppInstallCoordinator removabilityDataWithCompletion:]_block_invoke
+ ___58+[IXAppInstallCoordinator removabilityDataWithCompletion:]_block_invoke_2
+ ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.651
+ ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.654
+ ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.657
+ ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.658
+ ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.248
+ ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.248.cold.1
+ ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.248.cold.2
+ ___58-[IXAppInstallCoordinator setDeviceSecurityPromise:error:]_block_invoke.247
+ ___58-[IXAppInstallCoordinator setRemovability:byClient:error:]_block_invoke.262
+ ___59-[IXAppInstallCoordinator essentialAssetPromisesWithError:]_block_invoke.257
+ ___59-[IXAppInstallCoordinator placeholderDispositionWithError:]_block_invoke.265
+ ___59-[IXAppInstallCoordinator setEssentialAssetPromises:error:]_block_invoke.256
+ ___59-[IXAppInstallCoordinator setPlaceholderDisposition:error:]_block_invoke.264
+ ___59-[IXAppInstallCoordinator setPreparationPromise:withError:]_block_invoke.246
+ ___60-[IXAppInstallCoordinator initialODRAssetPromisesWithError:]_block_invoke.215
+ ___60-[IXAppInstallCoordinator setInitialODRAssetPromises:error:]_block_invoke.214
+ ___61-[IXAppInstallCoordinator getHasDeviceSecurityPromise:error:]_block_invoke.252
+ ___62-[IXAppInstallCoordinator getHasEssentialAssetPromises:error:]_block_invoke.261
+ ___62-[IXAppInstallCoordinator getPostProcessingShouldBegin:error:]_block_invoke.255
+ ___65+[IXAppInstallCoordinator removabilityDataWithChangeClock:error:]_block_invoke
+ ___65+[IXAppInstallCoordinator removabilityDataWithChangeClock:error:]_block_invoke.112
+ ___68-[IXAppInstallCoordinator appAssetPromiseHasBegunFulfillment:error:]_block_invoke.189
+ ___69-[IXAppInstallCoordinator appAssetPromiseResponsibleClientWithError:]_block_invoke.194
+ ___69-[IXAppInstallCoordinator setAppAssetPromiseResponsibleClient:error:]_block_invoke.193
+ ___71-[IXAppInstallCoordinator convertToGloballyScopedCoordinatorWithError:]_block_invoke.268
+ ___78+[IXAppInstallCoordinator(IXTesting) postNSCurrentLocaleDidChangeNotification]_block_invoke.661
+ ___79+[IXAppInstallCoordinator updateSINFForAppWithIdentity:sinfData:options:error:]_block_invoke.117
+ ___80+[IXAppInstallCoordinator(IXTesting) purgeAllCoordinatorsAndPromisesForCreator:]_block_invoke.650
+ ___85+[IXAppInstallCoordinator refreshContainerTypes:forApplicationIdentity:reason:error:]_block_invoke.143
+ ___90+[IXAppInstallCoordinator updateiTunesMetadataForAppWithIdentity:plistData:options:error:]_block_invoke.118
+ ___block_descriptor_56_e8_32r40r48r_e55_v32?0"NSDictionary"8"IXDataStoreClock"16"NSError"24lr32l8r40l8r48l8
+ ___block_literal_global.656
+ ___block_literal_global.663
+ ___block_literal_global.666
+ _interface.weakInterface.295
+ _kIXDataStoreClockGUIDKey
+ _kIXDataStoreClockSequenceNumberKey
+ _kIXNotificationPayloadDataStoreClockGUIDKey
+ _kIXNotificationPayloadDataStoreClockSequenceNumberKey
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_remote_removabilityDataWithCompletion:
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$guid
+ _objc_msgSend$initWithGUID:sequenceNumber:
+ _objc_msgSend$initWithUUIDString:
+ _objc_msgSend$newClockWithDictionary:
+ _objc_msgSend$propertyListWithData:options:format:error:
+ _objc_msgSend$sequenceNumber
+ _objc_msgSend$setGuid:
+ _objc_msgSend$setSequenceNumber:
+ _objc_retain_x27
+ _objc_retain_x28
- GCC_except_table133
- GCC_except_table137
- GCC_except_table142
- GCC_except_table146
- GCC_except_table150
- GCC_except_table153
- GCC_except_table254
- GCC_except_table257
- GCC_except_table285
- GCC_except_table292
- GCC_except_table306
- GCC_except_table309
- GCC_except_table311
- GCC_except_table314
- GCC_except_table327
- GCC_except_table364
- GCC_except_table367
- GCC_except_table372
- GCC_except_table375
- GCC_except_table376
- GCC_except_table379
- GCC_except_table389
- GCC_except_table392
- ___105+[IXAppInstallCoordinator(IXTesting) setTestModeForIdentifierPrefix:testMode:testSpecificValidationData:]_block_invoke.662
- ___32-[IXAppInstallCoordinator error]_block_invoke.270
- ___32-[IXAppInstallCoordinator error]_block_invoke_2.271
- ___37-[IXAppInstallCoordinator isComplete]_block_invoke.274
- ___37-[IXAppInstallCoordinator isComplete]_block_invoke.275
- ___39-[IXAppInstallCoordinator setObserver:]_block_invoke.286
- ___39-[IXAppInstallCoordinator setObserver:]_block_invoke.287
- ___42-[IXAppInstallCoordinator pauseWithError:]_block_invoke.288
- ___43-[IXAppInstallCoordinator resumeWithError:]_block_invoke.289
- ___44-[IXAppInstallCoordinator coordinationState]_block_invoke.298
- ___44-[IXAppInstallCoordinator hasInstallOptions]_block_invoke.208
- ___45-[IXAppInstallCoordinator hasAppAssetPromise]_block_invoke.186
- ___45-[IXAppInstallCoordinator hasUserDataPromise]_block_invoke.238
- ___46-[IXAppInstallCoordinator isPaused:withError:]_block_invoke.290
- ___47+[IXAppInstallCoordinator(IXTesting) daemonPid]_block_invoke.655
- ___47-[IXAppInstallCoordinator importanceWithError:]_block_invoke.210
- ___47-[IXAppInstallCoordinator prioritizeWithError:]_block_invoke.291
- ___47-[IXAppInstallCoordinator setImportance:error:]_block_invoke.209
- ___48-[IXAppInstallCoordinator errorSourceIdentifier]_block_invoke.272
- ___48-[IXAppInstallCoordinator errorSourceIdentifier]_block_invoke_2.273
- ___48-[IXAppInstallCoordinator hasPlaceholderPromise]_block_invoke.176
- ___49-[IXAppInstallCoordinator progressHintWithError:]_block_invoke.267
- ___49-[IXAppInstallCoordinator removabilityWithError:]_block_invoke.261
- ___51-[IXAppInstallCoordinator setInstallOptions:error:]_block_invoke.207
- ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.178
- ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.178.cold.1
- ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.178.cold.2
- ___52-[IXAppInstallCoordinator setAppAssetPromise:error:]_block_invoke.177
- ___52-[IXAppInstallCoordinator setUserDataPromise:error:]_block_invoke.229
- ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.230
- ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.230.cold.1
- ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.230.cold.2
- ___53-[IXAppInstallCoordinator coordinatorScopeWithError:]_block_invoke.264
- ___53-[IXAppInstallCoordinator hasInitialODRAssetPromises]_block_invoke.228
- ___53-[IXAppInstallCoordinator setProgressHint:withError:]_block_invoke.269
- ___54-[IXAppInstallCoordinator userDataRestoreShouldBegin:]_block_invoke.239
- ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.164
- ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.164.cold.1
- ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.164.cold.2
- ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.240
- ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.240.cold.1
- ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.240.cold.2
- ___55-[IXAppInstallCoordinator setPlaceholderPromise:error:]_block_invoke.163
- ___56+[IXAppInstallCoordinator(IXTesting) setTestingEnabled:]_block_invoke.659
- ___56-[IXAppInstallCoordinator cancelForReason:client:error:]_block_invoke.148
- ___56-[IXAppInstallCoordinator cancelForReason:client:error:]_block_invoke.149
- ___56-[IXAppInstallCoordinator getNeedsPostProcessing:error:]_block_invoke.252
- ___56-[IXAppInstallCoordinator setNeedsPostProcessing:error:]_block_invoke.251
- ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.663
- ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.664
- ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.665
- ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.646
- ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.648
- ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.649
- ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.652
- ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.246
- ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.246.cold.1
- ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.246.cold.2
- ___58-[IXAppInstallCoordinator setDeviceSecurityPromise:error:]_block_invoke.245
- ___58-[IXAppInstallCoordinator setRemovability:byClient:error:]_block_invoke.260
- ___59-[IXAppInstallCoordinator essentialAssetPromisesWithError:]_block_invoke.255
- ___59-[IXAppInstallCoordinator placeholderDispositionWithError:]_block_invoke.263
- ___59-[IXAppInstallCoordinator setEssentialAssetPromises:error:]_block_invoke.254
- ___59-[IXAppInstallCoordinator setPlaceholderDisposition:error:]_block_invoke.262
- ___59-[IXAppInstallCoordinator setPreparationPromise:withError:]_block_invoke.244
- ___60-[IXAppInstallCoordinator initialODRAssetPromisesWithError:]_block_invoke.213
- ___60-[IXAppInstallCoordinator setInitialODRAssetPromises:error:]_block_invoke.212
- ___61-[IXAppInstallCoordinator getHasDeviceSecurityPromise:error:]_block_invoke.250
- ___62-[IXAppInstallCoordinator getHasEssentialAssetPromises:error:]_block_invoke.259
- ___62-[IXAppInstallCoordinator getPostProcessingShouldBegin:error:]_block_invoke.253
- ___68-[IXAppInstallCoordinator appAssetPromiseHasBegunFulfillment:error:]_block_invoke.187
- ___69-[IXAppInstallCoordinator appAssetPromiseResponsibleClientWithError:]_block_invoke.192
- ___69-[IXAppInstallCoordinator setAppAssetPromiseResponsibleClient:error:]_block_invoke.191
- ___71-[IXAppInstallCoordinator convertToGloballyScopedCoordinatorWithError:]_block_invoke.266
- ___78+[IXAppInstallCoordinator(IXTesting) postNSCurrentLocaleDidChangeNotification]_block_invoke.656
- ___79+[IXAppInstallCoordinator updateSINFForAppWithIdentity:sinfData:options:error:]_block_invoke.115
- ___80+[IXAppInstallCoordinator(IXTesting) purgeAllCoordinatorsAndPromisesForCreator:]_block_invoke.645
- ___85+[IXAppInstallCoordinator refreshContainerTypes:forApplicationIdentity:reason:error:]_block_invoke.141
- ___90+[IXAppInstallCoordinator updateiTunesMetadataForAppWithIdentity:plistData:options:error:]_block_invoke.116
- ___block_literal_global.651
- ___block_literal_global.658
- ___block_literal_global.661
- _interface.weakInterface.289
CStrings:
+ "%s: Deserialized key for removability entry is not string %@ : %@"
+ "%s: Deserialized removability plist is missing key %@"
+ "%s: Deserialized removability plist is missing key %@ : %@"
+ "%s: Deserialized removability plist is not dictionary"
+ "%s: Failed to deserialize removability plist: %@"
+ "%s: Failed to extract change clock from deserialized removability plist: %@"
+ "%s: Failed to extract removability entries from deserialized removability plist: %@"
+ "%s: Failed to fetch removability metadata from %@"
+ "%s: Received non dictionary object for %@ : %@"
+ "%s: Received non dictionary object for change clock in deserialized removability plist: %@"
+ "%s: Received non dictionary object for removability entries in deserialized removability plist: %@"
+ "%s: Received non dictionary object for requested keys %@ : %@"
+ "+[IXAppInstallCoordinator removabilityDataWithChangeClock:error:]_block_invoke"
+ "+[IXAppInstallCoordinator removabilityDataWithCompletion:]_block_invoke_2"
+ "<%@ guid:%@ serialNumber:%llu>"
+ "@32@0:8@16Q24"
+ "@32@0:8^@16^@24"
+ "ClockedRemovabilityMetadata.plist"
+ "IXDataStoreClock"
+ "IXGetUncachedRemovabilityDataStore"
+ "RemovabilityChangeClock"
+ "RemovabilityEntries"
+ "RemovabilityStoreClock"
+ "RemovabilityVal"
+ "T@\"NSDictionary\",R,N"
+ "T@\"NSUUID\",&,N,V_guid"
+ "TQ,N,V_sequenceNumber"
+ "UUID"
+ "UUIDString"
+ "_ExtractObjectsFromDeserializedRemovabilityPlist"
+ "_guid"
+ "_remote_removabilityDataWithCompletion:"
+ "_sequenceNumber"
+ "guid"
+ "increment"
+ "initWithGUID:sequenceNumber:"
+ "initWithUUIDString:"
+ "newClock"
+ "newClockWithDictionary:"
+ "notificationDictionary"
+ "propertyListWithData:options:format:error:"
+ "removabilityDataWithChangeClock:error:"
+ "removabilityDataWithCompletion:"
+ "sequenceNumber"
+ "setGuid:"
+ "setSequenceNumber:"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"IXDataStoreClock\"@\"NSError\">16"
+ "v32@?0@\"NSDictionary\"8@\"IXDataStoreClock\"16@\"NSError\"24"
- "RemovabilityMetadata.plist"

```
