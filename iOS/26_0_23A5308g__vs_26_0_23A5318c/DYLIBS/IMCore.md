## IMCore

> `/System/Library/PrivateFrameworks/IMCore.framework/IMCore`

```diff

-1447.100.7.2.3
-  __TEXT.__text: 0x279d14
-  __TEXT.__auth_stubs: 0x3610
+1448.100.1.2.41
+  __TEXT.__text: 0x27deec
+  __TEXT.__auth_stubs: 0x3640
   __TEXT.__delay_stubs: 0x58
   __TEXT.__delay_helper: 0x110
-  __TEXT.__objc_methlist: 0x16d4c
-  __TEXT.__const: 0x95d0
-  __TEXT.__gcc_except_tab: 0x169a4
-  __TEXT.__cstring: 0x136a6
-  __TEXT.__oslogstring: 0x203b5
+  __TEXT.__objc_methlist: 0x16e24
+  __TEXT.__const: 0x9600
+  __TEXT.__gcc_except_tab: 0x16ae4
+  __TEXT.__cstring: 0x137a6
+  __TEXT.__oslogstring: 0x207e5
   __TEXT.__ustring: 0xc0
   __TEXT.__dlopen_cstrs: 0x184
-  __TEXT.__constg_swiftt: 0x2080
-  __TEXT.__swift5_typeref: 0x224b
-  __TEXT.__swift5_builtin: 0x104
+  __TEXT.__constg_swiftt: 0x20c8
+  __TEXT.__swift5_typeref: 0x2251
+  __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_reflstr: 0x23d6
-  __TEXT.__swift5_fieldmd: 0x2b38
+  __TEXT.__swift5_fieldmd: 0x2b44
   __TEXT.__swift5_assocty: 0x548
   __TEXT.__swift5_proto: 0x92c
-  __TEXT.__swift5_types: 0x264
-  __TEXT.__swift5_capture: 0x744
+  __TEXT.__swift5_types: 0x268
+  __TEXT.__swift5_capture: 0x794
   __TEXT.__swift_as_entry: 0xe0
   __TEXT.__swift_as_ret: 0xb0
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xa790
-  __TEXT.__eh_frame: 0x4cc8
+  __TEXT.__unwind_info: 0xa848
+  __TEXT.__eh_frame: 0x4ce0
   __TEXT.__objc_classname: 0x2750
-  __TEXT.__objc_methname: 0x40e62
-  __TEXT.__objc_methtype: 0x6915
-  __TEXT.__objc_stubs: 0x26320
-  __DATA_CONST.__got: 0x23d8
-  __DATA_CONST.__const: 0x5408
+  __TEXT.__objc_methname: 0x412b4
+  __TEXT.__objc_methtype: 0x6946
+  __TEXT.__objc_stubs: 0x26540
+  __DATA_CONST.__got: 0x23f0
+  __DATA_CONST.__const: 0x5488
   __DATA_CONST.__objc_classlist: 0x858
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x478
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdce8
+  __DATA_CONST.__objc_selrefs: 0xdda0
   __DATA_CONST.__objc_protorefs: 0x1b0
   __DATA_CONST.__objc_superrefs: 0x598
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x1b28
-  __AUTH_CONST.__const: 0x8130
-  __AUTH_CONST.__cfstring: 0xb740
-  __AUTH_CONST.__objc_const: 0x1e9f0
+  __AUTH_CONST.__auth_got: 0x1b40
+  __AUTH_CONST.__const: 0x8240
+  __AUTH_CONST.__cfstring: 0xb720
+  __AUTH_CONST.__objc_const: 0x1ea58
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x3ad0
   __AUTH.__data: 0x2300
-  __DATA.__objc_ivar: 0x11dc
-  __DATA.__data: 0x44e8
+  __DATA.__objc_ivar: 0x11e0
+  __DATA.__data: 0x4518
   __DATA.__bss: 0x12070
   __DATA.__common: 0x4a8
-  __DATA_DIRTY.__objc_data: 0x1b00
-  __DATA_DIRTY.__data: 0x210
+  __DATA_DIRTY.__objc_data: 0x1b30
+  __DATA_DIRTY.__data: 0x220
   __DATA_DIRTY.__bss: 0x3a0
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F35C8248-30B1-343A-8167-E8274F384826
-  Functions: 12583
-  Symbols:   2466
-  CStrings:  16823
+  UUID: 309AB2D7-E8B5-39AC-9DD2-1AF15E7F1A61
+  Functions: 12640
+  Symbols:   2471
+  CStrings:  16875
 
Symbols:
+ _IMChatHistoryClearedNotification
+ _IMChatPropertyLatestMessageDate
+ _IMChatPropertyParticipants
+ _OBJC_CLASS_$_IDSURI
+ __ConfigureContextForIMItem
CStrings:
+ "@16@?0@\"NSDictionary\"8"
+ "Accounts expect forced filtering."
+ "B16@?0@\"NSDictionary\"8"
+ "Cannot reset participants due to mismatching participant hashes."
+ "Chat with chat identifier %@ had no groupID. A new groupID was created: %@"
+ "Device does not allow forced unknown filtering"
+ "Device does not force unknown filtering."
+ "Device expects forced unknown filtering."
+ "Failed to find cached chat for guid: %@. Properties were not updated: %@"
+ "Failed to find chat for chatIdentifier: %@"
+ "Falling back to %{bool}d for %s"
+ "Found %{bool}d for %s"
+ "Getting cached chat with GUID: %@ found chat: %@"
+ "Handles are identical, not updating the participants."
+ "IMDeviceRegionIsEligibleToBeForcedIntoFilteringUnknownSender"
+ "IMMessagesFilteringSettingForPreferedSubscription"
+ "Local value allows forced unkown filtering"
+ "Marking %ld chats as reviewed."
+ "Received transcriptBackgroundUpdatedForChatIdentifier: %@, style: %d, accountID: %@, userInfo: %@"
+ "Region does not expect forced unknown filtering"
+ "Server allows forced unkown filtering"
+ "Subcription %s expect forced unknown filtering"
+ "T@\"NSString\",&,N,S__setChatIdentifierForGroups:,V__chatIdentifierForGroups"
+ "Trying to change participants from %@ to %@ (Chat: %@)"
+ "Updating chat identifier from %@ to %@"
+ "User modified unknown or spam. Device does not force unknown filtering"
+ "__chatIdentifierForGroups"
+ "__imArrayByApplyingBlock:filter:"
+ "__kIMChatHistoryClearedNotification"
+ "__setChatIdentifierForGroups:"
+ "_chatDidRecoverFromJunk:"
+ "_chatIdentifierForGroups"
+ "_clearHistoryAndReplaceLastMessage:"
+ "_currentCachedRemoteDevicesForDestinations:service:preferredFromID:listenerID:"
+ "_mergedChatGUIDsForChatGUIDs:"
+ "_removeAllItemsSkippingCallToItemsDidChange:"
+ "_resetParticipants:"
+ "_shouldUpdateChatPropertyByRecencyOnChat:incomingDictionary:"
+ "_sortedParticipantIDHashForParticipants:usesPersonCentricID:fallbackToContactID:"
+ "_updateChat:chatIdentifierForGroups:shouldPostNotification:"
+ "_winningChatIdentifierForExistingChat:incomingDictionary:"
+ "_winningGroupIDForExistingChat:incomingDictionary:"
+ "_winningParticipantsForExistingChat:incomingDictionary:"
+ "allow-force-unknown-filtering-on"
+ "chat: %@  joinProperties: %@"
+ "chatDidRecoverFromJunk:"
+ "clearHistoryAndReloadLastMessageForChatsWithGUIDs:"
+ "clearHistoryAndReloadLastMessageForMergedFilteredChats"
+ "could not make SyncedSettingKey from updated key: %s"
+ "fetchSettingExplicitlySet:reply:"
+ "initWithPrefixedURI:"
+ "initWithSuiteName:"
+ "kCKMessageFilteringSettingsConfirmedKey"
+ "kCKMessageSpamFilteringSettingsConfirmedKey"
+ "loadLastMessageItemsForMergedChatsWithGUIDs:completionHandler:"
+ "lt_preferredLocales"
+ "posting notification for %s"
+ "preferredLanguagesContainVariantForCode:"
+ "settingExplicitlySet:reply:"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\">24"
+ "v32@?0@\"NSString\"8@\"IMChat\"16^B24"
+ "valueCache"
- "Received transcriptBackgroundUpdatedForChatIdentifier: %@ userInfo: %@"
- "Translations not supported for system language"
- "_chat:joinWithProperties:guid:"
- "_currentCachedRemoteDevicesForDestinations:service:listenerID:"
- "chat: %@  joinProperties: %@, guid: %@"
- "clearMessagesForMergedFilteredChats"
- "sendSentMessageEvent"

```
