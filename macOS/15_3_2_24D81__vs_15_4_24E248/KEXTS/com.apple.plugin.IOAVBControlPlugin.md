## com.apple.plugin.IOAVBControlPlugin

> `com.apple.plugin.IOAVBControlPlugin`

```diff

   __TEXT.__cstring: 0xc3a
   __TEXT.__os_log: 0x16b6
   __TEXT.__const: 0x8
-  __TEXT_EXEC.__text: 0x8898
+  __TEXT_EXEC.__text: 0x8980
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xd4
   __DATA.__common: 0x1c8

   __DATA_CONST.__mod_term_func: 0x58
   __DATA_CONST.__const: 0x61c0
   __DATA_CONST.__kalloc_type: 0x2c0
-  UUID: E8BD9AD8-2AAC-3414-84CA-C513EA57408A
-  Functions: 288
-  Symbols:   850
+  UUID: 8D6C8588-CC68-369A-865A-D5F77D3257B2
+  Functions: 289
+  Symbols:   852
   CStrings:  143
 
Symbols:
+ _ZN34IOAVB1722ApplicationControlService4initEhPhbP12OSDictionary.cold.1
+ _ZN44IOAVB1722ApplicationControlServiceUserClient16sendControlFrameEyj.cold.1
Functions:
~ __ZN44IOAVB1722ApplicationControlServiceUserClient4freeEv : 132 -> 136
~ __ZN44IOAVB1722ApplicationControlServiceUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv : 244 -> 232
- sub_fffffe000a997768
~ __ZN44IOAVB1722ApplicationControlServiceUserClient19addControlRoutingIDEy : 408 -> 428
~ __ZN44IOAVB1722ApplicationControlServiceUserClient22removeControlRoutingIDEy : 464 -> 456
~ __ZN44IOAVB1722ApplicationControlServiceUserClient16sendControlFrameEyj : 556 -> 488
~ __ZN44IOAVB1722ApplicationControlServiceUserClient19clientMemoryForTypeEjPjPP18IOMemoryDescriptor : 124 -> 128
~ __ZN23IOAVB1722ControlService5startEP9IOService : 1932 -> 1980
~ __ZN23IOAVB1722ControlService4stopEP9IOService : 324 -> 328
~ __ZN23IOAVB1722ControlService7messageEjP9IOServicePv : 852 -> 892
~ __ZN23IOAVB1722ControlService16sendControlFrameEP27IOAVB1722ControlServiceInfoPhm : 864 -> 856
~ __ZN23IOAVB1722ControlService9logPacketEPKhm : 476 -> 472
~ __ZN23IOAVB1722ControlService19filterReceivedFrameEPP6__mbufPPc : 648 -> 652
~ __ZN31IOAVB17221ACMPServiceUserClient20receivedControlFrameEP27IOAVB1722ControlServiceInfoPhm : 528 -> 536
~ __ZN31IOAVB17221AECPServiceUserClient20receivedControlFrameEP27IOAVB1722ControlServiceInfoPhm : 508 -> 512
~ __ZN20IOAVBMACAddressRange4freeEv : 100 -> 104
~ __ZN20IOAVBMACAddressRange4initEPhjb : 384 -> 392
~ __ZN20IOAVBMACAddressRange16changeMACAddressEPh : 24 -> 28
~ __ZN20IOAVBMACAddressRange18copyBaseMACAddressEPh : 24 -> 28
~ __ZN20IOAVBMACAddressRange18representsMACRangeEPS_ : 56 -> 60
~ __ZN30IOAVB1722MAAPServiceUserClient12initWithTaskEP4taskPvjP12OSDictionary : 340 -> 348
~ __ZN30IOAVB1722MAAPServiceUserClient4freeEv : 132 -> 136
~ __ZN30IOAVB1722MAAPServiceUserClient11clientCloseEv : 80 -> 88
~ __ZN30IOAVB1722MAAPServiceUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv : 124 -> 132
~ __ZN20IOAVB1722MAAPService21generateRandomMAAPMACEPht : 544 -> 532
~ __ZN20IOAVB1722MAAPService18maapProbeTimerFireEv : 840 -> 856
~ __ZN20IOAVB1722MAAPService21maapAnnounceTimerFireEv : 344 -> 340
~ __ZN20IOAVB1722MAAPService20allocateMulticastMACEPhPP15IOAVBMACAddress : 1020 -> 1036
~ __ZN20IOAVB1722MAAPService22deallocateMulticastMACEP15IOAVBMACAddress : 316 -> 320
~ __ZN34IOAVB1722ApplicationControlService4initEhPhbP12OSDictionary : 436 -> 368
~ __ZN34IOAVB1722ApplicationControlService4freeEv : 136 -> 140
~ __ZN34IOAVB1722ApplicationControlService13addUserClientEP44IOAVB1722ApplicationControlServiceUserClient : 116 -> 124
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBControlPlugin/IOAVB1722ApplicationControlService.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBControlPlugin/IOAVB1722ApplicationControlServiceUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBControlPlugin/IOAVB1722ControlService.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBControlPlugin/IOAVB1722MAAPService.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBControlPlugin/IOAVB1722MAAPServiceUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBControlPlugin/IOAVBMACAddressRange.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBControlPlugin/IOAVB1722ApplicationControlService.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBControlPlugin/IOAVB1722ApplicationControlServiceUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBControlPlugin/IOAVB1722ControlService.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBControlPlugin/IOAVB1722MAAPService.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBControlPlugin/IOAVB1722MAAPServiceUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOAVBFamily_kexts/IOAVBControlPlugin/IOAVBMACAddressRange.cpp"

```
