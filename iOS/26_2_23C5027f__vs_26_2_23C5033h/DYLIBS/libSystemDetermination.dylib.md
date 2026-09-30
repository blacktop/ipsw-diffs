## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

```diff

-13123.3.0.0.0
-  __TEXT.__text: 0x5d55c
-  __TEXT.__auth_stubs: 0x1150
+13125.3.0.0.0
+  __TEXT.__text: 0x5ce58
+  __TEXT.__auth_stubs: 0x1130
   __TEXT.__const: 0x2a27
-  __TEXT.__gcc_except_tab: 0x4acc
+  __TEXT.__gcc_except_tab: 0x4ab8
   __TEXT.__cstring: 0x294c
-  __TEXT.__oslogstring: 0x8361
+  __TEXT.__oslogstring: 0x7f87
   __TEXT.__unwind_info: 0x1c88
   __DATA_CONST.__got: 0x260
   __DATA_CONST.__const: 0xdb8
-  __AUTH_CONST.__auth_got: 0x8b0
+  __AUTH_CONST.__auth_got: 0x8a0
   __AUTH_CONST.__const: 0x30d0
   __AUTH_CONST.__cfstring: 0x840
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 8F156DDD-334E-3B9B-AC3C-D1660DF08E2F
+  UUID: 72E1D3A7-145F-311D-8B69-74BA92C5E4D7
   Functions: 1296
-  Symbols:   3104
-  CStrings:  1324
+  Symbols:   3102
+  CStrings:  1306
 
Symbols:
- _TelephonyUtilIsOversteerEnabled
- __os_log_debug_impl
Functions:
~ __ZN2sd10DCNManager11scheduleDCNERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 444 -> 380
~ __ZN26SystemDeterminationManager22handleWebPushConnectedEb : 168 -> 4
~ __ZThn72_N26SystemDeterminationManager22handleWebPushConnectedEb : 8 -> 4
~ __ZN26SystemDeterminationManager23submitRcsDurationMetricERK13PersonalityID : 2244 -> 2180
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
