## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

```diff

-12227.1.1.0.0
-  __TEXT.__text: 0x525b0
+12317.2.0.0.0
+  __TEXT.__text: 0x54134
   __TEXT.__auth_stubs: 0x1050
-  __TEXT.__gcc_except_tab: 0x3e54
-  __TEXT.__const: 0x2257
-  __TEXT.__cstring: 0x242e
-  __TEXT.__oslogstring: 0x751a
-  __TEXT.__unwind_info: 0x18f8
-  __DATA_CONST.__got: 0x1d8
+  __TEXT.__const: 0x2487
+  __TEXT.__gcc_except_tab: 0x41c0
+  __TEXT.__cstring: 0x2525
+  __TEXT.__oslogstring: 0x78c2
+  __TEXT.__unwind_info: 0x1988
+  __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0xcc8
   __AUTH_CONST.__auth_got: 0x830
-  __AUTH_CONST.__const: 0x2a50
-  __AUTH_CONST.__cfstring: 0x740
+  __AUTH_CONST.__const: 0x2b40
+  __AUTH_CONST.__cfstring: 0x800
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 1143
-  Symbols:   1567
-  CStrings:  1125
+  Functions: 1155
+  Symbols:   1583
+  CStrings:  1155
 
Symbols:
+ __ZN2sd23IMSSubscriberController20onRCSWatchdogTimeoutEv
+ __ZN2sd23IMSSubscriberController21abortRCSWatchdogTimerEv
+ __ZN2sd23IMSSubscriberController21startRCSWatchdogTimerEv
+ __ZNK2sd18IMSSubscriberModel20isQualifiedToProceedEv
+ __ZNK2sd18IMSSubscriberModel31isIMSAllowedBasedOnTTYMode_syncEb
+ __ZNK2sd19IMSSubscriberConfig15getRTTSupportedEv
+ __ZNK2sd19IMSSubscriberConfig24getEmergencyRTTSupportedEv
+ __ZNK2sd19IMSSubscriberConfig26getRCSWatchdogTimeoutValueEv
+ __ZNK2sd19IMSSubscriberConfig30getRcsPinnedCertificateDigestsEv
+ __ZNK2sd23IMSSubscriberController20triggerABCForRCSIdleEv
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ __os_log_debug_impl
- __ZNK2sd18IMSSubscriberModel22allowIMSBasedOnTTYModeEv
- __ZNK2sd18IMSSubscriberModel30isIMSAlowedBasedOnTTYMode_syncEv
- __ZNKSt9exception4whatEv
- __ZNSt9exceptionD2Ev
- __ZTISt9exception
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
+ "#I 5wi.ctr:: \t fMaskUpDesired = %s, fMaskUpDesiredMask = %s, fPendingImsSwitchStatusNotification = %s, fPendingPcscfChangeUpdateDueToActiveCall = %s, fPendingPcscfChangeUpdateDueToContextMismatch = %s, fPendingSubscriptionChangeNotification = %s, fLimitedModeRegistrationRequested = %s, fUnprovisionedRegistrationRequested = %s, fSendImsStatusToBaseband = %s, fSendImsStatusToBasebandWithConnectivityCheck = %s, fPendingSimFilesUpdate = %s, fPendingReprovisionRequest = %s"
+ "#I 5wi.ctr:: \t fRCSWatchdogCount = %lu"
+ "#I ABC report %s for Lazuli not registered"
+ "#I Generating RCS Idle ABC report"
+ "#I IMS Registration Info: Carrier-Based: %s, AuthType: %s"
+ "#I RCS Pinned certificate digests %{public}@"
+ "#I RCSWatchdogTimeoutSeconds=%u"
+ "#I RCSWatchdogTimer: Aborting RCS_Watchdog timer"
+ "#I RCSWatchdogTimer: Starting RCS_Watchdog timer: %u seconds"
+ "#I WiFiAvailable: IMS registration ongoing, do not interrupt"
+ "#N RCSWatchdogTimer: expired."
+ "AttestationPrivateKey"
+ "AuthType"
+ "EmergencyRTTSupported"
+ "Lazuli not registered for extended period"
+ "LazuliNotRegistered"
+ "PinnedCertificateDigests"
+ "RCSWatchdogTimeoutSeconds"
+ "RCS_Watchdog"
+ "RTTSupported"
+ "RcsCertificatePublicKeyDigestList"
+ "WaitForRingingTimerMOSeconds"
+ "success"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}8@?0"
- "#I 5wi.ctr:: \t fMaskUpDesired = %s, fMaskUpDesiredMask = %s, fPendingImsSwitchStatusNotification = %s, fPendingPcscfChangeUpdateDueToActiveCall = %s, fPendingPcscfChangeUpdateDueToContextMismatch = %s, fPendingSubscriptionChangeNotification = %s, fLimitedModeRegistrationRequested = %s, fUnprovisionedRegistrationRequested = %s, fSendImsStatusToBaseband = %s, fSendImsStatusToBasebandWithConnectivityCheck = %s, fPendingSimFilesUpdate = %s"
- "#I IMS Registration Info: Carrier-Based: %s"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}8@?0"

```
