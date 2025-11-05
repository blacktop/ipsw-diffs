## com.apple.driver.AppleUSBXDCIARM

> `com.apple.driver.AppleUSBXDCIARM`

```diff

-818.60.2.0.0
-  __TEXT.__const: 0x40
+818.100.6.0.0
+  __TEXT.__const: 0x38
   __TEXT.__cstring: 0x33f9
   __TEXT.__os_log: 0x53a1
-  __TEXT_EXEC.__text: 0x31460
+  __TEXT_EXEC.__text: 0x31124
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1c8

   __DATA_CONST.__mod_term_func: 0x50
   __DATA_CONST.__const: 0x8430
   __DATA_CONST.__kalloc_type: 0x280
-  UUID: 5C99159A-D136-30D2-8179-136707518EB0
+  UUID: DCE189B1-0142-30CC-BC95-2DDA4EACF69D
   Functions: 306
   Symbols:   1166
   CStrings:  269
Functions:
~ __ZN17AppleT8112USBXDCI5startEP9IOService : 4064 -> 4040
~ __ZN17AppleT8112USBXDCI4freeEv : 464 -> 440
~ __ZN17AppleT8112USBXDCI7powerOnEv : 8884 -> 8808
~ __ZN17AppleT8112USBXDCI15controllerResetEv : 2400 -> 2376
~ __ZN17AppleT8112USBXDCI8powerOffEv : 4068 -> 4040
~ __ZN17AppleT8112USBXDCI20enumDoneTimerExpiredEP18IOTimerEventSource : 884 -> 880
~ __ZN17AppleT8027USBXDCI5startEP9IOService : 1512 -> 1508
~ __ZN17AppleT8027USBXDCI7powerOnEv : 1640 -> 1624
~ __ZN17AppleT8130USBXDCI5startEP9IOService : 4064 -> 4040
~ __ZN17AppleT8130USBXDCI4freeEv : 464 -> 440
~ __ZN17AppleT8130USBXDCI7powerOnEv : 8884 -> 8808
~ __ZN17AppleT8130USBXDCI15controllerResetEv : 2400 -> 2376
~ __ZN17AppleT8130USBXDCI8powerOffEv : 4068 -> 4040
~ __ZN17AppleT8130USBXDCI20enumDoneTimerExpiredEP18IOTimerEventSource : 884 -> 880
~ __ZN17AppleT8122USBXDCI5startEP9IOService : 4064 -> 4040
~ __ZN17AppleT8122USBXDCI4freeEv : 464 -> 440
~ __ZN17AppleT8122USBXDCI7powerOnEv : 14880 -> 14776
~ __ZN17AppleT8122USBXDCI15controllerResetEv : 2400 -> 2376
~ __ZN17AppleT8122USBXDCI8powerOffEv : 7828 -> 7772
~ __ZN17AppleT8122USBXDCI20enumDoneTimerExpiredEP18IOTimerEventSource : 884 -> 880
~ __ZN17AppleT8132USBXDCI5startEP9IOService : 2096 -> 2088
~ __ZN17AppleT8132USBXDCI4freeEv : 240 -> 232
~ __ZN17AppleT8132USBXDCI7powerOnEv : 14880 -> 14776
~ __ZN17AppleT8132USBXDCI15controllerResetEv : 2400 -> 2376
~ __ZN17AppleT8132USBXDCI8powerOffEv : 7828 -> 7772
~ __ZN17AppleT8132USBXDCI20enumDoneTimerExpiredEP18IOTimerEventSource : 884 -> 880
~ __ZN15AppleUSBXDCIARM4stopEP9IOService : 976 -> 1056
~ __ZN15AppleUSBXDCIARM4freeEv : 168 -> 172
~ __ZN15AppleUSBXDCIARM22powerStateWillChangeToEmmP9IOService : 608 -> 604
~ ____ZN15AppleUSBXDCIARM22powerStateWillChangeToEmmP9IOService_block_invoke : 292 -> 300
~ __ZN15AppleUSBXDCIARM21powerStateDidChangeToEmmP9IOService : 636 -> 648
~ __ZN15AppleUSBXDCIARM20stopDeviceControllerEv : 248 -> 284
~ __ZN15AppleUSBXDCIARM14softDisconnectEN21IOUSBDeviceController41IOUSBDeviceControllerSoftDisconnectReasonE : 368 -> 376
~ __ZN15AppleUSBXDCIARM7powerOnEv : 2604 -> 2668
~ __ZN15AppleUSBXDCIARM8powerOffEv : 480 -> 476
~ __ZN15AppleUSBXDCIARM13startUSBStackEv : 496 -> 492
~ __ZN15AppleUSBXDCIARM27addDevCapabilityDescriptorsEv : 132 -> 180
~ __ZN15AppleUSBXDCIARM23handleUSBConnectionDoneEv : 860 -> 900
~ __ZN15AppleUSBXDCIARM18connectedToUSBHostEv : 60 -> 56
~ __ZN15AppleUSBXDCIARM27connectedWithAccessoryCableEv : 220 -> 212
~ __ZN15AppleUSBXDCIARM37initCableChangeNotificationThreadCallEP11thread_call : 240 -> 260
~ __ZN15AppleUSBXDCIARM30registerTransportNotificationsEv : 1148 -> 1160
~ __ZN15AppleUSBXDCIARM16transportCreatedEPvP9IOServiceP10IONotifier : 2216 -> 2240
~ __ZN15AppleUSBXDCIARM16transportMessageEPvjP9IOServiceS0_m : 588 -> 584
~ __ZN15AppleUSBXDCIARM15updatePortStateEj : 3768 -> 3832
~ __ZN15AppleUSBXDCIARM19cableChangeOccurredEP18IOTimerEventSource : 2032 -> 2024
~ __ZN15AppleUSBXDCIARM18setupDriverRequestEv : 1048 -> 1040
~ __ZN17AppleT8140USBXDCI5startEP9IOService : 2096 -> 2088
~ __ZN17AppleT8140USBXDCI4freeEv : 240 -> 232
~ __ZN17AppleT8140USBXDCI7powerOnEv : 8884 -> 8808
~ __ZN17AppleT8140USBXDCI15controllerResetEv : 2400 -> 2376
~ __ZN17AppleT8140USBXDCI8powerOffEv : 4068 -> 4040
~ __ZN17AppleT8140USBXDCI20enumDoneTimerExpiredEP18IOTimerEventSource : 884 -> 880
~ __ZN17AppleT8103USBXDCI5startEP9IOService : 4064 -> 4040
~ __ZN17AppleT8103USBXDCI4freeEv : 464 -> 440
~ __ZN17AppleT8103USBXDCI7powerOnEv : 8884 -> 8808
~ __ZN17AppleT8103USBXDCI15controllerResetEv : 2400 -> 2376
~ __ZN17AppleT8103USBXDCI8powerOffEv : 4068 -> 4040
~ __ZN17AppleT8103USBXDCI20enumDoneTimerExpiredEP18IOTimerEventSource : 884 -> 880
~ __ZN35AppleUSBXDCIModifiedControlTransfer11startEp0OutEv : 2960 -> 2936
~ __ZN35AppleUSBXDCIModifiedControlTransfer19ep0OutEventOccurredEN7USBXDCI22tAppleUSBXDCIEventTypeE : 2452 -> 2436
~ __ZN35AppleUSBXDCIModifiedControlTransfer18ep0InEventOccurredEN7USBXDCI22tAppleUSBXDCIEventTypeE : 2376 -> 2360

```
