## Moments

> `/System/Library/PrivateFrameworks/Moments.framework/Moments`

```diff

-205.0.1.0.0
-  __TEXT.__text: 0x4e24c
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0x57e0
-  __TEXT.__cstring: 0xa7bc
+206.0.7.0.0
+  __TEXT.__text: 0x4e2e8
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__objc_methlist: 0x5cfc
+  __TEXT.__cstring: 0xa7f3
   __TEXT.__const: 0x360
-  __TEXT.__oslogstring: 0x4a2f
+  __TEXT.__oslogstring: 0x495d
   __TEXT.__gcc_except_tab: 0x384
-  __TEXT.__unwind_info: 0x1078
-  __TEXT.__objc_classname: 0x86a
-  __TEXT.__objc_methname: 0xd53b
-  __TEXT.__objc_methtype: 0x189e
-  __TEXT.__objc_stubs: 0x7a20
-  __DATA_CONST.__got: 0x4b0
-  __DATA_CONST.__const: 0x2438
-  __DATA_CONST.__objc_classlist: 0x270
+  __TEXT.__unwind_info: 0x1098
+  __TEXT.__objc_classname: 0x88d
+  __TEXT.__objc_methname: 0xd76b
+  __TEXT.__objc_methtype: 0x18ca
+  __TEXT.__objc_stubs: 0x7b00
+  __DATA_CONST.__got: 0x4c0
+  __DATA_CONST.__const: 0x24e0
+  __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c18
+  __DATA_CONST.__objc_selrefs: 0x2cf0
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x238
+  __DATA_CONST.__objc_superrefs: 0x248
   __DATA_CONST.__objc_arraydata: 0x358
-  __AUTH_CONST.__auth_got: 0x380
+  __AUTH_CONST.__auth_got: 0x388
   __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0xca60
-  __AUTH_CONST.__objc_const: 0x9ef0
+  __AUTH_CONST.__cfstring: 0xcac0
+  __AUTH_CONST.__objc_const: 0x9ae0
   __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1810
-  __DATA.__objc_ivar: 0x730
+  __DATA.__objc_ivar: 0x748
   __DATA.__data: 0xb20
   __DATA.__bss: 0xe8
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2117
-  Symbols:   3435
-  CStrings:  4624
+  Functions: 2143
+  Symbols:   3479
+  CStrings:  4650
 
Symbols:
+ _OBJC_CLASS_$_MOCategoryUsage
+ _OBJC_CLASS_$_MOEventScreenTime
+ _OBJC_METACLASS_$_MOCategoryUsage
+ _OBJC_METACLASS_$_MOEventScreenTime
+ _kMOEventCategoryUsage
+ _kMOEventCategoryUsageAppCategory
+ _kMOEventCategoryUsageDuration
+ _kMOEventLongestScreenTimeEndDate
+ _kMOEventLongestScreenTimeStartDate
+ _kMOKeyPersonGivenName
+ _objc_retainAutoreleasedReturnValue
- _kMOAddressFormatOptionCurrentFormat
- _kMOAddressFormatOptionCurrentFormatCountryCode
- _kMOAddressFormatOptionCurrentFormatDisplayLanguage
CStrings:
+ "\x161"
+ "\x17!\x1f\x01"
+ "%@, format option, %@, output string, %@, AOI List, %@"
+ "@\"MOEventScreenTime\""
+ "B56@0:8@16@24@32d40d48"
+ "Creativity"
+ "Game"
+ "MOCategoryUsage"
+ "MOEventScreenTime"
+ "Networking"
+ "OtherUnknown"
+ "ReadingAndReference"
+ "ShoppingAndFood"
+ "System"
+ "SystemBlockable"
+ "SystemHidden"
+ "SystemUnblockable"
+ "T@\"MOEventScreenTime\",&,N,V_screenTimeEvent"
+ "T@\"NSArray\",&,N,V_appCategoryUsages"
+ "T@\"NSDateInterval\",&,N,V_longestActivity"
+ "T@\"NSNumber\",&,N,V_duration"
+ "T@\"NSString\",&,N,V_givenName"
+ "TQ,N,V_appCategory"
+ "_appCategory"
+ "_appCategoryUsages"
+ "_givenName"
+ "_longestActivity"
+ "_screenTimeEvent"
+ "app category, %@, duration, %f"
+ "app usages, %@, longest activity, %@"
+ "appCategory"
+ "appCategoryUsages"
+ "areaOfInterests"
+ "calling localizeEventBundles"
+ "categoryUsages"
+ "descriptionOfAppCategory:"
+ "eventCategoryUsage"
+ "eventCategoryUsageAppCategory"
+ "eventCategoryUsageDuration"
+ "eventLongestScreenTimeEndDate"
+ "eventLongestScreenTimeStartDate"
+ "fallbackToAddressFormattingWithFormatOption:preferredCategories:poiCategoryBlocklist:mediumConfidenceThreshold:aoiConfidenceThreshold:"
+ "givenName"
+ "longestActivity"
+ "screenTimeEvent"
+ "setAppCategory:"
+ "setAppCategoryUsages:"
+ "setDuration:"
+ "setGivenName:"
+ "setLongestActivity:"
+ "setScreenTimeEvent:"
+ "structuredAddress"
- "\x151"
- "\x17!\x1f"
- "%@, country code, %@, using current format output string, %@"
- "%@, country code, %@, using parking display name output string, %@, fallback, %i"
- "%@, short address format doesn't support the administrative area (state), option, %@, will use default"
- "MOAction.m"
- "MOAppEngagementReporter.m"
- "MODefaultsManager.m"
- "MODictionaryEncoder.m"
- "MOEvent.m"
- "MOEventBundle.m"
- "MOEventBundleLabelCondition.m"
- "MOEventBundleLabelFormat.m"
- "MOEventBundleLabelLocalizer.m"
- "MOEventBundleLabelTemplate.m"
- "MOEventExtendedAtrributes.m"
- "MOInteraction.m"
- "MOMediaPlaySession.m"
- "MOPlace.m"
- "MOResource.m"
- "MOTime.m"
- "MOXPCContext.m"
- "US"
- "calling localizeEventBundlesForReplayWithOptions"
- "country"
- "countryCode"
- "currentFormat"
- "formatAddressCurrentFormatWithFallback:"
- "getPreferredName"
- "locality"

```
