## SafariShared

> `/System/Library/PrivateFrameworks/SafariShared.framework/Versions/A/SafariShared`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-624.4.5.11.5
-  __TEXT.__text: 0x1ea1f0
+624.5.1.11.2
+  __TEXT.__text: 0x1ea238
   __TEXT.__auth_stubs: 0x2520
   __TEXT.__objc_methlist: 0x154d4
   __TEXT.__const: 0x58490
-  __TEXT.__gcc_except_tab: 0x20300
+  __TEXT.__gcc_except_tab: 0x20304
   __TEXT.__cstring: 0x1e7a5
   __TEXT.__ustring: 0xce62
   __TEXT.__oslogstring: 0x12b32

   __TEXT.__unwind_info: 0xc6c8
   __TEXT.__eh_frame: 0x138
   __TEXT.__objc_classname: 0x377b
-  __TEXT.__objc_methname: 0x3d859
+  __TEXT.__objc_methname: 0x3d8a9
   __TEXT.__objc_methtype: 0xac0b
   __TEXT.__objc_stubs: 0x21320
   __DATA_CONST.__got: 0x1730
Symbols:
+ -[WBSBrowserTabCompletionProvider _compareTabMatch:otherTabMatch:usingSelectedTabInfo:]
+ -[WBSBrowserTabCompletionProvider _distanceFromSelectedTabForTabMatch:usingSelectedTabInfo:]
+ ___block_descriptor_48_ea8_32s40s_e71_q24?0"WBSBrowserTabCompletionMatch"8"WBSBrowserTabCompletionMatch"16l
+ _objc_msgSend$_compareTabMatch:otherTabMatch:usingSelectedTabInfo:
+ _objc_msgSend$_distanceFromSelectedTabForTabMatch:usingSelectedTabInfo:
- -[WBSBrowserTabCompletionProvider _compareTabMatch:otherTabMatch:]
- -[WBSBrowserTabCompletionProvider _distanceFromSelectedTabForTabMatch:]
- ___block_descriptor_40_ea8_32s_e71_q24?0"WBSBrowserTabCompletionMatch"8"WBSBrowserTabCompletionMatch"16l
- _objc_msgSend$_compareTabMatch:otherTabMatch:
- _objc_msgSend$_distanceFromSelectedTabForTabMatch:
Functions:
~ -[WBSBrowserTabCompletionProvider _matchesForQuery:tabInfos:selectedTabInfo:forQueryID:] : 1464 -> 1496
~ __88-[WBSBrowserTabCompletionProvider _matchesForQuery:tabInfos:selectedTabInfo:forQueryID:]_block_invoke.61 : 16 -> 20
~ -[WBSBrowserTabCompletionProvider _compareTabMatch:otherTabMatch:] -> -[WBSBrowserTabCompletionProvider _compareTabMatch:otherTabMatch:usingSelectedTabInfo:] : 716 -> 752
CStrings:
+ "21624.5.1.11.2"
+ "_compareTabMatch:otherTabMatch:usingSelectedTabInfo:"
+ "_distanceFromSelectedTabForTabMatch:usingSelectedTabInfo:"
- "21624.4.5.11.5"
- "_compareTabMatch:otherTabMatch:"
- "_distanceFromSelectedTabForTabMatch:"
```
