## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1448.100.1.2.101
-  __TEXT.__text: 0xbcf74
+1450.200.35.2.5
+  __TEXT.__text: 0xbdda4
   __TEXT.__auth_stubs: 0x1b00
-  __TEXT.__objc_stubs: 0xc460
-  __TEXT.__objc_methlist: 0x2b7c
+  __TEXT.__objc_stubs: 0xc480
+  __TEXT.__objc_methlist: 0x2b84
   __TEXT.__const: 0xbf0
-  __TEXT.__gcc_except_tab: 0xb4e0
-  __TEXT.__cstring: 0x339d
-  __TEXT.__oslogstring: 0x16966
+  __TEXT.__gcc_except_tab: 0xb4f8
+  __TEXT.__cstring: 0x340d
+  __TEXT.__oslogstring: 0x16b66
   __TEXT.__objc_classname: 0x548
-  __TEXT.__objc_methname: 0x1253e
+  __TEXT.__objc_methname: 0x125fa
   __TEXT.__objc_methtype: 0x2955
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x662

   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2388
+  __TEXT.__unwind_info: 0x2398
   __TEXT.__eh_frame: 0x930
   __DATA_CONST.__auth_got: 0xd90
   __DATA_CONST.__got: 0xfe8

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_const: 0x32a8
-  __DATA.__objc_selrefs: 0x39f8
+  __DATA.__objc_selrefs: 0x3a10
   __DATA.__objc_ivar: 0x214
   __DATA.__objc_data: 0xa58
   __DATA.__data: 0xa50
-  __DATA.__bss: 0x7b0
+  __DATA.__bss: 0x7d0
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0588ABD3-D029-352D-B071-2EC511D11C62
-  Functions: 1667
+  UUID: 31947FFD-21CB-3B7D-B951-51F914900BD0
+  Functions: 1674
   Symbols:   860
-  CStrings:  5062
+  CStrings:  5074
 
Symbols:
+ _IMSetDomainIntForKey
- _dispatch_get_global_queue
CStrings:
+ "  Unable to reflect mark as reviewed, callerID is nil for account: %@"
+ "BackgroundProactiveRequestVersion"
+ "Could not find chat identifier %s or service name %s"
+ "Done proactively requesting backgrounds. Setting currentProactiveRequestVersion: %ld"
+ "Got %ld chats to request backgrounds for."
+ "Not proactively requesting backgrounds. currentProactiveRequestVersion: %ld, lastProactiveRequestVersion: %ld"
+ "Not requesting background for chat because its requestDateID is nil. Chat: %@"
+ "Requesting from %s to %s, on chat %@"
+ "TranscriptBackgrounds+BackgroundRequesting"
+ "callerURIForMessageGUID:idsAccount:"
+ "existingChatsFilteredUsingPredicate:sortedUsingLastMessageDateAscending:limit:"
+ "lastIncomingMessageForChatWithIdentifier:chatStyle:onService:"
+ "requestBackgroundsFromRecentChatsIfNeeded"
- "isScheduledMessagesCoreEnabled"

```
