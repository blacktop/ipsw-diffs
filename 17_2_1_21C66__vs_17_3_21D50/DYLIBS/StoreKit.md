## StoreKit

> `/System/Library/Frameworks/StoreKit.framework/StoreKit`

```diff

-813.2.8.0.0
-  __TEXT.__text: 0x16f9b0
-  __TEXT.__auth_stubs: 0x3120
-  __TEXT.__objc_methlist: 0x46f4
-  __TEXT.__gcc_except_tab: 0xef0
+813.3.3.0.0
+  __TEXT.__text: 0x170280
+  __TEXT.__auth_stubs: 0x3110
+  __TEXT.__objc_methlist: 0x470c
+  __TEXT.__gcc_except_tab: 0xef4
   __TEXT.__const: 0x942a
-  __TEXT.__cstring: 0x731a
-  __TEXT.__oslogstring: 0x1fe0
+  __TEXT.__cstring: 0x72ba
+  __TEXT.__oslogstring: 0x20a9
   __TEXT.__dlopen_cstrs: 0x3dd
   __TEXT.__swift5_typeref: 0x3263
   __TEXT.__constg_swiftt: 0x2a84

   __TEXT.__swift5_capture: 0xd3c
   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__unwind_info: 0x6ecc
-  __TEXT.__eh_frame: 0x8660
+  __TEXT.__unwind_info: 0x6f40
+  __TEXT.__eh_frame: 0x8698
   __TEXT.__objc_classname: 0x1202
-  __TEXT.__objc_methname: 0xc902
+  __TEXT.__objc_methname: 0xc956
   __TEXT.__objc_methtype: 0x2af5
-  __TEXT.__objc_stubs: 0x8240
+  __TEXT.__objc_stubs: 0x82a0
   __DATA_CONST.__got: 0x7b0
-  __DATA_CONST.__const: 0x1960
+  __DATA_CONST.__const: 0x1988
   __DATA_CONST.__objc_classlist: 0x3c8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x12eb0
-  __DATA_CONST.__objc_selrefs: 0x2cd8
+  __DATA_CONST.__objc_const: 0x12ed0
+  __DATA_CONST.__objc_selrefs: 0x2cf0
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__const: 0x94c8
   __AUTH_CONST.__objc_const: 0x2798

   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_ptr: 0x190
-  __AUTH_CONST.__auth_got: 0x18a0
+  __AUTH_CONST.__auth_got: 0x1898
   __AUTH.__objc_data: 0x2488
   __AUTH.__data: 0x27c8
   __DATA.__objc_protorefs: 0x110
   __DATA.__objc_classrefs: 0x580
   __DATA.__objc_superrefs: 0x228
-  __DATA.__objc_ivar: 0x5d0
+  __DATA.__objc_ivar: 0x5d4
   __DATA.__data: 0x8258
   __DATA.__bss: 0xdc30
   __DATA.__common: 0x68

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11107
-  Symbols:   14041
-  CStrings:  3713
+  Functions: 11117
+  Symbols:   14062
+  CStrings:  3719
 
Symbols:
+ -[SKProductRemoteViewTask _dismissProductViewControllerWithResult:]
+ -[SKProductRemoteViewTask lookupProductWithParameters:completion:].cold.1
+ -[SKStoreProductViewController _isInvalidSubclass]
+ -[SKStoreProductViewController viewWillLayoutSubviews].cold.1
+ -[SKStoreProductViewController willMoveToParentViewController:].cold.1
+ GCC_except_table31
+ GCC_except_table39
+ GCC_except_table43
+ GCC_except_table48
+ GCC_except_table62
+ GCC_except_table73
+ GCC_except_table82
+ _OBJC_IVAR_$_SKStoreProductViewController._viewWillAppearWasCalled
+ ___47-[SKProductRemoteViewTask _displayItemIfNeeded]_block_invoke.30
+ ___47-[SKProductRemoteViewTask _displayItemIfNeeded]_block_invoke.cold.1
+ ___48-[SKProductRemoteViewTask _showExtensionWithID:]_block_invoke.46
+ ___66-[SKProductRemoteViewTask lookupProductWithParameters:completion:]_block_invoke.cold.3
+ ___67-[SKProductRemoteViewTask _dismissProductViewControllerWithResult:]_block_invoke
+ ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.39
+ ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.39.cold.1
+ ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.41
+ ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.41.cold.1
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_literal_global.33
+ ___block_literal_global.43
+ ___block_literal_global.52
+ ___block_literal_global.56
+ ___unnamed_2
+ _objc_msgSend$_dismissProductViewControllerWithResult:
+ _objc_msgSend$_isInvalidSubclass
+ _objc_msgSend$isMemberOfClass:
- GCC_except_table33
- GCC_except_table40
- GCC_except_table46
- GCC_except_table64
- ___47-[SKProductRemoteViewTask _displayItemIfNeeded]_block_invoke_3
- ___48-[SKProductRemoteViewTask _showExtensionWithID:]_block_invoke.45
- ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.38
- ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.38.cold.1
- ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.40
- ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.40.cold.1
- ___block_literal_global.32
- ___block_literal_global.42
- ___block_literal_global.51
- ___block_literal_global.55
CStrings:
+ "Invalid configuration for loading product. Dismissing."
+ "[%@] Invalid configuration for loading product."
+ "[%@] Invalid use of SKStoreProductViewController."
+ "[%{public}@][%{public}@]: Finishing controller."
+ "_dismissProductViewControllerWithResult:"
+ "_isInvalidSubclass"
+ "_viewWillAppearWasCalled"
- "Failed to decode transaction for %{public}s, price field out of bounds: %{public}ld"

```
