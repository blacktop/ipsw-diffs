## SearchUI

> `/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI`

```diff

-634.4.6.1.0
-  __TEXT.__text: 0xfc41c
+634.4.7.0.0
+  __TEXT.__text: 0xfc690
   __TEXT.__auth_stubs: 0x2e40
   __TEXT.__objc_methlist: 0x121e0
   __TEXT.__const: 0x3754

   __TEXT.__unwind_info: 0x4f50
   __TEXT.__eh_frame: 0x21e4
   __TEXT.__objc_classname: 0x36c7
-  __TEXT.__objc_methname: 0x2ad31
+  __TEXT.__objc_methname: 0x2ad41
   __TEXT.__objc_methtype: 0x7df8
   __TEXT.__objc_stubs: 0x21140
   __DATA_CONST.__got: 0x24a0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D0837596-D9FC-33DB-BE00-00C7862CE933
+  UUID: 34CC2B6C-890A-37D3-9019-E96D57E5AF30
   Functions: 6857
   Symbols:   21310
   CStrings:  9153
Symbols:
+ +[SnippetUIUtilities performSFCommand:sourceView:rowModel:delegate:]
+ _objc_msgSend$performSFCommand:sourceView:rowModel:delegate:
- +[SnippetUIUtilities performSFCommand:rowModel:delegate:]
- _objc_msgSend$performSFCommand:rowModel:delegate:
Functions:
~ -[SearchUICardSectionTableCell performSFCommand:] : 152 -> 156
~ -[SearchUICardSectionCollectionViewCell performSFCommand:] : 152 -> 156
~ -[SearchUICombinedCollectionViewCell performSFCommand:] : 152 -> 156
~ -[SearchUICombinedCardSectionTableCell performSFCommand:] : 152 -> 156
~ +[SnippetUIUtilities performSFCommand:rowModel:delegate:] -> +[SnippetUIUtilities performSFCommand:sourceView:rowModel:delegate:] : 220 -> 252
~ sub_1de43ef9c -> sub_1de4cdfcc : 4748 -> 4792
~ sub_1de4602fc -> sub_1de4ef358 : 784 -> 856
~ sub_1de46060c -> sub_1de4ef6b0 : 784 -> 856
~ sub_1de46101c -> sub_1de4f0108 : 4844 -> 4800
~ sub_1de462844 -> sub_1de4f1904 : 1156 -> 1140
~ sub_1de462cc8 -> sub_1de4f1d78 : 1136 -> 1120
~ sub_1de464988 -> sub_1de4f3a28 : 1512 -> 1588
~ sub_1de465028 -> sub_1de4f4114 : 312 -> 436
~ sub_1de465160 -> sub_1de4f42c8 : 1732 -> 1820
~ sub_1de4658d4 -> sub_1de4f4a94 : 384 -> 404
~ sub_1de465a54 -> sub_1de4f4c28 : 364 -> 488
~ sub_1de465be4 -> sub_1de4f4e34 : 480 -> 516
CStrings:
+ "performSFCommand:sourceView:rowModel:delegate:"
- "performSFCommand:rowModel:delegate:"

```
