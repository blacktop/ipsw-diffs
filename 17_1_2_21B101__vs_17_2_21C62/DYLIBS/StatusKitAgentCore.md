## StatusKitAgentCore

> `/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore`

```diff

-25.200.71.2.2
-  __TEXT.__text: 0xa5368
+25.300.51.0.0
+  __TEXT.__text: 0xa5f20
   __TEXT.__auth_stubs: 0x1540
-  __TEXT.__objc_methlist: 0x55b4
+  __TEXT.__objc_methlist: 0x561c
   __TEXT.__const: 0x57c
-  __TEXT.__cstring: 0x400a
-  __TEXT.__oslogstring: 0xdef0
-  __TEXT.__gcc_except_tab: 0xaa8
+  __TEXT.__cstring: 0x409a
+  __TEXT.__oslogstring: 0xdfb9
+  __TEXT.__gcc_except_tab: 0xaf8
   __TEXT.__swift5_typeref: 0x764
   __TEXT.__swift5_capture: 0x1d0
   __TEXT.__constg_swiftt: 0x128

   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x205c
+  __TEXT.__unwind_info: 0x209c
   __TEXT.__eh_frame: 0x1388
-  __TEXT.__objc_classname: 0xc72
-  __TEXT.__objc_methname: 0xe9f2
-  __TEXT.__objc_methtype: 0x40ea
-  __TEXT.__objc_stubs: 0x8580
+  __TEXT.__objc_classname: 0xc7f
+  __TEXT.__objc_methname: 0xea7c
+  __TEXT.__objc_methtype: 0x4109
+  __TEXT.__objc_stubs: 0x85e0
   __DATA_CONST.__got: 0x350
   __DATA_CONST.__const: 0x17a8
-  __DATA_CONST.__objc_classlist: 0x268
+  __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xc558
-  __DATA_CONST.__objc_selrefs: 0x2b28
+  __DATA_CONST.__objc_const: 0xc630
+  __DATA_CONST.__objc_selrefs: 0x2b38
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__cfstring: 0x2040
-  __AUTH_CONST.__const: 0x1058
-  __AUTH_CONST.__objc_const: 0x1f58
+  __AUTH_CONST.__cfstring: 0x20c0
+  __AUTH_CONST.__const: 0x1078
+  __AUTH_CONST.__objc_const: 0x1fa0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0xab0
-  __AUTH.__objc_data: 0xae8
+  __AUTH.__objc_data: 0xb38
   __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x4b0
+  __DATA.__objc_classrefs: 0x4b8
   __DATA.__objc_superrefs: 0x1f0
-  __DATA.__objc_ivar: 0x518
+  __DATA.__objc_ivar: 0x524
   __DATA.__data: 0x1370
   __DATA.__bss: 0x4c0
   __DATA_DIRTY.__objc_data: 0xe78
   __DATA_DIRTY.__data: 0x2e0
-  __DATA_DIRTY.__bss: 0x368
+  __DATA_DIRTY.__bss: 0x378
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3D70533D-4FDD-3D7F-B2C7-8131AF96ABB8
-  Functions: 3304
-  Symbols:   8730
-  CStrings:  3997
+  UUID: F89615A1-C22F-357A-BEB2-701FBC2B3E88
+  Functions: 3320
+  Symbols:   8776
+  CStrings:  4017
 
Symbols:
+ +[SKAServerBag logger]
+ +[SKAServerBag presenceEnabledByServerForServiceIdentifier:]
+ +[SKAServerBag presenceEnabledByServer]
+ -[SKAInvitationManager sendInvitationForPresenceChannelWithPresenceIdentifier:toHandles:fromSenderHandle:options:completion:].cold.4
+ -[SKAPresenceClient setTransaction:]
+ -[SKAPresenceClient transaction]
+ -[SKAStatusPublishingServiceClient setTransaction:]
+ -[SKAStatusPublishingServiceClient transaction]
+ -[SKAStatusSubscriptionServiceClient setTransaction:]
+ -[SKAStatusSubscriptionServiceClient transaction]
+ _OBJC_CLASS_$_SKAServerBag
+ _OBJC_IVAR_$_SKAPresenceClient._transaction
+ _OBJC_IVAR_$_SKAStatusPublishingServiceClient._transaction
+ _OBJC_IVAR_$_SKAStatusSubscriptionServiceClient._transaction
+ _OBJC_METACLASS_$_SKAServerBag
+ _OUTLINED_FUNCTION_13
+ __OBJC_$_CLASS_METHODS_SKAServerBag
+ __OBJC_CLASS_RO_$_SKAServerBag
+ __OBJC_METACLASS_RO_$_SKAServerBag
+ ___100-[SKAPresenceManager createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.45
+ ___100-[SKAPresenceManager createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.45.cold.1
+ ___100-[SKAPresenceManager createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.cold.2
+ ___101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.61.cold.1
+ ___101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.62
+ ___101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke_2.63
+ ___101-[SKAPresenceManager findPresenceChannelForPresenceIdentifier:isPersonal:databaseContext:completion:]_block_invoke.44
+ ___103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke.20.cold.1
+ ___103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke.21
+ ___103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke_2.22
+ ___103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke_2.22.cold.1
+ ___106-[SKAPresenceManager findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.43
+ ___106-[SKAPresenceManager findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.cold.2
+ ___107-[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.60
+ ___113-[SKAPresenceManager retainPresenceAssertionForPresenceIdentifier:withPresencePayload:options:client:completion:]_block_invoke.13
+ ___113-[SKAPresenceManager retainPresenceAssertionForPresenceIdentifier:withPresencePayload:options:client:completion:]_block_invoke.cold.3
+ ___132-[SKAStatusSubscriptionServiceClient retainTransientSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:completion:]_block_invoke.54
+ ___132-[SKAStatusSubscriptionServiceClient retainTransientSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:completion:]_block_invoke.54.cold.1
+ ___133-[SKAStatusSubscriptionServiceClient releaseTransientSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:completion:]_block_invoke.55
+ ___133-[SKAStatusSubscriptionServiceClient releaseTransientSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:completion:]_block_invoke.55.cold.1
+ ___155-[SKAStatusSubscriptionServiceClient retainPersistentSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:applicationIdentifier:completion:]_block_invoke.56
+ ___155-[SKAStatusSubscriptionServiceClient retainPersistentSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:applicationIdentifier:completion:]_block_invoke.56.cold.1
+ ___156-[SKAStatusSubscriptionServiceClient releasePersistentSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:applicationIdentifier:completion:]_block_invoke.57
+ ___156-[SKAStatusSubscriptionServiceClient releasePersistentSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:applicationIdentifier:completion:]_block_invoke.57.cold.1
+ ___22+[SKAServerBag logger]_block_invoke
+ ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.84
+ ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.84.cold.1
+ ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.85
+ ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.85.cold.1
+ ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.86
+ ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.86.cold.1
+ ___63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke.26.cold.1
+ ___63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke.27
+ ___63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke_2.28
+ ___63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke_2.28.cold.1
+ ___67-[SKAPresenceClient handleReceivedInvitationForPresenceIdentifier:]_block_invoke.80
+ ___68-[SKAPresenceClient presentDevicesForPresenceIdentifier:completion:]_block_invoke.56
+ ___72-[SKAPresenceClient removeInvitedHandles:presenceIdentifier:completion:]_block_invoke.49
+ ___72-[SKAPresenceClient removeInvitedHandles:presenceIdentifier:completion:]_block_invoke.49.cold.1
+ ___77-[SKAPresenceClient handleReceivedPresentDevicesUpdateForPresenceIdentifier:]_block_invoke.73
+ ___77-[SKAPresenceClient handleReceivedPresentDevicesUpdateForPresenceIdentifier:]_block_invoke.75
+ ___80-[SKAPresenceManager presentDevicesForPresenceIdentifier:isPersonal:completion:]_block_invoke.38
+ ___84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.33.cold.1
+ ___84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.34
+ ___84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke_2.35
+ ___84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke_2.35.cold.1
+ ___90-[SKAPresenceClient retainTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.50
+ ___90-[SKAPresenceClient retainTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.50.cold.1
+ ___90-[SKAPresenceClient retainTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.51
+ ___90-[SKAPresenceClient retainTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.51.cold.1
+ ___90-[SKAPresenceManager releaseAllPresenceAssertionsAssociatedWithClient:options:completion:]_block_invoke.36
+ ___90-[SKAPresenceManager releaseAllPresenceAssertionsAssociatedWithClient:options:completion:]_block_invoke.36.cold.1
+ ___90-[SKAPresenceManager releaseAllPresenceAssertionsAssociatedWithClient:options:completion:]_block_invoke.cold.2
+ ___91-[SKAPresenceClient releaseTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.53
+ ___91-[SKAPresenceClient releaseTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.53.cold.1
+ ___91-[SKAPresenceClient releaseTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.54
+ ___91-[SKAPresenceClient releaseTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.54.cold.1
+ ___94-[SKAPresenceManager releasePresenceAssertionForPresenceIdentifier:options:client:completion:]_block_invoke.31
+ ___94-[SKAPresenceManager releasePresenceAssertionForPresenceIdentifier:options:client:completion:]_block_invoke.31.cold.1
+ ___97-[SKAInvitationManager _createPersonalChannelForStatusTypeIdentifier:databaseContext:completion:]_block_invoke.81.cold.1
+ ___97-[SKAInvitationManager _createPersonalChannelForStatusTypeIdentifier:databaseContext:completion:]_block_invoke.82
+ ___block_literal_global.115
+ ___block_literal_global.72
+ ___block_literal_global.77
+ ___block_literal_global.82
+ _objc_msgSend$description
+ _objc_msgSend$presenceEnabledByServerForServiceIdentifier:
+ _objc_msgSend$setTransaction:
+ _objc_msgSend$transaction
- -[SKAInvitationManager _presenceEnabledByServer]
- -[SKAPresenceManager _presenceEnabledByServer]
- ___100-[SKAPresenceManager createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.44
- ___100-[SKAPresenceManager createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.44.cold.1
- ___101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.60
- ___101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.60.cold.1
- ___101-[SKAPresenceManager _createPresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke_2.62
- ___101-[SKAPresenceManager findPresenceChannelForPresenceIdentifier:isPersonal:databaseContext:completion:]_block_invoke.43
- ___103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke.18
- ___103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke.19.cold.1
- ___103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke_2.21
- ___103-[SKAPresenceManager _sendPresenceAssertionMessageForChannel:withPayload:options:isRefresh:completion:]_block_invoke_2.21.cold.1
- ___106-[SKAPresenceManager findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.42
- ___107-[SKAPresenceManager _findOrCreatePresenceChannelForPresenceIdentifier:options:databaseContext:completion:]_block_invoke.55
- ___113-[SKAPresenceManager retainPresenceAssertionForPresenceIdentifier:withPresencePayload:options:client:completion:]_block_invoke.11
- ___132-[SKAStatusSubscriptionServiceClient retainTransientSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:completion:]_block_invoke.51
- ___132-[SKAStatusSubscriptionServiceClient retainTransientSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:completion:]_block_invoke.51.cold.1
- ___133-[SKAStatusSubscriptionServiceClient releaseTransientSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:completion:]_block_invoke.52
- ___133-[SKAStatusSubscriptionServiceClient releaseTransientSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:completion:]_block_invoke.52.cold.1
- ___155-[SKAStatusSubscriptionServiceClient retainPersistentSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:applicationIdentifier:completion:]_block_invoke.53
- ___155-[SKAStatusSubscriptionServiceClient retainPersistentSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:applicationIdentifier:completion:]_block_invoke.53.cold.1
- ___156-[SKAStatusSubscriptionServiceClient releasePersistentSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:applicationIdentifier:completion:]_block_invoke.54
- ___156-[SKAStatusSubscriptionServiceClient releasePersistentSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:applicationIdentifier:completion:]_block_invoke.54.cold.1
- ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.80
- ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.80.cold.1
- ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.81
- ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.81.cold.1
- ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.82
- ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.82.cold.1
- ___63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke.25
- ___63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke.25.cold.1
- ___63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke_2.27
- ___63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke_2.27.cold.1
- ___67-[SKAPresenceClient handleReceivedInvitationForPresenceIdentifier:]_block_invoke.77
- ___68-[SKAPresenceClient presentDevicesForPresenceIdentifier:completion:]_block_invoke.53
- ___72-[SKAPresenceClient removeInvitedHandles:presenceIdentifier:completion:]_block_invoke.46
- ___72-[SKAPresenceClient removeInvitedHandles:presenceIdentifier:completion:]_block_invoke.46.cold.1
- ___77-[SKAPresenceClient handleReceivedPresentDevicesUpdateForPresenceIdentifier:]_block_invoke.70
- ___77-[SKAPresenceClient handleReceivedPresentDevicesUpdateForPresenceIdentifier:]_block_invoke.72
- ___80-[SKAPresenceManager presentDevicesForPresenceIdentifier:isPersonal:completion:]_block_invoke.37
- ___84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.32
- ___84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.32.cold.1
- ___84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke_2.34
- ___84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke_2.34.cold.1
- ___90-[SKAPresenceClient retainTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.47
- ___90-[SKAPresenceClient retainTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.47.cold.1
- ___90-[SKAPresenceClient retainTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.48
- ___90-[SKAPresenceClient retainTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.48.cold.1
- ___90-[SKAPresenceManager releaseAllPresenceAssertionsAssociatedWithClient:options:completion:]_block_invoke.35
- ___90-[SKAPresenceManager releaseAllPresenceAssertionsAssociatedWithClient:options:completion:]_block_invoke.35.cold.1
- ___91-[SKAPresenceClient releaseTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.50
- ___91-[SKAPresenceClient releaseTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.50.cold.1
- ___91-[SKAPresenceClient releaseTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.51
- ___91-[SKAPresenceClient releaseTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.51.cold.1
- ___94-[SKAPresenceManager releasePresenceAssertionForPresenceIdentifier:options:client:completion:]_block_invoke.29
- ___94-[SKAPresenceManager releasePresenceAssertionForPresenceIdentifier:options:client:completion:]_block_invoke.30.cold.1
- ___97-[SKAInvitationManager _createPersonalChannelForStatusTypeIdentifier:databaseContext:completion:]_block_invoke.80
- ___97-[SKAInvitationManager _createPersonalChannelForStatusTypeIdentifier:databaseContext:completion:]_block_invoke.80.cold.1
- ___block_literal_global.117
- ___block_literal_global.69
- ___block_literal_global.74
- ___block_literal_global.76
- _objc_msgSend$_presenceEnabledByServer
CStrings:
+ "\x13\x14"
+ "\x13\x17"
+ "\x13\x19"
+ "@\"NSObject<OS_os_transaction>\""
+ "A"
+ "Presence has been disabled by the server for identifier %@."
+ "SKAServerBag"
+ "SKATransaction: Completed transaction %@"
+ "SKATransaction: Creating transaction {%@}"
+ "Server bag indicates presence disablement for service: %@"
+ "T@\"NSObject<OS_os_transaction>\",&,N,V_transaction"
+ "_transaction"
+ "activity-presence-adopter-disabled"
+ "com.apple.statuskit.presence.%@"
+ "com.apple.statuskit.publishing.%@"
+ "com.apple.statuskit.subscription.%@"
+ "presenceEnabledByServerForServiceIdentifier:"
+ "setTransaction:"
+ "transaction"
- "\x12\x14"
- "\x12\x17"
- "\x12\x19"
- "1"

```
