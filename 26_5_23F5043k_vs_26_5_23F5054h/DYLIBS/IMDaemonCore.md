## IMDaemonCore

> `/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore`

```diff

-1450.600.13.2.2
-  __TEXT.__text: 0x366cc0
-  __TEXT.__auth_stubs: 0x5540
-  __TEXT.__objc_methlist: 0x19bec
-  __TEXT.__const: 0x6c98
-  __TEXT.__cstring: 0x12e3c
-  __TEXT.__gcc_except_tab: 0x21fb8
-  __TEXT.__oslogstring: 0x4ec47
+1450.600.43.2.1
+  __TEXT.__text: 0x366518
+  __TEXT.__auth_stubs: 0x5530
+  __TEXT.__objc_methlist: 0x19c44
+  __TEXT.__const: 0x6c78
+  __TEXT.__cstring: 0x12d8c
+  __TEXT.__gcc_except_tab: 0x22158
+  __TEXT.__oslogstring: 0x4f1f7
   __TEXT.__ustring: 0x32c
   __TEXT.__dlopen_cstrs: 0x246
   __TEXT.__swift5_typeref: 0x2f5c

   __TEXT.__swift5_reflstr: 0x136f
   __TEXT.__swift5_fieldmd: 0x15d4
   __TEXT.__swift5_assocty: 0x6b8
-  __TEXT.__swift5_capture: 0x1348
+  __TEXT.__swift5_capture: 0x12f8
   __TEXT.__swift5_proto: 0x328
   __TEXT.__swift5_types: 0x204
-  __TEXT.__swift_as_entry: 0x340
-  __TEXT.__swift_as_ret: 0x418
+  __TEXT.__swift_as_entry: 0x334
+  __TEXT.__swift_as_ret: 0x40c
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xd7f8
-  __TEXT.__eh_frame: 0x780c
+  __TEXT.__unwind_info: 0xd7e0
+  __TEXT.__eh_frame: 0x773c
   __TEXT.__objc_classname: 0x44f1
-  __TEXT.__objc_methname: 0x513e7
-  __TEXT.__objc_methtype: 0xb2ef
-  __TEXT.__objc_stubs: 0x32a00
-  __DATA_CONST.__got: 0x3328
-  __DATA_CONST.__const: 0x6588
+  __TEXT.__objc_methname: 0x514e7
+  __TEXT.__objc_methtype: 0xb30f
+  __TEXT.__objc_stubs: 0x32ac0
+  __DATA_CONST.__got: 0x3330
+  __DATA_CONST.__const: 0x65b8
   __DATA_CONST.__objc_classlist: 0x988
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x778
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfe50
+  __DATA_CONST.__objc_selrefs: 0xfe80
   __DATA_CONST.__objc_protorefs: 0x278
   __DATA_CONST.__objc_superrefs: 0x5d8
   __DATA_CONST.__objc_arraydata: 0x170
-  __AUTH_CONST.__auth_got: 0x2ab0
-  __AUTH_CONST.__const: 0x8228
-  __AUTH_CONST.__cfstring: 0xe6c0
-  __AUTH_CONST.__objc_const: 0x21110
+  __AUTH_CONST.__auth_got: 0x2aa8
+  __AUTH_CONST.__const: 0x81b0
+  __AUTH_CONST.__cfstring: 0xe780
+  __AUTH_CONST.__objc_const: 0x211b8
   __AUTH_CONST.__objc_intobj: 0xac8
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x3418
   __AUTH.__data: 0x5e0
-  __DATA.__objc_ivar: 0x1230
+  __DATA.__objc_ivar: 0x123c
   __DATA.__data: 0x57c0
   __DATA.__bss: 0x5000
   __DATA.__common: 0x178

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 826AEFF8-3A84-3F50-873D-D9475539A9D2
-  Functions: 13086
-  Symbols:   3023
-  CStrings:  21621
+  UUID: 124D1454-F36A-3A24-BEB6-F0F184398E77
+  Functions: 13074
+  Symbols:   3025
+  CStrings:  21654
 
Symbols:
+ _IDSServerBagFinishedLoadingNotification
+ _IMItemCKRecordCreationErrorDomain
CStrings:
+ ".Migration"
+ "@\"<NSObject>\""
+ "AcceptFileTransfer completion guid: %@ success: %{BOOL}d error: %@"
+ "AcceptFileTransfers: full CK error with nil failedTransfers, treating all %lu transfers as failed. error: %@"
+ "Attempt starting bag load to trigger fallback logic."
+ "B32@0:8^@16@?24"
+ "Chat %@ successfully validated."
+ "Chat from chat identifiers %@ passed validation. This chat should have been used for the outgoing relay message!"
+ "EmptyStringDisplayName [v2]"
+ "Error not provided to caller."
+ "Failed to generate CKRecord for Chat with unknown error."
+ "Failed to generate CKRecord for Chat. code: %lld domain: %@"
+ "Found chat %@ failed validation due to mismatched participants, but the found chat will still be returned."
+ "Found chat %@ failed validation due to mismatched participants. The found chat will not be returned."
+ "Found chat %@ failed validation with error: %@"
+ "Found chat %@ failed validation, but the outgoing message is reflect only. The chat will conversge to recipients: %@"
+ "Incompatible action type %lld"
+ "MiC creating a chat with an empty string display name"
+ "Missing Destination Information [v2]"
+ "Not converging participants because validation error has no added or removed participants"
+ "NullCKRecordForIMDChat [v2]"
+ "Parent Chat ID of message %@ associated with group chat %@ is a chat guid %@. This is never expected!"
+ "Server bag attempted to be read, but not loaded."
+ "Server bag not loaded, but attempted to read MiCOnByDefault"
+ "Server loaded delayed, invoking fallback logic."
+ "T@\"<NSObject>\",&,N,V_serverBagFinishedLoadingObserver"
+ "Unvalidated chat %@ failed validation and does not match chat from identifiers %@. Validating chat from chat identifiers to see whether it passes validation."
+ "Validating chat %@ for outgoing relay message."
+ "_handleFileTransfer:acceptedWithPath:autoRename:overwrite:options:source:postNotification:"
+ "_serverBagFinishedLoadingObserver"
+ "_setAcceptSource:"
+ "acceptSource"
+ "addParentChatID:toChat:messageItem:"
+ "calculateServiceForSendingToChat:accounts:forceServerRefresh:completionBlock:"
+ "chatForHandles creating a chat with an empty string display name"
+ "chatForOutgoingMessage not providing error to caller."
+ "com.apple.messages.IMItemCKRecordCreation"
+ "didReceiveDisplayNameChange:guid:fromID:toIdentifier:forChat:style:account:shouldRelay:unattributed:"
+ "fileTransfer:acceptedWithPath:autoRename:overwrite:options:source:"
+ "isFirstUnencryptedSend"
+ "reachabilityContextForChat:forceServerRefresh:"
+ "serverBagFinishedLoadingObserver"
+ "setIsFirstUnencryptedSend:"
+ "setServerBagFinishedLoadingObserver:"
+ "shouldAttemptMiCOnByDefaultWithError:retryFallback:"
+ "startBagLoad"
+ "u"
+ "v56@0:8@\"NSString\"16@\"NSString\"24B32B36q40q48"
+ "v56@0:8@16@24B32B36q40q48"
+ "v60@0:8@16@24B32B36q40q48B56"
+ "v76@0:8@16@24@32@40@48C56@60B68B72"
- "An attachment was unexpectedly marked as unpurgeable on disk, but Messages database lists it as purgeable."
- "EmptyStringDisplayName"
- "FilePurgeabilityError"
- "FilePurgeabilityError-PurgeabilityMismatch"
- "Missing Destination Information"
- "NullCKRecordForIMDChat"
- "PurgeabilityMismatch"
- "Replicated Message Deferral Timeout"
- "[Internal] Messages Storage Management"
- "_handleFileTransfer:acceptedWithPath:autoRename:overwrite:options:postNotification:"
- "addParentChatID:toChat:service:"
- "calculateServiceForSendingToChat:accounts:completionBlock:"
- "didReceiveDisplayNameChange:guid:fromID:toIdentifier:forChat:style:account:shouldRelay:"
- "doubleForKey:"
- "fileTransfer:acceptedWithPath:autoRename:overwrite:options:"
- "purgeability-taptoradar-enabled"
- "purgeability-taptoradar-interval"
- "purgeability-taptoradar-lastdate"
- "setShowInLockScreen:"
- "shouldAttemptMiCOnByDefault"
- "v48@0:8@\"NSString\"16@\"NSString\"24B32B36q40"
- "v48@0:8@16@24B32B36q40"
- "v52@0:8@16@24B32B36q40B48"
- "v72@0:8@16@24@32@40@48C56@60B68"

```
