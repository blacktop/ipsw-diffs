## ACIPCBTLib.dylib

> `/usr/lib/ACIPCBTLib.dylib`

```diff

-183.100.2.0.0
-  __TEXT.__text: 0x4264
-  __TEXT.__auth_stubs: 0x310
+194.0.0.0.0
+  __TEXT.__text: 0x3f94
   __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x38
+  __TEXT.__gcc_except_tab: 0x20
   __TEXT.__cstring: 0xbe2
   __TEXT.__oslogstring: 0x7d6
   __TEXT.__unwind_info: 0x128
-  __DATA_CONST.__got: 0x38
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x430
-  __AUTH_CONST.__auth_got: 0x190
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x60
+  __AUTH_CONST.__auth_got: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: ECAB463C-1B0D-3184-82FB-D636844AFB74
+  UUID: 8BE4AFEC-95A9-3620-B28C-B5A15F2075F8
   Functions: 88
-  Symbols:   193
+  Symbols:   192
   CStrings:  169
 
Symbols:
- __Unwind_Resume
Functions:
~ __ZN12ACIPCBTClassD2Ev : 212 -> 160
~ __ZN12ACIPCBTClass4stopEP16dispatch_group_s : 728 -> 684
~ __ZN12ACIPCBTClass8start_nlEPKcP11__CFRunLoopP16dispatch_queue_sU13block_pointerFvjES7_U13block_pointerFv14acipcErrorTypejiE : 1496 -> 1452
~ __ZN12ACIPCBTClass8close_nlEv : 264 -> 220
~ __ZN12ACIPCBTClass4openEj : 216 -> 172
~ __ZN12ACIPCBTClass25setUpNotificationCallbackEj : 244 -> 200
~ __ZN12ACIPCBTClass5closeEv : 208 -> 164
~ __ZN19ACIPCBTControlClassD2Ev : 208 -> 156
~ __ZN19ACIPCBTControlClass4stopEv : 324 -> 280
~ __ZN19ACIPCBTControlClass14waitforServiceEv : 928 -> 884
~ __ZN19ACIPCBTControlClass5startEv : 340 -> 296
~ __ZN19ACIPCBTControlClass30deregisterEventNotification_nlEP16dispatch_group_s : 672 -> 628
~ __ZN19ACIPCBTControlClass4openEP11__CFRunLoop : 220 -> 176
~ __ZN19ACIPCBTControlClass4openEP16dispatch_queue_s : 220 -> 176
~ __ZN19ACIPCBTControlClass5closeEv : 208 -> 164
~ __ZN19ACIPCBTControlClass28registerEventNotification_nlEP11__CFRunLoopP16dispatch_queue_sP17ACIPCControlEvent : 1132 -> 1088

```
