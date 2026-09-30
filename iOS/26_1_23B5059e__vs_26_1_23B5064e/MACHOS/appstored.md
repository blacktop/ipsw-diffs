## appstored

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Support/appstored`

```diff

-12.1.13.0.0
-  __TEXT.__text: 0x405cd4
-  __TEXT.__auth_stubs: 0x46a0
-  __TEXT.__objc_stubs: 0x133e0
-  __TEXT.__objc_methlist: 0xe3b0
+12.1.15.0.0
+  __TEXT.__text: 0x405ddc
+  __TEXT.__auth_stubs: 0x4680
+  __TEXT.__objc_stubs: 0x13420
+  __TEXT.__objc_methlist: 0xe3c8
   __TEXT.__dlopen_cstrs: 0x45e
   __TEXT.__const: 0x17e50
-  __TEXT.__cstring: 0x23eb6
-  __TEXT.__objc_methname: 0x1badf
+  __TEXT.__cstring: 0x23e20
+  __TEXT.__objc_methname: 0x1bbaa
   __TEXT.__constg_swiftt: 0x2794
   __TEXT.__swift5_typeref: 0x4250
   __TEXT.__swift5_fieldmd: 0x2930

   __TEXT.__swift5_assocty: 0x450
   __TEXT.__swift5_proto: 0x40c
   __TEXT.__swift5_types: 0x2c4
-  __TEXT.__objc_classname: 0x4250
-  __TEXT.__objc_methtype: 0x7d4b
+  __TEXT.__objc_classname: 0x423e
+  __TEXT.__objc_methtype: 0x7d85
   __TEXT.__swift5_capture: 0x27bc
-  __TEXT.__oslogstring: 0x39d8c
+  __TEXT.__oslogstring: 0x39d77
   __TEXT.__swift_as_entry: 0x490
   __TEXT.__swift_as_ret: 0x584
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_types2: 0x4
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__gcc_except_tab: 0xa6c8
-  __TEXT.__unwind_info: 0xb6a0
+  __TEXT.__gcc_except_tab: 0xa708
+  __TEXT.__unwind_info: 0xb6a8
   __TEXT.__eh_frame: 0xc3e4
-  __DATA_CONST.__auth_got: 0x2360
+  __DATA_CONST.__auth_got: 0x2350
   __DATA_CONST.__got: 0x1978
   __DATA_CONST.__auth_ptr: 0x9f0
-  __DATA_CONST.__const: 0x20248
+  __DATA_CONST.__const: 0x202a0
   __DATA_CONST.__cfstring: 0x1b820
-  __DATA_CONST.__objc_classlist: 0x1690
+  __DATA_CONST.__objc_classlist: 0x1688
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x558
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1a0
-  __DATA_CONST.__objc_superrefs: 0xdb0
-  __DATA_CONST.__objc_intobj: 0x1c50
+  __DATA_CONST.__objc_superrefs: 0xda8
+  __DATA_CONST.__objc_intobj: 0x1c98
   __DATA_CONST.__objc_arraydata: 0x890
   __DATA_CONST.__objc_arrayobj: 0x4b0
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x35e30
-  __DATA.__objc_selrefs: 0x66d8
-  __DATA.__objc_ivar: 0x2454
-  __DATA.__objc_data: 0x10bb0
+  __DATA.__objc_const: 0x35db8
+  __DATA.__objc_selrefs: 0x66f0
+  __DATA.__objc_ivar: 0x2460
+  __DATA.__objc_data: 0x10b60
   __DATA.__data: 0x73a0
-  __DATA.__bss: 0x8888
+  __DATA.__bss: 0x8880
   __DATA.__common: 0xb6c
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 360A2E55-81D4-3361-866F-B3590BAD3E8B
-  Functions: 13665
-  Symbols:   2178
-  CStrings:  18901
+  UUID: 0A36F0ED-A467-3EFC-A640-998775FDE6BF
+  Functions: 13664
+  Symbols:   2177
+  CStrings:  18905
 
Symbols:
+ _objc_retain_x7
- _drand48
- _srand48
CStrings:
+ "01:56:18"
+ "Memory entity loaded from entity missing property: %{public}@.%{public}@"
+ "Oct  6 2025"
+ "TB,GisPreorderFulfillment,V_preorderFulfillment"
+ "[%@] Cleared actorID with reason: %{public}@"
+ "[%@] Queue contains preorder fulfillment info for %llu"
+ "[%@] Skipping subscription state update due to entitlement lookup error: %{public}@"
+ "[%{public}s] Enqueueing %ld event(s)"
+ "[%{public}s] Flushed %@ event(s)"
+ "[DNU] Initiated session with actorID: %{public}@"
+ "_preorderFulfillment"
+ "_preorderPushUUID"
+ "_pushUUID"
+ "com.apple.appstored.downloadqueue"
+ "com.apple.appstored.metrics.purchase"
+ "com.apple.appstored.pushreceived"
+ "failedImportCount"
+ "isPreorderFulfillment"
+ "missingMatchingItem"
+ "preorderFulfillment"
+ "resultCount"
+ "service:account:inviteDroppedForSessionID:fromID:error:"
+ "setPreorderFulfillment:"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"
- "21:35:07"
- "@\"PushDiagnostic\""
- "AppUsageEnableMetricsForActorIDSession"
- "AppUsagePostMetricsSamplingPercentageOverride"
- "CrossfirePostMetricsSamplingPercentageOverride"
- "Post skipped for actorID session"
- "Post skipped for crossfire interval"
- "PushDiagnostic"
- "Sep 29 2025"
- "[%@] Crossfire interval not in session"
- "[%@]: ** RECEIVED CONNECTION TEST: %@ **"
- "[%@]: App usage metrics for %@: %f"
- "[%@]: Cleared actorID with reason: %{public}@"
- "[%@]: Using defaults based app usage post sampling override: %f"
- "[%{public}s] Enqueueing %{public}s"
- "[%{public}s] Flushed %{public}s"
- "[DNU] Initiated session with actorID: %{public}@ with sampling enabled: %d"
- "[DNU] Skipping metrics for actorID session"
- "_pushDiagnostic"
- "metrics/sampling/custom/xp_amp_app_usage_dnu/percentage"
- "metrics/sampling/custom/xp_amp_usage_analytics/percentage"

```
