## AirPortSettings

> `/System/Library/PreferenceBundles/AirPortSettings.bundle/AirPortSettings`

```diff

 1175.0.0.0.0
-  __TEXT.__text: 0xc50
-  __TEXT.__auth_stubs: 0x190
+  __TEXT.__text: 0xb1c
   __TEXT.__objc_methlist: 0xf8
-  __TEXT.__cstring: 0x267
-  __TEXT.__unwind_info: 0xa8
-  __TEXT.__objc_classname: 0x17
-  __TEXT.__objc_methname: 0x479
-  __TEXT.__objc_methtype: 0x8f
-  __TEXT.__objc_stubs: 0x480
-  __DATA_CONST.__got: 0x20
+  __TEXT.__cstring: 0x269
+  __TEXT.__unwind_info: 0x90
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x180
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xd0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0x280
   __AUTH_CONST.__objc_const: 0x1c0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x4

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D29FB1FF-D98E-3838-924C-47E99651F677
+  UUID: 035550D5-C9BD-30D2-BCF5-E1DACD49FDA6
   Functions: 20
-  Symbols:   126
-  CStrings:  111
+  Symbols:   124
+  CStrings:  41
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x2
- _objc_release_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x20
- _objc_retain_x21
Functions:
~ -[APNetworksController initWithNibName:bundle:] : 148 -> 140
~ -[APNetworksController loadView] : 660 -> 624
~ -[APNetworksController viewDidAppear:] : 108 -> 104
~ -[APNetworksController viewDidDisappear:] : 132 -> 124
~ -[APNetworksController viewWillDisappear:] : 108 -> 104
~ -[APNetworksController handleURL:] : 472 -> 452
~ -[APNetworksController _loadHealthOverrides] : 728 -> 724
~ -[APNetworksController healthOverrides] : 16 -> 20
~ -[APNetworksController setHealthOverrides:] : 80 -> 20
~ -[APNetworksController airportController] : 16 -> 20
~ -[APNetworksController setAirportController:] : 80 -> 20
~ -[APNetworksController settingsViewController] : 16 -> 20
~ -[APNetworksController setSettingsViewController:] : 80 -> 20
~ -[APNetworksController deferredURL] : 16 -> 20
~ -[APNetworksController setDeferredURL:] : 80 -> 20
CStrings:
- ".cxx_destruct"
- "@\"NSURL\""
- "@\"WFAirportViewController\""
- "@\"WFHealthIssueOverrides\""
- "@\"WFNetworkListController\""
- "@16@0:8"
- "@32@0:8@16@24"
- "APNetworksController"
- "B"
- "T@\"NSURL\",&,N,V_deferredURL"
- "T@\"WFAirportViewController\",&,N,V_settingsViewController"
- "T@\"WFHealthIssueOverrides\",&,N,V_healthOverrides"
- "T@\"WFNetworkListController\",&,N,V_airportController"
- "URLWithString:"
- "_airportController"
- "_deferredURL"
- "_healthOverrides"
- "_joinEnterprise"
- "_loadHealthOverrides"
- "_notifyAirPortSettingsVisible:"
- "_pushDataUsage"
- "_settingsViewController"
- "_viewLoaded"
- "addChildViewController:"
- "addSubview:"
- "airportController"
- "deferredURL"
- "didWake"
- "frame"
- "handleURL:"
- "healthOverrides"
- "initWithNibName:bundle:"
- "initWithViewController:"
- "isEqualToString:"
- "length"
- "loadView"
- "lowercaseString"
- "navigationItem"
- "objectForKey:"
- "pushDataUsageViewController"
- "setAirportController:"
- "setCarrierNetwork:"
- "setCommonSSID:"
- "setDeferredURL:"
- "setDnsFiltered:"
- "setFrame:"
- "setHealthOverrides:"
- "setHealthRecommendationOverrides:"
- "setHiddenNetwork:"
- "setLargeTitleDisplayMode:"
- "setLegacyPHY:"
- "setNoInternetConnection:"
- "setPrivateAddressOverride:"
- "setSecurityOverride:"
- "setSettingsViewController:"
- "setTitle:"
- "settingsViewController"
- "startScanning"
- "stopScanning"
- "stringByAppendingString:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "view"
- "viewController"
- "viewDidAppear:"
- "viewDidDisappear:"
- "viewWillDisappear:"
- "willBecomeActive"
- "willResignActive"

```
