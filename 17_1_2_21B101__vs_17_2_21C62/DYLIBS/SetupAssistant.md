## SetupAssistant

> `/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant`

```diff

-5063.5.0.0.0
-  __TEXT.__text: 0x38344
-  __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0x2c88
+5071.0.0.0.0
+  __TEXT.__text: 0x39b0c
+  __TEXT.__auth_stubs: 0xbf0
+  __TEXT.__objc_methlist: 0x2d98
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0xa40
-  __TEXT.__oslogstring: 0x4887
-  __TEXT.__cstring: 0x254d
-  __TEXT.__dlopen_cstrs: 0x114b
-  __TEXT.__unwind_info: 0xef4
-  __TEXT.__objc_classname: 0x70e
-  __TEXT.__objc_methname: 0x8d27
-  __TEXT.__objc_methtype: 0xfe4
-  __TEXT.__objc_stubs: 0x6bc0
+  __TEXT.__gcc_except_tab: 0xa7c
+  __TEXT.__oslogstring: 0x4a8f
+  __TEXT.__cstring: 0x25c4
+  __TEXT.__dlopen_cstrs: 0x11a1
+  __TEXT.__unwind_info: 0xf38
+  __TEXT.__objc_classname: 0x720
+  __TEXT.__objc_methname: 0x929f
+  __TEXT.__objc_methtype: 0x104d
+  __TEXT.__objc_stubs: 0x6f40
   __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x1570
-  __DATA_CONST.__objc_classlist: 0x190
+  __DATA_CONST.__const: 0x15b0
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4450
-  __DATA_CONST.__objc_selrefs: 0x2298
+  __DATA_CONST.__objc_const: 0x45b8
+  __DATA_CONST.__objc_selrefs: 0x2390
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__objc_const: 0x1700
-  __AUTH_CONST.__cfstring: 0x2960
+  __AUTH_CONST.__objc_const: 0x1748
+  __AUTH_CONST.__cfstring: 0x2a00
   __AUTH_CONST.__const: 0x9a0
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x600
-  __AUTH.__objc_data: 0x140
+  __AUTH_CONST.__auth_got: 0x608
+  __AUTH.__objc_data: 0x190
   __DATA.__objc_protorefs: 0x60
-  __DATA.__objc_classrefs: 0x2a8
+  __DATA.__objc_classrefs: 0x2c0
   __DATA.__objc_superrefs: 0x110
-  __DATA.__objc_ivar: 0x318
+  __DATA.__objc_ivar: 0x330
   __DATA.__data: 0x950
-  __DATA.__bss: 0x498
+  __DATA.__bss: 0x4a8
   __DATA_DIRTY.__objc_data: 0xe60
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DDF15089-ADE6-3213-8467-9A59EF4B666C
-  Functions: 1464
-  Symbols:   5316
-  CStrings:  2915
+  UUID: 1431E602-BF2D-31FF-8492-61AD3D94A7AA
+  Functions: 1511
+  Symbols:   5457
+  CStrings:  2988
 
Symbols:
+ -[BYAnalyticsEventAppearance _analyticsManagerDidProduceLazyEvents]
+ -[BYAnalyticsEventAppearance _biomeEvent]
+ -[BYAnalyticsEventAppearance _eventPayloadFromPreferencesIfComplete]
+ -[BYAnalyticsEventAppearance _eventPayloadFromPreferencesIfComplete].cold.1
+ -[BYAnalyticsEventAppearance setChildAge:]
+ -[BYAnalyticsEventAppearance setChildAge:].cold.1
+ -[BYAnalyticsEventAppearance setShouldRemoveAnalyticsEventPayloadFromPreferences:]
+ -[BYAnalyticsEventAppearance shouldRemoveAnalyticsEventPayloadFromPreferences]
+ -[BYAnalyticsManager _sendAppearanceSetupEventWithData:dataVersion:]
+ -[BYAnalyticsManager _sendAppearanceSetupEventWithData:dataVersion:].cold.1
+ -[BYAnalyticsManager _sendAppearanceSetupEventWithData:dataVersion:].cold.2
+ -[BYAnalyticsManager _sendChildMultitaskingSetupEventWithData:dataVersion:]
+ -[BYAnalyticsManager _sendChildMultitaskingSetupEventWithData:dataVersion:].cold.1
+ -[BYAnalyticsManager _sendChildMultitaskingSetupEventWithData:dataVersion:].cold.2
+ -[BYAnalyticsManager _stashablePayloadForBiomeEvent:]
+ -[BYAnalyticsManager addDidProduceLazyEventsBlock:]
+ -[BYAnalyticsManager appearanceSetupEventBlock]
+ -[BYAnalyticsManager appearanceSetupEvent]
+ -[BYAnalyticsManager childMultitaskingSetupEventBlock]
+ -[BYAnalyticsManager childMultitaskingSetupEvent]
+ -[BYAnalyticsManager commit].cold.1
+ -[BYAnalyticsManager commit].cold.2
+ -[BYAnalyticsManager didProduceLazyEventsBlocks]
+ -[BYAnalyticsManager sendStashedEventWithName:payload:]
+ -[BYAnalyticsManager sendStashedEventWithName:payload:].cold.1
+ -[BYAnalyticsManager sendStashedEventWithName:payload:].cold.2
+ -[BYAnalyticsManager sendStashedEventWithName:payload:].cold.3
+ -[BYAnalyticsManager setAppearanceSetupEvent:]
+ -[BYAnalyticsManager setAppearanceSetupEventBlock:]
+ -[BYAnalyticsManager setChildMultitaskingSetupEvent:]
+ -[BYAnalyticsManager setChildMultitaskingSetupEventBlock:]
+ -[BYAnalyticsManager setDidProduceLazyEventsBlocks:]
+ -[BYAnalyticsManager stash:].cold.1
+ -[BYAnalyticsManager stash:].cold.2
+ -[BYFindMyManager isFindMyEnabled]
+ _BiomeLibrary
+ _OBJC_CLASS_$_BMSystemSettingsAppearanceSetup
+ _OBJC_CLASS_$_BMSystemSettingsChildMultitaskingSetup
+ _OBJC_CLASS_$_BYFindMyManager
+ _OBJC_IVAR_$_BYAnalyticsEventAppearance._shouldRemoveAnalyticsEventPayloadFromPreferences
+ _OBJC_IVAR_$_BYAnalyticsManager._appearanceSetupEvent
+ _OBJC_IVAR_$_BYAnalyticsManager._appearanceSetupEventBlock
+ _OBJC_IVAR_$_BYAnalyticsManager._childMultitaskingSetupEvent
+ _OBJC_IVAR_$_BYAnalyticsManager._childMultitaskingSetupEventBlock
+ _OBJC_IVAR_$_BYAnalyticsManager._didProduceLazyEventsBlocks
+ _OBJC_METACLASS_$_BYFindMyManager
+ _OUTLINED_FUNCTION_4
+ __OBJC_$_INSTANCE_METHODS_BYFindMyManager
+ __OBJC_CLASS_RO_$_BYFindMyManager
+ __OBJC_METACLASS_RO_$_BYFindMyManager
+ ___34-[BYFindMyManager isFindMyEnabled]_block_invoke
+ ___34-[BYFindMyManager isFindMyEnabled]_block_invoke.cold.1
+ ___34-[BYFindMyManager isFindMyEnabled]_block_invoke.cold.2
+ ___90-[BYAnalyticsEventAppearance initWithAnalyticsManager:buddyPreferencesExcludedFromBackup:]_block_invoke_2
+ ___90-[BYAnalyticsEventAppearance initWithAnalyticsManager:buddyPreferencesExcludedFromBackup:]_block_invoke_3
+ ___block_descriptor_40_e8_32s_e38_"BMSystemSettingsAppearanceSetup"8?0ls32l8
+ _objc_msgSend$AppearanceSetup
+ _objc_msgSend$ChildMultitaskingSetup
+ _objc_msgSend$SystemSettings
+ _objc_msgSend$_analyticsManagerDidProduceLazyEvents
+ _objc_msgSend$_biomeEvent
+ _objc_msgSend$_eventPayloadFromPreferencesIfComplete
+ _objc_msgSend$_sendAppearanceSetupEventWithData:dataVersion:
+ _objc_msgSend$_sendChildMultitaskingSetupEventWithData:dataVersion:
+ _objc_msgSend$_stashablePayloadForBiomeEvent:
+ _objc_msgSend$addDidProduceLazyEventsBlock:
+ _objc_msgSend$appearanceSetupEvent
+ _objc_msgSend$appearanceSetupEventBlock
+ _objc_msgSend$childMultitaskingSetupEvent
+ _objc_msgSend$childMultitaskingSetupEventBlock
+ _objc_msgSend$dataVersion
+ _objc_msgSend$didProduceLazyEventsBlocks
+ _objc_msgSend$eventWithData:dataVersion:
+ _objc_msgSend$initWithChoice:childSetup:childChoice:childAge:
+ _objc_msgSend$sendEvent:
+ _objc_msgSend$sendStashedEventWithName:payload:
+ _objc_msgSend$serialize
+ _objc_msgSend$setAppearanceSetupEvent:
+ _objc_msgSend$setAppearanceSetupEventBlock:
+ _objc_msgSend$setChildMultitaskingSetupEvent:
+ _objc_msgSend$setChildMultitaskingSetupEventBlock:
+ _objc_msgSend$setShouldRemoveAnalyticsEventPayloadFromPreferences:
+ _objc_msgSend$shouldRemoveAnalyticsEventPayloadFromPreferences
+ _objc_msgSend$unsignedIntValue
- -[BYAnalyticsEventAppearance _eventPayload].cold.1
CStrings:
+ "\a"
+ "@\"BMSystemSettingsAppearanceSetup\""
+ "@\"BMSystemSettingsAppearanceSetup\"8@?0"
+ "@\"BMSystemSettingsChildMultitaskingSetup\""
+ "AppearanceSetup"
+ "B32@0:8@16@24"
+ "BYFindMyManager"
+ "ChildMultitaskingSetup"
+ "Did fetch Find My state %lu"
+ "Did finish waiting for Find My state."
+ "Failed to create appearance setup event"
+ "Failed to create child multitasking setup event"
+ "Failed to create payload for appearance setup event"
+ "Failed to create payload for child multitasking setup event"
+ "Failed to fetch Find My state: %{public}@"
+ "Missing data for event name %{public}@"
+ "Missing data version for event name %{public}@"
+ "Sending appearance setup event"
+ "Sending child multitasking setup event"
+ "SystemSettings"
+ "T@\"BMSystemSettingsAppearanceSetup\",&,N,V_appearanceSetupEvent"
+ "T@\"BMSystemSettingsChildMultitaskingSetup\",&,N,V_childMultitaskingSetupEvent"
+ "T@\"NSMutableArray\",&,N,V_didProduceLazyEventsBlocks"
+ "T@?,C,N,V_appearanceSetupEventBlock"
+ "T@?,C,N,V_childMultitaskingSetupEventBlock"
+ "TB,V_shouldRemoveAnalyticsEventPayloadFromPreferences"
+ "Unknown event name %{public}@"
+ "Will fetch Find My state."
+ "_analyticsManagerDidProduceLazyEvents"
+ "_appearanceSetupEvent"
+ "_appearanceSetupEventBlock"
+ "_biomeEvent"
+ "_childMultitaskingSetupEvent"
+ "_childMultitaskingSetupEventBlock"
+ "_didProduceLazyEventsBlocks"
+ "_eventPayloadFromPreferencesIfComplete"
+ "_sendAppearanceSetupEventWithData:dataVersion:"
+ "_sendChildMultitaskingSetupEventWithData:dataVersion:"
+ "_shouldRemoveAnalyticsEventPayloadFromPreferences"
+ "_stashablePayloadForBiomeEvent:"
+ "addDidProduceLazyEventsBlock:"
+ "appearanceSetupEvent"
+ "appearanceSetupEventBlock"
+ "biome."
+ "biome.appearanceSetup"
+ "biome.childMultitaskingSetup"
+ "childMultitaskingSetupEvent"
+ "childMultitaskingSetupEventBlock"
+ "child_age"
+ "dataVersion"
+ "didProduceLazyEventsBlocks"
+ "eventWithData:dataVersion:"
+ "initWithChoice:childSetup:childChoice:childAge:"
+ "isFindMyEnabled"
+ "sendEvent:"
+ "sendStashedEventWithName:payload:"
+ "serialize"
+ "setAppearanceSetupEvent:"
+ "setAppearanceSetupEventBlock:"
+ "setChildAge:"
+ "setChildMultitaskingSetupEvent:"
+ "setChildMultitaskingSetupEventBlock:"
+ "setDidProduceLazyEventsBlocks:"
+ "setShouldRemoveAnalyticsEventPayloadFromPreferences:"
+ "shouldRemoveAnalyticsEventPayloadFromPreferences"
+ "unsignedIntValue"
+ "v28@0:8@16I24"

```
