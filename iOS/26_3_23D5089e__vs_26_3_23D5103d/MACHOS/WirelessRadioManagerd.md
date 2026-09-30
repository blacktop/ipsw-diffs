## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

-1860.4.0.0.0
-  __TEXT.__text: 0x15ec00
+1860.5.1.0.0
+  __TEXT.__text: 0x15fc38
   __TEXT.__auth_stubs: 0x24a0
-  __TEXT.__objc_stubs: 0x1e1a0
+  __TEXT.__objc_stubs: 0x1e3c0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x1014c
+  __TEXT.__objc_methlist: 0x102a4
   __TEXT.__gcc_except_tab: 0x5230
-  __TEXT.__const: 0x18c58
-  __TEXT.__cstring: 0x4df7e
-  __TEXT.__objc_classname: 0x1082
-  __TEXT.__objc_methname: 0x2f815
-  __TEXT.__objc_methtype: 0x78d8
+  __TEXT.__const: 0x18c60
+  __TEXT.__cstring: 0x4e443
+  __TEXT.__objc_classname: 0x10aa
+  __TEXT.__objc_methname: 0x2fabb
+  __TEXT.__objc_methtype: 0x79e7
   __TEXT.__dlopen_cstrs: 0x3ca
   __TEXT.__oslogstring: 0x90
-  __TEXT.__unwind_info: 0x46c0
+  __TEXT.__unwind_info: 0x46f0
   __DATA_CONST.__auth_got: 0x1268
   __DATA_CONST.__got: 0x710
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x4d60
-  __DATA_CONST.__cfstring: 0x2cd80
-  __DATA_CONST.__objc_classlist: 0x4d0
+  __DATA_CONST.__const: 0x4db0
+  __DATA_CONST.__cfstring: 0x2d380
+  __DATA_CONST.__objc_classlist: 0x4e0
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x4f8
+  __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_intobj: 0x3558
   __DATA_CONST.__objc_arraydata: 0x12810
   __DATA_CONST.__objc_arrayobj: 0x80d0
   __DATA_CONST.__objc_dictobj: 0x7a8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x1a130
-  __DATA.__objc_selrefs: 0x90b8
-  __DATA.__objc_ivar: 0x1b1c
-  __DATA.__objc_data: 0x3020
+  __DATA.__objc_const: 0x1a3e0
+  __DATA.__objc_selrefs: 0x9158
+  __DATA.__objc_ivar: 0x1b3c
+  __DATA.__objc_data: 0x30c0
   __DATA.__data: 0x760
   __DATA.__common: 0x1e1
-  __DATA.__bss: 0x5b8
+  __DATA.__bss: 0x5c8
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D0E5180C-0ED6-3514-90B8-7E1C38FF7AA1
-  Functions: 7018
+  UUID: 60FEA27A-E131-3979-8E43-D4BECBE60F3C
+  Functions: 7047
   Symbols:   816
-  CStrings:  21020
+  CStrings:  21158
 
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
+ "v32@0:8{?=BBBBBBBBd}16"
+ "validateDuration:"
+ "{?=\"wifiAssociated\"B\"btConnected\"B\"personalHotspotActive\"B\"awdlActive\"B\"nanActive\"B\"cellularConnected\"B\"carPlayActive\"B\"threadRadioActive\"B\"timestamp\"d}"
+ "{?=BBBBBBBBd}16@0:8"

```
