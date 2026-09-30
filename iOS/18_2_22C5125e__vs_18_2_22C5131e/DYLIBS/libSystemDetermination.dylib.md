## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

```diff

-12212.4.0.0.0
-  __TEXT.__text: 0x525c8
-  __TEXT.__auth_stubs: 0x1060
-  __TEXT.__gcc_except_tab: 0x3e44
+12213.3.0.0.0
+  __TEXT.__text: 0x525b0
+  __TEXT.__auth_stubs: 0x1050
+  __TEXT.__gcc_except_tab: 0x3e54
   __TEXT.__const: 0x2257
   __TEXT.__cstring: 0x242e
-  __TEXT.__oslogstring: 0x75fc
-  __TEXT.__unwind_info: 0x18f0
+  __TEXT.__oslogstring: 0x751a
+  __TEXT.__unwind_info: 0x18f8
   __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__const: 0xcc8
-  __AUTH_CONST.__auth_got: 0x838
-  __AUTH_CONST.__const: 0x2a20
+  __AUTH_CONST.__auth_got: 0x830
+  __AUTH_CONST.__const: 0x2a50
   __AUTH_CONST.__cfstring: 0x740
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x60

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 1140
-  Symbols:   1565
-  CStrings:  1131
+  Functions: 1143
+  Symbols:   1567
+  CStrings:  1125
 
Symbols:
+ __ZN2sd23IMSSubscriberController24setPendingSimFilesUpdateEb
+ __ZNK2sd23IMSSubscriberController23isPendingSimFilesUpdateEv
- __os_log_debug_impl
CStrings:
+ "#I 5wi.ctr:: \t fMaskUpDesired = %!s(MISSING), fMaskUpDesiredMask = %!s(MISSING), fPendingImsSwitchStatusNotification = %!s(MISSING), fPendingPcscfChangeUpdateDueToActiveCall = %!s(MISSING), fPendingPcscfChangeUpdateDueToContextMismatch = %!s(MISSING), fPendingSubscriptionChangeNotification = %!s(MISSING), fLimitedModeRegistrationRequested = %!s(MISSING), fUnprovisionedRegistrationRequested = %!s(MISSING), fSendImsStatusToBaseband = %!s(MISSING), fSendImsStatusToBasebandWithConnectivityCheck = %!s(MISSING), fPendingSimFilesUpdate = %!s(MISSING)"
+ "#N LazuliControllerShutdown: controller was re-enabled during shutdown - restarting, accountId=%!s(MISSING)"
+ "#N LazuliInfoReady: controller is shutting down - defer restart, accountId=%!s(MISSING)"
+ "#N PcscfList: Ignoring Proxy update while the stack is disabled"
- "#D DCN already scheduled"
- "#D DomesticRoamingUpdate: roaming state %!s(MISSING)"
- "#D EmergencyAccessNetworkInfoUpdate: Not in emergency call. Don't send emergency access network info update"
- "#D ISIM info didn't change"
- "#D Roaming result remains as %!s(MISSING)"
- "#D RoamingUpdate: Ignore undetermined roaming state %!s(MISSING)"
- "#D Telephony was NOT %!s(MISSING) successfully"
- "#D WiFiCalling-only mode: true. Baseband booted assertion required. iSimInfoReady: %!s(MISSING), deviceInfoReady: %!s(MISSING). BB booted assertion held: %!s(MISSING)"
- "#D fInCallImsPref is inactive!"
- "#I 5wi.ctr:: \t fMaskUpDesired = %!s(MISSING), fMaskUpDesiredMask = %!s(MISSING), fPendingImsSwitchStatusNotification = %!s(MISSING), fPendingPcscfChangeUpdateDueToActiveCall = %!s(MISSING), fPendingPcscfChangeUpdateDueToContextMismatch = %!s(MISSING), fPendingSubscriptionChangeNotification = %!s(MISSING), fLimitedModeRegistrationRequested = %!s(MISSING), fUnprovisionedRegistrationRequested = %!s(MISSING), fSendImsStatusToBaseband = %!s(MISSING), fSendImsStatusToBasebandWithConnectivityCheck = %!s(MISSING)"

```
