## feedbackd

> `/usr/libexec/feedbackd`

```diff

-118.0.0.0.0
-  __TEXT.__text: 0x52b24
-  __TEXT.__auth_stubs: 0x17d0
-  __TEXT.__objc_methlist: 0x1ac
-  __TEXT.__const: 0x1490
-  __TEXT.__cstring: 0x22a1
-  __TEXT.__objc_methname: 0x11a1
-  __TEXT.__swift5_typeref: 0xaac
-  __TEXT.__swift5_capture: 0x408
-  __TEXT.__constg_swiftt: 0x9cc
-  __TEXT.__swift5_reflstr: 0x9de
-  __TEXT.__swift5_fieldmd: 0x788
-  __TEXT.__oslogstring: 0x18b8
-  __TEXT.__swift5_builtin: 0x64
+120.0.0.0.0
+  __TEXT.__text: 0x575b4
+  __TEXT.__auth_stubs: 0x18b0
+  __TEXT.__objc_methlist: 0x1bc
+  __TEXT.__const: 0x14c0
+  __TEXT.__cstring: 0x2491
+  __TEXT.__objc_methname: 0x11e9
+  __TEXT.__swift5_typeref: 0xb6e
+  __TEXT.__swift5_capture: 0x4b4
+  __TEXT.__constg_swiftt: 0xa34
+  __TEXT.__swift5_reflstr: 0xa4e
+  __TEXT.__swift5_fieldmd: 0x7e4
+  __TEXT.__oslogstring: 0x19d8
+  __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_assocty: 0x120
   __TEXT.__swift5_proto: 0xec
-  __TEXT.__swift5_types: 0x80
+  __TEXT.__swift5_types: 0x88
   __TEXT.__objc_classname: 0x72
   __TEXT.__objc_methtype: 0x28b
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_entry: 0x8
   __TEXT.__info_plist: 0x3b9
-  __TEXT.__unwind_info: 0xfb8
-  __TEXT.__eh_frame: 0x2778
-  __DATA_CONST.__auth_got: 0xbe8
-  __DATA_CONST.__got: 0x5c0
-  __DATA_CONST.__auth_ptr: 0x3d0
-  __DATA_CONST.__const: 0x14a8
+  __TEXT.__unwind_info: 0x1088
+  __TEXT.__eh_frame: 0x2958
+  __DATA_CONST.__auth_got: 0xc58
+  __DATA_CONST.__got: 0x600
+  __DATA_CONST.__auth_ptr: 0x3e8
+  __DATA_CONST.__const: 0x16a0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA.__objc_const: 0x1a58
-  __DATA.__objc_selrefs: 0x4d8
-  __DATA.__objc_data: 0x7b0
-  __DATA.__data: 0x1720
+  __DATA.__objc_const: 0x1aa0
+  __DATA.__objc_selrefs: 0x4f0
+  __DATA.__objc_data: 0x7f8
+  __DATA.__data: 0x1820
   __DATA.__bss: 0x1d90
   __DATA.__common: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/UserNotifications.framework/Versions/A/UserNotifications
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/Versions/A/BackgroundSystemTasks

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1095
-  Symbols:   666
-  CStrings:  238
+  Functions: 1172
+  Symbols:   689
+  CStrings:  248
 
Symbols:
+ _$s10Foundation3URLV15fileURLWithPathACSSh_tcfC
+ _$s10Foundation4UUIDV2eeoiySbAC_ACtFZ
+ _$s15FeedbackService15FBKSInteractionC7ContentO4htmlyAESScAEmFWC
+ _$s15FeedbackService7StringsV3XPCV011CentralizedA0V27remoteEvaluationEntitlementSSvgZ
+ _$s2os21OSAllocatedUnfairLockVMn
+ _$s6Darwin5noErrs5Int32Vvg
+ _$s8Dispatch0A12TimeIntervalO7secondsyACSicACmFWC
+ _$s8Dispatch0A12TimeIntervalOMa
+ _$s8Dispatch0A4TimeV3nowACyFZ
+ _$s8Dispatch0A4TimeVMa
+ _$s8Dispatch1poiyAA0A4TimeVAD_AA0aB8IntervalOtF
+ _$sBi32_WV
+ _$sS2cEycfC
+ _$sScEMa
+ _$sScEs5ErrorsMc
+ _$sSo17OS_dispatch_queueC8DispatchE10asyncAfter8deadline3qos5flags7executeyAC0D4TimeV_AC0D3QoSVAC0D13WorkItemFlagsVyyXBtF
+ _$sSo17OS_dispatch_queueC8DispatchE4mainABvgZ
+ _$ss13ManagedBufferCMn
+ _$ss5Int32VN
+ _$ss5Int32Vs23CustomStringConvertiblesWP
+ _$syycWV
+ _LSOpenFromURLSpec
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- _$s15FeedbackService7StringsV3XPCV27remoteEvaluationEntitlementSSvgZ
CStrings:
+ "/System/Library/PrivateFrameworks/FeedbackService.framework/Versions/A/Support/FeedbackRemoteView.app"
+ "Client not entitled to call remoteCheckin(endpointJSON:completion:)"
+ "Client not entitled to call remoteLaunch(completion:)"
+ "Failed to launch FeedbackRemoteView: OSStatus("
+ "HTML"
+ "No clients waiting for remote evaluation"
+ "remoteCheckin(endpointJSON:completion:)"
+ "remoteEvaluationRequestLock"
+ "remoteEvaluationRequestQueue"
+ "remoteLaunch(completion:)"
+ "v24@0:8@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">16"
+ "v32@0:8@\"NSXPCListenerEndpoint\"16@?<v@?@\"NSError\">24"
- "remoteEvaluate(request:completion:) not supported on this platform"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSError\">24"

```
