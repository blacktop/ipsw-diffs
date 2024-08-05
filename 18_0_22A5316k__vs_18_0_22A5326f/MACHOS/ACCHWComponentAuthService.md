## ACCHWComponentAuthService

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCHWComponentAuthService.xpc/ACCHWComponentAuthService`

```diff

-1008.0.0.502.1
-  __TEXT.__text: 0xf814
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_stubs: 0x880
-  __TEXT.__objc_methlist: 0x214
-  __TEXT.__const: 0x6888
-  __TEXT.__cstring: 0x10cc
+1017.0.0.0.0
+  __TEXT.__text: 0x103fc
+  __TEXT.__auth_stubs: 0x790
+  __TEXT.__objc_stubs: 0x960
+  __TEXT.__objc_methlist: 0x224
+  __TEXT.__const: 0x6890
+  __TEXT.__cstring: 0x1199
   __TEXT.__objc_classname: 0x9e
-  __TEXT.__objc_methname: 0x978
-  __TEXT.__objc_methtype: 0x2c2
-  __TEXT.__oslogstring: 0xe67
-  __TEXT.__unwind_info: 0x378
-  __DATA_CONST.__auth_got: 0x3c0
-  __DATA_CONST.__got: 0xc0
+  __TEXT.__objc_methname: 0xa41
+  __TEXT.__objc_methtype: 0x2df
+  __TEXT.__oslogstring: 0xe8d
+  __TEXT.__unwind_info: 0x380
+  __DATA_CONST.__auth_got: 0x3d0
+  __DATA_CONST.__got: 0xd8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1860
-  __DATA_CONST.__cfstring: 0x1020
+  __DATA_CONST.__const: 0x1890
+  __DATA_CONST.__cfstring: 0x11a0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x8f0
-  __DATA.__objc_selrefs: 0x270
+  __DATA.__objc_selrefs: 0x2a8
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x1b0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /usr/lib/libFDR.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 328
-  Symbols:   2120
-  CStrings:  442
+  Functions: 337
+  Symbols:   2186
+  CStrings:  466
 
Symbols:
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:]
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:]
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.1
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.10
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.10
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.11
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.12
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.13
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.14
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.14
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.15
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.16
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.16
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.17
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.18
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.19
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.2
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.20
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.3
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.4
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.5
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.6
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.7
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.8
+ -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:].cold.9
+ -[ACCHWComponentAuthService _logToAnalytics:authError:fdrValidationStatus:authDurationInMS:]
+ -[ACCHWComponentAuthService _logToAnalytics:authError:fdrValidationStatus:authDurationInMS:]
+ -[ACCHWComponentAuthService _logToAnalytics:authError:fdrValidationStatus:authDurationInMS:].cold.1
+ -[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]
+ -[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]
+ /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/ACCHWComponentAuthService.build/Objects-normal/arm64e/acc_analytics_utilities.o
+ _AnalyticsSendEvent
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_NSString
+ __138-[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke.cold.1
+ ___128-[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke
+ ___128-[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke
+ ___128-[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke_2
+ ___128-[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke_2
+ ___138-[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke
+ ___138-[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke
+ ___block_descriptor_59_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_59_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ __block_literal_global.103
+ __block_literal_global.103
+ __block_literal_global.106
+ __block_literal_global.106
+ __block_literal_global.109
+ __block_literal_global.109
+ _acc_analytics_createBucketizeBatteryPackConnectionDuration
+ _acc_analytics_createBucketizeBatteryPackConnectionDuration
+ _acc_analytics_createBucketizePowerSourceChargingTime
+ _acc_analytics_createBucketizePowerSourceChargingTime
+ _acc_analytics_createBucketizedAnalyticEventDuration
+ _acc_analytics_createBucketizedAnalyticEventDuration
+ _acc_analytics_createBucketizedBatteryChargeDelta
+ _acc_analytics_createBucketizedBatteryChargeDelta
+ _acc_analytics_createBucketizedBatteryChargeLevel
+ _acc_analytics_createBucketizedBatteryChargeLevel
+ _acc_analytics_createBucketizedInductiveAuthDuration
+ _acc_analytics_createBucketizedInductiveAuthDuration
+ _acc_analytics_createBucketizedUnlockDialogAnalyticEventTime
+ _acc_analytics_createBucketizedUnlockDialogAnalyticEventTime
+ _acc_analytics_createBucketizedWiredAuthDuration
+ _acc_analytics_createBucketizedWiredAuthDuration
+ _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:.disableAuth
+ _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:.disableAuth
+ _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:.onceToken
+ _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:.onceToken
+ _kACCHWComponentAuthServiceFDRStatus_Strings
+ _kACCHWComponentAuthServiceFDRStatus_Strings
+ _kACCHWComponentAuthServiceInternalModule_Strings
+ _kACCHWComponentAuthServiceInternalModule_Strings
+ _objc_msgSend$_authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:
+ _objc_msgSend$_logToAnalytics:authError:fdrValidationStatus:authDurationInMS:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$processInfo
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$systemUptime
+ _objc_retain_x25
+ acc_analytics_utilities.c
+ authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:.onceToken
+ authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:.onceToken
+ authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:.veridianQueue
+ authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:.veridianQueue
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:]
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:]
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.1
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.10
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.10
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.11
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.12
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.13
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.14
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.14
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.15
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.16
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.16
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.17
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.18
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.19
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.2
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.20
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.3
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.4
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.5
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.6
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.7
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.8
- -[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:].cold.9
- -[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:]
- -[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:]
- __123-[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:]_block_invoke.cold.1
- ___113-[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:]_block_invoke
- ___113-[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:]_block_invoke
- ___113-[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:]_block_invoke_2
- ___113-[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:]_block_invoke_2
- ___123-[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:]_block_invoke
- ___123-[ACCHWComponentAuthService _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:]_block_invoke
- ___block_descriptor_58_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_58_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- __block_literal_global.54
- __block_literal_global.54
- __block_literal_global.57
- __block_literal_global.57
- __block_literal_global.60
- __block_literal_global.60
- _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:.disableAuth
- _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:.disableAuth
- _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:.onceToken
- _authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:.onceToken
- _objc_msgSend$_authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:
- authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:.onceToken
- authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:.onceToken
- authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:.veridianQueue
- authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:.veridianQueue
CStrings:
+ "CoreAnalytics event: %!@(MISSING)\neventDict: %!@(MISSING)"
+ "FDRStatus"
+ "FDRStatusFail"
+ "FDRStatusPass"
+ "FDRStatusUnknown"
+ "Failed"
+ "Passed"
+ "Uptime"
+ "Veridian"
+ "_authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:logToAnalytics:"
+ "_logToAnalytics:authError:fdrValidationStatus:authDurationInMS:"
+ "authState"
+ "authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:"
+ "com.apple.accessories.authCPEvent"
+ "dictionaryWithDictionary:"
+ "internalModuleType"
+ "isBatteryModule"
+ "isInductive"
+ "isPeriodic"
+ "numberWithBool:"
+ "numberWithDouble:"
+ "processInfo"
+ "stringWithUTF8String:"
+ "systemUptime"
+ "v36@0:8i16i20i24Q28"
+ "v44@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24B32B36B40"
+ "v44@0:8@16@?24B32B36B40"
+ "v48@0:8@16@?24i32B36B40B44"
+ "wiredAuthDuration"
- "_authenticateModuleWithChallenge:completionHandler:moduleType:updateRegistry:updateUIProperty:"
- "authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:"
- "v40@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24B32B36"
- "v40@0:8@16@?24B32B36"
- "v44@0:8@16@?24i32B36B40"

```
