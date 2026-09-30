## NanoPassKit

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit`

```diff

-1261.0.0.0.0
-  __TEXT.__text: 0x24dedc
-  __TEXT.__auth_stubs: 0x1e50
-  __TEXT.__objc_methlist: 0x25338
-  __TEXT.__cstring: 0x173c8
-  __TEXT.__const: 0xcf4
-  __TEXT.__oslogstring: 0x2be17
-  __TEXT.__gcc_except_tab: 0x6bbc
+1265.0.0.0.0
+  __TEXT.__text: 0x24f758
+  __TEXT.__auth_stubs: 0x1e80
+  __TEXT.__objc_methlist: 0x25400
+  __TEXT.__cstring: 0x174d8
+  __TEXT.__const: 0xd34
+  __TEXT.__oslogstring: 0x2c097
+  __TEXT.__gcc_except_tab: 0x6de4
   __TEXT.__dlopen_cstrs: 0x260
   __TEXT.__ustring: 0x160
-  __TEXT.__constg_swiftt: 0x258
-  __TEXT.__swift5_typeref: 0x28d
+  __TEXT.__constg_swiftt: 0x294
+  __TEXT.__swift5_typeref: 0x2af
   __TEXT.__swift5_reflstr: 0x104
-  __TEXT.__swift5_fieldmd: 0x194
-  __TEXT.__swift5_types: 0x34
-  __TEXT.__swift5_capture: 0x16c
+  __TEXT.__swift5_fieldmd: 0x1b0
+  __TEXT.__swift5_types: 0x38
+  __TEXT.__swift5_capture: 0x17c
   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__unwind_info: 0x8ca0
-  __TEXT.__eh_frame: 0x350
+  __TEXT.__unwind_info: 0x8d48
+  __TEXT.__eh_frame: 0x378
   __TEXT.__objc_classname: 0x6a59
-  __TEXT.__objc_methname: 0x3efa5
-  __TEXT.__objc_methtype: 0x9f64
-  __TEXT.__objc_stubs: 0x217c0
-  __DATA_CONST.__got: 0x1e38
-  __DATA_CONST.__const: 0x6a70
-  __DATA_CONST.__objc_classlist: 0x11c8
+  __TEXT.__objc_methname: 0x3f1f1
+  __TEXT.__objc_methtype: 0x9fa7
+  __TEXT.__objc_stubs: 0x218c0
+  __DATA_CONST.__got: 0x1e40
+  __DATA_CONST.__const: 0x6ae0
+  __DATA_CONST.__objc_classlist: 0x11d0
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc720
-  __DATA_CONST.__objc_protorefs: 0x90
+  __DATA_CONST.__objc_selrefs: 0xc780
+  __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x1100
   __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__auth_got: 0xf38
-  __AUTH_CONST.__const: 0x1648
-  __AUTH_CONST.__cfstring: 0xe640
-  __AUTH_CONST.__objc_const: 0x44f08
+  __AUTH_CONST.__auth_got: 0xf50
+  __AUTH_CONST.__const: 0x1670
+  __AUTH_CONST.__cfstring: 0xe680
+  __AUTH_CONST.__objc_const: 0x450d8
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0xb140
-  __AUTH.__data: 0x1a8
-  __DATA.__objc_ivar: 0x1c0c
-  __DATA.__data: 0x1ee0
+  __AUTH.__objc_data: 0xb200
+  __AUTH.__data: 0x1d0
+  __DATA.__objc_ivar: 0x1c1c
+  __DATA.__data: 0x1ee8
   __DATA.__bss: 0x1200
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7EF8943D-3E9D-303D-B8E7-A98C99372908
-  Functions: 14294
-  Symbols:   41938
-  CStrings:  16822
+  UUID: D938FBAC-2794-3699-97D9-552E600AB937
+  Functions: 14331
+  Symbols:   42024
+  CStrings:  16859
 
