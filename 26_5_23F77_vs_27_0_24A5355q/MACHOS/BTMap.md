## BTMap

> `/usr/sbin/BTMap`

```diff

-354.11.0.0.0
-  __TEXT.__text: 0x3e38
-  __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x494
+2700.30.2.0.0
+  __TEXT.__text: 0x4350
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_stubs: 0x1020
+  __TEXT.__objc_methlist: 0x4a4
   __TEXT.__const: 0x28
-  __TEXT.__cstring: 0x3da
-  __TEXT.__objc_methname: 0xbf6
-  __TEXT.__oslogstring: 0x34d
-  __TEXT.__objc_classname: 0x70
+  __TEXT.__cstring: 0x48e
+  __TEXT.__objc_methname: 0xd93
+  __TEXT.__oslogstring: 0x37a
+  __TEXT.__objc_classname: 0x66
   __TEXT.__objc_methtype: 0x270
   __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__unwind_info: 0x170
-  __DATA_CONST.__auth_got: 0x2d0
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__auth_ptr: 0x8
+  __TEXT.__unwind_info: 0x168
   __DATA_CONST.__const: 0x2a0
-  __DATA_CONST.__cfstring: 0x420
+  __DATA_CONST.__cfstring: 0x540
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__auth_got: 0x310
+  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x790
-  __DATA.__objc_selrefs: 0x470
+  __DATA.__objc_selrefs: 0x530
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0x190
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/IMCore.framework/IMCore
+  - /System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AA8DD5AC-148F-3D43-AEFE-7584F7F2BAE6
-  Functions: 108
-  Symbols:   135
-  CStrings:  330
+  UUID: 9EF23437-28CA-3879-8B06-A73DA495A1A6
+  Functions: 106
+  Symbols:   153
+  CStrings:  374
 
Symbols:
+ _IMChatCanonicalIDSIDsForAddress
+ _IMPreferredAccountForService
+ _IMPreferredSendingAccountForAddressesWantsGroupWithFallbackService
+ _OBJC_CLASS_$_IMChatRegistry
+ _OBJC_CLASS_$_IMMe
+ _OBJC_CLASS_$_IMMessage
+ _OBJC_CLASS_$_IMServiceImpl
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSAttributedString
+ _OBJC_CLASS_$_NSMutableDictionary
+ __xpc_type_array
+ _kFZListenerCapSendMessages
+ _kFZListenerCapSentMessageObserver
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _xpc_array_apply
- _IMSPISendMessageWithAttachmentsReturningGUID
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x28
CStrings:
+ "Adding guid %@ to pending send list with chatIdentifier %@"
+ "Attempting to send message through IMCore"
+ "B24@?0Q8@\"NSObject<OS_xpc_object>\"16"
+ "Invalid or missing recipients array"
+ "No valid recipients found"
+ "_isUsableForSending"
+ "_stripFZIDPrefix"
+ "arrayWithObjects:count:"
+ "bestIMHandle"
+ "chatIdentifier"
+ "chatSummary"
+ "chatWithHandles:"
+ "count"
+ "existingChatWithChatIdentifier:"
+ "iMessage is not available for use, defaulting to SMS"
+ "iMessageService"
+ "imHandleWithID:"
+ "initWithString:"
+ "instantMessageWithText:flags:threadIdentifier:"
+ "kChatIdentifier"
+ "kChatsInfo"
+ "kConversationName"
+ "kLastActivity"
+ "kParticipantHandle"
+ "kParticipantName"
+ "kParticipants"
+ "kReadStatus"
+ "kRecipientIdentifiers"
+ "kSummary"
+ "lastMessage"
+ "me"
+ "mutableCopy"
+ "numberWithInt:"
+ "participantsWithState:"
+ "sendMessage:"
+ "serializeIMChats:"
+ "setObject:forKeyedSubscript:"
+ "sharedController"
+ "sharedRegistry"
+ "smsService"
+ "time"
+ "unreadMessageCount"
- "Adding guid %@ to pending send list"
- "Message failed to send through IMCore, could not send new chat"
- "Message handed off to ImCore for sending"
- "Sending message through IMCore"
- "objectAtIndex:"
- "sharedInstance"
- "v16@?0@\"NSString\"8"

```
