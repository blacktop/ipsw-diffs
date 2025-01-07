## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1402.400.112.0.0
+1402.400.122.0.0
   __TEXT.__text: 0x11c370
   __TEXT.__auth_stubs: 0x2820
   __TEXT.__objc_methlist: 0x37d4
   __TEXT.__const: 0xb6a
-  __TEXT.__cstring: 0x39631
+  __TEXT.__cstring: 0x39671
   __TEXT.__oslogstring: 0x1a265
   __TEXT.__gcc_except_tab: 0xe510
   __TEXT.__ustring: 0x434
CStrings:
+ "SELECT   m.ROWID FROM   message m INNER JOIN  chat_message_join cmj ON cmj.message_id = m.ROWID WHERE   m.associated_message_guid = ?  AND m.thread_originator_guid IS NULL"
- "SELECT   m.ROWID FROM   message m WHERE   m.associated_message_guid = ?  AND m.thread_originator_guid IS NULL"

```
