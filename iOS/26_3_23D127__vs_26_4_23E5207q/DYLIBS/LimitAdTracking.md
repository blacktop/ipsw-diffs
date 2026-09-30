## LimitAdTracking

> `/System/Library/PrivateFrameworks/LimitAdTracking.framework/LimitAdTracking`

```diff

-637.2.3.0.0
-  __TEXT.__text: 0x3a10
-  __TEXT.__auth_stubs: 0x1a0
+637.4.6.0.0
+  __TEXT.__text: 0x3b10
+  __TEXT.__auth_stubs: 0x150
   __TEXT.__objc_methlist: 0x270
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x9c

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x288
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0xe0
+  __AUTH_CONST.__auth_got: 0xb8
   __AUTH_CONST.__const: 0x280
   __AUTH_CONST.__cfstring: 0x280
   __AUTH_CONST.__objc_const: 0x3d0

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 267B4C47-1F7E-3FCF-9D85-917058C4D9F4
+  UUID: 3E640F59-2480-3E5B-8889-64CC8DE8BBBD
   Functions: 71
-  Symbols:   314
+  Symbols:   309
   CStrings:  204
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x22
- _objc_retain_x8
Functions:
~ -[ADTrackingTransparency personalizedAds] : 96 -> 100
~ -[ADTrackingTransparency personalizedAdsSwitchEnabled] : 368 -> 380
~ -[ADTrackingTransparency _userAllowedToChangeSettings] : 524 -> 528
~ -[ADTrackingTransparency _isUserEDURestricted] : 112 -> 120
~ -[ADTrackingTransparency _isUserManagedRestricted] : 148 -> 164
~ -[ADTrackingTransparency acknowledgedVersionForPersonalizedAds] : 112 -> 116
~ -[ADTrackingTransparency crossAppTrackingAllowedSwitchEnabled] : 356 -> 368
~ -[ADTrackingTransparency accountLevelSwitchDisabledReason] : 540 -> 548
~ -[ADTrackingTransparency shouldDisplayPAUI] : 544 -> 552
~ -[ADTrackingTransparency adSwitchDisabledReasons] : 528 -> 568
~ -[ADTrackingTransparency crossAppTrackingAllowedSwitchDisabledReason] : 304 -> 308
~ -[ADTrackingTransparency crossAppTrackingAllowed] : 96 -> 100
~ -[ADTrackingTransparency setCrossAppTrackingAllowed:] : 100 -> 104
~ -[ADTrackingTransparency personalizedAdsSwitchDisabledReason] : 416 -> 420
~ -[ADTrackingTransparency personalizedAdsAvailable:] : 456 -> 464
~ ___51-[ADTrackingTransparency personalizedAdsAvailable:]_block_invoke.54 : 220 -> 224
~ -[ADTrackingTransparency personalizedAdsAvailableForAdPlatforms] : 120 -> 124
~ -[ADTrackingTransparency setAcknowledgedVersionForPersonalizedAds:] : 144 -> 148
~ -[ADTrackingTransparency latestVersionForPersonalizedAdsConsent] : 120 -> 124
~ -[ADTrackingTransparency setPersonalizedAds:] : 400 -> 408
~ ___45-[ADTrackingTransparency setPersonalizedAds:]_block_invoke.68 : 220 -> 224
~ ___50-[ADTrackingTransparency appTrackingServiceProxy:]_block_invoke : 220 -> 224
~ -[APLocalEnforcementManager disabledReasons] : 380 -> 412
~ -[APLocalEnforcementManager adServicesEnabled:] : 576 -> 580
~ ___47-[APLocalEnforcementManager adServicesEnabled:]_block_invoke.10 : 304 -> 312
~ -[APLocalEnforcementManager deviceRegionStorefrontEnabled] : 540 -> 548
~ -[APLocalEnforcementManager isU13MAIDEDU] : 228 -> 244
~ -[APLocalEnforcementManager accountStorefront] : 616 -> 620
~ ___53-[APLocalEnforcementManager appTrackingServiceProxy:]_block_invoke : 220 -> 224
~ -[APLocalEnforcementManager shouldShowTCCWithAds] : 540 -> 548

```
