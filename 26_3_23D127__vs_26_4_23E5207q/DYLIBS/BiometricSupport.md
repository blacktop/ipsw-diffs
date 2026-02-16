## BiometricSupport

> `/System/Library/PrivateFrameworks/BiometricSupport.framework/BiometricSupport`

```diff

-545.40.2.0.0
-  __TEXT.__text: 0x59d04
-  __TEXT.__auth_stubs: 0x1020
-  __TEXT.__objc_methlist: 0x288c
-  __TEXT.__const: 0x1294
-  __TEXT.__cstring: 0x688f
-  __TEXT.__oslogstring: 0x3695
-  __TEXT.__gcc_except_tab: 0x1328
-  __TEXT.__unwind_info: 0x1068
-  __TEXT.__objc_classname: 0x33f
-  __TEXT.__objc_methname: 0x6c43
+545.100.10.0.0
+  __TEXT.__text: 0x517c8
+  __TEXT.__auth_stubs: 0xfc0
+  __TEXT.__objc_methlist: 0x2914
+  __TEXT.__const: 0x130c
+  __TEXT.__cstring: 0x7181
+  __TEXT.__oslogstring: 0x3715
+  __TEXT.__gcc_except_tab: 0x12c8
+  __TEXT.__unwind_info: 0x11a0
+  __TEXT.__objc_classname: 0x35f
+  __TEXT.__objc_methname: 0x6d55
   __TEXT.__objc_methtype: 0x1594
-  __TEXT.__objc_stubs: 0x4d60
-  __DATA_CONST.__got: 0x320
-  __DATA_CONST.__const: 0x1a68
-  __DATA_CONST.__objc_classlist: 0xe0
+  __TEXT.__objc_stubs: 0x4e40
+  __DATA_CONST.__got: 0x330
+  __DATA_CONST.__const: 0x1a98
+  __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b50
+  __DATA_CONST.__objc_selrefs: 0x1b98
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x820
+  __AUTH_CONST.__auth_got: 0x7f0
   __AUTH_CONST.__const: 0x1b0
-  __AUTH_CONST.__cfstring: 0x2060
-  __AUTH_CONST.__objc_const: 0x3e50
+  __AUTH_CONST.__cfstring: 0x20c0
+  __AUTH_CONST.__objc_const: 0x3f48
   __AUTH_CONST.__objc_intobj: 0xcd8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x284
-  __DATA.__data: 0xbc8
+  __DATA.__objc_ivar: 0x288
+  __DATA.__data: 0xbd0
   __DATA.__common: 0x28
   __DATA.__bss: 0x61
-  __DATA_DIRTY.__objc_data: 0x730
+  __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__common: 0x30
-  __DATA_DIRTY.__bss: 0x70
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 40A3F931-D4C0-3E78-9877-C5E0A2820982
-  Functions: 1926
-  Symbols:   5982
-  CStrings:  2873
+  UUID: 495C7653-39A9-3DB1-9ED8-BFA822078714
+  Functions: 1974
+  Symbols:   6115
+  CStrings:  2922
 
Symbols:
+ +[BiometricKitCoreAnalyticsLogger sharedInstance]
+ -[BiometricKitCoreAnalyticsLogger analyticsOSLogNSDictionary:forEvent:toLogPath:withPrefix:]
+ -[BiometricKitCoreAnalyticsLogger analyticsOSLogNSDictionary:forEvent:toLogPath:withPrefix:].cold.1
+ -[BiometricKitCoreAnalyticsLogger analyticsOSLogNSDictionary:forEvent:toLogPath:withPrefix:].cold.2
+ -[BiometricKitCoreAnalyticsLogger analyticsSaveToFile]
+ -[BiometricKitCoreAnalyticsLogger init]
+ -[BiometricKitCoreAnalyticsLogger init].cold.1
+ -[BiometricKitCoreAnalyticsLogger setAnalyticsSaveToFile:]
+ -[BiometricKitCoreAnalyticsLogger updateDefaults]
+ -[BiometricKitXPCExportedObject removeAllPreferencesWithClient:replyBlock:]
+ -[BiometricKitXPCExportedObject removeAllPreferencesWithClient:replyBlock:].cold.1
+ -[BiometricKitXPCExportedObject removeAllPreferencesWithClient:replyBlock:].cold.2
+ -[BiometricKitXPCServer doSharedMemoryTransfers].cold.3
+ -[BiometricKitXPCServer removeAllPreferencesWithClient:]
+ GCC_except_table136
+ GCC_except_table155
+ GCC_except_table158
+ GCC_except_table161
+ GCC_except_table230
+ GCC_except_table244
+ GCC_except_table249
+ GCC_except_table305
+ GCC_except_table526
+ GCC_except_table529
+ _NSFileOwnerAccountName
+ _NSFileProtectionNone
+ _OBJC_CLASS_$_BiometricKitCoreAnalyticsLogger
+ _OBJC_IVAR_$_BiometricKitCoreAnalyticsLogger._analyticsSaveToFile
+ _OBJC_METACLASS_$_BiometricKitCoreAnalyticsLogger
+ _OUTLINED_FUNCTION_76
+ _OUTLINED_FUNCTION_77
+ _OUTLINED_FUNCTION_78
+ _OUTLINED_FUNCTION_79
+ _OUTLINED_FUNCTION_80
+ _OUTLINED_FUNCTION_81
+ _OUTLINED_FUNCTION_82
+ _OUTLINED_FUNCTION_83
+ _OUTLINED_FUNCTION_84
+ _OUTLINED_FUNCTION_85
+ _OUTLINED_FUNCTION_86
+ _OUTLINED_FUNCTION_87
+ _OUTLINED_FUNCTION_88
+ _OUTLINED_FUNCTION_89
+ __OBJC_$_CLASS_METHODS_BiometricKitCoreAnalyticsLogger
+ __OBJC_$_INSTANCE_METHODS_BiometricKitCoreAnalyticsLogger
+ __OBJC_$_INSTANCE_VARIABLES_BiometricKitCoreAnalyticsLogger
+ __OBJC_$_PROP_LIST_BiometricKitCoreAnalyticsLogger
+ __OBJC_CLASS_RO_$_BiometricKitCoreAnalyticsLogger
+ __OBJC_METACLASS_RO_$_BiometricKitCoreAnalyticsLogger
+ ___39-[BiometricKitCoreAnalyticsLogger init]_block_invoke
+ ___49+[BiometricKitCoreAnalyticsLogger sharedInstance]_block_invoke
+ ___60-[BiometricKitXPCServer listener:shouldAcceptNewConnection:]_block_invoke.608
+ ___92-[BiometricKitCoreAnalyticsLogger analyticsOSLogNSDictionary:forEvent:toLogPath:withPrefix:]_block_invoke
+ ___92-[BiometricKitCoreAnalyticsLogger analyticsOSLogNSDictionary:forEvent:toLogPath:withPrefix:]_block_invoke.cold.1
+ ___92-[BiometricKitCoreAnalyticsLogger analyticsOSLogNSDictionary:forEvent:toLogPath:withPrefix:]_block_invoke.cold.2
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e5_v8?0ls32l8s40l8r72l8s48l8s56l8s64l8
+ ___block_descriptor_tmp.181
+ ___block_literal_global.183
+ ___der_key_keybag_type
+ _akstest_new_ekwk.cold.1
+ _akstest_new_key.cold.1
+ _akstest_unwrap_ek.cold.1
+ _akstest_unwrap_key.cold.1
+ _der_key_keybag_type
+ _kBiometricKitCASaveToFile
+ _objc_msgSend$appendString:
+ _objc_msgSend$description
+ _objc_msgSend$getParagraphStart:end:contentsEnd:forRange:
+ _objc_msgSend$registerUpdateNotification:
+ _objc_msgSend$removeAllPreferences
+ _objc_msgSend$removeAllPreferencesWithClient:
+ _objc_msgSend$removeLegacyPreferences
+ _objc_msgSend$updateDefaults
+ _sharedInstance.logger
+ _sharedInstance.onceToken
- GCC_except_table135
- GCC_except_table154
- GCC_except_table160
- GCC_except_table229
- GCC_except_table243
- GCC_except_table248
- GCC_except_table304
- GCC_except_table525
- GCC_except_table528
- _OBJC_CLASS_$_BiometricSupportTools
- ___60-[BiometricKitXPCServer listener:shouldAcceptNewConnection:]_block_invoke.606
- ___block_descriptor_tmp.170
- ___block_literal_global.172
- _copy_raw_secret
- _fv_init_cred_from_secret
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$analyticsOSLogNSDictionary:forEvent:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "%@/%d_%@.plist"
+ "%@: sendEvent: %@ (print %ld of %ld): \n%@\n"
+ "%@: write event: %@ to file: %@\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestCheckClass failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestLastUser failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEKWK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewKey failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestRewrapEK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapEK failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapKey failed with 0x%x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 1)%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 3)%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s unpack data failed%s\n"
+ "([[NSFileManager defaultManager] createDirectoryAtPath:path withIntermediateDirectories:__objc_no attributes:@{ NSFileOwnerAccountName: @\"mobile\", NSFileProtectionKey: NSFileProtectionNone } error:((void*)0)])"
+ "-[BiometricKitXPCExportedObject removeAllPreferencesWithClient:replyBlock:]"
+ "/Library/Caches/com.apple.xbs/6204B476-D773-4B94-9699-B5D40A8526DA/TemporaryDirectory.GU0JV2/Sources/BiometricSupport/BiometricSupport/Analytics/BiometricKitCoreAnalyticsEvent.m"
+ "/Library/Caches/com.apple.xbs/6204B476-D773-4B94-9699-B5D40A8526DA/TemporaryDirectory.GU0JV2/Sources/BiometricSupport/BiometricSupport/Analytics/BiometricKitCoreAnalyticsLockState.m"
+ "/Library/Caches/com.apple.xbs/6204B476-D773-4B94-9699-B5D40A8526DA/TemporaryDirectory.GU0JV2/Sources/BiometricSupport/BiometricSupport/Analytics/BiometricKitCoreAnalyticsLogger.m"
+ "/Library/Caches/com.apple.xbs/6204B476-D773-4B94-9699-B5D40A8526DA/TemporaryDirectory.GU0JV2/Sources/BiometricSupport/BiometricSupport/BKCatacomb.m"
+ "/Library/Caches/com.apple.xbs/6204B476-D773-4B94-9699-B5D40A8526DA/TemporaryDirectory.GU0JV2/Sources/BiometricSupport/BiometricSupport/BiometricAutoBugCapture.m"
+ "/Library/Caches/com.apple.xbs/6204B476-D773-4B94-9699-B5D40A8526DA/TemporaryDirectory.GU0JV2/Sources/BiometricSupport/BiometricSupport/BiometricSupportUserNotification.m"
+ "/Library/Caches/com.apple.xbs/6204B476-D773-4B94-9699-B5D40A8526DA/TemporaryDirectory.GU0JV2/Sources/BiometricSupport/BiometricSupport/biometrickitd/BiometricKitXPCExportedObject.m"
+ "/Library/Caches/com.apple.xbs/6204B476-D773-4B94-9699-B5D40A8526DA/TemporaryDirectory.GU0JV2/Sources/BiometricSupport/BiometricSupport/biometrickitd/BiometricKitXPCServer.m"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/backup_serialize.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "/Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/shared_crypto.c"
+ "BiometricKitCoreAnalyticsLogger"
+ "PearlAWD"
+ "TB,V_analyticsSaveToFile"
+ "[dict writeToFile:filePath atomically:__objc_yes]"
+ "_analyticsSaveToFile"
+ "akstest_check_class"
+ "akstest_last_user"
+ "akstest_new_ek"
+ "akstest_new_ekwk"
+ "akstest_new_key"
+ "akstest_rewrap_ek"
+ "akstest_unwrap_ek"
+ "akstest_unwrap_key"
+ "analyticsDispatchQueue"
+ "analyticsSaveToFile"
+ "appendString:"
+ "com.apple.biometrickit.analyticsFileLog"
+ "getParagraphStart:end:contentsEnd:forRange:"
+ "prefix"
+ "registerUpdateNotification:"
+ "removeAllPreferences"
+ "removeAllPreferences\n"
+ "removeAllPreferences -> void\n"
+ "removeAllPreferencesWithClient:"
+ "removeAllPreferencesWithClient:replyBlock:"
+ "removeLegacyPreferences"
+ "self = [super init]"
+ "setAnalyticsSaveToFile:"
+ "updateDefaults"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"
- "/Library/Caches/com.apple.xbs/Sources/BiometricSupport/BiometricSupport/Analytics/BiometricKitCoreAnalyticsEvent.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricSupport/BiometricSupport/Analytics/BiometricKitCoreAnalyticsLockState.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricSupport/BiometricSupport/BKCatacomb.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricSupport/BiometricSupport/BiometricAutoBugCapture.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricSupport/BiometricSupport/BiometricSupportUserNotification.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricSupport/BiometricSupport/biometrickitd/BiometricKitXPCExportedObject.m"
- "/Library/Caches/com.apple.xbs/Sources/BiometricSupport/BiometricSupport/biometrickitd/BiometricKitXPCServer.m"
- "analyticsOSLogNSDictionary:forEvent:"

```
