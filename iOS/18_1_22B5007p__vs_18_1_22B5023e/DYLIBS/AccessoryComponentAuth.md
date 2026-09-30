## AccessoryComponentAuth

> `/System/Library/PrivateFrameworks/AccessoryComponentAuth.framework/AccessoryComponentAuth`

```diff

-1008.0.0.502.1
-  __TEXT.__text: 0xf88c
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0x1b4
+1025.0.0.0.0
+  __TEXT.__text: 0x10474
+  __TEXT.__auth_stubs: 0x740
+  __TEXT.__objc_methlist: 0x1c4
   __TEXT.__const: 0x68d8
-  __TEXT.__cstring: 0x967
-  __TEXT.__oslogstring: 0xf51
-  __TEXT.__unwind_info: 0x368
+  __TEXT.__cstring: 0xa34
+  __TEXT.__oslogstring: 0xf77
+  __TEXT.__unwind_info: 0x370
   __TEXT.__objc_classname: 0x5f
-  __TEXT.__objc_methname: 0x6c6
-  __TEXT.__objc_methtype: 0x1e9
-  __TEXT.__objc_stubs: 0x660
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0xd88
+  __TEXT.__objc_methname: 0x7a1
+  __TEXT.__objc_methtype: 0x206
+  __TEXT.__objc_stubs: 0x760
+  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__const: 0xdb8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c0
-  __AUTH_CONST.__auth_got: 0x398
+  __DATA_CONST.__objc_selrefs: 0x200
+  __AUTH_CONST.__auth_got: 0x3a8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x648
-  __AUTH_CONST.__cfstring: 0x5e0
+  __AUTH_CONST.__cfstring: 0x760
   __AUTH_CONST.__objc_const: 0x390
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xa0

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
-  Functions: 311
-  Symbols:   830
-  CStrings:  304
+  Functions: 320
+  Symbols:   845
+  CStrings:  329
 
Symbols:
+ _AnalyticsSendEvent
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_NSString
+ _acc_analytics_createBucketizeBatteryPackConnectionDuration
+ _acc_analytics_createBucketizePowerSourceChargingTime
+ _acc_analytics_createBucketizedAnalyticEventDuration
+ _acc_analytics_createBucketizedBatteryChargeDelta
+ _acc_analytics_createBucketizedBatteryChargeLevel
+ _acc_analytics_createBucketizedInductiveAuthDuration
+ _acc_analytics_createBucketizedUnlockDialogAnalyticEventTime
+ _acc_analytics_createBucketizedWiredAuthDuration
+ _objc_retain_x25
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
+ "setObject:forKey:"
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
