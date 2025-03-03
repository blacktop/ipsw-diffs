## SetupAssistant

> `/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant`

```diff

-5355.6.0.0.0
-  __TEXT.__text: 0x3ef4c
-  __TEXT.__auth_stubs: 0xd50
-  __TEXT.__objc_methlist: 0x3254
-  __TEXT.__const: 0x128
-  __TEXT.__gcc_except_tab: 0xec0
-  __TEXT.__oslogstring: 0x54f8
-  __TEXT.__cstring: 0x2ae5
+5359.4.9.100.0
+  __TEXT.__text: 0x40c28
+  __TEXT.__auth_stubs: 0xd80
+  __TEXT.__objc_methlist: 0x3c6c
+  __TEXT.__const: 0x138
+  __TEXT.__gcc_except_tab: 0xf30
+  __TEXT.__oslogstring: 0x5829
+  __TEXT.__cstring: 0x2b66
   __TEXT.__dlopen_cstrs: 0x1245
-  __TEXT.__unwind_info: 0x10f0
-  __TEXT.__objc_classname: 0x79b
-  __TEXT.__objc_methname: 0xa102
-  __TEXT.__objc_methtype: 0x1116
-  __TEXT.__objc_stubs: 0x7a00
-  __DATA_CONST.__got: 0x4e8
-  __DATA_CONST.__const: 0x1618
-  __DATA_CONST.__objc_classlist: 0x1c8
+  __TEXT.__unwind_info: 0x1190
+  __TEXT.__objc_classname: 0x7ce
+  __TEXT.__objc_methname: 0xa832
+  __TEXT.__objc_methtype: 0x113b
+  __TEXT.__objc_stubs: 0x7f20
+  __DATA_CONST.__got: 0x518
+  __DATA_CONST.__const: 0x1610
+  __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2728
+  __DATA_CONST.__objc_selrefs: 0x2960
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x130
+  __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0x178
-  __AUTH_CONST.__auth_got: 0x6b8
+  __AUTH_CONST.__auth_got: 0x6d0
   __AUTH_CONST.__const: 0xa40
-  __AUTH_CONST.__cfstring: 0x2f60
-  __AUTH_CONST.__objc_const: 0x6768
+  __AUTH_CONST.__cfstring: 0x2f80
+  __AUTH_CONST.__objc_const: 0x5c08
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x37c
+  __AUTH.__objc_data: 0x3c0
+  __DATA.__objc_ivar: 0x3a8
   __DATA.__data: 0x970
   __DATA.__bss: 0x5c0
   __DATA_DIRTY.__objc_data: 0xeb0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1591
-  Symbols:   2207
-  CStrings:  2935
+  Functions: 1667
+  Symbols:   2295
+  CStrings:  3035
 
Symbols:
+ OBJC_IVAR_$_BYLocationController.forceGuessedCountries
+ _OBJC_CLASS_$_BYCellularNetworkInformation
+ _OBJC_CLASS_$_BYSIMRegionService
+ _OBJC_CLASS_$_CTXPCServiceSubscriptionContext
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_METACLASS_$_BYCellularNetworkInformation
+ _OBJC_METACLASS_$_BYSIMRegionService
+ ___NSArray0__struct
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_retainAutoreleasedReturnValue
- _BYPrivacySubscriptionBundleIdentifier
CStrings:
+ "\x04C"
+ "%s: %{public}@ -> %{public}@"
+ "%s: exception = %{public}@"
+ "%s: following E major = %d"
+ "-"
+ "-[BYChronicleEntry hasCrossedEBoundarySinceCreationForCurrentProductVersion:]"
+ "@\"CoreTelephonyClient\""
+ "@32@0:8q16q24"
+ "AgeAttestationPhase1"
+ "AuthKit"
+ "B\x11"
+ "BYCellularNetworkInformation"
+ "BYSIMRegionService"
+ "Creating new chronicle..."
+ "D"
+ "Error getting ISO code from MCC: %@, error: %@"
+ "Error getting subregion ISO code from MCC: %@, MNC: %@, error: %@"
+ "Error reading telephony network information { error: %@ }"
+ "Getting subregion languages for Home Region"
+ "Getting subregion languages for Network Region"
+ "Home subregion languages: %@"
+ "Language codes for region %@, subregion %@: %@"
+ "MDMFlowControllerAdoption"
+ "Network subregion languages: %@"
+ "No guessed region found and forcing guessed country from location."
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
+ "Unable to read chronicle data; found %@, expected NSDictionary!"
+ "_dictionaryRepresentationForBackedUpFeatures:"
+ "_homeCountryISOCode"
+ "_homeMCC"
+ "_homeMNC"
+ "_homeSubregionISOCodes"
+ "_isBackedUpFeature:"
+ "_languagesForRegionsUsingSIMRegionService:"
+ "_mgProductType"
+ "_networkCountryISOCode"
+ "_networkMCC"
+ "_networkMNC"
+ "_networkSubregionISOCodes"
+ "_parseChronicleFeaturesFromPreferences:includeCache:"
+ "_subregionLanguagesForRegion:subregionsISOCodes:"
+ "_telephonyClient"
+ "addObjectsFromArray:"
+ "cellularNetworkInformation"
+ "com.apple.private.restrict-post.purplebuddy.launchMigrationSourceUI"
+ "copyMobileNetworkCode:error:"
+ "copyMobileSubscriberCountryCode:error:"
+ "copyMobileSubscriberIsoSubregionCode:MNC:error:"
+ "copyMobileSubscriberNetworkCode:error:"
+ "forceGuessedCountries"
+ "getActiveContexts:"
+ "hasCrossedEBoundarySinceCreationForCurrentProductVersion:"
+ "homeCountryISOCode"
+ "homeMCC"
+ "homeMNC"
+ "homeSubregionISOCodes"
+ "initFromBackedUpPreferences:andNotBackedUpPreferences:"
+ "initFromBackedUpPreferences:andNotBackedUpPreferences:includeCache:"
+ "initWithCapacity:"
+ "initWithSlot:"
+ "isAgeAttestationPhase1Enabled"
+ "isMDMEnrollmentFlowControllerAdoptionEnabled"
+ "isoCodeForMCC:"
+ "languagesForRegion:subdivision:withThreshold:filter:"
+ "logTelephonyError:"
+ "lowercaseString"
+ "mgProductType"
+ "myselfChild"
+ "networkCountryISOCode"
+ "networkMCC"
+ "networkMNC"
+ "networkSubregionISOCodes"
+ "persistBackedUpFeaturesInPreferences:andNotBackedFeaturesInPreferences:persistImmediately:"
+ "persistKeys:"
+ "removeRecordForFeature:"
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
- "\x043"
- "C"
- "com.apple.onboarding.subscriptionbundle"
- "com.apple.purplebuddy.launchMigrationSourceUI"

```
