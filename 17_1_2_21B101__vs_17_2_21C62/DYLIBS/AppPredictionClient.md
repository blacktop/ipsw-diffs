## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient`

```diff

-541.5.2.0.1
-  __TEXT.__text: 0x1684c8
-  __TEXT.__auth_stubs: 0xe40
-  __TEXT.__objc_methlist: 0x14788
+541.10.0.0.0
+  __TEXT.__text: 0x168654
+  __TEXT.__auth_stubs: 0xe50
+  __TEXT.__objc_methlist: 0x14818
   __TEXT.__const: 0x568
   __TEXT.__cstring: 0x18bdf
-  __TEXT.__oslogstring: 0x1564d
+  __TEXT.__oslogstring: 0x1567c
   __TEXT.__gcc_except_tab: 0x1af4
   __TEXT.__dlopen_cstrs: 0x438
   __TEXT.__ustring: 0x18a
-  __TEXT.__unwind_info: 0x5ca0
+  __TEXT.__unwind_info: 0x5cb8
   __TEXT.__objc_classname: 0x33aa
-  __TEXT.__objc_methname: 0x2d39b
-  __TEXT.__objc_methtype: 0x5e9c
-  __TEXT.__objc_stubs: 0x19720
+  __TEXT.__objc_methname: 0x2d547
+  __TEXT.__objc_methtype: 0x5ede
+  __TEXT.__objc_stubs: 0x19840
   __DATA_CONST.__got: 0x2d8
   __DATA_CONST.__const: 0x5898
   __DATA_CONST.__objc_classlist: 0xc28
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x347b8
-  __DATA_CONST.__objc_selrefs: 0x8a98
+  __DATA_CONST.__objc_const: 0x34858
+  __DATA_CONST.__objc_selrefs: 0x8ae8
   __DATA_CONST.__objc_arraydata: 0xaf0
   __AUTH_CONST.__cfstring: 0x12fa0
   __AUTH_CONST.__objc_const: 0xa5f8

   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x730
+  __AUTH_CONST.__auth_got: 0x738
   __AUTH.__objc_data: 0x3318
   __DATA.__objc_protorefs: 0x98
-  __DATA.__objc_classrefs: 0x1258
+  __DATA.__objc_classrefs: 0x1260
   __DATA.__objc_superrefs: 0xa88
   __DATA.__objc_ivar: 0x18d8
   __DATA.__data: 0x18e8

   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation
+  - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/Sleep.framework/Sleep
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpotlightFoundation.framework/SpotlightFoundation

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9796
-  Symbols:   31028
-  CStrings:  11846
+  Functions: 9803
+  Symbols:   31053
+  CStrings:  11859
 
Symbols:
+ +[ATXSpotlightClient _imageCornerRoundingStyleForIconDisplayStyle:]
+ -[ATXFakeModeEntityScorer rankedContactsForDenyListForMode:options:]
+ -[ATXFakeModeEntityScorer rankedContactsForDenyListForMode:options:reply:]
+ -[ATXInterruptionManager recommendedDeniedContactsForMode:options:]
+ -[ATXModeEntityScorer rankedContactsForDenyListForMode:options:]
+ -[ATXModeEntityScorer rankedContactsForDenyListForMode:options:reply:]
+ -[ATXModeEntityScorerClient rankedContactsForDenyListForMode:options:reply:]
+ -[ATXModeEntityScorerClient rankedContactsForDenyListForMode:options:reply:].cold.1
+ -[ATXModeEntityScorerClient rankedContactsForDenyListForMode:options:reply:].cold.2
+ GCC_except_table38
+ GCC_except_table42
+ GCC_except_table44
+ GCC_except_table83
+ _ATXBundleIdReplacementForBundleIdWithWebpageURLHint
+ _OBJC_CLASS_$_BYSetupUserDisposition
+ ___124-[ATXModeEntityScorerClient assignModeEntityScores:entityTypeIdentifier:entityIdentifier:score:modeConfigurationType:reply:]_block_invoke.87
+ ___125-[ATXModeEntityScorerClient modeEntityScoresFromCacheForModeEntityTypeIdentifier:modeIdentifier:modeConfigurationType:reply:]_block_invoke.85
+ ___33-[ATXModeEntityScorerClient init]_block_invoke.50
+ ___50-[ATXModeEntityScorerClient scoreApps:mode:reply:]_block_invoke.68
+ ___53-[ATXModeEntityScorerClient rankedAppsForMode:reply:]_block_invoke.69
+ ___54-[ATXModeEntityScorerClient scoreContacts:mode:reply:]_block_invoke.65
+ ___56-[ATXModeEntityScorerClient rankedWidgetsForMode:reply:]_block_invoke.70
+ ___57-[ATXModeEntityScorerClient rankedContactsForMode:reply:]_block_invoke.67
+ ___59-[ATXModeEntityScorerClient scoreNotifications:mode:reply:]_block_invoke.71
+ ___61-[ATXModeEntityScorerClient scoreAppsForDenyList:mode:reply:]_block_invoke.78
+ ___62-[ATXModeEntityScorerClient rankedNotificationsForMode:reply:]_block_invoke.72
+ ___64-[ATXModeEntityScorer rankedContactsForDenyListForMode:options:]_block_invoke
+ ___64-[ATXModeEntityScorer rankedContactsForDenyListForMode:options:]_block_invoke.32
+ ___64-[ATXModeEntityScorer rankedContactsForDenyListForMode:options:]_block_invoke.32.cold.1
+ ___64-[ATXModeEntityScorer rankedContactsForDenyListForMode:options:]_block_invoke_2
+ ___64-[ATXModeEntityScorerClient rankedAppsForDenyListForMode:reply:]_block_invoke.79
+ ___65-[ATXModeEntityScorerClient scoreContactsForDenyList:mode:reply:]_block_invoke.83
+ ___67-[ATXInterruptionManager recommendedDeniedContactsForMode:options:]_block_invoke
+ ___69-[ATXModeEntityScorerClient rankedAppsForNotificationsForMode:reply:]_block_invoke.73
+ ___70-[ATXModeEntityScorer rankedContactsForDenyListForMode:options:reply:]_block_invoke
+ ___70-[ATXModeEntityScorer rankedContactsForDenyListForMode:options:reply:]_block_invoke.cold.1
+ ___73-[ATXModeEntityScorerClient rankedContactsForNotificationsForMode:reply:]_block_invoke.74
+ ___76-[ATXModeEntityScorerClient rankedContactsForDenyListForMode:options:reply:]_block_invoke
+ ___76-[ATXModeEntityScorerClient rankedContactsForDenyListForMode:options:reply:]_block_invoke.84
+ ___76-[ATXModeEntityScorerClient rankedContactsForDenyListForMode:options:reply:]_block_invoke.cold.1
+ ___block_literal_global.52
+ _objc_msgSend$_descriptorsByFilteringDescriptors:variant:
+ _objc_msgSend$_imageCornerRoundingStyleForIconDisplayStyle:
+ _objc_msgSend$_onboardingStacksByFilteringDescriptorsInOnboardingStacks:variant:
+ _objc_msgSend$_widgetStackByFilteringDescriptorsInWidgetStack:variant:
+ _objc_msgSend$isCHSWidgetDescriptorAllowedForAmbientOnboardingStacks:
+ _objc_msgSend$isChild
+ _objc_msgSend$isDescriptorSpecial:
+ _objc_msgSend$rankedContactsForDenyListForMode:options:
+ _objc_msgSend$rankedContactsForDenyListForMode:options:reply:
+ _objc_msgSend$recommendedDeniedContactsForMode:options:
- -[ATXModeEntityScorerClient rankedContactsForDenyListForMode:reply:].cold.1
- -[ATXModeEntityScorerClient rankedContactsForDenyListForMode:reply:].cold.2
- GCC_except_table43
- GCC_except_table82
- ___124-[ATXModeEntityScorerClient assignModeEntityScores:entityTypeIdentifier:entityIdentifier:score:modeConfigurationType:reply:]_block_invoke.84
- ___125-[ATXModeEntityScorerClient modeEntityScoresFromCacheForModeEntityTypeIdentifier:modeIdentifier:modeConfigurationType:reply:]_block_invoke.82
- ___33-[ATXModeEntityScorerClient init]_block_invoke.47
- ___50-[ATXModeEntityScorerClient scoreApps:mode:reply:]_block_invoke.65
- ___53-[ATXModeEntityScorerClient rankedAppsForMode:reply:]_block_invoke.66
- ___54-[ATXModeEntityScorerClient scoreContacts:mode:reply:]_block_invoke.62
- ___56-[ATXModeEntityScorer rankedContactsForDenyListForMode:]_block_invoke
- ___56-[ATXModeEntityScorer rankedContactsForDenyListForMode:]_block_invoke.32
- ___56-[ATXModeEntityScorer rankedContactsForDenyListForMode:]_block_invoke.32.cold.1
- ___56-[ATXModeEntityScorer rankedContactsForDenyListForMode:]_block_invoke_2
- ___56-[ATXModeEntityScorerClient rankedWidgetsForMode:reply:]_block_invoke.67
- ___57-[ATXModeEntityScorerClient rankedContactsForMode:reply:]_block_invoke.64
- ___59-[ATXInterruptionManager recommendedDeniedContactsForMode:]_block_invoke
- ___59-[ATXModeEntityScorerClient scoreNotifications:mode:reply:]_block_invoke.68
- ___61-[ATXModeEntityScorerClient scoreAppsForDenyList:mode:reply:]_block_invoke.75
- ___62-[ATXModeEntityScorer rankedContactsForDenyListForMode:reply:]_block_invoke
- ___62-[ATXModeEntityScorer rankedContactsForDenyListForMode:reply:]_block_invoke.cold.1
- ___62-[ATXModeEntityScorerClient rankedNotificationsForMode:reply:]_block_invoke.69
- ___64-[ATXModeEntityScorerClient rankedAppsForDenyListForMode:reply:]_block_invoke.76
- ___65-[ATXModeEntityScorerClient scoreContactsForDenyList:mode:reply:]_block_invoke.80
- ___68-[ATXModeEntityScorerClient rankedContactsForDenyListForMode:reply:]_block_invoke
- ___68-[ATXModeEntityScorerClient rankedContactsForDenyListForMode:reply:]_block_invoke.81
- ___68-[ATXModeEntityScorerClient rankedContactsForDenyListForMode:reply:]_block_invoke.cold.1
- ___69-[ATXModeEntityScorerClient rankedAppsForNotificationsForMode:reply:]_block_invoke.70
- ___73-[ATXModeEntityScorerClient rankedContactsForNotificationsForMode:reply:]_block_invoke.71
- ___block_literal_global.49
- _objc_msgSend$rankedContactsForDenyListForMode:reply:
CStrings:
+ "%s: in news supported country, allowing News widget"
+ "%s: in parsec editorial locale, allowing News widget"
+ "%s: no country code in locale, allowing News widget"
+ "%s: no locale identifier, allowing News widget"
+ "%s: not allowing News widget for child account"
+ "@\"NSArray\"32@0:8Q16Q24"
+ "_descriptorsByFilteringDescriptors:variant:"
+ "_imageCornerRoundingStyleForIconDisplayStyle:"
+ "_onboardingStacksByFilteringDescriptorsInOnboardingStacks:variant:"
+ "_widgetStackByFilteringDescriptorsInWidgetStack:variant:"
+ "isCHSWidgetDescriptorAllowedForAmbientOnboardingStacks:"
+ "isChild"
+ "isDescriptorSpecial:"
+ "rankedContactsForDenyListForMode:options:"
+ "rankedContactsForDenyListForMode:options:reply:"
+ "recommendedDeniedContactsForMode:options:"
+ "v40@0:8Q16Q24@?<v@?@\"NSArray\"@\"NSError\">32"
- "%s: in news supported country, allowing news widget"
- "%s: in parsec editorial locale, allowing news widget"
- "%s: no country code in locale, allowing news widget"
- "%s: no locale identifier, allowing news widget"

```
