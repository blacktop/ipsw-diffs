## TipsDaemon

> `/System/Library/PrivateFrameworks/TipsDaemon.framework/Versions/A/TipsDaemon`

```diff

-772.1.0.0.0
-  __TEXT.__text: 0x8690c
-  __TEXT.__auth_stubs: 0x1870
-  __TEXT.__objc_methlist: 0x30a4
-  __TEXT.__const: 0x1938
-  __TEXT.__oslogstring: 0x1ffe
-  __TEXT.__cstring: 0x39e8
-  __TEXT.__gcc_except_tab: 0x1408
+778.4.3.0.0
+  __TEXT.__text: 0x83528
+  __TEXT.__auth_stubs: 0x1830
+  __TEXT.__objc_methlist: 0x3218
+  __TEXT.__const: 0x1918
+  __TEXT.__oslogstring: 0x1e74
+  __TEXT.__cstring: 0x38a8
+  __TEXT.__gcc_except_tab: 0x13c8
   __TEXT.__dlopen_cstrs: 0x8ac
-  __TEXT.__swift5_typeref: 0xa1c
+  __TEXT.__swift5_typeref: 0xa1a
   __TEXT.__swift5_fieldmd: 0x5fc
   __TEXT.__constg_swiftt: 0x8d8
   __TEXT.__swift5_builtin: 0xb4

   __TEXT.__swift5_proto: 0x150
   __TEXT.__swift5_types: 0xac
   __TEXT.__swift5_capture: 0x434
+  __TEXT.__swift_as_entry: 0xe8
+  __TEXT.__swift_as_ret: 0x154
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x25e0
-  __TEXT.__eh_frame: 0x3384
-  __TEXT.__objc_classname: 0xf64
-  __TEXT.__objc_methname: 0x8e21
-  __TEXT.__objc_methtype: 0xb56
-  __TEXT.__objc_stubs: 0x7060
-  __DATA_CONST.__got: 0xad8
-  __DATA_CONST.__const: 0x888
-  __DATA_CONST.__objc_classlist: 0x4b0
+  __TEXT.__unwind_info: 0x2560
+  __TEXT.__eh_frame: 0x35f4
+  __TEXT.__objc_classname: 0xec0
+  __TEXT.__objc_methname: 0x878b
+  __TEXT.__objc_methtype: 0xb42
+  __TEXT.__objc_stubs: 0x6c40
+  __DATA_CONST.__got: 0xa60
+  __DATA_CONST.__const: 0x688
+  __DATA_CONST.__objc_classlist: 0x488
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2258
+  __DATA_CONST.__objc_selrefs: 0x21a0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1b8
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0xc48
-  __AUTH_CONST.__const: 0x3288
-  __AUTH_CONST.__cfstring: 0x25e0
-  __AUTH_CONST.__objc_const: 0x7f30
+  __AUTH_CONST.__auth_got: 0xc28
+  __AUTH_CONST.__const: 0x3588
+  __AUTH_CONST.__cfstring: 0x2480
+  __AUTH_CONST.__objc_const: 0x7668
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x34e0
+  __AUTH.__objc_data: 0x3318
   __AUTH.__data: 0x748
-  __DATA.__objc_ivar: 0x254
+  __DATA.__objc_ivar: 0x234
   __DATA.__data: 0xe48
   __DATA.__bss: 0x2b50
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/IDS.framework/Versions/A/IDS
   - /System/Library/PrivateFrameworks/LinkServices.framework/Versions/A/LinkServices
   - /System/Library/PrivateFrameworks/PeopleSuggester.framework/Versions/A/PeopleSuggester
-  - /System/Library/PrivateFrameworks/ReminderKit.framework/Versions/A/ReminderKit
   - /System/Library/PrivateFrameworks/SPOwner.framework/Versions/A/SPOwner
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/TipKitServices.framework/Versions/A/TipKitServices

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 33861D63-6E75-319C-99D7-27B77743D814
-  Functions: 2695
-  Symbols:   4601
-  CStrings:  2716
+  UUID: DA26CF34-1198-3BD7-BE37-5AA68E986917
+  Functions: 2690
+  Symbols:   4544
+  CStrings:  2625
 
Symbols:
+ +[TPSBluetoothChecker sharedInstance].cold.1
+ +[TPSCloudDeviceValidation idsService].cold.1
+ +[TPSCustomCapabilityValidationBuilder deviceCapabilityValidationMap].cold.1
+ +[TPSCustomCapabilityValidationBuilder watchCapabilityValidationMap].cold.1
+ +[TPSKeyboardUtilities isExtendedSuggestionSupportedForInputMode:].cold.1
+ -[TPSBluetoothChecker devicesAccessQueue].cold.1
+ -[TPSDiscoverabilityController updateDesiredOutcomeConditionForObserverIdentifiers:]
+ -[TPSTipsManager finalEligibleContentWithCollections:collectionsMap:collectionDeliveryInfoMap:eligibleTipIdentifiers:eligibleContextualTipIdentifiers:allFullTipsMap:tipDeliveryInfoMap:deliveryInfoMap:completionHandler:]
+ GCC_except_table175
+ GCC_except_table180
+ GCC_except_table197
+ GCC_except_table65
+ __189-[TPSTipsManager contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke.134
+ __189-[TPSTipsManager contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke.135
+ __189-[TPSTipsManager contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke.139
+ __189-[TPSTipsManager contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke.141
+ __189-[TPSTipsManager contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke_2.138
+ __189-[TPSTipsManager contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke_2.142
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.148
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.154
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.161
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.167
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.174
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.178
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.183
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.193
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.203
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.211
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.222
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.228
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.234
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.155
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.162
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.168
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.179
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.185
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.194
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.204
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.213
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.213.cold.1
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.224
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.224.cold.1
+ __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.229
+ __219-[TPSTipsManager finalEligibleContentWithCollections:collectionsMap:collectionDeliveryInfoMap:eligibleTipIdentifiers:eligibleContextualTipIdentifiers:allFullTipsMap:tipDeliveryInfoMap:deliveryInfoMap:completionHandler:]_block_invoke.282
+ __52-[TPSTipsManager welcomeDocumentFromContentPackage:]_block_invoke.309
+ __65-[TPSTipsManager contentForVariantIdentifiers:completionHandler:]_block_invoke.120
+ __65-[TPSTipsManager reindexAllSearchableItemsWithCompletionHandler:]_block_invoke.290
+ __65-[TPSTipsManager reindexAllSearchableItemsWithCompletionHandler:]_block_invoke.296
+ __65-[TPSTipsManager reindexAllSearchableItemsWithCompletionHandler:]_block_invoke_2.292
+ __65-[TPSTipsManager reindexAllSearchableItemsWithCompletionHandler:]_block_invoke_2.292.cold.1
+ __66-[TPSTipsManager processTipDocumentsDictionary:completionHandler:]_block_invoke.241
+ __70-[TPSDiscoverabilityController processEventProviderQueryResults:type:]_block_invoke.25
+ __75-[TPSTipsManager processClientConditions:targetingCache:completionHandler:]_block_invoke.275
+ __75-[TPSTipsManager processClientConditions:targetingCache:completionHandler:]_block_invoke.276
+ __75-[TPSTipsManager processClientConditions:targetingCache:completionHandler:]_block_invoke.276.cold.1
+ __75-[TPSTipsManager processClientConditions:targetingCache:completionHandler:]_block_invoke.277
+ __78-[TPSDiscoverabilityController _updateTriggerConditionForObserverIdentifiers:]_block_invoke.35
+ __91-[TPSTipsManager processTipsDeliveryInfo:deliveryInfoMap:targetingCache:completionHandler:]_block_invoke.254
+ __91-[TPSTipsManager processTipsDeliveryInfo:deliveryInfoMap:targetingCache:completionHandler:]_block_invoke.254.cold.1
+ __91-[TPSTipsManager processTipsDeliveryInfo:deliveryInfoMap:targetingCache:completionHandler:]_block_invoke.255
+ __91-[TPSTipsManager processTipsDeliveryInfo:deliveryInfoMap:targetingCache:completionHandler:]_block_invoke.255.cold.1
+ __91-[TPSTipsManager processTipsDeliveryInfo:deliveryInfoMap:targetingCache:completionHandler:]_block_invoke.262
+ __91-[TPSTipsManager processTipsDeliveryInfo:deliveryInfoMap:targetingCache:completionHandler:]_block_invoke.267
+ __91-[TPSTipsManager processTipsDeliveryInfo:deliveryInfoMap:targetingCache:completionHandler:]_block_invoke.270
+ __91-[TPSTipsManager processTipsDeliveryInfo:deliveryInfoMap:targetingCache:completionHandler:]_block_invoke_2.268
+ __91-[TPSTipsManager processTipsDeliveryInfo:deliveryInfoMap:targetingCache:completionHandler:]_block_invoke_2.271
+ ___219-[TPSTipsManager finalEligibleContentWithCollections:collectionsMap:collectionDeliveryInfoMap:eligibleTipIdentifiers:eligibleContextualTipIdentifiers:allFullTipsMap:tipDeliveryInfoMap:deliveryInfoMap:completionHandler:]_block_invoke
+ ___84-[TPSDiscoverabilityController updateDesiredOutcomeConditionForObserverIdentifiers:]_block_invoke
+ ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96s104r112r120r_e25_v32?0"NSString"8Q16^B24l
+ ___block_descriptor_160_e8_32s40s48s56r64r72r80r88r96r104r112r120r128r136r144r152w_e24_v16?0?<v?"NSError">8l
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e39_v32?0"NSString"8"NSDictionary"16^B24l
+ ___copy_helper_block_e8_32s40s48s56r64r72r80r88r96r104r112r120r128r136r144r152w
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104r112r120r
+ ___destroy_helper_block_e8_32s40s48s56r64r72r80r88r96r104r112r120r128r136r144r152w
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104r112r120r
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.262
+ _objc_msgSend$featuredDocumentInterval
+ _objc_msgSend$finalEligibleContentWithCollections:collectionsMap:collectionDeliveryInfoMap:eligibleTipIdentifiers:eligibleContextualTipIdentifiers:allFullTipsMap:tipDeliveryInfoMap:deliveryInfoMap:completionHandler:
+ _objc_msgSend$isHintIneligibleForIdentifier:
+ _objc_msgSend$updateDesiredOutcomeConditionForObserverIdentifiers:
+ _objc_msgSend$updateHintIneligibleForIdentifier:value:
+ _symbolic Sccy___________pG 10Foundation4DataV s5ErrorP
+ _symbolic Sccyyt______pG s5ErrorP
+ block_copy_helper.10
+ block_copy_helper.12
+ block_copy_helper.14
+ block_copy_helper.15
+ block_copy_helper.2
+ block_copy_helper.25
+ block_copy_helper.31
+ block_copy_helper.32
+ block_copy_helper.5
+ block_copy_helper.6
+ block_copy_helper.77
+ block_copy_helper.80
+ block_copy_helper.83
+ block_copy_helper.94
+ block_descriptor.14
+ block_descriptor.16
+ block_descriptor.17
+ block_descriptor.33
+ block_descriptor.34
+ block_descriptor.4
+ block_descriptor.7
+ block_descriptor.79
+ block_descriptor.8
+ block_descriptor.82
+ block_descriptor.96
+ block_destroy_helper.11
+ block_destroy_helper.13
+ block_destroy_helper.15
+ block_destroy_helper.16
+ block_destroy_helper.26
+ block_destroy_helper.3
+ block_destroy_helper.32
+ block_destroy_helper.33
+ block_destroy_helper.6
+ block_destroy_helper.7
+ block_destroy_helper.78
+ block_destroy_helper.81
+ block_destroy_helper.84
+ block_destroy_helper.95
- -[TPSContextualInfo customizationID]
- -[TPSContextualInfo displayBundleID]
- -[TPSContextualInfo displayBundleIDs]
- -[TPSContextualInfo displayMaxCount]
- -[TPSContextualInfo eligibleContext]
- -[TPSContextualInfo monitoringEvents]
- -[TPSContextualInfo setCustomizationID:]
- -[TPSContextualInfo setDisplayBundleIDs:]
- -[TPSContextualInfo setDisplayMaxCount:]
- -[TPSContextualInfo setEligibleContext:]
- -[TPSContextualInfo setMonitoringEvents:]
- -[TPSDiscoverabilityController _reconcileRegisteredEvents]
- -[TPSDiscoverabilityController _reconcileRegisteredEvents].cold.1
- -[TPSDiscoverabilityController _registerWakingCallbackForContextualInfo:]
- -[TPSDiscoverabilityController _updateRegisteredEventIdentifiers]
- -[TPSDiscoverabilityController customizationIDForContentID:]
- -[TPSDiscoverabilityController discoverabilityTipWithMetadata:contentDictionary:preconditions:]
- -[TPSDiscoverabilityController isContentHintDisplayMaxDisplayedCountExceededForIdentifier:]
- -[TPSDiscoverabilityController monitoringEventsForContentID:]
- -[TPSDiscoverabilityController updateDesiredOutcomeConditionForObserverIdentifers:]
- -[TPSDiscoverabilityController updateHintDismissedForIdentifier:dismissType:context:]
- -[TPSDiscoverabilityController updateHintDismissedForIdentifier:dismissType:context:].cold.1
- -[TPSReminderCloudKitValidation validateWithCompletion:]
- -[TPSReminderCloudKitValidation validateWithCompletion:].cold.1
- -[TPSReminderCompletedItemValidation validateWithCompletion:]
- -[TPSReminderCompletedItemValidation validateWithCompletion:].cold.1
- -[TPSReminderCustomBadgeValidation validateWithCompletion:]
- -[TPSReminderCustomBadgeValidation validateWithCompletion:].cold.1
- -[TPSReminderCustomSmartListValidation validateWithCompletion:]
- -[TPSReminderCustomSmartListValidation validateWithCompletion:].cold.1
- -[TPSReminderHashtagValidation validateWithCompletion:]
- -[TPSReminderHashtagValidation validateWithCompletion:].cold.1
- -[TPSTipsManager finalEligibleContentWithCollections:collectionsMap:collectionDeliveryInfoMap:eligibleTipIdentifiers:eligibleContextualTipIdentifiers:allFullTipsMap:allMiniTipsMap:tipDeliveryInfoMap:deliveryInfoMap:completionHandler:]
- GCC_except_table10
- GCC_except_table178
- GCC_except_table183
- GCC_except_table200
- GCC_except_table49
- GCC_except_table75
- OBJC_IVAR_$_TPSContextualInfo._customizationID
- OBJC_IVAR_$_TPSContextualInfo._displayBundleIDs
- OBJC_IVAR_$_TPSContextualInfo._displayMaxCount
- OBJC_IVAR_$_TPSContextualInfo._eligibleContext
- OBJC_IVAR_$_TPSContextualInfo._monitoringEvents
- OBJC_IVAR_$_TPSDiscoverabilityController._eventRegistrationQueue
- OBJC_IVAR_$_TPSDiscoverabilityController._overrideHintMaxDisplayedCount
- OBJC_IVAR_$_TPSDiscoverabilityController._registeredEventIdentifiers
- _OBJC_CLASS_$_REMStore
- _OBJC_CLASS_$_TPSAnalyticsEventContentEligibilityMet
- _OBJC_CLASS_$_TPSAnalyticsEventTipDismissed
- _OBJC_CLASS_$_TPSDiscoverabilityTip
- _OBJC_CLASS_$_TPSMonitoringEvents
- _OBJC_CLASS_$_TPSReminderCloudKitValidation
- _OBJC_CLASS_$_TPSReminderCompletedItemValidation
- _OBJC_CLASS_$_TPSReminderCustomBadgeValidation
- _OBJC_CLASS_$_TPSReminderCustomSmartListValidation
- _OBJC_CLASS_$_TPSReminderHashtagValidation
- _OBJC_CLASS_$_TPSTipStatus
- _OBJC_METACLASS_$_TPSReminderCloudKitValidation
- _OBJC_METACLASS_$_TPSReminderCompletedItemValidation
- _OBJC_METACLASS_$_TPSReminderCustomBadgeValidation
- _OBJC_METACLASS_$_TPSReminderCustomSmartListValidation
- _OBJC_METACLASS_$_TPSReminderHashtagValidation
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _TPSAnalyticsDismissTypeHintMaxDurationExceeded
- _TPSDocumentDeliveryInfoKey
- _TPSMonitoringEventsKey
- __189-[TPSTipsManager contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke.138
- __189-[TPSTipsManager contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke.142
- __189-[TPSTipsManager contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke.143
- __189-[TPSTipsManager contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke.144
- __189-[TPSTipsManager contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke_2.141
- __189-[TPSTipsManager contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:]_block_invoke_2.145
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.151
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.157
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.164
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.170
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.177
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.181
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.186
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.196
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.206
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.214
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.225
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.231
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke.237
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.158
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.165
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.171
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.182
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.188
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.197
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.207
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.216
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.216.cold.1
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.227
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.227.cold.1
- __199-[TPSTipsManager contentWithMetaDictionary:documents:isRemote:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:completionHandler:]_block_invoke_2.232
- __234-[TPSTipsManager finalEligibleContentWithCollections:collectionsMap:collectionDeliveryInfoMap:eligibleTipIdentifiers:eligibleContextualTipIdentifiers:allFullTipsMap:allMiniTipsMap:tipDeliveryInfoMap:deliveryInfoMap:completionHandler:]_block_invoke.286
- __234-[TPSTipsManager finalEligibleContentWithCollections:collectionsMap:collectionDeliveryInfoMap:eligibleTipIdentifiers:eligibleContextualTipIdentifiers:allFullTipsMap:allMiniTipsMap:tipDeliveryInfoMap:deliveryInfoMap:completionHandler:]_block_invoke.287
- __52-[TPSTipsManager welcomeDocumentFromContentPackage:]_block_invoke.314
- __57-[TPSDiscoverabilityController _cleanupContextualInfoMap]_block_invoke.cold.3
- __57-[TPSDiscoverabilityController _cleanupContextualInfoMap]_block_invoke.cold.4
- __65-[TPSTipsManager contentForVariantIdentifiers:completionHandler:]_block_invoke.125
- __65-[TPSTipsManager reindexAllSearchableItemsWithCompletionHandler:]_block_invoke.295
- __65-[TPSTipsManager reindexAllSearchableItemsWithCompletionHandler:]_block_invoke.306
- __65-[TPSTipsManager reindexAllSearchableItemsWithCompletionHandler:]_block_invoke_2.302
- __65-[TPSTipsManager reindexAllSearchableItemsWithCompletionHandler:]_block_invoke_2.302.cold.1
- __66-[TPSTipsManager processTipDocumentsDictionary:completionHandler:]_block_invoke.245
- __70-[TPSDiscoverabilityController processEventProviderQueryResults:type:]_block_invoke.31
- __75-[TPSTipsManager processClientConditions:targetingCache:completionHandler:]_block_invoke.279
- __75-[TPSTipsManager processClientConditions:targetingCache:completionHandler:]_block_invoke.280
- __75-[TPSTipsManager processClientConditions:targetingCache:completionHandler:]_block_invoke.280.cold.1
- __75-[TPSTipsManager processClientConditions:targetingCache:completionHandler:]_block_invoke.281
- __78-[TPSDiscoverabilityController _updateTriggerConditionForObserverIdentifiers:]_block_invoke.42
- __91-[TPSTipsManager processTipsDeliveryInfo:deliveryInfoMap:targetingCache:completionHandler:]_block_invoke.258
- __91-[TPSTipsManager processTipsDeliveryInfo:deliveryInfoMap:targetingCache:completionHandler:]_block_invoke.258.cold.1
- __91-[TPSTipsManager processTipsDeliveryInfo:deliveryInfoMap:targetingCache:completionHandler:]_block_invoke.259
- __91-[TPSTipsManager processTipsDeliveryInfo:deliveryInfoMap:targetingCache:completionHandler:]_block_invoke.259.cold.1
- __91-[TPSTipsManager processTipsDeliveryInfo:deliveryInfoMap:targetingCache:completionHandler:]_block_invoke.266
- __91-[TPSTipsManager processTipsDeliveryInfo:deliveryInfoMap:targetingCache:completionHandler:]_block_invoke.271
- __91-[TPSTipsManager processTipsDeliveryInfo:deliveryInfoMap:targetingCache:completionHandler:]_block_invoke.274
- __91-[TPSTipsManager processTipsDeliveryInfo:deliveryInfoMap:targetingCache:completionHandler:]_block_invoke_2.272
- __91-[TPSTipsManager processTipsDeliveryInfo:deliveryInfoMap:targetingCache:completionHandler:]_block_invoke_2.275
- __OBJC_$_INSTANCE_METHODS_TPSReminderCloudKitValidation
- __OBJC_$_INSTANCE_METHODS_TPSReminderCompletedItemValidation
- __OBJC_$_INSTANCE_METHODS_TPSReminderCustomBadgeValidation
- __OBJC_$_INSTANCE_METHODS_TPSReminderCustomSmartListValidation
- __OBJC_$_INSTANCE_METHODS_TPSReminderHashtagValidation
- __OBJC_CLASS_RO_$_TPSReminderCloudKitValidation
- __OBJC_CLASS_RO_$_TPSReminderCompletedItemValidation
- __OBJC_CLASS_RO_$_TPSReminderCustomBadgeValidation
- __OBJC_CLASS_RO_$_TPSReminderCustomSmartListValidation
- __OBJC_CLASS_RO_$_TPSReminderHashtagValidation
- __OBJC_METACLASS_RO_$_TPSReminderCloudKitValidation
- __OBJC_METACLASS_RO_$_TPSReminderCompletedItemValidation
- __OBJC_METACLASS_RO_$_TPSReminderCustomBadgeValidation
- __OBJC_METACLASS_RO_$_TPSReminderCustomSmartListValidation
- __OBJC_METACLASS_RO_$_TPSReminderHashtagValidation
- ___234-[TPSTipsManager finalEligibleContentWithCollections:collectionsMap:collectionDeliveryInfoMap:eligibleTipIdentifiers:eligibleContextualTipIdentifiers:allFullTipsMap:allMiniTipsMap:tipDeliveryInfoMap:deliveryInfoMap:completionHandler:]_block_invoke
- ___73-[TPSDiscoverabilityController _registerWakingCallbackForContextualInfo:]_block_invoke
- ___73-[TPSDiscoverabilityController _registerWakingCallbackForContextualInfo:]_block_invoke_2
- ___83-[TPSDiscoverabilityController updateDesiredOutcomeConditionForObserverIdentifers:]_block_invoke
- ___86-[TPSDiscoverabilityController dataProviderManager:didReceiveCallbackWithResult:type:]_block_invoke_2
- ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96s104s112r120r128r_e25_v32?0"NSString"8Q16^B24l
- ___block_descriptor_168_e8_32s40s48s56r64r72r80r88r96r104r112r120r128r136r144r152r160w_e24_v16?0?<v?"NSError">8l
- ___block_descriptor_32_e28_B16?0"TPSContextualEvent"8l
- ___block_descriptor_64_e8_32s40s48s56s_e39_v32?0"NSString"8"NSDictionary"16^B24l
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e39_v32?0"NSString"8"NSDictionary"16^B24l
- ___copy_helper_block_e8_32s40s48s56r64r72r80r88r96r104r112r120r128r136r144r152r160w
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112r120r128r
- ___destroy_helper_block_e8_32s40s48s56r64r72r80r88r96r104r112r120r128r136r144r152r160w
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112r120r128r
- __block_literal_global.282
- __block_literal_global.48
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_TipsDaemon
- _kTPSCapabilityReminderCloudKit
- _kTPSCapabilityReminderCompletedItems
- _kTPSCapabilityReminderCustomBadge
- _kTPSCapabilityReminderCustomSmartList
- _kTPSCapabilityReminderHashtag
- _kTipsAnalyticsDisplayTypeMiniHintString
- _objc_msgSend$_reconcileRegisteredEvents
- _objc_msgSend$_registerWakingCallbackForContextualInfo:
- _objc_msgSend$_updateRegisteredEventIdentifiers
- _objc_msgSend$completedRemindersCountForTipKitWithError:
- _objc_msgSend$containsCustomSmartListForTipKitWithError:
- _objc_msgSend$containsHashtagsForTipKitWithError:
- _objc_msgSend$containsListWithCustomBadgeForTipKitWithError:
- _objc_msgSend$customizationID
- _objc_msgSend$desiredOutcomeEventMap
- _objc_msgSend$discoverabilityOverrideMaxDisplayCount
- _objc_msgSend$discoverabilitySuppressionInterval
- _objc_msgSend$displayBundleID
- _objc_msgSend$displayBundleIDs
- _objc_msgSend$displayMaxCount
- _objc_msgSend$eligibleContext
- _objc_msgSend$eventWithContentID:bundleID:eligibleContext:displayType:usageFlags:date:
- _objc_msgSend$eventWithTipID:correlationID:bundleID:context:dismissType:timeToDismissal:date:
- _objc_msgSend$finalEligibleContentWithCollections:collectionsMap:collectionDeliveryInfoMap:eligibleTipIdentifiers:eligibleContextualTipIdentifiers:allFullTipsMap:allMiniTipsMap:tipDeliveryInfoMap:deliveryInfoMap:completionHandler:
- _objc_msgSend$firstHintDisplayDateForIdentifier:
- _objc_msgSend$hasActiveCloudKitAccountForTipKitWithError:
- _objc_msgSend$hintDisplayedCountForIdentifier:
- _objc_msgSend$initWithDictionary:desiredOutcomeDictionary:
- _objc_msgSend$isEligibilityTrackingNeedsRestartForIdentifier:
- _objc_msgSend$isHintInelgibileForIdentifier:
- _objc_msgSend$isHintMaxDurationExcceededForIdentifier:
- _objc_msgSend$monitoringEvents
- _objc_msgSend$setCustomizationID:
- _objc_msgSend$setDisplayBundleIDs:
- _objc_msgSend$setDisplayMaxCount:
- _objc_msgSend$setEligibleContext:
- _objc_msgSend$setMonitoringEvents:
- _objc_msgSend$setPreconditions:
- _objc_msgSend$subarrayWithRange:
- _objc_msgSend$timeIntervalSinceDate:
- _objc_msgSend$updateDesiredOutcomeConditionForObserverIdentifers:
- _objc_msgSend$updateHintDismissedForIdentifier:dismissType:context:
- _objc_msgSend$updateHintDismissedForIdentifier:value:
- _objc_msgSend$updateHintInelgibileForIdentifier:value:
- _objc_sync_enter
- _objc_sync_exit
- _symbolic SDySSSiG
- _symbolic _____ySSSiG s18_DictionaryStorageC
- _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
- block_descriptor.11
- block_descriptor.2
- block_descriptor.22
- block_descriptor.23
- block_descriptor.24
- block_descriptor.25
- block_descriptor.26
- block_descriptor.29
- block_descriptor.5
CStrings:
+ "$"
+ "A"
+ "countDisplayedOnLockScreen: %ld"
+ "featuredDocumentInterval"
+ "finalEligibleContentWithCollections:collectionsMap:collectionDeliveryInfoMap:eligibleTipIdentifiers:eligibleContextualTipIdentifiers:allFullTipsMap:tipDeliveryInfoMap:deliveryInfoMap:completionHandler:"
+ "isHintIneligibleForIdentifier:"
+ "updateDesiredOutcomeConditionForObserverIdentifiers:"
+ "updateHintIneligibleForIdentifier:value:"
+ "v88@0:8@16@24@32@40@48@56@64@72@?80"
- "@\"NSMutableSet\""
- "@\"TPSMonitoringEvents\""
- "AirPodsMax"
- "B16@?0@\"TPSContextualEvent\"8"
- "Content %@ became invalid due eligibility expired"
- "Content %@ became invalid due to max duration exceeded"
- "First display date not found on hint dismissal for identifier %@"
- "First hint display date (%f) is later than dismissal date (%f) for identifier %@. Clock went back in time?"
- "G"
- "Re-registering notification for duet events: %@"
- "RegisteredDeliveryEventIdentifiers"
- "ReminderCloudKit"
- "ReminderCompletedItems"
- "ReminderCustomSmartList"
- "ReminderHashtags"
- "ReminderListWithCustomBadge"
- "T@\"NSArray\",C,N,V_displayBundleIDs"
- "T@\"NSArray\",C,N,V_eligibleContext"
- "T@\"TPSMonitoringEvents\",C,N,V_monitoringEvents"
- "TPSReminderCloudKitValidation"
- "TPSReminderCompletedItemValidation"
- "TPSReminderCustomBadgeValidation"
- "TPSReminderCustomSmartListValidation"
- "TPSReminderHashtagValidation"
- "Tq,N,V_customizationID"
- "Tq,N,V_displayMaxCount"
- "_customizationID"
- "_displayBundleIDs"
- "_displayMaxCount"
- "_eligibleContext"
- "_eventRegistrationQueue"
- "_monitoringEvents"
- "_overrideHintMaxDisplayedCount"
- "_reconcileRegisteredEvents"
- "_registerWakingCallbackForContextualInfo:"
- "_registeredEventIdentifiers"
- "_updateRegisteredEventIdentifiers"
- "com.apple.tipsd.eventRegistrationQueue"
- "completedRemindersCountForTipKitWithError:"
- "containsCustomSmartListForTipKitWithError:"
- "containsHashtagsForTipKitWithError:"
- "containsListWithCustomBadgeForTipKitWithError:"
- "correlationIdentifier"
- "countDisplayedEmbeeded: %ld countDisplayedOnLockScreen: %ld"
- "customizationID"
- "customizationIDForContentID:"
- "customizationId"
- "desiredOutcomeEventMap"
- "discoverabilityOverrideMaxDisplayCount"
- "discoverabilitySuppressionInterval"
- "discoverabilityTipWithMetadata:contentDictionary:preconditions:"
- "displayBundleID"
- "displayBundleIDs"
- "displayMaxCount"
- "eligibleContext"
- "eligibleContexts"
- "eventWithContentID:bundleID:eligibleContext:displayType:usageFlags:date:"
- "eventWithTipID:correlationID:bundleID:context:dismissType:timeToDismissal:date:"
- "finalEligibleContentWithCollections:collectionsMap:collectionDeliveryInfoMap:eligibleTipIdentifiers:eligibleContextualTipIdentifiers:allFullTipsMap:allMiniTipsMap:tipDeliveryInfoMap:deliveryInfoMap:completionHandler:"
- "firstHintDisplayDateForIdentifier:"
- "hasActiveCloudKitAccountForTipKitWithError:"
- "hintDisplayedCountForIdentifier:"
- "hintIneligibleReason"
- "initWithDictionary:desiredOutcomeDictionary:"
- "isContentHintDisplayMaxDisplayedCountExceededForIdentifier:"
- "isEligibilityTrackingNeedsRestartForIdentifier:"
- "isHintInelgibile"
- "isHintInelgibileForIdentifier:"
- "isHintMaxDurationExcceededForIdentifier:"
- "lastTipDisplayed"
- "monitoringEvents"
- "monitoringEventsForContentID:"
- "setCustomizationID:"
- "setDisplayBundleIDs:"
- "setDisplayMaxCount:"
- "setEligibleContext:"
- "setMonitoringEvents:"
- "setPreconditions:"
- "subarrayWithRange:"
- "timeIntervalSinceDate:"
- "update hint dismissed for %@, context %@"
- "updateDesiredOutcomeConditionForObserverIdentifers:"
- "updateHintDismissedForIdentifier:dismissType:context:"
- "updateHintDismissedForIdentifier:value:"
- "updateHintInelgibileForIdentifier:value:"

```
