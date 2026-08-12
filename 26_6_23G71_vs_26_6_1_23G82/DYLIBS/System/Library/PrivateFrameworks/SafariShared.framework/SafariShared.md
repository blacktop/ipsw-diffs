## SafariShared

> `/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-624.4.5.10.5
-  __TEXT.__text: 0x1b0020
+624.5.1.10.1
+  __TEXT.__text: 0x1b0058
   __TEXT.__auth_stubs: 0x24b0
   __TEXT.__objc_methlist: 0x1439c
   __TEXT.__const: 0x57f80
-  __TEXT.__gcc_except_tab: 0x1e598
+  __TEXT.__gcc_except_tab: 0x1e59c
   __TEXT.__cstring: 0x1cf95
   __TEXT.__ustring: 0xce62
   __TEXT.__oslogstring: 0x11922

   __TEXT.__unwind_info: 0xbb98
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0x33eb
-  __TEXT.__objc_methname: 0x3af08
+  __TEXT.__objc_methname: 0x3af38
   __TEXT.__objc_methtype: 0xa78b
   __TEXT.__objc_stubs: 0x1f8e0
   __DATA_CONST.__got: 0x1638
Symbols:
+ -[WBSBrowserTabCompletionProvider _compareTabMatch:otherTabMatch:usingSelectedTabInfo:]
+ -[WBSBrowserTabCompletionProvider _distanceFromSelectedTabForTabMatch:usingSelectedTabInfo:]
+ ___block_descriptor_48_ea8_32s40s_e71_q24?0"WBSBrowserTabCompletionMatch"8"WBSBrowserTabCompletionMatch"16ls32l8s40l8
+ _objc_msgSend$_compareTabMatch:otherTabMatch:usingSelectedTabInfo:
+ _objc_msgSend$_distanceFromSelectedTabForTabMatch:usingSelectedTabInfo:
- -[WBSBrowserTabCompletionProvider _compareTabMatch:otherTabMatch:]
- -[WBSBrowserTabCompletionProvider _distanceFromSelectedTabForTabMatch:]
- ___block_descriptor_40_ea8_32s_e71_q24?0"WBSBrowserTabCompletionMatch"8"WBSBrowserTabCompletionMatch"16ls32l8
- _objc_msgSend$_compareTabMatch:otherTabMatch:
- _objc_msgSend$_distanceFromSelectedTabForTabMatch:
Functions:
~ -[WBSBrowserTabCompletionProvider _matchesForQuery:tabInfos:selectedTabInfo:forQueryID:] : 1348 -> 1376
~ ___88-[WBSBrowserTabCompletionProvider _matchesForQuery:tabInfos:selectedTabInfo:forQueryID:]_block_invoke_2 : 16 -> 20
~ -[WBSBrowserTabCompletionProvider _compareTabMatch:otherTabMatch:] -> -[WBSBrowserTabCompletionProvider _compareTabMatch:otherTabMatch:usingSelectedTabInfo:] : 664 -> 688
CStrings:
+ "8624.5.1.10.1"
+ "_compareTabMatch:otherTabMatch:usingSelectedTabInfo:"
+ "_distanceFromSelectedTabForTabMatch:usingSelectedTabInfo:"
- "8624.4.5.10.5"
- "_compareTabMatch:otherTabMatch:"
- "_distanceFromSelectedTabForTabMatch:"
```
