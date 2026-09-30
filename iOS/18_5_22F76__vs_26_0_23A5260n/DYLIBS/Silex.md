## Silex

> `/System/Library/PrivateFrameworks/Silex.framework/Silex`

```diff

-5681.0.0.0.0
-  __TEXT.__text: 0x113970
-  __TEXT.__auth_stubs: 0xf60
-  __TEXT.__objc_methlist: 0x1de14
-  __TEXT.__const: 0x4bc
-  __TEXT.__cstring: 0x9a2c
+5718.1.0.0.0
+  __TEXT.__text: 0x114af0
+  __TEXT.__auth_stubs: 0xf80
+  __TEXT.__objc_methlist: 0x1e184
+  __TEXT.__const: 0x4cc
+  __TEXT.__cstring: 0x9b7b
   __TEXT.__gcc_except_tab: 0x23b8
-  __TEXT.__oslogstring: 0x2236
+  __TEXT.__oslogstring: 0x2324
   __TEXT.__ustring: 0x6c
-  __TEXT.__unwind_info: 0x4e38
-  __TEXT.__objc_classname: 0x75b4
-  __TEXT.__objc_methname: 0x3ae58
-  __TEXT.__objc_methtype: 0xe3e0
-  __TEXT.__objc_stubs: 0x23960
-  __DATA_CONST.__got: 0x24c0
-  __DATA_CONST.__const: 0x3b70
-  __DATA_CONST.__objc_classlist: 0x1c70
+  __TEXT.__unwind_info: 0x4e50
+  __TEXT.__objc_classname: 0x771a
+  __TEXT.__objc_methname: 0x3b5ac
+  __TEXT.__objc_methtype: 0xe6ba
+  __TEXT.__objc_stubs: 0x23ca0
+  __DATA_CONST.__got: 0x2520
+  __DATA_CONST.__const: 0x3bf8
+  __DATA_CONST.__objc_classlist: 0x1ca8
   __DATA_CONST.__objc_catlist: 0xc8
-  __DATA_CONST.__objc_protolist: 0xcf8
+  __DATA_CONST.__objc_protolist: 0xd20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb5d8
-  __DATA_CONST.__objc_protorefs: 0x568
-  __DATA_CONST.__objc_superrefs: 0x1018
+  __DATA_CONST.__objc_selrefs: 0xb6d8
+  __DATA_CONST.__objc_protorefs: 0x580
+  __DATA_CONST.__objc_superrefs: 0x1028
   __DATA_CONST.__objc_arraydata: 0x3cc8
-  __AUTH_CONST.__auth_got: 0x7c8
-  __AUTH_CONST.__const: 0x3be0
-  __AUTH_CONST.__cfstring: 0x95c0
-  __AUTH_CONST.__objc_const: 0x507a0
+  __AUTH_CONST.__auth_got: 0x7d8
+  __AUTH_CONST.__const: 0x3c80
+  __AUTH_CONST.__cfstring: 0x96a0
+  __AUTH_CONST.__objc_const: 0x51238
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x2aa8
-  __AUTH.__objc_data: 0x32a0
-  __DATA.__objc_ivar: 0x1f2c
-  __DATA.__data: 0x9ca8
+  __AUTH.__objc_data: 0x3390
+  __DATA.__objc_ivar: 0x1f5c
+  __DATA.__data: 0x9e98
   __DATA.__bss: 0x40
-  __DATA_DIRTY.__objc_data: 0xe9c0
+  __DATA_DIRTY.__objc_data: 0xeb00
   __DATA_DIRTY.__bss: 0x1e8
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/ARKit.framework/ARKit

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/WebKit.framework/WebKit
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
   - /System/Library/PrivateFrameworks/DataAccessExpress.framework/DataAccessExpress
   - /System/Library/PrivateFrameworks/NewsFoundation.framework/NewsFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3BCDAD07-F78F-3BB8-8F17-7EBCF36DC42B
-  Functions: 8426
-  Symbols:   34023
-  CStrings:  14455
+  UUID: B197D6DD-2A17-3642-9529-6851EF5A8F0C
+  Functions: 8473
+  Symbols:   34244
+  CStrings:  14563
 
Symbols:
+ -[SXCondition followingWithValue:withType:]
+ -[SXCondition offerIdentifierWithValue:withType:]
+ -[SXConditionHints followingWithValue:withType:]
+ -[SXConditionHints offerIdentifierWithValue:withType:]
+ -[SXConditionValidationContext offerIdentifier]
+ -[SXConditionValidationContext tagSubscriptionStatus]
+ -[SXDebugLayoutOptionsProvider offerIdentifier]
+ -[SXDebugLayoutOptionsProvider overrideOfferIdentifier:]
+ -[SXDebugLayoutOptionsProvider overrideTagSubscriptionStatus:]
+ -[SXDebugLayoutOptionsProvider setOfferIdentifier:]
+ -[SXEmbedComponentView initWithDOMObjectProvider:viewport:presentationDelegate:componentStyleRendererFactory:reachabilityProvider:embedDataProvider:actionHandler:layoutInvalidator:websiteDataStore:processPoolCache:proxyAuthenticationHandler:sceneStateMonitor:analyticsReporting:]
+ -[SXEmbedComponentView processPoolCache]
+ -[SXEmbedComponentViewFactory initWithDOMObjectProvider:viewport:presentationDelegateProvider:componentStyleRendererFactory:reachabilityProvider:embedDataProvider:actionHandler:layoutInvalidator:websiteDataStore:processPoolCache:proxyAuthenticationHandler:sceneStateMonitor:analyticsReportingProvider:]
+ -[SXEmbedComponentViewFactory processPoolCache]
+ -[SXFollowingCondition .cxx_destruct]
+ -[SXFollowingCondition following]
+ -[SXFollowingCondition initWithFollowing:tagIdentifier:]
+ -[SXFollowingCondition tagIdentifier]
+ -[SXFollowingConditionValidator validateCondition:context:]
+ -[SXFormatInteractor initWithLayoutCoordinator:layoutOptionsFactory:presentationAttributesProvider:subscriptionStatusProvider:debugLayoutOptionsProvider:newsletterSubscriptionStatusProvider:offerUpsellScenarioProvider:subscriptionActivationEligibilityProvider:offerIdentifierProvider:renderingConfigurationProvider:tagSubscriptionStatusProvider:]
+ -[SXFormatInteractor offerIdentifierDidChangeFromIdentifier:to:]
+ -[SXFormatInteractor offerIdentifierProvider]
+ -[SXFormatInteractor tagSubscriptionStatusChangedFromStatus:]
+ -[SXFormatInteractor tagSubscriptionStatusProvider]
+ -[SXLayoutOptions initWithColumnLayout:viewportSize:traitCollection:contentSizeCategory:bundleSubscriptionStatus:channelSubscriptionStatus:testing:viewingLocation:contentScaleFactor:newsletterSubscriptionStatus:offerUpsellScenario:subscriptionActivationEligibility:offerIdentifier:smartInvertColorsEnabled:conditionKeys:tagSubscriptionStatus:]
+ -[SXLayoutOptions offerIdentifier]
+ -[SXLayoutOptions tagSubscriptionStatus]
+ -[SXLayoutOptionsFactory createLayoutOptionsWithViewportSize:safeAreaInsets:traitCollection:bundleSubscriptionStatus:channelSubscriptionStatus:contentSizeCategory:testing:viewingLocation:contentScaleFactor:newsletterSubscriptionStatus:offerUpsellScenario:subscriptionActivationEligibility:offerIdentifier:smartInvertColorsEnabled:conditionKeys:tagSubscriptionStatus:]
+ -[SXLinkAction initWithURL:analytics:openInBrowser:]
+ -[SXLinkAction openInBrowser]
+ -[SXOfferIdentifierConditionValidator validateCondition:context:]
+ -[SXOfferIdentifierDefaultProvider addObserver:]
+ -[SXOfferIdentifierDefaultProvider offerIdentifier]
+ -[SXOfferIdentifierDefaultProvider removeObserver:]
+ -[SXTagSubscriptionStatus .cxx_destruct]
+ -[SXTagSubscriptionStatus description]
+ -[SXTagSubscriptionStatus following]
+ -[SXTagSubscriptionStatus initWithFollowing:tags:]
+ -[SXTagSubscriptionStatus init]
+ -[SXTagSubscriptionStatus isEqual:]
+ -[SXTagSubscriptionStatus tags]
+ -[SXTagSubscriptionStatusAssembly loadInRegistry:]
+ -[SXTagSubscriptionStatusProvider addObserver:]
+ -[SXTagSubscriptionStatusProvider removeObserver:]
+ -[SXTagSubscriptionStatusProvider tagSubscriptionStatus]
+ -[SXURLActionFactory actionForURL:analytics:openInBrowser:]
+ -[SXVideoFillPlayerView registerForHDRTraitChanges]
+ -[SXWebContentConfigurationProvider feedConfigurationFactory]
+ -[SXWebContentConfigurationProvider initWithPresentationAttributesProvider:storeFrontProvider:liveActivityAttributesProvider:feedConfigurationFactory:viewControllerPresentationManager:locale:location:]
+ -[SXWebContentConfigurationProvider viewControllerPresentationManager]
+ -[SXWebProcessPoolCache .cxx_destruct]
+ -[SXWebProcessPoolCache cache]
+ -[SXWebProcessPoolCache init]
+ -[SXWebProcessPoolCache processPoolForBaseURL:]
+ OBJC_IVAR_$_SXLayoutOptions._offerIdentifier
+ OBJC_IVAR_$_SXLayoutOptions._tagSubscriptionStatus
+ _CADynamicRangeConstrainedHigh
+ _CADynamicRangeHigh
+ _OBJC_CLASS_$_SWLayoutGuide
+ _OBJC_CLASS_$_SXFollowingCondition
+ _OBJC_CLASS_$_SXFollowingConditionValidator
+ _OBJC_CLASS_$_SXOfferIdentifierConditionValidator
+ _OBJC_CLASS_$_SXOfferIdentifierDefaultProvider
+ _OBJC_CLASS_$_SXTagSubscriptionStatus
+ _OBJC_CLASS_$_SXTagSubscriptionStatusAssembly
+ _OBJC_CLASS_$_SXTagSubscriptionStatusProvider
+ _OBJC_CLASS_$_SXWebProcessPoolCache
+ _OBJC_CLASS_$__UITraitHDRHeadroomUsage
+ _OBJC_CLASS_$__WKProcessPoolConfiguration
+ _OBJC_IVAR_$_SXDebugLayoutOptionsProvider._offerIdentifier
+ _OBJC_IVAR_$_SXEmbedComponentView._processPoolCache
+ _OBJC_IVAR_$_SXEmbedComponentViewFactory._processPoolCache
+ _OBJC_IVAR_$_SXFollowingCondition._following
+ _OBJC_IVAR_$_SXFollowingCondition._tagIdentifier
+ _OBJC_IVAR_$_SXFormatInteractor._offerIdentifierProvider
+ _OBJC_IVAR_$_SXFormatInteractor._tagSubscriptionStatusProvider
+ _OBJC_IVAR_$_SXLinkAction._openInBrowser
+ _OBJC_IVAR_$_SXTagSubscriptionStatus._following
+ _OBJC_IVAR_$_SXTagSubscriptionStatus._tags
+ _OBJC_IVAR_$_SXWebContentConfigurationProvider._feedConfigurationFactory
+ _OBJC_IVAR_$_SXWebContentConfigurationProvider._viewControllerPresentationManager
+ _OBJC_IVAR_$_SXWebProcessPoolCache._cache
+ _OBJC_METACLASS_$_SXFollowingCondition
+ _OBJC_METACLASS_$_SXFollowingConditionValidator
+ _OBJC_METACLASS_$_SXOfferIdentifierConditionValidator
+ _OBJC_METACLASS_$_SXOfferIdentifierDefaultProvider
+ _OBJC_METACLASS_$_SXTagSubscriptionStatus
+ _OBJC_METACLASS_$_SXTagSubscriptionStatusAssembly
+ _OBJC_METACLASS_$_SXTagSubscriptionStatusProvider
+ _OBJC_METACLASS_$_SXWebProcessPoolCache
+ _SXConditionFollowing
+ _SXConditionOfferIdentifier
+ _TUFaceTimeAudioServiceName
+ __OBJC_$_INSTANCE_METHODS_SXFollowingCondition
+ __OBJC_$_INSTANCE_METHODS_SXFollowingConditionValidator
+ __OBJC_$_INSTANCE_METHODS_SXOfferIdentifierConditionValidator
+ __OBJC_$_INSTANCE_METHODS_SXOfferIdentifierDefaultProvider
+ __OBJC_$_INSTANCE_METHODS_SXTagSubscriptionStatus
+ __OBJC_$_INSTANCE_METHODS_SXTagSubscriptionStatusAssembly
+ __OBJC_$_INSTANCE_METHODS_SXTagSubscriptionStatusProvider
+ __OBJC_$_INSTANCE_METHODS_SXWebProcessPoolCache
+ __OBJC_$_INSTANCE_VARIABLES_SXFollowingCondition
+ __OBJC_$_INSTANCE_VARIABLES_SXTagSubscriptionStatus
+ __OBJC_$_INSTANCE_VARIABLES_SXWebProcessPoolCache
+ __OBJC_$_PROP_LIST_SXCondition.196
+ __OBJC_$_PROP_LIST_SXConditionHints.126
+ __OBJC_$_PROP_LIST_SXConditionValidationContext.112
+ __OBJC_$_PROP_LIST_SXFollowingCondition
+ __OBJC_$_PROP_LIST_SXFollowingConditionValidator
+ __OBJC_$_PROP_LIST_SXFormatInteractor.174
+ __OBJC_$_PROP_LIST_SXLinkAction.76
+ __OBJC_$_PROP_LIST_SXOfferIdentifierConditionValidator
+ __OBJC_$_PROP_LIST_SXOfferIdentifierDefaultProvider
+ __OBJC_$_PROP_LIST_SXOfferIdentifierProviding
+ __OBJC_$_PROP_LIST_SXTagSubscriptionStatus
+ __OBJC_$_PROP_LIST_SXTagSubscriptionStatusAssembly
+ __OBJC_$_PROP_LIST_SXTagSubscriptionStatusProvider
+ __OBJC_$_PROP_LIST_SXTagSubscriptionStatusProviding
+ __OBJC_$_PROP_LIST_SXWebProcessPoolCache
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SWFeedConfigurationFactory
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SXOfferIdentifierObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SXOfferIdentifierProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SXTagSubscriptionStatusObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SXTagSubscriptionStatusProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SWFeedConfigurationFactory
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SXOfferIdentifierObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SXOfferIdentifierProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SXTagSubscriptionStatusObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SXTagSubscriptionStatusProviding
+ __OBJC_$_PROTOCOL_REFS_SWFeedConfigurationFactory
+ __OBJC_$_PROTOCOL_REFS_SXOfferIdentifierObserving
+ __OBJC_$_PROTOCOL_REFS_SXOfferIdentifierProviding
+ __OBJC_$_PROTOCOL_REFS_SXTagSubscriptionStatusObserving
+ __OBJC_$_PROTOCOL_REFS_SXTagSubscriptionStatusProviding
+ __OBJC_CLASS_PROTOCOLS_$_SXFollowingConditionValidator
+ __OBJC_CLASS_PROTOCOLS_$_SXOfferIdentifierConditionValidator
+ __OBJC_CLASS_PROTOCOLS_$_SXOfferIdentifierDefaultProvider
+ __OBJC_CLASS_PROTOCOLS_$_SXTagSubscriptionStatusAssembly
+ __OBJC_CLASS_PROTOCOLS_$_SXTagSubscriptionStatusProvider
+ __OBJC_CLASS_RO_$_SXFollowingCondition
+ __OBJC_CLASS_RO_$_SXFollowingConditionValidator
+ __OBJC_CLASS_RO_$_SXOfferIdentifierConditionValidator
+ __OBJC_CLASS_RO_$_SXOfferIdentifierDefaultProvider
+ __OBJC_CLASS_RO_$_SXTagSubscriptionStatus
+ __OBJC_CLASS_RO_$_SXTagSubscriptionStatusAssembly
+ __OBJC_CLASS_RO_$_SXTagSubscriptionStatusProvider
+ __OBJC_CLASS_RO_$_SXWebProcessPoolCache
+ __OBJC_LABEL_PROTOCOL_$_SWFeedConfigurationFactory
+ __OBJC_LABEL_PROTOCOL_$_SXOfferIdentifierObserving
+ __OBJC_LABEL_PROTOCOL_$_SXOfferIdentifierProviding
+ __OBJC_LABEL_PROTOCOL_$_SXTagSubscriptionStatusObserving
+ __OBJC_LABEL_PROTOCOL_$_SXTagSubscriptionStatusProviding
+ __OBJC_METACLASS_RO_$_SXFollowingCondition
+ __OBJC_METACLASS_RO_$_SXFollowingConditionValidator
+ __OBJC_METACLASS_RO_$_SXOfferIdentifierConditionValidator
+ __OBJC_METACLASS_RO_$_SXOfferIdentifierDefaultProvider
+ __OBJC_METACLASS_RO_$_SXTagSubscriptionStatus
+ __OBJC_METACLASS_RO_$_SXTagSubscriptionStatusAssembly
+ __OBJC_METACLASS_RO_$_SXTagSubscriptionStatusProvider
+ __OBJC_METACLASS_RO_$_SXWebProcessPoolCache
+ __OBJC_PROTOCOL_$_SWFeedConfigurationFactory
+ __OBJC_PROTOCOL_$_SXOfferIdentifierObserving
+ __OBJC_PROTOCOL_$_SXOfferIdentifierProviding
+ __OBJC_PROTOCOL_$_SXTagSubscriptionStatusObserving
+ __OBJC_PROTOCOL_$_SXTagSubscriptionStatusProviding
+ __OBJC_PROTOCOL_REFERENCE_$_SWFeedConfigurationFactory
+ __OBJC_PROTOCOL_REFERENCE_$_SXOfferIdentifierProviding
+ __OBJC_PROTOCOL_REFERENCE_$_SXTagSubscriptionStatusProviding
+ __UISolariumEnabled
+ ___279-[SXEmbedComponentView initWithDOMObjectProvider:viewport:presentationDelegate:componentStyleRendererFactory:reachabilityProvider:embedDataProvider:actionHandler:layoutInvalidator:websiteDataStore:processPoolCache:proxyAuthenticationHandler:sceneStateMonitor:analyticsReporting:]_block_invoke
+ ___32-[SXDOMAssembly loadInRegistry:]_block_invoke_78
+ ___32-[SXDOMAssembly loadInRegistry:]_block_invoke_79
+ ___367-[SXLayoutOptionsFactory createLayoutOptionsWithViewportSize:safeAreaInsets:traitCollection:bundleSubscriptionStatus:channelSubscriptionStatus:contentSizeCategory:testing:viewingLocation:contentScaleFactor:newsletterSubscriptionStatus:offerUpsellScenario:subscriptionActivationEligibility:offerIdentifier:smartInvertColorsEnabled:conditionKeys:tagSubscriptionStatus:]_block_invoke
+ ___41-[SXSubscriptionAssembly loadInRegistry:]_block_invoke_4
+ ___50-[SXTagSubscriptionStatusAssembly loadInRegistry:]_block_invoke
+ ___51-[SXVideoFillPlayerView registerForHDRTraitChanges]_block_invoke
+ ___block_descriptor_32_e27_v16?0"<UIMutableTraits>"8l
+ ___block_descriptor_32_e52_"<SXOfferIdentifierProviding>"16?0"<TFResolver>"8l
+ ___block_descriptor_32_e59_"SXOfferIdentifierConditionValidator"16?0"<TFResolver>"8l
+ ___block_descriptor_40_e8_32s_e52_v24?0"<UITraitEnvironment>"8"UITraitCollection"16ls32l8
+ ___block_literal_global.151
+ ___block_literal_global.166
+ ___block_literal_global.183
+ ___block_literal_global.208
+ ___block_literal_global.215
+ ___block_literal_global.225
+ ___block_literal_global.234
+ ___block_literal_global.244
+ ___block_literal_global.246
+ ___block_literal_global.249
+ ___block_literal_global.282
+ ___block_literal_global.290
+ ___block_literal_global.294
+ ___block_literal_global.298
+ ___block_literal_global.302
+ ___block_literal_global.321
+ ___block_literal_global.421
+ ___block_literal_global.424
+ ___block_literal_global.427
+ ___block_literal_global.430
+ ___block_literal_global.434
+ ___block_literal_global.437
+ ___block_literal_global.440
+ ___block_literal_global.443
+ ___block_literal_global.446
+ ___block_literal_global.449
+ ___block_literal_global.452
+ ___block_literal_global.455
+ ___block_literal_global.458
+ ___block_literal_global.461
+ ___block_literal_global.464
+ ___block_literal_global.467
+ ___block_literal_global.473
+ ___block_literal_global.475
+ ___block_literal_global.477
+ ___block_literal_global.479
+ ___block_literal_global.481
+ ___block_literal_global.483
+ ___block_literal_global.487
+ ___block_literal_global.489
+ ___block_literal_global.491
+ ___block_literal_global.495
+ ___block_literal_global.500
+ ___block_literal_global.505
+ ___block_literal_global.508
+ ___block_literal_global.510
+ ___block_literal_global.77
+ _objc_msgSend$_headroomUsage
+ _objc_msgSend$actionForURL:analytics:openInBrowser:
+ _objc_msgSend$createFeedConfigurationForViewController:
+ _objc_msgSend$createLayoutOptionsWithViewportSize:safeAreaInsets:traitCollection:bundleSubscriptionStatus:channelSubscriptionStatus:contentSizeCategory:testing:viewingLocation:contentScaleFactor:newsletterSubscriptionStatus:offerUpsellScenario:subscriptionActivationEligibility:offerIdentifier:smartInvertColorsEnabled:conditionKeys:tagSubscriptionStatus:
+ _objc_msgSend$feedConfigurationFactory
+ _objc_msgSend$following
+ _objc_msgSend$initWithBounds:contentFrame:contentSafeAreaFrame:systemSafeAreaFrame:
+ _objc_msgSend$initWithColumnLayout:viewportSize:traitCollection:contentSizeCategory:bundleSubscriptionStatus:channelSubscriptionStatus:testing:viewingLocation:contentScaleFactor:newsletterSubscriptionStatus:offerUpsellScenario:subscriptionActivationEligibility:offerIdentifier:smartInvertColorsEnabled:conditionKeys:tagSubscriptionStatus:
+ _objc_msgSend$initWithDOMObjectProvider:viewport:presentationDelegate:componentStyleRendererFactory:reachabilityProvider:embedDataProvider:actionHandler:layoutInvalidator:websiteDataStore:processPoolCache:proxyAuthenticationHandler:sceneStateMonitor:analyticsReporting:
+ _objc_msgSend$initWithDOMObjectProvider:viewport:presentationDelegateProvider:componentStyleRendererFactory:reachabilityProvider:embedDataProvider:actionHandler:layoutInvalidator:websiteDataStore:processPoolCache:proxyAuthenticationHandler:sceneStateMonitor:analyticsReportingProvider:
+ _objc_msgSend$initWithFollowing:tagIdentifier:
+ _objc_msgSend$initWithFollowing:tags:
+ _objc_msgSend$initWithLayoutCoordinator:layoutOptionsFactory:presentationAttributesProvider:subscriptionStatusProvider:debugLayoutOptionsProvider:newsletterSubscriptionStatusProvider:offerUpsellScenarioProvider:subscriptionActivationEligibilityProvider:offerIdentifierProvider:renderingConfigurationProvider:tagSubscriptionStatusProvider:
+ _objc_msgSend$initWithPresentationAttributesProvider:storeFrontProvider:liveActivityAttributesProvider:feedConfigurationFactory:viewControllerPresentationManager:locale:location:
+ _objc_msgSend$initWithStoreFront:locale:contentEnvironment:contentSizeCategory:layoutGuide:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:networkStatus:isTransitioning:
+ _objc_msgSend$initWithURL:analytics:openInBrowser:
+ _objc_msgSend$isDefaultCallingAppScheme:
+ _objc_msgSend$offerIdentifier
+ _objc_msgSend$offerIdentifierProvider
+ _objc_msgSend$openInBrowser
+ _objc_msgSend$overrideOfferIdentifier:
+ _objc_msgSend$overridePropertyMap
+ _objc_msgSend$overrideTagSubscriptionStatus:
+ _objc_msgSend$processPoolCache
+ _objc_msgSend$processPoolForBaseURL:
+ _objc_msgSend$registerForHDRTraitChanges
+ _objc_msgSend$registerForTraitChanges:withHandler:
+ _objc_msgSend$setOverrideUserInterfaceStyle:
+ _objc_msgSend$setPreferredDynamicRange:
+ _objc_msgSend$setUserInterfaceStyle:
+ _objc_msgSend$setUsesSingleWebProcess:
+ _objc_msgSend$setValuesForProperties:
+ _objc_msgSend$tagIdentifier
+ _objc_msgSend$tagSubscriptionStatus
+ _objc_msgSend$tagSubscriptionStatusProvider
+ _objc_msgSend$tags
+ _objc_msgSend$traitCollectionByModifyingTraits:
+ _objc_msgSend$viewControllerPresentationManager
- -[SXEmbedComponentView initWithDOMObjectProvider:viewport:presentationDelegate:componentStyleRendererFactory:reachabilityProvider:embedDataProvider:actionHandler:layoutInvalidator:websiteDataStore:relatedWebViewCache:proxyAuthenticationHandler:sceneStateMonitor:analyticsReporting:]
- -[SXEmbedComponentView relatedWebViewCache]
- -[SXEmbedComponentViewFactory initWithDOMObjectProvider:viewport:presentationDelegateProvider:componentStyleRendererFactory:reachabilityProvider:embedDataProvider:actionHandler:layoutInvalidator:websiteDataStore:relatedWebViewCache:proxyAuthenticationHandler:sceneStateMonitor:analyticsReportingProvider:]
- -[SXEmbedComponentViewFactory relatedWebViewCache]
- -[SXFormatInteractor initWithLayoutCoordinator:layoutOptionsFactory:presentationAttributesProvider:subscriptionStatusProvider:debugLayoutOptionsProvider:newsletterSubscriptionStatusProvider:offerUpsellScenarioProvider:subscriptionActivationEligibilityProvider:renderingConfigurationProvider:]
- -[SXLayoutOptions initWithColumnLayout:viewportSize:traitCollection:contentSizeCategory:bundleSubscriptionStatus:channelSubscriptionStatus:testing:viewingLocation:contentScaleFactor:newsletterSubscriptionStatus:offerUpsellScenario:subscriptionActivationEligibility:smartInvertColorsEnabled:conditionKeys:]
- -[SXLayoutOptionsFactory createLayoutOptionsWithViewportSize:safeAreaInsets:traitCollection:bundleSubscriptionStatus:channelSubscriptionStatus:contentSizeCategory:testing:viewingLocation:contentScaleFactor:newsletterSubscriptionStatus:offerUpsellScenario:subscriptionActivationEligibility:smartInvertColorsEnabled:conditionKeys:]
- -[SXRelatedWebViewCache .cxx_destruct]
- -[SXRelatedWebViewCache cache]
- -[SXRelatedWebViewCache init]
- -[SXRelatedWebViewCache relatedWebViewForBaseURL:]
- -[SXRelatedWebViewCache storeRelatedWebView:baseURL:]
- -[SXWebContentConfigurationProvider initWithPresentationAttributesProvider:storeFrontProvider:liveActivityAttributesProvider:locale:location:]
- _OBJC_CLASS_$_SXRelatedWebViewCache
- _OBJC_IVAR_$_SXEmbedComponentView._relatedWebViewCache
- _OBJC_IVAR_$_SXEmbedComponentViewFactory._relatedWebViewCache
- _OBJC_IVAR_$_SXRelatedWebViewCache._cache
- _OBJC_METACLASS_$_SXRelatedWebViewCache
- __OBJC_$_INSTANCE_METHODS_SXRelatedWebViewCache
- __OBJC_$_INSTANCE_VARIABLES_SXRelatedWebViewCache
- __OBJC_$_PROP_LIST_SXCondition.186
- __OBJC_$_PROP_LIST_SXConditionHints.120
- __OBJC_$_PROP_LIST_SXConditionValidationContext.106
- __OBJC_$_PROP_LIST_SXFormatInteractor.158
- __OBJC_$_PROP_LIST_SXLinkAction.68
- __OBJC_$_PROP_LIST_SXRelatedWebViewCache
- __OBJC_CLASS_RO_$_SXRelatedWebViewCache
- __OBJC_METACLASS_RO_$_SXRelatedWebViewCache
- ___282-[SXEmbedComponentView initWithDOMObjectProvider:viewport:presentationDelegate:componentStyleRendererFactory:reachabilityProvider:embedDataProvider:actionHandler:layoutInvalidator:websiteDataStore:relatedWebViewCache:proxyAuthenticationHandler:sceneStateMonitor:analyticsReporting:]_block_invoke
- ___block_literal_global.114
- ___block_literal_global.134
- ___block_literal_global.180
- ___block_literal_global.205
- ___block_literal_global.212
- ___block_literal_global.237
- ___block_literal_global.241
- ___block_literal_global.243
- ___block_literal_global.247
- ___block_literal_global.255
- ___block_literal_global.271
- ___block_literal_global.273
- ___block_literal_global.285
- ___block_literal_global.299
- ___block_literal_global.309
- ___block_literal_global.419
- ___block_literal_global.422
- ___block_literal_global.425
- ___block_literal_global.428
- ___block_literal_global.432
- ___block_literal_global.435
- ___block_literal_global.438
- ___block_literal_global.441
- ___block_literal_global.444
- ___block_literal_global.447
- ___block_literal_global.450
- ___block_literal_global.453
- ___block_literal_global.456
- ___block_literal_global.459
- ___block_literal_global.462
- ___block_literal_global.465
- ___block_literal_global.468
- ___block_literal_global.472
- ___block_literal_global.474
- ___block_literal_global.476
- ___block_literal_global.480
- ___block_literal_global.482
- ___block_literal_global.484
- ___block_literal_global.488
- ___block_literal_global.493
- ___block_literal_global.496
- ___block_literal_global.498
- ___block_literal_global.501
- _objc_msgSend$_setRelatedWebView:
- _objc_msgSend$createLayoutOptionsWithViewportSize:safeAreaInsets:traitCollection:bundleSubscriptionStatus:channelSubscriptionStatus:contentSizeCategory:testing:viewingLocation:contentScaleFactor:newsletterSubscriptionStatus:offerUpsellScenario:subscriptionActivationEligibility:smartInvertColorsEnabled:conditionKeys:
- _objc_msgSend$hasTelephonyScheme
- _objc_msgSend$initWithColumnLayout:viewportSize:traitCollection:contentSizeCategory:bundleSubscriptionStatus:channelSubscriptionStatus:testing:viewingLocation:contentScaleFactor:newsletterSubscriptionStatus:offerUpsellScenario:subscriptionActivationEligibility:smartInvertColorsEnabled:conditionKeys:
- _objc_msgSend$initWithDOMObjectProvider:viewport:presentationDelegate:componentStyleRendererFactory:reachabilityProvider:embedDataProvider:actionHandler:layoutInvalidator:websiteDataStore:relatedWebViewCache:proxyAuthenticationHandler:sceneStateMonitor:analyticsReporting:
- _objc_msgSend$initWithDOMObjectProvider:viewport:presentationDelegateProvider:componentStyleRendererFactory:reachabilityProvider:embedDataProvider:actionHandler:layoutInvalidator:websiteDataStore:relatedWebViewCache:proxyAuthenticationHandler:sceneStateMonitor:analyticsReportingProvider:
- _objc_msgSend$initWithLayoutCoordinator:layoutOptionsFactory:presentationAttributesProvider:subscriptionStatusProvider:debugLayoutOptionsProvider:newsletterSubscriptionStatusProvider:offerUpsellScenarioProvider:subscriptionActivationEligibilityProvider:renderingConfigurationProvider:
- _objc_msgSend$initWithPresentationAttributesProvider:storeFrontProvider:liveActivityAttributesProvider:locale:location:
- _objc_msgSend$initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:networkStatus:isTransitioning:
- _objc_msgSend$relatedWebViewCache
- _objc_msgSend$relatedWebViewForBaseURL:
- _objc_msgSend$storeRelatedWebView:baseURL:
CStrings:
+ "  offerIdentifier: %@; \n"
+ "  tagSubscriptionStatus: %@; \n"
+ "1.30"
+ "; following: %@"
+ "; tags: %@"
+ "@\"<SWFeedConfigurationFactory>\""
+ "@\"<SWViewControllerPresentingManager>\""
+ "@\"<SXAction>\"36@0:8@\"NSURL\"16@\"SXJSONDictionary\"24B32"
+ "@\"<SXOfferIdentifierProviding>\""
+ "@\"<SXOfferIdentifierProviding>\"16@?0@\"<TFResolver>\"8"
+ "@\"<SXTagSubscriptionStatusProviding>\""
+ "@\"SWFeedConfiguration\"24@0:8@\"UIViewController\"16"
+ "@\"SXFollowingCondition\"16@0:8"
+ "@\"SXLayoutOptions\"168@0:8{CGSize=dd}16{UIEdgeInsets=dddd}32@\"UITraitCollection\"64q72q80@\"NSString\"88B96Q100d108Q116q124q132@\"NSString\"140B148@\"NSSet\"152@\"SXTagSubscriptionStatus\"160"
+ "@\"SXOfferIdentifierConditionValidator\"16@?0@\"<TFResolver>\"8"
+ "@\"SXTagSubscriptionStatus\""
+ "@\"SXTagSubscriptionStatus\"16@0:8"
+ "@\"SXTagSubscriptionStatus\"24@0:8@\"SXTagSubscriptionStatus\"16"
+ "@\"SXWebProcessPoolCache\""
+ "@104@0:8@16@24@32@40@48@56@64@72@80@88@96"
+ "@144@0:8@16{CGSize=dd}24@40@48q56q64B72Q76d84Q92q100q108@116B124@128@136"
+ "@168@0:8{CGSize=dd}16{UIEdgeInsets=dddd}32@64q72q80@88B96Q100d108Q116q124q132@140B148@152@160"
+ "@28@0:8B16@20"
+ "@36@0:8@16@24B32"
+ "Received callback in response to change in offer identifier"
+ "Received callback in response to change in tag subscription status"
+ "SWFeedConfigurationFactory"
+ "SXFollowingCondition"
+ "SXFollowingConditionValidator"
+ "SXOfferIdentifierConditionValidator"
+ "SXOfferIdentifierDefaultProvider"
+ "SXOfferIdentifierObserving"
+ "SXOfferIdentifierProviding"
+ "SXTagSubscriptionStatus"
+ "SXTagSubscriptionStatusAssembly"
+ "SXTagSubscriptionStatusObserving"
+ "SXTagSubscriptionStatusProvider"
+ "SXTagSubscriptionStatusProviding"
+ "SXWebProcessPoolCache"
+ "T@\"<SWFeedConfigurationFactory>\",R,N,V_feedConfigurationFactory"
+ "T@\"<SWViewControllerPresentingManager>\",R,N,V_viewControllerPresentationManager"
+ "T@\"<SXOfferIdentifierProviding>\",R,N,V_offerIdentifierProvider"
+ "T@\"<SXTagSubscriptionStatusProviding>\",R,N,V_tagSubscriptionStatusProvider"
+ "T@\"NSArray\",R,C,N,V_tags"
+ "T@\"NSString\",C,N,V_offerIdentifier"
+ "T@\"NSString\",R,N,V_offerIdentifier"
+ "T@\"NSString\",R,N,V_tagIdentifier"
+ "T@\"SXFollowingCondition\",R,D,N"
+ "T@\"SXFollowingCondition\",R,N"
+ "T@\"SXTagSubscriptionStatus\",R,N"
+ "T@\"SXTagSubscriptionStatus\",R,N,V_tagSubscriptionStatus"
+ "T@\"SXWebProcessPoolCache\",R,N,V_processPoolCache"
+ "TB,R,N,V_following"
+ "TB,R,N,V_openInBrowser"
+ "TagSubscriptionStatus; "
+ "Will determine optimal image resources, viewportSize=(%.0f, %.0f), screenScale=%0.1f, extendedColor=%{public}@"
+ "_feedConfigurationFactory"
+ "_following"
+ "_headroomUsage"
+ "_offerIdentifier"
+ "_offerIdentifierProvider"
+ "_openInBrowser"
+ "_processPoolCache"
+ "_tagIdentifier"
+ "_tagSubscriptionStatus"
+ "_tagSubscriptionStatusProvider"
+ "_tags"
+ "_viewControllerPresentationManager"
+ "actionForURL:analytics:openInBrowser:"
+ "b"
+ "createFeedConfigurationForViewController:"
+ "createLayoutOptionsWithViewportSize:safeAreaInsets:traitCollection:bundleSubscriptionStatus:channelSubscriptionStatus:contentSizeCategory:testing:viewingLocation:contentScaleFactor:newsletterSubscriptionStatus:offerUpsellScenario:subscriptionActivationEligibility:offerIdentifier:smartInvertColorsEnabled:conditionKeys:tagSubscriptionStatus:"
+ "feedConfigurationFactory"
+ "following"
+ "followingWithValue:withType:"
+ "initWithBounds:contentFrame:contentSafeAreaFrame:systemSafeAreaFrame:"
+ "initWithColumnLayout:viewportSize:traitCollection:contentSizeCategory:bundleSubscriptionStatus:channelSubscriptionStatus:testing:viewingLocation:contentScaleFactor:newsletterSubscriptionStatus:offerUpsellScenario:subscriptionActivationEligibility:offerIdentifier:smartInvertColorsEnabled:conditionKeys:tagSubscriptionStatus:"
+ "initWithDOMObjectProvider:viewport:presentationDelegate:componentStyleRendererFactory:reachabilityProvider:embedDataProvider:actionHandler:layoutInvalidator:websiteDataStore:processPoolCache:proxyAuthenticationHandler:sceneStateMonitor:analyticsReporting:"
+ "initWithDOMObjectProvider:viewport:presentationDelegateProvider:componentStyleRendererFactory:reachabilityProvider:embedDataProvider:actionHandler:layoutInvalidator:websiteDataStore:processPoolCache:proxyAuthenticationHandler:sceneStateMonitor:analyticsReportingProvider:"
+ "initWithFollowing:tagIdentifier:"
+ "initWithFollowing:tags:"
+ "initWithLayoutCoordinator:layoutOptionsFactory:presentationAttributesProvider:subscriptionStatusProvider:debugLayoutOptionsProvider:newsletterSubscriptionStatusProvider:offerUpsellScenarioProvider:subscriptionActivationEligibilityProvider:offerIdentifierProvider:renderingConfigurationProvider:tagSubscriptionStatusProvider:"
+ "initWithPresentationAttributesProvider:storeFrontProvider:liveActivityAttributesProvider:feedConfigurationFactory:viewControllerPresentationManager:locale:location:"
+ "initWithStoreFront:locale:contentEnvironment:contentSizeCategory:layoutGuide:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:networkStatus:isTransitioning:"
+ "initWithURL:analytics:openInBrowser:"
+ "isDefaultCallingAppScheme:"
+ "offerIdentifier"
+ "offerIdentifierDidChangeFromIdentifier:to:"
+ "offerIdentifierProvider"
+ "offerIdentifierWithValue:withType:"
+ "openInBrowser"
+ "overrideOfferIdentifier:"
+ "overridePropertyMap"
+ "overrideTagSubscriptionStatus:"
+ "processPoolCache"
+ "processPoolForBaseURL:"
+ "registerForHDRTraitChanges"
+ "registerForTraitChanges:withHandler:"
+ "setOfferIdentifier:"
+ "setOverrideUserInterfaceStyle:"
+ "setPreferredDynamicRange:"
+ "setUserInterfaceStyle:"
+ "setUsesSingleWebProcess:"
+ "setValuesForProperties:"
+ "tagIdentifier"
+ "tagSubscriptionStatus"
+ "tagSubscriptionStatusChangedFromStatus:"
+ "tagSubscriptionStatusProvider"
+ "tags"
+ "traitCollectionByModifyingTraits:"
+ "unknown-offer-identifier"
+ "v16@?0@\"<UIMutableTraits>\"8"
+ "v24@0:8@\"<SXOfferIdentifierObserving>\"16"
+ "v24@0:8@\"<SXTagSubscriptionStatusObserving>\"16"
+ "v24@0:8@\"SXTagSubscriptionStatus\"16"
+ "v24@?0@\"<UITraitEnvironment>\"8@\"UITraitCollection\"16"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
+ "v32@0:8@\"WKWebView\"16@\"UIInputSuggestion\"24"
+ "viewControllerPresentationManager"
+ "webView:insertInputSuggestion:"
- "1.29.1"
- "@\"SXLayoutOptions\"152@0:8{CGSize=dd}16{UIEdgeInsets=dddd}32@\"UITraitCollection\"64q72q80@\"NSString\"88B96Q100d108Q116q124q132B140@\"NSSet\"144"
- "@\"SXRelatedWebViewCache\""
- "@128@0:8@16{CGSize=dd}24@40@48q56q64B72Q76d84Q92q100q108B116@120"
- "@152@0:8{CGSize=dd}16{UIEdgeInsets=dddd}32@64q72q80@88B96Q100d108Q116q124q132B140@144"
- "FaceTime Audio"
- "SXRelatedWebViewCache"
- "T@\"SXRelatedWebViewCache\",R,N,V_relatedWebViewCache"
- "_relatedWebViewCache"
- "_setRelatedWebView:"
- "createLayoutOptionsWithViewportSize:safeAreaInsets:traitCollection:bundleSubscriptionStatus:channelSubscriptionStatus:contentSizeCategory:testing:viewingLocation:contentScaleFactor:newsletterSubscriptionStatus:offerUpsellScenario:subscriptionActivationEligibility:smartInvertColorsEnabled:conditionKeys:"
- "hasTelephonyScheme"
- "initWithColumnLayout:viewportSize:traitCollection:contentSizeCategory:bundleSubscriptionStatus:channelSubscriptionStatus:testing:viewingLocation:contentScaleFactor:newsletterSubscriptionStatus:offerUpsellScenario:subscriptionActivationEligibility:smartInvertColorsEnabled:conditionKeys:"
- "initWithDOMObjectProvider:viewport:presentationDelegate:componentStyleRendererFactory:reachabilityProvider:embedDataProvider:actionHandler:layoutInvalidator:websiteDataStore:relatedWebViewCache:proxyAuthenticationHandler:sceneStateMonitor:analyticsReporting:"
- "initWithDOMObjectProvider:viewport:presentationDelegateProvider:componentStyleRendererFactory:reachabilityProvider:embedDataProvider:actionHandler:layoutInvalidator:websiteDataStore:relatedWebViewCache:proxyAuthenticationHandler:sceneStateMonitor:analyticsReportingProvider:"
- "initWithLayoutCoordinator:layoutOptionsFactory:presentationAttributesProvider:subscriptionStatusProvider:debugLayoutOptionsProvider:newsletterSubscriptionStatusProvider:offerUpsellScenarioProvider:subscriptionActivationEligibilityProvider:renderingConfigurationProvider:"
- "initWithPresentationAttributesProvider:storeFrontProvider:liveActivityAttributesProvider:locale:location:"
- "initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:networkStatus:isTransitioning:"
- "relatedWebViewCache"
- "relatedWebViewForBaseURL:"
- "storeRelatedWebView:baseURL:"

```
