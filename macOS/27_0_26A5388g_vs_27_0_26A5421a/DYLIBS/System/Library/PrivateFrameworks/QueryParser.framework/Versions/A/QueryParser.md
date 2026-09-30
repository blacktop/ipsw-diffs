## QueryParser

> `/System/Library/PrivateFrameworks/QueryParser.framework/Versions/A/QueryParser`

```diff

-3600.31.18.0.0
-  __TEXT.__text: 0x11edcc
-  __TEXT.__objc_methlist: 0x29b4
-  __TEXT.__const: 0x2d28
-  __TEXT.__gcc_except_tab: 0x13770
-  __TEXT.__oslogstring: 0x79ae
-  __TEXT.__cstring: 0xd445
+3600.31.21.0.0
+  __TEXT.__text: 0x11fdf8
+  __TEXT.__objc_methlist: 0x29ec
+  __TEXT.__const: 0x2d38
+  __TEXT.__gcc_except_tab: 0x138ac
+  __TEXT.__oslogstring: 0x7a0e
+  __TEXT.__cstring: 0xd475
   __TEXT.__ustring: 0x112
   __TEXT.__swift5_typeref: 0x5c2
   __TEXT.__constg_swiftt: 0x5f0

   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x52e8
+  __TEXT.__unwind_info: 0x5368
   __TEXT.__eh_frame: 0xc90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x20d8
+  __DATA_CONST.__objc_selrefs: 0x2118
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x1ff8
-  __DATA_CONST.__got: 0x778
-  __AUTH_CONST.__const: 0x4aa0
+  __DATA_CONST.__got: 0x780
+  __AUTH_CONST.__const: 0x4be0
   __AUTH_CONST.__cfstring: 0x12880
-  __AUTH_CONST.__objc_const: 0x4630
+  __AUTH_CONST.__objc_const: 0x4650
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x1b18
   __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_doubleobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1480
+  __AUTH_CONST.__auth_got: 0x1478
   __AUTH.__objc_data: 0x8e8
   __AUTH.__data: 0x448
-  __DATA.__objc_ivar: 0x308
-  __DATA.__data: 0x11b8
+  __DATA.__objc_ivar: 0x30c
+  __DATA.__data: 0x11b0
   __DATA.__bss: 0x1510
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x738

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4388
-  Symbols:   7109
-  CStrings:  3400
+  Functions: 4409
+  Symbols:   7139
+  CStrings:  3402
 
Symbols:
+ +[QPNeuralParserBridge _locked_cooldown]
+ +[QPNeuralParserBridge _locked_groundPersonPhrase:locale:argLabel:]
+ +[QPNeuralParserBridge _locked_groundTimePhrase:]
+ +[QPNeuralParserBridge _locked_prewarmForContext:]
+ +[QPNeuralParserBridge _locked_prewarm]
+ +[QPNeuralParserBridge _locked_sharedParserForContext:]
+ +[QPNeuralParserBridge _locked_sharedParser]
+ -[QPAssetManager(Testing) _test_scopedRBSAssertionAcquireFailureCount]
+ -[QPAssetManager(Testing) _test_waitForInvalidateCount:timeout:]
+ OBJC_IVAR_$_QPAssetManager._locked_scopedRBSAcquireFailureCount
+ _OBJC_CLASS_$_NSThread
+ _ZL11bridgeQueuev
+ __OBJC_$_CLASS_METHODS_QPAssetManager
+ __ZL11bridgeQueuev
+ __ZZL11bridgeQueuevE5queue
+ __ZZL11bridgeQueuevE9onceToken
+ ___31+[QPNeuralParserBridge prewarm]_block_invoke
+ ___32+[QPNeuralParserBridge cooldown]_block_invoke
+ ___41+[QPNeuralParserBridge groundTimePhrase:]_block_invoke
+ ___42+[QPNeuralParserBridge prewarmForContext:]_block_invoke
+ ___49+[QPNeuralParserBridge parse:options:completion:]_block_invoke
+ ___59+[QPNeuralParserBridge groundPersonPhrase:locale:argLabel:]_block_invoke
+ ___70-[QPAssetManager(Testing) _test_scopedRBSAssertionAcquireFailureCount]_block_invoke
+ ____ZL11bridgeQueuev_block_invoke
+ ___block_descriptor_48_ea8_32s40s_e17_v16?0"NSError"8l
+ ___block_descriptor_48_ea8_32s_e5_v8?0l
+ ___block_descriptor_56_ea8_32s40r_e5_v8?0l
+ ___block_descriptor_72_ea8_32s40s48s56r_e5_v8?0l
+ ___block_descriptor_88_ea8_32s40s48s56r64r72r_e5_v8?0l
+ ___block_descriptor_97_ea8_32s40s48s56r64r72r80r_e5_v8?0l
+ ___copy_helper_block_ea8_32s40s48s56r64r72r80r
+ ___destroy_helper_block_ea8_32s40s48s56r64r72r80r
+ _objc_msgSend$_locked_cooldown
+ _objc_msgSend$_locked_groundPersonPhrase:locale:argLabel:
+ _objc_msgSend$_locked_groundTimePhrase:
+ _objc_msgSend$_locked_prewarm
+ _objc_msgSend$_locked_prewarmForContext:
+ _objc_msgSend$_locked_sharedParser
+ _objc_msgSend$_locked_sharedParserForContext:
+ _objc_msgSend$_test_scopedRBSAssertionInvalidateCount
+ _objc_msgSend$invalidateWithQueue:completion:
+ _objc_msgSend$sleepForTimeInterval:
+ _objc_msgSend$timeIntervalSinceNow
- +[QPAssetManager(Testing) _test_scopedAssertionInvalidateDelayNsec]
- +[QPAssetManager(Testing) _test_setScopedAssertionInvalidateDelayNsec:]
- +[QPNeuralParserBridge sharedParserForContext:]
- +[QPNeuralParserBridge sharedParser]
- __OBJC_$_CLASS_METHODS_QPAssetManager(Testing)
- __ZL16_parserOnceToken
- __ZL37sQPScopedAssertionInvalidateDelayNsec
- ___47+[QPNeuralParserBridge sharedParserForContext:]_block_invoke
- _dispatch_after
- _objc_msgSend$groundPersonPhrase:locale:argLabel:
- _objc_msgSend$groundTimePhrase:
- _objc_msgSend$sharedParser
- _objc_msgSend$sharedParserForContext:
CStrings:
+ "[UAF] invalidateWithQueue:completion: reported error (flock marked released regardless): %s"
+ "com.apple.QueryParser.NeuralParserBridge"
```
