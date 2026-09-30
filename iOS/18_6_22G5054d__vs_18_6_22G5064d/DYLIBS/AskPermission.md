## AskPermission

> `/System/Library/PrivateFrameworks/AskPermission.framework/AskPermission`

```diff

-128.6.2.0.0
-  __TEXT.__text: 0x65f0
-  __TEXT.__auth_stubs: 0x430
+128.6.4.0.0
+  __TEXT.__text: 0x7000
+  __TEXT.__auth_stubs: 0x450
   __TEXT.__objc_methlist: 0x9cc
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x338
-  __TEXT.__cstring: 0x5f7
-  __TEXT.__oslogstring: 0x8e8
-  __TEXT.__unwind_info: 0x290
+  __TEXT.__cstring: 0x60c
+  __TEXT.__oslogstring: 0x9f1
+  __TEXT.__unwind_info: 0x280
   __TEXT.__objc_classname: 0x169
   __TEXT.__objc_methname: 0x18bc
   __TEXT.__objc_methtype: 0x54e

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x228
+  __AUTH_CONST.__auth_got: 0x238
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0xb00
+  __AUTH_CONST.__cfstring: 0xb40
   __AUTH_CONST.__objc_const: 0x1038
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1F2A5F76-677D-3121-857E-B6C740CC2314
+  UUID: CA0FAFE3-8DB4-3992-A610-9B5F7148F845
   Functions: 180
-  Symbols:   833
-  CStrings:  590
+  Symbols:   835
+  CStrings:  599
 
Symbols:
+ _AMSLogKey
+ _NSStringFromSelector
+ ___57+[APMetricsEvent nonIdentifiableMetricsFieldsForAccount:]_block_invoke.61
+ ___block_descriptor_56_e8_32s_e42_"AMSPromise"24?0"NSString"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s_e59_"AMSPromise"24?0"AMSMetricsIdentifierStore"8"NSError"16ls32l8
+ ___block_descriptor_64_e8_32s40s_e46_"AMSPromise"24?0"NSDictionary"8"NSError"16ls32l8s40l8
- ___57+[APMetricsEvent nonIdentifiableMetricsFieldsForAccount:]_block_invoke.54
- ___block_descriptor_48_e8_32s40s_e46_"AMSPromise"24?0"NSDictionary"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s_e42_"AMSPromise"24?0"NSString"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32s_e59_"AMSPromise"24?0"AMSMetricsIdentifierStore"8"NSError"16ls32l8
Functions:
~ +[APMetricsEvent metricsEventWithAccount:request:] : 512 -> 1368
~ ___50+[APMetricsEvent metricsEventWithAccount:request:]_block_invoke : 448 -> 1164
~ +[APMetricsEvent nonIdentifiableMetricsFieldsForAccount:] : 336 -> 728
~ ___57+[APMetricsEvent nonIdentifiableMetricsFieldsForAccount:]_block_invoke : 624 -> 948
~ ___57+[APMetricsEvent nonIdentifiableMetricsFieldsForAccount:]_block_invoke.54 -> ___57+[APMetricsEvent nonIdentifiableMetricsFieldsForAccount:]_block_invoke.61 : 728 -> 1016
CStrings:
+ "%@: %@ "
+ "%@: [%@] %@ "
+ "%{public}@Creating metrics event. Account: %{public}@ | Request: %{public}@"
+ "%{public}@Error loading Metrics Store for userID: %@"
+ "%{public}@Error loading Metrics clientID: %@"
+ "%{public}@Error obtaining metrics fields: %{public}@"
+ "%{public}@Generating metrics fields for account: %{public}@"
+ "%{public}@LOB is not App Store. Enqueueing standard metrics."
+ "%{public}@Loaded Metrics clientID: %@"
+ "%{public}@Loaded Metrics event fields: %@"
+ "%{public}@Obtained metrics fields: %{public}@"
+ "%{public}@Request is for App Store LOB."
- "%{public}@: Error loading Metrics Store for userID: %@"
- "%{public}@: Error loading Metrics clientID: %@"
- "%{public}@: LOB is not App Store. Enqueueing standard metrics."
- "%{public}@: Loaded Metrics clientID: %@"
- "%{public}@: Loaded Metrics event fields: %@"

```
