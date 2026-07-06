## CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

```diff

-  __TEXT.__text: 0x75d6b0
-  __TEXT.__auth_stubs: 0x7210
-  __TEXT.__objc_stubs: 0xba80
+  __TEXT.__text: 0x75d01c
+  __TEXT.__auth_stubs: 0x71f0
+  __TEXT.__objc_stubs: 0xbbe0
   __TEXT.__init_offsets: 0x184
-  __TEXT.__objc_methlist: 0x6cec
-  __TEXT.__const: 0x9616c
-  __TEXT.__cstring: 0x2274b
-  __TEXT.__gcc_except_tab: 0x8b37c
-  __TEXT.__oslogstring: 0x87154
+  __TEXT.__objc_methlist: 0x6d34
+  __TEXT.__const: 0x96abc
+  __TEXT.__cstring: 0x227e1
+  __TEXT.__gcc_except_tab: 0x8b1f8
+  __TEXT.__oslogstring: 0x87744
   __TEXT.__objc_classname: 0x18a2
-  __TEXT.__objc_methname: 0x11ea2
-  __TEXT.__objc_methtype: 0xe379
+  __TEXT.__objc_methname: 0x11feb
+  __TEXT.__objc_methtype: 0xe3e6
   __TEXT.__ustring: 0x3e2
-  __TEXT.__unwind_info: 0x2a410
-  __DATA_CONST.__const: 0x77918
-  __DATA_CONST.__cfstring: 0xbca0
+  __TEXT.__unwind_info: 0x2a2b0
+  __DATA_CONST.__const: 0x77950
+  __DATA_CONST.__cfstring: 0xbce0
   __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x310

   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__linkguard: 0x1b
-  __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x3920
-  __DATA_CONST.__got: 0x1d80
+  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__auth_got: 0x3910
+  __DATA_CONST.__got: 0x1ea8
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA.__objc_const: 0x8020
-  __DATA.__objc_selrefs: 0x4998
+  __DATA.__objc_const: 0x8050
+  __DATA.__objc_selrefs: 0x4a00
   __DATA.__objc_ivar: 0x354
   __DATA.__objc_data: 0x17c0
   __DATA.__data: 0x3498
-  __DATA.__bss: 0x1520
+  __DATA.__bss: 0x1518
   __DATA.__common: 0x2e0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 32773
-  Symbols:   2978
-  CStrings:  21137
+  Functions: 32769
+  Symbols:   2971
+  CStrings:  21175
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ __ZTI24TARandomizationInterface
- _CFURLCopyHostName
- __ZN10byte_order3bigclEt
- _kCTPhoneNumberRegistrationImsiKey
- _kCTPhoneNumberRegistrationMechanismKey
- _kCTPhoneNumberRegistrationResponseLabelID
- _kCTPhoneNumberRegistrationResponseStatusHTTPFailed
- _kCTPhoneNumberRegistrationResponseStatusKey
- _kCTPhoneNumberRegistrationResponseStatusSuccess
CStrings:
+ "### CallDeny: Can't dial a TTY call %{public,uuid_t}.16P during active IMS calls since TTY over IMS is disallowed"
+ "### CallDeny: Can't dial a TTY call %{public,uuid_t}.16P during existing IMS calls because TTY over IMS is not supported"
+ "### CallDeny: Can't dial a TTY call %{public,uuid_t}.16P when there is already a call"
+ "### CallDeny: Can't dial another call %{public,uuid_t}.16P when there is already a TTY call"
+ "### CallDeny: Can't dial call %{public,uuid_t}.16P because TTY over IMS is disallowed by carrier and %s is unable to make calls"
+ "### CallDeny: Can't dial call %{public,uuid_t}.16P because TTY over IMS is disallowed by carrier and we have no CS driver"
+ "### CallDeny: Can't dial call %{public,uuid_t}.16P during user entered Airplane mode"
+ "### CallDeny: Can't dial call %{public,uuid_t}.16P when baseband is offline"
+ "### CallDeny: Can't dial new MO call %{public,uuid_t}.16P. Already reached max call count. [Max: %lu, Current Calls: %lu] driver: %s"
+ "### CallDeny: Can't dial non-emergency call %{public,uuid_t}.16P during setup assistant. It's emergency calling only. Please check device setup"
+ "### CallDeny: Can't dial normal call %{public,uuid_t}.16P when there is an emergency call going on SOS PDN if carrier supports Wifi Calling"
+ "### CallDeny: QSSuppress call %{public,uuid_t}.16P"
+ "### CallDeny: SIM not usable for call %{public,uuid_t}.16P on this primary device"
+ "### CallFail: Can't dial call %{public,uuid_t}.16P with error number type"
+ "### CallFail: No preferred driver to dial call %{public,uuid_t}.16P"
+ "%s%s%s%sCanceling kickedOut request:%@"
+ "%s%s%s%sJoined enquiryID(s):%s with existing %@:-> %s"
+ "%s%s%s%sKicked out request:{%@}"
+ "%s%s%s%sKicking out existing %@ enquiryID(s):%s in favor of %@"
+ "%s%s%s%sKicking out existing %@ enquiryID(s):%s in favor of update %s"
+ "%s%shandle getAuthorizationTokens response: Event cause is %s, enquiryID(s):%s"
+ "%s%shandleGetSIMStatusResponse_sync: Event cause is %s, enquiryID(s):%s"
+ "%s%sremap '%s' -> '%s' is not possible - persona From is present!"
+ "-[CTXPCClientHandler(PNR) getPNRContext:completion:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/CallModule/CallStateModel.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/APNStorage.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/DataAPNSettings.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/DataCollocationCommon.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/DataConnectionAgent.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/DataConnectionIMS.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/DataConnectionInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/DataPDPActivator.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/DataServiceController.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/DataiRatControlleriOSBase.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/IPCU_CellProfile.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/Data/Source/IWLANDataContext.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Modules/SystemObserver/PowerObserver.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Source/Common/CSIPersistentProperties.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CSI/Source/PlatformSpecific/CSIFlatFileNvpStore.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CommCenter/Location/CTLocationBasedCountryDetermination.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CommCenter/Source/CSI/DarwinPDPConfig.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CommCenter/Source/DarwinPDPManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iqTMSA/Sources/CoreTelephony/CommCenter/Source/Startup/StartupActions.cpp"
+ "/cc/events/wifi_availability_info"
+ "13478.2"
+ "13478.2~176"
+ "BBIMSCallStatus: sub switch for normal-setup emergency redial: sending STOP on previous slot %s"
+ "CTXPCClientHandler+PNR.mm"
+ "Can't dial call %{public,uuid_t}.16P because preferred driver %s is unable to make calls"
+ "Can't dial call %{public,uuid_t}.16P with number %s over Wi-Fi"
+ "CleanUp: callsLeftOnSim size: %lu"
+ "Client [%@] (cid=%lu, rid=%lu) invoking clearVoicemailQuickSwitchDataLostStatus"
+ "Client [%@] (cid=%lu, rid=%lu) invoking getVoicemailQuickSwitchData"
+ "Could not find TAR interface for getting TA randomization preference"
+ "Could not find TAR interface for getting TA randomization support"
+ "Could not find TAR interface for setting TA randomization preference"
+ "Dialing emergency call as normal-setup emergency due to change in PLMN"
+ "Emergency TTY override: user pref enabled and operator bundle SupportsTTY=true; upgrading kTTYTypeNone -> kTTYTypeDirect"
+ "Emergency call dialed with normal setup. No need to send E911 state exit to BB."
+ "Failed to fetch VVM data after subscription established, status: %d"
+ "IMSRegChange: overriding the slot for %s from %s to kOne"
+ "ImsFeatureState: overriding the slot for %s from %s to kOne"
+ "Invalid completion handler for clearVoicemailQuickSwitchDataLostStatus"
+ "Invalid completion handler for getVoicemailQuickSwitchData"
+ "NOT QSSuppress: CB key AllowCallsOnPassiveDevice true"
+ "NOT QSSuppress: not enrolled"
+ "NOT QSSuppress: not in passive mode"
+ "Not QSSuppress MT call %{public,uuid_t}.16P: MT high priority"
+ "Not QSSuppress MT call %{public,uuid_t}.16P: slot %s not QSSuppress"
+ "SKChannel fetch failed with status: %d"
+ "SKChannel fetch returned no records — no iPhone has written a channel yet, PresenceService will not be created"
+ "SKChannel fetch succeeded: %zu record(s) returned"
+ "Save - Manatee identity lost creating zone: %@"
+ "SendBBIMSCallStatusResponse dropped: call %{public,uuid_t}.16P not found"
+ "Type:%@ enquiry=[%@], attempts:%slimited (%u), expire:%us secure-intent:%s, full-auth:%s, user-initiated:%s, Info: %@"
+ "VVM subscription established, triggering data fetch"
+ "WiFi status (default route) changed: %s -> %s"
+ "[THIS SHOULD NOT HAPPEN] SendBBIMSCallStatusResponse invalid UUID %{public,uuid_t}.16P: slot lookup fall back to UUID %{public,uuid_t}.16P"
+ "arrayByAddingObjectsFromArray:"
+ "cannot clear: %{bool}d : %{bool}d : %{bool}d : %{bool}d : %{bool}d"
+ "cannot clear: no activator"
+ "cannot detach: %{bool}d : %{bool}d : %{bool}d : %{bool}d : %{bool}d"
+ "cannot detach: by activator"
+ "cannot detach: no activator"
+ "channelClientDataUpdateHandler: channel mismatch, rolling to new channel."
+ "channelClientDataUpdateHandler: channel unchanged, no roll needed."
+ "clearVoicemailQuickSwitchDataLostStatus:"
+ "com.apple.purplebuddy"
+ "componentsJoinedByString:"
+ "detach:"
+ "didSignUpQuickSwitchPlan:secondaryIccid:secondaryEid:secondaryImei:smdp:state:planIdentifier:error:completion:"
+ "enquiryIDs"
+ "entCtrl"
+ "getActivateForEsimSetupInBuddy:"
+ "getVoicemailQuickSwitchData:"
+ "isEqualToData:"
+ "kPhoneNumberRegistrationRequestId"
+ "rdar://179859812"
+ "setActivateForEsimSetupInBuddy:"
+ "setRequestID:"
+ "setUserSelectedPlan called on macOS - not supported"
+ "subscription established for (%s)"
+ "taRandomizationSupportChanged:support:"
+ "v24@0:8@?<v@?>16"
+ "v32@0:8@\"CTServiceDescriptor\"16q24"
+ "v88@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"CTPlanIdentifier\"64@\"NSError\"72@?<v@?@\"NSError\">80"
+ "v88@0:8@16@24@32@40@48@56@64@72@?80"
+ "voicemailQuickSwitchDataChanged:"
+ "voicemailQuickSwitchDataLost"
- "### CallDeny: Can't dial a TTY call during active IMS calls since TTY over IMS is disallowed"
- "### CallDeny: Can't dial a TTY call during existing IMS calls because TTY over IMS is not supported"
- "### CallDeny: Can't dial a TTY call if there is already a call"
- "### CallDeny: Can't dial another call if there is already a TTY call"
- "### CallDeny: Can't dial any call during user entered Airplane mode"
- "### CallDeny: Can't dial any call when baseband is offline"
- "### CallDeny: Can't dial new MO call. Already reached max call count. [Max: %lu, Current Calls: %lu] driver: %s"
- "### CallDeny: Can't dial non-emergency call during setup assistant. It's emergency calling only. Please check device setup"
- "### CallDeny: Can't dial normal call when there is an emergency call going on SOS PDN if carrier supports Wifi Calling"
- "### CallDeny: SIM not usable for this primary device"
- "### CallFail: Can't dial call with error number type"
- "### CallFail: No preferred driver to dial"
- "%s%s%s%sRemoving the existing %@"
- "%s%s%s%sRemoving the existing %s"
- "%s%sAdding HTTP header for PNR signature version %s"
- "%s%sFailed to create PNR notification dictionary"
- "%s%sFailed to get PNR Notification interface."
- "%s%sIssuing PNR Response received"
- "%s%sNo driver for task %s while processing getPhoneNumber response"
- "%s%sPNR response with empty phone number"
- "%s%sPNR response with empty signature"
- "%s%sgiving out the ONLY existing label %{public}@ as a replacement for unknown %{public}@"
- "%s%shandle getAuthorizationTokens response: Event cause is %s"
- "%s%shandleGetSIMStatusResponse_sync: Event cause is %s, EnquiryID:%llu"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.waPAE4/Sources/CoreTelephony/CSI/Modules/CallModule/CallStateModel.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.waPAE4/Sources/CoreTelephony/CSI/Modules/Data/Source/APNStorage.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.waPAE4/Sources/CoreTelephony/CSI/Modules/Data/Source/DataAPNSettings.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.waPAE4/Sources/CoreTelephony/CSI/Modules/Data/Source/DataCollocationCommon.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.waPAE4/Sources/CoreTelephony/CSI/Modules/Data/Source/DataConnectionAgent.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.waPAE4/Sources/CoreTelephony/CSI/Modules/Data/Source/DataConnectionIMS.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.waPAE4/Sources/CoreTelephony/CSI/Modules/Data/Source/DataConnectionInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.waPAE4/Sources/CoreTelephony/CSI/Modules/Data/Source/DataPDPActivator.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.waPAE4/Sources/CoreTelephony/CSI/Modules/Data/Source/DataServiceController.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.waPAE4/Sources/CoreTelephony/CSI/Modules/Data/Source/DataiRatControlleriOSBase.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.waPAE4/Sources/CoreTelephony/CSI/Modules/Data/Source/IPCU_CellProfile.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.waPAE4/Sources/CoreTelephony/CSI/Modules/Data/Source/IWLANDataContext.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.waPAE4/Sources/CoreTelephony/CSI/Modules/SystemObserver/PowerObserver.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.waPAE4/Sources/CoreTelephony/CSI/Source/Common/CSIPersistentProperties.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.waPAE4/Sources/CoreTelephony/CSI/Source/PlatformSpecific/CSIFlatFileNvpStore.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.waPAE4/Sources/CoreTelephony/CommCenter/Location/CTLocationBasedCountryDetermination.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.waPAE4/Sources/CoreTelephony/CommCenter/Source/CSI/DarwinPDPConfig.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.waPAE4/Sources/CoreTelephony/CommCenter/Source/DarwinPDPManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.waPAE4/Sources/CoreTelephony/CommCenter/Source/Startup/StartupActions.cpp"
- "13473.1"
- "13473.1~84"
- "Can't dial because preferred driver %s is unable to make calls"
- "Can't dial new MO call"
- "Can't dial number %s over Wi-Fi"
- "Carrier Entitlement Controller not available for slot %s"
- "CleanUp: currentCallsOnSim size: %lu"
- "CleanUp: the last CS call on sim"
- "CleanUp: the last IMS call on sim"
- "Client [%@] (cid=%lu, rid=%lu) invoking getDeviceState: bundleID=%@ (audit token)"
- "Could not find baseband settings interface for getting TA randomization preference"
- "Could not find baseband settings interface for getting TA randomization support"
- "Could not find baseband settings interface for setting TA randomization preference"
- "Dialing emergency call as normal due to change in PLMN"
- "Emergency call dialed with normal setup. No need to send E911 state exit."
- "Not QSSuppress %{public,uuid_t}.16P: MT call marked high priority"
- "Not QSSuppress %{public,uuid_t}.16P: QSMode is %s"
- "Not QSSuppress %{public,uuid_t}.16P: carrier supports AllowCallsOnPassiveDevice"
- "Not QSSuppress %{public,uuid_t}.16P: not enrolled on slot %s"
- "SendBBIMSCallStatusResponse dropped: Null call"
- "SendBBIMSCallStatusResponse dropped: have more than one call"
- "Sending reply for request (cid=%lu, rid=%lu): getDeviceState: result=%ld, error=%@"
- "Type:%@ %llu, attempts:%slimited (%u), expire:%us secure-intent:%s, full-auth:%s, user-initiated:%s, Info: %@"
- "abortAll: "
- "clear parameters: %{bool}d : %{bool}d : %{bool}d : %{bool}d : %{bool}d"
- "detach parameters: %{bool}d : %{bool}d : %{bool}d : %{bool}d : %{bool}d"
- "detach parameters: no activator"
- "didSignUpQuickSwitchPlan:secondaryIccid:secondaryEid:secondaryImei:smdp:state:error:completion:"
- "getDeviceStateWithCompletion:"
- "kCTEventIndicatorPhoneNumberRegistrationNotification"
- "no activator"
- "v80@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSError\"64@?<v@?@\"NSError\">72"

```
