## IMDPersistence

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence`

```diff

-1450.600.61.2.7
-  __TEXT.__text: 0x265454
-  __TEXT.__auth_stubs: 0x4f20
-  __TEXT.__objc_methlist: 0x7ff4
-  __TEXT.__const: 0xc888
-  __TEXT.__cstring: 0x48e94
-  __TEXT.__oslogstring: 0x1e9b6
-  __TEXT.__gcc_except_tab: 0xb6c0
+1450.700.11.2.3
+  __TEXT.__text: 0x265d84
+  __TEXT.__auth_stubs: 0x4f40
+  __TEXT.__objc_methlist: 0x809c
+  __TEXT.__const: 0xc848
+  __TEXT.__cstring: 0x49014
+  __TEXT.__oslogstring: 0x1ea46
+  __TEXT.__gcc_except_tab: 0xb6ec
   __TEXT.__ustring: 0x434
   __TEXT.__dlopen_cstrs: 0x30a
-  __TEXT.__swift5_typeref: 0x3fb8
-  __TEXT.__swift5_capture: 0x1284
-  __TEXT.__constg_swiftt: 0x5864
+  __TEXT.__swift5_typeref: 0x3f8a
+  __TEXT.__swift5_capture: 0x123c
+  __TEXT.__constg_swiftt: 0x586c
   __TEXT.__swift5_builtin: 0x2a8
   __TEXT.__swift5_reflstr: 0x3249
   __TEXT.__swift5_fieldmd: 0x359c

   __TEXT.__swift5_proto: 0x74c
   __TEXT.__swift5_types: 0x3b0
   __TEXT.__swift5_protos: 0x4c
-  __TEXT.__swift_as_entry: 0xb4
-  __TEXT.__swift_as_ret: 0xb0
+  __TEXT.__swift_as_entry: 0xac
+  __TEXT.__swift_as_ret: 0xa8
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0x95c0
-  __TEXT.__eh_frame: 0x8b88
+  __TEXT.__unwind_info: 0x95d0
+  __TEXT.__eh_frame: 0x8a80
   __TEXT.__objc_classname: 0x28fa
-  __TEXT.__objc_methname: 0x1bcf5
+  __TEXT.__objc_methname: 0x1be45
   __TEXT.__objc_methtype: 0x4667
-  __TEXT.__objc_stubs: 0x13e40
-  __DATA_CONST.__got: 0x1908
-  __DATA_CONST.__const: 0x8230
+  __TEXT.__objc_stubs: 0x13f80
+  __DATA_CONST.__got: 0x1920
+  __DATA_CONST.__const: 0x8228
   __DATA_CONST.__objc_classlist: 0x6d8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5898
+  __DATA_CONST.__objc_selrefs: 0x58e8
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x300
-  __AUTH_CONST.__auth_got: 0x27a0
-  __AUTH_CONST.__const: 0xadd8
-  __AUTH_CONST.__cfstring: 0x124c0
-  __AUTH_CONST.__objc_const: 0x119b8
+  __AUTH_CONST.__auth_got: 0x27b0
+  __AUTH_CONST.__const: 0xad90
+  __AUTH_CONST.__cfstring: 0x124e0
+  __AUTH_CONST.__objc_const: 0x119f0
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x22b0
-  __AUTH.__data: 0x4c20
+  __AUTH.__data: 0x4c30
   __DATA.__objc_ivar: 0x4d0
-  __DATA.__data: 0x34c0
-  __DATA.__bss: 0xae78
+  __DATA.__data: 0x34c8
+  __DATA.__bss: 0xae98
   __DATA.__common: 0x210
   __DATA_DIRTY.__objc_data: 0x1710
   __DATA_DIRTY.__data: 0x4138

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 34F6C827-E2DE-328C-B7DE-B00CCC3A8BAD
-  Functions: 11753
-  Symbols:   2659
-  CStrings:  12884
+  UUID: 2911E727-7A82-3533-960A-9851ED2C6E5A
+  Functions: 11766
+  Symbols:   2664
+  CStrings:  12899
 
Symbols:
+ _IMSharedMessageCustomAcknowledgementSummaryCreate
+ _IMSharedMessagePollAddChoiceSummaryCreate
+ _MDItemMessageFromKnownSender
+ _MDItemMessageRead
+ _MDItemOwnerIdentifier
CStrings:
+ "@\"NSArray\"16@?0@\"NSString\"8"
+ "POLL_FALLBACK"
+ "Prior ack for vote %@ (associatedGUID: %@): found %@ (type: %lld, associatedGUID: %@)"
+ "Prior ack for vote %@ (associatedGUID: %@): none found"
+ "SELECT guid, preview_generation_state, uti FROM attachment WHERE "
+ "SELECT m.ROWID, m.guid, m.attributedBody, m.balloon_bundle_id, m.message_summary_info, m.is_from_me, coalesce(h.id, h.uncanonicalized_id), m.associated_message_type\nFROM chat_message_join cmj\nINNER JOIN message m ON m.ROWID = cmj.message_id\nINNER JOIN chat c ON c.ROWID = cmj.chat_id\nLEFT JOIN handle h ON m.handle_id = h.rowid\nWHERE\n    cmj.message_id BETWEEN  ?  AND  ? \n    AND m.item_type = 0\n    AND (m.associated_message_type = 0 OR m.associated_message_type BETWEEN  ?  AND  ? )\n    AND c.is_blackholed = 0\n    AND COALESCE(c.is_filtered, 0) !=  ? "
+ "Summary:  Creating Poll message summary - message type is %lld"
+ "Summary:  Creating add choice summary"
+ "Summary:  Creating custom acknowledgement summary"
+ "UPDATE attachment\nSET preview_generation_state = 3, ck_sync_state = 0\nWHERE preview_generation_state IN (0, 5)"
+ "_baseItemForCustomAcknowledgement:"
+ "_priorAcknowledgementForCustomAcknowledgement:"
+ "_priorPollDefinitionForItem:"
+ "fetchMeContactWithKeys:"
+ "mostRecentPriorCustomAcknowledgementForItem:definitionItem:fetchAssociatedItemsBlock:"
+ "sentinelAttributeForAuxiliaryItem"
+ "sentinelAttributeForPrimaryItem"
+ "sentinelAttributesForAuxiliaryItems"
+ "sentinelAttributesForPrimaryItems"
- "\n    AND m.item_type = 0\n    AND (associated_message_type = 0 OR associated_message_type BETWEEN "
- " LIKE ?\nORDER BY "
- "Failed to check siblings for participant ROWID %lld: %@"
- "SELECT m.ROWID, m.guid, m.attributedBody, m.balloon_bundle_id, m.message_summary_info, m.is_from_me, coalesce(h.id, h.uncanonicalized_id), m.associated_message_type\nFROM message m\nLEFT JOIN handle h ON m.handle_id = h.rowid\nWHERE\n    m.ROWID BETWEEN "
- "Skipping participant ROWID %lld with address '%s' - already processed with siblings"

```
