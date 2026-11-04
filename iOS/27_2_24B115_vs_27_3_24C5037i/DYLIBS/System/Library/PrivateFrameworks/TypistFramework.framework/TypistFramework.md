## TypistFramework

> `/System/Library/PrivateFrameworks/TypistFramework.framework/TypistFramework`

```diff

-501.0.0.0.0
-  __TEXT.__text: 0x432e4
-  __TEXT.__objc_methlist: 0x3b04
-  __TEXT.__const: 0x462
-  __TEXT.__ustring: 0x13ea
-  __TEXT.__cstring: 0x5c72
-  __TEXT.__gcc_except_tab: 0xd34
+505.0.0.0.0
+  __TEXT.__text: 0x51320
+  __TEXT.__objc_methlist: 0x4254
+  __TEXT.__const: 0x602
+  __TEXT.__ustring: 0x1464
+  __TEXT.__cstring: 0x6e42
+  __TEXT.__gcc_except_tab: 0xf70
   __TEXT.__dlopen_cstrs: 0x6d
   __TEXT.__oslogstring: 0xc
   __TEXT.__swift5_typeref: 0xaa

   __TEXT.__swift5_fieldmd: 0x94
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x11c8
+  __TEXT.__unwind_info: 0x1480
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x900
-  __DATA_CONST.__objc_classlist: 0x190
-  __DATA_CONST.__objc_catlist: 0x30
+  __DATA_CONST.__const: 0xbd8
+  __DATA_CONST.__objc_classlist: 0x1a8
+  __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2660
-  __DATA_CONST.__objc_superrefs: 0x120
-  __DATA_CONST.__objc_arraydata: 0x3c18
-  __DATA_CONST.__got: 0x540
-  __AUTH_CONST.__const: 0x788
-  __AUTH_CONST.__cfstring: 0x11920
-  __AUTH_CONST.__objc_const: 0x4ca8
-  __AUTH_CONST.__objc_intobj: 0xbb8
-  __AUTH_CONST.__objc_arrayobj: 0x390
+  __DATA_CONST.__objc_selrefs: 0x2d38
+  __DATA_CONST.__objc_superrefs: 0x138
+  __DATA_CONST.__objc_arraydata: 0x3c98
+  __DATA_CONST.__got: 0x5a8
+  __AUTH_CONST.__const: 0x828
+  __AUTH_CONST.__cfstring: 0x129c0
+  __AUTH_CONST.__objc_const: 0x55f0
+  __AUTH_CONST.__objc_intobj: 0xbd0
+  __AUTH_CONST.__objc_arrayobj: 0x3d8
   __AUTH_CONST.__objc_dictobj: 0x3e8
-  __AUTH_CONST.__objc_doubleobj: 0xa0
+  __AUTH_CONST.__objc_doubleobj: 0xe0
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0x700
-  __AUTH.__objc_data: 0xe08
+  __AUTH_CONST.__auth_got: 0x798
+  __AUTH.__objc_data: 0xef8
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x2d8
-  __DATA.__data: 0x1e8
+  __DATA.__objc_ivar: 0x368
+  __DATA.__data: 0x200
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1b8
   __DATA_DIRTY.__bss: 0x48

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 1397
-  Symbols:   2400
-  CStrings:  2303
+  Functions: 1594
+  Symbols:   2717
+  CStrings:  2442
 
Symbols:
+ +[NSCharacterSet(Devanagari) headlineBearingCharacterSet]
+ +[TypistDevanagariSyllable hasHeadline:]
+ +[TypistKeyboardDataInProcess appearanceFieldsForTraits:geometryOverride:]
+ +[TypistKeyboardDataInProcess generatePopupKeySubtrees:key:plane:layout:keyplaneKeycaps:popupTraitsCache:]
+ +[TypistKeyboardDataInProcess generateSnapshotForInputMode:keyplaneName:]
+ +[TypistKeyboardDataInProcess isActiveKeyboardEquivalentTo:]
+ +[TypistKeyboardDataInProcess isKeyboardVisible]
+ +[TypistKeyboardDataInProcess keyboardBackgroundForKeyboardView:]
+ +[TypistKeyboardDataInProcess renderFieldsForKey:traits:layout:]
+ +[TypistKeyboardDataInProcess secondaryLabelOffsetForTraits:atIndex:]
+ +[TypistKeyboardDataInProcess secondaryOffsetsFromTraits:]
+ +[TypistKeyboardDataInputUIClient generateSnapshotForInputMode:keyplaneName:]
+ +[TypistKeyboardDataInputUIClient isActiveKeyboardEquivalentTo:]
+ +[TypistKeyboardDataInputUIClient isKeyboardVisible]
+ +[TypistKeyboardUtilities(BimanualUtilities) bimanualGroupSpanForTouchCount:overlapStyle:holdDuration:overlapRatio:]
+ +[TypistKeyboardUtilities(BimanualUtilities) bimanualIsPlainTapAction:]
+ +[TypistKeyboardUtilities(BimanualUtilities) bimanualIsWaitAction:]
+ +[TypistKeyboardUtilities(BimanualUtilities) bimanualOverlapStyleForRollToChordMix:uniform:]
+ +[TypistKeyboardUtilities(BimanualUtilities) bimanualPressOrderForTouchCount:transposed:uniform:]
+ +[TypistKeyboardUtilities(BimanualUtilities) bimanualScheduleForPressOrder:overlapStyle:holdDuration:overlapRatio:]
+ +[TypistKeyboardUtilities(BimanualUtilities) fingerIndexForKeyCenter:withinBounds:fingerCount:]
+ +[TypistKeyboardUtilities(BimanualUtilities) validateBimanualOverlapRatio:forOverlapStyle:touchCount:]
+ +[TypistKeyboardUtilities(KeyboardSettings) isSplitPreferenceRecorded]
+ +[TypistKeyboardUtilities(KeyboardSettings) recordDockedKeyboardPosition:]
+ +[TypistKeyboardUtilities(KeyboardSettings) recordSplitPreferences:]
+ +[TypistKeyboardUtilities(KeyboardSettings) resetSplitPreferencesToDefaults]
+ +[TypistKeyboardUtilities(KeyboardUI) _missingReadinessConditionForKeyboardID:]
+ +[TypistKeyboardUtilities(KeyboardUI) _refocusAndWaitForFirstResponder:]
+ +[TypistKeyboardUtilities(KeyboardUI) captureKeyboardImageForInputMode:keyplaneName:]
+ +[TypistKeyboardUtilities(KeyboardUI) refocusTextInput:andWaitForKeyboardID:]
+ +[TypistKeyboardUtilities(MathUtilities) _microDragTagActions:taggedCopies:fingerForAction:]
+ +[TypistKeyboardUtilities(MathUtilities) acceptsTapNoiseForKey:]
+ +[TypistKeyboardUtilities(MathUtilities) annotateMicroDragAction:withSample:]
+ +[TypistKeyboardUtilities(MathUtilities) annotatePressDurationAction:withSample:]
+ +[TypistKeyboardUtilities(MathUtilities) indexOfNearestThumbArcForKeyCenter:references:count:millimetresPerPoint:]
+ +[TypistKeyboardUtilities(MathUtilities) inverseNormalCDF:]
+ +[TypistKeyboardUtilities(MathUtilities) isMicroDragTouchDownAction:]
+ +[TypistKeyboardUtilities(MathUtilities) isPlaneControlKey:]
+ +[TypistKeyboardUtilities(MathUtilities) microDragEligibleForLettersPlane:acceptsTapNoise:tenKey:kana:flick:]
+ +[TypistKeyboardUtilities(MathUtilities) microDragFilledBoundsForTouchDownBounds:]
+ +[TypistKeyboardUtilities(MathUtilities) microDragFingerSourceForBimanualRate:twoThumb:]
+ +[TypistKeyboardUtilities(MathUtilities) microDragSampleForTuning:uniformMix:uniformMagnitude:uniformDirection:uniformFallback:]
+ +[TypistKeyboardUtilities(MathUtilities) microDragStream:taggingFingersWith:]
+ +[TypistKeyboardUtilities(MathUtilities) microDragTuningForTwoThumb:scale:median:spread:severity:substantialRate:directionSpread:]
+ +[TypistKeyboardUtilities(MathUtilities) pointOffsetFromEdge:ofRect:offset:crossAxisFraction:]
+ +[TypistKeyboardUtilities(MathUtilities) pressDurationSampleForTuning:uniformDuration:uniformSplit:]
+ +[TypistKeyboardUtilities(MathUtilities) pressDurationTuningForMedian:spread:]
+ +[TypistKeyboardUtilities(RecapUtilities) _bimanualRenamingReleasesForSchedule:touchCount:]
+ +[TypistKeyboardUtilities(RecapUtilities) _commandsForSegment:segmentOffset:bimanualGroups:displayUUID:]
+ +[TypistKeyboardUtilities(RecapUtilities) _compileCLICommandsFromActions:]
+ +[TypistKeyboardUtilities(RecapUtilities) _composeBimanualGroup:segmentActions:segmentOffset:intoComposer:slots:lastTime:]
+ +[TypistKeyboardUtilities(RecapUtilities) _composeSerialTapAction:intoComposer:commandString:commandDescription:]
+ +[TypistKeyboardUtilities(RecapUtilities) _composedCommandForSegment:segmentOffset:groups:displayUUID:]
+ +[TypistKeyboardUtilities(RecapUtilities) bimanualDragEndsForGroup:segmentActions:segmentOffset:moveDuration:]
+ +[TypistKeyboardUtilities(RecapUtilities) bimanualRenamedTouchesForSchedule:touchCount:]
+ +[TypistKeyboardUtilities(RecapUtilities) bimanualTimelineForSchedule:startPoints:dragEnds:moveDuration:touchFrequency:]
+ +[TypistKeyboardUtilities(RecapUtilities) convertRecapCommandsFromListOfActions:bimanualGroups:]
+ +[TypistKeyboardUtilities(RecapUtilities) flattenedActionsForKeystrokeStream:]
+ +[TypistKeyboardUtilities(RecapUtilities) microDragActivePoints:forSlots:currentPoints:]
+ +[TypistKeyboardUtilities(RecapUtilities) microDragCLIFragmentForAction:radiusAddition:]
+ +[TypistKeyboardUtilities(RecapUtilities) microDragMoveStepCountForDuration:touchFrequency:]
+ +[TypistKeyboardUtilities(RecapUtilities) plainTapCLIFragmentForAction:radiusAddition:]
+ +[TypistKeyboardUtilities(RecapUtilities) resolveMicroDragEndpointsForActions:screenSize:]
+ +[TypistPathUtilities _extractBodyStrokesFrom:forCharacter:withTransform:]
+ +[TypistPathUtilities _lookupLeftMatraData:forLocale:]
+ +[TypistPathUtilities _processDevanagariCharacter:withPathMap:forLocale:]
+ +[TypistPathUtilities _shiftDevanagariPath:forCharacters:]
+ +[TypistPathUtilities _synthesizeLeftMatraCanopy:stemOriginX:targetStemX:]
+ -[TYBimanualGroup .cxx_destruct]
+ -[TYBimanualGroup actionRange]
+ -[TYBimanualGroup description]
+ -[TYBimanualGroup fingerIndexes]
+ -[TYBimanualGroup hasConsistentActionRange]
+ -[TYBimanualGroup initWithActionRange:taps:fingerIndexes:pressOrder:overlapStyle:holdDuration:overlapRatio:trailingInterval:]
+ -[TYBimanualGroup isTransposed]
+ -[TYBimanualGroup keyDescription]
+ -[TYBimanualGroup overlapStyle]
+ -[TYBimanualGroup pressOrder]
+ -[TYBimanualGroup schedule]
+ -[TYBimanualGroup taps]
+ -[TYBimanualGroup trailingInterval]
+ -[TYBimanualTimelineEvent .cxx_destruct]
+ -[TYBimanualTimelineEvent description]
+ -[TYBimanualTimelineEvent initWithKind:time:touchIndex:movedPoints:]
+ -[TYBimanualTimelineEvent kind]
+ -[TYBimanualTimelineEvent movedPoints]
+ -[TYBimanualTimelineEvent time]
+ -[TYBimanualTimelineEvent touchIndex]
+ -[TYBimanualTouchEvent description]
+ -[TYBimanualTouchEvent initWithTouchIndex:time:isDown:]
+ -[TYBimanualTouchEvent isDown]
+ -[TYBimanualTouchEvent time]
+ -[TYBimanualTouchEvent touchIndex]
+ -[TYRecapCommand initWithCommandType:eventStream:commandString:commandDescription:]
+ -[TypistKeyboard _annotateMicroDragTapAction:]
+ -[TypistKeyboard _annotatePressDurationTapAction:]
+ -[TypistKeyboard _bimanualGroupsForActions:]
+ -[TypistKeyboard _fingerIndexForTapAction:]
+ -[TypistKeyboard _generateTapKeystrokeStream:]
+ -[TypistKeyboard _isTwoThumbMicroDragPosture:]
+ -[TypistKeyboard _keyplaneBoundsForPlaneName:]
+ -[TypistKeyboard _logPressDurationsForKeystrokeStream:]
+ -[TypistKeyboard _microDragKeyplaneBoundsForActions:]
+ -[TypistKeyboard _microDragResolvedKeystrokeStream:]
+ -[TypistKeyboard _microDragTaggedKeystrokeStream:]
+ -[TypistKeyboard _recapCommandsForKeystrokeStream:]
+ -[TypistKeyboard _resolvedMicroDragTuning]
+ -[TypistKeyboard _warnOnceIfBimanualIsUnreachableUnderPrediction]
+ -[TypistKeyboard _warnOnceIfUnfaithfulReleaseIsEnabled:]
+ -[TypistKeyboard bimanualAllowUnfaithfulRelease]
+ -[TypistKeyboard bimanualFingers]
+ -[TypistKeyboard bimanualKeyplaneBounds]
+ -[TypistKeyboard bimanualOverlapRatio]
+ -[TypistKeyboard bimanualRate]
+ -[TypistKeyboard bimanualRollToChordMix]
+ -[TypistKeyboard bimanualTransposeRate]
+ -[TypistKeyboard hasWarnedBimanualRollIsBlocked]
+ -[TypistKeyboard hasWarnedBimanualUnreachable]
+ -[TypistKeyboard resetBimanualRandomStateForTestCase:]
+ -[TypistKeyboard resetMicroDragRandomStateForTestCase:]
+ -[TypistKeyboard resetPressDurationRandomStateForTestCase:]
+ -[TypistKeyboard resetTapNoiseRandomStateForTestCase:]
+ -[TypistKeyboard setBimanualAllowUnfaithfulRelease:]
+ -[TypistKeyboard setBimanualFingers:]
+ -[TypistKeyboard setBimanualKeyplaneBounds:]
+ -[TypistKeyboard setBimanualOverlapRatio:]
+ -[TypistKeyboard setBimanualRate:]
+ -[TypistKeyboard setBimanualRollToChordMix:]
+ -[TypistKeyboard setBimanualTransposeRate:]
+ -[TypistKeyboard setHasWarnedBimanualRollIsBlocked:]
+ -[TypistKeyboard setHasWarnedBimanualUnreachable:]
+ -[TypistKeyboard setTapMicroDragDirectionSpread:]
+ -[TypistKeyboard setTapMicroDragMedian:]
+ -[TypistKeyboard setTapMicroDragPosture:]
+ -[TypistKeyboard setTapMicroDragScale:]
+ -[TypistKeyboard setTapMicroDragSeverity:]
+ -[TypistKeyboard setTapMicroDragSpread:]
+ -[TypistKeyboard setTapMicroDragSubstantialRate:]
+ -[TypistKeyboard setTapPressDuration:]
+ -[TypistKeyboard setTapPressDurationSpread:]
+ -[TypistKeyboard tapMicroDragDirectionSpread]
+ -[TypistKeyboard tapMicroDragMedian]
+ -[TypistKeyboard tapMicroDragPosture]
+ -[TypistKeyboard tapMicroDragScale]
+ -[TypistKeyboard tapMicroDragSeverity]
+ -[TypistKeyboard tapMicroDragSpread]
+ -[TypistKeyboard tapMicroDragSubstantialRate]
+ -[TypistKeyboard tapPressDurationSpread]
+ -[TypistKeyboard tapPressDuration]
+ -[UIWindow(SplitKeyboard) ty_boundsSize]
+ -[UIWindow(SplitKeyboard) ty_expectsSplitKeyboard]
+ GCC_except_table102
+ GCC_except_table109
+ GCC_except_table115
+ GCC_except_table117
+ GCC_except_table119
+ GCC_except_table121
+ GCC_except_table26
+ GCC_except_table39
+ GCC_except_table48
+ GCC_except_table57
+ GCC_except_table59
+ GCC_except_table61
+ GCC_except_table65
+ GCC_except_table67
+ GCC_except_table75
+ GCC_except_table80
+ GCC_except_table86
+ GCC_except_table89
+ GCC_except_table92
+ GCC_except_table98
+ _CFAbsoluteTimeGetCurrent
+ _CGContextTranslateCTM
+ _CGRectGetMaxY
+ _CGRectGetMidX
+ _CGRectGetMinY
+ _CGRectIntegral
+ _CGRectIntersection
+ _CGRectIntersectsRect
+ _CGRectIsInfinite
+ _CGRectIsNull
+ _CGRectUnion
+ _CGSizeZero
+ _NSSelectorFromString
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_NSMutableIndexSet
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_TYBimanualGroup
+ _OBJC_CLASS_$_TYBimanualTimelineEvent
+ _OBJC_CLASS_$_TYBimanualTouchEvent
+ _OBJC_CLASS_$_UIKBBackdropView
+ _OBJC_CLASS_$_UIKBInputBackdropView
+ _OBJC_CLASS_$_UIKBRenderGeometry
+ _OBJC_IVAR_$_TYBimanualGroup._actionRange
+ _OBJC_IVAR_$_TYBimanualGroup._fingerIndexes
+ _OBJC_IVAR_$_TYBimanualGroup._isTransposed
+ _OBJC_IVAR_$_TYBimanualGroup._overlapStyle
+ _OBJC_IVAR_$_TYBimanualGroup._pressOrder
+ _OBJC_IVAR_$_TYBimanualGroup._schedule
+ _OBJC_IVAR_$_TYBimanualGroup._taps
+ _OBJC_IVAR_$_TYBimanualGroup._trailingInterval
+ _OBJC_IVAR_$_TYBimanualTimelineEvent._kind
+ _OBJC_IVAR_$_TYBimanualTimelineEvent._movedPoints
+ _OBJC_IVAR_$_TYBimanualTimelineEvent._time
+ _OBJC_IVAR_$_TYBimanualTimelineEvent._touchIndex
+ _OBJC_IVAR_$_TYBimanualTouchEvent._isDown
+ _OBJC_IVAR_$_TYBimanualTouchEvent._time
+ _OBJC_IVAR_$_TYBimanualTouchEvent._touchIndex
+ _OBJC_IVAR_$_TypistKeyboard._bimanualAllowUnfaithfulRelease
+ _OBJC_IVAR_$_TypistKeyboard._bimanualFingers
+ _OBJC_IVAR_$_TypistKeyboard._bimanualKeyplaneBounds
+ _OBJC_IVAR_$_TypistKeyboard._bimanualOverlapRatio
+ _OBJC_IVAR_$_TypistKeyboard._bimanualRate
+ _OBJC_IVAR_$_TypistKeyboard._bimanualRollToChordMix
+ _OBJC_IVAR_$_TypistKeyboard._bimanualTransposeRate
+ _OBJC_IVAR_$_TypistKeyboard._hasWarnedBimanualRollIsBlocked
+ _OBJC_IVAR_$_TypistKeyboard._hasWarnedBimanualUnreachable
+ _OBJC_IVAR_$_TypistKeyboard._microDragStreamDepth
+ _OBJC_IVAR_$_TypistKeyboard._microDragTuning
+ _OBJC_IVAR_$_TypistKeyboard._pressDurationTuning
+ _OBJC_IVAR_$_TypistKeyboard._tapMicroDragDirectionSpread
+ _OBJC_IVAR_$_TypistKeyboard._tapMicroDragMedian
+ _OBJC_IVAR_$_TypistKeyboard._tapMicroDragPosture
+ _OBJC_IVAR_$_TypistKeyboard._tapMicroDragScale
+ _OBJC_IVAR_$_TypistKeyboard._tapMicroDragSeverity
+ _OBJC_IVAR_$_TypistKeyboard._tapMicroDragSpread
+ _OBJC_IVAR_$_TypistKeyboard._tapMicroDragSubstantialRate
+ _OBJC_IVAR_$_TypistKeyboard._tapPressDuration
+ _OBJC_IVAR_$_TypistKeyboard._tapPressDurationSpread
+ _OBJC_METACLASS_$_TYBimanualGroup
+ _OBJC_METACLASS_$_TYBimanualTimelineEvent
+ _OBJC_METACLASS_$_TYBimanualTouchEvent
+ _TYBimanualFingerIsFree
+ _TYBimanualReleaseSlot
+ _TYInputModeMatches
+ _TYMicroDragDescription
+ _TYMicroDragEndPoint
+ _TYMicroDragHasNumber
+ _TYMicroDragMove
+ _TYMicroDragSettle
+ _TYOptionalRadiusAddition
+ _TYSeedRandStateForTestCase
+ _TYSoftwareLayout
+ _TYSplitPreferenceDefaults
+ _TYTapHasHold
+ _TYTapHold
+ _TypistComponentsForColorName
+ _TypistCornersForView
+ _TypistEnumerateInputBackdrops
+ _TypistFixedCoordinateSpaceForView
+ _TypistInnerBackdrop
+ _UIKBColorDefLookup
+ _UIKeyboardDidChangeFrameNotification
+ _UIKeyboardDidShowNotification
+ _UITextInputCurrentInputModeDidChangeNotification
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UIWindow_$_SplitKeyboard
+ __OBJC_$_CATEGORY_UIWindow_$_SplitKeyboard
+ __OBJC_$_CLASS_METHODS_TypistKeyboardUtilities(BimanualUtilities|KeyboardSettings|KeyboardUI|MathUtilities|RecapUtilities|SystemSettings)
+ __OBJC_$_INSTANCE_METHODS_TYBimanualGroup
+ __OBJC_$_INSTANCE_METHODS_TYBimanualTimelineEvent
+ __OBJC_$_INSTANCE_METHODS_TYBimanualTouchEvent
+ __OBJC_$_INSTANCE_VARIABLES_TYBimanualGroup
+ __OBJC_$_INSTANCE_VARIABLES_TYBimanualTimelineEvent
+ __OBJC_$_INSTANCE_VARIABLES_TYBimanualTouchEvent
+ __OBJC_$_PROP_LIST_TYBimanualGroup
+ __OBJC_$_PROP_LIST_TYBimanualTimelineEvent
+ __OBJC_$_PROP_LIST_TYBimanualTouchEvent
+ __OBJC_CLASS_RO_$_TYBimanualGroup
+ __OBJC_CLASS_RO_$_TYBimanualTimelineEvent
+ __OBJC_CLASS_RO_$_TYBimanualTouchEvent
+ __OBJC_METACLASS_RO_$_TYBimanualGroup
+ __OBJC_METACLASS_RO_$_TYBimanualTimelineEvent
+ __OBJC_METACLASS_RO_$_TYBimanualTouchEvent
+ ___103+[TypistKeyboardUtilities(RecapUtilities) _composedCommandForSegment:segmentOffset:groups:displayUUID:]_block_invoke
+ ___106+[TypistKeyboardDataInProcess generatePopupKeySubtrees:key:plane:layout:keyplaneKeycaps:popupTraitsCache:]_block_invoke
+ ___115+[TypistKeyboardUtilities(BimanualUtilities) bimanualScheduleForPressOrder:overlapStyle:holdDuration:overlapRatio:]_block_invoke
+ ___120+[TypistKeyboardUtilities(RecapUtilities) bimanualTimelineForSchedule:startPoints:dragEnds:moveDuration:touchFrequency:]_block_invoke
+ ___120+[TypistKeyboardUtilities(RecapUtilities) bimanualTimelineForSchedule:startPoints:dragEnds:moveDuration:touchFrequency:]_block_invoke_2
+ ___40-[UIWindow(SplitKeyboard) ty_boundsSize]_block_invoke
+ ___48+[TypistKeyboardDataInProcess isKeyboardVisible]_block_invoke
+ ___48+[TypistKeyboardDataInProcess switchToKeyboard:]_block_invoke_3
+ ___49+[TypistKeyboardDataInProcess getKeyboardLayout:]_block_invoke_4
+ ___50-[TypistKeyboard _microDragTaggedKeystrokeStream:]_block_invoke
+ ___50-[TypistKeyboard _microDragTaggedKeystrokeStream:]_block_invoke_2
+ ___50-[TypistKeyboard _microDragTaggedKeystrokeStream:]_block_invoke_3
+ ___52-[TypistKeyboard _microDragResolvedKeystrokeStream:]_block_invoke
+ ___57+[NSCharacterSet(Devanagari) headlineBearingCharacterSet]_block_invoke
+ ___60+[TypistKeyboardDataInProcess isActiveKeyboardEquivalentTo:]_block_invoke
+ ___71+[TypistKeyboardUtilities(BimanualUtilities) bimanualIsPlainTapAction:]_block_invoke
+ ___72+[TypistKeyboardUtilities(KeyboardUI) _refocusAndWaitForFirstResponder:]_block_invoke
+ ___72+[TypistKeyboardUtilities(KeyboardUI) _refocusAndWaitForFirstResponder:]_block_invoke_2
+ ___73+[TypistKeyboardDataInProcess addKeyboardGestureKeys:keys:inPlane:addTo:]_block_invoke_2
+ ___73+[TypistKeyboardDataInProcess generateSnapshotForInputMode:keyplaneName:]_block_invoke
+ ___73+[TypistKeyboardDataInProcess generateSnapshotForInputMode:keyplaneName:]_block_invoke_2
+ ___73+[TypistKeyboardDataInProcess generateSnapshotForInputMode:keyplaneName:]_block_invoke_3
+ ___74+[TypistKeyboardUtilities(RecapUtilities) _compileCLICommandsFromActions:]_block_invoke
+ ___77+[TypistKeyboardUtilities(KeyboardUI) refocusTextInput:andWaitForKeyboardID:]_block_invoke
+ ___77+[TypistKeyboardUtilities(KeyboardUI) refocusTextInput:andWaitForKeyboardID:]_block_invoke_2
+ ___77+[TypistKeyboardUtilities(KeyboardUI) refocusTextInput:andWaitForKeyboardID:]_block_invoke_3
+ ___87+[TypistKeyboardDataInProcess addKeyboardPopupKeys:keys:inPlane:addTo:keyplaneKeycaps:]_block_invoke_2
+ ___87+[TypistKeyboardDataInProcess addKeyboardPopupKeys:keys:inPlane:addTo:keyplaneKeycaps:]_block_invoke_3
+ ___TypistFindInputBackdrop_block_invoke
+ ___block_descriptor_120_e8_32s40r48r56r64r72r80r88r96r_e5_v8?0lr40l8r48l8s32l8r56l8r64l8r72l8r80l8r88l8r96l8
+ ___block_descriptor_32_e22_Q16?0"NSDictionary"8l
+ ___block_descriptor_32_e29_B32?0"NSDictionary"8Q16^B24l
+ ___block_descriptor_32_e61_q24?0"TYBimanualTimelineEvent"8"TYBimanualTimelineEvent"16l
+ ___block_descriptor_40_e8_32s_e22_Q16?0"NSDictionary"8ls32l8
+ ___block_descriptor_40_e8_32s_e24_v16?0"NSNotification"8ls32l8
+ ___block_descriptor_40_e8_32s_e46_v32?0"NSNumber"8"NSMutableDictionary"16^B24ls32l8
+ ___block_descriptor_48_e8_32s_e55_q24?0"TYBimanualTouchEvent"8"TYBimanualTouchEvent"16ls32l8
+ ___block_descriptor_56_e8_32r40r_e5_v8?0lr32l8r40l8
+ ___block_descriptor_64_e8_32r40r48r56r_e5_v8?0lr32l8r40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e5_v8?0lr48l8r56l8s32l8r64l8s40l8
+ ___block_descriptor_72_e8_32s_e40_v16?0"UIGraphicsImageRendererContext"8ls32l8
+ ___block_descriptor_80_e8_32s40r_e31_v16?0"UIKBInputBackdropView"8ls32l8r40l8
+ ___block_descriptor_80_e8_32s40s48r56r64r_e5_v8?0ls32l8s40l8r48l8r56l8r64l8
+ ___block_descriptor_88_e8_32s40r48r_e31_v16?0"UIKBInputBackdropView"8ls32l8r40l8r48l8
+ ___block_descriptor_88_e8_32s40s48s56s64s_e34_v16?0"<RCPEventStreamComposer>"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_96_e8_32s40s48r56r64r72r80r88r_e5_v8?0lr48l8s32l8s40l8r56l8r64l8r72l8r80l8r88l8
+ _bimanualIsPlainTapAction:.nonTapCommands
+ _bimanualIsPlainTapAction:.onceToken
+ _erand48
+ _exp
+ _gTYBimanualRandState
+ _gTYMicroDragRandState
+ _gTYPressDurationRandState
+ _headlineBearingCharacterSet.onceToken
+ _headlineBearingCharacterSet.set
+ _kTYMicroDragRandSeed
+ _kTYPressDurationRandSeed
+ _kTYTapNoiseRandSeed
+ _nextafter
+ _objc_exception_rethrow
+ _objc_terminate
+ _pow
+ _seed48
+ _strlen
- +[TypistKeyboardDataInProcess generatePopupKeySubtrees:key:plane:layout:keyplaneKeycaps:]
- GCC_except_table25
- GCC_except_table29
- GCC_except_table31
- GCC_except_table36
- GCC_except_table58
- GCC_except_table63
- GCC_except_table66
- GCC_except_table68
- GCC_except_table74
- GCC_except_table85
- GCC_except_table91
- GCC_except_table93
- GCC_except_table94
- GCC_except_table95
- GCC_except_table97
- __OBJC_$_CLASS_METHODS_TypistKeyboardUtilities(KeyboardSettings|KeyboardUI|MathUtilities|RecapUtilities|SystemSettings)
- ___81+[TypistKeyboardUtilities(RecapUtilities) convertRecapCommandsFromListOfActions:]_block_invoke
- ___89+[TypistKeyboardDataInProcess generatePopupKeySubtrees:key:plane:layout:keyplaneKeycaps:]_block_invoke
- _arc4random
- _arc4random_uniform
CStrings:
+ " (drag %.1fpt%@)"
+ " D%lu %@@%.4f(%.0f,%.0f) n=%lu"
+ " M%lu %@@%.4f(%.1f,%.1f)"
+ " ROCK"
+ " TRANSPOSED"
+ " U%lu %@@%.4f MISSING-SLOT"
+ " U%lu %@@%.4f idx%lu OUT-OF-ORDER"
+ " U%lu %@@%.4f tail"
+ " n=%lu"
+ " transposed"
+ " | trailing=%.4f span=%.4f"
+ "# %@[%lu] %@ %@ "
+ "######## SPECIFIED KEYBOARD OPTIONS FOR %@\n%@"
+ "%@ n=%lu"
+ "%@ when %@ lifts first"
+ "%@=%@;"
+ ", layout not loaded"
+ ", transposed"
+ "<%@ %@ %@%@>"
+ "<%@ move %@ at %.4fs>"
+ "<%@ touch %lu %@ at %.4fs>"
+ "B32@?0@\"NSDictionary\"8Q16^B24"
+ "Cannot snapshot out of process without an explicit input mode; pass one, or force the in-process data client"
+ "Cannot snapshot: failed to switch to input mode %@"
+ "Cannot snapshot: the keyboard has no on-screen extent"
+ "Cannot snapshot: the keyboard layout has no window"
+ "Cannot write %s on this OS; it is left as it is."
+ "Failed to extract layout prefix from keyboardID: [%@]"
+ "Failed to load valid path data for left matra U+093F, falling back to base consonant"
+ "Invalid keyboard identifier [%@]; cannot resolve input mode"
+ "No keyboard backdrop overlaps the keyboard layout; reporting the keyboard background with an empty frame and no corner radius"
+ "No keyboard background descriptor: no render config was reachable from the layout"
+ "No keyboard layout for %@; preprocessing skipped"
+ "No keyboard layout loaded (keyplane=%@); cannot read the layout"
+ "Popup traits cache miss for key %@ on plane %@; falling back to popupTraitsForKey:"
+ "Q16@?0@\"NSDictionary\"8"
+ "SIGMA_ERRANT"
+ "Snapshot fell back to renderInContext:; the keyboard material is missing from this image"
+ "Snapshot produced no PNG data for input mode %@ keyplane %@"
+ "Typing "
+ "Unable to switch to keyboard [%@] (active=%@%@)"
+ "[%@ %@%@] "
+ "[KbdReady] %@ not ready after %.1fs (missing: %@), proceeding anyway"
+ "[KbdReady] %@ ready in %.0f ms"
+ "[KbdReady] %@: text input did not become first responder"
+ "[KbdReady] Called on the main thread; presenting without waiting"
+ "backdropStyle"
+ "backgroundColorComponents"
+ "bimanual trace: %@[%lu] %@%@ hold=%.4f |"
+ "bimanual: %@ is set to %@ but the predictive path plays one keystroke per event stream, so no two keys can overlap. Nothing will be grouped. Turn off usePredictionBar or predictive text to exercise it."
+ "bimanual: %@=YES with mix %.2f - rolls past %d keys emit a stream no digitizer produces. Results measure malformed-input handling, not typing."
+ "bimanual: %lu groups fired (%lu transposed, longest %lu), %lu abandoned with no free finger, %lu taps considered"
+ "bimanual: DROPPING group %@ - it puts %lu touches down at once, past Recap's limit of %d. Playing those taps serially instead."
+ "bimanual: DROPPING group %@ - it spans %lu actions but holds %lu taps, which would lose or duplicate a keystroke. Playing those taps serially instead. This is a bug in the group builder."
+ "bimanual: capped %lu roll(s) at %d keys. Recap cannot release a non-tail touch faithfully. Set %@=YES to override."
+ "bimanual: dropped the swap on %lu rolled group(s) - the swapped order needed one finger on two keys at once."
+ "bimanual: dropping %lu group(s), segment contains a \"%@\" which cannot be composed"
+ "bimanual: tap %lu of %@ is \"%@\" but action %lu is \"%@\". Playing it without a drag."
+ "bimanualAllowUnfaithfulRelease"
+ "bimanualFingers"
+ "bimanualOverlapRatio"
+ "bimanualRate"
+ "bimanualRollToChordMix"
+ "bimanualTransposeRate"
+ "blurEffectStyle"
+ "blurRadius"
+ "blurSaturation"
+ "chord"
+ "cornerMask"
+ "cornerRadius"
+ "displayFrame"
+ "displayString"
+ "displayStringOffset"
+ "down"
+ "first responder"
+ "frame"
+ "hi"
+ "hi-Translit"
+ "input mode"
+ "isAnimatedBackground"
+ "isColorAdaptiveBackground"
+ "isEmptyBackground"
+ "isLightKeyboard"
+ "keyBackdropStyle"
+ "keyBackgroundColor"
+ "keyBackgroundColorComponents"
+ "keyBackgroundOpacity"
+ "keyCornerMask"
+ "keyCornerRadius"
+ "keyboardBackground"
+ "keyboardID is nil or empty, cannot determine region code"
+ "keycapColor"
+ "keycapColorComponents"
+ "keycapOpacity"
+ "keyplane"
+ "micro-drag: %lu taps, %lu drags (%lu substantial), mean %.2fpt, max %.2fpt. s=%.2f %@ p=%.3f median=%.2f spread=%.2f severity=%.2f direction=%.1fdeg"
+ "micro-drag: not dragging %@ in %@ %@ - Recap renames %@"
+ "microDragAngularOffset"
+ "microDragEndX"
+ "microDragEndY"
+ "microDragFallbackAngle"
+ "microDragFinger"
+ "microDragMagnitude"
+ "microDragMove"
+ "microDragSettle"
+ "microDragSubstantial"
+ "oneHanded"
+ "presented"
+ "press duration: %lu taps, median %.0fms, %.0f-%.0fms. median=%.3fs spread=%.2f"
+ "pressDurationHold"
+ "pressDurationSpread"
+ "q24@?0@\"TYBimanualTimelineEvent\"8@\"TYBimanualTimelineEvent\"16"
+ "q24@?0@\"TYBimanualTouchEvent\"8@\"TYBimanualTouchEvent\"16"
+ "renderConfigKeycapOpacity"
+ "representedString"
+ "representedStringOffset"
+ "roll"
+ "secondaryDisplayStringOffsets"
+ "secondaryRepresentedStringOffsets"
+ "secondaryRepresentedStrings"
+ "setShouldSplitInDefaultContext:"
+ "setShouldSplitInSplitPreferringContext:"
+ "shouldSplitInDefaultContext"
+ "symbolFrame"
+ "t %@ %@ %@%.4f "
+ "t %@ %@ %@%.4f d %@ %@ %.4f "
+ "tapMicroDragDirectionSpread"
+ "tapMicroDragMedian"
+ "tapMicroDragPosture"
+ "tapMicroDragScale"
+ "tapMicroDragSeverity"
+ "tapMicroDragSpread"
+ "tapMicroDragSubstantialRate"
+ "textOffset"
+ "transposed "
+ "twoThumb"
+ "up"
+ "usesWhiteText"
+ "v16@?0@\"UIKBInputBackdropView\"8"
+ "v32@?0@\"NSNumber\"8@\"NSMutableDictionary\"16^B24"
+ "कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहळअआइईउऊऋऌएऐओऔऑॲािीॉोौ"
+ "ि_%lu"
- "######## SPECIFIED KEYBOARD OPTIONS FOR %@\n%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;%@=%@;"
- "SIGMA_PIVOT"
- "Unable to switch to keyboard [%@] after %ld"
```
