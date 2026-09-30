## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1402.300.181.2.14
-  __TEXT.__text: 0x11c26c
-  __TEXT.__auth_stubs: 0x2830
+1402.300.181.2.19
+  __TEXT.__text: 0x11c218
+  __TEXT.__auth_stubs: 0x2820
   __TEXT.__objc_methlist: 0x37d4
   __TEXT.__const: 0xb6a
   __TEXT.__cstring: 0x395b1

   __TEXT.__objc_methtype: 0x23ae
   __TEXT.__objc_stubs: 0xdc40
   __DATA_CONST.__got: 0xe90
-  __DATA_CONST.__const: 0x10f60
+  __DATA_CONST.__const: 0x10f38
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110

   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x190
-  __AUTH_CONST.__auth_got: 0x1428
+  __AUTH_CONST.__auth_got: 0x1420
   __AUTH_CONST.__auth_ptr: 0xf8
   __AUTH_CONST.__const: 0x1a70
   __AUTH_CONST.__cfstring: 0x10ca0

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 4549
-  Symbols:   2358
+  Symbols:   2357
   CStrings:  7455
 
Symbols:
- _IMMessageCreateBalloonPluginAssociatedMessageGUIDFromThreadIdentifier
CStrings:
+ "SELECT   m.ROWID FROM   message m WHERE   m.associated_message_guid = ?  AND m.thread_originator_guid IS NULL"
- "SELECT   m.ROWID FROM   message m WHERE   m.associated_message_guid IN (?, ?)  AND m.thread_originator_guid IS NULL"

```
