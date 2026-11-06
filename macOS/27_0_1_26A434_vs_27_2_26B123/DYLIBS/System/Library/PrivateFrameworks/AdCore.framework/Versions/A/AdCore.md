## AdCore

> `/System/Library/PrivateFrameworks/AdCore.framework/Versions/A/AdCore`

```diff

-638.1.7.0.0
-  __TEXT.__text: 0x321c0
-  __TEXT.__objc_methlist: 0x4074
-  __TEXT.__const: 0x188
-  __TEXT.__cstring: 0x3ef2
+638.2.3.0.0
+  __TEXT.__text: 0x3376c
+  __TEXT.__objc_methlist: 0x4494
+  __TEXT.__const: 0x1e8
+  __TEXT.__cstring: 0x3fa7
   __TEXT.__gcc_except_tab: 0x4c0
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0x53
-  __TEXT.__unwind_info: 0xc20
+  __TEXT.__unwind_info: 0xca8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3f8
-  __DATA_CONST.__objc_classlist: 0x150
+  __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fd0
+  __DATA_CONST.__objc_selrefs: 0x2150
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x150
+  __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x188
-  __DATA_CONST.__got: 0x340
-  __AUTH_CONST.__const: 0x700
-  __AUTH_CONST.__cfstring: 0x4ba0
-  __AUTH_CONST.__objc_const: 0x5c70
+  __DATA_CONST.__got: 0x3c0
+  __AUTH_CONST.__const: 0x730
+  __AUTH_CONST.__cfstring: 0x4ca0
+  __AUTH_CONST.__objc_const: 0x7a88
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x3c8
+  __AUTH_CONST.__auth_got: 0x3d0
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x3f8
-  __DATA.__data: 0x1e0
-  __DATA.__bss: 0x10
+  __AUTH.__objc_data: 0x5f0
+  __DATA.__objc_ivar: 0x434
+  __DATA.__data: 0x420
   __DATA_DIRTY.__objc_data: 0xaf0
-  __DATA_DIRTY.__bss: 0x240
+  __DATA_DIRTY.__bss: 0x250
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /System/Library/PrivateFrameworks/AppleAccount.framework/Versions/A/AppleAccount
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/A/AppleMediaServices
   - /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1435
-  Symbols:   2889
-  CStrings:  646
+  Functions: 1497
+  Symbols:   3137
+  CStrings:  655
 
Symbols:
+ +[ADAccountQualityDiagnosticSample sampleWithBirthYearValidity:personalizedAdsStatus:storefrontID:]
+ +[ADAccountQualityDiagnostics(Production) production]
+ +[ADAccountSyncDiagnosticSample sampleWithRemoteLoadStatus:localStoreStatus:storefrontID:]
+ +[ADAccountSyncDiagnostics(Production) production]
+ +[ADStorefront storefrontWithValue:]
+ +[ADStorefrontID storefrontIDWithValue:]
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
+ -[ADAccountSyncDiagnosticSample .cxx_destruct]
+ -[ADAccountSyncDiagnosticSample initWithRemoteLoadStatus:localStoreStatus:storefrontID:]
+ -[ADAccountSyncDiagnosticSample loadStatus]
+ -[ADAccountSyncDiagnosticSample storeStatus]
+ -[ADAccountSyncDiagnosticSample storefrontID]
+ -[ADAccountSyncDiagnostics .cxx_destruct]
+ -[ADAccountSyncDiagnostics depositLoadStatus:storeStatus:]
+ -[ADAccountSyncDiagnostics depot]
+ -[ADAccountSyncDiagnostics initWithDepot:storefrontIDSource:]
+ -[ADAccountSyncDiagnostics loadStatusForCocoaError:]
+ -[ADAccountSyncDiagnostics loadStatusForCoreError:]
+ -[ADAccountSyncDiagnostics loadStatusForError:]
+ -[ADAccountSyncDiagnostics localStoreCompletedWithStatus:]
+ -[ADAccountSyncDiagnostics remoteLoadFailedWithError:]
+ -[ADAccountSyncDiagnostics storeStatusForStatus:]
+ -[ADAccountSyncDiagnostics storefrontIDSource]
+ -[ADAdCoreSettingsStorefrontSource storefront]
+ -[ADCoreAnalyticsAccountQualityDiagnosticDepot depositSample:]
+ -[ADCoreAnalyticsAccountSyncDiagnosticDepot depositSample:]
+ -[ADCoreSettingsPersonalizedAdsSource personalizedAds]
+ -[ADStorefront initWithValue:]
+ -[ADStorefront storefrontID]
+ -[ADStorefront value]
+ -[ADStorefrontID hash]
+ -[ADStorefrontID initWithValue:]
+ -[ADStorefrontID isEqual:]
+ -[ADStorefrontID isEqualToStorefrontID:]
+ -[ADStorefrontID value]
+ -[ADStorefrontToStorefrontIDSource .cxx_destruct]
+ -[ADStorefrontToStorefrontIDSource initWithStorefrontSource:]
+ -[ADStorefrontToStorefrontIDSource storefrontID]
+ -[ADStorefrontToStorefrontIDSource storefrontSource]
+ -[ADSystemClock now]
+ -[DSIDRecord(Helpers) isConsumer]
+ -[DSIDRecord(Helpers) isRestricted]
+ OBJC_IVAR_$_ADAccountQualityDiagnosticSample._birthYearValidity
+ OBJC_IVAR_$_ADAccountQualityDiagnosticSample._personalizedAdsStatus
+ OBJC_IVAR_$_ADAccountQualityDiagnosticSample._storefrontID
+ OBJC_IVAR_$_ADAccountQualityDiagnostics._clock
+ OBJC_IVAR_$_ADAccountQualityDiagnostics._depot
+ OBJC_IVAR_$_ADAccountQualityDiagnostics._personalizedAdsSource
+ OBJC_IVAR_$_ADAccountQualityDiagnostics._storefrontIDSource
+ OBJC_IVAR_$_ADAccountSyncDiagnosticSample._loadStatus
+ OBJC_IVAR_$_ADAccountSyncDiagnosticSample._storeStatus
+ OBJC_IVAR_$_ADAccountSyncDiagnosticSample._storefrontID
+ OBJC_IVAR_$_ADAccountSyncDiagnostics._depot
+ OBJC_IVAR_$_ADAccountSyncDiagnostics._storefrontIDSource
+ OBJC_IVAR_$_ADStorefront._value
+ OBJC_IVAR_$_ADStorefrontID._value
+ OBJC_IVAR_$_ADStorefrontToStorefrontIDSource._storefrontSource
+ _AnalyticsSendEventLazy
+ _NSCalendarIdentifierGregorian
+ _NSCocoaErrorDomain
+ _OBJC_CLASS_$_ADAccountQualityDiagnosticSample
+ _OBJC_CLASS_$_ADAccountQualityDiagnostics
+ _OBJC_CLASS_$_ADAccountSyncDiagnosticSample
+ _OBJC_CLASS_$_ADAccountSyncDiagnostics
+ _OBJC_CLASS_$_ADAdCoreSettingsStorefrontSource
+ _OBJC_CLASS_$_ADCoreAnalyticsAccountQualityDiagnosticDepot
+ _OBJC_CLASS_$_ADCoreAnalyticsAccountSyncDiagnosticDepot
+ _OBJC_CLASS_$_ADCoreSettingsPersonalizedAdsSource
+ _OBJC_CLASS_$_ADStorefront
+ _OBJC_CLASS_$_ADStorefrontID
+ _OBJC_CLASS_$_ADStorefrontToStorefrontIDSource
+ _OBJC_CLASS_$_ADSystemClock
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_METACLASS_$_ADAccountQualityDiagnosticSample
+ _OBJC_METACLASS_$_ADAccountQualityDiagnostics
+ _OBJC_METACLASS_$_ADAccountSyncDiagnosticSample
+ _OBJC_METACLASS_$_ADAccountSyncDiagnostics
+ _OBJC_METACLASS_$_ADAdCoreSettingsStorefrontSource
+ _OBJC_METACLASS_$_ADCoreAnalyticsAccountQualityDiagnosticDepot
+ _OBJC_METACLASS_$_ADCoreAnalyticsAccountSyncDiagnosticDepot
+ _OBJC_METACLASS_$_ADCoreSettingsPersonalizedAdsSource
+ _OBJC_METACLASS_$_ADStorefront
+ _OBJC_METACLASS_$_ADStorefrontID
+ _OBJC_METACLASS_$_ADStorefrontToStorefrontIDSource
+ _OBJC_METACLASS_$_ADSystemClock
+ __OBJC_$_CLASS_METHODS_ADAccountQualityDiagnosticSample
+ __OBJC_$_CLASS_METHODS_ADAccountQualityDiagnostics(Production)
+ __OBJC_$_CLASS_METHODS_ADAccountSyncDiagnosticSample
+ __OBJC_$_CLASS_METHODS_ADAccountSyncDiagnostics(Production)
+ __OBJC_$_CLASS_METHODS_ADStorefront
+ __OBJC_$_CLASS_METHODS_ADStorefrontID
+ __OBJC_$_INSTANCE_METHODS_ADAccountQualityDiagnosticSample
+ __OBJC_$_INSTANCE_METHODS_ADAccountQualityDiagnostics
+ __OBJC_$_INSTANCE_METHODS_ADAccountSyncDiagnosticSample
+ __OBJC_$_INSTANCE_METHODS_ADAccountSyncDiagnostics
+ __OBJC_$_INSTANCE_METHODS_ADAdCoreSettingsStorefrontSource
+ __OBJC_$_INSTANCE_METHODS_ADCoreAnalyticsAccountQualityDiagnosticDepot
+ __OBJC_$_INSTANCE_METHODS_ADCoreAnalyticsAccountSyncDiagnosticDepot
+ __OBJC_$_INSTANCE_METHODS_ADCoreSettingsPersonalizedAdsSource
+ __OBJC_$_INSTANCE_METHODS_ADStorefront
+ __OBJC_$_INSTANCE_METHODS_ADStorefrontID
+ __OBJC_$_INSTANCE_METHODS_ADStorefrontToStorefrontIDSource
+ __OBJC_$_INSTANCE_METHODS_ADSystemClock
+ __OBJC_$_INSTANCE_METHODS_DSIDRecord(Helpers)
+ __OBJC_$_INSTANCE_VARIABLES_ADAccountQualityDiagnosticSample
+ __OBJC_$_INSTANCE_VARIABLES_ADAccountQualityDiagnostics
+ __OBJC_$_INSTANCE_VARIABLES_ADAccountSyncDiagnosticSample
+ __OBJC_$_INSTANCE_VARIABLES_ADAccountSyncDiagnostics
+ __OBJC_$_INSTANCE_VARIABLES_ADStorefront
+ __OBJC_$_INSTANCE_VARIABLES_ADStorefrontID
+ __OBJC_$_INSTANCE_VARIABLES_ADStorefrontToStorefrontIDSource
+ __OBJC_$_PROP_LIST_ADAccountQualityDiagnosticSample
+ __OBJC_$_PROP_LIST_ADAccountQualityDiagnostics
+ __OBJC_$_PROP_LIST_ADAccountSyncDiagnosticSample
+ __OBJC_$_PROP_LIST_ADAccountSyncDiagnostics
+ __OBJC_$_PROP_LIST_ADAdCoreSettingsStorefrontSource
+ __OBJC_$_PROP_LIST_ADCoreAnalyticsAccountQualityDiagnosticDepot
+ __OBJC_$_PROP_LIST_ADCoreAnalyticsAccountSyncDiagnosticDepot
+ __OBJC_$_PROP_LIST_ADCoreSettingsPersonalizedAdsSource
+ __OBJC_$_PROP_LIST_ADStorefront
+ __OBJC_$_PROP_LIST_ADStorefrontID
+ __OBJC_$_PROP_LIST_ADStorefrontToStorefrontIDSource
+ __OBJC_$_PROP_LIST_ADSystemClock
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ADAccountQualityDiagnosticDepot
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ADAccountSyncDiagnosticDepot
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ADClock
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ADPersonalizedAdsSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ADStorefrontIDSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ADStorefrontSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ADAccountQualityDiagnosticDepot
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ADAccountSyncDiagnosticDepot
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ADClock
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ADPersonalizedAdsSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ADStorefrontIDSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ADStorefrontSource
+ __OBJC_$_PROTOCOL_REFS_ADAccountQualityDiagnosticDepot
+ __OBJC_$_PROTOCOL_REFS_ADAccountSyncDiagnosticDepot
+ __OBJC_$_PROTOCOL_REFS_ADClock
+ __OBJC_$_PROTOCOL_REFS_ADPersonalizedAdsSource
+ __OBJC_$_PROTOCOL_REFS_ADStorefrontIDSource
+ __OBJC_$_PROTOCOL_REFS_ADStorefrontSource
+ __OBJC_CLASS_PROTOCOLS_$_ADAdCoreSettingsStorefrontSource
+ __OBJC_CLASS_PROTOCOLS_$_ADCoreAnalyticsAccountQualityDiagnosticDepot
+ __OBJC_CLASS_PROTOCOLS_$_ADCoreAnalyticsAccountSyncDiagnosticDepot
+ __OBJC_CLASS_PROTOCOLS_$_ADCoreSettingsPersonalizedAdsSource
+ __OBJC_CLASS_PROTOCOLS_$_ADStorefrontToStorefrontIDSource
+ __OBJC_CLASS_PROTOCOLS_$_ADSystemClock
+ __OBJC_CLASS_RO_$_ADAccountQualityDiagnosticSample
+ __OBJC_CLASS_RO_$_ADAccountQualityDiagnostics
+ __OBJC_CLASS_RO_$_ADAccountSyncDiagnosticSample
+ __OBJC_CLASS_RO_$_ADAccountSyncDiagnostics
+ __OBJC_CLASS_RO_$_ADAdCoreSettingsStorefrontSource
+ __OBJC_CLASS_RO_$_ADCoreAnalyticsAccountQualityDiagnosticDepot
+ __OBJC_CLASS_RO_$_ADCoreAnalyticsAccountSyncDiagnosticDepot
+ __OBJC_CLASS_RO_$_ADCoreSettingsPersonalizedAdsSource
+ __OBJC_CLASS_RO_$_ADStorefront
+ __OBJC_CLASS_RO_$_ADStorefrontID
+ __OBJC_CLASS_RO_$_ADStorefrontToStorefrontIDSource
+ __OBJC_CLASS_RO_$_ADSystemClock
+ __OBJC_LABEL_PROTOCOL_$_ADAccountQualityDiagnosticDepot
+ __OBJC_LABEL_PROTOCOL_$_ADAccountSyncDiagnosticDepot
+ __OBJC_LABEL_PROTOCOL_$_ADClock
+ __OBJC_LABEL_PROTOCOL_$_ADPersonalizedAdsSource
+ __OBJC_LABEL_PROTOCOL_$_ADStorefrontIDSource
+ __OBJC_LABEL_PROTOCOL_$_ADStorefrontSource
+ __OBJC_METACLASS_RO_$_ADAccountQualityDiagnosticSample
+ __OBJC_METACLASS_RO_$_ADAccountQualityDiagnostics
+ __OBJC_METACLASS_RO_$_ADAccountSyncDiagnosticSample
+ __OBJC_METACLASS_RO_$_ADAccountSyncDiagnostics
+ __OBJC_METACLASS_RO_$_ADAdCoreSettingsStorefrontSource
+ __OBJC_METACLASS_RO_$_ADCoreAnalyticsAccountQualityDiagnosticDepot
+ __OBJC_METACLASS_RO_$_ADCoreAnalyticsAccountSyncDiagnosticDepot
+ __OBJC_METACLASS_RO_$_ADCoreSettingsPersonalizedAdsSource
+ __OBJC_METACLASS_RO_$_ADStorefront
+ __OBJC_METACLASS_RO_$_ADStorefrontID
+ __OBJC_METACLASS_RO_$_ADStorefrontToStorefrontIDSource
+ __OBJC_METACLASS_RO_$_ADSystemClock
+ __OBJC_PROTOCOL_$_ADAccountQualityDiagnosticDepot
+ __OBJC_PROTOCOL_$_ADAccountSyncDiagnosticDepot
+ __OBJC_PROTOCOL_$_ADClock
+ __OBJC_PROTOCOL_$_ADPersonalizedAdsSource
+ __OBJC_PROTOCOL_$_ADStorefrontIDSource
+ __OBJC_PROTOCOL_$_ADStorefrontSource
+ ___59-[ADCoreAnalyticsAccountSyncDiagnosticDepot depositSample:]_block_invoke
+ ___62-[ADCoreAnalyticsAccountQualityDiagnosticDepot depositSample:]_block_invoke
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0l
+ _currentYear
+ _objc_msgSend$birthYearValidity
+ _objc_msgSend$birthYearValidityForAccount:
+ _objc_msgSend$birthYearValidityForConsumerAccount:
+ _objc_msgSend$birthYearValidityForRestrictedAccount:
+ _objc_msgSend$calendarWithIdentifier:
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$clock
+ _objc_msgSend$component:fromDate:
+ _objc_msgSend$componentsSeparatedByCharactersInSet:
+ _objc_msgSend$depositLoadStatus:storeStatus:
+ _objc_msgSend$depositSample:
+ _objc_msgSend$depot
+ _objc_msgSend$domain
+ _objc_msgSend$firstObject
+ _objc_msgSend$initWithBirthYearValidity:personalizedAdsStatus:storefrontID:
+ _objc_msgSend$initWithClock:depot:personalizedAdsSource:storefrontIDSource:
+ _objc_msgSend$initWithDepot:storefrontIDSource:
+ _objc_msgSend$initWithRemoteLoadStatus:localStoreStatus:storefrontID:
+ _objc_msgSend$initWithStorefrontSource:
+ _objc_msgSend$initWithValue:
+ _objc_msgSend$isConsumer
+ _objc_msgSend$isEqualToStorefrontID:
+ _objc_msgSend$isRestricted
+ _objc_msgSend$loadStatus
+ _objc_msgSend$loadStatusForCocoaError:
+ _objc_msgSend$loadStatusForCoreError:
+ _objc_msgSend$loadStatusForError:
+ _objc_msgSend$localStoreCompletedWithStatus:
+ _objc_msgSend$now
+ _objc_msgSend$personalizedAds
+ _objc_msgSend$personalizedAdsSource
+ _objc_msgSend$personalizedAdsStatus
+ _objc_msgSend$production
+ _objc_msgSend$sampleWithBirthYearValidity:personalizedAdsStatus:storefrontID:
+ _objc_msgSend$sampleWithRemoteLoadStatus:localStoreStatus:storefrontID:
+ _objc_msgSend$storeStatus
+ _objc_msgSend$storeStatusForStatus:
+ _objc_msgSend$storefront
+ _objc_msgSend$storefrontID
+ _objc_msgSend$storefrontIDSource
+ _objc_msgSend$storefrontIDWithValue:
+ _objc_msgSend$storefrontSource
+ _objc_msgSend$storefrontWithValue:
+ _objc_msgSend$value
- __OBJC_$_INSTANCE_METHODS_DSIDRecord
CStrings:
+ "-,"
+ "@\"NSDictionary\"8@?0"
+ "PAStatus"
+ "birthYearValidity"
+ "com.apple.ap.adprivacyd.account.quality"
+ "com.apple.ap.adprivacyd.account.syncStatus"
+ "localSaveStatus"
+ "remoteLoadStatus"
+ "storefrontID"
```
