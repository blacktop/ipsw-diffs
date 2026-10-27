## CommCenter

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CommCenter`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__linkguard`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-13487.1.0.0.0
-  __TEXT.__text: 0x74185c
-  __TEXT.__auth_stubs: 0x7200
-  __TEXT.__objc_stubs: 0xbb80
+13499.0.0.0.0
+  __TEXT.__text: 0x742de0
+  __TEXT.__auth_stubs: 0x7280
+  __TEXT.__objc_stubs: 0xbd40
   __TEXT.__init_offsets: 0x184
-  __TEXT.__objc_methlist: 0x6d1c
-  __TEXT.__const: 0x9665c
-  __TEXT.__cstring: 0x21c23
-  __TEXT.__gcc_except_tab: 0x8ac10
-  __TEXT.__oslogstring: 0x820dd
-  __TEXT.__objc_classname: 0x18a2
-  __TEXT.__objc_methname: 0x11fe2
-  __TEXT.__objc_methtype: 0xe377
+  __TEXT.__objc_methlist: 0x6d5c
+  __TEXT.__const: 0x9659c
+  __TEXT.__cstring: 0x21cc5
+  __TEXT.__gcc_except_tab: 0x8ad60
+  __TEXT.__oslogstring: 0x8265a
+  __TEXT.__objc_classname: 0x18c4
+  __TEXT.__objc_methname: 0x1212c
+  __TEXT.__objc_methtype: 0xe3c0
   __TEXT.__ustring: 0x3e2
-  __TEXT.__info_plist: 0x645
-  __TEXT.__unwind_info: 0x2d388
-  __DATA_CONST.__const: 0x77a38
-  __DATA_CONST.__cfstring: 0xbca0
+  __TEXT.__info_plist: 0x643
+  __TEXT.__unwind_info: 0x2d3b8
+  __DATA_CONST.__const: 0x77b20
+  __DATA_CONST.__cfstring: 0xbd40
   __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_catlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x310
+  __DATA_CONST.__objc_protolist: 0x318
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x120

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__linkguard: 0x1b
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA_CONST.__auth_got: 0x3918
+  __DATA_CONST.__auth_got: 0x3958
   __DATA_CONST.__got: 0x1e88
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA.__objc_const: 0x8040
-  __DATA.__objc_selrefs: 0x49e0
+  __DATA.__objc_const: 0x8070
+  __DATA.__objc_selrefs: 0x4a58
   __DATA.__objc_ivar: 0x354
   __DATA.__objc_data: 0x17c0
-  __DATA.__data: 0x3508
-  __DATA.__bss: 0x14b0
+  __DATA.__data: 0x3568
+  __DATA.__bss: 0x14b8
   __DATA.__common: 0x2e0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 32822
-  Symbols:   2967
-  CStrings:  19048
+  Functions: 32841
+  Symbols:   2976
+  CStrings:  19090
 
