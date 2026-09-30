## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

-1770.8.0.0.0
-  __TEXT.__text: 0x8b718
+1770.10.0.0.0
+  __TEXT.__text: 0x8c4fc
   __TEXT.__auth_stubs: 0xca0
-  __TEXT.__objc_stubs: 0x12da0
-  __TEXT.__objc_methlist: 0xa624
+  __TEXT.__objc_stubs: 0x12f80
+  __TEXT.__objc_methlist: 0xa774
   __TEXT.__gcc_except_tab: 0x980
   __TEXT.__const: 0x31e4
-  __TEXT.__cstring: 0x2b396
-  __TEXT.__objc_methname: 0x224f3
-  __TEXT.__objc_classname: 0x6f3
-  __TEXT.__objc_methtype: 0x4b34
+  __TEXT.__cstring: 0x2b85b
+  __TEXT.__objc_methname: 0x22799
+  __TEXT.__objc_classname: 0x71b
+  __TEXT.__objc_methtype: 0x4c51
   __TEXT.__dlopen_cstrs: 0x43
   __TEXT.__oslogstring: 0x44
-  __TEXT.__unwind_info: 0x1610
+  __TEXT.__unwind_info: 0x1648
   __DATA_CONST.__auth_got: 0x668
   __DATA_CONST.__got: 0x4d8
-  __DATA_CONST.__const: 0x2270
-  __DATA_CONST.__cfstring: 0x19140
-  __DATA_CONST.__objc_classlist: 0x258
+  __DATA_CONST.__const: 0x22a0
+  __DATA_CONST.__cfstring: 0x19740
+  __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2a8
+  __DATA_CONST.__objc_superrefs: 0x2b8
   __DATA_CONST.__objc_intobj: 0x1728
   __DATA_CONST.__objc_arraydata: 0x1ba0
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x570
-  __DATA.__objc_const: 0xff80
-  __DATA.__objc_selrefs: 0x6430
-  __DATA.__objc_ivar: 0x126c
-  __DATA.__objc_data: 0x1770
+  __DATA.__objc_const: 0x10230
+  __DATA.__objc_selrefs: 0x64d0
+  __DATA.__objc_ivar: 0x128c
+  __DATA.__objc_data: 0x1810
   __DATA.__data: 0x2f0
-  __DATA.__bss: 0x374
+  __DATA.__bss: 0x384
   __DATA.__common: 0xc8
   - /System/Library/Frameworks/CallKit.framework/Versions/A/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 62AC01D1-B53D-32DE-B61F-BEE8BFACA366
-  Functions: 3627
+  UUID: ED22F017-31A3-3296-AEC1-91BD472B82F7
+  Functions: 3655
   Symbols:   357
-  CStrings:  12732
+  CStrings:  12871
 
CStrings:
+ "@\"NSMutableDictionary\"8@?0"
+ "@32@0:8{?=BBBBBBBBd}16"
+ "@56@0:8{?=BBBBBBBBd}16{?=BBBBBBBBd}32d48"
+ "AWDL"
+ "AWDL:%@,"
+ "AWDLActive_Current"
+ "AWDLActive_Previous"
+ "Associated"
+ "BT:%@,"
+ "BTConnected_Current"
+ "BTConnected_Previous"
+ "Bluetooth connection"
+ "CarPlay Session Active"
+ "CarPlay:%@,"
+ "CarPlayActive_Current"
+ "CarPlayActive_Previous"
+ "Cellular connection"
+ "Cellular:%@,"
+ "CellularConnected_Current"
+ "CellularConnected_Previous"
+ "Connected"
+ "Disconnected"
+ "Duration"
+ "HotspotActive_Current"
+ "HotspotActive_Previous"
+ "Idle"
+ "Inactive"
+ "NAN"
+ "NAN:%@,"
+ "NANActive_Current"
+ "NANActive_Previous"
+ "PHS:%@,"
+ "Personal Hotspot"
+ "RadioStateAnalytics: %@ state changed to %@"
+ "RadioStateAnalytics: Initialized radio state analytics"
+ "RadioStateAnalytics: Negative duration detected (%f seconds), resetting to 0"
+ "RadioStateAnalytics: Recorded state transition - %@"
+ "RadioStateAnalytics: Skipping event with short duration: %f"
+ "RadioStateAnalytics: Submitting event to CoreAnalytics"
+ "RadioStateAnalytics: Unusually large duration detected (%f seconds), capping at 1 week"
+ "RadioStateEvent"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_analyticsQueue"
+ "Td,N,V_duration"
+ "Td,N,V_lastTransitionTime"
+ "Td,N,V_transitionTime"
+ "Thread Radio Active"
+ "Thread:%@"
+ "ThreadActive_Current"
+ "ThreadActive_Previous"
+ "Transition at %f - From: %@ To: %@ Duration: %f"
+ "T{?=BBBBBBBBd},N,V_currentState"
+ "T{?=BBBBBBBBd},N,V_previousState"
+ "WCM_RadioStateAnalytics"
+ "WiFi association"
+ "WiFi:%@,"
+ "WiFiAssociated_Current"
+ "WiFiAssociated_Previous"
+ "_analyticsQueue"
+ "_currentState"
+ "_duration"
+ "_lastSeenState"
+ "_lastTransitionTime"
+ "_previousState"
+ "_transitionTime"
+ "analyticsQueue"
+ "com.apple.WirelessRadioManager.CoexRadioStatesInsights"
+ "com.apple.WirelessRadioManager.RadioStateAnalytics"
+ "currentState"
+ "d24@0:8d16"
+ "initWithPreviousState:currentState:transitionTime:"
+ "lastTransitionTime"
+ "previousState"
+ "recordStateTransition"
+ "setAnalyticsQueue:"
+ "setCurrentState:"
+ "setDuration:"
+ "setLastTransitionTime:"
+ "setPreviousState:"
+ "setTransitionTime:"
+ "stateToString:"
+ "submitEventToAnalytics:"
+ "transitionTime"
+ "updateCarPlaySession:"
+ "updateCellularState"
+ "updateRadioState:value:"
+ "v28@0:8q16B24"
+ "v32@0:8{?=BBBBBBBBd}16"
+ "validateDuration:"
+ "{?=\"wifiAssociated\"B\"btConnected\"B\"personalHotspotActive\"B\"awdlActive\"B\"nanActive\"B\"cellularConnected\"B\"carPlayActive\"B\"threadRadioActive\"B\"timestamp\"d}"
+ "{?=BBBBBBBBd}16@0:8"

```
