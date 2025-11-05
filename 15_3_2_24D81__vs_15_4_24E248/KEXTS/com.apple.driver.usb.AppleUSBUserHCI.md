## com.apple.driver.usb.AppleUSBUserHCI

> `com.apple.driver.usb.AppleUSBUserHCI`

```diff

-1402.60.3.0.0
-  __TEXT.__const: 0x94
+1402.100.21.0.0
+  __TEXT.__const: 0x84
   __TEXT.__cstring: 0x247a
   __TEXT.__os_log: 0x1491
-  __TEXT_EXEC.__text: 0x1a2c0
+  __TEXT_EXEC.__text: 0x1a4e8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1f0

   __DATA_CONST.__mod_term_func: 0x50
   __DATA_CONST.__const: 0x5368
   __DATA_CONST.__kalloc_type: 0x380
-  UUID: 9ADA613E-97BC-3602-AA49-B4190A5E4286
-  Functions: 450
+  UUID: 4D19D93E-BD8D-3080-AA84-3BCEFC22AC58
+  Functions: 449
   Symbols:   1518
   CStrings:  373
 
Functions:
~ __ZN15AppleUSBUserHCI5startEP9IOService : 5008 -> 4960
~ __ZN15AppleUSBUserHCI4freeEv : 408 -> 412
~ __ZN15AppleUSBUserHCI7messageEjP9IOServicePv : 148 -> 144
~ __ZN15AppleUSBUserHCI11createPortsEv : 1644 -> 1640
~ __ZN15AppleUSBUserHCI20lowerOnePowerStateToEm : 780 -> 772
~ __ZN15AppleUSBUserHCI20raiseOnePowerStateToEm : 788 -> 784
~ ____ZN15AppleUSBUserHCI12createDeviceE31tInternalUSBHostConnectionSpeedjj_block_invoke : 2100 -> 2120
~ ____ZN15AppleUSBUserHCI13destroyDeviceEP15IOUSBHostDevice_block_invoke : 232 -> 236
~ ____ZN15AppleUSBUserHCI19getAddressForDeviceEP15IOUSBHostDevice_block_invoke : 172 -> 176
~ __ZN15AppleUSBUserHCI17processInterruptsEb : 2592 -> 2564
~ __ZN15AppleUSBUserHCI16registerHubGatedEP15IOUSBHostDevicePKN11StandardUSB13HubDescriptorE17tRegisterHubFlags : 176 -> 180
~ __ZN15AppleUSBUserHCI26registerSuperSpeedHubGatedEP15IOUSBHostDevicePKN11StandardUSB23SuperSpeedHubDescriptorE : 176 -> 180
~ __ZN15AppleUSBUserHCI15createPipeGatedERN13IOUSBHostPipe22StandardUSBDescriptorsEP15IOUSBHostDeviceP18IOUSBHostInterfaceRPS0_ : 1284 -> 1292
~ __ZN15AppleUSBUserHCI17suspendPipesGatedEP15IOUSBHostDevice : 168 -> 172
~ __ZN15AppleUSBUserHCI16resumePipesGatedEP15IOUSBHostDevice : 168 -> 172
~ __ZN15AppleUSBUserHCI14closePipeGatedEP13IOUSBHostPipe : 968 -> 972
~ __ZN15AppleUSBUserHCI14getFrameNumberEPy : 164 -> 176
~ __ZN15AppleUSBUserHCI16getFrameRolloverEPy : 60 -> 80
~ __ZN15AppleUSBUserHCI26powerStateDidChangeToGatedEmmP9IOService : 764 -> 760
~ __ZN15AppleUSBUserHCI27systemPowerChangeThreadCallEPNS_38AppleUSBUserHCISystemPowerChangeParamsE : 1896 -> 1880
~ __ZN33AppleUSBUserHCITransferStructPool17getTransferStructEv : 1044 -> 1040
~ __ZN33AppleUSBUserHCITransferStructPool20returnTransferStructEP29AppleUSBUserHCITransferStruct : 48 -> 44
~ __ZN33AppleUSBUserHCITransferStructPool4freeEv : 172 -> 176
~ __ZN22AppleUSBUserHCIRequest4freeEv : 120 -> 124
~ __ZN22AppleUSBUserHCIRequest7prepareEP19AppleUSBHostRequest : 5564 -> 5496
~ __ZN22AppleUSBUserHCIRequest4linkEPS_ : 696 -> 736
~ __ZN22AppleUSBUserHCIRequest6updateEPK18IOUSBHostCIMessage : 2692 -> 2824
- sub_fffffe000b539f20
~ __ZN22AppleUSBUserHCIRequest8completeEv : 384 -> 392
~ __ZN22AppleUSBUserHCIRequest22getFirstTransferStructEv : 20 -> 24
~ __ZN26AppleUSBUserHCIRequestPool18initWithControllerEP15AppleUSBUserHCI : 216 -> 208
~ __ZN26AppleUSBUserHCIRequestPool4freeEv : 120 -> 124
~ __ZN25AppleUSBUserHCIUserClient23externalMethodInterruptEPS_PvP25IOExternalMethodArguments : 1016 -> 1012
~ __ZN25AppleUSBUserHCIUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv : 68 -> 88
~ __ZN25AppleUSBUserHCIUserClient12initWithTaskEP4taskPvj : 336 -> 340
~ __ZN25AppleUSBUserHCIUserClient11clientCloseEv : 476 -> 472
~ __ZN25AppleUSBUserHCIUserClient10clientDiedEv : 464 -> 460
~ __ZN25AppleUSBUserHCIUserClient5startEP9IOService : 1300 -> 1316
~ __ZN25AppleUSBUserHCIUserClient4freeEv : 264 -> 268
~ __ZN25AppleUSBUserHCIUserClient12commandWriteERK18IOUSBHostCIMessage : 636 -> 640
~ ____ZN25AppleUSBUserHCIUserClient12commandWriteERK18IOUSBHostCIMessage_block_invoke : 604 -> 600
~ __ZN25AppleUSBUserHCIUserClient11commandReadEPK25IOExternalMethodArguments : 160 -> 168
~ ____ZN25AppleUSBUserHCIUserClient11commandReadEPK25IOExternalMethodArguments_block_invoke : 1032 -> 1028
~ __ZN25AppleUSBUserHCIUserClient13doorbellWriteERKj : 188 -> 244
~ __ZN25AppleUSBUserHCIUserClient12doorbellReadEPK25IOExternalMethodArguments : 160 -> 168
~ ____ZN25AppleUSBUserHCIUserClient12doorbellReadEPK25IOExternalMethodArguments_block_invoke : 1212 -> 1356
~ ____ZN25AppleUSBUserHCIUserClient14interruptWriteEPK25IOExternalMethodArguments_block_invoke : 2116 -> 2148
~ __ZN25AppleUSBUserHCIUserClient13interruptReadER18IOUSBHostCIMessage : 544 -> 560
~ __ZN25AppleUSBUserHCIUserClient17hardwareExceptionE24IOUSBHostCIExceptionType : 624 -> 632
~ ____ZN25AppleUSBUserHCIUserClient16cancelAsyncCallsEv_block_invoke : 532 -> 564
~ __ZN24AppleUSBUserHCIResources13newUserClientEP4taskPvjP12OSDictionaryPP12IOUserClient : 396 -> 416
~ __ZN19AppleUSBUserHCIPipe4freeEv : 168 -> 172
~ __ZN28AppleUSBUserHCITransferQueue18initWithParametersEtRN13IOUSBHostPipe22StandardUSBDescriptorsEP15AppleUSBUserHCIP27AppleUSBUserHCICommandQueue : 872 -> 892
~ __ZN28AppleUSBUserHCITransferQueue4freeEv : 416 -> 420
~ __ZN28AppleUSBUserHCITransferQueue14updateEndpointERN13IOUSBHostPipe22StandardUSBDescriptorsE : 1216 -> 1224
~ __ZN28AppleUSBUserHCITransferQueue14enqueueRequestEP22AppleUSBUserHCIRequest : 780 -> 784
~ __ZNK28AppleUSBUserHCITransferQueue11hasRequestsEP9IOService : 180 -> 204
~ __ZN28AppleUSBUserHCITransferQueue16abortAllRequestsEiP9IOService : 872 -> 876
~ __ZN28AppleUSBUserHCITransferQueue4stopEb : 656 -> 652
~ __ZN28AppleUSBUserHCITransferQueue6unhaltEb : 96 -> 104
~ __ZN28AppleUSBUserHCITransferQueue7suspendEv : 436 -> 432
~ __ZN28AppleUSBUserHCITransferQueue6resumeEv : 400 -> 396
~ __ZN39AppleUSBUserHCIIsochronousTransferQueue14enqueueRequestEP22AppleUSBUserHCIRequest : 1840 -> 1832
~ __ZN19AppleUSBUserHCIPort18initWithParametersERK18IOUSBHostCIMessageP27AppleUSBUserHCICommandQueue : 320 -> 344
~ __ZN19AppleUSBUserHCIPort5startEP9IOService : 596 -> 592
~ __ZN19AppleUSBUserHCIPort4freeEv : 120 -> 124
~ __ZN19AppleUSBUserHCIPort20resetAndCreateDeviceEj : 1416 -> 1404
~ __ZN19AppleUSBUserHCIPort17interruptOccurredEP22IOInterruptEventSourcei : 3444 -> 3440
~ __ZN27AppleUSBUserHCICommandQueue18initWithControllerEP15AppleUSBUserHCI : 272 -> 276
~ __ZN27AppleUSBUserHCICommandQueue4freeEv : 168 -> 172
~ __ZN27AppleUSBUserHCICommandQueue14executeCommandER18IOUSBHostCIMessagey : 2256 -> 2240
~ __ZN27AppleUSBUserHCICommandQueue21notifyCommandCompleteEPK18IOUSBHostCIMessage : 484 -> 480
~ __ZN27AppleUSBUserHCICommandQueue12deviceCreateEjRt : 504 -> 500
~ __ZN21AppleUSBUserHCIDevice18initWithParametersEP15AppleUSBUserHCIP27AppleUSBUserHCICommandQueuej : 484 -> 504
~ __ZN21AppleUSBUserHCIDevice4freeEv : 476 -> 480
~ __ZN21AppleUSBUserHCIDevice12updateDeviceEPKN11StandardUSB10DescriptorE : 1312 -> 1352
~ __ZN21AppleUSBUserHCIDevice7suspendEv : 124 -> 128
~ __ZN21AppleUSBUserHCIDevice6resumeEv : 124 -> 128
~ __ZN21AppleUSBUserHCIDevice7destroyEv : 508 -> 512
~ __ZN21AppleUSBUserHCIDevice11destroyPipeEP19AppleUSBUserHCIPipe : 368 -> 372

```
