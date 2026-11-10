## QueryUnderstanding

> `/System/Library/PrivateFrameworks/QueryUnderstanding.framework/Versions/A/QueryUnderstanding`

```diff

-3600.31.21.0.0
-  __TEXT.__text: 0x8834
-  __TEXT.__objc_methlist: 0x7ec
+3605.8.1.0.0
+  __TEXT.__text: 0x99a4
+  __TEXT.__objc_methlist: 0x87c
   __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0xebd
-  __TEXT.__oslogstring: 0x655
-  __TEXT.__gcc_except_tab: 0xa30
-  __TEXT.__unwind_info: 0x348
+  __TEXT.__cstring: 0xef5
+  __TEXT.__oslogstring: 0x73a
+  __TEXT.__gcc_except_tab: 0xbc4
+  __TEXT.__unwind_info: 0x3e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x598
+  __DATA_CONST.__const: 0x5a0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d8
+  __DATA_CONST.__objc_selrefs: 0x778
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x60
-  __DATA_CONST.__got: 0x178
-  __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x5a0
-  __AUTH_CONST.__objc_const: 0xfb0
+  __DATA_CONST.__got: 0x188
+  __AUTH_CONST.__const: 0x3e0
+  __AUTH_CONST.__cfstring: 0x620
+  __AUTH_CONST.__objc_const: 0x1010
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x94
+  __DATA.__objc_ivar: 0xa0
   __DATA.__data: 0x180
-  __DATA.__bss: 0x28
-  __DATA_DIRTY.__objc_data: 0x280
+  __DATA.__bss: 0x18
+  __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__data: 0x1
-  __DATA_DIRTY.__bss: 0x69
+  __DATA_DIRTY.__bss: 0x79
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/Versions/A/CoreML
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 183
-  Symbols:   648
-  CStrings:  261
+  Functions: 211
+  Symbols:   718
+  CStrings:  269
 
Symbols:
+ +[QUAssetHelper _acquireAssetLockAssertion]
+ -[QUAssetHelper _cacheKeyForLocale:]
+ -[QUAssetHelper _onQueueHandleAssetSetUpdate]
+ -[QUAssetHelper _populateForLocale:]
+ -[QUAssetHelper _registerAssetObserver]
+ -[QUAssetHelper _requestSandboxExtension]
+ -[QUAssetHelper _unregisterAssetObserver]
+ -[QUAssetHelper dealloc]
+ -[QUAssetHelper(Testing) _test_pathCacheCount]
+ -[QUAssetHelper(Testing) _test_populateForLocale:]
+ -[QUAssetHelper(Testing) _test_populateShortCircuitCount]
+ -[QUAssetHelper(Testing) _test_simulateAssetUpdate]
+ GCC_except_table11
+ GCC_except_table13
+ GCC_except_table14
+ GCC_except_table2
+ GCC_except_table21
+ GCC_except_table27
+ GCC_except_table41
+ GCC_except_table59
+ GCC_except_table6
+ GCC_except_table7
+ GCC_except_table8
+ OBJC_IVAR_$_QUAssetHelper._assetSetCache
+ OBJC_IVAR_$_QUAssetHelper._locked_populateShortCircuitCount
+ OBJC_IVAR_$_QUAssetHelper._updateObserverToken
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_RBSAcquisitionCompletionAttribute
+ __36-[QUAssetHelper _populateForLocale:]_block_invoke
+ __ZL22kQUAssetHelperQueueKey
+ ___36-[QUAssetHelper _populateForLocale:]_block_invoke
+ ___36-[QUAssetHelper _populateForLocale:]_block_invoke_2
+ ___39-[QUAssetHelper _registerAssetObserver]_block_invoke
+ ___41-[QUAssetHelper _requestSandboxExtension]_block_invoke
+ ___41-[QUAssetHelper _unregisterAssetObserver]_block_invoke
+ ___46-[QUAssetHelper(Testing) _test_pathCacheCount]_block_invoke
+ ___51-[QUAssetHelper(Testing) _test_simulateAssetUpdate]_block_invoke
+ ___57-[QUAssetHelper(Testing) _test_populateShortCircuitCount]_block_invoke
+ ___block_descriptor_40_ea8_32s_e17_v16?0"NSError"8l
+ ___block_descriptor_40_ea8_32s_e5_v8?0l
+ ___block_descriptor_40_ea8_32w_e5_v8?0l
+ ___block_descriptor_56_ea8_32s40s48s_e17_v16?0"NSError"8l
+ ___block_descriptor_64_ea8_32s40s48r56r_e5_v8?0l
+ ___copy_helper_block_ea8_32s
+ ___copy_helper_block_ea8_32s40s48r56r
+ ___copy_helper_block_ea8_32s40s48s
+ ___copy_helper_block_ea8_32w
+ ___destroy_helper_block_ea8_32s
+ ___destroy_helper_block_ea8_32s40s48r56r
+ ___destroy_helper_block_ea8_32s40s48s
+ ___destroy_helper_block_ea8_32w
+ _dispatch_get_specific
+ _dispatch_queue_set_specific
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _objc_msgSend$_acquireAssetLockAssertion
+ _objc_msgSend$_cacheKeyForLocale:
+ _objc_msgSend$_onQueueHandleAssetSetUpdate
+ _objc_msgSend$_populateForLocale:
+ _objc_msgSend$_registerAssetObserver
+ _objc_msgSend$_requestSandboxExtension
+ _objc_msgSend$_unregisterAssetObserver
+ _objc_msgSend$attributeWithCompletionPolicy:
+ _objc_msgSend$consistencyToken
+ _objc_msgSend$isLatestConsistencyToken:
+ _objc_msgSend$null
+ _objc_msgSend$observeAssetSet:queue:handler:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$requestSandboxExtension:queue:completion:
+ _objc_opt_isKindOfClass
- GCC_except_table10
- GCC_except_table9
- ___block_descriptor_48_ea8_32s40s_e17_v16?0"NSError"8l
CStrings:
+ ""
+ "%@.%@.%@"
+ "UAFAssetAccess"
+ "[UAF] Asset set changed during enumeration for locale %@ — discarding"
+ "[UAF] Failed to acquire scoped RBS assertion: %@"
+ "[UAF] Failed to request sandbox extension for %@: %@"
+ "[UAF] Timed out waiting for UAF flock release; skipping enumeration (locale=%@)"
+ "[UAF] UAFAssetAccess unavailable, using FinishTaskUninterruptable: %@"
+ "com.apple.UnifiedAssetFramework"
- "[UAF] Failed to acquire scoped RBS assertion; skipping OTA retrieval this call (locale=%@): %@"
```
