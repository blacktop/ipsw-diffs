## BrailleTranslation

> `/System/Library/PrivateFrameworks/ScreenReader.framework/Versions/A/Frameworks/BrailleTranslation.framework/Versions/A/BrailleTranslation`

```diff

-1048.3.0.0.0
-  __TEXT.__text: 0x32d00
-  __TEXT.__objc_methlist: 0x1d1c
+1050.3.0.0.0
+  __TEXT.__text: 0x33a10
+  __TEXT.__objc_methlist: 0x1d84
   __TEXT.__const: 0xc50
   __TEXT.__swift5_typeref: 0x234
   __TEXT.__constg_swiftt: 0xe04
   __TEXT.__swift5_reflstr: 0x66f
   __TEXT.__swift5_fieldmd: 0x440
-  __TEXT.__cstring: 0x839
+  __TEXT.__cstring: 0x83a
   __TEXT.__swift5_types: 0x20
-  __TEXT.__oslogstring: 0x59f
+  __TEXT.__oslogstring: 0x6e7
   __TEXT.__gcc_except_tab: 0xec
   __TEXT.__ustring: 0xc2
-  __TEXT.__unwind_info: 0xde8
+  __TEXT.__unwind_info: 0xe28
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1168
+  __DATA_CONST.__objc_selrefs: 0x11d0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x138
-  __DATA_CONST.__got: 0x268
-  __AUTH_CONST.__const: 0x410
+  __DATA_CONST.__got: 0x278
+  __AUTH_CONST.__const: 0x4d0
   __AUTH_CONST.__cfstring: 0x1180
-  __AUTH_CONST.__objc_const: 0x33e8
+  __AUTH_CONST.__objc_const: 0x3488
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x5c0
+  __AUTH_CONST.__auth_got: 0x5f0
   __AUTH.__objc_data: 0x1260
   __AUTH.__data: 0x7a0
-  __DATA.__objc_ivar: 0x164
+  __DATA.__objc_ivar: 0x178
   __DATA.__data: 0x608
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/Versions/A/AXCoreUtilities
   - /System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/Versions/A/AccessibilitySharedSupport
   - /System/Library/PrivateFrameworks/CoreEmoji.framework/Versions/A/CoreEmoji
+  - /System/Library/PrivateFrameworks/KeyboardServices.framework/KeyboardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1105
-  Symbols:   1592
-  CStrings:  192
+  Functions: 1122
+  Symbols:   1637
+  CStrings:  197
 
Symbols:
+ -[BRLTJMecabraWrapper _applyPendingUserWordKeyPairsIfNeeded]
+ -[BRLTJMecabraWrapper _moveToNextRawCandidate]
+ -[BRLTJMecabraWrapper _reloadUserWordKeyPairs]
+ -[BRLTJMecabraWrapper _setPendingUserWordKeyPairs:]
+ -[BRLTJMecabraWrapper _startObservingUserDictionary]
+ -[BRLTJMecabraWrapper initWithUnitTesting:requiresFullAnalysisCoverage:]
+ -[BRLTJMecabraWrapper(Testing) setUserWordKeyPairsForTesting:]
+ -[BRLTTranslationService _queue_replyOnce:]
+ -[BRLTTranslationService _queue_serviceProxyWithErrorHandler:]
+ GCC_except_table128
+ GCC_except_table130
+ GCC_except_table501
+ OBJC_IVAR_$_BRLTJMecabraWrapper._appliedUserWordKeyPairs
+ OBJC_IVAR_$_BRLTJMecabraWrapper._pendingUserWordKeyPairs
+ OBJC_IVAR_$_BRLTJMecabraWrapper._pendingUserWordKeyPairsLock
+ OBJC_IVAR_$_BRLTJMecabraWrapper._requiresFullAnalysisCoverage
+ OBJC_IVAR_$_BRLTJMecabraWrapper._textReplacementStore
+ _BRLTJTextReplacementsDidChange
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterRemoveObserver
+ _KSTextReplacementDidChangeNotification
+ _MecabraSetBuildDynamicDictionariesAsynchronously
+ _MecabraSetUserWordKeyPairs
+ _OBJC_CLASS_$__KSTextReplacementClientStore
+ __62-[BRLTTranslationService brailleForText:parameters:withReply:]_block_invoke
+ __62-[BRLTTranslationService textForBraille:parameters:withReply:]_block_invoke
+ __OBJC_$_INSTANCE_METHODS_BRLTJMecabraWrapper(Testing)
+ ___43-[BRLTTranslationService _queue_replyOnce:]_block_invoke
+ ___43-[BRLTTranslationService _queue_replyOnce:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32s40bs48r_e29_v24?0"NSString"8"NSData"16l
+ ___block_descriptor_64_e8_32s40s48bs56r_e5_v8?0l
+ ___copy_helper_block_e8_32s40b
+ ___copy_helper_block_e8_32s40b48r
+ ___copy_helper_block_e8_32s40s48b56r
+ _objc_msgSend$_applyPendingUserWordKeyPairsIfNeeded
+ _objc_msgSend$_moveToNextRawCandidate
+ _objc_msgSend$_queue_replyOnce:
+ _objc_msgSend$_queue_serviceProxyWithErrorHandler:
+ _objc_msgSend$_reloadUserWordKeyPairs
+ _objc_msgSend$_setPendingUserWordKeyPairs:
+ _objc_msgSend$_startObservingUserDictionary
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$initWithUnitTesting:requiresFullAnalysisCoverage:
+ _objc_msgSend$phrase
+ _objc_msgSend$shortcut
+ _objc_msgSend$textReplacementEntries
+ _objc_retainBlock
- GCC_except_table117
- GCC_except_table119
- GCC_except_table483
- __OBJC_$_INSTANCE_METHODS_BRLTJMecabraWrapper
- _objc_msgSend$initWithUnitTesting:
CStrings:
+ "Input back-translation on an invalidated service, replying empty. service:%@"
+ "Input back-translation unavailable, replying empty. service:%@ / %@"
+ "Output translation on an invalidated service, replying empty"
+ "Output translation unavailable, replying empty. %@"
+ "Text Replacement query returned no result; keeping previous user words"
```
