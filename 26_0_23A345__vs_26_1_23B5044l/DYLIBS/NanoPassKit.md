## NanoPassKit

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit`

```diff

-1276.0.0.0.0
-  __TEXT.__text: 0x2569e8
+1282.0.0.0.0
+  __TEXT.__text: 0x2580a0
   __TEXT.__auth_stubs: 0x1e80
-  __TEXT.__objc_methlist: 0x25b58
-  __TEXT.__cstring: 0x18018
-  __TEXT.__const: 0xd34
-  __TEXT.__oslogstring: 0x2cae7
-  __TEXT.__gcc_except_tab: 0x6dc8
+  __TEXT.__objc_methlist: 0x25c20
+  __TEXT.__cstring: 0x180d8
+  __TEXT.__const: 0xd44
+  __TEXT.__oslogstring: 0x2d037
+  __TEXT.__gcc_except_tab: 0x6eb8
   __TEXT.__dlopen_cstrs: 0x260
   __TEXT.__ustring: 0x160
   __TEXT.__constg_swiftt: 0x294

   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__unwind_info: 0x8f08
+  __TEXT.__unwind_info: 0x8f98
   __TEXT.__eh_frame: 0x378
   __TEXT.__objc_classname: 0x6b98
-  __TEXT.__objc_methname: 0x3fcaa
-  __TEXT.__objc_methtype: 0xa108
-  __TEXT.__objc_stubs: 0x220a0
-  __DATA_CONST.__got: 0x1e80
-  __DATA_CONST.__const: 0x6b80
+  __TEXT.__objc_methname: 0x3fdde
+  __TEXT.__objc_methtype: 0xa15f
+  __TEXT.__objc_stubs: 0x22160
+  __DATA_CONST.__got: 0x1e78
+  __DATA_CONST.__const: 0x6bb8
   __DATA_CONST.__objc_classlist: 0x1200
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc9d0
+  __DATA_CONST.__objc_selrefs: 0xca10
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x1130
   __DATA_CONST.__objc_arraydata: 0x98
   __AUTH_CONST.__auth_got: 0xf50
   __AUTH_CONST.__const: 0x1750
-  __AUTH_CONST.__cfstring: 0xeac0
-  __AUTH_CONST.__objc_const: 0x45c50
+  __AUTH_CONST.__cfstring: 0xeb20
+  __AUTH_CONST.__objc_const: 0x45cc8
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH.__objc_data: 0xb3e0
   __AUTH.__data: 0x1d0
-  __DATA.__objc_ivar: 0x1c64
+  __DATA.__objc_ivar: 0x1c70
   __DATA.__data: 0x1f48
   __DATA.__bss: 0x1200
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/Security.framework/Security
-  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppConduit.framework/AppConduit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CBBF6D71-B911-332C-A05E-6C8A84F43B6A
-  Functions: 14500
-  Symbols:   42519
-  CStrings:  17063
+  UUID: C1E7B3CA-359B-3DD2-88D3-225ADDE5E29A
+  Functions: 14523
+  Symbols:   42581
+  CStrings:  17099
 
