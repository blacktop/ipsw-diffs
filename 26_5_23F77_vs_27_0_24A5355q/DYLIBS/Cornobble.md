## Cornobble

> `/System/Library/PrivateFrameworks/Cornobble.framework/Cornobble`

```diff

-51.0.0.0.0
-  __TEXT.__text: 0x4a38
-  __TEXT.__auth_stubs: 0x300
+56.0.0.0.0
+  __TEXT.__text: 0x49c0
   __TEXT.__objc_methlist: 0x804
   __TEXT.__const: 0xa8
   __TEXT.__gcc_except_tab: 0xf4
-  __TEXT.__cstring: 0x1b9
+  __TEXT.__cstring: 0x1be
   __TEXT.__dlopen_cstrs: 0x1d1
   __TEXT.__unwind_info: 0x268
-  __TEXT.__objc_classname: 0x130
-  __TEXT.__objc_methname: 0x1402
-  __TEXT.__objc_methtype: 0x7f1
-  __TEXT.__objc_stubs: 0x940
-  __DATA_CONST.__got: 0x40
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3f8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x190
+  __DATA_CONST.__got: 0x40
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0x1db8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x9c
   __DATA.__data: 0x180

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E9666587-3EE6-3AB6-8A51-9A6CF216BC27
+  UUID: E8DBCAB3-BC34-3821-934F-0D2D75889ED4
   Functions: 177
-  Symbols:   669
-  CStrings:  283
+  Symbols:   675
+  CStrings:  19
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutorelease
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x6
+ _objc_retain_x7
+ _objc_retain_x8
+ _objc_retain_x9
- _objc_autorelease
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
Functions:
~ +[CornobbleTestRunner playInteraction:completionHandler:] : 124 -> 120
~ +[CornobbleTestRunner performStandardScrollingTestNamed:onScrollView:iterations:canFlick:completionHandler:] : 196 -> 200
~ +[CornobbleTestRunner performStandardScrollingTestNamed:onScrollView:iterations:pages:direction:canFlick:completionHandler:] : 296 -> 300
~ +[CornobbleTestRunner performTestNamed:withEventStream:completionHandler:] : 640 -> 636
~ ___74+[CornobbleTestRunner performTestNamed:withEventStream:completionHandler:]_block_invoke : 128 -> 124
~ +[CornobbleTestRunner performTestNamed:usingComposer:completionHandler:] : 168 -> 172
~ _getRCPSyntheticEventStreamClass : 220 -> 224
~ +[CornobbleTestRunner performTestNamed:withRecapFile:onView:completionHandler:] : 172 -> 176
~ +[CornobbleTestRunner performFingerOnGlassScrollWithParameters:] : 180 -> 168
~ +[CornobbleTestRunner performFingerOnGlassScrollTestNamed:withParameters:completionHandler:] : 108 -> 104
~ +[CRNGroupScrollTestParameters parametersByCombining:testName:completionHandler:] : 128 -> 136
~ -[CRNGroupScrollTestParameters initWithTestName:withParameters:completionHandler:] : 136 -> 140
~ -[CRNGroupScrollTestParameters eventStream] : 308 -> 296
~ ___45-[CRNGroupScrollTestParameters composerBlock]_block_invoke : 300 -> 296
~ -[CRNGroupScrollTestParameters setParameters:] : 64 -> 12
~ _CRNViewFrameInWindow : 264 -> 244
~ _CRNQuadrantOfContentOffsetFor : 192 -> 188
~ +[CRNStandardScrollTestParameters parametersForTestName:scrollView:iterations:amplitude:direction:preventDismissalGestures:canUseFlicks:completionHandler:] : 428 -> 432
~ +[CRNStandardScrollTestParameters parametersForTestName:scrollView:iterations:direction:preventDismissalGestures:canUseFlicks:completionHandler:] : 440 -> 444
~ +[CRNStandardScrollTestParameters parametersForTestName:scrollView:iterations:preventDismissalGestures:canUseFlicks:completionHandler:] : 184 -> 188
~ -[CRNStandardScrollTestParameters initWithTestName:iterations:scrollingBounds:amplitude:direction:preventDismissalGestures:iterationDuration:canUseFlicks:completionHandler:] : 1220 -> 1184
~ -[CRNStandardScrollTestParameters composerBlock] : 1412 -> 1368
~ -[CRNStandardScrollTestParameters testName] : 16 -> 20
~ -[CRNStandardScrollTestParameters completionHandler] : 16 -> 20
~ -[CRNStandardScrollTestParameters amplitude] : 16 -> 20
~ -[CRNStandardScrollTestParameters setAmplitude:] : 16 -> 20
~ -[CRNStandardScrollTestParameters direction] : 16 -> 20
~ -[CRNStandardScrollTestParameters setDirection:] : 16 -> 20
~ -[CRNStandardScrollTestParameters preventDismissalGestures] : 16 -> 20
~ -[CRNStandardScrollTestParameters setPreventDismissalGestures:] : 16 -> 20
~ -[CRNStandardScrollTestParameters iterationDuration] : 16 -> 20
~ -[CRNStandardScrollTestParameters setIterationDuration:] : 16 -> 20
~ -[CRNStandardScrollTestParameters iterations] : 16 -> 20
~ -[CRNStandardScrollTestParameters setIterations:] : 16 -> 20
~ -[CRNStandardScrollTestParameters shouldFlick] : 16 -> 20
~ -[CRNStandardScrollTestParameters setShouldFlick:] : 16 -> 20
~ _getRCPInlinePlayerClass : 220 -> 224
~ _getRCPEventStreamClass : 220 -> 224
~ _getRCPSyntheticEventStreamClass : 220 -> 224
~ _getRCPPlayerPlaybackOptionsClass : 220 -> 224
~ _getRCPEventSenderPropertiesClass : 220 -> 224
~ -[CRNPagingScrollTestParameters eventStream] : 308 -> 296
~ -[CRNBlockScrollTestParameters initWithTestName:withComposerBlock:completionHandler:] : 180 -> 196
~ -[CRNBlockScrollTestParameters eventStream] : 308 -> 296
~ -[CRNOscillationScrollTestParameters eventStream] : 308 -> 296
~ +[CRNFluidSplitViewInteraction newWithSplitViewController:] : 148 -> 144
~ -[CRNFluidSplitViewInteraction composerBlock] : 244 -> 236
~ ___45-[CRNFluidSplitViewInteraction composerBlock]_block_invoke : 320 -> 312
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"RCPSyntheticEventStream\"16@0:8"
- "@\"UISplitViewController\""
- "@\"UIViewController\""
- "@100@0:8@16Q24{CGRect={CGPoint=dd}{CGSize=dd}}32d64q72d80B88@?92"
- "@104@0:8@16Q24{CGRect={CGPoint=dd}{CGSize=dd}}32d64q72B80d84B92@?96"
- "@108@0:8@16Q24{CGRect={CGPoint=dd}{CGSize=dd}}32B64B68d72d80q88d96B104"
- "@116@0:8@16Q24{CGRect={CGPoint=dd}{CGSize=dd}}32B64B68d72d80q88d96B104@?108"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@?24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8@16@?24@?32"
- "@56@0:8@16@24Q32B40B44@?48"
- "@56@0:8@16@24Q32q40B48B52"
- "@64@0:8@16@24Q32q40B48B52@?56"
- "@72@0:8@16@24Q32d40q48B56B60@?64"
- "@96@0:8@16Q24{CGRect={CGPoint=dd}{CGSize=dd}}32d64q72B80d84B92"
- "@?"
- "@?16@0:8"
- "@?<v@?>16@0:8"
- "@?<v@?@\"<RCPEventStreamComposer>\">16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CRNBlockBasedScrollTestParameters"
- "CRNBlockScrollTestParameters"
- "CRNFluidSplitViewInteraction"
- "CRNGroupScrollTestParameters"
- "CRNOscillationScrollTestParameters"
- "CRNPagingScrollTestParameters"
- "CRNScrollTestParameters"
- "CRNStandardScrollTestParameters"
- "CornobbleTestRunner"
- "CornobbleTestRunnerProtocol"
- "NSObject"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"NSArray\",&,N,V_parameters"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,V_testName"
- "T@\"NSString\",C,N,VtestName"
- "T@\"NSString\",R,C"
- "T@\"RCPSyntheticEventStream\",R,N"
- "T@?,C,N,V_completionHandler"
- "T@?,C,N,V_composerBlock"
- "T@?,R,C,N"
- "TB,N,V_finishWithHalfIteration"
- "TB,N,V_preventDismissalGestures"
- "TB,N,V_shouldFlick"
- "TB,N,V_useFlicks"
- "TQ,N,V_iterations"
- "TQ,R"
- "Td,N,V_amplitude"
- "Td,N,V_amplitudeVariationPerIteration"
- "Td,N,V_initialAmplitude"
- "Td,N,V_iterationDuration"
- "Tq,N,V_direction"
- "Tq,N,V_initialDirection"
- "Tq,R,N,V_realDirection"
- "Tq,R,N,V_realInitialDirection"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_scrollingBounds"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_amplitude"
- "_amplitudeVariationPerIteration"
- "_completionHandler"
- "_composerBlock"
- "_direction"
- "_finishWithHalfIteration"
- "_initialAmplitude"
- "_initialDirection"
- "_iterationDuration"
- "_iterations"
- "_parameters"
- "_preventDismissalGestures"
- "_primaryController"
- "_realDirection"
- "_realInitialDirection"
- "_scrollingBounds"
- "_shouldFlick"
- "_splitViewController"
- "_supplementalController"
- "_testName"
- "_useFlicks"
- "adjustedContentInset"
- "advanceTime:"
- "amplitude"
- "amplitudeVariationPerIteration"
- "arrayByAddingObjectsFromArray:"
- "arrayWithObjects:count:"
- "autorelease"
- "bounds"
- "class"
- "completionHandler"
- "componentsSeparatedByString:"
- "composerBlock"
- "conformsToProtocol:"
- "contentOffset"
- "contentSize"
- "convertRect:toCoordinateSpace:"
- "convertRect:toView:"
- "copy"
- "countByEnumeratingWithState:objects:count:"
- "currentDevice"
- "d"
- "d16@0:8"
- "debugDescription"
- "description"
- "direction"
- "dragWithStartPoint:endPoint:duration:"
- "eventStream"
- "eventStreamWithCLIArguments:"
- "eventStreamWithEventActions:"
- "eventStreamWithFileURL:error:"
- "failedTest:withFailure:"
- "finalFingerPosition"
- "finishWithHalfIteration"
- "finishedTest:waitForCommit:extraResults:"
- "fixedCoordinateSpace"
- "frame"
- "hash"
- "init"
- "initWithTestName:iterations:scrollingBounds:amplitude:direction:iterationDuration:useFlicks:completionHandler:"
- "initWithTestName:iterations:scrollingBounds:amplitude:direction:preventDismissalGestures:iterationDuration:canUseFlicks:"
- "initWithTestName:iterations:scrollingBounds:amplitude:direction:preventDismissalGestures:iterationDuration:canUseFlicks:completionHandler:"
- "initWithTestName:iterations:scrollingBounds:useFlicks:preventDismissalGestures:initialAmplitude:amplitudeVariationPerIteration:initialDirection:iterationDuration:finishWithHalfIteration:"
- "initWithTestName:iterations:scrollingBounds:useFlicks:preventDismissalGestures:initialAmplitude:amplitudeVariationPerIteration:initialDirection:iterationDuration:finishWithHalfIteration:completionHandler:"
- "initWithTestName:withComposerBlock:"
- "initWithTestName:withComposerBlock:completionHandler:"
- "initWithTestName:withParameters:completionHandler:"
- "initialAmplitude"
- "initialDirection"
- "initialFingerPosition"
- "isCornobbleAvailable"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "iterationDuration"
- "iterations"
- "liftUp:"
- "moveToPoint:duration:"
- "newWithSplitViewController:"
- "parameters"
- "parametersByCombining:testName:completionHandler:"
- "parametersForTestName:scrollView:iterations:amplitude:direction:preventDismissalGestures:canUseFlicks:completionHandler:"
- "parametersForTestName:scrollView:iterations:direction:preventDismissalGestures:canUseFlicks:"
- "parametersForTestName:scrollView:iterations:direction:preventDismissalGestures:canUseFlicks:completionHandler:"
- "parametersForTestName:scrollView:iterations:preventDismissalGestures:canUseFlicks:completionHandler:"
- "performFingerOnGlassScrollTestNamed:withParameters:completionHandler:"
- "performFingerOnGlassScrollWithParameters:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performStandardScrollingTestNamed:onScrollView:"
- "performStandardScrollingTestNamed:onScrollView:iterations:"
- "performStandardScrollingTestNamed:onScrollView:iterations:canFlick:"
- "performStandardScrollingTestNamed:onScrollView:iterations:canFlick:completionHandler:"
- "performStandardScrollingTestNamed:onScrollView:iterations:pages:canFlick:completionHandler:"
- "performStandardScrollingTestNamed:onScrollView:iterations:pages:direction:canFlick:completionHandler:"
- "performTestNamed:usingComposer:"
- "performTestNamed:usingComposer:completionHandler:"
- "performTestNamed:withEventStream:"
- "performTestNamed:withEventStream:completionHandler:"
- "performTestNamed:withRecapCommandString:onView:"
- "performTestNamed:withRecapCommandString:onView:completionHandler:"
- "performTestNamed:withRecapFile:onView:"
- "performTestNamed:withRecapFile:onView:completionHandler:"
- "playEventStream:options:completion:"
- "playInteraction:completionHandler:"
- "preventDismissalGestures"
- "q"
- "q16@0:8"
- "realDirection"
- "realInitialDirection"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "screen"
- "scrollWithComposer:fromPoint:toPoint:duration:"
- "scrollingBounds"
- "self"
- "sendFlickWithStartPoint:endPoint:duration:"
- "setAmplitude:"
- "setAmplitudeVariationPerIteration:"
- "setCompletionHandler:"
- "setComposerBlock:"
- "setDirection:"
- "setFinishWithHalfIteration:"
- "setInitialAmplitude:"
- "setInitialDirection:"
- "setIterationDuration:"
- "setIterations:"
- "setParameters:"
- "setPreventDismissalGestures:"
- "setScrollingBounds:"
- "setShouldFlick:"
- "setTestName:"
- "setUseFlicks:"
- "sharedApplication"
- "shouldFlick"
- "startedTest:"
- "superclass"
- "superview"
- "testName"
- "touchDown:"
- "useFlicks"
- "userInterfaceIdiom"
- "userInterfaceLayoutDirection"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"<CRNScrollTestParameters>\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v32@0:8@\"NSString\"16@\"RCPEventStream\"24"
- "v32@0:8@\"NSString\"16@\"UIScrollView\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"<RCPEventStreamComposer>\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSString\"16@\"NSString\"24@\"UIView\"32"
- "v40@0:8@\"NSString\"16@\"NSURL\"24@\"UIView\"32"
- "v40@0:8@\"NSString\"16@\"RCPEventStream\"24@?<v@?>32"
- "v40@0:8@\"NSString\"16@\"UIScrollView\"24Q32"
- "v40@0:8@\"NSString\"16@?<v@?@\"<RCPEventStreamComposer>\">24@?<v@?>32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24Q32"
- "v40@0:8@16@?24@?32"
- "v44@0:8@\"NSString\"16@\"UIScrollView\"24Q32B40"
- "v44@0:8@16@24Q32B40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"UIView\"32@?<v@?>40"
- "v48@0:8@\"NSString\"16@\"NSURL\"24@\"UIView\"32@?<v@?>40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v52@0:8@\"NSString\"16@\"UIScrollView\"24Q32B40@?<v@?>44"
- "v52@0:8@16@24Q32B40@?44"
- "v60@0:8@16@24Q32Q40B48@?52"
- "v64@0:8@16{CGPoint=dd}24{CGPoint=dd}40d56"
- "v68@0:8@16@24Q32Q40q48B56@?60"
- "view"
- "viewControllerForColumn:"
- "window"
- "zone"
- "{CGPoint=dd}16@0:8"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"

```
