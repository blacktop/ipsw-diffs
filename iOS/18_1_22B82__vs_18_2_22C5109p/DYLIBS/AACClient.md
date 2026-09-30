## AACClient

> `/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient`

```diff

-14.1.2.1.0
-  __TEXT.__text: 0x1a32c
-  __TEXT.__auth_stubs: 0xee0
+14.2.3.0.0
+  __TEXT.__text: 0x1a4ec
+  __TEXT.__auth_stubs: 0xef0
   __TEXT.__objc_methlist: 0x614
-  __TEXT.__const: 0x1420
+  __TEXT.__const: 0x1430
   __TEXT.__cstring: 0x17d9
-  __TEXT.__swift5_typeref: 0xdf3
-  __TEXT.__swift5_reflstr: 0x92b
+  __TEXT.__swift5_typeref: 0xe3f
+  __TEXT.__swift5_reflstr: 0x96b
   __TEXT.__swift5_assocty: 0xc8
-  __TEXT.__constg_swiftt: 0x134c
+  __TEXT.__constg_swiftt: 0x135c
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_fieldmd: 0x8f4
+  __TEXT.__swift5_fieldmd: 0x90c
   __TEXT.__swift5_proto: 0xc4
   __TEXT.__swift5_types: 0xb0
   __TEXT.__swift5_capture: 0x5e0

   __TEXT.__oslogstring: 0x36a
   __TEXT.__unwind_info: 0x880
   __TEXT.__eh_frame: 0x128
-  __TEXT.__objc_classname: 0x237
-  __TEXT.__objc_methname: 0x1adb
-  __TEXT.__objc_methtype: 0x7be
+  __TEXT.__objc_classname: 0x25f
+  __TEXT.__objc_methname: 0x1339
+  __TEXT.__objc_methtype: 0x84e
   __TEXT.__objc_stubs: 0x5a0
-  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__got: 0x238
   __DATA_CONST.__const: 0x158
   __DATA_CONST.__objc_classlist: 0xa8
-  __DATA_CONST.__objc_protolist: 0x180
+  __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e0
-  __DATA_CONST.__objc_protorefs: 0xc0
+  __DATA_CONST.__objc_selrefs: 0x400
+  __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x778
+  __AUTH_CONST.__auth_got: 0x780
   __AUTH_CONST.__auth_ptr: 0x308
-  __AUTH_CONST.__const: 0x1cd8
-  __AUTH_CONST.__objc_const: 0x2d20
+  __AUTH_CONST.__const: 0x1cf0
+  __AUTH_CONST.__objc_const: 0x2678
   __AUTH.__objc_data: 0x710
   __AUTH.__data: 0xc10
   __DATA.__objc_ivar: 0x38
-  __DATA.__data: 0x1148
+  __DATA.__data: 0x11a8
   __DATA.__bss: 0x1100
   __DATA.__common: 0x80
   - /System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACDependencies.framework/AACDependencies

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 913
-  Symbols:   305
-  CStrings:  562
+  Symbols:   310
+  CStrings:  483
 
Symbols:
+ _AEAssessmentPreferenceDomain
+ _OBJC_CLASS_$_AEConcretePreferencePrimitives
+ _OBJC_CLASS_$_AEConcreteSystemNotificationPrimitives
+ _OBJC_CLASS_$_AEOSGestalt
+ _OBJC_CLASS_$_AEPreferences
+ _objc_release_x10
- _OBJC_CLASS_$_AEPreferencesProvider
CStrings:
+ "@\"<AEObservation>\"40@0:8@\"NSString\"16@\"OS_dispatch_queue\"24@?<v@?>32"
+ "@24@0:8@\"NSString\"16"
+ "@40@0:8@16@24@?32"
+ "AEPreferencePrimitives"
+ "AESystemNotificationPrimitives"
+ "defaultPreferences"
+ "initWithDomain:"
+ "isBeingTested"
+ "isInternalOS"
+ "objectForKey:"
+ "observeSystemNotificationWithName:onQueue:withHandler:"
+ "postSystemNotificationWithName:"
+ "preferencesWithPreferencePrimitives:systemNotificationPrimitives:queue:"
+ "setObject:forKey:"
+ "v24@0:8@\"NSString\"16"
+ "v32@0:8@\"NSObject\"16@\"NSString\"24"
- "AEPreferences"
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
- "allowRemotelyKillingAgent"
- "captureDisplays"
- "d16@0:8"
- "disableContinuity"
- "disableDictation"
- "disableQuickNote"
- "disableSiri"
- "disableTrackpadLookup"
- "elevateWindows"
- "enforceSingleAppMode"
- "enterSandbox"
- "expirationTime"
- "failOnDeactivation"
- "forceScreenMirroring"
- "isPortalDemoModeActive"
- "makePreferences"
- "portalDemoModeActive"
- "presentShields"
- "restrictContentCapture"
- "restrictFrontmostApp"
- "restrictMedia"
- "restrictNetworkAccess"
- "scrubPasteboard"
- "setAllowRemotelyKillingAgent:"
- "setCaptureDisplays:"
- "setCustomHomeScreenLayout"
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
- "shouldCaptureDisplays"
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
- "showPromptsAndBanners"
- "stopAirPlayBeforehand"
- "v24@0:8d16"

```
