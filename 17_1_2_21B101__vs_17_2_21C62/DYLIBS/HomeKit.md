## HomeKit

> `/System/Library/Frameworks/HomeKit.framework/HomeKit`

```diff

-1076.2.8.1.1
-  __TEXT.__text: 0x25d8d0
-  __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_methlist: 0x1fe04
+1092.3.10.1.2
+  __TEXT.__text: 0x261674
+  __TEXT.__auth_stubs: 0xcc0
+  __TEXT.__objc_methlist: 0x201c4
   __TEXT.__const: 0x290
-  __TEXT.__gcc_except_tab: 0x3f6c
-  __TEXT.__cstring: 0x256ce
-  __TEXT.__oslogstring: 0x24f52
+  __TEXT.__gcc_except_tab: 0x3fc0
+  __TEXT.__cstring: 0x25866
+  __TEXT.__oslogstring: 0x25183
   __TEXT.__dlopen_cstrs: 0x3a2
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x9298
-  __TEXT.__objc_classname: 0x4a29
-  __TEXT.__objc_methname: 0x3eb11
-  __TEXT.__objc_methtype: 0x74a6
-  __TEXT.__objc_stubs: 0x23560
+  __TEXT.__unwind_info: 0x92a0
+  __TEXT.__objc_classname: 0x49a5
+  __TEXT.__objc_methname: 0x3fd0f
+  __TEXT.__objc_methtype: 0x77f8
+  __TEXT.__objc_stubs: 0x234a0
   __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0x6d00
-  __DATA_CONST.__objc_classlist: 0x1090
+  __DATA_CONST.__const: 0x6d68
+  __DATA_CONST.__objc_classlist: 0x1068
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x470
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x316b0
-  __DATA_CONST.__objc_selrefs: 0xb998
+  __DATA_CONST.__objc_const: 0x319f8
+  __DATA_CONST.__objc_selrefs: 0xbd08
   __DATA_CONST.__objc_arraydata: 0x1330
-  __AUTH_CONST.__cfstring: 0x232c0
-  __AUTH_CONST.__objc_const: 0xf3c8
+  __AUTH_CONST.__cfstring: 0x23500
+  __AUTH_CONST.__objc_const: 0xf188
   __AUTH_CONST.__const: 0x1920
   __AUTH_CONST.__objc_intobj: 0x798
   __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x540
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x688
-  __AUTH.__objc_data: 0x7d00
+  __AUTH_CONST.__auth_got: 0x670
+  __AUTH.__objc_data: 0x7bc0
   __DATA.__objc_protorefs: 0x98
-  __DATA.__objc_classrefs: 0x1330
-  __DATA.__objc_superrefs: 0xde0
-  __DATA.__objc_ivar: 0x211c
+  __DATA.__objc_classrefs: 0x1308
+  __DATA.__objc_superrefs: 0xdd8
+  __DATA.__objc_ivar: 0x2188
   __DATA.__data: 0x3608
   __DATA.__common: 0x18
-  __DATA.__bss: 0x7f0
-  __DATA_DIRTY.__objc_data: 0x28a0
-  __DATA_DIRTY.__bss: 0x1e0
+  __DATA.__bss: 0x800
+  __DATA_DIRTY.__objc_data: 0x2850
+  __DATA_DIRTY.__bss: 0x1d0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 12493
-  Symbols:   40112
-  CStrings:  18415
+  Functions: 12583
+  Symbols:   40278
+  CStrings:  18587
 
Symbols:
+ -[HMAccessory installManagedConfigurationProfileWithData:completionHandler:]
+ -[HMAccessoryCapabilities supportsInstallManagedConfigurationProfile]
+ -[HMAccessoryDiagnosticInfo currentAccessoryMediaRouteId]
+ -[HMAccessoryDiagnosticInfo softwareUpdateDescriptor]
+ -[HMAccessoryDiagnosticInfo softwareUpdateProgress]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo hasSoftwareUpdateDescriptor]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo hasSoftwareUpdateProgress]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setSoftwareUpdateDescriptor:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setSoftwareUpdateProgress:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo softwareUpdateDescriptor]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo softwareUpdateProgress]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo hasLastSetupInfo]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo lastSetupInfo]
+ -[HMAccessoryDiagnosticInfoProtoDiagnosticInfo setLastSetupInfo:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo .cxx_destruct]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo StringAsICloudAvailableINT:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo StringAsIDSAvailableINT:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo StringAsManateeAvailableINT:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo StringAsNetworkAvailableINT:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo accessoryAddMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo accountSettleWaitMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo controllerKeyExchangeMSHH1]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo copyTo:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo copyWithZone:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo currentDeviceIDSWaitMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo description]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo dictionaryRepresentation]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo eventRouterFirstEventPushMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo eventRouterServerConnectionMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo firstCoreDataImportMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasAccessoryAddMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasAccountSettleWaitMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasControllerKeyExchangeMSHH1]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasCurrentDeviceIDSWaitMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasEventRouterFirstEventPushMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasEventRouterServerConnectionMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasFirstCoreDataImportMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasHomeManagerReadyMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasICloudAvailableINT]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasIDSAvailableINT]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasLastKnownStageErrorCode]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasLastKnownStageErrorDomain]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasLastKnownStageErrorString]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasLastKnownStageUnderlyingErrorCode]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasLastKnownStageUnderlyingErrorDomain]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasManateeAvailableINT]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasNetworkAvailableINT]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasNewAccessoryTransferMSHH1]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasPairingIdentityCreationMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasPrimaryResidentElectionMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasSavedEventState]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasSentinelZoneFetchMSHH1]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasSessionSetupCloseMSHH1]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasSessionSetupOpenMSHH1]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasSettingsCreationMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasSiriReadyMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasTotalDurationMSHH1]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasTotalDurationMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasVersion]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hash]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo homeManagerReadyMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo iCloudAvailableINTAsString:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo iCloudAvailableINT]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo iDSAvailableINTAsString:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo iDSAvailableINT]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo isEqual:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo lastKnownStageErrorCode]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo lastKnownStageErrorDomain]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo lastKnownStageErrorString]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo lastKnownStageUnderlyingErrorCode]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo lastKnownStageUnderlyingErrorDomain]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo manateeAvailableINTAsString:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo manateeAvailableINT]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo mergeFrom:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo networkAvailableINTAsString:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo networkAvailableINT]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo newAccessoryTransferMSHH1]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo pairingIdentityCreationMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo primaryResidentElectionMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo readFrom:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo savedEventState]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo sentinelZoneFetchMSHH1]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo sessionSetupCloseMSHH1]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo sessionSetupOpenMSHH1]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setAccessoryAddMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setAccountSettleWaitMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setControllerKeyExchangeMSHH1:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setCurrentDeviceIDSWaitMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setEventRouterFirstEventPushMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setEventRouterServerConnectionMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setFirstCoreDataImportMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasAccessoryAddMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasAccountSettleWaitMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasControllerKeyExchangeMSHH1:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasCurrentDeviceIDSWaitMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasEventRouterFirstEventPushMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasEventRouterServerConnectionMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasFirstCoreDataImportMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasHomeManagerReadyMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasICloudAvailableINT:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasIDSAvailableINT:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasLastKnownStageErrorCode:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasLastKnownStageUnderlyingErrorCode:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasManateeAvailableINT:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasNetworkAvailableINT:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasNewAccessoryTransferMSHH1:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasPairingIdentityCreationMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasPrimaryResidentElectionMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasSavedEventState:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasSentinelZoneFetchMSHH1:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasSessionSetupCloseMSHH1:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasSessionSetupOpenMSHH1:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasSettingsCreationMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasSiriReadyMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasTotalDurationMSHH1:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasTotalDurationMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasVersion:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHomeManagerReadyMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setICloudAvailableINT:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setIDSAvailableINT:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setLastKnownStageErrorCode:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setLastKnownStageErrorDomain:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setLastKnownStageErrorString:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setLastKnownStageUnderlyingErrorCode:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setLastKnownStageUnderlyingErrorDomain:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setManateeAvailableINT:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setNetworkAvailableINT:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setNewAccessoryTransferMSHH1:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setPairingIdentityCreationMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setPrimaryResidentElectionMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setSavedEventState:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setSentinelZoneFetchMSHH1:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setSessionSetupCloseMSHH1:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setSessionSetupOpenMSHH1:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setSettingsCreationMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setSiriReadyMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setTotalDurationMSHH1:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setTotalDurationMSHH2:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setVersion:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo settingsCreationMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo siriReadyMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo totalDurationMSHH1]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo totalDurationMSHH2]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo version]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo writeTo:]
+ -[HMAccessorySetupPayload initWithInternalSetupPayload:]
+ -[HMDeviceSetupOperation initWithSession:setupSessionFactory:]
+ -[HMHome setPreferredPrimary:oneTime:triggerElection:completionHandler:]
+ -[HMHomeManager isiPhoneOnlyPairingSupportedForMatterAccessories]
+ -[HMPlainTextDocument initWithURL:fileManager:error:]
+ -[HMProtoAccessoryCapabilities hasSupportsInstallManagedConfigurationProfile]
+ -[HMProtoAccessoryCapabilities setHasSupportsInstallManagedConfigurationProfile:]
+ -[HMProtoAccessoryCapabilities setSupportsInstallManagedConfigurationProfile:]
+ -[HMProtoAccessoryCapabilities supportsInstallManagedConfigurationProfile]
+ -[HMProtoResidentCapabilities hasSupportsEventLog]
+ -[HMProtoResidentCapabilities setHasSupportsEventLog:]
+ -[HMProtoResidentCapabilities setSupportsEventLog:]
+ -[HMProtoResidentCapabilities supportsEventLog]
+ -[HMSoftwareUpdate nextPermittedRequestDocumentationDate]
+ -[HMSoftwareUpdate setNextPermittedRequestDocumentationDate:]
+ -[HMSoftwareUpdateDescriptor copyWithZone:]
+ -[HMSoftwareUpdateDescriptor hash]
+ -[HMSoftwareUpdateDescriptor isEqual:]
+ -[HMThreadNetworkMetadata initWithName:channel:PANID:extendedPANID:masterKey:passPhrase:PSKc:operationalDataset:]
+ -[HMThreadNetworkMetadata operationalDataset]
+ -[HMThreadNetworkMetadata setOperationalDataset:]
+ -[HMUserInviteInformation validateInviteForHome:]
+ -[_HMDocument initWithURL:fileManager:error:]
+ -[__HMHomeDataSyncOperation logIdentifier]
+ GCC_except_table10002
+ GCC_except_table1001
+ GCC_except_table1010
+ GCC_except_table10302
+ GCC_except_table10304
+ GCC_except_table10306
+ GCC_except_table10307
+ GCC_except_table10338
+ GCC_except_table10340
+ GCC_except_table10348
+ GCC_except_table10349
+ GCC_except_table10350
+ GCC_except_table10458
+ GCC_except_table10459
+ GCC_except_table10485
+ GCC_except_table10492
+ GCC_except_table10566
+ GCC_except_table10579
+ GCC_except_table10603
+ GCC_except_table10607
+ GCC_except_table10648
+ GCC_except_table10649
+ GCC_except_table10650
+ GCC_except_table10651
+ GCC_except_table10652
+ GCC_except_table10653
+ GCC_except_table10654
+ GCC_except_table10655
+ GCC_except_table10656
+ GCC_except_table10657
+ GCC_except_table10658
+ GCC_except_table10659
+ GCC_except_table10660
+ GCC_except_table10661
+ GCC_except_table10662
+ GCC_except_table10679
+ GCC_except_table10706
+ GCC_except_table1078
+ GCC_except_table1080
+ GCC_except_table10813
+ GCC_except_table10814
+ GCC_except_table10817
+ GCC_except_table1083
+ GCC_except_table1085
+ GCC_except_table1087
+ GCC_except_table10879
+ GCC_except_table10881
+ GCC_except_table10889
+ GCC_except_table10895
+ GCC_except_table10896
+ GCC_except_table10902
+ GCC_except_table10904
+ GCC_except_table10909
+ GCC_except_table1091
+ GCC_except_table10910
+ GCC_except_table10911
+ GCC_except_table11138
+ GCC_except_table11139
+ GCC_except_table11292
+ GCC_except_table11295
+ GCC_except_table11300
+ GCC_except_table11304
+ GCC_except_table11310
+ GCC_except_table11315
+ GCC_except_table11317
+ GCC_except_table11322
+ GCC_except_table11323
+ GCC_except_table11325
+ GCC_except_table1140
+ GCC_except_table11408
+ GCC_except_table11410
+ GCC_except_table11429
+ GCC_except_table11430
+ GCC_except_table11431
+ GCC_except_table11432
+ GCC_except_table11437
+ GCC_except_table11451
+ GCC_except_table11460
+ GCC_except_table11462
+ GCC_except_table11542
+ GCC_except_table11544
+ GCC_except_table11547
+ GCC_except_table11555
+ GCC_except_table11556
+ GCC_except_table11561
+ GCC_except_table11567
+ GCC_except_table11569
+ GCC_except_table11571
+ GCC_except_table11573
+ GCC_except_table11575
+ GCC_except_table11577
+ GCC_except_table11711
+ GCC_except_table11766
+ GCC_except_table11767
+ GCC_except_table11768
+ GCC_except_table11779
+ GCC_except_table11780
+ GCC_except_table11804
+ GCC_except_table11805
+ GCC_except_table11859
+ GCC_except_table11884
+ GCC_except_table11887
+ GCC_except_table12019
+ GCC_except_table12139
+ GCC_except_table12140
+ GCC_except_table12190
+ GCC_except_table12195
+ GCC_except_table12197
+ GCC_except_table12199
+ GCC_except_table12231
+ GCC_except_table12274
+ GCC_except_table12279
+ GCC_except_table12282
+ GCC_except_table12342
+ GCC_except_table12427
+ GCC_except_table12487
+ GCC_except_table12489
+ GCC_except_table12498
+ GCC_except_table12501
+ GCC_except_table12521
+ GCC_except_table12523
+ GCC_except_table12524
+ GCC_except_table1255
+ GCC_except_table1277
+ GCC_except_table1354
+ GCC_except_table1357
+ GCC_except_table1506
+ GCC_except_table1575
+ GCC_except_table1578
+ GCC_except_table1647
+ GCC_except_table1649
+ GCC_except_table1723
+ GCC_except_table1724
+ GCC_except_table1772
+ GCC_except_table2001
+ GCC_except_table2004
+ GCC_except_table2007
+ GCC_except_table2012
+ GCC_except_table2016
+ GCC_except_table2025
+ GCC_except_table2027
+ GCC_except_table2030
+ GCC_except_table2040
+ GCC_except_table2042
+ GCC_except_table2043
+ GCC_except_table2048
+ GCC_except_table2049
+ GCC_except_table2050
+ GCC_except_table2051
+ GCC_except_table2238
+ GCC_except_table2240
+ GCC_except_table2244
+ GCC_except_table2246
+ GCC_except_table2248
+ GCC_except_table2250
+ GCC_except_table2256
+ GCC_except_table2479
+ GCC_except_table2482
+ GCC_except_table2496
+ GCC_except_table2528
+ GCC_except_table2541
+ GCC_except_table2544
+ GCC_except_table2545
+ GCC_except_table2548
+ GCC_except_table2571
+ GCC_except_table2573
+ GCC_except_table2575
+ GCC_except_table2577
+ GCC_except_table2737
+ GCC_except_table2755
+ GCC_except_table2756
+ GCC_except_table2812
+ GCC_except_table2814
+ GCC_except_table2817
+ GCC_except_table2818
+ GCC_except_table2842
+ GCC_except_table2844
+ GCC_except_table2852
+ GCC_except_table2854
+ GCC_except_table2861
+ GCC_except_table2862
+ GCC_except_table2863
+ GCC_except_table2865
+ GCC_except_table2866
+ GCC_except_table2867
+ GCC_except_table2868
+ GCC_except_table2869
+ GCC_except_table2921
+ GCC_except_table2945
+ GCC_except_table2954
+ GCC_except_table2957
+ GCC_except_table2960
+ GCC_except_table2963
+ GCC_except_table3028
+ GCC_except_table3029
+ GCC_except_table3073
+ GCC_except_table3080
+ GCC_except_table3081
+ GCC_except_table3082
+ GCC_except_table3085
+ GCC_except_table3086
+ GCC_except_table3087
+ GCC_except_table3089
+ GCC_except_table3097
+ GCC_except_table3105
+ GCC_except_table3106
+ GCC_except_table3124
+ GCC_except_table3131
+ GCC_except_table3135
+ GCC_except_table3138
+ GCC_except_table3141
+ GCC_except_table3180
+ GCC_except_table3184
+ GCC_except_table3188
+ GCC_except_table3193
+ GCC_except_table3201
+ GCC_except_table3205
+ GCC_except_table3214
+ GCC_except_table3216
+ GCC_except_table3448
+ GCC_except_table3452
+ GCC_except_table3456
+ GCC_except_table3463
+ GCC_except_table3467
+ GCC_except_table3473
+ GCC_except_table3480
+ GCC_except_table3504
+ GCC_except_table3506
+ GCC_except_table3508
+ GCC_except_table3511
+ GCC_except_table3512
+ GCC_except_table3514
+ GCC_except_table3517
+ GCC_except_table3599
+ GCC_except_table3604
+ GCC_except_table3616
+ GCC_except_table3619
+ GCC_except_table3621
+ GCC_except_table3624
+ GCC_except_table3631
+ GCC_except_table3684
+ GCC_except_table3765
+ GCC_except_table3768
+ GCC_except_table3882
+ GCC_except_table3883
+ GCC_except_table3885
+ GCC_except_table3890
+ GCC_except_table3894
+ GCC_except_table3897
+ GCC_except_table3899
+ GCC_except_table3907
+ GCC_except_table4106
+ GCC_except_table4109
+ GCC_except_table4121
+ GCC_except_table419
+ GCC_except_table4193
+ GCC_except_table4212
+ GCC_except_table422
+ GCC_except_table424
+ GCC_except_table4299
+ GCC_except_table430
+ GCC_except_table432
+ GCC_except_table434
+ GCC_except_table4414
+ GCC_except_table4419
+ GCC_except_table4420
+ GCC_except_table4428
+ GCC_except_table4430
+ GCC_except_table4455
+ GCC_except_table4457
+ GCC_except_table4458
+ GCC_except_table4518
+ GCC_except_table4528
+ GCC_except_table4593
+ GCC_except_table4595
+ GCC_except_table4597
+ GCC_except_table4639
+ GCC_except_table4642
+ GCC_except_table4643
+ GCC_except_table4717
+ GCC_except_table4804
+ GCC_except_table4805
+ GCC_except_table4811
+ GCC_except_table4813
+ GCC_except_table4842
+ GCC_except_table4844
+ GCC_except_table4863
+ GCC_except_table4909
+ GCC_except_table4959
+ GCC_except_table5045
+ GCC_except_table5065
+ GCC_except_table5066
+ GCC_except_table5067
+ GCC_except_table5069
+ GCC_except_table5072
+ GCC_except_table5073
+ GCC_except_table5075
+ GCC_except_table5281
+ GCC_except_table5287
+ GCC_except_table5289
+ GCC_except_table5299
+ GCC_except_table5300
+ GCC_except_table5547
+ GCC_except_table5656
+ GCC_except_table5662
+ GCC_except_table5669
+ GCC_except_table5674
+ GCC_except_table572
+ GCC_except_table575
+ GCC_except_table5750
+ GCC_except_table5756
+ GCC_except_table5758
+ GCC_except_table580
+ GCC_except_table583
+ GCC_except_table584
+ GCC_except_table5895
+ GCC_except_table6052
+ GCC_except_table6053
+ GCC_except_table606
+ GCC_except_table6080
+ GCC_except_table6094
+ GCC_except_table6109
+ GCC_except_table6116
+ GCC_except_table6119
+ GCC_except_table6133
+ GCC_except_table6138
+ GCC_except_table6172
+ GCC_except_table6183
+ GCC_except_table6189
+ GCC_except_table6193
+ GCC_except_table6201
+ GCC_except_table6206
+ GCC_except_table6220
+ GCC_except_table6225
+ GCC_except_table6233
+ GCC_except_table6235
+ GCC_except_table6238
+ GCC_except_table6243
+ GCC_except_table6250
+ GCC_except_table6255
+ GCC_except_table6259
+ GCC_except_table6287
+ GCC_except_table6293
+ GCC_except_table6318
+ GCC_except_table6323
+ GCC_except_table6327
+ GCC_except_table6356
+ GCC_except_table6362
+ GCC_except_table6363
+ GCC_except_table640
+ GCC_except_table6501
+ GCC_except_table6507
+ GCC_except_table6609
+ GCC_except_table6614
+ GCC_except_table6622
+ GCC_except_table6667
+ GCC_except_table6669
+ GCC_except_table6681
+ GCC_except_table6692
+ GCC_except_table6718
+ GCC_except_table6727
+ GCC_except_table6734
+ GCC_except_table6737
+ GCC_except_table6740
+ GCC_except_table6743
+ GCC_except_table6746
+ GCC_except_table6755
+ GCC_except_table6765
+ GCC_except_table6789
+ GCC_except_table679
+ GCC_except_table6792
+ GCC_except_table6795
+ GCC_except_table6801
+ GCC_except_table6804
+ GCC_except_table6807
+ GCC_except_table6810
+ GCC_except_table6813
+ GCC_except_table6816
+ GCC_except_table6819
+ GCC_except_table682
+ GCC_except_table6822
+ GCC_except_table6825
+ GCC_except_table6828
+ GCC_except_table683
+ GCC_except_table6831
+ GCC_except_table6834
+ GCC_except_table6837
+ GCC_except_table6841
+ GCC_except_table6853
+ GCC_except_table6854
+ GCC_except_table6862
+ GCC_except_table6879
+ GCC_except_table6881
+ GCC_except_table6906
+ GCC_except_table6920
+ GCC_except_table6922
+ GCC_except_table6942
+ GCC_except_table6946
+ GCC_except_table7075
+ GCC_except_table7281
+ GCC_except_table7351
+ GCC_except_table7452
+ GCC_except_table7457
+ GCC_except_table7468
+ GCC_except_table748
+ GCC_except_table751
+ GCC_except_table752
+ GCC_except_table753
+ GCC_except_table754
+ GCC_except_table7544
+ GCC_except_table755
+ GCC_except_table7562
+ GCC_except_table757
+ GCC_except_table7570
+ GCC_except_table7572
+ GCC_except_table7573
+ GCC_except_table758
+ GCC_except_table765
+ GCC_except_table766
+ GCC_except_table7704
+ GCC_except_table7707
+ GCC_except_table7718
+ GCC_except_table7721
+ GCC_except_table7723
+ GCC_except_table7726
+ GCC_except_table7759
+ GCC_except_table7777
+ GCC_except_table7787
+ GCC_except_table7789
+ GCC_except_table7791
+ GCC_except_table7798
+ GCC_except_table7806
+ GCC_except_table7808
+ GCC_except_table7809
+ GCC_except_table7819
+ GCC_except_table7820
+ GCC_except_table7821
+ GCC_except_table7832
+ GCC_except_table7834
+ GCC_except_table7877
+ GCC_except_table7879
+ GCC_except_table7887
+ GCC_except_table7889
+ GCC_except_table7891
+ GCC_except_table7893
+ GCC_except_table7895
+ GCC_except_table7901
+ GCC_except_table7905
+ GCC_except_table7917
+ GCC_except_table7919
+ GCC_except_table7921
+ GCC_except_table7923
+ GCC_except_table7942
+ GCC_except_table8092
+ GCC_except_table8094
+ GCC_except_table8095
+ GCC_except_table8096
+ GCC_except_table8098
+ GCC_except_table8100
+ GCC_except_table8101
+ GCC_except_table8102
+ GCC_except_table8138
+ GCC_except_table8141
+ GCC_except_table8142
+ GCC_except_table8145
+ GCC_except_table8148
+ GCC_except_table8149
+ GCC_except_table8193
+ GCC_except_table8194
+ GCC_except_table8195
+ GCC_except_table8202
+ GCC_except_table8203
+ GCC_except_table8205
+ GCC_except_table8267
+ GCC_except_table8268
+ GCC_except_table8269
+ GCC_except_table8306
+ GCC_except_table8488
+ GCC_except_table8489
+ GCC_except_table8490
+ GCC_except_table8494
+ GCC_except_table8549
+ GCC_except_table8570
+ GCC_except_table8641
+ GCC_except_table8647
+ GCC_except_table8649
+ GCC_except_table8651
+ GCC_except_table8653
+ GCC_except_table8661
+ GCC_except_table8710
+ GCC_except_table8711
+ GCC_except_table8713
+ GCC_except_table8738
+ GCC_except_table8766
+ GCC_except_table8924
+ GCC_except_table8983
+ GCC_except_table8988
+ GCC_except_table8993
+ GCC_except_table8997
+ GCC_except_table9010
+ GCC_except_table9013
+ GCC_except_table9016
+ GCC_except_table9018
+ GCC_except_table9048
+ GCC_except_table9069
+ GCC_except_table9108
+ GCC_except_table9112
+ GCC_except_table9114
+ GCC_except_table9116
+ GCC_except_table9175
+ GCC_except_table9202
+ GCC_except_table9205
+ GCC_except_table9207
+ GCC_except_table9209
+ GCC_except_table9211
+ GCC_except_table9213
+ GCC_except_table9219
+ GCC_except_table9221
+ GCC_except_table9227
+ GCC_except_table9231
+ GCC_except_table9234
+ GCC_except_table9241
+ GCC_except_table9245
+ GCC_except_table9251
+ GCC_except_table9257
+ GCC_except_table9260
+ GCC_except_table9268
+ GCC_except_table9269
+ GCC_except_table9282
+ GCC_except_table9296
+ GCC_except_table9507
+ GCC_except_table9520
+ GCC_except_table9569
+ GCC_except_table9570
+ GCC_except_table9572
+ GCC_except_table9576
+ GCC_except_table9580
+ GCC_except_table9636
+ GCC_except_table9639
+ GCC_except_table9640
+ GCC_except_table967
+ GCC_except_table971
+ GCC_except_table978
+ GCC_except_table9950
+ GCC_except_table9989
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._softwareUpdateDescriptor
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._softwareUpdateProgress
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoDiagnosticInfo._lastSetupInfo
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._accessoryAddMSHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._accountSettleWaitMSHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._controllerKeyExchangeMSHH1
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._currentDeviceIDSWaitMSHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._eventRouterFirstEventPushMSHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._eventRouterServerConnectionMSHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._firstCoreDataImportMSHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._has
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._homeManagerReadyMSHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._iCloudAvailableINT
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._iDSAvailableINT
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._lastKnownStageErrorCode
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._lastKnownStageErrorDomain
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._lastKnownStageErrorString
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._lastKnownStageUnderlyingErrorCode
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._lastKnownStageUnderlyingErrorDomain
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._manateeAvailableINT
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._networkAvailableINT
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._newAccessoryTransferMSHH1
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._pairingIdentityCreationMSHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._primaryResidentElectionMSHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._savedEventState
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._sentinelZoneFetchMSHH1
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._sessionSetupCloseMSHH1
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._sessionSetupOpenMSHH1
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._settingsCreationMSHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._siriReadyMSHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._totalDurationMSHH1
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._totalDurationMSHH2
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._version
+ OBJC_IVAR_$_HMProtoAccessoryCapabilities._supportsInstallManagedConfigurationProfile
+ OBJC_IVAR_$_HMProtoResidentCapabilities._supportsEventLog
+ _CoreAnalyticsLibraryCore.frameworkLibrary.35973
+ _HMAccessoryDiagnosticInfoProtoSetupInfoReadFrom
+ _HMAccessoryInstallManagedConfigurationProfileMessage
+ _HMAccessoryManagedConfigurationProfileDataMessageKey
+ _HMAccessoryUUIDsAsStringForAccessories
+ _HMHomeManagerDiagnosticInfoAccessoryUUIDMessageKey
+ _HMHomeManagerDiagnosticInfoAdditionalFetchKeysMessageKey
+ _HMHomeManagerDiagnosticInfoAdditionalFetchOptionSetupMetricKey
+ _HMHomeManagerDiagnosticInfoDataKey
+ _HMHomeManagerDiagnosticInfoFetchOptionsMessageKey
+ _HMHomeSetPreferredPrimaryMessage
+ _HMHomeSetPreferredPrimaryMessageKeyIdentifier
+ _HMHomeSetPreferredPrimaryMessageKeyOneTime
+ _HMHomeSetPreferredPrimaryMessageKeyTriggerElection
+ _HMSoftwareUpdateNextPermittedRequestDocumentationDateKey
+ _IDSFoundationLibraryCore.39539
+ _IDSFoundationLibraryCore.frameworkLibrary.39541
+ _OBJC_CLASS_$_HMAccessoryDiagnosticInfoProtoSetupInfo
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._currentAccessoryMediaRouteId
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._softwareUpdateDescriptor
+ _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._softwareUpdateProgress
+ _OBJC_IVAR_$_HMSoftwareUpdate._nextPermittedRequestDocumentationDate
+ _OBJC_IVAR_$_HMThreadNetworkMetadata._operationalDataset
+ _OBJC_IVAR_$___HMHomeDataSyncOperation._logIdentifier
+ _OBJC_METACLASS_$_HMAccessoryDiagnosticInfoProtoSetupInfo
+ _UIKitLibrary.39773
+ _UIKitLibraryCore.39767
+ _UIKitLibraryCore.frameworkLibrary.39782
+ __OBJC_$_INSTANCE_METHODS_HMAccessoryDiagnosticInfoProtoSetupInfo
+ __OBJC_$_INSTANCE_VARIABLES_HMAccessoryDiagnosticInfoProtoSetupInfo
+ __OBJC_$_PROP_LIST_HMAccessoryDiagnosticInfoProtoSetupInfo
+ __OBJC_$_PROP_LIST_HMApplicationData.11455
+ __OBJC_$_PROP_LIST_HMResidentCapabilities.195
+ __OBJC_CLASS_PROTOCOLS_$_HMAccessoryDiagnosticInfoProtoSetupInfo
+ __OBJC_CLASS_RO_$_HMAccessoryDiagnosticInfoProtoSetupInfo
+ __OBJC_METACLASS_RO_$_HMAccessoryDiagnosticInfoProtoSetupInfo
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.737
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.739
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.740
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.743
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.747
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.749
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.742
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.745
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.748
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.750
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_3.746
+ ___22-[HMHome _mergeRooms:]_block_invoke.739
+ ___22-[HMHome _mergeRooms:]_block_invoke.740
+ ___22-[HMHome _mergeRooms:]_block_invoke.742
+ ___22-[HMHome _mergeRooms:]_block_invoke_2.744
+ ___22-[HMHome _mergeRooms:]_block_invoke_3.745
+ ___22-[HMHome _mergeUsers:]_block_invoke.785
+ ___22-[HMHome _mergeUsers:]_block_invoke.786
+ ___22-[HMHome _mergeUsers:]_block_invoke.788
+ ___22-[HMHome _mergeUsers:]_block_invoke_2.790
+ ___22-[HMHome _mergeUsers:]_block_invoke_3.791
+ ___22-[HMHome _mergeZones:]_block_invoke.747
+ ___22-[HMHome _mergeZones:]_block_invoke.748
+ ___22-[HMHome _mergeZones:]_block_invoke.750
+ ___22-[HMHome _mergeZones:]_block_invoke_2.752
+ ___22-[HMHome _mergeZones:]_block_invoke_3.753
+ ___25-[HMHome _mergeTriggers:]_block_invoke.781
+ ___25-[HMHome _mergeTriggers:]_block_invoke.783
+ ___27-[HMHome _mergeActionSets:]_block_invoke.772
+ ___27-[HMHome _mergeActionSets:]_block_invoke.773
+ ___27-[HMHome _mergeActionSets:]_block_invoke.775
+ ___27-[HMHome _mergeActionSets:]_block_invoke_2.777
+ ___27-[HMHome _mergeActionSets:]_block_invoke_3.778
+ ___28-[HMHome _mergeAccessories:]_block_invoke.755
+ ___28-[HMHome _mergeAccessories:]_block_invoke.756
+ ___28-[HMHome _mergeAccessories:]_block_invoke.758
+ ___28-[HMHome _mergeAccessories:]_block_invoke.759
+ ___28-[HMHome _mergeAccessories:]_block_invoke.761
+ ___28-[HMHome _mergeAccessories:]_block_invoke_2.762
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.525
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.529
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.533
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.535
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.539
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.559
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.563
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.567
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.718
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.721
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.729
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.732
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.735
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.526
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.530
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.534
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.536
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.540
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.560
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.564
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.568
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.719
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.722
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.730
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.733
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.736
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_3.724
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_4.725
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_5.726
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_6.727
+ ___29-[HMUser mergeFromNewObject:]_block_invoke.296
+ ___29-[HMUser mergeFromNewObject:]_block_invoke.301
+ ___29-[HMUser mergeFromNewObject:]_block_invoke_2.297
+ ___29-[HMUser mergeFromNewObject:]_block_invoke_2.302
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1105
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1106
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1108
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1112
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1110
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1113
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_3.1111
+ ___30-[HMAccessory _mergeServices:]_block_invoke.926
+ ___30-[HMAccessory _mergeServices:]_block_invoke.928
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke.764
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke.765
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke.767
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke_2.769
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke_3.770
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke.793
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke.794
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke.796
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke_2.798
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke_3.799
+ ___33-[__HMHomeDataSyncOperation main]_block_invoke.7
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1088
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1091
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1093
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1094
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1095
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1096
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1097
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1098
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1100
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1102
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1103
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.931
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.935
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.941
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.944
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.950
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.953
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.955
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.960
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.964
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1082
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1089
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1092
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1101
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.932
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.936
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.942
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.945
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.951
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.954
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.956
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.961
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.965
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.957
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.962
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.967
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.968
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.969
+ ___36-[HMHome _mergeOutgoingInvitations:]_block_invoke.801
+ ___36-[HMHome _mergeOutgoingInvitations:]_block_invoke.803
+ ___38-[HMHomeManager _updateDataSyncState:]_block_invoke.489
+ ___39-[HMHome _mergeTriggerOwnedActionSets:]_block_invoke.779
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.752
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.754
+ ___39-[HMSoftwareUpdate mergeFromNewObject:]_block_invoke.170
+ ___39-[HMSoftwareUpdate mergeFromNewObject:]_block_invoke.172
+ ___39-[HMSoftwareUpdate mergeFromNewObject:]_block_invoke_2.171
+ ___39-[HMSoftwareUpdate mergeFromNewObject:]_block_invoke_2.173
+ ___40-[HMSoftwareUpdate requestDocumentation]_block_invoke.158
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.805
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.806
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.807
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.808
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.810
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke_2.809
+ ___43-[HMHome fetchPresenceForUsers:completion:]_block_invoke.819
+ ___43-[HMHome fetchPresenceForUsers:completion:]_block_invoke.821
+ ___44-[HMHome _handleAccessoryAddedNotification:]_block_invoke.890
+ ___44-[HMUser _mergeWithNewAccessoryInvitations:]_block_invoke.293
+ ___45-[HMAccessory _handleCharacteristicsUpdated:]_block_invoke.1124
+ ___47-[HMHomeManager _recomputeAssistantIdentifiers]_block_invoke.661
+ ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1125
+ ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1126
+ ___50-[HMSoftwareUpdate updateState:completionHandler:]_block_invoke.147
+ ___50-[HMSoftwareUpdate updateState:completionHandler:]_block_invoke.149
+ ___51-[HMHomeManager _updatePrimaryHome:notifyDelegate:]_block_invoke.721
+ ___52-[HMHome(HMUser) _manageUsersWithCompletionHandler:]_block_invoke.1702
+ ___54-[HMHome _notifyDelegateOfAccessControlUpdateForUser:]_block_invoke.926
+ ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.582
+ ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.583
+ ___58-[HMHomeManager __resolveAccountHandle:completionHandler:]_block_invoke.648
+ ___60-[HMDeviceSetupOperation initWithSession:sessionIdentifier:]_block_invoke
+ ___61-[HMAccessory _notifyClientsOfSymptomsHandlerAddedOrRemoved:]_block_invoke.1140
+ ___61-[HMHomeManager __removeAccountWithHandle:completionHandler:]_block_invoke.650
+ ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.860
+ ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.862
+ ___63-[HMUser updateAnnounceUserSettings:forHome:completionHandler:]_block_invoke.217
+ ___63-[HMUser updateAnnounceUserSettings:forHome:completionHandler:]_block_invoke.218
+ ___64-[HMHome(HMMediaProfile) updateMediaPassword:completionHandler:]_block_invoke.1777
+ ___65-[HMHomeManager __removeAccountWithIdentifier:completionHandler:]_block_invoke.649
+ ___65-[HMUser updateAssistantAccessControl:forHome:completionHandler:]_block_invoke.150
+ ___66-[HMSoftwareUpdate updateDocumentationMetadata:completionHandler:]_block_invoke.157
+ ___67-[HMHome _addEventTriggerFromResponse:withEventTrigger:completion:]_block_invoke.883
+ ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.679
+ ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.683
+ ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.685
+ ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.687
+ ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke_2.688
+ ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.805
+ ___72-[HMHome setPreferredPrimary:oneTime:triggerElection:completionHandler:]_block_invoke
+ ___74-[HMHomeManager __processSyncResponse:refreshRequested:completionHandler:]_block_invoke.658
+ ___75-[HMHome(HMAccessory) addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.1565
+ ___75-[HMUser updateMediaContentProfileAccessControl:forHome:completionHandler:]_block_invoke.219
+ ___75-[HMUser updateMediaContentProfileAccessControl:forHome:completionHandler:]_block_invoke.220
+ ___76-[HMAccessory installManagedConfigurationProfileWithData:completionHandler:]_block_invoke
+ ___76-[HMUser updateUserListeningHistoryUpdateControl:forHome:completionHandler:]_block_invoke.221
+ ___76-[HMUser updateUserListeningHistoryUpdateControl:forHome:completionHandler:]_block_invoke.222
+ ___88-[HMHome(HMAccessory) addAccessoryWithAccessorySetupPayload:progress:completionHandler:]_block_invoke.1576
+ ___88-[HMHome(HMAccessory) addAndSetUpNewAccessoriesWithSuggestedRoomName:completionHandler:]_block_invoke.1567
+ ___88-[HMHome(HomeLocationFeedback) retrieveHomeKitLocationForFeedbackWithCompletionHandler:]_block_invoke.1862
+ ___89-[HMHome(NetworkRouter) updateAccessoryNetworkProtectionGroup:protectionMode:completion:]_block_invoke.1832
+ ___93-[HMHomeManager _pingDeviceWithUUID:monitor:secure:restrictToLocalNetwork:completionHandler:]_block_invoke.651
+ ___Block_byref_object_copy_.14413
+ ___Block_byref_object_copy_.14726
+ ___Block_byref_object_copy_.21405
+ ___Block_byref_object_copy_.23476
+ ___Block_byref_object_copy_.27603
+ ___Block_byref_object_copy_.29351
+ ___Block_byref_object_copy_.35860
+ ___Block_byref_object_copy_.38707
+ ___Block_byref_object_copy_.39768
+ ___Block_byref_object_copy_.59879
+ ___Block_byref_object_dispose_.14414
+ ___Block_byref_object_dispose_.14727
+ ___Block_byref_object_dispose_.21406
+ ___Block_byref_object_dispose_.23477
+ ___Block_byref_object_dispose_.27604
+ ___Block_byref_object_dispose_.29352
+ ___Block_byref_object_dispose_.35861
+ ___Block_byref_object_dispose_.38708
+ ___Block_byref_object_dispose_.39769
+ ___Block_byref_object_dispose_.59880
+ ___CoreAnalyticsLibraryCore_block_invoke.35974
+ ___IDSFoundationLibraryCore_block_invoke.39542
+ ___UIKitLibraryCore_block_invoke.39783
+ _____HMHomeManagerRegisterForNotifications_block_invoke.1364
+ ___block_descriptor_40_e8_32s_e62_"HMDeviceSetupSession"16?0"<HMDeviceSetupSessionDelegate>"8ls32l8
+ ___block_literal_global.101.35981
+ ___block_literal_global.10527
+ ___block_literal_global.11516
+ ___block_literal_global.1197
+ ___block_literal_global.12.45532
+ ___block_literal_global.121.48471
+ ___block_literal_global.12485
+ ___block_literal_global.12632
+ ___block_literal_global.13086
+ ___block_literal_global.13279
+ ___block_literal_global.13846
+ ___block_literal_global.14179
+ ___block_literal_global.14497
+ ___block_literal_global.15091
+ ___block_literal_global.1584
+ ___block_literal_global.16148
+ ___block_literal_global.16679
+ ___block_literal_global.16870
+ ___block_literal_global.17.17802
+ ___block_literal_global.17002
+ ___block_literal_global.17164
+ ___block_literal_global.1730
+ ___block_literal_global.175.16178
+ ___block_literal_global.1774
+ ___block_literal_global.17809
+ ___block_literal_global.18476
+ ___block_literal_global.18881
+ ___block_literal_global.19.14164
+ ___block_literal_global.192.22699
+ ___block_literal_global.19432
+ ___block_literal_global.19756
+ ___block_literal_global.20788
+ ___block_literal_global.21443
+ ___block_literal_global.21716
+ ___block_literal_global.2199
+ ___block_literal_global.22201
+ ___block_literal_global.22420
+ ___block_literal_global.22705
+ ___block_literal_global.22840
+ ___block_literal_global.23086
+ ___block_literal_global.23337
+ ___block_literal_global.23500
+ ___block_literal_global.23592
+ ___block_literal_global.26107
+ ___block_literal_global.26242
+ ___block_literal_global.26717
+ ___block_literal_global.27465
+ ___block_literal_global.27761
+ ___block_literal_global.28100
+ ___block_literal_global.28312
+ ___block_literal_global.28590
+ ___block_literal_global.28664
+ ___block_literal_global.29533
+ ___block_literal_global.29889
+ ___block_literal_global.30.17792
+ ___block_literal_global.30.7709
+ ___block_literal_global.30160
+ ___block_literal_global.30996
+ ___block_literal_global.31364
+ ___block_literal_global.32547
+ ___block_literal_global.33.59223
+ ___block_literal_global.33373
+ ___block_literal_global.33604
+ ___block_literal_global.33827
+ ___block_literal_global.34776
+ ___block_literal_global.35968
+ ___block_literal_global.36218
+ ___block_literal_global.3646
+ ___block_literal_global.36554
+ ___block_literal_global.37179
+ ___block_literal_global.37981
+ ___block_literal_global.38106
+ ___block_literal_global.38378
+ ___block_literal_global.3846
+ ___block_literal_global.3937
+ ___block_literal_global.39605
+ ___block_literal_global.39699
+ ___block_literal_global.40408
+ ___block_literal_global.40597
+ ___block_literal_global.41224
+ ___block_literal_global.41850
+ ___block_literal_global.42264
+ ___block_literal_global.42583
+ ___block_literal_global.43258
+ ___block_literal_global.44144
+ ___block_literal_global.445
+ ___block_literal_global.45254
+ ___block_literal_global.45544
+ ___block_literal_global.45810
+ ___block_literal_global.46004
+ ___block_literal_global.46233
+ ___block_literal_global.46938
+ ___block_literal_global.47057
+ ___block_literal_global.474
+ ___block_literal_global.47788
+ ___block_literal_global.479
+ ___block_literal_global.48225
+ ___block_literal_global.48559
+ ___block_literal_global.49472
+ ___block_literal_global.5108
+ ___block_literal_global.52078
+ ___block_literal_global.52781
+ ___block_literal_global.54037
+ ___block_literal_global.54671
+ ___block_literal_global.5504
+ ___block_literal_global.55202
+ ___block_literal_global.55514
+ ___block_literal_global.56011
+ ___block_literal_global.56183
+ ___block_literal_global.5640
+ ___block_literal_global.56571
+ ___block_literal_global.56815
+ ___block_literal_global.58461
+ ___block_literal_global.58627
+ ___block_literal_global.58964
+ ___block_literal_global.59229
+ ___block_literal_global.59589
+ ___block_literal_global.59877
+ ___block_literal_global.60171
+ ___block_literal_global.6158
+ ___block_literal_global.632
+ ___block_literal_global.6639
+ ___block_literal_global.6913
+ ___block_literal_global.700
+ ___block_literal_global.702
+ ___block_literal_global.73.21694
+ ___block_literal_global.7374
+ ___block_literal_global.7491
+ ___block_literal_global.75.36171
+ ___block_literal_global.76.25874
+ ___block_literal_global.7727
+ ___block_literal_global.809
+ ___block_literal_global.8183
+ ___block_literal_global.84.59891
+ ___block_literal_global.863
+ ___block_literal_global.8666
+ ___block_literal_global.888
+ ___block_literal_global.8947
+ ___block_literal_global.9124
+ ___block_literal_global.9552
+ ___block_literal_global.957
+ ___block_literal_global.959
+ ___block_literal_global.962
+ ___block_literal_global.9815
+ ___getAnalyticsSendEventLazySymbolLoc_block_invoke.35971
+ ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.39778
+ ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.39772
+ __unnamed_array_storage.14430
+ __unnamed_array_storage.22612
+ __unnamed_array_storage.227.26021
+ __unnamed_array_storage.239.26020
+ __unnamed_array_storage.251.26024
+ __unnamed_array_storage.26097
+ __unnamed_array_storage.29230
+ __unnamed_array_storage.54159
+ __unnamed_array_storage.55639
+ __unnamed_array_storage.59080
+ _audit_stringCoreAnalytics.35977
+ _audit_stringIDSFoundation.39544
+ _audit_stringUIKit.39785
+ _getAnalyticsSendEventLazySymbolLoc.ptr.35970
+ _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.39777
+ _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.39771
+ _logCategory._hmf_once_t0.12631
+ _logCategory._hmf_once_t0.21715
+ _logCategory._hmf_once_t0.28311
+ _logCategory._hmf_once_t0.28663
+ _logCategory._hmf_once_t0.40407
+ _logCategory._hmf_once_t0.40596
+ _logCategory._hmf_once_t0.41223
+ _logCategory._hmf_once_t0.56814
+ _logCategory._hmf_once_t1.17001
+ _logCategory._hmf_once_t1.18880
+ _logCategory._hmf_once_t1.36194
+ _logCategory._hmf_once_t1.41849
+ _logCategory._hmf_once_t1.45531
+ _logCategory._hmf_once_t1.47056
+ _logCategory._hmf_once_t1.52077
+ _logCategory._hmf_once_t15.56570
+ _logCategory._hmf_once_t16.33603
+ _logCategory._hmf_once_t16.58626
+ _logCategory._hmf_once_t17.37973
+ _logCategory._hmf_once_t19.13305
+ _logCategory._hmf_once_t2.26241
+ _logCategory._hmf_once_t2.29888
+ _logCategory._hmf_once_t20.5639
+ _logCategory._hmf_once_t22.23085
+ _logCategory._hmf_once_t24.36548
+ _logCategory._hmf_once_t25.23336
+ _logCategory._hmf_once_t25.59588
+ _logCategory._hmf_once_t26.48306
+ _logCategory._hmf_once_t27.47787
+ _logCategory._hmf_once_t27.55513
+ _logCategory._hmf_once_t3.38105
+ _logCategory._hmf_once_t3.59222
+ _logCategory._hmf_once_t31.21442
+ _logCategory._hmf_once_t31.58460
+ _logCategory._hmf_once_t313
+ _logCategory._hmf_once_t33.48584
+ _logCategory._hmf_once_t339
+ _logCategory._hmf_once_t34.14492
+ _logCategory._hmf_once_t34.18475
+ _logCategory._hmf_once_t35.34775
+ _logCategory._hmf_once_t4.1208
+ _logCategory._hmf_once_t4.5503
+ _logCategory._hmf_once_t52
+ _logCategory._hmf_once_t6.30995
+ _logCategory._hmf_once_t6.33372
+ _logCategory._hmf_once_t6.52780
+ _logCategory._hmf_once_t64.54036
+ _logCategory._hmf_once_t7.23591
+ _logCategory._hmf_once_t7.46937
+ _logCategory._hmf_once_t8.33826
+ _logCategory._hmf_once_t8.43257
+ _logCategory._hmf_once_t8.46022
+ _logCategory._hmf_once_v1.12633
+ _logCategory._hmf_once_v1.21717
+ _logCategory._hmf_once_v1.28313
+ _logCategory._hmf_once_v1.28665
+ _logCategory._hmf_once_v1.40409
+ _logCategory._hmf_once_v1.40598
+ _logCategory._hmf_once_v1.41225
+ _logCategory._hmf_once_v1.56816
+ _logCategory._hmf_once_v16.56572
+ _logCategory._hmf_once_v17.33605
+ _logCategory._hmf_once_v17.58628
+ _logCategory._hmf_once_v18.37974
+ _logCategory._hmf_once_v2.17003
+ _logCategory._hmf_once_v2.18882
+ _logCategory._hmf_once_v2.36195
+ _logCategory._hmf_once_v2.41851
+ _logCategory._hmf_once_v2.45533
+ _logCategory._hmf_once_v2.47058
+ _logCategory._hmf_once_v2.52079
+ _logCategory._hmf_once_v20.13306
+ _logCategory._hmf_once_v21.5641
+ _logCategory._hmf_once_v23.23087
+ _logCategory._hmf_once_v25.36549
+ _logCategory._hmf_once_v26.23338
+ _logCategory._hmf_once_v26.59590
+ _logCategory._hmf_once_v27.48307
+ _logCategory._hmf_once_v28.47789
+ _logCategory._hmf_once_v28.55515
+ _logCategory._hmf_once_v3.26243
+ _logCategory._hmf_once_v3.29890
+ _logCategory._hmf_once_v314
+ _logCategory._hmf_once_v32.21444
+ _logCategory._hmf_once_v32.58462
+ _logCategory._hmf_once_v34.48585
+ _logCategory._hmf_once_v340
+ _logCategory._hmf_once_v35.14493
+ _logCategory._hmf_once_v35.18477
+ _logCategory._hmf_once_v36.34777
+ _logCategory._hmf_once_v4.38107
+ _logCategory._hmf_once_v4.59224
+ _logCategory._hmf_once_v5.1209
+ _logCategory._hmf_once_v5.5505
+ _logCategory._hmf_once_v53
+ _logCategory._hmf_once_v65.54038
+ _logCategory._hmf_once_v7.30997
+ _logCategory._hmf_once_v7.33374
+ _logCategory._hmf_once_v7.52782
+ _logCategory._hmf_once_v8.23593
+ _logCategory._hmf_once_v8.46939
+ _logCategory._hmf_once_v9.33828
+ _logCategory._hmf_once_v9.43259
+ _logCategory._hmf_once_v9.46023
+ _objc_msgSend$currentAccessoryMediaRouteId
+ _objc_msgSend$hasSoftwareUpdateDescriptor
+ _objc_msgSend$hasSoftwareUpdateProgress
+ _objc_msgSend$hmf_UUIDWithNamespace:data:salts:
+ _objc_msgSend$initWithSession:setupSessionFactory:
+ _objc_msgSend$initWithURL:fileManager:error:
+ _objc_msgSend$nextPermittedRequestDocumentationDate
+ _objc_msgSend$setLastKnownStageErrorDomain:
+ _objc_msgSend$setLastKnownStageErrorString:
+ _objc_msgSend$setLastKnownStageUnderlyingErrorDomain:
+ _objc_msgSend$setLastSetupInfo:
+ _objc_msgSend$setNextPermittedRequestDocumentationDate:
+ _objc_msgSend$setOperationalDataset:
+ _objc_msgSend$setSoftwareUpdateDescriptor:
+ _objc_msgSend$setSoftwareUpdateProgress:
+ _objc_msgSend$setSupportsEventLog:
+ _objc_msgSend$setSupportsInstallManagedConfigurationProfile:
+ _objc_msgSend$softwareUpdateDescriptor
+ _objc_msgSend$softwareUpdateProgress
+ _objc_msgSend$supportsInstallManagedConfigurationProfile
+ _objc_msgSend$syncOperationQueue
+ _sharedInstance.onceToken.37980
+ _sharedManager.onceToken.55656
+ _supportedValueClasses.onceToken.45809
+ _supportedValueClasses.onceToken.54001
+ _supportedValueClasses.supportedValueClasses.45811
+ _supportedValueClasses.supportedValueClasses.54002
+ _unconfigureQueue.onceToken.36553
+ _unconfigureQueue.unconfigureQueue.36555
- +[HMUserHomeAccessSchedule shortDescription]
- +[HMUserHomeAccessSchedule supportsSecureCoding]
- +[HMUserHomeAccessScheduleRule shortDescription]
- +[HMUserHomeAccessScheduleRule supportsSecureCoding]
- +[HMUserHomeAccessSettings shortDescription]
- +[HMUserHomeAccessSettings supportsSecureCoding]
- +[NSUUID(HomeKitClient) hm_uuid:identifierSalt:withSalts:]
- -[HMAccessoryDiagnosticInfo currrentAccessoryMediaRouteId]
- -[HMDeviceSetupOperation initWithSession:setupSession:]
- -[HMHome(HMUser) _inviteWithUserInformation:completionHandler:]
- -[HMMutableUserHomeAccessSchedule copyWithZone:]
- -[HMMutableUserHomeAccessScheduleRule copyWithZone:]
- -[HMMutableUserHomeAccessSettings copyWithZone:]
- -[HMProtoResidentCapabilities hasSupports40e39e789f11ed6f1738]
- -[HMProtoResidentCapabilities setHasSupports40e39e789f11ed6f1738:]
- -[HMProtoResidentCapabilities setSupports40e39e789f11ed6f1738:]
- -[HMProtoResidentCapabilities supports40e39e789f11ed6f1738]
- -[HMUserHomeAccessSchedule .cxx_destruct]
- -[HMUserHomeAccessSchedule attributeDescriptions]
- -[HMUserHomeAccessSchedule copyWithZone:]
- -[HMUserHomeAccessSchedule description]
- -[HMUserHomeAccessSchedule encodeWithCoder:]
- -[HMUserHomeAccessSchedule hash]
- -[HMUserHomeAccessSchedule initWithCoder:]
- -[HMUserHomeAccessSchedule init]
- -[HMUserHomeAccessSchedule isAccessCurrentlyAllowed]
- -[HMUserHomeAccessSchedule isEqual:]
- -[HMUserHomeAccessSchedule isExpired]
- -[HMUserHomeAccessSchedule mutableCopyWithZone:]
- -[HMUserHomeAccessSchedule privateDescription]
- -[HMUserHomeAccessSchedule rules]
- -[HMUserHomeAccessSchedule setRules:]
- -[HMUserHomeAccessSchedule shortDescription]
- -[HMUserHomeAccessSchedule validFrom]
- -[HMUserHomeAccessSchedule validThrough]
- -[HMUserHomeAccessScheduleRule .cxx_destruct]
- -[HMUserHomeAccessScheduleRule attributeDescriptions]
- -[HMUserHomeAccessScheduleRule copyWithZone:]
- -[HMUserHomeAccessScheduleRule daysOfTheWeek]
- -[HMUserHomeAccessScheduleRule description]
- -[HMUserHomeAccessScheduleRule encodeWithCoder:]
- -[HMUserHomeAccessScheduleRule endTime]
- -[HMUserHomeAccessScheduleRule hash]
- -[HMUserHomeAccessScheduleRule initWithCoder:]
- -[HMUserHomeAccessScheduleRule initWithStartTime:endTime:]
- -[HMUserHomeAccessScheduleRule initWithStartTime:endTime:daysOfTheWeek:validFrom:validThrough:]
- -[HMUserHomeAccessScheduleRule isEqual:]
- -[HMUserHomeAccessScheduleRule mutableCopyWithZone:]
- -[HMUserHomeAccessScheduleRule privateDescription]
- -[HMUserHomeAccessScheduleRule setDaysOfTheWeek:]
- -[HMUserHomeAccessScheduleRule setEndTime:]
- -[HMUserHomeAccessScheduleRule setStartTime:]
- -[HMUserHomeAccessScheduleRule setValidFrom:]
- -[HMUserHomeAccessScheduleRule setValidThrough:]
- -[HMUserHomeAccessScheduleRule shortDescription]
- -[HMUserHomeAccessScheduleRule startTime]
- -[HMUserHomeAccessScheduleRule validFrom]
- -[HMUserHomeAccessScheduleRule validThrough]
- -[HMUserHomeAccessSettings .cxx_destruct]
- -[HMUserHomeAccessSettings allowedAccessoryCategoryTypes]
- -[HMUserHomeAccessSettings allowedAccessoryIdentifiers]
- -[HMUserHomeAccessSettings allowedRoomIdentifiers]
- -[HMUserHomeAccessSettings attributeDescriptions]
- -[HMUserHomeAccessSettings copyWithZone:]
- -[HMUserHomeAccessSettings description]
- -[HMUserHomeAccessSettings encodeWithCoder:]
- -[HMUserHomeAccessSettings hash]
- -[HMUserHomeAccessSettings initWithCoder:]
- -[HMUserHomeAccessSettings isAccessAllowedToAllAccessories]
- -[HMUserHomeAccessSettings isEqual:]
- -[HMUserHomeAccessSettings mutableCopyWithZone:]
- -[HMUserHomeAccessSettings privateDescription]
- -[HMUserHomeAccessSettings schedule]
- -[HMUserHomeAccessSettings setAccessAllowedToAllAccessories:]
- -[HMUserHomeAccessSettings setAllowedAccessoryCategoryTypes:]
- -[HMUserHomeAccessSettings setAllowedAccessoryIdentifiers:]
- -[HMUserHomeAccessSettings setAllowedRoomIdentifiers:]
- -[HMUserHomeAccessSettings setSchedule:]
- -[HMUserHomeAccessSettings shortDescription]
- -[HMUserInviteInformation homeAccessSettings]
- -[HMUserInviteInformation initWithUser:administrator:remoteAccess:announceAccess:camerasAccessLevel:homeAccessSettings:]
- -[HMUserInviteInformation setHomeAccessSettings:]
- -[__HMHomeDataSyncOperation initWithHomeManager:timeout:]
- GCC_except_table1005
- GCC_except_table10187
- GCC_except_table10189
- GCC_except_table10191
- GCC_except_table10192
- GCC_except_table10222
- GCC_except_table10224
- GCC_except_table10226
- GCC_except_table10232
- GCC_except_table10233
- GCC_except_table10234
- GCC_except_table10341
- GCC_except_table10369
- GCC_except_table10371
- GCC_except_table10375
- GCC_except_table10376
- GCC_except_table10424
- GCC_except_table10450
- GCC_except_table10463
- GCC_except_table10532
- GCC_except_table10533
- GCC_except_table10534
- GCC_except_table10535
- GCC_except_table10536
- GCC_except_table10537
- GCC_except_table10538
- GCC_except_table10539
- GCC_except_table10541
- GCC_except_table10542
- GCC_except_table10543
- GCC_except_table10544
- GCC_except_table10545
- GCC_except_table10546
- GCC_except_table10563
- GCC_except_table10590
- GCC_except_table10697
- GCC_except_table10698
- GCC_except_table10701
- GCC_except_table10763
- GCC_except_table10765
- GCC_except_table10773
- GCC_except_table10779
- GCC_except_table10780
- GCC_except_table10786
- GCC_except_table10788
- GCC_except_table10793
- GCC_except_table10794
- GCC_except_table10795
- GCC_except_table11022
- GCC_except_table11023
- GCC_except_table1120
- GCC_except_table11202
- GCC_except_table11205
- GCC_except_table11210
- GCC_except_table11214
- GCC_except_table11220
- GCC_except_table11225
- GCC_except_table11227
- GCC_except_table11232
- GCC_except_table11233
- GCC_except_table11235
- GCC_except_table11318
- GCC_except_table11320
- GCC_except_table11339
- GCC_except_table11340
- GCC_except_table11341
- GCC_except_table11342
- GCC_except_table11347
- GCC_except_table11361
- GCC_except_table11367
- GCC_except_table11370
- GCC_except_table11372
- GCC_except_table1142
- GCC_except_table11452
- GCC_except_table11454
- GCC_except_table11465
- GCC_except_table11466
- GCC_except_table11471
- GCC_except_table11477
- GCC_except_table11479
- GCC_except_table11481
- GCC_except_table11483
- GCC_except_table11485
- GCC_except_table11487
- GCC_except_table11621
- GCC_except_table11676
- GCC_except_table11677
- GCC_except_table11678
- GCC_except_table11689
- GCC_except_table11690
- GCC_except_table11714
- GCC_except_table11715
- GCC_except_table11769
- GCC_except_table11794
- GCC_except_table11797
- GCC_except_table11929
- GCC_except_table12049
- GCC_except_table12050
- GCC_except_table12051
- GCC_except_table12099
- GCC_except_table12100
- GCC_except_table12102
- GCC_except_table12105
- GCC_except_table12107
- GCC_except_table12109
- GCC_except_table12184
- GCC_except_table1219
- GCC_except_table1222
- GCC_except_table12252
- GCC_except_table12337
- GCC_except_table12344
- GCC_except_table1236
- GCC_except_table12398
- GCC_except_table12400
- GCC_except_table12409
- GCC_except_table12412
- GCC_except_table12432
- GCC_except_table12435
- GCC_except_table1440
- GCC_except_table1443
- GCC_except_table1512
- GCC_except_table1514
- GCC_except_table1588
- GCC_except_table1589
- GCC_except_table1637
- GCC_except_table1866
- GCC_except_table1869
- GCC_except_table1872
- GCC_except_table1877
- GCC_except_table1881
- GCC_except_table1890
- GCC_except_table1892
- GCC_except_table1895
- GCC_except_table1905
- GCC_except_table1907
- GCC_except_table1908
- GCC_except_table1913
- GCC_except_table1914
- GCC_except_table1915
- GCC_except_table1916
- GCC_except_table2100
- GCC_except_table2102
- GCC_except_table2106
- GCC_except_table2108
- GCC_except_table2110
- GCC_except_table2112
- GCC_except_table2118
- GCC_except_table2341
- GCC_except_table2344
- GCC_except_table2358
- GCC_except_table2390
- GCC_except_table2403
- GCC_except_table2406
- GCC_except_table2407
- GCC_except_table2410
- GCC_except_table2433
- GCC_except_table2435
- GCC_except_table2437
- GCC_except_table2439
- GCC_except_table2599
- GCC_except_table2617
- GCC_except_table2618
- GCC_except_table2674
- GCC_except_table2676
- GCC_except_table2679
- GCC_except_table2680
- GCC_except_table2704
- GCC_except_table2706
- GCC_except_table2714
- GCC_except_table2716
- GCC_except_table2723
- GCC_except_table2724
- GCC_except_table2725
- GCC_except_table2727
- GCC_except_table2728
- GCC_except_table2729
- GCC_except_table2730
- GCC_except_table2731
- GCC_except_table2783
- GCC_except_table2807
- GCC_except_table2810
- GCC_except_table2813
- GCC_except_table2816
- GCC_except_table2819
- GCC_except_table2822
- GCC_except_table2825
- GCC_except_table287
- GCC_except_table2890
- GCC_except_table2891
- GCC_except_table290
- GCC_except_table292
- GCC_except_table2935
- GCC_except_table2942
- GCC_except_table2943
- GCC_except_table2944
- GCC_except_table2947
- GCC_except_table2949
- GCC_except_table2959
- GCC_except_table2967
- GCC_except_table2968
- GCC_except_table298
- GCC_except_table2986
- GCC_except_table2993
- GCC_except_table2997
- GCC_except_table300
- GCC_except_table3000
- GCC_except_table3003
- GCC_except_table302
- GCC_except_table3042
- GCC_except_table3046
- GCC_except_table3050
- GCC_except_table3055
- GCC_except_table3063
- GCC_except_table3067
- GCC_except_table3076
- GCC_except_table3078
- GCC_except_table3310
- GCC_except_table3316
- GCC_except_table3319
- GCC_except_table3323
- GCC_except_table3324
- GCC_except_table3327
- GCC_except_table3333
- GCC_except_table3336
- GCC_except_table3340
- GCC_except_table3364
- GCC_except_table3366
- GCC_except_table3368
- GCC_except_table3371
- GCC_except_table3372
- GCC_except_table3374
- GCC_except_table3377
- GCC_except_table3479
- GCC_except_table3481
- GCC_except_table3484
- GCC_except_table3491
- GCC_except_table3544
- GCC_except_table3610
- GCC_except_table3625
- GCC_except_table3628
- GCC_except_table3742
- GCC_except_table3743
- GCC_except_table3745
- GCC_except_table3754
- GCC_except_table3757
- GCC_except_table3759
- GCC_except_table3767
- GCC_except_table3965
- GCC_except_table3968
- GCC_except_table3980
- GCC_except_table4052
- GCC_except_table4071
- GCC_except_table4158
- GCC_except_table4273
- GCC_except_table4278
- GCC_except_table4279
- GCC_except_table4287
- GCC_except_table4289
- GCC_except_table4314
- GCC_except_table4315
- GCC_except_table4316
- GCC_except_table4317
- GCC_except_table4377
- GCC_except_table4387
- GCC_except_table440
- GCC_except_table443
- GCC_except_table4452
- GCC_except_table4454
- GCC_except_table448
- GCC_except_table4498
- GCC_except_table4501
- GCC_except_table4502
- GCC_except_table451
- GCC_except_table452
- GCC_except_table4576
- GCC_except_table4662
- GCC_except_table4663
- GCC_except_table4669
- GCC_except_table4671
- GCC_except_table4700
- GCC_except_table4702
- GCC_except_table4721
- GCC_except_table474
- GCC_except_table4767
- GCC_except_table4816
- GCC_except_table4899
- GCC_except_table491
- GCC_except_table4919
- GCC_except_table4920
- GCC_except_table4921
- GCC_except_table4923
- GCC_except_table4926
- GCC_except_table4927
- GCC_except_table4929
- GCC_except_table508
- GCC_except_table5135
- GCC_except_table5141
- GCC_except_table5143
- GCC_except_table5153
- GCC_except_table5154
- GCC_except_table5401
- GCC_except_table547
- GCC_except_table550
- GCC_except_table5507
- GCC_except_table551
- GCC_except_table5513
- GCC_except_table5520
- GCC_except_table5525
- GCC_except_table5601
- GCC_except_table5607
- GCC_except_table5609
- GCC_except_table5746
- GCC_except_table5903
- GCC_except_table5904
- GCC_except_table5929
- GCC_except_table5931
- GCC_except_table5937
- GCC_except_table5945
- GCC_except_table5960
- GCC_except_table5967
- GCC_except_table5970
- GCC_except_table5984
- GCC_except_table5989
- GCC_except_table6025
- GCC_except_table6036
- GCC_except_table6042
- GCC_except_table6046
- GCC_except_table6054
- GCC_except_table6059
- GCC_except_table6073
- GCC_except_table6088
- GCC_except_table6091
- GCC_except_table6096
- GCC_except_table6103
- GCC_except_table6108
- GCC_except_table6112
- GCC_except_table613
- GCC_except_table6140
- GCC_except_table6146
- GCC_except_table616
- GCC_except_table617
- GCC_except_table6171
- GCC_except_table6176
- GCC_except_table618
- GCC_except_table6180
- GCC_except_table619
- GCC_except_table620
- GCC_except_table6209
- GCC_except_table6213
- GCC_except_table6215
- GCC_except_table6216
- GCC_except_table622
- GCC_except_table630
- GCC_except_table631
- GCC_except_table6354
- GCC_except_table6440
- GCC_except_table6462
- GCC_except_table6467
- GCC_except_table6475
- GCC_except_table6518
- GCC_except_table6520
- GCC_except_table6522
- GCC_except_table6534
- GCC_except_table6545
- GCC_except_table6571
- GCC_except_table6580
- GCC_except_table6590
- GCC_except_table6593
- GCC_except_table6596
- GCC_except_table6599
- GCC_except_table6607
- GCC_except_table6617
- GCC_except_table6641
- GCC_except_table6644
- GCC_except_table6647
- GCC_except_table6650
- GCC_except_table6653
- GCC_except_table6656
- GCC_except_table6659
- GCC_except_table6662
- GCC_except_table6668
- GCC_except_table6671
- GCC_except_table6674
- GCC_except_table6677
- GCC_except_table6680
- GCC_except_table6683
- GCC_except_table6686
- GCC_except_table6689
- GCC_except_table6693
- GCC_except_table6705
- GCC_except_table6706
- GCC_except_table6714
- GCC_except_table6731
- GCC_except_table6733
- GCC_except_table6758
- GCC_except_table6772
- GCC_except_table6774
- GCC_except_table6794
- GCC_except_table6921
- GCC_except_table7123
- GCC_except_table7217
- GCC_except_table7321
- GCC_except_table7332
- GCC_except_table7408
- GCC_except_table7426
- GCC_except_table7432
- GCC_except_table7434
- GCC_except_table7436
- GCC_except_table7437
- GCC_except_table7571
- GCC_except_table7582
- GCC_except_table7585
- GCC_except_table7587
- GCC_except_table7590
- GCC_except_table7621
- GCC_except_table7623
- GCC_except_table7641
- GCC_except_table7649
- GCC_except_table7651
- GCC_except_table7653
- GCC_except_table7660
- GCC_except_table7666
- GCC_except_table7668
- GCC_except_table7670
- GCC_except_table7671
- GCC_except_table7681
- GCC_except_table7682
- GCC_except_table7683
- GCC_except_table7694
- GCC_except_table7696
- GCC_except_table7698
- GCC_except_table7739
- GCC_except_table7741
- GCC_except_table7749
- GCC_except_table7751
- GCC_except_table7753
- GCC_except_table7755
- GCC_except_table7763
- GCC_except_table7767
- GCC_except_table7779
- GCC_except_table7781
- GCC_except_table7783
- GCC_except_table7954
- GCC_except_table7956
- GCC_except_table7957
- GCC_except_table7958
- GCC_except_table7960
- GCC_except_table7962
- GCC_except_table7963
- GCC_except_table7964
- GCC_except_table8000
- GCC_except_table8003
- GCC_except_table8004
- GCC_except_table8007
- GCC_except_table8010
- GCC_except_table8011
- GCC_except_table8055
- GCC_except_table8056
- GCC_except_table8057
- GCC_except_table8064
- GCC_except_table8065
- GCC_except_table8067
- GCC_except_table8129
- GCC_except_table8130
- GCC_except_table8131
- GCC_except_table8168
- GCC_except_table832
- GCC_except_table8349
- GCC_except_table8350
- GCC_except_table8351
- GCC_except_table8355
- GCC_except_table836
- GCC_except_table8410
- GCC_except_table843
- GCC_except_table8431
- GCC_except_table8502
- GCC_except_table8508
- GCC_except_table8510
- GCC_except_table8512
- GCC_except_table8514
- GCC_except_table8522
- GCC_except_table8571
- GCC_except_table8572
- GCC_except_table8574
- GCC_except_table8599
- GCC_except_table8627
- GCC_except_table866
- GCC_except_table875
- GCC_except_table8785
- GCC_except_table8844
- GCC_except_table8849
- GCC_except_table8854
- GCC_except_table8858
- GCC_except_table8871
- GCC_except_table8874
- GCC_except_table8877
- GCC_except_table8879
- GCC_except_table8909
- GCC_except_table8929
- GCC_except_table8930
- GCC_except_table8931
- GCC_except_table8968
- GCC_except_table8969
- GCC_except_table8973
- GCC_except_table8975
- GCC_except_table8977
- GCC_except_table9036
- GCC_except_table9063
- GCC_except_table9066
- GCC_except_table9072
- GCC_except_table9074
- GCC_except_table9080
- GCC_except_table9082
- GCC_except_table9088
- GCC_except_table9092
- GCC_except_table9095
- GCC_except_table9103
- GCC_except_table9113
- GCC_except_table9119
- GCC_except_table9122
- GCC_except_table9130
- GCC_except_table9131
- GCC_except_table9144
- GCC_except_table9158
- GCC_except_table9369
- GCC_except_table9382
- GCC_except_table943
- GCC_except_table9431
- GCC_except_table9432
- GCC_except_table9434
- GCC_except_table9438
- GCC_except_table9442
- GCC_except_table945
- GCC_except_table948
- GCC_except_table9498
- GCC_except_table950
- GCC_except_table9501
- GCC_except_table9502
- GCC_except_table952
- GCC_except_table956
- GCC_except_table9812
- GCC_except_table9851
- GCC_except_table9864
- OBJC_IVAR_$_HMProtoResidentCapabilities._supports40e39e789f11ed6f1738
- _CC_SHA1_Final
- _CC_SHA1_Init
- _CC_SHA1_Update
- _CoreAnalyticsLibraryCore.frameworkLibrary.35568
- _HHMHomeManagerDiagnosticInfoAccessoryUUIDMessageKey
- _HHMHomeManagerDiagnosticInfoDataKey
- _HHMHomeManagerDiagnosticInfoFetchOptionsMessageKey
- _HMUserHomeAccessSettingsCodingKey
- _IDSFoundationLibraryCore.39158
- _IDSFoundationLibraryCore.frameworkLibrary.39160
- _OBJC_CLASS_$_HMMutableUserHomeAccessSchedule
- _OBJC_CLASS_$_HMMutableUserHomeAccessScheduleRule
- _OBJC_CLASS_$_HMMutableUserHomeAccessSettings
- _OBJC_CLASS_$_HMUserHomeAccessSchedule
- _OBJC_CLASS_$_HMUserHomeAccessScheduleRule
- _OBJC_CLASS_$_HMUserHomeAccessSettings
- _OBJC_IVAR_$_HMAccessoryDiagnosticInfo._currrentAccessoryMediaRouteId
- _OBJC_IVAR_$_HMUserHomeAccessSchedule._rules
- _OBJC_IVAR_$_HMUserHomeAccessScheduleRule._daysOfTheWeek
- _OBJC_IVAR_$_HMUserHomeAccessScheduleRule._endTime
- _OBJC_IVAR_$_HMUserHomeAccessScheduleRule._startTime
- _OBJC_IVAR_$_HMUserHomeAccessScheduleRule._validFrom
- _OBJC_IVAR_$_HMUserHomeAccessScheduleRule._validThrough
- _OBJC_IVAR_$_HMUserHomeAccessSettings._accessAllowedToAllAccessories
- _OBJC_IVAR_$_HMUserHomeAccessSettings._allowedAccessoryCategoryTypes
- _OBJC_IVAR_$_HMUserHomeAccessSettings._allowedAccessoryIdentifiers
- _OBJC_IVAR_$_HMUserHomeAccessSettings._allowedRoomIdentifiers
- _OBJC_IVAR_$_HMUserHomeAccessSettings._schedule
- _OBJC_IVAR_$_HMUserInviteInformation._homeAccessSettings
- _OBJC_METACLASS_$_HMMutableUserHomeAccessSchedule
- _OBJC_METACLASS_$_HMMutableUserHomeAccessScheduleRule
- _OBJC_METACLASS_$_HMMutableUserHomeAccessSettings
- _OBJC_METACLASS_$_HMUserHomeAccessSchedule
- _OBJC_METACLASS_$_HMUserHomeAccessScheduleRule
- _OBJC_METACLASS_$_HMUserHomeAccessSettings
- _UIKitLibrary.39393
- _UIKitLibraryCore.39387
- _UIKitLibraryCore.frameworkLibrary.39402
- __OBJC_$_CLASS_METHODS_HMUserHomeAccessSchedule
- __OBJC_$_CLASS_METHODS_HMUserHomeAccessScheduleRule
- __OBJC_$_CLASS_METHODS_HMUserHomeAccessSettings
- __OBJC_$_CLASS_PROP_LIST_HMUserHomeAccessSchedule
- __OBJC_$_CLASS_PROP_LIST_HMUserHomeAccessScheduleRule
- __OBJC_$_CLASS_PROP_LIST_HMUserHomeAccessSettings
- __OBJC_$_INSTANCE_METHODS_HMMutableUserHomeAccessSchedule
- __OBJC_$_INSTANCE_METHODS_HMMutableUserHomeAccessScheduleRule
- __OBJC_$_INSTANCE_METHODS_HMMutableUserHomeAccessSettings
- __OBJC_$_INSTANCE_METHODS_HMUserHomeAccessSchedule
- __OBJC_$_INSTANCE_METHODS_HMUserHomeAccessScheduleRule
- __OBJC_$_INSTANCE_METHODS_HMUserHomeAccessSettings
- __OBJC_$_INSTANCE_VARIABLES_HMUserHomeAccessSchedule
- __OBJC_$_INSTANCE_VARIABLES_HMUserHomeAccessScheduleRule
- __OBJC_$_INSTANCE_VARIABLES_HMUserHomeAccessSettings
- __OBJC_$_PROP_LIST_HMApplicationData.11105
- __OBJC_$_PROP_LIST_HMMutableUserHomeAccessSchedule
- __OBJC_$_PROP_LIST_HMMutableUserHomeAccessScheduleRule
- __OBJC_$_PROP_LIST_HMMutableUserHomeAccessSettings
- __OBJC_$_PROP_LIST_HMResidentCapabilities.196
- __OBJC_$_PROP_LIST_HMUserHomeAccessSchedule
- __OBJC_$_PROP_LIST_HMUserHomeAccessScheduleRule
- __OBJC_$_PROP_LIST_HMUserHomeAccessSettings
- __OBJC_CLASS_PROTOCOLS_$_HMUserHomeAccessSchedule
- __OBJC_CLASS_PROTOCOLS_$_HMUserHomeAccessScheduleRule
- __OBJC_CLASS_PROTOCOLS_$_HMUserHomeAccessSettings
- __OBJC_CLASS_RO_$_HMMutableUserHomeAccessSchedule
- __OBJC_CLASS_RO_$_HMMutableUserHomeAccessScheduleRule
- __OBJC_CLASS_RO_$_HMMutableUserHomeAccessSettings
- __OBJC_CLASS_RO_$_HMUserHomeAccessSchedule
- __OBJC_CLASS_RO_$_HMUserHomeAccessScheduleRule
- __OBJC_CLASS_RO_$_HMUserHomeAccessSettings
- __OBJC_METACLASS_RO_$_HMMutableUserHomeAccessSchedule
- __OBJC_METACLASS_RO_$_HMMutableUserHomeAccessScheduleRule
- __OBJC_METACLASS_RO_$_HMMutableUserHomeAccessSettings
- __OBJC_METACLASS_RO_$_HMUserHomeAccessSchedule
- __OBJC_METACLASS_RO_$_HMUserHomeAccessScheduleRule
- __OBJC_METACLASS_RO_$_HMUserHomeAccessSettings
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.723
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.725
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.726
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.729
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.733
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.735
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.728
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.731
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.734
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.736
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_3.732
- ___22-[HMHome _mergeRooms:]_block_invoke.727
- ___22-[HMHome _mergeRooms:]_block_invoke.728
- ___22-[HMHome _mergeRooms:]_block_invoke.730
- ___22-[HMHome _mergeRooms:]_block_invoke_2.732
- ___22-[HMHome _mergeRooms:]_block_invoke_3.733
- ___22-[HMHome _mergeUsers:]_block_invoke.773
- ___22-[HMHome _mergeUsers:]_block_invoke.774
- ___22-[HMHome _mergeUsers:]_block_invoke.776
- ___22-[HMHome _mergeUsers:]_block_invoke_2.778
- ___22-[HMHome _mergeUsers:]_block_invoke_3.779
- ___22-[HMHome _mergeZones:]_block_invoke.735
- ___22-[HMHome _mergeZones:]_block_invoke.736
- ___22-[HMHome _mergeZones:]_block_invoke.738
- ___22-[HMHome _mergeZones:]_block_invoke_2.740
- ___22-[HMHome _mergeZones:]_block_invoke_3.741
- ___25-[HMHome _mergeTriggers:]_block_invoke.769
- ___25-[HMHome _mergeTriggers:]_block_invoke.771
- ___27-[HMHome _mergeActionSets:]_block_invoke.760
- ___27-[HMHome _mergeActionSets:]_block_invoke.761
- ___27-[HMHome _mergeActionSets:]_block_invoke.763
- ___27-[HMHome _mergeActionSets:]_block_invoke_2.765
- ___27-[HMHome _mergeActionSets:]_block_invoke_3.766
- ___28-[HMHome _mergeAccessories:]_block_invoke.743
- ___28-[HMHome _mergeAccessories:]_block_invoke.744
- ___28-[HMHome _mergeAccessories:]_block_invoke.746
- ___28-[HMHome _mergeAccessories:]_block_invoke.747
- ___28-[HMHome _mergeAccessories:]_block_invoke.749
- ___28-[HMHome _mergeAccessories:]_block_invoke_2.750
- ___29-[HMHome mergeFromNewObject:]_block_invoke.513
- ___29-[HMHome mergeFromNewObject:]_block_invoke.517
- ___29-[HMHome mergeFromNewObject:]_block_invoke.521
- ___29-[HMHome mergeFromNewObject:]_block_invoke.523
- ___29-[HMHome mergeFromNewObject:]_block_invoke.527
- ___29-[HMHome mergeFromNewObject:]_block_invoke.531
- ___29-[HMHome mergeFromNewObject:]_block_invoke.547
- ___29-[HMHome mergeFromNewObject:]_block_invoke.551
- ___29-[HMHome mergeFromNewObject:]_block_invoke.697
- ___29-[HMHome mergeFromNewObject:]_block_invoke.706
- ___29-[HMHome mergeFromNewObject:]_block_invoke.717
- ___29-[HMHome mergeFromNewObject:]_block_invoke.720
- ___29-[HMHome mergeFromNewObject:]_block_invoke.723
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.514
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.518
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.522
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.524
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.528
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.532
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.548
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.552
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.698
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.707
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.718
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.721
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.724
- ___29-[HMHome mergeFromNewObject:]_block_invoke_3.712
- ___29-[HMHome mergeFromNewObject:]_block_invoke_4.713
- ___29-[HMHome mergeFromNewObject:]_block_invoke_5.714
- ___29-[HMHome mergeFromNewObject:]_block_invoke_6.715
- ___29-[HMUser mergeFromNewObject:]_block_invoke.302
- ___29-[HMUser mergeFromNewObject:]_block_invoke.316
- ___29-[HMUser mergeFromNewObject:]_block_invoke_2.303
- ___29-[HMUser mergeFromNewObject:]_block_invoke_2.314
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1088
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1089
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1091
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1095
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1093
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1096
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_3.1094
- ___30-[HMAccessory _mergeServices:]_block_invoke.909
- ___30-[HMAccessory _mergeServices:]_block_invoke.911
- ___30-[HMHome _mergeServiceGroups:]_block_invoke.752
- ___30-[HMHome _mergeServiceGroups:]_block_invoke.753
- ___30-[HMHome _mergeServiceGroups:]_block_invoke.755
- ___30-[HMHome _mergeServiceGroups:]_block_invoke_2.757
- ___30-[HMHome _mergeServiceGroups:]_block_invoke_3.758
- ___32-[HMHome _mergeResidentDevices:]_block_invoke.781
- ___32-[HMHome _mergeResidentDevices:]_block_invoke.782
- ___32-[HMHome _mergeResidentDevices:]_block_invoke.784
- ___32-[HMHome _mergeResidentDevices:]_block_invoke_2.786
- ___32-[HMHome _mergeResidentDevices:]_block_invoke_3.787
- ___33-[__HMHomeDataSyncOperation main]_block_invoke.6
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1064
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1066
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1068
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1069
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1071
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1074
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1076
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1077
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1078
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1079
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1080
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.913
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.914
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.918
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.921
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.924
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.927
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.933
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.936
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.943
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1065
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1067
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1072
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1075
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.915
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.919
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.922
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.925
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.928
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.931
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.934
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.937
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.944
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.940
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.945
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.950
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.951
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.952
- ___36-[HMHome _mergeOutgoingInvitations:]_block_invoke.789
- ___36-[HMHome _mergeOutgoingInvitations:]_block_invoke.791
- ___38-[HMHomeManager _updateDataSyncState:]_block_invoke.483
- ___39-[HMHome _mergeTriggerOwnedActionSets:]_block_invoke.767
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.738
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.740
- ___39-[HMSoftwareUpdate mergeFromNewObject:]_block_invoke.166
- ___39-[HMSoftwareUpdate mergeFromNewObject:]_block_invoke.168
- ___39-[HMSoftwareUpdate mergeFromNewObject:]_block_invoke_2.167
- ___39-[HMSoftwareUpdate mergeFromNewObject:]_block_invoke_2.169
- ___40-[HMSoftwareUpdate requestDocumentation]_block_invoke.154
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.793
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.794
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.795
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.796
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.798
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke_2.797
- ___43-[HMHome fetchPresenceForUsers:completion:]_block_invoke.807
- ___43-[HMHome fetchPresenceForUsers:completion:]_block_invoke.809
- ___44-[HMHome _handleAccessoryAddedNotification:]_block_invoke.878
- ___44-[HMUser _mergeWithNewAccessoryInvitations:]_block_invoke.296
- ___45-[HMAccessory _handleCharacteristicsUpdated:]_block_invoke.1107
- ___47-[HMHomeManager _recomputeAssistantIdentifiers]_block_invoke.647
- ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1108
- ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1109
- ___50-[HMSoftwareUpdate updateState:completionHandler:]_block_invoke.144
- ___50-[HMSoftwareUpdate updateState:completionHandler:]_block_invoke.146
- ___51-[HMHomeManager _updatePrimaryHome:notifyDelegate:]_block_invoke.707
- ___52-[HMHome(HMUser) _manageUsersWithCompletionHandler:]_block_invoke.1688
- ___54-[HMHome _notifyDelegateOfAccessControlUpdateForUser:]_block_invoke.914
- ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.576
- ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.577
- ___58-[HMHomeManager __resolveAccountHandle:completionHandler:]_block_invoke.634
- ___61-[HMAccessory _notifyClientsOfSymptomsHandlerAddedOrRemoved:]_block_invoke.1123
- ___61-[HMHomeManager __removeAccountWithHandle:completionHandler:]_block_invoke.636
- ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.843
- ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.845
- ___63-[HMHome(HMUser) _inviteWithUserInformation:completionHandler:]_block_invoke
- ___63-[HMUser updateAnnounceUserSettings:forHome:completionHandler:]_block_invoke.220
- ___63-[HMUser updateAnnounceUserSettings:forHome:completionHandler:]_block_invoke.221
- ___64-[HMHome(HMMediaProfile) updateMediaPassword:completionHandler:]_block_invoke.1764
- ___65-[HMHomeManager __removeAccountWithIdentifier:completionHandler:]_block_invoke.635
- ___65-[HMUser updateAssistantAccessControl:forHome:completionHandler:]_block_invoke.153
- ___66-[HMSoftwareUpdate updateDocumentationMetadata:completionHandler:]_block_invoke.153
- ___67-[HMHome _addEventTriggerFromResponse:withEventTrigger:completion:]_block_invoke.871
- ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.665
- ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.669
- ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.671
- ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.673
- ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke_2.674
- ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.792
- ___74-[HMHomeManager __processSyncResponse:refreshRequested:completionHandler:]_block_invoke.644
- ___75-[HMHome(HMAccessory) addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.1551
- ___75-[HMUser updateMediaContentProfileAccessControl:forHome:completionHandler:]_block_invoke.222
- ___75-[HMUser updateMediaContentProfileAccessControl:forHome:completionHandler:]_block_invoke.223
- ___76-[HMUser updateUserListeningHistoryUpdateControl:forHome:completionHandler:]_block_invoke.224
- ___76-[HMUser updateUserListeningHistoryUpdateControl:forHome:completionHandler:]_block_invoke.225
- ___88-[HMHome(HMAccessory) addAccessoryWithAccessorySetupPayload:progress:completionHandler:]_block_invoke.1562
- ___88-[HMHome(HMAccessory) addAndSetUpNewAccessoriesWithSuggestedRoomName:completionHandler:]_block_invoke.1553
- ___88-[HMHome(HomeLocationFeedback) retrieveHomeKitLocationForFeedbackWithCompletionHandler:]_block_invoke.1849
- ___89-[HMHome(NetworkRouter) updateAccessoryNetworkProtectionGroup:protectionMode:completion:]_block_invoke.1819
- ___93-[HMHomeManager _pingDeviceWithUUID:monitor:secure:restrictToLocalNetwork:completionHandler:]_block_invoke.637
- ___Block_byref_object_copy_.14048
- ___Block_byref_object_copy_.14357
- ___Block_byref_object_copy_.21027
- ___Block_byref_object_copy_.23116
- ___Block_byref_object_copy_.27137
- ___Block_byref_object_copy_.28823
- ___Block_byref_object_copy_.35455
- ___Block_byref_object_copy_.38312
- ___Block_byref_object_copy_.39388
- ___Block_byref_object_copy_.59774
- ___Block_byref_object_dispose_.14049
- ___Block_byref_object_dispose_.14358
- ___Block_byref_object_dispose_.21028
- ___Block_byref_object_dispose_.23117
- ___Block_byref_object_dispose_.27138
- ___Block_byref_object_dispose_.28824
- ___Block_byref_object_dispose_.35456
- ___Block_byref_object_dispose_.38313
- ___Block_byref_object_dispose_.39389
- ___Block_byref_object_dispose_.59775
- ___CoreAnalyticsLibraryCore_block_invoke.35569
- ___IDSFoundationLibraryCore_block_invoke.39161
- ___UIKitLibraryCore_block_invoke.39403
- _____HMHomeManagerRegisterForNotifications_block_invoke.1350
- ___accessoryIdsForAccessories
- ___block_literal_global.101.35576
- ___block_literal_global.1016
- ___block_literal_global.10180
- ___block_literal_global.11166
- ___block_literal_global.12.45313
- ___block_literal_global.121.48239
- ___block_literal_global.12126
- ___block_literal_global.12273
- ___block_literal_global.12727
- ___block_literal_global.12919
- ___block_literal_global.13483
- ___block_literal_global.13814
- ___block_literal_global.14132
- ___block_literal_global.14721
- ___block_literal_global.1512
- ___block_literal_global.1570
- ___block_literal_global.15782
- ___block_literal_global.16309
- ___block_literal_global.16500
- ___block_literal_global.16632
- ___block_literal_global.16794
- ___block_literal_global.17.17425
- ___block_literal_global.171
- ___block_literal_global.17432
- ___block_literal_global.1761
- ___block_literal_global.18099
- ___block_literal_global.18502
- ___block_literal_global.19.13799
- ___block_literal_global.19053
- ___block_literal_global.192.22341
- ___block_literal_global.19377
- ___block_literal_global.1962
- ___block_literal_global.20410
- ___block_literal_global.21065
- ___block_literal_global.21338
- ___block_literal_global.21823
- ___block_literal_global.22042
- ___block_literal_global.22347
- ___block_literal_global.22481
- ___block_literal_global.22727
- ___block_literal_global.22978
- ___block_literal_global.23139
- ___block_literal_global.23231
- ___block_literal_global.25723
- ___block_literal_global.25858
- ___block_literal_global.26331
- ___block_literal_global.27020
- ___block_literal_global.27266
- ___block_literal_global.27605
- ___block_literal_global.27817
- ___block_literal_global.28095
- ___block_literal_global.28169
- ___block_literal_global.29021
- ___block_literal_global.29346
- ___block_literal_global.29617
- ___block_literal_global.30.17415
- ___block_literal_global.30.7383
- ___block_literal_global.30446
- ___block_literal_global.30984
- ___block_literal_global.32158
- ___block_literal_global.32968
- ___block_literal_global.33.59117
- ___block_literal_global.33199
- ___block_literal_global.33422
- ___block_literal_global.3397
- ___block_literal_global.34372
- ___block_literal_global.35563
- ___block_literal_global.358
- ___block_literal_global.35813
- ___block_literal_global.3592
- ___block_literal_global.36149
- ___block_literal_global.36781
- ___block_literal_global.3683
- ___block_literal_global.37583
- ___block_literal_global.37708
- ___block_literal_global.37983
- ___block_literal_global.39223
- ___block_literal_global.39319
- ___block_literal_global.40028
- ___block_literal_global.40217
- ___block_literal_global.40849
- ___block_literal_global.41474
- ___block_literal_global.41890
- ___block_literal_global.42210
- ___block_literal_global.42883
- ___block_literal_global.43767
- ___block_literal_global.45035
- ___block_literal_global.45325
- ___block_literal_global.45591
- ___block_literal_global.45785
- ___block_literal_global.46012
- ___block_literal_global.46704
- ___block_literal_global.468
- ___block_literal_global.46824
- ___block_literal_global.473
- ___block_literal_global.47556
- ___block_literal_global.47993
- ___block_literal_global.48326
- ___block_literal_global.4852
- ___block_literal_global.49239
- ___block_literal_global.51788
- ___block_literal_global.5243
- ___block_literal_global.52491
- ___block_literal_global.5379
- ___block_literal_global.53927
- ___block_literal_global.544
- ___block_literal_global.54567
- ___block_literal_global.55097
- ___block_literal_global.55408
- ___block_literal_global.55905
- ___block_literal_global.56077
- ___block_literal_global.56462
- ___block_literal_global.56706
- ___block_literal_global.58355
- ___block_literal_global.58521
- ___block_literal_global.5873
- ___block_literal_global.58858
- ___block_literal_global.59123
- ___block_literal_global.59483
- ___block_literal_global.59772
- ___block_literal_global.60065
- ___block_literal_global.6345
- ___block_literal_global.6614
- ___block_literal_global.684
- ___block_literal_global.686
- ___block_literal_global.688
- ___block_literal_global.7049
- ___block_literal_global.7166
- ___block_literal_global.73.21316
- ___block_literal_global.7401
- ___block_literal_global.75.35766
- ___block_literal_global.76.25490
- ___block_literal_global.7852
- ___block_literal_global.796
- ___block_literal_global.8335
- ___block_literal_global.85.59786
- ___block_literal_global.8613
- ___block_literal_global.876
- ___block_literal_global.8789
- ___block_literal_global.9216
- ___block_literal_global.945
- ___block_literal_global.947
- ___block_literal_global.9470
- ___block_literal_global.950
- ___getAnalyticsSendEventLazySymbolLoc_block_invoke.35566
- ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.39398
- ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.39392
- __unnamed_array_storage.14065
- __unnamed_array_storage.22254
- __unnamed_array_storage.227.25637
- __unnamed_array_storage.239.25636
- __unnamed_array_storage.251.25640
- __unnamed_array_storage.25713
- __unnamed_array_storage.28682
- __unnamed_array_storage.54043
- __unnamed_array_storage.55533
- __unnamed_array_storage.58974
- _audit_stringCoreAnalytics.35572
- _audit_stringIDSFoundation.39163
- _audit_stringUIKit.39405
- _getAnalyticsSendEventLazySymbolLoc.ptr.35565
- _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.39397
- _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.39391
- _logCategory._hmf_once_t0.12272
- _logCategory._hmf_once_t0.21337
- _logCategory._hmf_once_t0.27816
- _logCategory._hmf_once_t0.28168
- _logCategory._hmf_once_t0.40027
- _logCategory._hmf_once_t0.40216
- _logCategory._hmf_once_t0.40848
- _logCategory._hmf_once_t0.56705
- _logCategory._hmf_once_t1.16631
- _logCategory._hmf_once_t1.18501
- _logCategory._hmf_once_t1.35789
- _logCategory._hmf_once_t1.41473
- _logCategory._hmf_once_t1.45312
- _logCategory._hmf_once_t1.46823
- _logCategory._hmf_once_t1.51787
- _logCategory._hmf_once_t15.56461
- _logCategory._hmf_once_t16.33198
- _logCategory._hmf_once_t16.58520
- _logCategory._hmf_once_t17.37575
- _logCategory._hmf_once_t19.12945
- _logCategory._hmf_once_t2.25857
- _logCategory._hmf_once_t2.29345
- _logCategory._hmf_once_t20.5378
- _logCategory._hmf_once_t22.22726
- _logCategory._hmf_once_t24.36143
- _logCategory._hmf_once_t25.22977
- _logCategory._hmf_once_t25.59482
- _logCategory._hmf_once_t26.48074
- _logCategory._hmf_once_t27.47555
- _logCategory._hmf_once_t27.55407
- _logCategory._hmf_once_t3.37707
- _logCategory._hmf_once_t3.59116
- _logCategory._hmf_once_t31.21064
- _logCategory._hmf_once_t31.58354
- _logCategory._hmf_once_t311
- _logCategory._hmf_once_t33.48351
- _logCategory._hmf_once_t337
- _logCategory._hmf_once_t34.14127
- _logCategory._hmf_once_t34.18098
- _logCategory._hmf_once_t35.34371
- _logCategory._hmf_once_t4.1027
- _logCategory._hmf_once_t4.5242
- _logCategory._hmf_once_t50.37982
- _logCategory._hmf_once_t6.30445
- _logCategory._hmf_once_t6.32967
- _logCategory._hmf_once_t6.46703
- _logCategory._hmf_once_t6.52490
- _logCategory._hmf_once_t64.53926
- _logCategory._hmf_once_t7.23230
- _logCategory._hmf_once_t8.33421
- _logCategory._hmf_once_t8.42882
- _logCategory._hmf_once_t8.45803
- _logCategory._hmf_once_v1.12274
- _logCategory._hmf_once_v1.21339
- _logCategory._hmf_once_v1.27818
- _logCategory._hmf_once_v1.28170
- _logCategory._hmf_once_v1.40029
- _logCategory._hmf_once_v1.40218
- _logCategory._hmf_once_v1.40850
- _logCategory._hmf_once_v1.56707
- _logCategory._hmf_once_v16.56463
- _logCategory._hmf_once_v17.33200
- _logCategory._hmf_once_v17.58522
- _logCategory._hmf_once_v18.37576
- _logCategory._hmf_once_v2.16633
- _logCategory._hmf_once_v2.18503
- _logCategory._hmf_once_v2.35790
- _logCategory._hmf_once_v2.41475
- _logCategory._hmf_once_v2.45314
- _logCategory._hmf_once_v2.46825
- _logCategory._hmf_once_v2.51789
- _logCategory._hmf_once_v20.12946
- _logCategory._hmf_once_v21.5380
- _logCategory._hmf_once_v23.22728
- _logCategory._hmf_once_v25.36144
- _logCategory._hmf_once_v26.22979
- _logCategory._hmf_once_v26.59484
- _logCategory._hmf_once_v27.48075
- _logCategory._hmf_once_v28.47557
- _logCategory._hmf_once_v28.55409
- _logCategory._hmf_once_v3.25859
- _logCategory._hmf_once_v3.29347
- _logCategory._hmf_once_v312
- _logCategory._hmf_once_v32.21066
- _logCategory._hmf_once_v32.58356
- _logCategory._hmf_once_v338
- _logCategory._hmf_once_v34.48352
- _logCategory._hmf_once_v35.14128
- _logCategory._hmf_once_v35.18100
- _logCategory._hmf_once_v36.34373
- _logCategory._hmf_once_v4.37709
- _logCategory._hmf_once_v4.59118
- _logCategory._hmf_once_v5.1028
- _logCategory._hmf_once_v5.5244
- _logCategory._hmf_once_v51.37984
- _logCategory._hmf_once_v65.53928
- _logCategory._hmf_once_v7.30447
- _logCategory._hmf_once_v7.32969
- _logCategory._hmf_once_v7.46705
- _logCategory._hmf_once_v7.52492
- _logCategory._hmf_once_v8.23232
- _logCategory._hmf_once_v9.33423
- _logCategory._hmf_once_v9.42884
- _logCategory._hmf_once_v9.45804
- _objc_msgSend$_inviteWithUserInformation:completionHandler:
- _objc_msgSend$allowedAccessoryCategoryTypes
- _objc_msgSend$allowedAccessoryIdentifiers
- _objc_msgSend$allowedRoomIdentifiers
- _objc_msgSend$currrentAccessoryMediaRouteId
- _objc_msgSend$daysOfTheWeek
- _objc_msgSend$endTime
- _objc_msgSend$hm_uuid:identifierSalt:withSalts:
- _objc_msgSend$homeAccessSettings
- _objc_msgSend$initWithHomeManager:timeout:
- _objc_msgSend$initWithSession:setupSession:
- _objc_msgSend$initWithStartTime:endTime:daysOfTheWeek:validFrom:validThrough:
- _objc_msgSend$isAccessAllowedToAllAccessories
- _objc_msgSend$rules
- _objc_msgSend$schedule
- _objc_msgSend$setAccessAllowedToAllAccessories:
- _objc_msgSend$setAllowedAccessoryCategoryTypes:
- _objc_msgSend$setAllowedAccessoryIdentifiers:
- _objc_msgSend$setAllowedRoomIdentifiers:
- _objc_msgSend$setHomeAccessSettings:
- _objc_msgSend$setRules:
- _objc_msgSend$setSchedule:
- _objc_msgSend$setSupports40e39e789f11ed6f1738:
- _objc_msgSend$startTime
- _objc_msgSend$supports40e39e789f11ed6f1738
- _objc_msgSend$validFrom
- _objc_msgSend$validThrough
- _sharedInstance.onceToken.37582
- _sharedManager.onceToken.55550
- _supportedValueClasses.onceToken.45590
- _supportedValueClasses.onceToken.53889
- _supportedValueClasses.supportedValueClasses.45592
- _supportedValueClasses.supportedValueClasses.53890
- _unconfigureQueue.onceToken.36148
- _unconfigureQueue.unconfigureQueue.36150
CStrings:
+ "\x11\x13\x11S1/\x02G"
+ "\x12\x12!\x11\""
+ "\x1d"
+ "!\x11\x11"
+ "%{public}@API Misuse: baseUUID passed in as nil!"
+ "%{public}@Error occurred while fetching the presence for users: %@"
+ "%{public}@Error processing primary user info as supportsMessagedHomePodSettings is disabled"
+ "%{public}@Error processing wifi info as supportsMessagedHomePodSettings is disabled"
+ "%{public}@Failed to process sync response: %@"
+ "%{public}@Install managed configuration profiles responded with error: %@"
+ "%{public}@Install managed configuration profiles succeeded: %@"
+ "%{public}@Manager was deallocated before fetch response was handled"
+ "%{public}@Manager was deallocated before sync operation started"
+ "%{public}@Nil profileData"
+ "%{public}@Notifying delegate of updated access control via merge: %@"
+ "%{public}@Queried initial authorization status: %ld"
+ "%{public}@Requesting home configuration with generation counter: %tu, QoS: %@, operation: %@"
+ "%{public}@Successfully processed sync response"
+ "%{public}@Sync operation failed: %@"
+ "%{public}@The framework's generation counter matches the daemon's generation counter"
+ "%{public}@This client cannot access home data with current authorization status: %lu"
+ "%{public}@update invitation: %@"
+ "+\x11"
+ "-[HMAccessory installManagedConfigurationProfileWithData:completionHandler:]"
+ "/Library/Managed Preferences/mobile/com.apple.homed.plist"
+ "<%@ [cloudkit=> accountStatus: %d, cdp: %d, firstImport: %d>] [ids=> status: %d identifier: %@ ] [device=> %@ - %@ - %@, s/w: %@, upd: (%@, %@)] hh2: %d, numHomes: %lu, uuid: %@, mediaRouteID: %@, isPrimary: %d, wifi: %@, [eventrouter=> connected: %d date: %@, clients: %@] >"
+ "@\"HMAccessoryDiagnosticInfoProtoSetupInfo\""
+ "@\"HMDeviceSetupSession\"16@?0@\"<HMDeviceSetupSessionDelegate>\"8"
+ "@\"HMSoftwareUpdateEventProtoSoftwareUpdateDescriptor\""
+ "@\"HMSoftwareUpdateEventProtoSoftwareUpdateProgress\""
+ "@28@0:8@16{_HMAccessoryCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}24"
+ "@40@0:8@16@24^@32"
+ "@76@0:8@16C24@28@36@44@52@60@68"
+ "HM.set.preferred.primary"
+ "HMAccessory.mc.data"
+ "HMAccessoryDiagnosticInfoProtoSetupInfo"
+ "HMAccessoryInstallManagedConfigurationProfileMessage"
+ "IDSAvailable_INT"
+ "MatteriPhoneOnlyPairing"
+ "MatteriPhoneOnlyPairingEnabled"
+ "StringAsICloudAvailableINT:"
+ "StringAsIDSAvailableINT:"
+ "StringAsManateeAvailableINT:"
+ "StringAsNetworkAvailableINT:"
+ "T@\"HMAccessoryDiagnosticInfoProtoSetupInfo\",&,N,V_lastSetupInfo"
+ "T@\"HMSoftwareUpdateDescriptor\",R,C,N,V_softwareUpdateDescriptor"
+ "T@\"HMSoftwareUpdateEventProtoSoftwareUpdateDescriptor\",&,N,V_softwareUpdateDescriptor"
+ "T@\"HMSoftwareUpdateEventProtoSoftwareUpdateProgress\",&,N,V_softwareUpdateProgress"
+ "T@\"HMSoftwareUpdateProgress\",R,C,N,V_softwareUpdateProgress"
+ "T@\"NSData\",&,N,V_operationalDataset"
+ "T@\"NSDate\",C,V_nextPermittedRequestDocumentationDate"
+ "T@\"NSString\",&,N,V_lastKnownStageErrorDomain"
+ "T@\"NSString\",&,N,V_lastKnownStageErrorString"
+ "T@\"NSString\",&,N,V_lastKnownStageUnderlyingErrorDomain"
+ "T@\"NSString\",R,C,V_logIdentifier"
+ "T@\"NSString\",R,N,V_currentAccessoryMediaRouteId"
+ "TB,N,V_supportsEventLog"
+ "TB,N,V_supportsInstallManagedConfigurationProfile"
+ "TQ,N,V_savedEventState"
+ "Ti,N,V_iCloudAvailableINT"
+ "Ti,N,V_iDSAvailableINT"
+ "Ti,N,V_manateeAvailableINT"
+ "Ti,N,V_networkAvailableINT"
+ "Tq,N,V_accessoryAddMSHH2"
+ "Tq,N,V_accountSettleWaitMSHH2"
+ "Tq,N,V_controllerKeyExchangeMSHH1"
+ "Tq,N,V_currentDeviceIDSWaitMSHH2"
+ "Tq,N,V_eventRouterFirstEventPushMSHH2"
+ "Tq,N,V_eventRouterServerConnectionMSHH2"
+ "Tq,N,V_firstCoreDataImportMSHH2"
+ "Tq,N,V_homeManagerReadyMSHH2"
+ "Tq,N,V_lastKnownStageErrorCode"
+ "Tq,N,V_lastKnownStageUnderlyingErrorCode"
+ "Tq,N,V_newAccessoryTransferMSHH1"
+ "Tq,N,V_pairingIdentityCreationMSHH2"
+ "Tq,N,V_primaryResidentElectionMSHH2"
+ "Tq,N,V_sentinelZoneFetchMSHH1"
+ "Tq,N,V_sessionSetupCloseMSHH1"
+ "Tq,N,V_sessionSetupOpenMSHH1"
+ "Tq,N,V_settingsCreationMSHH2"
+ "Tq,N,V_siriReadyMSHH2"
+ "Tq,N,V_totalDurationMSHH1"
+ "Tq,N,V_totalDurationMSHH2"
+ "T{_HMAccessoryCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1},R,N,V_capabilities"
+ "_accessoryAddMSHH2"
+ "_accountSettleWaitMSHH2"
+ "_controllerKeyExchangeMSHH1"
+ "_currentAccessoryMediaRouteId"
+ "_currentDeviceIDSWaitMSHH2"
+ "_eventRouterFirstEventPushMSHH2"
+ "_eventRouterServerConnectionMSHH2"
+ "_firstCoreDataImportMSHH2"
+ "_homeManagerReadyMSHH2"
+ "_iCloudAvailableINT"
+ "_iDSAvailableINT"
+ "_lastKnownStageErrorCode"
+ "_lastKnownStageErrorDomain"
+ "_lastKnownStageErrorString"
+ "_lastKnownStageUnderlyingErrorCode"
+ "_lastKnownStageUnderlyingErrorDomain"
+ "_lastSetupInfo"
+ "_manateeAvailableINT"
+ "_networkAvailableINT"
+ "_newAccessoryTransferMSHH1"
+ "_nextPermittedRequestDocumentationDate"
+ "_operationalDataset"
+ "_pairingIdentityCreationMSHH2"
+ "_primaryResidentElectionMSHH2"
+ "_savedEventState"
+ "_sentinelZoneFetchMSHH1"
+ "_sessionSetupCloseMSHH1"
+ "_sessionSetupOpenMSHH1"
+ "_settingsCreationMSHH2"
+ "_siriReadyMSHH2"
+ "_softwareUpdateDescriptor"
+ "_softwareUpdateProgress"
+ "_supportsEventLog"
+ "_supportsInstallManagedConfigurationProfile"
+ "_totalDurationMSHH1"
+ "_totalDurationMSHH2"
+ "accessoryAddMSHH2"
+ "accessoryAddMS_HH2"
+ "accountSettleWaitMSHH2"
+ "accountSettleWaitMS_HH2"
+ "additionalFetchKeys"
+ "controllerKeyExchangeMSHH1"
+ "controllerKeyExchangeMS_HH1"
+ "currentAccessoryMediaRouteId"
+ "currentDeviceIDSWaitMSHH2"
+ "currentDeviceIDSWaitMS_HH2"
+ "eventRouterFirstEventPushMSHH2"
+ "eventRouterFirstEventPushMS_HH2"
+ "eventRouterServerConnectionMSHH2"
+ "eventRouterServerConnectionMS_HH2"
+ "firstCoreDataImportMSHH2"
+ "firstCoreDataImportMS_HH2"
+ "hasAccessoryAddMSHH2"
+ "hasAccountSettleWaitMSHH2"
+ "hasControllerKeyExchangeMSHH1"
+ "hasCurrentDeviceIDSWaitMSHH2"
+ "hasEventRouterFirstEventPushMSHH2"
+ "hasEventRouterServerConnectionMSHH2"
+ "hasFirstCoreDataImportMSHH2"
+ "hasHomeManagerReadyMSHH2"
+ "hasICloudAvailableINT"
+ "hasIDSAvailableINT"
+ "hasLastKnownStageErrorCode"
+ "hasLastKnownStageErrorDomain"
+ "hasLastKnownStageErrorString"
+ "hasLastKnownStageUnderlyingErrorCode"
+ "hasLastKnownStageUnderlyingErrorDomain"
+ "hasLastSetupInfo"
+ "hasManateeAvailableINT"
+ "hasNetworkAvailableINT"
+ "hasNewAccessoryTransferMSHH1"
+ "hasPairingIdentityCreationMSHH2"
+ "hasPrimaryResidentElectionMSHH2"
+ "hasSavedEventState"
+ "hasSentinelZoneFetchMSHH1"
+ "hasSessionSetupCloseMSHH1"
+ "hasSessionSetupOpenMSHH1"
+ "hasSettingsCreationMSHH2"
+ "hasSiriReadyMSHH2"
+ "hasSoftwareUpdateDescriptor"
+ "hasSoftwareUpdateProgress"
+ "hasSupportsEventLog"
+ "hasSupportsInstallManagedConfigurationProfile"
+ "hasTotalDurationMSHH1"
+ "hasTotalDurationMSHH2"
+ "hmf_UUIDWithNamespace:data:salts:"
+ "homeManagerReadyMSHH2"
+ "homeManagerReadyMS_HH2"
+ "iCloudAvailableINT"
+ "iCloudAvailableINTAsString:"
+ "iCloudAvailable_INT"
+ "iDSAvailableINT"
+ "iDSAvailableINTAsString:"
+ "initWithInternalSetupPayload:"
+ "initWithName:channel:PANID:extendedPANID:masterKey:passPhrase:PSKc:operationalDataset:"
+ "initWithSession:setupSessionFactory:"
+ "initWithURL:fileManager:error:"
+ "installManagedConfigurationProfileWithData:completionHandler:"
+ "isiPhoneOnlyPairingSupportedForMatterAccessories"
+ "lastKnownStageErrorCode"
+ "lastKnownStageErrorDomain"
+ "lastKnownStageErrorString"
+ "lastKnownStageUnderlyingErrorCode"
+ "lastKnownStageUnderlyingErrorDomain"
+ "lastSetupInfo"
+ "manateeAvailableINT"
+ "manateeAvailableINTAsString:"
+ "manateeAvailable_INT"
+ "networkAvailableINT"
+ "networkAvailableINTAsString:"
+ "networkAvailable_INT"
+ "newAccessoryTransferMSHH1"
+ "newAccessoryTransferMS_HH1"
+ "nextPermittedRequestDocumentationDate"
+ "operationalDataset"
+ "pairingIdentityCreationMSHH2"
+ "pairingIdentityCreationMS_HH2"
+ "preferred.primary.identifier"
+ "preferred.primary.one.time"
+ "preferred.primary.trigger.election"
+ "primaryResidentElectionMSHH2"
+ "primaryResidentElectionMS_HH2"
+ "savedEventState"
+ "sentinelZoneFetchMSHH1"
+ "sentinelZoneFetchMS_HH1"
+ "sessionSetupCloseMSHH1"
+ "sessionSetupCloseMS_HH1"
+ "sessionSetupOpenMSHH1"
+ "sessionSetupOpenMS_HH1"
+ "setAccessoryAddMSHH2:"
+ "setAccountSettleWaitMSHH2:"
+ "setControllerKeyExchangeMSHH1:"
+ "setCurrentDeviceIDSWaitMSHH2:"
+ "setEventRouterFirstEventPushMSHH2:"
+ "setEventRouterServerConnectionMSHH2:"
+ "setFirstCoreDataImportMSHH2:"
+ "setHasAccessoryAddMSHH2:"
+ "setHasAccountSettleWaitMSHH2:"
+ "setHasControllerKeyExchangeMSHH1:"
+ "setHasCurrentDeviceIDSWaitMSHH2:"
+ "setHasEventRouterFirstEventPushMSHH2:"
+ "setHasEventRouterServerConnectionMSHH2:"
+ "setHasFirstCoreDataImportMSHH2:"
+ "setHasHomeManagerReadyMSHH2:"
+ "setHasICloudAvailableINT:"
+ "setHasIDSAvailableINT:"
+ "setHasLastKnownStageErrorCode:"
+ "setHasLastKnownStageUnderlyingErrorCode:"
+ "setHasManateeAvailableINT:"
+ "setHasNetworkAvailableINT:"
+ "setHasNewAccessoryTransferMSHH1:"
+ "setHasPairingIdentityCreationMSHH2:"
+ "setHasPrimaryResidentElectionMSHH2:"
+ "setHasSavedEventState:"
+ "setHasSentinelZoneFetchMSHH1:"
+ "setHasSessionSetupCloseMSHH1:"
+ "setHasSessionSetupOpenMSHH1:"
+ "setHasSettingsCreationMSHH2:"
+ "setHasSiriReadyMSHH2:"
+ "setHasSupportsEventLog:"
+ "setHasSupportsInstallManagedConfigurationProfile:"
+ "setHasTotalDurationMSHH1:"
+ "setHasTotalDurationMSHH2:"
+ "setHomeManagerReadyMSHH2:"
+ "setICloudAvailableINT:"
+ "setIDSAvailableINT:"
+ "setLastKnownStageErrorCode:"
+ "setLastKnownStageErrorDomain:"
+ "setLastKnownStageErrorString:"
+ "setLastKnownStageUnderlyingErrorCode:"
+ "setLastKnownStageUnderlyingErrorDomain:"
+ "setLastSetupInfo:"
+ "setManateeAvailableINT:"
+ "setNetworkAvailableINT:"
+ "setNewAccessoryTransferMSHH1:"
+ "setNextPermittedRequestDocumentationDate:"
+ "setOperationalDataset:"
+ "setPairingIdentityCreationMSHH2:"
+ "setPreferredPrimary:oneTime:triggerElection:completionHandler:"
+ "setPrimaryResidentElectionMSHH2:"
+ "setSavedEventState:"
+ "setSentinelZoneFetchMSHH1:"
+ "setSessionSetupCloseMSHH1:"
+ "setSessionSetupOpenMSHH1:"
+ "setSettingsCreationMSHH2:"
+ "setSiriReadyMSHH2:"
+ "setSoftwareUpdateDescriptor:"
+ "setSoftwareUpdateProgress:"
+ "setSupportsEventLog:"
+ "setSupportsInstallManagedConfigurationProfile:"
+ "setTotalDurationMSHH1:"
+ "setTotalDurationMSHH2:"
+ "settingsCreationMSHH2"
+ "settingsCreationMS_HH2"
+ "setupMetric"
+ "siriReadyMSHH2"
+ "siriReadyMS_HH2"
+ "softwareUpdateDescriptor"
+ "softwareUpdateProgress"
+ "supportsInstallManagedConfigurationProfile"
+ "totalDurationMSHH1"
+ "totalDurationMSHH2"
+ "totalDurationMS_HH1"
+ "totalDurationMS_HH2"
+ "validateInviteForHome:"
+ "{?=\"accessoryAddMSHH2\"b1\"accountSettleWaitMSHH2\"b1\"controllerKeyExchangeMSHH1\"b1\"currentDeviceIDSWaitMSHH2\"b1\"eventRouterFirstEventPushMSHH2\"b1\"eventRouterServerConnectionMSHH2\"b1\"firstCoreDataImportMSHH2\"b1\"homeManagerReadyMSHH2\"b1\"lastKnownStageErrorCode\"b1\"lastKnownStageUnderlyingErrorCode\"b1\"newAccessoryTransferMSHH1\"b1\"pairingIdentityCreationMSHH2\"b1\"primaryResidentElectionMSHH2\"b1\"savedEventState\"b1\"sentinelZoneFetchMSHH1\"b1\"sessionSetupCloseMSHH1\"b1\"sessionSetupOpenMSHH1\"b1\"settingsCreationMSHH2\"b1\"siriReadyMSHH2\"b1\"totalDurationMSHH1\"b1\"totalDurationMSHH2\"b1\"version\"b1\"iCloudAvailableINT\"b1\"iDSAvailableINT\"b1\"manateeAvailableINT\"b1\"networkAvailableINT\"b1}"
+ "{?=\"supports2c25465bb0b47366\"b1\"supports89024c1cadcb8b00\"b1\"supports90bb069d6bx54e7\"b1\"supportsAnnounce\"b1\"supportsAssistantAccessControl\"b1\"supportsAudioReturnChannel\"b1\"supportsCaptiveNetworks\"b1\"supportsCloudDataSync\"b1\"supportsCompanionInitiatedRestart\"b1\"supportsCoordinationDoorbellChime\"b1\"supportsDeviceSetup\"b1\"supportsDoorbellChime\"b1\"supportsHomeHub\"b1\"supportsHomeInvitation\"b1\"supportsHomeLevelAnalyticsAndImprovementSetting\"b1\"supportsHomeLevelLocationServiceSetting\"b1\"supportsInstallManagedConfigurationProfile\"b1\"supportsKeyTransferClient\"b1\"supportsKeyTransferServer\"b1\"supportsKeychainSync\"b1\"supportsManagedConfigurationProfile\"b1\"supportsMediaActions\"b1\"supportsMessagedHomePodSettings\"b1\"supportsMultiUser\"b1\"supportsMusicAlarm\"b1\"supportsPreferredMediaUser\"b1\"supportsStandaloneMode\"b1\"supportsTargetControl\"b1\"supportsThirdPartyMusic\"b1\"supportsThreadBorderRouter\"b1\"supportsUserMediaSettings\"b1\"supportsWholeHouseAudio\"b1\"supportsf9cc0d9d6aa54e7\"b1}"
+ "{?=\"supports5348b248a25f84b0c83e\"b1\"supportsAccessCodes\"b1\"supportsAnnounce\"b1\"supportsCHIP\"b1\"supportsCameraActivityZones\"b1\"supportsCameraPackageDetection\"b1\"supportsCameraRecording\"b1\"supportsCameraRecordingReachabilityNotifications\"b1\"supportsCameraSignificantEventNotifications\"b1\"supportsCustomMediaApplicationDestination\"b1\"supportsEventLog\"b1\"supportsFaceClassification\"b1\"supportsFirmwareUpdate\"b1\"supportsHomeHub\"b1\"supportsLockNotificationContext\"b1\"supportsMatterTTU\"b1\"supportsMediaActions\"b1\"supportsNaturalLighting\"b1\"supportsResidentFirmwareUpdate\"b1\"supportsResidentFirstAccessoryCommunication\"b1\"supportsRouterManagement\"b1\"supportsShortcutActions\"b1\"supportsSiriEndpointSetup\"b1\"supportsThreadBorderRouter\"b1\"supportsThreadNetworkCredentialSharing\"b1\"supportsUnifiedMediaNotifications\"b1\"supportsWakeOnLAN\"b1\"supportsWalletKey\"b1}"
+ "{_HMAccessoryCapabilitiesStruct=\"supportsKeychainSync\"b1\"supportsDeviceSetup\"b1\"supportsKeyTransferClient\"b1\"supportsKeyTransferServer\"b1\"supportsStandaloneMode\"b1\"supportsCloudDataSync\"b1\"supportsWholeHouseAudio\"b1\"supportsAssistantAccessControl\"b1\"supportsHomeInvitation\"b1\"supportsTargetControl\"b1\"supportsMultiUser\"b1\"supportsHomeLevelLocationServiceSetting\"b1\"supportsCompanionInitiatedRestart\"b1\"supportsMusicAlarm\"b1\"supportsAnnounce\"b1\"supportsAudioAnalysis\"b1\"supportsThirdPartyMusic\"b1\"supportsPreferredMediaUser\"b1\"supportsThreadBorderRouter\"b1\"supportsDoorbellChime\"b1\"supportsUserMediaSettings\"b1\"supportsCoordinationDoorbellChime\"b1\"supportsHomeHub\"b1\"supportsAudioReturnChannel\"b1\"supportsManagedConfigurationProfile\"b1\"supportsCaptiveNetworks\"b1\"supportsMessagedHomePodSettings\"b1\"supportsMediaActions\"b1\"supportsDropIn\"b1\"supportsRMVonAppleTV\"b1\"supportsJustSiri\"b1\"supportsInstallManagedConfigurationProfile\"b1}"
+ "{_HMAccessoryCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@0:8"
+ "\x91Q"
+ "\xb1"
+ "\xf0\x83"
- "\x02\x12"
- "\x12\x121\""
- "\x12\x13\x11S1/\x01G"
- "\x1b"
- "%{public}@Completed sync processing with error: %@"
- "%{public}@Error in calling the accessoryInfoDataProvider delegate"
- "%{public}@Error occured while fetching the presence for users: %@"
- "%{public}@Home data access for this client is either not determined or restricted : %@"
- "%{public}@Managed Configuration Profile is not enabled"
- "%{public}@Manager is invalid, operation no longer applicable"
- "%{public}@Manager is invalided, dropping fetch response"
- "%{public}@Requesting home configuration with generation counter: %tu with QoS: %@"
- "%{public}@Sync operation failed with error: %@"
- ")\x11"
- "-[HMHome(HMUser) _inviteWithUserInformation:completionHandler:]"
- "<%@ [cloudkit=> accountStatus: %d, cdp: %d, firstImport: %d>] [ids=> status: %d identifier: %@ ] [device=> %@ - %@ - %@, s/w: %@] hh2: %d, numHomes: %lu, uuid: %@, mediaRouteID: %@, isPrimary: %d, wifi: %@, [eventrouter=> connected: %d date: %@, clients: %@] >"
- "@\"HMUserHomeAccessSchedule\""
- "@\"HMUserHomeAccessSettings\""
- "@28@0:8@16{_HMAccessoryCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}24"
- "@52@0:8@16B24B28B32Q36@44"
- "@56@0:8@16@24Q32@40@48"
- "HM.u.homeaccesssettings"
- "HMMutableUserHomeAccessSchedule"
- "HMMutableUserHomeAccessScheduleRule"
- "HMMutableUserHomeAccessSettings"
- "HMUserHomeAccessCodingKeyAccessAllowedToAllAccessories"
- "HMUserHomeAccessCodingKeyAllowedAccessoryCategoryTypes"
- "HMUserHomeAccessCodingKeyAllowedAccessoryIdentifiers"
- "HMUserHomeAccessCodingKeyAllowedRoomIdentifiers"
- "HMUserHomeAccessCodingKeySchedule"
- "HMUserHomeAccessCodingKeyScheduleRuleDaysOfTheWeek"
- "HMUserHomeAccessCodingKeyScheduleRuleEndTime"
- "HMUserHomeAccessCodingKeyScheduleRuleStartTime"
- "HMUserHomeAccessCodingKeyScheduleRuleValidFrom"
- "HMUserHomeAccessCodingKeyScheduleRuleValidThrough"
- "HMUserHomeAccessCodingKeyScheduleRules"
- "HMUserHomeAccessSchedule"
- "HMUserHomeAccessScheduleRule"
- "HMUserHomeAccessSettings"
- "HMUserInviteInformationHomeAccessSettingsCodingKey"
- "Hindsight"
- "Home Access Settings"
- "ManagedConfigurationProfile"
- "T@\"HMUserHomeAccessSchedule\",C,D"
- "T@\"HMUserHomeAccessSchedule\",C,V_schedule"
- "T@\"HMUserHomeAccessSettings\",C,D"
- "T@\"HMUserHomeAccessSettings\",C,V_homeAccessSettings"
- "T@\"NSArray\",C,V_rules"
- "T@\"NSDate\",C,D"
- "T@\"NSDate\",C,V_validFrom"
- "T@\"NSDate\",C,V_validThrough"
- "T@\"NSDate\",R"
- "T@\"NSDateComponents\",C,D"
- "T@\"NSDateComponents\",C,V_endTime"
- "T@\"NSDateComponents\",C,V_startTime"
- "T@\"NSSet\",C,V_allowedAccessoryCategoryTypes"
- "T@\"NSSet\",C,V_allowedAccessoryIdentifiers"
- "T@\"NSSet\",C,V_allowedRoomIdentifiers"
- "T@\"NSString\",R,N,V_currrentAccessoryMediaRouteId"
- "TB,D,GisAccessAllowedToAllAccessories"
- "TB,GisAccessAllowedToAllAccessories,V_accessAllowedToAllAccessories"
- "TB,N,V_supports40e39e789f11ed6f1738"
- "TB,R,GisAccessCurrentlyAllowed"
- "TB,R,GisExpired"
- "TQ,V_daysOfTheWeek"
- "T{_HMAccessoryCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1},R,N,V_capabilities"
- "_accessAllowedToAllAccessories"
- "_allowedAccessoryCategoryTypes"
- "_allowedAccessoryIdentifiers"
- "_allowedRoomIdentifiers"
- "_currrentAccessoryMediaRouteId"
- "_daysOfTheWeek"
- "_endTime"
- "_homeAccessSettings"
- "_inviteWithUserInformation:completionHandler:"
- "_rules"
- "_schedule"
- "_startTime"
- "_supports40e39e789f11ed6f1738"
- "_validFrom"
- "_validThrough"
- "accessAllowedToAllAccessories"
- "accessCurrentlyAllowed"
- "allowedAccessoryCategoryTypes"
- "allowedAccessoryIdentifiers"
- "allowedRoomIdentifiers"
- "currrentAccessoryMediaRouteId"
- "daysOfTheWeek"
- "endTime"
- "endTine"
- "expired"
- "hasSupports40e39e789f11ed6f1738"
- "hm_uuid:identifierSalt:withSalts:"
- "homeAccessSettings"
- "initWithHomeManager:timeout:"
- "initWithSession:setupSession:"
- "initWithStartTime:endTime:"
- "initWithStartTime:endTime:daysOfTheWeek:validFrom:validThrough:"
- "initWithUser:administrator:remoteAccess:announceAccess:camerasAccessLevel:homeAccessSettings:"
- "isAccessAllowedToAllAccessories"
- "isAccessCurrentlyAllowed"
- "rules"
- "schedule"
- "setAccessAllowedToAllAccessories:"
- "setAllowedAccessoryCategoryTypes:"
- "setAllowedAccessoryIdentifiers:"
- "setAllowedRoomIdentifiers:"
- "setDaysOfTheWeek:"
- "setEndTime:"
- "setHasSupports40e39e789f11ed6f1738:"
- "setHomeAccessSettings:"
- "setRules:"
- "setSchedule:"
- "setStartTime:"
- "setSupports40e39e789f11ed6f1738:"
- "setValidFrom:"
- "setValidThrough:"
- "startTime"
- "supports40e39e789f11ed6f1738"
- "validFrom"
- "validThrough"
- "{?=\"supports2c25465bb0b47366\"b1\"supports89024c1cadcb8b00\"b1\"supports90bb069d6bx54e7\"b1\"supportsAnnounce\"b1\"supportsAssistantAccessControl\"b1\"supportsAudioReturnChannel\"b1\"supportsCaptiveNetworks\"b1\"supportsCloudDataSync\"b1\"supportsCompanionInitiatedRestart\"b1\"supportsCoordinationDoorbellChime\"b1\"supportsDeviceSetup\"b1\"supportsDoorbellChime\"b1\"supportsHomeHub\"b1\"supportsHomeInvitation\"b1\"supportsHomeLevelAnalyticsAndImprovementSetting\"b1\"supportsHomeLevelLocationServiceSetting\"b1\"supportsKeyTransferClient\"b1\"supportsKeyTransferServer\"b1\"supportsKeychainSync\"b1\"supportsManagedConfigurationProfile\"b1\"supportsMediaActions\"b1\"supportsMessagedHomePodSettings\"b1\"supportsMultiUser\"b1\"supportsMusicAlarm\"b1\"supportsPreferredMediaUser\"b1\"supportsStandaloneMode\"b1\"supportsTargetControl\"b1\"supportsThirdPartyMusic\"b1\"supportsThreadBorderRouter\"b1\"supportsUserMediaSettings\"b1\"supportsWholeHouseAudio\"b1\"supportsf9cc0d9d6aa54e7\"b1}"
- "{?=\"supports40e39e789f11ed6f1738\"b1\"supports5348b248a25f84b0c83e\"b1\"supportsAccessCodes\"b1\"supportsAnnounce\"b1\"supportsCHIP\"b1\"supportsCameraActivityZones\"b1\"supportsCameraPackageDetection\"b1\"supportsCameraRecording\"b1\"supportsCameraRecordingReachabilityNotifications\"b1\"supportsCameraSignificantEventNotifications\"b1\"supportsCustomMediaApplicationDestination\"b1\"supportsFaceClassification\"b1\"supportsFirmwareUpdate\"b1\"supportsHomeHub\"b1\"supportsLockNotificationContext\"b1\"supportsMatterTTU\"b1\"supportsMediaActions\"b1\"supportsNaturalLighting\"b1\"supportsResidentFirmwareUpdate\"b1\"supportsResidentFirstAccessoryCommunication\"b1\"supportsRouterManagement\"b1\"supportsShortcutActions\"b1\"supportsSiriEndpointSetup\"b1\"supportsThreadBorderRouter\"b1\"supportsThreadNetworkCredentialSharing\"b1\"supportsUnifiedMediaNotifications\"b1\"supportsWakeOnLAN\"b1\"supportsWalletKey\"b1}"
- "{_HMAccessoryCapabilitiesStruct=\"supportsKeychainSync\"b1\"supportsDeviceSetup\"b1\"supportsKeyTransferClient\"b1\"supportsKeyTransferServer\"b1\"supportsStandaloneMode\"b1\"supportsCloudDataSync\"b1\"supportsWholeHouseAudio\"b1\"supportsAssistantAccessControl\"b1\"supportsHomeInvitation\"b1\"supportsTargetControl\"b1\"supportsMultiUser\"b1\"supportsHomeLevelLocationServiceSetting\"b1\"supportsCompanionInitiatedRestart\"b1\"supportsMusicAlarm\"b1\"supportsAnnounce\"b1\"supportsAudioAnalysis\"b1\"supportsThirdPartyMusic\"b1\"supportsPreferredMediaUser\"b1\"supportsThreadBorderRouter\"b1\"supportsDoorbellChime\"b1\"supportsUserMediaSettings\"b1\"supportsCoordinationDoorbellChime\"b1\"supportsHomeHub\"b1\"supportsAudioReturnChannel\"b1\"supportsManagedConfigurationProfile\"b1\"supportsCaptiveNetworks\"b1\"supportsMessagedHomePodSettings\"b1\"supportsMediaActions\"b1\"supportsDropIn\"b1\"supportsRMVonAppleTV\"b1\"supportsJustSiri\"b1}"
- "{_HMAccessoryCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@0:8"
- "\x81Q"

```
