## libSystemDetermination.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libSystemDetermination.dylib`

```diff

-12227.1.2.0.0
-  __TEXT.__text: 0x525b0
-  __TEXT.__auth_stubs: 0x1050
-  __TEXT.__gcc_except_tab: 0x3e54
-  __TEXT.__const: 0x2257
-  __TEXT.__cstring: 0x242e
-  __TEXT.__oslogstring: 0x751a
-  __TEXT.__unwind_info: 0x18f8
-  __DATA_CONST.__got: 0x1d8
+12320.0.0.0.0
+  __TEXT.__text: 0x542d4
+  __TEXT.__auth_stubs: 0x1080
+  __TEXT.__const: 0x2487
+  __TEXT.__gcc_except_tab: 0x41b8
+  __TEXT.__cstring: 0x24ea
+  __TEXT.__oslogstring: 0x7884
+  __TEXT.__unwind_info: 0x1980
+  __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0xcc8
-  __AUTH_CONST.__auth_got: 0x830
-  __AUTH_CONST.__const: 0x2a50
-  __AUTH_CONST.__cfstring: 0x740
+  __AUTH_CONST.__auth_got: 0x848
+  __AUTH_CONST.__const: 0x2b48
+  __AUTH_CONST.__cfstring: 0x7c0
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
+  Symbols:   1586
+  CStrings:  1152
 
Symbols:
+ _TelephonyUtilIsOversteerEnabled
+ __ZN16CSIPacketAddressaSERKS_
+ __ZN2sd18IMSSubscriberModel15updatePcscfListERKNSt3__16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEERKS8_
+ __ZN2sd23IMSSubscriberController20onRCSWatchdogTimeoutEv
+ __ZN2sd23IMSSubscriberController21abortRCSWatchdogTimerEv
+ __ZN2sd23IMSSubscriberController21startRCSWatchdogTimerEv
+ __ZN2sd23IMSSubscriberController27handlePcscfListChanged_syncERKNSt3__16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE15DataContextTypeRKS8_
+ __ZNK2sd18IMSSubscriberModel10isUsingTlsEv
+ __ZNK2sd18IMSSubscriberModel20isQualifiedToProceedEv
+ __ZNK2sd18IMSSubscriberModel31isIMSAllowedBasedOnTTYMode_syncEb
+ __ZNK2sd19IMSSubscriberConfig15getRTTSupportedEb
+ __ZNK2sd19IMSSubscriberConfig24getEmergencyRTTSupportedEb
+ __ZNK2sd19IMSSubscriberConfig26getRCSWatchdogTimeoutValueEv
+ __ZNK2sd23IMSSubscriberController10isUsingTlsEv
+ __ZNK2sd23IMSSubscriberController20triggerABCForRCSIdleEv
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ __ZThn48_N2sd23IMSSubscriberController27handlePcscfListChanged_syncERKNSt3__16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE15DataContextTypeRKS8_
+ __ZThn48_NK2sd23IMSSubscriberController10isUsingTlsEv
+ __os_log_debug_impl
+ _memchr
- __ZN2sd18IMSSubscriberModel15updatePcscfListERKNSt3__16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEERKS8_jj
- __ZN2sd23IMSSubscriberController27handlePcscfListChanged_syncERKNSt3__16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE15DataContextTypeRKS8_jj
- __ZNK2sd18IMSSubscriberModel12getPcscfPortEv
- __ZNK2sd18IMSSubscriberModel22allowIMSBasedOnTTYModeEv
- __ZNK2sd18IMSSubscriberModel30isIMSAlowedBasedOnTTYMode_syncEv
- __ZNKSt9exception4whatEv
- __ZNSt9exceptionD2Ev
- __ZTISt9exception
- __ZThn48_N2sd23IMSSubscriberController27handlePcscfListChanged_syncERKNSt3__16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE15DataContextTypeRKS8_jj
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
+ "#I 5wi.mdl:: \t fUEInfo: [[IsimInfo: fIsPresent = %s, fIsAllFilesRead = %s, fImpi = %s, fImpuList = %s, fDomain = %s, fPcscfList = %s, fPcscfDomain = %s], [fDeviceInfo: fImsi = %s, fMdn = %s, fIsSimPersonality = %s, fDeviceId = %s, fDeviceSVN = %s, fMcc = %s, fMnc = %s, fUSimPresent = %s]]"
+ "#I ABC report %s for Lazuli not registered"
+ "#I Generating RCS Idle ABC report"
+ "#I IMS Registration Info: Carrier-Based: %s, AuthType: %s"
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
+ "RCSWatchdogTimeoutSeconds"
+ "RCS_Watchdog"
+ "RTTSupported"
+ "WaitForRingingTimerMOSeconds"
+ "success"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}8@?0"
- "#I 5wi.ctr:: \t fMaskUpDesired = %s, fMaskUpDesiredMask = %s, fPendingImsSwitchStatusNotification = %s, fPendingPcscfChangeUpdateDueToActiveCall = %s, fPendingPcscfChangeUpdateDueToContextMismatch = %s, fPendingSubscriptionChangeNotification = %s, fLimitedModeRegistrationRequested = %s, fUnprovisionedRegistrationRequested = %s, fSendImsStatusToBaseband = %s, fSendImsStatusToBasebandWithConnectivityCheck = %s, fPendingSimFilesUpdate = %s"
- "#I 5wi.mdl:: \t fUEInfo: [[IsimInfo: fIsPresent = %s, fIsAllFilesRead = %s, fImpi = %s, fImpuList = %s, fDomain = %s, fPcscfList = %s, fPcscfDomain = %s, fPcscfPort = %u], [fDeviceInfo: fImsi = %s, fMdn = %s, fIsSimPersonality = %s, fDeviceId = %s, fDeviceSVN = %s, fMcc = %s, fMnc = %s, fUSimPresent = %s]]"
- "#I IMS Registration Info: Carrier-Based: %s"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}8@?0"

```
