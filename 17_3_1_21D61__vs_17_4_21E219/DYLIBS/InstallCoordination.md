## InstallCoordination

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination`

```diff

-554.80.2.0.0
-  __TEXT.__text: 0x5d904
+579.102.3.0.0
+  __TEXT.__text: 0x5dde4
   __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_methlist: 0x2c88
+  __TEXT.__objc_methlist: 0x2cb0
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0xd131
-  __TEXT.__oslogstring: 0x7097
+  __TEXT.__cstring: 0xd365
+  __TEXT.__oslogstring: 0x70c6
   __TEXT.__gcc_except_tab: 0x16a0
-  __TEXT.__unwind_info: 0x151c
+  __TEXT.__unwind_info: 0x1548
   __TEXT.__objc_classname: 0x81c
-  __TEXT.__objc_methname: 0x957c
-  __TEXT.__objc_methtype: 0x1fc7
-  __TEXT.__objc_stubs: 0x5500
+  __TEXT.__objc_methname: 0x9664
+  __TEXT.__objc_methtype: 0x204a
+  __TEXT.__objc_stubs: 0x5580
   __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x1830
+  __DATA_CONST.__const: 0x1868
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9f20
-  __DATA_CONST.__objc_selrefs: 0x1c08
+  __DATA_CONST.__objc_const: 0x9f40
+  __DATA_CONST.__objc_selrefs: 0x1c38
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x2d0
+  __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__cfstring: 0x5060
+  __AUTH_CONST.__cfstring: 0x50c0
   __AUTH_CONST.__objc_const: 0xd8
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__auth_got: 0x578
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x2d0
-  __DATA.__objc_superrefs: 0x110
   __DATA.__objc_ivar: 0x1a8
   __DATA.__data: 0x8a8
   __DATA.__bss: 0x58
-  __DATA_DIRTY.__const: 0x300
+  __DATA_DIRTY.__const: 0x2a0
   __DATA_DIRTY.__objc_const: 0x18b0
   __DATA_DIRTY.__objc_data: 0xe60
   __DATA_DIRTY.__data: 0x8

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1789
-  Symbols:   5829
-  CStrings:  3085
+  Functions: 1797
+  Symbols:   5852
+  CStrings:  3104
 
