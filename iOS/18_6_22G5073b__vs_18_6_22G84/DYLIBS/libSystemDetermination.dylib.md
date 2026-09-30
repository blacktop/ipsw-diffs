## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

```diff

 12412.1.0.0.0
-  __TEXT.__text: 0x554dc
-  __TEXT.__auth_stubs: 0x10d0
+  __TEXT.__text: 0x55180
+  __TEXT.__auth_stubs: 0x10b0
   __TEXT.__const: 0x2487
   __TEXT.__gcc_except_tab: 0x43c4
   __TEXT.__cstring: 0x259a
-  __TEXT.__oslogstring: 0x798f
+  __TEXT.__oslogstring: 0x77a0
   __TEXT.__unwind_info: 0x19f0
   __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__const: 0xcc8
-  __AUTH_CONST.__auth_got: 0x870
+  __AUTH_CONST.__auth_got: 0x860
   __AUTH_CONST.__const: 0x2b88
   __AUTH_CONST.__cfstring: 0x7c0
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 6F58DF68-3F7E-3969-A4DB-DBED2A4AB834
+  UUID: 057480DE-9B41-3E05-90EA-2FD8535E287F
   Functions: 1167
-  Symbols:   2789
-  CStrings:  1229
+  Symbols:   2787
+  CStrings:  1220
 
Symbols:
- _TelephonyUtilIsOversteerEnabled
- __os_log_debug_impl
Functions:
~ __ZNK2sd23IMSSubscriberController41sendEmergencyAccessNetworkInfoUpdate_syncEv : 848 -> 784
~ __ZN2sd10DCNManager11scheduleDCNERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE : 444 -> 380
~ __ZN26SystemDeterminationManager50checkBasebandAssertionIfInWiFiCallingOnlyMode_syncERKNSt3__110shared_ptrIN2sd27IMSSubscriberModelInterfaceEEE : 1000 -> 820
~ __ZN26SystemDeterminationManager26handleIsRoamingUpdate_syncEN10subscriber7SimSlotE13RoamingResult : 816 -> 732
~ __ZN26SystemDeterminationManager32handleDomesticRoamingUpdate_syncEN10subscriber7SimSlotEb : 388 -> 272
~ __ZThn48_N26SystemDeterminationManager32handleDomesticRoamingUpdate_syncEN10subscriber7SimSlotEb : 8 -> 12
~ __ZN2sd18IMSSubscriberModel9bootstrapENSt3__110shared_ptrINS_27IMSSubscriberEventInterfaceEEENS2_INS_26IMSSubscriberModelDelegateEEE : 164 -> 148
~ __ZN2sd18IMSSubscriberModel32setImsRegistrationQualifierMasksEv : 68 -> 24
~ __ZN2sd18IMSSubscriberModel10setImsPrefE15DataContextTypePKN5caulk10option_setINS_14ImsServiceTypeEjEE : 1088 -> 1032
~ __ZN2sd18IMSSubscriberModel15enableTelephonyEb : 488 -> 392
~ __ZN2sd18IMSSubscriberModel18updateRoamingStateE13RoamingResult : 392 -> 312
~ __ZN2sd18IMSSubscriberModel14updateIsimInfoEv : 1724 -> 1660
CStrings:
- "#D DCN already scheduled"
- "#D DomesticRoamingUpdate: roaming state %s"
- "#D EmergencyAccessNetworkInfoUpdate: Not in emergency call. Don't send emergency access network info update"
- "#D ISIM info didn't change"
- "#D Roaming result remains as %s"
- "#D RoamingUpdate: Ignore undetermined roaming state %s"
- "#D Telephony was NOT %s successfully"
- "#D WiFiCalling-only mode: true. Baseband booted assertion required. iSimInfoReady: %s, deviceInfoReady: %s. BB booted assertion held: %s"
- "#D fInCallImsPref is inactive!"

```
