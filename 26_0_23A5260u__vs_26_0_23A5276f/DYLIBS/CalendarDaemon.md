## CalendarDaemon

> `/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon`

```diff

-1216.0.0.0.0
-  __TEXT.__text: 0x712e0
-  __TEXT.__auth_stubs: 0x37e0
-  __TEXT.__objc_methlist: 0x615c
-  __TEXT.__cstring: 0x6f3d
+1218.0.0.0.0
+  __TEXT.__text: 0x714cc
+  __TEXT.__auth_stubs: 0x3810
+  __TEXT.__objc_methlist: 0x617c
+  __TEXT.__cstring: 0x6f58
   __TEXT.__const: 0x150
-  __TEXT.__oslogstring: 0x81af
+  __TEXT.__oslogstring: 0x81fe
   __TEXT.__gcc_except_tab: 0x1ba4
   __TEXT.__dlopen_cstrs: 0xc0
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1a88
+  __TEXT.__unwind_info: 0x1a90
   __TEXT.__objc_classname: 0x1499
-  __TEXT.__objc_methname: 0xea03
+  __TEXT.__objc_methname: 0xea51
   __TEXT.__objc_methtype: 0x6620
-  __TEXT.__objc_stubs: 0x9b00
+  __TEXT.__objc_stubs: 0x9b40
   __DATA_CONST.__got: 0x9e8
   __DATA_CONST.__const: 0x1fe0
   __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3108
+  __DATA_CONST.__objc_selrefs: 0x3120
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x350
-  __AUTH_CONST.__auth_got: 0x1c00
+  __AUTH_CONST.__auth_got: 0x1c18
   __AUTH_CONST.__const: 0x880
-  __AUTH_CONST.__cfstring: 0x7980
-  __AUTH_CONST.__objc_const: 0xc0b8
+  __AUTH_CONST.__cfstring: 0x79a0
+  __AUTH_CONST.__objc_const: 0xc0d0
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: CC37E7F8-4582-34E7-B336-A0B7AA4132BA
-  Functions: 2146
-  Symbols:   8927
-  CStrings:  5539
+  UUID: 0A83EA98-6DD3-3FF7-94AD-9E457DFC7609
+  Functions: 2148
+  Symbols:   8937
+  CStrings:  5545
 
Symbols:
+ +[CADSpotlightIndexer calDBChangeFetchBatchSize]
+ -[CADSpotlightIndexer _spotlightRecurrenceId:]
+ _CalEventCopyDetachedEvents
+ _CalEventCopyOriginalEvent
+ _CalEventCopyRecurrenceSet
+ __OBJC_$_CLASS_PROP_LIST_CADSpotlightIndexer
+ ___41-[CADSpotlightIndexer _incrementalUpdate]_block_invoke.cold.7
+ ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.147
+ ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.147.cold.1
+ ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.151
+ ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.151.cold.1
+ ___99-[CADSpotlightIndexer reindexItemsWithIdentifiers:bundleID:protectionClass:acknowledgementHandler:]_block_invoke.196
+ _objc_msgSend$_spotlightRecurrenceId:
+ _objc_msgSend$setRelatedUniqueIdentifier:
- GCC_except_table42
- _OUTLINED_FUNCTION_8
- ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.144
- ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.144.cold.1
- ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.148
- ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.148.cold.1
- ___99-[CADSpotlightIndexer reindexItemsWithIdentifiers:bundleID:protectionClass:acknowledgementHandler:]_block_invoke.193
CStrings:
+ "Failed to get personaID for aux database, not advancing change sequence number"
+ "_spotlightRecurrenceId:"
+ "calDBChangeFetchBatchSize"
+ "has_recurrence_set_changed"
+ "setRelatedUniqueIdentifier:"

```
