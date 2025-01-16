## CloudSubscriptionFeatures

> `/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures`

```diff

-301.22.2.8.0
-  __TEXT.__text: 0xd7ba4
-  __TEXT.__auth_stubs: 0x1ea0
-  __TEXT.__objc_methlist: 0xbec
-  __TEXT.__const: 0x65c8
+301.22.3.1.0
+  __TEXT.__text: 0xe5844
+  __TEXT.__auth_stubs: 0x1f40
+  __TEXT.__objc_methlist: 0xc38
+  __TEXT.__const: 0x6e78
+  __TEXT.__cstring: 0x59f1
+  __TEXT.__oslogstring: 0x846c
   __TEXT.__gcc_except_tab: 0x168
-  __TEXT.__cstring: 0x53e1
-  __TEXT.__oslogstring: 0x7dec
   __TEXT.__dlopen_cstrs: 0xc4
-  __TEXT.__swift5_typeref: 0x1fbc
-  __TEXT.__swift5_fieldmd: 0x1c30
-  __TEXT.__constg_swiftt: 0x2050
-  __TEXT.__swift5_reflstr: 0x153d
+  __TEXT.__swift5_typeref: 0x225e
+  __TEXT.__swift5_fieldmd: 0x1f38
+  __TEXT.__constg_swiftt: 0x234c
+  __TEXT.__swift5_reflstr: 0x179d
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_assocty: 0x360
-  __TEXT.__swift5_capture: 0xea0
-  __TEXT.__swift5_protos: 0x78
-  __TEXT.__swift5_proto: 0x5cc
-  __TEXT.__swift5_types: 0x22c
+  __TEXT.__swift5_capture: 0xf80
+  __TEXT.__swift5_protos: 0x8c
+  __TEXT.__swift5_proto: 0x648
+  __TEXT.__swift5_types: 0x264
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x3940
-  __TEXT.__eh_frame: 0x85f8
-  __TEXT.__objc_classname: 0x131
-  __TEXT.__objc_methname: 0x1d72
-  __TEXT.__objc_methtype: 0x28e
-  __TEXT.__objc_stubs: 0xb80
-  __DATA_CONST.__got: 0x4f8
-  __DATA_CONST.__const: 0x638
-  __DATA_CONST.__objc_classlist: 0x158
+  __TEXT.__unwind_info: 0x3c70
+  __TEXT.__eh_frame: 0x8b90
+  __TEXT.__objc_classname: 0x142
+  __TEXT.__objc_methname: 0x1f0a
+  __TEXT.__objc_methtype: 0x2be
+  __TEXT.__objc_stubs: 0xd00
+  __DATA_CONST.__got: 0x518
+  __DATA_CONST.__const: 0x670
+  __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x880
+  __DATA_CONST.__objc_selrefs: 0x8e8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0xf60
-  __AUTH_CONST.__auth_ptr: 0x9a8
-  __AUTH_CONST.__const: 0x5c90
-  __AUTH_CONST.__cfstring: 0x440
-  __AUTH_CONST.__objc_const: 0x3a20
-  __AUTH.__objc_data: 0x438
-  __AUTH.__data: 0x418
-  __DATA.__objc_ivar: 0x2c
-  __DATA.__data: 0x19d0
-  __DATA.__bss: 0x8d90
+  __AUTH_CONST.__auth_got: 0xfb0
+  __AUTH_CONST.__auth_ptr: 0xa60
+  __AUTH_CONST.__const: 0x6410
+  __AUTH_CONST.__cfstring: 0x4a0
+  __AUTH_CONST.__objc_const: 0x3c50
+  __AUTH.__objc_data: 0x4a0
+  __AUTH.__data: 0x600
+  __DATA.__objc_ivar: 0x30
+  __DATA.__data: 0x1ba0
+  __DATA.__bss: 0x9ac0
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x1148
-  __DATA_DIRTY.__data: 0x1d88
-  __DATA_DIRTY.__bss: 0x1cd0
+  __DATA_DIRTY.__objc_data: 0x1178
+  __DATA_DIRTY.__data: 0x1d78
+  __DATA_DIRTY.__bss: 0x1cf0
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4169
-  Symbols:   616
-  CStrings:  1508
+  Functions: 4450
+  Symbols:   642
+  CStrings:  1591
 
Symbols:
+ _OBJC_CLASS_$_TapToRadarHelper
+ _OBJC_METACLASS_$_TapToRadarHelper
+ _dlopen
+ _swift_dynamicCastClass
CStrings:
+ "/AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit"
+ "@\"NSObject<OS_dispatch_queue>\""
+ "A missing JWT has been detected when returning \"cloud.llm\"."
+ "An excessive number of requests were detected over the last 24 hours. We expect 1-5 requests per day. Actual was "
+ "Attempted to set GMOptIn.isAutoOptedIn to %{bool}d but it already has that value. Early returning."
+ "Attempting to post a new TTR, dispatching."
+ "Attempting to post new TTR from inside the dispatch block."
+ "Can't construct Array with count < 0"
+ "Checking for excessive /features requests"
+ "Completed posting TTR"
+ "Device is being rate limited and is not eligible for another TTR prompt. will be shown %@"
+ "Device is not being rate limited and is eligible for another TTR prompt."
+ "Error posting TTR: %@"
+ "Excessive requests detected (%{public}ld exceeded %{public}ld. Attempting to post TTR."
+ "Expired JWT has been detected when returning \"cloud.llm\"."
+ "Feature ID %s is supported? %{bool}d"
+ "Feature appears valid: %{public}s"
+ "Fetched value for isAutoOptedIn status: %{bool}d"
+ "Found %ld recent requests."
+ "Got settings, checking if we should post a new TTR."
+ "Greymatter"
+ "Missing JWT detected"
+ "No diagnostics found, will return empty array."
+ "No excessive requests detected. Not posting TTR."
+ "Posting TTR."
+ "Process has unknown authorization to display prompt %lu, will not post prompt."
+ "Process is fully authorized to display TTR."
+ "Process is not authorized for TTR. Will not prompt user."
+ "Process is rate limited for sending TTRs. Will not prompt user."
+ "RadarComponent"
+ "RadarDraft"
+ "Sending message %s with body %s"
+ "Serving cloud.llm enabled feature with expired JWT."
+ "Serving cloud.llm enabled feature with missing JWT."
+ "Serving cloud.llm feature with access %{bool,public}d but GMS does not match the state."
+ "Set new value for isAutoOptedIn %{bool}d."
+ "Swift/Array.swift"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_dispatchQueue"
+ "TapToRadarHelper"
+ "TapToRadarService"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "User denied authorization for process to file TTR. Will not prompt user."
+ "User is opting in, setting followup to true to prevent CFU from showing."
+ "Validating feature %{public}s"
+ "[ER] Excessive Requests to iCloud servers"
+ "[Expired-JWT] Expired JWT detected"
+ "_TtC25CloudSubscriptionFeaturesP33_41A2CE00D5243E1E8B98F3F55D67C94315HardwareChecker"
+ "_dispatchQueue"
+ "a missing token was detected"
+ "an excessive number of requests to iCloud servers was detected"
+ "an expired token was detected"
+ "appleIntelligenceCapable"
+ "authorizationStatus"
+ "com.apple.CloudSubscriptionFeatures.requestFeature.finish"
+ "com.apple.CloudSubscriptionFeatures.requestFeature.start"
+ "com.apple.csf.coretelephony"
+ "com.apple.musebuddy"
+ "compare:"
+ "coreTelephonyQueue"
+ "createDraft:forProcessNamed:withDisplayReason:completionHandler:"
+ "deviceCapabilities"
+ "gmsIsAvailable()"
+ "iCloud daemon"
+ "iCloudSubscription Client"
+ "initWithName:version:identifier:"
+ "interfaceLanguage"
+ "performInternalValidation(feature:systemProperties:)"
+ "performInternalValidationForFeature:completion:"
+ "rateLimitResetDate"
+ "serviceSettings"
+ "setClassification:"
+ "setComponent:"
+ "setIsUserInitiated:"
+ "setProblemDescription:"
+ "setReproducibility:"
+ "showTTRPromptIfNecessary(forFeature:)"
+ "startFeatureRequest"
+ "stewieCapable"
+ "tapToRadar:withMessage:withReason:"
+ "tapToRadarPoster"
+ "v32@0:8@\"CloudFeature\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@16@24@32"

```
