## Email

> `/System/Library/PrivateFrameworks/Email.framework/Email`

```diff

-3864.600.1.2.3
-  __TEXT.__text: 0xd947c
+3864.600.31.2.1
+  __TEXT.__text: 0xd9ae8
   __TEXT.__auth_stubs: 0x14d0
   __TEXT.__objc_methlist: 0xcda4
-  __TEXT.__gcc_except_tab: 0x1b7f8
+  __TEXT.__gcc_except_tab: 0x1b8f4
   __TEXT.__const: 0x1240
-  __TEXT.__cstring: 0xb7bc
-  __TEXT.__oslogstring: 0x6313
+  __TEXT.__cstring: 0xb7cc
+  __TEXT.__oslogstring: 0x6353
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__ustring: 0x154
   __TEXT.__swift5_typeref: 0x385

   __TEXT.__swift5_capture: 0x38
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x8050
+  __TEXT.__unwind_info: 0x8070
   __TEXT.__eh_frame: 0x1b0
   __TEXT.__objc_classname: 0x1b5b
-  __TEXT.__objc_methname: 0x1bdf4
+  __TEXT.__objc_methname: 0x1bde4
   __TEXT.__objc_methtype: 0x4861
   __TEXT.__objc_stubs: 0x12620
-  __DATA_CONST.__got: 0xc58
-  __DATA_CONST.__const: 0x4350
+  __DATA_CONST.__got: 0xc60
+  __DATA_CONST.__const: 0x4378
   __DATA_CONST.__objc_classlist: 0x580
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x348
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6110
+  __DATA_CONST.__objc_selrefs: 0x6108
   __DATA_CONST.__objc_protorefs: 0x118
   __DATA_CONST.__objc_superrefs: 0x480
   __DATA_CONST.__objc_arraydata: 0x1e8
   __AUTH_CONST.__auth_got: 0xa78
   __AUTH_CONST.__const: 0x18c8
-  __AUTH_CONST.__cfstring: 0x9fe0
+  __AUTH_CONST.__cfstring: 0xa020
   __AUTH_CONST.__objc_const: 0x16bb0
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0x108

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 86E0BE13-5CE1-34DB-8645-3667E824C020
-  Functions: 4861
-  Symbols:   18110
-  CStrings:  8604
+  UUID: 1E5D9D04-B1F7-323B-A851-2AAF0BEB68BD
+  Functions: 4863
+  Symbols:   18118
+  CStrings:  8608
 
Symbols:
+ -[BMPruner(EMBiomeAdditions) pruneLogsExcludingQueryStrings:]
+ -[EMMailSearchQueryBiomeLogger pruneLogsExcludingQueryStrings:]
+ -[EMMessageRepository _updateObserversForSenderBlockingAction:]
+ GCC_except_table164
+ GCC_except_table185
+ GCC_except_table186
+ GCC_except_table187
+ GCC_except_table192
+ GCC_except_table193
+ GCC_except_table197
+ GCC_except_table202
+ GCC_except_table203
+ GCC_except_table207
+ GCC_except_table209
+ GCC_except_table214
+ GCC_except_table215
+ GCC_except_table220
+ GCC_except_table225
+ GCC_except_table226
+ GCC_except_table232
+ ___44-[EMMessageRepository metadataForAddresses:]_block_invoke.514
+ ___44-[EMMessageRepository metadataForAddresses:]_block_invoke.514.cold.1
+ ___54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.544
+ ___54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.544.cold.1
+ ___55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.523
+ ___55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.526
+ ___58-[EMMessageRepository cachedMetadataJSONForKey:messageID:]_block_invoke.509
+ ___61-[BMPruner(EMBiomeAdditions) pruneLogsExcludingQueryStrings:]_block_invoke
+ ___63-[EMMailSearchQueryBiomeLogger pruneLogsExcludingQueryStrings:]_block_invoke
+ ___63-[EMMessageRepository _updateObserversForSenderBlockingAction:]_block_invoke
+ ___63-[EMMessageRepository _updateObserversForSenderBlockingAction:]_block_invoke_2
+ ___block_descriptor_41_ea8_32s_e54_"EMMessageListItemChange"16?0"<EMMessageListItem>"8ls32l8
+ ___block_literal_global.506
+ ___block_literal_global.517
+ ___block_literal_global.562
+ ___block_literal_global.564
+ ___block_literal_global.566
+ _objc_msgSend$_updateObserversForSenderBlockingAction:
+ _objc_msgSend$pruneLogsExcludingQueryStrings:
- -[BMPruner(EMBiomeAdditions) pruneLogWithQueryString:]
- -[EMMailSearchQueryBiomeLogger _pruneBiomeLogForSuggestion:]
- -[EMMailSearchQueryBiomeLogger pruneLogForSuggestion:]
- GCC_except_table165
- GCC_except_table175
- GCC_except_table177
- GCC_except_table189
- GCC_except_table190
- GCC_except_table194
- GCC_except_table196
- GCC_except_table200
- GCC_except_table201
- GCC_except_table206
- GCC_except_table211
- GCC_except_table212
- GCC_except_table216
- GCC_except_table217
- GCC_except_table223
- GCC_except_table229
- ___44-[EMMessageRepository metadataForAddresses:]_block_invoke.513
- ___44-[EMMessageRepository metadataForAddresses:]_block_invoke.513.cold.1
- ___54-[BMPruner(EMBiomeAdditions) pruneLogWithQueryString:]_block_invoke
- ___54-[EMMailSearchQueryBiomeLogger pruneLogForSuggestion:]_block_invoke
- ___54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.543
- ___54-[EMMessageRepository persistentIDForMessageObjectID:]_block_invoke.543.cold.1
- ___55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.522
- ___55-[EMMessageRepository setUpURLCacheWithMemoryCapacity:]_block_invoke.525
- ___58-[EMMessageRepository cachedMetadataJSONForKey:messageID:]_block_invoke.508
- ___block_literal_global.505
- ___block_literal_global.516
- ___block_literal_global.553
- ___block_literal_global.556
- ___block_literal_global.558
- _objc_msgSend$_pruneBiomeLogForSuggestion:
- _objc_msgSend$pruneLogWithQueryString:
CStrings:
+ "<%p> Optimistic update for sender %{public}@ with %lu senders"
+ "Logs pruned excluding %lu query strings"
+ "_updateObserversForSenderBlockingAction:"
+ "blocking"
+ "pruneLogsExcludingQueryStrings:"
+ "unblocking"
- "Logs pruned for suggestion <%{public}p>"
- "_pruneBiomeLogForSuggestion:"
- "pruneLogForSuggestion:"
- "pruneLogWithQueryString:"

```
