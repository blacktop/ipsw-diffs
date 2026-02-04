## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

```diff

-13149.11.0.0.0
-  __TEXT.__text: 0x60de8
-  __TEXT.__auth_stubs: 0x1160
+13149.12.0.0.0
+  __TEXT.__text: 0x603e8
+  __TEXT.__auth_stubs: 0x1140
   __TEXT.__const: 0x3067
-  __TEXT.__gcc_except_tab: 0x4d6c
+  __TEXT.__gcc_except_tab: 0x4d50
   __TEXT.__cstring: 0x29d2
-  __TEXT.__oslogstring: 0x8747
+  __TEXT.__oslogstring: 0x8301
   __TEXT.__unwind_info: 0x1d80
   __DATA_CONST.__got: 0x268
   __DATA_CONST.__const: 0xdb8
-  __AUTH_CONST.__auth_got: 0x8b8
+  __AUTH_CONST.__auth_got: 0x8a8
   __AUTH_CONST.__const: 0x3398
   __AUTH_CONST.__cfstring: 0x840
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: FA2D2B43-8B67-3383-A652-BD8AD1271D4F
+  UUID: 98D0AB14-1C46-32D1-AD6B-AC87C6173431
   Functions: 1354
-  Symbols:   3251
-  CStrings:  1345
+  Symbols:   3249
+  CStrings:  1324
 
Symbols:
- _TelephonyUtilIsOversteerEnabled
- __os_log_debug_impl
Functions:
~ __ZN2sd10DCNManager11scheduleDCNERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 444 -> 380
~ __ZN26SystemDeterminationManager22handleWebPushConnectedEb : 168 -> 4
~ __ZThn72_N26SystemDeterminationManager22handleWebPushConnectedEb : 8 -> 4
~ __ZN26SystemDeterminationManager23submitRcsDurationMetricERK13PersonalityID : 2340 -> 2276
~ __ZN26SystemDeterminationManager50checkBasebandAssertionIfInWiFiCallingOnlyMode_syncERKNSt3__110shared_ptrIN2sd27IMSSubscriberModelInterfaceEEE : 1000 -> 820
~ __ZN26SystemDeterminationManager26handleCountryOfOriginationERKNSt3__110shared_ptrIN2sd32IMSSubscriberControllerInterfaceEEENS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 1840 -> 1756
~ __ZN26SystemDeterminationManager26handleIsRoamingUpdate_syncEN10subscriber7SimSlotE13RoamingResult : 816 -> 732
~ __ZN26SystemDeterminationManager32handleDomesticRoamingUpdate_syncEN10subscriber7SimSlotEb : 388 -> 272
~ __ZThn48_N26SystemDeterminationManager32handleDomesticRoamingUpdate_syncEN10subscriber7SimSlotEb : 8 -> 12
~ __ZNSt3__110__function6__funcIZZN26SystemDeterminationManager15subscribeToPushEN10subscriber7SimSlotERKNS_6vectorIhNS_9allocatorIhEEEERKNS_12basic_stringIcNS_11char_traitsIcEENS6_IcEEEENS_8functionIFvSH_xEEEENK3$_0clEvEUlSH_xE_NS6_ISM_EESJ_EclESH_Ox : 776 -> 416
~ __ZNSt3__110__function6__funcIZZN26SystemDeterminationManager26initPushUrlCheckTimer_syncEvENK3$_0clEvEUlRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEExE_NS7_ISC_EEFvSB_xEEclESB_Ox : 624 -> 304
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
- "#D Received PushURL: %{public}s"
- "#D Returning isCellularFootprintSeen as %s"
- "#D Roaming result remains as %s"
- "#D RoamingUpdate: Ignore undetermined roaming state %s"
- "#D Setting isCellularFootprintSeen to %s"
- "#D Stored PushURL: %{public}s"
- "#D Telephony was NOT %s successfully"
- "#D WebPush connection status: %s"
- "#D WiFiCalling-only mode: true. Baseband booted assertion required. iSimInfoReady: %s, deviceInfoReady: %s. BB booted assertion held: %s"
- "#D fInCallImsPref is inactive!"
- "#D handleCountryOfOrigination: mcc INT is: %u"

```
