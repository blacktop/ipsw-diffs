## MediaServices

> `/System/Library/PrivateFrameworks/MediaServices.framework/Versions/A/MediaServices`

```diff

-  __TEXT.__text: 0x5c734
+  __TEXT.__text: 0x5c72c
   __TEXT.__objc_methlist: 0x5784
   __TEXT.__const: 0x3ac
   __TEXT.__dlopen_cstrs: 0x70
-  __TEXT.__gcc_except_tab: 0xff4
-  __TEXT.__cstring: 0x5d80
+  __TEXT.__gcc_except_tab: 0x1008
+  __TEXT.__cstring: 0x5dad
   __TEXT.__oslogstring: 0x2c0a
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x16e0
+  __TEXT.__unwind_info: 0x16f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x2fa8
+  __DATA_CONST.__objc_selrefs: 0x2fb0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x138
   __DATA_CONST.__got: 0x658
-  __AUTH_CONST.__const: 0x1930
-  __AUTH_CONST.__cfstring: 0x57e0
+  __AUTH_CONST.__const: 0x1950
+  __AUTH_CONST.__cfstring: 0x5800
   __AUTH_CONST.__objc_const: 0x9c68
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0xf18
-  __AUTH.__objc_data: 0x15e0
+  __AUTH.__objc_data: 0x18b0
   __AUTH.__data: 0xc8
   __DATA.__objc_ivar: 0x6b8
   __DATA.__data: 0x740
-  __DATA.__bss: 0x19c
-  __DATA_DIRTY.__objc_data: 0x910
+  __DATA.__bss: 0x1b0
+  __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2137
-  Symbols:   5497
-  CStrings:  1781
+  Functions: 2138
+  Symbols:   5503
+  CStrings:  1783
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ GCC_except_table2084
+ GCC_except_table2090
+ __ZZL28MSVArtworkColorAnalysisQueuevE5queue
+ __ZZL28MSVArtworkColorAnalysisQueuevE5token
+ ____ZL28MSVArtworkColorAnalysisQueuev_block_invoke
+ _objc_msgSend$addOperationWithBlock:
- GCC_except_table2088
Functions:
~ __ZN13ImageAnalyzer19PickBackgroundColorEv : 536 -> 532
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERPFb22sortQuantizeColorEntryS2_EPS2_Lb0EEEvT1_S7_T0_NS_15iterator_traitsIS7_E15difference_typeEb : 7840 -> 7808
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERPFb22sortQuantizeColorEntryS2_EPS2_EEbT1_S7_T0_ : 2320 -> 2296
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERPFb14sortColorEntryS2_EPS2_Lb0EEEvT1_S7_T0_NS_15iterator_traitsIS7_E15difference_typeEb : 5672 -> 5652
~ __ZNSt3__127__insertion_sort_incompleteB9nqe220106INS_17_ClassicAlgPolicyERPFb14sortColorEntryS2_EPS2_EEbT1_S7_T0_ : 1644 -> 1624
~ -[NSError(MSVErrorAdditions) msv_codeDescription] : 416 -> 408
~ -[NSError(MSVErrorAdditions) msv_signature] : 3540 -> 3524
~ __MSVPropertyListEncoderAppendCharacters : 412 -> 400
~ _carrayBestIndex : 240 -> 232
~ -[MSVSQLDatabaseTransaction initWithConnection:name:error:] : 4452 -> 4444
~ -[MSVSQLDatabaseTransaction commit] : 4068 -> 4060
~ -[MSVSQLDatabaseTransaction rollback] : 4068 -> 4060
~ -[_MSVSQLConnection initWithDatabaseURI:options:error:] : 4896 -> 4888
~ -[_MSVSQLConnection statementWithString:error:] : 8176 -> 8160
~ -[MSVArtworkColorAnalyzer analyzeWithCompletionHandler:] : 200 -> 272
+ ____ZL28MSVArtworkColorAnalysisQueuev_block_invoke
CStrings:
+ "com.apple.MediaServices.artworkColorAnalysis"

```
