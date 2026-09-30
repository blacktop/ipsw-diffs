## BiometricKit

> `/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`

```diff

-545.40.2.0.0
-  __TEXT.__text: 0x43a38
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_methlist: 0x2c9c
-  __TEXT.__const: 0x220
-  __TEXT.__cstring: 0x2c82
-  __TEXT.__oslogstring: 0x4e24
-  __TEXT.__gcc_except_tab: 0xdf4
-  __TEXT.__unwind_info: 0x10a0
-  __TEXT.__objc_classname: 0x4e7
-  __TEXT.__objc_methname: 0x5daf
-  __TEXT.__objc_methtype: 0x12ef
-  __TEXT.__objc_stubs: 0x3920
-  __DATA_CONST.__got: 0x278
-  __DATA_CONST.__const: 0x870
-  __DATA_CONST.__objc_classlist: 0x178
+545.100.10.0.0
+  __TEXT.__text: 0x40780
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_methlist: 0x2cc4
+  __TEXT.__const: 0x218
+  __TEXT.__cstring: 0x2eba
+  __TEXT.__oslogstring: 0x4f6a
+  __TEXT.__gcc_except_tab: 0xcac
+  __TEXT.__unwind_info: 0x1258
+  __TEXT.__objc_classname: 0x4d2
+  __TEXT.__objc_methname: 0x5d29
+  __TEXT.__objc_methtype: 0x12db
+  __TEXT.__objc_stubs: 0x3800
+  __DATA_CONST.__got: 0x248
+  __DATA_CONST.__const: 0x848
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1778
+  __DATA_CONST.__objc_selrefs: 0x1748
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x3d0
+  __AUTH_CONST.__auth_got: 0x390
   __AUTH_CONST.__const: 0x540
-  __AUTH_CONST.__cfstring: 0x1800
-  __AUTH_CONST.__objc_const: 0x5250
+  __AUTH_CONST.__cfstring: 0x17a0
+  __AUTH_CONST.__objc_const: 0x51c8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH.__objc_data: 0x960
+  __AUTH.__objc_data: 0x910
   __DATA.__objc_ivar: 0x2e0
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5FC3DD44-FD01-3D32-B2E2-D0054D5DD6EC
-  Functions: 1512
-  Symbols:   4580
-  CStrings:  2238
+  UUID: 4F92F4BB-4DB2-3467-8786-84C682F5CFBA
+  Functions: 1553
+  Symbols:   4674
+  CStrings:  2223
 
Symbols:
+ +[BKDefaults removeAllPreferencesWithError:]
+ +[BKDefaults removeAllPreferencesWithError:].cold.1
+ +[BKDefaults removeAllPreferencesWithError:].cold.2
+ +[BKDefaults setValue:forKey:withError:]
+ +[BKDefaults setValue:forKey:withError:].cold.1
+ +[BKDefaults setValue:forKey:withError:].cold.2
+ +[BKDefaults valueForKey:withError:]
+ +[BKDefaults valueForKey:withError:].cold.1
+ +[BKDefaults valueForKey:withError:].cold.2
+ +[BioUserDefaults initialize]
+ +[BioUserDefaults initialize].cold.1
+ +[BioUserDefaults removeAllPreferences]
+ +[BioUserDefaults removeLegacyPreferences]
+ -[BioUserDefaults objectForKey:]
+ -[BiometricKitXPCClient removeAllPreferences]
+ -[BiometricKitXPCClient removeAllPreferences].cold.1
+ GCC_except_table109
+ GCC_except_table155
+ GCC_except_table278
+ GCC_except_table3
+ _CFPreferencesSetMultiple
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ ___45-[BiometricKitXPCClient removeAllPreferences]_block_invoke
+ ___45-[BiometricKitXPCClient removeAllPreferences]_block_invoke_2
+ ___46-[BKEnrollPearlOperation enrollUpdate:client:]_block_invoke.374
+ ___46-[BKEnrollPearlOperation enrollUpdate:client:]_block_invoke.375
+ ___47-[BKEnrollPearlOperation statusMessage:client:]_block_invoke.363
+ ___47-[BKEnrollPearlOperation statusMessage:client:]_block_invoke.367
+ ___48-[BiometricKitXPCClientConnection xpcConnection]_block_invoke.229
+ ___48-[BiometricKitXPCClientConnection xpcConnection]_block_invoke.231
+ ___48-[BiometricKitXPCClientConnection xpcConnection]_block_invoke.233
+ ___54-[BKFaceDetectOperation statusMessage:details:client:]_block_invoke.276
+ ___54-[BKMatchPearlOperation statusMessage:details:client:]_block_invoke.461
+ ___54-[BKMatchPearlOperation statusMessage:details:client:]_block_invoke.471
+ ___54-[BKMatchPearlOperation statusMessage:details:client:]_block_invoke.472
+ ___54-[BKMatchPearlOperation statusMessage:details:client:]_block_invoke.475
+ ___block_literal_global.301
+ ___block_literal_global.303
+ ___block_literal_global.305
+ ___block_literal_global.307
+ ___block_literal_global.309
+ ___block_literal_global.313
+ ___block_literal_global.315
+ ___block_literal_global.317
+ ___block_literal_global.320
+ ___block_literal_global.323
+ ___block_literal_global.326
+ ___block_literal_global.328
+ ___block_literal_global.331
+ ___block_literal_global.333
+ ___block_literal_global.335
+ ___block_literal_global.338
+ ___block_literal_global.342
+ ___block_literal_global.345
+ ___block_literal_global.348
+ ___block_literal_global.351
+ ___block_literal_global.353
+ ___block_literal_global.355
+ ___block_literal_global.357
+ ___block_literal_global.359
+ ___block_literal_global.361
+ ___block_literal_global.363
+ ___block_literal_global.365
+ ___block_literal_global.368
+ ___block_literal_global.370
+ ___block_literal_global.372
+ ___block_literal_global.375
+ ___block_literal_global.378
+ ___block_literal_global.380
+ ___block_literal_global.382
+ ___block_literal_global.384
+ ___block_literal_global.388
+ _objc_msgSend$operation:captureInterrupted:
+ _objc_msgSend$removeAllPreferences
+ _objc_msgSend$removeAllPreferencesWithClient:replyBlock:
+ _objc_msgSend$removeLegacyPreferences
+ _objc_retainAutoreleasedReturnValue
- +[BiometricPreferences preferenceValueOfClass:forKey:]
- +[BiometricPreferences setPreferenceValue:forKey:]
- +[BiometricSupportTools analyticsOSLogNSDictionary:forEvent:]
- +[BiometricSupportTools analyticsOSLogNSDictionary:forEvent:toLogPath:withPrefix:]
- +[BiometricSupportTools analyticsOSLogNSDictionary:forEvent:toLogPath:withPrefix:].cold.1
- +[BiometricSupportTools analyticsOSLogNSDictionary:forEvent:toLogPath:withPrefix:].cold.2
- +[BiometricSupportTools analyticsOSLogNSDictionary:forEvent:toLogPath:withPrefix:].cold.3
- GCC_except_table147
- GCC_except_table2
- GCC_except_table4
- _NSFileOwnerAccountName
- _NSFileProtectionKey
- _NSFileProtectionNone
- _OBJC_CLASS_$_BiometricPreferences
- _OBJC_CLASS_$_NSMutableString
- _OBJC_METACLASS_$_BiometricPreferences
- __OBJC_$_CLASS_METHODS_BiometricPreferences
- __OBJC_CLASS_RO_$_BiometricPreferences
- __OBJC_METACLASS_RO_$_BiometricPreferences
- ___46-[BKEnrollPearlOperation enrollUpdate:client:]_block_invoke.368
- ___46-[BKEnrollPearlOperation enrollUpdate:client:]_block_invoke.369
- ___47-[BKEnrollPearlOperation statusMessage:client:]_block_invoke.357
- ___47-[BKEnrollPearlOperation statusMessage:client:]_block_invoke.361
- ___48-[BiometricKitXPCClientConnection xpcConnection]_block_invoke.228
- ___48-[BiometricKitXPCClientConnection xpcConnection]_block_invoke.230
- ___48-[BiometricKitXPCClientConnection xpcConnection]_block_invoke.232
- ___54-[BKMatchPearlOperation statusMessage:details:client:]_block_invoke.455
- ___54-[BKMatchPearlOperation statusMessage:details:client:]_block_invoke.459
- ___54-[BKMatchPearlOperation statusMessage:details:client:]_block_invoke.466
- ___54-[BKMatchPearlOperation statusMessage:details:client:]_block_invoke.469
- ___82+[BiometricSupportTools analyticsOSLogNSDictionary:forEvent:toLogPath:withPrefix:]_block_invoke
- ___82+[BiometricSupportTools analyticsOSLogNSDictionary:forEvent:toLogPath:withPrefix:]_block_invoke.cold.1
- ___82+[BiometricSupportTools analyticsOSLogNSDictionary:forEvent:toLogPath:withPrefix:]_block_invoke.cold.2
- ___GenerateTemplateTopology.cold.2
- ___TranslateNodePlacement.cold.4
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e5_v8?0ls32l8s40l8r72l8s48l8s56l8s64l8
- ___block_literal_global.300
- ___block_literal_global.302
- ___block_literal_global.304
- ___block_literal_global.306
- ___block_literal_global.308
- ___block_literal_global.312
- ___block_literal_global.314
- ___block_literal_global.316
- ___block_literal_global.319
- ___block_literal_global.322
- ___block_literal_global.325
- ___block_literal_global.327
- ___block_literal_global.330
- ___block_literal_global.332
- ___block_literal_global.334
- ___block_literal_global.337
- ___block_literal_global.341
- ___block_literal_global.344
- ___block_literal_global.347
- ___block_literal_global.350
- ___block_literal_global.352
- ___block_literal_global.354
- ___block_literal_global.356
- ___block_literal_global.358
- ___block_literal_global.360
- ___block_literal_global.362
- ___block_literal_global.364
- ___block_literal_global.367
- ___block_literal_global.369
- ___block_literal_global.371
- ___block_literal_global.374
- ___block_literal_global.377
- ___block_literal_global.379
- ___block_literal_global.381
- ___block_literal_global.383
- ___block_literal_global.387
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$analyticsOSLogNSDictionary:forEvent:toLogPath:withPrefix:
- _objc_msgSend$appendString:
- _objc_msgSend$boolForKey:
- _objc_msgSend$date
- _objc_msgSend$description
- _objc_msgSend$fileExistsAtPath:
- _objc_msgSend$getParagraphStart:end:contentsEnd:forRange:
- _objc_msgSend$objectAtIndexedSubscript:
- _objc_msgSend$sharedInstance
- _objc_msgSend$string
- _objc_msgSend$substringWithRange:
- _objc_msgSend$timeIntervalSince1970
- _objc_msgSend$writeToFile:atomically:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x27
- _objc_retain_x28
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x8
- _os_transaction_create
CStrings:
+ "/Library/Caches/com.apple.xbs/4CBE2313-62C6-4AE3-9B7A-04BA3C295AE4/TemporaryDirectory.vplTtM/Sources/BiometricKit/BiometricKit/BKAccessory.m"
+ "/Library/Caches/com.apple.xbs/4CBE2313-62C6-4AE3-9B7A-04BA3C295AE4/TemporaryDirectory.vplTtM/Sources/BiometricKit/BiometricKit/BKAccessoryGroup.m"
+ "/Library/Caches/com.apple.xbs/4CBE2313-62C6-4AE3-9B7A-04BA3C295AE4/TemporaryDirectory.vplTtM/Sources/BiometricKit/BiometricKit/BKDefaults.m"
+ "/Library/Caches/com.apple.xbs/4CBE2313-62C6-4AE3-9B7A-04BA3C295AE4/TemporaryDirectory.vplTtM/Sources/BiometricKit/BiometricKit/BKDevice.m"
+ "/Library/Caches/com.apple.xbs/4CBE2313-62C6-4AE3-9B7A-04BA3C295AE4/TemporaryDirectory.vplTtM/Sources/BiometricKit/BiometricKit/BKDevicePearl.m"
+ "/Library/Caches/com.apple.xbs/4CBE2313-62C6-4AE3-9B7A-04BA3C295AE4/TemporaryDirectory.vplTtM/Sources/BiometricKit/BiometricKit/BKDeviceTouchID.m"
+ "/Library/Caches/com.apple.xbs/4CBE2313-62C6-4AE3-9B7A-04BA3C295AE4/TemporaryDirectory.vplTtM/Sources/BiometricKit/BiometricKit/BKMatchEvent.m"
+ "/Library/Caches/com.apple.xbs/4CBE2313-62C6-4AE3-9B7A-04BA3C295AE4/TemporaryDirectory.vplTtM/Sources/BiometricKit/BiometricKit/BKOperation.m"
+ "/Library/Caches/com.apple.xbs/4CBE2313-62C6-4AE3-9B7A-04BA3C295AE4/TemporaryDirectory.vplTtM/Sources/BiometricKit/BiometricKit/BKOperationDelegate.m"
+ "/Library/Caches/com.apple.xbs/4CBE2313-62C6-4AE3-9B7A-04BA3C295AE4/TemporaryDirectory.vplTtM/Sources/BiometricKit/BiometricKit/BioUserDefaults.m"
+ "/Library/Caches/com.apple.xbs/4CBE2313-62C6-4AE3-9B7A-04BA3C295AE4/TemporaryDirectory.vplTtM/Sources/BiometricKit/BiometricKit/BiometricKit.m"
+ "/Library/Caches/com.apple.xbs/4CBE2313-62C6-4AE3-9B7A-04BA3C295AE4/TemporaryDirectory.vplTtM/Sources/BiometricKit/BiometricKit/BiometricKitEnrollProgressInfo.m"
+ "/Library/Caches/com.apple.xbs/4CBE2313-62C6-4AE3-9B7A-04BA3C295AE4/TemporaryDirectory.vplTtM/Sources/BiometricKit/BiometricKit/BiometricKitXPCClient.m"
+ "/Library/Caches/com.apple.xbs/4CBE2313-62C6-4AE3-9B7A-04BA3C295AE4/TemporaryDirectory.vplTtM/Sources/BiometricKit/BiometricKit/BiometricSupportTools.m"
+ "/Library/Caches/com.apple.xbs/4CBE2313-62C6-4AE3-9B7A-04BA3C295AE4/TemporaryDirectory.vplTtM/Sources/BiometricKit/TouchID/nodevis.c"
+ "BKDefaults::removeAllPreferences\n"
+ "BKDefaults::removeAllPreferences -> %d, error:%@\n"
+ "BKDefaults::setString:forKey: (%@: %@)\n"
+ "BKDefaults::setString:forKey: (%@: %@) -> %d, error:%@\n"
+ "BKDefaults::setValue:forKey: (%@: %@)\n"
+ "BKDefaults::valueForKey: %@\n"
+ "BKDefaults::valueForKey: -> (%@: %@), error:%@\n"
+ "BKFaceDetectOperation::statusMessage:details:client: captureInterrupted:%u => delegate:%p(%@)\n"
+ "BKStatusDetailCaptureInterruption"
+ "Couldn't create OS Log for 'com.apple.BiometricKit.BioUserDefaults'!\n"
+ "operation:captureInterrupted:"
+ "removeAllPreferences"
+ "removeAllPreferencesWithClient:replyBlock:"
+ "removeAllPreferencesWithError:"
+ "removeLegacyPreferences"
+ "setValue:forKey:withError:"
+ "updateCallback(observer:%p, name:%@, object:%p, userInfo:%@)\n"
+ "valueForKey:withError:"
- "%@/%d_%@.plist"
- "%@: sendEvent: %@ (print %ld of %ld): \n%@\n"
- "%@: write event: %@ to file: %@\n"
- "([[NSFileManager defaultManager] createDirectoryAtPath:path withIntermediateDirectories:__objc_no attributes:@{ NSFileOwnerAccountName: @\"mobile\", NSFileProtectionKey: NSFileProtectionNone } error:((void*)0)])"
- "/Library/Caches/com.apple.xbs/Sources/BiometricKit/BiometricKit/BKAccessory.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricKit/BiometricKit/BKAccessoryGroup.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricKit/BiometricKit/BKDefaults.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricKit/BiometricKit/BKDevice.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricKit/BiometricKit/BKDevicePearl.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricKit/BiometricKit/BKDeviceTouchID.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricKit/BiometricKit/BKMatchEvent.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricKit/BiometricKit/BKOperation.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricKit/BiometricKit/BKOperationDelegate.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricKit/BiometricKit/BioUserDefaults.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricKit/BiometricKit/BiometricKit.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricKit/BiometricKit/BiometricKitEnrollProgressInfo.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricKit/BiometricKit/BiometricKitXPCClient.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricKit/BiometricKit/BiometricSupportTools.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricKit/TouchID/nodevis.c"
- "/private/var/tmp/"
- "BKDevice::setString:forKey: (%@: %@)\n"
- "BKDevice::setString:forKey: (%@: %@) -> %d, error:%@\n"
- "BiometricPreferences"
- "PearlAWD"
- "[dict writeToFile:filePath atomically:__objc_yes]"
- "analyticsDispatchQueue"
- "analyticsOSLogNSDictionary:forEvent:"
- "analyticsOSLogNSDictionary:forEvent:toLogPath:withPrefix:"
- "analyticsSaveToFile"
- "appendString:"
- "com.apple.biometrickit.analyticsFileLog"
- "convertedTopology"
- "date"
- "fileExistsAtPath:"
- "getParagraphStart:end:contentsEnd:forRange:"
- "objectAtIndexedSubscript:"
- "outNodePlacement"
- "preferenceValueOfClass:forKey:"
- "prefix"
- "setPreferenceValue:forKey:"
- "string"
- "substringWithRange:"
- "timeIntervalSince1970"
- "updateCallback(observer:%p)\n"
- "v48@0:8@16@24@32@40"
- "writeToFile:atomically:"

```
