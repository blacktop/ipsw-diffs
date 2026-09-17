## SpotlightUIShared

> `/System/Library/PrivateFrameworks/SpotlightUIShared.framework/Versions/A/SpotlightUIShared`

```diff

-236.0.21.401.0
-  __TEXT.__text: 0xf3e58
-  __TEXT.__objc_methlist: 0x13d0
-  __TEXT.__const: 0xb01c
-  __TEXT.__cstring: 0x3de8
+250.1.2.0.0
+  __TEXT.__text: 0xf4770
+  __TEXT.__objc_methlist: 0x13c0
+  __TEXT.__const: 0xb05c
+  __TEXT.__cstring: 0x3e08
   __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__oslogstring: 0x19b2
+  __TEXT.__oslogstring: 0x1a02
   __TEXT.__ustring: 0x7de
   __TEXT.__swift5_typeref: 0x39f2
   __TEXT.__swift5_reflstr: 0x1f98

   __TEXT.__constg_swiftt: 0x3d00
   __TEXT.__swift5_fieldmd: 0x244c
   __TEXT.__swift5_proto: 0x834
-  __TEXT.__swift5_types: 0x36c
+  __TEXT.__swift5_types: 0x370
   __TEXT.__swift_as_entry: 0x5e4
   __TEXT.__swift_as_ret: 0x55c
   __TEXT.__swift_as_cont: 0x818

   __TEXT.__swift5_capture: 0x8dc
   __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_mpenum: 0x34
-  __TEXT.__unwind_info: 0x5548
-  __TEXT.__eh_frame: 0x98b4
+  __TEXT.__unwind_info: 0x5550
+  __TEXT.__eh_frame: 0x98bc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cd0
+  __DATA_CONST.__objc_selrefs: 0x1cc8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x1250
-  __AUTH_CONST.__const: 0x7a89
-  __AUTH_CONST.__cfstring: 0xa80
-  __AUTH_CONST.__objc_const: 0x40f8
+  __AUTH_CONST.__const: 0x7a99
+  __AUTH_CONST.__cfstring: 0xae0
+  __AUTH_CONST.__objc_const: 0x40c8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1dd0
+  __AUTH_CONST.__auth_got: 0x1dd8
   __AUTH.__objc_data: 0x1348
   __AUTH.__data: 0x28c8
-  __DATA.__objc_ivar: 0x88
+  __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x1b98
   __DATA.__objc_stublist: 0x8
   __DATA.__common: 0x170
   __DATA_DIRTY.__objc_data: 0xcd0
   __DATA_DIRTY.__data: 0x1810
   __DATA_DIRTY.__bss: 0x3820
-  __DATA_DIRTY.__common: 0x78
+  __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Carbon.framework/Versions/A/Carbon

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5703
-  Symbols:   3314
-  CStrings:  547
+  Functions: 5709
+  Symbols:   3319
+  CStrings:  551
 
Symbols:
+ +[SUIUtilities isSearchFieldAutocorrectAlwaysEnabled]
+ SUISCorespotlightLog
+ SUISCorespotlightLog.log
+ SUISCorespotlightLog.once
+ _OUTLINED_FUNCTION_1
+ _SUISCorespotlightLog
+ __73-[SUISPasteboardManager _deleteExpiredItemsAndDispatchForNextExpiration:]_block_invoke_2
+ ___SUISCorespotlightLog_block_invoke
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSArray"8l
+ ___block_descriptor_49_e8_32s40s_e17_v16?0"NSError"8l
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0l
+ _swift_getDynamicType
- -[SUISPasteboardManager foundItems]
- -[SUISPasteboardManager setFoundItems:]
- OBJC_IVAR_$_SUISPasteboardManager._foundItems
- ___block_descriptor_40_e8_32s_e17_v16?0"NSArray"8l
- ___block_descriptor_41_e8_32s_e17_v16?0"NSError"8l
- ___block_descriptor_41_e8_32s_e5_v8?0l
- _objc_msgSend$foundItems
- _objc_msgSend$setFoundItems:
CStrings:
+ "QueryController: Starting query(%llu): %{sensitive}s browseMode: %s queryType: %s tokens: %s context: %s"
+ "com.apple.spotlight.clear.pasteboard.history"
+ "com.apple.spotlight.delete.pasteboard.expired"
+ "delete command had nothing to delete reason:%@"
+ "deleting domains (%lu) reason:%@ domains:%@"
+ "deleting files (%lu) reason:%@"
+ "deleting items (%lu) reason:%@ hashes:%@"
+ "expiration fetch failed with error: %@"
+ "failed to delete domains with error: %@"
+ "failed to delete files with error: %@"
+ "failed to delete items with error: %@"
+ "finished deleting domains reason:%@"
+ "finished deleting items by hash reason:%@"
+ "unspecified"
- "Deleting expired files (%lu)"
- "QueryController: Starting query(%llu): %{sensitive}s context: %s"
- "deleting expired pasteboard items (%lu) hashes:%@"
- "deleting pasteboard domains (%lu): %@"
- "failed to delete expired domains with error: %@"
- "failed to delete expired files with error: %@"
- "failed to delete expired items with error: %@"
- "finished deleting expired pasteboard items by hash"
- "finished deleting pasteboard domains"
- "title for suggestion section in files and apps browse"
```