Symbols:
+ __ZN12capabilities2ct13supportsVoLTEEv
+ __ZN12capabilities2ct22supportsPrivateNetworkEv
+ __ZN12capabilities2ct22supportsSecurityStatusEv
+ __ZN12capabilities2ct24supportsCMASCampOnlyModeEv
+ __ZN12capabilities2ct25requiresIMSFeatureMaskingEv
+ __ZN12capabilities2ct27supportsEmptyNITZIndicationEv
+ __ZN12capabilities2ct30supportsGPSVisibilityReportingEv
+ __ZN12capabilities2ct31supportsCellNetworkSearchGeoMCCEv
+ __ZN12capabilities2ct33supportsRRCRejectionCodeReportingEv
+ __ZN12capabilities2ct34supportsSystemSelectionDataRoamingEv
+ __ZN12capabilities2ct37supportsOnlineModeDueToUserPowerCycleEv
+ __ZN12registration16write_rest_valueERKNS_19RatSelectionRequestE
+ __ZN2sd19IMSSubscriberConfig6createERKNSt3__110shared_ptrIK8RegistryEERKNS2_IK15PersonalityInfoEERKNS2_INS_37IMSSubscriberPersonalityBoundInstanceEEEN8dispatch5queueE
+ __ZN3ctu12TimerService13systemTimeNowEv
- __ZN2sd19IMSSubscriberConfig6createERKNSt3__110shared_ptrIK8RegistryEERKNS2_IK15PersonalityInfoEERKNS2_INS_37IMSSubscriberPersonalityBoundInstanceEEE
- __ZNK16RatSelectionType10getSimSlotEv
- __ZNK16RatSelectionType12getSelectionEv
- __ZNK16RatSelectionType13getIsInternalEv
- __ZNK16RatSelectionType21getPreferredSelectionEv
CStrings:
+ "/cc/events/lazuli_push_credentials_watchdog_interval_override"
+ "13499"
+ "13499~164"
+ "BMP height %d out of allowed range (1..%d)"
+ "BMP width %d out of allowed range (1..%d)"
+ "Branded image exceeds maximum allowed size: %lu bytes (limit %lu)"
+ "CTXPCServiceAppMigrationInterface"
+ "NWAgent %{uuid_t}.16P created"
+ "Not QSSuppress MT call %{public,uuid_t}.16P: slot %s has %lu ongoing call(s)"
+ "Sending CTM for TTY call: %{bool}d, RTT is not supported"
+ "Sending reply for request (cid=%lu, rid=%lu): decodeSuggestionsBase64: count=%lu, suggestions=%{sensitive}@"
+ "Sending reply for request (cid=%lu, rid=%lu): decodeSuggestionsBase64: error=%@"
+ "Sending reply for request (cid=%lu, rid=%lu): decodeSuggestionsBase64: result=nil"
+ "Sending reply for request (cid=%lu, rid=%lu): readCachedChatBotRenderInformation: cacheType=%ld"
+ "Sending reply for request (cid=%lu, rid=%lu): readCachedChatBotRenderInformation: cacheType=%ld, verification=%@, welcome=%{sensitive}@, botInfo=%@"
+ "Sending reply for request (cid=%lu, rid=%lu): readCachedChatBotRenderInformation: error=%@"
+ "Sending reply for request (cid=%lu, rid=%lu): readCachedChatBotRenderInformation: result=nil"
+ "ShowCallWaitingOnPassiveDeviceOneCallLeg"
+ "ShowCallWaitingOnPassiveDeviceOneCallLeg %{bool}d"
+ "URL is not a well-formed https URL"
+ "Unsupported BMP DIB header size %u"
+ "_handoffCurrentReplyToQueue:block:"
+ "botInfo"
+ "cacheType"
+ "caseInsensitiveCompare:"
+ "chipList"
+ "componentsWithURL:resolvingAgainstBaseURL:"
+ "doUpdateInterface: NWAgent %{uuid_t}.16P: interface changed from %s to %s"
+ "getQuickSwitchModeIfRegisteredForStateEvents called on macOS - not supported"
+ "handoffCurrentReplyToQueue:block:"
+ "http://"
+ "https"
+ "interfaceMatch:"
+ "interfaceMatch: NWAgent: fInterfaceObserver is empty"
+ "intervalSeconds"
+ "lowercaseString"
+ "migrateAppDataFromBundleID:toBundleID:completion:"
+ "migrateBundleID called on macOS - not supported"
+ "notifyConnectionState: Not posting external event because the context state %d is different from the connection state %d"
+ "notifyConnectionState: Not posting pdpContextStateChange event since transport does not match the interface: %s"
+ "pathSatisfied check: NWAgent %{uuid_t}.16P Observe: agentPath description=[%{public}@]: pathPath description=[%{public}@]"
+ "rcs::pushCredWatchdogInterval"
+ "rcs::pushCredWatchdogInterval command invoked"
+ "renderInformation"
+ "scheme"
+ "stringByAppendingString:"
+ "v32@0:8^{dispatch_queue_s=}16@?24"
+ "v32@0:8^{dispatch_queue_s=}16@?<v@?>24"
+ "verificationDetails"
+ "welcomeMessage"
- "13487.1"
- "13487.1~121"
- "Sending CTM for TTY call: %{bool}d, RTT supported: %{bool}d"
- "Sending reply for request (cid=%lu, rid=%lu): decodeSuggestionsBase64: error=%@, result=%@"
- "Sending reply for request (cid=%lu, rid=%lu): readCachedChatBotRenderInformation: result=%@, error=%@"
- "notifyConnectionState: We are not posting external event because the context state %d is different from the connection state %d"
- "preferred"
- "selection"
```
