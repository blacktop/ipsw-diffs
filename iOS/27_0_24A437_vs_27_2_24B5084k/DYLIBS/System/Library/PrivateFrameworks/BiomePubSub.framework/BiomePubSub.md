## BiomePubSub

> `/System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub`

```diff

-250.0.0.3.0
-  __TEXT.__text: 0x3e924
-  __TEXT.__objc_methlist: 0x588c
+255.0.2.0.0
+  __TEXT.__text: 0x3e9dc
+  __TEXT.__objc_methlist: 0x5894
   __TEXT.__const: 0x1000
   __TEXT.__cstring: 0x116f
   __TEXT.__oslogstring: 0x6ec

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16c8
+  __DATA_CONST.__objc_selrefs: 0x16d0
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__got: 0x3f8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2348
-  Symbols:   5086
+  Functions: 2349
+  Symbols:   5088
   CStrings:  218
 
Symbols:
+ -[BMBookmarkablePublisher validateBookmarkValue:]
+ -[BPSBuffer validateBookmarkValue:]
+ -[BPSCollect validateBookmarkValue:]
+ -[BPSFlatMap validateBookmarkValue:]
+ -[BPSMerge validateBookmarkValue:]
+ -[BPSMergeMany validateBookmarkValue:]
+ -[BPSMulticast validateBookmarkValue:]
+ -[BPSOrderedMerge validateBookmarkValue:]
+ -[BPSPassThroughSubject validateBookmarkValue:]
+ -[BPSSequence validateBookmarkValue:]
+ -[BPSWindower validateBookmarkValue:]
+ _objc_msgSend$validateBookmarkValue:
- -[BPSBuffer validateBookmark:]
- -[BPSCollect validateBookmark:]
- -[BPSFlatMap validateBookmark:]
- -[BPSMerge validateBookmark:]
- -[BPSMergeMany validateBookmark:]
- -[BPSMulticast validateBookmark:]
- -[BPSOrderedMerge validateBookmark:]
- -[BPSPassThroughSubject validateBookmark:]
- -[BPSSequence validateBookmark:]
- -[BPSWindower validateBookmark:]
Functions:
~ -[BMBookmarkablePublisher validateBookmark:] : 8 -> 184
- -[BPSOrderedMerge validateBookmark:]
+ -[BPSOrderedMerge validateBookmarkValue:]
+ -[BMBookmarkablePublisher validateBookmarkValue:]
```
