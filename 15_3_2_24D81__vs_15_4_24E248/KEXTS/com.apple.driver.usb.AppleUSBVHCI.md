## com.apple.driver.usb.AppleUSBVHCI

> `com.apple.driver.usb.AppleUSBVHCI`

```diff

-1402.60.3.0.0
+1402.100.21.0.0
   __TEXT.__cstring: 0x26d1
   __TEXT.__os_log: 0x1b0e
   __TEXT.__const: 0x50
-  __TEXT_EXEC.__text: 0x1bc38
+  __TEXT_EXEC.__text: 0x1bca4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x240
-  __DATA_CONST.__auth_got: 0x250
-  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0xd8
   __DATA_CONST.__mod_init_func: 0x48
   __DATA_CONST.__mod_term_func: 0x48
   __DATA_CONST.__const: 0x4da0
   __DATA_CONST.__kalloc_type: 0x380
-  UUID: 4003845A-DBEA-3549-A7DF-6107FDEE1C71
+  UUID: 46BADBE8-1E55-32FA-A8E9-1B7AC501285A
   Functions: 436
-  Symbols:   1486
+  Symbols:   1488
   CStrings:  348
 
Symbols:
+ ___stack_chk_fail
+ ___stack_chk_guard
Functions:
~ __ZN20AppleUSBVHCIEndpoint18initWithParametersEP12AppleUSBVHCIP18AppleUSBVHCIDeviceP28AppleUSBVHCIHostCommandQueueRN13IOUSBHostPipe22StandardUSBDescriptorsE : 1440 -> 1448
~ __ZN20AppleUSBVHCIEndpoint4freeEv : 312 -> 316
~ __ZN20AppleUSBVHCIEndpoint5startENS_19tStateRequestSourceE : 780 -> 784
~ __ZN20AppleUSBVHCIEndpoint5pauseENS_19tStateRequestSourceE : 928 -> 932
~ __ZN20AppleUSBVHCIEndpoint6unhaltEv : 444 -> 440
~ __ZN20AppleUSBVHCIEndpoint7destroyEb : 1196 -> 1184
~ __ZN20AppleUSBVHCIEndpoint23executeDeferredCommandsEv : 412 -> 408
~ __ZN20AppleUSBVHCIEndpoint20firmwarePauseTimeoutEP18IOTimerEventSource : 1364 -> 1360
~ __ZN19AppleUSBVHCIRequest6cancelEv : 152 -> 156
~ __ZN19AppleUSBVHCIRequest6finishEi : 852 -> 840
~ __ZN19AppleUSBVHCIRequest8completeEv : 152 -> 156
~ __ZN19AppleUSBVHCIRequest8activateEv : 1136 -> 1128
~ __ZN19AppleUSBVHCIRequest5pauseEv : 292 -> 288
~ __ZN19AppleUSBVHCIRequest10update0070EPN15StandardUSBVHCI11VHCIMessageE : 2588 -> 2568
~ __ZN26AppleUSBVHCIControlRequest6cancelEv : 116 -> 120
~ __ZN26AppleUSBVHCIControlRequest6updateEPN15StandardUSBVHCI11VHCIMessageE : 5156 -> 5112
~ __ZN26AppleUSBVHCIControlRequest8completeEv : 116 -> 120
~ __ZN18AppleUSBVHCIDevice4freeEv : 216 -> 220
~ __ZN18AppleUSBVHCIDevice7destroyEb : 896 -> 888
~ __ZN18AppleUSBVHCIDevice12processEventEPKN15StandardUSBVHCI11VHCIMessageE : 544 -> 540
~ __ZN18AppleUSBVHCIDevice10createPipeERN13IOUSBHostPipe22StandardUSBDescriptorsEP15IOUSBHostDeviceP18IOUSBHostInterface : 1204 -> 1208
~ __ZN18AppleUSBVHCIDevice11destroyPipeEP16AppleUSBVHCIPipe : 480 -> 484
~ __ZN18AppleUSBVHCIDevice7suspendEv : 108 -> 112
~ __ZN18AppleUSBVHCIDevice6resumeEv : 108 -> 112
~ __ZN18AppleUSBVHCIDevice23executeDeferredCommandsEv : 336 -> 344
~ __ZN29AppleUSBVHCIHostTransferQueue18initWithParametersEjPKN15StandardUSBVHCI11VHCIMessageEP23AppleUSBVHCIBufferQueueP24AppleUSBVHCIMessageQueueP28AppleUSBVHCIHostCommandQueueP12AppleUSBVHCI : 596 -> 612
~ __ZN29AppleUSBVHCIHostTransferQueue4freeEv : 332 -> 336
~ __ZN29AppleUSBVHCIHostTransferQueue16processEvent0070EPKN15StandardUSBVHCI11VHCIMessageE : 2384 -> 2376
~ __ZN29AppleUSBVHCIHostTransferQueue18pollForCompletionsEj : 1388 -> 1372
~ __ZN29AppleUSBVHCIHostTransferQueue13setQueueStateEN15StandardUSBVHCI18tVHCIEndpointStateE : 424 -> 420
~ __ZN29AppleUSBVHCIHostTransferQueue18processCommand0070EPKN15StandardUSBVHCI11VHCIMessageE : 1680 -> 1648
~ __ZN29AppleUSBVHCIHostTransferQueue6unhaltEv : 200 -> 208
~ __ZN25AppleUSBVHCIBringupDriver5startEP9IOService : 1324 -> 1316
~ __ZN25AppleUSBVHCIBringupDriver4testEP18IOTimerEventSource : 7024 -> 7188
~ __ZN25AppleUSBVHCIBringupDriver10testBulkInEjjt : 880 -> 884
~ __ZN25AppleUSBVHCIBringupDriver14bulkCompletionEPvij : 168 -> 164
~ __ZN16AppleUSBVHCIPort18initWithParametersEjP28AppleUSBVHCIHostCommandQueuehh : 308 -> 348
~ __ZN16AppleUSBVHCIPort5startEP9IOService : 604 -> 600
~ __ZN16AppleUSBVHCIPort4freeEv : 168 -> 172
~ __ZN16AppleUSBVHCIPort20resetAndCreateDeviceEj : 2312 -> 2300
~ __ZN16AppleUSBVHCIPort17interruptOccurredEP22IOInterruptEventSourcei : 3564 -> 3560
~ __ZN28AppleUSBVHCIHostCommandQueue4freeEv : 168 -> 172
~ __ZN16AppleUSBVHCIPipe4freeEv : 120 -> 124
~ __ZN12AppleUSBVHCI5startEP9IOService : 3880 -> 3844
~ __ZN12AppleUSBVHCI4freeEv : 388 -> 392
~ __ZN12AppleUSBVHCI22powerStateWillChangeToEmmP9IOService : 716 -> 712
~ __ZN12AppleUSBVHCI11createPortsEv : 1880 -> 1856
~ __ZN12AppleUSBVHCI20lowerOnePowerStateToEm : 1728 -> 1724
~ __ZN12AppleUSBVHCI20raiseOnePowerStateToEm : 4824 -> 4788
~ ____ZN12AppleUSBVHCI12createDeviceE31tInternalUSBHostConnectionSpeedjj_block_invoke : 1916 -> 2020
~ ____ZN12AppleUSBVHCI13destroyDeviceEP15IOUSBHostDevice_block_invoke : 1488 -> 1472
~ __ZN12AppleUSBVHCI17processInterruptsENS_14tInterruptMaskEb : 10280 -> 10288
~ __ZN12AppleUSBVHCI15createPipeGatedERN13IOUSBHostPipe22StandardUSBDescriptorsEP15IOUSBHostDeviceP18IOUSBHostInterfaceRPS0_ : 296 -> 304
~ __ZN12AppleUSBVHCI7ioGatedEP19AppleUSBHostRequest : 3176 -> 3180
~ __ZN12AppleUSBVHCI19clearPipeStallGatedEP13IOUSBHostPipe : 1932 -> 1924
~ __ZN12AppleUSBVHCI17suspendPipesGatedEP15IOUSBHostDevice : 168 -> 172
~ __ZN12AppleUSBVHCI16resumePipesGatedEP15IOUSBHostDevice : 168 -> 172
~ __ZN12AppleUSBVHCI14closePipeGatedEP13IOUSBHostPipe : 352 -> 356

```
