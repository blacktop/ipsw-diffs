## IMCore

> `/System/Library/PrivateFrameworks/IMCore.framework/IMCore`

```diff

-1402.500.128.2.2
-  __TEXT.__text: 0x1c16d4
-  __TEXT.__auth_stubs: 0x2730
+1402.500.164.2.1
+  __TEXT.__text: 0x1c71ac
+  __TEXT.__auth_stubs: 0x2760
   __TEXT.__delay_stubs: 0x58
   __TEXT.__delay_helper: 0xec
-  __TEXT.__objc_methlist: 0x1611c
+  __TEXT.__objc_methlist: 0x16104
   __TEXT.__const: 0x1850
-  __TEXT.__gcc_except_tab: 0x16a84
-  __TEXT.__cstring: 0x10427
-  __TEXT.__oslogstring: 0x1e7e9
+  __TEXT.__gcc_except_tab: 0x16a1c
+  __TEXT.__cstring: 0x10357
+  __TEXT.__oslogstring: 0x1e959
   __TEXT.__ustring: 0xc0
   __TEXT.__dlopen_cstrs: 0x184
   __TEXT.__constg_swiftt: 0x550
-  __TEXT.__swift5_typeref: 0xa07
+  __TEXT.__swift5_typeref: 0xa39
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_reflstr: 0x7c6
   __TEXT.__swift5_fieldmd: 0x720
   __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift5_proto: 0x128
   __TEXT.__swift5_types: 0x6c
-  __TEXT.__swift5_capture: 0x4c0
+  __TEXT.__swift5_capture: 0x520
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x7e28
-  __TEXT.__eh_frame: 0x890
+  __TEXT.__unwind_info: 0x7e58
+  __TEXT.__eh_frame: 0x8dc
   __TEXT.__objc_classname: 0x2571
-  __TEXT.__objc_methname: 0x3d5bf
-  __TEXT.__objc_methtype: 0x65a1
-  __TEXT.__objc_stubs: 0x24bc0
-  __DATA_CONST.__got: 0x1f38
+  __TEXT.__objc_methname: 0x3d5bb
+  __TEXT.__objc_methtype: 0x65ae
+  __TEXT.__objc_stubs: 0x24b80
+  __DATA_CONST.__got: 0x1f60
   __DATA_CONST.__const: 0x5128
   __DATA_CONST.__objc_classlist: 0x730
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x440
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd1e8
+  __DATA_CONST.__objc_selrefs: 0xd1d8
   __DATA_CONST.__objc_protorefs: 0x1a0
   __DATA_CONST.__objc_superrefs: 0x560
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x13b8
-  __AUTH_CONST.__auth_ptr: 0x328
-  __AUTH_CONST.__const: 0x42d8
-  __AUTH_CONST.__cfstring: 0xbd20
-  __AUTH_CONST.__objc_const: 0x1c2b0
+  __AUTH_CONST.__auth_got: 0x13d0
+  __AUTH_CONST.__auth_ptr: 0x360
+  __AUTH_CONST.__const: 0x4370
+  __AUTH_CONST.__cfstring: 0xbcc0
+  __AUTH_CONST.__objc_const: 0x1c278
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x24e8
   __AUTH.__data: 0x100
-  __DATA.__objc_ivar: 0x1140
-  __DATA.__data: 0x29f8
-  __DATA.__bss: 0x2d78
+  __DATA.__objc_ivar: 0x113c
+  __DATA.__data: 0x2a68
+  __DATA.__bss: 0x2d88
   __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x26e0
   __DATA_DIRTY.__data: 0x3f0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9056
-  Symbols:   2368
-  CStrings:  14441
+  Functions: 9072
+  Symbols:   2373
+  CStrings:  14443
 
Symbols:
+ _IMIsRunningInMessagesAssistantExtension
+ __IMGroupIDChangedChatIdentifierKey
+ __IMGroupIDChangedNotification
+ __IMGroupIDChangedPreviousGroupIDKey
+ __IMGroupIDChangedUpdatedGroupIDKey
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
CStrings:
+ "\x02G\x12\x16\x112=!!\x12\"#\")"
+ "(IMChat) Daemon did delete message guids"
+ "ChatBot Logo - Cached logo does not exist for %@, its url is %@"
+ "ChatBot Logo - Client is not a UI process, skip saving logo data for %@"
+ "ChatBot Logo - Use cached logo %lu for %@"
+ "Chatbot %s needs brand info due to defaults, request it from relay"
+ "Chatbot %s needs persistent menu due to defaults, request it from relay"
+ "Handle daemon did delete message guids: %@"
+ "IMHandle_Business"
+ "Not unregistering listener because it's already not listening %p"
+ "RCSForceNeedBrandInfoFromRelay"
+ "RCSForceNeedPersistentMenu"
+ "Registering as photo library persistence change listener %p"
+ "Unregistering as photo library persistence change listener %p"
+ "Unregistering listener %p"
+ "_daemonMovedChatsToRecentlyDeleted:deletionDate:"
+ "_daemonMovedMessagesWithGUIDsToRecentlyDeleted:chatGUID:deleteDate:"
+ "_fetchBrandLogoFromChatRegistryFor:"
+ "_refreshKTData"
+ "brandLogoUrlFromChatIdentifier:"
+ "handleDaemonDidDeleteMessageGUIDs:"
+ "movedMessageGUIDsToRecentlyDeleted:forChatWithGUID:queryID:deletionDate:"
+ "updateBalloonPayload:attachments:bundleID:forMessageGUID:"
+ "v48@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"NSDate\"40"
- "\x02G\x12\x16\x112=!!\x122#\")"
- "Chat with previousGroupID (%@) was muted, but that group ID changed. Adding new group ID (%@) to the muted chat list too. chat: %@"
- "IMMutedChatList"
- "Not unregistering listener because it's already not listening %@"
- "Registering as photo library persistence change listener %@"
- "TQ,N,V_lastKTStatus"
- "Unregistering as photo library persistence change listener %@"
- "Unregistering listener %@"
- "Updating group ID in muted chat list. previousGroupID: %@, newGroupID: %@, chat: %@"
- "_completedMovingChatsToRecentlyDeleted:deletionDate:"
- "_lastKTStatus"
- "_updateGroupID:toGroupID:forChat:"
- "lastKTStatus"
- "movedMessagesToRecentlyDeletedWithQueryID:"
- "registerForGroupIDChangeNotifications"
- "setLastKTStatus:"
- "syncChats"
- "unmuteChatWithMuteIdentifiers:syncToPairedDevice:"
- "unmuteDateForMuteIdentifier:"
- "updateBalloonPayload:attachments:forMessageGUID:"
- "v40@0:8@\"NSData\"16@\"NSArray\"24@\"NSString\"32"

```
