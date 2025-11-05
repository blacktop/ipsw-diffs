## ACIPCBTLib.dylib

> `/usr/lib/ACIPCBTLib.dylib`

```diff

-110.0.0.0.0
-  __TEXT.__text: 0x4408
+126.0.0.0.0
+  __TEXT.__text: 0x432c
   __TEXT.__auth_stubs: 0x330
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x38

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: A8607C87-C9B6-354F-8D39-A31719A27187
+  UUID: 1D0977BA-7BC9-3957-A8A6-040A1B55D9A9
   Functions: 92
   Symbols:   170
   CStrings:  169
Functions:
~ __ZN12ACIPCBTClass4stopEP16dispatch_group_s : 740 -> 728
~ __ZN12ACIPCBTClass5startEPKcP11__CFRunLoopU13block_pointerFvjES5_U13block_pointerFv14acipcErrorTypejiE : 136 -> 124
~ __ZN12ACIPCBTClass8start_nlEPKcP11__CFRunLoopP16dispatch_queue_sU13block_pointerFvjES7_U13block_pointerFv14acipcErrorTypejiE : 1504 -> 1496
~ __ZN12ACIPCBTClass5startEPKcP16dispatch_queue_sU13block_pointerFvjES5_U13block_pointerFv14acipcErrorTypejiE : 136 -> 124
~ __ZN12ACIPCBTClass8close_nlEv : 268 -> 264
~ __ZN12ACIPCBTClass4openEj : 228 -> 216
~ __ZN12ACIPCBTClass5closeEv : 212 -> 208
~ __ZN12ACIPCBTClass5writeEPKvj : 288 -> 284
~ __ZN12ACIPCBTClass10writeAsyncEPKvjPFvPviS2_ES2_ : 444 -> 440
~ __ZN12ACIPCBTClass4readEPvPj : 316 -> 312
~ __ZN12ACIPCBTClass9readAsyncEPvjPFvS0_iS0_ES0_ : 444 -> 440
~ __ZN12ACIPCBTClass9sendImageEPKvjPj : 464 -> 460
~ __ZN12ACIPCBTClass14sendImageAsyncEPKvjPFvPviS2_S2_ES2_ : 460 -> 456
~ __ZN12ACIPCBTClass12readRegisterEjPvPj : 336 -> 324
~ __ZN12ACIPCBTClass17abortChannelAsyncE14acipcDirectionPFvPviES1_ : 468 -> 456
~ __ZN12ACIPCBTClass17startChannelAsyncE14acipcDirectionPFvPviES1_ : 468 -> 456
~ __ZN19ACIPCBTControlClass4stopEv : 328 -> 324
~ __ZN19ACIPCBTControlClass14waitforServiceEv : 948 -> 928
~ __ZN19ACIPCBTControlClass5startEv : 344 -> 340
~ __ZN19ACIPCBTControlClass8close_nlEv : 144 -> 148
~ __ZN19ACIPCBTControlClass4openEP11__CFRunLoop : 232 -> 220
~ __ZN19ACIPCBTControlClass7open_nlEP11__CFRunLoopP16dispatch_queue_s : 224 -> 216
~ __ZN19ACIPCBTControlClass4openEP16dispatch_queue_s : 232 -> 220
~ __ZN19ACIPCBTControlClass5closeEv : 212 -> 208
~ __ZN19ACIPCBTControlClass13readLogsAsyncEPvjbPFvS0_iS0_ES0_ : 464 -> 452
~ __ZN19ACIPCBTControlClass25registerEventNotificationEP11__CFRunLoopP17ACIPCControlEvent : 96 -> 92
~ __ZN19ACIPCBTControlClass25registerEventNotificationEP16dispatch_queue_sP17ACIPCControlEvent : 96 -> 92
~ __ZN19ACIPCBTControlClass27deregisterEventNotificationEP16dispatch_group_s : 88 -> 76
~ __ZN19ACIPCBTControlClass10loggerTuneEjjPvS0_ : 320 -> 316

```
