## Sharing

> `/System/Library/PrivateFrameworks/Sharing.framework/Versions/A/Sharing`

```diff

-1960.10.4.0.0
-  __TEXT.__text: 0x3084c8
-  __TEXT.__auth_stubs: 0x4390
-  __TEXT.__objc_methlist: 0xf930
+1962.10.12.1.1
+  __TEXT.__text: 0x30936c
+  __TEXT.__auth_stubs: 0x4380
+  __TEXT.__objc_methlist: 0xf9c0
   __TEXT.__cstring: 0x2a8e5
-  __TEXT.__const: 0x1741c
-  __TEXT.__gcc_except_tab: 0x2fa0
-  __TEXT.__oslogstring: 0x91be
+  __TEXT.__const: 0x1742c
+  __TEXT.__gcc_except_tab: 0x2ff4
+  __TEXT.__oslogstring: 0x92ee
   __TEXT.__dlopen_cstrs: 0x398
   __TEXT.__ustring: 0x18
-  __TEXT.__swift5_typeref: 0x69e3
+  __TEXT.__swift5_typeref: 0x6973
   __TEXT.__constg_swiftt: 0x55b8
   __TEXT.__swift5_reflstr: 0x2cca
-  __TEXT.__swift5_fieldmd: 0x5028
+  __TEXT.__swift5_fieldmd: 0x5034
   __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_assocty: 0xc80
-  __TEXT.__swift5_capture: 0x1cf4
+  __TEXT.__swift5_capture: 0x1cd4
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_proto: 0x15dc
   __TEXT.__swift5_types: 0x6dc
   __TEXT.__swift5_mpenum: 0xa8
-  __TEXT.__unwind_info: 0xb258
-  __TEXT.__eh_frame: 0xa098
+  __TEXT.__unwind_info: 0xb278
+  __TEXT.__eh_frame: 0xa038
   __TEXT.__objc_classname: 0x1b4c
-  __TEXT.__objc_methname: 0x24fe9
-  __TEXT.__objc_methtype: 0x51f1
-  __TEXT.__objc_stubs: 0x13e80
-  __DATA_CONST.__got: 0xfe0
+  __TEXT.__objc_methname: 0x25110
+  __TEXT.__objc_methtype: 0x51bd
+  __TEXT.__objc_stubs: 0x13ec0
+  __DATA_CONST.__got: 0xfd8
   __DATA_CONST.__const: 0x2c28
   __DATA_CONST.__objc_classlist: 0x768
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7890
+  __DATA_CONST.__objc_selrefs: 0x78c0
   __DATA_CONST.__objc_protorefs: 0x198
   __DATA_CONST.__objc_classrefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x500
   __DATA_CONST.__objc_arraydata: 0x2e8
-  __AUTH_CONST.__auth_got: 0x21e0
-  __AUTH_CONST.__auth_ptr: 0xdc8
+  __AUTH_CONST.__auth_got: 0x21d8
+  __AUTH_CONST.__auth_ptr: 0xde8
   __AUTH_CONST.__const: 0x12e68
   __AUTH_CONST.__cfstring: 0x10ba0
-  __AUTH_CONST.__objc_const: 0x32190
+  __AUTH_CONST.__objc_const: 0x32280
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x5e50
+  __AUTH.__objc_data: 0x5db0
   __AUTH.__data: 0x2758
-  __DATA.__objc_ivar: 0x1efc
-  __DATA.__data: 0xa5a8
+  __DATA.__objc_ivar: 0x1f00
+  __DATA.__data: 0xa598
   __DATA.__bss: 0x2c430
   __DATA.__common: 0x110
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 17192
-  Symbols:   20602
-  CStrings:  6037
+  Functions: 17199
+  Symbols:   20617
+  CStrings:  6038
 
Symbols:
+ -[SFAuthenticationManager disabledAuthenticationSessionWithID:]
+ -[SFAuthenticationManager failedToDisableDeviceForSessionID:error:]
+ -[SFAuthenticationManager isEnabledForType:].cold.1
+ -[SFHeadphoneProduct hasCaseWithoutBattery]
+ -[SFHeadphoneProduct setHasCaseWithoutBattery:]
+ OBJC_IVAR_$_SFHeadphoneProduct._hasCaseWithoutBattery
+ __40-[SFAutoUnlockManager attemptAutoUnlock]_block_invoke.521
+ __40-[SFAutoUnlockManager attemptAutoUnlock]_block_invoke.525
+ __44-[SFAuthenticationManager isEnabledForType:]_block_invoke.368
+ __44-[SFAuthenticationManager isEnabledForType:]_block_invoke.cold.1
+ __44-[SFAuthenticationManager isEnabledForType:]_block_invoke_2.cold.1
+ __46-[SFAutoUnlockManager mockedAttemptAutoUnlock]_block_invoke.500
+ __46-[SFAutoUnlockManager mockedAttemptAutoUnlock]_block_invoke.507
+ __46-[SFAutoUnlockManager mockedAttemptAutoUnlock]_block_invoke.508
+ __59-[SFAutoUnlockManager authPromptInfoWithCompletionHandler:]_block_invoke.625
+ __59-[SFAutoUnlockManager enableAutoUnlockWithDevice:passcode:]_block_invoke.444
+ __59-[SFAutoUnlockManager enableAutoUnlockWithDevice:passcode:]_block_invoke.448
+ __60-[SFAutoUnlockManager autoUnlockStateWithCompletionHandler:]_block_invoke.615
+ __60-[SFAutoUnlockManager autoUnlockStateWithCompletionHandler:]_block_invoke.619
+ __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke.445
+ __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_2.446
+ __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_2.446.cold.1
+ __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_3.447
+ __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_3.447.cold.1
+ __68-[SFAutoUnlockManager disableAutoUnlockForDevice:completionHandler:]_block_invoke.464
+ __70-[SFAutoUnlockManager eligibleAutoUnlockDevicesWithCompletionHandler:]_block_invoke.412
+ __70-[SFAutoUnlockManager eligibleAutoUnlockDevicesWithCompletionHandler:]_block_invoke.420
+ __70-[SFAutoUnlockManager eligibleAutoUnlockDevicesWithCompletionHandler:]_block_invoke_2.416
+ __72-[SFAuthenticationManager listEligibleDevicesForType:completionHandler:]_block_invoke.383
+ __73-[SFAuthenticationManager listCandidateDevicesForType:completionHandler:]_block_invoke.388
+ ___44-[SFAuthenticationManager isEnabledForType:]_block_invoke
+ ___44-[SFAuthenticationManager isEnabledForType:]_block_invoke_2
+ ___63-[SFAuthenticationManager disabledAuthenticationSessionWithID:]_block_invoke
+ ___67-[SFAuthenticationManager failedToDisableDeviceForSessionID:error:]_block_invoke
+ ___block_descriptor_48_e8_32r40r_e27_v24?0"NSSet"8"NSError"16l
+ ___block_descriptor_56_e8_32r40r_e60_v24?0"<SFUnlockProtocol><NSXPCProxyCreating>"8"NSError"16l
+ __block_literal_global.379
+ __block_literal_global.395
+ __block_literal_global.399
+ __block_literal_global.407
+ __block_literal_global.412
+ __block_literal_global.414
+ __block_literal_global.449
+ __block_literal_global.456
+ __block_literal_global.510
+ __block_literal_global.514
+ __block_literal_global.518
+ __block_literal_global.529
+ __block_literal_global.531
+ __block_literal_global.737
+ __block_literal_global.741
+ __block_literal_global.746
+ __block_literal_global.750
+ __block_literal_global.755
+ __block_literal_global.779
+ _objc_msgSend$disableUsingClientProxy:authenticationType:device:sessionID:
+ _objc_msgSend$manager:didDisableAuthenticationForSessionWithID:
+ _objc_msgSend$manager:didFailToDisableDeviceForSessionWithID:error:
+ _objc_msgSend$setHasCaseWithoutBattery:
+ block_copy_helper.63
+ block_descriptor.65
+ block_destroy_helper.64
- _SFAuthenticationsDynamicStoreEnabledMacUnlockPhonePath
- __40-[SFAutoUnlockManager attemptAutoUnlock]_block_invoke.524
- __40-[SFAutoUnlockManager attemptAutoUnlock]_block_invoke.528
- __46-[SFAutoUnlockManager mockedAttemptAutoUnlock]_block_invoke.503
- __46-[SFAutoUnlockManager mockedAttemptAutoUnlock]_block_invoke.510
- __46-[SFAutoUnlockManager mockedAttemptAutoUnlock]_block_invoke.511
- __59-[SFAutoUnlockManager authPromptInfoWithCompletionHandler:]_block_invoke.628
- __59-[SFAutoUnlockManager enableAutoUnlockWithDevice:passcode:]_block_invoke.447
- __59-[SFAutoUnlockManager enableAutoUnlockWithDevice:passcode:]_block_invoke.454
- __60-[SFAutoUnlockManager autoUnlockStateWithCompletionHandler:]_block_invoke.618
- __60-[SFAutoUnlockManager autoUnlockStateWithCompletionHandler:]_block_invoke.622
- __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke.433
- __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_2.434
- __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_2.434.cold.1
- __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_3.435
- __67-[SFAuthenticationManager receivedApproveRequestForSessionID:info:]_block_invoke_3.435.cold.1
- __68-[SFAutoUnlockManager disableAutoUnlockForDevice:completionHandler:]_block_invoke.467
- __70-[SFAutoUnlockManager eligibleAutoUnlockDevicesWithCompletionHandler:]_block_invoke.418
- __70-[SFAutoUnlockManager eligibleAutoUnlockDevicesWithCompletionHandler:]_block_invoke.423
- __70-[SFAutoUnlockManager eligibleAutoUnlockDevicesWithCompletionHandler:]_block_invoke_2.419
- __72-[SFAuthenticationManager listEligibleDevicesForType:completionHandler:]_block_invoke.371
- __73-[SFAuthenticationManager listCandidateDevicesForType:completionHandler:]_block_invoke.378
- ___block_descriptor_56_e8_32s40s_e60_v24?0"<SFUnlockProtocol><NSXPCProxyCreating>"8"NSError"16l
- __block_literal_global.377
- __block_literal_global.385
- __block_literal_global.389
- __block_literal_global.392
- __block_literal_global.394
- __block_literal_global.425
- __block_literal_global.459
- __block_literal_global.513
- __block_literal_global.517
- __block_literal_global.521
- __block_literal_global.532
- __block_literal_global.534
- __block_literal_global.736
- __block_literal_global.740
- __block_literal_global.745
- __block_literal_global.749
- __block_literal_global.754
- __block_literal_global.780
- _objc_msgSend$checkDynamicStoreForType:
- _objc_msgSend$disableWithAuthenticationType:device:sessionID:
- _symbolic ___________pSg______pSg__________AA______pIegHgggggozo_ 10Foundation4DataV 7Sharing36_SFXPCAsyncSequenceContainerProtocolP AD011_SFXPCBlockfG0P AD01_deF0C AD01_hF0C s5ErrorP
- _symbolic ___________pSg______pSg__________AA______pIeggggggozo_ 10Foundation4DataV 7Sharing36_SFXPCAsyncSequenceContainerProtocolP AD011_SFXPCBlockfG0P AD01_deF0C AD01_hF0C s5ErrorP
- block_copy_helper.66
- block_descriptor.68
- block_destroy_helper.67
CStrings:
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/Date+Additions.swift"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFAirDrop.TransferIdentifier.swift"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFAirDropClient.swift"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFAirDropUserDefaults.swift"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFCodableCGImage.swift"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFCommon.swift"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFProgressTask.swift"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFSecurityScopedURL.swift"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFUserDefaults.swift"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFClientIdentity.swift"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFXPCAsyncSequence.swift"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFXPCBlock.swift"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFXPCConnection.swift"
+ "/AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFXPCListener.swift"
+ "SFAuthenticationErrorNetworkNotConnected"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFTokenBucket.m:142 : Don't use init on SFTokenBucketWithDups"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/96985a0d-388b-11ef-a93f-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFTokenBucket.m:25 : Don't use init on SFTokenBucket"
+ "iOSWiFiSetup"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/Date+Additions.swift"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFAirDrop.TransferIdentifier.swift"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFAirDropClient.swift"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFAirDropUserDefaults.swift"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFCodableCGImage.swift"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFCommon.swift"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFProgressTask.swift"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFSecurityScopedURL.swift"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFUserDefaults.swift"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFClientIdentity.swift"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFXPCAsyncSequence.swift"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFXPCBlock.swift"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFXPCConnection.swift"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/XPC/SFXPCListener.swift"
- "Unimplemented at /AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFTokenBucket.m:142 : Don't use init on SFTokenBucketWithDups"
- "Unimplemented at /AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Sharing/Framework/SFTokenBucket.m:25 : Don't use init on SFTokenBucket"
- "com.apple.sharing:/Authentications/MacUnlockPhone/Enabled"

```
