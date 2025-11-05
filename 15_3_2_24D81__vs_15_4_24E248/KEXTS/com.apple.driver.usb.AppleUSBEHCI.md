## com.apple.driver.usb.AppleUSBEHCI

> `com.apple.driver.usb.AppleUSBEHCI`

```diff

-1402.60.3.0.0
+1402.100.21.0.0
   __TEXT.__cstring: 0x43c3
   __TEXT.__os_log: 0x3cd6
-  __TEXT_EXEC.__text: 0x333a4
+  __TEXT_EXEC.__text: 0x335cc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x3a8

   __DATA_CONST.__mod_term_func: 0x68
   __DATA_CONST.__const: 0x5968
   __DATA_CONST.__kalloc_type: 0xa80
-  UUID: C43C708C-88D0-3DB6-8EB5-814CD1F36CC3
+  UUID: A11972CC-A7A4-32B4-9BAF-BA92348FD31D
   Functions: 627
   Symbols:   1938
   CStrings:  634
Functions:
~ __ZN35AppleUSBEHCISplitIsochronousRequest7prepareEP19AppleUSBHostRequestP31AppleUSBEHCIIsochronousEndpoint : 3516 -> 3568
~ __ZN35AppleUSBEHCISplitIsochronousRequest6cancelEv : 176 -> 192
~ __ZN35AppleUSBEHCISplitIsochronousRequest6updateEi : 1200 -> 1352
~ __ZN35AppleUSBEHCISplitIsochronousRequest6finishEi : 2016 -> 2004
~ __ZN25AppleUSBEHCIQueueHeadPool5getQHEhhhhththht : 1008 -> 1016
~ __ZN25AppleUSBEHCIQueueHeadPool8returnQHEP21AppleUSBEHCIQueueHead : 40 -> 36
~ __ZN25AppleUSBEHCIQueueHeadPool4freeEv : 488 -> 484
~ __ZN21AppleUSBEHCIQueueHead4freeEv : 648 -> 652
~ __ZN21AppleUSBEHCIQueueHead5closeEv : 76 -> 84
~ __ZN21AppleUSBEHCIQueueHead14enqueueRequestEP19AppleUSBEHCIRequest : 628 -> 632
~ __ZN21AppleUSBEHCIQueueHead7timeoutEP18IOTimerEventSource : 1524 -> 1512
~ __ZN21AppleUSBEHCIQueueHead12abortRequestEi : 428 -> 416
~ __ZN21AppleUSBEHCIQueueHead16abortAllRequestsEiP9IOService : 760 -> 756
~ __ZN21AppleUSBEHCIQueueHead6unhaltEb : 552 -> 536
~ __ZN21AppleUSBEHCIQueueHead5startEv : 196 -> 192
~ __ZN21AppleUSBEHCIQueueHead6resumeEv : 88 -> 96
~ __ZN21AppleUSBEHCIQueueHead5printEv : 984 -> 972
~ __ZN31AppleUSBEHCIIsochronousEndpoint4initEv : 156 -> 168
~ __ZN31AppleUSBEHCIIsochronousEndpoint4freeEv : 672 -> 676
~ __ZN31AppleUSBEHCIIsochronousEndpoint5printEv : 1988 -> 1956
~ __ZN31AppleUSBEHCIIsochronousEndpoint14enqueueRequestEP30AppleUSBEHCIIsochronousRequest : 640 -> 644
~ __ZN22AppleUSBEHCIDMACommand19setMemoryDescriptorEPK18IOMemoryDescriptorbjyP19AppleUSBHostRequest : 1052 -> 1072
~ __ZN26AppleUSBEHCIDARTDMACommand19setMemoryDescriptorEPK18IOMemoryDescriptorbjyP19AppleUSBHostRequest : 1720 -> 1688
~ __ZN34AppleUSBEHCIIsochronousRequestPool4freeEv : 120 -> 124
~ __ZN30AppleUSBEHCIIsochronousRequest25initWithControllerAndPoolEP12AppleUSBEHCIP19AppleUSBRequestPool : 300 -> 312
~ __ZN30AppleUSBEHCIIsochronousRequest4freeEv : 168 -> 172
~ __ZN30AppleUSBEHCIIsochronousRequest6cancelEv : 180 -> 196
~ __ZN30AppleUSBEHCIIsochronousRequest6updateEi : 1384 -> 1552
~ __ZN30AppleUSBEHCIIsochronousRequest6finishEi : 2996 -> 2992
~ __ZN30AppleUSBEHCIIsochronousRequest4linkEv : 200 -> 208
~ __ZN20AppleUSBEHCIsiTDPool28initWithControllerAndOptionsEP22AppleUSBHostControllerjP8IOMapper : 212 -> 224
~ __ZN20AppleUSBEHCIsiTDPool4freeEv : 436 -> 480
~ __ZN20AppleUSBEHCIsiTDPool5getTDEv : 508 -> 528
~ __ZN16AppleUSBEHCIsiTD20initWithSharedMemoryEP19StandardUSBEHCIsiTDy : 96 -> 100
~ __ZN16AppleUSBEHCIPipe4freeEv : 168 -> 172
~ __ZN19AppleUSBEHCIqTDPool15initWithOptionsEjP8IOMapper : 196 -> 200
~ __ZN19AppleUSBEHCIqTDPool5getTDEv : 524 -> 544
~ __ZN19AppleUSBEHCIqTDPool4freeEv : 260 -> 264
~ __ZN12AppleUSBEHCI5startEP9IOService : 8480 -> 8412
~ __ZN12AppleUSBEHCI22InterruptThresholdInitEP9IOService : 1416 -> 1404
~ __ZN12AppleUSBEHCI19InterruptInitializeEv : 772 -> 776
~ __ZN12AppleUSBEHCI19stopThreadCallGatedEv : 664 -> 676
~ __ZN12AppleUSBEHCI4freeEv : 444 -> 448
~ __ZN12AppleUSBEHCI11createPortsEv : 1668 -> 1672
~ __ZN12AppleUSBEHCI10StopUSBBusEv : 1296 -> 1292
~ __ZN12AppleUSBEHCI13RestartUSBBusEv : 1456 -> 1452
~ __ZN12AppleUSBEHCI19EnableAsyncScheduleEb : 1028 -> 1024
~ __ZN12AppleUSBEHCI20DisableAsyncScheduleEv : 320 -> 312
~ __ZN12AppleUSBEHCI22EnablePeriodicScheduleEb : 296 -> 288
~ __ZN12AppleUSBEHCI23DisablePeriodicScheduleEb : 296 -> 288
~ __ZN12AppleUSBEHCI22RingAndWaitForDoorbellEv : 1968 -> 1956
~ __ZN12AppleUSBEHCI13linkQueueHeadEP21AppleUSBEHCIQueueHead : 992 -> 980
~ __ZN12AppleUSBEHCI15unlinkQueueHeadEP21AppleUSBEHCIQueueHeadb : 884 -> 868
~ __ZN12AppleUSBEHCI23insertPeriodicListEntryEiP33AppleUSBHostControllerListElement : 1740 -> 1680
~ __ZN12AppleUSBEHCI23removePeriodicListEntryEiP33AppleUSBHostControllerListElement : 1632 -> 1636
~ __ZN12AppleUSBEHCI21FindInterruptEndpointEsss : 264 -> 288
~ __ZN12AppleUSBEHCI26AllocateInterruptBandwidthEP21AppleUSBEHCIQueueHeadP18AppleUSBEHCITTInfo : 6008 -> 5988
~ __ZN12AppleUSBEHCI25ShowPeriodicBandwidthUsedEPKc : 928 -> 920
~ __ZN12AppleUSBEHCI24ReservePeriodicBandwidthEiit : 2500 -> 2492
~ __ZN12AppleUSBEHCI24ReleasePeriodicBandwidthEiit : 2496 -> 2484
~ __ZN12AppleUSBEHCI32AllocateHSPeriodicSplitBandwidthEP33AppleUSBEHCISplitPeriodicEndpoint : 4548 -> 4504
~ __ZN12AppleUSBEHCI10AdjustSPEsEP33AppleUSBEHCISplitPeriodicEndpointb : 2348 -> 2328
~ __ZN12AppleUSBEHCI24ReturnInterruptBandwidthEP21AppleUSBEHCIQueueHead : 2728 -> 2720
~ __ZN12AppleUSBEHCI30ReturnHSPeriodicSplitBandwidthEP33AppleUSBEHCISplitPeriodicEndpoint : 1536 -> 1528
~ __ZN12AppleUSBEHCI22AllocateIsochBandwidthEP31AppleUSBEHCIIsochronousEndpointP18AppleUSBEHCITTInfo : 5824 -> 5788
~ __ZN12AppleUSBEHCI20ReturnIsochBandwidthEP31AppleUSBEHCIIsochronousEndpoint : 3152 -> 3132
~ __ZN12AppleUSBEHCI17interruptOccurredEP22IOInterruptEventSourcei : 1512 -> 1520
~ __ZN12AppleUSBEHCI29scavengeCompletedTransactionsEv : 448 -> 480
~ __ZN12AppleUSBEHCI16registerHubGatedEP15IOUSBHostDevicePKN11StandardUSB13HubDescriptorE17tRegisterHubFlags : 212 -> 228
~ __ZN12AppleUSBEHCI18unregisterHubGatedEP15IOUSBHostDevice : 180 -> 196
~ __ZN12AppleUSBEHCI28setupSplitTransactionRoutingEtjtj : 116 -> 168
~ __ZN12AppleUSBEHCI20raiseOnePowerStateToEm : 976 -> 984
~ __ZN12AppleUSBEHCI19clearPipeStallGatedEP13IOUSBHostPipe : 712 -> 692
~ __ZN12AppleUSBEHCI15adjustPipeGatedEP13IOUSBHostPipeRNS0_22StandardUSBDescriptorsE : 3212 -> 3256
~ __ZN12AppleUSBEHCI14closePipeGatedEP13IOUSBHostPipe : 1044 -> 1068
~ __ZN12AppleUSBEHCI15createPipeGatedERN13IOUSBHostPipe22StandardUSBDescriptorsEP15IOUSBHostDeviceP18IOUSBHostInterfaceRPS0_ : 2828 -> 3008
~ __ZN12AppleUSBEHCI25createSetAddressPipeGatedEPKN11StandardUSB18EndpointDescriptorEhRP13IOUSBHostPipe : 548 -> 528
~ __ZN12AppleUSBEHCI21hasEndpointForAddressEt : 356 -> 388
~ __ZN12AppleUSBEHCI7ioGatedEP19AppleUSBHostRequest : 3452 -> 3432
~ __ZN12AppleUSBEHCI17suspendPipesGatedEP15IOUSBHostDevice : 1436 -> 1452
~ __ZN12AppleUSBEHCI14createIOBufferEjy : 332 -> 336
~ __ZN12AppleUSBEHCI13getDMACommandEjj : 240 -> 232
~ __ZN12AppleUSBEHCI8testModeEj13tEHCITestMode : 668 -> 676
~ __ZN19AppleUSBEHCIHubInfo10AddHubInfoEPPS_tj : 420 -> 412
~ __ZN19AppleUSBEHCIHubInfo11FindHubInfoEPS_t : 332 -> 320
~ __ZN19AppleUSBEHCIHubInfo13DeleteHubInfoEPPS_t : 1352 -> 1324
~ __ZN19AppleUSBEHCIHubInfo9GetTTInfoEi : 368 -> 364
~ __ZN18AppleUSBEHCITTInfo9NewTTInfoEi : 1044 -> 1040
~ __ZN33AppleUSBEHCISplitPeriodicEndpoint24NewSplitPeriodicEndpointEP18AppleUSBEHCITTInfotP8OSObjectth : 888 -> 908
~ __ZN18AppleUSBEHCITTInfo21ReserveHSSplitINBytesEiit : 1356 -> 1332
~ __ZN18AppleUSBEHCITTInfo21ReleaseHSSplitINBytesEiit : 1648 -> 1624
~ __ZN18AppleUSBEHCITTInfo17ReserveFSBusBytesEit : 1352 -> 1332
~ __ZN18AppleUSBEHCITTInfo17ReleaseFSBusBytesEit : 1368 -> 1348
~ __ZN18AppleUSBEHCITTInfo25AllocatePeriodicBandwidthEP33AppleUSBEHCISplitPeriodicEndpoint : 1760 -> 1888
~ __ZN33AppleUSBEHCISplitPeriodicEndpoint26FindStartFrameAndStartTimeEv : 2492 -> 2364
~ __ZN33AppleUSBEHCISplitPeriodicEndpoint20CheckPlacementBeforeEPS_ : 408 -> 404
~ __ZN18AppleUSBEHCITTInfo32CalculateSPEsToAdjustAfterChangeEP33AppleUSBEHCISplitPeriodicEndpointb : 6428 -> 6472
~ __ZNK18AppleUSBEHCITTInfo7releaseEv : 1016 -> 1052
~ __ZN18AppleUSBEHCITTInfo19ShowHSSplitTimeUsedEPKc : 616 -> 612
~ __ZN18AppleUSBEHCITTInfo5printEPKc : 1668 -> 1760
~ __ZN33AppleUSBEHCISplitPeriodicEndpoint5printEv : 712 -> 696
~ __ZN33AppleUSBEHCISplitPeriodicEndpoint27CalculateAllFrameStartTimesEPt : 416 -> 428
~ __ZN33AppleUSBEHCISplitPeriodicEndpoint18CalculateStartTimeEtPS_S0_ : 1032 -> 1080
~ __ZN33AppleUSBEHCISplitPeriodicEndpoint31CalculateNewStartTimeFromChangeEPS_ : 908 -> 948
~ __ZN19AppleUSBEHCIiTDPool28initWithControllerAndOptionsEP22AppleUSBHostControllerjP8IOMapper : 212 -> 216
~ __ZN19AppleUSBEHCIiTDPool4freeEv : 436 -> 480
~ __ZN19AppleUSBEHCIiTDPool5getTDEv : 572 -> 596
~ __ZN15AppleUSBEHCIiTD20initWithSharedMemoryEP18StandardUSBEHCIiTDy : 96 -> 100
~ __ZN16AppleUSBEHCIPort24initWithPortSCandDTEntryEP14IODeviceMemoryP15IORegistryEntry : 1020 -> 1012
~ __ZN16AppleUSBEHCIPort23initWithPortSCandNumberEP14IODeviceMemoryj : 240 -> 260
~ __ZN16AppleUSBEHCIPort5startEP9IOService : 1336 -> 1332
~ __ZN16AppleUSBEHCIPort4freeEv : 124 -> 128
~ __ZN16AppleUSBEHCIPort22powerStateWillChangeToEmmP9IOService : 196 -> 192
~ __ZN16AppleUSBEHCIPort13enterTestModeE13tEHCITestMode : 1148 -> 1136
~ __ZN16AppleUSBEHCIPort8testModeE13tEHCITestMode : 644 -> 640
~ __ZN16AppleUSBEHCIPort8powerOffEv : 792 -> 788
~ __ZN16AppleUSBEHCIPort7powerOnEv : 2220 -> 2204
~ __ZN16AppleUSBEHCIPort7suspendEv : 596 -> 592
~ __ZN16AppleUSBEHCIPort6resumeEv : 912 -> 908
~ __ZN16AppleUSBEHCIPort9resetPortEj : 1048 -> 1040
~ __ZN16AppleUSBEHCIPort20resetAndCreateDeviceEj : 3796 -> 3772
~ __ZN16AppleUSBEHCIPort17interruptOccurredEP22IOInterruptEventSourcei : 5652 -> 5628
~ __ZN16AppleUSBEHCIPort21enableChangeInterruptEv : 692 -> 688
~ __ZN23AppleUSBEHCIRequestPool4freeEv : 120 -> 124
~ __ZN19AppleUSBEHCIRequest4freeEv : 216 -> 220
~ __ZN19AppleUSBEHCIRequest7prepareEP19AppleUSBHostRequestP21AppleUSBEHCIQueueHead : 5520 -> 5500
~ __ZN19AppleUSBEHCIRequest6cancelEv : 280 -> 288
~ __ZN19AppleUSBEHCIRequest6finishEi : 2976 -> 2960
~ __ZN19AppleUSBEHCIRequest5printEv : 1252 -> 1228

```
