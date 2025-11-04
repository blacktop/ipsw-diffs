## CoreRecognition

> `/System/Library/PrivateFrameworks/CoreRecognition.framework/CoreRecognition`

```diff

-430.1.1.0.0
-  __TEXT.__text: 0x526c0
+430.2.0.0.0
+  __TEXT.__text: 0x526dc
   __TEXT.__auth_stubs: 0x1370
   __TEXT.__objc_methlist: 0x2204
   __TEXT.__const: 0x824

   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x2f1
   __TEXT.__objc_methname: 0x78f3
-  __TEXT.__objc_methtype: 0x1745
+  __TEXT.__objc_methtype: 0x1759
   __TEXT.__objc_stubs: 0x73e0
   __DATA_CONST.__got: 0x5c0
   __DATA_CONST.__const: 0xa18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A72D56DE-E16B-3815-863B-3788DB317958
+  UUID: FF645CC1-1FF4-3B37-85E2-E232CE0CAEC7
   Functions: 1063
   Symbols:   4369
   CStrings:  4780
Functions:
~ __ZNSt3__16vectorIiNS_9allocatorIiEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZN3CNN27scoreOneOutputEncodedVectorEjP10CNNSignals : 624 -> 628
~ __ZN3CNN9RecognizeEP6CorpusNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE : 4376 -> 4380
~ __ZN10CNNSignalsC2Ej : 1704 -> 1708
~ __ZNSt3__16vectorI6matrixIfENS_9allocatorIS2_EEE6resizeEm : 700 -> 704
~ __ZN6CorpusC2ERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEibbbjP6TagMapPKNS0_6vectorIdNS4_IdEEEESF_dd : 2400 -> 2392
~ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne200100Em : 60 -> 64
~ +[ActivationMapTools fitSpacingModel:toActivationMap:codeMap:minWordLengthFractionForCorrelationPeak:cost:] : 5552 -> 5548
~ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE11__vallocateB8ne200100Em : 76 -> 80
~ -[CRMLModel(Activations) activationsFromImage:] : 1988 -> 1992
~ __ZN8CTCLayer14setActivationsENSt3__16vectorINS1_INS1_IfNS0_9allocatorIfEEEENS2_IS4_EEEENS2_IS6_EEEE : 564 -> 568
CStrings:
+ "@132@0:8@16{vImage_Buffer=^vQQQ}24{CGPoint=dd}56@72{CGSize=dd}80^v96{vector<std::vector<std::vector<float>>, std::allocator<std::vector<std::vector<float>>>>=^v^v{?=^v}}104B128"
+ "@136@0:8@16{vImage_Buffer=^vQQQ}24{CGPoint=dd}56@72{CGSize=dd}80^v96{vector<std::vector<std::vector<float>>, std::allocator<std::vector<std::vector<float>>>>=^v^v{?=^v}}104B128S132"
+ "@148@0:8@16{vImage_Buffer=^vQQQ}24{CGPoint=dd}56@72{CGSize=dd}80r^i96{vector<std::vector<std::vector<float>>, std::allocator<std::vector<std::vector<float>>>>=^v^v{?=^v}}104B128{CGSize=dd}132"
+ "@152@0:8@16{vImage_Buffer=^vQQQ}24{CGPoint=dd}56@72{CGSize=dd}80r^i96{vector<std::vector<std::vector<float>>, std::allocator<std::vector<std::vector<float>>>>=^v^v{?=^v}}104B128{CGSize=dd}132S148"
+ "{vector<std::vector<std::vector<float>>, std::allocator<std::vector<std::vector<float>>>>=^v^v{?=^v}}24@0:8@16"
- "@132@0:8@16{vImage_Buffer=^vQQQ}24{CGPoint=dd}56@72{CGSize=dd}80^v96{vector<std::vector<std::vector<float>>, std::allocator<std::vector<std::vector<float>>>>=^v^v^v}104B128"
- "@136@0:8@16{vImage_Buffer=^vQQQ}24{CGPoint=dd}56@72{CGSize=dd}80^v96{vector<std::vector<std::vector<float>>, std::allocator<std::vector<std::vector<float>>>>=^v^v^v}104B128S132"
- "@148@0:8@16{vImage_Buffer=^vQQQ}24{CGPoint=dd}56@72{CGSize=dd}80r^i96{vector<std::vector<std::vector<float>>, std::allocator<std::vector<std::vector<float>>>>=^v^v^v}104B128{CGSize=dd}132"
- "@152@0:8@16{vImage_Buffer=^vQQQ}24{CGPoint=dd}56@72{CGSize=dd}80r^i96{vector<std::vector<std::vector<float>>, std::allocator<std::vector<std::vector<float>>>>=^v^v^v}104B128{CGSize=dd}132S148"
- "{vector<std::vector<std::vector<float>>, std::allocator<std::vector<std::vector<float>>>>=^v^v^v}24@0:8@16"

```
