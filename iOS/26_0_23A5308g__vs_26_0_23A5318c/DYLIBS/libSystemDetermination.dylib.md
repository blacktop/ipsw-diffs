## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

```diff

-13090.3.0.0.0
-  __TEXT.__text: 0x57ac8
-  __TEXT.__auth_stubs: 0x10e0
+13091.1.6.0.0
+  __TEXT.__text: 0x5762c
+  __TEXT.__auth_stubs: 0x10c0
   __TEXT.__const: 0x2677
-  __TEXT.__gcc_except_tab: 0x4570
+  __TEXT.__gcc_except_tab: 0x4564
   __TEXT.__cstring: 0x25b9
-  __TEXT.__oslogstring: 0x7c9b
+  __TEXT.__oslogstring: 0x79c0
   __TEXT.__unwind_info: 0x1af0
   __DATA_CONST.__got: 0x218
   __DATA_CONST.__const: 0xcc8
-  __AUTH_CONST.__auth_got: 0x878
+  __AUTH_CONST.__auth_got: 0x868
   __AUTH_CONST.__const: 0x2cf8
   __AUTH_CONST.__cfstring: 0x800
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 6B717E80-847C-3B57-A5DE-CD9454FEF215
+  UUID: C42C009E-EF89-3974-82A2-2C2A9AA07750
   Functions: 1207
-  Symbols:   2892
-  CStrings:  1245
+  Symbols:   2890
+  CStrings:  1232
 
Symbols:
- _TelephonyUtilIsOversteerEnabled
- __os_log_debug_impl
Functions:
~ __ZN2sd10DCNManager11scheduleDCNERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 444 -> 380
~ __ZN26SystemDeterminationManager23submitRcsDurationMetricERK13PersonalityID : 1744 -> 1680
~ __ZN26SystemDeterminationManager50checkBasebandAssertionIfInWiFiCallingOnlyMode_syncERKNSt3__110shared_ptrIN2sd27IMSSubscriberModelInterfaceEEE : 1000 -> 820
~ __ZN26SystemDeterminationManager26handleIsRoamingUpdate_syncEN10subscriber7SimSlotE13RoamingResult : 816 -> 732
~ __ZN26SystemDeterminationManager32handleDomesticRoamingUpdate_syncEN10subscriber7SimSlotEb : 388 -> 272
~ __ZThn48_N26SystemDeterminationManager32handleDomesticRoamingUpdate_syncEN10subscriber7SimSlotEb : 8 -> 12
~ __ZNK2sd23IMSSubscriberController41sendEmergencyAccessNetworkInfoUpdate_syncEv : 848 -> 784
~ __ZNK2sd23IMSSubscriberController36isRequirementMetForCellularFootprintEv : 728 -> 548
~ __ZNK2sd23IMSSubscriberController38updateLazuliThirdPartyAppConfigurationEv : 400 -> 324
~ __ZN2sd18IMSSubscriberModel9bootstrapENSt3__110shared_ptrINS_27IMSSubscriberEventInterfaceEEENS2_INS_26IMSSubscriberModelDelegateEEE : 164 -> 148
~ __ZN2sd18IMSSubscriberModel32setImsRegistrationQualifierMasksEv : 68 -> 24
~ __ZN2sd18IMSSubscriberModel10setImsPrefE15DataContextTypePKN5caulk10option_setINS_14ImsServiceTypeEjEE : 1132 -> 1076
~ __ZN2sd18IMSSubscriberModel15enableTelephonyEb : 488 -> 392
~ __ZN2sd18IMSSubscriberModel18updateRoamingStateE13RoamingResult : 392 -> 312
~ __ZN2sd18IMSSubscriberModel14updateIsimInfoEv : 1724 -> 1660
CStrings:
- "#D Async getting is LazuliThirdPartyApp"
- "#D Cellular footprint is not required for VoWiFi, ok to bring up IMS PDN"
- "#D Current DataContext is: %s. Checking CB key is not needed"
- "#D DCN already scheduled"
- "#D DomesticRoamingUpdate: roaming state %s"
- "#D EmergencyAccessNetworkInfoUpdate: Not in emergency call. Don't send emergency access network info update"
- "#D ISIM info didn't change"
- "#D Not submitting RCSServiceDuration metric for zero duration"
- "#D Roaming result remains as %s"
- "#D RoamingUpdate: Ignore undetermined roaming state %s"
- "#D Telephony was NOT %s successfully"
- "#D WiFiCalling-only mode: true. Baseband booted assertion required. iSimInfoReady: %s, deviceInfoReady: %s. BB booted assertion held: %s"
- "#D fInCallImsPref is inactive!"

```
