## TimeSync

> `/System/Library/PrivateFrameworks/TimeSync.framework/Versions/A/TimeSync`

```diff

-1330.2.0.0.0
-  __TEXT.__text: 0x5383c
+1340.12.0.0.0
+  __TEXT.__text: 0x555d4
   __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x5c60
-  __TEXT.__const: 0x270
-  __TEXT.__oslogstring: 0x3598
-  __TEXT.__cstring: 0x6d85
-  __TEXT.__gcc_except_tab: 0xa4c
-  __TEXT.__unwind_info: 0x14b0
-  __TEXT.__objc_classname: 0x9cd
-  __TEXT.__objc_methname: 0xb091
-  __TEXT.__objc_methtype: 0x14f1
-  __TEXT.__objc_stubs: 0x6b60
+  __TEXT.__objc_methlist: 0x6020
+  __TEXT.__const: 0x2a0
+  __TEXT.__oslogstring: 0x389b
+  __TEXT.__cstring: 0x6db8
+  __TEXT.__gcc_except_tab: 0xa88
+  __TEXT.__unwind_info: 0x1698
+  __TEXT.__objc_classname: 0x9ce
+  __TEXT.__objc_methname: 0xb0c5
+  __TEXT.__objc_methtype: 0x14fe
+  __TEXT.__objc_stubs: 0x6b80
   __DATA_CONST.__got: 0x3b0
   __DATA_CONST.__const: 0x5d8
   __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2198
+  __DATA_CONST.__objc_selrefs: 0x2218
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x340
   __AUTH_CONST.__auth_got: 0x3b0
   __AUTH_CONST.__const: 0x970
   __AUTH_CONST.__cfstring: 0x5040
-  __AUTH_CONST.__objc_const: 0xbfe0
+  __AUTH_CONST.__objc_const: 0xb9d0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0x1bd0
-  __DATA.__objc_ivar: 0x824
+  __DATA.__objc_ivar: 0x830
   __DATA.__data: 0x488
-  __DATA.__bss: 0x138
+  __DATA.__bss: 0x140
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__bss: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 60ECBB59-39FE-3001-80EF-581C3D17D43A
-  Functions: 2132
-  Symbols:   4848
-  CStrings:  3704
+  UUID: A3577CF4-5BF5-3419-B845-73A794F8215A
+  Functions: 2459
+  Symbols:   5265
+  CStrings:  3713
 
Symbols:
+ +[TSPythonRunner executePythonCode:error:].cold.1
+ +[TSPythonRunner executePythonScript:error:].cold.1
+ +[TSPythonRunner executePythonScript:error:].cold.2
+ +[TSPythonRunner executePythonScript:error:].cold.3
+ +[TSTime timeConverter].cold.1
+ +[TSXDaemonServiceClient sharedDaemonServiceClient].cold.1
+ +[_TSF_TSDCallbackRefconMap sharedTSDCallbackRefconMap].cold.1
+ +[_TSF_TSDClockManager daemonClassNameForClockIdentifier:].cold.1
+ +[_TSF_TSDClockManager diagnosticInfoForClockIdentifier:daemonClassName:].cold.1
+ +[_TSF_TSDClockManager diagnosticInfo].cold.1
+ +[_TSF_TSDClockManager diagnosticInfo].cold.2
+ +[_TSF_TSDClockManager initialize].cold.1
+ +[_TSF_TSDClockManager sharedClockManager].cold.1
+ +[_TSF_TSDClockSyncManager sharedClockSyncManager].cold.1
+ +[_TSF_TSDgPTPManager diagnosticInfo].cold.1
+ +[_TSF_TSDgPTPManager diagnosticInfo].cold.2
+ +[_TSF_TSDgPTPManager initialize].cold.1
+ +[_TSF_TSDgPTPManager sharedgPTPManager].cold.1
+ +[_TSF_TSDgPTPPort diagnosticInfoForClockIdentifier:andPortNumber:].cold.1
+ -[IOKRegistryEntry(daemon_iokit_get_property_proxy) iodProperties].cold.1
+ -[IOKRegistryEntry(daemon_iokit_get_property_proxy) iodProperties].cold.2
+ -[IOKRegistryEntry(daemon_iokit_get_property_proxy) iodPropertyForKey:].cold.1
+ -[IOKRegistryEntry(daemon_iokit_get_property_proxy) iodPropertyForKey:].cold.2
+ -[TSClockInterface initWithClockIdentifier:].cold.1
+ -[TSClockManager init].cold.1
+ -[TSClockManager init].cold.2
+ -[TSClockManager init].cold.3
+ -[TSClockManagerInterface init].cold.1
+ -[TSClockPulser initWithPulseClock:].cold.1
+ -[TSClockPulser initWithPulseClock:].cold.2
+ -[TSClockPulser stopPulsing].cold.1
+ -[TSDCKernelClock convertFromDomainIntervalToTimeSyncTimeInterval:].cold.1
+ -[TSDCKernelClock convertFromDomainIntervalToTimeSyncTimeInterval:].cold.2
+ -[TSDCKernelClock convertFromDomainTime:toMachAbsoluteTime:withCount:].cold.1
+ -[TSDCKernelClock convertFromDomainTime:toMachAbsoluteTime:withCount:].cold.2
+ -[TSDCKernelClock convertFromDomainTime:toTimeSyncTime:withCount:].cold.1
+ -[TSDCKernelClock convertFromDomainTime:toTimeSyncTime:withCount:].cold.2
+ -[TSDCKernelClock convertFromDomainToTimeSyncTime:].cold.1
+ -[TSDCKernelClock convertFromDomainToTimeSyncTime:].cold.2
+ -[TSDCKernelClock convertFromMachAbsoluteTime:toDomainTime:withCount:].cold.1
+ -[TSDCKernelClock convertFromMachAbsoluteTime:toDomainTime:withCount:].cold.2
+ -[TSDCKernelClock convertFromTimeSyncTime:toDomainTime:withCount:].cold.1
+ -[TSDCKernelClock convertFromTimeSyncTime:toDomainTime:withCount:].cold.2
+ -[TSDCKernelClock convertFromTimeSyncTimeIntervalToDomainInterval:].cold.1
+ -[TSDCKernelClock convertFromTimeSyncTimeIntervalToDomainInterval:].cold.2
+ -[TSDCKernelClock convertFromTimeSyncToDomainTime:].cold.1
+ -[TSDCKernelClock convertFromTimeSyncToDomainTime:].cold.2
+ -[TSDCKernelClock getMachAbsoluteRateRatioNumerator:denominator:machAnchor:andDomainAnchor:withError:].cold.1
+ -[TSDCKernelClock getMachAbsoluteRateRatioNumerator:denominator:machAnchor:andDomainAnchor:withError:].cold.2
+ -[TSDCKernelClock getMachAbsoluteRateRatioNumerator:denominator:machAnchor:andDomainAnchor:withError:].cold.3
+ -[TSDCKernelClock getTimeSyncTimeRateRatioNumerator:denominator:timeSyncAnchor:andDomainAnchor:withError:].cold.1
+ -[TSDCKernelClock updateTimeSyncTime:timeSyncInterval:domainTime:domainInterval:].cold.1
+ -[TSDCKernelClock updateTimeSyncTime:timeSyncInterval:domainTime:domainInterval:].cold.2
+ -[TSDCKernelClock updateTimeSyncTime:timeSyncInterval:domainTime:domainInterval:].cold.3
+ -[TSDCKernelClock updateTimeSyncTime:timeSyncInterval:domainTime:domainInterval:].cold.4
+ -[TSDCTranslationClock initWithClockIdentifier:].cold.1
+ -[TSDCUserFilteredClock getMachAbsoluteRateRatioNumerator:denominator:machAnchor:andDomainAnchor:withError:].cold.1
+ -[TSDCgPTPClock convertFrom32BitASTime:toMachAbsoluteTime:withCount:].cold.1
+ -[TSDCgPTPClock convertFrom32BitASTime:toMachAbsoluteTime:withCount:].cold.2
+ -[TSDCgPTPClock convertFrom32BitASTime:toTimeSyncTime:withCount:].cold.1
+ -[TSDCgPTPClock convertFrom32BitASTime:toTimeSyncTime:withCount:].cold.2
+ -[TSDCgPTPClock convertFrom32BitASToTimeSyncTime:].cold.1
+ -[TSDCgPTPClock convertFromDomainIntervalToTimeSyncTimeInterval:].cold.1
+ -[TSDCgPTPClock convertFromDomainIntervalToTimeSyncTimeInterval:].cold.2
+ -[TSDCgPTPClock convertFromDomainTime:toMachAbsoluteTime:withCount:].cold.1
+ -[TSDCgPTPClock convertFromDomainTime:toMachAbsoluteTime:withCount:].cold.2
+ -[TSDCgPTPClock convertFromDomainTime:toTimeSyncTime:withCount:].cold.1
+ -[TSDCgPTPClock convertFromDomainTime:toTimeSyncTime:withCount:].cold.2
+ -[TSDCgPTPClock convertFromDomainTimeToTimeSyncTime:grandmasterUsed:portNumber:].cold.1
+ -[TSDCgPTPClock convertFromMachAbsoluteTime:toDomainTime:withCount:].cold.1
+ -[TSDCgPTPClock convertFromMachAbsoluteTime:toDomainTime:withCount:].cold.2
+ -[TSDCgPTPClock convertFromTimeSyncTime:toDomainTime:withCount:].cold.1
+ -[TSDCgPTPClock convertFromTimeSyncTime:toDomainTime:withCount:].cold.2
+ -[TSDCgPTPClock convertFromTimeSyncTimeIntervalToDomainInterval:].cold.1
+ -[TSDCgPTPClock convertFromTimeSyncTimeIntervalToDomainInterval:].cold.2
+ -[TSDCgPTPClock getMachAbsoluteRateRatioNumerator:denominator:machAnchor:andDomainAnchor:forGrandmasterIdentity:portNumber:withError:].cold.1
+ -[TSDCgPTPClock getMachAbsoluteRateRatioNumerator:denominator:machAnchor:andDomainAnchor:forGrandmasterIdentity:portNumber:withError:].cold.2
+ -[TSDCgPTPClock getMachAbsoluteRateRatioNumerator:denominator:machAnchor:andDomainAnchor:forGrandmasterIdentity:portNumber:withError:].cold.3
+ -[TSDCgPTPClock getTimeSyncTimeRateRatioNumerator:denominator:timeSyncAnchor:andDomainAnchor:forGrandmasterIdentity:portNumber:withError:].cold.1
+ -[TSDCgPTPClock updateWithSyncInfoValid:syncFlags:timeSyncTime:domainTimeHi:domainTimeLo:cumulativeScaledRate:inverseCumulativeScaledRate:grandmasterID:localPortNumber:].cold.1
+ -[TSDCgPTPClock updateWithSyncInfoValid:syncFlags:timeSyncTime:domainTimeHi:domainTimeLo:cumulativeScaledRate:inverseCumulativeScaledRate:grandmasterID:localPortNumber:].cold.2
+ -[TSKernelClock initWithClockIdentifier:].cold.1
+ -[TSKernelClock initWithImplDC:].cold.1
+ -[TSTAIUTCValue init].cold.1
+ -[TSTranslationClock initWithTranslationClock:].cold.1
+ -[TSUserFilteredClock initWithImplDC:].cold.1
+ -[TSXTranslationClock convertFromDomainIntervalToTimeSyncTimeInterval:].cold.1
+ -[TSXTranslationClock convertFromDomainIntervalToTimeSyncTimeInterval:].cold.2
+ -[TSXTranslationClock convertFromDomainTime:toMachAbsoluteTime:withCount:].cold.1
+ -[TSXTranslationClock convertFromDomainTime:toMachAbsoluteTime:withCount:].cold.2
+ -[TSXTranslationClock convertFromDomainTime:toTimeSyncTime:withCount:].cold.1
+ -[TSXTranslationClock convertFromDomainTime:toTimeSyncTime:withCount:].cold.2
+ -[TSXTranslationClock convertFromDomainToTimeSyncTime:].cold.1
+ -[TSXTranslationClock convertFromDomainToTimeSyncTime:].cold.2
+ -[TSXTranslationClock convertFromMachAbsoluteTime:toDomainTime:withCount:].cold.1
+ -[TSXTranslationClock convertFromMachAbsoluteTime:toDomainTime:withCount:].cold.2
+ -[TSXTranslationClock convertFromTimeSyncTime:toDomainTime:withCount:].cold.1
+ -[TSXTranslationClock convertFromTimeSyncTime:toDomainTime:withCount:].cold.2
+ -[TSXTranslationClock convertFromTimeSyncTimeIntervalToDomainInterval:].cold.1
+ -[TSXTranslationClock convertFromTimeSyncTimeIntervalToDomainInterval:].cold.2
+ -[TSXTranslationClock convertFromTimeSyncToDomainTime:].cold.1
+ -[TSXTranslationClock convertFromTimeSyncToDomainTime:].cold.2
+ -[TSXTranslationClock getTimeSyncTimeRateRatioNumerator:denominator:timeSyncAnchor:andDomainAnchor:withError:].cold.1
+ -[TSgPTPClock initWithImplDC:].cold.1
+ -[TSgPTPFDEtEPort initWithImplDC:].cold.1
+ -[TSgPTPFDPtPPort initWithImplDC:].cold.1
+ -[TSgPTPLocalClockPort initWithImplDC:].cold.1
+ -[TSgPTPManager init].cold.1
+ -[TSgPTPNetworkPort initWithImplDC:].cold.1
+ -[TSgPTPPort initWithImplDC:].cold.1
+ -[TSgPTPPort initWithImplDC:].cold.2
+ -[TSgPTPUnicastLinkLayerEtEPort initWithImplDC:].cold.1
+ -[TSgPTPUnicastLinkLayerPtPPort initWithImplDC:].cold.1
+ -[TSgPTPUnicastUDPv4EtEPort initWithImplDC:].cold.1
+ -[TSgPTPUnicastUDPv4PtPPort initWithImplDC:].cold.1
+ -[TSgPTPUnicastUDPv6EtEPort initWithImplDC:].cold.1
+ -[TSgPTPUnicastUDPv6PtPPort initWithimplDC:].cold.1
+ -[_TSF_IODConnection initWithService:andType:].cold.1
+ -[_TSF_TSDClockManager addMappingFromClockID:toCoreAudioClockDomain:error:].cold.1
+ -[_TSF_TSDClockManager addTSNCaptureServicesWithError:].cold.1
+ -[_TSF_TSDClockManager addUserFilteredClockWithMachInterval:domainInterval:usingFilterShift:isAdaptive:error:].cold.1
+ -[_TSF_TSDClockManager addgPTPServicesWithError:].cold.1
+ -[_TSF_TSDClockManager classNameForClockService:].cold.1
+ -[_TSF_TSDClockManager getTimeSyncTimeClockID:error:].cold.1
+ -[_TSF_TSDClockManager getTimeSyncTimeIsMachAbsolute:error:].cold.1
+ -[_TSF_TSDClockManager initWithPid:].cold.1
+ -[_TSF_TSDClockManager initWithPid:].cold.2
+ -[_TSF_TSDClockManager nextAvailableDynamicClockID:error:].cold.1
+ -[_TSF_TSDClockManager releaseDynamicClockID:error:].cold.1
+ -[_TSF_TSDClockManager removeMappingFromClockIDToCoreAudioClockDomainForClockID:error:].cold.1
+ -[_TSF_TSDClockManager removeTSNCaptureServicesWithError:].cold.1
+ -[_TSF_TSDClockManager removeUserFilteredClockWithIdentifier:error:].cold.1
+ -[_TSF_TSDClockManager removegPTPServicesWithError:].cold.1
+ -[_TSF_TSDClockSync _handleNotification:withArgs:ofCount:].cold.1
+ -[_TSF_TSDClockSync _handleNotification:withArgs:ofCount:].cold.2
+ -[_TSF_TSDClockSync initWithClockIdentifier:pid:].cold.1
+ -[_TSF_TSDClockSync initWithClockIdentifier:pid:].cold.2
+ -[_TSF_TSDClockSync initWithClockIdentifier:pid:].cold.3
+ -[_TSF_TSDClockSync registerAsyncCallback].cold.1
+ -[_TSF_TSDIOKServiceMatcher init].cold.1
+ -[_TSF_TSDIOKServiceMatcher init].cold.2
+ -[_TSF_TSDIOKServiceMatcher init].cold.3
+ -[_TSF_TSDIOKServiceMatcher init].cold.4
+ -[_TSF_TSDIOKServiceMatcher startNotificationsWithMatchingDictionary:].cold.1
+ -[_TSF_TSDIOKServiceMatcher startNotificationsWithMatchingDictionary:].cold.2
+ -[_TSF_TSDKernelClock _lockState].cold.1
+ -[_TSF_TSDKernelClock convertFromDomainIntervalToMachAbsoluteInterval:].cold.1
+ -[_TSF_TSDKernelClock convertFromDomainIntervalToTimeSyncTimeInterval:].cold.1
+ -[_TSF_TSDKernelClock convertFromDomainTime:toMachAbsoluteTime:withCount:].cold.1
+ -[_TSF_TSDKernelClock convertFromDomainTime:toTimeSyncTime:withCount:].cold.1
+ -[_TSF_TSDKernelClock convertFromDomainToMachAbsoluteTime:].cold.1
+ -[_TSF_TSDKernelClock convertFromDomainToTimeSyncTime:].cold.1
+ -[_TSF_TSDKernelClock convertFromMachAbsoluteIntervalToDomainInterval:].cold.1
+ -[_TSF_TSDKernelClock convertFromMachAbsoluteTime:toDomainTime:withCount:].cold.1
+ -[_TSF_TSDKernelClock convertFromMachAbsoluteToDomainTime:].cold.1
+ -[_TSF_TSDKernelClock convertFromTimeSyncTime:toDomainTime:withCount:].cold.1
+ -[_TSF_TSDKernelClock convertFromTimeSyncTimeIntervalToDomainInterval:].cold.1
+ -[_TSF_TSDKernelClock convertFromTimeSyncToDomainTime:].cold.1
+ -[_TSF_TSDKernelClock getCoreAudioReanchors].cold.1
+ -[_TSF_TSDKernelClock getMachAbsoluteRateRatioNumerator:denominator:machAnchor:andDomainAnchor:withError:].cold.1
+ -[_TSF_TSDKernelClock getTimeSyncTimeRateRatioNumerator:denominator:timeSyncAnchor:andDomainAnchor:withError:].cold.1
+ -[_TSF_TSDKernelClock hostRateRatio].cold.1
+ -[_TSF_TSDKernelClock initWithClockIdentifier:pid:].cold.1
+ -[_TSF_TSDKernelClock initWithClockIdentifier:pid:].cold.2
+ -[_TSF_TSDKernelClock initWithClockIdentifier:pid:].cold.3
+ -[_TSF_TSDKernelClock initWithClockIdentifier:pid:].cold.4
+ -[_TSF_TSDKernelClock initWithClockIdentifier:pid:].cold.5
+ -[_TSF_TSDKernelClock registerAsyncCallback].cold.1
+ -[_TSF_TSDKernelClock updateCoreAudioReanchors:].cold.1
+ -[_TSF_TSDKextNotifier init].cold.1
+ -[_TSF_TSDKextNotifier init].cold.2
+ -[_TSF_TSDKextNotifier notifyWhenServiceIsAvailable:].cold.1
+ -[_TSF_TSDKextNotifier notifyWhenServiceIsUnavailable:].cold.1
+ -[_TSF_TSDUserFilteredClock addTimestampWithMachAbsolute:andDomainTime:error:].cold.1
+ -[_TSF_TSDUserFilteredClock resetFilterToNominal:error:].cold.1
+ -[_TSF_TSDUserFilteredClock resetSyncServiceWithError:].cold.1
+ -[_TSF_TSDgPTPClock addLinkLayerPortOnInterfaceNamed:allocatedPortNumber:error:].cold.1
+ -[_TSF_TSDgPTPClock addReverseSyncOnInterfaceNamed:withDomainNumner:syncInterval:error:].cold.1
+ -[_TSF_TSDgPTPClock addUnicastLinkLayerEtEPortOnInterfaceNamed:withDestinationAddress:allocatedPortNumber:error:].cold.1
+ -[_TSF_TSDgPTPClock addUnicastLinkLayerPtPPortOnInterfaceNamed:withDestinationAddress:allocatedPortNumber:error:].cold.1
+ -[_TSF_TSDgPTPClock addUnicastUDPv4EtEPortOnInterfaceNamed:withDestinationAddress:allocatedPortNumber:error:].cold.1
+ -[_TSF_TSDgPTPClock addUnicastUDPv4PtPPortOnInterfaceNamed:withDestinationAddress:allocatedPortNumber:error:].cold.1
+ -[_TSF_TSDgPTPClock addUnicastUDPv6EtEPortOnInterfaceNamed:withDestinationAddress:allocatedPortNumber:error:].cold.1
+ -[_TSF_TSDgPTPClock addUnicastUDPv6PtPPortOnInterfaceNamed:withDestinationAddress:allocatedPortNumber:error:].cold.1
+ -[_TSF_TSDgPTPClock convertFrom128BitgPTPTimeToMachAbsoluteTime:grandmasterUsed:portNumber:].cold.1
+ -[_TSF_TSDgPTPClock convertFrom128BitgPTPTimeToTimeSyncTime:grandmasterUsed:portNumber:].cold.1
+ -[_TSF_TSDgPTPClock convertFrom32BitASTime:toMachAbsoluteTime:withCount:].cold.1
+ -[_TSF_TSDgPTPClock convertFrom32BitASTime:toTimeSyncTime:withCount:].cold.1
+ -[_TSF_TSDgPTPClock convertFrom32BitASToMachAbsoluteTime:].cold.1
+ -[_TSF_TSDgPTPClock convertFrom32BitASToTimeSyncTime:].cold.1
+ -[_TSF_TSDgPTPClock convertFromDomainTimeToTimeSyncTime:grandmasterUsed:portNumber:].cold.1
+ -[_TSF_TSDgPTPClock convertFromDomainToMachAbsoluteTime:grandmasterUsed:portNumber:].cold.1
+ -[_TSF_TSDgPTPClock convertFromMachAbsoluteTo128BitgPTPTime:grandmasterUsed:portNumber:].cold.1
+ -[_TSF_TSDgPTPClock convertFromMachAbsoluteToDomainTime:grandmasterUsed:portNumber:].cold.1
+ -[_TSF_TSDgPTPClock convertFromTimeSyncTimeTo128BitgPTPTime:grandmasterUsed:portNumber:].cold.1
+ -[_TSF_TSDgPTPClock convertFromTimeSyncTimeToDomainTime:grandmasterUsed:portNumber:].cold.1
+ -[_TSF_TSDgPTPClock gPTPTimeFromMachAbsoluteTime:].cold.1
+ -[_TSF_TSDgPTPClock gPTPTimeFromTimeSyncTime:].cold.1
+ -[_TSF_TSDgPTPClock getMachAbsoluteRateRatioNumerator:denominator:machAnchor:andDomainAnchor:forGrandmasterIdentity:portNumber:withError:].cold.1
+ -[_TSF_TSDgPTPClock getSyncInfoWithSyncInfoValid:syncFlags:timeSyncTime:domainTimeHi:domainTimeLo:cumulativeScaledRate:inverseCumulativeScaledRate:grandmasterID:localPortNumber:error:].cold.1
+ -[_TSF_TSDgPTPClock getTimeSyncTimeRateRatioNumerator:denominator:timeSyncAnchor:andDomainAnchor:forGrandmasterIdentity:portNumber:withError:].cold.1
+ -[_TSF_TSDgPTPClock machAbsoluteFromgPTPTime:].cold.1
+ -[_TSF_TSDgPTPClock removeLinkLayerPortFromInterfaceNamed:error:].cold.1
+ -[_TSF_TSDgPTPClock removeReverseSyncFromInterfaceNamed:withDomainNumner:error:].cold.1
+ -[_TSF_TSDgPTPClock removeUnicastLinkLayerEtEPortFromInterfaceNamed:withDestinationAddress:error:].cold.1
+ -[_TSF_TSDgPTPClock removeUnicastLinkLayerPtPPortFromInterfaceNamed:withDestinationAddress:error:].cold.1
+ -[_TSF_TSDgPTPClock removeUnicastUDPv4EtEPortFromInterfaceNamed:withDestinationAddress:error:].cold.1
+ -[_TSF_TSDgPTPClock removeUnicastUDPv4PtPPortFromInterfaceNamed:withDestinationAddress:error:].cold.1
+ -[_TSF_TSDgPTPClock removeUnicastUDPv6EtEPortFromInterfaceNamed:withDestinationAddress:error:].cold.1
+ -[_TSF_TSDgPTPClock removeUnicastUDPv6PtPPortFromInterfaceNamed:withDestinationAddress:error:].cold.1
+ -[_TSF_TSDgPTPClock timeSyncTimeFromgPTPTime:].cold.1
+ -[_TSF_TSDgPTPManager addAVBPTPInstanceIndex:identifier:error:].cold.1
+ -[_TSF_TSDgPTPManager addAirPlayPTPInstance:error:].cold.1
+ -[_TSF_TSDgPTPManager addCopresencePTPInstance:error:].cold.1
+ -[_TSF_TSDgPTPManager addPTPInstance:error:].cold.1
+ -[_TSF_TSDgPTPManager addTimeOfDayPTPInstance:error:].cold.1
+ -[_TSF_TSDgPTPManager init].cold.1
+ -[_TSF_TSDgPTPManager init].cold.2
+ -[_TSF_TSDgPTPManager logInterfaceStatisticsWithError:].cold.1
+ -[_TSF_TSDgPTPManager removeAVBPTPInstanceWithIndex:error:].cold.1
+ -[_TSF_TSDgPTPManager removeAirPlayPTPInstanceWithError:].cold.1
+ -[_TSF_TSDgPTPManager removeCopresencePTPInstanceWithError:].cold.1
+ -[_TSF_TSDgPTPManager removePTPInstanceWithIdentifier:error:].cold.1
+ -[_TSF_TSDgPTPNetworkPort deregisterAsyncCallbackError:].cold.1
+ -[_TSF_TSDgPTPNetworkPort disablePortError:].cold.1
+ -[_TSF_TSDgPTPNetworkPort enablePortError:].cold.1
+ -[_TSF_TSDgPTPNetworkPort initWithService:pid:].cold.1
+ -[_TSF_TSDgPTPNetworkPort logNotifyTest]
+ -[_TSF_TSDgPTPNetworkPort overrideReceiveMatchingWithRemoteClockIdentity:remotePortNumber:error:].cold.1
+ -[_TSF_TSDgPTPNetworkPort requestRemoteMessageIntervalsWithPDelayMessageInterval:syncMessageInterval:announceMessageInterval:error:].cold.1
+ -[_TSF_TSDgPTPNetworkPort restoreReceiveMatchingError:].cold.1
+ -[_TSF_TSDgPTPPort initWithService:pid:].cold.1
+ -[_TSF_TSDgPTPPort initWithService:pid:].cold.2
+ -[_TSF_TSDgPTPPort initWithService:pid:].cold.3
+ -[_TSF_TSDgPTPPort initWithService:pid:].cold.4
+ -[_TSF_TSDgPTPPort initWithService:pid:].cold.5
+ -[_TSF_TSDgPTPPort logNotifyTest]
+ GCC_except_table35
+ GCC_except_table42
+ GCC_except_table43
+ GCC_except_table57
+ GCC_except_table58
+ OBJC_IVAR_$__TSF_TSDClockSync._logNotifyTest
+ OBJC_IVAR_$__TSF_TSDKernelClock._logNotifyTest
+ OBJC_IVAR_$__TSF_TSDgPTPPort._logNotifyTest
+ TimeSyncClockAddAWDLPortAndGetIdentity.cold.1
+ TimeSyncClockAddAWDLPortAndGetIdentity.cold.2
+ TimeSyncClockAddAWDLPortAndGetIdentity.cold.3
+ TimeSyncClockAddAWDLPortAndGetIdentity.cold.4
+ TimeSyncClockAddTimestamps.cold.1
+ TimeSyncClockAddUDPv4EndToEndPortAndGetIdentity.cold.1
+ TimeSyncClockAddUDPv4EndToEndPortAndGetIdentity.cold.2
+ TimeSyncClockAddUDPv4EndToEndPortAndGetIdentity.cold.3
+ TimeSyncClockAddUDPv4EndToEndPortAndGetIdentity.cold.4
+ TimeSyncClockAddUDPv6EndToEndPortAndGetIdentity.cold.1
+ TimeSyncClockAddUDPv6EndToEndPortAndGetIdentity.cold.2
+ TimeSyncClockAddUDPv6EndToEndPortAndGetIdentity.cold.3
+ TimeSyncClockAddUDPv6EndToEndPortAndGetIdentity.cold.4
+ TimeSyncClockCreateAudioClockDeviceUID.cold.1
+ TimeSyncClockCreateAudioClockDeviceUID.cold.2
+ TimeSyncClockCreateWithClockIdentifier.cold.1
+ TimeSyncClockCreateWithClockIdentifier.cold.2
+ TimeSyncClockDispose.cold.1
+ TimeSyncClockGetClockIdentifier.cold.1
+ TimeSyncClockGetClockRate.cold.1
+ TimeSyncClockGetClockRateAnchorsAndGrandmasterIdentity.cold.1
+ TimeSyncClockGetClockRateAnchorsAndGrandmasterIdentity.cold.2
+ TimeSyncClockGetClockRateAndAnchors.cold.1
+ TimeSyncClockGetClockTimeAndGrandmasterIdentityLocalPortForHostTime.cold.1
+ TimeSyncClockGetClockTimeAndGrandmasterIdentityLocalPortForHostTime.cold.2
+ TimeSyncClockGetClockTimeForHostTime.cold.1
+ TimeSyncClockGetHostTimeAndGrandmasterIdentityLocalPortForClockTime.cold.1
+ TimeSyncClockGetHostTimeAndGrandmasterIdentityLocalPortForClockTime.cold.2
+ TimeSyncClockGetHostTimeForClockTime.cold.1
+ TimeSyncClockGetLockState.cold.1
+ TimeSyncClockGetgPTPGrandmasterIdentity.cold.1
+ TimeSyncClockGetgPTPGrandmasterIdentity.cold.2
+ TimeSyncClockRemoveAWDLPort.cold.1
+ TimeSyncClockRemoveAWDLPort.cold.2
+ TimeSyncClockRemoveUDPv4EndToEndPort.cold.1
+ TimeSyncClockRemoveUDPv4EndToEndPort.cold.2
+ TimeSyncClockRemoveUDPv6EndToEndPort.cold.1
+ TimeSyncClockRemoveUDPv6EndToEndPort.cold.2
+ TimeSyncClockResetClock.cold.1
+ TimeSyncClockResetFilter.cold.1
+ TimeSyncClockSetAllPortRemoteSyncMessageIntervals.cold.1
+ TimeSyncClockSetAllPortRemoteSyncMessageIntervals.cold.2
+ TimeSyncClockSetConnectionInterruptedCallback.cold.1
+ TimeSyncClockSetLockStateChangeCallback.cold.1
+ TimeSyncClockSetMasterChangeCallback.cold.1
+ TimeSyncClockSetTimeSyncTimeChangeCallback.cold.1
+ TimeSyncClockSetgPTPGrandmasterAndPortChangeCallback.cold.1
+ TimeSyncClockSetgPTPGrandmasterChangeCallback.cold.1
+ TimeSyncClockSetgPTPLocalPortChangeCallback.cold.1
+ TimeSyncCreateTimeSyncClockManagerConnectionCallbackWithInterruptedHandler.cold.1
+ TimeSyncGetClockMetricsWithSize.cold.1
+ TimeSyncGetClockMetricsWithSize.cold.2
+ TimeSyncGetClockMetricsWithSize.cold.3
+ TimeSyncGetClockMetricsWithSize.cold.4
+ TimeSyncGetClockMetricsWithSize.cold.5
+ TimeSyncGetPortMetricsWithSize.cold.1
+ TimeSyncGetPortMetricsWithSize.cold.2
+ TimeSyncGetPortMetricsWithSize.cold.3
+ TimeSyncGetPortMetricsWithSize.cold.4
+ TimeSyncGetPortMetricsWithSize.cold.5
+ TimeSyncGetPortMetricsWithSize.cold.6
+ TimeSyncGetPortMetricsWithSize.cold.7
+ TimeSyncPortCreateFromClock.cold.1
+ TimeSyncPortCreateFromClock.cold.2
+ TimeSyncPortCreateFromClock.cold.3
+ TimeSyncPortCreateFromClock.cold.4
+ TimeSyncPortCreateFromClock.cold.5
+ TimeSyncPortDisable.cold.1
+ TimeSyncPortDisable.cold.2
+ TimeSyncPortDisable.cold.3
+ TimeSyncPortDispose.cold.1
+ TimeSyncPortEnable.cold.1
+ TimeSyncPortEnable.cold.2
+ TimeSyncPortEnable.cold.3
+ TimeSyncPortGetCurrentPortInfo.cold.1
+ TimeSyncPortGetCurrentPortInfo.cold.2
+ TimeSyncPortGetCurrentPortInfo.cold.3
+ TimeSyncPortOverridePortReceiveMatching.cold.1
+ TimeSyncPortOverridePortReceiveMatching.cold.2
+ TimeSyncPortOverridePortReceiveMatching.cold.3
+ TimeSyncPortRestorePortReceiveMatching.cold.1
+ TimeSyncPortRestorePortReceiveMatching.cold.2
+ TimeSyncPortRestorePortReceiveMatching.cold.3
+ TimeSyncPortSetMACLookupTimeoutCallback.cold.1
+ TimeSyncPortSetRemoteSyncMessageIntervals.cold.1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ ___40-[_TSF_TSDgPTPNetworkPort logNotifyTest]_block_invoke
+ _objc_msgSend$logNotifyTest
+ logNotifyTest.onceToken
CStrings:
+ "%@Records = np.rec.array(np.genfromtxt(%@, dtype=None, delimiter=',', names=True, encoding='utf-8'))\n\ntau = %@Records.observation_interval\n%@ = %@Records.%@\n\n%@\n"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSClockManager.mm"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSInterface.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSKernelClock.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSTranslationClock.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSUserFilteredClock.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSgPTPClock.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSgPTPManager.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSgPTPPort.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/Analysis/TSPythonRunner.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/DC/TSDCKernelClock.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/DC/TSDCUserFilteredClock.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/DC/TSDCgPTPClock.mm"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/Utilities/TSClockPulser.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/XPC/TSXTranslationClock.mm"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/IOKRegistryEntryExtendedFramework.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDClockManager.mm"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDClockSync.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDKernelClock.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDKextNotifier.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDUserFilteredClock.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDgPTPClock.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDgPTPManager.m"
+ "/AppleInternal/Library/BuildRoots/e6f62b94-fc55-11ef-ade3-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDgPTPPort.m"
+ "TB,R,N,V_logNotifyTest"
+ "TSDClockSync _handleNotification kIOTimeSyncSyncNotificationGeneralSyncUpdate rateNumerator=%llu rateDenominator=%llu timeSyncAnchor=%llu domainAnchor=%llu"
+ "TSDClockSync _handleNotification kIOTimeSyncSyncNotificationPTPSyncUpdate cumulativeScaledRate=%llu inverseCumulativeScaledRate=%llu timeSyncAnchor=%llu domainAnchorHi=%llu domainAnchorLo=%llu grandmasterID=%llu localPortNumber=%u syncFlags=%u syncInfoValid=%u"
+ "TSDKernelClock _handleNotification kIOTimeSyncDomainNotificationEtEDelayStats localPortNumber=%u mean=%llu median=%llu stddev=%llu min=%llu max=%llu numberOfSamples=%u"
+ "TSDKernelClock _handleNotification notification=%u arg1=%llu arg2=%llu"
+ "TSDgPTPPort asyncNotificationsCallback notification=%u arg1=%llu arg2=%llu arg3=%llu arg4=%llu arg5=%llu arg6=%llu"
+ "_logNotifyTest"
+ "logNotifyTest"
+ "numArgs == 13"
+ "numArgs == 8"
+ "timeErrorRecords = np.rec.array(np.genfromtxt(%@, dtype=None, delimiter=',', names=True, encoding='utf-8'))\n\ntime = timeErrorRecords.time\ntimeError = timeErrorRecords.time_error\n\n"
+ "timesync_tsnotifytest"
+ "v32@0:8I16I20^{ScalarArgsArrayUserReference=[16Q]I}24"
- "%@Records = np.recfromtxt(%@, dtype=None, delimiter=',', names=True, encoding='utf-8')\n\ntau = %@Records.observation_interval\n%@ = %@Records.%@\n\n%@\n"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSClockManager.mm"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSInterface.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSKernelClock.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSTranslationClock.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSUserFilteredClock.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSgPTPClock.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSgPTPManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSgPTPPort.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/Analysis/TSPythonRunner.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/DC/TSDCKernelClock.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/DC/TSDCUserFilteredClock.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/DC/TSDCgPTPClock.mm"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/Utilities/TSClockPulser.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/XPC/TSXTranslationClock.mm"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/IOKRegistryEntryExtendedFramework.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDClockManager.mm"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDClockSync.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDKernelClock.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDKextNotifier.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDUserFilteredClock.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDgPTPClock.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDgPTPManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDgPTPPort.m"
- "numArgs == 4"
- "numArgs == 7"
- "timeErrorRecords = np.recfromtxt(%@, dtype=None, delimiter=',', names=True, encoding='utf-8')\n\ntime = timeErrorRecords.time\ntimeError = timeErrorRecords.time_error\n\n"
- "v32@0:8I16I20^{ScalarArgsArray=[16Q]I}24"

```
