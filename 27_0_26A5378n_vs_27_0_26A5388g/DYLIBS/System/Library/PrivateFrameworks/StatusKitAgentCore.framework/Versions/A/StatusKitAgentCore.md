## StatusKitAgentCore

> `/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/Versions/A/StatusKitAgentCore`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`

```diff

-149.100.1.0.0
-  __TEXT.__text: 0x1cddf8
-  __TEXT.__objc_methlist: 0xb138
-  __TEXT.__const: 0x5ca8
-  __TEXT.__cstring: 0x971c
-  __TEXT.__oslogstring: 0x190e6
+151.100.1.0.0
+  __TEXT.__text: 0x1cdc90
+  __TEXT.__objc_methlist: 0xb0f0
+  __TEXT.__const: 0x5bf8
+  __TEXT.__cstring: 0x96ac
+  __TEXT.__oslogstring: 0x191e6
   __TEXT.__gcc_except_tab: 0xea8
-  __TEXT.__swift5_typeref: 0x29c4
-  __TEXT.__constg_swiftt: 0x1c24
-  __TEXT.__swift5_reflstr: 0x1557
-  __TEXT.__swift5_fieldmd: 0x14a4
+  __TEXT.__swift5_typeref: 0x29b6
+  __TEXT.__constg_swiftt: 0x1c08
+  __TEXT.__swift5_reflstr: 0x1527
+  __TEXT.__swift5_fieldmd: 0x1470
   __TEXT.__swift5_builtin: 0x26c
   __TEXT.__swift5_assocty: 0x470
-  __TEXT.__swift5_proto: 0x2c8
-  __TEXT.__swift5_types: 0x1d4
+  __TEXT.__swift5_proto: 0x2bc
+  __TEXT.__swift5_types: 0x1d0
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_capture: 0x19f0

   __TEXT.__swift_as_ret: 0x360
   __TEXT.__swift_as_cont: 0x6f8
   __TEXT.__swift5_acfuncs: 0x3c
-  __TEXT.__unwind_info: 0x5ce8
+  __TEXT.__unwind_info: 0x5cc0
   __TEXT.__eh_frame: 0x9d30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x838
+  __DATA_CONST.__const: 0x820
   __DATA_CONST.__objc_classlist: 0x538
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4490
+  __DATA_CONST.__objc_selrefs: 0x4478
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0xd70
-  __AUTH_CONST.__const: 0x81d8
-  __AUTH_CONST.__cfstring: 0x3320
-  __AUTH_CONST.__objc_const: 0x11760
-  __AUTH_CONST.__objc_intobj: 0x390
+  __DATA_CONST.__got: 0xd78
+  __AUTH_CONST.__const: 0x8108
+  __AUTH_CONST.__cfstring: 0x3240
+  __AUTH_CONST.__objc_const: 0x11740
+  __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1410
-  __AUTH.__objc_data: 0x1738
-  __AUTH.__data: 0x2b8
+  __AUTH_CONST.__auth_got: 0x1408
+  __AUTH.__objc_data: 0x1360
+  __AUTH.__data: 0x198
   __DATA.__objc_ivar: 0x808
-  __DATA.__data: 0x1fb0
-  __DATA.__common: 0x18
-  __DATA.__bss: 0x4580
-  __DATA_DIRTY.__objc_data: 0x3700
-  __DATA_DIRTY.__data: 0x1aa0
-  __DATA_DIRTY.__bss: 0x1350
-  __DATA_DIRTY.__common: 0xa0
+  __DATA.__data: 0x1c08
+  __DATA.__bss: 0x4200
+  __DATA_DIRTY.__objc_data: 0x3ad0
+  __DATA_DIRTY.__data: 0x1f10
+  __DATA_DIRTY.__bss: 0x1550
+  __DATA_DIRTY.__common: 0xb0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7884
-  Symbols:   16162
-  CStrings:  2603
+  Functions: 7870
+  Symbols:   16123
+  CStrings:  2597
 
