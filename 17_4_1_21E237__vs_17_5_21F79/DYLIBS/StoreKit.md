## StoreKit

> `/System/Library/Frameworks/StoreKit.framework/StoreKit`

```diff

-813.4.32.0.0
-  __TEXT.__text: 0x16b074
+813.4.41.0.0
+  __TEXT.__text: 0x16ed04
   __TEXT.__auth_stubs: 0x3110
-  __TEXT.__objc_methlist: 0x4754
+  __TEXT.__objc_methlist: 0x47fc
   __TEXT.__gcc_except_tab: 0xf0c
-  __TEXT.__const: 0x8e5a
-  __TEXT.__cstring: 0x76aa
-  __TEXT.__oslogstring: 0x20a9
+  __TEXT.__const: 0x8f1a
+  __TEXT.__cstring: 0x772a
+  __TEXT.__oslogstring: 0x21ce
   __TEXT.__dlopen_cstrs: 0x43f
-  __TEXT.__swift5_typeref: 0x2f85
-  __TEXT.__constg_swiftt: 0x21d4
-  __TEXT.__swift5_reflstr: 0x1d35
-  __TEXT.__swift5_fieldmd: 0x29a8
+  __TEXT.__swift5_typeref: 0x2fd1
+  __TEXT.__constg_swiftt: 0x21f0
+  __TEXT.__swift5_reflstr: 0x1d75
+  __TEXT.__swift5_fieldmd: 0x29c4
   __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_assocty: 0x620
-  __TEXT.__swift5_proto: 0x878
-  __TEXT.__swift5_types: 0x334
-  __TEXT.__swift5_capture: 0xd70
+  __TEXT.__swift5_assocty: 0x638
+  __TEXT.__swift5_proto: 0x884
+  __TEXT.__swift5_types: 0x338
+  __TEXT.__swift5_capture: 0xd90
   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__unwind_info: 0x6cd0
-  __TEXT.__eh_frame: 0x8908
-  __TEXT.__objc_classname: 0x1217
-  __TEXT.__objc_methname: 0xcaa6
-  __TEXT.__objc_methtype: 0x2b8d
-  __TEXT.__objc_stubs: 0x82e0
+  __TEXT.__unwind_info: 0x7238
+  __TEXT.__eh_frame: 0x8d30
+  __TEXT.__objc_classname: 0x1235
+  __TEXT.__objc_methname: 0xcbae
+  __TEXT.__objc_methtype: 0x2be3
+  __TEXT.__objc_stubs: 0x83c0
   __DATA_CONST.__got: 0x728
   __DATA_CONST.__const: 0x1968
-  __DATA_CONST.__objc_classlist: 0x3c8
+  __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x12eb0
-  __DATA_CONST.__objc_selrefs: 0x2d08
+  __DATA_CONST.__objc_const: 0x13090
+  __DATA_CONST.__objc_selrefs: 0x2d48
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_classrefs: 0x580
   __DATA_CONST.__objc_superrefs: 0x228
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__const: 0x8ee0
-  __AUTH_CONST.__objc_const: 0x2798
-  __AUTH_CONST.__cfstring: 0x3780
+  __AUTH_CONST.__const: 0x9060
+  __AUTH_CONST.__objc_const: 0x2828
+  __AUTH_CONST.__cfstring: 0x37c0
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x1898
-  __AUTH.__objc_data: 0x2488
-  __AUTH.__data: 0x1c90
-  __DATA.__objc_ivar: 0x5dc
-  __DATA.__data: 0x9a98
-  __DATA.__bss: 0xd1c0
+  __AUTH.__objc_data: 0x24d8
+  __AUTH.__data: 0x1c20
+  __DATA.__objc_ivar: 0x5e8
+  __DATA.__data: 0x9ba8
+  __DATA.__bss: 0xd2b0
   __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0x370
-  __DATA_DIRTY.__data: 0x70
+  __DATA_DIRTY.__data: 0xe0
   __DATA_DIRTY.__bss: 0x38
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9B9EDA97-9624-39FD-B7A4-9DEB7AC50543
-  Functions: 10253
-  Symbols:   13153
-  CStrings:  4199
+  UUID: F2CA7CCD-9558-3093-AADB-3353C09DD93C
+  Functions: 10393
+  Symbols:   13363
+  CStrings:  4222
 
Symbols:
+ +[ExternalPurchaseLinkResponse supportsSecureCoding]
+ -[ExternalPurchaseLinkResponse .cxx_destruct]
+ -[ExternalPurchaseLinkResponse encodeWithCoder:]
+ -[ExternalPurchaseLinkResponse initWithCoder:]
+ -[ExternalPurchaseLinkResponse initWithSingle:multi:]
+ -[ExternalPurchaseLinkResponse multi]
+ -[ExternalPurchaseLinkResponse single]
+ -[SKProductPageExtension userDidInteractWithProduct:]
+ -[SKProductPageRemoteViewController userDidInteractWithProduct:]
+ -[SKProductRemoteViewTask productPageRemoteViewController:userDidInteractWithProduct:]
+ -[SKProductRemoteViewTask productPageRemoteViewController:userDidInteractWithProduct:].cold.1
+ -[SKRemoteProductViewController userDidInteractWithProduct:]
+ -[SKStoreProductViewController _isInvalidSubclass].cold.1
+ -[SKStoreProductViewController _isInvalidSubclass].cold.2
+ -[SKStoreProductViewController _userDidInteractWithProduct:]
+ GCC_except_table59
+ GCC_except_table61
+ GCC_except_table67
+ GCC_except_table69
+ GCC_except_table75
+ GCC_except_table77
+ GCC_except_table79
+ GCC_except_table81
+ GCC_except_table83
+ _OBJC_CLASS_$_ExternalPurchaseLinkResponse
+ _OBJC_IVAR_$_ExternalPurchaseLinkResponse._multi
+ _OBJC_IVAR_$_ExternalPurchaseLinkResponse._single
+ _OBJC_IVAR_$_SKStoreProductViewController._bundleID
+ _OBJC_METACLASS_$_ExternalPurchaseLinkResponse
+ __OBJC_$_CLASS_METHODS_ExternalPurchaseLinkResponse
+ __OBJC_$_CLASS_PROP_LIST_ExternalPurchaseLinkResponse
+ __OBJC_$_INSTANCE_METHODS_ExternalPurchaseLinkResponse
+ __OBJC_$_INSTANCE_VARIABLES_ExternalPurchaseLinkResponse
+ __OBJC_$_PROP_LIST_ExternalPurchaseLinkResponse
+ __OBJC_CLASS_PROTOCOLS_$_ExternalPurchaseLinkResponse
+ __OBJC_CLASS_RO_$_ExternalPurchaseLinkResponse
+ __OBJC_METACLASS_RO_$_ExternalPurchaseLinkResponse
+ ___47-[SKProductRemoteViewTask _displayItemIfNeeded]_block_invoke_3
+ ___48-[SKProductRemoteViewTask _showExtensionWithID:]_block_invoke.45
+ ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.38
+ ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.38.cold.1
+ ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.40
+ ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.40.cold.1
+ ___block_literal_global.32
+ ___block_literal_global.42
+ ___block_literal_global.51
+ ___block_literal_global.55
+ _associated conformance 15StoreKit_Shared25ExternalGatewayOptionsKeyOSHAASQ
+ _block_copy_helper.29
+ _block_descriptor.31
+ _block_destroy_helper.30
+ _objc_msgSend$_userDidInteractWithProduct:
+ _objc_msgSend$initWithSingle:multi:
+ _objc_msgSend$multi
+ _objc_msgSend$productPageRemoteViewController:userDidInteractWithProduct:
+ _objc_msgSend$productViewController:userDidInteractWithProduct:
+ _objc_msgSend$single
+ _objc_msgSend$userDidInteractWithProduct:
+ _objectdestroy.15Tm
+ _symbolic Say_____GSg 10Foundation3URLV
+ _symbolic ScCySay_____GSg_____G 10Foundation3URLV s5NeverO
+ _symbolic _____ 15StoreKit_Shared25ExternalGatewayOptionsKeyO
+ _symbolic _____y_____G s11_SetStorageC 8StoreKit20ExternalPurchaseLinkO6OptionV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 8StoreKit20ExternalPurchaseLinkO6OptionV
- -[SKProductRemoteViewTask lookupProductWithParameters:completion:].cold.1
- -[SKStoreProductViewController willMoveToParentViewController:].cold.1
- GCC_except_table56
- GCC_except_table58
- GCC_except_table62
- GCC_except_table68
- GCC_except_table72
- GCC_except_table76
- GCC_except_table78
- GCC_except_table80
- GCC_except_table82
- ___47-[SKProductRemoteViewTask _displayItemIfNeeded]_block_invoke.30
- ___47-[SKProductRemoteViewTask _displayItemIfNeeded]_block_invoke.cold.1
- ___48-[SKProductRemoteViewTask _showExtensionWithID:]_block_invoke.46
- ___66-[SKProductRemoteViewTask lookupProductWithParameters:completion:]_block_invoke.cold.3
- ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.39
- ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.39.cold.1
- ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.41
- ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.41.cold.1
- ___block_literal_global.33
- ___block_literal_global.43
- ___block_literal_global.52
- ___block_literal_global.56
CStrings:
+ "\x02\x12\x11#\x12\x12\x11\x11\x13"
+ "00:04:27"
+ "Apr 19 2024"
+ "ExternalPurchaseLinkResponse"
+ "Subclassing SKStoreProductViewController is not supported. Please update your implementation to stop subclassing SKStoreProductViewController. This will become an error in the future."
+ "T@\"NSArray\",R,N,V_multi"
+ "T@\"NSURL\",R,N,V_single"
+ "[%@] Subclassing SKStoreProductViewController is not supported."
+ "[%{public}@][%{public}@]: Invalid SKProductPageExtensionInteractionType: %lu"
+ "[%{public}@][%{public}@]: Product page user did interact with product."
+ "_multi"
+ "_single"
+ "_userDidInteractWithProduct:"
+ "com.apple.StoreKit"
+ "externalPurchaseLinkURLsForBundleID:reply:"
+ "externalPurchaseURL"
+ "initWithSingle:multi:"
+ "multi"
+ "productPageRemoteViewController:userDidInteractWithProduct:"
+ "productViewController:userDidInteractWithProduct:"
+ "single"
+ "userDidInteractWithProduct:"
+ "v16@?0@\"ExternalPurchaseLinkResponse\"8"
+ "v32@0:8@\"NSString\"16@?<v@?@\"ExternalPurchaseLinkResponse\">24"
+ "v32@0:8@\"SKProductPageRemoteViewController\"16Q24"
+ "v32@0:8@16Q24"
- "\x02\x12\x11#\x12\x12\x11\x13"
- "02:29:54"
- "Invalid configuration for loading product. Dismissing."
- "Mar  9 2024"
- "[%@] Invalid configuration for loading product."
- "externalPurchaseLinkURLForBundleID:reply:"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSURL\">24"

```
