## BiomePubSub

> `/System/Library/PrivateFrameworks/BiomePubSub.framework/Versions/A/BiomePubSub`

```diff

-250.0.0.3.0
-  __TEXT.__text: 0x43e94
-  __TEXT.__objc_methlist: 0x588c
+259.0.0.0.0
+  __TEXT.__text: 0x43f64
+  __TEXT.__objc_methlist: 0x5894
   __TEXT.__const: 0x1010
   __TEXT.__cstring: 0x11bf
   __TEXT.__oslogstring: 0x6ec

   __TEXT.__swift5_assocty: 0x4b0
   __TEXT.__swift5_proto: 0xc8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x1280
+  __TEXT.__unwind_info: 0x1288
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16c8
+  __DATA_CONST.__objc_selrefs: 0x16d0
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__got: 0x3f8

   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__auth_got: 0x430
   __AUTH_CONST.__auth_ptr: 0x38
-  __AUTH.__objc_data: 0x1270
   __AUTH.__data: 0x580
   __DATA.__objc_ivar: 0x738
   __DATA.__data: 0x1210
   __DATA.__bss: 0x1690
-  __DATA_DIRTY.__objc_data: 0x1040
+  __DATA_DIRTY.__objc_data: 0x22b0
   __DATA_DIRTY.__data: 0x310
   __DATA_DIRTY.__bss: 0x2c0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2366
-  Symbols:   5073
+  Functions: 2367
+  Symbols:   5075
   CStrings:  219
 
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
~ -[BMBookmarkablePublisher validateBookmark:] : 8 -> 208
+ -[BMBookmarkablePublisher validateBookmarkValue:]
```
