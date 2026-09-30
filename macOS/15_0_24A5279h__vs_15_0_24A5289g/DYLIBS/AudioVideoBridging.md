## AudioVideoBridging

> `/System/Library/Frameworks/AudioVideoBridging.framework/Versions/A/AudioVideoBridging`

```diff

-1300.21.0.0.0
-  __TEXT.__text: 0x1b5cf4
+1300.22.0.0.0
+  __TEXT.__text: 0x1b6ad8
   __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_methlist: 0x186dc
+  __TEXT.__objc_methlist: 0x186e4
   __TEXT.__const: 0x4e0
-  __TEXT.__gcc_except_tab: 0x1b84
-  __TEXT.__cstring: 0x19665
-  __TEXT.__oslogstring: 0x632c
+  __TEXT.__gcc_except_tab: 0x1bbc
+  __TEXT.__cstring: 0x19716
+  __TEXT.__oslogstring: 0x64e9
   __TEXT.__ustring: 0x60
-  __TEXT.__unwind_info: 0x52e8
-  __TEXT.__objc_classname: 0x4443
-  __TEXT.__objc_methname: 0x24c0e
+  __TEXT.__unwind_info: 0x5318
+  __TEXT.__objc_classname: 0x4444
+  __TEXT.__objc_methname: 0x24c31
   __TEXT.__objc_methtype: 0x31e7
-  __TEXT.__objc_stubs: 0x137e0
+  __TEXT.__objc_stubs: 0x13800
   __DATA_CONST.__got: 0xf78
   __DATA_CONST.__const: 0x1238
   __DATA_CONST.__objc_classlist: 0xff8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7fd0
+  __DATA_CONST.__objc_selrefs: 0x7fd8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xdb8
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0x4d8
   __AUTH_CONST.__const: 0x1560
   __AUTH_CONST.__cfstring: 0x13300
-  __AUTH_CONST.__objc_const: 0x26da8
+  __AUTH_CONST.__objc_const: 0x26dc8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x9fb0
-  __DATA.__objc_ivar: 0x1364
+  __DATA.__objc_ivar: 0x1368
   __DATA.__data: 0x668
   __DATA.__bss: 0x148
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8282
-  Symbols:   16650
-  CStrings:  3164
+  Functions: 8289
+  Symbols:   16662
+  CStrings:  3170
 
Symbols:
+ -[AVBClock updateTimeSyncTime:timeSyncInterval:domainTime:domainInterval:].cold.1
+ -[AVBClock updateTimeSyncTime:timeSyncInterval:domainTime:domainInterval:].cold.2
+ -[AVBMediaClockSink hasMediaClockSource]
+ -[AVBPTPClock updateWithSyncInfoValid:syncFlags:timeSyncTime:domainTimeHi:domainTimeLo:cumulativeScaledRate:inverseCumulativeScaledRate:grandmasterID:localPortNumber:].cold.1
+ -[AVBPTPClock updateWithSyncInfoValid:syncFlags:timeSyncTime:domainTimeHi:domainTimeLo:cumulativeScaledRate:inverseCumulativeScaledRate:grandmasterID:localPortNumber:].cold.2
+ GCC_except_table24
+ GCC_except_table25
+ OBJC_IVAR_$_AVBIOKClockSync._lastLockState
+ ___block_descriptor_291_e8_32s40s48s56r64r72r80r88r96r104r112r120r128r136r144r152r_e11_v24?0Q8Q16l
+ ___copy_helper_block_e8_32s40s48s56r64r72r80r88r96r104r112r120r128r136r144r152r
+ ___destroy_helper_block_e8_32s40s48s56r64r72r80r88r96r104r112r120r128r136r144r152r
+ _objc_msgSend$hasMediaClockSource
- ___block_descriptor_283_e8_32s40s48s56r64r72r80r88r96r104r112r120r128r136r144r_e11_v24?0Q8Q16l
- ___copy_helper_block_e8_32s40s48s56r64r72r80r88r96r104r112r120r128r136r144r
- ___destroy_helper_block_e8_32s40s48s56r64r72r80r88r96r104r112r120r128r136r144r
CStrings:
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/1722Control/AVB1722ControlInterface.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AECP/AVB17221AECPAEMGeneralMessages.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AECP/AVB17221AECPAEMPTPInstanceMessages.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AECP/AVB17221AECPAEMSecurityMessages.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AECP/AVB17221AECPAEMStreamingMessages.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMAVBInterface.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMAudioCluster.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMAudioMap.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMAudioUnit.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMAuthenticationKey.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMBaseControl.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMClockDomain.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMClockDomainedModelObject.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMClockSource.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMCluster.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMControl.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMControlBlock.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMEntity.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMExternalPort.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMInternalPort.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMJack.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMLocale.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMMatrix.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMMatrixSignal.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMMemoryObject.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMMixer.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMModelObject.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMNamedClockDomainedModelObject.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMNamedModelObject.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMPTPInstance.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMPTPPort.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMPort.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSensorCluster.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSensorMap.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSensorUnit.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSignalCombiner.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSignalDemultiplexer.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSignalMultiplexer.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSignalPort.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSignalSelector.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSignalSplitter.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSignalTranscoder.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMStream.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMStreamFormat.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMStreamPort.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMStrings.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMTiming.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMUnit.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMVideoCluster.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMVideoMap.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMVideoUnit.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Analysis/AVBMediaClockFitter.mm"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Analysis/AVBTimeErrorAnalysis.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Analysis/AVBTimeErrorFilter.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Clock/AVBClock.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Clock/AVBClockManager.mm"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Clock/AVBIOKClockSync.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Clock/AVBPTPClock.mm"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/IOAVBFamily/AVB17221EntityDiscovery.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/IOAVBFamily/AVB1722MAAP.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/IOAVBFamily/AVBInterfaceStreamingManager.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/IOAVBFamily/AVBMRP.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/IOAVBFamily/AVBMSRPDomain.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/IOAVBFamily/AVBNub.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Interface/AVBATDECCCommandSequence.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Interface/AVBATDECCController.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Interface/AVBATDECCEntity.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Interface/AVBBuiltInAVDECCController.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Interface/AVBBuiltInAVDECCEntity.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Interface/AVBCentralManager.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Interface/AVBInterface.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Interface/AVBKextNotifier.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Interface/AVBVirtualEntity.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/MediaClockStream/AVBMediaClockInputStream.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/MediaClockStream/AVBMediaClockOutputStream.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/MediaClocking/AVBMediaClockDomain.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/MediaClocking/AVBMediaClockThread.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/PTP/AVBIOKPTPInstance.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/PTP/AVBIOKPTPPort.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/PTP/AVBPTPInstance.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/PTP/AVBPTPManager.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/PTP/AVBPTPPort.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Streams/AVBOutputStream.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Streams/AVBStream.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Utilities/AVBIntervalFilter.mm"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Utilities/AVBPythonRunner.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Utilities/AVBTimeLineFilter.mm"
+ "_threadShouldBeRunning"
+ "machNanoWake != AVBInvalidTime"
+ "newDomain != AVBInvalidTime"
+ "nowTimeSyncTime - timeSyncTime < limit"
+ "self.hasMediaClockSource"
+ "timeSyncTime < nowTimeSyncTime"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/1722Control/AVB1722ControlInterface.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AECP/AVB17221AECPAEMGeneralMessages.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AECP/AVB17221AECPAEMPTPInstanceMessages.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AECP/AVB17221AECPAEMSecurityMessages.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AECP/AVB17221AECPAEMStreamingMessages.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMAVBInterface.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMAudioCluster.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMAudioMap.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMAudioUnit.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMAuthenticationKey.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMBaseControl.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMClockDomain.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMClockDomainedModelObject.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMClockSource.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMCluster.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMConfiguration.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMControl.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMControlBlock.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMEntity.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMExternalPort.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMInternalPort.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMJack.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMLocale.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMMatrix.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMMatrixSignal.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMMemoryObject.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMMixer.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMModelObject.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMNamedClockDomainedModelObject.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMNamedModelObject.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMPTPInstance.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMPTPPort.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMPort.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSensorCluster.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSensorMap.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSensorUnit.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSignalCombiner.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSignalDemultiplexer.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSignalMultiplexer.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSignalPort.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSignalSelector.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSignalSplitter.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMSignalTranscoder.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMStream.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMStreamFormat.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMStreamPort.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMStrings.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMTiming.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMUnit.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMVideoCluster.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMVideoMap.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/AEM/AVB17221AEMVideoUnit.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Analysis/AVBMediaClockFitter.mm"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Analysis/AVBTimeErrorAnalysis.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Analysis/AVBTimeErrorFilter.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Clock/AVBClock.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Clock/AVBClockManager.mm"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Clock/AVBIOKClockSync.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Clock/AVBPTPClock.mm"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/IOAVBFamily/AVB17221EntityDiscovery.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/IOAVBFamily/AVB1722MAAP.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/IOAVBFamily/AVBInterfaceStreamingManager.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/IOAVBFamily/AVBMRP.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/IOAVBFamily/AVBMSRPDomain.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/IOAVBFamily/AVBNub.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Interface/AVBATDECCCommandSequence.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Interface/AVBATDECCController.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Interface/AVBATDECCEntity.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Interface/AVBBuiltInAVDECCController.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Interface/AVBBuiltInAVDECCEntity.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Interface/AVBCentralManager.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Interface/AVBInterface.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Interface/AVBKextNotifier.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Interface/AVBVirtualEntity.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/MediaClockStream/AVBMediaClockInputStream.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/MediaClockStream/AVBMediaClockOutputStream.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/MediaClocking/AVBMediaClockDomain.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/MediaClocking/AVBMediaClockThread.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/PTP/AVBIOKPTPInstance.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/PTP/AVBIOKPTPPort.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/PTP/AVBPTPInstance.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/PTP/AVBPTPManager.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/PTP/AVBPTPPort.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Streams/AVBOutputStream.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Streams/AVBStream.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Utilities/AVBIntervalFilter.mm"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Utilities/AVBPythonRunner.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/IOAVBFamily/AVBKit/Utilities/AVBTimeLineFilter.mm"

```
