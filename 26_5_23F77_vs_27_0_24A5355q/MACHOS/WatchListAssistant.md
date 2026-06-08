## WatchListAssistant

> `/System/Library/Assistant/Plugins/WatchListAssistant.assistantBundle/WatchListAssistant`

```diff

-907.50.1.0.0
-  __TEXT.__text: 0x2af4
+950.0.0.0.0
+  __TEXT.__text: 0x2964
   __TEXT.__auth_stubs: 0x220
   __TEXT.__objc_stubs: 0xbe0
   __TEXT.__objc_methlist: 0x1ec

   __TEXT.__objc_methname: 0x79d
   __TEXT.__objc_methtype: 0x1cf
   __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x120
-  __DATA_CONST.__got: 0x188
   __DATA_CONST.__const: 0x190
   __DATA_CONST.__cfstring: 0x720
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x120
+  __DATA_CONST.__got: 0x188
   __DATA.__objc_const: 0x1068
   __DATA.__objc_selrefs: 0x3b8
   __DATA.__objc_data: 0x1e0

   - /System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 99075801-21E0-30CD-A48E-1992E6F08C00
+  UUID: 209A2F9A-AA6E-3829-BA14-C6287D1EE956
   Functions: 20
   Symbols:   297
   CStrings:  278
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x24
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x25
Functions:
~ +[WLAPlayContent _WLKContentTypeForSAVCSContentType:] : 172 -> 168
~ -[WLAPlayContent performWithCompletion:] : 700 -> 688
~ ___40-[WLAPlayContent performWithCompletion:]_block_invoke : 360 -> 352
~ ___40-[WLAPlayContent performWithCompletion:]_block_invoke_2 : 892 -> 872
~ ___40-[WLAPlayContent performWithCompletion:]_block_invoke_3 : 188 -> 184
~ ___40-[WLAPlayContent performWithCompletion:]_block_invoke_4 : 220 -> 212
~ ___50-[WLAGetWatchListPlayables performWithCompletion:]_block_invoke : 1360 -> 1304
~ -[WLASearchPlayableContentFromWatchList performWithCompletion:] : 1148 -> 1104
~ ___63-[WLASearchPlayableContentFromWatchList performWithCompletion:]_block_invoke : 156 -> 152
~ ___63-[WLASearchPlayableContentFromWatchList performWithCompletion:]_block_invoke_2 : 1176 -> 1104
~ ___63-[WLASearchPlayableContentFromWatchList performWithCompletion:]_block_invoke_3 : 560 -> 552
~ +[WLASearchUtilities populateSearchResult:withMetadata:] : 464 -> 440
~ +[WLASearchUtilities populateSearchImage:withMetadata:artworkType:] : 232 -> 216
~ -[WLARemoveContentFromWatchList performWithCompletion:] : 872 -> 828
~ ___55-[WLARemoveContentFromWatchList performWithCompletion:]_block_invoke : 304 -> 292
~ ___55-[WLARemoveContentFromWatchList performWithCompletion:]_block_invoke_2 : 976 -> 952
~ ___55-[WLARemoveContentFromWatchList performWithCompletion:]_block_invoke_3 : 208 -> 200
~ -[WLAAddContentToWatchList performWithCompletion:] : 468 -> 448
~ ___50-[WLAAddContentToWatchList performWithCompletion:]_block_invoke : 316 -> 304

```