Symbols:
+ +[IXAppInstallCoordinator updateiTunesMetadata:forAppWithIdentity:error:]
+ +[IXAppInstallCoordinator updateiTunesMetadata:forAppWithIdentity:wrapperURL:error:]
+ +[IXAppInstallCoordinator updateiTunesMetadata:forAppWithIdentity:wrapperURL:error:].cold.1
+ +[IXAppInstallCoordinator updateiTunesMetadataForAppWithIdentity:plistData:options:error:].cold.1
+ -[IXAppInstallCoordinator installOptionsWithError:]
+ GCC_except_table145
+ GCC_except_table150
+ GCC_except_table154
+ GCC_except_table158
+ GCC_except_table161
+ GCC_except_table164
+ GCC_except_table167
+ GCC_except_table170
+ GCC_except_table173
+ GCC_except_table176
+ GCC_except_table179
+ GCC_except_table182
+ GCC_except_table185
+ GCC_except_table188
+ GCC_except_table191
+ GCC_except_table194
+ GCC_except_table197
+ GCC_except_table200
+ GCC_except_table203
+ GCC_except_table206
+ GCC_except_table209
+ GCC_except_table212
+ GCC_except_table215
+ GCC_except_table218
+ GCC_except_table221
+ GCC_except_table224
+ GCC_except_table227
+ GCC_except_table230
+ GCC_except_table233
+ GCC_except_table236
+ GCC_except_table239
+ GCC_except_table242
+ GCC_except_table245
+ GCC_except_table248
+ GCC_except_table251
+ GCC_except_table265
+ GCC_except_table268
+ GCC_except_table271
+ GCC_except_table274
+ GCC_except_table277
+ GCC_except_table280
+ GCC_except_table283
+ GCC_except_table286
+ GCC_except_table289
+ GCC_except_table296
+ GCC_except_table303
+ GCC_except_table322
+ GCC_except_table325
+ GCC_except_table328
+ GCC_except_table331
+ GCC_except_table338
+ GCC_except_table375
+ GCC_except_table383
+ GCC_except_table386
+ GCC_except_table387
+ GCC_except_table390
+ GCC_except_table393
+ GCC_except_table396
+ GCC_except_table400
+ GCC_except_table403
+ _IXEncodeRootObject
+ _IXEncodeRootObject.cold.1
+ _IXSanitizeAndValidateRestrictedStoreMetadata
+ ___105+[IXAppInstallCoordinator(IXTesting) setTestModeForIdentifierPrefix:testMode:testSpecificValidationData:]_block_invoke.673
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.119
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.119.cold.1
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.119.cold.2
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.119.cold.3
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.119.cold.4
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.119.cold.5
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.119.cold.6
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.119.cold.7
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.119.cold.8
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.121
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.121.cold.1
+ ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.121.cold.2
+ ___175+[IXAppInstallCoordinator(IXDemoteToPlaceholder) _demoteAppToPlaceholderWithApplicationIdentity:forReason:waitForDeletion:ignoreRemovability:returnEarlyForTesting:completion:]_block_invoke_2.101
+ ___175+[IXAppInstallCoordinator(IXDemoteToPlaceholder) _demoteAppToPlaceholderWithApplicationIdentity:forReason:waitForDeletion:ignoreRemovability:returnEarlyForTesting:completion:]_block_invoke_2.101.cold.1
+ ___175+[IXAppInstallCoordinator(IXDemoteToPlaceholder) _demoteAppToPlaceholderWithApplicationIdentity:forReason:waitForDeletion:ignoreRemovability:returnEarlyForTesting:completion:]_block_invoke_2.101.cold.2
+ ___175+[IXAppInstallCoordinator(IXDemoteToPlaceholder) _demoteAppToPlaceholderWithApplicationIdentity:forReason:waitForDeletion:ignoreRemovability:returnEarlyForTesting:completion:]_block_invoke_2.101.cold.3
+ ___175+[IXAppInstallCoordinator(IXDemoteToPlaceholder) _demoteAppToPlaceholderWithApplicationIdentity:forReason:waitForDeletion:ignoreRemovability:returnEarlyForTesting:completion:]_block_invoke_2.101.cold.4
+ ___175+[IXAppInstallCoordinator(IXDemoteToPlaceholder) _demoteAppToPlaceholderWithApplicationIdentity:forReason:waitForDeletion:ignoreRemovability:returnEarlyForTesting:completion:]_block_invoke_2.101.cold.5
+ ___175+[IXAppInstallCoordinator(IXDemoteToPlaceholder) _demoteAppToPlaceholderWithApplicationIdentity:forReason:waitForDeletion:ignoreRemovability:returnEarlyForTesting:completion:]_block_invoke_2.101.cold.6
+ ___175+[IXAppInstallCoordinator(IXDemoteToPlaceholder) _demoteAppToPlaceholderWithApplicationIdentity:forReason:waitForDeletion:ignoreRemovability:returnEarlyForTesting:completion:]_block_invoke_2.101.cold.7
+ ___32-[IXAppInstallCoordinator error]_block_invoke.274
+ ___32-[IXAppInstallCoordinator error]_block_invoke_2.275
+ ___35-[IXPlaceholder setMetadata:error:]_block_invoke.268
+ ___35-[IXPlaceholder setSinfData:error:]_block_invoke.279
+ ___37-[IXAppInstallCoordinator isComplete]_block_invoke.278
+ ___37-[IXAppInstallCoordinator isComplete]_block_invoke.279
+ ___39-[IXAppInstallCoordinator setObserver:]_block_invoke.290
+ ___39-[IXAppInstallCoordinator setObserver:]_block_invoke.291
+ ___42-[IXAppInstallCoordinator pauseWithError:]_block_invoke.292
+ ___43-[IXAppInstallCoordinator resumeWithError:]_block_invoke.293
+ ___44-[IXAppInstallCoordinator coordinationState]_block_invoke.302
+ ___45-[IXAppInstallCoordinator hasAppAssetPromise]_block_invoke.192
+ ___45-[IXAppInstallCoordinator hasUserDataPromise]_block_invoke.242
+ ___46-[IXAppInstallCoordinator isPaused:withError:]_block_invoke.294
+ ___47+[IXAppInstallCoordinator(IXTesting) daemonPid]_block_invoke.666
+ ___47-[IXAppInstallCoordinator importanceWithError:]_block_invoke.214
+ ___47-[IXAppInstallCoordinator prioritizeWithError:]_block_invoke.295
+ ___47-[IXAppInstallCoordinator setImportance:error:]_block_invoke.213
+ ___48-[IXAppInstallCoordinator errorSourceIdentifier]_block_invoke.276
+ ___48-[IXAppInstallCoordinator errorSourceIdentifier]_block_invoke_2.277
+ ___48-[IXAppInstallCoordinator hasPlaceholderPromise]_block_invoke.182
+ ___49-[IXAppInstallCoordinator progressHintWithError:]_block_invoke.271
+ ___49-[IXAppInstallCoordinator removabilityWithError:]_block_invoke.265
+ ___51-[IXAppInstallCoordinator installOptionsWithError:]_block_invoke
+ ___51-[IXAppInstallCoordinator installOptionsWithError:]_block_invoke.211
+ ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.184
+ ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.184.cold.1
+ ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.184.cold.2
+ ___52-[IXAppInstallCoordinator setAppAssetPromise:error:]_block_invoke.183
+ ___52-[IXAppInstallCoordinator setUserDataPromise:error:]_block_invoke.233
+ ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.234
+ ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.234.cold.1
+ ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.234.cold.2
+ ___53-[IXAppInstallCoordinator coordinatorScopeWithError:]_block_invoke.268
+ ___53-[IXAppInstallCoordinator hasInitialODRAssetPromises]_block_invoke.232
+ ___53-[IXAppInstallCoordinator setProgressHint:withError:]_block_invoke.273
+ ___54-[IXAppInstallCoordinator userDataRestoreShouldBegin:]_block_invoke.243
+ ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.170
+ ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.170.cold.1
+ ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.170.cold.2
+ ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.244
+ ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.244.cold.1
+ ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.244.cold.2
+ ___55-[IXAppInstallCoordinator setPlaceholderPromise:error:]_block_invoke.169
+ ___56+[IXAppInstallCoordinator(IXTesting) setTestingEnabled:]_block_invoke.670
+ ___56-[IXAppInstallCoordinator cancelForReason:client:error:]_block_invoke.154
+ ___56-[IXAppInstallCoordinator cancelForReason:client:error:]_block_invoke.155
+ ___56-[IXAppInstallCoordinator getNeedsPostProcessing:error:]_block_invoke.256
+ ___56-[IXAppInstallCoordinator setNeedsPostProcessing:error:]_block_invoke.255
+ ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.674
+ ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.675
+ ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.676
+ ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.659
+ ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.660
+ ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.663
+ ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.664
+ ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.250
+ ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.250.cold.1
+ ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.250.cold.2
+ ___58-[IXAppInstallCoordinator setDeviceSecurityPromise:error:]_block_invoke.249
+ ___58-[IXAppInstallCoordinator setRemovability:byClient:error:]_block_invoke.264
+ ___59-[IXAppInstallCoordinator essentialAssetPromisesWithError:]_block_invoke.259
+ ___59-[IXAppInstallCoordinator placeholderDispositionWithError:]_block_invoke.267
+ ___59-[IXAppInstallCoordinator setEssentialAssetPromises:error:]_block_invoke.258
+ ___59-[IXAppInstallCoordinator setPlaceholderDisposition:error:]_block_invoke.266
+ ___59-[IXAppInstallCoordinator setPreparationPromise:withError:]_block_invoke.248
+ ___60-[IXAppInstallCoordinator initialODRAssetPromisesWithError:]_block_invoke.217
+ ___60-[IXAppInstallCoordinator setInitialODRAssetPromises:error:]_block_invoke.216
+ ___61-[IXAppInstallCoordinator getHasDeviceSecurityPromise:error:]_block_invoke.254
+ ___62-[IXAppInstallCoordinator getHasEssentialAssetPromises:error:]_block_invoke.263
+ ___62-[IXAppInstallCoordinator getPostProcessingShouldBegin:error:]_block_invoke.257
+ ___68-[IXAppInstallCoordinator appAssetPromiseHasBegunFulfillment:error:]_block_invoke.193
+ ___69-[IXAppInstallCoordinator appAssetPromiseResponsibleClientWithError:]_block_invoke.198
+ ___69-[IXAppInstallCoordinator setAppAssetPromiseResponsibleClient:error:]_block_invoke.197
+ ___71-[IXAppInstallCoordinator convertToGloballyScopedCoordinatorWithError:]_block_invoke.270
+ ___73+[IXAppInstallCoordinator updateiTunesMetadata:forAppWithIdentity:error:]_block_invoke
+ ___73+[IXAppInstallCoordinator updateiTunesMetadata:forAppWithIdentity:error:]_block_invoke.122
+ ___78+[IXAppInstallCoordinator(IXTesting) postNSCurrentLocaleDidChangeNotification]_block_invoke.667
+ ___80+[IXAppInstallCoordinator(IXTesting) purgeAllCoordinatorsAndPromisesForCreator:]_block_invoke.656
+ ___85+[IXAppInstallCoordinator refreshContainerTypes:forApplicationIdentity:reason:error:]_block_invoke.147
+ ___IXPresentErrorHighlightingLocalizedAppName_block_invoke.79
+ ___IXPresentErrorHighlightingLocalizedAppName_block_invoke.95
+ ___IXPresentErrorHighlightingLocalizedAppName_block_invoke_2.99
+ ___block_descriptor_48_e8_32r40r_e38_v24?0"MIInstallOptions"8"NSError"16lr32l8r40l8
+ ___block_literal_global.127
+ ___block_literal_global.153
+ ___block_literal_global.662
+ ___block_literal_global.669
+ ___block_literal_global.672
+ ___block_literal_global.81
+ _interface.weakInterface.299
+ _objc_msgSend$_remote_IXSCoordinatedAppInstall:getInstallOptions:
+ _objc_msgSend$_remote_updateiTunesMetadata:forAppWithIdentity:completion:
+ _objc_msgSend$distributorID
+ _objc_msgSend$distributorInfo
+ _objc_msgSend$metadataFromPlistData:error:
+ _objc_msgSend$updateiTunesMetadata:forAppWithIdentity:error:
- -[IXAppInstallCoordinator setInstallOptions:error:].cold.3
- -[IXPlaceholder setMetadata:error:].cold.2
- GCC_except_table143
- GCC_except_table148
- GCC_except_table152
- GCC_except_table156
- GCC_except_table159
- GCC_except_table162
- GCC_except_table165
- GCC_except_table168
- GCC_except_table171
- GCC_except_table174
- GCC_except_table177
- GCC_except_table180
- GCC_except_table183
- GCC_except_table186
- GCC_except_table189
- GCC_except_table192
- GCC_except_table195
- GCC_except_table198
- GCC_except_table201
- GCC_except_table204
- GCC_except_table207
- GCC_except_table210
- GCC_except_table213
- GCC_except_table216
- GCC_except_table219
- GCC_except_table222
- GCC_except_table225
- GCC_except_table228
- GCC_except_table231
- GCC_except_table234
- GCC_except_table237
- GCC_except_table240
- GCC_except_table243
- GCC_except_table246
- GCC_except_table260
- GCC_except_table263
- GCC_except_table266
- GCC_except_table269
- GCC_except_table272
- GCC_except_table275
- GCC_except_table278
- GCC_except_table281
- GCC_except_table284
- GCC_except_table291
- GCC_except_table298
- GCC_except_table312
- GCC_except_table315
- GCC_except_table323
- GCC_except_table326
- GCC_except_table333
- GCC_except_table370
- GCC_except_table373
- GCC_except_table381
- GCC_except_table382
- GCC_except_table385
- GCC_except_table388
- GCC_except_table391
- GCC_except_table395
- GCC_except_table398
- _OUTLINED_FUNCTION_23
- ___105+[IXAppInstallCoordinator(IXTesting) setTestModeForIdentifierPrefix:testMode:testSpecificValidationData:]_block_invoke.667
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.118
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.118.cold.1
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.118.cold.2
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.118.cold.3
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.118.cold.4
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.118.cold.5
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.118.cold.6
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.118.cold.7
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.118.cold.8
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.120
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.120.cold.1
- ___148+[IXAppInstallCoordinator(IXSimpleInstaller) _beginInstallForURL:forPersonaUniqueString:consumeSource:options:progressBlock:completionWithIdentity:]_block_invoke.120.cold.2
- ___175+[IXAppInstallCoordinator(IXDemoteToPlaceholder) _demoteAppToPlaceholderWithApplicationIdentity:forReason:waitForDeletion:ignoreRemovability:returnEarlyForTesting:completion:]_block_invoke_2.100
- ___175+[IXAppInstallCoordinator(IXDemoteToPlaceholder) _demoteAppToPlaceholderWithApplicationIdentity:forReason:waitForDeletion:ignoreRemovability:returnEarlyForTesting:completion:]_block_invoke_2.100.cold.1
- ___175+[IXAppInstallCoordinator(IXDemoteToPlaceholder) _demoteAppToPlaceholderWithApplicationIdentity:forReason:waitForDeletion:ignoreRemovability:returnEarlyForTesting:completion:]_block_invoke_2.100.cold.2
- ___175+[IXAppInstallCoordinator(IXDemoteToPlaceholder) _demoteAppToPlaceholderWithApplicationIdentity:forReason:waitForDeletion:ignoreRemovability:returnEarlyForTesting:completion:]_block_invoke_2.100.cold.3
- ___175+[IXAppInstallCoordinator(IXDemoteToPlaceholder) _demoteAppToPlaceholderWithApplicationIdentity:forReason:waitForDeletion:ignoreRemovability:returnEarlyForTesting:completion:]_block_invoke_2.100.cold.4
- ___175+[IXAppInstallCoordinator(IXDemoteToPlaceholder) _demoteAppToPlaceholderWithApplicationIdentity:forReason:waitForDeletion:ignoreRemovability:returnEarlyForTesting:completion:]_block_invoke_2.100.cold.5
- ___175+[IXAppInstallCoordinator(IXDemoteToPlaceholder) _demoteAppToPlaceholderWithApplicationIdentity:forReason:waitForDeletion:ignoreRemovability:returnEarlyForTesting:completion:]_block_invoke_2.100.cold.6
- ___175+[IXAppInstallCoordinator(IXDemoteToPlaceholder) _demoteAppToPlaceholderWithApplicationIdentity:forReason:waitForDeletion:ignoreRemovability:returnEarlyForTesting:completion:]_block_invoke_2.100.cold.7
- ___175+[IXAppInstallCoordinator(IXDemoteToPlaceholder) _demoteAppToPlaceholderWithApplicationIdentity:forReason:waitForDeletion:ignoreRemovability:returnEarlyForTesting:completion:]_block_invoke_2.100.cold.8
- ___32-[IXAppInstallCoordinator error]_block_invoke.272
- ___32-[IXAppInstallCoordinator error]_block_invoke_2.273
- ___35-[IXPlaceholder setMetadata:error:]_block_invoke.272
- ___35-[IXPlaceholder setSinfData:error:]_block_invoke.283
- ___37-[IXAppInstallCoordinator isComplete]_block_invoke.276
- ___37-[IXAppInstallCoordinator isComplete]_block_invoke.277
- ___39-[IXAppInstallCoordinator setObserver:]_block_invoke.288
- ___39-[IXAppInstallCoordinator setObserver:]_block_invoke.289
- ___42-[IXAppInstallCoordinator pauseWithError:]_block_invoke.290
- ___43-[IXAppInstallCoordinator resumeWithError:]_block_invoke.291
- ___44-[IXAppInstallCoordinator coordinationState]_block_invoke.300
- ___45-[IXAppInstallCoordinator hasAppAssetPromise]_block_invoke.188
- ___45-[IXAppInstallCoordinator hasUserDataPromise]_block_invoke.240
- ___46-[IXAppInstallCoordinator isPaused:withError:]_block_invoke.292
- ___47+[IXAppInstallCoordinator(IXTesting) daemonPid]_block_invoke.660
- ___47-[IXAppInstallCoordinator importanceWithError:]_block_invoke.212
- ___47-[IXAppInstallCoordinator prioritizeWithError:]_block_invoke.293
- ___47-[IXAppInstallCoordinator setImportance:error:]_block_invoke.211
- ___48-[IXAppInstallCoordinator errorSourceIdentifier]_block_invoke.274
- ___48-[IXAppInstallCoordinator errorSourceIdentifier]_block_invoke_2.275
- ___48-[IXAppInstallCoordinator hasPlaceholderPromise]_block_invoke.178
- ___49-[IXAppInstallCoordinator progressHintWithError:]_block_invoke.269
- ___49-[IXAppInstallCoordinator removabilityWithError:]_block_invoke.263
- ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.180
- ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.180.cold.1
- ___52-[IXAppInstallCoordinator appAssetPromiseWithError:]_block_invoke.180.cold.2
- ___52-[IXAppInstallCoordinator setAppAssetPromise:error:]_block_invoke.179
- ___52-[IXAppInstallCoordinator setUserDataPromise:error:]_block_invoke.231
- ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.232
- ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.232.cold.1
- ___52-[IXAppInstallCoordinator userDataPromiseWithError:]_block_invoke.232.cold.2
- ___53-[IXAppInstallCoordinator coordinatorScopeWithError:]_block_invoke.266
- ___53-[IXAppInstallCoordinator hasInitialODRAssetPromises]_block_invoke.230
- ___53-[IXAppInstallCoordinator setProgressHint:withError:]_block_invoke.271
- ___54-[IXAppInstallCoordinator userDataRestoreShouldBegin:]_block_invoke.241
- ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.166
- ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.166.cold.1
- ___55-[IXAppInstallCoordinator placeholderPromiseWithError:]_block_invoke.166.cold.2
- ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.242
- ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.242.cold.1
- ___55-[IXAppInstallCoordinator preparationPromiseWithError:]_block_invoke.242.cold.2
- ___55-[IXAppInstallCoordinator setPlaceholderPromise:error:]_block_invoke.165
- ___56+[IXAppInstallCoordinator(IXTesting) setTestingEnabled:]_block_invoke.664
- ___56-[IXAppInstallCoordinator cancelForReason:client:error:]_block_invoke.150
- ___56-[IXAppInstallCoordinator cancelForReason:client:error:]_block_invoke.151
- ___56-[IXAppInstallCoordinator getNeedsPostProcessing:error:]_block_invoke.254
- ___56-[IXAppInstallCoordinator setNeedsPostProcessing:error:]_block_invoke.253
- ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.668
- ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.669
- ___57+[IXAppInstallCoordinator(IXTesting) simulateClientDeath]_block_invoke.670
- ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.651
- ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.653
- ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.654
- ___58+[IXAppInstallCoordinator(IXTesting) killDaemonForTesting]_block_invoke.658
- ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.248
- ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.248.cold.1
- ___58-[IXAppInstallCoordinator deviceSecurityPromiseWithError:]_block_invoke.248.cold.2
- ___58-[IXAppInstallCoordinator setDeviceSecurityPromise:error:]_block_invoke.247
- ___58-[IXAppInstallCoordinator setRemovability:byClient:error:]_block_invoke.262
- ___59-[IXAppInstallCoordinator essentialAssetPromisesWithError:]_block_invoke.257
- ___59-[IXAppInstallCoordinator placeholderDispositionWithError:]_block_invoke.265
- ___59-[IXAppInstallCoordinator setEssentialAssetPromises:error:]_block_invoke.256
- ___59-[IXAppInstallCoordinator setPlaceholderDisposition:error:]_block_invoke.264
- ___59-[IXAppInstallCoordinator setPreparationPromise:withError:]_block_invoke.246
- ___60-[IXAppInstallCoordinator initialODRAssetPromisesWithError:]_block_invoke.215
- ___60-[IXAppInstallCoordinator setInitialODRAssetPromises:error:]_block_invoke.214
- ___61-[IXAppInstallCoordinator getHasDeviceSecurityPromise:error:]_block_invoke.252
- ___62-[IXAppInstallCoordinator getHasEssentialAssetPromises:error:]_block_invoke.261
- ___62-[IXAppInstallCoordinator getPostProcessingShouldBegin:error:]_block_invoke.255
- ___68-[IXAppInstallCoordinator appAssetPromiseHasBegunFulfillment:error:]_block_invoke.189
- ___69-[IXAppInstallCoordinator appAssetPromiseResponsibleClientWithError:]_block_invoke.194
- ___69-[IXAppInstallCoordinator setAppAssetPromiseResponsibleClient:error:]_block_invoke.193
- ___71-[IXAppInstallCoordinator convertToGloballyScopedCoordinatorWithError:]_block_invoke.268
- ___78+[IXAppInstallCoordinator(IXTesting) postNSCurrentLocaleDidChangeNotification]_block_invoke.661
- ___80+[IXAppInstallCoordinator(IXTesting) purgeAllCoordinatorsAndPromisesForCreator:]_block_invoke.650
- ___85+[IXAppInstallCoordinator refreshContainerTypes:forApplicationIdentity:reason:error:]_block_invoke.143
- ___90+[IXAppInstallCoordinator updateiTunesMetadataForAppWithIdentity:plistData:options:error:]_block_invoke
- ___90+[IXAppInstallCoordinator updateiTunesMetadataForAppWithIdentity:plistData:options:error:]_block_invoke.118
- ___IXPresentErrorHighlightingLocalizedAppName_block_invoke.76
- ___IXPresentErrorHighlightingLocalizedAppName_block_invoke.92
- ___IXPresentErrorHighlightingLocalizedAppName_block_invoke_2.96
- ___block_literal_global.124
- ___block_literal_global.150
- ___block_literal_global.656
- ___block_literal_global.663
- ___block_literal_global.666
- ___block_literal_global.78
- _interface.weakInterface.295
- _objc_msgSend$_remote_updateiTunesMetadataForAppWithIdentity:plistData:options:completion:
- _objc_msgSend$bundleContainerURL
CStrings:
+ "%s: Client %@ setting the %@ did not have the required entitlement \"%@\" = TRUE to allow the distribution info in the store metadata to be set (supplied distributor ID was '%@'). : %@"
+ "%s: Failed to update iTunesMetadata for identity %@ : %@"
+ "%s: Failed to update iTunesMetadata: %@"
+ "%s: Got exception while trying to encode object %@ : %@ : %@"
+ "%s: Unable to decode supplied plist data : %@"
+ "+[IXAppInstallCoordinator updateiTunesMetadata:forAppWithIdentity:error:]_block_invoke"
+ "+[IXAppInstallCoordinator updateiTunesMetadata:forAppWithIdentity:wrapperURL:error:]"
+ "+[IXAppInstallCoordinator updateiTunesMetadataForAppWithIdentity:plistData:options:error:]"
+ "-[IXAppInstallCoordinator installOptionsWithError:]_block_invoke"
+ "Client %@ setting the %@ did not have the required entitlement \"%@\" = TRUE to allow the distribution info in the store metadata to be set (supplied distributor ID was '%@')."
+ "Device is not eligible to install this app."
+ "Got exception while trying to encode object %@ : %@"
+ "IXEncodeRootObject"
+ "IXSanitizeAndValidateRestrictedStoreMetadata"
+ "T@\"NSString\",?,R,C"
+ "TB,?,R,N"
+ "This app could not be installed because this device is not eligible to install it."
+ "Unable to decode supplied plist data"
+ "Vv32@0:8@\"NSUUID\"16@?<v@?@\"MIInstallOptions\"@\"NSError\">24"
+ "_remote_IXSCoordinatedAppInstall:getInstallOptions:"
+ "_remote_updateiTunesMetadata:forAppWithIdentity:completion:"
+ "com.apple.private.install.distributor-info-source"
+ "distributorID"
+ "distributorInfo"
+ "installOptionsWithError:"
+ "kIXUserPresentableDeviceNotEligibleError"
+ "metadataFromPlistData:error:"
+ "updateiTunesMetadata:forAppWithIdentity:error:"
+ "updateiTunesMetadata:forAppWithIdentity:wrapperURL:error:"
+ "v24@?0@\"MIInstallOptions\"8@\"NSError\"16"
+ "v40@0:8@\"MIStoreMetadata\"16@\"IXApplicationIdentity\"24@?<v@?@\"NSError\">32"
- "%s: Failed to read iTunesMetadata.plist from %@ when demoting %@ : %@"
- "%s: Failed to update iTunesMetadata for identity:%@ with:%@"
- "%s: Got exception while trying to encode metadata: %@ : %@"
- "%s: Got exception while trying to encode options data: %@ : %@"
- "%s: LSApplicationProxy for %@ did not contain a bundleContainerURL during demotion : %@"
- "+[IXAppInstallCoordinator updateiTunesMetadataForAppWithIdentity:plistData:options:error:]_block_invoke"
- "Failed to read iTunesMetadata.plist from %@ when demoting %@"
- "Got exception while trying to encode metadata: %@"
- "Got exception while trying to encode options data: %@"
- "LSApplicationProxy for %@ did not contain a bundleContainerURL during demotion"
- "_remote_updateiTunesMetadataForAppWithIdentity:plistData:options:completion:"
- "bundleContainerURL"

```
