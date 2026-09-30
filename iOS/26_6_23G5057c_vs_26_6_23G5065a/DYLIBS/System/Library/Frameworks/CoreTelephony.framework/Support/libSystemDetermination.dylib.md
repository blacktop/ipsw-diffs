## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`

```diff

-  __TEXT.__text: 0x60a08
-  __TEXT.__auth_stubs: 0x11a0
+  __TEXT.__text: 0x6012c
+  __TEXT.__auth_stubs: 0x1180
   __TEXT.__const: 0x32b4
-  __TEXT.__gcc_except_tab: 0x50a4
+  __TEXT.__gcc_except_tab: 0x5088
   __TEXT.__cstring: 0x2be5
-  __TEXT.__oslogstring: 0x90ba
+  __TEXT.__oslogstring: 0x8c71
   __TEXT.__unwind_info: 0x1eb0
   __DATA_CONST.__got: 0x268
   __DATA_CONST.__const: 0xdc0
-  __AUTH_CONST.__auth_got: 0x8d8
+  __AUTH_CONST.__auth_got: 0x8c8
   __AUTH_CONST.__const: 0x3608
   __AUTH_CONST.__cfstring: 0x840
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   Functions: 1419
-  Symbols:   2444
-  CStrings:  1330
+  Symbols:   2442
+  CStrings:  1310
 
Symbols:
- _TelephonyUtilIsOversteerEnabled
- __os_log_debug_impl
Functions:
~ __ZN2sd10DCNManager11scheduleDCNERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 428 -> 364
~ __ZN26SystemDeterminationManager23submitRcsDurationMetricERK13PersonalityID : 2412 -> 2348
~ __ZN26SystemDeterminationManager50checkBasebandAssertionIfInWiFiCallingOnlyMode_syncERKNSt3__110shared_ptrIN2sd27IMSSubscriberModelInterfaceEEE : 892 -> 748
~ __ZN26SystemDeterminationManager26handleCountryOfOriginationERKNSt3__110shared_ptrIN2sd32IMSSubscriberControllerInterfaceEEENS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 1760 -> 1692
~ __ZN26SystemDeterminationManager26handleIsRoamingUpdate_syncEN10subscriber7SimSlotE13RoamingResult : 760 -> 676
~ __ZN26SystemDeterminationManager32handleDomesticRoamingUpdate_syncEN10subscriber7SimSlotEb : 364 -> 264
~ __ZNSt3__110__function6__funcIZZN26SystemDeterminationManager15subscribeToPushEN10subscriber7SimSlotERKNS_6vectorIhNS_9allocatorIhEEEERKNS_12basic_stringIcNS_11char_traitsIcEENS6_IcEEEENS_8functionIFvSH_xEEEENK3$_0clEvEUlSH_xE_SJ_EclESH_Ox : 744 -> 400
~ __ZNSt3__110__function6__funcIZZN26SystemDeterminationManager26initPushUrlCheckTimer_syncEvENK3$_0clEvEUlRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEExE_FvSB_xEEclESB_Ox : 592 -> 288
~ __ZNK2sd23IMSSubscriberController41sendEmergencyAccessNetworkInfoUpdate_syncEv : 808 -> 744
~ __ZN2sd23IMSSubscriberController23handleImsPdpActive_syncEb15DataContextType : 1420 -> 1292
~ __ZNK2sd23IMSSubscriberController36isRequirementMetForCellularFootprintEv : 640 -> 436
~ __ZNK2sd23IMSSubscriberController38updateLazuliThirdPartyAppConfigurationEv : 400 -> 324
~ __ZN2sd18IMSSubscriberModel9bootstrapENSt3__110shared_ptrINS_27IMSSubscriberEventInterfaceEEENS2_INS_26IMSSubscriberModelDelegateEEE : 172 -> 156
~ __ZN2sd18IMSSubscriberModel32setImsRegistrationQualifierMasksEv : 68 -> 24
~ __ZN2sd18IMSSubscriberModel10setImsPrefE15DataContextTypePKN5caulk10option_setINS_14ImsServiceTypeEjEE : 1072 -> 1016
~ __ZN2sd18IMSSubscriberModel15enableTelephonyEb : 472 -> 376
~ __ZN2sd18IMSSubscriberModel18updateRoamingStateE13RoamingResult : 376 -> 296
~ __ZNK2sd18IMSSubscriberModel26getIsCellularFootprintSeenEv : 232 -> 100
~ __ZN2sd18IMSSubscriberModel26setIsCellularFootprintSeenEb : 240 -> 104
~ __ZN2sd18IMSSubscriberModel14updateIsimInfoEv : 1700 -> 1636
CStrings:
- "#D Async getting is LazuliThirdPartyApp"
- "#D Cellular footprint is not required for VoWiFi, ok to bring up IMS PDN"
- "#D Current DataContext is: %s. Checking CB key is not needed"
- "#D DCN already scheduled"
- "#D DomesticRoamingUpdate: roaming state %{bool}d"
- "#D EmergencyAccessNetworkInfoUpdate: Not in emergency call. Don't send emergency access network info update"
- "#D ISIM info didn't change"
- "#D ImsPdpActive: Lazuli mode. Country Of Origination not required"
- "#D ImsPdpActive: Not in iWLAN mode. Country Of Origination not required"
- "#D Not submitting RCSServiceDuration metric for zero duration"
- "#D Received PushURL: %{public}s"
- "#D Returning isCellularFootprintSeen as %{bool}d"
- "#D Roaming result remains as %s"
- "#D RoamingUpdate: Ignore undetermined roaming state %s"
- "#D Setting isCellularFootprintSeen to %{bool}d"
- "#D Stored PushURL: %{public}s"
- "#D Telephony was NOT %s successfully"
- "#D WiFiCalling-only mode: true. Baseband booted assertion required. iSimInfoReady: %{bool}d, deviceInfoReady: %{bool}d. BB booted assertion held: %{bool}d"
- "#D fInCallImsPref is inactive!"
- "#D handleCountryOfOrigination: mcc INT is: %u"
```
