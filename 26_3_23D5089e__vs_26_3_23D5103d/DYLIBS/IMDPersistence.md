## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1450.400.3.2.1
-  __TEXT.__text: 0x23353c
+1450.400.13.2.1
+  __TEXT.__text: 0x2347c0
   __TEXT.__auth_stubs: 0x4770
-  __TEXT.__objc_methlist: 0x73cc
+  __TEXT.__objc_methlist: 0x73dc
   __TEXT.__const: 0xb648
-  __TEXT.__cstring: 0x4883b
+  __TEXT.__cstring: 0x489cb
   __TEXT.__oslogstring: 0x1e1d6
   __TEXT.__gcc_except_tab: 0xd0f0
   __TEXT.__ustring: 0x434

   __TEXT.__swift5_reflstr: 0x2b94
   __TEXT.__swift5_fieldmd: 0x2ebc
   __TEXT.__swift5_assocty: 0x548
-  __TEXT.__swift5_capture: 0x10e8
+  __TEXT.__swift5_capture: 0x1120
   __TEXT.__swift5_proto: 0x6d4
   __TEXT.__swift5_types: 0x340
   __TEXT.__swift5_protos: 0x3c
   __TEXT.__swift_as_entry: 0x7c
   __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x8b18
+  __TEXT.__unwind_info: 0x8b28
   __TEXT.__eh_frame: 0x7348
   __TEXT.__objc_classname: 0x11e5
-  __TEXT.__objc_methname: 0x17d57
-  __TEXT.__objc_methtype: 0x3823
-  __TEXT.__objc_stubs: 0x11d00
+  __TEXT.__objc_methname: 0x17dcb
+  __TEXT.__objc_methtype: 0x38a8
+  __TEXT.__objc_stubs: 0x11d20
   __DATA_CONST.__got: 0x1780
   __DATA_CONST.__const: 0x8470
   __DATA_CONST.__objc_classlist: 0x618
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5308
+  __DATA_CONST.__objc_selrefs: 0x5318
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x2f0
   __AUTH_CONST.__auth_got: 0x23c8
-  __AUTH_CONST.__const: 0xa018
+  __AUTH_CONST.__const: 0xa0a8
   __AUTH_CONST.__cfstring: 0x122e0
-  __AUTH_CONST.__objc_const: 0xf738
-  __AUTH_CONST.__objc_intobj: 0x108
+  __AUTH_CONST.__objc_const: 0xf740
+  __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x1d10

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1B7AAC03-707F-3C8B-BFFC-478B4AE0BC8E
-  Functions: 10815
+  UUID: 3D64D28D-329A-3374-8519-52114A20F216
+  Functions: 10825
   Symbols:   2589
-  CStrings:  12431
+  CStrings:  12443
 
CStrings:
+ " AND c.style =  ?  "
+ " AND cl.identifier =  ?  AND cl.domain =  ?  "
+ "AND EXISTS (\n    SELECT 1 FROM chat_service cs\n    WHERE cs.chat = c.rowid\n    AND cs.service IN "
+ "MAX(excluded.lane, persistent_tasks.lane)"
+ "ON CONFLICT (guid, flag)\nDO UPDATE SET\n    lane = "
+ "SELECT c.guid FROM chat c "
+ "SELECT chat_id FROM chat_handle_join \nWHERE handle_id IN (\n    SELECT ROWID FROM handle \n    WHERE id =  ? \n)"
+ "copyChatRecordsWithHandles:displayName:identifier:domain:style:everOnServices:completionHandler:"
+ "messageReadVersion"
+ "persistent_tasks(lane DESC, flag_group ASC, flag_priority DESC, reason_priority DESC, retry_count ASC)"
+ "persistent_tasks.lane"
+ "v72@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40q48@\"NSArray\"56@?<v@?@\"NSArray\"@\"NSError\">64"
+ "v72@0:8@16@24@32@40q48@56@?64"
- "ON CONFLICT (guid, flag)\nDO UPDATE SET\n    lane = MAX(excluded.lane, persistent_tasks.lane),\n    reason = "
- "persistent_tasks(lane DESC, flag_group ASC, flag_priority DESC, reason_priority DESC, retry_count ASC, ROWID ASC)"

```
