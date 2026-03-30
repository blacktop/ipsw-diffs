## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`

```diff

-2169.100.30.0.0
-  __TEXT.__text: 0x28ca04
+2169.120.2.0.0
+  __TEXT.__text: 0x28ca1c
   __TEXT.__auth_stubs: 0x2c30
   __TEXT.__objc_methlist: 0x17a90
   __TEXT.__cstring: 0x25369
   __TEXT.__const: 0x1050
-  __TEXT.__oslogstring: 0x43b7f
+  __TEXT.__oslogstring: 0x43b6f
   __TEXT.__gcc_except_tab: 0x5474
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__swift5_typeref: 0x304

   __TEXT.__unwind_info: 0x7570
   __TEXT.__eh_frame: 0x6c8
   __TEXT.__objc_classname: 0x1d95
-  __TEXT.__objc_methname: 0x3d309
+  __TEXT.__objc_methname: 0x3d2f9
   __TEXT.__objc_methtype: 0x6dd8
-  __TEXT.__objc_stubs: 0x25be0
+  __TEXT.__objc_stubs: 0x25c20
   __DATA_CONST.__got: 0xf68
   __DATA_CONST.__const: 0x67c8
   __DATA_CONST.__objc_classlist: 0x870

   __DATA.__objc_ivar: 0x2e20
   __DATA.__data: 0x1d78
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xf50
+  __DATA.__bss: 0xf58
   __DATA.__common: 0x18098
   __DATA_DIRTY.__objc_data: 0x3f20
   __DATA_DIRTY.__data: 0x1e8
-  __DATA_DIRTY.__bss: 0x16d0
+  __DATA_DIRTY.__bss: 0x16c8
   __DATA_DIRTY.__common: 0x1a8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D6FAB3F4-94BE-3A7A-B555-19F2EE38F54E
+  UUID: 141B38F0-1BC3-3731-9156-B4A4F16D27B7
   Functions: 11555
-  Symbols:   37143
+  Symbols:   37145
   CStrings:  26815
 
Symbols:
+ -[LocationStateRelay wifiLocationManager]
+ _OBJC_IVAR_$_LocationStateRelay.wifiBundle
+ _OBJC_IVAR_$_LocationStateRelay.wifiLocationManager
+ ___41-[LocationStateRelay wifiLocationManager]_block_invoke
+ _objc_msgSend$observeSetupAssistantFinished
+ _objc_msgSend$requireUserNotification
+ _objc_msgSend$wifiLocationManager
+ _wifiLocationManager.pred
- -[LocationStateRelay mobileWiFiLocationManager]
- _OBJC_IVAR_$_LocationStateRelay.mobileWiFiBundle
- _OBJC_IVAR_$_LocationStateRelay.mobileWiFiLocationManager
- ___47-[LocationStateRelay mobileWiFiLocationManager]_block_invoke
- _mobileWiFiLocationManager.pred
- _objc_msgSend$mobileWiFiLocationManager
Functions:
~ -[SystemProperties init] : 1148 -> 1152
~ -[ArbitratorExpertSystemHandler init] : 376 -> 396
CStrings:
+ "CoreLocation WiFiLocationManager is nil."
+ "Did not receive location from WiFiLocationManager after %d seconds, clearing pending block."
+ "Requesting location from WiFiLocationManager"
+ "wifiBundle"
+ "wifiLocationManager"
- "CoreLocation mobileWiFiLocationManager is nil."
- "Did not receive location from MobileWiFiLocationManager after %d seconds, clearing pending block."
- "Requesting location from MobileWiFiLocationManager"
- "mobileWiFiBundle"
- "mobileWiFiLocationManager"

```
