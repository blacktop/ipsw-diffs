## identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

-1926.600.41.0.0
-  __TEXT.__text: 0x713760
+1926.700.31.0.0
+  __TEXT.__text: 0x713a54
   __TEXT.__auth_stubs: 0x5550
-  __TEXT.__objc_stubs: 0x45720
-  __TEXT.__objc_methlist: 0x29650
-  __TEXT.__const: 0x42c40
-  __TEXT.__gcc_except_tab: 0x2a854
-  __TEXT.__objc_methname: 0x71436
-  __TEXT.__cstring: 0x5746f
-  __TEXT.__oslogstring: 0x7c35b
-  __TEXT.__objc_classname: 0x43cc
+  __TEXT.__objc_stubs: 0x45640
+  __TEXT.__objc_methlist: 0x29608
+  __TEXT.__const: 0x42d10
+  __TEXT.__gcc_except_tab: 0x2a858
+  __TEXT.__objc_methname: 0x71316
+  __TEXT.__cstring: 0x5741f
+  __TEXT.__oslogstring: 0x7c25b
+  __TEXT.__objc_classname: 0x43a4
   __TEXT.__objc_methtype: 0x11b63
   __TEXT.__ustring: 0x4ca
   __TEXT.__dlopen_cstrs: 0xea

   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift5_assocty: 0x240
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xfae0
+  __TEXT.__unwind_info: 0xfad8
   __TEXT.__eh_frame: 0x4c14
   __DATA_CONST.__auth_got: 0x2ab8
   __DATA_CONST.__got: 0x3430
-  __DATA_CONST.__auth_ptr: 0x710
+  __DATA_CONST.__auth_ptr: 0x738
   __DATA_CONST.__const: 0x1ce58
-  __DATA_CONST.__cfstring: 0x34500
-  __DATA_CONST.__objc_classlist: 0xec0
+  __DATA_CONST.__cfstring: 0x344c0
+  __DATA_CONST.__objc_classlist: 0xeb8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x768
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x118
-  __DATA_CONST.__objc_superrefs: 0xb68
+  __DATA_CONST.__objc_superrefs: 0xb60
   __DATA_CONST.__objc_intobj: 0x19f8
   __DATA_CONST.__objc_arraydata: 0x640
   __DATA_CONST.__objc_arrayobj: 0x378
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x40870
-  __DATA.__objc_selrefs: 0x155d0
-  __DATA.__objc_ivar: 0x31ec
-  __DATA.__objc_data: 0xb678
-  __DATA.__data: 0xa2a8
+  __DATA.__objc_const: 0x40748
+  __DATA.__objc_selrefs: 0x155a0
+  __DATA.__objc_ivar: 0x31e0
+  __DATA.__objc_data: 0xb628
+  __DATA.__data: 0xa218
   __DATA.__bss: 0x9480
   __DATA.__common: 0x480
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 8D1ED5E6-3C6E-3A6C-B3E7-35BCD3B057DC
-  Functions: 20551
+  UUID: 782FF656-6911-31DF-BDC5-C1ABF62F7983
+  Functions: 20545
   Symbols:   2647
-  CStrings:  40940
+  CStrings:  40922
 
CStrings:
+ "22:58:17"
+ "<%@> link:%@ reportNoSessionState:%@"
+ "CREATE INDEX IF NOT EXISTS incoming_message_message_identifier_idx ON incoming_message(message_identifier);"
+ "CREATE INDEX IF NOT EXISTS outgoing_message_similarity_idx ON outgoing_message(account_guid, priority, is_sent);"
+ "Jun  3 2025"
+ "SELECT ROWID, guid, topic, from_id, message_data, date, is_local, message_identifier, expiration_date, control_category FROM incoming_message WHERE message_identifier = ? LIMIT 1"
+ "link:reportNoSessionState:"
+ "provisionPsueudonymForURI -- sentinel alias is an invalid alias -- failing"
- "21:24:12"
- "Apr 20 2025"
- "Finished capturing AutoBugCapture diagnostics for queued query refresh { context: %@, sessionID: %@, error: %@ }"
- "IDSPeerIDQueryHandlerCompletionsForURIs"
- "Query ID %@ queued behind query %@ for URIs: %@, original query start %@"
- "Query with ID %@ has been queued for %f seconds. Allowing next query to skip the queue to try to unblock."
- "SELECT ROWID, guid, topic, from_id, message_data, date, is_local, message_identifier, expiration_date, control_category FROM incoming_message WHERE message_identifier = ? "
- "T@\"NSDate\",&,N,V_queryStart"
- "T@\"NSMutableArray\",R,N,V_completionBlocks"
- "T@\"NSUUID\",&,N,V_queryIdentifier"
- "Triggering AutoBugCapture for queued query refresh, we think a query is stuck!"
- "We think a queued query is blocking the queue!"
- "_queryIdentifier"
- "_queryStart"
- "_triggerAutoBugCaptureForQueuedQueryRefresh"
- "id-query-refresh-queued-query-interval"
- "initWithCompletionArray:queryIdentifier:queryStart:"
- "queryIdentifier"
- "queryStart"
- "setQueryIdentifier:"
- "setQueryStart:"
- "timeToRefreshQueuedQuery"

```
