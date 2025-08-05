## AssistantServices

> `/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices`

```diff

-3500.113.1.1.1
-  __TEXT.__text: 0x1aebb0
+3500.120.4.0.0
+  __TEXT.__text: 0x1af270
   __TEXT.__auth_stubs: 0x1560
-  __TEXT.__objc_methlist: 0x1dcb4
+  __TEXT.__objc_methlist: 0x1dd04
   __TEXT.__const: 0x488
   __TEXT.__dlopen_cstrs: 0x484
-  __TEXT.__gcc_except_tab: 0x2aec
-  __TEXT.__cstring: 0x3db0e
-  __TEXT.__oslogstring: 0x115b5
+  __TEXT.__gcc_except_tab: 0x2b50
+  __TEXT.__cstring: 0x3dc46
+  __TEXT.__oslogstring: 0x116af
   __TEXT.__ustring: 0x2ac
-  __TEXT.__unwind_info: 0x7da8
+  __TEXT.__unwind_info: 0x7dc8
   __TEXT.__objc_classname: 0x4f80
-  __TEXT.__objc_methname: 0x3b246
-  __TEXT.__objc_methtype: 0xab13
-  __TEXT.__objc_stubs: 0x24680
-  __DATA_CONST.__got: 0x1648
-  __DATA_CONST.__const: 0x83e8
+  __TEXT.__objc_methname: 0x3b3c5
+  __TEXT.__objc_methtype: 0xab6f
+  __TEXT.__objc_stubs: 0x24700
+  __DATA_CONST.__got: 0x1650
+  __DATA_CONST.__const: 0x83f0
   __DATA_CONST.__objc_classlist: 0xde8
   __DATA_CONST.__objc_catlist: 0x2a0
   __DATA_CONST.__objc_protolist: 0x560
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc340
+  __DATA_CONST.__objc_selrefs: 0xc370
   __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0xe00
   __DATA_CONST.__objc_arraydata: 0x20a0
   __AUTH_CONST.__auth_got: 0xac0
   __AUTH_CONST.__const: 0x3ac0
-  __AUTH_CONST.__cfstring: 0x27200
-  __AUTH_CONST.__objc_const: 0x33800
+  __AUTH_CONST.__cfstring: 0x27260
+  __AUTH_CONST.__objc_const: 0x338d0
   __AUTH_CONST.__objc_intobj: 0x2310
   __AUTH_CONST.__objc_dictobj: 0xbb8
   __AUTH_CONST.__objc_arrayobj: 0x5b8
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x7b98
+  __AUTH.__objc_data: 0x7bc0
   __AUTH.__data: 0x288
-  __DATA.__objc_ivar: 0x2550
+  __DATA.__objc_ivar: 0x2564
   __DATA.__data: 0x41c8
-  __DATA.__bss: 0x1300
+  __DATA.__bss: 0x12e0
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0xf78
+  __DATA_DIRTY.__objc_data: 0xf50
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__common: 0xf0
-  __DATA_DIRTY.__bss: 0x1f0
+  __DATA_DIRTY.__bss: 0x210
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 38016A44-B568-3E72-9988-2285D14DCCDA
-  Functions: 11794
-  Symbols:   37546
-  CStrings:  24247
+  UUID: E621AC64-C190-387F-AA6E-EE067F2974B2
+  Functions: 11802
+  Symbols:   37573
+  CStrings:  24273
 
Symbols:
+ -[AFASRSharedUserInfo initWithSharedUserId:loggableSharedUserId:loggableUserIdHash:personaId:]
+ -[AFASRSharedUserInfo loggableUserIdHash]
+ -[AFMultiUserConnection postMessageToMUXWithMultiUserInfo:completion:]
+ -[AFRequestInfo isAlwaysAllowedWhileDeviceLocked]
+ -[AFRequestInfo setIsAlwaysAllowedWhileDeviceLocked:]
+ -[AFSiriAudioRoute isNonAnnounceSupportedWirelessHeadset]
+ -[_AFASRSharedUserInfoMutation getLoggableUserIdHash]
+ -[_AFASRSharedUserInfoMutation setLoggableUserIdHash:]
+ GCC_except_table10121
+ GCC_except_table10124
+ GCC_except_table10133
+ GCC_except_table10159
+ GCC_except_table10180
+ GCC_except_table10373
+ GCC_except_table10434
+ GCC_except_table10440
+ GCC_except_table10443
+ GCC_except_table10449
+ GCC_except_table10453
+ GCC_except_table10459
+ GCC_except_table10734
+ GCC_except_table10902
+ GCC_except_table10915
+ GCC_except_table11103
+ GCC_except_table11242
+ GCC_except_table11255
+ GCC_except_table11293
+ GCC_except_table11551
+ GCC_except_table11695
+ GCC_except_table11714
+ GCC_except_table11717
+ GCC_except_table11719
+ GCC_except_table4768
+ GCC_except_table4834
+ GCC_except_table4897
+ GCC_except_table4907
+ GCC_except_table4918
+ GCC_except_table4931
+ GCC_except_table5056
+ GCC_except_table5410
+ GCC_except_table5413
+ GCC_except_table5480
+ GCC_except_table5481
+ GCC_except_table5495
+ GCC_except_table5496
+ GCC_except_table5502
+ GCC_except_table5540
+ GCC_except_table5546
+ GCC_except_table5552
+ GCC_except_table5626
+ GCC_except_table5661
+ GCC_except_table5664
+ GCC_except_table5798
+ GCC_except_table5897
+ GCC_except_table5920
+ GCC_except_table5990
+ GCC_except_table6004
+ GCC_except_table6010
+ GCC_except_table6133
+ GCC_except_table6140
+ GCC_except_table6495
+ GCC_except_table6510
+ GCC_except_table6517
+ GCC_except_table6533
+ GCC_except_table6636
+ GCC_except_table6645
+ GCC_except_table6684
+ GCC_except_table6716
+ GCC_except_table6786
+ GCC_except_table7262
+ GCC_except_table7265
+ GCC_except_table7268
+ GCC_except_table7271
+ GCC_except_table7274
+ GCC_except_table7484
+ GCC_except_table7486
+ GCC_except_table7498
+ GCC_except_table7571
+ GCC_except_table7577
+ GCC_except_table7747
+ GCC_except_table7853
+ GCC_except_table7883
+ GCC_except_table8077
+ GCC_except_table8141
+ GCC_except_table8247
+ GCC_except_table8676
+ GCC_except_table8730
+ GCC_except_table8774
+ GCC_except_table8862
+ GCC_except_table8902
+ GCC_except_table8939
+ GCC_except_table8943
+ GCC_except_table9189
+ GCC_except_table9259
+ GCC_except_table9265
+ GCC_except_table9300
+ GCC_except_table9303
+ GCC_except_table9381
+ GCC_except_table9410
+ GCC_except_table9482
+ GCC_except_table9485
+ GCC_except_table9489
+ GCC_except_table9594
+ GCC_except_table9598
+ GCC_except_table9602
+ GCC_except_table9635
+ GCC_except_table9680
+ _AnnounceLibrary.sLib.43791
+ _AnnounceLibrary.sOnce.43789
+ _BiomeLibraryLibraryCore.45932
+ _BiomeLibraryLibraryCore.frameworkLibrary.27199
+ _BiomeLibraryLibraryCore.frameworkLibrary.45935
+ _BluetoothManagerLibrary.46027
+ _BluetoothManagerLibraryCore.frameworkLibrary.20479
+ _CoreServicesLibrary.frameworkLibrary.46677
+ _CoreSpeechLibrary.frameworkLibrary.39432
+ _DataCollectionServicesLibrary.sLib.46689
+ _DataCollectionServicesLibrary.sOnce.46688
+ _IntentsLibrary.15271
+ _IntentsLibraryCore.frameworkLibrary.15275
+ _IntentsLibraryCore.frameworkLibrary.31274
+ _LSApplicationProxyFunction.34755
+ _LSApplicationProxyFunction.46683
+ _MediaExperienceLibrary.27650
+ _MediaExperienceLibraryCore.frameworkLibrary.27676
+ _OBJC_CLASS_$_NSRecursiveLock
+ _OBJC_IVAR_$_AFASRSharedUserInfo._loggableUserIdHash
+ _OBJC_IVAR_$_AFRequestInfo._isAlwaysAllowedWhileDeviceLocked
+ _OBJC_IVAR_$_AFSettingsConnection._connectionLock
+ _OBJC_IVAR_$_AFSettingsConnection._connectionSetupComplete
+ _OBJC_IVAR_$__AFASRSharedUserInfoMutation._loggableUserIdHash
+ _SoftBiomeLibrary.45918
+ _VTPreferencesFunction.46889
+ _VoiceTriggerLibrary.frameworkLibrary.46883
+ ___31-[AFSettingsConnection barrier]_block_invoke.58
+ ___35-[AFSettingsConnection _connection]_block_invoke.11
+ ___35-[AFSettingsConnection _connection]_block_invoke_2.12
+ ___40-[AFSettingsConnection configOverrides:]_block_invoke.69
+ ___43-[AFSettingsConnection dumpAssistantState:]_block_invoke.242
+ ___43-[AFSettingsConnection fetchActiveAccount:]_block_invoke.20
+ ___44-[AFSettingsConnection currectNWActivityId:]_block_invoke.143
+ ___47-[AFSettingsConnection startUIRequestWithInfo:]_block_invoke.165
+ ___47-[AFSettingsConnection startUIRequestWithText:]_block_invoke.160
+ ___48-[AFSettingsConnection siriDesignModeIsEnabled:]_block_invoke.235
+ ___50-[AFSettingsConnection areSiriSAEAssetsAvailable:]_block_invoke.241
+ ___56-[AFSettingsConnection isSearchDataSharingStatusForced:]_block_invoke.238
+ ___57-[AFSettingsConnection setIsHomePodInHH2Mode:completion:]_block_invoke.229
+ ___58-[AFSettingsConnection getSearchQueriesDataSharingStatus:]_block_invoke.237
+ ___60-[AFSettingsConnection multiUserCompanionDeviceIdentifiers:]_block_invoke.219
+ ___60-[AFSettingsConnection setSiriDesignModeEnabled:completion:]_block_invoke.234
+ ___60-[AFSettingsConnection(Internal) _handleCommand:completion:]_block_invoke.567
+ ___62-[AFSettingsConnection fetchAccountsSynchronously:completion:]_block_invoke.16
+ ___62-[AFSettingsConnection getCurrentAccessoryInfoWithCompletion:]_block_invoke.150
+ ___62-[AFSettingsConnection getPersonalMultiUserDeviceIdentifiers:]_block_invoke.218
+ ___63-[AFSettingsConnection forceMultiUserSync:download:completion:]_block_invoke.71
+ ___64-[AFSettingsConnection disableAndDeleteCloudSyncWithCompletion:]_block_invoke.61
+ ___64-[AFSettingsConnection shouldSuppressSiriDataSharingOptInAlert:]_block_invoke.232
+ ___65-[AFSettingsConnection setSiriDataSharingOptInStatus:completion:]_block_invoke.224
+ ___68-[AFSettingsConnection deleteSiriHistoryWithContext:withCompletion:]_block_invoke.233
+ ___68-[AFSettingsConnection getSiriDataSharingOptInStatusWithCompletion:]_block_invoke.225
+ ___69-[AFSettingsConnection setSearchQueriesDataSharingStatus:completion:]_block_invoke.236
+ ___70-[AFMultiUserConnection postMessageToMUXWithMultiUserInfo:completion:]_block_invoke
+ ___70-[AFMultiUserConnection postMessageToMUXWithMultiUserInfo:completion:]_block_invoke_2
+ ___73-[AFSettingsConnection setSiriDataSharingOptInAlertPresented:completion:]_block_invoke.227
+ ___77-[AFSettingsConnection _createRadarWithReason:room:process:crash:completion:]_block_invoke.251
+ ___79-[AFSettingsConnection setSiriDataSharingHomePodSetupDeviceIsValid:completion:]_block_invoke.228
+ ___94-[AFASRSharedUserInfo initWithSharedUserId:loggableSharedUserId:loggableUserIdHash:personaId:]_block_invoke
+ ___AnnounceLibrary_block_invoke.43795
+ ___BiomeLibraryLibraryCore_block_invoke.27200
+ ___BiomeLibraryLibraryCore_block_invoke.45936
+ ___Block_byref_object_copy_.10003
+ ___Block_byref_object_copy_.10709
+ ___Block_byref_object_copy_.10902
+ ___Block_byref_object_copy_.11534
+ ___Block_byref_object_copy_.12116
+ ___Block_byref_object_copy_.13383
+ ___Block_byref_object_copy_.13665
+ ___Block_byref_object_copy_.16653
+ ___Block_byref_object_copy_.17182
+ ___Block_byref_object_copy_.17686
+ ___Block_byref_object_copy_.19723
+ ___Block_byref_object_copy_.19964
+ ___Block_byref_object_copy_.20495
+ ___Block_byref_object_copy_.21567
+ ___Block_byref_object_copy_.22518
+ ___Block_byref_object_copy_.23192
+ ___Block_byref_object_copy_.23609
+ ___Block_byref_object_copy_.24218
+ ___Block_byref_object_copy_.26341
+ ___Block_byref_object_copy_.29185
+ ___Block_byref_object_copy_.30856
+ ___Block_byref_object_copy_.35182
+ ___Block_byref_object_copy_.35628
+ ___Block_byref_object_copy_.37854
+ ___Block_byref_object_copy_.39042
+ ___Block_byref_object_copy_.42173
+ ___Block_byref_object_copy_.46821
+ ___Block_byref_object_copy_.48062
+ ___Block_byref_object_copy_.48798
+ ___Block_byref_object_copy_.49080
+ ___Block_byref_object_copy_.8763
+ ___Block_byref_object_dispose_.10004
+ ___Block_byref_object_dispose_.10710
+ ___Block_byref_object_dispose_.10903
+ ___Block_byref_object_dispose_.11535
+ ___Block_byref_object_dispose_.12117
+ ___Block_byref_object_dispose_.13384
+ ___Block_byref_object_dispose_.13666
+ ___Block_byref_object_dispose_.16654
+ ___Block_byref_object_dispose_.17183
+ ___Block_byref_object_dispose_.17687
+ ___Block_byref_object_dispose_.19724
+ ___Block_byref_object_dispose_.19965
+ ___Block_byref_object_dispose_.20496
+ ___Block_byref_object_dispose_.21568
+ ___Block_byref_object_dispose_.22519
+ ___Block_byref_object_dispose_.23193
+ ___Block_byref_object_dispose_.23610
+ ___Block_byref_object_dispose_.24219
+ ___Block_byref_object_dispose_.26342
+ ___Block_byref_object_dispose_.29186
+ ___Block_byref_object_dispose_.30857
+ ___Block_byref_object_dispose_.35183
+ ___Block_byref_object_dispose_.35629
+ ___Block_byref_object_dispose_.37855
+ ___Block_byref_object_dispose_.39043
+ ___Block_byref_object_dispose_.42174
+ ___Block_byref_object_dispose_.46822
+ ___Block_byref_object_dispose_.48063
+ ___Block_byref_object_dispose_.48799
+ ___Block_byref_object_dispose_.49081
+ ___Block_byref_object_dispose_.8764
+ ___BluetoothManagerLibraryCore_block_invoke.20480
+ ___DataCollectionServicesLibrary_block_invoke.46691
+ ___IntentsLibraryCore_block_invoke.15276
+ ___IntentsLibraryCore_block_invoke.31275
+ ___MediaExperienceLibraryCore_block_invoke.27677
+ ___block_descriptor_64_e8_32s40s48s56s_e39_v16?0"<AFASRSharedUserInfoMutating>"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.100
+ ___block_literal_global.101.39154
+ ___block_literal_global.102
+ ___block_literal_global.104.39148
+ ___block_literal_global.10438
+ ___block_literal_global.10495
+ ___block_literal_global.106
+ ___block_literal_global.10647
+ ___block_literal_global.10714
+ ___block_literal_global.108
+ ___block_literal_global.110
+ ___block_literal_global.112.10642
+ ___block_literal_global.112.22633
+ ___block_literal_global.11209
+ ___block_literal_global.114
+ ___block_literal_global.116
+ ___block_literal_global.11750
+ ___block_literal_global.118.33867
+ ___block_literal_global.11829
+ ___block_literal_global.11856
+ ___block_literal_global.11931
+ ___block_literal_global.120.10579
+ ___block_literal_global.120.22627
+ ___block_literal_global.12136
+ ___block_literal_global.122
+ ___block_literal_global.12392
+ ___block_literal_global.124
+ ___block_literal_global.12432
+ ___block_literal_global.126.22620
+ ___block_literal_global.128.22616
+ ___block_literal_global.129.33920
+ ___block_literal_global.12942
+ ___block_literal_global.130
+ ___block_literal_global.13086
+ ___block_literal_global.132.33923
+ ___block_literal_global.134.22610
+ ___block_literal_global.136.22606
+ ___block_literal_global.138.33914
+ ___block_literal_global.13816
+ ___block_literal_global.140
+ ___block_literal_global.14007
+ ___block_literal_global.14164
+ ___block_literal_global.142.39430
+ ___block_literal_global.142.43790
+ ___block_literal_global.144.33872
+ ___block_literal_global.14489
+ ___block_literal_global.14517
+ ___block_literal_global.14626
+ ___block_literal_global.147.33899
+ ___block_literal_global.149.39423
+ ___block_literal_global.15.23202
+ ___block_literal_global.15.27187
+ ___block_literal_global.15.44733
+ ___block_literal_global.15.46083
+ ___block_literal_global.153.33896
+ ___block_literal_global.159.33892
+ ___block_literal_global.160.43797
+ ___block_literal_global.16126
+ ___block_literal_global.162.33889
+ ___block_literal_global.164.46199
+ ___block_literal_global.16486
+ ___block_literal_global.16690
+ ___block_literal_global.167.46266
+ ___block_literal_global.168.33882
+ ___block_literal_global.16827
+ ___block_literal_global.169
+ ___block_literal_global.16996
+ ___block_literal_global.171.33865
+ ___block_literal_global.17231
+ ___block_literal_global.17265
+ ___block_literal_global.173
+ ___block_literal_global.175
+ ___block_literal_global.17679
+ ___block_literal_global.177
+ ___block_literal_global.179
+ ___block_literal_global.181
+ ___block_literal_global.183
+ ___block_literal_global.185
+ ___block_literal_global.18698
+ ___block_literal_global.187
+ ___block_literal_global.18717
+ ___block_literal_global.189
+ ___block_literal_global.19065
+ ___block_literal_global.191
+ ___block_literal_global.19208
+ ___block_literal_global.19247
+ ___block_literal_global.19279
+ ___block_literal_global.193.46296
+ ___block_literal_global.195
+ ___block_literal_global.197
+ ___block_literal_global.19830
+ ___block_literal_global.199
+ ___block_literal_global.19905
+ ___block_literal_global.19966
+ ___block_literal_global.201
+ ___block_literal_global.203.46306
+ ___block_literal_global.205
+ ___block_literal_global.20537
+ ___block_literal_global.20779
+ ___block_literal_global.208
+ ___block_literal_global.20916
+ ___block_literal_global.21061
+ ___block_literal_global.21165
+ ___block_literal_global.212
+ ___block_literal_global.21289
+ ___block_literal_global.21319
+ ___block_literal_global.214.46212
+ ___block_literal_global.217
+ ___block_literal_global.21720
+ ___block_literal_global.22703
+ ___block_literal_global.231
+ ___block_literal_global.23210
+ ___block_literal_global.23659
+ ___block_literal_global.23683
+ ___block_literal_global.23766
+ ___block_literal_global.240
+ ___block_literal_global.241.46335
+ ___block_literal_global.24165
+ ___block_literal_global.24341
+ ___block_literal_global.25518
+ ___block_literal_global.26.46094
+ ___block_literal_global.26418
+ ___block_literal_global.26445
+ ___block_literal_global.26711
+ ___block_literal_global.26908
+ ___block_literal_global.27075
+ ___block_literal_global.27207
+ ___block_literal_global.27394
+ ___block_literal_global.27705
+ ___block_literal_global.28534
+ ___block_literal_global.28720
+ ___block_literal_global.29143
+ ___block_literal_global.29221
+ ___block_literal_global.29316
+ ___block_literal_global.29636
+ ___block_literal_global.29699
+ ___block_literal_global.30341
+ ___block_literal_global.30468
+ ___block_literal_global.30567
+ ___block_literal_global.30610
+ ___block_literal_global.31419
+ ___block_literal_global.32135
+ ___block_literal_global.33064
+ ___block_literal_global.33442
+ ___block_literal_global.33927
+ ___block_literal_global.34.47571
+ ___block_literal_global.34062
+ ___block_literal_global.34748
+ ___block_literal_global.35342
+ ___block_literal_global.35473
+ ___block_literal_global.35643
+ ___block_literal_global.35714
+ ___block_literal_global.37342
+ ___block_literal_global.37362
+ ___block_literal_global.37786
+ ___block_literal_global.37873
+ ___block_literal_global.38733
+ ___block_literal_global.38762
+ ___block_literal_global.38857
+ ___block_literal_global.38924
+ ___block_literal_global.39
+ ___block_literal_global.39161
+ ___block_literal_global.39356
+ ___block_literal_global.39823
+ ___block_literal_global.39874
+ ___block_literal_global.40814
+ ___block_literal_global.40848
+ ___block_literal_global.41.22687
+ ___block_literal_global.41122
+ ___block_literal_global.41346
+ ___block_literal_global.41779
+ ___block_literal_global.41989
+ ___block_literal_global.42.14973
+ ___block_literal_global.42200
+ ___block_literal_global.42322
+ ___block_literal_global.43.22684
+ ___block_literal_global.43.47564
+ ___block_literal_global.43554
+ ___block_literal_global.43615
+ ___block_literal_global.43810
+ ___block_literal_global.44263
+ ___block_literal_global.44534
+ ___block_literal_global.44626
+ ___block_literal_global.44737
+ ___block_literal_global.45.27083
+ ___block_literal_global.45950
+ ___block_literal_global.46078
+ ___block_literal_global.47.22680
+ ___block_literal_global.47.49095
+ ___block_literal_global.47233
+ ___block_literal_global.47256
+ ___block_literal_global.47410
+ ___block_literal_global.47558
+ ___block_literal_global.48082
+ ___block_literal_global.48745
+ ___block_literal_global.49
+ ___block_literal_global.49103
+ ___block_literal_global.5.49086
+ ___block_literal_global.51
+ ___block_literal_global.53
+ ___block_literal_global.55.49091
+ ___block_literal_global.560
+ ___block_literal_global.562
+ ___block_literal_global.564
+ ___block_literal_global.566
+ ___block_literal_global.57.22671
+ ___block_literal_global.58.33074
+ ___block_literal_global.60.35645
+ ___block_literal_global.63.22668
+ ___block_literal_global.63.35647
+ ___block_literal_global.66.19960
+ ___block_literal_global.68.19956
+ ___block_literal_global.68.22662
+ ___block_literal_global.68.35651
+ ___block_literal_global.70.46112
+ ___block_literal_global.71.30530
+ ___block_literal_global.74.22658
+ ___block_literal_global.75.46119
+ ___block_literal_global.76
+ ___block_literal_global.78
+ ___block_literal_global.80.46126
+ ___block_literal_global.82.35636
+ ___block_literal_global.82.46132
+ ___block_literal_global.8367
+ ___block_literal_global.84
+ ___block_literal_global.8419
+ ___block_literal_global.85.27078
+ ___block_literal_global.859.46915
+ ___block_literal_global.86.43680
+ ___block_literal_global.88
+ ___block_literal_global.8968
+ ___block_literal_global.90
+ ___block_literal_global.92.39150
+ ___block_literal_global.94
+ ___block_literal_global.96
+ ___block_literal_global.9788
+ ___block_literal_global.98.39157
+ ___getBMSiriServiceClass_block_invoke.27218
+ ___getBiomeLibrarySymbolLoc_block_invoke.45924
+ ___getINSearchForMessagesIntentIdentifierSymbolLoc_block_invoke.15280
+ ___getINSendMessageIntentIdentifierSymbolLoc_block_invoke.15270
+ ___initLSApplicationProxy_block_invoke.34752
+ ___initLSApplicationProxy_block_invoke.46676
+ ___initVTPreferences_block_invoke.46882
+ _audit_stringBiomeLibrary.27202
+ _audit_stringBiomeLibrary.45938
+ _audit_stringBluetoothManager.20484
+ _audit_stringIntents.15278
+ _audit_stringIntents.31289
+ _audit_stringMediaExperience.27680
+ _classLSApplicationProxy.34749
+ _classLSApplicationProxy.46674
+ _classVTPreferences.46880
+ _getBMSiriServiceClass.softClass.27217
+ _getBiomeLibrarySymbolLoc.ptr.45923
+ _getBluetoothPairedStatusChangedNotification.46034
+ _getINSearchForMessagesIntentIdentifier.15268
+ _getINSearchForMessagesIntentIdentifierSymbolLoc.ptr.15279
+ _getINSendMessageIntentIdentifierSymbolLoc.ptr.15269
+ _getLSApplicationProxyClass.34741
+ _getLSApplicationProxyClass.46670
+ _getVTPreferencesClass.46876
+ _initLSApplicationProxy.34746
+ _initLSApplicationProxy.46672
+ _initLSApplicationProxy.sOnce.34747
+ _initLSApplicationProxy.sOnce.46673
+ _initVTPreferences.46878
+ _initVTPreferences.sOnce.46879
+ _objc_msgSend$getLoggableUserIdHash
+ _objc_msgSend$initWithSharedUserId:loggableSharedUserId:loggableUserIdHash:personaId:
+ _objc_msgSend$loggableUserIdHash
+ _objc_msgSend$postMessageToMUXWithMultiUserInfo:completion:
+ _objc_msgSend$setIsAlwaysAllowedWhileDeviceLocked:
+ _objc_msgSend$setLoggableUserIdHash:
+ _provider.onceToken.15283
+ _provider.provider.15284
+ _sharedInstance.onceToken.17230
+ _sharedInstance.onceToken.22734
+ _sharedInstance.onceToken.23658
+ _sharedInstance.onceToken.28719
+ _sharedInstance.onceToken.37361
+ _sharedInstance.onceToken.44755
+ _sharedInstance.singleton.44756
+ _sharedManager.onceToken.16689
+ _sharedManager.onceToken.22200
+ _sharedManager.onceToken.33063
+ _sharedManager.onceToken.43553
+ _sharedManager.result.33065
+ _sharedManager.sharedManager.43555
+ _sharedMonitor.monitor.20551
+ _sharedMonitor.onceToken.19762
+ _sharedMonitor.onceToken.20550
+ _sharedObserver.onceToken.31418
+ _sharedObserver.onceToken.46037
+ _sharedObserver.onceToken.49102
+ _sharedObserver.sharedObserver.31420
+ _sharedObserver.sharedObserver.49104
- -[AFASRSharedUserInfo initWithSharedUserId:loggableSharedUserId:personaId:]
- -[AFSiriAudioRoute isThirdPartyBluetoothHeadset]
- GCC_except_table10114
- GCC_except_table10116
- GCC_except_table10128
- GCC_except_table10154
- GCC_except_table10175
- GCC_except_table10368
- GCC_except_table10429
- GCC_except_table10433
- GCC_except_table10435
- GCC_except_table10444
- GCC_except_table10448
- GCC_except_table10454
- GCC_except_table10726
- GCC_except_table10894
- GCC_except_table10907
- GCC_except_table11095
- GCC_except_table11234
- GCC_except_table11247
- GCC_except_table11285
- GCC_except_table11543
- GCC_except_table11687
- GCC_except_table11706
- GCC_except_table11709
- GCC_except_table11711
- GCC_except_table4766
- GCC_except_table4832
- GCC_except_table4895
- GCC_except_table4905
- GCC_except_table4916
- GCC_except_table4929
- GCC_except_table5054
- GCC_except_table5408
- GCC_except_table5411
- GCC_except_table5478
- GCC_except_table5479
- GCC_except_table5492
- GCC_except_table5493
- GCC_except_table5500
- GCC_except_table5538
- GCC_except_table5544
- GCC_except_table5550
- GCC_except_table5622
- GCC_except_table5659
- GCC_except_table5662
- GCC_except_table5796
- GCC_except_table5895
- GCC_except_table5916
- GCC_except_table5982
- GCC_except_table6002
- GCC_except_table6008
- GCC_except_table6131
- GCC_except_table6138
- GCC_except_table6493
- GCC_except_table6508
- GCC_except_table6531
- GCC_except_table6634
- GCC_except_table6643
- GCC_except_table6682
- GCC_except_table6714
- GCC_except_table6781
- GCC_except_table7252
- GCC_except_table7260
- GCC_except_table7263
- GCC_except_table7266
- GCC_except_table7269
- GCC_except_table7476
- GCC_except_table7479
- GCC_except_table7493
- GCC_except_table7566
- GCC_except_table7572
- GCC_except_table7742
- GCC_except_table7848
- GCC_except_table7878
- GCC_except_table8067
- GCC_except_table8136
- GCC_except_table8242
- GCC_except_table8671
- GCC_except_table8725
- GCC_except_table8769
- GCC_except_table8857
- GCC_except_table8897
- GCC_except_table8928
- GCC_except_table8934
- GCC_except_table9184
- GCC_except_table9254
- GCC_except_table9260
- GCC_except_table9295
- GCC_except_table9298
- GCC_except_table9376
- GCC_except_table9405
- GCC_except_table9477
- GCC_except_table9480
- GCC_except_table9484
- GCC_except_table9589
- GCC_except_table9593
- GCC_except_table9597
- GCC_except_table9630
- GCC_except_table9675
- _AnnounceLibrary.sLib.43743
- _AnnounceLibrary.sOnce.43741
- _BiomeLibraryLibraryCore.45883
- _BiomeLibraryLibraryCore.frameworkLibrary.27167
- _BiomeLibraryLibraryCore.frameworkLibrary.45886
- _BluetoothManagerLibrary.45978
- _BluetoothManagerLibraryCore.frameworkLibrary.20455
- _CoreServicesLibrary.frameworkLibrary.46623
- _CoreSpeechLibrary.frameworkLibrary.39378
- _DataCollectionServicesLibrary.sLib.46635
- _DataCollectionServicesLibrary.sOnce.46634
- _IntentsLibrary.15264
- _IntentsLibraryCore.frameworkLibrary.15268
- _IntentsLibraryCore.frameworkLibrary.31242
- _LSApplicationProxyFunction.34713
- _LSApplicationProxyFunction.46629
- _MediaExperienceLibrary.27618
- _MediaExperienceLibraryCore.frameworkLibrary.27644
- _SoftBiomeLibrary.45869
- _VTPreferencesFunction.46835
- _VoiceTriggerLibrary.frameworkLibrary.46829
- ___31-[AFSettingsConnection barrier]_block_invoke.57
- ___35-[AFSettingsConnection _connection]_block_invoke.10
- ___35-[AFSettingsConnection _connection]_block_invoke_2.11
- ___40-[AFSettingsConnection configOverrides:]_block_invoke.68
- ___43-[AFSettingsConnection dumpAssistantState:]_block_invoke.241
- ___43-[AFSettingsConnection fetchActiveAccount:]_block_invoke.19
- ___44-[AFSettingsConnection currectNWActivityId:]_block_invoke.142
- ___47-[AFSettingsConnection startUIRequestWithInfo:]_block_invoke.164
- ___47-[AFSettingsConnection startUIRequestWithText:]_block_invoke.159
- ___48-[AFSettingsConnection siriDesignModeIsEnabled:]_block_invoke.234
- ___50-[AFSettingsConnection areSiriSAEAssetsAvailable:]_block_invoke.240
- ___56-[AFSettingsConnection isSearchDataSharingStatusForced:]_block_invoke.237
- ___57-[AFSettingsConnection setIsHomePodInHH2Mode:completion:]_block_invoke.228
- ___58-[AFSettingsConnection getSearchQueriesDataSharingStatus:]_block_invoke.236
- ___60-[AFSettingsConnection multiUserCompanionDeviceIdentifiers:]_block_invoke.218
- ___60-[AFSettingsConnection setSiriDesignModeEnabled:completion:]_block_invoke.233
- ___60-[AFSettingsConnection(Internal) _handleCommand:completion:]_block_invoke.562
- ___62-[AFSettingsConnection fetchAccountsSynchronously:completion:]_block_invoke.14
- ___62-[AFSettingsConnection getCurrentAccessoryInfoWithCompletion:]_block_invoke.149
- ___62-[AFSettingsConnection getPersonalMultiUserDeviceIdentifiers:]_block_invoke.217
- ___63-[AFSettingsConnection forceMultiUserSync:download:completion:]_block_invoke.70
- ___64-[AFSettingsConnection disableAndDeleteCloudSyncWithCompletion:]_block_invoke.60
- ___64-[AFSettingsConnection shouldSuppressSiriDataSharingOptInAlert:]_block_invoke.231
- ___65-[AFSettingsConnection setSiriDataSharingOptInStatus:completion:]_block_invoke.223
- ___68-[AFSettingsConnection deleteSiriHistoryWithContext:withCompletion:]_block_invoke.232
- ___68-[AFSettingsConnection getSiriDataSharingOptInStatusWithCompletion:]_block_invoke.224
- ___69-[AFSettingsConnection setSearchQueriesDataSharingStatus:completion:]_block_invoke.235
- ___73-[AFSettingsConnection setSiriDataSharingOptInAlertPresented:completion:]_block_invoke.226
- ___75-[AFASRSharedUserInfo initWithSharedUserId:loggableSharedUserId:personaId:]_block_invoke
- ___77-[AFSettingsConnection _createRadarWithReason:room:process:crash:completion:]_block_invoke.250
- ___79-[AFSettingsConnection setSiriDataSharingHomePodSetupDeviceIsValid:completion:]_block_invoke.227
- ___AnnounceLibrary_block_invoke.43747
- ___BiomeLibraryLibraryCore_block_invoke.27168
- ___BiomeLibraryLibraryCore_block_invoke.45887
- ___Block_byref_object_copy_.10702
- ___Block_byref_object_copy_.10895
- ___Block_byref_object_copy_.11527
- ___Block_byref_object_copy_.12109
- ___Block_byref_object_copy_.13376
- ___Block_byref_object_copy_.13658
- ___Block_byref_object_copy_.16637
- ___Block_byref_object_copy_.17166
- ___Block_byref_object_copy_.17657
- ___Block_byref_object_copy_.19699
- ___Block_byref_object_copy_.19940
- ___Block_byref_object_copy_.20471
- ___Block_byref_object_copy_.21543
- ___Block_byref_object_copy_.22492
- ___Block_byref_object_copy_.23166
- ___Block_byref_object_copy_.23583
- ___Block_byref_object_copy_.24181
- ___Block_byref_object_copy_.26306
- ___Block_byref_object_copy_.29153
- ___Block_byref_object_copy_.30825
- ___Block_byref_object_copy_.35140
- ___Block_byref_object_copy_.35584
- ___Block_byref_object_copy_.37806
- ___Block_byref_object_copy_.38997
- ___Block_byref_object_copy_.42123
- ___Block_byref_object_copy_.46767
- ___Block_byref_object_copy_.48008
- ___Block_byref_object_copy_.48744
- ___Block_byref_object_copy_.49026
- ___Block_byref_object_copy_.8759
- ___Block_byref_object_copy_.9999
- ___Block_byref_object_dispose_.10000
- ___Block_byref_object_dispose_.10703
- ___Block_byref_object_dispose_.10896
- ___Block_byref_object_dispose_.11528
- ___Block_byref_object_dispose_.12110
- ___Block_byref_object_dispose_.13377
- ___Block_byref_object_dispose_.13659
- ___Block_byref_object_dispose_.16638
- ___Block_byref_object_dispose_.17167
- ___Block_byref_object_dispose_.17658
- ___Block_byref_object_dispose_.19700
- ___Block_byref_object_dispose_.19941
- ___Block_byref_object_dispose_.20472
- ___Block_byref_object_dispose_.21544
- ___Block_byref_object_dispose_.22493
- ___Block_byref_object_dispose_.23167
- ___Block_byref_object_dispose_.23584
- ___Block_byref_object_dispose_.24182
- ___Block_byref_object_dispose_.26307
- ___Block_byref_object_dispose_.29154
- ___Block_byref_object_dispose_.30826
- ___Block_byref_object_dispose_.35141
- ___Block_byref_object_dispose_.35585
- ___Block_byref_object_dispose_.37807
- ___Block_byref_object_dispose_.38998
- ___Block_byref_object_dispose_.42124
- ___Block_byref_object_dispose_.46768
- ___Block_byref_object_dispose_.48009
- ___Block_byref_object_dispose_.48745
- ___Block_byref_object_dispose_.49027
- ___Block_byref_object_dispose_.8760
- ___BluetoothManagerLibraryCore_block_invoke.20456
- ___DataCollectionServicesLibrary_block_invoke.46637
- ___IntentsLibraryCore_block_invoke.15269
- ___IntentsLibraryCore_block_invoke.31243
- ___MediaExperienceLibraryCore_block_invoke.27645
- ___block_descriptor_56_e8_32s40s48s_e39_v16?0"<AFASRSharedUserInfoMutating>"8ls32l8s40l8s48l8
- ___block_literal_global.101.22622
- ___block_literal_global.101.39105
- ___block_literal_global.103.22618
- ___block_literal_global.10431
- ___block_literal_global.10488
- ___block_literal_global.105
- ___block_literal_global.10640
- ___block_literal_global.107
- ___block_literal_global.10707
- ___block_literal_global.109.22611
- ___block_literal_global.111.22608
- ___block_literal_global.112.10635
- ___block_literal_global.11202
- ___block_literal_global.113
- ___block_literal_global.115.22603
- ___block_literal_global.117
- ___block_literal_global.11743
- ___block_literal_global.11822
- ___block_literal_global.11849
- ___block_literal_global.119
- ___block_literal_global.11924
- ___block_literal_global.120.10572
- ___block_literal_global.121.33883
- ___block_literal_global.12129
- ___block_literal_global.123.22595
- ___block_literal_global.12385
- ___block_literal_global.12425
- ___block_literal_global.125
- ___block_literal_global.127
- ___block_literal_global.129.22589
- ___block_literal_global.129.33879
- ___block_literal_global.12935
- ___block_literal_global.13079
- ___block_literal_global.131.46087
- ___block_literal_global.133
- ___block_literal_global.135.33873
- ___block_literal_global.137
- ___block_literal_global.13809
- ___block_literal_global.139
- ___block_literal_global.14000
- ___block_literal_global.141.33861
- ___block_literal_global.14157
- ___block_literal_global.142.43742
- ___block_literal_global.144.33837
- ___block_literal_global.14482
- ___block_literal_global.14510
- ___block_literal_global.146
- ___block_literal_global.14619
- ___block_literal_global.148.43755
- ___block_literal_global.15.23176
- ___block_literal_global.15.27155
- ___block_literal_global.15.44684
- ___block_literal_global.15.46033
- ___block_literal_global.152.22566
- ___block_literal_global.158
- ___block_literal_global.160.43749
- ___block_literal_global.161
- ___block_literal_global.16110
- ___block_literal_global.163.43739
- ___block_literal_global.16470
- ___block_literal_global.166
- ___block_literal_global.16674
- ___block_literal_global.168.22559
- ___block_literal_global.168.33847
- ___block_literal_global.16811
- ___block_literal_global.16980
- ___block_literal_global.170
- ___block_literal_global.172
- ___block_literal_global.17215
- ___block_literal_global.17249
- ___block_literal_global.174
- ___block_literal_global.176.22553
- ___block_literal_global.17650
- ___block_literal_global.178
- ___block_literal_global.180.41731
- ___block_literal_global.182.46228
- ___block_literal_global.184
- ___block_literal_global.186
- ___block_literal_global.18668
- ___block_literal_global.18687
- ___block_literal_global.188.46242
- ___block_literal_global.190
- ___block_literal_global.19035
- ___block_literal_global.19178
- ___block_literal_global.192
- ___block_literal_global.19217
- ___block_literal_global.19249
- ___block_literal_global.194
- ___block_literal_global.196
- ___block_literal_global.198.46252
- ___block_literal_global.19806
- ___block_literal_global.19881
- ___block_literal_global.19942
- ___block_literal_global.200
- ___block_literal_global.202
- ___block_literal_global.204
- ___block_literal_global.20513
- ___block_literal_global.207
- ___block_literal_global.20755
- ___block_literal_global.20892
- ___block_literal_global.21037
- ___block_literal_global.211
- ___block_literal_global.21141
- ___block_literal_global.21265
- ___block_literal_global.21295
- ___block_literal_global.213
- ___block_literal_global.216
- ___block_literal_global.21696
- ___block_literal_global.22682
- ___block_literal_global.230
- ___block_literal_global.23184
- ___block_literal_global.23634
- ___block_literal_global.23658
- ___block_literal_global.23741
- ___block_literal_global.239
- ___block_literal_global.241.46281
- ___block_literal_global.24128
- ___block_literal_global.24304
- ___block_literal_global.25479
- ___block_literal_global.26.46044
- ___block_literal_global.26383
- ___block_literal_global.26410
- ___block_literal_global.26676
- ___block_literal_global.26874
- ___block_literal_global.27043
- ___block_literal_global.27175
- ___block_literal_global.27362
- ___block_literal_global.27673
- ___block_literal_global.28502
- ___block_literal_global.28688
- ___block_literal_global.29111
- ___block_literal_global.29189
- ___block_literal_global.29284
- ___block_literal_global.29604
- ___block_literal_global.29667
- ___block_literal_global.30309
- ___block_literal_global.30436
- ___block_literal_global.30535
- ___block_literal_global.30578
- ___block_literal_global.31387
- ___block_literal_global.32103
- ___block_literal_global.33
- ___block_literal_global.33032
- ___block_literal_global.33412
- ___block_literal_global.33886
- ___block_literal_global.34021
- ___block_literal_global.34706
- ___block_literal_global.35300
- ___block_literal_global.35429
- ___block_literal_global.35597
- ___block_literal_global.35668
- ___block_literal_global.37296
- ___block_literal_global.37316
- ___block_literal_global.37738
- ___block_literal_global.37825
- ___block_literal_global.38.22670
- ___block_literal_global.38688
- ___block_literal_global.38717
- ___block_literal_global.38812
- ___block_literal_global.38879
- ___block_literal_global.39112
- ___block_literal_global.39306
- ___block_literal_global.39769
- ___block_literal_global.39820
- ___block_literal_global.40.47516
- ___block_literal_global.40760
- ___block_literal_global.40794
- ___block_literal_global.41068
- ___block_literal_global.41292
- ___block_literal_global.41727
- ___block_literal_global.41939
- ___block_literal_global.42.14966
- ___block_literal_global.42.22663
- ___block_literal_global.42150
- ___block_literal_global.42272
- ___block_literal_global.43.47510
- ___block_literal_global.43504
- ___block_literal_global.43565
- ___block_literal_global.43764
- ___block_literal_global.44
- ___block_literal_global.44217
- ___block_literal_global.44488
- ___block_literal_global.44580
- ___block_literal_global.44688
- ___block_literal_global.45901
- ___block_literal_global.46
- ___block_literal_global.46028
- ___block_literal_global.47.49039
- ___block_literal_global.47179
- ___block_literal_global.47202
- ___block_literal_global.47356
- ___block_literal_global.47504
- ___block_literal_global.48.27051
- ___block_literal_global.48028
- ___block_literal_global.48691
- ___block_literal_global.49047
- ___block_literal_global.5.49032
- ___block_literal_global.50
- ___block_literal_global.52
- ___block_literal_global.54.22653
- ___block_literal_global.555
- ___block_literal_global.557
- ___block_literal_global.559
- ___block_literal_global.56
- ___block_literal_global.561
- ___block_literal_global.58.33042
- ___block_literal_global.59
- ___block_literal_global.62
- ___block_literal_global.63.35600
- ___block_literal_global.66.19936
- ___block_literal_global.67
- ___block_literal_global.68.19932
- ___block_literal_global.68.35604
- ___block_literal_global.70.46062
- ___block_literal_global.71.30498
- ___block_literal_global.73.35605
- ___block_literal_global.75.22641
- ___block_literal_global.75.46069
- ___block_literal_global.77
- ___block_literal_global.79
- ___block_literal_global.81
- ___block_literal_global.82.46080
- ___block_literal_global.83
- ___block_literal_global.8363
- ___block_literal_global.8415
- ___block_literal_global.85.22634
- ___block_literal_global.85.27046
- ___block_literal_global.859.46861
- ___block_literal_global.87
- ___block_literal_global.89.43629
- ___block_literal_global.8964
- ___block_literal_global.91
- ___block_literal_global.93.22628
- ___block_literal_global.95.39109
- ___block_literal_global.97
- ___block_literal_global.9784
- ___block_literal_global.99
- ___getBMSiriServiceClass_block_invoke.27186
- ___getBiomeLibrarySymbolLoc_block_invoke.45875
- ___getINSearchForMessagesIntentIdentifierSymbolLoc_block_invoke.15273
- ___getINSendMessageIntentIdentifierSymbolLoc_block_invoke.15263
- ___initLSApplicationProxy_block_invoke.34710
- ___initLSApplicationProxy_block_invoke.46622
- ___initVTPreferences_block_invoke.46828
- _audit_stringBiomeLibrary.27170
- _audit_stringBiomeLibrary.45889
- _audit_stringBluetoothManager.20460
- _audit_stringIntents.15271
- _audit_stringIntents.31257
- _audit_stringMediaExperience.27648
- _classLSApplicationProxy.34707
- _classLSApplicationProxy.46620
- _classVTPreferences.46826
- _getBMSiriServiceClass.softClass.27185
- _getBiomeLibrarySymbolLoc.ptr.45874
- _getBluetoothPairedStatusChangedNotification.45984
- _getINSearchForMessagesIntentIdentifier.15261
- _getINSearchForMessagesIntentIdentifierSymbolLoc.ptr.15272
- _getINSendMessageIntentIdentifierSymbolLoc.ptr.15262
- _getLSApplicationProxyClass.34699
- _getLSApplicationProxyClass.46616
- _getVTPreferencesClass.46822
- _initLSApplicationProxy.34704
- _initLSApplicationProxy.46618
- _initLSApplicationProxy.sOnce.34705
- _initLSApplicationProxy.sOnce.46619
- _initVTPreferences.46824
- _initVTPreferences.sOnce.46825
- _objc_msgSend$_isAppleHeadphone
- _objc_msgSend$initWithSharedUserId:loggableSharedUserId:personaId:
- _provider.onceToken.15276
- _provider.provider.15277
- _sharedInstance.onceToken.17214
- _sharedInstance.onceToken.22711
- _sharedInstance.onceToken.23633
- _sharedInstance.onceToken.28687
- _sharedInstance.onceToken.37315
- _sharedInstance.onceToken.44706
- _sharedInstance.singleton.44707
- _sharedManager.onceToken.16673
- _sharedManager.onceToken.22176
- _sharedManager.onceToken.33031
- _sharedManager.onceToken.43503
- _sharedManager.result.33033
- _sharedManager.sharedManager.43505
- _sharedMonitor.monitor.20527
- _sharedMonitor.onceToken.19738
- _sharedMonitor.onceToken.20526
- _sharedObserver.onceToken.31386
- _sharedObserver.onceToken.45987
- _sharedObserver.onceToken.49046
- _sharedObserver.sharedObserver.31388
- _sharedObserver.sharedObserver.49048
CStrings:
+ "%@ {sharedUserId = %@, loggableSharedUserId = %@, loggableUserIdHash = %@, personaId = %@}"
+ "%s Error in postMessageToMUXWithMultiUserInfo:%@"
+ "%s Search Queries Data Sharing status: using default value."
+ "%s Search Queries Data Sharing value has unexpected type: %{private}@"
+ "%s Search Queries Data Sharing value has unexpected value: %{private}@"
+ "-[AFMultiUserConnection postMessageToMUXWithMultiUserInfo:completion:]"
+ "-[AFMultiUserConnection postMessageToMUXWithMultiUserInfo:completion:]_block_invoke_2"
+ "@\"NSRecursiveLock\""
+ "AFASRSharedUserInfo::loggableUserIdHash"
+ "T@\"NSString\",R,C,N,V_loggableUserIdHash"
+ "TB,N,V_isAlwaysAllowedWhileDeviceLocked"
+ "Vv32@0:8@\"SAMultiUserInfo\"16@?<v@?@\"NSError\">24"
+ "_connectionLock"
+ "_connectionSetupComplete"
+ "_isAlwaysAllowedWhileDeviceLocked"
+ "_loggableUserIdHash"
+ "getLoggableUserIdHash"
+ "initWithSharedUserId:loggableSharedUserId:loggableUserIdHash:personaId:"
+ "isAlwaysAllowedWhileDeviceLocked"
+ "isNonAnnounceSupportedWirelessHeadset"
+ "loggableUserIdHash"
+ "postMessageToMUXWithMultiUserInfo:completion:"
+ "setIsAlwaysAllowedWhileDeviceLocked:"
+ "setLoggableUserIdHash:"
+ "uuid: %@, timestamp: %llu, requestId: %@, turnId: %@, options: %lu, notifyState: %@ text: %@ directAction: %@ handoffOriginDeviceName: %@ handOffData: %@ handoffURL: %@ handoffRequiresUserInteraction ? %d handoffNotification %@ correctedSpeech: %@ startRequest: %@ activationEvent: %@ speechRequestOptions: %@ testRequestOptions: %@ requestCompletionOptions: %@ sharedUserID: %@ confidenceScore: %lu nonspeakerConfidenceScores: %@ SuggestionRequestType: %@ isAlwaysAllowedWhileDeviceLocked: %@"
+ "{_mutationFlags=\"isDirty\"b1\"hasSharedUserId\"b1\"hasLoggableSharedUserId\"b1\"hasLoggableUserIdHash\"b1\"hasPersonaId\"b1}"
- "%@ {sharedUserId = %@, loggableSharedUserId = %@, personaId = %@}"
- "initWithSharedUserId:loggableSharedUserId:personaId:"
- "isThirdPartyBluetoothHeadset"
- "uuid: %@, timestamp: %llu, requestId: %@, turnId: %@, options: %lu, notifyState: %@ text: %@ directAction: %@ handoffOriginDeviceName: %@ handOffData: %@ handoffURL: %@ handoffRequiresUserInteraction ? %d handoffNotification %@ correctedSpeech: %@ startRequest: %@ activationEvent: %@ speechRequestOptions: %@ testRequestOptions: %@ requestCompletionOptions: %@ sharedUserID: %@ confidenceScore: %lu nonspeakerConfidenceScores: %@ SuggestionRequestType: %@"
- "{_mutationFlags=\"isDirty\"b1\"hasSharedUserId\"b1\"hasLoggableSharedUserId\"b1\"hasPersonaId\"b1}"

```
