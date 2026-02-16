## WatchListAssistant

> `/System/Library/Assistant/Plugins/WatchListAssistant.assistantBundle/WatchListAssistant`

```diff

-907.30.4.0.0
-  __TEXT.__text: 0x2960
+907.40.26.0.0
+  __TEXT.__text: 0x2af4
   __TEXT.__auth_stubs: 0x220
   __TEXT.__objc_stubs: 0xbe0
   __TEXT.__objc_methlist: 0x1ec

   - /System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FDF609C8-E4B0-3315-9285-0CE598D0680E
+  UUID: F2B6BCC9-E6E4-3F66-AD74-8925C3773A24
   Functions: 20
   Symbols:   297
   CStrings:  278
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x22
+ _objc_retain_x25
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x24
- _objc_retain_x8
Functions:
~ +[WLAPlayContent _WLKContentTypeForSAVCSContentType:] : 168 -> 172
~ -[WLAPlayContent performWithCompletion:] : 688 -> 700
~ ___40-[WLAPlayContent performWithCompletion:]_block_invoke : 352 -> 360
~ ___40-[WLAPlayContent performWithCompletion:]_block_invoke_2 : 872 -> 892
~ ___40-[WLAPlayContent performWithCompletion:]_block_invoke_3 : 184 -> 188
~ ___40-[WLAPlayContent performWithCompletion:]_block_invoke_4 : 212 -> 220
~ ___50-[WLAGetWatchListPlayables performWithCompletion:]_block_invoke : 1300 -> 1360
~ -[WLASearchPlayableContentFromWatchList performWithCompletion:] : 1104 -> 1148
~ ___63-[WLASearchPlayableContentFromWatchList performWithCompletion:]_block_invoke : 152 -> 156
~ ___63-[WLASearchPlayableContentFromWatchList performWithCompletion:]_block_invoke_2 : 1096 -> 1176
~ ___63-[WLASearchPlayableContentFromWatchList performWithCompletion:]_block_invoke_3 : 548 -> 560
~ +[WLASearchUtilities populateSearchResult:withMetadata:] : 440 -> 464
~ +[WLASearchUtilities populateSearchImage:withMetadata:artworkType:] : 216 -> 232
~ -[WLARemoveContentFromWatchList performWithCompletion:] : 828 -> 872
~ ___55-[WLARemoveContentFromWatchList performWithCompletion:]_block_invoke : 300 -> 304
~ ___55-[WLARemoveContentFromWatchList performWithCompletion:]_block_invoke_2 : 948 -> 976
~ ___55-[WLARemoveContentFromWatchList performWithCompletion:]_block_invoke_3 : 200 -> 208
~ -[WLAAddContentToWatchList performWithCompletion:] : 448 -> 468
~ ___50-[WLAAddContentToWatchList performWithCompletion:]_block_invoke : 312 -> 316

```
