## AppleNeuralEngine

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`

```diff

-380.200.3.0.0
-  __TEXT.__text: 0x44a1c
-  __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_methlist: 0x260c
-  __TEXT.__const: 0x288
-  __TEXT.__oslogstring: 0x80f8
-  __TEXT.__cstring: 0x2da1
-  __TEXT.__gcc_except_tab: 0x5290
-  __TEXT.__unwind_info: 0x1110
+380.502.0.0.0
+  __TEXT.__text: 0x45bd8
+  __TEXT.__auth_stubs: 0xb70
+  __TEXT.__objc_methlist: 0x263c
+  __TEXT.__const: 0x280
+  __TEXT.__oslogstring: 0x81e6
+  __TEXT.__cstring: 0x2e21
+  __TEXT.__gcc_except_tab: 0x51a8
+  __TEXT.__unwind_info: 0x1208
   __TEXT.__objc_classname: 0x2ef
-  __TEXT.__objc_methname: 0x5f8a
-  __TEXT.__objc_methtype: 0x24a8
-  __TEXT.__objc_stubs: 0x4420
+  __TEXT.__objc_methname: 0x5fce
+  __TEXT.__objc_methtype: 0x24ac
+  __TEXT.__objc_stubs: 0x4440
   __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0x658
+  __DATA_CONST.__const: 0x6a8
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1650
+  __DATA_CONST.__objc_selrefs: 0x1668
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x118
-  __AUTH_CONST.__auth_got: 0x600
+  __AUTH_CONST.__auth_got: 0x5d0
   __AUTH_CONST.__const: 0x490
-  __AUTH_CONST.__cfstring: 0x3740
+  __AUTH_CONST.__cfstring: 0x3a60
   __AUTH_CONST.__objc_const: 0x3658
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30

   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x200
   __DATA.__data: 0x3c0
-  __DATA.__bss: 0x158
+  __DATA.__bss: 0x160
   __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0xf8

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: 9366647A-38D7-3090-80E8-6ECAAB0B5F97
-  Functions: 1412
-  Symbols:   4630
-  CStrings:  2647
+  UUID: A7FDBA01-DD31-3CB4-8DC5-3B47D321A918
+  Functions: 1426
+  Symbols:   4706
+  CStrings:  2704
 
Symbols:
+ +[_ANEDataReporter reportTelemetryToCoreAnalytics:payload:]
+ +[_ANEDeviceInfo aneSubTypeAndVariant]
+ +[_ANEDeviceInfo aneSubTypeAndVariant].cold.1
+ +[_ANEDeviceInfo aneSubTypeAndVariant].cold.2
+ +[_ANEStrings mlirExtension]
+ -[_ANEVirtualClient aneSubTypeAndVariant]
+ GCC_except_table104
+ GCC_except_table107
+ GCC_except_table111
+ GCC_except_table39
+ GCC_except_table42
+ GCC_except_table58
+ GCC_except_table61
+ GCC_except_table70
+ GCC_except_table88
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ __ZNKSt9type_infoeqB9foe210106ERKS_
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9foe210106ILi0EEEPKc
+ __ZNSt3__119__shared_weak_count16__release_sharedB9foe210106Ev
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZZ38+[_ANEDeviceInfo aneSubTypeAndVariant]E10aneArchStr
+ ___38+[_ANEDeviceInfo aneSubTypeAndVariant]_block_invoke
+ ___38+[_ANEDeviceInfo aneSubTypeAndVariant]_block_invoke.cold.1
+ ___42+[_ANEDeviceInfo aneSubTypeProductVariant]_block_invoke.140
+ ___59+[_ANEDataReporter reportTelemetryToCoreAnalytics:payload:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
+ ___block_descriptor_48_ea8_32s_e8_v16?0q8ls32l8
+ ___block_literal_global.139
+ ___block_literal_global.142
+ ___block_literal_global.147
+ ___block_literal_global.231
+ ___block_literal_global.236
+ ___block_literal_global.247
+ ___block_literal_global.261
+ ___block_literal_global.266
+ _objc_msgSend$aneSubTypeAndVariant
+ _objc_msgSend$stringWithString:
- GCC_except_table105
- GCC_except_table110
- GCC_except_table121
- GCC_except_table24
- GCC_except_table26
- GCC_except_table27
- GCC_except_table40
- GCC_except_table56
- GCC_except_table59
- GCC_except_table65
- GCC_except_table71
- __ZNKSt9type_infoeqB8ne200100ERKS_
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne200100Ev
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- ___42+[_ANEDeviceInfo aneSubTypeProductVariant]_block_invoke.68
- ___block_literal_global.228
- ___block_literal_global.233
- ___block_literal_global.244
- ___block_literal_global.258
- ___block_literal_global.263
- ___block_literal_global.67
- ___block_literal_global.70
- ___block_literal_global.75
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$stringByAppendingString:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
CStrings:
+ ".mlir"
+ "ANE Arch String: %@"
+ "ChipID"
+ "ChipID: 0x%llx, Ane Subtype: 0x%llx"
+ "ERROR : Failed to get aneSubTypeAndVariant from VM host, (no connection to virtualClient)"
+ "ERROR : Failed to get aneSubTypeAndVariant from VM host, using default AneSubTypeAndVariant"
+ "aneSubTypeAndVariant"
+ "h13c"
+ "h13d"
+ "h13g"
+ "h13p"
+ "h13s"
+ "h14c"
+ "h14d"
+ "h14g"
+ "h14p"
+ "h14s"
+ "h15c"
+ "h15d"
+ "h15g"
+ "h15m"
+ "h15p"
+ "h15s"
+ "h16c"
+ "h16g"
+ "h16p"
+ "h16s"
+ "h17g"
+ "h17p"
+ "h18p"
+ "mlirExtension"
+ "reportTelemetryToCoreAnalytics:payload:"
+ "stringWithString:"
+ "{DeviceExtendedInfo={DeviceInfo=IqqB}BII[32c][8c]}16@0:8"
- "stringByAppendingString:"
- "{DeviceExtendedInfo={DeviceInfo=IqqB}BII[32c]}16@0:8"

```
