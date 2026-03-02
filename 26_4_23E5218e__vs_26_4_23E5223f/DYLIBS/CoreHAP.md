## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP`

```diff

-1418.5.9.0.1
-  __TEXT.__text: 0x1e7258
+1418.5.13.0.1
+  __TEXT.__text: 0x1e7330
   __TEXT.__auth_stubs: 0x1590
-  __TEXT.__objc_methlist: 0x162e8
+  __TEXT.__objc_methlist: 0x162f0
   __TEXT.__const: 0x770
   __TEXT.__dlopen_cstrs: 0x4e
   __TEXT.__gcc_except_tab: 0x67f0
   __TEXT.__cstring: 0x128d5
-  __TEXT.__oslogstring: 0x210ae
+  __TEXT.__oslogstring: 0x210fd
   __TEXT.__unwind_info: 0x74e0
   __TEXT.__objc_classname: 0x3444
-  __TEXT.__objc_methname: 0x28f62
-  __TEXT.__objc_methtype: 0x94f3
-  __TEXT.__objc_stubs: 0x1a160
+  __TEXT.__objc_methname: 0x28f83
+  __TEXT.__objc_methtype: 0x9512
+  __TEXT.__objc_stubs: 0x1a180
   __DATA_CONST.__got: 0xcf8
   __DATA_CONST.__const: 0x5448
   __DATA_CONST.__objc_classlist: 0xb10
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x348
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7620
+  __DATA_CONST.__objc_selrefs: 0x7628
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x980
   __DATA_CONST.__objc_arraydata: 0x208
   __AUTH_CONST.__auth_got: 0xae0
   __AUTH_CONST.__const: 0x7e0
   __AUTH_CONST.__cfstring: 0xede0
-  __AUTH_CONST.__objc_const: 0x27258
+  __AUTH_CONST.__objc_const: 0x27260
   __AUTH_CONST.__objc_intobj: 0x6f0
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9E3BA91C-0949-3998-B341-7C0E20085758
+  UUID: D5550268-8098-34CA-BB5C-D15F04EEBBA0
   Functions: 8356
-  Symbols:   26944
-  CStrings:  13748
+  Symbols:   26945
+  CStrings:  13751
 
Symbols:
+ __CopyPairingIdentityDelegateCallback_f.17290
+ __CopyPairingIdentityDelegateCallback_f.24253
+ __CopyPairingIdentityDelegateCallback_f.3062
+ __FindPairedPeerDelegateCallback_f.3061
+ __PairSetupPromptForSetupCodeDelegateCallback_f.24255
+ __SavePairedPeerDelegateCallback_f.17282
+ __SavePairedPeerDelegateCallback_f.24249
+ ___103-[_HAPAccessoryServerBTLE100 _handlePairingsReadForCharacteristic:readError:removing:queue:completion:]_block_invoke.336
+ ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke.248
+ ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke.249
+ ___115-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:expiry:queue:completionHandler:]_block_invoke.230
+ ___120-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:expiry:queue:completionHandler:]_block_invoke.186
+ ___41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.480
+ ___44-[HAPAccessoryServerIP _pairVerifyStartWAC:]_block_invoke.106
+ ___45-[HAPAccessoryServerIP _pairSetupContinueWAC]_block_invoke.104
+ ___45-[HAPAccessoryServerIP stopPairingWithError:]_block_invoke.147
+ ___45-[_HAPAccessoryServerBTLE100 _pairSetupStart]_block_invoke.321
+ ___47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.598
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.107
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.110
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.113
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.109
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.112
+ ___48-[HAPAccessoryServerIP startPairingWithRequest:]_block_invoke.145
+ ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.114
+ ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.119
+ ___49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.523
+ ___50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.475
+ ___53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.379
+ ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.513
+ ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.518
+ ___55-[_HAPAccessoryServerBTLE200 authSession:authComplete:]_block_invoke.995
+ ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.507
+ ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.511
+ ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.438
+ ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke_2.439
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.416
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.421
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.422
+ ___59-[_HAPAccessoryServerBTLE200 peripheral:didModifyServices:]_block_invoke.960
+ ___60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.491
+ ___63-[_HAPAccessoryServerBTLE100 _handlePairSetupExchangeWithData:]_block_invoke.322
+ ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke.988
+ ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke_2.991
+ ___64-[_HAPAccessoryServerBTLE200 securitySession:didCloseWithError:]_block_invoke.1013
+ ___65-[HAPAccessoryServerIP _continuePairingAfterAuthPromptWithRetry:]_block_invoke.430
+ ___65-[HAPAccessoryServerIP _httpClientDidCloseConnectionDueToServer:]_block_invoke.384
+ ___75-[_HAPAccessoryServerBTLE100 peripheral:didUpdateValueForDescriptor:error:]_block_invoke.317
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.558
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.559
+ ___79-[HAPAccessoryServerIP _queueListPairingWithCompletionQueue:completionHandler:]_block_invoke.169
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1231
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1233
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1232
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1234
+ ___82-[_HAPAccessoryServerBTLE100 removePairingForCurrentControllerOnQueue:completion:]_block_invoke.344
+ ___82-[_HAPAccessoryServerBTLE100 removePairingForCurrentControllerOnQueue:completion:]_block_invoke.345
+ ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.231
+ ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.239
+ ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.240
+ ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.305
+ ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.306
+ ___86-[HAPAccessoryServerIP _establishSecureConnectionAndFetchAttributeDatabaseWithReason:]_block_invoke.143
+ ___86-[_HAPAccessoryServerBTLE100 _removePairingWithIdentifier:publicKey:queue:completion:]_block_invoke.343
+ ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.241
+ ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.242
+ ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.243
+ ___88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.168
+ ___88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.534
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.189
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.198
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.208
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.209
+ ___89-[_HAPAccessoryServerBTLE100 _addPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.333
+ ___90-[HAPAccessoryServerIP _queueEnableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.170
+ ___90-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.228
+ ___99-[HAPAccessoryServerIP writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.227
+ ___Block_byref_object_copy_.11107
+ ___Block_byref_object_copy_.11506
+ ___Block_byref_object_copy_.12338
+ ___Block_byref_object_copy_.12535
+ ___Block_byref_object_copy_.14447
+ ___Block_byref_object_copy_.15199
+ ___Block_byref_object_copy_.15989
+ ___Block_byref_object_copy_.17194
+ ___Block_byref_object_copy_.18550
+ ___Block_byref_object_copy_.19448
+ ___Block_byref_object_copy_.19668
+ ___Block_byref_object_copy_.20672
+ ___Block_byref_object_copy_.21287
+ ___Block_byref_object_copy_.22412
+ ___Block_byref_object_copy_.23237
+ ___Block_byref_object_copy_.2342
+ ___Block_byref_object_copy_.26249
+ ___Block_byref_object_copy_.27529
+ ___Block_byref_object_copy_.27696
+ ___Block_byref_object_copy_.3012
+ ___Block_byref_object_copy_.4597
+ ___Block_byref_object_copy_.5491
+ ___Block_byref_object_copy_.5785
+ ___Block_byref_object_copy_.6213
+ ___Block_byref_object_copy_.6854
+ ___Block_byref_object_copy_.7039
+ ___Block_byref_object_copy_.7840
+ ___Block_byref_object_copy_.854
+ ___Block_byref_object_copy_.9438
+ ___Block_byref_object_copy_.9781
+ ___Block_byref_object_copy_.9985
+ ___Block_byref_object_dispose_.11108
+ ___Block_byref_object_dispose_.11507
+ ___Block_byref_object_dispose_.12339
+ ___Block_byref_object_dispose_.12536
+ ___Block_byref_object_dispose_.14448
+ ___Block_byref_object_dispose_.15200
+ ___Block_byref_object_dispose_.15990
+ ___Block_byref_object_dispose_.17195
+ ___Block_byref_object_dispose_.18551
+ ___Block_byref_object_dispose_.19449
+ ___Block_byref_object_dispose_.19669
+ ___Block_byref_object_dispose_.20673
+ ___Block_byref_object_dispose_.21288
+ ___Block_byref_object_dispose_.22413
+ ___Block_byref_object_dispose_.23238
+ ___Block_byref_object_dispose_.2343
+ ___Block_byref_object_dispose_.26250
+ ___Block_byref_object_dispose_.27530
+ ___Block_byref_object_dispose_.27697
+ ___Block_byref_object_dispose_.3013
+ ___Block_byref_object_dispose_.4598
+ ___Block_byref_object_dispose_.5492
+ ___Block_byref_object_dispose_.5786
+ ___Block_byref_object_dispose_.6214
+ ___Block_byref_object_dispose_.6855
+ ___Block_byref_object_dispose_.7040
+ ___Block_byref_object_dispose_.7841
+ ___Block_byref_object_dispose_.855
+ ___Block_byref_object_dispose_.9439
+ ___Block_byref_object_dispose_.9782
+ ___Block_byref_object_dispose_.9986
+ ___block_literal_global.10130
+ ___block_literal_global.1022
+ ___block_literal_global.10776
+ ___block_literal_global.11562
+ ___block_literal_global.12334
+ ___block_literal_global.1250
+ ___block_literal_global.12706
+ ___block_literal_global.1287
+ ___block_literal_global.14736
+ ___block_literal_global.1518
+ ___block_literal_global.17311
+ ___block_literal_global.177
+ ___block_literal_global.17738
+ ___block_literal_global.19101
+ ___block_literal_global.19458
+ ___block_literal_global.20826
+ ___block_literal_global.22155
+ ___block_literal_global.22434
+ ___block_literal_global.2248
+ ___block_literal_global.22890
+ ___block_literal_global.23842
+ ___block_literal_global.25284
+ ___block_literal_global.25623
+ ___block_literal_global.27302
+ ___block_literal_global.27925
+ ___block_literal_global.3077
+ ___block_literal_global.4037
+ ___block_literal_global.5579
+ ___block_literal_global.5781
+ ___block_literal_global.6334
+ ___block_literal_global.6865
+ ___block_literal_global.7013
+ ___block_literal_global.8157
+ ___block_literal_global.905
+ ___block_literal_global.9067
+ ___block_literal_global.9537
+ _hkConfig.23826
+ _logCategory._hmf_once_t436
+ _logCategory._hmf_once_v437
+ _objc_msgSend$accessoryServerHasActiveClients:
+ _sharedInstance.onceToken.17737
- __CopyPairingIdentityDelegateCallback_f.17267
- __CopyPairingIdentityDelegateCallback_f.24247
- __CopyPairingIdentityDelegateCallback_f.3023
- __FindPairedPeerDelegateCallback_f.3022
- __PairSetupPromptForSetupCodeDelegateCallback_f.24249
- __SavePairedPeerDelegateCallback_f.17259
- __SavePairedPeerDelegateCallback_f.24243
- ___103-[_HAPAccessoryServerBTLE100 _handlePairingsReadForCharacteristic:readError:removing:queue:completion:]_block_invoke.334
- ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke.246
- ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke.247
- ___115-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:expiry:queue:completionHandler:]_block_invoke.228
- ___120-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:expiry:queue:completionHandler:]_block_invoke.184
- ___41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.478
- ___44-[HAPAccessoryServerIP _pairVerifyStartWAC:]_block_invoke.104
- ___45-[HAPAccessoryServerIP _pairSetupContinueWAC]_block_invoke.102
- ___45-[HAPAccessoryServerIP stopPairingWithError:]_block_invoke.145
- ___45-[_HAPAccessoryServerBTLE100 _pairSetupStart]_block_invoke.319
- ___47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.595
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.105
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.106
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.109
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.107
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.110
- ___48-[HAPAccessoryServerIP startPairingWithRequest:]_block_invoke.143
- ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.112
- ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.117
- ___49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.521
- ___50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.473
- ___53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.377
- ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.511
- ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.516
- ___55-[_HAPAccessoryServerBTLE200 authSession:authComplete:]_block_invoke.993
- ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.505
- ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.509
- ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.436
- ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke_2.437
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.414
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.419
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.420
- ___59-[_HAPAccessoryServerBTLE200 peripheral:didModifyServices:]_block_invoke.958
- ___60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.489
- ___63-[_HAPAccessoryServerBTLE100 _handlePairSetupExchangeWithData:]_block_invoke.320
- ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke.986
- ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke_2.989
- ___64-[_HAPAccessoryServerBTLE200 securitySession:didCloseWithError:]_block_invoke.1011
- ___65-[HAPAccessoryServerIP _continuePairingAfterAuthPromptWithRetry:]_block_invoke.428
- ___65-[HAPAccessoryServerIP _httpClientDidCloseConnectionDueToServer:]_block_invoke.382
- ___75-[_HAPAccessoryServerBTLE100 peripheral:didUpdateValueForDescriptor:error:]_block_invoke.315
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.554
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.555
- ___79-[HAPAccessoryServerIP _queueListPairingWithCompletionQueue:completionHandler:]_block_invoke.167
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1227
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1228
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1229
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1231
- ___82-[_HAPAccessoryServerBTLE100 removePairingForCurrentControllerOnQueue:completion:]_block_invoke.342
- ___82-[_HAPAccessoryServerBTLE100 removePairingForCurrentControllerOnQueue:completion:]_block_invoke.343
- ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.229
- ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.237
- ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.238
- ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.303
- ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.304
- ___86-[HAPAccessoryServerIP _establishSecureConnectionAndFetchAttributeDatabaseWithReason:]_block_invoke.141
- ___86-[_HAPAccessoryServerBTLE100 _removePairingWithIdentifier:publicKey:queue:completion:]_block_invoke.341
- ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.239
- ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.240
- ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.241
- ___88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.166
- ___88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.532
- ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.185
- ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.196
- ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.206
- ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.207
- ___89-[_HAPAccessoryServerBTLE100 _addPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.331
- ___90-[HAPAccessoryServerIP _queueEnableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.168
- ___90-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.226
- ___99-[HAPAccessoryServerIP writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.225
- ___Block_byref_object_copy_.11080
- ___Block_byref_object_copy_.11477
- ___Block_byref_object_copy_.12308
- ___Block_byref_object_copy_.12505
- ___Block_byref_object_copy_.14415
- ___Block_byref_object_copy_.15168
- ___Block_byref_object_copy_.15957
- ___Block_byref_object_copy_.17168
- ___Block_byref_object_copy_.18530
- ___Block_byref_object_copy_.19434
- ___Block_byref_object_copy_.19654
- ___Block_byref_object_copy_.20661
- ___Block_byref_object_copy_.21280
- ___Block_byref_object_copy_.22409
- ___Block_byref_object_copy_.2303
- ___Block_byref_object_copy_.23229
- ___Block_byref_object_copy_.26244
- ___Block_byref_object_copy_.27524
- ___Block_byref_object_copy_.27691
- ___Block_byref_object_copy_.2973
- ___Block_byref_object_copy_.4554
- ___Block_byref_object_copy_.5441
- ___Block_byref_object_copy_.5738
- ___Block_byref_object_copy_.6168
- ___Block_byref_object_copy_.6823
- ___Block_byref_object_copy_.7008
- ___Block_byref_object_copy_.7807
- ___Block_byref_object_copy_.850
- ___Block_byref_object_copy_.9411
- ___Block_byref_object_copy_.9754
- ___Block_byref_object_copy_.9958
- ___Block_byref_object_dispose_.11081
- ___Block_byref_object_dispose_.11478
- ___Block_byref_object_dispose_.12309
- ___Block_byref_object_dispose_.12506
- ___Block_byref_object_dispose_.14416
- ___Block_byref_object_dispose_.15169
- ___Block_byref_object_dispose_.15958
- ___Block_byref_object_dispose_.17169
- ___Block_byref_object_dispose_.18531
- ___Block_byref_object_dispose_.19435
- ___Block_byref_object_dispose_.19655
- ___Block_byref_object_dispose_.20662
- ___Block_byref_object_dispose_.21281
- ___Block_byref_object_dispose_.22410
- ___Block_byref_object_dispose_.2304
- ___Block_byref_object_dispose_.23230
- ___Block_byref_object_dispose_.26245
- ___Block_byref_object_dispose_.27525
- ___Block_byref_object_dispose_.27692
- ___Block_byref_object_dispose_.2974
- ___Block_byref_object_dispose_.4555
- ___Block_byref_object_dispose_.5442
- ___Block_byref_object_dispose_.5739
- ___Block_byref_object_dispose_.6169
- ___Block_byref_object_dispose_.6824
- ___Block_byref_object_dispose_.7009
- ___Block_byref_object_dispose_.7808
- ___Block_byref_object_dispose_.851
- ___Block_byref_object_dispose_.9412
- ___Block_byref_object_dispose_.9755
- ___Block_byref_object_dispose_.9959
- ___block_literal_global.10103
- ___block_literal_global.1020
- ___block_literal_global.10749
- ___block_literal_global.11531
- ___block_literal_global.12304
- ___block_literal_global.1247
- ___block_literal_global.12674
- ___block_literal_global.1284
- ___block_literal_global.14705
- ___block_literal_global.1516
- ___block_literal_global.17288
- ___block_literal_global.175
- ___block_literal_global.17718
- ___block_literal_global.19087
- ___block_literal_global.19444
- ___block_literal_global.20819
- ___block_literal_global.2208
- ___block_literal_global.22152
- ___block_literal_global.22431
- ___block_literal_global.22882
- ___block_literal_global.23835
- ___block_literal_global.25279
- ___block_literal_global.25618
- ___block_literal_global.27297
- ___block_literal_global.27920
- ___block_literal_global.3038
- ___block_literal_global.3995
- ___block_literal_global.5523
- ___block_literal_global.5734
- ___block_literal_global.6289
- ___block_literal_global.6834
- ___block_literal_global.6982
- ___block_literal_global.8122
- ___block_literal_global.902
- ___block_literal_global.9036
- ___block_literal_global.9510
- _hkConfig.23819
- _logCategory._hmf_once_t435
- _logCategory._hmf_once_v436
- _sharedInstance.onceToken.17717
Functions:
~ -[HAPAccessoryServerIP _shouldConnectBasedOnDisconnectOnIdle] : 276 -> 492
CStrings:
+ "%{public}@Active clients exist, allowing connection despite disconnect-on-idle"
+ "B24@0:8@\"HAPAccessoryServer\"16"
+ "accessoryServerHasActiveClients:"

```
