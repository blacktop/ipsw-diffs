## StatusKitAgentCore

> `/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/Versions/A/StatusKitAgentCore`

```diff

-80.400.131.0.0
-  __TEXT.__text: 0xc26a4
-  __TEXT.__auth_stubs: 0x15b0
-  __TEXT.__objc_methlist: 0x6308
-  __TEXT.__const: 0x694
-  __TEXT.__cstring: 0x2f8a
-  __TEXT.__oslogstring: 0x101ed
-  __TEXT.__gcc_except_tab: 0xd58
-  __TEXT.__swift5_typeref: 0x8f4
-  __TEXT.__swift5_capture: 0x1c0
+80.500.181.0.0
+  __TEXT.__text: 0xc8d88
+  __TEXT.__auth_stubs: 0x15d0
+  __TEXT.__objc_methlist: 0x7388
+  __TEXT.__const: 0x6a4
+  __TEXT.__cstring: 0x2dba
+  __TEXT.__oslogstring: 0x1093d
+  __TEXT.__gcc_except_tab: 0xe34
+  __TEXT.__swift5_typeref: 0x9d0
+  __TEXT.__swift5_capture: 0x488
   __TEXT.__constg_swiftt: 0x160
-  __TEXT.__swift5_reflstr: 0x2e8
+  __TEXT.__swift5_reflstr: 0x326
   __TEXT.__swift5_assocty: 0x60
-  __TEXT.__swift5_fieldmd: 0x1fc
+  __TEXT.__swift5_fieldmd: 0x214
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x38
   __TEXT.__swift5_types: 0x20
+  __TEXT.__swift_as_entry: 0x70
+  __TEXT.__swift_as_ret: 0x4c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x20c8
-  __TEXT.__eh_frame: 0x1110
-  __TEXT.__objc_classname: 0xe00
-  __TEXT.__objc_methname: 0xfabc
-  __TEXT.__objc_methtype: 0x43ea
-  __TEXT.__objc_stubs: 0x8c80
-  __DATA_CONST.__got: 0x760
-  __DATA_CONST.__const: 0x4a8
+  __TEXT.__unwind_info: 0x21f8
+  __TEXT.__eh_frame: 0x12d8
+  __TEXT.__objc_classname: 0xe24
+  __TEXT.__objc_methname: 0xfee9
+  __TEXT.__objc_methtype: 0x44af
+  __TEXT.__objc_stubs: 0x8f20
+  __DATA_CONST.__got: 0x770
+  __DATA_CONST.__const: 0x4b0
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x158
+  __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e38
-  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_selrefs: 0x30a0
+  __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x240
-  __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0xae8
-  __AUTH_CONST.__const: 0x25c8
-  __AUTH_CONST.__cfstring: 0x2360
-  __AUTH_CONST.__objc_const: 0xfae0
-  __AUTH_CONST.__objc_intobj: 0x78
+  __DATA_CONST.__objc_arraydata: 0x18
+  __AUTH_CONST.__auth_got: 0xaf8
+  __AUTH_CONST.__const: 0x2d80
+  __AUTH_CONST.__cfstring: 0x2420
+  __AUTH_CONST.__objc_const: 0xde58
+  __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1cf0
+  __AUTH.__objc_data: 0x1cf8
   __AUTH.__data: 0x170
-  __DATA.__objc_ivar: 0x5d8
-  __DATA.__data: 0x12e0
-  __DATA.__bss: 0x9c0
+  __DATA.__objc_ivar: 0x5e4
+  __DATA.__data: 0x13e0
+  __DATA.__bss: 0x9d0
   __DATA.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 9F17E5BE-7100-30FA-9FB7-621E90A997EF
-  Functions: 3466
-  Symbols:   6597
-  CStrings:  4261
+  UUID: 8D7A5F74-144D-3373-BAB9-C726D38C6F30
+  Functions: 3597
+  Symbols:   6722
+  CStrings:  4333
 
Symbols:
+ +[SKAAccountProvider logger].cold.1
+ +[SKAChannelManager logger].cold.1
+ +[SKADatabaseChannel logger].cold.1
+ +[SKADatabaseManager logger].cold.1
+ +[SKADatabaseProvider logger].cold.1
+ +[SKADatabaseReceivedInvitation logger].cold.1
+ +[SKADatabaseStatus logger].cold.1
+ +[SKAGeneratedEncryptionKey logger].cold.1
+ +[SKAInvitationManager logger].cold.1
+ +[SKAMessagingProvider logger].cold.1
+ +[SKAPresenceAssertion logger].cold.1
+ +[SKAPresenceClient logger].cold.1
+ +[SKAPresenceClient oversizeLogger].cold.1
+ +[SKAPresenceClientConnection logger].cold.1
+ +[SKAPresenceEncryptionKey logger].cold.1
+ +[SKAPresenceManager logger].cold.1
+ +[SKAPresenceManager oversizeLogger].cold.1
+ +[SKAPresenceMembershipKey logger].cold.1
+ +[SKAPresenceSubscriptionAssertion logger].cold.1
+ +[SKAPushManager logger].cold.1
+ +[SKAServerBag logger].cold.1
+ +[SKAStatusEncryptionManager logger].cold.1
+ +[SKAStatusPublishingManager logger].cold.1
+ +[SKAStatusPublishingServiceClient logger].cold.1
+ +[SKAStatusPublishingServiceClientConnection logger].cold.1
+ +[SKAStatusReceivingManager logger].cold.1
+ +[SKAStatusServer logger].cold.1
+ +[SKAStatusServer sharedInstance].cold.1
+ +[SKAStatusSubscriptionManager logger].cold.1
+ +[SKAStatusSubscriptionServiceClient logger].cold.1
+ +[SKAStatusSubscriptionServiceClientConnection logger].cold.1
+ +[SKASystemMonitor logger].cold.1
+ +[SKASystemMonitor sharedInstance].cold.1
+ +[SKATransientSubscriptionAssertion logger].cold.1
+ -[SKADatabaseProvider handlePersistentStoreEventChangedNotification:].cold.1
+ -[SKADatabaseProvider setSetupVoucher:]
+ -[SKADatabaseProvider setupVoucher]
+ -[SKADatabasePublishedLocalStatusDevice discoverySource]
+ -[SKADatabasePublishedLocalStatusDevice initWithIDSIdentifier:pendingStatuses:deliveredStatuses:discoverySource:]
+ -[SKAInvitationManager _acceptInvitationMessage:fromHandle:toHandle:messageGuid:existingChannel:databaseContext:]
+ -[SKAInvitationManager _acceptInvitationMessage:fromHandle:toHandle:messageGuid:existingChannel:databaseContext:].cold.1
+ -[SKAInvitationManager _acceptInvitationMessage:fromHandle:toHandle:messageGuid:existingChannel:databaseContext:].cold.2
+ -[SKAInvitationManager _shouldAcceptInvitationMessageForPresenceIdentifier:fromHandle:fromMergeID:inServiceFirewall:databaseContext:completion:]
+ -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:]
+ -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:].cold.1
+ -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:].cold.10
+ -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:].cold.11
+ -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:].cold.12
+ -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:].cold.13
+ -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:].cold.14
+ -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:].cold.15
+ -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:].cold.2
+ -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:].cold.3
+ -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:].cold.4
+ -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:].cold.5
+ -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:].cold.6
+ -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:].cold.7
+ -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:].cold.8
+ -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:].cold.9
+ -[SKAMessagingProvider isHandle:inFirewallForService:completion:]
+ -[SKAMessagingProvider isHandle:inFirewallForService:completion:].cold.1
+ -[SKAMessagingProvider listOfValidSenderHandles:containsSenderMergeID:completion:]
+ -[SKAMessagingProvider listOfValidSenderHandles:containsSenderMergeID:completion:].cold.1
+ -[SKAMessagingProvider queue]
+ -[SKAMessagingProvider setQueue:]
+ -[SKAPresenceManager _markReassert].cold.1
+ -[SKAPresenceManager _maxReassertions]
+ -[SKAPresenceManager _shouldReassert].cold.1
+ -[SKAStatusServer _kettleFeatureEnabled].cold.1
+ -[SKAStatusServer service:didReceiveIncomingMessage:fromID:fromMergeID:toID:messageGuid:]
+ -[SKAStatusSubscriptionManager _removeActivePresenceSubscriptionsForClient:]
+ -[SKAStatusSubscriptionManager _removeActiveTransientSubscriptionsForClient:]
+ -[SKHandle(StatusKitAgent) idsURI]
+ GCC_except_table100
+ GCC_except_table122
+ GCC_except_table133
+ GCC_except_table145
+ GCC_except_table197
+ GCC_except_table222
+ GCC_except_table51
+ GCC_except_table54
+ GCC_except_table74
+ GCC_except_table75
+ GCC_except_table76
+ OBJC_IVAR_$_SKADatabaseProvider._setupVoucher
+ OBJC_IVAR_$_SKADatabasePublishedLocalStatusDevice._discoverySource
+ OBJC_IVAR_$_SKAMessagingProvider._queue
+ _OBJC_CLASS_$_CKOperationConfiguration
+ _OBJC_CLASS_$_IDSFirewall
+ _OBJC_CLASS_$_NSPersistentCloudKitContainerActivityVoucher
+ _PROTOCOLS_SKALocalStatusServer.12
+ _PROTOCOLS__TtCC18StatusKitAgentCore20SKALocalStatusServer16DatabaseDelegate.17
+ __100-[SKAPresenceManager createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.71
+ __100-[SKAPresenceManager createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.71.cold.1
+ __101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.98
+ __101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.98.cold.1
+ __101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.99
+ __101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke_2.100
+ __101-[SKAPresenceManager findPresenceChannelForPresenceIdentifier:isPersonal:databaseContext:completion:]_block_invoke.70
+ __103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke.25
+ __103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke.26
+ __103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke.26.cold.1
+ __103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke.27
+ __103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke_2.28
+ __103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke_2.28.cold.1
+ __106-[SKAPresenceManager findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.69
+ __107-[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:]_block_invoke.cold.1
+ __107-[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.93
+ __107-[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.94
+ __107-[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.95
+ __113-[SKAPresenceManager retainPresenceAssertionForPresenceIdentifier:withPresencePayload:options:client:completion:]_block_invoke.18
+ __113-[SKAPresenceManager retainPresenceAssertionForPresenceIdentifier:withPresencePayload:options:client:completion:]_block_invoke.19
+ __144-[SKAInvitationManager _shouldAcceptInvitationMessageForPresenceIdentifier:fromHandle:fromMergeID:inServiceFirewall:databaseContext:completion:]_block_invoke.90
+ __144-[SKAInvitationManager _shouldAcceptInvitationMessageForPresenceIdentifier:fromHandle:fromMergeID:inServiceFirewall:databaseContext:completion:]_block_invoke.90.cold.1
+ __144-[SKAInvitationManager _shouldAcceptInvitationMessageForPresenceIdentifier:fromHandle:fromMergeID:inServiceFirewall:databaseContext:completion:]_block_invoke.cold.1
+ __144-[SKAInvitationManager _shouldAcceptInvitationMessageForPresenceIdentifier:fromHandle:fromMergeID:inServiceFirewall:databaseContext:completion:]_block_invoke.cold.2
+ __48-[SKADatabaseProvider createPersistentContainer]_block_invoke.16
+ __48-[SKADatabaseProvider createPersistentContainer]_block_invoke.16.cold.1
+ __48-[SKADatabaseProvider createPersistentContainer]_block_invoke.cold.2
+ __48-[SKADatabaseProvider createPersistentContainer]_block_invoke.cold.3
+ __63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke.33
+ __63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke.33.cold.1
+ __63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke.34
+ __63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke_2.35
+ __63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke_2.35.cold.1
+ __65-[SKAMessagingProvider isHandle:inFirewallForService:completion:]_block_invoke.cold.1
+ __80-[SKAPresenceManager presentDevicesForPresenceIdentifier:isPersonal:completion:]_block_invoke.62
+ __82-[SKAMessagingProvider listOfValidSenderHandles:containsSenderMergeID:completion:]_block_invoke.cold.1
+ __84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.50
+ __84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.50.cold.1
+ __84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.51
+ __84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke_2.52
+ __84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke_2.52.cold.1
+ __90-[SKAPresenceManager releaseAllPresenceAssertionsAssociatedWithClient:options:completion:]_block_invoke.60
+ __90-[SKAPresenceManager releaseAllPresenceAssertionsAssociatedWithClient:options:completion:]_block_invoke.60.cold.1
+ __94-[SKAPresenceManager releasePresenceAssertionForPresenceIdentifier:options:client:completion:]_block_invoke.43
+ __94-[SKAPresenceManager releasePresenceAssertionForPresenceIdentifier:options:client:completion:]_block_invoke.44
+ __94-[SKAPresenceManager releasePresenceAssertionForPresenceIdentifier:options:client:completion:]_block_invoke.44.cold.1
+ __97-[SKAInvitationManager _createPersonalChannelForStatusTypeIdentifier:databaseContext:completion:]_block_invoke.103
+ __97-[SKAInvitationManager _createPersonalChannelForStatusTypeIdentifier:databaseContext:completion:]_block_invoke.103.cold.1
+ __97-[SKAInvitationManager _createPersonalChannelForStatusTypeIdentifier:databaseContext:completion:]_block_invoke.104
+ __OBJC_$_PROTOCOL_REFS_OS_os_transaction
+ __OBJC_$_PROTOCOL_REFS_OS_xpc_object
+ __OBJC_LABEL_PROTOCOL_$_OS_os_transaction
+ __OBJC_LABEL_PROTOCOL_$_OS_xpc_object
+ __OBJC_PROTOCOL_$_OS_os_transaction
+ __OBJC_PROTOCOL_$_OS_xpc_object
+ ___107-[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:]_block_invoke
+ ___113-[SKAInvitationManager _acceptInvitationMessage:fromHandle:toHandle:messageGuid:existingChannel:databaseContext:]_block_invoke
+ ___144-[SKAInvitationManager _shouldAcceptInvitationMessageForPresenceIdentifier:fromHandle:fromMergeID:inServiceFirewall:databaseContext:completion:]_block_invoke
+ ___65-[SKAMessagingProvider isHandle:inFirewallForService:completion:]_block_invoke
+ ___82-[SKAMessagingProvider listOfValidSenderHandles:containsSenderMergeID:completion:]_block_invoke
+ ___block_descriptor_32_e50_v24?0"NSPersistentStoreDescription"8"NSError"16l
+ ___block_descriptor_56_e8_32s40bs48r_e40_v24?0"SKADatabaseChannel"8"NSError"16l
+ ___block_descriptor_56_e8_32s40r48r_e50_v24?0"NSPersistentStoreDescription"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48bs_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48bs56w_e8_v12?0B8l
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e40_v24?0"SKADatabaseChannel"8"NSError"16l
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e40_v24?0"SKADatabaseChannel"8"NSError"16l
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e8_v12?0B8l
+ ___copy_helper_block_e8_32s40b48r
+ ___copy_helper_block_e8_32s40s48s56b64r
+ ___copy_helper_block_e8_32s40s48s56s64s72b80r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_project_boxed_opaque_existential_0
+ __block_literal_global.166
+ __block_literal_global.93
+ __xpc_event_key_name
+ _flat unique So13OS_xpc_object_p
+ _flat unique So17OS_os_transaction_p
+ _objc_msgSend$_acceptInvitationMessage:fromHandle:toHandle:messageGuid:existingChannel:databaseContext:
+ _objc_msgSend$_maxReassertions
+ _objc_msgSend$_removeActivePresenceSubscriptionsForClient:
+ _objc_msgSend$_removeActiveTransientSubscriptionsForClient:
+ _objc_msgSend$_shouldAcceptInvitationMessageForPresenceIdentifier:fromHandle:fromMergeID:inServiceFirewall:databaseContext:completion:
+ _objc_msgSend$addListenerID:forService:
+ _objc_msgSend$configurationName
+ _objc_msgSend$currentEntries:
+ _objc_msgSend$destinationURIs
+ _objc_msgSend$discoverySource
+ _objc_msgSend$endpoints
+ _objc_msgSend$expireActivityVoucher:
+ _objc_msgSend$handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:
+ _objc_msgSend$idInfoForDestinations:service:infoTypes:options:listenerID:queue:completionBlock:
+ _objc_msgSend$idsURI
+ _objc_msgSend$initWithIDSIdentifier:pendingStatuses:deliveredStatuses:discoverySource:
+ _objc_msgSend$initWithLabel:forEventsOfType:withConfiguration:affectingObjectsMatching:
+ _objc_msgSend$initWithService:queue:
+ _objc_msgSend$isHandle:inFirewallForService:completion:
+ _objc_msgSend$listOfValidSenderHandles:containsSenderMergeID:completion:
+ _objc_msgSend$senderCorrelationIdentifier
+ _objc_msgSend$service:didReceiveIncomingMessage:fromID:fromMergeID:toID:messageGuid:
+ _objc_msgSend$setActivityVouchers:
+ _objc_msgSend$setQualityOfService:
+ _objc_msgSend$setSource:
+ _objc_msgSend$source
+ _objc_msgSend$uri
+ _symbolic SSIego_
+ _symbolic Sbz_Xx
+ _symbolic Sccyyt______pG s5ErrorP
+ _symbolic So21RPCompanionLinkClientCSg
+ _symbolic So9IDSDeviceC
+ _symbolic SsIegr_
+ _symbolic _____ s5UInt8V
+ _symbolic _____XDXMT 18StatusKitAgentCore08SKALocalA6ServerC
+ _symbolic ______p So13OS_xpc_objectP
+ _symbolic ______pSg So17OS_os_transactionP
+ _symbolic _____yySpy_____Gz_SpySo8NSObjectCSgGSgzSpyypGSgztcG s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic yyc
+ _xpc_dictionary_create_reply
+ _xpc_dictionary_get_bool
+ _xpc_dictionary_get_string
+ _xpc_dictionary_send_reply
+ _xpc_set_event_stream_handler
+ block_copy_helper.234
+ block_copy_helper.237
+ block_copy_helper.240
+ block_copy_helper.243
+ block_copy_helper.246
+ block_copy_helper.256
+ block_copy_helper.287
+ block_copy_helper.49
+ block_copy_helper.56
+ block_copy_helper.62
+ block_copy_helper.72
+ block_descriptor.236
+ block_descriptor.239
+ block_descriptor.242
+ block_descriptor.245
+ block_descriptor.248
+ block_descriptor.258
+ block_descriptor.289
+ block_descriptor.51
+ block_descriptor.58
+ block_descriptor.74
+ block_destroy_helper.235
+ block_destroy_helper.238
+ block_destroy_helper.241
+ block_destroy_helper.244
+ block_destroy_helper.247
+ block_destroy_helper.257
+ block_destroy_helper.288
+ block_destroy_helper.50
+ block_destroy_helper.57
+ block_destroy_helper.63
+ block_destroy_helper.73
+ get_witness_table SeRzSERzl10Foundation4DataVSEHPyHC.233
+ get_witness_table SeRzSERzl10Foundation4DataVSeHPyHC.232
+ objectdestroy.270Tm
+ objectdestroy.83Tm
- -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:]
- -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:].cold.1
- -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:].cold.10
- -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:].cold.11
- -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:].cold.12
- -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:].cold.13
- -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:].cold.14
- -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:].cold.15
- -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:].cold.16
- -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:].cold.17
- -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:].cold.2
- -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:].cold.3
- -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:].cold.4
- -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:].cold.5
- -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:].cold.6
- -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:].cold.7
- -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:].cold.8
- -[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:].cold.9
- -[SKAStatusServer service:didReceiveIncomingMessage:fromID:toID:messageGuid:]
- GCC_except_table10
- GCC_except_table113
- GCC_except_table128
- GCC_except_table140
- GCC_except_table191
- GCC_except_table215
- GCC_except_table32
- GCC_except_table42
- GCC_except_table52
- GCC_except_table53
- GCC_except_table66
- GCC_except_table67
- _NSPersistentStoreRemoteChangeNotification
- _NSPersistentStoreRemoteChangeNotificationPostOptionKey
- _OBJC_CLASS_$_NSPersistentStoreCoordinator
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _PROTOCOLS_SKALocalStatusServer.28
- _PROTOCOLS__TtCC18StatusKitAgentCore20SKALocalStatusServer16DatabaseDelegate.33
- __100-[SKAPresenceManager createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.68
- __100-[SKAPresenceManager createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.68.cold.1
- __101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.100
- __101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.100.cold.1
- __101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.101
- __101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke_2.102
- __101-[SKAPresenceManager findPresenceChannelForPresenceIdentifier:isPersonal:databaseContext:completion:]_block_invoke.67
- __103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke.22
- __103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke.23
- __103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke.23.cold.1
- __103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke.24
- __103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke_2.25
- __103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke_2.25.cold.1
- __106-[SKAPresenceManager findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.66
- __107-[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.89
- __107-[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.90
- __107-[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.97
- __113-[SKAPresenceManager retainPresenceAssertionForPresenceIdentifier:withPresencePayload:options:client:completion:]_block_invoke.15
- __113-[SKAPresenceManager retainPresenceAssertionForPresenceIdentifier:withPresencePayload:options:client:completion:]_block_invoke.16
- __63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke.30
- __63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke.30.cold.1
- __63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke.31
- __63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke_2.32
- __63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke_2.32.cold.1
- __80-[SKAPresenceManager presentDevicesForPresenceIdentifier:isPersonal:completion:]_block_invoke.59
- __84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.47
- __84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.47.cold.1
- __84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.48
- __84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke_2.49
- __84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke_2.49.cold.1
- __90-[SKAPresenceManager releaseAllPresenceAssertionsAssociatedWithClient:options:completion:]_block_invoke.57
- __90-[SKAPresenceManager releaseAllPresenceAssertionsAssociatedWithClient:options:completion:]_block_invoke.57.cold.1
- __94-[SKAPresenceManager releasePresenceAssertionForPresenceIdentifier:options:client:completion:]_block_invoke.40
- __94-[SKAPresenceManager releasePresenceAssertionForPresenceIdentifier:options:client:completion:]_block_invoke.41
- __94-[SKAPresenceManager releasePresenceAssertionForPresenceIdentifier:options:client:completion:]_block_invoke.41.cold.1
- __97-[SKAInvitationManager _createPersonalChannelForStatusTypeIdentifier:databaseContext:completion:]_block_invoke.90
- __97-[SKAInvitationManager _createPersonalChannelForStatusTypeIdentifier:databaseContext:completion:]_block_invoke.90.cold.1
- __97-[SKAInvitationManager _createPersonalChannelForStatusTypeIdentifier:databaseContext:completion:]_block_invoke.91
- ___95-[SKAInvitationManager handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:]_block_invoke
- ___block_descriptor_40_e8_32r_e50_v24?0"NSPersistentStoreDescription"8"NSError"16l
- ___block_descriptor_48_e8_32s40bs_e40_v24?0"SKADatabaseChannel"8"NSError"16l
- ___block_descriptor_64_e8_32s40s48s56bs_e40_v24?0"SKADatabaseChannel"8"NSError"16l
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e40_v24?0"SKADatabaseChannel"8"NSError"16l
- ___copy_helper_block_e8_32r
- ___destroy_helper_block_e8_32r
- __block_literal_global.164
- _objc_msgSend$activePresenceSubscriptionsByClient
- _objc_msgSend$activeTransientSubscriptionsByClient
- _objc_msgSend$handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:
- _objc_msgSend$initWithIDSIdentifier:pendingStatuses:deliveredStatuses:
- _objc_msgSend$initWithManagedObjectModel:
- _objc_msgSend$service:didReceiveIncomingMessage:fromID:toID:messageGuid:
- block_copy_helper.12
- block_copy_helper.121
- block_copy_helper.15
- block_copy_helper.6
- block_copy_helper.61
- block_copy_helper.75
- block_copy_helper.82
- block_copy_helper.85
- block_copy_helper.9
- block_descriptor.11
- block_descriptor.123
- block_descriptor.14
- block_descriptor.17
- block_descriptor.63
- block_descriptor.77
- block_descriptor.8
- block_descriptor.84
- block_descriptor.87
- block_destroy_helper.10
- block_destroy_helper.122
- block_destroy_helper.13
- block_destroy_helper.16
- block_destroy_helper.62
- block_destroy_helper.7
- block_destroy_helper.76
- block_destroy_helper.83
- block_destroy_helper.86
- get_witness_table SeRzSERzl10Foundation4DataVSEHPyHC.101
- get_witness_table SeRzSERzl10Foundation4DataVSeHPyHC.100
- objectdestroy.104Tm
- objectdestroy.96Tm
CStrings:
+ "%"
+ "%@ Setup Voucher"
+ "@\"NSPersistentCloudKitContainer\""
+ "@\"NSPersistentCloudKitContainerActivityVoucher\""
+ "@44@0:8@16@24@32S40"
+ "Attempting to reload persistent stores"
+ "Boosting import priority with voucher: %@"
+ "CloudKitVoucher"
+ "CompanionLink activate delivery SKIP - no IDS identifiers"
+ "Could not retreive IDS firewall for %@"
+ "Error executing fetch for channels by presence identifier \"%@\". Error: %@"
+ "Error querying IDS for destination info: %@"
+ "Expiring voucher %@"
+ "Failed to destroy persistent store %@ -- %@"
+ "Failed to load %@ on second attempt due to %@"
+ "Failed to reply to Rapport wake event: %s"
+ "Fetch request for channels by presence identifier \"%@\" completed with %ld result(s) (limited = %@). Representative channel is %@, created at: %@"
+ "Fetch request for channels by presence identifier \"%@\" found no match."
+ "Fetch request for channels by presence identifier \"%@\" returned a nil result"
+ "Found cloud store: %@"
+ "Found local store: %@"
+ "Invitation message did not contain a presence identifier with a valid client ID, dropping: %@"
+ "Invitation message missing date channel created. Will use current server time"
+ "Invitation was rejected for sender insecurity, dropping: %@"
+ "No URI destinations to query"
+ "OS_os_transaction"
+ "OS_xpc_object"
+ "Presence channel has never been seen before, accepting"
+ "Querying IDS for URI destinations: %@ looking for sender merge ID: %@"
+ "Querying if sender %@ is in list of valid sender handles: %@"
+ "Received Rapport wake event for: %s"
+ "Received incoming message: %@ fromID: %@ (%@)"
+ "Received publish device found without a browserTask. Ignoring"
+ "Releasing transaction"
+ "Retreived IDS firewall entries for %@: %@"
+ "Retreiving IDS firewall for %@ returned error: %@"
+ "S"
+ "S16@0:8"
+ "Sender %@ was in list of valid sender handles, accepting"
+ "Sender %@ was not in list of valid sender handles"
+ "Sender %@ was not in list of valid sender handles, checking firewall for %@"
+ "Sender %@ was not in the firewall for %@"
+ "Server bag indicates our max reassertion count for reasserting presence should be %lu"
+ "Skipping unexpected found status device %@"
+ "Stopping existing browser task for shared home"
+ "T@\"IDSURI\",R,N"
+ "T@\"NSPersistentCloudKitContainer\",&,N,V_persistentContainer"
+ "T@\"NSPersistentCloudKitContainerActivityVoucher\",&,N,V_setupVoucher"
+ "TS,R,N,V_discoverySource"
+ "Taking transaction out for 30 seconds due to launch on demand"
+ "URI destinations: %@ map to valid merge IDs: %@"
+ "Unexpected store configuration name: %@"
+ "Unhandled NSPersistentCloudKitContainerEventType: %ld"
+ "User defaults returning incorrect class type - lastAttemptDate type: %@, countSinceLastAttempt type: %@ - resetting values and continuing to reassert"
+ "_acceptInvitationMessage:fromHandle:toHandle:messageGuid:existingChannel:databaseContext:"
+ "_discoverySource"
+ "_maxReassertions"
+ "_removeActivePresenceSubscriptionsForClient:"
+ "_removeActiveTransientSubscriptionsForClient:"
+ "_setupVoucher"
+ "_shouldAcceptInvitationMessageForPresenceIdentifier:fromHandle:fromMergeID:inServiceFirewall:databaseContext:completion:"
+ "addListenerID:forService:"
+ "assertionsSinceLastReassertTime"
+ "checking if we should reassert - currentTime: %@, lastAttempt: %@, countSinceLastAttempt: %ld, reassertResetTime: %f"
+ "com.apple.LocalStatusKit.deviceFound"
+ "com.apple.private.alloy.home"
+ "com.apple.rapport.matching"
+ "configurationName"
+ "currentEntries:"
+ "destinationURIs"
+ "discoverySource"
+ "endpoints"
+ "expireActivityVoucher:"
+ "handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:"
+ "homed"
+ "idInfoForDestinations:service:infoTypes:options:listenerID:queue:completionBlock:"
+ "idsURI"
+ "initWithIDSIdentifier:pendingStatuses:deliveredStatuses:discoverySource:"
+ "initWithLabel:forEventsOfType:withConfiguration:affectingObjectsMatching:"
+ "initWithService:queue:"
+ "isHandle:inFirewallForService:completion:"
+ "launchOnDemandTransaction"
+ "listOfValidSenderHandles:containsSenderMergeID:completion:"
+ "loadPersistentStore called asynchronously"
+ "marking reassert - currentTime: %@, lastAttempt: %@, countSinceLastAttempt: %ld, reassertResetTime: %f"
+ "reassert - resetting timer and setting assertion count to 0"
+ "reassert - updating reassertion count to count + 1"
+ "replyRequired"
+ "senderCorrelationIdentifier"
+ "service:didReceiveIncomingMessage:fromID:fromMergeID:toID:messageGuid:"
+ "setActivityVouchers:"
+ "setQualityOfService:"
+ "setSetupVoucher:"
+ "setSource:"
+ "setupVoucher"
+ "shared-channels-max-reassertion-count"
+ "source"
+ "uri"
+ "v16@?0@\"<OS_xpc_object>\"8"
+ "v40@0:8@\"NSSet\"16@\"NSString\"24@?<v@?B>32"
+ "v40@0:8@\"SKHandle\"16@\"NSString\"24@?<v@?B>32"
+ "v64@0:8@\"NSDictionary\"16@\"SKHandle\"24@\"NSString\"32@\"NSString\"40@\"SKHandle\"48@\"NSString\"56"
+ "v64@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56"
- "@\"NSPersistentContainer\""
- "Completed creation of persistent container"
- "Destroyed persistent store %@"
- "Division by zero"
- "Division results in an overflow"
- "Failed creation of persistent container"
- "Failed to Destroyed persistent store %@ -- %@"
- "Fatal error"
- "Fetch request for channel by identifier completed with %ld result(s)"
- "Fetch request for channel by identifier found no match."
- "Insufficient space allocated to copy string contents"
- "Invitation message missing date channel created. Using current server time"
- "Received incoming message: %@ fromID: %@"
- "Received publish device found without a browserTask. Ignorning"
- "Skipping status with missing IDS Device {idsIdentifier: %s}"
- "Skipping status with missing timestamp {idsIdentifier: %s, timestamps: %s}"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T@\"NSPersistentContainer\",&,N,V_persistentContainer"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:"
- "initWithManagedObjectModel:"
- "invalid Collection: less than 'count' elements in collection"
- "reconcileObservations skipping device with nil idsIdentifier {device: %@}"
- "reconcileObservations skipping device with no statuses {device: %@, deviceID: %s}"
- "service:didReceiveIncomingMessage:fromID:toID:messageGuid:"
- "v56@0:8@\"NSDictionary\"16@\"SKHandle\"24@\"NSString\"32@\"SKHandle\"40@\"NSString\"48"
- "v56@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48"

```
