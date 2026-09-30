## QueryUnderstanding

> `/System/Library/PrivateFrameworks/QueryUnderstanding.framework/Versions/A/QueryUnderstanding`

```diff

-3600.31.18.0.0
-  __TEXT.__text: 0x7a58
-  __TEXT.__objc_methlist: 0x754
-  __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0xe22
-  __TEXT.__oslogstring: 0x59a
-  __TEXT.__gcc_except_tab: 0x954
-  __TEXT.__unwind_info: 0x2c8
+3600.31.21.0.0
+  __TEXT.__text: 0x8834
+  __TEXT.__objc_methlist: 0x7ec
+  __TEXT.__const: 0xc8
+  __TEXT.__cstring: 0xebd
+  __TEXT.__oslogstring: 0x655
+  __TEXT.__gcc_except_tab: 0xa30
+  __TEXT.__unwind_info: 0x348
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x598
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x650
-  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_selrefs: 0x6d8
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x60
-  __DATA_CONST.__got: 0x158
-  __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x520
-  __AUTH_CONST.__objc_const: 0xe78
+  __DATA_CONST.__got: 0x178
+  __AUTH_CONST.__const: 0x300
+  __AUTH_CONST.__cfstring: 0x5a0
+  __AUTH_CONST.__objc_const: 0xfb0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x80
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x94
   __DATA.__data: 0x180
-  __DATA.__bss: 0x8
+  __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__data: 0x1
   __DATA_DIRTY.__bss: 0x69

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CoreNLP.framework/Versions/A/CoreNLP
   - /System/Library/PrivateFrameworks/EmbeddingService.framework/Versions/A/EmbeddingService
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpotlightResources.framework/Versions/A/SpotlightResources
   - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/Versions/A/UnifiedAssetFramework
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 156
-  Symbols:   575
-  CStrings:  254
+  Functions: 183
+  Symbols:   648
+  CStrings:  261
 
Symbols:
+ +[QUAssetHelper log]
+ +[QUAssetHelper sharedHelper]
+ -[QUAssetHelper .cxx_destruct]
+ -[QUAssetHelper filePathsForLocale:]
+ -[QUAssetHelper initWithAssetSetManager:]
+ -[QUAssetHelper init]
+ -[QUAssetHelper(Testing) _test_drainQueue]
+ -[QUAssetHelper(Testing) _test_scopedRBSAssertionAcquireCount]
+ -[QUAssetHelper(Testing) _test_scopedRBSAssertionAcquireFailureCount]
+ -[QUAssetHelper(Testing) _test_scopedRBSAssertionInvalidateCount]
+ -[QUAssetHelper(Testing) _test_waitForInvalidateCount:timeout:]
+ GCC_except_table10
+ GCC_except_table20
+ GCC_except_table5
+ GCC_except_table9
+ OBJC_IVAR_$_QUAssetHelper._assetSetManager
+ OBJC_IVAR_$_QUAssetHelper._locked_scopedRBSAcquireCount
+ OBJC_IVAR_$_QUAssetHelper._locked_scopedRBSAcquireFailureCount
+ OBJC_IVAR_$_QUAssetHelper._locked_scopedRBSInvalidateCount
+ OBJC_IVAR_$_QUAssetHelper._queue
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_QUAssetHelper
+ _OBJC_CLASS_$_RBSAssertion
+ _OBJC_CLASS_$_RBSDomainAttribute
+ _OBJC_CLASS_$_RBSTarget
+ _OBJC_METACLASS_$_QUAssetHelper
+ __36-[QUAssetHelper filePathsForLocale:]_block_invoke
+ __OBJC_$_CLASS_METHODS_QUAssetHelper
+ __OBJC_$_INSTANCE_METHODS_QUAssetHelper(Testing)
+ __OBJC_$_INSTANCE_VARIABLES_QUAssetHelper
+ __OBJC_CLASS_RO_$_QUAssetHelper
+ __OBJC_METACLASS_RO_$_QUAssetHelper
+ __ZSt9terminatev
+ __ZZ20+[QUAssetHelper log]E3log
+ __ZZ20+[QUAssetHelper log]E9onceToken
+ __ZZ29+[QUAssetHelper sharedHelper]E12sharedHelper
+ __ZZ29+[QUAssetHelper sharedHelper]E9onceToken
+ ___20+[QUAssetHelper log]_block_invoke
+ ___29+[QUAssetHelper sharedHelper]_block_invoke
+ ___36-[QUAssetHelper filePathsForLocale:]_block_invoke
+ ___42-[QUAssetHelper(Testing) _test_drainQueue]_block_invoke
+ ___62-[QUAssetHelper(Testing) _test_scopedRBSAssertionAcquireCount]_block_invoke
+ ___65-[QUAssetHelper(Testing) _test_scopedRBSAssertionInvalidateCount]_block_invoke
+ ___69-[QUAssetHelper(Testing) _test_scopedRBSAssertionAcquireFailureCount]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_48_ea8_32s40r_e5_v8?0l
+ ___block_descriptor_48_ea8_32s40s_e17_v16?0"NSError"8l
+ ___block_descriptor_48_ea8_32s40s_e5_v8?0l
+ ___block_descriptor_56_ea8_32s40s48r_e5_v8?0l
+ ___clang_call_terminate
+ ___copy_helper_block_ea8_32s40r
+ ___copy_helper_block_ea8_32s40s
+ ___cxa_begin_catch
+ ___destroy_helper_block_ea8_32s40r
+ _dispatch_async
+ _dispatch_queue_create
+ _dispatch_sync
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_msgSend$_test_scopedRBSAssertionInvalidateCount
+ _objc_msgSend$acquireWithError:
+ _objc_msgSend$attributeWithDomain:name:
+ _objc_msgSend$currentProcess
+ _objc_msgSend$filePathsForLocale:
+ _objc_msgSend$initWithAssetSetManager:
+ _objc_msgSend$initWithExplanation:target:attributes:
+ _objc_msgSend$invalidate
+ _objc_msgSend$invalidateWithQueue:completion:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$sharedHelper
+ _objc_msgSend$sleepForTimeInterval:
+ _objc_msgSend$timeIntervalSinceNow
- GCC_except_table2
CStrings:
+ "(nil)"
+ "FinishTaskUninterruptable"
+ "QueryUnderstanding holding UAFAssetSet during retrieve+enumerate"
+ "[UAF] Failed to acquire scoped RBS assertion; skipping OTA retrieval this call (locale=%@): %@"
+ "[UAF] invalidateWithQueue:completion: reported error (flock marked released regardless): %@"
+ "com.apple.QueryUnderstanding.AssetHelper"
+ "com.apple.common"
```
