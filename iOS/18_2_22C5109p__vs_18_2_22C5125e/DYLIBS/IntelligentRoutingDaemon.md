## IntelligentRoutingDaemon

> `/System/Library/PrivateFrameworks/IntelligentRoutingDaemon.framework/IntelligentRoutingDaemon`

```diff

-96.0.6.0.0
-  __TEXT.__text: 0x69c20
+96.0.6.0.1
+  __TEXT.__text: 0x6a0c8
   __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0x6aac
-  __TEXT.__oslogstring: 0x5e4f
-  __TEXT.__cstring: 0x846a
+  __TEXT.__objc_methlist: 0x6aec
+  __TEXT.__oslogstring: 0x5de3
+  __TEXT.__cstring: 0x8426
   __TEXT.__const: 0x128
-  __TEXT.__gcc_except_tab: 0x1930
-  __TEXT.__unwind_info: 0x18b8
+  __TEXT.__gcc_except_tab: 0x1938
+  __TEXT.__unwind_info: 0x18c0
   __TEXT.__objc_classname: 0xed4
-  __TEXT.__objc_methname: 0x1668f
-  __TEXT.__objc_methtype: 0x1de7
-  __TEXT.__objc_stubs: 0xde80
+  __TEXT.__objc_methname: 0x16737
+  __TEXT.__objc_methtype: 0x1e16
+  __TEXT.__objc_stubs: 0xdf20
   __DATA_CONST.__got: 0x7a0
-  __DATA_CONST.__const: 0x1be0
+  __DATA_CONST.__const: 0x1be8
   __DATA_CONST.__objc_classlist: 0x428
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d30
+  __DATA_CONST.__objc_selrefs: 0x3d58
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0x108
   __AUTH_CONST.__auth_got: 0x430
   __AUTH_CONST.__const: 0x720
-  __AUTH_CONST.__cfstring: 0x63e0
-  __AUTH_CONST.__objc_const: 0xe7b8
+  __AUTH_CONST.__cfstring: 0x6440
+  __AUTH_CONST.__objc_const: 0xe818
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH.__objc_data: 0x870
-  __DATA.__objc_ivar: 0x924
+  __DATA.__objc_ivar: 0x928
   __DATA.__data: 0xba0
   __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x2120

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2550
-  Symbols:   3119
-  CStrings:  4774
+  Functions: 2555
+  Symbols:   3125
+  CStrings:  4780
 
Symbols:
+ _IRContextChangeReasonDisplayOn
CStrings:
+ "%!s(MISSING)[%!@(MISSING)], Event rejected, type: %!@(MISSING), subtype: %!@(MISSING), for candidateIdentifier: %!@(MISSING), displayOn: %!@(MISSING)"
+ "&\x11!!"
+ "<IRSystemStateDO | appInFocusBundleID:%!@(MISSING) appInFocusWindowValid:%!@(MISSING) deviceWiFiSSID:%!@(MISSING) locationSemanticUserSpecificPlaceType:%!@(MISSING) locationSemanticLoiIdentifier:%!@(MISSING) iCloudId:%!@(MISSING) avInitialRouteSharingPolicy:%!@(MISSING) mediaRouteGroupLeaderOutputDeviceID:%!@(MISSING) timeZoneSeconds:%!@(MISSING) outputDeviceName:%!@(MISSING) outputDeviceType:%!@(MISSING) outputDeviceSubType:%!@(MISSING) predictedOutputDeviceName:%!@(MISSING) predictedOutputDeviceType:%!@(MISSING) predictedOutputDeviceSubType:%!@(MISSING) appInFocusWindowScreenUnlockEvent:%!@(MISSING) pdrFenceActive:%!@(MISSING) latestPickerChoiceDate:%!@(MISSING) isContinuityDisplay:%!@(MISSING) displayOn:%!@(MISSING)>"
+ "@152@0:8@16B24@28i36@40@48@56@64q72@80Q88Q96@104Q112Q120B128B132@136B144B148"
+ "B56@0:8@\"IREventDO\"16@\"IRHistoryEventsContainerDO\"24@\"IRSystemStateDO\"32@\"IRCandidateDO\"40@\"NSDate\"48"
+ "B56@0:8@16@24@32@40@48"
+ "Display On"
+ "Missing serialized value for IRSystemStateDO.displayOn"
+ "TB,R,N,V_displayOn"
+ "_updateSystemStateWithDisplayOn:"
+ "appInFocusBundleID: %!@(MISSING)\n appInFocusWindowValid: %!@(MISSING)\n appInFocusWindowScreenUnlockEvent: %!@(MISSING)\n deviceWiFiSSID: %!@(MISSING)\n locationSemanticLoiIdentifier: %!@(MISSING)\n iCloudId: %!@(MISSING)\n locationSemanticUserSpecificPlaceType: %!@(MISSING)\n avInitialRouteSharingPolicy: %!@(MISSING)\n mediaRouteGroupLeaderOutputDeviceID: %!@(MISSING)\n outputDevice: Name - %!@(MISSING), Type - %!@(MISSING), SubType - %!@(MISSING)\n predictedOutputDevice: Name - %!@(MISSING), Type - %!@(MISSING), SubType - %!@(MISSING)\n pdrFenceActive: %!@(MISSING)\n latestPickerChoiceDate: %!@(MISSING)\n isContinuityDisplay: %!@(MISSING)\n displayOn: %!@(MISSING)\n"
+ "containsString:"
+ "copyWithReplacementDisplayOn:"
+ "initWithAppInFocusBundleID:appInFocusWindowValid:deviceWiFiSSID:locationSemanticUserSpecificPlaceType:locationSemanticLoiIdentifier:iCloudId:avInitialRouteSharingPolicy:mediaRouteGroupLeaderOutputDeviceID:timeZoneSeconds:outputDeviceName:outputDeviceType:outputDeviceSubType:predictedOutputDeviceName:predictedOutputDeviceType:predictedOutputDeviceSubType:appInFocusWindowScreenUnlockEvent:pdrFenceActive:latestPickerChoiceDate:isContinuityDisplay:displayOn:"
+ "isIOS"
+ "monitor:didUpdateDisplayOn:"
+ "shouldRejectEvent:withHistoryEventsContainer:withSystemState:forCandidate:date:"
+ "systemStateDOWithAppInFocusBundleID:appInFocusWindowValid:deviceWiFiSSID:locationSemanticUserSpecificPlaceType:locationSemanticLoiIdentifier:iCloudId:avInitialRouteSharingPolicy:mediaRouteGroupLeaderOutputDeviceID:timeZoneSeconds:outputDeviceName:outputDeviceType:outputDeviceSubType:predictedOutputDeviceName:predictedOutputDeviceType:predictedOutputDeviceSubType:appInFocusWindowScreenUnlockEvent:pdrFenceActive:latestPickerChoiceDate:isContinuityDisplay:displayOn:"
- "\x16\x11!!"
- "#display-monitor, %!s(MISSING):%!d(MISSING): assertion failure in %!s(MISSING)"
- "#display-monitor, [ErrorId - appInFocusTimestamp is nil] appInFocusTimestamp is nil"
- "%!s(MISSING)[%!@(MISSING)], Event rejected, type: %!@(MISSING), subtype: %!@(MISSING), for candidate: %!@(MISSING)"
- "-[IRDisplayMonitor _didUpdateMainDisplayLayout:]"
- "/Library/Caches/com.apple.xbs/Sources/IntelligentRouting/IntelligentRoutingDaemon/DataProviders/Display/IRDisplayMonitor.m"
- "<IRSystemStateDO | appInFocusBundleID:%!@(MISSING) appInFocusWindowValid:%!@(MISSING) deviceWiFiSSID:%!@(MISSING) locationSemanticUserSpecificPlaceType:%!@(MISSING) locationSemanticLoiIdentifier:%!@(MISSING) iCloudId:%!@(MISSING) avInitialRouteSharingPolicy:%!@(MISSING) mediaRouteGroupLeaderOutputDeviceID:%!@(MISSING) timeZoneSeconds:%!@(MISSING) outputDeviceName:%!@(MISSING) outputDeviceType:%!@(MISSING) outputDeviceSubType:%!@(MISSING) predictedOutputDeviceName:%!@(MISSING) predictedOutputDeviceType:%!@(MISSING) predictedOutputDeviceSubType:%!@(MISSING) appInFocusWindowScreenUnlockEvent:%!@(MISSING) pdrFenceActive:%!@(MISSING) latestPickerChoiceDate:%!@(MISSING) isContinuityDisplay:%!@(MISSING)>"
- "@148@0:8@16B24@28i36@40@48@56@64q72@80Q88Q96@104Q112Q120B128B132@136B144"
- "B48@0:8@\"IREventDO\"16@\"IRHistoryEventsContainerDO\"24@\"IRCandidateDO\"32@\"NSDate\"40"
- "appInFocusBundleID: %!@(MISSING)\n appInFocusWindowValid: %!@(MISSING)\n appInFocusWindowScreenUnlockEvent: %!@(MISSING)\n deviceWiFiSSID: %!@(MISSING)\n locationSemanticLoiIdentifier: %!@(MISSING)\n iCloudId: %!@(MISSING)\n locationSemanticUserSpecificPlaceType: %!@(MISSING)\n avInitialRouteSharingPolicy: %!@(MISSING)\n mediaRouteGroupLeaderOutputDeviceID: %!@(MISSING)\n outputDevice: Name - %!@(MISSING), Type - %!@(MISSING), SubType - %!@(MISSING)\n predictedOutputDevice: Name - %!@(MISSING), Type - %!@(MISSING), SubType - %!@(MISSING)\n pdrFenceActive: %!@(MISSING)\n latestPickerChoiceDate: %!@(MISSING)\n isContinuityDisplay: %!@(MISSING)\n"
- "initWithAppInFocusBundleID:appInFocusWindowValid:deviceWiFiSSID:locationSemanticUserSpecificPlaceType:locationSemanticLoiIdentifier:iCloudId:avInitialRouteSharingPolicy:mediaRouteGroupLeaderOutputDeviceID:timeZoneSeconds:outputDeviceName:outputDeviceType:outputDeviceSubType:predictedOutputDeviceName:predictedOutputDeviceType:predictedOutputDeviceSubType:appInFocusWindowScreenUnlockEvent:pdrFenceActive:latestPickerChoiceDate:isContinuityDisplay:"
- "shouldRejectEvent:withHistoryEventsContainer:forCandidate:date:"
- "systemStateDOWithAppInFocusBundleID:appInFocusWindowValid:deviceWiFiSSID:locationSemanticUserSpecificPlaceType:locationSemanticLoiIdentifier:iCloudId:avInitialRouteSharingPolicy:mediaRouteGroupLeaderOutputDeviceID:timeZoneSeconds:outputDeviceName:outputDeviceType:outputDeviceSubType:predictedOutputDeviceName:predictedOutputDeviceType:predictedOutputDeviceSubType:appInFocusWindowScreenUnlockEvent:pdrFenceActive:latestPickerChoiceDate:isContinuityDisplay:"

```
