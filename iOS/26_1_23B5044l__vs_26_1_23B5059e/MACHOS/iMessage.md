## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1450.200.35.2.5
-  __TEXT.__text: 0xbdda4
-  __TEXT.__auth_stubs: 0x1b00
-  __TEXT.__objc_stubs: 0xc480
+1450.200.75.0.0
+  __TEXT.__text: 0xbc5a0
+  __TEXT.__auth_stubs: 0x1b30
+  __TEXT.__objc_stubs: 0xc4c0
   __TEXT.__objc_methlist: 0x2b84
   __TEXT.__const: 0xbf0
-  __TEXT.__gcc_except_tab: 0xb4f8
-  __TEXT.__cstring: 0x340d
-  __TEXT.__oslogstring: 0x16b66
+  __TEXT.__gcc_except_tab: 0xabac
+  __TEXT.__cstring: 0x342d
+  __TEXT.__oslogstring: 0x16f96
   __TEXT.__objc_classname: 0x548
-  __TEXT.__objc_methname: 0x125fa
+  __TEXT.__objc_methname: 0x1262f
   __TEXT.__objc_methtype: 0x2955
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x662

   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2398
+  __TEXT.__unwind_info: 0x22e0
   __TEXT.__eh_frame: 0x930
-  __DATA_CONST.__auth_got: 0xd90
-  __DATA_CONST.__got: 0xfe8
+  __DATA_CONST.__auth_got: 0xda8
+  __DATA_CONST.__got: 0xff0
   __DATA_CONST.__auth_ptr: 0x170
-  __DATA_CONST.__const: 0x38a8
-  __DATA_CONST.__cfstring: 0x36a0
+  __DATA_CONST.__const: 0x38b0
+  __DATA_CONST.__cfstring: 0x37e0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_const: 0x32a8
-  __DATA.__objc_selrefs: 0x3a10
+  __DATA.__objc_selrefs: 0x3a28
   __DATA.__objc_ivar: 0x214
   __DATA.__objc_data: 0xa58
   __DATA.__data: 0xa50

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 31947FFD-21CB-3B7D-B951-51F914900BD0
-  Functions: 1674
-  Symbols:   860
-  CStrings:  5074
+  UUID: 8EC057F3-FD75-36F7-B571-41E76ACAD8D9
+  Functions: 1666
+  Symbols:   864
+  CStrings:  5102
 
Symbols:
+ _IMAttachmentsLogHandle
+ _IMBalloonBundleIdentifierSafetyMonitor
+ _IMDisableFilteringProcessing
+ _IMMessagePushHandlerLogHandle
CStrings:
+ "   isFromTrustedSender: %@"
+ "Attempting to update group photo with invalid chat item type. transferGuid: %@, itemGuid: %@"
+ "Attempting to update photo with an invalid group action item. transferGuid: %@, itemGuid: %@"
+ "Attempting to update photo with an older group action item. transferGuid: %@, itemGuid: %@"
+ "E"
+ "Group photo message parsed: isExplicitlyRequestedResponse: %d, isExplicitResponseThatWeDidNotRequest: %d, isExplicitRefresh: %d, isLegacyRequestedResponse: %d, isExplicitlyNewPhoto: %d, isAssumedLegacyNewPhoto: %d, isForMissingLocalTransfer: %d"
+ "Overriding isHidden to show because we are missing the item locally. transferGuid: %@, itemGuid: %@"
+ "P"
+ "Pm"
+ "Received message {\n   IDSIncomingMessageDecryptedData = \"<data of length %lu>\"\n   IDSIncomingMessageOriginalEncryptionType = %@\n   IDSIncomingMessagePushPayload = {\n       E = %@\n       P = \"<data of length %lu>\"\n       Pm = \"<data of length %lu>\"\n       U = \"<data of length %lu>\"\n       c = %ld\n       cdr = \"<data of length %lu>\"\n       cdv = %ld\n       di = %ld\n       e = %lu\n       eX = %ld\n       htu = %ld\n       nr = %lu\n       sP = %@\n       skU = \"<data of length %lu>\"\n       t = \"<data of length %lu>\"\n       tP = %@\n       v = %ld\n       \"x-internal\" = %ld\n   }\n   mid = %@\n} for service %@  context: %p  fromID: %@"
+ "We already have an item for guid: %@, and it is not a IMGroupActionItem. That shouldn't be possible. Generating a new GUID to prevent us overwriting an existing message with an IMGroupActionItem. New guid: %@ Existing item: %@"
+ "actionType"
+ "cdr"
+ "cdv"
+ "di"
+ "eX"
+ "htu"
+ "nr"
+ "setSpamDetectedMessage:"
+ "unsignedLongValue"
+ "x-internal"
- "Group photo message parsed: isExplicitlyRequestedResponse: %d, isExplicitResponseThatWeDidNotRequest: %d, isExplicitRefresh: %d, isLegacyRequestedResponse: %d, isExplicitlyNewPhoto: %d, isAssumedLegacyNewPhoto: %d"
- "Received message %@ for service %@  context: %p, fromID: %@, "
- "We've already created a status item for this transfer, and the new one is hidden. Don't process as we won't handle it later anyway. transferGuid: %@, itemGuid: %@"

```
