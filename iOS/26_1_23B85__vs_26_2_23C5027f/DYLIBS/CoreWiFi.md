## CoreWiFi

> `/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`

```diff

-985.22.0.0.0
-  __TEXT.__text: 0x1ac0c4
+988.8.0.0.0
+  __TEXT.__text: 0x1affb8
   __TEXT.__auth_stubs: 0x1ad0
-  __TEXT.__objc_methlist: 0x10554
+  __TEXT.__objc_methlist: 0x107dc
   __TEXT.__const: 0x2f08
   __TEXT.__dlopen_cstrs: 0x966
   __TEXT.__swift5_typeref: 0x7e5

   __TEXT.__swift5_fieldmd: 0x6a0
   __TEXT.__swift5_proto: 0x270
   __TEXT.__swift5_types: 0xac
-  __TEXT.__cstring: 0x1de93
-  __TEXT.__gcc_except_tab: 0x7898
-  __TEXT.__oslogstring: 0x1adb0
+  __TEXT.__cstring: 0x1e119
+  __TEXT.__gcc_except_tab: 0x7a9c
+  __TEXT.__oslogstring: 0x1b5d0
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x54e0
+  __TEXT.__unwind_info: 0x5560
   __TEXT.__eh_frame: 0x570
-  __TEXT.__objc_classname: 0xfb4
-  __TEXT.__objc_methname: 0x26d9a
-  __TEXT.__objc_methtype: 0x382b
-  __TEXT.__objc_stubs: 0x1bdc0
-  __DATA_CONST.__got: 0x910
-  __DATA_CONST.__const: 0x5018
+  __TEXT.__objc_classname: 0xfb1
+  __TEXT.__objc_methname: 0x278e2
+  __TEXT.__objc_methtype: 0x3934
+  __TEXT.__objc_stubs: 0x1c3c0
+  __DATA_CONST.__got: 0x918
+  __DATA_CONST.__const: 0x50c0
   __DATA_CONST.__objc_classlist: 0x3a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x81a0
+  __DATA_CONST.__objc_selrefs: 0x8308
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x338
-  __DATA_CONST.__objc_arraydata: 0x19f8
+  __DATA_CONST.__objc_arraydata: 0x1a00
   __AUTH_CONST.__auth_got: 0xd78
   __AUTH_CONST.__const: 0x32d0
-  __AUTH_CONST.__cfstring: 0x18140
-  __AUTH_CONST.__objc_const: 0x15640
+  __AUTH_CONST.__cfstring: 0x18340
+  __AUTH_CONST.__objc_const: 0x158b8
   __AUTH_CONST.__objc_arrayobj: 0x450
-  __AUTH_CONST.__objc_intobj: 0x37f8
+  __AUTH_CONST.__objc_intobj: 0x3828
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH.__objc_data: 0xe58
   __AUTH.__data: 0x320
-  __DATA.__objc_ivar: 0x122c
+  __DATA.__objc_ivar: 0x1258
   __DATA.__data: 0x1700
   __DATA.__bss: 0x4fa0
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x7c
+  __DATA_DIRTY.__objc_ivar: 0x80
   __DATA_DIRTY.__objc_data: 0x1568
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x298

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 787EB0A9-4664-3471-BFC0-2776FD56E973
-  Functions: 7469
-  Symbols:   1080
-  CStrings:  14943
+  UUID: 77C9F634-26C6-38E0-A1B2-9E4D03E19F5F
+  Functions: 7540
+  Symbols:   1082
+  CStrings:  15075
 
Symbols:
+ _CWFXPCWiFiNetworkSharingBundleIDKey
+ _kTCCServiceAccessoryWiFiNetworkSharing
CStrings:
+ "(mostRecentlyShared=%@, firstShared=%@, lastModified=%@, ack=[shared=%lu, modified=%lu], askToShareStatus=%@ (%@), waitingForAssoc=%d)"
+ "-[CWFHotspotClientManager clientAssociatedToHostPersonalHotspot:]"
+ "@32@0:8@16^B24"
+ "B32@0:8@16B24B28"
+ "B48@0:8@16@24Q32B40B44"
+ "RESET WIFI NETWORK SHARING"
+ "SSID change event"
+ "T@\"CWFWiFiNetworkSharingClientID\",C,V_askToShareProxCardClientID"
+ "T@\"CWFWiFiNetworkSharingClientID\",C,V_authorizationProxCardClientID"
+ "T@?,C,V_cancelAskToShareProxCardHandler"
+ "T@?,C,V_cancelAskToShareUserNotificationHandler"
+ "T@?,C,V_cancelAuthorizationProxCardHandler"
+ "T@?,C,V_cancelWiFiNetworkSharingAskToShareProxCardHandler"
+ "T@?,C,V_cancelWiFiNetworkSharingAskToShareUserNotificationHandler"
+ "T@?,C,V_cancelWiFiNetworkSharingAuthorizationProxCardHandler"
+ "TB,N,V_mfpc"
+ "TQ,V_acknowledgedNetworksListUpdateCounterWhenModified"
+ "TQ,V_acknowledgedNetworksListUpdateCounterWhenShared"
+ "Tq,N,V_h2eonly"
+ "Tq,N,V_transitiondisabledflags"
+ "WiFiNetworkSharingBundleIDKey"
+ "[OTA_SET] %s:  --- Received asset discovered notification --- "
+ "[OTA_SET] %s:  --- Received asset download notification --- "
+ "[corewifi-PH] %{public}s (%{public}s:%u) %s NULL macAddress. Returning."
+ "[corewifi] [wifi-network-sharing] Authorization level has already been configured, will return current auth level (clientID=%{public}@, authLevel=%lu)"
+ "[corewifi] [wifi-network-sharing] Canceling ask-to-share proxcard (clientID=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Canceling ask-to-share user notification (clientID=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Canceling authorization proxcard (clientID=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Checking for authorization level change (clientID=%{public}@, authLevel=%lu, cachedAuthLevel=%lu)"
+ "[corewifi] [wifi-network-sharing] Current network is ask-to-share eligible for clientID (clientID=%{public}@, metadata=%{public}@, authLevel=%lu, knownNetwork=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Launch interaction completed (device=%{public}@, clientID=%{public}@, error=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Presented ask-to-share banner has matching clientID, dismissing (clientID=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Presented ask-to-share proxcard has matching clientID, dismissing (clientID=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Presented authorization proxcard has matching clientID, dismissing (clientID=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Received ask-to-share proxcard response (clientID=%{public}@, error=%{public}@, status=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Received authorization proxcard response (clientID=%{public}@, error=%{public}@, authLevel=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Received request to dismiss ask-to-share banner (clientID=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Received request to dismiss ask-to-share proxcard (clientID=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Received request to dismiss authorization proxcard (clientID=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Removed all database entries"
+ "[corewifi] [wifi-network-sharing] Removed database entries matching %{public}@/*"
+ "[corewifi] [wifi-network-sharing] Removed database entry matching %{public}@/%{public}@"
+ "[corewifi] [wifi-network-sharing] Removed database entry matching */%{public}@ (bundleID=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Removing ask-to-share notification (error=%{public}@, status=%lu, reason=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Resetting database for %{public}@/%{public}@"
+ "[corewifi] [wifi-network-sharing] Triggering ask-to-share proxcard (clientID=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Triggering authorization proxcard (clientID=%{public}@)"
+ "[corewifi] [wifi-network-sharing] Updated DB with per-network update acknowledgement counter (clientID=%{public}@, counter=%lu, network=%{public}@, metadata=%{public}@)"
+ "__addAskToShareFromAppTimestampWithClientID:"
+ "__addAskToShareFromAppexTimestampWithClientID:networkID:"
+ "__addAuthorizationTimestampWithClientID:"
+ "__askToShareNetworkForCurrentNetworkWithClientID:onDemand:forNetworkEvent:"
+ "__authorizationLevelForClientID:isAuthorizedForDeviceAccess:"
+ "__canAskToShareCurrentNetworkForClientID:onDemand:forNetworkEvent:"
+ "__canAskToShareKnownNetwork:metadata:authorizationStatus:onDemand:forNetworkEvent:"
+ "__cancelAskToShareProxCardForClientID:"
+ "__cancelAskToShareUserNotificationForClientID:"
+ "__cancelAuthorizationProxCardForClientID:"
+ "__presentAskToShareUserNotificationForClientID:network:accessoryName:"
+ "__removeAskToShareNotificationWithError:status:debugReason:"
+ "__removeMostRecentTimestampForAskToShareFromAppexWithClientID:networkID:"
+ "__resetWiFiNetworkSharing:"
+ "__sendNetworkListUpdateEventForClientID:force:"
+ "_acknowledgedNetworksListUpdateCounterWhenModified"
+ "_acknowledgedNetworksListUpdateCounterWhenShared"
+ "_askToShareProxCardClientID"
+ "_authorizationProxCardClientID"
+ "_cancelAskToShareProxCardHandler"
+ "_cancelAskToShareUserNotificationHandler"
+ "_cancelAuthorizationProxCardHandler"
+ "_cancelWiFiNetworkSharingAskToShareProxCardHandler"
+ "_cancelWiFiNetworkSharingAskToShareUserNotificationHandler"
+ "_cancelWiFiNetworkSharingAuthorizationProxCardHandler"
+ "_h2eonly"
+ "_mfpc"
+ "_transitiondisabledflags"
+ "accessoryServicesMap"
+ "acknowledgedNetworksListUpdateCounterWhenModified"
+ "acknowledgedNetworksListUpdateCounterWhenShared"
+ "acknowledgedNetworksUpdateCounterWhenModified"
+ "acknowledgedNetworksUpdateCounterWhenShared"
+ "askToShareProxCardClientID"
+ "associatedBundleID"
+ "associatedDeviceID"
+ "authorizationLevel"
+ "authorizationProxCardClientID"
+ "cancelAskToShareProxCardHandler"
+ "cancelAskToShareUserNotificationHandler"
+ "cancelAuthorizationProxCardHandler"
+ "cancelWiFiNetworkSharingAskToShareProxCardForClientID:"
+ "cancelWiFiNetworkSharingAskToShareProxCardHandler"
+ "cancelWiFiNetworkSharingAskToShareUserNotificationForClientID:"
+ "cancelWiFiNetworkSharingAskToShareUserNotificationHandler"
+ "cancelWiFiNetworkSharingAuthorizationProxCardForClientID:"
+ "cancelWiFiNetworkSharingAuthorizationProxCardHandler"
+ "h2eonly"
+ "h2eonly=%d, "
+ "hyperviewd"
+ "kWiFiLocWiFiNetworkSharingUserNotificationBody"
+ "kWiFiLocWiFiNetworkSharingUserNotificationTitle"
+ "kWiFiLocWiFiNetworkSharingUserNotificationTitleCH"
+ "launchInteractionWithDevice:flags:reason:completionHandler:"
+ "link down event"
+ "mfpc"
+ "mfpc=%d, "
+ "request canceled (client invalidated)"
+ "resetMetadataForBundleID:accessoryID:"
+ "resetWiFiNetworkSharingForBundleID:accessoryID:error:"
+ "resetWiFiNetworkSharingForBundleID:accessoryID:requestParams:reply:"
+ "setAcknowledgedNetworksListUpdateCounterWhenModified:"
+ "setAcknowledgedNetworksListUpdateCounterWhenShared:"
+ "setAskToShareProxCardClientID:"
+ "setAuthorizationProxCardClientID:"
+ "setCancelAskToShareProxCardHandler:"
+ "setCancelAskToShareUserNotificationHandler:"
+ "setCancelAuthorizationProxCardHandler:"
+ "setCancelWiFiNetworkSharingAskToShareProxCardHandler:"
+ "setCancelWiFiNetworkSharingAskToShareUserNotificationHandler:"
+ "setCancelWiFiNetworkSharingAuthorizationProxCardHandler:"
+ "setH2eonly:"
+ "setMfpc:"
+ "setShouldAuthenticateDefaultAction:"
+ "setShouldShowSubordinateIcon:"
+ "setTransitiondisabledflags:"
+ "showPermissionPrompt:accessoryIdentifier:accessoryName:authorizationLevel:overrideBundleID:"
+ "transitiondisabledflags"
+ "transitiondisabledflags=%ld, "
+ "v16@?0@\"CWFWiFiNetworkSharingClientID\"8"
+ "v24@0:8@\"CWFWiFiNetworkSharingClientID\"16"
+ "v28@0:8@16B24"
+ "v32@?0@\"CWFWiFiNetworkSharingNetworkID\"8@\"CWFWiFiNetworkSharingNetworkMetadata\"16^B24"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"CWFRequestParameters\"32@?<v@?@\"NSError\">40"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSNumber\"40@\"NSString\"48"
+ "v56@0:8@16@24@32@40@48"
- "(shared=%@, firstShared=%@, lastModified=%@, askToShareStatus=%@ (%@), waitingForAssoc=%d)"
- "B44@0:8@16@24Q32B40"
- "[OTA_SET] %s:  --- Received asset discovered notificaiton --- "
- "[OTA_SET] %s:  --- Received asset download notificaiton --- "
- "[corewifi] [wifi-network-sharing] Automatically removing ask-to-share notification (timeout=%ds)"
- "[corewifi] [wifi-network-sharing] Current network is ask-to-share eligible for clientID (clientID=%{public}@, knownNetwork=%{public}@)"
- "[corewifi] [wifi-network-sharing] Received ask-to-share UI service response (clientID=%{public}@, error=%{public}@, status=%{public}@)"
- "[corewifi] [wifi-network-sharing] Received authorization UI response (clientID=%{public}@, error=%{public}@, authLevel=%{public}@)"
- "[corewifi] [wifi-network-sharing] Triggering ask-to-share UI service (clientID=%{public}@)"
- "[corewifi] [wifi-network-sharing] Triggering authorization UI (clientID=%{public}@)"
- "__askToShareNetworkForCurrentNetworkWithClientID:onDemand:"
- "__canAskToShareCurrentNetworkForClientID:onDemand:"
- "__canAskToShareKnownNetwork:metadata:authorizationStatus:onDemand:"
- "__cancelRecommendedNetworkNotificationTimeout"
- "__presentAskToShareUserNotificationForNetwork:accessoryName:"
- "__scheduleRecommendedNetworkNotificationTimeout"
- "__sendNetworkListUpdateEventForClientID:"
- "__updateRateLimitAskToShareFromAppRequestTimestampCacheForClientID:"
- "__updateRateLimitAskToShareFromAppexRequestTimestampCacheForClientID:networkID:"
- "__updateRateLimitAuthorizationRequestTimestampCacheForClientID:"
- "_wifiNetworkSharingAskToShareNotificationStatusTimer"
- "kWiFiLocWiFiNetworkSharingUserNoticationBody"
- "kWiFiLocWiFiNetworkSharingUserNoticationTitle"
- "kWiFiLocWiFiNetworkSharingUserNoticationTitleCH"

```
