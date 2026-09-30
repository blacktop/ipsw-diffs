## com.apple.driver.usb.AppleUSBRecoveryHost

> `com.apple.driver.usb.AppleUSBRecoveryHost`

```diff

-1402.60.3.0.0
+1402.100.21.0.0
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0xdac
   __TEXT.__os_log: 0x7da
-  __TEXT_EXEC.__text: 0xb470
+  __TEXT_EXEC.__text: 0xb43c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1a0

   __DATA_CONST.__mod_term_func: 0x30
   __DATA_CONST.__const: 0x41d0
   __DATA_CONST.__kalloc_type: 0x3c0
-  UUID: B2AD3BE8-29B4-3ED8-B42D-CBD7E42560F8
+  UUID: CF216AFE-EBC5-32B4-BD12-8ED43720E0AA
   Functions: 285
   Symbols:   1164
   CStrings:  136
Functions:
~ __ZN20AppleUSBRecoveryHost4freeEv : 216 -> 220
~ ____ZN20AppleUSBRecoveryHost13destroyDeviceEP15IOUSBHostDevice_block_invoke : 236 -> 244
~ __ZN20AppleUSBRecoveryHost15createPipeGatedERN13IOUSBHostPipe22StandardUSBDescriptorsEP15IOUSBHostDeviceP18IOUSBHostInterfaceRPS0_ : 1596 -> 1584
~ __ZN20AppleUSBRecoveryHost7ioGatedEP19AppleUSBHostRequest : 564 -> 568
~ __ZN20AppleUSBRecoveryHost17suspendPipesGatedEP15IOUSBHostDevice : 104 -> 108
~ __ZN20AppleUSBRecoveryHost16resumePipesGatedEP15IOUSBHostDevice : 104 -> 108
~ __ZN20AppleUSBRecoveryHost14closePipeGatedEP13IOUSBHostPipe : 460 -> 452
~ __ZN20AppleUSBRecoveryHost19closeAllQueuesGatedEv : 968 -> 960
~ __ZN20AppleUSBRecoveryHost11createPortsEv : 1100 -> 1092
~ __ZN20AppleUSBRecoveryHost17interruptOccurredEP22IOInterruptEventSourcei : 100 -> 104
~ __ZN23AppleUSBRecoveryRSMHost5startEP9IOService : 1176 -> 1172
~ __ZN23AppleUSBRecoveryRSMHost4freeEv : 168 -> 172
~ __ZN23AppleUSBRecoveryRSMHost18rsmReceiveCallbackEP12IORSMChannelPKvyh : 2020 -> 2000
~ __ZN23AppleUSBRecoveryRSMHost15rsmSendCallbackEP27AppleUSBRecoveryBufferEntryi : 1436 -> 1424
~ __ZN23AppleUSBRecoveryRSMHost4sendEh : 988 -> 984
~ __ZN23AppleUSBRecoveryRequest6updateEP27AppleUSBRecoveryBufferEntry : 2296 -> 2288
~ __ZN23AppleUSBRecoveryRequest6finishEi : 412 -> 408
~ __ZN30AppleUSBRecoveryControlRequest8activateEv : 1008 -> 1000
~ __ZN20AppleUSBRecoveryPort12recoveryPortEv : 192 -> 212
~ __ZN20AppleUSBRecoveryPort4initEv : 232 -> 252
~ __ZN20AppleUSBRecoveryPort5startEP9IOService : 648 -> 664
~ __ZN20AppleUSBRecoveryPort4freeEv : 120 -> 124
~ __ZN21AppleUSBRecoveryQueue18initWithParametersEP20AppleUSBRecoveryHostht : 492 -> 496
~ __ZN21AppleUSBRecoveryQueue4freeEv : 296 -> 300
~ __ZN21AppleUSBRecoveryQueue4sendEP27AppleUSBRecoveryBufferEntry : 520 -> 516
~ __ZN21AppleUSBRecoveryQueue15queueCompletionEP27AppleUSBRecoveryBufferEntry : 120 -> 116
~ __ZN21AppleUSBRecoveryQueue18processBufferQueueEv : 912 -> 908
~ __ZN21AppleUSBRecoveryQueue5startEv : 224 -> 216
~ __ZN21AppleUSBRecoveryQueue4stopEv : 828 -> 824
~ __ZN21AppleUSBRecoveryQueue5closeEv : 676 -> 668
~ __ZN21AppleUSBRecoveryQueue16abortAllRequestsEiP9IOService : 684 -> 680
~ __ZN21AppleUSBRecoveryQueue11hasRequestsEv : 20 -> 24
~ __ZN21AppleUSBRecoveryQueue7timeoutEP18IOTimerEventSource : 724 -> 712
~ __ZN28AppleUSBRecoveryControlQueue18processBufferQueueEv : 1336 -> 1324
~ __ZN28AppleUSBRecoveryControlQueue4stopEv : 940 -> 936
~ __ZN20AppleUSBRecoveryPipe4freeEv : 120 -> 124

```
