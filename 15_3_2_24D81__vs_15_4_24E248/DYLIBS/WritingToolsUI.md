## WritingToolsUI

> `/System/Library/PrivateFrameworks/WritingToolsUI.framework/Versions/A/WritingToolsUI`

```diff

-44.228.200.0.0
-  __TEXT.__text: 0x23fe0
-  __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_methlist: 0x1ce0
-  __TEXT.__const: 0x604
-  __TEXT.__gcc_except_tab: 0x6a0
-  __TEXT.__oslogstring: 0x7b4
-  __TEXT.__cstring: 0x149e
+44.321.202.0.0
+  __TEXT.__text: 0x24754
+  __TEXT.__auth_stubs: 0x900
+  __TEXT.__objc_methlist: 0x272c
+  __TEXT.__const: 0x624
+  __TEXT.__gcc_except_tab: 0x6a4
+  __TEXT.__cstring: 0x12ce
+  __TEXT.__oslogstring: 0x7c0
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__constg_swiftt: 0xa8
-  __TEXT.__swift5_typeref: 0x36
-  __TEXT.__swift5_reflstr: 0x194
-  __TEXT.__swift5_fieldmd: 0xe4
+  __TEXT.__constg_swiftt: 0x10c
+  __TEXT.__swift5_typeref: 0x3c
+  __TEXT.__swift5_reflstr: 0x154
+  __TEXT.__swift5_fieldmd: 0xdc
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x9f0
-  __TEXT.__objc_classname: 0x453
-  __TEXT.__objc_methname: 0x7130
-  __TEXT.__objc_methtype: 0x1ab6
-  __TEXT.__objc_stubs: 0x6080
-  __DATA_CONST.__got: 0x410
-  __DATA_CONST.__const: 0x250
-  __DATA_CONST.__objc_classlist: 0x108
+  __TEXT.__swift5_types: 0x10
+  __TEXT.__unwind_info: 0xa00
+  __TEXT.__objc_classname: 0x46e
+  __TEXT.__objc_methname: 0x72b1
+  __TEXT.__objc_methtype: 0x1ae7
+  __TEXT.__objc_stubs: 0x6200
+  __DATA_CONST.__got: 0x428
+  __DATA_CONST.__const: 0x240
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b00
+  __DATA_CONST.__objc_selrefs: 0x1f10
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0x4b0
-  __AUTH_CONST.__const: 0xcc0
-  __AUTH_CONST.__cfstring: 0x7a0
-  __AUTH_CONST.__objc_const: 0x4d00
+  __AUTH_CONST.__auth_got: 0x490
+  __AUTH_CONST.__const: 0xd60
+  __AUTH_CONST.__cfstring: 0x840
+  __AUTH_CONST.__objc_const: 0x3b38
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0xa68
-  __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x234
+  __AUTH.__data: 0x180
+  __DATA.__objc_ivar: 0x238
   __DATA.__data: 0x640
-  __DATA.__bss: 0x390
+  __DATA.__bss: 0x3a0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
-  - /usr/lib/swift/libswiftSafariServices.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_errno.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 2879187A-B4C6-35DC-8F39-C8971D077CFA
-  Functions: 857
-  Symbols:   2619
-  CStrings:  1826
+  UUID: 7D65417A-41BD-3988-87A6-18AD910F80B3
+  Functions: 875
+  Symbols:   2662
+  CStrings:  1844
 
Symbols:
+ +[WTAffordanceUIController minNumberOfLinesDebug].cold.1
+ +[WTAffordanceUIController mustEnterSelectionAreaFirstToShowDebug].cold.1
+ +[WTAffordanceUIController mustPauseOnSelectionAreaToShowDebug].cold.1
+ +[WTAffordanceUIController selectionDwellShowDelayDebug].cold.1
+ +[WTAffordanceUIController shouldColorizeDebug].cold.1
+ +[WTWritingTools sharedInstance].cold.1
+ -[NSView(WTWritingToolsUtilities) scrollRectToVisible:animated:completionHandler:]
+ -[WTWritingToolsConfiguration configurationWithPrompt:]
+ -[WTWritingToolsConfiguration initWithRequestedTool:prompt:positioningRect:positioningView:]
+ -[WTWritingToolsConfiguration prompt]
+ -[WTWritingToolsConfiguration setPrompt:]
+ GCC_except_table135
+ GCC_except_table68
+ OBJC_IVAR_$_WTWritingToolsConfiguration._prompt
+ WTIATextAssistantLog.cold.1
+ WTIAWritingToolsLog.cold.1
+ WTInputAnalyticsLog.cold.1
+ _OBJC_CLASS_$_NSTextList
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_NSVisualEffectView
+ _WTSizingLog.cold.1
+ _WTSizingLog.log
+ _WTSizingLog.onceToken
+ _WTVCLog.cold.1
+ __108+[WTAffordanceUIController findGutterXLocation:selectedRange:previousXLocation:exitAfter:completionHandler:]_block_invoke.137
+ __110+[WTAffordanceUIController findFirstSelectionRectWithTextForClient:selectedRange:exitAfter:completionHandler:]_block_invoke.133
+ __130+[WTAffordanceUIController numberOfSelectedLinesOfTextIsAtLeast:client:selectedRange:rectOriginYPrev:exitAfter:completionHandler:]_block_invoke.129
+ __43-[WTWritingToolsViewController viewDidLoad]_block_invoke.404
+ __43-[WTWritingToolsViewController viewDidLoad]_block_invoke.407
+ __43-[WTWritingToolsViewController viewDidLoad]_block_invoke_2.438
+ __82-[NSView(WTWritingToolsUtilities) scrollRectToVisible:animated:completionHandler:]_block_invoke.2
+ __83-[WTWritingToolsRemoteViewController willBeginWritingToolsSession:requestContexts:]_block_invoke.146
+ __83-[WTWritingToolsRemoteViewController willBeginWritingToolsSession:requestContexts:]_block_invoke.148
+ __83-[WTWritingToolsRemoteViewController willBeginWritingToolsSession:requestContexts:]_block_invoke.150
+ __DATA__TtC14WritingToolsUI12Availability
+ __METACLASS_DATA__TtC14WritingToolsUI12Availability
+ __OBJC_$_CATEGORY_NSView_$_WTWritingToolsUtilities
+ __OBJC_$_INSTANCE_METHODS_NSView(WTWritingToolsUtilities|WritingToolsUI)
+ __WTSizingLog
+ ___63-[WTWritingToolsRemoteViewController endWritingToolsWithError:]_block_invoke_3
+ ___64-[WTWritingToolsViewController showInPopover:withConfiguration:]_block_invoke
+ ___82-[NSView(WTWritingToolsUtilities) scrollRectToVisible:animated:completionHandler:]_block_invoke
+ ____WTSizingLog_block_invoke
+ ___block_descriptor_72_e8_32s_e28_v16?0"NSAnimationContext"8l
+ ___block_descriptor_88_e8_32s40s_e5_v8?0l
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_1
+ __block_literal_global.154
+ __block_literal_global.157
+ __block_literal_global.161
+ __block_literal_global.163
+ __block_literal_global.188
+ __block_literal_global.194
+ __block_literal_global.215
+ __block_literal_global.221
+ __block_literal_global.223
+ __block_literal_global.396
+ __block_literal_global.4
+ __block_literal_global.440
+ __block_literal_global.445
+ __block_literal_global.447
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftDataDetection_$_WritingToolsUI
+ _kDesiredShapeTopMargin
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$animator
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$enclosingScrollView
+ _objc_msgSend$initWithRequestedTool:prompt:positioningRect:positioningView:
+ _objc_msgSend$prompt
+ _objc_msgSend$reflectScrolledClipView:
+ _objc_msgSend$runAnimationGroup:completionHandler:
+ _objc_msgSend$scrollRectToVisible:
+ _objc_msgSend$scrollRectToVisible:animated:completionHandler:
+ _objc_msgSend$setBounds:
+ _objc_msgSend$setBoundsOrigin:
+ _objc_msgSend$setPrompt:
+ _symbolic _____ 14WritingToolsUI12AvailabilityC
- GCC_except_table130
- GCC_except_table64
- __108+[WTAffordanceUIController findGutterXLocation:selectedRange:previousXLocation:exitAfter:completionHandler:]_block_invoke.136
- __110+[WTAffordanceUIController findFirstSelectionRectWithTextForClient:selectedRange:exitAfter:completionHandler:]_block_invoke.132
- __130+[WTAffordanceUIController numberOfSelectedLinesOfTextIsAtLeast:client:selectedRange:rectOriginYPrev:exitAfter:completionHandler:]_block_invoke.128
- __43-[WTWritingToolsViewController viewDidLoad]_block_invoke.368
- __43-[WTWritingToolsViewController viewDidLoad]_block_invoke.371
- __43-[WTWritingToolsViewController viewDidLoad]_block_invoke_2.402
- __83-[WTWritingToolsRemoteViewController willBeginWritingToolsSession:requestContexts:]_block_invoke.127
- __83-[WTWritingToolsRemoteViewController willBeginWritingToolsSession:requestContexts:]_block_invoke.129
- __83-[WTWritingToolsRemoteViewController willBeginWritingToolsSession:requestContexts:]_block_invoke.131
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSView_$_WritingToolsUI
- __OBJC_$_CATEGORY_NSView_$_WritingToolsUI
- ___swift_destroy_boxed_opaque_existential_1Tm
- __block_literal_global.153
- __block_literal_global.156
- __block_literal_global.158
- __block_literal_global.160
- __block_literal_global.162
- __block_literal_global.181
- __block_literal_global.187
- __block_literal_global.189
- __block_literal_global.360
- __block_literal_global.404
- __block_literal_global.409
- __block_literal_global.411
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_WritingToolsUI
- __swift_FORCE_LOAD_$_swiftSafariServices
- __swift_FORCE_LOAD_$_swiftSafariServices_$_WritingToolsUI
- __swift_FORCE_LOAD_$_swiftWebKit
- __swift_FORCE_LOAD_$_swiftWebKit_$_WritingToolsUI
- _kShapeTopMargin
- _objc_msgSend$mainBundle
- _swift_arrayDestroy
CStrings:
+ "!1"
+ "Learn More"
+ "Localizable"
+ "OK"
+ "Sizing"
+ "T@\"NSString\",&,N,V_prompt"
+ "TB,?,R,N"
+ "URLWithString:"
+ "WTUnsupportedLanguageErrorKey"
+ "WTWritingToolsUtilities"
+ "_TtC14WritingToolsUI12Availability"
+ "_prompt"
+ "animator"
+ "configurationWithPrompt:"
+ "dismissShareSheet"
+ "enclosingScrollView"
+ "handoffFromUCBWithPrompt:"
+ "https://support.apple.com/121115"
+ "initWithRequestedTool:prompt:positioningRect:positioningView:"
+ "prompt"
+ "reflectScrolledClipView:"
+ "runAnimationGroup:completionHandler:"
+ "scrollRectToVisible:"
+ "scrollRectToVisible:animated:completionHandler:"
+ "setBounds:"
+ "setBoundsOrigin:"
+ "setPrompt:"
+ "triggerShareSheetWithText:"
+ "v16@?0@\"NSAnimationContext\"8"
+ "v60@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16B48@?52"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Montara_NonInlineClients"
- "OpenEndedAdjustmentV2"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "handOffFromUCBWithPrompt:"
- "invalid Collection: less than 'count' elements in collection"
- "mainBundle"

```
