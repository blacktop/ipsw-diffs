## BrailleTranslation

> `/System/Library/PrivateFrameworks/BrailleTranslation.framework/BrailleTranslation`

```diff

-465.0.0.0.0
-  __TEXT.__text: 0x30fa8
-  __TEXT.__objc_methlist: 0x1d1c
+467.3.0.0.0
+  __TEXT.__text: 0x31b60
+  __TEXT.__objc_methlist: 0x1d84
   __TEXT.__const: 0xc50
   __TEXT.__swift5_typeref: 0x234
   __TEXT.__constg_swiftt: 0xe04
   __TEXT.__swift5_reflstr: 0x66f
   __TEXT.__swift5_fieldmd: 0x440
   __TEXT.__swift5_types: 0x20
-  __TEXT.__cstring: 0x7d9
-  __TEXT.__oslogstring: 0x59f
+  __TEXT.__cstring: 0x7da
+  __TEXT.__oslogstring: 0x6e7
   __TEXT.__gcc_except_tab: 0xe0
   __TEXT.__ustring: 0xc2
-  __TEXT.__unwind_info: 0xdb0
+  __TEXT.__unwind_info: 0xde8
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x590
+  __DATA_CONST.__const: 0x638
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1168
+  __DATA_CONST.__objc_selrefs: 0x11d0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x138
-  __DATA_CONST.__got: 0x268
+  __DATA_CONST.__got: 0x278
   __AUTH_CONST.__const: 0x230
   __AUTH_CONST.__cfstring: 0x1180
-  __AUTH_CONST.__objc_const: 0x33e8
+  __AUTH_CONST.__objc_const: 0x3488
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x718
+  __AUTH_CONST.__auth_got: 0x748
   __AUTH.__objc_data: 0x1260
   __AUTH.__data: 0x7a0
-  __DATA.__objc_ivar: 0x164
+  __DATA.__objc_ivar: 0x178
   __DATA.__data: 0x608
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport
   - /System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji
+  - /System/Library/PrivateFrameworks/KeyboardServices.framework/KeyboardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1088
-  Symbols:   1615
-  CStrings:  189
+  Functions: 1102
+  Symbols:   1657
+  CStrings:  194
 
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
+ GCC_except_table112
+ GCC_except_table114
+ GCC_except_table482
+ _BRLTJTextReplacementsDidChange
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterRemoveObserver
+ _KSTextReplacementDidChangeNotification
+ _MecabraSetBuildDynamicDictionariesAsynchronously
+ _MecabraSetUserWordKeyPairs
+ _OBJC_CLASS_$__KSTextReplacementClientStore
+ _OBJC_IVAR_$_BRLTJMecabraWrapper._appliedUserWordKeyPairs
+ _OBJC_IVAR_$_BRLTJMecabraWrapper._pendingUserWordKeyPairs
+ _OBJC_IVAR_$_BRLTJMecabraWrapper._pendingUserWordKeyPairsLock
+ _OBJC_IVAR_$_BRLTJMecabraWrapper._requiresFullAnalysisCoverage
+ _OBJC_IVAR_$_BRLTJMecabraWrapper._textReplacementStore
+ __OBJC_$_INSTANCE_METHODS_BRLTJMecabraWrapper(Testing)
+ ___43-[BRLTTranslationService _queue_replyOnce:]_block_invoke
+ ___43-[BRLTTranslationService _queue_replyOnce:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48r_e29_v24?0"NSString"8"NSData"16ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e5_v8?0lr56l8s48l8s32l8s40l8
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage_$_BrailleTranslation
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
- GCC_except_table106
- GCC_except_table108
- GCC_except_table468
- __OBJC_$_INSTANCE_METHODS_BRLTJMecabraWrapper
- _objc_msgSend$initWithUnitTesting:
CStrings:
+ "Input back-translation on an invalidated service, replying empty. service:%@"
+ "Input back-translation unavailable, replying empty. service:%@ / %@"
+ "Output translation on an invalidated service, replying empty"
+ "Output translation unavailable, replying empty. %@"
+ "Text Replacement query returned no result; keeping previous user words"
```
