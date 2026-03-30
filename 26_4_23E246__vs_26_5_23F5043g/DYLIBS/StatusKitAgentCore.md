## StatusKitAgentCore

> `/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore`

```diff

-116.500.152.0.0
-  __TEXT.__text: 0x1859d0
+116.600.1.0.0
+  __TEXT.__text: 0x185d0c
   __TEXT.__auth_stubs: 0x2190
-  __TEXT.__objc_methlist: 0xa19c
+  __TEXT.__objc_methlist: 0xa1bc
   __TEXT.__const: 0x4248
-  __TEXT.__cstring: 0x663d
-  __TEXT.__oslogstring: 0x164a6
-  __TEXT.__gcc_except_tab: 0x1430
+  __TEXT.__cstring: 0x666d
+  __TEXT.__oslogstring: 0x164d6
+  __TEXT.__gcc_except_tab: 0x1438
   __TEXT.__constg_swiftt: 0xd98
   __TEXT.__swift5_typeref: 0x2136
   __TEXT.__swift5_reflstr: 0xe87

   __TEXT.__unwind_info: 0x58e8
   __TEXT.__eh_frame: 0x8a60
   __TEXT.__objc_classname: 0x15fb
-  __TEXT.__objc_methname: 0x16a51
+  __TEXT.__objc_methname: 0x16aa1
   __TEXT.__objc_methtype: 0x6b65
-  __TEXT.__objc_stubs: 0xc360
+  __TEXT.__objc_stubs: 0xc380
   __DATA_CONST.__got: 0xad8
   __DATA_CONST.__const: 0x2380
   __DATA_CONST.__objc_classlist: 0x450
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f30
+  __DATA_CONST.__objc_selrefs: 0x3f38
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x2b8
   __AUTH_CONST.__auth_got: 0x10d8
   __AUTH_CONST.__const: 0x5138
-  __AUTH_CONST.__cfstring: 0x2c00
-  __AUTH_CONST.__objc_const: 0xf360
+  __AUTH_CONST.__cfstring: 0x2c20
+  __AUTH_CONST.__objc_const: 0xf368
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH.__objc_data: 0x1428
   __AUTH.__data: 0x230
   __DATA.__objc_ivar: 0x780
-  __DATA.__data: 0x1c70
+  __DATA.__data: 0x1c80
   __DATA.__bss: 0x3730
-  __DATA.__common: 0x10
+  __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x24a8
   __DATA_DIRTY.__data: 0xdf8
   __DATA_DIRTY.__bss: 0xb70

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D26B2454-F21E-3891-A88F-7CD32A2F6561
-  Functions: 6756
-  Symbols:   21748
-  CStrings:  5987
+  UUID: 2ED66C75-FDF0-34DF-AC9E-B0DA19B00272
+  Functions: 6757
+  Symbols:   21753
+  CStrings:  5991
 
Symbols:
+ -[SKAServerBag forceSharedOwnershipAuthForPresence]
+ GCC_except_table125
+ GCC_except_table128
+ GCC_except_table131
+ GCC_except_table209
+ GCC_except_table244
+ _$s18StatusKitAgentCore18SKAPresenceProfileC12featureFlags33_89FD40E2ED6DFFE699C0A34BEE1FDC54LLSo22SKFeatureFlagProviding_s8SendablepvpZ
+ _$s18StatusKitAgentCore18SKAPresenceProfileC9serverBagSo09SKAServerH9Providing_s8SendablepvpZ
+ _$s18StatusKitAgentCore18SKAPresenceProfileC9serverBag_WZ
+ _$s18StatusKitAgentCore18SKAPresenceProfileC9serverBag_Wz
+ ___101-[SKAPresenceManager findPresenceChannelForPresenceIdentifier:isPersonal:databaseContext:completion:]_block_invoke.109
+ ___101-[SKAPresenceManager findPresenceChannelForPresenceIdentifier:isPersonal:databaseContext:completion:]_block_invoke.109.cold.1
+ ___101-[SKAPresenceManager setPersistentPayloadForPresenceIdentifier:onChannel:payload:options:completion:]_block_invoke.111
+ ___101-[SKAPresenceManager setPersistentPayloadForPresenceIdentifier:onChannel:payload:options:completion:]_block_invoke.111.cold.1
+ ___103-[SKAPresenceManager releaseTransientPresenceAssertionForPresenceIdentifier:options:client:completion:]_block_invoke.87
+ ___106-[SKAPresenceManager findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.108
+ ___107-[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.143
+ ___107-[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.143.cold.1
+ ___114-[SKAPresenceManager createPresenceChannelForPresenceIdentifier:options:shouldPersist:databaseContext:completion:]_block_invoke.110
+ ___114-[SKAPresenceManager createPresenceChannelForPresenceIdentifier:options:shouldPersist:databaseContext:completion:]_block_invoke.110.cold.1
+ ___115-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:shouldPersist:databaseContext:completion:]_block_invoke.144
+ ___115-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:shouldPersist:databaseContext:completion:]_block_invoke.144.cold.1
+ ___115-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:shouldPersist:databaseContext:completion:]_block_invoke.145
+ ___115-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:shouldPersist:databaseContext:completion:]_block_invoke_2.146
+ ___116-[SKAPresenceManager _releasePersistentPresenceAssertionForPresenceIdentifier:onDatabaseChannel:options:completion:]_block_invoke.90
+ ___116-[SKAPresenceManager _releasePersistentPresenceAssertionForPresenceIdentifier:onDatabaseChannel:options:completion:]_block_invoke.90.cold.1
+ ___122-[SKAPresenceManager _releaseTransientPresenceAssertionForPresenceIdentifier:onDatabaseChannel:options:client:completion:]_block_invoke.88
+ ___122-[SKAPresenceManager _releaseTransientPresenceAssertionForPresenceIdentifier:onDatabaseChannel:options:client:completion:]_block_invoke.88.cold.1
+ ___176-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPresencePayload:persistentPayload:serverRoutablePayload:withConnectivityPriority:options:isRefresh:completion:]_block_invoke.59
+ ___176-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPresencePayload:persistentPayload:serverRoutablePayload:withConnectivityPriority:options:isRefresh:completion:]_block_invoke.63
+ ___176-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPresencePayload:persistentPayload:serverRoutablePayload:withConnectivityPriority:options:isRefresh:completion:]_block_invoke.63.cold.1
+ ___176-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPresencePayload:persistentPayload:serverRoutablePayload:withConnectivityPriority:options:isRefresh:completion:]_block_invoke.64
+ ___176-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPresencePayload:persistentPayload:serverRoutablePayload:withConnectivityPriority:options:isRefresh:completion:]_block_invoke_2.61
+ ___176-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPresencePayload:persistentPayload:serverRoutablePayload:withConnectivityPriority:options:isRefresh:completion:]_block_invoke_2.61.cold.1
+ ___176-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPresencePayload:persistentPayload:serverRoutablePayload:withConnectivityPriority:options:isRefresh:completion:]_block_invoke_2.61.cold.2
+ ___176-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPresencePayload:persistentPayload:serverRoutablePayload:withConnectivityPriority:options:isRefresh:completion:]_block_invoke_2.65
+ ___176-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPresencePayload:persistentPayload:serverRoutablePayload:withConnectivityPriority:options:isRefresh:completion:]_block_invoke_2.65.cold.1
+ ___74-[SKAPresenceManager _presentDevicesChanged:persistentDevices:forChannel:]_block_invoke.134
+ ___74-[SKAPresenceManager _sendPollingMessageForChannel:withReason:completion:]_block_invoke.76
+ ___74-[SKAPresenceManager _sendPollingMessageForChannel:withReason:completion:]_block_invoke.77
+ ___74-[SKAPresenceManager _sendPollingMessageForChannel:withReason:completion:]_block_invoke.77.cold.1
+ ___74-[SKAPresenceManager _sendPollingMessageForChannel:withReason:completion:]_block_invoke.78
+ ___74-[SKAPresenceManager _sendPollingMessageForChannel:withReason:completion:]_block_invoke_2.79
+ ___74-[SKAPresenceManager _sendPollingMessageForChannel:withReason:completion:]_block_invoke_2.79.cold.1
+ ___80-[SKAPresenceManager presentDevicesForPresenceIdentifier:isPersonal:completion:]_block_invoke.98
+ ___82-[SKAPresenceManager pollAndUpdatePresentDevicesForChannel:withReason:completion:]_block_invoke.73
+ ___83-[SKAPresenceManager persistentDevicesForPresenceIdentifier:isPersonal:completion:]_block_invoke.100
+ ___83-[SKAPresenceManager sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.91
+ ___83-[SKAPresenceManager sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.91.cold.1
+ ___83-[SKAPresenceManager sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.92
+ ___83-[SKAPresenceManager sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke_2.93
+ ___83-[SKAPresenceManager sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke_2.93.cold.1
+ ___94-[SKAPresenceManager sendSetPersistentPayloadForChannel:payload:options:isRefresh:completion:]_block_invoke.112
+ ___94-[SKAPresenceManager sendSetPersistentPayloadForChannel:payload:options:isRefresh:completion:]_block_invoke.113
+ ___94-[SKAPresenceManager sendSetPersistentPayloadForChannel:payload:options:isRefresh:completion:]_block_invoke.113.cold.1
+ ___94-[SKAPresenceManager sendSetPersistentPayloadForChannel:payload:options:isRefresh:completion:]_block_invoke.114
+ ___94-[SKAPresenceManager sendSetPersistentPayloadForChannel:payload:options:isRefresh:completion:]_block_invoke_2.115
+ ___94-[SKAPresenceManager sendSetPersistentPayloadForChannel:payload:options:isRefresh:completion:]_block_invoke_2.115.cold.1
+ ___97-[SKAPresenceManager releasePersistentPresenceAssertionForPresenceIdentifier:options:completion:]_block_invoke.89
+ ___99-[SKAPresenceManager releaseAllTransientPresenceAssertionsAssociatedWithClient:options:completion:]_block_invoke.95
+ ___99-[SKAPresenceManager releaseAllTransientPresenceAssertionsAssociatedWithClient:options:completion:]_block_invoke.95.cold.1
+ ___99-[SKAPresenceManager releaseAllTransientPresenceAssertionsAssociatedWithClient:options:completion:]_block_invoke.96
+ ___block_literal_global.175
+ _objc_msgSend$forceSharedOwnershipAuthForPresence
- GCC_except_table126
- GCC_except_table129
- GCC_except_table132
- GCC_except_table210
- GCC_except_table245
- _$s18StatusKitAgentCore18SKAPresenceProfileC12featureFlags33_89FD40E2ED6DFFE699C0A34BEE1FDC54LLSo21SKFeatureFlagProviderCvpZ
- ___101-[SKAPresenceManager findPresenceChannelForPresenceIdentifier:isPersonal:databaseContext:completion:]_block_invoke.100
- ___101-[SKAPresenceManager findPresenceChannelForPresenceIdentifier:isPersonal:databaseContext:completion:]_block_invoke.100.cold.1
- ___101-[SKAPresenceManager setPersistentPayloadForPresenceIdentifier:onChannel:payload:options:completion:]_block_invoke.102
- ___101-[SKAPresenceManager setPersistentPayloadForPresenceIdentifier:onChannel:payload:options:completion:]_block_invoke.102.cold.1
- ___103-[SKAPresenceManager releaseTransientPresenceAssertionForPresenceIdentifier:options:client:completion:]_block_invoke.78
- ___106-[SKAPresenceManager findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.99
- ___107-[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.137
- ___107-[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.141
- ___107-[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.141.cold.1
- ___114-[SKAPresenceManager createPresenceChannelForPresenceIdentifier:options:shouldPersist:databaseContext:completion:]_block_invoke.101
- ___114-[SKAPresenceManager createPresenceChannelForPresenceIdentifier:options:shouldPersist:databaseContext:completion:]_block_invoke.101.cold.1
- ___115-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:shouldPersist:databaseContext:completion:]_block_invoke.142
- ___115-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:shouldPersist:databaseContext:completion:]_block_invoke.142.cold.1
- ___115-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:shouldPersist:databaseContext:completion:]_block_invoke.143
- ___115-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:shouldPersist:databaseContext:completion:]_block_invoke_2.144
- ___116-[SKAPresenceManager _releasePersistentPresenceAssertionForPresenceIdentifier:onDatabaseChannel:options:completion:]_block_invoke.81
- ___116-[SKAPresenceManager _releasePersistentPresenceAssertionForPresenceIdentifier:onDatabaseChannel:options:completion:]_block_invoke.81.cold.1
- ___122-[SKAPresenceManager _releaseTransientPresenceAssertionForPresenceIdentifier:onDatabaseChannel:options:client:completion:]_block_invoke.79
- ___122-[SKAPresenceManager _releaseTransientPresenceAssertionForPresenceIdentifier:onDatabaseChannel:options:client:completion:]_block_invoke.79.cold.1
- ___176-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPresencePayload:persistentPayload:serverRoutablePayload:withConnectivityPriority:options:isRefresh:completion:]_block_invoke.47
- ___176-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPresencePayload:persistentPayload:serverRoutablePayload:withConnectivityPriority:options:isRefresh:completion:]_block_invoke.51
- ___176-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPresencePayload:persistentPayload:serverRoutablePayload:withConnectivityPriority:options:isRefresh:completion:]_block_invoke.51.cold.1
- ___176-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPresencePayload:persistentPayload:serverRoutablePayload:withConnectivityPriority:options:isRefresh:completion:]_block_invoke.52
- ___176-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPresencePayload:persistentPayload:serverRoutablePayload:withConnectivityPriority:options:isRefresh:completion:]_block_invoke_2.49
- ___176-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPresencePayload:persistentPayload:serverRoutablePayload:withConnectivityPriority:options:isRefresh:completion:]_block_invoke_2.49.cold.1
- ___176-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPresencePayload:persistentPayload:serverRoutablePayload:withConnectivityPriority:options:isRefresh:completion:]_block_invoke_2.49.cold.2
- ___176-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPresencePayload:persistentPayload:serverRoutablePayload:withConnectivityPriority:options:isRefresh:completion:]_block_invoke_2.53
- ___176-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPresencePayload:persistentPayload:serverRoutablePayload:withConnectivityPriority:options:isRefresh:completion:]_block_invoke_2.53.cold.1
- ___74-[SKAPresenceManager _presentDevicesChanged:persistentDevices:forChannel:]_block_invoke.125
- ___74-[SKAPresenceManager _sendPollingMessageForChannel:withReason:completion:]_block_invoke.67
- ___74-[SKAPresenceManager _sendPollingMessageForChannel:withReason:completion:]_block_invoke.68
- ___74-[SKAPresenceManager _sendPollingMessageForChannel:withReason:completion:]_block_invoke.68.cold.1
- ___74-[SKAPresenceManager _sendPollingMessageForChannel:withReason:completion:]_block_invoke.69
- ___74-[SKAPresenceManager _sendPollingMessageForChannel:withReason:completion:]_block_invoke_2.70
- ___74-[SKAPresenceManager _sendPollingMessageForChannel:withReason:completion:]_block_invoke_2.70.cold.1
- ___80-[SKAPresenceManager presentDevicesForPresenceIdentifier:isPersonal:completion:]_block_invoke.89
- ___82-[SKAPresenceManager pollAndUpdatePresentDevicesForChannel:withReason:completion:]_block_invoke.62
- ___83-[SKAPresenceManager persistentDevicesForPresenceIdentifier:isPersonal:completion:]_block_invoke.91
- ___83-[SKAPresenceManager sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.82
- ___83-[SKAPresenceManager sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.82.cold.1
- ___83-[SKAPresenceManager sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.83
- ___83-[SKAPresenceManager sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke_2.84
- ___83-[SKAPresenceManager sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke_2.84.cold.1
- ___94-[SKAPresenceManager sendSetPersistentPayloadForChannel:payload:options:isRefresh:completion:]_block_invoke.103
- ___94-[SKAPresenceManager sendSetPersistentPayloadForChannel:payload:options:isRefresh:completion:]_block_invoke.104
- ___94-[SKAPresenceManager sendSetPersistentPayloadForChannel:payload:options:isRefresh:completion:]_block_invoke.104.cold.1
- ___94-[SKAPresenceManager sendSetPersistentPayloadForChannel:payload:options:isRefresh:completion:]_block_invoke.105
- ___94-[SKAPresenceManager sendSetPersistentPayloadForChannel:payload:options:isRefresh:completion:]_block_invoke_2.106
- ___94-[SKAPresenceManager sendSetPersistentPayloadForChannel:payload:options:isRefresh:completion:]_block_invoke_2.106.cold.1
- ___97-[SKAPresenceManager releasePersistentPresenceAssertionForPresenceIdentifier:options:completion:]_block_invoke.80
- ___99-[SKAPresenceManager releaseAllTransientPresenceAssertionsAssociatedWithClient:options:completion:]_block_invoke.86
- ___99-[SKAPresenceManager releaseAllTransientPresenceAssertionsAssociatedWithClient:options:completion:]_block_invoke.86.cold.1
- ___99-[SKAPresenceManager releaseAllTransientPresenceAssertionsAssociatedWithClient:options:completion:]_block_invoke.87
- ___block_literal_global.176
Functions:
+ -[SKAServerBag forceSharedOwnershipAuthForPresence]
~ -[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPresencePayload:persistentPayload:serverRoutablePayload:withConnectivityPriority:options:isRefresh:completion:] : 1792 -> 2052
~ -[SKAPresenceManager _sendPollingMessageForChannel:withReason:completion:] : 1420 -> 1672
~ -[SKAPresenceManager sendSetPersistentPayloadForChannel:payload:options:isRefresh:completion:] : 1044 -> 1316
~ -[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:] : 560 -> 444
~ ___107-[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke : 356 -> 948
- ___107-[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.137
+ _$s18StatusKitAgentCore18SKAPresenceProfileC9serverBag_WZ
~ _$s18StatusKitAgentCore18SKAPresenceProfileC20channelOwnershipTypeSo07ChannelhI0VvgTo : 60 -> 136
~ _$s18StatusKitAgentCore18SKAPresenceProfileC20channelOwnershipTypeSo07ChannelhI0Vvg : 40 -> 116
CStrings:
+ "Server bag indicates should force shared ownership auth: %@"
+ "forceSharedOwnershipAuthForPresence"
+ "shared-channels-force-shared-ownership-auth-presence"

```
