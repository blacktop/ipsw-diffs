## AppleMobileFileIntegrity

> `/System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/Versions/A/AppleMobileFileIntegrity`

```diff

-938.81.1.0.0
-  __TEXT.__text: 0x102f8
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x4e8
+938.101.1.0.0
+  __TEXT.__text: 0x10d84
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_methlist: 0x5c4
   __TEXT.__const: 0x210
-  __TEXT.__cstring: 0x1c56
-  __TEXT.__oslogstring: 0x13ff
+  __TEXT.__cstring: 0x1cf6
+  __TEXT.__oslogstring: 0x145f
   __TEXT.__gcc_except_tab: 0x288
-  __TEXT.__unwind_info: 0x400
-  __TEXT.__objc_classname: 0x96
-  __TEXT.__objc_methname: 0x12cc
-  __TEXT.__objc_methtype: 0x451
-  __TEXT.__objc_stubs: 0xe40
-  __DATA_CONST.__got: 0x208
+  __TEXT.__unwind_info: 0x418
+  __TEXT.__objc_classname: 0xa8
+  __TEXT.__objc_methname: 0x13c1
+  __TEXT.__objc_methtype: 0x46e
+  __TEXT.__objc_stubs: 0xf40
+  __DATA_CONST.__got: 0x220
   __DATA_CONST.__const: 0x650
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x460
+  __DATA_CONST.__objc_selrefs: 0x4a0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x338
-  __AUTH_CONST.__const: 0x620
-  __AUTH_CONST.__cfstring: 0x720
-  __AUTH_CONST.__objc_const: 0xda8
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0xbc
+  __AUTH_CONST.__auth_got: 0x370
+  __AUTH_CONST.__const: 0x6a0
+  __AUTH_CONST.__cfstring: 0x820
+  __AUTH_CONST.__objc_const: 0xd28
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0xc0
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/ConfigProfileHelper.framework/Versions/A/ConfigProfileHelper
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 90625AE8-01B2-3B79-9E84-F4A9286DB7A3
-  Functions: 368
-  Symbols:   837
-  CStrings:  647
+  UUID: 1E80220F-9D99-3FF9-A59F-EAC3A5FCD54A
+  Functions: 375
+  Symbols:   876
+  CStrings:  678
 
Symbols:
+ +[AMFIFMKLog generic].cold.1
+ +[ValidationMetrics dispatchMetrics:]
+ +[ValidationMetrics dispatchMetrics:].cold.1
+ +[ValidationMetrics dispatchMetrics:].cold.2
+ +[ValidationMetrics sendSHA1CodeDirectoryMetricWithFilename:withSigningID:withCDHash:withTeamID:withBundleID:withVersion:withIsApple:]
+ -[AMFIPathValidator_ios profileID]
+ -[AMFIPathValidator_macos sendMetrics]
+ OBJC_IVAR_$_AMFIPathValidator_ios._profileID
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_ValidationMetrics
+ _OBJC_METACLASS_$_ValidationMetrics
+ __OBJC_$_CLASS_METHODS_ValidationMetrics
+ __OBJC_CLASS_RO_$_ValidationMetrics
+ __OBJC_METACLASS_RO_$_ValidationMetrics
+ ___134+[ValidationMetrics sendSHA1CodeDirectoryMetricWithFilename:withSigningID:withCDHash:withTeamID:withBundleID:withVersion:withIsApple:]_block_invoke
+ ___37+[ValidationMetrics dispatchMetrics:]_block_invoke
+ ___37+[ValidationMetrics dispatchMetrics:]_block_invoke_2
+ ___38-[AMFIPathValidator_macos sendMetrics]_block_invoke
+ ___block_descriptor_40_e8_32bs_e5_v8?0l
+ ___block_descriptor_81_e8_32s40s48s56s64s72s_e19_"NSDictionary"8?0l
+ ___copy_helper_block_e8_32s40s48s56s64s72s
+ ___destroy_helper_block_e8_32s40s48s56s64s72s
+ _dispatch_async
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _kCFBundleIdentifierKey
+ _kCFBundleVersionKey
+ _kSecCodeInfoDigestAlgorithm
+ _objc_msgSend$dispatchMetrics:
+ _objc_msgSend$infoPlist
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$null
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$sendMetrics
+ _objc_msgSend$sendSHA1CodeDirectoryMetricWithFilename:withSigningID:withCDHash:withTeamID:withBundleID:withVersion:withIsApple:
+ _objc_msgSend$stringWithString:
+ dispatchMetrics:._metricsQueue
+ dispatchMetrics:._metricsSemaphore
+ dispatchMetrics:.onceToken
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _copyCodeSigningInfo
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "Dropping validation metrics because queue is full"
+ "Reporting metrics for SHA1 signed software %@"
+ "T@\"NSDictionary\",R,V_infoPlist"
+ "T@\"NSString\",R,N"
+ "ValidationMetrics"
+ "_profileID"
+ "amfid.validation.metrics"
+ "bundle_identifier"
+ "com.apple.sha1.code_directory.usage"
+ "dispatchMetrics:"
+ "filename"
+ "is_apple"
+ "lastPathComponent"
+ "null"
+ "objectForKeyedSubscript:"
+ "profileID"
+ "sendMetrics"
+ "sendSHA1CodeDirectoryMetricWithFilename:withSigningID:withCDHash:withTeamID:withBundleID:withVersion:withIsApple:"
+ "signing_identifier"
+ "stringWithString:"
+ "team_identifier"
+ "v68@0:8@16@24@32@40@48@56B64"
+ "version"
- "T@\"NSDictionary\",R,N,V_infoPlist"

```
