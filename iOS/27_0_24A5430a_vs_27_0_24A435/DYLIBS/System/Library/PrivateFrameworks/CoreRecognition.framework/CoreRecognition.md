## CoreRecognition

> `/System/Library/PrivateFrameworks/CoreRecognition.framework/CoreRecognition`

```diff

 446.13.100.0.0
-  __TEXT.__text: 0x5b3cc
+  __TEXT.__text: 0x5b334
   __TEXT.__objc_methlist: 0x23ec
   __TEXT.__const: 0x744
   __TEXT.__cstring: 0x4b5f
Functions:
~ __ZN3CNNC2EP6CorpusP17NetworkParameters : 8764 -> 8784
~ __ZNSt3__16vectorIfNS_9allocatorIfEEE6resizeEm : 284 -> 288
~ __ZNSt3__16vectorIP5LayerIfffENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_ : 184 -> 176
~ +[ActivationMapTools textFromActivationMap:codeMap:invert:] : 2072 -> 2076
~ +[ActivationMapTools extractActivationSignals:fromActivationMap:forModel:codeMap:] : 1356 -> 1328
~ +[ActivationMapTools fitSpacingModel:toActivationMap:codeMap:minWordLengthFractionForCorrelationPeak:cost:] : 7516 -> 7512
~ _extractDigitCodeImages : 4816 -> 4780
~ _matchAgainstContact : 4420 -> 4320
~ -[CRMLModel(Activations) activationsFromImage:] : 2044 -> 2048
~ __ZN8CTCLayer22pathDecodingCTCSegmentE17FieldDecodingTypePKi : 4468 -> 4452
~ __ZN8CTCLayer14setActivationsENSt3__16vectorINS1_INS1_IfNS0_9allocatorIfEEEENS2_IS4_EEEENS2_IS6_EEEE : 936 -> 940
~ +[GeometricCutTools geometricRecognitionOf:inDerotatedRegion:withPadding:fromCorrectedBoundingBox:inImageWithSize:withCodeMap:activations:invert:networkInputSize:] : 5184 -> 5188
```
