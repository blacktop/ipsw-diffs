## AACCore

> `/System/Library/PrivateFrameworks/AACCore.framework/AACCore`

```diff

-14.1.2.1.0
-  __TEXT.__text: 0xdf50
+14.2.3.0.0
+  __TEXT.__text: 0xe130
   __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x122c
+  __TEXT.__objc_methlist: 0xfdc
   __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0xd34
+  __TEXT.__cstring: 0xd61
   __TEXT.__oslogstring: 0x506
-  __TEXT.__gcc_except_tab: 0x144
-  __TEXT.__unwind_info: 0x5c8
-  __TEXT.__objc_classname: 0x8a4
-  __TEXT.__objc_methname: 0x28a3
-  __TEXT.__objc_methtype: 0x810
-  __TEXT.__objc_stubs: 0x17a0
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x600
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __TEXT.__gcc_except_tab: 0x158
+  __TEXT.__unwind_info: 0x550
+  __TEXT.__objc_classname: 0x872
+  __TEXT.__objc_methname: 0x2636
+  __TEXT.__objc_methtype: 0x878
+  __TEXT.__objc_stubs: 0x1a00
+  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__const: 0x610
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0xd8
+  __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x878
+  __DATA_CONST.__objc_selrefs: 0x880
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x108
   __AUTH_CONST.__auth_got: 0x2d0
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0xd20
-  __AUTH_CONST.__objc_const: 0x4928
-  __AUTH.__objc_data: 0xe60
-  __DATA.__objc_ivar: 0x194
-  __DATA.__data: 0xa40
+  __AUTH_CONST.__cfstring: 0xdc0
+  __AUTH_CONST.__objc_const: 0x40d0
+  __AUTH.__objc_data: 0xe10
+  __DATA.__objc_ivar: 0x1b4
+  __DATA.__data: 0x9e0
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x230
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 501
-  Symbols:   709
-  CStrings:  778
+  Functions: 449
+  Symbols:   666
+  CStrings:  757
 
Symbols:
+ _AEAssessmentPreferenceDomain
+ _AEPreferencesDidChangeNotificationName
+ _CFNotificationCenterPostNotification
+ _OBJC_CLASS_$_AEConcretePreferencePrimitives
+ _OBJC_CLASS_$_AEConcreteSystemNotificationPrimitives
+ _OBJC_CLASS_$_AEPreference
+ _OBJC_CLASS_$_AEPreferences
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_METACLASS_$_AEConcretePreferencePrimitives
+ _OBJC_METACLASS_$_AEConcreteSystemNotificationPrimitives
+ _OBJC_METACLASS_$_AEPreference
+ _OBJC_METACLASS_$_AEPreferences
+ ___kCFBooleanFalse
- _CFBooleanGetValue
- _OBJC_CLASS_$_AEPreferencesProvider
- _OBJC_METACLASS_$_AEPreferencesProvider
- _kCFBooleanFalse
- _kCFBooleanTrue
CStrings:
+ "@"
+ "@\"<AEObservation>\"40@0:8@\"NSString\"16@\"NSObject<OS_dispatch_queue>\"24@?<v@?>32"
+ "@\"NSMapTable\""
+ "@24@0:8@\"NSString\"16"
+ "@40@0:8@16@24@32"
+ "AEPreference"
+ "AEPreference.m"
+ "CaptureDisplays"
+ "CreateAssessmentFile"
+ "CustomHomeScreenLayout"
+ "DisableContinuity"
+ "DisableDication"
+ "DisableQuickNote"
+ "DisableSiri"
+ "DisableTrackpadLookup"
+ "ElevateWindows"
+ "EnforceSingleAppMode"
+ "EnterSandbox"
+ "FailOnDeactivation"
+ "ForceScreenMirroring"
+ "KillingAgentRemotely"
+ "NetworkPolicyExemptExecutablePaths"
+ "PresentShields"
+ "RestrictContentCapture"
+ "RestrictFrontmostApp"
+ "RestrictMedia"
+ "RestrictNetworkAccess"
+ "ScrubPasteboard"
+ "ShowPromptsAndBanners"
+ "StopAirPlayBeforehand"
+ "T@\"<AEObservation>\",R,N,V_notificationObservation"
+ "T@\"<AEPreferencePrimitives>\",R,N,V_preferencePrimitives"
+ "T@\"<AESystemNotificationPrimitives>\",R,N,V_systemNotificationPrimitives"
+ "T@\"AEPreference\",R,N"
+ "T@\"NSMapTable\",R,N,V_cachedPreferencesByKey"
+ "T@\"NSString\",R,C,N,V_key"
+ "T@,&,N"
+ "T@,C,N,V_value"
+ "T@,R,N,V_defaultValue"
+ "TB,R,N,GisOverridden,V_overridden"
+ "Value should be PropertyListType"
+ "_cachedPreferencesByKey"
+ "_defaultValue"
+ "_key"
+ "_notificationObservation"
+ "_overridden"
+ "_preferencePrimitives"
+ "_value"
+ "allObjects"
+ "cachedPreferencesByKey"
+ "com.apple.assessmentmode.preferencesDidChangeNotification"
+ "createAssessmentFile"
+ "defaultPreferences"
+ "defaultValue"
+ "initWithDomain:"
+ "initWithKey:preferencesPrimitives:systemNotificationPrimitives:defaultValue:"
+ "initWithPreferencePrimitives:systemNotificationPrimitives:queue:"
+ "isBeingTested"
+ "isOverridden"
+ "key"
+ "networkPolicyExemptExecutablePaths"
+ "notificationObservation"
+ "objectEnumerator"
+ "objectForKey:"
+ "observeSystemNotificationWithName:onQueue:withHandler:"
+ "overridden"
+ "postSystemNotificationWithName:"
+ "preferenceDidUpdate"
+ "preferenceForKey:defaultArrayValue:"
+ "preferenceForKey:defaultNumberValue:"
+ "preferencePrimitives"
+ "preferenceValue"
+ "preferencesDidUpdate"
+ "preferencesWithPreferencePrimitives:systemNotificationPrimitives:queue:"
+ "propertyList:isValidForFormat:"
+ "setObject:forKey:"
+ "setPreferenceValue:"
+ "setValue:"
+ "strongToWeakObjectsMapTable"
+ "systemNotificationPrimitives"
+ "v24@0:8@\"NSString\"16"
+ "v32@0:8@\"NSObject\"16@\"NSString\"24"
+ "value"
- "@\"NSNumber\"24@0:8@\"NSString\"16"
- "AEConcretePreferences"
- "AEEmptyPreferences"
- "AEPreferencesProvider"
- "FailOnDeactivationKey"
- "IgnoreCaptureDisplays"
- "IgnoreCustomHomeScreenLayout"
- "IgnoreDisableContinuity"
- "IgnoreDisableDication"
- "IgnoreDisableQuickNote"
- "IgnoreDisableSiri"
- "IgnoreDisableTrackpadLookup"
- "IgnoreElevateWindows"
- "IgnoreEnforceSingleAppMode"
- "IgnoreEnterSandbox"
- "IgnoreForceScreenMirroring"
- "IgnorePresentShields"
- "IgnoreRestrictContentCapture"
- "IgnoreRestrictFrontmostApp"
- "IgnoreRestrictMedia"
- "IgnoreRestrictNetworkAccess"
- "IgnoreScrubPasteboard"
- "IgnoreShowPromptsAndBanners"
- "IgnoreStopAirPlayBeforehand"
- "PortalDemoModeActive"
- "TB,N,GisPortalDemoModeActive"
- "TB,N,GshouldAllowRemotelyKillingAgent"
- "TB,N,GshouldCaptureDisplays"
- "TB,N,GshouldDisableContinuity"
- "TB,N,GshouldDisableDictation"
- "TB,N,GshouldDisableQuickNote"
- "TB,N,GshouldDisableSiri"
- "TB,N,GshouldDisableTrackpadLookup"
- "TB,N,GshouldElevateWindows"
- "TB,N,GshouldEnforceSingleAppMode"
- "TB,N,GshouldEnterSandbox"
- "TB,N,GshouldFailOnDeactivation"
- "TB,N,GshouldForceScreenMirroring"
- "TB,N,GshouldPresentShields"
- "TB,N,GshouldRestrictContentCapture"
- "TB,N,GshouldRestrictFrontmostApp"
- "TB,N,GshouldRestrictMedia"
- "TB,N,GshouldRestrictNetworkAccess"
- "TB,N,GshouldScrubPasteboard"
- "TB,N,GshouldSetCustomHomeScreenLayout"
- "TB,N,GshouldShowPromptsAndBanners"
- "TB,N,GshouldStopAirPlayBeforehand"
- "Td,N"
- "_primitives"
- "boolForKey:"
- "d16@0:8"
- "doubleValue"
- "isPortalDemoModeActive"
- "makePreferences"
- "numberForKey:"
- "observeAssessmentStateChangeOnQueue:withHandler:"
- "portalDemoModeActive"
- "setAllowRemotelyKillingAgent:"
- "setBool:forKey:"
- "setCaptureDisplays:"
- "setDisableContinuity:"
- "setDisableDictation:"
- "setDisableQuickNote:"
- "setDisableSiri:"
- "setDisableTrackpadLookup:"
- "setElevateWindows:"
- "setEnforceSingleAppMode:"
- "setEnterSandbox:"
- "setExpirationTime:"
- "setFailOnDeactivation:"
- "setForceScreenMirroring:"
- "setNumber:forKey:"
- "setPortalDemoModeActive:"
- "setPresentShields:"
- "setRestrictContentCapture:"
- "setRestrictFrontmostApp:"
- "setRestrictMedia:"
- "setRestrictNetworkAccess:"
- "setScrubPasteboard:"
- "setSetCustomHomeScreenLayout:"
- "setShowPromptsAndBanners:"
- "setStopAirPlayBeforehand:"
- "shouldAllowRemotelyKillingAgent"
- "shouldDisableContinuity"
- "shouldDisableDictation"
- "shouldDisableQuickNote"
- "shouldDisableSiri"
- "shouldDisableTrackpadLookup"
- "shouldElevateWindows"
- "shouldEnforceSingleAppMode"
- "shouldEnterSandbox"
- "shouldFailOnDeactivation"
- "shouldForceScreenMirroring"
- "shouldPresentShields"
- "shouldRestrictContentCapture"
- "shouldRestrictFrontmostApp"
- "shouldRestrictMedia"
- "shouldRestrictNetworkAccess"
- "shouldScrubPasteboard"
- "shouldSetCustomHomeScreenLayout"
- "shouldShowPromptsAndBanners"
- "shouldStopAirPlayBeforehand"
- "v24@0:8d16"
- "v32@0:8@\"NSNumber\"16@\"NSString\"24"

```
