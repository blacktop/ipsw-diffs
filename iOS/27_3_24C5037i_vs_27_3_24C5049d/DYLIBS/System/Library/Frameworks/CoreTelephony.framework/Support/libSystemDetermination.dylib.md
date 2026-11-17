## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

```diff

-13504.1.0.0.0
-  __TEXT.__text: 0x7114c
-  __TEXT.__const: 0x4289
-  __TEXT.__gcc_except_tab: 0x5c20
-  __TEXT.__cstring: 0x36ea
-  __TEXT.__oslogstring: 0xa4a0
-  __TEXT.__unwind_info: 0x2860
+13508.0.0.0.0
+  __TEXT.__text: 0x7191c
+  __TEXT.__const: 0x4279
+  __TEXT.__gcc_except_tab: 0x5d08
+  __TEXT.__cstring: 0x3727
+  __TEXT.__oslogstring: 0xa30a
+  __TEXT.__unwind_info: 0x2888
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xe00
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x4cc8
+  __AUTH_CONST.__const: 0x4cd8
   __AUTH_CONST.__cfstring: 0x960
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1864
-  Symbols:   3066
-  CStrings:  1485
+  Functions: 1873
+  Symbols:   3075
+  CStrings:  1475
 
Symbols:
+ GCC_except_table103
+ GCC_except_table127
+ GCC_except_table138
+ GCC_except_table161
+ GCC_except_table172
+ GCC_except_table189
+ GCC_except_table207
+ GCC_except_table234
+ GCC_except_table252
+ GCC_except_table256
+ GCC_except_table261
+ GCC_except_table264
+ GCC_except_table273
+ GCC_except_table278
+ GCC_except_table357
+ GCC_except_table361
+ __ZN2sd17getImsPhoneNumberERKNSt3__110shared_ptrIK8RegistryEERK13PersonalityIDb15QuickSwitchRoleRKNS1_I14CSIPhoneNumberEE
+ __ZN2sd18IMSSubscriberModel21setRcsAccessTransportE15DataContextType
+ __ZN2sd23RCSSubscriberController20clearDnsRestartStateEv
+ __ZNK23GestaltUtilityInterface8isIPhoneEv
+ __ZNK2sd18IMSSubscriberModel20getAccessNetworkModeEv
+ __ZNK2sd18IMSSubscriberModel21getRcsAccessTransportEv
+ __ZNK2sd23RCSSubscriberController17recordPushArrivalEv
+ __ZNK2sd23RCSSubscriberController25recordPcscfConnectFailureEv
+ __ZNK2sd23RCSSubscriberController26shouldRestartDnsAfterRoundEv
+ __ZNK2sd23RCSSubscriberController34submitIgnoredPushSystemStateMetricEN3ims17RegistrationStateE
+ __ZNK2sd23RCSSubscriberController35sendRcsAccessNetworkInfoUpdate_syncEv
- GCC_except_table140
- GCC_except_table144
- GCC_except_table155
- GCC_except_table183
- GCC_except_table192
- GCC_except_table237
- GCC_except_table249
- GCC_except_table254
- GCC_except_table258
- GCC_except_table267
- GCC_except_table355
- GCC_except_table79
- GCC_except_table81
- GCC_except_table83
- GCC_except_table94
- _TelephonyUtilIsOversteerEnabled
- __Z8asString18RegistrationStatus
- __os_log_debug_impl
CStrings:
+ ", IsPushIgnored=false, primarynetworkinterface="
+ "5wi.ctr:: \t fRCSThrottlingRoundCount = %lu, fRoundAllConnectionErrors = %{bool}d, fDnsRestartPending = %{bool}d, fDnsRestartInFlight = %{bool}d"
+ "5wi.mdl:: \t fRcsAccessTransport: %s"
+ "New push while RCSPushSystemState metric pending; submitting previous metric"
+ "No PCSCF connected in TransientDisconnected - restarting RCS stack"
+ "PCSCF connection ready for re-registration (TransientDisconnected) over %s"
+ "PCSCF transport changed (%s -> %s): updating the access network info first"
+ "PCSCF transport changed, but the access network info could not be updated"
+ "PhoneNumber: QS secondary, using Alt number %s instead of %s"
+ "RCSDnsRestartUnchanged"
+ "RCSPushSystemStateMetric: timeout"
+ "RCSThrottlingTimer: P-CSCF DNS re-resolution did not report back. Continue with the current list"
+ "RCSThrottlingTimer: re-resolving P-CSCF DNS before the next round"
+ "RCSTransientPcscfRoundFailed"
+ "Received push while push or wakeup event in progress, state %s"
+ "Submitting RCSPushSystemState: regState=%u ignored=false storage=%{bool}d regComplete=%{bool}d msgRx=%{bool}d imdnRx=%{bool}d duration=%lld"
+ "Submitting RCSPushSystemState: regState=%u ignored=true"
+ "handlePcscfListChanged_sync: P-CSCF re-resolution returned the same list. Resume with it"
+ "none"
- ", IsPushIgnored="
- ", primarynetworkinterface="
- "Cellular footprint is not required for VoWiFi, ok to bring up IMS PDN"
- "Current DataContext is: %s. Checking CB key is not needed"
- "DCN already scheduled"
- "DomesticRoamingUpdate: roaming state %{bool}d"
- "EmergencyAccessNetworkInfoUpdate: Not in emergency call. Don't send emergency access network info update"
- "ISIM info didn't change"
- "ImsPdpActive: Lazuli mode. Country Of Origination not required"
- "ImsPdpActive: Not in iWLAN mode. Country Of Origination not required"
- "Not submitting RCSServiceDuration metric for zero duration"
- "PCSCF connection ready for re-registration (TransientDisconnected)"
- "RCSPushSystemStateMetric: 5-minute timeout"
- "Received PushURL: %{public}s"
- "Returning isCellularFootprintSeen as %{bool}d"
- "Roaming result remains as %s"
- "RoamingUpdate: Ignore undetermined roaming state %s"
- "Setting isCellularFootprintSeen to %{bool}d"
- "Skipping fLastRegisteredNetworkInfo update: no valid cell info (RAT=%s DataMode=%s regStatus=%s)"
- "Stored PushURL: %{public}s"
- "Submitting RCSPushSystemState: regState=%u ignored=%{bool}d msgRx=%{bool}d imdnRx=%{bool}d"
- "Submitting RCSPushSystemState: regState=%u ignored=%{bool}d storage=%{bool}d regComplete=%{bool}d msgRx=%{bool}d imdnRx=%{bool}d duration=%lld"
- "Submitting inline ignored RCSPushSystemState while in-flight metric pending"
- "Telephony was NOT %s successfully"
- "Updating RCSPcscfPropertyList: \n"
- "WiFiCalling-only mode: true. Baseband booted assertion required. iSimInfoReady: %{bool}d, deviceInfoReady: %{bool}d. BB booted assertion held: %{bool}d"
- "addr = %s"
- "fInCallImsPref is inactive!"
- "handleCountryOfOrigination: mcc INT is: %u"
```
