## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

```diff

-13113.1.0.0.0
-  __TEXT.__text: 0x5c168
-  __TEXT.__auth_stubs: 0x1140
+13114.1.0.0.0
+  __TEXT.__text: 0x5ba64
+  __TEXT.__auth_stubs: 0x1120
   __TEXT.__const: 0x2a07
-  __TEXT.__gcc_except_tab: 0x49dc
+  __TEXT.__gcc_except_tab: 0x49c8
   __TEXT.__cstring: 0x2814
-  __TEXT.__oslogstring: 0x7fb1
+  __TEXT.__oslogstring: 0x7bd7
   __TEXT.__unwind_info: 0x1c90
   __DATA_CONST.__got: 0x258
   __DATA_CONST.__const: 0xd98
-  __AUTH_CONST.__auth_got: 0x8a8
+  __AUTH_CONST.__auth_got: 0x898
   __AUTH_CONST.__const: 0x3098
   __AUTH_CONST.__cfstring: 0x800
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 0332E91D-46CD-33A4-B7DA-F4774D069150
+  UUID: 26CDC152-C387-35EE-8645-FE7A6D64EB97
   Functions: 1290
-  Symbols:   3100
-  CStrings:  1298
+  Symbols:   3098
+  CStrings:  1280
 
Symbols:
- _TelephonyUtilIsOversteerEnabled
- __os_log_debug_impl
Functions:
~ __ZN2sd10DCNManager11scheduleDCNERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 444 -> 380
~ __ZN26SystemDeterminationManager22handleWebPushConnectedEb : 168 -> 4
~ __ZThn72_N26SystemDeterminationManager22handleWebPushConnectedEb : 8 -> 4
~ __ZN26SystemDeterminationManager23submitRcsDurationMetricERK13PersonalityID : 2140 -> 2076
~ __ZN26SystemDeterminationManager50checkBasebandAssertionIfInWiFiCallingOnlyMode_syncERKNSt3__110shared_ptrIN2sd27IMSSubscriberModelInterfaceEEE : 1000 -> 820
~ __ZN26SystemDeterminationManager26handleIsRoamingUpdate_syncEN10subscriber7SimSlotE13RoamingResult : 816 -> 732
~ __ZN26SystemDeterminationManager32handleDomesticRoamingUpdate_syncEN10subscriber7SimSlotEb : 388 -> 272
~ __ZThn48_N26SystemDeterminationManager32handleDomesticRoamingUpdate_syncEN10subscriber7SimSlotEb : 8 -> 12
~ __ZNK2sd23IMSSubscriberController41sendEmergencyAccessNetworkInfoUpdate_syncEv : 848 -> 784
~ __ZN2sd23IMSSubscriberController23handleImsPdpActive_syncEb15DataContextType : 1556 -> 1428
~ __ZNK2sd23IMSSubscriberController36isRequirementMetForCellularFootprintEv : 696 -> 476
~ __ZNK2sd23IMSSubscriberController38updateLazuliThirdPartyAppConfigurationEv : 400 -> 324
~ __ZN2sd18IMSSubscriberModel9bootstrapENSt3__110shared_ptrINS_27IMSSubscriberEventInterfaceEEENS2_INS_26IMSSubscriberModelDelegateEEE : 164 -> 148
~ __ZN2sd18IMSSubscriberModel32setImsRegistrationQualifierMasksEv : 68 -> 24
~ __ZN2sd18IMSSubscriberModel10setImsPrefE15DataContextTypePKN5caulk10option_setINS_14ImsServiceTypeEjEE : 1132 -> 1076
~ __ZN2sd18IMSSubscriberModel15enableTelephonyEb : 488 -> 392
~ __ZN2sd18IMSSubscriberModel18updateRoamingStateE13RoamingResult : 392 -> 312
~ __ZNK2sd18IMSSubscriberModel26getIsCellularFootprintSeenEv : 252 -> 116
~ __ZN2sd18IMSSubscriberModel26setIsCellularFootprintSeenEb : 264 -> 120
~ __ZN2sd18IMSSubscriberModel14updateIsimInfoEv : 1724 -> 1660
CStrings:
- "#D Async getting is LazuliThirdPartyApp"
- "#D Cellular footprint is not required for VoWiFi, ok to bring up IMS PDN"
- "#D Current DataContext is: %s. Checking CB key is not needed"
- "#D DCN already scheduled"
- "#D DomesticRoamingUpdate: roaming state %s"
- "#D EmergencyAccessNetworkInfoUpdate: Not in emergency call. Don't send emergency access network info update"
- "#D ISIM info didn't change"
- "#D ImsPdpActive: Lazuli mode. Country Of Origination not required"
- "#D ImsPdpActive: Not in iWLAN mode. Country Of Origination not required"
- "#D Not submitting RCSServiceDuration metric for zero duration"
- "#D Returning isCellularFootprintSeen as %s"
- "#D Roaming result remains as %s"
- "#D RoamingUpdate: Ignore undetermined roaming state %s"
- "#D Setting isCellularFootprintSeen to %s"
- "#D Telephony was NOT %s successfully"
- "#D WebPush connection status: %s"
- "#D WiFiCalling-only mode: true. Baseband booted assertion required. iSimInfoReady: %s, deviceInfoReady: %s. BB booted assertion held: %s"
- "#D fInCallImsPref is inactive!"

```
