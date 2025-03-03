## SetupAssistant

> `/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant`

```diff

-5359.4.6.100.0
-  __TEXT.__text: 0x3f8f0
+5359.4.9.100.0
+  __TEXT.__text: 0x40c28
   __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_methlist: 0x3aec
+  __TEXT.__objc_methlist: 0x3c6c
   __TEXT.__const: 0x138
   __TEXT.__gcc_except_tab: 0xf30
-  __TEXT.__oslogstring: 0x55e8
-  __TEXT.__cstring: 0x2b4e
+  __TEXT.__oslogstring: 0x5829
+  __TEXT.__cstring: 0x2b66
   __TEXT.__dlopen_cstrs: 0x1245
-  __TEXT.__unwind_info: 0x1170
-  __TEXT.__objc_classname: 0x79b
-  __TEXT.__objc_methname: 0xa336
-  __TEXT.__objc_methtype: 0x1116
-  __TEXT.__objc_stubs: 0x7ac0
-  __DATA_CONST.__got: 0x4f8
+  __TEXT.__unwind_info: 0x1190
+  __TEXT.__objc_classname: 0x7ce
+  __TEXT.__objc_methname: 0xa832
+  __TEXT.__objc_methtype: 0x113b
+  __TEXT.__objc_stubs: 0x7f20
+  __DATA_CONST.__got: 0x518
   __DATA_CONST.__const: 0x1610
-  __DATA_CONST.__objc_classlist: 0x1c8
+  __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2840
+  __DATA_CONST.__objc_selrefs: 0x2960
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x130
+  __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x178
   __AUTH_CONST.__auth_got: 0x6d0
   __AUTH_CONST.__const: 0xa40
-  __AUTH_CONST.__cfstring: 0x2f60
-  __AUTH_CONST.__objc_const: 0x58b8
+  __AUTH_CONST.__cfstring: 0x2f80
+  __AUTH_CONST.__objc_const: 0x5c08
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x380
+  __AUTH.__objc_data: 0x3c0
+  __DATA.__objc_ivar: 0x3a8
   __DATA.__data: 0x970
   __DATA.__bss: 0x5c0
   __DATA_DIRTY.__objc_data: 0xeb0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1635
-  Symbols:   2257
-  CStrings:  2959
+  Functions: 1667
+  Symbols:   2295
+  CStrings:  3035
 
Symbols:
+ _OBJC_CLASS_$_BYCellularNetworkInformation
+ _OBJC_CLASS_$_BYSIMRegionService
+ _OBJC_CLASS_$_CTXPCServiceSubscriptionContext
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ _OBJC_METACLASS_$_BYCellularNetworkInformation
+ _OBJC_METACLASS_$_BYSIMRegionService
CStrings:
+ "-"
+ "@\"CoreTelephonyClient\""
+ "@32@0:8q16q24"
+ "B\x11"
+ "BYCellularNetworkInformation"
+ "BYSIMRegionService"
+ "D"
+ "Error getting ISO code from MCC: %@, error: %@"
+ "Error getting subregion ISO code from MCC: %@, MNC: %@, error: %@"
+ "Error reading telephony network information { error: %@ }"
+ "Getting subregion languages for Home Region"
+ "Getting subregion languages for Network Region"
+ "Home subregion languages: %@"
+ "Language codes for region %@, subregion %@: %@"
+ "Network subregion languages: %@"
+ "Region ISO Code: %@"
+ "Subregion languages: %@"
+ "Subregions ISO Codes: %@"
+ "T@\"CoreTelephonyClient\",&,N,V_telephonyClient"
+ "T@\"NSArray\",C,N,V_homeSubregionISOCodes"
+ "T@\"NSArray\",C,N,V_networkSubregionISOCodes"
+ "T@\"NSString\",C,N,V_homeCountryISOCode"
+ "T@\"NSString\",C,N,V_networkCountryISOCode"
+ "Ti,R,N"
+ "Ti,R,N,V_mgProductType"
+ "Tq,N,V_homeMCC"
+ "Tq,N,V_homeMNC"
+ "Tq,N,V_networkMCC"
+ "Tq,N,V_networkMNC"
+ "Unable to find selected context to load telephony network information { slot: %ld }"
+ "Unable to get active telephony contexts { error: %@ }"
+ "_homeCountryISOCode"
+ "_homeMCC"
+ "_homeMNC"
+ "_homeSubregionISOCodes"
+ "_languagesForRegionsUsingSIMRegionService:"
+ "_mgProductType"
+ "_networkCountryISOCode"
+ "_networkMCC"
+ "_networkMNC"
+ "_networkSubregionISOCodes"
+ "_subregionLanguagesForRegion:subregionsISOCodes:"
+ "_telephonyClient"
+ "cellularNetworkInformation"
+ "com.apple.private.restrict-post.purplebuddy.launchMigrationSourceUI"
+ "copyMobileNetworkCode:error:"
+ "copyMobileSubscriberCountryCode:error:"
+ "copyMobileSubscriberIsoSubregionCode:MNC:error:"
+ "copyMobileSubscriberNetworkCode:error:"
+ "getActiveContexts:"
+ "homeCountryISOCode"
+ "homeMCC"
+ "homeMNC"
+ "homeSubregionISOCodes"
+ "initWithSlot:"
+ "isoCodeForMCC:"
+ "languagesForRegion:subdivision:withThreshold:filter:"
+ "logTelephonyError:"
+ "lowercaseString"
+ "mgProductType"
+ "networkCountryISOCode"
+ "networkMCC"
+ "networkMNC"
+ "networkSubregionISOCodes"
+ "setHomeCountryISOCode:"
+ "setHomeMCC:"
+ "setHomeMNC:"
+ "setHomeSubregionISOCodes:"
+ "setNetworkCountryISOCode:"
+ "setNetworkMCC:"
+ "setNetworkMNC:"
+ "setNetworkSubregionISOCodes:"
+ "setTelephonyClient:"
+ "slotID"
+ "stringValue"
+ "subregionISOCodesForMCC:MNC:"
+ "subscriptions"
+ "telephonyClient"
- "C"
- "com.apple.purplebuddy.launchMigrationSourceUI"

```
