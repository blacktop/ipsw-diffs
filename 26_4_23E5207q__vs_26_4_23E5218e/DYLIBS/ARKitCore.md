## ARKitCore

> `/System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore`

```diff

-738.100.1.0.0
-  __TEXT.__text: 0x1a6acc
-  __TEXT.__auth_stubs: 0x3c70
-  __TEXT.__objc_methlist: 0x11124
-  __TEXT.__const: 0x2c118
-  __TEXT.__gcc_except_tab: 0x13e04
-  __TEXT.__oslogstring: 0x1e6c5
-  __TEXT.__cstring: 0x1f109
+738.100.2.0.0
+  __TEXT.__text: 0x1a5908
+  __TEXT.__auth_stubs: 0x3c50
+  __TEXT.__objc_methlist: 0x10f7c
+  __TEXT.__const: 0x2c108
+  __TEXT.__gcc_except_tab: 0x13de8
+  __TEXT.__oslogstring: 0x1e643
+  __TEXT.__cstring: 0x1f090
   __TEXT.__ustring: 0xe6
-  __TEXT.__unwind_info: 0x6c48
-  __TEXT.__objc_classname: 0x2029
-  __TEXT.__objc_methname: 0x2a4e3
-  __TEXT.__objc_methtype: 0xa722
-  __TEXT.__objc_stubs: 0x1ac80
-  __DATA_CONST.__got: 0x1680
-  __DATA_CONST.__const: 0x3658
-  __DATA_CONST.__objc_classlist: 0x860
+  __TEXT.__unwind_info: 0x6bf8
+  __TEXT.__objc_classname: 0x1fd6
+  __TEXT.__objc_methname: 0x2a129
+  __TEXT.__objc_methtype: 0xa6c5
+  __TEXT.__objc_stubs: 0x1a9c0
+  __DATA_CONST.__got: 0x1658
+  __DATA_CONST.__const: 0x3608
+  __DATA_CONST.__objc_classlist: 0x848
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x250
+  __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7da8
+  __DATA_CONST.__objc_selrefs: 0x7cc0
   __DATA_CONST.__objc_protorefs: 0x90
-  __DATA_CONST.__objc_superrefs: 0x790
-  __DATA_CONST.__objc_arraydata: 0x880
-  __AUTH_CONST.__auth_got: 0x1e50
+  __DATA_CONST.__objc_superrefs: 0x778
+  __DATA_CONST.__objc_arraydata: 0x870
+  __AUTH_CONST.__auth_got: 0x1e40
   __AUTH_CONST.__const: 0x3cb8
-  __AUTH_CONST.__cfstring: 0x104a0
-  __AUTH_CONST.__objc_const: 0x3cef0
+  __AUTH_CONST.__cfstring: 0x10420
+  __AUTH_CONST.__objc_const: 0x3cb48
+  __AUTH_CONST.__objc_arrayobj: 0x5d0
   __AUTH_CONST.__objc_intobj: 0x3240
-  __AUTH_CONST.__objc_arrayobj: 0x600
   __AUTH_CONST.__objc_doubleobj: 0x380
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x3660
+  __AUTH.__objc_data: 0x3570
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x200c
-  __DATA.__data: 0x1ca0
+  __DATA.__objc_ivar: 0x1fe8
+  __DATA.__data: 0x1c40
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x1dd8
   __DATA.__common: 0x8

   - /usr/lib/libchannel.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
-  UUID: 70423E03-4FE9-3C47-BF46-3F83C5F66B3E
-  Functions: 7908
-  Symbols:   30361
-  CStrings:  14451
+  UUID: 4F874228-CCEC-3CCD-A7F4-4229F6C2BA0F
+  Functions: 7879
+  Symbols:   30229
+  CStrings:  14393
 
Symbols:
+ GCC_except_table72
+ _ARFillPlanar8PixelBuffer
+ _ARFillPlanarFloat32PixelBuffer
+ _ARFillRectInPlanar8PixelBuffer
+ _ARFillRectInPlanar8VImageBuffer
+ _ARFillRectInPlanarFloat32PixelBuffer
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSDictionary_$_ARAdditions
+ __OBJC_$_CATEGORY_NSDictionary_$_ARAdditions
+ __OBJC_$_INSTANCE_METHODS_NSDictionary(ARAdditions|ARPersonDetectionData)
+ ___block_literal_global.108
+ ___block_literal_global.111
+ _vImageOverwriteChannelsWithScalar_PlanarF
- +[gan_model_pre_A11 URLOfModelInThisBundle]
- +[gan_model_pre_A11 URLOfModelInThisBundle].cold.1
- +[gan_model_pre_A11 loadContentsOfURL:configuration:completionHandler:]
- +[gan_model_pre_A11 loadWithConfiguration:completionHandler:]
- -[ARCubemapCompletion srgbToLog:]
- -[gan_model_pre_A11 .cxx_destruct]
- -[gan_model_pre_A11 initWithConfiguration:error:]
- -[gan_model_pre_A11 initWithContentsOfURL:configuration:error:]
- -[gan_model_pre_A11 initWithContentsOfURL:error:]
- -[gan_model_pre_A11 initWithMLModel:]
- -[gan_model_pre_A11 init]
- -[gan_model_pre_A11 model]
- -[gan_model_pre_A11 predictionFromFeatures:completionHandler:]
- -[gan_model_pre_A11 predictionFromFeatures:error:]
- -[gan_model_pre_A11 predictionFromFeatures:options:completionHandler:]
- -[gan_model_pre_A11 predictionFromFeatures:options:error:]
- -[gan_model_pre_A11 predictionFromInput:error:]
- -[gan_model_pre_A11 predictionsFromInputs:options:error:]
- -[gan_model_pre_A11Input .cxx_destruct]
- -[gan_model_pre_A11Input featureNames]
- -[gan_model_pre_A11Input featureValueForName:]
- -[gan_model_pre_A11Input initWithInput:]
- -[gan_model_pre_A11Input input]
- -[gan_model_pre_A11Input setInput:]
- -[gan_model_pre_A11Output .cxx_destruct]
- -[gan_model_pre_A11Output featureNames]
- -[gan_model_pre_A11Output featureValueForName:]
- -[gan_model_pre_A11Output initWithOutput:]
- -[gan_model_pre_A11Output output]
- -[gan_model_pre_A11Output setOutput:]
- _OBJC_CLASS_$_MLArrayBatchProvider
- _OBJC_CLASS_$_MLFeatureValue
- _OBJC_CLASS_$_MLModel
- _OBJC_CLASS_$_MLPredictionOptions
- _OBJC_CLASS_$_gan_model_pre_A11
- _OBJC_CLASS_$_gan_model_pre_A11Input
- _OBJC_CLASS_$_gan_model_pre_A11Output
- _OBJC_IVAR_$_ARCubemapCompletion._b_bias_pre_A11
- _OBJC_IVAR_$_ARCubemapCompletion._bias_height_pre_A11
- _OBJC_IVAR_$_ARCubemapCompletion._g_bias_pre_A11
- _OBJC_IVAR_$_ARCubemapCompletion._r_bias_pre_A11
- _OBJC_IVAR_$_ARCubemapCompletion._srgbToLogLUT_pre_A11
- _OBJC_IVAR_$_ARCubemapCompletion._use_model_pre_A11
- _OBJC_IVAR_$_gan_model_pre_A11._model
- _OBJC_IVAR_$_gan_model_pre_A11Input._input
- _OBJC_IVAR_$_gan_model_pre_A11Output._output
- _OBJC_METACLASS_$_gan_model_pre_A11
- _OBJC_METACLASS_$_gan_model_pre_A11Input
- _OBJC_METACLASS_$_gan_model_pre_A11Output
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDictionary_$_ARPersonDetectionData
- __OBJC_$_CATEGORY_NSDictionary_$_ARPersonDetectionData
- __OBJC_$_CLASS_METHODS_NSDictionary(ARPersonDetectionData|ARAdditions)
- __OBJC_$_CLASS_METHODS_gan_model_pre_A11
- __OBJC_$_INSTANCE_METHODS_gan_model_pre_A11
- __OBJC_$_INSTANCE_METHODS_gan_model_pre_A11Input
- __OBJC_$_INSTANCE_METHODS_gan_model_pre_A11Output
- __OBJC_$_INSTANCE_VARIABLES_gan_model_pre_A11
- __OBJC_$_INSTANCE_VARIABLES_gan_model_pre_A11Input
- __OBJC_$_INSTANCE_VARIABLES_gan_model_pre_A11Output
- __OBJC_$_PROP_LIST_MLFeatureProvider
- __OBJC_$_PROP_LIST_gan_model_pre_A11
- __OBJC_$_PROP_LIST_gan_model_pre_A11Input
- __OBJC_$_PROP_LIST_gan_model_pre_A11Output
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MLFeatureProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_MLFeatureProvider
- __OBJC_CLASS_PROTOCOLS_$_gan_model_pre_A11Input
- __OBJC_CLASS_PROTOCOLS_$_gan_model_pre_A11Output
- __OBJC_CLASS_RO_$_gan_model_pre_A11
- __OBJC_CLASS_RO_$_gan_model_pre_A11Input
- __OBJC_CLASS_RO_$_gan_model_pre_A11Output
- __OBJC_LABEL_PROTOCOL_$_MLFeatureProvider
- __OBJC_METACLASS_RO_$_gan_model_pre_A11
- __OBJC_METACLASS_RO_$_gan_model_pre_A11Input
- __OBJC_METACLASS_RO_$_gan_model_pre_A11Output
- __OBJC_PROTOCOL_$_MLFeatureProvider
- __ZNSt3__16vectorIhNS_9allocatorIhEEE9push_backB9foe210106EOh
- ___62-[gan_model_pre_A11 predictionFromFeatures:completionHandler:]_block_invoke
- ___70-[gan_model_pre_A11 predictionFromFeatures:options:completionHandler:]_block_invoke
- ___71+[gan_model_pre_A11 loadContentsOfURL:configuration:completionHandler:]_block_invoke
- ___block_descriptor_40_e8_32bs_e29_v24?0"MLModel"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e41_v24?0"<MLFeatureProvider>"8"NSError"16ls32l8
- ___exp10
- __os_log_default
- __os_log_error_impl
- _log10
- _objc_msgSend$URLOfModelInThisBundle
- _objc_msgSend$bundleForClass:
- _objc_msgSend$featureValueForName:
- _objc_msgSend$featureValueWithMultiArray:
- _objc_msgSend$featuresAtIndex:
- _objc_msgSend$initWithContentsOfURL:configuration:error:
- _objc_msgSend$initWithFeatureProviderArray:
- _objc_msgSend$initWithInput:
- _objc_msgSend$initWithMLModel:
- _objc_msgSend$initWithOutput:
- _objc_msgSend$input
- _objc_msgSend$loadContentsOfURL:configuration:completionHandler:
- _objc_msgSend$model
- _objc_msgSend$modelWithContentsOfURL:configuration:error:
- _objc_msgSend$modelWithContentsOfURL:error:
- _objc_msgSend$multiArrayValue
- _objc_msgSend$predictionFromFeatures:completionHandler:
- _objc_msgSend$predictionFromFeatures:error:
- _objc_msgSend$predictionFromFeatures:options:completionHandler:
- _objc_msgSend$predictionFromFeatures:options:error:
- _objc_msgSend$predictionsFromBatch:options:error:
- _objc_msgSend$srgbToLog:
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CI7hugCIU1qvdztdhDqoFgkqSQy_FE8XHfmC49I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7hugCIU1qvdztdhDqoFgkqSQy_FE8XHfmC49I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7hugCIU1qvdztdhDqoFgkqSQy_FE8XHfmC49I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7hugCIU1qvdztdhDqoFgkqSQy_FE8XHfmC49I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7hugCIU1qvdztdhDqoFgkqSQy_FE8XHfmC49I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7hugCIU1qvdztdhDqoFgkqSQy_FE8XHfmC49I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7hugCIU1qvdztdhDqoFgkqSQy_FE8XHfmC49I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7hugCIU1qvdztdhDqoFgkqSQy_FE8XHfmC49I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7hugCIU1qvdztdhDqoFgkqSQy_FE8XHfmC49I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7hugCIU1qvdztdhDqoFgkqSQy_FE8XHfmC49I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7hugCIU1qvdztdhDqoFgkqSQy_FE8XHfmC49I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7hugCIU1qvdztdhDqoFgkqSQy_FE8XHfmC49I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:286: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7hugCIU1qvdztdhDqoFgkqSQy_FE8XHfmC49I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7hugCIU1qvdztdhDqoFgkqSQy_FE8XHfmC49I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7hugCIU1qvdztdhDqoFgkqSQy_FE8XHfmC49I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7hugCIU1qvdztdhDqoFgkqSQy_FE8XHfmC49I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7hugCIU1qvdztdhDqoFgkqSQy_FE8XHfmC49I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7hugCIU1qvdztdhDqoFgkqSQy_FE8XHfmC49I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CI7hugCIU1qvdztdhDqoFgkqSQy_FE8XHfmC49I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "%{public}@ <%p>: Completion model espresso plan at low priority."
- "/AppleInternal/Library/BuildRoots/4~CHo4ugDvgeprNjVVUO2IZCs1PPQFN_daZgv8Efo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CHo4ugDvgeprNjVVUO2IZCs1PPQFN_daZgv8Efo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CHo4ugDvgeprNjVVUO2IZCs1PPQFN_daZgv8Efo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CHo4ugDvgeprNjVVUO2IZCs1PPQFN_daZgv8Efo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CHo4ugDvgeprNjVVUO2IZCs1PPQFN_daZgv8Efo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CHo4ugDvgeprNjVVUO2IZCs1PPQFN_daZgv8Efo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CHo4ugDvgeprNjVVUO2IZCs1PPQFN_daZgv8Efo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CHo4ugDvgeprNjVVUO2IZCs1PPQFN_daZgv8Efo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CHo4ugDvgeprNjVVUO2IZCs1PPQFN_daZgv8Efo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CHo4ugDvgeprNjVVUO2IZCs1PPQFN_daZgv8Efo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CHo4ugDvgeprNjVVUO2IZCs1PPQFN_daZgv8Efo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CHo4ugDvgeprNjVVUO2IZCs1PPQFN_daZgv8Efo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:286: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CHo4ugDvgeprNjVVUO2IZCs1PPQFN_daZgv8Efo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CHo4ugDvgeprNjVVUO2IZCs1PPQFN_daZgv8Efo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CHo4ugDvgeprNjVVUO2IZCs1PPQFN_daZgv8Efo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CHo4ugDvgeprNjVVUO2IZCs1PPQFN_daZgv8Efo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CHo4ugDvgeprNjVVUO2IZCs1PPQFN_daZgv8Efo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CHo4ugDvgeprNjVVUO2IZCs1PPQFN_daZgv8Efo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CHo4ugDvgeprNjVVUO2IZCs1PPQFN_daZgv8Efo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "@\"MLFeatureValue\"24@0:8@\"NSString\"16"
- "@\"MLModel\""
- "@\"MLMultiArray\""
- "C20@0:8C16"
- "Could not load gan_model_pre_A11.mlmodelc in the bundle resource"
- "MLFeatureProvider"
- "T@\"MLModel\",R,N,V_model"
- "T@\"MLMultiArray\",&,N,V_input"
- "T@\"MLMultiArray\",&,N,V_output"
- "URLOfModelInThisBundle"
- "_b_bias_pre_A11"
- "_bias_height_pre_A11"
- "_g_bias_pre_A11"
- "_model"
- "_r_bias_pre_A11"
- "_srgbToLogLUT_pre_A11"
- "_use_model_pre_A11"
- "bundleForClass:"
- "combine_buffers_to_hdr_pre_A11"
- "featureNames"
- "featureValueForName:"
- "featureValueWithMultiArray:"
- "featuresAtIndex:"
- "gan_model_pre_A11"
- "gan_model_pre_A11Input"
- "gan_model_pre_A11Output"
- "initWithConfiguration:error:"
- "initWithContentsOfURL:configuration:error:"
- "initWithFeatureProviderArray:"
- "initWithInput:"
- "initWithMLModel:"
- "initWithOutput:"
- "loadContentsOfURL:configuration:completionHandler:"
- "loadWithConfiguration:completionHandler:"
- "model"
- "modelWithContentsOfURL:configuration:error:"
- "modelWithContentsOfURL:error:"
- "multiArrayValue"
- "predictionFromFeatures:completionHandler:"
- "predictionFromFeatures:error:"
- "predictionFromFeatures:options:completionHandler:"
- "predictionFromFeatures:options:error:"
- "predictionFromInput:error:"
- "predictionsFromBatch:options:error:"
- "predictionsFromInputs:options:error:"
- "setInput:"
- "setOutput:"
- "srgbToLog:"
- "v24@?0@\"<MLFeatureProvider>\"8@\"NSError\"16"
- "v24@?0@\"MLModel\"8@\"NSError\"16"
- "v40@0:8@16@24@?32"

```
