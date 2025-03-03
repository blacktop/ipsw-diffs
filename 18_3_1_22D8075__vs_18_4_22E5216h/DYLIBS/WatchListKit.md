## WatchListKit

> `/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit`

```diff

-850.30.4.0.0
-  __TEXT.__text: 0x65bac
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x670c
+850.40.38.0.0
+  __TEXT.__text: 0x65a7c
+  __TEXT.__auth_stubs: 0x850
+  __TEXT.__objc_methlist: 0x6e8c
   __TEXT.__const: 0x1ac
-  __TEXT.__cstring: 0x7892
-  __TEXT.__oslogstring: 0x60b2
-  __TEXT.__gcc_except_tab: 0x11a0
+  __TEXT.__cstring: 0x7989
+  __TEXT.__oslogstring: 0x6094
+  __TEXT.__gcc_except_tab: 0x11d0
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x1cf8
-  __TEXT.__objc_classname: 0x1331
-  __TEXT.__objc_methname: 0xfd7a
-  __TEXT.__objc_methtype: 0x1c74
-  __TEXT.__objc_stubs: 0x9ae0
+  __TEXT.__unwind_info: 0x1e00
+  __TEXT.__objc_classname: 0x1320
+  __TEXT.__objc_methname: 0xfdc9
+  __TEXT.__objc_methtype: 0x1c1e
+  __TEXT.__objc_stubs: 0x9b60
   __DATA_CONST.__got: 0x8d8
-  __DATA_CONST.__const: 0x2630
-  __DATA_CONST.__objc_classlist: 0x568
+  __DATA_CONST.__const: 0x2780
+  __DATA_CONST.__objc_classlist: 0x560
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3610
+  __DATA_CONST.__objc_selrefs: 0x3820
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x4b8
+  __DATA_CONST.__objc_superrefs: 0x4b0
   __DATA_CONST.__objc_arraydata: 0x620
-  __AUTH_CONST.__auth_got: 0x468
-  __AUTH_CONST.__const: 0xe60
-  __AUTH_CONST.__cfstring: 0xa000
-  __AUTH_CONST.__objc_const: 0x12820
+  __AUTH_CONST.__auth_got: 0x438
+  __AUTH_CONST.__const: 0xe80
+  __AUTH_CONST.__cfstring: 0xa0a0
+  __AUTH_CONST.__objc_const: 0x119c8
   __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x78

   __DATA.__objc_ivar: 0xa14
   __DATA.__data: 0x7a0
   __DATA.__bss: 0x110
-  __DATA_DIRTY.__objc_data: 0x3520
+  __DATA_DIRTY.__objc_data: 0x34d0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x448
   __DATA_DIRTY.__common: 0x8

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
-  - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2632
-  Symbols:   3637
-  CStrings:  5092
+  Functions: 2712
+  Symbols:   3718
+  CStrings:  5099
 
Symbols:
+ _TVAppExtensionBundleID
+ _TVProductPageExtensionBundleID
+ __WLKUserEnvironmentPlatformCompanion
+ __WLKUserEnvironmentPlatformPadExtension
+ __WLKUserEnvironmentPlatformPhoneExtension
- _OBJC_CLASS_$_WLKMetricsActivity
- _OBJC_METACLASS_$_WLKMetricsActivity
- _nw_activity_activate
- _nw_activity_complete_with_reason
- _nw_activity_complete_with_reason_and_underlying_error
- _nw_activity_create
- _nw_activity_is_activated
- _nw_activity_is_complete
CStrings:
+ "\x04\x11\x12\x12\x14"
+ "@\"AMSURLResult\""
+ "@32@0:8q16@24"
+ "A"
+ "T@\"AMSURLResult\",&,N,V_amsUrlResponse"
+ "T@\"NSNumber\",&,N,V_networkLabel"
+ "T@\"NSObject<OS_nw_activity>\",&,N,V_networkActivity"
+ "T@\"NSSet\",R,N"
+ "WLKConfigurationRequest - Configuration request is completed"
+ "WLKNetworkRequestOperation - Request status: %lu elapsed time: %.5f id: %@ ck:%@ url: %@ %@ %@ %f"
+ "_amsUrlResponse"
+ "_createAMSEncoder:account:"
+ "_executeRequest"
+ "_networkActivity"
+ "_networkLabel"
+ "_prepareEncoder:account:sessionConfiguration:options:completionHandler:"
+ "amsUrlResponse"
+ "com.apple.VideosUI.TVAppExtension"
+ "com.apple.VideosUI.TVProductPageExtension"
+ "iPad-extension"
+ "iPhone-extension"
+ "isRunningInTVAppExtension"
+ "isRunningInTVExtension"
+ "li"
+ "networkActivity"
+ "networkLabel"
+ "resultWithCompletion:"
+ "setAmsUrlResponse:"
+ "setNetworkActivity:"
+ "setNetworkLabel:"
+ "signNetworkRequest:completionHandler:"
+ "signaturePromiseFromData:type:bag:"
+ "staticLanguageCodes"
+ "taskInterval"
+ "tvExtensionBundleIDs"
+ "v24@?0@\"AMSURLRequest\"8@\"NSError\"16"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v32@?0@\"AMSURLRequestEncoder\"8@\"NSURLRequest\"16@\"NSError\"24"
+ "vision-companion"
- "\x02\x12\x11\x12\x14"
- "@\"WLKMetricsActivity\""
- "@20@0:8I16"
- "@40@0:8@16q24@32"
- "@56@0:8@16@24@32q40^@48"
- "B32@0:8@16^@24"
- "T@\"NSObject<OS_nw_activity>\",R,V_activity"
- "T@\"WLKMetricsActivity\",&,N,V_nwactivity"
- "TI,R,V_label"
- "WLKMetricsActivity"
- "WLKMetricsActivity - activity already completed."
- "WLKMetricsActivity - activity not activated."
- "WLKNetworkRequestOperation - Request status: %lu elapsed time: %.5f id: %@ ck:%@ url: %@ %@ %@"
- "_activity"
- "_label"
- "_nwactivity"
- "_prepareEncoder:account:sessionConfiguration:options:error:"
- "activity"
- "dataTaskPromiseWithRequest:activity:"
- "dataTaskWithRequest:completionHandler:"
- "finish:"
- "initWithLabel:"
- "initWithURLRequest:options:activity:"
- "label"
- "li-CG"
- "nwactivity"
- "resultWithError:"
- "setNwactivity:"
- "signNetworkRequest:error:"
- "signatureFromData:type:bag:error:"
- "startNetworkRequest:account:sessionConfiguration:options:activity:completion:"
- "v64@0:8@16@24@32q40@48@?56"

```
