## ContinuitySing

> `/System/Library/PrivateFrameworks/ContinuitySing.framework/ContinuitySing`

```diff

-664.0.0.0.2
-  __TEXT.__text: 0x51a68
-  __TEXT.__auth_stubs: 0x1710
-  __TEXT.__objc_methlist: 0x317c
-  __TEXT.__const: 0xba4
-  __TEXT.__gcc_except_tab: 0xb24
-  __TEXT.__cstring: 0x5259
-  __TEXT.__oslogstring: 0x28e9
+664.2.5.0.0
+  __TEXT.__text: 0x544bc
+  __TEXT.__auth_stubs: 0x1750
+  __TEXT.__objc_methlist: 0x32b4
+  __TEXT.__const: 0xbb4
+  __TEXT.__gcc_except_tab: 0xb60
+  __TEXT.__cstring: 0x54d9
+  __TEXT.__oslogstring: 0x2b89
   __TEXT.__ustring: 0x2a
-  __TEXT.__swift5_typeref: 0x906
+  __TEXT.__swift5_typeref: 0x90e
   __TEXT.__swift5_fieldmd: 0x328
   __TEXT.__constg_swiftt: 0x6d4
   __TEXT.__swift5_reflstr: 0x26a

   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_types: 0x40
   __TEXT.__swift_as_entry: 0x70
-  __TEXT.__swift_as_ret: 0x88
+  __TEXT.__swift_as_ret: 0x90
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__unwind_info: 0x1640
-  __TEXT.__eh_frame: 0xd50
-  __TEXT.__objc_classname: 0x7a6
-  __TEXT.__objc_methname: 0x9085
-  __TEXT.__objc_methtype: 0x1254
-  __TEXT.__objc_stubs: 0x7180
-  __DATA_CONST.__got: 0x910
-  __DATA_CONST.__const: 0x13a8
-  __DATA_CONST.__objc_classlist: 0x2a0
+  __TEXT.__unwind_info: 0x16a0
+  __TEXT.__eh_frame: 0xe18
+  __TEXT.__objc_classname: 0x7f7
+  __TEXT.__objc_methname: 0x944b
+  __TEXT.__objc_methtype: 0x12a5
+  __TEXT.__objc_stubs: 0x7560
+  __DATA_CONST.__got: 0x938
+  __DATA_CONST.__const: 0x13b0
+  __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2688
+  __DATA_CONST.__objc_selrefs: 0x2798
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x248
-  __AUTH_CONST.__auth_got: 0xb98
-  __AUTH_CONST.__const: 0x1178
-  __AUTH_CONST.__cfstring: 0x1dc0
-  __AUTH_CONST.__objc_const: 0x6948
-  __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0x1e58
+  __DATA_CONST.__objc_superrefs: 0x260
+  __DATA_CONST.__objc_arraydata: 0x20
+  __AUTH_CONST.__auth_got: 0xbb8
+  __AUTH_CONST.__const: 0x11f8
+  __AUTH_CONST.__cfstring: 0x1e80
+  __AUTH_CONST.__objc_const: 0x6d10
+  __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH.__objc_data: 0x1f98
   __AUTH.__data: 0x590
-  __DATA.__objc_ivar: 0x410
-  __DATA.__data: 0x900
+  __DATA.__objc_ivar: 0x434
+  __DATA.__data: 0x908
   __DATA.__bss: 0x858
   __DATA.__common: 0x68
   - /System/Library/Frameworks/AVKit.framework/AVKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CF977BEE-C2F1-30C5-BFB1-4872DC5E2BEA
-  Functions: 1699
-  Symbols:   5108
-  CStrings:  2929
+  UUID: C6A15B55-A588-32C0-A15F-EB517A75BC3C
+  Functions: 1732
+  Symbols:   5245
+  CStrings:  3018
 
Symbols:
+ +[CSStartSingingEvent messageID]
+ -[CSHelpPanelViewController _createViews].cold.1
+ -[CSHelpPanelViewController _linkWithAttributedString:textStyle:weight:color:]
+ -[CSHelpPanelViewController gameModeDescriptionLabel]
+ -[CSHelpPanelViewController setGameModeDescriptionLabel:]
+ -[CSLatencyCardResultView .cxx_destruct]
+ -[CSLatencyCardResultView _infoText]
+ -[CSLatencyCardResultView _progressBarOffset]
+ -[CSLatencyCardResultView _updateView]
+ -[CSLatencyCardResultView initWithLatency:]
+ -[CSLatencyCardResultView layoutSubviews]
+ -[CSLatencyCardResultView updateWithLatency:]
+ -[CSLatencyCardViewController _buttonTitleForCurrentState]
+ -[CSLatencyCardViewController _showLatencyCheckConfirmationIfNeededWithCompletion:]
+ -[CSLatencyCardViewController _updateContentViewFromCurrentState]
+ -[CSLatencyCardViewController failedInfoView]
+ -[CSLatencyCardViewController failedStateConstraints]
+ -[CSLatencyCardViewController resultView]
+ -[CSRemoteRequestClient sendStartSingingEvent]
+ -[CSSegmentedValue .cxx_destruct]
+ -[CSSegmentedValue initWithThresholds:value:]
+ -[CSSegmentedValue numberOfSegments]
+ -[CSSegmentedValue progressWithinSegment]
+ -[CSSegmentedValue segment]
+ -[CSSegmentedValue setProgressWithinSegment:]
+ -[CSSegmentedValue setSegment:]
+ -[CSSegmentedValue setThresholds:]
+ -[CSSegmentedValue setValue:]
+ -[CSSegmentedValue thresholds]
+ -[CSSegmentedValue updateSegmentAndProgress]
+ -[CSSegmentedValue value]
+ -[CSTipTriangleView drawRect:]
+ -[CSTipTriangleView init]
+ _NSLinkAttributeName
+ _OBJC_CLASS_$_CSLatencyCardResultView
+ _OBJC_CLASS_$_CSSegmentedValue
+ _OBJC_CLASS_$_CSStartSingingEvent
+ _OBJC_CLASS_$_CSTipTriangleView
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_UIProgressView
+ _OBJC_IVAR_$_CSHelpPanelViewController._gameModeDescriptionLabel
+ _OBJC_IVAR_$_CSLatencyCardResultView._infoLabel
+ _OBJC_IVAR_$_CSLatencyCardResultView._latencyLabel
+ _OBJC_IVAR_$_CSLatencyCardResultView._latencyTipTriangleCenterXOffset
+ _OBJC_IVAR_$_CSLatencyCardResultView._progressBars
+ _OBJC_IVAR_$_CSLatencyCardResultView._segmentedLatency
+ _OBJC_IVAR_$_CSLatencyCardViewController._failedInfoView
+ _OBJC_IVAR_$_CSLatencyCardViewController._failedStateConstraints
+ _OBJC_IVAR_$_CSLatencyCardViewController._resultView
+ _OBJC_IVAR_$_CSSegmentedValue._progressWithinSegment
+ _OBJC_IVAR_$_CSSegmentedValue._segment
+ _OBJC_IVAR_$_CSSegmentedValue._thresholds
+ _OBJC_IVAR_$_CSSegmentedValue._value
+ _OBJC_METACLASS_$_CSLatencyCardResultView
+ _OBJC_METACLASS_$_CSSegmentedValue
+ _OBJC_METACLASS_$_CSStartSingingEvent
+ _OBJC_METACLASS_$_CSTipTriangleView
+ _UIEdgeInsetsZero
+ _UIFontTextStyleCaption2
+ __OBJC_$_CLASS_METHODS_CSStartSingingEvent
+ __OBJC_$_INSTANCE_METHODS_CSLatencyCardResultView
+ __OBJC_$_INSTANCE_METHODS_CSSegmentedValue
+ __OBJC_$_INSTANCE_METHODS_CSTipTriangleView
+ __OBJC_$_INSTANCE_VARIABLES_CSLatencyCardResultView
+ __OBJC_$_INSTANCE_VARIABLES_CSSegmentedValue
+ __OBJC_$_PROP_LIST_CSSegmentedValue
+ __OBJC_CLASS_RO_$_CSLatencyCardResultView
+ __OBJC_CLASS_RO_$_CSSegmentedValue
+ __OBJC_CLASS_RO_$_CSStartSingingEvent
+ __OBJC_CLASS_RO_$_CSTipTriangleView
+ __OBJC_METACLASS_RO_$_CSLatencyCardResultView
+ __OBJC_METACLASS_RO_$_CSSegmentedValue
+ __OBJC_METACLASS_RO_$_CSStartSingingEvent
+ __OBJC_METACLASS_RO_$_CSTipTriangleView
+ ___41-[CSLatencyCardResultView layoutSubviews]_block_invoke
+ ___41-[CSLatencyCardResultView layoutSubviews]_block_invoke_2
+ ___46-[CSRemoteRequestClient sendStartSingingEvent]_block_invoke
+ ___46-[CSRemoteRequestClient sendStartSingingEvent]_block_invoke.cold.1
+ ___58-[CSLatencyCardViewController _startAudioLatencyEstimator]_block_invoke.59
+ ___83-[CSLatencyCardViewController _showLatencyCheckConfirmationIfNeededWithCompletion:]_block_invoke
+ ___83-[CSLatencyCardViewController _showLatencyCheckConfirmationIfNeededWithCompletion:]_block_invoke.78
+ ___83-[CSLatencyCardViewController _showLatencyCheckConfirmationIfNeededWithCompletion:]_block_invoke.79
+ ___block_descriptor_32_e23_v32?0"UIView"8Q16^B24l
+ ___block_descriptor_32_e31_v32?0"UIProgressView"8Q16^B24l
+ ___block_descriptor_40_e8_32bs_e23_v16?0"UIAlertAction"8ls32l8
+ ___block_descriptor_40_e8_32s_e25_v24?0Q8"NSDictionary"16ls32l8
+ ___block_literal_global.42
+ ___block_literal_global.91
+ _objc_msgSend$_buttonTitleForCurrentState
+ _objc_msgSend$_infoText
+ _objc_msgSend$_linkWithAttributedString:textStyle:weight:color:
+ _objc_msgSend$_progressBarOffset
+ _objc_msgSend$_showLatencyCheckConfirmationIfNeededWithCompletion:
+ _objc_msgSend$_updateContentViewFromCurrentState
+ _objc_msgSend$_updateView
+ _objc_msgSend$addAttribute:value:range:
+ _objc_msgSend$addLineToPoint:
+ _objc_msgSend$closePath
+ _objc_msgSend$constraintGreaterThanOrEqualToAnchor:constant:
+ _objc_msgSend$fill
+ _objc_msgSend$initWithLatency:
+ _objc_msgSend$initWithProgressViewStyle:
+ _objc_msgSend$initWithThresholds:value:
+ _objc_msgSend$moveToPoint:
+ _objc_msgSend$numberOfSegments
+ _objc_msgSend$progressWithinSegment
+ _objc_msgSend$segment
+ _objc_msgSend$sendStartSingingEvent
+ _objc_msgSend$setBottomPadding:
+ _objc_msgSend$setDistribution:
+ _objc_msgSend$setFill
+ _objc_msgSend$setLineFragmentPadding:
+ _objc_msgSend$setMasksToBounds:
+ _objc_msgSend$setOpaque:
+ _objc_msgSend$setProgress:
+ _objc_msgSend$setProgressTintColor:
+ _objc_msgSend$setScrollEnabled:
+ _objc_msgSend$setTextContainerInset:
+ _objc_msgSend$setTitleAlignment:
+ _objc_msgSend$setTrackTintColor:
+ _objc_msgSend$setValue:
+ _objc_msgSend$subviews
+ _objc_msgSend$systemBlueColor
+ _objc_msgSend$textContainer
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$updateSegmentAndProgress
+ _objc_msgSend$updateWithLatency:
+ _symbolic _____Sg 16MusicKitInternal0cA6PlayerC5QueueC5EntryV
- -[CSHelpPanelViewController gameModelDescriptionLabel]
- -[CSHelpPanelViewController setGameModelDescriptionLabel:]
- -[CSLatencyCardViewController _latencyResultForCurrentState]
- -[CSLatencyCardViewController _symbolColorForResult:]
- -[CSLatencyCardViewController _symbolNameForResult:]
- -[CSLatencyCardViewController _textForResult:]
- -[CSLatencyCardViewController _updateViewFromCurrentState]
- -[CSLatencyCardViewController errorState]
- -[CSLatencyCardViewController imageView]
- -[CSLatencyCardViewController resultLabel]
- _OBJC_IVAR_$_CSHelpPanelViewController._gameModelDescriptionLabel
- _OBJC_IVAR_$_CSLatencyCardViewController._errorState
- _OBJC_IVAR_$_CSLatencyCardViewController._imageView
- _OBJC_IVAR_$_CSLatencyCardViewController._resultLabel
- ___58-[CSLatencyCardViewController _startAudioLatencyEstimator]_block_invoke_2
- ___block_descriptor_48_e8_32s_e25_v24?0Q8"NSDictionary"16ls32l8
- ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
- _objc_msgSend$_latencyResultForCurrentState
- _objc_msgSend$_symbolColorForResult:
- _objc_msgSend$_symbolNameForResult:
- _objc_msgSend$_textForResult:
- _objc_msgSend$_updateViewFromCurrentState
- _objc_msgSend$systemGrayColor
- _objc_msgSend$systemGreenColor
- _objc_msgSend$systemYellowColor
CStrings:
+ "%1$@"
+ "%s: %s - Audio Latency card updating for event: %ld"
+ "%s: Audio Latency Estimator alert presented."
+ "%s: Audio Latency Estimator confirmed."
+ "%s: Audio Latency Estimator did not confirm."
+ "%s: Mic is local. Don't need confirmation to start audio latency estimator."
+ "%s: Need confirmation to start audio latency estimator."
+ "%s: Placeholder '%%1$@' not found in localized string '%@'"
+ "%s: failed to send start singing event with error: %@"
+ "%s: sent start singing event"
+ "-[CSHelpPanelViewController _createViews]"
+ "-[CSLatencyCardViewController _showLatencyCheckConfirmationIfNeededWithCompletion:]"
+ "-[CSLatencyCardViewController _showLatencyCheckConfirmationIfNeededWithCompletion:]_block_invoke"
+ "-[CSLatencyCardViewController _startAudioLatencyEstimator]_block_invoke"
+ "-[CSLatencyCardViewController _updateCardForEvent:info:]"
+ "-[CSRemoteRequestClient sendStartSingingEvent]_block_invoke"
+ "@\"CSLatencyCardResultView\""
+ "@\"CSSegmentedValue\""
+ "@32@0:8@16Q24"
+ "@48@0:8@16@24d32@40"
+ "AUDIO_HELP_GAME_MODE_LEARN_MORE"
+ "AUDIO_HELP_GAME_MODE_LEARN_MORE_URL"
+ "CSLatencyCardResultView"
+ "CSSegmentedValue"
+ "CSStartSingingEvent"
+ "CSTipTriangleView"
+ "MEASUREMENT_CONFIRMATION_CANCEL"
+ "MEASUREMENT_CONFIRMATION_CONTINUE"
+ "MEASUREMENT_CONFIRMATION_MESSAGE"
+ "MEASUREMENT_CONFIRMATION_TITLE"
+ "MEASUREMENT_LOWER_BOUND"
+ "MEASUREMENT_UPPER_BOUND"
+ "No Text here yet!"
+ "T@\"CSLatencyCardResultView\",R,N,V_resultView"
+ "T@\"CSPaddingView\",&,N,V_gameModeDescriptionLabel"
+ "T@\"NSArray\",&,N,V_thresholds"
+ "T@\"NSArray\",R,N,V_failedStateConstraints"
+ "T@\"UIStackView\",R,N,V_failedInfoView"
+ "TQ,N,V_segment"
+ "TQ,N,V_value"
+ "TQ,R,N"
+ "Td,N,V_progressWithinSegment"
+ "_buttonTitleForCurrentState"
+ "_failedInfoView"
+ "_failedStateConstraints"
+ "_gameModeDescriptionLabel"
+ "_infoLabel"
+ "_infoText"
+ "_latencyLabel"
+ "_latencyTipTriangleCenterXOffset"
+ "_linkWithAttributedString:textStyle:weight:color:"
+ "_progressBarOffset"
+ "_progressBars"
+ "_progressWithinSegment"
+ "_resultView"
+ "_segment"
+ "_segmentedLatency"
+ "_showLatencyCheckConfirmationIfNeededWithCompletion:"
+ "_thresholds"
+ "_updateContentViewFromCurrentState"
+ "_updateView"
+ "_value"
+ "addAttribute:value:range:"
+ "addLineToPoint:"
+ "arrow.trianglehead.clockwise"
+ "closePath"
+ "com.apple.ContinuitySing.startSinging"
+ "constraintGreaterThanOrEqualToAnchor:constant:"
+ "could not queue after current entry, but there is a current entry, so queueing music video at tail"
+ "could not queue after current entry, but there is a current entry, so queueing song at tail"
+ "drawRect:"
+ "failedInfoView"
+ "failedStateConstraints"
+ "fill"
+ "gameModeDescriptionLabel"
+ "i"
+ "initWithLatency:"
+ "initWithProgressViewStyle:"
+ "initWithThresholds:value:"
+ "numberOfSegments"
+ "progressWithinSegment"
+ "resultView"
+ "segment"
+ "sendStartSingingEvent"
+ "setDistribution:"
+ "setFill"
+ "setGameModeDescriptionLabel:"
+ "setLineFragmentPadding:"
+ "setOpaque:"
+ "setProgress:"
+ "setProgressTintColor:"
+ "setProgressWithinSegment:"
+ "setScrollEnabled:"
+ "setSegment:"
+ "setTextContainerInset:"
+ "setThresholds:"
+ "setTitleAlignment:"
+ "setTrackTintColor:"
+ "setValue:"
+ "subviews"
+ "systemBlueColor"
+ "textContainer"
+ "thresholds"
+ "unsignedIntegerValue"
+ "updateSegmentAndProgress"
+ "updateWithLatency:"
+ "v32@?0@\"UIProgressView\"8Q16^B24"
+ "v32@?0@\"UIView\"8Q16^B24"
- "%@\n%@"
- "-[CSLatencyCardViewController _startAudioLatencyEstimator]"
- "MEASUREMENT_RETRY"
- "T@\"CSPaddingView\",&,N,V_gameModelDescriptionLabel"
- "T@\"UIImageView\",R,N,V_imageView"
- "T@\"UILabel\",R,N,V_resultLabel"
- "TQ,R,N,V_errorState"
- "_errorState"
- "_gameModelDescriptionLabel"
- "_latencyResultForCurrentState"
- "_resultLabel"
- "_symbolColorForResult:"
- "_symbolNameForResult:"
- "_textForResult:"
- "_updateViewFromCurrentState"
- "checkmark.circle.fill"
- "errorState"
- "exclamationmark.triangle.fill"
- "gameModelDescriptionLabel"
- "resultLabel"
- "setGameModelDescriptionLabel:"
- "systemGrayColor"
- "systemGreenColor"
- "systemYellowColor"
- "tv.and.mediabox"
- "xmark.circle.fill"

```
