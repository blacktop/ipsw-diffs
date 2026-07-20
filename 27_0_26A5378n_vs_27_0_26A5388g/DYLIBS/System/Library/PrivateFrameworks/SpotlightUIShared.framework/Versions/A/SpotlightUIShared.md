## SpotlightUIShared

> `/System/Library/PrivateFrameworks/SpotlightUIShared.framework/Versions/A/SpotlightUIShared`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_reflstr`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__data`
- `__DATA.__objc_stublist`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-236.0.4.0.0
-  __TEXT.__text: 0xfdeec
-  __TEXT.__objc_methlist: 0x1358
-  __TEXT.__const: 0xae8c
-  __TEXT.__cstring: 0x3d78
+236.0.11.401.0
+  __TEXT.__text: 0x1003c4
+  __TEXT.__objc_methlist: 0x13c0
+  __TEXT.__const: 0xaf4c
+  __TEXT.__cstring: 0x3e08
   __TEXT.__gcc_except_tab: 0xd0
-  __TEXT.__oslogstring: 0x17e2
+  __TEXT.__oslogstring: 0x19d2
   __TEXT.__ustring: 0x7de
-  __TEXT.__swift5_typeref: 0x396c
+  __TEXT.__swift5_typeref: 0x39b2
   __TEXT.__swift5_reflstr: 0x1f38
-  __TEXT.__swift5_assocty: 0xbf8
+  __TEXT.__swift5_assocty: 0xc10
   __TEXT.__constg_swiftt: 0x3c98
-  __TEXT.__swift5_fieldmd: 0x23fc
-  __TEXT.__swift5_proto: 0x828
+  __TEXT.__swift5_fieldmd: 0x2408
+  __TEXT.__swift5_proto: 0x834
   __TEXT.__swift5_types: 0x364
-  __TEXT.__swift_as_entry: 0x5e0
-  __TEXT.__swift_as_ret: 0x558
+  __TEXT.__swift_as_entry: 0x5e4
+  __TEXT.__swift_as_ret: 0x55c
   __TEXT.__swift_as_cont: 0x818
   __TEXT.__swift5_protos: 0xa8
   __TEXT.__swift5_capture: 0x8bc
   __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_mpenum: 0x38
-  __TEXT.__unwind_info: 0x47d8
-  __TEXT.__eh_frame: 0x99ac
+  __TEXT.__unwind_info: 0x4838
+  __TEXT.__eh_frame: 0x99d4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x5a0
-  __DATA_CONST.__objc_classlist: 0x228
+  __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0xa8
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c98
+  __DATA_CONST.__objc_selrefs: 0x1ce0
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x1240
-  __AUTH_CONST.__const: 0x78c9
-  __AUTH_CONST.__cfstring: 0x9c0
-  __AUTH_CONST.__objc_const: 0x4010
+  __DATA_CONST.__got: 0x1260
+  __AUTH_CONST.__const: 0x79b1
+  __AUTH_CONST.__cfstring: 0x9e0
+  __AUTH_CONST.__objc_const: 0x4128
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1da0
-  __AUTH.__objc_data: 0x12f8
+  __AUTH_CONST.__auth_got: 0x1db8
+  __AUTH.__objc_data: 0x1348
   __AUTH.__data: 0x28c8
   __DATA.__objc_ivar: 0x88
-  __DATA.__data: 0x1b10
+  __DATA.__data: 0x1b98
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0xc540
+  __DATA.__bss: 0xc600
   __DATA.__common: 0x170
   __DATA_DIRTY.__objc_data: 0xcd0
   __DATA_DIRTY.__data: 0x17e0
-  __DATA_DIRTY.__bss: 0x37a0
+  __DATA_DIRTY.__bss: 0x3820
   __DATA_DIRTY.__common: 0x78
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams
   - /System/Library/PrivateFrameworks/Calculate.framework/Versions/A/Calculate
+  - /System/Library/PrivateFrameworks/CoreParsec.framework/Versions/A/CoreParsec
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/Versions/A/FeatureFlags
   - /System/Library/PrivateFrameworks/IntentsFoundation.framework/Versions/A/IntentsFoundation
   - /System/Library/PrivateFrameworks/LinkMetadata.framework/Versions/A/LinkMetadata

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5627
-  Symbols:   3273
-  CStrings:  532
+  Functions: 5663
+  Symbols:   3312
+  CStrings:  545
 
