## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient`

```diff

-617.0.0.0.0
-  __TEXT.__text: 0x18c6b8
+619.0.1.0.0
+  __TEXT.__text: 0x18ce9c
   __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_methlist: 0x18a84
+  __TEXT.__objc_methlist: 0x18a94
   __TEXT.__const: 0x6f8
-  __TEXT.__cstring: 0x1b84e
-  __TEXT.__oslogstring: 0x1746f
-  __TEXT.__gcc_except_tab: 0x22fc
+  __TEXT.__cstring: 0x1b8d4
+  __TEXT.__oslogstring: 0x17944
+  __TEXT.__gcc_except_tab: 0x2314
   __TEXT.__dlopen_cstrs: 0x42d
   __TEXT.__ustring: 0x18a
-  __TEXT.__unwind_info: 0x66b0
-  __TEXT.__objc_classname: 0x3be3
-  __TEXT.__objc_methname: 0x34135
-  __TEXT.__objc_methtype: 0x676d
-  __TEXT.__objc_stubs: 0x1cae0
-  __DATA_CONST.__got: 0x16f8
-  __DATA_CONST.__const: 0x6370
-  __DATA_CONST.__objc_classlist: 0xe48
+  __TEXT.__unwind_info: 0x66c0
+  __TEXT.__objc_classname: 0x3bc8
+  __TEXT.__objc_methname: 0x341af
+  __TEXT.__objc_methtype: 0x675c
+  __TEXT.__objc_stubs: 0x1cb40
+  __DATA_CONST.__got: 0x16e8
+  __DATA_CONST.__const: 0x62f0
+  __DATA_CONST.__objc_classlist: 0xe40
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9ea8
+  __DATA_CONST.__objc_selrefs: 0x9ec8
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0xc50
+  __DATA_CONST.__objc_superrefs: 0xc48
   __DATA_CONST.__objc_arraydata: 0xaf8
   __AUTH_CONST.__auth_got: 0x790
-  __AUTH_CONST.__const: 0x2a60
-  __AUTH_CONST.__cfstring: 0x15180
-  __AUTH_CONST.__objc_const: 0x45cf0
-  __AUTH_CONST.__objc_intobj: 0xa38
+  __AUTH_CONST.__const: 0x2a80
+  __AUTH_CONST.__cfstring: 0x151a0
+  __AUTH_CONST.__objc_const: 0x45c88
+  __AUTH_CONST.__objc_intobj: 0xa20
   __AUTH_CONST.__objc_arrayobj: 0x6d8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x168
-  __AUTH.__objc_data: 0x3de0
-  __DATA.__objc_ivar: 0x1c58
+  __AUTH.__objc_data: 0x4330
+  __DATA.__objc_ivar: 0x1c5c
   __DATA.__data: 0x1cf0
   __DATA.__bss: 0x390
-  __DATA_DIRTY.__objc_data: 0x50f0
+  __DATA_DIRTY.__objc_data: 0x4b50
   __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__bss: 0x2c8
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E79F413E-AFB7-373B-A033-4BABB8955627
-  Functions: 10656
-  Symbols:   35071
-  CStrings:  15992
+  UUID: 69DAE239-7106-3B1B-824C-546A6B63ECDD
+  Functions: 10661
+  Symbols:   35077
+  CStrings:  16013
 
Symbols:
+ +[ATXDefaultHomeScreenItemManager isCHSWidgetDescriptorAllowedForCarPlay:disabledApps:excludedWidgetsWithIdentifiers:]
+ +[ATXDefaultHomeScreenItemManager isDescriptorWithWidgetKindSpecial:]
+ +[ATXDefaultHomeScreenItemManager shouldFilterOutChronoWidgetDescriptorDueToDenyList:fromExcludedWidgetsWithIdentifiers:]
+ +[ATXDefaultHomeScreenItemManager shouldFilterOutWidgetDescriptorWithBundleIdDueToAppProtection:fromDisabledApps:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer hasConfiguredHomeAccessoryControl]
+ -[ATXDefaultHomeScreenItemTilerGridSize2 initWithDefaultStack:defaultWidgetsSmall:defaultWidgetsMedium:defaultWidgetsLarge:defaultWidgetsExtraLarge:widgetFamilyMask:targetNumberOfSuggestions:]
+ -[ATXDefaultHomeScreenItemTilerGridSize3 initWithDefaultStack:defaultWidgetsSmall:defaultWidgetsMedium:defaultWidgetsLarge:defaultWidgetsExtraLarge:widgetFamilyMask:targetNumberOfSuggestions:]
+ -[ATXDefaultHomeScreenItemTilerPodBuilder initWithDefaultStack:defaultWidgetsSmall:defaultWidgetsMedium:defaultWidgetsLarge:defaultWidgetsExtraLarge:widgetFamilyMask:targetNumberOfSuggestions:]
+ -[ATXDefaultHomeScreenItemTilerPodBuilder setTargetNumberOfSuggestions:]
+ -[ATXDefaultHomeScreenItemTilerPodBuilder targetNumberOfSuggestions]
+ -[ATXDefaultHomeScreenItemTilerWrapper initWithDefaultStack:defaultWidgetsSmall:defaultWidgetsMedium:defaultWidgetsLarge:defaultWidgetsExtraLarge:widgetFamilyMask:gridSize:galleryRequest:]
+ -[ATXDefaultHomeScreenItemTilerWrapper initWithDefaultStack:defaultWidgetsSmall:defaultWidgetsMedium:defaultWidgetsLarge:defaultWidgetsExtraLarge:widgetFamilyMask:gridSize:galleryRequest:].cold.1
+ _OBJC_CLASS_$_BMHomeKitClientAccessoryControl
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemTilerGridSize2._targetNumberOfSuggestions
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemTilerGridSize3._targetNumberOfSuggestions
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemTilerPodBuilder._targetNumberOfSuggestions
+ ___202-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedAmbientOnboardingStacksForSize:stack1RequiredWidgetPersonalities:stack2RequiredWidgetPersonalities:rankedWidgets:usedWidgetPersonalities:]_block_invoke.112
+ ___248-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedOnboardingStackForSize:requiredWidgetPersonalities:conditionalWidgetPersonalities:fallbackWidgetPersonalities:rankedThirdPartyWidgets:usedWidgetPersonalities:shouldAdd3PWidgetToStack:]_block_invoke.124
+ ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.377
+ ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.377.cold.1
+ ___75-[ATXDefaultHomeScreenItemManager galleryItemsForCarPlayWithRequest:error:]_block_invoke
+ ___76-[ATXDefaultHomeScreenItemOnboardingStacksProducer _carPlayOnboardingStacks]_block_invoke
+ ___76-[ATXDefaultHomeScreenItemOnboardingStacksProducer _carPlayOnboardingStacks]_block_invoke.91
+ ___76-[ATXDefaultHomeScreenItemOnboardingStacksProducer _carPlayOnboardingStacks]_block_invoke.96
+ ___85-[ATXDefaultHomeScreenItemOnboardingStacksProducer hasConfiguredHomeAccessoryControl]_block_invoke
+ ___85-[ATXDefaultHomeScreenItemOnboardingStacksProducer hasConfiguredHomeAccessoryControl]_block_invoke.146
+ ___85-[ATXDefaultHomeScreenItemOnboardingStacksProducer hasConfiguredHomeAccessoryControl]_block_invoke.146.cold.1
+ ___85-[ATXDefaultHomeScreenItemOnboardingStacksProducer hasConfiguredHomeAccessoryControl]_block_invoke.cold.1
+ ___86-[ATXDefaultHomeScreenItemManager fetchWidgetSmartStackWithRequest:completionHandler:]_block_invoke.67
+ ___86-[ATXDefaultHomeScreenItemManager fetchWidgetSmartStackWithRequest:completionHandler:]_block_invoke.71
+ ___91-[ATXDefaultHomeScreenItemUpdater _updateAmbientDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke.51
+ ___91-[ATXDefaultHomeScreenItemUpdater _updateAmbientDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke_2.56
+ ___91-[ATXDefaultHomeScreenItemUpdater _updateAmbientDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke_2.56.cold.1
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.77.cold.1
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.77.cold.2
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.77.cold.3
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.77.cold.4
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.87
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.88
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.91
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke_2.89
+ ___block_descriptor_32_e30_16?0"ATXWidgetPersonality"8l
+ ___block_descriptor_32_e39_16?0"ATXHomeScreenWidgetDescriptor"8l
+ ___block_descriptor_33_e30_B16?0"ATXWidgetPersonality"8l
+ ___block_literal_global.105
+ ___block_literal_global.114
+ ___block_literal_global.121
+ ___block_literal_global.123
+ ___block_literal_global.145
+ ___block_literal_global.54
+ ___block_literal_global.94
+ _objc_msgSend$AccessoryControl
+ _objc_msgSend$Client
+ _objc_msgSend$HomeKit
+ _objc_msgSend$hasConfiguredHomeAccessoryControl
+ _objc_msgSend$initWithDefaultStack:defaultWidgetsSmall:defaultWidgetsMedium:defaultWidgetsLarge:defaultWidgetsExtraLarge:widgetFamilyMask:gridSize:galleryRequest:
+ _objc_msgSend$initWithDefaultStack:defaultWidgetsSmall:defaultWidgetsMedium:defaultWidgetsLarge:defaultWidgetsExtraLarge:widgetFamilyMask:targetNumberOfSuggestions:
+ _objc_msgSend$isCHSWidgetDescriptorAllowedForCarPlay:disabledApps:excludedWidgetsWithIdentifiers:
+ _objc_msgSend$isDescriptorWithWidgetKindSpecial:
+ _objc_msgSend$serviceType
+ _objc_msgSend$shouldFilterOutChronoWidgetDescriptorDueToDenyList:fromExcludedWidgetsWithIdentifiers:
+ _objc_msgSend$shouldFilterOutWidgetDescriptorWithBundleIdDueToAppProtection:fromDisabledApps:
+ _objc_msgSend$targetNumberOfSuggestions
- +[ATXDefaultHomeScreenItemManager isCHSWidgetDescriptorAllowedForCarPlayOnboardingStacks:]
- -[ATXAppLaunchCarPlayContext .cxx_destruct]
- -[ATXAppLaunchCarPlayContext appLaunchCountAndDistinctDaysLaunchedWhileConnectedToCarPlayForNumberOfDays:]
- -[ATXAppLaunchCarPlayContext initWithAppInFocusStream:carPlayStream:]
- -[ATXAppLaunchCarPlayContext init]
- -[ATXDefaultHomeScreenItemTilerGridSize2 initWithDefaultStack:defaultWidgetsSmall:defaultWidgetsMedium:defaultWidgetsLarge:defaultWidgetsExtraLarge:widgetFamilyMask:]
- -[ATXDefaultHomeScreenItemTilerGridSize3 initWithDefaultStack:defaultWidgetsSmall:defaultWidgetsMedium:defaultWidgetsLarge:defaultWidgetsExtraLarge:widgetFamilyMask:]
- -[ATXDefaultHomeScreenItemTilerPodBuilder initWithDefaultStack:defaultWidgetsSmall:defaultWidgetsMedium:defaultWidgetsLarge:defaultWidgetsExtraLarge:widgetFamilyMask:]
- -[ATXDefaultHomeScreenItemTilerWrapper initWithDefaultStack:defaultWidgetsSmall:defaultWidgetsMedium:defaultWidgetsLarge:defaultWidgetsExtraLarge:widgetFamilyMask:gridSize:]
- -[ATXDefaultHomeScreenItemTilerWrapper initWithDefaultStack:defaultWidgetsSmall:defaultWidgetsMedium:defaultWidgetsLarge:defaultWidgetsExtraLarge:widgetFamilyMask:gridSize:].cold.1
- _OBJC_CLASS_$_ATXAppInFocusStream
- _OBJC_CLASS_$_ATXAppLaunchCarPlayContext
- _OBJC_CLASS_$_ATXCarPlayConnectedStream
- _OBJC_IVAR_$_ATXAppLaunchCarPlayContext._appInFocusStream
- _OBJC_IVAR_$_ATXAppLaunchCarPlayContext._carPlayConnectedStream
- _OBJC_METACLASS_$_ATXAppLaunchCarPlayContext
- __OBJC_$_INSTANCE_METHODS_ATXAppLaunchCarPlayContext
- __OBJC_$_INSTANCE_VARIABLES_ATXAppLaunchCarPlayContext
- __OBJC_CLASS_RO_$_ATXAppLaunchCarPlayContext
- __OBJC_METACLASS_RO_$_ATXAppLaunchCarPlayContext
- ___106-[ATXAppLaunchCarPlayContext appLaunchCountAndDistinctDaysLaunchedWhileConnectedToCarPlayForNumberOfDays:]_block_invoke
- ___106-[ATXAppLaunchCarPlayContext appLaunchCountAndDistinctDaysLaunchedWhileConnectedToCarPlayForNumberOfDays:]_block_invoke.25
- ___106-[ATXAppLaunchCarPlayContext appLaunchCountAndDistinctDaysLaunchedWhileConnectedToCarPlayForNumberOfDays:]_block_invoke_2
- ___106-[ATXAppLaunchCarPlayContext appLaunchCountAndDistinctDaysLaunchedWhileConnectedToCarPlayForNumberOfDays:]_block_invoke_3
- ___106-[ATXAppLaunchCarPlayContext appLaunchCountAndDistinctDaysLaunchedWhileConnectedToCarPlayForNumberOfDays:]_block_invoke_4
- ___106-[ATXAppLaunchCarPlayContext appLaunchCountAndDistinctDaysLaunchedWhileConnectedToCarPlayForNumberOfDays:]_block_invoke_5
- ___202-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedAmbientOnboardingStacksForSize:stack1RequiredWidgetPersonalities:stack2RequiredWidgetPersonalities:rankedWidgets:usedWidgetPersonalities:]_block_invoke.102
- ___248-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedOnboardingStackForSize:requiredWidgetPersonalities:conditionalWidgetPersonalities:fallbackWidgetPersonalities:rankedThirdPartyWidgets:usedWidgetPersonalities:shouldAdd3PWidgetToStack:]_block_invoke.114
- ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.374
- ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.374.cold.1
- ___86-[ATXDefaultHomeScreenItemManager fetchWidgetSmartStackWithRequest:completionHandler:]_block_invoke_3
- ___91-[ATXDefaultHomeScreenItemUpdater _updateAmbientDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke.52
- ___91-[ATXDefaultHomeScreenItemUpdater _updateAmbientDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke_2.57
- ___91-[ATXDefaultHomeScreenItemUpdater _updateAmbientDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke_2.57.cold.1
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.72
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.72.cold.1
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.72.cold.2
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.72.cold.3
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.72.cold.4
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.73
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.86
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke_2.84
- ___block_descriptor_32_e34_B16?0"ATXCarPlayConnectedEvent"8l
- ___block_descriptor_32_e63_q24?0"ATXCarPlayConnectedEvent"8"ATXCarPlayConnectedEvent"16l
- ___block_descriptor_40_e8_32s_e27_B24?0"NSDate"8"NSDate"16ls32l8
- ___block_descriptor_40_e8_32s_e34_v16?0"ATXCarPlayConnectedEvent"8ls32l8
- ___block_descriptor_48_e8_32s40s_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e35_B16?0"ATXAppInFocusEventSession"8ls56l8s32l8s40l8s48l8
- ___block_literal_global.63
- ___block_literal_global.99
- _objc_msgSend$appLaunchCountAndDistinctDaysLaunchedWhileConnectedToCarPlayForNumberOfDays:
- _objc_msgSend$appSessionEndTime
- _objc_msgSend$appSessionStartTime
- _objc_msgSend$enumerateAllAppLaunchSessionsFromStartDate:bundleIDFilter:block:
- _objc_msgSend$enumerateConnectedEventsFromStartDate:endDate:filterBlock:limit:ascending:block:
- _objc_msgSend$initWithAppInFocusStream:carPlayStream:
- _objc_msgSend$initWithDefaultStack:defaultWidgetsSmall:defaultWidgetsMedium:defaultWidgetsLarge:defaultWidgetsExtraLarge:widgetFamilyMask:
- _objc_msgSend$initWithDefaultStack:defaultWidgetsSmall:defaultWidgetsMedium:defaultWidgetsLarge:defaultWidgetsExtraLarge:widgetFamilyMask:gridSize:
- _objc_msgSend$isCHSWidgetDescriptorAllowedForCarPlayOnboardingStacks:
CStrings:
+ "%s BundleID: %@; Raw launch Count: %lu; Unique days launched: %lu"
+ "%s Randomly selecting a widget from all equally ranked widgets for Stack"
+ "%s Returning the highest-ranked widget for stack based on app usage: %@"
+ "%s: No bundleId provided for Widget descriptor"
+ "%s: Number of Stacks being requested %lu"
+ "%s: filtering out widget descriptor. Reason: Show on Homescreen is disabled for widget with bundleId %@"
+ "%s: filtering out widget descriptor. Reason: The parent bundleId %@ is locked or hidden by user preference"
+ "+[ATXDefaultHomeScreenItemManager shouldFilterOutWidgetDescriptorWithBundleIdDueToAppProtection:fromDisabledApps:]"
+ "+[ATXDefaultHomeScreenItemProducerUtilities eligibleThirdPartyWidgetFromSimilarWidgets:launchCounts:]"
+ "-[ATXDefaultHomeScreenItemOnboardingStacksProducer _carPlayOnboardingStacks]"
+ "@72@0:8@\"ATXDefaultWidgetStack\"16@\"NSArray\"24@\"NSArray\"32@\"NSArray\"40@\"NSArray\"48Q56Q64"
+ "@80@0:8@16@24@32@40@48Q56Q64@72"
+ "AccessoryControl"
+ "Client"
+ "Could not fetch Home accessory events. Error: %@"
+ "Descriptor with container bundle identifier is either disabled on homescreen or locked/hidden due to app protection: %@"
+ "Descriptor with extension bundle identifier is disfavored in CarPlay: %@"
+ "Descriptor with extension bundle identifier is in the deny list: %@"
+ "Descriptor with extension bundle identifier is linked before Crystal: %@"
+ "Descriptor with kind is not allowed in CarPlay: %@"
+ "HomeKit"
+ "Incorrect class received while fetching home accessory events: %@"
+ "No Home accessory is configured. Filtering out default Home widget"
+ "Number of Stacks returned for Carplay: %lu"
+ "Number of widgets requested for CarPlay widget add sheet: %@"
+ "Number of widgets returned for CarPlay widget add sheet suggestions is %lu; Widgets: %@"
+ "Required widgets for Stack with key %@ are %@"
+ "TQ,N,V_targetNumberOfSuggestions"
+ "Widgets in Stack %lu: %@"
+ "_targetNumberOfSuggestions"
+ "com.apple.Home.HomeWidget.Interactive"
+ "hasConfiguredHomeAccessoryControl"
+ "initWithDefaultStack:defaultWidgetsSmall:defaultWidgetsMedium:defaultWidgetsLarge:defaultWidgetsExtraLarge:widgetFamilyMask:gridSize:galleryRequest:"
+ "initWithDefaultStack:defaultWidgetsSmall:defaultWidgetsMedium:defaultWidgetsLarge:defaultWidgetsExtraLarge:widgetFamilyMask:targetNumberOfSuggestions:"
+ "isCHSWidgetDescriptorAllowedForCarPlay:disabledApps:excludedWidgetsWithIdentifiers:"
+ "isDescriptorWithWidgetKindSpecial:"
+ "serviceType"
+ "setTargetNumberOfSuggestions:"
+ "shouldFilterOutChronoWidgetDescriptorDueToDenyList:fromExcludedWidgetsWithIdentifiers:"
+ "shouldFilterOutWidgetDescriptorWithBundleIdDueToAppProtection:fromDisabledApps:"
+ "targetNumberOfSuggestions"
- "%s: filtering out widget descriptor: %@. Reason: Show on Homescreen is disabled for parent bundleId %@"
- "@\"ATXAppInFocusStream\""
- "@\"ATXCarPlayConnectedStream\""
- "@64@0:8@\"ATXDefaultWidgetStack\"16@\"NSArray\"24@\"NSArray\"32@\"NSArray\"40@\"NSArray\"48Q56"
- "ATXAppLaunchCarPlayContext"
- "B16@?0@\"ATXAppInFocusEventSession\"8"
- "B16@?0@\"ATXCarPlayConnectedEvent\"8"
- "B24@?0@\"NSDate\"8@\"NSDate\"16"
- "_appInFocusStream"
- "_carPlayConnectedStream"
- "appLaunchCountAndDistinctDaysLaunchedWhileConnectedToCarPlayForNumberOfDays:"
- "appSessionEndTime"
- "appSessionStartTime"
- "enumerateAllAppLaunchSessionsFromStartDate:bundleIDFilter:block:"
- "enumerateConnectedEventsFromStartDate:endDate:filterBlock:limit:ascending:block:"
- "initWithAppInFocusStream:carPlayStream:"
- "initWithDefaultStack:defaultWidgetsSmall:defaultWidgetsMedium:defaultWidgetsLarge:defaultWidgetsExtraLarge:widgetFamilyMask:"
- "initWithDefaultStack:defaultWidgetsSmall:defaultWidgetsMedium:defaultWidgetsLarge:defaultWidgetsExtraLarge:widgetFamilyMask:gridSize:"
- "isCHSWidgetDescriptorAllowedForCarPlayOnboardingStacks:"
- "q24@?0@\"ATXCarPlayConnectedEvent\"8@\"ATXCarPlayConnectedEvent\"16"
- "v16@?0@\"ATXCarPlayConnectedEvent\"8"

```
