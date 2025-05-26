## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3304.77.1.1.1
-  __TEXT.__text: 0x5483c
+3305.19.1.0.0
+  __TEXT.__text: 0x542c8
   __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_methlist: 0x29d0
+  __TEXT.__objc_methlist: 0x2a08
   __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x824
-  __TEXT.__cstring: 0x7e64
-  __TEXT.__oslogstring: 0x915d
+  __TEXT.__gcc_except_tab: 0x83c
+  __TEXT.__cstring: 0x7e2d
+  __TEXT.__oslogstring: 0x91c9
   __TEXT.__dlopen_cstrs: 0x238
-  __TEXT.__unwind_info: 0xe10
+  __TEXT.__unwind_info: 0xe24
   __TEXT.__objc_classname: 0x38b
-  __TEXT.__objc_methname: 0x8331
+  __TEXT.__objc_methname: 0x8355
   __TEXT.__objc_methtype: 0xc45
-  __TEXT.__objc_stubs: 0x6c00
+  __TEXT.__objc_stubs: 0x6c20
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x16b0
+  __DATA_CONST.__const: 0x15c0
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x2b08
-  __DATA_CONST.__objc_selrefs: 0x2028
+  __DATA_CONST.__objc_selrefs: 0x2038
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x340
   __DATA_CONST.__objc_superrefs: 0xc8

   __AUTH_CONST.__const: 0x2e0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__auth_got: 0x528
-  __AUTH.__objc_data: 0x140
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x2cc
-  __DATA.__data: 0x210
-  __DATA.__common: 0x18
-  __DATA.__bss: 0x8
+  __DATA.__data: 0x228
+  __DATA.__common: 0x0
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__const: 0x280
   __DATA_DIRTY.__objc_const: 0xc10
-  __DATA_DIRTY.__objc_data: 0xaa0
+  __DATA_DIRTY.__objc_data: 0xb40
   __DATA_DIRTY.__common: 0x48
   __DATA_DIRTY.__bss: 0x2a8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1173
-  Symbols:   4391
-  CStrings:  2959
+  Functions: 1170
+  Symbols:   4382
+  CStrings:  2965
 
Symbols:
+ +[UAFAutoAssetManager latestStatusForClients:error:]
+ +[UAFAutoAssetManager lockLatestAssetSet:]
+ +[UAFCommonUtilities isUODAttentionRequired:]
+ -[UAFXPCService _startObservers]
+ -[UAFXPCService _stopObservers]
+ GCC_except_table20
+ ___112+[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:]_block_invoke.328
+ ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.335
+ ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.336
+ ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.337
+ ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.338
+ ___27-[UAFXPCService runUpdates]_block_invoke.269
+ ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.319
+ ___42+[UAFAutoAssetManager lockLatestAssetSet:]_block_invoke
+ ___90-[UAFAssetSetObserver initWithAssetSet:configurationDirURLs:queue:updateHandler:delegate:]_block_invoke.253
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0ls32l8w48l8s40l8
+ ___block_literal_global.317
+ ___getAFUODAttentionRequiredSymbolLoc_block_invoke
+ _getAFUODAttentionRequiredSymbolLoc.ptr
+ _objc_msgSend$_startObservers
+ _objc_msgSend$isUODAttentionRequired:
+ _objc_msgSend$latestStatusForClients:error:
+ _objc_msgSend$lockAtomicSync:forAtomicInstance:withNeedPolicy:withTimeout:lockedAtomicEntries:error:
+ _objc_msgSend$lockLatestAssetSet:
- +[UAFAutoAssetSet latestAtomicInstance:completion:]
- GCC_except_table13
- ___112+[UAFAutoAssetManager configureAutoAssetsFromAssetSetUsages:subscriptions:configurationManager:lockIfUnchanged:]_block_invoke.333
- ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.341
- ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.342
- ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.343
- ___119+[UAFAutoAssetManager updateAutoAssetsFromAssetSetUsages:configurationManager:expensiveNetworking:progress:completion:]_block_invoke.344
- ___27-[UAFXPCService runUpdates]_block_invoke.270
- ___39+[UAFAutoAssetManager observeAssetSet:]_block_invoke.324
- ___51+[UAFAutoAssetSet latestAtomicInstance:completion:]_block_invoke
- ___51+[UAFAutoAssetSet latestAtomicInstance:completion:]_block_invoke.247
- ___53+[UAFAutoAssetManager lockLatestAssetSet:completion:]_block_invoke.308
- ___53+[UAFAutoAssetManager lockLatestAssetSet:completion:]_block_invoke_2.309
- ___53+[UAFAutoAssetManager lockLatestAssetSet:completion:]_block_invoke_3
- ___53+[UAFAutoAssetManager lockLatestAssetSet:completion:]_block_invoke_4
- ___65+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:]_block_invoke.328
- ___71+[UAFAutoAssetManager shouldCheckAssetSet:autoAssetSet:changed:locked:]_block_invoke
- ___90-[UAFAssetSetObserver initWithAssetSet:configurationDirURLs:queue:updateHandler:delegate:]_block_invoke.252
- ___98+[UAFAutoAssetManager conditionallyLockLatestAssetSet:newestInstance:checkAtomicError:completion:]_block_invoke.338
- ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
- ___block_descriptor_56_e8_32s40s48w_e5_v8?0ls32l8s40l8w48l8
- ___block_descriptor_64_e8_32s40s48bs_e42_v32?0"NSString"8"NSArray"16"NSError"24ls32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56bs_e42_v24?0"MAAutoAssetSetStatus"8"NSError"16ls32l8s56l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_literal_global.322
- _objc_msgSend$isTop13Locale:
- _objc_msgSend$latestAtomicInstance:completion:
- _objc_msgSend$lockAtomic:forAtomicInstance:completion:
- _objc_msgSend$lockAtomic:forAtomicInstance:withNeedPolicy:withTimeout:completion:
CStrings:
+ "%s Self is nil while calling Update notification for %{public}@"
+ "%s Starting observers"
+ "%s Stopping observers"
+ "+[UAFAutoAssetManager conditionallyLockLatestAssetSet:newestInstance:checkAtomicError:completion:]"
+ "+[UAFAutoAssetManager latestStatusForClients:error:]"
+ "+[UAFAutoAssetManager lockLatestAssetSet:]"
+ "-[UAFXPCService _startObservers]"
+ "-[UAFXPCService _stopObservers]"
+ "AFUODAttentionRequired"
+ "_startObservers"
+ "isUODAttentionRequired:"
+ "latestStatusForClients:error:"
+ "lockAtomicSync:forAtomicInstance:withNeedPolicy:withTimeout:lockedAtomicEntries:error:"
+ "lockLatestAssetSet:"
- "+[UAFAutoAssetManager lockLatestAssetSet:completion:]_block_invoke"
- "+[UAFAutoAssetManager lockLatestAssetSet:completion:]_block_invoke_4"
- "+[UAFAutoAssetManager shouldCheckAssetSet:autoAssetSet:changed:locked:]_block_invoke"
- "+[UAFAutoAssetSet latestAtomicInstance:completion:]"
- "+[UAFAutoAssetSet latestAtomicInstance:completion:]_block_invoke"
- "latestAtomicInstance:completion:"
- "lockAtomic:forAtomicInstance:completion:"
- "lockAtomic:forAtomicInstance:withNeedPolicy:withTimeout:completion:"

```
