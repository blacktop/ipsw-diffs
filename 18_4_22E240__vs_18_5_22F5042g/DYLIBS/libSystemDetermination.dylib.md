## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

```diff

-12322.6.0.0.0
-  __TEXT.__text: 0x53c80
-  __TEXT.__auth_stubs: 0x1060
+12403.2.2.0.0
+  __TEXT.__text: 0x554dc
+  __TEXT.__auth_stubs: 0x10d0
   __TEXT.__const: 0x2487
-  __TEXT.__gcc_except_tab: 0x4178
-  __TEXT.__cstring: 0x24c7
-  __TEXT.__oslogstring: 0x76a3
-  __TEXT.__unwind_info: 0x1978
-  __DATA_CONST.__got: 0x1f0
+  __TEXT.__gcc_except_tab: 0x43c4
+  __TEXT.__cstring: 0x25ad
+  __TEXT.__oslogstring: 0x798f
+  __TEXT.__unwind_info: 0x19f0
+  __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__const: 0xcc8
-  __AUTH_CONST.__auth_got: 0x838
-  __AUTH_CONST.__const: 0x2b40
+  __AUTH_CONST.__auth_got: 0x870
+  __AUTH_CONST.__const: 0x2b88
   __AUTH_CONST.__cfstring: 0x7c0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x60

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 1155
-  Symbols:   1584
-  CStrings:  1141
+  Functions: 1167
+  Symbols:   1605
+  CStrings:  1168
 
Symbols:
+ _TelephonyUtilIsOversteerEnabled
+ __Z23SlotIdFromPersonalityIdRKNSt3__110shared_ptrIK8RegistryEERK13PersonalityID
+ __ZN26SystemDeterminationManager23submitRcsDurationMetricERK13PersonalityID
+ __ZN26SystemDeterminationManager27handleLazuliTransportSwitchERK13PersonalityIDb
+ __ZN26SystemDeterminationManager29notifyLazuliRegistrationStateERKNSt3__110shared_ptrIN2sd27IMSSubscriberModelInterfaceEEERKNS2_21ImsRegistrationStatusE
+ __ZN26SystemDeterminationManager31handleLazuliRefreshStarted_syncERK13PersonalityID
+ __ZN2sd8asStringENS_20RCSStateChangeReasonE
+ __ZNK2sd18IMSSubscriberModel31isIMSAllowedBasedOnTTYMode_syncEb
+ __ZNK2sd19IMSSubscriberConfig15getRTTSupportedEb
+ __ZNK2sd19IMSSubscriberConfig24getEmergencyRTTSupportedEb
+ __ZTI27TelephonyAnalyticsInterface
+ __ZThn48_N26SystemDeterminationManager31handleLazuliRefreshStarted_syncERK13PersonalityID
+ __ZThn56_N26SystemDeterminationManager27handleLazuliTransportSwitchERK13PersonalityIDb
+ __ZThn56_N26SystemDeterminationManager29notifyLazuliRegistrationStateERKNSt3__110shared_ptrIN2sd27IMSSubscriberModelInterfaceEEERKNS2_21ImsRegistrationStatusE
+ __os_log_debug_impl
+ _dispatch_assert_queue$V2
+ _xpc_dictionary_set_value
+ _xpc_int64_create
- __ZNK2sd18IMSSubscriberModel22allowIMSBasedOnTTYModeEv
- __ZNK2sd18IMSSubscriberModel30isIMSAlowedBasedOnTTYMode_syncEv
CStrings:
+ "#D DCN already scheduled"
+ "#D DomesticRoamingUpdate: roaming state %s"
+ "#D EmergencyAccessNetworkInfoUpdate: Not in emergency call. Don't send emergency access network info update"
+ "#D ISIM info didn't change"
+ "#D Roaming result remains as %s"
+ "#D RoamingUpdate: Ignore undetermined roaming state %s"
+ "#D Telephony was NOT %s successfully"
+ "#D WiFiCalling-only mode: true. Baseband booted assertion required. iSimInfoReady: %s, deviceInfoReady: %s. BB booted assertion held: %s"
+ "#D fInCallImsPref is inactive!"
+ "#I RCS transport switch %s"
+ "#I RCSRegistrationState: previous state same as current, isWifi: %s"
+ "#I Submitting RCSServiceDuration metric with provisioning state: %s, registration state: %s, duration: %llu, reason: %s"
+ "EmergencyRTTSupported"
+ "NotProvisioned"
+ "NotRegistered"
+ "Provisioned"
+ "RCSServiceDuration"
+ "RTTSupported"
+ "TelephonyAnalytics service not found!"
+ "elapsed_duration"
+ "ended"
+ "provisioned_new_state"
+ "provisioned_old_state"
+ "reason"
+ "registered_new_state"
+ "registered_old_state"
+ "started"

```