Symbols:
+ -[SKAPresenceClient clientPrefixedPresenceIdentifierForPresenceIdentifier:serviceIdentifier:error:]
+ _$s18StatusKitAgentCore18SKAPresenceProfileC16identifierPrefix11channelType7options9pushTopic27serverObservableAdopterName17serviceIdentifier21subscribedFilterState24maxPersistentPayloadSize0w8PresenceyZ018presenceTTLSeconds0I10TTLSeconds018idsFirewallServiceQ023presenceProtocolVersion25persistentProtocolVersionACSS_AC011ChannelSyncJ0OAA0eF7OptionsVAA014SKAProfilePushM0CAC0S0OAYSo08SKATopicU0VAC0yZ0OA1_S2dSSAC15ProtocolVersionOA3_tcfCTq
+ _$s18StatusKitAgentCore18SKAPresenceProfileC16identifierPrefix11channelType7options9pushTopic27serverObservableAdopterName17serviceIdentifier21subscribedFilterState24maxPersistentPayloadSize0w8PresenceyZ018presenceTTLSeconds0I10TTLSeconds018idsFirewallServiceQ023presenceProtocolVersion25persistentProtocolVersionACSS_AC011ChannelSyncJ0OAA0eF7OptionsVAA014SKAProfilePushM0CAC0S0OAYSo08SKATopicU0VAC0yZ0OA1_S2dSSAC15ProtocolVersionOA3_tcfcTf4nnngnnnnnnnnnnn_n
+ _$s18StatusKitAgentCore26SKAIncomingMessageMetadataC8prioritySivg
+ _$s18StatusKitAgentCore26SKAIncomingMessageMetadataC8prioritySivgTo
+ _$s18StatusKitAgentCore26SKAIncomingMessageMetadataC8prioritySivpMV
+ _RPOptionStatusFlags
+ __PROPERTIES__TtC18StatusKitAgentCore26SKAIncomingMessageMetadata
+ _objc_msgSend$clientPrefixedPresenceIdentifierForPresenceIdentifier:serviceIdentifier:error:
+ _objc_msgSend$initWithUnsignedLongLong:
+ _objc_msgSend$sk_clientIdentifierPrefixFromPresenceIdentifier
+ _objc_msgSend$sk_descriptionFromSKUpdatePriority:
+ _objc_msgSend$sk_sha256Hash
- +[NSString(StatusKitAgent) descriptionFromSKUpdatePriority:]
- -[NSString(StatusKitAgent) clientIdentifierPrefixFromPresenceIdentifier]
- -[NSString(StatusKitAgent) ska_sha256Hash]
- -[SKAPresenceClient clientPrefixedPresenceIdentifierForPresenceIdentifier:serviceIdentifier:]
- -[SKAServerBag forceSharedOwnershipAuthForPresence]
- _$s18StatusKitAgentCore18SKAPresenceProfileC15ChannelSyncTypeOSHAASH13_rawHashValue4seedS2i_tFTWTm
- _$s18StatusKitAgentCore18SKAPresenceProfileC15ChannelSyncTypeOSHAASH9hashValueSivgTWTm
- _$s18StatusKitAgentCore18SKAPresenceProfileC16identifierPrefix11channelType7options9pushTopic27serverObservableAdopterName17serviceIdentifier21subscribedFilterState24maxPersistentPayloadSize0w8PresenceyZ018presenceTTLSeconds0I10TTLSeconds018idsFirewallServiceQ00N12BackingStore23presenceProtocolVersion25persistentProtocolVersionACSS_AC011ChannelSyncJ0OAA0eF7OptionsVAA014SKAProfilePushM0CAC0S0OAZSo08SKATopicU0VAC0yZ0OA2_S2dSSAC18ServerBackingStoreOAC15ProtocolVersionOA6_tcfCTq
- _$s18StatusKitAgentCore18SKAPresenceProfileC16identifierPrefix11channelType7options9pushTopic27serverObservableAdopterName17serviceIdentifier21subscribedFilterState24maxPersistentPayloadSize0w8PresenceyZ018presenceTTLSeconds0I10TTLSeconds018idsFirewallServiceQ00N12BackingStore23presenceProtocolVersion25persistentProtocolVersionACSS_AC011ChannelSyncJ0OAA0eF7OptionsVAA014SKAProfilePushM0CAC0S0OAZSo08SKATopicU0VAC0yZ0OA2_S2dSSAC18ServerBackingStoreOAC15ProtocolVersionOA6_tcfcTf4nnngnnnnnnnnnnnn_n
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOAESQAAWL
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOAESQAAWl
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOMF
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOMa
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOMf
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOMn
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreON
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOSHAAMc
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOSHAAMcMK
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOSHAASH13_rawHashValue4seedS2i_tFTW
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOSHAASH4hash4intoys6HasherVz_tFTW
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOSHAASH9hashValueSivgTW
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOSHAASQWb
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOSQAAMc
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOSQAAMcMK
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOSQAASQ2eeoiySbx_xtFZTW
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOWV
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOs23CustomStringConvertibleAAMc
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOs23CustomStringConvertibleAAMcMK
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOs23CustomStringConvertibleAAsAFP11descriptionSSvgTW
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOwet
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOwst
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOwug
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOwui
- _$s18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOwup
- _$s18StatusKitAgentCore18SKAPresenceProfileC18serverBackingStoreAC06ServerhI0Ovg
- _$s18StatusKitAgentCore18SKAPresenceProfileC18serverBackingStoreAC06ServerhI0OvgTv_r
- _$s18StatusKitAgentCore18SKAPresenceProfileC19_serverBackingStoreAC06ServerhI0OvpWvd
- _$s18StatusKitAgentCore18SKAPresenceProfileC9serverBagSo09SKAServerH9Providing_s8SendablepvpZ
- _$s18StatusKitAgentCore18SKAPresenceProfileC9serverBag_WZ
- _$s18StatusKitAgentCore18SKAPresenceProfileC9serverBag_Wz
- __OBJC_$_CATEGORY_CLASS_METHODS_NSString_$_StatusKitAgent
- _associated conformance 18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreOSHAASQ
- _objc_msgSend$UTF8String
- _objc_msgSend$clientIdentifierPrefixFromPresenceIdentifier
- _objc_msgSend$clientPrefixedPresenceIdentifierForPresenceIdentifier:serviceIdentifier:
- _objc_msgSend$componentsSeparatedByString:
- _objc_msgSend$descriptionFromSKUpdatePriority:
- _objc_msgSend$forceSharedOwnershipAuthForPresence
- _objc_msgSend$ska_sha256Hash
- _objc_msgSend$stringWithCapacity:
- _strlen
- _symbolic _____ 18StatusKitAgentCore18SKAPresenceProfileC18ServerBackingStoreO
CStrings:
+ "Could not derive a client-prefixed presence identifier"
+ "Could not derive a client-prefixed presence identifier, client identifier prefix was nil { presenceIdentifier: %{public}@, serviceIdentifier: %{public}@, clientConnection: %@ }"
+ "Could not derive a client-prefixed presence identifier, presence identifier was nil { serviceIdentifier: %{public}@, clientConnection: %@ }"
- "%02x"
- ", serverBackingStore="
- "-"
- "SKUpdatePriorityDefault"
- "SKUpdatePriorityHigh"
- "SKUpdatePriorityMedium"
- "Server bag indicates should force shared ownership auth: %@"
- "Unknown Priority"
- "shared-channels-force-shared-ownership-auth-presence"
```
