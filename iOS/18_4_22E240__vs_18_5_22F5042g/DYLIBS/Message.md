## Message

> `/System/Library/PrivateFrameworks/Message.framework/Message`

```diff

-3826.500.181.2.5
-  __TEXT.__text: 0xab3748
+3826.600.15.2.1
+  __TEXT.__text: 0xab409c
   __TEXT.__auth_stubs: 0x7ed0
-  __TEXT.__objc_methlist: 0x14144
-  __TEXT.__gcc_except_tab: 0x38824
-  __TEXT.__const: 0x62de8
-  __TEXT.__cstring: 0x30d7e
+  __TEXT.__objc_methlist: 0x1416c
+  __TEXT.__gcc_except_tab: 0x388d8
+  __TEXT.__const: 0x62e60
+  __TEXT.__cstring: 0x30ede
   __TEXT.__oslogstring: 0x24760
   __TEXT.__ustring: 0x23ca
-  __TEXT.__swift5_typeref: 0x1228f
+  __TEXT.__swift5_typeref: 0x122af
   __TEXT.__swift5_capture: 0x32174
-  __TEXT.__constg_swiftt: 0xd5ec
+  __TEXT.__constg_swiftt: 0xd620
   __TEXT.__swift5_builtin: 0xd70
-  __TEXT.__swift5_reflstr: 0xe989
-  __TEXT.__swift5_fieldmd: 0x146bc
+  __TEXT.__swift5_reflstr: 0xe9a9
+  __TEXT.__swift5_fieldmd: 0x146e4
   __TEXT.__swift5_assocty: 0x1b40
-  __TEXT.__swift5_proto: 0x279c
-  __TEXT.__swift5_types: 0x175c
+  __TEXT.__swift5_proto: 0x27a0
+  __TEXT.__swift5_types: 0x1760
   __TEXT.__swift5_protos: 0x74
   __TEXT.__swift5_mpenum: 0x7a8
-  __TEXT.__unwind_info: 0x20a80
-  __TEXT.__eh_frame: 0x1e8ec
+  __TEXT.__unwind_info: 0x20ab8
+  __TEXT.__eh_frame: 0x1e874
   __TEXT.__objc_classname: 0x2a35
-  __TEXT.__objc_methname: 0x2e6bb
+  __TEXT.__objc_methname: 0x2e6d7
   __TEXT.__objc_methtype: 0x67c5
-  __TEXT.__objc_stubs: 0x24740
-  __DATA_CONST.__got: 0x2db0
+  __TEXT.__objc_stubs: 0x24760
+  __DATA_CONST.__got: 0x2dc8
   __DATA_CONST.__const: 0x155e0
   __DATA_CONST.__objc_classlist: 0xb30
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x548
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb5a8
+  __DATA_CONST.__objc_selrefs: 0xb5b0
   __DATA_CONST.__objc_protorefs: 0x1c0
   __DATA_CONST.__objc_superrefs: 0x678
   __DATA_CONST.__objc_arraydata: 0xf58
   __AUTH_CONST.__auth_got: 0x3f80
-  __AUTH_CONST.__auth_ptr: 0x30e8
-  __AUTH_CONST.__const: 0xa7ad8
+  __AUTH_CONST.__auth_ptr: 0x3110
+  __AUTH_CONST.__const: 0xa7af8
   __AUTH_CONST.__cfstring: 0x184e0
-  __AUTH_CONST.__objc_const: 0x229b0
+  __AUTH_CONST.__objc_const: 0x22a38
   __AUTH_CONST.__objc_arrayobj: 0xb88
-  __AUTH_CONST.__objc_intobj: 0xa20
+  __AUTH_CONST.__objc_intobj: 0xa08
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0x52e8
   __AUTH.__data: 0xb080
-  __DATA.__objc_ivar: 0x13a4
-  __DATA.__data: 0xec68
+  __DATA.__objc_ivar: 0x13a8
+  __DATA.__data: 0xec70
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x4e470
+  __DATA.__bss: 0x4e4f0
   __DATA.__common: 0xec0
   __DATA_DIRTY.__objc_data: 0x1860
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 52281
-  Symbols:   14310
-  CStrings:  17322
+  Functions: 52300
+  Symbols:   14317
+  CStrings:  17325
 
Symbols:
+ _EMPersistenceStatisticsKeyMessagesToRedonate
+ _EMPersistenceStatisticsKeyPercentUnindexedBodiesInFrecentMailboxes
+ _EMPersistenceStatisticsKeyRemoteMessagesToRedonate
CStrings:
+ "/AppleInternal/Library/BuildRoots/3ad7e567-0958-11f0-a889-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECFlagChangeMessageActionResults.h"
+ "/AppleInternal/Library/BuildRoots/3ad7e567-0958-11f0-a889-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageAction.h"
+ "/AppleInternal/Library/BuildRoots/3ad7e567-0958-11f0-a889-de23e2c06a38/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageActionResults.h"
+ "SELECT COUNT(*) AS indexable_messages,       SUM(CASE WHEN messages.searchable_message IS NULL THEN 1 ELSE 0 END) AS messages_to_index,       SUM(CASE WHEN messages.searchable_message IS NOT NULL then 1 ELSE 0 END) as indexed_messages,       SUM(CASE WHEN searchable_messages.message_body_indexed then 1 ELSE 0 END) as message_bodies_indexed,       SUM(CASE WHEN searchable_messages.transaction_id = %lld THEN 1 ELSE 0 END) AS messages_to_redonate,       SUM(CASE WHEN NOT searchable_messages.message_body_indexed AND messages.mailbox IN (%@) THEN 1 ELSE 0 END) as unindexed_message_bodies_in_frecents  FROM messages       LEFT OUTER JOIN searchable_messages ON messages.searchable_message = searchable_messages.ROWID WHERE deleted = '0' %@"
+ "com.apple.email.MFSearchableIndexManager_iOS.contentProtectionQueue"
+ "messagesToRedonate"
+ "senderForUnsubscribeMessage"
- "/AppleInternal/Library/BuildRoots/5d1ee3e9-00b3-11f0-8d26-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECFlagChangeMessageActionResults.h"
- "/AppleInternal/Library/BuildRoots/5d1ee3e9-00b3-11f0-8d26-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageAction.h"
- "/AppleInternal/Library/BuildRoots/5d1ee3e9-00b3-11f0-8d26-c2c15871b32e/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/System/Library/PrivateFrameworks/EmailCore.framework/Headers/ECTransferMessageActionResults.h"
- "SELECT COUNT(*) AS indexable_messages,       SUM(CASE WHEN messages.searchable_message IS NULL THEN 1 ELSE 0 END) AS messages_to_index,       SUM(CASE WHEN messages.searchable_message IS NOT NULL then 1 ELSE 0 END) as indexed_messages,       SUM(CASE WHEN searchable_messages.message_body_indexed then 1 ELSE 0 END) as message_bodies_indexed  FROM messages       LEFT OUTER JOIN searchable_messages ON messages.searchable_message = searchable_messages.ROWID WHERE deleted = '0' %@"

```
