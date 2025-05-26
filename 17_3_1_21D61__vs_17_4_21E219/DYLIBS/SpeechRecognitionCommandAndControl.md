## SpeechRecognitionCommandAndControl

> `/System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl`

```diff

-33.7.0.0.0
-  __TEXT.__text: 0x81008
+33.10.0.0.0
+  __TEXT.__text: 0x81068
   __TEXT.__auth_stubs: 0x1460
-  __TEXT.__objc_methlist: 0x8a58
+  __TEXT.__objc_methlist: 0x8a88
   __TEXT.__const: 0x3a0
   __TEXT.__oslogstring: 0x1cea
   __TEXT.__cstring: 0x6308

   __TEXT.__ustring: 0x4c
   __TEXT.__unwind_info: 0x21ac
   __TEXT.__objc_classname: 0x1588
-  __TEXT.__objc_methname: 0x1b623
-  __TEXT.__objc_methtype: 0x37a3
-  __TEXT.__objc_stubs: 0x12100
+  __TEXT.__objc_methname: 0x1b88f
+  __TEXT.__objc_methtype: 0x37c2
+  __TEXT.__objc_stubs: 0x12120
   __DATA_CONST.__got: 0x420
   __DATA_CONST.__const: 0x1400
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xc9a8
-  __DATA_CONST.__objc_selrefs: 0x6250
+  __DATA_CONST.__objc_const: 0xcca8
+  __DATA_CONST.__objc_selrefs: 0x6278
+  __DATA_CONST.__objc_classrefs: 0x860
+  __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x400
   __AUTH_CONST.__objc_const: 0x32a8
   __AUTH_CONST.__cfstring: 0x7520

   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__auth_got: 0xa40
   __AUTH.__objc_data: 0x2760
-  __DATA.__objc_classrefs: 0x858
-  __DATA.__objc_superrefs: 0x2a8
-  __DATA.__objc_ivar: 0x974
+  __DATA.__objc_ivar: 0x984
   __DATA.__data: 0x1430
   __DATA.__bss: 0x418
   __DATA.__common: 0x58

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/PrivateFrameworks/AACCore.framework/AACCore
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/AXMediaUtilities.framework/AXMediaUtilities
   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3446
-  Symbols:   12237
-  CStrings:  6167
+  Functions: 3450
+  Symbols:   12251
+  CStrings:  6189
 
Symbols:
+ -[CACCorrectionsCandidateViewStyle alternativeTextLeftSpacing]
+ -[CACCorrectionsCandidateViewStyle groupHeaderPadding]
+ -[CACCorrectionsCandidateViewStyle hideLinesOnDisambiguationGridEdges]
+ -[CACCorrectionsCandidateViewStyle maximizeSortControlWidthWithPadding]
+ _OBJC_CLASS_$_AEAssessmentModeGestalt
+ _OBJC_IVAR_$_CACCorrectionsCandidateViewStyle.alternativeTextLeftSpacing
+ _OBJC_IVAR_$_CACCorrectionsCandidateViewStyle.groupHeaderPadding
+ _OBJC_IVAR_$_CACCorrectionsCandidateViewStyle.hideLinesOnDisambiguationGridEdges
+ _OBJC_IVAR_$_CACCorrectionsCandidateViewStyle.maximizeSortControlWidthWithPadding
+ ___53-[CACSpokenCommandManager beginObservingApplications]_block_invoke.553
+ ____NotificationLiveMicrophoneDidTurnOnAfterInterruption_block_invoke.1530
+ ___block_literal_global.1495
+ ___block_literal_global.1497
+ ___block_literal_global.1499
+ ___block_literal_global.1501
+ ___block_literal_global.1506
+ ___block_literal_global.1529
+ ___block_literal_global.1532
+ ___block_literal_global.242
+ ___block_literal_global.244
+ ___block_literal_global.269
+ ___block_literal_global.271
+ ___block_literal_global.273
+ ___block_literal_global.275
+ ___block_literal_global.276
+ ___block_literal_global.279
+ ___block_literal_global.283
+ ___block_literal_global.285
+ ___block_literal_global.287
+ ___block_literal_global.289
+ ___block_literal_global.291
+ ___block_literal_global.294
+ ___block_literal_global.296
+ ___block_literal_global.298
+ ___block_literal_global.301
+ ___block_literal_global.304
+ ___block_literal_global.305
+ ___block_literal_global.306
+ ___block_literal_global.308
+ ___block_literal_global.310
+ ___block_literal_global.312
+ ___block_literal_global.314
+ ___block_literal_global.385
+ ___block_literal_global.441
+ ___block_literal_global.499
+ ___block_literal_global.511
+ ___block_literal_global.515
+ ___block_literal_global.528
+ ___block_literal_global.533
+ ___block_literal_global.538
+ ___block_literal_global.555
+ ___block_literal_global.576
+ ___block_literal_global.577
+ ___block_literal_global.583
+ ___block_literal_global.602
+ ___block_literal_global.614
+ ___block_literal_global.631
+ ___block_literal_global.639
+ ___block_literal_global.696
+ ___block_literal_global.704
+ ___block_literal_global.744
+ ___block_literal_global.861
+ __unnamed_array_storage.257
+ __unnamed_array_storage.530
+ __unnamed_array_storage.561
+ __unnamed_array_storage.701
+ __unnamed_array_storage.706
+ _objc_msgSend$isActive
- ___53-[CACSpokenCommandManager beginObservingApplications]_block_invoke.529
- ____NotificationLiveMicrophoneDidTurnOnAfterInterruption_block_invoke.1505
- ___block_literal_global.1470
- ___block_literal_global.1472
- ___block_literal_global.1474
- ___block_literal_global.1476
- ___block_literal_global.1479
- ___block_literal_global.1481
- ___block_literal_global.1507
- ___block_literal_global.213
- ___block_literal_global.215
- ___block_literal_global.218
- ___block_literal_global.220
- ___block_literal_global.223
- ___block_literal_global.225
- ___block_literal_global.227
- ___block_literal_global.228
- ___block_literal_global.229
- ___block_literal_global.231
- ___block_literal_global.233
- ___block_literal_global.235
- ___block_literal_global.241
- ___block_literal_global.243
- ___block_literal_global.245
- ___block_literal_global.270
- ___block_literal_global.272
- ___block_literal_global.274
- ___block_literal_global.280
- ___block_literal_global.282
- ___block_literal_global.284
- ___block_literal_global.286
- ___block_literal_global.288
- ___block_literal_global.290
- ___block_literal_global.361
- ___block_literal_global.417
- ___block_literal_global.475
- ___block_literal_global.487
- ___block_literal_global.491
- ___block_literal_global.504
- ___block_literal_global.509
- ___block_literal_global.514
- ___block_literal_global.531
- ___block_literal_global.552
- ___block_literal_global.553
- ___block_literal_global.559
- ___block_literal_global.578
- ___block_literal_global.590
- ___block_literal_global.607
- ___block_literal_global.615
- ___block_literal_global.672
- ___block_literal_global.680
- ___block_literal_global.720
- ___block_literal_global.837
- __unnamed_array_storage.233
- __unnamed_array_storage.506
- __unnamed_array_storage.537
- __unnamed_array_storage.677
- __unnamed_array_storage.682
CStrings:
+ "@\"UIButtonConfiguration\"16@0:8"
+ "T@\"NSString\",?,R,C"
+ "T@\"UIButtonConfiguration\",?,R,N"
+ "T@\"UIColor\",?,R,N"
+ "TB,?,R,N"
+ "TB,?,R,N,VhideLinesOnDisambiguationGridEdges"
+ "TB,?,R,N,VmaximizeSortControlWidthWithPadding"
+ "Td,?,R,N"
+ "Td,?,R,N,ValternativeTextLeftSpacing"
+ "T{UIEdgeInsets=dddd},?,R,N"
+ "T{UIEdgeInsets=dddd},?,R,N,VgroupHeaderPadding"
+ "alternativeTextLeftSpacing"
+ "arrowButtonConfig"
+ "arrowButtonHighlightBackgroundHidden"
+ "groupHeaderPadding"
+ "hideLinesOnDisambiguationGridEdges"
+ "isActive"
+ "maximizeSortControlWidthWithPadding"
+ "o\x0f\x04"
+ "performScalingAnimationOnCellHighlight"
+ "showCellBorderForSpaceConfirmationCandidate"
+ "spaceConfirmationCandidateCellBackgroundColor"
+ "widthOfGridGradient"
- "_\x0f\x04"

```
