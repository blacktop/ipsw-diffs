## SafariShared

> `/System/iOSSupport/System/Library/PrivateFrameworks/SafariShared.framework/Versions/A/SafariShared`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-624.4.5.11.5
-  __TEXT.__text: 0x189ba4
+624.5.1.11.2
+  __TEXT.__text: 0x189bd8
   __TEXT.__auth_stubs: 0x22d0
   __TEXT.__objc_methlist: 0x123e4
   __TEXT.__const: 0x543f2
-  __TEXT.__gcc_except_tab: 0x1d420
+  __TEXT.__gcc_except_tab: 0x1d424
   __TEXT.__cstring: 0x1939a
   __TEXT.__ustring: 0xcb4a
   __TEXT.__oslogstring: 0xf422

   __TEXT.__swift5_protos: 0x8
   __TEXT.__unwind_info: 0xacb8
   __TEXT.__objc_classname: 0x2d7b
-  __TEXT.__objc_methname: 0x34112
+  __TEXT.__objc_methname: 0x34142
   __TEXT.__objc_methtype: 0xa02b
   __TEXT.__objc_stubs: 0x1c020
   __DATA_CONST.__got: 0x13d8
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
~ -[WBSBrowserTabCompletionProvider _matchesForQuery:tabInfos:selectedTabInfo:forQueryID:] : 984 -> 1008
~ ___88-[WBSBrowserTabCompletionProvider _matchesForQuery:tabInfos:selectedTabInfo:forQueryID:]_block_invoke : 16 -> 20
~ -[WBSBrowserTabCompletionProvider _compareTabMatch:otherTabMatch:] -> -[WBSBrowserTabCompletionProvider _compareTabMatch:otherTabMatch:usingSelectedTabInfo:] : 664 -> 688
CStrings:
+ "21624.5.1.11.2"
+ "_compareTabMatch:otherTabMatch:usingSelectedTabInfo:"
+ "_distanceFromSelectedTabForTabMatch:usingSelectedTabInfo:"
- "21624.4.5.11.5"
- "_compareTabMatch:otherTabMatch:"
- "_distanceFromSelectedTabForTabMatch:"
```
