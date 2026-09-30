## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

```diff

-13487.3.0.0.0
-  __TEXT.__text: 0x707d4
+13487.6.0.0.0
+  __TEXT.__text: 0x6fef8
   __TEXT.__const: 0x3f09
-  __TEXT.__gcc_except_tab: 0x5a38
+  __TEXT.__gcc_except_tab: 0x5a2c
   __TEXT.__cstring: 0x36e0
-  __TEXT.__oslogstring: 0xa272
+  __TEXT.__oslogstring: 0x9dfe
   __TEXT.__unwind_info: 0x2458
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xdf8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1804
-  Symbols:   2973
-  CStrings:  1475
+  Symbols:   2970
+  CStrings:  1453
 
Symbols:
- _TelephonyUtilIsOversteerEnabled
- __Z8asString18RegistrationStatus
- __os_log_debug_impl
Functions:
~ __ZN2sd10DCNManager11scheduleDCNERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 384 -> 320
~ __ZN26SystemDeterminationManager23submitRcsDurationMetricERK13PersonalityID : 2992 -> 2932
~ __ZN26SystemDeterminationManager50checkBasebandAssertionIfInWiFiCallingOnlyMode_syncERKNSt3__110shared_ptrIN2sd27IMSSubscriberModelInterfaceEEE : 792 -> 636
~ __ZZN26SystemDeterminationManager32handleRegisteredNetworkInfo_syncEN10subscriber7SimSlotERKNSt3__16vectorI27RegisteredNetworkInfoChangeNS2_9allocatorIS4_EEEERK21RegisteredNetworkInfoENK3$_0clINS2_10shared_ptrIN2sd32IMSSubscriberControllerInterfaceEEEEEDaT_ : 1344 -> 1200
~ __ZN26SystemDeterminationManager26handleCountryOfOriginationERKNSt3__110shared_ptrIN2sd32IMSSubscriberControllerInterfaceEEENS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 1608 -> 1516
~ __ZN26SystemDeterminationManager26handleIsRoamingUpdate_syncEN10subscriber7SimSlotE13RoamingResult : 672 -> 588
~ __ZN26SystemDeterminationManager32handleDomesticRoamingUpdate_syncEN10subscriber7SimSlotEb : 320 -> 264
~ __ZNSt3__110__function6__funcIZZN26SystemDeterminationManager15subscribeToPushERK13PersonalityIDRKNS_6vectorIhNS_9allocatorIhEEEERKNS_12basic_stringIcNS_11char_traitsIcEENS7_IcEEEENS_8functionIFvSI_xEEEENK3$_0clEvEUlSI_xE_SK_EclESI_Ox : 668 -> 400
~ __ZNSt3__110__function6__funcIZZN26SystemDeterminationManager26initPushUrlCheckTimer_syncEvENK3$_0clEvEUlRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEExE_FvSB_xEEclESB_Ox : 556 -> 288
~ __ZN2sd27IMSSubscriberControllerBase13resetShutdownEv : 64 -> 112
~ __ZN2sd27IMSSubscriberControllerBase23handleImsPdpActive_syncEb15DataContextType : 1456 -> 1328
~ __ZNK2sd23IMSSubscriberController41sendEmergencyAccessNetworkInfoUpdate_syncEv : 828 -> 764
~ __ZNK2sd23IMSSubscriberController36isRequirementMetForCellularFootprintEv : 596 -> 424
~ __ZN2sd18IMSSubscriberModel9bootstrapENSt3__110shared_ptrINS_27IMSSubscriberEventInterfaceEEENS2_INS_26IMSSubscriberModelDelegateEEE : 172 -> 156
~ __ZN2sd18IMSSubscriberModel32setImsRegistrationQualifierMasksEv : 68 -> 24
~ __ZN2sd18IMSSubscriberModel10setImsPrefE15DataContextTypePKN5caulk10option_setINS_14ImsServiceTypeEjEE : 1072 -> 1016
~ __ZN2sd18IMSSubscriberModel15enableTelephonyEb : 428 -> 332
~ __ZN2sd18IMSSubscriberModel23setRCSPcscfPropertyListENSt3__16vectorINS1_4pairINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_6UEInfo16RCSPcscfPropertyEEENS7_ISC_EEEE : 736 -> 512
~ __ZN2sd18IMSSubscriberModel18updateRoamingStateE13RoamingResult : 332 -> 252
~ __ZNK2sd18IMSSubscriberModel26getIsCellularFootprintSeenEv : 188 -> 100
~ __ZN2sd18IMSSubscriberModel26setIsCellularFootprintSeenEb : 196 -> 104
~ __ZN2sd18IMSSubscriberModel14updateIsimInfoEv : 1640 -> 1576
CStrings:
- "Cellular footprint is not required for VoWiFi, ok to bring up IMS PDN"
- "Current DataContext is: %s. Checking CB key is not needed"
- "DCN already scheduled"
- "DomesticRoamingUpdate: roaming state %{bool}d"
- "EmergencyAccessNetworkInfoUpdate: Not in emergency call. Don't send emergency access network info update"
- "ISIM info didn't change"
- "ImsPdpActive: Lazuli mode. Country Of Origination not required"
- "ImsPdpActive: Not in iWLAN mode. Country Of Origination not required"
- "Not submitting RCSServiceDuration metric for zero duration"
- "Received PushURL: %{public}s"
- "Returning isCellularFootprintSeen as %{bool}d"
- "Roaming result remains as %s"
- "RoamingUpdate: Ignore undetermined roaming state %s"
- "Setting isCellularFootprintSeen to %{bool}d"
- "Skipping fLastRegisteredNetworkInfo update: no valid cell info (RAT=%s DataMode=%s regStatus=%s)"
- "Stored PushURL: %{public}s"
- "Telephony was NOT %s successfully"
- "Updating RCSPcscfPropertyList: \n"
- "WiFiCalling-only mode: true. Baseband booted assertion required. iSimInfoReady: %{bool}d, deviceInfoReady: %{bool}d. BB booted assertion held: %{bool}d"
- "addr = %s"
- "fInCallImsPref is inactive!"
- "handleCountryOfOrigination: mcc INT is: %u"
```
