## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

```diff

-13173.1.3.0.0
-  __TEXT.__text: 0x5fb20
-  __TEXT.__auth_stubs: 0x1160
+13184.1.0.0.0
+  __TEXT.__text: 0x602bc
+  __TEXT.__auth_stubs: 0x1180
   __TEXT.__const: 0x32b4
-  __TEXT.__gcc_except_tab: 0x5080
+  __TEXT.__gcc_except_tab: 0x5084
   __TEXT.__cstring: 0x2c00
-  __TEXT.__oslogstring: 0x8a73
+  __TEXT.__oslogstring: 0x8ebc
   __TEXT.__unwind_info: 0x1ea0
-  __DATA_CONST.__got: 0x268
+  __DATA_CONST.__got: 0x260
   __DATA_CONST.__const: 0xdc0
-  __AUTH_CONST.__auth_got: 0x8b8
+  __AUTH_CONST.__auth_got: 0x8c8
   __AUTH_CONST.__const: 0x35f8
   __AUTH_CONST.__cfstring: 0x840
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 904BF574-2D52-3CCA-A9C4-9A0F5B2566CB
+  UUID: 99F256AF-CCC5-301B-9959-EBC919E365EF
   Functions: 1417
-  Symbols:   3390
-  CStrings:  1368
+  Symbols:   3391
+  CStrings:  1388
 
Symbols:
+ _TelephonyUtilIsOversteerEnabled
+ __os_log_debug_impl
- __ZTI28LazuliHealthMonitorInterface
Functions:
~ __ZN2sd10DCNManager11scheduleDCNERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 364 -> 428
~ __ZN26SystemDeterminationManager23submitRcsDurationMetricERK13PersonalityID : 2348 -> 2412
~ __ZN26SystemDeterminationManager50checkBasebandAssertionIfInWiFiCallingOnlyMode_syncERKNSt3__110shared_ptrIN2sd27IMSSubscriberModelInterfaceEEE : 748 -> 892
~ __ZN26SystemDeterminationManager26handleCountryOfOriginationERKNSt3__110shared_ptrIN2sd32IMSSubscriberControllerInterfaceEEENS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 1692 -> 1760
~ __ZN26SystemDeterminationManager26handleIsRoamingUpdate_syncEN10subscriber7SimSlotE13RoamingResult : 676 -> 760
~ __ZN26SystemDeterminationManager32handleDomesticRoamingUpdate_syncEN10subscriber7SimSlotEb : 264 -> 364
~ __ZNSt3__110__function6__funcIZZN26SystemDeterminationManager15subscribeToPushEN10subscriber7SimSlotERKNS_6vectorIhNS_9allocatorIhEEEERKNS_12basic_stringIcNS_11char_traitsIcEENS6_IcEEEENS_8functionIFvSH_xEEEENK3$_0clEvEUlSH_xE_SJ_EclESH_Ox : 400 -> 744
~ __ZNSt3__110__function6__funcIZZN26SystemDeterminationManager26initPushUrlCheckTimer_syncEvENK3$_0clEvEUlRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEExE_FvSB_xEEclESB_Ox : 288 -> 592
~ __ZN2sd23IMSSubscriberController24initializeImsClient_syncEb : 2340 -> 2344
~ __ZNK2sd23IMSSubscriberController41sendEmergencyAccessNetworkInfoUpdate_syncEv : 744 -> 808
~ __ZN2sd23IMSSubscriberController23handleImsPdpActive_syncEb15DataContextType : 1292 -> 1420
~ __ZNK2sd23IMSSubscriberController36isRequirementMetForCellularFootprintEv : 436 -> 640
~ __ZNK2sd23IMSSubscriberController38updateLazuliThirdPartyAppConfigurationEv : 324 -> 400
~ __ZN2sd23IMSSubscriberController20handleWebPushMessageERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERK17WebPushTimestampsbRKNS1_10shared_ptrINS1_3mapIS7_S7_NS1_4lessIS7_EENS5_INS1_4pairIS8_S7_EEEEEEEE : 2692 -> 2368
~ __ZN2sd18IMSSubscriberModel9bootstrapENSt3__110shared_ptrINS_27IMSSubscriberEventInterfaceEEENS2_INS_26IMSSubscriberModelDelegateEEE : 156 -> 172
~ __ZN2sd18IMSSubscriberModel32setImsRegistrationQualifierMasksEv : 24 -> 68
~ __ZN2sd18IMSSubscriberModel10setImsPrefE15DataContextTypePKN5caulk10option_setINS_14ImsServiceTypeEjEE : 1016 -> 1072
~ __ZN2sd18IMSSubscriberModel15enableTelephonyEb : 376 -> 472
~ __ZN2sd18IMSSubscriberModel18updateRoamingStateE13RoamingResult : 296 -> 376
~ __ZNK2sd18IMSSubscriberModel26getIsCellularFootprintSeenEv : 100 -> 232
~ __ZN2sd18IMSSubscriberModel26setIsCellularFootprintSeenEb : 104 -> 240
~ __ZN2sd18IMSSubscriberModel14updateIsimInfoEv : 1636 -> 1700
CStrings:
+ "#D Async getting is LazuliThirdPartyApp"
+ "#D Cellular footprint is not required for VoWiFi, ok to bring up IMS PDN"
+ "#D Current DataContext is: %s. Checking CB key is not needed"
+ "#D DCN already scheduled"
+ "#D DomesticRoamingUpdate: roaming state %{bool}d"
+ "#D EmergencyAccessNetworkInfoUpdate: Not in emergency call. Don't send emergency access network info update"
+ "#D ISIM info didn't change"
+ "#D ImsPdpActive: Lazuli mode. Country Of Origination not required"
+ "#D ImsPdpActive: Not in iWLAN mode. Country Of Origination not required"
+ "#D Not submitting RCSServiceDuration metric for zero duration"
+ "#D Received PushURL: %{public}s"
+ "#D Returning isCellularFootprintSeen as %{bool}d"
+ "#D Roaming result remains as %s"
+ "#D RoamingUpdate: Ignore undetermined roaming state %s"
+ "#D Setting isCellularFootprintSeen to %{bool}d"
+ "#D Stored PushURL: %{public}s"
+ "#D Telephony was NOT %s successfully"
+ "#D WiFiCalling-only mode: true. Baseband booted assertion required. iSimInfoReady: %{bool}d, deviceInfoReady: %{bool}d. BB booted assertion held: %{bool}d"
+ "#D fInCallImsPref is inactive!"
+ "#D handleCountryOfOrigination: mcc INT is: %u"

```