Symbols:
+ -[NPKCompanionAgentConnection identityPassesOfTypes:completion:]
+ -[NPKCompanionAgentConnection passesOfCardType:completion:]
+ -[NPKDoublePressSuppressionAssertion _resyncStateWithCompletion:]
+ -[NPKIDVRemoteDeviceSession remoteService]
+ -[NPKIDVRemoteDeviceSession setRemoteService:]
+ -[NPKIDVRemoteDevicesManager _initRemoteDeviceService]
+ -[NPKIDVRemoteDevicesManager noDeviceDidBecomeActive]
+ -[NPKPaymentWebServiceCompanionTargetDevice identityPassesOfTypes:]
+ -[NPKPaymentWebServiceCompanionTargetDevice passesOfCardType:]
+ -[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:passWithUniqueID:]
+ -[NPKQuickPaymentSession contactlessInterfaceSessionDidReceiveTerminalError:]
+ -[NPKTransientAssertion _remoteObjectProxyWithErrorHandler:]
+ -[NPKTransientAssertion dealloc]
+ GCC_except_table100
+ GCC_except_table114
+ GCC_except_table141
+ GCC_except_table142
+ GCC_except_table168
+ GCC_except_table178
+ GCC_except_table184
+ GCC_except_table231
+ GCC_except_table236
+ GCC_except_table257
+ GCC_except_table262
+ GCC_except_table272
+ GCC_except_table277
+ GCC_except_table289
+ GCC_except_table292
+ GCC_except_table296
+ GCC_except_table301
+ GCC_except_table306
+ GCC_except_table310
+ GCC_except_table315
+ GCC_except_table320
+ GCC_except_table326
+ GCC_except_table331
+ GCC_except_table338
+ GCC_except_table345
+ GCC_except_table350
+ GCC_except_table355
+ GCC_except_table360
+ GCC_except_table365
+ GCC_except_table378
+ GCC_except_table379
+ GCC_except_table383
+ GCC_except_table399
+ GCC_except_table405
+ GCC_except_table423
+ GCC_except_table432
+ GCC_except_table434
+ GCC_except_table439
+ GCC_except_table444
+ GCC_except_table455
+ GCC_except_table458
+ GCC_except_table467
+ GCC_except_table474
+ GCC_except_table488
+ GCC_except_table493
+ GCC_except_table504
+ GCC_except_table510
+ GCC_except_table515
+ GCC_except_table520
+ GCC_except_table526
+ GCC_except_table532
+ GCC_except_table545
+ GCC_except_table548
+ GCC_except_table550
+ GCC_except_table562
+ GCC_except_table564
+ GCC_except_table582
+ GCC_except_table588
+ GCC_except_table597
+ GCC_except_table602
+ GCC_except_table607
+ GCC_except_table612
+ GCC_except_table617
+ GCC_except_table622
+ GCC_except_table627
+ GCC_except_table632
+ GCC_except_table637
+ GCC_except_table642
+ GCC_except_table649
+ GCC_except_table656
+ GCC_except_table661
+ GCC_except_table666
+ GCC_except_table687
+ GCC_except_table693
+ GCC_except_table698
+ GCC_except_table703
+ GCC_except_table709
+ GCC_except_table715
+ GCC_except_table722
+ GCC_except_table727
+ GCC_except_table733
+ GCC_except_table738
+ GCC_except_table743
+ GCC_except_table748
+ GCC_except_table753
+ GCC_except_table758
+ GCC_except_table763
+ GCC_except_table768
+ GCC_except_table773
+ GCC_except_table778
+ GCC_except_table783
+ GCC_except_table788
+ GCC_except_table799
+ GCC_except_table801
+ GCC_except_table810
+ GCC_except_table812
+ GCC_except_table821
+ GCC_except_table827
+ GCC_except_table83
+ GCC_except_table834
+ GCC_except_table839
+ GCC_except_table844
+ GCC_except_table849
+ GCC_except_table854
+ GCC_except_table868
+ GCC_except_table879
+ GCC_except_table89
+ GCC_except_table905
+ _OBJC_IVAR_$_NPKDoublePressSuppressionAssertion._isInvalidating
+ _OBJC_IVAR_$_NPKDoublePressSuppressionAssertion._stateLock
+ _OBJC_IVAR_$_NPKIDVRemoteDeviceSession._remoteServiceLock
+ ___100-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:addPaymentPass:withCompletionHandler:]_block_invoke.443
+ ___102-[NPKQuickPaymentSession _internalQueue_updateContactlessSessionForPass:vasPasses:deferAuthorization:]_block_invoke.158
+ ___103-[NPKQuickPaymentSession _sessionQueue_startContactlessSessionWithSuccessfulCompletionOnInternalQueue:]_block_invoke.172
+ ___103-[NPKQuickPaymentSession _sessionQueue_startContactlessSessionWithSuccessfulCompletionOnInternalQueue:]_block_invoke.177
+ ___103-[NPKQuickPaymentSession _sessionQueue_startContactlessSessionWithSuccessfulCompletionOnInternalQueue:]_block_invoke_2.173
+ ___106-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:addSecureElementPass:properties:completion:]_block_invoke.446
+ ___106-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:addSecureElementPass:properties:completion:]_block_invoke.449
+ ___106-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:addSecureElementPass:properties:completion:]_block_invoke.454
+ ___106-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:addSecureElementPass:properties:completion:]_block_invoke.459
+ ___106-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:addSecureElementPass:properties:completion:]_block_invoke_2.456
+ ___107-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:didRegisterWithRegionMap:primaryRegionTopic:]_block_invoke.434
+ ___107-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:passOwnershipTokenWithIdentifier:completion:]_block_invoke.776
+ ___115-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:canAddSecureElementPassWithConfiguration:completion:]_block_invoke.708
+ ___115-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:validateAddBiometricPassPreconditionsWithCompletion:]_block_invoke.382
+ ___120-[NPKQuickPaymentSession contactlessInterfaceSessionDidFail:forPaymentApplications:paymentPass:valueAddedServicePasses:]_block_invoke.185
+ ___123-[NPKQuickPaymentSession contactlessInterfaceSessionDidTimeout:forPaymentApplications:paymentPass:valueAddedServicePasses:]_block_invoke.181
+ ___123-[NPKQuickPaymentSession contactlessInterfaceSessionDidTimeout:forPaymentApplications:paymentPass:valueAddedServicePasses:]_block_invoke.182
+ ___125-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:provisioningDataIncludingDeviceMetadata:withCompletionHandler:]_block_invoke.416
+ ___125-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:provisioningDataIncludingDeviceMetadata:withCompletionHandler:]_block_invoke.417
+ ___137-[NPKPaymentWebServiceCompanionTargetDevice remotePassUpgradeWithRequest:pass:requireAuthorization:notifyUserOnPairedDevice:updateBlock:]_block_invoke.553
+ ___137-[NPKPaymentWebServiceCompanionTargetDevice requestPasscodeUpgradeForPasscodeUpgradeFlowController:withVisibleViewController:completion:]_block_invoke.696
+ ___137-[NPKPaymentWebServiceCompanionTargetDevice requestPasscodeUpgradeForPasscodeUpgradeFlowController:withVisibleViewController:completion:]_block_invoke_2.698
+ ___138-[NPKQuickPaymentSession _sessionQueue_updateContactlessSessionForPass:paymentApplications:vasPasses:sessionConfirmed:deferAuthorization:]_block_invoke.162
+ ___150-[NPKPaymentWebServiceCompanionTargetDevice _singleExpressTransitPassPaymentWebService:handlePotentialExpressPassConfiguration:withCompletionHandler:]_block_invoke.643
+ ___150-[NPKPaymentWebServiceCompanionTargetDevice _singleExpressTransitPassPaymentWebService:handlePotentialExpressPassConfiguration:withCompletionHandler:]_block_invoke.646
+ ___152-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:presentStandaloneTransaction:forPassUniqueIdentifier:terminalReaderIdentifier:completion:]_block_invoke.759
+ ___152-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:presentStandaloneTransaction:forPassUniqueIdentifier:terminalReaderIdentifier:completion:]_block_invoke.762
+ ___152-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:presentStandaloneTransaction:forPassUniqueIdentifier:terminalReaderIdentifier:completion:]_block_invoke.767
+ ___152-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:presentStandaloneTransaction:forPassUniqueIdentifier:terminalReaderIdentifier:completion:]_block_invoke_2.763
+ ___157-[NPKPaymentWebServiceCompanionTargetDevice _multipleExpressTransitPassPaymentWebService:handlePotentialExpressPassConfiguration:pass:withCompletionHandler:]_block_invoke.641
+ ___39-[NPKTransientAssertion initWithQueue:]_block_invoke.120
+ ___40-[NPKQuickPaymentSession setCredential:]_block_invoke.128
+ ___41-[NPKQuickPaymentSession setCurrentPass:]_block_invoke.125
+ ___42-[NPKQuickPaymentSession _handleFieldExit]_block_invoke.216
+ ___43-[NPKQuickPaymentSession _handleFieldEntry]_block_invoke.212
+ ___48-[NPKDoublePressSuppressionAssertion invalidate]_block_invoke
+ ___57-[NPKDoublePressSuppressionAssertion _handleInvalidation]_block_invoke
+ ___60-[NPKTransientAssertion _remoteObjectProxyWithErrorHandler:]_block_invoke
+ ___62-[NPKPaymentWebServiceCompanionTargetDevice passesOfCardType:]_block_invoke
+ ___62-[NPKPaymentWebServiceCompanionTargetDevice passesOfCardType:]_block_invoke_2
+ ___65-[NPKDoublePressSuppressionAssertion _resyncStateWithCompletion:]_block_invoke
+ ___65-[NPKDoublePressSuppressionAssertion _resyncStateWithCompletion:]_block_invoke.186
+ ___65-[NPKQuickPaymentSession _updateSessionWithCredentialAndActivate]_block_invoke.146
+ ___65-[NPKQuickPaymentSessionSource _handleAuthIntentEventFromSource:]_block_invoke.88
+ ___65-[NPKQuickPaymentSessionSource _handleAuthIntentEventFromSource:]_block_invoke.91
+ ___65-[NPKQuickPaymentSessionSource _handleAuthIntentEventFromSource:]_block_invoke.93
+ ___65-[NPKQuickPaymentSessionSource _handleAuthIntentEventFromSource:]_block_invoke.94
+ ___67-[NPKPaymentWebServiceCompanionTargetDevice identityPassesOfTypes:]_block_invoke
+ ___67-[NPKPaymentWebServiceCompanionTargetDevice identityPassesOfTypes:]_block_invoke_2
+ ___69-[NPKPaymentWebServiceCompanionTargetDevice handleCredentialsChange:]_block_invoke.754
+ ___73-[NPKQuickPaymentSession _internalQueue_deactivateSessionWithCompletion:]_block_invoke.149
+ ___73-[NPKQuickPaymentSession _internalQueue_deactivateSessionWithCompletion:]_block_invoke_2.150
+ ___76-[NPKPaymentWebServiceCompanionTargetDevice productsWithRequest:completion:]_block_invoke.622
+ ___77-[NPKQuickPaymentSession contactlessInterfaceSessionDidReceiveTerminalError:]_block_invoke
+ ___78-[NPKPaymentWebServiceCompanionTargetDevice accountWithIdentifier:completion:]_block_invoke.615
+ ___79-[NPKQuickPaymentSession contactlessInterfaceSessionDidReceiveActivityTimeout:]_block_invoke.191
+ ___80-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:passWithUniqueID:]_block_invoke
+ ___85-[NPKQuickPaymentSession contactlessInterfaceSessionDidStartTransaction:withContext:]_block_invoke.186
+ ___90-[NPKPaymentWebServiceCompanionTargetDevice updatedAccountsForProvisioningWithCompletion:]_block_invoke.574
+ ___90-[NPKPaymentWebServiceCompanionTargetDevice updatedAccountsForProvisioningWithCompletion:]_block_invoke.579
+ ___90-[NPKPaymentWebServiceCompanionTargetDevice updatedAccountsForProvisioningWithCompletion:]_block_invoke.581
+ ___90-[NPKPaymentWebServiceCompanionTargetDevice updatedAccountsForProvisioningWithCompletion:]_block_invoke_2.580
+ ___98-[NPKPaymentWebServiceCompanionTargetDevice _canAddSecureElementPassWithConfiguration:completion:]_block_invoke.713
+ ___99-[NPKPaymentWebServiceCompanionTargetDevice handlePendingRemovalOfPaymentPass:uniqueID:completion:]_block_invoke.469
+ ___99-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:deviceMetadataWithFields:completion:]_block_invoke.598
+ ___Block_byref_object_copy_.384
+ ___Block_byref_object_dispose_.385
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSArray"8lr32l8
+ ___block_descriptor_40_e8_32r_e23_v16?0"PKPaymentPass"8lr32l8
+ ___block_literal_global.117
+ ___block_literal_global.124
+ ___block_literal_global.154
+ ___block_literal_global.160
+ ___block_literal_global.164
+ ___block_literal_global.180
+ ___block_literal_global.184
+ ___block_literal_global.436
+ ___block_literal_global.452
+ ___block_literal_global.630
+ ___block_literal_global.638
+ ___block_literal_global.649
+ ___block_literal_global.656
+ ___block_literal_global.662
+ ___block_literal_global.671
+ ___block_literal_global.679
+ ___block_literal_global.683
+ ___block_literal_global.689
+ ___block_literal_global.766
+ _objc_msgSend$_initRemoteDeviceService
+ _objc_msgSend$_resyncStateWithCompletion:
+ _objc_msgSend$identityPassesOfTypes:completion:
+ _objc_msgSend$identityPassesOfTypes:withCompletion:
+ _objc_msgSend$passesOfCardType:completion:
+ _objc_msgSend$passesOfCardType:withCompletion:
+ _objc_msgSend$setDoublePressSuppressionRequested:withCompletion:
+ _objc_msgSend$setRemoteService:
- GCC_except_table134
- GCC_except_table139
- GCC_except_table146
- GCC_except_table160
- GCC_except_table165
- GCC_except_table170
- GCC_except_table176
- GCC_except_table210
- GCC_except_table233
- GCC_except_table242
- GCC_except_table249
- GCC_except_table254
- GCC_except_table259
- GCC_except_table264
- GCC_except_table269
- GCC_except_table281
- GCC_except_table284
- GCC_except_table288
- GCC_except_table293
- GCC_except_table298
- GCC_except_table302
- GCC_except_table307
- GCC_except_table312
- GCC_except_table318
- GCC_except_table323
- GCC_except_table330
- GCC_except_table337
- GCC_except_table342
- GCC_except_table347
- GCC_except_table352
- GCC_except_table357
- GCC_except_table370
- GCC_except_table371
- GCC_except_table375
- GCC_except_table391
- GCC_except_table397
- GCC_except_table415
- GCC_except_table424
- GCC_except_table426
- GCC_except_table431
- GCC_except_table436
- GCC_except_table447
- GCC_except_table450
- GCC_except_table459
- GCC_except_table464
- GCC_except_table466
- GCC_except_table485
- GCC_except_table494
- GCC_except_table496
- GCC_except_table507
- GCC_except_table512
- GCC_except_table518
- GCC_except_table524
- GCC_except_table529
- GCC_except_table540
- GCC_except_table542
- GCC_except_table554
- GCC_except_table556
- GCC_except_table566
- GCC_except_table580
- GCC_except_table589
- GCC_except_table594
- GCC_except_table599
- GCC_except_table604
- GCC_except_table609
- GCC_except_table614
- GCC_except_table619
- GCC_except_table624
- GCC_except_table629
- GCC_except_table634
- GCC_except_table641
- GCC_except_table648
- GCC_except_table653
- GCC_except_table658
- GCC_except_table663
- GCC_except_table685
- GCC_except_table690
- GCC_except_table695
- GCC_except_table701
- GCC_except_table707
- GCC_except_table714
- GCC_except_table719
- GCC_except_table725
- GCC_except_table730
- GCC_except_table735
- GCC_except_table740
- GCC_except_table745
- GCC_except_table750
- GCC_except_table755
- GCC_except_table760
- GCC_except_table765
- GCC_except_table770
- GCC_except_table775
- GCC_except_table780
- GCC_except_table785
- GCC_except_table791
- GCC_except_table796
- GCC_except_table802
- GCC_except_table813
- GCC_except_table819
- GCC_except_table826
- GCC_except_table831
- GCC_except_table836
- GCC_except_table84
- GCC_except_table841
- GCC_except_table846
- GCC_except_table852
- GCC_except_table87
- GCC_except_table871
- GCC_except_table897
- GCC_except_table98
- _NPKCashRecurringPaymentsEnabled
- _UIApplicationWillEnterForegroundNotification
- ___100-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:addPaymentPass:withCompletionHandler:]_block_invoke.442
- ___102-[NPKQuickPaymentSession _internalQueue_updateContactlessSessionForPass:vasPasses:deferAuthorization:]_block_invoke.155
- ___103-[NPKQuickPaymentSession _sessionQueue_startContactlessSessionWithSuccessfulCompletionOnInternalQueue:]_block_invoke.166
- ___103-[NPKQuickPaymentSession _sessionQueue_startContactlessSessionWithSuccessfulCompletionOnInternalQueue:]_block_invoke.174
- ___103-[NPKQuickPaymentSession _sessionQueue_startContactlessSessionWithSuccessfulCompletionOnInternalQueue:]_block_invoke_2.170
- ___106-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:addSecureElementPass:properties:completion:]_block_invoke.444
- ___106-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:addSecureElementPass:properties:completion:]_block_invoke.448
- ___106-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:addSecureElementPass:properties:completion:]_block_invoke.452
- ___106-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:addSecureElementPass:properties:completion:]_block_invoke.456
- ___106-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:addSecureElementPass:properties:completion:]_block_invoke_2.455
- ___107-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:didRegisterWithRegionMap:primaryRegionTopic:]_block_invoke.430
- ___107-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:passOwnershipTokenWithIdentifier:completion:]_block_invoke.775
- ___115-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:canAddSecureElementPassWithConfiguration:completion:]_block_invoke.707
- ___115-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:validateAddBiometricPassPreconditionsWithCompletion:]_block_invoke.380
- ___120-[NPKQuickPaymentSession contactlessInterfaceSessionDidFail:forPaymentApplications:paymentPass:valueAddedServicePasses:]_block_invoke.182
- ___123-[NPKQuickPaymentSession contactlessInterfaceSessionDidTimeout:forPaymentApplications:paymentPass:valueAddedServicePasses:]_block_invoke.178
- ___123-[NPKQuickPaymentSession contactlessInterfaceSessionDidTimeout:forPaymentApplications:paymentPass:valueAddedServicePasses:]_block_invoke.179
- ___125-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:provisioningDataIncludingDeviceMetadata:withCompletionHandler:]_block_invoke.412
- ___125-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:provisioningDataIncludingDeviceMetadata:withCompletionHandler:]_block_invoke.415
- ___137-[NPKPaymentWebServiceCompanionTargetDevice remotePassUpgradeWithRequest:pass:requireAuthorization:notifyUserOnPairedDevice:updateBlock:]_block_invoke.552
- ___137-[NPKPaymentWebServiceCompanionTargetDevice requestPasscodeUpgradeForPasscodeUpgradeFlowController:withVisibleViewController:completion:]_block_invoke.695
- ___137-[NPKPaymentWebServiceCompanionTargetDevice requestPasscodeUpgradeForPasscodeUpgradeFlowController:withVisibleViewController:completion:]_block_invoke_2.697
- ___138-[NPKQuickPaymentSession _sessionQueue_updateContactlessSessionForPass:paymentApplications:vasPasses:sessionConfirmed:deferAuthorization:]_block_invoke.159
- ___150-[NPKPaymentWebServiceCompanionTargetDevice _singleExpressTransitPassPaymentWebService:handlePotentialExpressPassConfiguration:withCompletionHandler:]_block_invoke.642
- ___150-[NPKPaymentWebServiceCompanionTargetDevice _singleExpressTransitPassPaymentWebService:handlePotentialExpressPassConfiguration:withCompletionHandler:]_block_invoke.645
- ___152-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:presentStandaloneTransaction:forPassUniqueIdentifier:terminalReaderIdentifier:completion:]_block_invoke.758
- ___152-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:presentStandaloneTransaction:forPassUniqueIdentifier:terminalReaderIdentifier:completion:]_block_invoke.760
- ___152-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:presentStandaloneTransaction:forPassUniqueIdentifier:terminalReaderIdentifier:completion:]_block_invoke.766
- ___152-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:presentStandaloneTransaction:forPassUniqueIdentifier:terminalReaderIdentifier:completion:]_block_invoke_2.762
- ___157-[NPKPaymentWebServiceCompanionTargetDevice _multipleExpressTransitPassPaymentWebService:handlePotentialExpressPassConfiguration:pass:withCompletionHandler:]_block_invoke.640
- ___39-[NPKTransientAssertion initWithQueue:]_block_invoke.117
- ___40-[NPKQuickPaymentSession setCredential:]_block_invoke.125
- ___41-[NPKQuickPaymentSession setCurrentPass:]_block_invoke.119
- ___42-[NPKQuickPaymentSession _handleFieldExit]_block_invoke.213
- ___43-[NPKQuickPaymentSession _handleFieldEntry]_block_invoke.209
- ___43-[NPKTransientAssertion _remoteObjectProxy]_block_invoke
- ___65-[NPKQuickPaymentSession _updateSessionWithCredentialAndActivate]_block_invoke.140
- ___65-[NPKQuickPaymentSessionSource _handleAuthIntentEventFromSource:]_block_invoke.85
- ___65-[NPKQuickPaymentSessionSource _handleAuthIntentEventFromSource:]_block_invoke.86
- ___65-[NPKQuickPaymentSessionSource _handleAuthIntentEventFromSource:]_block_invoke.87
- ___69-[NPKPaymentWebServiceCompanionTargetDevice handleCredentialsChange:]_block_invoke.753
- ___73-[NPKQuickPaymentSession _internalQueue_deactivateSessionWithCompletion:]_block_invoke.146
- ___73-[NPKQuickPaymentSession _internalQueue_deactivateSessionWithCompletion:]_block_invoke_2.147
- ___76-[NPKPaymentWebServiceCompanionTargetDevice productsWithRequest:completion:]_block_invoke.621
- ___78-[NPKPaymentWebServiceCompanionTargetDevice accountWithIdentifier:completion:]_block_invoke.614
- ___79-[NPKQuickPaymentSession contactlessInterfaceSessionDidReceiveActivityTimeout:]_block_invoke.188
- ___85-[NPKQuickPaymentSession contactlessInterfaceSessionDidStartTransaction:withContext:]_block_invoke.183
- ___90-[NPKPaymentWebServiceCompanionTargetDevice updatedAccountsForProvisioningWithCompletion:]_block_invoke.573
- ___90-[NPKPaymentWebServiceCompanionTargetDevice updatedAccountsForProvisioningWithCompletion:]_block_invoke.578
- ___90-[NPKPaymentWebServiceCompanionTargetDevice updatedAccountsForProvisioningWithCompletion:]_block_invoke.580
- ___90-[NPKPaymentWebServiceCompanionTargetDevice updatedAccountsForProvisioningWithCompletion:]_block_invoke_2.579
- ___98-[NPKPaymentWebServiceCompanionTargetDevice _canAddSecureElementPassWithConfiguration:completion:]_block_invoke.712
- ___99-[NPKPaymentWebServiceCompanionTargetDevice handlePendingRemovalOfPaymentPass:uniqueID:completion:]_block_invoke.468
- ___99-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:deviceMetadataWithFields:completion:]_block_invoke.597
- ___Block_byref_object_copy_.382
- ___Block_byref_object_dispose_.383
- ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
- ___block_literal_global.121
- ___block_literal_global.157
- ___block_literal_global.161
- ___block_literal_global.177
- ___block_literal_global.181
- ___block_literal_global.434
- ___block_literal_global.451
- ___block_literal_global.632
- ___block_literal_global.640
- ___block_literal_global.651
- ___block_literal_global.655
- ___block_literal_global.661
- ___block_literal_global.670
- ___block_literal_global.678
- ___block_literal_global.685
- ___block_literal_global.691
- ___block_literal_global.765
- _objc_msgSend$setDoublePressSuppressionRequested:
- _objc_msgSend$setEnabled:
CStrings:
+ "-[NPKCompanionAgentConnection identityPassesOfTypes:completion:]"
+ "-[NPKCompanionAgentConnection passesOfCardType:completion:]"
+ "Error: %@: Couldn't get remote object proxy. Error: %@"
+ "Error: %@: XPC connection is nil"
+ "Error: Double-press suppression assertion: XPC error during state sync: %@"
+ "NPKQuickPaymentSessionCompletionReasonTerminalError"
+ "Notice: %@ Declining to handle button event. System state lock (sleep mode, water lock, school mode, etc) in effect"
+ "Notice: Double-press suppression assertion: Server confirmed state change"
+ "Notice: Double-press suppression assertion: Suppression disabled locally due to interruption."
+ "Notice: Double-press suppression assertion: Suppression disabled on server after invalidation."
+ "Notice: Double-press suppression assertion: connection interrupted during invalidation; suppression disabled"
+ "Notice: Double-press suppression assertion: connection interrupted; disabling suppression locally."
+ "Notice: Double-press suppression assertion: connection invalidated during invalidation; suppression disabled"
+ "Notice: Double-press suppression assertion: connection invalidated; disabling suppression on server."
+ "Notice: Double-press suppression assertion: invalidation already in progress, ignoring duplicate call"
+ "Notice: Double-press suppression assertion: resyncing state (suppression: %@) with completion %@"
+ "Notice: Double-press suppression assertion: state sync completed, proceeding with invalidation"
+ "Notice: NPKIDVRemoteDeviceService: Handling Device did become active"
+ "Notice: NPKIDVRemoteDeviceService: Handling No Device did become active"
+ "Notice: Quick payment session: contactlessInterfaceSessionDidReceiveTerminalError: %@"
+ "SystemStateLocked"
+ "XPC connection is nil"
+ "_initRemoteDeviceService"
+ "_isInvalidating"
+ "_remoteServiceLock"
+ "_resyncStateWithCompletion:"
+ "_stateLock"
+ "identityPassesOfTypes:completion:"
+ "identityPassesOfTypes:withCompletion:"
+ "noDeviceDidBecomeActive"
+ "passesOfCardType:completion:"
+ "passesOfCardType:withCompletion:"
+ "setDoublePressSuppressionRequested:withCompletion:"
+ "v28@0:8B16@?<v@?>20"
+ "v32@0:8@\"NSSet\"16@?<v@?@\"NSArray\">24"
+ "v32@0:8q16@?<v@?@\"NSArray\">24"
- "Notice: Double-press suppression assertion: resyncing state"
- "Notice: NPKIDVRemoteDeviceService: Handling Device did become activate"
- "cash_recurring_payments"

```
