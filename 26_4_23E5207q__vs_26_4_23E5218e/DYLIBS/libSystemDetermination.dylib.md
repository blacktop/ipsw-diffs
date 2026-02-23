## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

```diff

-13169.2.1.2.0
-  __TEXT.__text: 0x5cd98
+13171.6.0.0.0
+  __TEXT.__text: 0x5d358
   __TEXT.__auth_stubs: 0x1160
   __TEXT.__const: 0x2ef4
-  __TEXT.__gcc_except_tab: 0x4ce0
-  __TEXT.__cstring: 0x29d7
-  __TEXT.__oslogstring: 0x8a60
+  __TEXT.__gcc_except_tab: 0x4d68
+  __TEXT.__cstring: 0x2a02
+  __TEXT.__oslogstring: 0x8ac0
   __TEXT.__unwind_info: 0x1db0
   __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0xdb8
+  __DATA_CONST.__const: 0xdc0
   __AUTH_CONST.__auth_got: 0x8b8
   __AUTH_CONST.__const: 0x33a8
   __AUTH_CONST.__cfstring: 0x840

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 32E03FC4-5CB9-3084-A55D-B78E1BDE87F4
+  UUID: 3D3311EE-9094-342C-9443-2AC11BDA79F3
   Functions: 1364
   Symbols:   3272
-  CStrings:  1348
+  CStrings:  1353
 
Symbols:
+ __ZNK2sd23IMSSubscriberController23isPrivateRelaySupportedEv
+ __ZThn48_NK2sd23IMSSubscriberController23isPrivateRelaySupportedEv
- __ZNK2sd23IMSSubscriberController21isPrivateRelayEnabledEv
- __ZThn48_NK2sd23IMSSubscriberController21isPrivateRelayEnabledEv
Functions:
~ __ZN26SystemDeterminationManager40handleLazuliRegistrationStateChange_syncERK13PersonalityIDRKN2sd21ImsRegistrationStatusE : 1052 -> 1248
~ __ZZN8dispatch5asyncIZNK3ctu20SharedSynchronizableI26SystemDeterminationManagerE15execute_wrappedIZNS3_22handleWebPushConnectedEbE3$_0EEvOT_EUlvE_EEvP16dispatch_queue_sNSt3__110unique_ptrIS7_NSC_14default_deleteIS7_EEEEENUlPvE_8__invokeESH_ : 368 -> 364
~ __ZN2sd23IMSSubscriberController30handleRegistrationStateChangedERKN3ims17RegistrationStateE : 2440 -> 2592
~ __ZN2sd23IMSSubscriberController24handleRegistrationActiveERKN3ims22RegistrationActiveInfoE : 1208 -> 1496
~ __ZN2sd23IMSSubscriberController33handleImsRegistrationStatusUpdateERKNS_21ImsRegistrationStatusE : 1228 -> 1360
~ __ZN2sd23IMSSubscriberController23handleRegistrationEventERKN3ims16RegistrationInfoE : 3516 -> 3688
~ __ZN2sd23IMSSubscriberController25handleRegistrationAllowedEv : 624 -> 812
~ __ZN2sd23IMSSubscriberController22onRCSSwitchoverTimeoutEv : 584 -> 728
~ __ZN2sd23IMSSubscriberController22handleWebPushConnectedEv : 164 -> 336
~ __ZNK2sd23IMSSubscriberController9dumpStateEv : 3604 -> 3616
~ __ZNK2sd9DataCache14getRuntimeInfoEv : 296 -> 304
~ __ZN2sd9DataCache17updateRuntimeInfoERKNS_11RuntimeInfoE : 188 -> 196
~ __ZN2sd9DataCacheC2Ev : 240 -> 244
CStrings:
+ "#I APNS connection is active, Checking if we need to restart RCS..."
+ "#I Private Relay Status: %s"
+ "#I WebPush connection status: %{bool}d"
+ "ACTIVE"
+ "INACTIVE"
+ "kInviteCompletion"
+ "kMsrpCompletion"
+ "kPagerCompletion"
+ "kRegistrationSuccess"
+ "kTransportInitComplete"
- "#D WebPush connection status: %{bool}d"
- "InviteCompletion"
- "MsrpCompletion"
- "PagerCompletion"
- "RegistrationSuccess"

```
