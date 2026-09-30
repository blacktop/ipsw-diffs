## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient`

```diff

-610.0.11.0.0
-  __TEXT.__text: 0x18a5f4
+613.0.1.0.0
+  __TEXT.__text: 0x18b220
   __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_methlist: 0x1893c
+  __TEXT.__objc_methlist: 0x189ec
   __TEXT.__const: 0x6f8
-  __TEXT.__cstring: 0x1b514
-  __TEXT.__oslogstring: 0x171bd
-  __TEXT.__gcc_except_tab: 0x22d0
+  __TEXT.__cstring: 0x1b6a7
+  __TEXT.__oslogstring: 0x1728e
+  __TEXT.__gcc_except_tab: 0x22e0
   __TEXT.__dlopen_cstrs: 0x3d0
   __TEXT.__ustring: 0x18a
-  __TEXT.__unwind_info: 0x65a0
-  __TEXT.__objc_classname: 0x3bbb
-  __TEXT.__objc_methname: 0x33d9c
-  __TEXT.__objc_methtype: 0x675a
-  __TEXT.__objc_stubs: 0x1c900
+  __TEXT.__unwind_info: 0x65e0
+  __TEXT.__objc_classname: 0x3be3
+  __TEXT.__objc_methname: 0x33f8a
+  __TEXT.__objc_methtype: 0x6773
+  __TEXT.__objc_stubs: 0x1c9e0
   __DATA_CONST.__got: 0x16f0
-  __DATA_CONST.__const: 0x62d0
-  __DATA_CONST.__objc_classlist: 0xe40
+  __DATA_CONST.__const: 0x6308
+  __DATA_CONST.__objc_classlist: 0xe48
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9df8
+  __DATA_CONST.__objc_selrefs: 0x9e58
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0xc48
+  __DATA_CONST.__objc_superrefs: 0xc50
   __DATA_CONST.__objc_arraydata: 0xaf8
   __AUTH_CONST.__auth_got: 0x790
-  __AUTH_CONST.__const: 0x2a20
-  __AUTH_CONST.__cfstring: 0x14f60
-  __AUTH_CONST.__objc_const: 0x45c00
+  __AUTH_CONST.__const: 0x2a60
+  __AUTH_CONST.__cfstring: 0x150a0
+  __AUTH_CONST.__objc_const: 0x45ce0
   __AUTH_CONST.__objc_intobj: 0xa38
   __AUTH_CONST.__objc_arrayobj: 0x6d8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x168
-  __AUTH.__objc_data: 0x3d90
-  __DATA.__objc_ivar: 0x1c50
+  __AUTH.__objc_data: 0x3de0
+  __DATA.__objc_ivar: 0x1c58
   __DATA.__data: 0x1cf0
   __DATA.__bss: 0x378
   __DATA_DIRTY.__objc_data: 0x50f0

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 9E53C382-6FF2-3FBA-AB1C-21414C6838DD
-  Functions: 10616
-  Symbols:   34957
-  CStrings:  15916
+  UUID: 86CAF497-126E-3DF7-965C-3600D9BE3064
+  Functions: 10636
+  Symbols:   35015
+  CStrings:  15956
 
Symbols:
+ +[ATXDefaultHomeScreenItemManager _widgetIdentifiersNotAllowed]
+ -[ATXAction canonicalIdentifier]
+ -[ATXClient fetchLastExecutedActions]
+ -[ATXCombinedIntentStream getSortedCombinedIntentEventsForTestingActionsBetweenStartDate:endDate:]
+ -[ATXDefaultHomeScreenItemManager fetchWidgetDiscoverabilityStacksForVariant:]
+ -[ATXDefaultHomeScreenItemManager fetchWidgetDiscoverabilityStacksForVariant:].cold.1
+ -[ATXDefaultHomeScreenItemManagerTransfer .cxx_destruct]
+ -[ATXDefaultHomeScreenItemManagerTransfer _readSmartStacksWithPath:error:]
+ -[ATXDefaultHomeScreenItemManagerTransfer _writeSmartStacks:toPath:]
+ -[ATXDefaultHomeScreenItemManagerTransfer _writeSmartStacks:toPath:].cold.1
+ -[ATXDefaultHomeScreenItemManagerTransfer fetchImportedWidgetSmartStackWithRequest:completionHandler:]
+ -[ATXDefaultHomeScreenItemManagerTransfer fetchImportedWidgetSmartStackWithRequest:completionHandler:].cold.1
+ -[ATXDefaultHomeScreenItemManagerTransfer importWidgetSmartStackWithRequest:response:completionHandler:]
+ -[ATXDefaultHomeScreenItemManagerTransfer initWithPath:]
+ -[ATXDefaultHomeScreenItemManagerTransfer init]
+ -[ATXDefaultHomeScreenItemManagerTransfer stringForSmartStackVariant:]
+ -[ATXSearchFeedbackListener initWithTarget:spotlightUIBiomeStream:engagementRecordManager:actionClient:appDirectoryClient:tracker:]
+ GCC_except_table67
+ _OBJC_CLASS_$_ATXDefaultHomeScreenItemManagerTransfer
+ _OBJC_IVAR_$_ATXDefaultHomeScreenItemManagerTransfer._path
+ _OBJC_IVAR_$_ATXSearchFeedbackListener._appDirectoryClient
+ _OBJC_METACLASS_$_ATXDefaultHomeScreenItemManagerTransfer
+ __OBJC_$_INSTANCE_METHODS_ATXDefaultHomeScreenItemManagerTransfer
+ __OBJC_$_INSTANCE_VARIABLES_ATXDefaultHomeScreenItemManagerTransfer
+ __OBJC_CLASS_RO_$_ATXDefaultHomeScreenItemManagerTransfer
+ __OBJC_METACLASS_RO_$_ATXDefaultHomeScreenItemManagerTransfer
+ ___18-[ATXAction proto]_block_invoke.121
+ ___202-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedAmbientOnboardingStacksForSize:stack1RequiredWidgetPersonalities:stack2RequiredWidgetPersonalities:rankedWidgets:usedWidgetPersonalities:]_block_invoke.102
+ ___248-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedOnboardingStackForSize:requiredWidgetPersonalities:conditionalWidgetPersonalities:fallbackWidgetPersonalities:rankedThirdPartyWidgets:usedWidgetPersonalities:shouldAdd3PWidgetToStack:]_block_invoke.114
+ ___37-[ATXClient fetchLastExecutedActions]_block_invoke
+ ___37-[ATXClient fetchLastExecutedActions]_block_invoke_2
+ ___37-[ATXClient fetchLastExecutedActions]_block_invoke_2.cold.1
+ ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.377
+ ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.377.cold.1
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke_3
+ ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke_3.cold.1
+ ___98-[ATXCombinedIntentStream getSortedCombinedIntentEventsForTestingActionsBetweenStartDate:endDate:]_block_invoke
+ ___block_literal_global.111
+ ___block_literal_global.36
+ ___block_literal_global.570
+ _objc_msgSend$_readSmartStacksWithPath:error:
+ _objc_msgSend$_widgetIdentifiersNotAllowed
+ _objc_msgSend$_writeSmartStacks:toPath:
+ _objc_msgSend$fetchLastExecutedActionsWithCompletion:
+ _objc_msgSend$fetchWidgetDiscoverabilityStacksForVariant:
+ _objc_msgSend$fetchWidgetSmartStackWithRequest:completionHandler:
+ _objc_msgSend$initWithTarget:spotlightUIBiomeStream:engagementRecordManager:actionClient:appDirectoryClient:tracker:
+ _objc_msgSend$setBadgingImage:
+ _objc_msgSend$stringForSmartStackVariant:
- -[ATXDefaultHomeScreenItemManager fetchWidgetDiscoverabilityStacks].cold.1
- -[ATXSearchFeedbackListener initWithTarget:spotlightUIBiomeStream:engagementRecordManager:actionClient:tracker:]
- GCC_except_table68
- ___18-[ATXAction proto]_block_invoke.117
- ___202-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedAmbientOnboardingStacksForSize:stack1RequiredWidgetPersonalities:stack2RequiredWidgetPersonalities:rankedWidgets:usedWidgetPersonalities:]_block_invoke.99
- ___248-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedOnboardingStackForSize:requiredWidgetPersonalities:conditionalWidgetPersonalities:fallbackWidgetPersonalities:rankedThirdPartyWidgets:usedWidgetPersonalities:shouldAdd3PWidgetToStack:]_block_invoke.111
- ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.374
- ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.374.cold.1
- ___93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke_2.cold.1
- ___block_literal_global.108
- ___block_literal_global.569
- ___block_literal_global.94
- _objc_msgSend$fetchWidgetDiscoverabilityStacks
- _objc_msgSend$initWithTarget:spotlightUIBiomeStream:engagementRecordManager:actionClient:tracker:
CStrings:
+ "%s: Couldn't fetch imported smart stacks. Attempting to fetch from local device"
+ "%s: Error writing smart stack: %@"
+ "%s: returning nil stack for non-pad devices. Stack variant: ATXSmartStackVariantOnboarding"
+ "-[ATXDefaultHomeScreenItemManager fetchWidgetDiscoverabilityStacksForVariant:]"
+ "-[ATXDefaultHomeScreenItemManagerTransfer _writeSmartStacks:toPath:]"
+ "-[ATXDefaultHomeScreenItemManagerTransfer fetchImportedWidgetSmartStackWithRequest:completionHandler:]"
+ "@\"ATXAppDirectoryClient\""
+ "ATXDefaultHomeScreenItemManagerTransfer"
+ "Ambient"
+ "AmbientOnboarding"
+ "AppList"
+ "Failed to fetch last executed actions: %@"
+ "Failed to import widget smart stack"
+ "Onboarding"
+ "OnboardingTvOS"
+ "Recent"
+ "_appDirectoryClient"
+ "_readSmartStacksWithPath:error:"
+ "_widgetIdentifiersNotAllowed"
+ "_writeSmartStacks:toPath:"
+ "canonicalIdentifier"
+ "carPlayOnboardingRequiredWidgetsForDefaultStack1-only"
+ "fetchImportedWidgetSmartStackWithRequest:completionHandler:"
+ "fetchLastExecutedActions"
+ "fetchLastExecutedActionsWithCompletion:"
+ "fetchWidgetDiscoverabilityStacksForVariant:"
+ "filemenu.and.selection"
+ "getSortedCombinedIntentEventsForTestingActionsBetweenStartDate:endDate:"
+ "importWidgetSmartStackWithRequest:response:completionHandler:"
+ "initWithTarget:spotlightUIBiomeStream:engagementRecordManager:actionClient:appDirectoryClient:tracker:"
+ "setBadgingImage:"
+ "stringForSmartStackVariant:"
- "%s: returning nil for non-pad devices"
- "-[ATXDefaultHomeScreenItemManager fetchWidgetDiscoverabilityStacks]"
- "initWithTarget:spotlightUIBiomeStream:engagementRecordManager:actionClient:tracker:"

```
