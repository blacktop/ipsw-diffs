## StoreKit

> `/System/Library/Frameworks/StoreKit.framework/StoreKit`

```diff

-813.0.63.2.2
-  __TEXT.__text: 0x13b7cc
-  __TEXT.__auth_stubs: 0x2f40
-  __TEXT.__objc_methlist: 0x4614
-  __TEXT.__gcc_except_tab: 0xf0c
-  __TEXT.__const: 0x7fc0
-  __TEXT.__cstring: 0x60fa
-  __TEXT.__oslogstring: 0x2282
+813.1.7.0.0
+  __TEXT.__text: 0x144c20
+  __TEXT.__auth_stubs: 0x3000
+  __TEXT.__objc_methlist: 0x4734
+  __TEXT.__gcc_except_tab: 0xf1c
+  __TEXT.__const: 0x8330
+  __TEXT.__cstring: 0x644a
+  __TEXT.__oslogstring: 0x22ee
   __TEXT.__dlopen_cstrs: 0x3dd
-  __TEXT.__constg_swiftt: 0x25d0
-  __TEXT.__swift5_typeref: 0x2bdf
+  __TEXT.__constg_swiftt: 0x2678
+  __TEXT.__swift5_typeref: 0x2d7c
   __TEXT.__swift5_builtin: 0x1f4
-  __TEXT.__swift5_reflstr: 0x1b7c
-  __TEXT.__swift5_fieldmd: 0x26cc
-  __TEXT.__swift5_capture: 0xabc
-  __TEXT.__swift5_assocty: 0xa58
-  __TEXT.__swift5_proto: 0x79c
-  __TEXT.__swift5_types: 0x35c
+  __TEXT.__swift5_reflstr: 0x1bac
+  __TEXT.__swift5_fieldmd: 0x27dc
+  __TEXT.__swift5_capture: 0xb70
+  __TEXT.__swift5_assocty: 0xa70
+  __TEXT.__swift5_proto: 0x7d8
+  __TEXT.__swift5_types: 0x370
   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__unwind_info: 0x606c
-  __TEXT.__eh_frame: 0x7278
-  __TEXT.__objc_classname: 0x11e8
-  __TEXT.__objc_methname: 0xc6c6
-  __TEXT.__objc_methtype: 0x2bcd
-  __TEXT.__objc_stubs: 0x8220
+  __TEXT.__unwind_info: 0x6804
+  __TEXT.__eh_frame: 0x7748
+  __TEXT.__objc_classname: 0x122a
+  __TEXT.__objc_methname: 0xc9c4
+  __TEXT.__objc_methtype: 0x2b66
+  __TEXT.__objc_stubs: 0x8340
   __DATA_CONST.__got: 0x798
-  __DATA_CONST.__const: 0x19a0
-  __DATA_CONST.__objc_classlist: 0x3c0
+  __DATA_CONST.__const: 0x1900
+  __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x248
+  __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x130f0
-  __DATA_CONST.__objc_selrefs: 0x2c68
+  __DATA_CONST.__objc_const: 0x132b0
+  __DATA_CONST.__objc_selrefs: 0x2cf0
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__const: 0x7d60
-  __AUTH_CONST.__objc_const: 0x2708
-  __AUTH_CONST.__cfstring: 0x3660
+  __AUTH_CONST.__const: 0x8270
+  __AUTH_CONST.__objc_const: 0x2828
+  __AUTH_CONST.__cfstring: 0x3700
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_ptr: 0x150
-  __AUTH_CONST.__auth_got: 0x17b0
-  __AUTH.__objc_data: 0x2418
-  __AUTH.__data: 0x2458
+  __AUTH_CONST.__auth_ptr: 0x160
+  __AUTH_CONST.__auth_got: 0x1810
+  __AUTH.__objc_data: 0x24b8
+  __AUTH.__data: 0x24e0
   __DATA.__objc_protorefs: 0x118
-  __DATA.__objc_classrefs: 0x568
-  __DATA.__objc_superrefs: 0x230
-  __DATA.__objc_ivar: 0x5c4
-  __DATA.__data: 0x7dd8
-  __DATA.__bss: 0xae50
+  __DATA.__objc_classrefs: 0x570
+  __DATA.__objc_superrefs: 0x238
+  __DATA.__objc_ivar: 0x5d8
+  __DATA.__data: 0x7fd8
+  __DATA.__bss: 0xb620
   __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__bss: 0x38

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9885
-  Symbols:   13133
-  CStrings:  3575
+  Functions: 10132
+  Symbols:   13362
+  CStrings:  3635
 
Symbols:
+ +[SKPPMUtilities PPMConfirmedValueWithValue:newValue:]
+ +[SKPPMUtilities PPMScaledValueUsingValue:]
+ +[SKProductLookupResponse supportsSecureCoding]
+ +[SKProductRemoteViewTask _unavailableErrorWithUserInfo:]
+ +[SKProductRemoteViewTask _unknownErrorWithUserInfo:]
+ -[SKProductLookupResponse .cxx_destruct]
+ -[SKProductLookupResponse encodeWithCoder:]
+ -[SKProductLookupResponse encodeWithCoder:].cold.1
+ -[SKProductLookupResponse encodeWithCoder:].cold.2
+ -[SKProductLookupResponse extensionBundleID]
+ -[SKProductLookupResponse initWithCoder:]
+ -[SKProductLookupResponse initWithCoder:].cold.1
+ -[SKProductLookupResponse initWithCoder:].cold.2
+ -[SKProductLookupResponse initWithResult:extensionID:productURL:isEntitled:parameters:]
+ -[SKProductLookupResponse isEntitled]
+ -[SKProductLookupResponse parameters]
+ -[SKProductLookupResponse productURL]
+ -[SKProductLookupResponse resultDictionary]
+ -[SKProductRemoteViewTask storeProductViewControllerWillDisappear]
+ -[SKProductRemoteViewTask storeProductViewControllerWillDismiss]
+ -[SKServiceBroker productLookupServiceWithErrorHandler:]
+ -[ServiceCardContainerViewController dealloc]
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table52
+ GCC_except_table56
+ GCC_except_table58
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table70
+ GCC_except_table76
+ GCC_except_table78
+ _OBJC_CLASS_$_SKPPMUtilities
+ _OBJC_CLASS_$_SKProductLookupResponse
+ _OBJC_IVAR_$_SKProductLookupResponse._extensionBundleID
+ _OBJC_IVAR_$_SKProductLookupResponse._isEntitled
+ _OBJC_IVAR_$_SKProductLookupResponse._parameters
+ _OBJC_IVAR_$_SKProductLookupResponse._productURL
+ _OBJC_IVAR_$_SKProductLookupResponse._resultDictionary
+ _OBJC_METACLASS_$_SKPPMUtilities
+ _OBJC_METACLASS_$_SKProductLookupResponse
+ __OBJC_$_CLASS_METHODS_SKPPMUtilities
+ __OBJC_$_CLASS_METHODS_SKProductLookupResponse
+ __OBJC_$_CLASS_METHODS_SKProductRemoteViewTask(Internal)
+ __OBJC_$_CLASS_PROP_LIST_SKProductLookupResponse
+ __OBJC_$_INSTANCE_METHODS_SKProductLookupResponse
+ __OBJC_$_INSTANCE_METHODS_SKProductRemoteViewTask(Internal)
+ __OBJC_$_INSTANCE_VARIABLES_SKProductLookupResponse
+ __OBJC_$_PROP_LIST_SKProductLookupResponse
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ProductPageLookupService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ProductPageLookupService
+ __OBJC_CLASS_PROTOCOLS_$_SKProductLookupResponse
+ __OBJC_CLASS_RO_$_SKPPMUtilities
+ __OBJC_CLASS_RO_$_SKProductLookupResponse
+ __OBJC_LABEL_PROTOCOL_$_ProductPageLookupService
+ __OBJC_METACLASS_RO_$_SKPPMUtilities
+ __OBJC_METACLASS_RO_$_SKProductLookupResponse
+ __OBJC_PROTOCOL_$_ProductPageLookupService
+ ___48-[SKProductRemoteViewTask _showExtensionWithID:]_block_invoke.40
+ ___56-[SKServiceBroker productLookupServiceWithErrorHandler:]_block_invoke
+ ___64-[SKProductRemoteViewTask storeProductViewControllerWillDismiss]_block_invoke
+ ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.35
+ ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.35.cold.1
+ ___block_descriptor_40_e8_32w_e48_v16?0"<SKUIServiceProductPageViewController>"8lw32l8
+ ___block_descriptor_48_e8_32bs40w_e45_v24?0"SKProductLookupResponse"8"NSError"16lw40l8s32l8
+ ___block_descriptor_72_e8_32s40s48s56s64w_e48_v16?0"<SKUIServiceProductPageViewController>"8lw64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.37
+ ___block_literal_global.46
+ ___block_literal_global.50
+ ___block_literal_global.52
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ _associated conformance 15StoreKit_Shared24ProductPageLookupRequestV09ParameterG0V10CodingKeys33_C6991225FB7E4EC38FC5B568EF39ADB4LLOSHAASQ
+ _associated conformance 15StoreKit_Shared24ProductPageLookupRequestV09ParameterG0V10CodingKeys33_C6991225FB7E4EC38FC5B568EF39ADB4LLOs0I3KeyAAs23CustomStringConvertible
+ _associated conformance 15StoreKit_Shared24ProductPageLookupRequestV09ParameterG0V10CodingKeys33_C6991225FB7E4EC38FC5B568EF39ADB4LLOs0I3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15StoreKit_Shared24ProductPageLookupRequestV10URLRequestV10CodingKeys33_C6991225FB7E4EC38FC5B568EF39ADB4LLOSHAASQ
+ _associated conformance 15StoreKit_Shared24ProductPageLookupRequestV10URLRequestV10CodingKeys33_C6991225FB7E4EC38FC5B568EF39ADB4LLOs0I3KeyAAs23CustomStringConvertible
+ _associated conformance 15StoreKit_Shared24ProductPageLookupRequestV10URLRequestV10CodingKeys33_C6991225FB7E4EC38FC5B568EF39ADB4LLOs0I3KeyAAs28CustomDebugStringConvertible
+ _block_copy_helper.108
+ _block_copy_helper.114
+ _block_copy_helper.58
+ _block_descriptor.110
+ _block_descriptor.116
+ _block_descriptor.60
+ _block_destroy_helper.109
+ _block_destroy_helper.115
+ _block_destroy_helper.59
+ _objc_msgSend$extensionBundleID
+ _objc_msgSend$isEntitled
+ _objc_msgSend$parameters
+ _objc_msgSend$performLookupWithIdentifier:parameters:logKey:keyProfile:completionHandler:
+ _objc_msgSend$performLookupWithURL:logKey:keyProfile:completionHandler:
+ _objc_msgSend$resultDictionary
+ _objc_msgSend$setTintColor:
+ _objc_msgSend$storeProductViewControllerWillDisappear
+ _objc_msgSend$storeProductViewControllerWillDismiss
+ _objc_msgSend$systemBlueColor
+ _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
+ _objectdestroy.16Tm
+ _objectdestroy.17Tm
+ _objectdestroy.23Tm
+ _symbolic ScCySo23SKProductLookupResponseC______pG s5ErrorP
+ _symbolic So12NSDictionaryCSg
+ _symbolic So23SKProductLookupResponseCSgSo7NSErrorCSgIeyByy_
+ _symbolic So23SKProductRemoteViewTaskC
+ _symbolic So23SKProductRemoteViewTaskCXDXMT
+ _symbolic So5NSURLCSg
+ _symbolic So8NSStringCSg
+ _symbolic _____ 10Foundation3URLV
+ _symbolic _____ 15StoreKit_Shared24ProductPageLookupRequestV
+ _symbolic _____ 15StoreKit_Shared24ProductPageLookupRequestV09ParameterG0V
+ _symbolic _____ 15StoreKit_Shared24ProductPageLookupRequestV09ParameterG0V10CodingKeys33_C6991225FB7E4EC38FC5B568EF39ADB4LLO
+ _symbolic _____ 15StoreKit_Shared24ProductPageLookupRequestV10URLRequestV
+ _symbolic _____ 15StoreKit_Shared24ProductPageLookupRequestV10URLRequestV10CodingKeys33_C6991225FB7E4EC38FC5B568EF39ADB4LLO
+ _symbolic _____Sg 10Foundation12URLQueryItemV
+ _symbolic _____Sg 10Foundation13URLComponentsV
+ _symbolic ______ypt s11AnyHashableV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared24ProductPageLookupRequestV09ParameterJ0V10CodingKeys33_C6991225FB7E4EC38FC5B568EF39ADB4LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15StoreKit_Shared24ProductPageLookupRequestV10URLRequestV10CodingKeys33_C6991225FB7E4EC38FC5B568EF39ADB4LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared24ProductPageLookupRequestV09ParameterJ0V10CodingKeys33_C6991225FB7E4EC38FC5B568EF39ADB4LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15StoreKit_Shared24ProductPageLookupRequestV10URLRequestV10CodingKeys33_C6991225FB7E4EC38FC5B568EF39ADB4LLO
+ _symbolic _____y_____ypG s18_DictionaryStorageC s11AnyHashableV
- GCC_except_table50
- GCC_except_table53
- GCC_except_table55
- GCC_except_table61
- GCC_except_table65
- GCC_except_table67
- GCC_except_table71
- GCC_except_table75
- GCC_except_table77
- __OBJC_$_INSTANCE_METHODS_SKProductRemoteViewTask
- ___48-[SKProductRemoteViewTask _showExtensionWithID:]_block_invoke.36
- ___62-[SKProductRemoteViewTask loadProductWithURL:completionBlock:]_block_invoke.44
- ___62-[SKProductRemoteViewTask loadProductWithURL:completionBlock:]_block_invoke.44.cold.1
- ___62-[SKProductRemoteViewTask loadProductWithURL:completionBlock:]_block_invoke.44.cold.2
- ___66-[SKProductRemoteViewTask lookupProductWithParameters:completion:]_block_invoke.22
- ___66-[SKProductRemoteViewTask lookupProductWithParameters:completion:]_block_invoke.22.cold.1
- ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.31
- ___67-[SKProductRemoteViewTask _loadUIServiceIfNecessaryWithCompletion:]_block_invoke.31.cold.1
- ___block_descriptor_40_e8_32s_e48_v16?0"<SKUIServiceProductPageViewController>"8ls32l8
- ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
- ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40bs48w_e67_v44?0"NSDictionary"8"NSError"16B24"NSString"28"NSDictionary"36lw48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e50_v36?0"NSDictionary"8"NSError"16B24"NSString"28ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e48_v16?0"<SKUIServiceProductPageViewController>"8ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.41
- ___block_literal_global.48
- _block_copy_helper.118
- _block_copy_helper.124
- _block_descriptor.120
- _block_descriptor.126
- _block_destroy_helper.119
- _block_destroy_helper.125
- _objc_msgSend$lookupProductWithID:keyProfile:logKey:parameters:reply:
- _objc_msgSend$lookupProductWithURLIfEntitled:keyProfile:logKey:reply:
- _objectdestroy.26Tm
- _objectdestroy.43Tm
CStrings:
+ "\x14"
+ "%{public}@: Dealloc."
+ "%{public}@: Start."
+ "@52@0:8@16@24@32B40@44"
+ "Could not cast param dictionary to Dictionary<AnyHashable, Any>"
+ "Did dismiss."
+ "Failed encode product lookup request: "
+ "Failed in XPC to perform product lookup: "
+ "Failed to decode lookup result: %{public}@."
+ "Failed to decode parameters: %{public}@."
+ "Failed to encode lookup result: %{public}@."
+ "Failed to encode parameters: %{public}@."
+ "Failed to get XPC remote object to perform product lookup"
+ "Failed to perform product lookup: "
+ "Lookup completed without a response or an error"
+ "Malformed URL for product lookup: "
+ "Missing URL for product lookup"
+ "Missing identifier for product lookup"
+ "Missing parameters for product lookup"
+ "PPMConfirmedValueWithValue:newValue:"
+ "PPMScaledValueUsingValue:"
+ "Product task deallocated."
+ "ProductPageLookupService"
+ "Remote controller dismissed."
+ "SKPPMUtilities"
+ "SKProductLookupResponse"
+ "T@\"NSDictionary\",R,N,V_parameters"
+ "T@\"NSDictionary\",R,N,V_resultDictionary"
+ "T@\"NSString\",R,N,V_extensionBundleID"
+ "T@\"NSURL\",R,N,V_productURL"
+ "TB,R,N,V_isEntitled"
+ "[%{public}@][%{public}@]: Disappearing."
+ "[%{public}@][%{public}@]: Finishing."
+ "[%{public}@][%{public}@]: Will dismiss."
+ "_extensionBundleID"
+ "_isEntitled"
+ "_resultDictionary"
+ "_unavailableErrorWithUserInfo:"
+ "_unknownErrorWithUserInfo:"
+ "d24@0:8d16"
+ "d32@0:8d16d24"
+ "extensionBundleID"
+ "initWithResult:extensionID:productURL:isEntitled:parameters:"
+ "isEntitled"
+ "keyProfile"
+ "lookupProductWithParametersProductRequest:reply:"
+ "lookupProductWithURLProductRequest:reply:"
+ "parameters"
+ "params"
+ "performLookup(with:logKey:keyProfile:)"
+ "performLookup(withIdentifier:parameters:logKey:keyProfile:)"
+ "performLookupWithIdentifier:parameters:logKey:keyProfile:completionHandler:"
+ "performLookupWithURL:logKey:keyProfile:completionHandler:"
+ "productID"
+ "productLookupServiceWithErrorHandler:"
+ "resultDictionary"
+ "setADPState:"
+ "setTintColor:"
+ "storeProductViewControllerWillDisappear"
+ "storeProductViewControllerWillDismiss"
+ "systemBlueColor"
+ "unarchivedObjectOfClasses:fromData:error:"
+ "v24@?0@\"SKProductLookupResponse\"8@\"NSError\"16"
+ "v32@0:8@\"NSData\"16@?<v@?@\"SKProductLookupResponse\"@\"NSError\">24"
+ "v48@0:8@\"NSURL\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"SKProductLookupResponse\"@\"NSError\">40"
+ "v56@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"SKProductLookupResponse\"@\"NSError\">48"
- "[%{public}@]: Error in remote proxy for product lookup: %{public}@"
- "[%{public}@]: Unable to perform lookup."
- "[%{public}@][%{public}@]: Dismiss."
- "[%{public}@][%{public}@]: Error in remote proxy for product lookup: %{public}@"
- "[%{public}@][%{public}@]: Lookup completed with error: %{public}@"
- "lookupProductWithID:keyProfile:logKey:parameters:reply:"
- "lookupProductWithURLIfEntitled:keyProfile:logKey:reply:"
- "v36@?0@\"NSDictionary\"8@\"NSError\"16B24@\"NSString\"28"
- "v44@?0@\"NSDictionary\"8@\"NSError\"16B24@\"NSString\"28@\"NSDictionary\"36"
- "v48@0:8@\"NSURL\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSDictionary\"@\"NSError\"B@\"NSString\"@\"NSDictionary\">40"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSDictionary\"40@?<v@?@\"NSDictionary\"@\"NSError\"B@\"NSString\">48"

```
