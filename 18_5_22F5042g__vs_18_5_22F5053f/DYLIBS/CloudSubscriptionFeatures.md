## CloudSubscriptionFeatures

> `/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures`

```diff

-301.22.5.2.0
-  __TEXT.__text: 0xf1148
+301.22.5.4.0
+  __TEXT.__text: 0xfbc00
   __TEXT.__auth_stubs: 0x1e80
-  __TEXT.__objc_methlist: 0xe40
-  __TEXT.__const: 0x7c38
+  __TEXT.__objc_methlist: 0xe5c
+  __TEXT.__const: 0x7da8
   __TEXT.__gcc_except_tab: 0x70
-  __TEXT.__cstring: 0x5151
-  __TEXT.__oslogstring: 0x6f1c
+  __TEXT.__cstring: 0x5521
+  __TEXT.__oslogstring: 0x751c
   __TEXT.__dlopen_cstrs: 0xc4
-  __TEXT.__swift5_typeref: 0x22d2
-  __TEXT.__swift5_fieldmd: 0x2258
-  __TEXT.__constg_swiftt: 0x24c0
-  __TEXT.__swift5_reflstr: 0x1a4d
+  __TEXT.__swift5_typeref: 0x2334
+  __TEXT.__swift5_fieldmd: 0x22e4
+  __TEXT.__constg_swiftt: 0x2538
+  __TEXT.__swift5_reflstr: 0x1b4d
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_assocty: 0x390
-  __TEXT.__swift5_capture: 0x13b4
+  __TEXT.__swift5_assocty: 0x3a8
+  __TEXT.__swift5_capture: 0x1448
   __TEXT.__swift5_protos: 0x88
-  __TEXT.__swift5_proto: 0x6ac
-  __TEXT.__swift5_types: 0x2a8
-  __TEXT.__swift_as_entry: 0x348
-  __TEXT.__swift_as_ret: 0x3c4
+  __TEXT.__swift5_proto: 0x6bc
+  __TEXT.__swift5_types: 0x2b0
+  __TEXT.__swift_as_entry: 0x374
+  __TEXT.__swift_as_ret: 0x3ec
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x3a80
-  __TEXT.__eh_frame: 0x9d70
+  __TEXT.__unwind_info: 0x3c68
+  __TEXT.__eh_frame: 0xa550
   __TEXT.__objc_classname: 0x144
-  __TEXT.__objc_methname: 0x1de3
+  __TEXT.__objc_methname: 0x1e17
   __TEXT.__objc_methtype: 0x2be
   __TEXT.__objc_stubs: 0xc40
-  __DATA_CONST.__got: 0x538
-  __DATA_CONST.__const: 0x448
+  __DATA_CONST.__got: 0x550
+  __DATA_CONST.__const: 0x458
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x920
+  __DATA_CONST.__objc_selrefs: 0x928
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x28
   __AUTH_CONST.__auth_got: 0xf50
-  __AUTH_CONST.__auth_ptr: 0x8d0
-  __AUTH_CONST.__const: 0x7098
+  __AUTH_CONST.__auth_ptr: 0xa28
+  __AUTH_CONST.__const: 0x72c0
   __AUTH_CONST.__cfstring: 0x480
-  __AUTH_CONST.__objc_const: 0x3710
+  __AUTH_CONST.__objc_const: 0x3758
   __AUTH.__objc_data: 0x5e0
   __AUTH.__data: 0x648
   __DATA.__objc_ivar: 0x34
-  __DATA.__data: 0x1f50
-  __DATA.__bss: 0xa950
+  __DATA.__data: 0x1fe0
+  __DATA.__bss: 0xab50
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0xce8
-  __DATA_DIRTY.__data: 0x1ac0
+  __DATA_DIRTY.__objc_data: 0xcf0
+  __DATA_DIRTY.__data: 0x1b10
   __DATA_DIRTY.__bss: 0x15c0
   __DATA_DIRTY.__common: 0x48
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4323
-  Symbols:   700
-  CStrings:  1439
+  Functions: 4424
+  Symbols:   704
+  CStrings:  1490
 
Symbols:
+ _FLGroupIdentifierDevice
CStrings:
+ "%{public}llu [Finish] [Async] FAILURE %{public}s"
+ "%{public}llu [Finish] [Async] SUCCESS %{public}s"
+ "%{public}llu [Finish] [Sync] FAILURE %{public}s"
+ "%{public}llu [Finish] [Sync] SUCCESS %{public}s"
+ "%{public}llu [Start] [Async] %{public}s"
+ "%{public}llu [Start] [Sync] %{public}s"
+ "%{public}s Attempted to post waitlist CFU on invalid configuration."
+ "%{public}s Posting CFU"
+ "%{public}s Setting ADM bypass to %{bool,public}d."
+ "%{public}s Setting AFM bypass to %{bool,public}d."
+ "%{public}s Successfully posted waitlist CFU."
+ "%{public}s Unable to create FollowUp controller."
+ "%{public}s Unable to post waitlist CFU: %@"
+ "%{public}s Updating availability with bypass enabled."
+ "Attempted to determine device waitlist CFU eligibility on ineligible configuration."
+ "Cached new waitlist result: %{public}s - %{public}s"
+ "Determining if device has feature access."
+ "Device does not have access. Do not post the CFU."
+ "Device does not have cached LLM feature, device is likely missing HW support."
+ "Does have ticket? %{bool,public}d. Has ticket cache ticket? %{bool,public}d. Has waitlist cache ticket? %{bool,public}d"
+ "GM_CFU_ACTION_TEXT"
+ "GM_CFU_DESCRIPTION"
+ "Unable to init UserDefaults, will not read hasSentWaitlistCFUDate and will return false. Use may see CFU erroneously."
+ "Unable to init UserDefaults, will not update hasSentWaitlistCFUDate."
+ "Updating UserDefaults for key %{public}s to value: %{public}s"
+ "[%{public}s] No valid cache value for %{public}s."
+ "doesNotHaveAccess"
+ "doesNotHaveTicket"
+ "hasSentCFUPreviously"
+ "hasSentWaitlistFollowUp"
+ "ineligibleConfiguration"
+ "postWaitlistCFU()"
+ "postWaitlistCFUIfEligible(hasFeatureAccess:hasExistingTicket:)"
+ "prefs:root=SIRI&path=gmCFU"
+ "requestFeature"
+ "requestFeature.callCompletion"
+ "requestFeature.fetchAccount"
+ "requestFeature.fetchDeviceUnlocked"
+ "requestFeature.fetchFromCache"
+ "requestFeature.fetchTaskLimiter"
+ "requestFeature.isFeatureSupported"
+ "requestFeature.processResponse"
+ "requestFeature.taskLimiterPerformRequest"
+ "setADMBypass(_:)"
+ "setGMEligibilityBypass(_:)"
+ "setGMEligibilityBypassAndWait(_:)"
+ "stubbedFeature=1"
+ "unableToDetermineAccountEligibility"
+ "updateAFMAvailability(bypass:)"
+ "v24@0:8@?<v@?q@\"NSError\">16"
+ "verifyDeviceIsEligibleForWaitlistCFU(completion:)"
+ "verifyDeviceIsEligibleForWaitlistCFUWithCompletion:"
- "[%{public}s] No valid cache value for %{public}s"

```
