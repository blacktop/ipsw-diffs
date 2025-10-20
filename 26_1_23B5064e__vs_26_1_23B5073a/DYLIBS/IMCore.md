## IMCore

> `/System/Library/PrivateFrameworks/IMCore.framework/IMCore`

```diff

-1450.200.88.2.1
-  __TEXT.__text: 0x2a24c4
-  __TEXT.__auth_stubs: 0x37a0
+1450.200.89.2.31
+  __TEXT.__text: 0x2a39fc
+  __TEXT.__auth_stubs: 0x37c0
   __TEXT.__delay_stubs: 0x58
   __TEXT.__delay_helper: 0x110
-  __TEXT.__objc_methlist: 0x170cc
-  __TEXT.__const: 0xb870
-  __TEXT.__gcc_except_tab: 0x160b0
-  __TEXT.__cstring: 0x14546
-  __TEXT.__oslogstring: 0x21693
+  __TEXT.__objc_methlist: 0x170e4
+  __TEXT.__const: 0xc440
+  __TEXT.__gcc_except_tab: 0x149cc
+  __TEXT.__cstring: 0x145d6
+  __TEXT.__oslogstring: 0x22003
   __TEXT.__ustring: 0xc0
   __TEXT.__dlopen_cstrs: 0x184
   __TEXT.__constg_swiftt: 0x24f4

   __TEXT.__swift_as_ret: 0xc0
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__unwind_info: 0xac08
-  __TEXT.__eh_frame: 0x5c00
+  __TEXT.__unwind_info: 0xa998
+  __TEXT.__eh_frame: 0x5ca8
   __TEXT.__objc_classname: 0x2786
-  __TEXT.__objc_methname: 0x4191d
+  __TEXT.__objc_methname: 0x41943
   __TEXT.__objc_methtype: 0x6998
   __TEXT.__objc_stubs: 0x26740
   __DATA_CONST.__got: 0x24a0

   __DATA_CONST.__objc_protorefs: 0x1d0
   __DATA_CONST.__objc_superrefs: 0x5a0
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x1bf0
-  __AUTH_CONST.__const: 0x9318
-  __AUTH_CONST.__cfstring: 0xb840
-  __AUTH_CONST.__objc_const: 0x1efe8
+  __AUTH_CONST.__auth_got: 0x1c00
+  __AUTH_CONST.__const: 0x9358
+  __AUTH_CONST.__cfstring: 0xb880
+  __AUTH_CONST.__objc_const: 0x1f018
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x3b40
   __AUTH.__data: 0x23e8
-  __DATA.__objc_ivar: 0x11fc
-  __DATA.__data: 0x4a88
-  __DATA.__bss: 0x15f10
+  __DATA.__objc_ivar: 0x1200
+  __DATA.__data: 0x4ae8
+  __DATA.__bss: 0x15f30
   __DATA.__common: 0x420
   __DATA_DIRTY.__objc_data: 0x1b30
-  __DATA_DIRTY.__data: 0x260
+  __DATA_DIRTY.__data: 0x1a0
   __DATA_DIRTY.__bss: 0x3a0
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 45DE1901-1BAF-3C2B-A977-B8E0466886F8
-  Functions: 13053
-  Symbols:   2507
-  CStrings:  17068
+  UUID: A18CC8F2-17DD-35F8-802D-6BF149040A50
+  Functions: 13066
+  Symbols:   2509
+  CStrings:  17103
 
Symbols:
+ _IMBagDoubleValueWithDefault
+ _IMSharedHelperCurrentRegionRequiresKnownSenderForNickname
CStrings:
+ " form deprecated initializer"
+ "Cache miss looking up chat with groupID: %@ displayName: %@ joinedChatsOnly: %{BOOL}d allowAlternativeService: %{BOOL}d handles: %@"
+ "Cached contact found"
+ "CanAlwaysInlineReply"
+ "Chat %@ required updated transcript background details (notify: %{BOOL}d)"
+ "Chat [%@] hasCancellableScheduledMessage to %{BOOL}d"
+ "Chat [%@] info dictionary has [hasCancellableScheduledMessage: %{BOOL}d]"
+ "Chat has known participants, and IMSharedHelperCurrentRegionRequiresKnownSenderForNickname is YES. Refusing to offer sharing."
+ "Closing chat session with business with chatIdentifier: %@ on account: %@"
+ "Daemon began deferred setup (firstLoad is: %{BOOL}d)"
+ "Daemon completed deferred setup (firstLoad was: %{BOOL}d)"
+ "First Load: %{BOOL}d, Full Reload: %{BOOL}d"
+ "Forwarding join chat to account %@ for: [IMChat guid: %@  chat identifier: %@  state: %lu  pcid: %@]"
+ "Forwarding leave chat for: %@"
+ "Found candidate chat %@ but rejected matchingParticipantHash: %{BOOL}d matchingDisplayName: %{BOOL}d matchingPersonCentricID: %{BOOL}d dictionary guid: %@"
+ "Found existing autoDonationBehavior: %ld for chat with GUID: %@ (notify: %{BOOL}d)"
+ "Getting cached chat with GUID: %@ found chat: %{BOOL}d"
+ "Ignoring groupID update (%@ -> %@) because chat is not group chat: [IMChat chat identifier: %@  style: %c]"
+ "Ignoring original groupID update (%@ -> %@) because chat is not group chat: [IMChat chat identifier: %@  style: %c]"
+ "Joining chat: [IMChat guid: %@  chat identifier: %@  state: %lu  person centric ID: %@]"
+ "Leaving chat %@ with account ID %@"
+ "Loaded chat was created: %{BOOL}d guid: %@ chat: <IMChat %p> [Identifier: %@  GUID: %@  Persistent ID: %@  Account: %@  Style: %c  State: %d  hasParticipants: %{BOOL}d  Participants: %lu  Room Name: %@  Display Name: %@  Last Addressed Handle: %@ Last Addressed SIMID: %@  Group ID: %@  Unread Count: %u  Failure Count: %u  isFiltered: %d  filterModes: %@  hasHadSuccessfulQuery: %{BOOL}d  bizIntent: %@  personCentricID: %@  isRecovered: %{BOOL}d  isDeletingIncomingMessages: %{BOOL}d  isPendingReview: %{BOOL}d  mergedPinningIdentifiers: %@]"
+ "Nickname feature disabled, nickname is not active."
+ "Nickname feature disabled, no unknown sender records"
+ "Nickname feature disabled, not denying handles"
+ "Nickname feature disabled, not offering handles for nicknames under scrutiny"
+ "Nickname feature disabled, not offering nickname sharing"
+ "Nickname feature disabled, not updating active handles"
+ "Nickname feature disabled, not updating all as pending"
+ "Nickname feature disabled, not updating allow list"
+ "Nickname feature disabled, not updating ignored handles"
+ "Nickname feature disabled, not updating nicknames"
+ "Nickname feature disabled, not updating pending nickname"
+ "Nickname feature disabled, not updating transitioned handles"
+ "Nickname feature disabled, not updating unknown sender records"
+ "Nickname feature disabled, returning NO for observed transition for %@"
+ "Nickname feature disabled, returning nil for archived nickname for %@"
+ "Nickname feature disabled, returning nil for current nickname for %@"
+ "Nickname feature disabled, returning nil for nickname for handles %@"
+ "Nickname feature disabled, returning nil for pending nickname for %@"
+ "Nickname feature is not enabled, no state oracle."
+ "Nickname feature not enabled, not updating personal nickname"
+ "Not returning nickname for handle %@, because their is no contact for the handle."
+ "Recently Deleted | Completing query: Loaded recoverableMessagesMetadata for query: %@, hasRecoverableMessages: %{BOOL}d"
+ "Recently Deleted | Loading recoverable message metadata synchronously %{BOOL}d loadsChats %{BOOL}d"
+ "Recipients list does not contain contact, refuse to create a state oracle."
+ "Registering dictionary for with newGUID: %@ isIncoming: %{BOOL}d shouldPostNotification: %{BOOL}d chat: %@"
+ "Registering outgoing chat."
+ "Skipping handle %@ because we do not have a contact for it."
+ "Ti,N,V_authorizationStatus"
+ "Total number of IMChats we expect to create %lu"
+ "Unable to create Participant with error "
+ "Using default autoDonationBehavior for chat with GUID: %@ (notify: %{BOOL}d)"
+ "_authorizationStatus"
+ "chat: %@ isDeletingIncomingMessagesUpdated: %{BOOL}d"
+ "chat: %@ isRecoveredUpdated: %{BOOL}d"
+ "chat: %@ uncachedAttachmentCountUpdated: %lu"
+ "md-transcript-coalescing-threshhold"
+ "registering outgoing chat."
+ "setAuthorizationStatus:"
- "Cache miss looking up chat with groupID: %@ displayName: %@ joinedChatsOnly: %@ allowAlternativeService: %@ handles: %@"
- "Cached contact found: %@"
- "Chat %@ required updated transcript background details (notify: %@)"
- "Chat [%@] hasCancellableScheduledMessage to %d"
- "Chat [%@] info dictionary has [hasCancellableScheduledMessage: %@]"
- "Closing chat session with business with chatIdentifier: %@ chat: %@ on account: %@"
- "Daemon began deferred setup (firstLoad is: %@)"
- "Daemon completed deferred setup (firstLoad was: %@)"
- "First Load: %@, Full Reload: %@"
- "Forwarding join chat for: %@   to account: %@"
- "Forwarding leave chat for: %@   to account: %@"
- "Found candidate chat %@ but rejected matchingParticipantHash: %@ matchingDisplayName: %@ matchingPersonCentricID: %@ dictionary guid: %@"
- "Found existing autoDonationBehavior: %ld for chat with GUID: %@ (notify: %@)"
- "Getting cached chat with GUID: %@ found chat: %@"
- "Ignoring groupID update (%@ -> %@) because chat is not group chat: %@"
- "Ignoring original groupID update (%@ -> %@) because chat is not group chat: %@"
- "Loaded chat was created: %@ guid: %@ chat: %@"
- "Recently Deleted | Completing query: Loaded recoverableMessagesMetadata for query: %@, hasRecoverableMessages: %@"
- "Recently Deleted | Loading recoverable message metadata synchronously %@ loadsChats %@"
- "Registering dictionary for with newGUID: %@ isIncoming: %@ shouldPostNotification: %@ chat: %@"
- "Total number of IMChats we expect to create %@"
- "Using default autoDonationBehavior for chat with GUID: %@ (notify: %@)"
- "chat: %@ isDeletingIncomingMessagesUpdated: %@"
- "chat: %@ isRecoveredUpdated: %@"
- "chat: %@ uncachedAttachmentCountUpdated: %@"
- "registering outgoing chat: %@"
- "setLastMessageSupportsEncryption:"

```
