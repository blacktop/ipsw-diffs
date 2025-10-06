## StatusKitAgentCore

> `/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore`

```diff

-25.300.51.0.0
-  __TEXT.__text: 0xa5f20
-  __TEXT.__auth_stubs: 0x1540
-  __TEXT.__objc_methlist: 0x561c
-  __TEXT.__const: 0x57c
-  __TEXT.__cstring: 0x409a
-  __TEXT.__oslogstring: 0xdfb9
-  __TEXT.__gcc_except_tab: 0xaf8
-  __TEXT.__swift5_typeref: 0x764
+25.500.131.0.0
+  __TEXT.__text: 0xa831c
+  __TEXT.__auth_stubs: 0x15a0
+  __TEXT.__objc_methlist: 0x563c
+  __TEXT.__const: 0x58c
+  __TEXT.__cstring: 0x439a
+  __TEXT.__oslogstring: 0xe0fd
+  __TEXT.__gcc_except_tab: 0xac0
+  __TEXT.__swift5_typeref: 0x78e
   __TEXT.__swift5_capture: 0x1d0
   __TEXT.__constg_swiftt: 0x128
   __TEXT.__swift5_reflstr: 0x25f

   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x209c
-  __TEXT.__eh_frame: 0x1388
-  __TEXT.__objc_classname: 0xc7f
-  __TEXT.__objc_methname: 0xea7c
-  __TEXT.__objc_methtype: 0x4109
-  __TEXT.__objc_stubs: 0x85e0
+  __TEXT.__unwind_info: 0x20d8
+  __TEXT.__eh_frame: 0x13a0
+  __TEXT.__objc_classname: 0xc81
+  __TEXT.__objc_methname: 0xec38
+  __TEXT.__objc_methtype: 0x412a
+  __TEXT.__objc_stubs: 0x8640
   __DATA_CONST.__got: 0x350
-  __DATA_CONST.__const: 0x17a8
+  __DATA_CONST.__const: 0x17d0
   __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xc630
-  __DATA_CONST.__objc_selrefs: 0x2b38
+  __DATA_CONST.__objc_const: 0xc680
+  __DATA_CONST.__objc_selrefs: 0x2b70
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_classrefs: 0x4b8
+  __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__cfstring: 0x20c0
   __AUTH_CONST.__const: 0x1078
   __AUTH_CONST.__objc_const: 0x1fa0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0xab0
-  __AUTH.__objc_data: 0xb38
-  __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x4b8
-  __DATA.__objc_superrefs: 0x1f0
-  __DATA.__objc_ivar: 0x524
+  __AUTH_CONST.__auth_got: 0xae0
+  __AUTH.__objc_data: 0xae8
+  __DATA.__objc_ivar: 0x528
   __DATA.__data: 0x1370
   __DATA.__bss: 0x4c0
-  __DATA_DIRTY.__objc_data: 0xe78
-  __DATA_DIRTY.__data: 0x2e0
+  __DATA_DIRTY.__objc_data: 0xec8
+  __DATA_DIRTY.__data: 0x2f0
   __DATA_DIRTY.__bss: 0x378
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2B48CDD1-DF60-311C-A510-0A825547BF76
-  Functions: 3320
-  Symbols:   8776
-  CStrings:  4017
+  UUID: 9FA51B4B-6B16-38BA-AC5A-A60B5B78703A
+  Functions: 3338
+  Symbols:   8796
+  CStrings:  4057
 
Symbols:
+ -[SKAPresenceClient lastSelfInviteSentTimestamp]
+ -[SKAPresenceClient setLastSelfInviteSentTimestamp:]
+ -[SKAPresenceManager sendPollingMessageForChannel:]
+ -[SKAStatusSubscriptionManager presenceSubscriptionsLock]
+ -[SKAStatusSubscriptionManager setPresenceSubscriptionsLock:]
+ -[SKAStatusSubscriptionManager setTransientSubscriptionsLock:]
+ -[SKAStatusSubscriptionManager transientSubscriptionsLock]
+ GCC_except_table15
+ GCC_except_table23
+ GCC_except_table27
+ GCC_except_table37
+ GCC_except_table55
+ GCC_except_table87
+ GCC_except_table92
+ _OBJC_IVAR_$_SKAPresenceClient._lastSelfInviteSentTimestamp
+ _OBJC_IVAR_$_SKAStatusSubscriptionManager._presenceSubscriptionsLock
+ _OBJC_IVAR_$_SKAStatusSubscriptionManager._transientSubscriptionsLock
+ ___132-[SKAStatusSubscriptionServiceClient retainTransientSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:completion:]_block_invoke.51
+ ___132-[SKAStatusSubscriptionServiceClient retainTransientSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:completion:]_block_invoke.51.cold.1
+ ___133-[SKAStatusSubscriptionServiceClient releaseTransientSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:completion:]_block_invoke.52
+ ___133-[SKAStatusSubscriptionServiceClient releaseTransientSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:completion:]_block_invoke.52.cold.1
+ ___155-[SKAStatusSubscriptionServiceClient retainPersistentSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:applicationIdentifier:completion:]_block_invoke.53
+ ___155-[SKAStatusSubscriptionServiceClient retainPersistentSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:applicationIdentifier:completion:]_block_invoke.53.cold.1
+ ___156-[SKAStatusSubscriptionServiceClient releasePersistentSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:applicationIdentifier:completion:]_block_invoke.54
+ ___156-[SKAStatusSubscriptionServiceClient releasePersistentSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:applicationIdentifier:completion:]_block_invoke.54.cold.1
+ ___51-[SKAPresenceManager sendPollingMessageForChannel:]_block_invoke
+ ___51-[SKAPresenceManager sendPollingMessageForChannel:]_block_invoke.cold.1
+ ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.91
+ ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.91.cold.1
+ ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.92
+ ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.92.cold.1
+ ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.93
+ ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.93.cold.1
+ ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.94
+ ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.94.cold.1
+ ___61-[SKAPresenceClient releasePresenceForIdentifier:completion:]_block_invoke.49
+ ___61-[SKAPresenceClient releasePresenceForIdentifier:completion:]_block_invoke.49.cold.1
+ ___63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke.27.cold.1
+ ___63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke.28
+ ___63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke_2.29
+ ___63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke_2.29.cold.1
+ ___67-[SKAPresenceClient handleReceivedInvitationForPresenceIdentifier:]_block_invoke.88
+ ___68-[SKAPresenceClient presentDevicesForPresenceIdentifier:completion:]_block_invoke.64
+ ___72-[SKAPresenceClient removeInvitedHandles:presenceIdentifier:completion:]_block_invoke.57
+ ___72-[SKAPresenceClient removeInvitedHandles:presenceIdentifier:completion:]_block_invoke.57.cold.1
+ ___77-[SKAPresenceClient handleReceivedPresentDevicesUpdateForPresenceIdentifier:]_block_invoke.81
+ ___77-[SKAPresenceClient handleReceivedPresentDevicesUpdateForPresenceIdentifier:]_block_invoke.83
+ ___80-[SKAPresenceClient assertPresenceForIdentifier:withPresencePayload:completion:]_block_invoke.40
+ ___80-[SKAPresenceManager presentDevicesForPresenceIdentifier:isPersonal:completion:]_block_invoke.39
+ ___82-[SKAPresenceClient inviteHandles:fromSenderHandle:presenceIdentifier:completion:]_block_invoke.52
+ ___82-[SKAPresenceClient inviteHandles:fromSenderHandle:presenceIdentifier:completion:]_block_invoke.52.cold.1
+ ___84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.34.cold.1
+ ___84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.35
+ ___84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke_2.36
+ ___84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke_2.36.cold.1
+ ___89-[SKAPresenceClient fetchHandleInvitability:fromHandle:forPresenceIdentifier:completion:]_block_invoke.50
+ ___90-[SKAPresenceClient retainTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.58
+ ___90-[SKAPresenceClient retainTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.58.cold.1
+ ___90-[SKAPresenceClient retainTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.59
+ ___90-[SKAPresenceClient retainTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.59.cold.1
+ ___90-[SKAPresenceManager releaseAllPresenceAssertionsAssociatedWithClient:options:completion:]_block_invoke.37
+ ___90-[SKAPresenceManager releaseAllPresenceAssertionsAssociatedWithClient:options:completion:]_block_invoke.37.cold.1
+ ___91-[SKAPresenceClient releaseTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.61
+ ___91-[SKAPresenceClient releaseTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.61.cold.1
+ ___91-[SKAPresenceClient releaseTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.62
+ ___91-[SKAPresenceClient releaseTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.62.cold.1
+ ___94-[SKAPresenceManager releasePresenceAssertionForPresenceIdentifier:options:client:completion:]_block_invoke.32
+ ___94-[SKAPresenceManager releasePresenceAssertionForPresenceIdentifier:options:client:completion:]_block_invoke.32.cold.1
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.80
+ ___block_literal_global.85
+ ___block_literal_global.87
+ ___block_literal_global.90
+ _block_copy_helper.143
+ _block_copy_helper.69
+ _block_copy_helper.76
+ _block_copy_helper.82
+ _block_copy_helper.89
+ _block_copy_helper.92
+ _block_descriptor.145
+ _block_descriptor.71
+ _block_descriptor.78
+ _block_descriptor.84
+ _block_descriptor.91
+ _block_descriptor.94
+ _block_destroy_helper.144
+ _block_destroy_helper.70
+ _block_destroy_helper.77
+ _block_destroy_helper.83
+ _block_destroy_helper.90
+ _block_destroy_helper.93
+ _free
+ _get_witness_table SeRzSERzl10Foundation4DataVSEHPyHC.108
+ _get_witness_table SeRzSERzl10Foundation4DataVSeHPyHC.107
+ _malloc
+ _objc_msgSend$lastSelfInviteSentTimestamp
+ _objc_msgSend$sendPollingMessageForChannel:
+ _objc_msgSend$setLastSelfInviteSentTimestamp:
+ _objectdestroy.103Tm
+ _objectdestroy.111Tm
+ _objectdestroy.141Tm
+ _symbolic SaySo31SKADatabasePublishedLocalStatusCG
- -[SKAStatusPublishingServiceClient setTransaction:]
- -[SKAStatusPublishingServiceClient transaction]
- -[SKAStatusSubscriptionServiceClient setTransaction:]
- -[SKAStatusSubscriptionServiceClient transaction]
- GCC_except_table21
- GCC_except_table85
- GCC_except_table90
- _OBJC_IVAR_$_SKAStatusPublishingServiceClient._transaction
- _OBJC_IVAR_$_SKAStatusSubscriptionServiceClient._transaction
- ___132-[SKAStatusSubscriptionServiceClient retainTransientSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:completion:]_block_invoke.54
- ___132-[SKAStatusSubscriptionServiceClient retainTransientSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:completion:]_block_invoke.54.cold.1
- ___133-[SKAStatusSubscriptionServiceClient releaseTransientSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:completion:]_block_invoke.55
- ___133-[SKAStatusSubscriptionServiceClient releaseTransientSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:completion:]_block_invoke.55.cold.1
- ___155-[SKAStatusSubscriptionServiceClient retainPersistentSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:applicationIdentifier:completion:]_block_invoke.56
- ___155-[SKAStatusSubscriptionServiceClient retainPersistentSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:applicationIdentifier:completion:]_block_invoke.56.cold.1
- ___156-[SKAStatusSubscriptionServiceClient releasePersistentSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:applicationIdentifier:completion:]_block_invoke.57
- ___156-[SKAStatusSubscriptionServiceClient releasePersistentSubscriptionAssertionForSubscriptionIdentifier:statusTypeIdentifier:applicationIdentifier:completion:]_block_invoke.57.cold.1
- ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.83
- ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.83.cold.1
- ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.84
- ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.84.cold.1
- ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.85
- ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.85.cold.1
- ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.86
- ___60-[SKAPresenceClient refreshAssertionsForPresenceIdentifier:]_block_invoke.86.cold.1
- ___61-[SKAPresenceClient releasePresenceForIdentifier:completion:]_block_invoke.40
- ___61-[SKAPresenceClient releasePresenceForIdentifier:completion:]_block_invoke.40.cold.1
- ___63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke.26
- ___63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke.26.cold.1
- ___63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke_2.28
- ___63-[SKAPresenceManager _sendPollingMessageForChannel:completion:]_block_invoke_2.28.cold.1
- ___67-[SKAPresenceClient handleReceivedInvitationForPresenceIdentifier:]_block_invoke.80
- ___68-[SKAPresenceClient presentDevicesForPresenceIdentifier:completion:]_block_invoke.56
- ___72-[SKAPresenceClient removeInvitedHandles:presenceIdentifier:completion:]_block_invoke.49
- ___72-[SKAPresenceClient removeInvitedHandles:presenceIdentifier:completion:]_block_invoke.49.cold.1
- ___77-[SKAPresenceClient handleReceivedPresentDevicesUpdateForPresenceIdentifier:]_block_invoke.73
- ___77-[SKAPresenceClient handleReceivedPresentDevicesUpdateForPresenceIdentifier:]_block_invoke.75
- ___80-[SKAPresenceManager presentDevicesForPresenceIdentifier:isPersonal:completion:]_block_invoke.38
- ___82-[SKAPresenceClient inviteHandles:fromSenderHandle:presenceIdentifier:completion:]_block_invoke.43
- ___82-[SKAPresenceClient inviteHandles:fromSenderHandle:presenceIdentifier:completion:]_block_invoke.43.cold.1
- ___84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.33
- ___84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke.33.cold.1
- ___84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke_2.35
- ___84-[SKAPresenceManager _sendPresenceDeactivationMessageForChannel:options:completion:]_block_invoke_2.35.cold.1
- ___89-[SKAPresenceClient fetchHandleInvitability:fromHandle:forPresenceIdentifier:completion:]_block_invoke.41
- ___90-[SKAPresenceClient retainTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.50
- ___90-[SKAPresenceClient retainTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.50.cold.1
- ___90-[SKAPresenceClient retainTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.51
- ___90-[SKAPresenceClient retainTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.51.cold.1
- ___90-[SKAPresenceManager releaseAllPresenceAssertionsAssociatedWithClient:options:completion:]_block_invoke.36
- ___90-[SKAPresenceManager releaseAllPresenceAssertionsAssociatedWithClient:options:completion:]_block_invoke.36.cold.1
- ___91-[SKAPresenceClient releaseTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.53
- ___91-[SKAPresenceClient releaseTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.53.cold.1
- ___91-[SKAPresenceClient releaseTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.54
- ___91-[SKAPresenceClient releaseTransientSubscriptionAssertionForPresenceIdentifier:completion:]_block_invoke.54.cold.1
- ___94-[SKAPresenceManager releasePresenceAssertionForPresenceIdentifier:options:client:completion:]_block_invoke.30
- ___94-[SKAPresenceManager releasePresenceAssertionForPresenceIdentifier:options:client:completion:]_block_invoke.31.cold.1
- ___block_literal_global.72
- ___block_literal_global.77
- ___block_literal_global.79
- ___block_literal_global.82
- _block_copy_helper.144
- _block_copy_helper.70
- _block_copy_helper.77
- _block_copy_helper.83
- _block_copy_helper.90
- _block_copy_helper.93
- _block_descriptor.146
- _block_descriptor.73
- _block_descriptor.79
- _block_descriptor.85
- _block_descriptor.92
- _block_descriptor.95
- _block_destroy_helper.145
- _block_destroy_helper.71
- _block_destroy_helper.78
- _block_destroy_helper.84
- _block_destroy_helper.91
- _block_destroy_helper.94
- _get_witness_table SeRzSERzl10Foundation4DataVSEHPyHC.109
- _get_witness_table SeRzSERzl10Foundation4DataVSeHPyHC.108
- _objectdestroy.104Tm
- _objectdestroy.112Tm
- _objectdestroy.142Tm
CStrings:
+ "\x12\x14"
+ "\x12\x17"
+ "1"
+ "Division by zero"
+ "Division results in an overflow"
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "NO"
+ "Not sending self invitation for personal channel with presenceIdentifier: %@ as last self invite was sent at %f"
+ "Polling for channel: %@"
+ "Polling for current state as there is no active assertion"
+ "Sending self invitation for personal channel with presenceIdentifier: %@"
+ "Sent self invites for personal channel %@, with error %@"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "Td,N,V_lastSelfInviteSentTimestamp"
+ "T{os_unfair_lock_s=I},N,V_presenceSubscriptionsLock"
+ "T{os_unfair_lock_s=I},N,V_transientSubscriptionsLock"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "YES"
+ "_lastSelfInviteSentTimestamp"
+ "_presenceSubscriptionsLock"
+ "_transientSubscriptionsLock"
+ "invalid Collection: less than 'count' elements in collection"
+ "lastSelfInviteSentTimestamp"
+ "presenceSubscriptionsLock"
+ "sendPollingMessageForChannel:"
+ "setLastSelfInviteSentTimestamp:"
+ "setPresenceSubscriptionsLock:"
+ "setTransientSubscriptionsLock:"
+ "transientSubscriptionsLock"
+ "v24@0:8@\"SKADatabaseChannel\"16"
- "\x13\x14"
- "\x13\x17"
- "com.apple.statuskit.publishing.%@"
- "com.apple.statuskit.subscription.%@"

```
