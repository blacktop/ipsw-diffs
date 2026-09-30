## AdCore

> `/System/Library/PrivateFrameworks/AdCore.framework/AdCore`

```diff

-638.2.0.0.0
-  __TEXT.__text: 0x304f4
-  __TEXT.__objc_methlist: 0x42d4
+638.2.2.0.0
+  __TEXT.__text: 0x30d44
+  __TEXT.__objc_methlist: 0x4494
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x405d
+  __TEXT.__cstring: 0x40a2
   __TEXT.__gcc_except_tab: 0x4c4
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0xe60
+  __TEXT.__unwind_info: 0xeb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x6f0
-  __DATA_CONST.__objc_classlist: 0x188
+  __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x20f8
+  __DATA_CONST.__objc_selrefs: 0x2198
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x178
+  __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x188
-  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__got: 0x3c8
   __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x4da0
-  __AUTH_CONST.__objc_const: 0x6c40
+  __AUTH_CONST.__cfstring: 0x4e00
+  __AUTH_CONST.__objc_const: 0x7a88
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0x4b0
-  __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x418
-  __DATA.__data: 0x300
+  __AUTH.__objc_data: 0x5f0
+  __DATA.__objc_ivar: 0x434
+  __DATA.__data: 0x420
   __DATA_DIRTY.__objc_data: 0xaf0
-  __DATA_DIRTY.__bss: 0x240
+  __DATA_DIRTY.__bss: 0x250
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1454
-  Symbols:   3046
-  CStrings:  661
+  Functions: 1481
+  Symbols:   3150
+  CStrings:  664
 
Symbols:
+ +[ADAccountQualityDiagnosticSample sampleWithBirthYearValidity:personalizedAdsStatus:storefrontID:]
+ +[ADAccountQualityDiagnostics(Production) production]
+ -[ADAccountQualityDiagnosticSample .cxx_destruct]
+ -[ADAccountQualityDiagnosticSample birthYearValidity]
+ -[ADAccountQualityDiagnosticSample initWithBirthYearValidity:personalizedAdsStatus:storefrontID:]
+ -[ADAccountQualityDiagnosticSample personalizedAdsStatus]
+ -[ADAccountQualityDiagnosticSample setBirthYearValidity:]
+ -[ADAccountQualityDiagnosticSample setPersonalizedAdsStatus:]
+ -[ADAccountQualityDiagnosticSample setStorefrontID:]
+ -[ADAccountQualityDiagnosticSample storefrontID]
+ -[ADAccountQualityDiagnostics .cxx_destruct]
+ -[ADAccountQualityDiagnostics birthYearValidityForAccount:]
+ -[ADAccountQualityDiagnostics birthYearValidityForConsumerAccount:]
+ -[ADAccountQualityDiagnostics birthYearValidityForRestrictedAccount:]
+ -[ADAccountQualityDiagnostics captureAccount:]
+ -[ADAccountQualityDiagnostics clock]
+ -[ADAccountQualityDiagnostics depot]
+ -[ADAccountQualityDiagnostics initWithClock:depot:personalizedAdsSource:storefrontIDSource:]
+ -[ADAccountQualityDiagnostics personalizedAdsSource]
+ -[ADAccountQualityDiagnostics storefrontIDSource]
+ -[ADCoreAnalyticsAccountQualityDiagnosticDepot depositSample:]
+ -[ADCoreSettingsPersonalizedAdsSource personalizedAds]
+ -[ADSystemClock now]
+ -[DSIDRecord(Helpers) isConsumer]
+ -[DSIDRecord(Helpers) isRestricted]
+ _NSCalendarIdentifierGregorian
+ _OBJC_CLASS_$_ADAccountQualityDiagnosticSample
+ _OBJC_CLASS_$_ADAccountQualityDiagnostics
+ _OBJC_CLASS_$_ADCoreAnalyticsAccountQualityDiagnosticDepot
+ _OBJC_CLASS_$_ADCoreSettingsPersonalizedAdsSource
+ _OBJC_CLASS_$_ADSystemClock
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_IVAR_$_ADAccountQualityDiagnosticSample._birthYearValidity
+ _OBJC_IVAR_$_ADAccountQualityDiagnosticSample._personalizedAdsStatus
+ _OBJC_IVAR_$_ADAccountQualityDiagnosticSample._storefrontID
+ _OBJC_IVAR_$_ADAccountQualityDiagnostics._clock
+ _OBJC_IVAR_$_ADAccountQualityDiagnostics._depot
+ _OBJC_IVAR_$_ADAccountQualityDiagnostics._personalizedAdsSource
+ _OBJC_IVAR_$_ADAccountQualityDiagnostics._storefrontIDSource
+ _OBJC_METACLASS_$_ADAccountQualityDiagnosticSample
+ _OBJC_METACLASS_$_ADAccountQualityDiagnostics
+ _OBJC_METACLASS_$_ADCoreAnalyticsAccountQualityDiagnosticDepot
+ _OBJC_METACLASS_$_ADCoreSettingsPersonalizedAdsSource
+ _OBJC_METACLASS_$_ADSystemClock
+ __OBJC_$_CLASS_METHODS_ADAccountQualityDiagnosticSample
+ __OBJC_$_CLASS_METHODS_ADAccountQualityDiagnostics(Production)
+ __OBJC_$_INSTANCE_METHODS_ADAccountQualityDiagnosticSample
+ __OBJC_$_INSTANCE_METHODS_ADAccountQualityDiagnostics
+ __OBJC_$_INSTANCE_METHODS_ADCoreAnalyticsAccountQualityDiagnosticDepot
+ __OBJC_$_INSTANCE_METHODS_ADCoreSettingsPersonalizedAdsSource
+ __OBJC_$_INSTANCE_METHODS_ADSystemClock
+ __OBJC_$_INSTANCE_METHODS_DSIDRecord(Helpers)
+ __OBJC_$_INSTANCE_VARIABLES_ADAccountQualityDiagnosticSample
+ __OBJC_$_INSTANCE_VARIABLES_ADAccountQualityDiagnostics
+ __OBJC_$_PROP_LIST_ADAccountQualityDiagnosticSample
+ __OBJC_$_PROP_LIST_ADAccountQualityDiagnostics
+ __OBJC_$_PROP_LIST_ADCoreAnalyticsAccountQualityDiagnosticDepot
+ __OBJC_$_PROP_LIST_ADCoreSettingsPersonalizedAdsSource
+ __OBJC_$_PROP_LIST_ADSystemClock
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ADAccountQualityDiagnosticDepot
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ADClock
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ADPersonalizedAdsSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ADAccountQualityDiagnosticDepot
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ADClock
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ADPersonalizedAdsSource
+ __OBJC_$_PROTOCOL_REFS_ADAccountQualityDiagnosticDepot
+ __OBJC_$_PROTOCOL_REFS_ADClock
+ __OBJC_$_PROTOCOL_REFS_ADPersonalizedAdsSource
+ __OBJC_CLASS_PROTOCOLS_$_ADCoreAnalyticsAccountQualityDiagnosticDepot
+ __OBJC_CLASS_PROTOCOLS_$_ADCoreSettingsPersonalizedAdsSource
+ __OBJC_CLASS_PROTOCOLS_$_ADSystemClock
+ __OBJC_CLASS_RO_$_ADAccountQualityDiagnosticSample
+ __OBJC_CLASS_RO_$_ADAccountQualityDiagnostics
+ __OBJC_CLASS_RO_$_ADCoreAnalyticsAccountQualityDiagnosticDepot
+ __OBJC_CLASS_RO_$_ADCoreSettingsPersonalizedAdsSource
+ __OBJC_CLASS_RO_$_ADSystemClock
+ __OBJC_LABEL_PROTOCOL_$_ADAccountQualityDiagnosticDepot
+ __OBJC_LABEL_PROTOCOL_$_ADClock
+ __OBJC_LABEL_PROTOCOL_$_ADPersonalizedAdsSource
+ __OBJC_METACLASS_RO_$_ADAccountQualityDiagnosticSample
+ __OBJC_METACLASS_RO_$_ADAccountQualityDiagnostics
+ __OBJC_METACLASS_RO_$_ADCoreAnalyticsAccountQualityDiagnosticDepot
+ __OBJC_METACLASS_RO_$_ADCoreSettingsPersonalizedAdsSource
+ __OBJC_METACLASS_RO_$_ADSystemClock
+ __OBJC_PROTOCOL_$_ADAccountQualityDiagnosticDepot
+ __OBJC_PROTOCOL_$_ADClock
+ __OBJC_PROTOCOL_$_ADPersonalizedAdsSource
+ ___62-[ADCoreAnalyticsAccountQualityDiagnosticDepot depositSample:]_block_invoke
+ _currentYear
+ _objc_msgSend$birthYearValidity
+ _objc_msgSend$birthYearValidityForAccount:
+ _objc_msgSend$birthYearValidityForConsumerAccount:
+ _objc_msgSend$birthYearValidityForRestrictedAccount:
+ _objc_msgSend$calendarWithIdentifier:
+ _objc_msgSend$clock
+ _objc_msgSend$component:fromDate:
+ _objc_msgSend$initWithBirthYearValidity:personalizedAdsStatus:storefrontID:
+ _objc_msgSend$initWithClock:depot:personalizedAdsSource:storefrontIDSource:
+ _objc_msgSend$isConsumer
+ _objc_msgSend$isRestricted
+ _objc_msgSend$now
+ _objc_msgSend$personalizedAds
+ _objc_msgSend$personalizedAdsSource
+ _objc_msgSend$personalizedAdsStatus
+ _objc_msgSend$sampleWithBirthYearValidity:personalizedAdsStatus:storefrontID:
- __OBJC_$_INSTANCE_METHODS_DSIDRecord
CStrings:
+ "PAStatus"
+ "birthYearValidity"
+ "com.apple.ap.adprivacyd.account.quality"
```
