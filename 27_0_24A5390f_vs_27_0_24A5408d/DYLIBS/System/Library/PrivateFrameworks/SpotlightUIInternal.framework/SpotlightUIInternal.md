## SpotlightUIInternal

> `/System/Library/PrivateFrameworks/SpotlightUIInternal.framework/SpotlightUIInternal`

```diff

-236.0.11.100.0
-  __TEXT.__text: 0x4ea80
-  __TEXT.__objc_methlist: 0x5d00
-  __TEXT.__const: 0x1398
-  __TEXT.__cstring: 0x1218
-  __TEXT.__oslogstring: 0x12da
+236.0.21.100.0
+  __TEXT.__text: 0x4f1d4
+  __TEXT.__objc_methlist: 0x5d28
+  __TEXT.__const: 0x13c0
+  __TEXT.__cstring: 0x13c2
+  __TEXT.__oslogstring: 0x132a
   __TEXT.__gcc_except_tab: 0x27c
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__constg_swiftt: 0x684
-  __TEXT.__swift5_typeref: 0xe00
-  __TEXT.__swift5_fieldmd: 0x3a0
-  __TEXT.__swift5_capture: 0x26c
-  __TEXT.__swift5_types: 0x60
-  __TEXT.__swift_as_entry: 0x34
-  __TEXT.__swift_as_ret: 0x44
-  __TEXT.__swift_as_cont: 0x84
-  __TEXT.__swift5_reflstr: 0x326
+  __TEXT.__swift5_typeref: 0xe1a
+  __TEXT.__swift5_capture: 0x270
+  __TEXT.__constg_swiftt: 0x6c8
+  __TEXT.__swift5_reflstr: 0x330
+  __TEXT.__swift5_fieldmd: 0x3bc
+  __TEXT.__swift5_types: 0x64
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x128
   __TEXT.__swift5_proto: 0x60
+  __TEXT.__swift_as_entry: 0x40
+  __TEXT.__swift_as_ret: 0x50
+  __TEXT.__swift_as_cont: 0x8c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x15b8
-  __TEXT.__eh_frame: 0xbf0
+  __TEXT.__unwind_info: 0x1600
+  __TEXT.__eh_frame: 0xc70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xb70
-  __DATA_CONST.__objc_classlist: 0x1d8
+  __DATA_CONST.__const: 0xc60
+  __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x42d8
+  __DATA_CONST.__objc_selrefs: 0x4320
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x90
-  __DATA_CONST.__got: 0xa88
-  __AUTH_CONST.__const: 0xca8
-  __AUTH_CONST.__cfstring: 0x15a0
-  __AUTH_CONST.__objc_const: 0x91f0
+  __DATA_CONST.__got: 0xa90
+  __AUTH_CONST.__const: 0xcc8
+  __AUTH_CONST.__cfstring: 0x1900
+  __AUTH_CONST.__objc_const: 0x92a0
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0xda0
+  __AUTH_CONST.__auth_got: 0xdb0
   __AUTH.__objc_data: 0xb98
-  __AUTH.__data: 0x3d0
-  __DATA.__objc_ivar: 0x420
-  __DATA.__data: 0x1738
-  __DATA.__bss: 0xbf8
+  __AUTH.__data: 0x470
+  __DATA.__objc_ivar: 0x418
+  __DATA.__data: 0x1740
+  __DATA.__bss: 0xc28
   __DATA_DIRTY.__objc_data: 0xac8
   __DATA_DIRTY.__data: 0x1c8
   __DATA_DIRTY.__bss: 0x260

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2038
-  Symbols:   4822
-  CStrings:  337
+  Functions: 2058
+  Symbols:   4841
+  CStrings:  367
 
Symbols:
+ +[SPUIFeedbackManager feedbackQueue]
+ +[SPUISearchViewController stringForInvocationSource:]
+ +[SPUISearchViewController stringForPresentationSource:]
+ -[SPUISearchHeader(SUICompletionViewControllerDelegate) completionTypedQueryAddressesExternalProvider:]
+ -[SPUISearchViewController currentlyDisplayedResultsViewController]
+ -[SPUISearchViewController shouldAllowAskSiriForModel:]
+ GCC_except_table92
+ _OBJC_CLASS_$_NSCache
+ __DATA__TtCC19SpotlightUIInternal36SPUIExternalGenerativePartnerManagerP33_A96508C3EE92D1DF1644A8F59FE141E316ProviderSnapshot
+ __IVARS__TtCC19SpotlightUIInternal36SPUIExternalGenerativePartnerManagerP33_A96508C3EE92D1DF1644A8F59FE141E316ProviderSnapshot
+ __METACLASS_DATA__TtCC19SpotlightUIInternal36SPUIExternalGenerativePartnerManagerP33_A96508C3EE92D1DF1644A8F59FE141E316ProviderSnapshot
+ __OBJC_$_CLASS_METHODS__TtC19SpotlightUIInternal36SPUIExternalGenerativePartnerManager(SpotlightUIInternal)
+ __OBJC_$_PROP_LIST_SearchUICommandDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SUICompletionViewControllerDelegate
+ ___36+[SPUIFeedbackManager feedbackQueue]_block_invoke
+ ___48+[SPUIFeedbackManager resultsDidFinishForModel:]_block_invoke
+ ___block_descriptor_65_e8_32s40s_e5_v8?0ls32l8s40l8
+ _feedbackQueue.feedbackQueue
+ _feedbackQueue.onceToken
+ _objc_msgSend$currentlyDisplayedResultsViewController
+ _objc_msgSend$feedbackQueue
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$shouldAllowAskSiriForModel:
+ _objc_msgSend$showsBackButton
+ _objc_msgSend$stringForAuthenticationState:
+ _objc_msgSend$stringForInvocationSource:
+ _objc_msgSend$stringForPresentationSource:
+ _objc_msgSend$typedQueryAddressesExternalProvider:
+ _symbolic Say_____G 13CampoServices15MontaraProviderV
+ _symbolic _____ 19SpotlightUIInternal36SPUIExternalGenerativePartnerManagerC16ProviderSnapshot33_A96508C3EE92D1DF1644A8F59FE141E3LLC
+ _symbolic _____XMT 19SpotlightUIInternal36SPUIExternalGenerativePartnerManagerC
- -[SPUITextField isCursorVisible]
- -[SPUITextField setIsCursorVisible:]
- -[SPUITextView caretAssertion]
- -[SPUITextView isCursorVisible]
- -[SPUITextView setCaretAssertion:]
- -[SPUITextView setIsCursorVisible:]
- GCC_except_table89
- _OBJC_IVAR_$_SPUITextField.isCursorVisible
- _OBJC_IVAR_$_SPUITextView._caretAssertion
- __CLASS_METHODS__TtC19SpotlightUIInternal36SPUIExternalGenerativePartnerManager
- _objc_msgSend$isFirstInitialization
- _objc_msgSend$setIsCursorVisible:
CStrings:
+ "AppToolbar"
+ "AskSiri"
+ "BreadCrumb"
+ "Camera"
+ "ContextMenu"
+ "DynamicIslandPullDown"
+ "HardwareKeyboard"
+ "HomeScreenButton"
+ "KeyboardCandidateBar"
+ "NO"
+ "NotificationCenter"
+ "PartialPullDown"
+ "Photos"
+ "PullDownHomeScreen"
+ "PullDownNotificationCenter"
+ "ScreenshotUI"
+ "ScribbleUI"
+ "SiriApp"
+ "TextCursorAffordance"
+ "TextEditMenu"
+ "TextEditWritingToolsPanel"
+ "TextFormatBar"
+ "TodayView"
+ "Unknown"
+ "Unspecified"
+ "VisualIntelligence"
+ "YES"
+ "com.apple.spotlightui.feedbackQueue"
+ "invoked deviceLockState=%@ isOverApp=%@ presentationSource=%@ afInvocationSource=%@"
+ "providers"
```