Symbols:
+ +[SUISCardLoader sharedSpotlightCardLoader]
+ +[SUISCardLoader spotlightPARSession]
+ -[SUISCardLoader canLoadCard:]
+ -[SUISCardLoader loadCard:completionHandler:]
+ _OBJC_CLASS_$_PARSession
+ _OBJC_CLASS_$_PARSessionConfiguration
+ _OBJC_CLASS_$_SUISCardLoader
+ _OBJC_METACLASS_$_SUISCardLoader
+ __OBJC_$_CLASS_METHODS_SUISCardLoader
+ __OBJC_$_INSTANCE_METHODS_SUISCardLoader
+ __OBJC_$_PROP_LIST_SUISCardLoader
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFCardResourceLoader
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFCardResourceLoader
+ __OBJC_$_PROTOCOL_REFS_SFCardResourceLoader
+ __OBJC_CLASS_PROTOCOLS_$_SUISCardLoader
+ __OBJC_CLASS_RO_$_SUISCardLoader
+ __OBJC_LABEL_PROTOCOL_$_SFCardResourceLoader
+ __OBJC_METACLASS_RO_$_SUISCardLoader
+ __OBJC_PROTOCOL_$_SFCardResourceLoader
+ ___37+[SUISCardLoader spotlightPARSession]_block_invoke
+ ___43+[SUISCardLoader sharedSpotlightCardLoader]_block_invoke
+ ___45-[SUISCardLoader loadCard:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e28_v24?0"SFCard"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSArray"8l
+ ___copy_helper_block_e8_32b
+ ___copy_helper_block_e8_32s40s48s
+ ___destroy_helper_block_e8_32s40s48s
+ _associated conformance 17SpotlightUIShared11LogCategoryOs12CaseIterableAA8AllCasessADP_Sl
+ _objc_msgSend$initWithId:userAgent:factory:
+ _objc_msgSend$loadCard:withCompletionHandler:
+ _objc_msgSend$removeAttribute:range:
+ _objc_msgSend$sessionWithConfiguration:
+ _objc_msgSend$spotlightPARSession
+ _symbolic Say_____G 17SpotlightUIShared11LogCategoryO
+ _symbolic ___________t 17SpotlightUIShared11LogCategoryO 2os6LoggerV
+ _symbolic _____y__________G s18_DictionaryStorageC 17SpotlightUIShared11LogCategoryO 2os6LoggerV
+ _symbolic _____y___________tG s23_ContiguousArrayStorageC 17SpotlightUIShared11LogCategoryO 2os6LoggerV
+ sharedSpotlightCardLoader.onceToken
+ sharedSpotlightCardLoader.shared
+ spotlightPARSession.gSession
+ spotlightPARSession.onceToken
- __73-[SUISPasteboardManager _deleteExpiredItemsAndDispatchForNextExpiration:]_block_invoke_2
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSArray"8l
CStrings:
+ "            cardSections("
+ "        results("
+ "Duplicate values for key: '"
+ "Swift/NativeDictionary.swift"
+ "collecting expired pasteboard item for deletion hash:%@ title:%{sensitive}@"
+ "deleting continuity pasteboard items domain:%{public}@"
+ "deleting expired pasteboard items (%lu) hashes:%@"
+ "deleting pasteboard domains (%lu): %@"
+ "error: %@ indexing pasteboard item hash:%@"
+ "fetched pasteboard item hash:%@ title:%{sensitive}@"
+ "finished deleting continuity pasteboard items"
+ "finished deleting expired pasteboard items by hash"
+ "finished deleting pasteboard domains"
+ "finished indexing pasteboard item hash:%@"
+ "fte"
+ "got attributes: %lu for hash:%@ title:%{sensitive}@"
+ "indexing pasteboard item hash:%@ domain:%@ title:%{sensitive}@"
+ "slow-fetching attributes for re-copied pasteboard item hash:%@"
+ "spotlight/1.0"
+ "v24@?0@\"SFCard\"8@\"NSError\"16"
- "        results: [\n"
- "Deleting expired domains (%lu)"
- "Deleting expired items (%lu)"
- "error: %@ indexing pasteboard item :%@"
- "finished indexing pasteboard contents"
- "got attributes: %lu"
- "indexing pasteboard contents"
```
