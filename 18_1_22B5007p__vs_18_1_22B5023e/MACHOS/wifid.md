## wifid

> `/usr/sbin/wifid`

```diff

-1753.97.0.0.0
-  __TEXT.__text: 0x1914a4
-  __TEXT.__auth_stubs: 0x2620
-  __TEXT.__objc_stubs: 0x11f00
+1753.107.4.2.1
+  __TEXT.__text: 0x19294c
+  __TEXT.__auth_stubs: 0x2630
+  __TEXT.__objc_stubs: 0x11ea0
   __TEXT.__objc_methlist: 0x53c8
-  __TEXT.__objc_methname: 0x172d6
+  __TEXT.__objc_methname: 0x172c7
   __TEXT.__objc_classname: 0x7f4
   __TEXT.__objc_methtype: 0x2c03
-  __TEXT.__const: 0x8b0
-  __TEXT.__gcc_except_tab: 0x1c24
-  __TEXT.__cstring: 0x68a64
+  __TEXT.__const: 0x8d0
+  __TEXT.__gcc_except_tab: 0x1c4c
+  __TEXT.__cstring: 0x69277
   __TEXT.__ustring: 0x4c2
-  __TEXT.__oslogstring: 0xd8e
+  __TEXT.__oslogstring: 0xdd4
   __TEXT.__dlopen_cstrs: 0x1a5
   __TEXT.__info_plist: 0x642
-  __TEXT.__unwind_info: 0x3678
-  __DATA_CONST.__auth_got: 0x1320
-  __DATA_CONST.__got: 0x1678
-  __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x7018
-  __DATA_CONST.__cfstring: 0x1ca20
+  __TEXT.__unwind_info: 0x36a0
+  __DATA_CONST.__auth_got: 0x1328
+  __DATA_CONST.__got: 0x1670
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0x7048
+  __DATA_CONST.__cfstring: 0x1cb40
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xc8

   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA.__objc_const: 0xd6d0
-  __DATA.__objc_selrefs: 0x52b0
+  __DATA.__objc_selrefs: 0x5298
   __DATA.__objc_ivar: 0x928
   __DATA.__objc_data: 0x1220
   __DATA.__data: 0x1078

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
-  - /System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport
   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /System/Library/PrivateFrameworks/CPMS.framework/CPMS
   - /System/Library/PrivateFrameworks/CaptiveNetwork.framework/CaptiveNetwork

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 5478
+  Functions: 5485
   Symbols:   1323
-  CStrings:  15566
+  CStrings:  15599
 
Symbols:
+ _qos_class_self
- _ZhuGeCopyValueWithError
CStrings:
+ "%!s(MISSING) WFMacRandomisation : Attempting to tri state upgrade for network<%!@(MISSING)>"
+ "%!s(MISSING) WFMacRandomisation : private MAC networks need to be sanitized due to device reboot [%!h(MISSING)hu]"
+ "%!s(MISSING) WFMacRandomisation : private MAC networks need to be sanitized due to iCloud restore on a new device [%!h(MISSING)hu]"
+ "%!s(MISSING) WFMacRandomisation : tri state upgrade for network<%!@(MISSING)>, using switch state : %!d(MISSING) "
+ "%!s(MISSING) for ssid [%!@(MISSING)] bssid [%!@(MISSING)] rssi [%!l(MISSING)d] ifname [%!@(MISSING)] linkEvent %!d(MISSING)"
+ "%!s(MISSING): Clearing all user suppressed Auto Hotspot Devices \n"
+ "%!s(MISSING): Found NSUserDefaults kManagedFaultConnectionStallOverrideAllow FALSE, removing WiFiAnalyticsMessageTypeManagedFault for %!@(MISSING)"
+ "%!s(MISSING): Found NSUserDefaults kManagedFaultConnectionStallOverrideAllow TRUE, setting WiFiAnalyticsMessageTypeManagedFault for %!@(MISSING)"
+ "%!s(MISSING): Found NSUserDefaults kManagedFaultOverrideAll FALSE, removing WiFiAnalyticsMessageTypeManagedFault for %!@(MISSING)"
+ "%!s(MISSING): Found NSUserDefaults kManagedFaultOverrideAll TRUE, setting WiFiAnalyticsMessageTypeManagedFault for %!@(MISSING)"
+ "%!s(MISSING): Got kWiFiUsageFaultReasonAirplayConnectionStall, checking audio state"
+ "%!s(MISSING): WFMacRandomisation : Adding new Network <%!@(MISSING)> to PrivateMacCache. Private mac pref is : <%!d(MISSING)>"
+ "%!s(MISSING): WFMacRandomisation : Temp networks updated with new MAC address"
+ "%!s(MISSING): WiFi is OFF"
+ "%!s(MISSING): control center state changed from '%!@(MISSING)' -> '%!@(MISSING)'"
+ "%!s(MISSING): did not manage to find password for HS2.0 account %!@(MISSING). Looking for next matching account..."
+ "%!s(MISSING): did not manage to find password for HS2.0 network %!@(MISSING). No more matching HS2.0 account"
+ "%!s(MISSING): disabling MIS discovery due to control center dismissal"
+ "%!s(MISSING): found HS2.0 account %!@(MISSING) matching %!@(MISSING), returning %!@(MISSING)"
+ "%!s(MISSING): immediately matched HS2.0 account %!@(MISSING), returning %!@(MISSING)"
+ "%!s(MISSING): inNetwork is NULL!"
+ "%!s(MISSING): linkRecoveryDisabled == FALSE implies No Audio Playing, removing WiFiAnalyticsMessageTypeManagedFault"
+ "%!s(MISSING): linkRecoveryDisabled == TRUE implies Audio Playing, setting WiFiAnalyticsMessageTypeManagedFault"
+ "%!s(MISSING): next HS2.0 account %!@(MISSING) matching %!@(MISSING) has no credentials, skipping"
+ "%!s(MISSING): outAccount is NULL!"
+ "%!s(MISSING): session based network is an accessory = '%!@(MISSING)'"
+ "ManagedFaultConnectionStallOverrideAllow"
+ "ManagedFaultOverrideAll"
+ "PRIVATE_MAC_ADDRESS_TYPE"
+ "PersonalHotspotControlExtension"
+ "PrivateMacListCloudRestoreSanitized"
+ "PrivateMacPrefChanged"
+ "PrivateMacPrefChangedTimestamp"
+ "UpdatePrivateMacReasonMigrateToTriState"
+ "WFMacRandomisation : Returning parameters to client for network [%!@(MISSING)]: privateMacSwitchState <%!d(MISSING)>"
+ "WFMacRandomisation : Unknow private MAC type for network [%!@(MISSING)]"
+ "WFMacRandomisation :%!s(MISSING): Temp network <%!@(MISSING)> gets new mac address: %!@(MISSING)"
+ "WiFiManager-1753.107.4.2.1 Aug  6 2024 20:56:06"
+ "WiFiManager-1753.107.4.2.1 Aug  6 2024 20:56:34"
+ "WiFiManagerPrivateMacNetworksEvaluateSanitizeRequired"
+ "[corewifi] Will process CoreWiFi XPC request (req=%!{(MISSING)public}@, qos=%!d(MISSING))"
+ "__WiFiDeviceCopyPreparedEAPProfile"
+ "__WiFiDeviceManagerClearSuppressedAutoHotSpotDevices"
+ "__WiFiDeviceManagerRequestForNextMatchingHS20AccountCallback"
+ "__WiFiManagerControlCenterStateChanged"
+ "__WiFiManagerPrivateMacUpdateTempNetworks"
+ "non-visible"
+ "visible"
- "%!s(MISSING): WFMacRandomisation : Adding new Network <%!@(MISSING)> to PrivateMacCache. Private mac pref is : <%!h(MISSING)hu>"
- "%!s(MISSING): WFMacRandomisation : Link UP. UI Status is <%!d(MISSING)> for network <%!@(MISSING)> and mac address is <%!@(MISSING)>"
- "%!s(MISSING): WFMacRandomisation : User turned private MAC UI from OFF to ON for network <%!@(MISSING)>"
- "%!s(MISSING): WFMacRandomisation : User turned private MAC UI from ON to OFF for network <%!@(MISSING)>"
- "FactoryShippingSettingTime"
- "WFMacRandomisation : Returning parameters to client for network [%!@(MISSING)]: privateMacSwitchState <%!h(MISSING)hu>"
- "WFMacRandomisation :%!s(MISSING): Sanitized network <%!@(MISSING)> is non-Trustworthy and gets new mac address: %!@(MISSING)"
- "WiFiDeviceManagerSetManufactureDate error<%!d(MISSING):%!p(MISSING):%!p(MISSING)> \n"
- "WiFiDeviceSetManufactureDate"
- "WiFiDeviceSetManufactureDate %!@(MISSING) %!d(MISSING)/%!d(MISSING)/%!d(MISSING) \n"
- "WiFiManager-1753.97 Jul 12 2024 09:01:25"
- "WiFiManager-1753.97 Jul 12 2024 09:01:52"
- "day"
- "month"
- "year"

```
