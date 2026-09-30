## TSText

> `/System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSText.framework/TSText`

```diff

-481.0.0.0.0
-  __TEXT.__text: 0x248b50
+482.0.0.0.0
+  __TEXT.__text: 0x248824
   __TEXT.__auth_stubs: 0x3820
   __TEXT.__init_offsets: 0xc
   __TEXT.__objc_methlist: 0x106b8
-  __TEXT.__gcc_except_tab: 0x2ae64
+  __TEXT.__gcc_except_tab: 0x2ac78
   __TEXT.__const: 0x14d32
   __TEXT.__cstring: 0x21afc
   __TEXT.__ustring: 0x284

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_types: 0x4c
-  __TEXT.__unwind_info: 0xef68
-  __TEXT.__eh_frame: 0x128
+  __TEXT.__unwind_info: 0xf028
+  __TEXT.__eh_frame: 0x118
   __TEXT.__objc_classname: 0x17f9
-  __TEXT.__objc_methname: 0x231b2
-  __TEXT.__objc_methtype: 0x9fe4
+  __TEXT.__objc_methname: 0x230c0
+  __TEXT.__objc_methtype: 0x97c6
   __TEXT.__objc_stubs: 0x17560
-  __DATA_CONST.__got: 0xb68
-  __DATA_CONST.__const: 0x36b8
+  __DATA_CONST.__got: 0xb70
+  __DATA_CONST.__const: 0x3690
   __DATA_CONST.__objc_classlist: 0x5f0
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x2e0

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/EquationKit.framework/EquationKit
   - /System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSCollaborationKit.framework/TSCollaborationKit
   - /System/Library/PrivateFrameworks/iWorkImport.framework/Frameworks/TSDrawables.framework/TSDrawables

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: BDA47894-2D1B-3DE2-AEF9-39B92A93D253
-  Functions: 13780
-  Symbols:   7949
+  UUID: BA21A5FD-15E1-3979-83F2-50E7E1F182ED
+  Functions: 13813
+  Symbols:   7944
   CStrings:  10674
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _swift_coroFrameAlloc
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _swift_bridgeObjectRelease_n
CStrings:
+ "T{vector<_NSRange, std::allocator<_NSRange>>=^{_NSRange}^{_NSRange}^{_NSRange}},R,N,V_rangeVector"
+ "T{vector<_TSWPCharIndexAndAffinity, std::allocator<_TSWPCharIndexAndAffinity>>=^{_TSWPCharIndexAndAffinity}^{_TSWPCharIndexAndAffinity}^{_TSWPCharIndexAndAffinity}},N,V_mappedIndexes"
+ "T{vector<_TSWPCharIndexAndAffinity, std::allocator<_TSWPCharIndexAndAffinity>>=^{_TSWPCharIndexAndAffinity}^{_TSWPCharIndexAndAffinity}^{_TSWPCharIndexAndAffinity}},N,V_unmappedIndexes"
+ "v40@0:8{vector<_TSWPCharIndexAndAffinity, std::allocator<_TSWPCharIndexAndAffinity>>=^{_TSWPCharIndexAndAffinity}^{_TSWPCharIndexAndAffinity}^{_TSWPCharIndexAndAffinity}}16"
+ "{list<unsigned long, std::allocator<unsigned long>>=\"__end_\"{__list_node_base<unsigned long, void *>=\"__prev_\"^v\"__next_\"^v}\"__size_\"Q}"
+ "{map<unsigned long, TSWPFontMetricsCacheEntry, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, TSWPFontMetricsCacheEntry>>>=\"__tree_\"{__tree<std::__value_type<unsigned long, TSWPFontMetricsCacheEntry>, std::__map_value_compare<unsigned long, std::__value_type<unsigned long, TSWPFontMetricsCacheEntry>, std::less<unsigned long>>, std::allocator<std::__value_type<unsigned long, TSWPFontMetricsCacheEntry>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{map<unsigned long, std::shared_ptr<TSWPParagraphTypesetter>, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, std::shared_ptr<TSWPParagraphTypesetter>>>>=\"__tree_\"{__tree<std::__value_type<unsigned long, std::shared_ptr<TSWPParagraphTypesetter>>, std::__map_value_compare<unsigned long, std::__value_type<unsigned long, std::shared_ptr<TSWPParagraphTypesetter>>, std::less<unsigned long>>, std::allocator<std::__value_type<unsigned long, std::shared_ptr<TSWPParagraphTypesetter>>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{vector<CGPoint, std::allocator<CGPoint>>=\"__begin_\"^{CGPoint}\"__end_\"^{CGPoint}\"__cap_\"^{CGPoint}}"
+ "{vector<CGRect, std::allocator<CGRect>>=\"__begin_\"^{CGRect}\"__end_\"^{CGRect}\"__cap_\"^{CGRect}}"
+ "{vector<TSWPAttachmentPosition, std::allocator<TSWPAttachmentPosition>>=\"__begin_\"^{?}\"__end_\"^{?}\"__cap_\"^{?}}"
+ "{vector<TSWPDirtyRange, std::allocator<TSWPDirtyRange>>=\"__begin_\"^{?}\"__end_\"^{?}\"__cap_\"^{?}}"
+ "{vector<TSWPParagraphMetrics, std::allocator<TSWPParagraphMetrics>>=\"__begin_\"^{TSWPParagraphMetrics}\"__end_\"^{TSWPParagraphMetrics}\"__cap_\"^{TSWPParagraphMetrics}}"
+ "{vector<_NSRange, std::allocator<_NSRange>>=\"__begin_\"^{_NSRange}\"__end_\"^{_NSRange}\"__cap_\"^{_NSRange}}"
+ "{vector<_NSRange, std::allocator<_NSRange>>=^{_NSRange}^{_NSRange}^{_NSRange}}16@0:8"
+ "{vector<_TSWPCharIndexAndAffinity, std::allocator<_TSWPCharIndexAndAffinity>>=\"__begin_\"^{_TSWPCharIndexAndAffinity}\"__end_\"^{_TSWPCharIndexAndAffinity}\"__cap_\"^{_TSWPCharIndexAndAffinity}}"
+ "{vector<_TSWPCharIndexAndAffinity, std::allocator<_TSWPCharIndexAndAffinity>>=^{_TSWPCharIndexAndAffinity}^{_TSWPCharIndexAndAffinity}^{_TSWPCharIndexAndAffinity}}16@0:8"
+ "{vector<bool, std::allocator<bool>>=\"__begin_\"^Q\"__size_\"Q\"__cap_\"Q}"
+ "{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"__cap_\"^Q}"
+ "{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q}24@0:8^{TSWPAttributeArray=^^?^{TSWPAttributeRecord}@b32b8b1}16"
+ "{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q^Q}32@0:8@16@24"
+ "{vector<unsigned short, std::allocator<unsigned short>>=\"__begin_\"^S\"__end_\"^S\"__cap_\"^S}"
- "T{vector<_NSRange, std::allocator<_NSRange>>=^{_NSRange}^{_NSRange}{__compressed_pair<_NSRange *, std::allocator<_NSRange>>=^{_NSRange}}},R,N,V_rangeVector"
- "T{vector<_TSWPCharIndexAndAffinity, std::allocator<_TSWPCharIndexAndAffinity>>=^{_TSWPCharIndexAndAffinity}^{_TSWPCharIndexAndAffinity}{__compressed_pair<_TSWPCharIndexAndAffinity *, std::allocator<_TSWPCharIndexAndAffinity>>=^{_TSWPCharIndexAndAffinity}}},N,V_mappedIndexes"
- "T{vector<_TSWPCharIndexAndAffinity, std::allocator<_TSWPCharIndexAndAffinity>>=^{_TSWPCharIndexAndAffinity}^{_TSWPCharIndexAndAffinity}{__compressed_pair<_TSWPCharIndexAndAffinity *, std::allocator<_TSWPCharIndexAndAffinity>>=^{_TSWPCharIndexAndAffinity}}},N,V_unmappedIndexes"
- "v40@0:8{vector<_TSWPCharIndexAndAffinity, std::allocator<_TSWPCharIndexAndAffinity>>=^{_TSWPCharIndexAndAffinity}^{_TSWPCharIndexAndAffinity}{__compressed_pair<_TSWPCharIndexAndAffinity *, std::allocator<_TSWPCharIndexAndAffinity>>=^{_TSWPCharIndexAndAffinity}}}16"
- "{list<unsigned long, std::allocator<unsigned long>>=\"__end_\"{__list_node_base<unsigned long, void *>=\"__prev_\"^v\"__next_\"^v}\"__size_alloc_\"{__compressed_pair<unsigned long, std::allocator<std::__list_node<unsigned long, void *>>>=\"__value_\"Q}}"
- "{map<unsigned long, TSWPFontMetricsCacheEntry, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, TSWPFontMetricsCacheEntry>>>=\"__tree_\"{__tree<std::__value_type<unsigned long, TSWPFontMetricsCacheEntry>, std::__map_value_compare<unsigned long, std::__value_type<unsigned long, TSWPFontMetricsCacheEntry>, std::less<unsigned long>>, std::allocator<std::__value_type<unsigned long, TSWPFontMetricsCacheEntry>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<unsigned long, TSWPFontMetricsCacheEntry>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<unsigned long, std::__value_type<unsigned long, TSWPFontMetricsCacheEntry>, std::less<unsigned long>>>=\"__value_\"Q}}}"
- "{map<unsigned long, std::shared_ptr<TSWPParagraphTypesetter>, std::less<unsigned long>, std::allocator<std::pair<const unsigned long, std::shared_ptr<TSWPParagraphTypesetter>>>>=\"__tree_\"{__tree<std::__value_type<unsigned long, std::shared_ptr<TSWPParagraphTypesetter>>, std::__map_value_compare<unsigned long, std::__value_type<unsigned long, std::shared_ptr<TSWPParagraphTypesetter>>, std::less<unsigned long>>, std::allocator<std::__value_type<unsigned long, std::shared_ptr<TSWPParagraphTypesetter>>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<unsigned long, std::shared_ptr<TSWPParagraphTypesetter>>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<unsigned long, std::__value_type<unsigned long, std::shared_ptr<TSWPParagraphTypesetter>>, std::less<unsigned long>>>=\"__value_\"Q}}}"
- "{vector<CGPoint, std::allocator<CGPoint>>=\"__begin_\"^{CGPoint}\"__end_\"^{CGPoint}\"__end_cap_\"{__compressed_pair<CGPoint *, std::allocator<CGPoint>>=\"__value_\"^{CGPoint}}}"
- "{vector<CGRect, std::allocator<CGRect>>=\"__begin_\"^{CGRect}\"__end_\"^{CGRect}\"__end_cap_\"{__compressed_pair<CGRect *, std::allocator<CGRect>>=\"__value_\"^{CGRect}}}"
- "{vector<TSWPAttachmentPosition, std::allocator<TSWPAttachmentPosition>>=\"__begin_\"^{?}\"__end_\"^{?}\"__end_cap_\"{__compressed_pair<TSWPAttachmentPosition *, std::allocator<TSWPAttachmentPosition>>=\"__value_\"^{?}}}"
- "{vector<TSWPDirtyRange, std::allocator<TSWPDirtyRange>>=\"__begin_\"^{?}\"__end_\"^{?}\"__end_cap_\"{__compressed_pair<TSWPDirtyRange *, std::allocator<TSWPDirtyRange>>=\"__value_\"^{?}}}"
- "{vector<TSWPParagraphMetrics, std::allocator<TSWPParagraphMetrics>>=\"__begin_\"^{TSWPParagraphMetrics}\"__end_\"^{TSWPParagraphMetrics}\"__end_cap_\"{__compressed_pair<TSWPParagraphMetrics *, std::allocator<TSWPParagraphMetrics>>=\"__value_\"^{TSWPParagraphMetrics}}}"
- "{vector<_NSRange, std::allocator<_NSRange>>=\"__begin_\"^{_NSRange}\"__end_\"^{_NSRange}\"__end_cap_\"{__compressed_pair<_NSRange *, std::allocator<_NSRange>>=\"__value_\"^{_NSRange}}}"
- "{vector<_NSRange, std::allocator<_NSRange>>=^{_NSRange}^{_NSRange}{__compressed_pair<_NSRange *, std::allocator<_NSRange>>=^{_NSRange}}}16@0:8"
- "{vector<_TSWPCharIndexAndAffinity, std::allocator<_TSWPCharIndexAndAffinity>>=\"__begin_\"^{_TSWPCharIndexAndAffinity}\"__end_\"^{_TSWPCharIndexAndAffinity}\"__end_cap_\"{__compressed_pair<_TSWPCharIndexAndAffinity *, std::allocator<_TSWPCharIndexAndAffinity>>=\"__value_\"^{_TSWPCharIndexAndAffinity}}}"
- "{vector<_TSWPCharIndexAndAffinity, std::allocator<_TSWPCharIndexAndAffinity>>=^{_TSWPCharIndexAndAffinity}^{_TSWPCharIndexAndAffinity}{__compressed_pair<_TSWPCharIndexAndAffinity *, std::allocator<_TSWPCharIndexAndAffinity>>=^{_TSWPCharIndexAndAffinity}}}16@0:8"
- "{vector<bool, std::allocator<bool>>=\"__begin_\"^Q\"__size_\"Q\"__cap_alloc_\"{__compressed_pair<unsigned long, std::allocator<unsigned long>>=\"__value_\"Q}}"
- "{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"__end_cap_\"{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=\"__value_\"^Q}}"
- "{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=^Q}}24@0:8^{TSWPAttributeArray=^^?^{TSWPAttributeRecord}@b32b8b1}16"
- "{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=^Q}}32@0:8@16@24"
- "{vector<unsigned short, std::allocator<unsigned short>>=\"__begin_\"^S\"__end_\"^S\"__end_cap_\"{__compressed_pair<unsigned short *, std::allocator<unsigned short>>=\"__value_\"^S}}"

```
