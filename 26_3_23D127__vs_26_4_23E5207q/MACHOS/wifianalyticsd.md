## wifianalyticsd

> `/usr/libexec/wifianalyticsd`

```diff

-788.1.0.0.0
-  __TEXT.__text: 0x99cf4
-  __TEXT.__auth_stubs: 0x15f0
-  __TEXT.__objc_stubs: 0x8ba0
-  __TEXT.__objc_methlist: 0x350c
-  __TEXT.__const: 0x498
+795.19.0.0.0
+  __TEXT.__text: 0xa08d8
+  __TEXT.__auth_stubs: 0x15b0
+  __TEXT.__objc_stubs: 0x8b60
+  __TEXT.__objc_methlist: 0x34fc
+  __TEXT.__const: 0x4a0
   __TEXT.__dlopen_cstrs: 0x1e2
-  __TEXT.__cstring: 0x14318
+  __TEXT.__objc_classname: 0x45d
   __TEXT.__constg_swiftt: 0x494
   __TEXT.__swift5_typeref: 0x276
   __TEXT.__swift5_fieldmd: 0x1ec
-  __TEXT.__oslogstring: 0x14753
+  __TEXT.__oslogstring: 0x14457
   __TEXT.__swift5_types: 0x30
+  __TEXT.__cstring: 0x14291
+  __TEXT.__objc_methname: 0xdd0f
   __TEXT.__swift5_reflstr: 0x12b
-  __TEXT.__objc_methname: 0xdb9a
-  __TEXT.__swift5_capture: 0xec
-  __TEXT.__gcc_except_tab: 0x52f8
-  __TEXT.__objc_classname: 0x334
-  __TEXT.__objc_methtype: 0x110b
-  __TEXT.__unwind_info: 0x1070
+  __TEXT.__swift5_capture: 0xdc
+  __TEXT.__objc_methtype: 0x1127
+  __TEXT.__gcc_except_tab: 0x50b4
+  __TEXT.__unwind_info: 0x1318
   __TEXT.__eh_frame: 0x90
-  __DATA_CONST.__auth_got: 0xb10
+  __DATA_CONST.__auth_got: 0xaf0
   __DATA_CONST.__got: 0x440
-  __DATA_CONST.__auth_ptr: 0x88
-  __DATA_CONST.__const: 0x1a88
-  __DATA_CONST.__cfstring: 0x10740
+  __DATA_CONST.__auth_ptr: 0x80
+  __DATA_CONST.__const: 0x1a60
+  __DATA_CONST.__cfstring: 0x10780
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x438
   __DATA_CONST.__objc_arrayobj: 0xd8
   __DATA.__objc_const: 0x5620
-  __DATA.__objc_selrefs: 0x2e40
+  __DATA.__objc_selrefs: 0x2e30
   __DATA.__objc_ivar: 0x50c
   __DATA.__objc_data: 0x9f8
   __DATA.__data: 0x998

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: A3DC6635-29C6-33E1-BB88-8DFD0394CEF3
-  Functions: 1499
-  Symbols:   527
-  CStrings:  8412
+  UUID: 7B46E506-68C5-32E9-B723-1873FA2F2211
+  Functions: 1496
+  Symbols:   525
+  CStrings:  8397
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _strlen
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x9
CStrings:
+ "\"WiFiAnalytics_executables-795.19\""
+ "%{public}s::%d:DPS Study starting - forcing fresh IOReporter subscription and sample"
+ "%{public}s::%d:NAN Status:%s NAN activity threshold: %ld, impact: %u, sdb: %u, updated before:%llu seconds"
+ "%{public}s::%d:Removed processToken %@ objects from cachedModelObjectsKeyToMessageMap"
+ "%{public}s::%d:Removing processToken %@ objects from cachedModelObjectsKeyToMessageMap"
+ "%{public}s::%d:SDNS: Triggering stepwiseRecovery approach"
+ "-[WAEngine _triggerDatapathDiagnosticsAndCollectUpdates:forProcessToken:waMessage:andReply:]"
+ "-[WAEngine triggerDNSResetRecoveryAction:]"
+ "-[WAEngine triggerStepwiseDNSRecovery:]"
+ "-[WAEngine triggerStepwiseDNSRecovery:]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/4~CIsLugAE3JHkc7Ut4pWWxB7NxLWGpE9mg5Ylixo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1471: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsLugAE3JHkc7Ut4pWWxB7NxLWGpE9mg5Ylixo/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3371: libc++ Hardening assertion !empty() failed: string::pop_back(): string is already empty\n"
+ "DPSNANS_nanInfraImpact"
+ "Feb  9 2026 22:44:46"
+ "NANInfraImpact(%)"
+ "TB,N,V_isFirstDPSSinceBoot"
+ "WiFiAnalytics_executables-795.19"
+ "WiFiAnalytics_executables-795.19 Feb  9 2026 22:44:43"
+ "_isFirstDPSSinceBoot"
+ "checkIfDPSResetRecoveryAllowed"
+ "com.apple.wifianalytics.WABackgroundTaskManager"
+ "isFirstDPSSinceBoot"
+ "setIsFirstDPSSinceBoot:"
+ "triggerDNSResetRecoveryAction:"
+ "triggerStepwiseDNSRecovery:"
- "\"WiFiAnalytics_executables-788.1\""
- "%{public}s::%d:NAN Status:%s NAN activity threshold: %ld, awdl usage: %u, sdb: %u, updated before:%llu seconds"
- "%{public}s::%d:PeerDiagnostics: Data collection failed with err:%@"
- "%{public}s::%d:PeerDiagnostics: No Recovery Action recommended for symptoms-dps"
- "%{public}s::%d:PeerDiagnostics: No budget"
- "%{public}s::%d:PeerDiagnostics: Triggering Reassoc for symptoms-dps"
- "%{public}s::%d:PeerDiagnostics: Triggering Trap for symptoms-dps"
- "%{public}s::%d:PeerDiagnostics: peerDiagnosticsStudy disabled"
- "%{public}s::%d:PeerDiagnostics: triggerPeerDiagnosticsStudy with type:%d"
- "%{public}s::%d:Removed processToken %@ objects from cachedModelObjectsKeyToMessageMap - final total is %ld"
- "%{public}s::%d:Removing processToken %@ objects from cachedModelObjectsKeyToMessageMap - countTotalKeysInNSObject to remove %ld, initial total is %ld"
- "%{public}s::%d:SDNS: Recommendation - WASymptomsDpsRecommendDoReset, Triggering Trap for symptoms-dps with reason TrapOnDNSSymptoms"
- "%{public}s::%d:WAMessageAWD allocated for processToken %@ grouptype %ld key: %@ keysCount: %ld"
- "%{public}s::%d:countTotalKeysInNSObject count %ld, for processToken %@ count %ld, for groupType %ld count %ld, for key %@ wamcount %ld"
- "-[WAEngine _cachedModelObjectsForProcess:groupType:key:]_block_invoke"
- "-[WAEngine triggerDNSResetRecoveryAction]"
- "-[WAEngine triggerPeerDiagnosticsStudy:symptomsDnsStats:]"
- "-[WAEngine triggerStepwiseDNSRecovery]"
- "-[WAEngine triggerStepwiseDNSRecovery]_block_invoke"
- "B24@0:8q16"
- "Jan 27 2026 21:04:25"
- "NoBudget"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_peerDiagnosticsStudyQueue"
- "WiFiAnalytics_executables-788.1"
- "WiFiAnalytics_executables-788.1 Jan 27 2026 21:04:22"
- "_peerDiagnosticsStudyQueue"
- "checkIfDPSResetRecoveryAllowed:"
- "com.apple.wifi.analytics.peerDiagnosticsQ"
- "com.apple.wifianalytics.triggerPeerDiagnosticsStudy"
- "countTotalKeysInNSObject:"
- "peerDiagnosticsStudyQueue"
- "setPeerDiagnosticsStudyQueue:"
- "triggerDNSResetRecoveryAction"
- "triggerPeerDiagnosticsStudy:symptomsDnsStats:"
- "triggerStepwiseDNSRecovery"
- "v32@0:8Q16@24"

```
