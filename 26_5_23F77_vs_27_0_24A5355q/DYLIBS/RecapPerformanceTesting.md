## RecapPerformanceTesting

> `/System/Library/PrivateFrameworks/RecapPerformanceTesting.framework/RecapPerformanceTesting`

```diff

-51.0.0.0.0
-  __TEXT.__text: 0xeb70
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_methlist: 0x1f88
-  __TEXT.__const: 0x298
-  __TEXT.__gcc_except_tab: 0x298
-  __TEXT.__cstring: 0x79b
-  __TEXT.__oslogstring: 0x11a5
-  __TEXT.__unwind_info: 0x630
-  __TEXT.__objc_classname: 0x529
-  __TEXT.__objc_methname: 0x4449
-  __TEXT.__objc_methtype: 0x1284
-  __TEXT.__objc_stubs: 0x22e0
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x328
-  __DATA_CONST.__objc_classlist: 0xe8
+56.0.0.0.0
+  __TEXT.__text: 0xfe88
+  __TEXT.__objc_methlist: 0x2190
+  __TEXT.__const: 0x278
+  __TEXT.__gcc_except_tab: 0x284
+  __TEXT.__cstring: 0x961
+  __TEXT.__oslogstring: 0x1381
+  __TEXT.__unwind_info: 0x5f0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x3b0
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xec8
-  __DATA_CONST.__objc_superrefs: 0xc0
-  __AUTH_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__objc_selrefs: 0x1030
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0xb8
+  __DATA_CONST.__objc_arraydata: 0x60
+  __DATA_CONST.__got: 0x190
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x480
-  __AUTH_CONST.__objc_const: 0x7480
+  __AUTH_CONST.__cfstring: 0x5a0
+  __AUTH_CONST.__objc_const: 0x7f18
+  __AUTH_CONST.__weak_auth_got: 0x10
+  __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_ivar: 0x204
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0x244
   __DATA.__data: 0x668
-  __DATA.__bss: 0x89
-  __DATA_DIRTY.__objc_data: 0x910
+  __DATA.__bss: 0x79
+  __DATA_DIRTY.__objc_data: 0x8c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B7A40269-44D9-3349-8AB1-56070DF619E6
-  Functions: 544
-  Symbols:   2134
-  CStrings:  1018
+  UUID: A047EF3C-C35B-36DF-AE85-0BA4251C4E41
+  Functions: 598
+  Symbols:   2315
+  CStrings:  186
 
Symbols:
+ +[RPTInteractionOptions platformSupportsInputType:]
+ +[RPTInteractionOptions platformSupportsInputType:].cold.1
+ +[RPTTestRunner composeTestParameters:ontoComposer:]
+ -[RPTActivationTestParameters activationCount]
+ -[RPTActivationTestParameters conversion]
+ -[RPTActivationTestParameters inputTypes]
+ -[RPTActivationTestParameters setActivationCount:]
+ -[RPTActivationTestParameters setInputTypes:]
+ -[RPTChainedCoordinateSpaceConverter isEqual:]
+ -[RPTCoordinateSpaceConverter isEqual:]
+ -[RPTDefaultPointerAndFingerInteroppingComposer _applyCurrentlySetAbsolutePosition]
+ -[RPTDefaultPointerAndFingerInteroppingComposer _applyInteractionOptions]
+ -[RPTDefaultPointerAndFingerInteroppingComposer _shouldConvertTouchPointsForSelector:]
+ -[RPTDefaultPointerAndFingerInteroppingComposer conversion]
+ -[RPTDefaultPointerAndFingerInteroppingComposer initFromWrapping:interactionOptions:conversion:]
+ -[RPTDefaultPointerAndFingerInteroppingComposer pointerSetAbsolutePosition:]
+ -[RPTDirectionalCrownTestParameters inputTypes]
+ -[RPTDirectionalCrownTestParameters scrollView]
+ -[RPTDirectionalSwipeTestParameters inputTypes]
+ -[RPTDirectionalSwipeTestParameters scrollView]
+ -[RPTDirectionalSwipeTestParameters setInputTypes:]
+ -[RPTDragTestParameters inputTypes]
+ -[RPTDragTestParameters setInputTypes:]
+ -[RPTFluidSplitViewTestParameters inputTypes]
+ -[RPTFluidSplitViewTestParameters setInputTypes:]
+ -[RPTGroupScrollTestParameters inputTypes]
+ -[RPTGroupScrollTestParameters setInputTypes:]
+ -[RPTInteractionOptions .cxx_destruct]
+ -[RPTInteractionOptions compatibleInputTypes:]
+ -[RPTInteractionOptions copyWithZone:]
+ -[RPTInteractionOptions displayID]
+ -[RPTInteractionOptions preferredInputType]
+ -[RPTInteractionOptions setDisplayID:]
+ -[RPTInteractionOptions setPreferredInputType:]
+ -[RPTInteractionOptions setSupportedInputTypes:]
+ -[RPTInteractionOptions supportedInputTypes]
+ -[RPTInteractionTestParameters inputTypes]
+ -[RPTInteractionTestParameters setInputTypes:]
+ -[RPTNullCoordinateSpaceConverter flippedY]
+ -[RPTNullCoordinateSpaceConverter isEqual:]
+ -[RPTNullCoordinateSpaceConverter screenHeight]
+ -[RPTOscillationScrollTestParameters inputTypes]
+ -[RPTOscillationScrollTestParameters setInputTypes:]
+ -[RPTPagingScrollTestParameters inputTypes]
+ -[RPTPagingScrollTestParameters setInputTypes:]
+ -[RPTPagingScrollViewTestParameters inputTypes]
+ -[RPTPagingScrollViewTestParameters scrollView]
+ -[RPTPagingScrollViewTestParameters setInputTypes:]
+ -[RPTResizeTestParameters inputTypes]
+ -[RPTResizeTestParameters setInputTypes:]
+ -[RPTScrollViewTestParameters _commonInitTestName:completionHandler:]
+ -[RPTScrollViewTestParameters avoidLargeTitle]
+ -[RPTScrollViewTestParameters direction].cold.1
+ -[RPTScrollViewTestParameters inputTypes]
+ -[RPTScrollViewTestParameters prepareForTestRunner:]
+ -[RPTScrollViewTestParameters scrollView]
+ -[RPTScrollViewTestParameters scrollingBounds].cold.1
+ -[RPTScrollViewTestParameters scrollingContentLength].cold.1
+ -[RPTScrollViewTestParameters setAvoidLargeTitle:]
+ -[RPTScrollViewTestParameters setInputTypes:]
+ -[RPTTestRunner _displayIDForParameters:]
+ -[RPTViewCoordinateSpaceConverter isEqual:]
+ -[RPTWaitTestParameters inputTypes]
+ -[RPTWaitTestParameters setInputTypes:]
+ -[RPTWindowCoordinateSpaceConverter isEqual:]
+ -[UIWindow(RPTWindowExtras) _rpt_moveToSafeTopLeftOfScreenVisibleFrameAndResize:composer:]
+ -[UIWindow(RPTWindowExtras) rpt_uniqueScreenIdentifier]
+ GCC_except_table22
+ GCC_except_table25
+ GCC_except_table6
+ GCC_except_table8
+ _CGRectZero
+ _NSGetSizeAndAlignment
+ _NSInternalInconsistencyException
+ _NSStringFromSelector
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSNumberFormatter
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_NSValue
+ _OBJC_CLASS_$_UIDevice
+ _OBJC_IVAR_$_RPTActivationTestParameters._activationCount
+ _OBJC_IVAR_$_RPTActivationTestParameters._conversion
+ _OBJC_IVAR_$_RPTActivationTestParameters._inputTypes
+ _OBJC_IVAR_$_RPTDefaultPointerAndFingerInteroppingComposer._conversion
+ _OBJC_IVAR_$_RPTDefaultPointerAndFingerInteroppingComposer._interactionOptionsStack
+ _OBJC_IVAR_$_RPTDirectionalCrownTestParameters._scrollView
+ _OBJC_IVAR_$_RPTDirectionalSwipeTestParameters._inputTypes
+ _OBJC_IVAR_$_RPTDirectionalSwipeTestParameters._scrollView
+ _OBJC_IVAR_$_RPTDragTestParameters._inputTypes
+ _OBJC_IVAR_$_RPTFluidSplitViewTestParameters._inputTypes
+ _OBJC_IVAR_$_RPTGroupScrollTestParameters._inputTypes
+ _OBJC_IVAR_$_RPTInteractionOptions._displayID
+ _OBJC_IVAR_$_RPTInteractionOptions._supportedInputTypes
+ _OBJC_IVAR_$_RPTInteractionTestParameters._inputTypes
+ _OBJC_IVAR_$_RPTOscillationScrollTestParameters._inputTypes
+ _OBJC_IVAR_$_RPTPagingScrollTestParameters._inputTypes
+ _OBJC_IVAR_$_RPTPagingScrollViewTestParameters._inputTypes
+ _OBJC_IVAR_$_RPTPagingScrollViewTestParameters._scrollView
+ _OBJC_IVAR_$_RPTResizeTestParameters._inputTypes
+ _OBJC_IVAR_$_RPTScrollViewTestParameters._avoidLargeTitle
+ _OBJC_IVAR_$_RPTScrollViewTestParameters._flags
+ _OBJC_IVAR_$_RPTScrollViewTestParameters._inputTypes
+ _OBJC_IVAR_$_RPTWaitTestParameters._inputTypes
+ _RPTTestParametersSafeGetConversion
+ _RPTTestParametersSafeGetConversion.cold.1
+ _RPTTestParametersSafeGetInputTypes
+ _RPTTestParametersSafeGetInputTypes.cold.1
+ __OBJC_PROTOCOL_REFERENCE_$_RCPTouchEventStreamComposer
+ __RPTNumberFromString.formatter
+ __RPTNumberFromString.onceToken
+ ___40-[RPTTestRunner _runTestWithParameters:]_block_invoke.101
+ ___40-[RPTTestRunner _runTestWithParameters:]_block_invoke.104
+ ___40-[RPTTestRunner _runTestWithParameters:]_block_invoke.106
+ ___40-[RPTTestRunner _runTestWithParameters:]_block_invoke.110
+ ___40-[RPTTestRunner _runTestWithParameters:]_block_invoke_2.102
+ ___40-[RPTTestRunner _runTestWithParameters:]_block_invoke_2.107
+ ___45-[RPTGroupScrollTestParameters composerBlock]_block_invoke_2
+ ___46-[RPTInteractionOptions compatibleInputTypes:]_block_invoke
+ ___48-[RPTInteractionOptions setSupportedInputTypes:]_block_invoke
+ ___52+[RPTTestRunner composeTestParameters:ontoComposer:]_block_invoke
+ ___62-[RPTScrollViewTestParameters completeAfterScrollEndSignpost:]_block_invoke.23
+ ___67-[RPTDefaultPointerAndFingerInteroppingComposer forwardInvocation:]_block_invoke
+ ___83-[RPTDefaultPointerAndFingerInteroppingComposer _applyCurrentlySetAbsolutePosition]_block_invoke
+ ____RPTNumberFromString_block_invoke
+ ___block_descriptor_32_e35_B24?0"NSNumber"8"NSDictionary"16l
+ ___block_descriptor_40_e8_32s_e25_B32?0"NSNumber"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e30_{CGPoint=dd}24?0{CGPoint=dd}8ls32l8
+ ___block_descriptor_40_e8_32s_e36_v32?0"<RPTTestParameters>"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s40r_e34_v16?0"<RCPEventStreamComposer>"8lr40l8s32l8
+ ___block_descriptor_56_e8_32s40s48r_e34_v16?0"<RCPEventStreamComposer>"8ls32l8r48l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8r64l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.75
+ ___kCFBooleanFalse
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_commonInitTestName:completionHandler:
+ _objc_msgSend$_displayID
+ _objc_msgSend$_displayIDForParameters:
+ _objc_msgSend$_hasTouchPad
+ _objc_msgSend$_rpt_moveToSafeTopLeftOfScreenVisibleFrameAndResize:composer:
+ _objc_msgSend$activationCount
+ _objc_msgSend$arrayWithObject:
+ _objc_msgSend$compatibleInputTypes:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$composeTestParameters:ontoComposer:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$convertPoint:fromCoordinateSpace:
+ _objc_msgSend$convertPointFromScreen:
+ _objc_msgSend$coordinateSpace
+ _objc_msgSend$crownSender
+ _objc_msgSend$currentDevice
+ _objc_msgSend$displayID
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$flippedY
+ _objc_msgSend$getArgument:atIndex:
+ _objc_msgSend$getArgumentTypeAtIndex:
+ _objc_msgSend$indexesOfObjectsPassingTest:
+ _objc_msgSend$initFromWrapping:interactionOptions:conversion:
+ _objc_msgSend$inputTypes
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isMemberOfClass:
+ _objc_msgSend$keyWindow
+ _objc_msgSend$lastObject
+ _objc_msgSend$localeWithLocaleIdentifier:
+ _objc_msgSend$methodSignature
+ _objc_msgSend$numberFromString:
+ _objc_msgSend$numberOfArguments
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$objectsAtIndexes:
+ _objc_msgSend$overrideInteractionOptions:withEventActionsBlock:
+ _objc_msgSend$pencilDigitizerSender
+ _objc_msgSend$platformSupportsInputType:
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$preferredInputType
+ _objc_msgSend$prepareForTestRunner:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeLastObject
+ _objc_msgSend$rpt_uniqueScreenIdentifier
+ _objc_msgSend$screenHeight
+ _objc_msgSend$selector
+ _objc_msgSend$setActivationCount:
+ _objc_msgSend$setArgument:atIndex:
+ _objc_msgSend$setContentOffset:
+ _objc_msgSend$setDisplayID:
+ _objc_msgSend$setInputTypes:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$setNumberStyle:
+ _objc_msgSend$setPreferredInputType:
+ _objc_msgSend$setScalePointerPhaseScrollToPixels:
+ _objc_msgSend$setSupportedInputTypes:
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$supportedInputTypes
+ _objc_msgSend$testRunner:targetDisplayIDForParameters:
+ _objc_msgSend$touchScreenDigitizerSenderForDisplayUUID:
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$userInterfaceIdiom
+ _objc_msgSend$valueWithBytes:objCType:
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x9
+ _protocol_getMethodDescription
+ _sel_getName
+ _strcmp
- +[RPTDefaultPointerAndFingerInteroppingComposer composerWrapping:withInteractionOptions:]
- +[RPTInteractionOptions defaultForPlatform].cold.1
- +[RPTSettings processEnvironment]
- +[RPTSettings processEnvironment].cold.1
- -[RPTDefaultPointerAndFingerInteroppingComposer _usePointer]
- -[RPTDefaultPointerAndFingerInteroppingComposer forwardingTargetForSelector:]
- -[RPTDefaultPointerAndFingerInteroppingComposer initFromWrapping:interactionOptions:]
- -[RPTDragInteraction _locationsAreAlreadyScreenSpace]
- -[RPTDragInteraction set_locationsAreAlreadyScreenSpace:]
- -[RPTInteractionOptions preferredIdiom]
- -[RPTInteractionOptions setPreferredIdiom:]
- -[RPTScrollViewTestParameters setScrollingBounds:].cold.1
- -[RPTScrollViewTestParameters setScrollingContentLength:].cold.1
- -[RPTSettings .cxx_destruct]
- -[RPTSettings activationIterationCount]
- -[RPTSettings initFromDictionary:]
- -[RPTSettings init]
- -[RPTSettings recapOverrideFileURL]
- -[RPTSettings setActivationIterationCount:]
- -[RPTSettings setRecapOverrideFileURL:]
- -[RPTTestRunner setSettings:]
- -[RPTTestRunner settings]
- -[UIWindow(RPTWindowExtras) _rpt_moveToSafeTopLeftOfScreemVisibleFrameAndResize:]
- GCC_except_table17
- GCC_except_table19
- _OBJC_CLASS_$_RPTSettings
- _OBJC_IVAR_$_RPTDefaultPointerAndFingerInteroppingComposer.__usePointer
- _OBJC_IVAR_$_RPTDefaultPointerAndFingerInteroppingComposer._interactionOptions
- _OBJC_IVAR_$_RPTDragInteraction.__locationsAreAlreadyScreenSpace
- _OBJC_IVAR_$_RPTInteractionOptions._preferredIdiom
- _OBJC_IVAR_$_RPTSettings._activationIterationCount
- _OBJC_IVAR_$_RPTSettings._recapOverrideFileURL
- _OBJC_IVAR_$_RPTTestRunner._settings
- _OBJC_METACLASS_$_RPTSettings
- _OUTLINED_FUNCTION_2
- _RPTSettingsKeyActivationIterationCount
- _RPTSettingsKeyOverrideRecapWithFile
- __OBJC_$_CLASS_METHODS_RPTDefaultPointerAndFingerInteroppingComposer
- __OBJC_$_CLASS_METHODS_RPTSettings
- __OBJC_$_CLASS_PROP_LIST_RPTSettings
- __OBJC_$_INSTANCE_METHODS_RPTSettings
- __OBJC_$_INSTANCE_VARIABLES_RPTSettings
- __OBJC_$_PROP_LIST_RPTSettings
- __OBJC_$_PROTOCOL_CLASS_METHODS_RPTComposer
- __OBJC_CLASS_RO_$_RPTSettings
- __OBJC_METACLASS_RO_$_RPTSettings
- ___33+[RPTSettings processEnvironment]_block_invoke
- ___40-[RPTTestRunner _runTestWithParameters:]_block_invoke.80
- ___40-[RPTTestRunner _runTestWithParameters:]_block_invoke.88
- ___40-[RPTTestRunner _runTestWithParameters:]_block_invoke.90
- ___40-[RPTTestRunner _runTestWithParameters:]_block_invoke.94
- ___40-[RPTTestRunner _runTestWithParameters:]_block_invoke_2.81
- ___40-[RPTTestRunner _runTestWithParameters:]_block_invoke_2.91
- ___43+[RPTInteractionOptions defaultForPlatform]_block_invoke
- ___62-[RPTScrollViewTestParameters completeAfterScrollEndSignpost:]_block_invoke.17
- ___block_descriptor_56_e8_32s40s48r_e34_v16?0"<RCPEventStreamComposer>"8lr48l8s32l8s40l8
- ___block_descriptor_57_e8_32s40s48r_e34_v16?0"<RCPEventStreamComposer>"8lr48l8s32l8s40l8
- ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_73_e8_32s40s48s56s64s_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_81_e8_32s40s48s56s64s72r_e5_v8?0ls32l8s40l8s48l8r72l8s56l8s64l8
- _defaultForPlatform.defaultForPlatform
- _defaultForPlatform.onceToken
- _objc_msgSend$_locationsAreAlreadyScreenSpace
- _objc_msgSend$_rpt_moveToSafeTopLeftOfScreemVisibleFrameAndResize:
- _objc_msgSend$activationIterationCount
- _objc_msgSend$arrayWithArray:
- _objc_msgSend$composerWrapping:withInteractionOptions:
- _objc_msgSend$eventStreamWithFileURL:error:
- _objc_msgSend$initFromDictionary:
- _objc_msgSend$initFromWrapping:interactionOptions:
- _objc_msgSend$intValue
- _objc_msgSend$preferredIdiom
- _objc_msgSend$prefersPointer
- _objc_msgSend$processEnvironment
- _objc_msgSend$recapOverrideFileURL
- _objc_msgSend$removeObjectAtIndex:
- _objc_msgSend$setPreferredIdiom:
- _objc_msgSend$set_locationsAreAlreadyScreenSpace:
- _objc_msgSend$settings
- _processEnvironment.currentEnvironment
- _processEnvironment.onceToken
CStrings:
+ "!"
+ ","
+ "1"
+ "<%@:%p preferredInputType: %lu; senderProperties: %@>"
+ "<failure?>=%{public}@"
+ "<testName>=%{public, name=testName}@ isAnimation=YES "
+ "B24@?0@\"NSNumber\"8@\"NSDictionary\"16"
+ "B32@?0@\"NSNumber\"8Q16^B24"
+ "Env RPT_FORCE_INPUT_TYPES contains non numeric value %@."
+ "Must not call %@"
+ "NSTouchDevice"
+ "No supported input types by platform in %@"
+ "RPT: -[RPTComposer %{public}s], transformed arg %d (%{public}@ -> %{public}@)"
+ "RPT: -[RPTComposer init] without a conversion, all RPTTestParameters should implement conversion."
+ "RPT: -[RPTDefaultPointerAndFingerInteroppingComposer _pointerOrFingerScrollAt: %{public}@ delta: %{public}@ duration: %f"
+ "RPT: -[RPTDefaultPointerAndFingerInteroppingComposer _pointerOrFingerScrollAt: %{public}@ to: %{public}@ duration: %f excessDuration: %f"
+ "RPT: -[RPTDefaultPointerAndFingerInteroppingComposer pointerMoveToPoint: %{public}@ duration: %f f"
+ "RPT: Legacy test parameters %{public}@ does not implement conversion property."
+ "RPT: Legacy test parameters %{public}@ does not implement inputTypes property."
+ "RPT: RPTScrollViewTestParameters failed to set up signpost monitoring with predicate: %{public}@ - Because of: %{public}@"
+ "RPT: RPTScrollViewTestParameters started monitoring for signpost with predicate: %{public}@"
+ "RPT: RPTScrollViewTestParameters: waitForPostEventStreamDelayWithHandler: effectiveVersion=%lu, has_scrollView=%i, _scrollViewIdentifier=%{public}@, _shouldFlick=%i"
+ "RPT: _forwardingTarget pointerSetAbsolutePosition: %{public}@"
+ "RPT: adjust by %f for safe area"
+ "RPTDefaultPointerAndFingerInteroppingComposer has unbalanced interactionOptions."
+ "RPT_FORCE_INPUT_TYPES"
+ "Requesting unset direction without a scrollView"
+ "Requesting unset scrollingBounds without a scrollView"
+ "Requesting unset scrollingContentLength without a scrollView"
+ "acceleratePhaseScrolls"
+ "en_US_POSIX"
+ "nsScreen._UUIDString"
+ "scrollView.window"
+ "v32@?0@\"<RPTTestParameters>\"8Q16^B24"
+ "{CGPoint=dd}"
+ "{CGPoint=dd}24@?0{CGPoint=dd}8"
+ "\xa1"
- "#16@0:8"
- ".cxx_destruct"
- "<%@:%p preferredIdiom: %lu; senderProperties: %@>"
- "<failure?>=%@"
- "<testName>=%{public, name=testName}@ <isOverride>=%{public, name=isOverride}@"
- "<testName>=%{public, name=testName}@ <isOverride>=%{public, name=isOverride}@ isAnimation=YES "
- "@"
- "@\"<RCPEventStreamComposer>\""
- "@\"<RPTTestRunnerDelegate>\""
- "@\"CAMediaTimingFunction\""
- "@\"CAMediaTimingFunction\"16@0:8"
- "@\"LSBundleRecord\""
- "@\"NSArray\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"RCPEventSenderProperties\"16@0:8"
- "@\"RCPInlinePlayer\""
- "@\"RPTCoordinateSpaceConverter\""
- "@\"RPTCoordinateSpaceConverter\"16@0:8"
- "@\"RPTInteractionOptions\""
- "@\"RPTInteractionOptions\"16@0:8"
- "@\"RPTSettings\""
- "@\"UIScreen\""
- "@\"UIScrollView\""
- "@\"UISplitViewController\""
- "@\"UIView\""
- "@\"UIViewController\""
- "@\"UIWindow\""
- "@100@0:8@16Q24{CGRect={CGPoint=dd}{CGSize=dd}}32d64q72d80B88@?92"
- "@108@0:8@16Q24{CGRect={CGPoint=dd}{CGSize=dd}}32B64B68d72d80q88d96B104"
- "@116@0:8@16Q24{CGRect={CGPoint=dd}{CGSize=dd}}32B64B68d72d80q88d96B104@?108"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8Q16"
- "@24@0:8d16"
- "@32@0:8:16@24"
- "@32@0:8@\"<RCPEventStreamComposer>\"16@\"RPTInteractionOptions\"24"
- "@32@0:8@16@24"
- "@32@0:8Q16@24"
- "@32@0:8{CGVector=dd}16"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8@16d24@?32"
- "@40@0:8@16{CGSize=dd}24"
- "@40@0:8@16{CGVector=dd}24"
- "@48@0:8@16@24d32@?40"
- "@48@0:8@16Q24@32@?40"
- "@48@0:8{CGPoint=dd}16{CGPoint=dd}32"
- "@64@0:8{CGPoint=dd}16{CGSize=dd}32{CGSize=dd}48"
- "@64@0:8{CGPoint=dd}16{CGVector=dd}32{CGSize=dd}48"
- "@72@0:8@16{CGSize=dd}24d40d48q56@?64"
- "@80@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24d56q64@?72"
- "@80@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24q56q64@?72"
- "@84@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24q56B64q68@?76"
- "@88@0:8@16@24{CGRect={CGPoint=dd}{CGSize=dd}}32d64q72@?80"
- "@?"
- "@?16@0:8"
- "@?<v@?>16@0:8"
- "@?<v@?@\"<RPTComposer>\">16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B24@0:8o^@16"
- "B32@0:8@\"RPTTestRunner\"16@\"<RPTTestParameters>\"24"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B32@0:8q16@24"
- "B40@0:8@\"RPTTestRunner\"16q24@\"<RPTTestParameters>\"32"
- "B40@0:8@16q24@32"
- "CGPointValue"
- "CGRectValue"
- "NO"
- "NSObject"
- "Overriding default amplitude %.1f pts with %.1f pts. This may have undefined behavior and should be avoided, when target scroll view is known."
- "Overriding default amplitude %@ pts with %@ pts. This may have undefined behavior and should be avoided, when target scroll view is known."
- "Q16@0:8"
- "RCPBaseEventStreamComposer"
- "RCPButtonEventStreamComposer"
- "RCPEventStreamComposer"
- "RCPFluidSwipeGesturesEventStreamComposer"
- "RCPGameControllerEventStreamComposer"
- "RCPPencilEventStreamComposer"
- "RCPPointerEventStreamComposer"
- "RCPTouchEventStreamComposer"
- "RCPVendorEventStreamComposer"
- "RPT: -[RPTDefaultPointerAndFingerInteroppingComposer pointerFlickAt: %{public}@ delta: %{public}@ duration: %f"
- "RPT: RPTScrollViewTestParameters failed to set up signpost monitoring with predicate: %@ - Because of: %@"
- "RPT: RPTScrollViewTestParameters started monitoring for signpost with predicate: %@"
- "RPT: RPTScrollViewTestParameters: waitForPostEventStreamDelayWithHandler: effectiveVersion=%lu, has_scrollView=%i, _scrollViewIdentifier=%@, _shouldFlick=%i"
- "RPTActivationInteraction"
- "RPTActivationTestParameters"
- "RPTBlockBasedScrollTestParameters"
- "RPTBlockInteraction"
- "RPTCatalystAdditions"
- "RPTChainedCoordinateSpaceConverter"
- "RPTComposer"
- "RPTCoordinateSpaceConverter"
- "RPTDefaultPointerAndFingerInteroppingComposer"
- "RPTDirectionalCrownTestParameters"
- "RPTDirectionalSwipeTestParameters"
- "RPTDockGestureInteraction"
- "RPTDragInteraction"
- "RPTDragTestParameters"
- "RPTEntitlementChecker"
- "RPTFluidSplitViewTestParameters"
- "RPTGroupScrollTestParameters"
- "RPTInteraction"
- "RPTInteractionOptions"
- "RPTInteractionTestParameters"
- "RPTNullCoordinateSpaceConverter"
- "RPTOscillationScrollTestParameters"
- "RPTPagingScrollTestParameters"
- "RPTPagingScrollViewTestParameters"
- "RPTPointerAndFingerInteroppingComposer"
- "RPTResizeInteraction"
- "RPTResizeTestParameters"
- "RPTScrollViewTestParameters"
- "RPTSettings"
- "RPTTestParameters"
- "RPTTestRunner"
- "RPTTestRunnerDelegate"
- "RPTViewCoordinateSpaceConverter"
- "RPTWaitTestParameters"
- "RPTWindowCoordinateSpaceConverter"
- "RPTWindowExtras"
- "RPT_ACTIVATION_ITERATION_COUNT"
- "RPT_OVERRIDE_RECAP_WITH_FILE"
- "T#,R"
- "T@\"<RCPEventStreamComposer>\",&,N,V_forwardingTarget"
- "T@\"<RPTTestRunnerDelegate>\",W,N,V_delegate"
- "T@\"CAMediaTimingFunction\",&,N"
- "T@\"CAMediaTimingFunction\",&,N,V_curveFunction"
- "T@\"LSBundleRecord\",&,N,V_bundleRecord"
- "T@\"NSArray\",C,N,V_delays"
- "T@\"NSArray\",C,N,V_durations"
- "T@\"NSArray\",C,N,V_parameters"
- "T@\"NSArray\",R,C,N,V_interactions"
- "T@\"NSNumber\",&,N,V_swipeSpeedFactor"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,V_testName"
- "T@\"NSString\",C,N,VtestName"
- "T@\"NSString\",R,C"
- "T@\"NSURL\",&,N,V_recapOverrideFileURL"
- "T@\"RCPEventSenderProperties\",&,D,N"
- "T@\"RCPEventSenderProperties\",&,N"
- "T@\"RCPEventSenderProperties\",R,N"
- "T@\"RCPInlinePlayer\",R,&,N,V_inlinePlayer"
- "T@\"RPTCoordinateSpaceConverter\",&,N"
- "T@\"RPTCoordinateSpaceConverter\",&,N,V_conversion"
- "T@\"RPTCoordinateSpaceConverter\",&,N,V_primary"
- "T@\"RPTCoordinateSpaceConverter\",&,N,V_secondary"
- "T@\"RPTCoordinateSpaceConverter\",R,N"
- "T@\"RPTEntitlementChecker\",R,N"
- "T@\"RPTInteractionOptions\",&,N,V_interactionOptions"
- "T@\"RPTInteractionOptions\",R"
- "T@\"RPTInteractionOptions\",R,N"
- "T@\"RPTInteractionOptions\",R,N,V_interactionOptions"
- "T@\"RPTSettings\",&,N,V_settings"
- "T@\"RPTSettings\",R"
- "T@\"UIScreen\",&,N,V_screen"
- "T@\"UIView\",&,N,V_view"
- "T@\"UIWindow\",&,N,V_window"
- "T@,&,N,V_nsScreen"
- "T@?,C,N,V_actionsComposer"
- "T@?,C,N,V_completionHandler"
- "T@?,C,N,VresultsHandler"
- "T@?,R,C,N"
- "T@?,R,C,N,V_completionHandler"
- "TB,?,R,N"
- "TB,N"
- "TB,N,V__locationsAreAlreadyScreenSpace"
- "TB,N,V_adjustRotationDurationForRevolution"
- "TB,N,V_finishWithHalfIteration"
- "TB,N,V_preventDismissalGestures"
- "TB,N,V_preventSheetDismissal"
- "TB,N,V_reverse"
- "TB,N,V_shouldFlick"
- "TB,N,V_shouldLift"
- "TB,N,V_shouldPress"
- "TB,N,V_useFlicks"
- "TB,R,N"
- "TB,R,N,V__usePointer"
- "TQ,N,V_action"
- "TQ,N,V_forceMaxVersion"
- "TQ,N,V_forceMinVersion"
- "TQ,N,V_gestureStyle"
- "TQ,N,V_iterations"
- "TQ,N,V_preferredIdiom"
- "TQ,R"
- "TQ,R,N"
- "Td,D,N"
- "Td,N"
- "Td,N,V_amplitude"
- "Td,N,V_amplitudeFactor"
- "Td,N,V_amplitudeVariationPerIteration"
- "Td,N,V_initialAmplitude"
- "Td,N,V_iterationDuration"
- "Td,N,V_iterationDurationFactor"
- "Td,N,V_rotationDuration"
- "Td,N,V_screenSpaceMultiplier"
- "Td,N,V_scrollingContentLength"
- "Td,N,V_useDefaultDurationForFlick"
- "Td,R,D,N"
- "Td,R,N"
- "Td,R,N,V_waitDuration"
- "Tq,D,N"
- "Tq,N"
- "Tq,N,V_activationIterationCount"
- "Tq,N,V_direction"
- "Tq,N,V_initialDirection"
- "Tq,N,V_pointerFrequency"
- "Tq,N,V_swipeCount"
- "Tq,R,N,V_realDirection"
- "T{CGPoint=dd},N,V__currentlySetAbsolutePosition"
- "T{CGPoint=dd},N,V_destinationLocation"
- "T{CGPoint=dd},N,V_dragPoint"
- "T{CGPoint=dd},N,V_sourceLocation"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_scrollingBounds"
- "T{CGSize=dd},N,V_maximumWindowSize"
- "T{CGSize=dd},N,V_minimumWindowSize"
- "T{CGSize=dd},N,V_scrollingSize"
- "T{CGSize=dd},R,N,V_finalSize"
- "T{CGSize=dd},R,N,V_initialSize"
- "T{CGVector=dd},N,V_delta"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_RPTCoordinateSpaces"
- "_RPTTestRunnerResultsDelegate"
- "__currentlySetAbsolutePosition"
- "__locationsAreAlreadyScreenSpace"
- "__usePointer"
- "_action"
- "_actionsComposer"
- "_activationIterationCount"
- "_adjustRotationDurationForRevolution"
- "_amplitude"
- "_amplitudeFactor"
- "_amplitudeVariationPerIteration"
- "_andThenDragBy:"
- "_bundleRecord"
- "_completionHandler"
- "_contentScrollsAlongXAxis"
- "_contentScrollsAlongYAxis"
- "_conversion"
- "_currentlySetAbsolutePosition"
- "_curveFunction"
- "_delays"
- "_delegate"
- "_delta"
- "_destinationLocation"
- "_direction"
- "_dragPoint"
- "_draggableFrame"
- "_durations"
- "_effectiveAmplitudeFactor"
- "_endSerializedRunner"
- "_failWithParameters:error:"
- "_finalSize"
- "_finishWithHalfIteration"
- "_finishWithParameters:"
- "_forceMaxVersion"
- "_forceMinVersion"
- "_forwardingTarget"
- "_gestureStyle"
- "_incrementPoint:final:"
- "_initialAmplitude"
- "_initialDirection"
- "_initialSize"
- "_inlinePlayer"
- "_interactionOptions"
- "_interactions"
- "_isReadyForRunningParameters:error:"
- "_iterationDuration"
- "_iterationDurationFactor"
- "_iterations"
- "_locationsAreAlreadyScreenSpace"
- "_makeDraggableVectors:forWindow:"
- "_managePPTLifetimeEvent:forParameters:"
- "_maximumWindowSize"
- "_minimumWindowSize"
- "_nsScreen"
- "_parameters"
- "_pointerFrequency"
- "_pointerOrFingerFlickAt:byDelta:duration:"
- "_pointerOrFingerScrollAt:byDelta:duration:touchDownAndLift:"
- "_preferredIdiom"
- "_preventDismissalGestures"
- "_preventSheetDismissal"
- "_primary"
- "_primaryController"
- "_realDirection"
- "_recapOverrideFileURL"
- "_reverse"
- "_rotationDuration"
- "_rpt_moveToSafeTopLeftOfScreemVisibleFrameAndResize:"
- "_rpt_safeVisibleFrameOfScreen"
- "_runTestWithParameters:"
- "_runTestWithParameters:retries:"
- "_screen"
- "_screenSpaceMultiplier"
- "_scrollView"
- "_scrollViewIdentifier"
- "_scrollingBounds"
- "_scrollingContentLength"
- "_scrollingSize"
- "_secondary"
- "_settings"
- "_shouldFlick"
- "_shouldLift"
- "_shouldPress"
- "_sourceLocation"
- "_splitViewController"
- "_startSerializedRunnerWithError:"
- "_supplementalController"
- "_swipeCount"
- "_swipeSpeedFactor"
- "_testName"
- "_useDefaultDurationForFlick"
- "_useFlicks"
- "_usePointer"
- "_v1_composerBlock"
- "_v2_composerBlock"
- "_v3_4_composerBlock"
- "_view"
- "_waitDuration"
- "_window"
- "action"
- "actionPoint"
- "actionsComposer"
- "activationIterationCount"
- "addObject:"
- "addObserverForName:object:queue:usingBlock:"
- "adjustRotationDurationForRevolution"
- "adjustedContentInset"
- "advanceTime:"
- "amplitude"
- "amplitudeFactor"
- "amplitudeVariationPerIteration"
- "array"
- "arrayByAddingObject:"
- "arrayByAddingObjectsFromArray:"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "autorelease"
- "barrelRollAtLocation:withZPosition:withAltitudeAngle:withAzimuthAngle:withRollAngle:"
- "beginButtonPressForButtonType:"
- "beginButtonPressWithPage:usage:"
- "boolValue"
- "bounds"
- "bundleRecord"
- "bundleRecordForCurrentProcess"
- "checkTestRequirementsWithError:"
- "checkWithError:"
- "checkerForCurrentProcess"
- "class"
- "completeAfterScrollEndNotification:"
- "completeAfterScrollEndSignpost:"
- "completionHandler"
- "composeDockGestureInMotion:frequency:actionBlock:"
- "composeDockGestureOfFlavor:motion:frequency:actionBlock:"
- "composeNavigationGestureInMotion:frequency:actionBlock:"
- "composeWithSender:actionBlock:"
- "composerBlock"
- "composerWrapping:withInteractionOptions:"
- "conformsToProtocol:"
- "contentOffset"
- "contentSize"
- "conversion"
- "convertPoint:"
- "convertPoint:toCoordinateSpace:"
- "convertPoint:toView:"
- "convertPointFromUIWindow:"
- "convertPointToScreen:"
- "convertRect:"
- "convertRect:toCoordinateSpace:"
- "convertRect:toView:"
- "convertSize:"
- "convertVector:"
- "converterFromView:"
- "converterFromWindow:"
- "converterFromWindow:toScreen:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "curveFunction"
- "d"
- "d16@0:8"
- "debugDescription"
- "defaultCenter"
- "defaultForPlatform"
- "defaultPressure"
- "defaultRadius"
- "delays"
- "delegate"
- "delta"
- "description"
- "destinationLocation"
- "dictionaryWithObjects:forKeys:count:"
- "direction"
- "doubleFingerTap:"
- "doubleTap:"
- "doubleValue"
- "dragPoint"
- "dragWithStartPoint:endPoint:duration:"
- "dragWithStartPoint:endPoint:duration:pressure:"
- "dragWithStartPoint:endPoint:duration:pressure:radius:"
- "dragWithStartPoint:endPoint:duration:radius:"
- "dragWithStartPoint:endPoint:duration:tapAndWait:lift:"
- "dragWithStartPoint:endPoint:duration:tapAndWait:lift:pressure:"
- "dragWithStartPoint:endPoint:duration:tapAndWait:lift:pressure:radius:"
- "dragWithStartPoint:endPoint:duration:tapAndWait:lift:radius:"
- "dragWithStartPoint:mask:endPoint:mask:duration:"
- "durations"
- "edgeOrb:"
- "edgeOrbSwipe:withEndLocation:withDuration:"
- "effectiveVersion"
- "endButtonPressForButtonType:"
- "endButtonPressWithPage:usage:"
- "entitlements"
- "enumerateObjectsUsingBlock:"
- "environment"
- "errorWithDomain:code:userInfo:"
- "eventStreamWithEventActions:"
- "eventStreamWithFileURL:error:"
- "failedTest:withFailure:"
- "finalFingerPosition"
- "finalSize"
- "finishWithHalfIteration"
- "finishedTest:waitForCommit:extraResults:"
- "firstObject"
- "fixedCoordinateSpace"
- "flipRingerSwitchToValue:"
- "forceMaxVersion"
- "forceMinVersion"
- "forwardInvocation:"
- "forwardingTarget"
- "forwardingTargetForSelector:"
- "frame"
- "functionWithName:"
- "gestureStyle"
- "hash"
- "hover:withZPosition:"
- "hover:withZPosition:withAltitudeAngle:withAzimuthAngle:withRollAngle:"
- "hoverAtLocation:withDuration:"
- "hoverAtLocation:withDuration:withZPosition:"
- "hoverAtLocation:withDuration:withZPosition:withAltitudeAngle:withAzimuthAngle:withRollAngle:"
- "hoverToTap:withZPosition:"
- "hoverToTapAtLocation:withDuration:"
- "hoverToTapAtLocation:withDuration:withZPosition:"
- "identityConverter"
- "init"
- "initByDraggingWindow:byDelta:"
- "initForAction:window:"
- "initFromDictionary:"
- "initFromSourceLocation:toDestinationLocation:"
- "initFromView:"
- "initFromWindow:toScreen:"
- "initFromWrapping:interactionOptions:"
- "initWithActions:"
- "initWithBundleRecord:"
- "initWithDragPoint:delta:sourceSize:"
- "initWithDragPoint:sourceSize:destinationSize:"
- "initWithGestureStyle:"
- "initWithInteractionOptions:"
- "initWithPrimary:secondary:"
- "initWithTestName:interactions:completionHandler:"
- "initWithTestName:iterations:scrollingBounds:amplitude:direction:iterationDuration:useFlicks:completionHandler:"
- "initWithTestName:iterations:scrollingBounds:useFlicks:preventDismissalGestures:initialAmplitude:amplitudeVariationPerIteration:initialDirection:iterationDuration:finishWithHalfIteration:"
- "initWithTestName:iterations:scrollingBounds:useFlicks:preventDismissalGestures:initialAmplitude:amplitudeVariationPerIteration:initialDirection:iterationDuration:finishWithHalfIteration:completionHandler:"
- "initWithTestName:scrollBounds:amplitude:direction:completionHandler:"
- "initWithTestName:scrollBounds:scrollContentLength:direction:completionHandler:"
- "initWithTestName:scrollView:completionHandler:"
- "initWithTestName:scrollViewIdentifier:scrollBounds:scrollContentLength:direction:completionHandler:"
- "initWithTestName:scrollingBounds:swipeCount:direction:completionHandler:"
- "initWithTestName:scrollingBounds:swipeCount:reverse:direction:completionHandler:"
- "initWithTestName:scrollingSize:screenSpaceMultiplier:rotationDuration:direction:completionHandler:"
- "initWithTestName:splitViewController:completionHandler:"
- "initWithTestName:testType:scrollView:completionHandler:"
- "initWithTestName:wait:completionHandler:"
- "initWithTestName:window:completionHandler:"
- "initWithWait:"
- "initWithWindow:destinationSize:"
- "initialAmplitude"
- "initialAndFinalPositions"
- "initialDirection"
- "initialFingerPosition"
- "initialSize"
- "inlinePlayer"
- "intValue"
- "integerValue"
- "interactionByScalingBy:"
- "interactionOptions"
- "interactionTestParametersWithTestName:interaction:duration:completionHandler:"
- "interactions"
- "invokeWithComposer:duration:"
- "invokeWithTarget:"
- "isDecelerating"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRecapAvailable"
- "isiOSAppOnMac"
- "iterationDuration"
- "iterationDurationFactor"
- "iterations"
- "knobNudge:buttonMask:duration:"
- "length"
- "liftUp:"
- "liftUp:touchCount:"
- "liftUpActivePointsByIndex:"
- "liftUpAtAllActivePoints"
- "liftUpAtAllActivePointsWithEventType:"
- "liftUpAtPoints:touchCount:"
- "mainScreen"
- "managesTestStartAndEnd"
- "maximumWindowSize"
- "methodSignatureForSelector:"
- "minimumWindowSize"
- "mouseSender"
- "moveToPoint:duration:"
- "moveToPoints:touchCount:duration:"
- "moveToPoints:touchCount:pressure:duration:"
- "moveToPoints:touchCount:pressure:duration:radius:"
- "multifingerDragWithPointArray:numPoints:duration:numFingers:"
- "newWithTestName:parameters:completionHandler:"
- "newWithTestName:scrollBounds:amplitude:direction:completionHandler:"
- "newWithTestName:scrollView:completionHandler:"
- "nsApplication"
- "nsScreen"
- "nsWindowFrame"
- "nsWindowProxy"
- "numberWithDouble:"
- "objectAtIndexedSubscript:"
- "objectForKey:ofClass:"
- "objectForKeyedSubscript:"
- "overrideInteractionOptions:withEventActionsBlock:"
- "parameters"
- "peekAndPop:commit:duration:"
- "peekAndPop:commit:duration:pressure:"
- "peekAndPop:commit:duration:pressure:radius:"
- "peekAndPop:commit:duration:radius:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pinchCloseWithStartPoint:endPoint:duration:"
- "pinchCloseWithStartPoint:endPoint:duration:pressure:"
- "pinchCloseWithStartPoint:endPoint:duration:pressure:radius:"
- "pinchCloseWithStartPoint:endPoint:duration:radius:"
- "pinchOpenWithStartPoint:endPoint:duration:"
- "pinchOpenWithStartPoint:endPoint:duration:pressure:"
- "pinchOpenWithStartPoint:endPoint:duration:pressure:radius:"
- "pinchOpenWithStartPoint:endPoint:duration:radius:"
- "playEventStream:options:completion:"
- "playInteraction:completionHandler:"
- "pointerBeginPressingButton:"
- "pointerDiscreteGesture:duration:frequency:"
- "pointerDiscreteScroll:duration:"
- "pointerDiscreteScroll:duration:frequency:"
- "pointerEndPressingButton:"
- "pointerFrequency"
- "pointerMoveByDelta:duration:"
- "pointerMoveDelta:duration:frequency:"
- "pointerMoveFromOriginPoint:toDestinationPoint:duration:frequency:"
- "pointerMoveToPoint:duration:"
- "pointerMoveToPointIfApplicable:"
- "pointerOrFingerDoubleTap:"
- "pointerOrFingerDragWithStartPoint:mask:endPoint:mask:duration:"
- "pointerOrFingerMoveToPoint:duration:"
- "pointerOrFingerScrollAt:byDelta:duration:"
- "pointerOrFingerTap:"
- "pointerOrFingerTapDown:"
- "pointerOrFingerTapUp:"
- "pointerPhasedFlick:duration:"
- "pointerPhasedFlick:duration:frequency:"
- "pointerPhasedScroll:duration:"
- "pointerPhasedScroll:duration:frequency:"
- "pointerRotation:duration:frequency:"
- "pointerScale:duration:frequency:"
- "pointerSetAbsolutePosition:"
- "pointerTranslatation:duration:frequency:"
- "positionsForDirection:startOut:endOut:"
- "preferredIdiom"
- "prefersPointer"
- "prepareWithComposer:"
- "pressButtons:duration:"
- "pressButtonsWithPages:usages:duration:"
- "pressDiscreteGameControllerButton:duration:"
- "preventDismissalGestures"
- "preventSheetDismissal"
- "prewarmForEventStream:completion:"
- "primary"
- "processEnvironment"
- "processInfo"
- "processNotificationsWithIntervalTimeoutInSeconds:errorOut:"
- "q"
- "q16@0:8"
- "raise:format:"
- "rcp_functionWithLinearEnd"
- "realDirection"
- "recapOverrideFileURL"
- "release"
- "removeObjectAtIndex:"
- "removeObserver:"
- "respondsToSelector:"
- "resultsHandler"
- "retain"
- "retainCount"
- "reverse"
- "reversedInteraction"
- "rotate:withRadius:rotation:duration:touchCount:"
- "rotationDuration"
- "rpt_accessibilityActivationPointAttribute"
- "runTestWithParameters:"
- "runTestWithParameters:delegate:"
- "runTestWithParameters:resultHandler:"
- "safeAreaInsets"
- "scalePointerPhaseScrollToPixels"
- "screen"
- "screenSpaceMultiplier"
- "scrollWithComposer:fromPoint:toPoint:duration:"
- "scrollWithComposer:fromPoint:toPoint:swipeDuration:"
- "scrollingBounds"
- "scrollingContentLength"
- "scrollingSize"
- "secondary"
- "self"
- "sendFlickWithStartPoint:endPoint:duration:"
- "sendFlickWithStartPoint:endPoint:duration:pressure:"
- "sendFlickWithStartPoint:endPoint:duration:pressure:radius:"
- "sendFlickWithStartPoint:endPoint:duration:radius:"
- "sendUnicodeString:"
- "sendUnicodeString:synthesizePerCharacterEvents:durationBetweenEvents:"
- "sendUnicodeStringByCharacters:durationBetweenEvents:"
- "senderProperties"
- "setAction:"
- "setActionsComposer:"
- "setActivationIterationCount:"
- "setAdjustRotationDurationForRevolution:"
- "setAmplitude:"
- "setAmplitudeFactor:"
- "setAmplitudeVariationPerIteration:"
- "setBundleRecord:"
- "setCompletionHandler:"
- "setConversion:"
- "setCurveFunction:"
- "setDelays:"
- "setDelegate:"
- "setDelta:"
- "setDestinationLocation:"
- "setDirection:"
- "setDragPoint:"
- "setDurations:"
- "setEndEventProcessingBlock:"
- "setFilterPredicateString:"
- "setFinishWithHalfIteration:"
- "setForceMaxVersion:"
- "setForceMinVersion:"
- "setForwardingTarget:"
- "setFrame:display:"
- "setGestureStyle:"
- "setInitialAmplitude:"
- "setInitialDirection:"
- "setInteractionOptions:"
- "setIterationDuration:"
- "setIterationDurationFactor:"
- "setIterations:"
- "setLinkEventDeliveryToDisplayRefreshRate:"
- "setMaximumWindowSize:"
- "setMinimumWindowSize:"
- "setNsScreen:"
- "setParameters:"
- "setPointerCurveFunction:"
- "setPointerFrequency:"
- "setPreferredIdiom:"
- "setPreventDismissalGestures:"
- "setPreventSheetDismissal:"
- "setPrimary:"
- "setRecapOverrideFileURL:"
- "setResultsHandler:"
- "setReverse:"
- "setRotationDuration:"
- "setScalePointerPhaseScrollToPixels:"
- "setScreen:"
- "setScreenSpaceMultiplier:"
- "setScrollingBounds:"
- "setScrollingContentLength:"
- "setScrollingSize:"
- "setSecondary:"
- "setSenderProperties:"
- "setSettings:"
- "setShouldFlick:"
- "setShouldLift:"
- "setShouldPress:"
- "setSourceLocation:"
- "setSwipeCount:"
- "setSwipeSpeedFactor:"
- "setTestName:"
- "setTouchCurveFunction:"
- "setTouchFrequency:"
- "setUseDefaultDurationForFlick:"
- "setUseFlicks:"
- "setValue:forKey:"
- "setView:"
- "setWindow:"
- "set_currentlySetAbsolutePosition:"
- "set_locationsAreAlreadyScreenSpace:"
- "settings"
- "sharedApplication"
- "shouldFlick"
- "shouldLift"
- "shouldPress"
- "sleepForTimeInterval:"
- "sourceLocation"
- "squeeze"
- "squeezeAtLocation:"
- "standardUserDefaults"
- "startedTest:"
- "stopProcessing"
- "stringWithFormat:"
- "stylusBarrelDoubleTap"
- "superclass"
- "superview"
- "swipeCount"
- "swipeSpeedFactor"
- "swipeWithComposer:fromPoint:toPoint:duration:"
- "tap:"
- "tap:pressure:"
- "tap:pressure:radius:"
- "tap:radius:"
- "tapToWakeAtPoint:"
- "testName"
- "testRunner:didFailRunningParameters:withError:"
- "testRunner:didFinishRunningParameters:"
- "testRunner:isReadyForRunningParameters:"
- "testRunner:shouldManagePPTLifetimeEvent:forParamaters:"
- "touchCurveFunction"
- "touchDown:"
- "touchDown:touchCount:"
- "touchDownAtPoints:touchCount:"
- "touchDownAtPoints:touchCount:pressure:"
- "touchDownAtPoints:touchCount:pressure:radius:"
- "touchDownAtPoints:touchCount:radius:"
- "touchFrequency"
- "touchScreenDigitizerSender"
- "touchSensitiveButtonClickWithPage:withUsage:withTouch:withNormalizedPositionY:withNormalizedPositionDeltaY:"
- "touchSensitiveButtonEngagedWithDuration:withPage:withUsage:withTouch:withNormalizedPositionY:withNormalizedPositionDeltaY:"
- "touchSensitiveButtonEngagedWithLiftWithDuration:withPage:withUsage:withTouch:withNormalizedPositionY:withNormalizedPositionDeltaY:"
- "touchSensitiveButtonEngagedWithPage:withUsage:withTouch:withNormalizedPositionY:withNormalizedPositionDeltaY:"
- "touchSensitiveButtonHoldWithDuration:withPage:withUsage:withTouch:withNormalizedPositionY:withNormalizedPositionDeltaY:"
- "touchSensitiveButtonHoldWithPage:withUsage:withTouch:withNormalizedPositionY:withNormalizedPositionDeltaY:"
- "touchSensitiveButtonIntermediatePressWithDuration:withPage:withUsage:withTouch:withNormalizedPositionY:withNormalizedPositionDeltaY:"
- "touchSensitiveButtonIntermediatePressWithPage:withUsage:withTouch:withNormalizedPositionY:withNormalizedPositionDeltaY:"
- "touchSensitiveButtonLiftWithPage:withUsage:"
- "touchSensitiveButtonReleaseHoldWithPage:withUsage:withTouch:withNormalizedPositionY:withNormalizedPositionDeltaY:"
- "touchTapDown:"
- "trackpadSender"
- "updateProgressTo:duration:"
- "useDefaultDurationForFlick"
- "useFlicks"
- "userInterfaceLayoutDirection"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"<RPTComposer>\"16"
- "v24@0:8@\"CAMediaTimingFunction\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"RCPEventSenderProperties\"16"
- "v24@0:8@\"RPTCoordinateSpaceConverter\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v32@0:8@\"<RPTComposer>\"16d24"
- "v32@0:8@\"NSArray\"16d24"
- "v32@0:8@\"NSNumber\"16@\"NSNumber\"24"
- "v32@0:8@\"RCPEventSenderProperties\"16@?<v@?@\"<RCPEventStreamComposer>\">24"
- "v32@0:8@\"RPTInteractionOptions\"16@?<v@?@\"<RPTComposer>\">24"
- "v32@0:8@\"RPTTestRunner\"16@\"<RPTTestParameters>\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16d24"
- "v32@0:8@16q24"
- "v32@0:8Q16Q24"
- "v32@0:8^{CGPoint=dd}16Q24"
- "v32@0:8^{CGVector=dd}16@24"
- "v32@0:8q16d24"
- "v32@0:8{CGPoint=dd}16"
- "v32@0:8{CGSize=dd}16"
- "v32@0:8{CGVector=dd}16"
- "v36@0:8@\"NSNumber\"16@\"NSNumber\"24C32"
- "v36@0:8@\"NSString\"16B24d28"
- "v36@0:8@16@24C32"
- "v36@0:8@16B24d28"
- "v36@0:8S16Q20@?28"
- "v36@0:8S16Q20@?<v@?@\"<RCPProgressEventStreamComposer>\">28"
- "v40@0:8@\"NSArray\"16@\"NSArray\"24d32"
- "v40@0:8@\"NSSet\"16d24q32"
- "v40@0:8@\"RPTTestRunner\"16@\"<RPTTestParameters>\"24@\"NSError\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24d32"
- "v40@0:8@16d24q32"
- "v40@0:8S16S20Q24@?32"
- "v40@0:8S16S20Q24@?<v@?@\"<RCPProgressEventStreamComposer>\">32"
- "v40@0:8^{CGPoint=dd}16Q24d32"
- "v40@0:8d16d24q32"
- "v40@0:8q16^{CGPoint=dd}24^{CGPoint=dd}32"
- "v40@0:8{CGPoint=dd}16Q32"
- "v40@0:8{CGPoint=dd}16d32"
- "v40@0:8{CGVector=dd}16d32"
- "v44@0:8@\"NSNumber\"16@\"NSNumber\"24C32@\"NSData\"36"
- "v44@0:8@16@24C32@36"
- "v44@0:8{CGPoint=dd}16B32d36"
- "v44@0:8{CGVector=dd}16I32d36"
- "v48@0:8^{CGPoint=dd}16Q24d32Q40"
- "v48@0:8^{CGPoint=dd}16Q24d32d40"
- "v48@0:8{CGPoint=dd}16d32d40"
- "v48@0:8{CGPoint=dd}16d32q40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v52@0:8@\"NSNumber\"16@\"NSNumber\"24i32d36d44"
- "v52@0:8@16@24i32d36d44"
- "v52@0:8{CGPoint=dd}16B32d36d44"
- "v56@0:8^{CGPoint=dd}16Q24d32d40d48"
- "v56@0:8{CGPoint=dd}16{CGPoint=dd}32d48"
- "v56@0:8{CGPoint=dd}16{CGVector=dd}32d48"
- "v60@0:8d16@\"NSNumber\"24@\"NSNumber\"32i40d44d52"
- "v60@0:8d16@24@32i40d44d52"
- "v60@0:8{CGPoint=dd}16B32d36d44d52"
- "v60@0:8{CGPoint=dd}16{CGVector=dd}32d48B56"
- "v64@0:8@16{CGPoint=dd}24{CGPoint=dd}40d56"
- "v64@0:8{CGPoint=dd}16d32d40d48Q56"
- "v64@0:8{CGPoint=dd}16d32d40d48d56"
- "v64@0:8{CGPoint=dd}16{CGPoint=dd}32d48d56"
- "v64@0:8{CGPoint=dd}16{CGPoint=dd}32d48q56"
- "v68@0:8{CGPoint=dd}16{CGPoint=dd}32d48d56B64"
- "v72@0:8{CGPoint=dd}16Q32{CGPoint=dd}40Q56d64"
- "v72@0:8{CGPoint=dd}16d32d40d48d56d64"
- "v72@0:8{CGPoint=dd}16{CGPoint=dd}32d48d56d64"
- "v76@0:8{CGPoint=dd}16{CGPoint=dd}32d48d56B64d68"
- "v84@0:8{CGPoint=dd}16{CGPoint=dd}32d48d56B64d68d76"
- "valueForKey:"
- "valueForKeyPath:"
- "vendorEventWithPage:withUsage:withVersion:"
- "vendorEventWithPage:withUsage:withVersion:withData:"
- "view"
- "viewControllerForColumn:"
- "visibleFrame"
- "waitDuration"
- "waitForPostEventStreamDelayWithHandler:"
- "windows"
- "zone"
- "{CGPoint=\"x\"d\"y\"d}"
- "{CGPoint=dd}16@0:8"
- "{CGPoint=dd}32@0:8{CGPoint=dd}16"
- "{CGPoint=dd}36@0:8{CGPoint=dd}16B32"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGRect={CGPoint=dd}{CGSize=dd}}48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"
- "{CGSize=dd}32@0:8{CGSize=dd}16"
- "{CGVector=\"dx\"d\"dy\"d}"
- "{CGVector=dd}16@0:8"
- "{CGVector=dd}32@0:8{CGVector=dd}16"
- "{pair<CGPoint, CGPoint>={CGPoint=dd}{CGPoint=dd}}16@0:8"

```
