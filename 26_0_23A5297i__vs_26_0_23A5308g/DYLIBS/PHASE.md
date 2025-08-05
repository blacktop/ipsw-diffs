## PHASE

> `/System/Library/Frameworks/PHASE.framework/PHASE`

```diff

-349.101.0.0.0
-  __TEXT.__text: 0x249e58
+349.105.0.0.0
+  __TEXT.__text: 0x249e8c
   __TEXT.__auth_stubs: 0x1a20
   __TEXT.__objc_methlist: 0x58f4
   __TEXT.__const: 0x43dec
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__gcc_except_tab: 0x28ac0
-  __TEXT.__oslogstring: 0x1fb30
+  __TEXT.__oslogstring: 0x1fb3d
   __TEXT.__cstring: 0x14891
   __TEXT.__unwind_info: 0xb908
   __TEXT.__eh_frame: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9133D67A-D5F9-363D-A4E0-A9223FCB0842
+  UUID: 1EA4B7E7-A6F4-352B-8F1B-C7A76AF4E19A
   Functions: 9407
   Symbols:   26455
   CStrings:  7600
Functions:
~ __ZN5Phase10Controller5DVM2310DvmAdapter23ConnectSubmixToRendererENS_14UniqueObjectIdES3_d : 1152 -> 1160
~ __ZN5Phase10Controller5DVM2316SubmixController14ConnectToGraphEPNS1_17DspVoiceManager23EPNS1_15GraphControllerENSt3__16vectorIfNS7_9allocatorIfEEEEdNS1_28SubmixChannelStripController6OutputE : 1844 -> 1880
~ __ZN5Phase10Controller5DVM2316SubmixController12SetSendLevelEPNS1_17DspVoiceManager23ENS_14UniqueObjectIdEdd : 260 -> 268
CStrings:
+ "%25s:%-5d Connecting SubmixId %llu to RendererId %llu with gain %f."
- "%25s:%-5d Connecting SubmixId %llu to RendererId %llu."

```