Symbols:
+ -[NPKButtonListener _queue_notifyButtonEventFromSource:]
+ -[NPKButtonListener registerObserver:]
+ -[NPKButtonListener unregisterObserver:]
+ -[NPKCompanionAgentConnection hasPaymentPassWithUniqueID:synchronous:reply:]
+ -[NPKGizmoDatabase _hasPassForUniqueIDLocked:]
+ -[NPKGizmoDatabase hasPassForUniqueID:]
+ -[NPKGizmoDatabase selectPassExistsStatement]
+ -[NPKPassesManager _loadContentAndImageSetsForAllPassesIfNecessaryWithCompletion:]
+ -[NPKPassesManager _loadContentAndImageSetsIfNecessaryForPasses:completion:]
+ -[NPKPaymentWebServiceCompanionTargetDevice carKeyAcceptInvitationWithInvitationIdentifier:activationCode:analyticsUpdateConfig:completion:]
+ -[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:hasPassWithUniqueID:]
+ -[NPKProtoCarKeyAcceptInvitationRequest analyticsUpdateConfigData]
+ -[NPKProtoCarKeyAcceptInvitationRequest hasAnalyticsUpdateConfigData]
+ -[NPKProtoCarKeyAcceptInvitationRequest setAnalyticsUpdateConfigData:]
+ GCC_except_table106
+ GCC_except_table120
+ GCC_except_table134
+ GCC_except_table135
+ GCC_except_table145
+ GCC_except_table146
+ GCC_except_table155
+ GCC_except_table160
+ GCC_except_table165
+ GCC_except_table170
+ GCC_except_table176
+ GCC_except_table183
+ GCC_except_table185
+ GCC_except_table187
+ GCC_except_table193
+ GCC_except_table199
+ GCC_except_table201
+ GCC_except_table203
+ GCC_except_table205
+ GCC_except_table207
+ GCC_except_table209
+ GCC_except_table213
+ GCC_except_table215
+ GCC_except_table217
+ GCC_except_table219
+ GCC_except_table227
+ GCC_except_table228
+ GCC_except_table229
+ GCC_except_table233
+ GCC_except_table241
+ GCC_except_table246
+ GCC_except_table249
+ GCC_except_table254
+ GCC_except_table259
+ GCC_except_table264
+ GCC_except_table269
+ GCC_except_table272
+ GCC_except_table274
+ GCC_except_table281
+ GCC_except_table284
+ GCC_except_table288
+ GCC_except_table293
+ GCC_except_table298
+ GCC_except_table302
+ GCC_except_table307
+ GCC_except_table312
+ GCC_except_table318
+ GCC_except_table323
+ GCC_except_table330
+ GCC_except_table337
+ GCC_except_table342
+ GCC_except_table347
+ GCC_except_table352
+ GCC_except_table357
+ GCC_except_table370
+ GCC_except_table371
+ GCC_except_table375
+ GCC_except_table39
+ GCC_except_table391
+ GCC_except_table397
+ GCC_except_table415
+ GCC_except_table426
+ GCC_except_table43
+ GCC_except_table431
+ GCC_except_table436
+ GCC_except_table447
+ GCC_except_table450
+ GCC_except_table459
+ GCC_except_table466
+ GCC_except_table472
+ GCC_except_table480
+ GCC_except_table485
+ GCC_except_table496
+ GCC_except_table502
+ GCC_except_table507
+ GCC_except_table512
+ GCC_except_table518
+ GCC_except_table524
+ GCC_except_table529
+ GCC_except_table537
+ GCC_except_table542
+ GCC_except_table55
+ GCC_except_table556
+ GCC_except_table566
+ GCC_except_table574
+ GCC_except_table580
+ GCC_except_table589
+ GCC_except_table594
+ GCC_except_table599
+ GCC_except_table604
+ GCC_except_table609
+ GCC_except_table614
+ GCC_except_table619
+ GCC_except_table624
+ GCC_except_table629
+ GCC_except_table634
+ GCC_except_table641
+ GCC_except_table648
+ GCC_except_table653
+ GCC_except_table658
+ GCC_except_table663
+ GCC_except_table671
+ GCC_except_table679
+ GCC_except_table685
+ GCC_except_table690
+ GCC_except_table695
+ GCC_except_table701
+ GCC_except_table707
+ GCC_except_table714
+ GCC_except_table719
+ GCC_except_table725
+ GCC_except_table730
+ GCC_except_table735
+ GCC_except_table740
+ GCC_except_table745
+ GCC_except_table750
+ GCC_except_table755
+ GCC_except_table760
+ GCC_except_table765
+ GCC_except_table770
+ GCC_except_table775
+ GCC_except_table780
+ GCC_except_table785
+ GCC_except_table795
+ GCC_except_table803
+ GCC_except_table812
+ GCC_except_table818
+ GCC_except_table825
+ GCC_except_table830
+ GCC_except_table835
+ GCC_except_table84
+ GCC_except_table840
+ GCC_except_table845
+ GCC_except_table851
+ GCC_except_table859
+ GCC_except_table87
+ GCC_except_table870
+ GCC_except_table896
+ GCC_except_table92
+ GCC_except_table98
+ _NPKPairedOrPairingDeviceSupportsUWB
+ _NPKSupportsUWBForNRDevice
+ _NPKViewAnnotationsEnabled
+ _OBJC_CLASS_$_NPKSemaphoreQueue
+ _OBJC_IVAR_$_NPKAssertionController._semaphoreQueue
+ _OBJC_IVAR_$_NPKButtonListener._observers
+ _OBJC_IVAR_$_NPKGizmoDatabase._selectPassExitsStatement
+ _OBJC_IVAR_$_NPKProtoCarKeyAcceptInvitationRequest._analyticsUpdateConfigData
+ _OBJC_METACLASS_$_NPKSemaphoreQueue
+ __DATA_NPKSemaphoreQueue
+ __INSTANCE_METHODS_NPKSemaphoreQueue
+ __IVARS_NPKSemaphoreQueue
+ __METACLASS_DATA_NPKSemaphoreQueue
+ __OBJC_PROTOCOL_REFERENCE_$_NSSecureCoding
+ ___100-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:addPaymentPass:withCompletionHandler:]_block_invoke.442
+ ___104-[NPKPaymentWebServiceCompanionTargetDevice carKeyDecryptData:credential:ephemeralPublicKey:completion:]_block_invoke.960
+ ___107-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:didRegisterWithRegionMap:primaryRegionTopic:]_block_invoke.430
+ ___107-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:didRegisterWithRegionMap:primaryRegionTopic:]_block_invoke.432
+ ___109-[NPKPaymentWebServiceCompanionTargetDevice carKeyHandleRecipientMessage:forInvitationIdentifier:completion:]_block_invoke.954
+ ___113-[NPKPaymentWebServiceCompanionTargetDevice serviceProviderDataForPassWithUniqueIdentifier:encrypted:completion:]_block_invoke.980
+ ___113-[NPKPaymentWebServiceCompanionTargetDevice serviceProviderDataForPassWithUniqueIdentifier:encrypted:completion:]_block_invoke.982
+ ___115-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:validateAddBiometricPassPreconditionsWithCompletion:]_block_invoke.380
+ ___118-[NPKPaymentWebServiceCompanionTargetDevice cancelAutoTopUpForPassWithUniqueIdentifier:balanceIdentifiers:completion:]_block_invoke.967
+ ___121-[NPKPaymentWebServiceCompanionTargetDevice carKeyRetryActivationCodeWithInvitationIdentifier:activationCode:completion:]_block_invoke.957
+ ___122-[NPKPaymentWebServiceCompanionTargetDevice _trackOutstandingRequestWithMessageIdentifier:completionHandler:errorHandler:]_block_invoke.1035
+ ___125-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:provisioningDataIncludingDeviceMetadata:withCompletionHandler:]_block_invoke.412
+ ___125-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:provisioningDataIncludingDeviceMetadata:withCompletionHandler:]_block_invoke.415
+ ___140-[NPKPaymentWebServiceCompanionTargetDevice carKeyAcceptInvitationWithInvitationIdentifier:activationCode:analyticsUpdateConfig:completion:]_block_invoke
+ ___140-[NPKPaymentWebServiceCompanionTargetDevice carKeyAcceptInvitationWithInvitationIdentifier:activationCode:analyticsUpdateConfig:completion:]_block_invoke.950
+ ___154-[NPKCompanionAgentConnection provisionIdentityPassWithPassMetadata:targetDeviceIdentifier:credentialIdentifier:attestations:supplementalData:completion:]_block_invoke.189
+ ___39-[NPKGizmoDatabase hasPassForUniqueID:]_block_invoke
+ ___41-[NPKGizmoDatabase savePass:isLocalPass:]_block_invoke.456
+ ___46-[NPKGizmoDatabase rebuildDatabaseWithPasses:]_block_invoke.458
+ ___51-[NPKGizmoDatabase restoreBlockForVolatilePassData]_block_invoke.462
+ ___51-[NPKGizmoDatabase restoreBlockForVolatilePassData]_block_invoke_2.463
+ ___56-[NPKButtonListener _queue_notifyButtonEventFromSource:]_block_invoke
+ ___58-[NPKPassesManager group:didInsertPass:withState:atIndex:]_block_invoke_2
+ ___58-[NPKPassesManager group:didUpdatePass:withState:atIndex:]_block_invoke_2
+ ___59-[NPKGizmoDatabase _savePassLocked:locallyAdded:wasUpdate:]_block_invoke.467
+ ___60-[NPKCompanionAgentConnection currentSecureElementSnapshot:]_block_invoke.226
+ ___60-[NPKCompanionAgentConnection passesSynchronous:completion:]_block_invoke.162
+ ___60-[NPKPassesManager groupsController:didInsertGroup:atIndex:]_block_invoke_2
+ ___61-[NPKGizmoDatabase _libraryHashLockedForWatchOSMajorVersion:]_block_invoke.560
+ ___61-[NPKPassesManager group:didUpdatePassState:forPass:atIndex:]_block_invoke_2
+ ___63-[NPKCompanionAgentConnection bridgedClientInfoWithCompletion:]_block_invoke.177
+ ___64-[NPKCompanionAgentConnection reclaimUnusedSecureElementMemory:]_block_invoke.228
+ ___66-[NPKGizmoDatabase setPreferredPaymentApplication:forPaymentPass:]_block_invoke.557
+ ___67-[NPKCompanionAgentConnection countOfPassesSynchronous:completion:]_block_invoke.160
+ ___68-[NPKCompanionAgentConnection savePaymentPass:forDevice:completion:]_block_invoke.153
+ ___69-[NPKGizmoDatabase _setLastAddValueAmountLocked:forPassWithUniqueID:]_block_invoke.471
+ ___69-[NPKGizmoDatabase _setTransitAppletStateLocked:forPassWithUniqueID:]_block_invoke.470
+ ___70-[NPKGizmoDatabase _setPendingAddValueDateLocked:forPassWithUniqueID:]_block_invoke.472
+ ___72-[NPKCompanionAgentConnection updateCredentials:forUniqueID:completion:]_block_invoke.176
+ ___73-[NPKCompanionAgentConnection deviceIDSIdentifierSynchronous:completion:]_block_invoke.164
+ ___73-[NPKCompanionAgentConnection paymentPassWithUniqueID:synchronous:reply:]_block_invoke.142
+ ___73-[NPKCompanionAgentConnection paymentPassWithUniqueID:synchronous:reply:]_block_invoke.143
+ ___74-[NPKCompanionAgentConnection credentialedPassUniqueIDsSynchronous:reply:]_block_invoke.145
+ ___74-[NPKCompanionAgentConnection credentialedPassUniqueIDsSynchronous:reply:]_block_invoke.146
+ ___76-[NPKCompanionAgentConnection hasPaymentPassWithUniqueID:synchronous:reply:]_block_invoke
+ ___76-[NPKCompanionAgentConnection hasPaymentPassWithUniqueID:synchronous:reply:]_block_invoke.138
+ ___76-[NPKCompanionAgentConnection hasPaymentPassWithUniqueID:synchronous:reply:]_block_invoke.139
+ ___76-[NPKCompanionAgentConnection hasPaymentPassWithUniqueID:synchronous:reply:]_block_invoke_2
+ ___76-[NPKCompanionAgentConnection passesWithReaderIdentifier:synchronous:reply:]_block_invoke.144
+ ___76-[NPKPassesManager _loadContentAndImageSetsIfNecessaryForPasses:completion:]_block_invoke
+ ___76-[NPKPassesManager _loadContentAndImageSetsIfNecessaryForPasses:completion:]_block_invoke_2
+ ___76-[NPKPassesManager _loadContentAndImageSetsIfNecessaryForPasses:completion:]_block_invoke_3
+ ___77-[NPKCompanionAgentConnection balanceReminderForBalance:pass:withCompletion:]_block_invoke.168
+ ___77-[NPKCompanionAgentConnection hasActiveExternallySharedPassesWithCompletion:]_block_invoke.174
+ ___77-[NPKCompanionAgentConnection setBalanceReminder:forBalance:pass:completion:]_block_invoke.170
+ ___78-[NPKCompanionAgentConnection expressModeEnabledForPassIdentifier:completion:]_block_invoke.175
+ ___79-[NPKPaymentWebServiceCompanionTargetDevice carKeyRejectInvitation:completion:]_block_invoke.963
+ ___80-[NPKAssertionController _releaseAssertionFromOwnerObject:withDelay:completion:]_block_invoke.59
+ ___82-[NPKCompanionAgentConnection _shouldShowApplePaySettingsForTinkerWithCompletion:]_block_invoke.198
+ ___83-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:hasPassWithUniqueID:]_block_invoke
+ ___85-[NPKCompanionAgentConnection commutePlanReminderForCommutePlan:pass:withCompletion:]_block_invoke.171
+ ___85-[NPKCompanionAgentConnection setCommutePlanReminder:forCommutePlan:pass:completion:]_block_invoke.173
+ ___91-[NPKPaymentWebServiceCompanionTargetDevice hasActiveExternallySharedPassesWithCompletion:]_block_invoke.1032
+ ___92-[NPKCompanionAgentConnection deletePaymentTransactionWithIdentifier:fromDevice:completion:]_block_invoke.166
+ ___93-[NPKPaymentWebServiceCompanionTargetDevice paymentSetupFeaturesForConfiguration:completion:]_block_invoke.994
+ ___96-[NPKCompanionAgentConnection canAddToCompanionPrecheckForegroundConnectivitySynchronous:reply:]_block_invoke.179
+ ___97-[NPKCompanionAgentConnection addPendingProvisionings:identityTargetDeviceIdentifier:completion:]_block_invoke.192
+ ___98-[NPKCompanionAgentConnection beginPairedWatchInstallationOfApplicationForPaymentPass:completion:]_block_invoke.214
+ ___99-[NPKCompanionAgentConnection trustedDeviceEnrollmentSignatureWithAccountDSID:sessionData:handler:]_block_invoke.185
+ ___Block_byref_object_copy_.382
+ ___Block_byref_object_dispose_.383
+ ___NPKPresentUserNotification_block_invoke.297
+ ___NPKUpdateDefaultsForRestrictedModeAndFailForward_block_invoke
+ ___block_descriptor_34_e5_v8?0l
+ ___block_descriptor_48_e8_32s_e37_v16?0"<NPKButtonListenerObserver>"8ls32l8
+ ___block_descriptor_49_e8_32s40bs_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_49_e8_32s40w_e23_v32?0"PKPass"8Q16^B24lw40l8s32l8
+ ___block_descriptor_64_e8_32s40s48s56s_e39_v16?0"<NPKPassesDataSourceObserver>"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___block_literal_global.1022
+ ___block_literal_global.148
+ ___block_literal_global.211
+ ___block_literal_global.216
+ ___block_literal_global.269
+ ___block_literal_global.275
+ ___block_literal_global.281
+ ___block_literal_global.299
+ ___block_literal_global.384
+ ___block_literal_global.422
+ ___block_literal_global.434
+ ___block_literal_global.513
+ ___block_literal_global.515
+ ___block_literal_global.546
+ ___block_literal_global.551
+ ___block_literal_global.632
+ ___block_literal_global.640
+ ___block_literal_global.651
+ ___block_literal_global.685
+ ___block_literal_global.691
+ ___block_literal_global.988
+ _objc_msgSend$_hasPassForUniqueIDLocked:
+ _objc_msgSend$_loadContentAndImageSetsForAllPassesIfNecessaryWithCompletion:
+ _objc_msgSend$_loadContentAndImageSetsIfNecessaryForPasses:completion:
+ _objc_msgSend$_queue_notifyButtonEventFromSource:
+ _objc_msgSend$buttonListener:didReceiveButtonEventFromSource:
+ _objc_msgSend$dispatchSync:
+ _objc_msgSend$hasPaymentPassWithUniqueID:reply:
+ _objc_msgSend$hasPaymentPassWithUniqueID:synchronous:reply:
+ _objc_msgSend$selectPassExistsStatement
+ _objc_msgSend$setAnalyticsUpdateConfigData:
+ _swift_isaMask
+ _symbolic So21OS_dispatch_semaphoreC
+ _symbolic _____ 11NanoPassKit14SemaphoreQueueC
- -[NPKButtonListener _handlerQueue_buttonHandler]
- -[NPKPassesManager _loadImageSetFromPasses:]
- -[NPKPaymentWebServiceCompanionTargetDevice carKeyAcceptInvitationWithInvitationIdentifier:activationCode:completion:]
- GCC_except_table115
- GCC_except_table125
- GCC_except_table132
- GCC_except_table144
- GCC_except_table158
- GCC_except_table163
- GCC_except_table168
- GCC_except_table174
- GCC_except_table184
- GCC_except_table186
- GCC_except_table188
- GCC_except_table190
- GCC_except_table194
- GCC_except_table196
- GCC_except_table198
- GCC_except_table200
- GCC_except_table202
- GCC_except_table204
- GCC_except_table206
- GCC_except_table208
- GCC_except_table212
- GCC_except_table214
- GCC_except_table216
- GCC_except_table220
- GCC_except_table226
- GCC_except_table231
- GCC_except_table236
- GCC_except_table240
- GCC_except_table247
- GCC_except_table252
- GCC_except_table257
- GCC_except_table260
- GCC_except_table262
- GCC_except_table268
- GCC_except_table270
- GCC_except_table279
- GCC_except_table282
- GCC_except_table286
- GCC_except_table291
- GCC_except_table296
- GCC_except_table300
- GCC_except_table305
- GCC_except_table310
- GCC_except_table316
- GCC_except_table321
- GCC_except_table328
- GCC_except_table335
- GCC_except_table340
- GCC_except_table345
- GCC_except_table35
- GCC_except_table350
- GCC_except_table355
- GCC_except_table368
- GCC_except_table369
- GCC_except_table373
- GCC_except_table389
- GCC_except_table395
- GCC_except_table413
- GCC_except_table422
- GCC_except_table429
- GCC_except_table434
- GCC_except_table445
- GCC_except_table448
- GCC_except_table457
- GCC_except_table462
- GCC_except_table470
- GCC_except_table478
- GCC_except_table483
- GCC_except_table492
- GCC_except_table500
- GCC_except_table505
- GCC_except_table510
- GCC_except_table516
- GCC_except_table522
- GCC_except_table527
- GCC_except_table535
- GCC_except_table538
- GCC_except_table552
- GCC_except_table564
- GCC_except_table572
- GCC_except_table578
- GCC_except_table587
- GCC_except_table592
- GCC_except_table597
- GCC_except_table602
- GCC_except_table607
- GCC_except_table612
- GCC_except_table617
- GCC_except_table622
- GCC_except_table627
- GCC_except_table632
- GCC_except_table639
- GCC_except_table646
- GCC_except_table651
- GCC_except_table656
- GCC_except_table661
- GCC_except_table669
- GCC_except_table677
- GCC_except_table683
- GCC_except_table688
- GCC_except_table693
- GCC_except_table699
- GCC_except_table705
- GCC_except_table712
- GCC_except_table717
- GCC_except_table723
- GCC_except_table728
- GCC_except_table733
- GCC_except_table738
- GCC_except_table743
- GCC_except_table748
- GCC_except_table753
- GCC_except_table758
- GCC_except_table763
- GCC_except_table768
- GCC_except_table773
- GCC_except_table778
- GCC_except_table783
- GCC_except_table789
- GCC_except_table799
- GCC_except_table810
- GCC_except_table816
- GCC_except_table82
- GCC_except_table823
- GCC_except_table828
- GCC_except_table833
- GCC_except_table838
- GCC_except_table843
- GCC_except_table849
- GCC_except_table85
- GCC_except_table857
- GCC_except_table868
- GCC_except_table894
- GCC_except_table96
- ___100-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:addPaymentPass:withCompletionHandler:]_block_invoke.441
- ___104-[NPKPaymentWebServiceCompanionTargetDevice carKeyDecryptData:credential:ephemeralPublicKey:completion:]_block_invoke.951
- ___107-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:didRegisterWithRegionMap:primaryRegionTopic:]_block_invoke.429
- ___107-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:didRegisterWithRegionMap:primaryRegionTopic:]_block_invoke.431
- ___109-[NPKPaymentWebServiceCompanionTargetDevice carKeyHandleRecipientMessage:forInvitationIdentifier:completion:]_block_invoke.945
- ___113-[NPKPaymentWebServiceCompanionTargetDevice serviceProviderDataForPassWithUniqueIdentifier:encrypted:completion:]_block_invoke.971
- ___113-[NPKPaymentWebServiceCompanionTargetDevice serviceProviderDataForPassWithUniqueIdentifier:encrypted:completion:]_block_invoke.973
- ___115-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:validateAddBiometricPassPreconditionsWithCompletion:]_block_invoke.379
- ___118-[NPKPaymentWebServiceCompanionTargetDevice cancelAutoTopUpForPassWithUniqueIdentifier:balanceIdentifiers:completion:]_block_invoke.958
- ___118-[NPKPaymentWebServiceCompanionTargetDevice carKeyAcceptInvitationWithInvitationIdentifier:activationCode:completion:]_block_invoke
- ___118-[NPKPaymentWebServiceCompanionTargetDevice carKeyAcceptInvitationWithInvitationIdentifier:activationCode:completion:]_block_invoke.941
- ___121-[NPKPaymentWebServiceCompanionTargetDevice carKeyRetryActivationCodeWithInvitationIdentifier:activationCode:completion:]_block_invoke.948
- ___122-[NPKPaymentWebServiceCompanionTargetDevice _trackOutstandingRequestWithMessageIdentifier:completionHandler:errorHandler:]_block_invoke.1026
- ___125-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:provisioningDataIncludingDeviceMetadata:withCompletionHandler:]_block_invoke.411
- ___125-[NPKPaymentWebServiceCompanionTargetDevice paymentWebService:provisioningDataIncludingDeviceMetadata:withCompletionHandler:]_block_invoke.413
- ___154-[NPKCompanionAgentConnection provisionIdentityPassWithPassMetadata:targetDeviceIdentifier:credentialIdentifier:attestations:supplementalData:completion:]_block_invoke.187
- ___41-[NPKGizmoDatabase savePass:isLocalPass:]_block_invoke.455
- ___44-[NPKPassesManager _loadImageSetFromPasses:]_block_invoke
- ___44-[NPKPassesManager _loadImageSetFromPasses:]_block_invoke_2
- ___44-[NPKPassesManager _loadImageSetFromPasses:]_block_invoke_3
- ___44-[NPKPassesManager _loadImageSetFromPasses:]_block_invoke_4
- ___46-[NPKGizmoDatabase rebuildDatabaseWithPasses:]_block_invoke.457
- ___51-[NPKGizmoDatabase restoreBlockForVolatilePassData]_block_invoke.461
- ___51-[NPKGizmoDatabase restoreBlockForVolatilePassData]_block_invoke_2.462
- ___59-[NPKGizmoDatabase _savePassLocked:locallyAdded:wasUpdate:]_block_invoke.466
- ___60-[NPKCompanionAgentConnection currentSecureElementSnapshot:]_block_invoke.224
- ___60-[NPKCompanionAgentConnection passesSynchronous:completion:]_block_invoke.160
- ___61-[NPKGizmoDatabase _libraryHashLockedForWatchOSMajorVersion:]_block_invoke.559
- ___63-[NPKCompanionAgentConnection bridgedClientInfoWithCompletion:]_block_invoke.175
- ___64-[NPKCompanionAgentConnection reclaimUnusedSecureElementMemory:]_block_invoke.226
- ___66-[NPKGizmoDatabase setPreferredPaymentApplication:forPaymentPass:]_block_invoke.555
- ___67-[NPKCompanionAgentConnection countOfPassesSynchronous:completion:]_block_invoke.158
- ___68-[NPKCompanionAgentConnection savePaymentPass:forDevice:completion:]_block_invoke.149
- ___69-[NPKGizmoDatabase _setLastAddValueAmountLocked:forPassWithUniqueID:]_block_invoke.470
- ___69-[NPKGizmoDatabase _setTransitAppletStateLocked:forPassWithUniqueID:]_block_invoke.469
- ___70-[NPKGizmoDatabase _setPendingAddValueDateLocked:forPassWithUniqueID:]_block_invoke.471
- ___72-[NPKCompanionAgentConnection updateCredentials:forUniqueID:completion:]_block_invoke.174
- ___73-[NPKCompanionAgentConnection deviceIDSIdentifierSynchronous:completion:]_block_invoke.162
- ___73-[NPKCompanionAgentConnection paymentPassWithUniqueID:synchronous:reply:]_block_invoke.138
- ___73-[NPKCompanionAgentConnection paymentPassWithUniqueID:synchronous:reply:]_block_invoke.141
- ___74-[NPKCompanionAgentConnection credentialedPassUniqueIDsSynchronous:reply:]_block_invoke.143
- ___74-[NPKCompanionAgentConnection credentialedPassUniqueIDsSynchronous:reply:]_block_invoke.144
- ___76-[NPKCompanionAgentConnection passesWithReaderIdentifier:synchronous:reply:]_block_invoke.142
- ___77-[NPKCompanionAgentConnection balanceReminderForBalance:pass:withCompletion:]_block_invoke.166
- ___77-[NPKCompanionAgentConnection hasActiveExternallySharedPassesWithCompletion:]_block_invoke.172
- ___77-[NPKCompanionAgentConnection setBalanceReminder:forBalance:pass:completion:]_block_invoke.168
- ___78-[NPKCompanionAgentConnection expressModeEnabledForPassIdentifier:completion:]_block_invoke.173
- ___79-[NPKPaymentWebServiceCompanionTargetDevice carKeyRejectInvitation:completion:]_block_invoke.954
- ___80-[NPKAssertionController _releaseAssertionFromOwnerObject:withDelay:completion:]_block_invoke.58
- ___82-[NPKCompanionAgentConnection _shouldShowApplePaySettingsForTinkerWithCompletion:]_block_invoke.196
- ___85-[NPKCompanionAgentConnection commutePlanReminderForCommutePlan:pass:withCompletion:]_block_invoke.169
- ___85-[NPKCompanionAgentConnection setCommutePlanReminder:forCommutePlan:pass:completion:]_block_invoke.171
- ___91-[NPKPaymentWebServiceCompanionTargetDevice hasActiveExternallySharedPassesWithCompletion:]_block_invoke.1023
- ___92-[NPKCompanionAgentConnection deletePaymentTransactionWithIdentifier:fromDevice:completion:]_block_invoke.164
- ___93-[NPKPaymentWebServiceCompanionTargetDevice paymentSetupFeaturesForConfiguration:completion:]_block_invoke.985
- ___96-[NPKCompanionAgentConnection canAddToCompanionPrecheckForegroundConnectivitySynchronous:reply:]_block_invoke.177
- ___97-[NPKCompanionAgentConnection addPendingProvisionings:identityTargetDeviceIdentifier:completion:]_block_invoke.190
- ___98-[NPKCompanionAgentConnection beginPairedWatchInstallationOfApplicationForPaymentPass:completion:]_block_invoke.212
- ___99-[NPKCompanionAgentConnection trustedDeviceEnrollmentSignatureWithAccountDSID:sessionData:handler:]_block_invoke.183
- ___Block_byref_object_copy_.381
- ___Block_byref_object_dispose_.382
- ___NPKPresentUserNotification_block_invoke.294
- ___block_descriptor_49_e8_32s40s_e23_v32?0"PKPass"8Q16^B24ls32l8s40l8
- ___block_descriptor_49_e8_32s40s_e24_v32?0"PKGroup"8Q16^B24ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e39_v16?0"<NPKPassesDataSourceObserver>"8ls32l8s40l8s48l8
- ___block_literal_global.1013
- ___block_literal_global.146
- ___block_literal_global.208
- ___block_literal_global.213
- ___block_literal_global.266
- ___block_literal_global.272
- ___block_literal_global.278
- ___block_literal_global.296
- ___block_literal_global.381
- ___block_literal_global.419
- ___block_literal_global.433
- ___block_literal_global.510
- ___block_literal_global.512
- ___block_literal_global.543
- ___block_literal_global.548
- ___block_literal_global.628
- ___block_literal_global.636
- ___block_literal_global.647
- ___block_literal_global.681
- ___block_literal_global.687
- ___block_literal_global.979
- _objc_msgSend$_handlerQueue_buttonHandler
- _objc_msgSend$_loadImageSetFromPasses:
CStrings:
+ "-[NPKGizmoDatabase selectPassExistsStatement]"
+ "@\"NPKSemaphoreQueue\""
+ "B32@0:8@\"NSString\"16@?<v@?B>24"
+ "B32@0:8@16@?24"
+ "Error: *** NPKAssertion failure in %{public}s, %{public}s:%ld (reason: Unable to prepare \"select exists pass\" statement)"
+ "Error: Error executing query: %s"
+ "NPKSemaphoreQueue"
+ "NPKUserDefaultViewAnnotationsEnabled"
+ "Notice: NPKCompanionAgentConnection (%@): Reply with has payment pass: %@"
+ "Notice: NPKCompanionAgentConnection (%@): Requesting has payment pass with unique ID: %@ synchronous: %d"
+ "Notice: NPKCompanionAgentConnection (%@): has payment pass: %@"
+ "Notice: Paired device doesn't support UWB; we won't forward standalone transaction events."
+ "Notice: Target device - Request to accept car key invitation with identifier: %{private}@, activation code: %{private}@, analytics update config: %{private}@, completion: %@"
+ "Notice: Target device reset Apple\u00a0Pay manatee view: incoming protobuf %@"
+ "Notice: [PaymentSessionManager] Payment session did ignore exit field notification while on STS_ISO18013 transaction"
+ "SELECT EXISTS (SELECT 1 FROM pass WHERE unique_id = ?);"
+ "T@\"NSData\",&,N,V_analyticsUpdateConfigData"
+ "_analyticsUpdateConfigData"
+ "_hasPassForUniqueIDLocked:"
+ "_loadContentAndImageSetsForAllPassesIfNecessaryWithCompletion:"
+ "_loadContentAndImageSetsIfNecessaryForPasses:completion:"
+ "_queue_notifyButtonEventFromSource:"
+ "_selectPassExitsStatement"
+ "_semaphoreQueue"
+ "analyticsUpdateConfigData"
+ "buttonListener:didReceiveButtonEventFromSource:"
+ "deviceSupportedRadioTechnologiesWithCompletion:"
+ "dispatchSync:"
+ "hasAnalyticsUpdateConfigData"
+ "hasPassForUniqueID:"
+ "hasPaymentPassWithUniqueID:reply:"
+ "hasPaymentPassWithUniqueID:synchronous:reply:"
+ "selectPassExistsStatement"
+ "selectPassExitsStatement"
+ "semaphore"
+ "setAnalyticsUpdateConfigData:"
+ "v16@?0@\"<NPKButtonListenerObserver>\"8"
- "Notice: Target device - Request to accept car key invitation with identifier: %{private}@, activation code: %{private}@, completion: %@"
- "Notice: Target device reset Apple\u00a0Pay manetee view: incoming protobuf %@"
- "_handlerQueue_buttonHandler"
- "_loadImageSetFromPasses:"

```
