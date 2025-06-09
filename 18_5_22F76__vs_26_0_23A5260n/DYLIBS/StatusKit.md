## StatusKit

> `/System/Library/PrivateFrameworks/StatusKit.framework/StatusKit`

```diff

-80.600.1.0.0
-  __TEXT.__text: 0x17fb4
-  __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_methlist: 0x1838
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0xc81
-  __TEXT.__oslogstring: 0x3aec
-  __TEXT.__gcc_except_tab: 0xb64
-  __TEXT.__unwind_info: 0x780
-  __TEXT.__objc_classname: 0x386
-  __TEXT.__objc_methname: 0x3b1c
-  __TEXT.__objc_methtype: 0xbbf
-  __TEXT.__objc_stubs: 0x1ba0
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x6a8
-  __DATA_CONST.__objc_classlist: 0xa8
+109.100.1.0.0
+  __TEXT.__text: 0x19f88
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_methlist: 0x1a28
+  __TEXT.__const: 0xa8
+  __TEXT.__gcc_except_tab: 0xbe0
+  __TEXT.__cstring: 0xfe0
+  __TEXT.__oslogstring: 0x3f4a
+  __TEXT.__unwind_info: 0x838
+  __TEXT.__objc_classname: 0x3c2
+  __TEXT.__objc_methname: 0x3f58
+  __TEXT.__objc_methtype: 0xc28
+  __TEXT.__objc_stubs: 0x1f80
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__const: 0x748
+  __DATA_CONST.__objc_classlist: 0xb8
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa90
+  __DATA_CONST.__objc_selrefs: 0xbc0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x270
-  __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x820
-  __AUTH_CONST.__objc_const: 0x3ae0
-  __DATA.__objc_ivar: 0x148
+  __DATA_CONST.__objc_superrefs: 0xb8
+  __DATA_CONST.__objc_arraydata: 0x60
+  __AUTH_CONST.__auth_got: 0x290
+  __AUTH_CONST.__const: 0x320
+  __AUTH_CONST.__cfstring: 0xbe0
+  __AUTH_CONST.__objc_const: 0x2790
+  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x15c
   __DATA.__data: 0x4e0
-  __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x690
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA_DIRTY.__objc_data: 0x6e0
+  __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E88EE08E-D0B2-349B-9ABD-EC5019859017
-  Functions: 651
-  Symbols:   2273
-  CStrings:  994
+  UUID: 7966CA54-F666-3472-A06D-842B5C2FBCCC
+  Functions: 714
+  Symbols:   2370
+  CStrings:  1133
 
Symbols:
+ +[NSString(StatusKitAgent) descriptionFromSKUpdatePriority:]
+ +[SKPresence clientID]
+ +[SKPresence clientPrefixedPresenceIdentifierForPresenceIdentifier:]
+ +[SKPresenceAssertionOptions supportsSecureCoding]
+ -[NSString(StatusKitAgent) clientIDFromPresenceIdentifier]
+ -[NSString(StatusKitAgent) ska_appearsToBeEmail]
+ -[NSString(StatusKitAgent) ska_sha256Hash]
+ -[SKPresence _handleStatusKitAgentAliveNotification:]
+ -[SKPresence _handleStatusKitAgentAliveNotification:].cold.1
+ -[SKPresence _reestablishDaemonConnection]
+ -[SKPresence _reretainTransientSubscriptionWithCompletion:]
+ -[SKPresence assertPresenceWithPresencePayload:assertionOptions:completion:]
+ -[SKPresence dealloc]
+ -[SKPresence initWithPresenceIdentifier:options:].cold.2
+ -[SKPresence presenceAssertionOptions]
+ -[SKPresence rollChannelWithCompletion:]
+ -[SKPresence setPresenceAssertionOptions:]
+ -[SKPresenceAssertionOptions copyWithZone:]
+ -[SKPresenceAssertionOptions description]
+ -[SKPresenceAssertionOptions encodeWithCoder:]
+ -[SKPresenceAssertionOptions hash]
+ -[SKPresenceAssertionOptions initWithCoder:]
+ -[SKPresenceAssertionOptions initWithPriority:]
+ -[SKPresenceAssertionOptions isEqual:]
+ -[SKPresenceAssertionOptions priority]
+ -[SKPresenceAssertionOptions setPriority:]
+ -[SKPresenceOptions copyWithZone:]
+ -[SKPresenceOptions isDaemonIdleExitEnabled]
+ -[SKPresenceOptions setIsDaemonIdleExitEnabled:]
+ -[SKStatusPublishingDaemonConnection _resetConnectionHandlers]
+ -[SKStatusPublishingDaemonConnection invalidate]
+ -[SKStatusPublishingDaemonConnection lock]
+ -[SKStatusPublishingDaemonConnection setLock:]
+ -[SKStatusPublishingService dealloc]
+ -[SKStatusSubscriptionDaemonConnection _resetConnectionHandlers]
+ -[SKStatusSubscriptionDaemonConnection invalidate]
+ -[SKStatusSubscriptionService dealloc]
+ -[SKWeakObjectProxy .cxx_destruct]
+ -[SKWeakObjectProxy forwardInvocation:]
+ -[SKWeakObjectProxy forwardingTargetForSelector:]
+ -[SKWeakObjectProxy initWithForwardingTarget:]
+ -[SKWeakObjectProxy methodSignatureForSelector:]
+ -[SKWeakObjectProxy respondsToSelector:]
+ -[SKWeakObjectProxy target]
+ GCC_except_table13
+ GCC_except_table16
+ GCC_except_table19
+ GCC_except_table22
+ GCC_except_table36
+ GCC_except_table43
+ GCC_except_table46
+ GCC_except_table5
+ GCC_except_table55
+ GCC_except_table56
+ GCC_except_table67
+ GCC_except_table80
+ GCC_except_table90
+ GCC_except_table93
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSDistributedNotificationCenter
+ _OBJC_CLASS_$_NSMutableCharacterSet
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_SKPresenceAssertionOptions
+ _OBJC_CLASS_$_SKWeakObjectProxy
+ _OBJC_IVAR_$_SKPresence._presenceAssertionOptions
+ _OBJC_IVAR_$_SKPresenceAssertionOptions._priority
+ _OBJC_IVAR_$_SKPresenceOptions._isDaemonIdleExitEnabled
+ _OBJC_IVAR_$_SKStatusPublishingDaemonConnection._lock
+ _OBJC_IVAR_$_SKWeakObjectProxy._target
+ _OBJC_METACLASS_$_SKPresenceAssertionOptions
+ _OBJC_METACLASS_$_SKWeakObjectProxy
+ _SKStatusKitErrorDomain
+ _StringFromSKStatusKitErrorCode
+ _ValidateClientIsInAllowlistForServiceName
+ _ValidateClientIsInAllowlistForServiceName.cold.1
+ _ValidateClientIsInAllowlistForServiceName.cold.2
+ _ValidateClientIsInAllowlistForServiceName.cold.3
+ _ValidateClientIsInAllowlistForServiceName.presenceClients
+ _ValidateClientIsInAllowlistForServiceName.presenceClientsToken
+ _ValidateClientIsInAllowlistForServiceName.statusClients
+ _ValidateClientIsInAllowlistForServiceName.statusClientsToken
+ _ValidateIdentifierMeetsBlastdoorRequirements
+ _ValidateIdentifierMeetsBlastdoorRequirements.cold.1
+ _ValidateIdentifierMeetsBlastdoorRequirements.cold.2
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSString_$_StatusKitAgent
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSString_$_StatusKitAgent
+ __OBJC_$_CATEGORY_NSString_$_StatusKitAgent
+ __OBJC_$_CLASS_METHODS_SKPresenceAssertionOptions
+ __OBJC_$_CLASS_PROP_LIST_SKPresenceAssertionOptions
+ __OBJC_$_INSTANCE_METHODS_SKPresenceAssertionOptions
+ __OBJC_$_INSTANCE_METHODS_SKWeakObjectProxy
+ __OBJC_$_INSTANCE_VARIABLES_SKPresenceAssertionOptions
+ __OBJC_$_INSTANCE_VARIABLES_SKWeakObjectProxy
+ __OBJC_$_PROP_LIST_NSString_$_StatusKitAgent
+ __OBJC_$_PROP_LIST_SKPresenceAssertionOptions
+ __OBJC_$_PROP_LIST_SKWeakObjectProxy
+ __OBJC_CLASS_PROTOCOLS_$_SKPresenceAssertionOptions
+ __OBJC_CLASS_RO_$_SKPresenceAssertionOptions
+ __OBJC_CLASS_RO_$_SKWeakObjectProxy
+ __OBJC_METACLASS_RO_$_SKPresenceAssertionOptions
+ __OBJC_METACLASS_RO_$_SKWeakObjectProxy
+ ___123-[SKStatusSubscriptionService validatePersonalStatusSubscriptionMatchesSubscriptionValidationTokens:fromSender:completion:]_block_invoke.19.cold.4
+ ___28-[SKPresence invitedHandles]_block_invoke.45
+ ___28-[SKPresence presentDevices]_block_invoke.43
+ ___38-[SKPresence fetchPresenceCapability:]_block_invoke.56
+ ___40-[SKPresence rollChannelWithCompletion:]_block_invoke
+ ___40-[SKPresence rollChannelWithCompletion:]_block_invoke.55
+ ___40-[SKPresence rollChannelWithCompletion:]_block_invoke.55.cold.1
+ ___40-[SKPresence rollChannelWithCompletion:]_block_invoke.cold.1
+ ___43-[SKPresenceDaemonConnection xpcConnection]_block_invoke.7
+ ___44-[SKPresence releasePresenceWithCompletion:]_block_invoke.40
+ ___44-[SKPresence releasePresenceWithCompletion:]_block_invoke.40.cold.1
+ ___46-[SKPresence removeInvitedHandles:completion:]_block_invoke.54
+ ___46-[SKPresence removeInvitedHandles:completion:]_block_invoke.54.cold.1
+ ___48-[SKPresence _isHandleInvited:fromSenderHandle:]_block_invoke.46
+ ___51-[SKStatusPublishingDaemonConnection xpcConnection]_block_invoke.7
+ ___52-[SKPresence presenceDaemonConnectionDidDisconnect:]_block_invoke.cold.1
+ ___53-[SKStatusSubscriptionDaemonConnection xpcConnection]_block_invoke.7
+ ___54-[SKPresence _registerForDelegateCallbacksIfNecessary]_block_invoke.59
+ ___54-[SKPresence _registerForDelegateCallbacksIfNecessary]_block_invoke.59.cold.1
+ ___57-[SKPresence _inviteHandles:fromSenderHandle:completion:]_block_invoke.53
+ ___57-[SKPresence _inviteHandles:fromSenderHandle:completion:]_block_invoke.53.cold.1
+ ___58-[SKPresence initialCloudKitImportReceivedWithCompletion:]_block_invoke.74
+ ___59-[SKPresence _isHandleInvited:fromSenderHandle:completion:]_block_invoke.48
+ ___59-[SKPresence _reretainTransientSubscriptionWithCompletion:]_block_invoke
+ ___59-[SKPresence _reretainTransientSubscriptionWithCompletion:]_block_invoke_2
+ ___61-[SKPresence hasInitialCloudKitImportOccurredWithCompletion:]_block_invoke.30
+ ___61-[SKPresence hasInitialCloudKitImportOccurredWithCompletion:]_block_invoke.30.cold.1
+ ___65-[SKPresence retainTransientSubscriptionAssertionWithCompletion:]_block_invoke.41
+ ___65-[SKPresence retainTransientSubscriptionAssertionWithCompletion:]_block_invoke.41.cold.1
+ ___66-[SKPresence releaseTransientSubscriptionAssertionWithCompletion:]_block_invoke.42
+ ___66-[SKPresence releaseTransientSubscriptionAssertionWithCompletion:]_block_invoke.42.cold.1
+ ___67-[SKPresence _fetchHandleInvitability:fromSenderHandle:completion:]_block_invoke.50
+ ___68-[SKPresence invitedHandlesChangedForPresenceIdentifier:completion:]_block_invoke.69
+ ___68-[SKPresence presentHandlesChangedForPresenceIdentifier:completion:]_block_invoke.66
+ ___73-[SKStatusSubscriptionService subscriptionInvitationReceived:completion:]_block_invoke.37
+ ___75-[SKStatusSubscriptionService subscriptionReceivedStatusUpdate:completion:]_block_invoke.34
+ ___76-[SKPresence assertPresenceWithPresencePayload:assertionOptions:completion:]_block_invoke
+ ___76-[SKPresence assertPresenceWithPresencePayload:assertionOptions:completion:]_block_invoke.39
+ ___76-[SKPresence assertPresenceWithPresencePayload:assertionOptions:completion:]_block_invoke.39.cold.1
+ ___76-[SKPresence assertPresenceWithPresencePayload:assertionOptions:completion:]_block_invoke.cold.1
+ ___83-[SKStatusSubscriptionService subscriptionStateChangedForSubscriptions:completion:]_block_invoke.30
+ ___ValidateClientIsInAllowlistForServiceName_block_invoke
+ ___ValidateClientIsInAllowlistForServiceName_block_invoke_2
+ ___block_descriptor_32_e8_v12?0B8l
+ ___block_descriptor_40_e8_32w_e8_v12?0B8lw32l8
+ ___block_descriptor_48_e8_32s40w_e30_v16?0"<SKPresenceDelegate>"8lw40l8s32l8
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e17_v16?0"NSError"8ls32l8w64l8s40l8s48l8s56l8
+ ___block_literal_global.23
+ ___block_literal_global.76
+ ___block_literal_global.78
+ ___block_literal_global.80
+ ___block_literal_global.84
+ ___logger_block_invoke
+ __os_feature_enabled_impl
+ _logger
+ _logger.cold.1
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_reestablishDaemonConnection
+ _objc_msgSend$_reretainTransientSubscriptionWithCompletion:
+ _objc_msgSend$addObserver:selector:name:object:
+ _objc_msgSend$alphanumericCharacterSet
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$assertPresenceForIdentifier:withPresencePayload:assertionOptions:completion:
+ _objc_msgSend$assertPresenceWithPresencePayload:assertionOptions:completion:
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$clientID
+ _objc_msgSend$clientPrefixedPresenceIdentifierForPresenceIdentifier:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$containsString:
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$descriptionFromSKUpdatePriority:
+ _objc_msgSend$encodeInt64:forKey:
+ _objc_msgSend$formUnionWithCharacterSet:
+ _objc_msgSend$init
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$initWithForwardingTarget:
+ _objc_msgSend$initWithPriority:
+ _objc_msgSend$invokeWithTarget:
+ _objc_msgSend$isDaemonIdleExitEnabled
+ _objc_msgSend$isSupersetOfSet:
+ _objc_msgSend$methodSignatureForSelector:
+ _objc_msgSend$object
+ _objc_msgSend$priority
+ _objc_msgSend$rollChannelForPresenceIdentifier:completion:
+ _objc_msgSend$selector
+ _objc_msgSend$setIsDaemonIdleExitEnabled:
+ _objc_msgSend$setPresenceAssertionOptions:
+ _objc_msgSend$ska_sha256Hash
+ _objc_msgSend$stringWithCapacity:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$substringToIndex:
+ _strlen
+ _xpc_copy_entitlement_for_self
+ _xpc_string_get_string_ptr
- -[SKPresence _inviteHandle:fromSenderHandle:completion:]
- -[SKPresence _reRetainTransientSubscriptionWithCompletion:]
- -[SKPresence hasAssertion]
- -[SKPresence setHasAssertion:]
- -[SKPresence setOptions:]
- -[SKStatusPublishingService _inviteHandle:fromSenderHandle:withInvitationPayload:completion:]
- GCC_except_table11
- GCC_except_table37
- GCC_except_table41
- GCC_except_table44
- GCC_except_table49
- GCC_except_table53
- GCC_except_table54
- GCC_except_table72
- GCC_except_table77
- GCC_except_table8
- GCC_except_table82
- _SKPresenceOptionIsPersonal
- _SKPresenceOptionServiceIdentifier
- ___28-[SKPresence invitedHandles]_block_invoke.27
- ___28-[SKPresence presentDevices]_block_invoke.25
- ___38-[SKPresence fetchPresenceCapability:]_block_invoke.37
- ___43-[SKPresenceDaemonConnection xpcConnection]_block_invoke.9
- ___44-[SKPresence releasePresenceWithCompletion:]_block_invoke.22
- ___44-[SKPresence releasePresenceWithCompletion:]_block_invoke.22.cold.1
- ___46-[SKPresence removeInvitedHandles:completion:]_block_invoke.36
- ___46-[SKPresence removeInvitedHandles:completion:]_block_invoke.36.cold.1
- ___48-[SKPresence _isHandleInvited:fromSenderHandle:]_block_invoke.28
- ___51-[SKStatusPublishingDaemonConnection xpcConnection]_block_invoke.6
- ___53-[SKStatusSubscriptionDaemonConnection xpcConnection]_block_invoke.6
- ___54-[SKPresence _registerForDelegateCallbacksIfNecessary]_block_invoke.40
- ___54-[SKPresence _registerForDelegateCallbacksIfNecessary]_block_invoke.40.cold.1
- ___57-[SKPresence _inviteHandles:fromSenderHandle:completion:]_block_invoke.35
- ___57-[SKPresence _inviteHandles:fromSenderHandle:completion:]_block_invoke.35.cold.1
- ___58-[SKPresence initialCloudKitImportReceivedWithCompletion:]_block_invoke.53
- ___59-[SKPresence _isHandleInvited:fromSenderHandle:completion:]_block_invoke.30
- ___59-[SKPresence _reRetainTransientSubscriptionWithCompletion:]_block_invoke
- ___59-[SKPresence _reRetainTransientSubscriptionWithCompletion:]_block_invoke_2
- ___59-[SKPresence assertPresenceWithPresencePayload:completion:]_block_invoke
- ___59-[SKPresence assertPresenceWithPresencePayload:completion:]_block_invoke.21
- ___59-[SKPresence assertPresenceWithPresencePayload:completion:]_block_invoke.21.cold.1
- ___59-[SKPresence assertPresenceWithPresencePayload:completion:]_block_invoke.cold.1
- ___61-[SKPresence hasInitialCloudKitImportOccurredWithCompletion:]_block_invoke.19
- ___61-[SKPresence hasInitialCloudKitImportOccurredWithCompletion:]_block_invoke.19.cold.1
- ___65-[SKPresence retainTransientSubscriptionAssertionWithCompletion:]_block_invoke.23
- ___65-[SKPresence retainTransientSubscriptionAssertionWithCompletion:]_block_invoke.23.cold.1
- ___66-[SKPresence releaseTransientSubscriptionAssertionWithCompletion:]_block_invoke.24
- ___66-[SKPresence releaseTransientSubscriptionAssertionWithCompletion:]_block_invoke.24.cold.1
- ___67-[SKPresence _fetchHandleInvitability:fromSenderHandle:completion:]_block_invoke.32
- ___68-[SKPresence invitedHandlesChangedForPresenceIdentifier:completion:]_block_invoke.48
- ___68-[SKPresence presentHandlesChangedForPresenceIdentifier:completion:]_block_invoke.45
- ___73-[SKStatusSubscriptionService subscriptionInvitationReceived:completion:]_block_invoke.35
- ___75-[SKStatusSubscriptionService subscriptionReceivedStatusUpdate:completion:]_block_invoke.32
- ___83-[SKStatusSubscriptionService subscriptionStateChangedForSubscriptions:completion:]_block_invoke.28
- ___block_descriptor_48_e8_32s40w_e30_v16?0"<SKPresenceDelegate>"8ls32l8w40l8
- ___block_literal_global.57
- ___block_literal_global.59
- ___block_literal_global.63
- _objc_msgSend$_inviteHandle:fromSenderHandle:completion:
- _objc_msgSend$_inviteHandle:fromSenderHandle:withInvitationPayload:completion:
- _objc_msgSend$_reRetainTransientSubscriptionWithCompletion:
- _objc_msgSend$assertPresenceForIdentifier:withPresencePayload:completion:
- _objc_msgSend$inviteHandles:fromSenderHandle:completion:
- _objc_msgSend$inviteHandles:fromSenderHandle:withInvitationPayload:completion:
CStrings:
+ "%02x"
+ "%@-%@-%@"
+ "'"
+ "-"
+ "-._~:"
+ "<%@: %p; handle = \"%@\"; deviceIdentifier = \"%@\"; deviceTokenURI = \"%@\"; assertionTime = \"%@\"; selfDevice = \"%d\"; selfHandle = \"%d\"; payload = \"%@\">"
+ "<%@: %p; serviceIdentifier = %@ isPersonal = %d isDaemonIdleExitEnabled = %d clientSpecifiedURI = %@>"
+ "@"
+ "@\"NSObject\""
+ "@\"SKPresenceAssertionOptions\""
+ "@24@0:8q16"
+ "A network error was encountered when completing the request"
+ "Attempting to reconnect to daemon"
+ "Checking if the initial CloudKit import has occurred."
+ "Completed presence channel roll"
+ "Deallocing SKPresence for presence identifier \"%@\""
+ "Deallocing SKStatusPublishingService for status type identifier \"%@\""
+ "Deallocing SKStatusSubscriptionService for status type identifier \"%@\""
+ "Delegate does not implement presentDevicesChangedForPresence:, not informing delegate: %@"
+ "Error checking if the CloudKit import has occurred. Error: %{public}@"
+ "ForceIdleExit"
+ "Has initial CloudKit import occurred? %@"
+ "Identifier uses unallowed characters, this will cause Blastdoored messages to fail: %@"
+ "Identifier was nil, could not validate it for Blastdoor requirements"
+ "MediaTransport"
+ "Notifying presence delegate that the initial CloudKit import was received."
+ "Presence channel roll completed with error: %@"
+ "Presence delegate does not implement the delegate method to be notified the initial CloudKit import was received."
+ "PresenceIdleExit"
+ "Received notice for wrong presenceIdentifier, not recreating state"
+ "Received notice that %@ has an update, re-establish state with SKA"
+ "Registering prefixed presenceIdentifier: %@"
+ "Registering presenceIdentifier: %@ to re-initiate connections to daemon"
+ "Retrieving present devices. Presence: %{public}@"
+ "Rolling presence channel with presence identifier: %@"
+ "SKDefines"
+ "SKPresenceAssertionOptions"
+ "SKPresenceAssertionOptionsPriority"
+ "SKPresenceOptionsEncodingKeyIsDaemonIdleExitEnabled"
+ "SKStatusKitErrorDomain"
+ "SKUpdatePriorityHigh"
+ "SKUpdatePriorityMedium"
+ "SKWeakObjectProxy"
+ "StatusKit"
+ "StatusKit encountered an internal error when performing the request"
+ "StatusKitAgent"
+ "T@\"NSObject\",R,W,N,V_target"
+ "T@\"SKPresenceAssertionOptions\",&,N,V_presenceAssertionOptions"
+ "T@\"SKPresenceOptions\",R,N,V_options"
+ "TB,N,V_isDaemonIdleExitEnabled"
+ "The attempted request was invalid"
+ "The device is currently under a rate limit for this request"
+ "The user's primary iCloud account is in a bad state"
+ "This error is not a valid SKStatusKitErrorCode"
+ "This feature has been disabled"
+ "This request failed due to a missing entitlement"
+ "Tq,N,V_priority"
+ "Tried to reconnect, but we already have a connection"
+ "UTF8String"
+ "Unable to listen on presenceIdentifier"
+ "Unhandled SKStatusSubscriptionValidationTokenValidity: %ld"
+ "Unknown Priority"
+ "Unknown service name %@ when checking allowlist"
+ "XPC Error checking initial CloudKit import. Error: %{public}@"
+ "XPC error rolling presence channel. Error: %{public}@"
+ "_handleStatusKitAgentAliveNotification:"
+ "_isDaemonIdleExitEnabled"
+ "_presenceAssertionOptions"
+ "_priority"
+ "_reestablishDaemonConnection"
+ "_reretainTransientSubscriptionWithCompletion:"
+ "_target"
+ "addObserver:selector:name:object:"
+ "alphanumericCharacterSet"
+ "ancli"
+ "appendFormat:"
+ "assertPresenceForIdentifier:withPresencePayload:assertionOptions:completion:"
+ "assertPresenceWithPresencePayload:assertionOptions:completion:"
+ "characterSetWithCharactersInString:"
+ "clientID"
+ "clientIDFromPresenceIdentifier"
+ "clientPrefixedPresenceIdentifierForPresenceIdentifier:"
+ "com.apple.StatusKit.presence.clientID"
+ "com.apple.availability"
+ "com.apple.focus.status"
+ "com.apple.mDNSResponder.statuskit.presence"
+ "com.apple.offgrid.status"
+ "componentsSeparatedByString:"
+ "containsObject:"
+ "containsString:"
+ "decodeInt64ForKey:"
+ "defaultCenter"
+ "descriptionFromSKUpdatePriority:"
+ "encodeInt64:forKey:"
+ "formUnionWithCharacterSet:"
+ "forwardInvocation:"
+ "forwardingTargetForSelector:"
+ "groupsessionservice"
+ "homed"
+ "identityservicesd"
+ "initWithFormat:"
+ "initWithForwardingTarget:"
+ "initWithPriority:"
+ "invokeWithTarget:"
+ "isDaemonIdleExitEnabled"
+ "isSupersetOfSet:"
+ "mediaremoted"
+ "methodSignatureForSelector:"
+ "no reference to self when trying to release/reestablish connection"
+ "object"
+ "presenceAssertionOptions"
+ "priority"
+ "q"
+ "q16@0:8"
+ "rollChannelForPresenceIdentifier:completion:"
+ "rollChannelWithCompletion:"
+ "safari"
+ "selector"
+ "setIsDaemonIdleExitEnabled:"
+ "setPresenceAssertionOptions:"
+ "setPriority:"
+ "ska_appearsToBeEmail"
+ "ska_sha256Hash"
+ "statustool"
+ "stringWithCapacity:"
+ "stringWithUTF8String:"
+ "substringToIndex:"
+ "target"
+ "v24@0:8q16"
+ "v48@0:8@\"NSString\"16@\"SKPresencePayload\"24@\"SKPresenceAssertionOptions\"32@?<v@?@\"NSError\">40"
- "&"
- "<%@: %p; handle = \"%@\"; deviceIdentifier = \"%@\"; deviceTokenURI = \"%@\"; payload = \"%@\"; assertionTime = \"%@\"; selfDevice = \"%d\"; selfHandle = \"%d\">"
- "<%@: %p; serviceIdentifier = %@ isPersonal = %d clientSpecifiedURI = %@>"
- "Checking if the initial cloud kit import has occurred."
- "Notifying presence delegate that the initial cloud kit import was received."
- "Presence delegate does not implement the delegate method to be notified the initial cloud kit import was received."
- "Retrieving present decives. Presence: %{public}@"
- "SKPresenceOptionIsPersonal"
- "SKPresenceOptionServiceIdentifier"
- "T@\"SKPresenceOptions\",&,N,V_options"
- "XPC Error checking if the cloudkit import has occurred. Error: %{public}@"
- "XPC Error checking initial cloud kit import. Error: %{public}@"
- "_delegateLock _registerForDelegateCallbacksIfNecessary unlocked already delegate count 0"
- "_inviteHandle:fromSenderHandle:completion:"
- "_inviteHandle:fromSenderHandle:withInvitationPayload:completion:"
- "_reRetainTransientSubscriptionWithCompletion:"
- "assertPresenceForIdentifier:withPresencePayload:completion:"
- "hasAssertion"
- "setHasAssertion:"
- "setOptions:"
- "v40@0:8@\"NSString\"16@\"SKPresencePayload\"24@?<v@?@\"NSError\">32"

```
