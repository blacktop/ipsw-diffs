## CalendarDaemon

> `/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon`

```diff

-1194.6.2.0.0
-  __TEXT.__text: 0x6bbb0
+1194.7.1.0.0
+  __TEXT.__text: 0x6bc28
   __TEXT.__auth_stubs: 0x3700
-  __TEXT.__objc_methlist: 0x5d2c
+  __TEXT.__objc_methlist: 0x5d3c
   __TEXT.__cstring: 0x6dad
   __TEXT.__const: 0x150
-  __TEXT.__oslogstring: 0x7fa2
+  __TEXT.__oslogstring: 0x7ff1
   __TEXT.__gcc_except_tab: 0x19f0
   __TEXT.__dlopen_cstrs: 0xc0
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x1980
   __TEXT.__objc_classname: 0x143c
-  __TEXT.__objc_methname: 0xe09a
+  __TEXT.__objc_methname: 0xe0bb
   __TEXT.__objc_methtype: 0x640a
   __TEXT.__objc_stubs: 0x92c0
   __DATA_CONST.__got: 0x998

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ef0
+  __DATA_CONST.__objc_selrefs: 0x2ef8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x280
   __DATA_CONST.__objc_arraydata: 0x350
   __AUTH_CONST.__auth_got: 0x1b90
   __AUTH_CONST.__const: 0x840
   __AUTH_CONST.__cfstring: 0x76a0
-  __AUTH_CONST.__objc_const: 0xb8f0
+  __AUTH_CONST.__objc_const: 0xb908
   __AUTH_CONST.__objc_intobj: 0x420
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 52903E7B-E1E5-3879-8508-0E87169D0A9B
-  Functions: 2050
-  Symbols:   8568
-  CStrings:  5360
+  UUID: B60B5ACE-6C70-3295-A61D-237AC1D6F536
+  Functions: 2051
+  Symbols:   8571
+  CStrings:  5363
 
Symbols:
+ +[CADSpotlightIndexer calDBChangeFetchBatchSize]
+ __OBJC_$_CLASS_PROP_LIST_CADSpotlightIndexer
+ ___41-[CADSpotlightIndexer _incrementalUpdate]_block_invoke.cold.7
- _OUTLINED_FUNCTION_8
Functions:
~ ___41-[CADSpotlightIndexer _incrementalUpdate]_block_invoke : 1196 -> 1240
+ +[CADSpotlightIndexer calDBChangeFetchBatchSize]
~ _OUTLINED_FUNCTION_4 : 32 -> 12
~ _OUTLINED_FUNCTION_6 : 12 -> 16
~ _OUTLINED_FUNCTION_7 : 16 -> 32
- _OUTLINED_FUNCTION_8
~ ___41-[CADSpotlightIndexer _incrementalUpdate]_block_invoke.cold.5 : 124 -> 52
+ ___41-[CADSpotlightIndexer _incrementalUpdate]_block_invoke.cold.6
~ ___40-[CADSpotlightIndexer _deleteFromIndex:]_block_invoke.cold.1 : 116 -> 128
~ ___61-[CADSpotlightIndexer _sendSpotlightUpdates:deletes:toIndex:]_block_invoke.148.cold.1 : 116 -> 128
~ -[CADSpotlightIndexer reindexAllItemsForBundleID:protectionClass:acknowledgementHandler:].cold.1 : 108 -> 120
~ -[CADSpotlightIndexer provideDataForBundleID:protectionClass:itemIdentifier:typeIdentifier:options:completionHandler:].cold.1 : 108 -> 120
CStrings:
+ "Failed to get personaID for aux database, not advancing change sequence number"
+ "Ti,R,N"
+ "calDBChangeFetchBatchSize"

```
