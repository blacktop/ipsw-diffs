## Calculate

> `/System/Library/PrivateFrameworks/Calculate.framework/Versions/A/Calculate`

```diff

-172.400.0.0.0
-  __TEXT.__text: 0xbe088
-  __TEXT.__auth_stubs: 0x15b0
-  __TEXT.__objc_methlist: 0x1e2c
-  __TEXT.__const: 0x13e7f0
-  __TEXT.__cstring: 0x27ba
-  __TEXT.__constg_swiftt: 0x15e0
-  __TEXT.__swift5_typeref: 0x724
-  __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x950
-  __TEXT.__swift5_fieldmd: 0xc2c
+174.400.0.0.0
+  __TEXT.__text: 0xc95a0
+  __TEXT.__auth_stubs: 0x1860
+  __TEXT.__objc_methlist: 0x1fe4
+  __TEXT.__const: 0x13e9e0
+  __TEXT.__cstring: 0x29bd
+  __TEXT.__constg_swiftt: 0x178c
+  __TEXT.__swift5_typeref: 0x868
+  __TEXT.__swift5_builtin: 0x8c
+  __TEXT.__swift5_reflstr: 0xa00
+  __TEXT.__swift5_fieldmd: 0xd10
   __TEXT.__swift5_assocty: 0x198
-  __TEXT.__swift5_proto: 0x12c
-  __TEXT.__swift5_types: 0xe0
-  __TEXT.__swift5_capture: 0xf0
-  __TEXT.__gcc_except_tab: 0x1094
+  __TEXT.__swift5_proto: 0x138
+  __TEXT.__swift5_types: 0xf8
+  __TEXT.__swift5_capture: 0x1a0
+  __TEXT.__gcc_except_tab: 0x10f8
   __TEXT.__oslogstring: 0x434
-  __TEXT.__ustring: 0x292
-  __TEXT.__unwind_info: 0x1e00
-  __TEXT.__eh_frame: 0x91c
-  __TEXT.__objc_classname: 0x22f
-  __TEXT.__objc_methname: 0x4faf
-  __TEXT.__objc_methtype: 0xcfd
-  __TEXT.__objc_stubs: 0x3bc0
-  __DATA_CONST.__got: 0x3a8
-  __DATA_CONST.__const: 0x668
-  __DATA_CONST.__objc_classlist: 0x1f0
+  __TEXT.__ustring: 0x286
+  __TEXT.__unwind_info: 0x20f0
+  __TEXT.__eh_frame: 0x1138
+  __TEXT.__objc_classname: 0x231
+  __TEXT.__objc_methname: 0x530a
+  __TEXT.__objc_methtype: 0xd01
+  __TEXT.__objc_stubs: 0x3dc0
+  __DATA_CONST.__got: 0x430
+  __DATA_CONST.__const: 0x650
+  __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13c0
+  __DATA_CONST.__objc_selrefs: 0x1490
   __DATA_CONST.__objc_superrefs: 0x90
   __DATA_CONST.__objc_arraydata: 0x880
-  __AUTH_CONST.__auth_got: 0xae8
-  __AUTH_CONST.__auth_ptr: 0x348
-  __AUTH_CONST.__const: 0x2898
-  __AUTH_CONST.__cfstring: 0x3960
-  __AUTH_CONST.__objc_const: 0x5c28
+  __AUTH_CONST.__auth_got: 0xc40
+  __AUTH_CONST.__auth_ptr: 0x3d8
+  __AUTH_CONST.__const: 0x2c70
+  __AUTH_CONST.__cfstring: 0x39a0
+  __AUTH_CONST.__objc_const: 0x5eb0
   __AUTH_CONST.__objc_intobj: 0x450
   __AUTH_CONST.__objc_arrayobj: 0x540
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH.__objc_data: 0xa80
-  __AUTH.__data: 0x21e0
-  __DATA.__objc_ivar: 0x2fc
-  __DATA.__data: 0x474
-  __DATA.__bss: 0x30b0
+  __AUTH.__objc_data: 0xc70
+  __AUTH.__data: 0x22e8
+  __DATA.__objc_ivar: 0x310
+  __DATA.__data: 0x5ec
+  __DATA.__bss: 0x3240
   __DATA.__common: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/Versions/A/FeatureFlags
   - /System/Library/PrivateFrameworks/OAuth.framework/Versions/A/OAuth
   - /System/Library/PrivateFrameworks/ScreenReaderCore.framework/Versions/A/ScreenReaderCore
+  - /System/Library/PrivateFrameworks/StocksKit.framework/Versions/A/StocksKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2784
-  Symbols:   3001
-  CStrings:  586
+  Functions: 2989
+  Symbols:   3114
+  CStrings:  609
 
Symbols:
+ +[CalculateResult resultWithResultTree:parseTree:locales:numberFormatter:unitsInfo:unitType:unitExponent:expression:isTrivial:isPartialExpression:variableLookups:variableResultTrees:variableResultTreesCount:resolvedUnitFormats:forceResult:assumeDegrees:localizeUnit:unitFormat:autoScientificNotation:scientificNotationFormat:flexibleFractionDigits:isSimpleVerticalMath:minimumFractionDigits:hasStaleCurrencyData:]
+ +[CalculateTokenizer loadPunctuationSet]
+ +[CalculateTokenizer nonWhitespaceLanguageSet]
+ +[CalculateTokenizer punctuationSet]
+ -[CalculateRequest evaluate]
+ -[CalculateResult isSimpleVerticalMath]
+ -[CalculateResult setIsSimpleVerticalMath:]
+ -[CalculateToken characterType]
+ -[CalculateToken isUnknown]
+ -[CalculateToken loadedNeedsWhitespaceAfter]
+ -[CalculateToken needsWhitespaceAfter]
+ -[CalculateToken setCharacterType:]
+ -[CalculateToken setLoadedNeedsWhitespaceAfter:]
+ -[CalculateToken setNeedsWhitespaceAfter:]
+ -[CalculateTokenizer foundGraphableValue]
+ -[CalculateTokenizer init]
+ -[CalculateTokenizer setFoundGraphableValue:]
+ -[CalculateUnitOutput resolvedUnitFormatForUnitID:string:]
+ -[NSString(Regex) calc_stringByReplacingOccurrencesOfRegex:usingBlock:]
+ -[NSString(Regex) calc_stringByReplacingOccurrencesOfRegex:usingBlockWithResult:]
+ GCC_except_table18
+ GCC_except_table238
+ GCC_except_table29
+ GCC_except_table32
+ GCC_except_table42
+ GCC_except_table479
+ GCC_except_table481
+ GCC_except_table516
+ GCC_except_table781
+ GCC_except_table892
+ OBJC_IVAR_$_CalculateResult._isSimpleVerticalMath
+ OBJC_IVAR_$_CalculateToken._characterType
+ OBJC_IVAR_$_CalculateToken._loadedNeedsWhitespaceAfter
+ OBJC_IVAR_$_CalculateToken._needsWhitespaceAfter
+ OBJC_IVAR_$_CalculateTokenizer._foundGraphableValue
+ _OBJC_CLASS_$__TtC9Calculate22StocksKitCurrencyCache
+ _OBJC_CLASS_$__TtC9Calculate26StocksKitCurrencyCacheImpl
+ _OBJC_METACLASS_$__TtC9Calculate22StocksKitCurrencyCache
+ _OBJC_METACLASS_$__TtC9Calculate26StocksKitCurrencyCacheImpl
+ __26-[CalculateRequest update]_block_invoke.927
+ __31-[CalculateTerm formattedValue]_block_invoke.595
+ __31-[CalculateTerm formattedValue]_block_invoke.599
+ __33+[CalculateTokenizer addSymbols:]_block_invoke.172
+ __33+[CalculateTokenizer addSymbols:]_block_invoke.175
+ __36-[CalculateTokenizer _findNextToken]_block_invoke.979
+ __36-[CalculateTokenizer _findNextToken]_block_invoke.980
+ __36-[CalculateTokenizer _findNextToken]_block_invoke.984
+ __36-[CalculateTokenizer _findNextToken]_block_invoke.986
+ __36-[CalculateTokenizer _findNextToken]_block_invoke.993
+ __39+[CalculateTokenizer addUnits:builtIn:]_block_invoke.559
+ __39+[CalculateTokenizer addUnits:builtIn:]_block_invoke.563
+ __39-[CalculateResult localizedConversions]_block_invoke.713
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke.1143
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke.1156
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke.1186
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke.1293
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke.1307
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke.1328
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke.1341
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke.1353
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_2.1147
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_2.1162
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_2.1192
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_2.1303
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_2.1311
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_2.990
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_3.1135
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_3.1171
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_3.1198
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_3.1313
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_4.1175
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_4.1204
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_4.1314
+ __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_5.1208
+ __58-[CalculateUnitOutput resolvedUnitFormatForUnitID:string:]_block_invoke.308
+ __81-[NSString(Regex) calc_stringByReplacingOccurrencesOfRegex:usingBlockWithResult:]_block_invoke.1
+ __Block_byref_object_copy_.343
+ __Block_byref_object_copy_.559
+ __Block_byref_object_copy_.632
+ __Block_byref_object_dispose_.344
+ __Block_byref_object_dispose_.560
+ __Block_byref_object_dispose_.633
+ __CLASS_METHODS__TtC9Calculate22StocksKitCurrencyCache
+ __CLASS_PROPERTIES__TtC9Calculate22StocksKitCurrencyCache
+ __DATA__TtC9Calculate22StocksKitCurrencyCache
+ __DATA__TtC9Calculate26StocksKitCurrencyCacheImpl
+ __INSTANCE_METHODS__TtC9Calculate22StocksKitCurrencyCache
+ __INSTANCE_METHODS__TtC9Calculate26StocksKitCurrencyCacheImpl
+ __IVARS__TtC9Calculate26StocksKitCurrencyCacheImpl
+ __METACLASS_DATA__TtC9Calculate22StocksKitCurrencyCache
+ __METACLASS_DATA__TtC9Calculate26StocksKitCurrencyCacheImpl
+ __OBJC_$_CLASS_PROP_LIST_CalculateCurrencyCache
+ __PROPERTIES__TtC9Calculate22StocksKitCurrencyCache
+ __PROPERTIES__TtC9Calculate26StocksKitCurrencyCacheImpl
+ ___40+[CalculateTokenizer loadPunctuationSet]_block_invoke
+ ___46+[CalculateTokenizer nonWhitespaceLanguageSet]_block_invoke
+ ___46+[CalculateTokenizer nonWhitespaceLanguageSet]_block_invoke_2
+ ___58-[CalculateUnitOutput resolvedUnitFormatForUnitID:string:]_block_invoke
+ ___71-[NSString(Regex) calc_stringByReplacingOccurrencesOfRegex:usingBlock:]_block_invoke
+ ___81-[NSString(Regex) calc_stringByReplacingOccurrencesOfRegex:usingBlockWithResult:]_block_invoke
+ ___81-[NSString(Regex) calc_stringByReplacingOccurrencesOfRegex:usingBlockWithResult:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e21_i24?0"UnitInfo"8Q16l
+ ___block_descriptor_40_e8_32bs_e28_"NSString"16?0"NSNumber"8l
+ ___block_descriptor_40_e8_32s_e34_"NSString"28?0"UnitInfo"8Q16B24l
+ ___block_descriptor_40_e8_32s_e8_v12?0B8l
+ ___block_descriptor_48_e8_32s_e34_"NSString"32?0"NSNumber"8Q16Q24l
+ ___block_descriptor_80_e8_32s40s48r_e5_v8?0l
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_memcpy0_1
+ __block_literal_global.1158
+ __block_literal_global.1164
+ __block_literal_global.1177
+ __block_literal_global.1188
+ __block_literal_global.1194
+ __block_literal_global.1200
+ __block_literal_global.1210
+ __block_literal_global.1218
+ __block_literal_global.1223
+ __block_literal_global.1228
+ __block_literal_global.1233
+ __block_literal_global.1241
+ __block_literal_global.1246
+ __block_literal_global.1251
+ __block_literal_global.1265
+ __block_literal_global.1273
+ __block_literal_global.1281
+ __block_literal_global.1356
+ __block_literal_global.148
+ __block_literal_global.160
+ __block_literal_global.162
+ __block_literal_global.165
+ __block_literal_global.397
+ __block_literal_global.537
+ __block_literal_global.553
+ __block_literal_global.565
+ __block_literal_global.68
+ __block_literal_global.681
+ __block_literal_global.700
+ __block_literal_global.709
+ __block_literal_global.844
+ __block_literal_global.858
+ __block_literal_global.88
+ __block_literal_global.90
+ __block_literal_global.918
+ __block_literal_global.921
+ __block_literal_global.929
+ __block_literal_global.97
+ __block_literal_global.971
+ __block_literal_global.975
+ __block_literal_global.977
+ __block_literal_global.980
+ __block_literal_global.983
+ __block_literal_global.996
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_Calculate
+ _associated conformance 9Calculate21StocksKitFeatureFlagsOSHAASQ
+ _characterTypeForCharacter
+ _lock.onceToken.536
+ _lock.onceToken.969
+ _objc_msgSend$addCharactersInRange:
+ _objc_msgSend$calc_stringByReplacingOccurrencesOfRegex:usingBlock:
+ _objc_msgSend$calc_stringByReplacingOccurrencesOfRegex:usingBlockWithResult:
+ _objc_msgSend$compare:options:
+ _objc_msgSend$decimalNumberByMultiplyingBy:
+ _objc_msgSend$evaluate
+ _objc_msgSend$isEnabled
+ _objc_msgSend$isSimpleVerticalMath
+ _objc_msgSend$isUnknown
+ _objc_msgSend$loadPunctuationSet
+ _objc_msgSend$needsWhitespaceAfter
+ _objc_msgSend$nonWhitespaceLanguageSet
+ _objc_msgSend$numberFromString:
+ _objc_msgSend$punctuationCharacterSet
+ _objc_msgSend$refreshSynchronously
+ _objc_msgSend$refreshSynchronouslyWithTimeout:
+ _objc_msgSend$refreshWithCompletionHandler:
+ _objc_msgSend$resolvedUnitFormatForUnitID:string:
+ _objc_msgSend$resultWithResultTree:parseTree:locales:numberFormatter:unitsInfo:unitType:unitExponent:expression:isTrivial:isPartialExpression:variableLookups:variableResultTrees:variableResultTreesCount:resolvedUnitFormats:forceResult:assumeDegrees:localizeUnit:unitFormat:autoScientificNotation:scientificNotationFormat:flexibleFractionDigits:isSimpleVerticalMath:minimumFractionDigits:hasStaleCurrencyData:
+ _objc_msgSend$setCharacterType:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _punctuationSet
+ _swift_getAssociatedConformanceWitness
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getOpaqueTypeConformance2
+ _swift_initStructMetadata
+ _swift_isaMask
+ _swift_storeEnumTagSinglePayloadGeneric
+ _symbolic IeAghH_
+ _symbolic IeghH_
+ _symbolic SbIeyBy_
+ _symbolic Sd
+ _symbolic So21OS_dispatch_semaphoreC
+ _symbolic _____ 10Foundation4DataV
+ _symbolic _____ 9Calculate21StocksKitFeatureFlagsO
+ _symbolic _____ 9Calculate22StocksKitCurrencyCacheC
+ _symbolic _____ 9Calculate22StocksKitCurrencyCacheC12ProviderDataV
+ _symbolic _____ 9Calculate22StocksKitCurrencyCacheC12ProviderLogoV
+ _symbolic _____ 9Calculate26StocksKitCurrencyCacheImplC
+ _symbolic _____ So16os_unfair_lock_sV
+ _symbolic _____ s6UInt32V
+ _symbolic _____Sg 10Foundation3URLV
+ _symbolic _____Sg 10Foundation4DataV
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____Sg 9Calculate22StocksKitCurrencyCacheC12ProviderLogoV
+ _symbolic _____Sg 9StocksKit10DataSourceV14DownloadedLogoV
+ _symbolic _____Sg 9StocksKit10DataSourceV4LogoV
+ _symbolic _____Sg 9StocksKit25CurrencyConversionsResultV
+ _symbolic _____Sg 9StocksKit8CurrencyV
+ _symbolic _____ySSSo8NSNumberCG s18_DictionaryStorageC
+ _symbolic _____ySbG 2os21OSAllocatedUnfairLockV
+ _symbolic _____ySb_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic _____y_Qo_ 9StocksKit19CurrencyConversionsV10currenciesQrvpQO
+ _symbolic _____y_Qo_8IteratorSTQx 9StocksKit19CurrencyConversionsV10currenciesQrvpQO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 9Calculate0D10ExpressionC9TokenTypeO
+ _symbolic _____y_____SgG 2os21OSAllocatedUnfairLockV 10Foundation4DateV
+ _symbolic _____y_____SgG 2os21OSAllocatedUnfairLockV 9StocksKit25CurrencyConversionsResultV
+ _symbolic _____y_____Sg_____G s13ManagedBufferCsRi__rlE 10Foundation4DateV So16os_unfair_lock_sV
+ _symbolic _____y_____Sg_____G s13ManagedBufferCsRi__rlE 9StocksKit25CurrencyConversionsResultV So16os_unfair_lock_sV
+ bid___div_128_by_128.1023
+ bid___div_128_by_128.991
+ bid_decimal128_moduli.1057
+ bid_get_BID128.1054
+ block_copy_helper.38
+ block_copy_helper.42
+ block_copy_helper.46
+ block_descriptor.40
+ block_descriptor.44
+ block_descriptor.48
+ block_destroy_helper.39
+ block_destroy_helper.43
+ block_destroy_helper.47
+ c_11000.1044
+ c_11000.984
+ c_1em40.1040
+ c_1em40.1061
+ c_1em40.942
+ c_1em40.951
+ c_1em40.970
+ c_1em40.980
+ c_64.1042
+ c_7_10ths.943
+ c_half.1002
+ c_half.1006
+ c_half.1045
+ c_half.973
+ c_half.996
+ c_log10.948
+ c_one.1001
+ c_one.1005
+ c_one.1041
+ c_one.944
+ c_one.971
+ c_one.981
+ c_one.997
+ c_pi.998
+ c_pi_ov_2.1037
+ c_pi_ov_2.1058
+ c_zero.1043
+ c_zero.945
+ c_zero.972
+ calc_stringByReplacingOccurrencesOfRegex:usingBlockWithResult:.lock
+ calc_stringByReplacingOccurrencesOfRegex:usingBlockWithResult:.onceToken
+ calc_stringByReplacingOccurrencesOfRegex:usingBlockWithResult:.regexes
+ loadPunctuationSet.onceToken
+ nonWhitespaceLanguageSet.nonWhitespaceLanguageSet
+ nonWhitespaceLanguageSet.onceToken
+ objectdestroy.23Tm
+ objectdestroy.27Tm
+ objectdestroy.43Tm
+ shared.onceToken.843
+ shared.shared.845
- +[CalculateResult resultWithResultTree:parseTree:locales:numberFormatter:unitsInfo:unitType:unitExponent:expression:isTrivial:isPartialExpression:variableLookups:variableResultTrees:variableResultTreesCount:resolvedUnitFormats:forceResult:assumeDegrees:localizeUnit:unitFormat:autoScientificNotation:scientificNotationFormat:flexibleFractionDigits:minimumFractionDigits:hasStaleCurrencyData:]
- -[CalculateCurrencyCache setCurrencyData:]
- -[CalculateUnitOutput resolvedUnitFormatForUnitID:stringLength:]
- -[NSString(Regex) stringByReplacingOccurrencesOfRegex:usingBlock:]
- -[NSString(Regex) stringByReplacingOccurrencesOfRegex:usingBlockWithResult:]
- GCC_except_table19
- GCC_except_table239
- GCC_except_table30
- GCC_except_table33
- GCC_except_table43
- GCC_except_table478
- GCC_except_table480
- GCC_except_table514
- GCC_except_table776
- GCC_except_table891
- __31-[CalculateTerm formattedValue]_block_invoke.592
- __33+[CalculateTokenizer addSymbols:]_block_invoke.143
- __33+[CalculateTokenizer addSymbols:]_block_invoke.146
- __36-[CalculateTokenizer _findNextToken]_block_invoke.953
- __36-[CalculateTokenizer _findNextToken]_block_invoke.954
- __36-[CalculateTokenizer _findNextToken]_block_invoke.958
- __36-[CalculateTokenizer _findNextToken]_block_invoke.960
- __36-[CalculateTokenizer _findNextToken]_block_invoke.967
- __39+[CalculateTokenizer addUnits:builtIn:]_block_invoke.530
- __39+[CalculateTokenizer addUnits:builtIn:]_block_invoke.534
- __39-[CalculateResult localizedConversions]_block_invoke.700
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke.1119
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke.1132
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke.1161
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke.1268
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke.1288
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke.1295
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke.1305
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke.1330
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_2.1123
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_2.1138
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_2.1167
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_2.1278
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_2.1290
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_2.966
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_3.1111
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_3.1147
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_3.1173
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_3.1284
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_3.1291
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_4.1151
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_4.1179
- __48+[Calculate evaluate:options:error:needsUpdate:]_block_invoke_5.1183
- __76-[NSString(Regex) stringByReplacingOccurrencesOfRegex:usingBlockWithResult:]_block_invoke.1
- __Block_byref_object_copy_.341
- __Block_byref_object_copy_.556
- __Block_byref_object_copy_.635
- __Block_byref_object_dispose_.342
- __Block_byref_object_dispose_.557
- __Block_byref_object_dispose_.636
- ___39+[CalculateTokenizer addUnits:builtIn:]_block_invoke_2
- ___64-[CalculateUnitOutput resolvedUnitFormatForUnitID:stringLength:]_block_invoke
- ___66-[NSString(Regex) stringByReplacingOccurrencesOfRegex:usingBlock:]_block_invoke
- ___76-[NSString(Regex) stringByReplacingOccurrencesOfRegex:usingBlockWithResult:]_block_invoke
- ___76-[NSString(Regex) stringByReplacingOccurrencesOfRegex:usingBlockWithResult:]_block_invoke_2
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_40_e8_32s_e21_i24?0"UnitInfo"8Q16l
- ___block_descriptor_40_e8_32s_e34_"NSString"32?0"NSNumber"8Q16Q24l
- ___block_descriptor_72_e8_32s40s48r_e5_v8?0l
- __block_literal_global.1134
- __block_literal_global.1140
- __block_literal_global.1153
- __block_literal_global.1163
- __block_literal_global.1169
- __block_literal_global.1175
- __block_literal_global.1185
- __block_literal_global.1193
- __block_literal_global.1198
- __block_literal_global.1203
- __block_literal_global.1208
- __block_literal_global.1216
- __block_literal_global.1221
- __block_literal_global.1226
- __block_literal_global.1231
- __block_literal_global.1240
- __block_literal_global.1248
- __block_literal_global.1280
- __block_literal_global.1333
- __block_literal_global.137
- __block_literal_global.138
- __block_literal_global.395
- __block_literal_global.534
- __block_literal_global.536
- __block_literal_global.550
- __block_literal_global.652
- __block_literal_global.67
- __block_literal_global.690
- __block_literal_global.696
- __block_literal_global.77
- __block_literal_global.829
- __block_literal_global.85
- __block_literal_global.899
- __block_literal_global.901
- __block_literal_global.902
- __block_literal_global.906
- __block_literal_global.947
- __block_literal_global.951
- __block_literal_global.953
- __block_literal_global.956
- __block_literal_global.959
- __block_literal_global.970
- _lock.onceToken.533
- _lock.onceToken.945
- _objc_msgSend$resolvedUnitFormatForUnitID:stringLength:
- _objc_msgSend$resultWithResultTree:parseTree:locales:numberFormatter:unitsInfo:unitType:unitExponent:expression:isTrivial:isPartialExpression:variableLookups:variableResultTrees:variableResultTreesCount:resolvedUnitFormats:forceResult:assumeDegrees:localizeUnit:unitFormat:autoScientificNotation:scientificNotationFormat:flexibleFractionDigits:minimumFractionDigits:hasStaleCurrencyData:
- _objc_msgSend$stringByReplacingOccurrencesOfRegex:usingBlock:
- _objc_msgSend$stringByReplacingOccurrencesOfRegex:usingBlockWithResult:
- _symbolic SDySS_____y_____GGz_Xx 9Calculate7WeakRefC AA0A10ExpressionC
- bid___div_128_by_128.1045
- bid___div_128_by_128.1077
- bid_decimal128_moduli.1111
- bid_get_BID128.1108
- block_copy_helper.41
- block_copy_helper.43
- block_copy_helper.45
- block_descriptor.43
- block_descriptor.45
- block_descriptor.47
- block_destroy_helper.42
- block_destroy_helper.44
- block_destroy_helper.46
- c_11000.1038
- c_11000.1098
- c_1em40.1005
- c_1em40.1024
- c_1em40.1034
- c_1em40.1094
- c_1em40.1115
- c_1em40.996
- c_64.1096
- c_7_10ths.997
- c_half.1027
- c_half.1050
- c_half.1056
- c_half.1060
- c_half.1099
- c_log10.1002
- c_one.1025
- c_one.1035
- c_one.1051
- c_one.1055
- c_one.1059
- c_one.1095
- c_one.998
- c_pi.1052
- c_pi_ov_2.1091
- c_pi_ov_2.1112
- c_zero.1026
- c_zero.1097
- c_zero.999
- shared.onceToken.900
- shared.shared.902
- stringByReplacingOccurrencesOfRegex:usingBlockWithResult:.lock
- stringByReplacingOccurrencesOfRegex:usingBlockWithResult:.onceToken
- stringByReplacingOccurrencesOfRegex:usingBlockWithResult:.regexes
CStrings:
+ "%!@(MISSING)%!@(MISSING)%!@(MISSING)"
+ "-0"
+ "@\"NSString\"16@?0@\"NSNumber\"8"
+ "@\"NSString\"28@?0@\"UnitInfo\"8Q16B24"
+ "B16@0:8"
+ "B24@0:8d16"
+ "LegacyCurrencyCache"
+ "T@\"NSDictionary\",N,R"
+ "T@\"_TtC9Calculate22StocksKitCurrencyCache\",N,&"
+ "TB,N,R"
+ "_TtC9Calculate22StocksKitCurrencyCache"
+ "_TtC9Calculate26StocksKitCurrencyCacheImpl"
+ "_isLikelyMath"
+ "currencyData"
+ "currencyDataLock"
+ "isEnabled"
+ "lastRefreshDateLock"
+ "needsRefresh"
+ "shared"
+ "v12@?0B8"
+ "v24@0:8@16"
+ "v24@0:8@?<v@?B>16"
+ "v32@0:8d16@?<v@?B>24"

```
