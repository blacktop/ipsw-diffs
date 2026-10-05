## webprivacyd

> `/System/Library/PrivateFrameworks/WebPrivacy.framework/webprivacyd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_intobj`

```diff

-58.0.0.0.0
-  __TEXT.__text: 0x128a8
-  __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_stubs: 0x740
-  __TEXT.__const: 0x195
-  __TEXT.__gcc_except_tab: 0x1580
-  __TEXT.__cstring: 0x4dc
-  __TEXT.__oslogstring: 0xc60
-  __TEXT.__objc_methname: 0x497
-  __TEXT.__unwind_info: 0xaf0
-  __DATA_CONST.__const: 0x920
-  __DATA_CONST.__cfstring: 0x600
+59.0.0.0.0
+  __TEXT.__text: 0x15b04
+  __TEXT.__auth_stubs: 0xa80
+  __TEXT.__objc_stubs: 0xa20
+  __TEXT.__const: 0x1ad
+  __TEXT.__gcc_except_tab: 0x1a58
+  __TEXT.__cstring: 0x6c1
+  __TEXT.__oslogstring: 0x127a
+  __TEXT.__dlopen_cstrs: 0xc0
+  __TEXT.__objc_methname: 0x684
+  __TEXT.__unwind_info: 0xd10
+  __DATA_CONST.__const: 0xae8
+  __DATA_CONST.__cfstring: 0x700
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x4c8
-  __DATA_CONST.__got: 0x108
-  __DATA.__objc_selrefs: 0x1d0
+  __DATA_CONST.__auth_got: 0x550
+  __DATA_CONST.__got: 0x118
+  __DATA.__objc_selrefs: 0x288
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/WebPrivacy.framework/WebPrivacy
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 462
-  Symbols:   903
-  CStrings:  205
+  Functions: 538
+  Symbols:   1054
+  CStrings:  270
 
Symbols:
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/WebPrivacy/install/TempContent/Objects/WebPrivacy.build/Daemon.build/Objects-normal/arm64e/SecurityFlagsBag.o
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/WebPrivacy/install/TempContent/Objects/WebPrivacy.build/Daemon.build/Objects-normal/arm64e/SecurityFlagsMonitor.o
+ GCC_except_table107
+ GCC_except_table111
+ GCC_except_table115
+ GCC_except_table120
+ GCC_except_table140
+ GCC_except_table141
+ GCC_except_table152
+ GCC_except_table153
+ GCC_except_table168
+ GCC_except_table169
+ GCC_except_table173
+ GCC_except_table177
+ GCC_except_table185
+ GCC_except_table193
+ GCC_except_table194
+ GCC_except_table195
+ GCC_except_table204
+ GCC_except_table205
+ GCC_except_table206
+ GCC_except_table223
+ GCC_except_table225
+ GCC_except_table238
+ GCC_except_table239
+ GCC_except_table247
+ GCC_except_table248
+ GCC_except_table249
+ GCC_except_table28
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table38
+ GCC_except_table45
+ GCC_except_table54
+ GCC_except_table55
+ GCC_except_table56
+ GCC_except_table80
+ SecurityFlagsBag.mm
+ SecurityFlagsMonitor.mm
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSNotificationCenter
+ _ZN7Backend20SecurityFlagsMonitor15observeBagLoadsEP11objc_objectP8NSString
+ _ZN7Backend20SecurityFlagsMonitor17announceIfChangedEONSt3__16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE
+ _ZN7Backend20SecurityFlagsMonitor20beginPeriodicRefreshEP12BGSystemTask
+ _ZN7Backend20SecurityFlagsMonitor23registerPeriodicRefreshEv
+ _ZN7Backend20SecurityFlagsMonitor6sharedEv
+ _ZN7Backend29securityFlagNamesFromBagValueEP11objc_object
+ _ZN7BackendL15sharedServerBagEv
+ _ZN7BackendL15sharedWebKitBagEv
+ _ZN7BackendL34bagFinishedLoadingNotificationNameEv
+ _ZZL20getIDSServerBagClassvE9softClass
+ _ZZL24IDSFoundationLibraryCorePPcE16frameworkLibrary
+ _ZZL26getIDSServerBagConfigClassvE9softClass
+ _ZZL29getBGSystemTaskSchedulerClassvE9softClass
+ _ZZL32BackgroundSystemTasksLibraryCorePPcE16frameworkLibrary
+ _ZZL51getIDSServerBagFinishedLoadingNotificationSymbolLocvE3ptr
+ __Block_object_dispose
+ __ZL20getIDSServerBagClassv
+ __ZL24IDSFoundationLibraryCorePPc
+ __ZL25audit_stringIDSFoundation
+ __ZL33audit_stringBackgroundSystemTasks
+ __ZL51getIDSServerBagFinishedLoadingNotificationSymbolLocv
+ __ZN10WebPrivacy3XPC14serializeReplyIL11MessageName13EJNS_12MessageErrorENSt3__16vectorINS4_12basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEENS9_ISB_EEEEEEEPU24objcproto13OS_xpc_object8NSObjectSG_DpOT0_
+ __ZN10WebPrivacy3XPC6decodeINS0_16GetSecurityFlagsEEENSt3__18optionalIT_EEPU24objcproto13OS_xpc_object8NSObject
+ __ZN10WebPrivacy3XPC9sendReplyINS0_21GetSecurityFlagsReplyEJNS_12MessageErrorENSt3__16vectorINS4_12basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEENS9_ISB_EEEEEEEvPU24objcproto13OS_xpc_object8NSObjectDpOT0_
+ __ZN7Backend13Configuration14defaultsDomainEv
+ __ZN7Backend15webKitBagURLKeyEv
+ __ZN7Backend16SecurityFlagsBag17disabledFlagNamesEv
+ __ZN7Backend16SecurityFlagsBag7refreshEv
+ __ZN7Backend16SecurityFlagsBag9isLoadingEv
+ __ZN7Backend19securityFlagsBagKeyEv
+ __ZN7Backend20SecurityFlagsMonitor14checkForChangeEv
+ __ZN7Backend20SecurityFlagsMonitor15observeBagLoadsEP11objc_objectP8NSString
+ __ZN7Backend20SecurityFlagsMonitor17announceIfChangedEONSt3__16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE
+ __ZN7Backend20SecurityFlagsMonitor17rememberFlagNamesERKNSt3__16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE
+ __ZN7Backend20SecurityFlagsMonitor18endPeriodicRefreshEv
+ __ZN7Backend20SecurityFlagsMonitor20beginPeriodicRefreshEP12BGSystemTask
+ __ZN7Backend20SecurityFlagsMonitor20resetStateForTestingEv
+ __ZN7Backend20SecurityFlagsMonitor23registerPeriodicRefreshEv
+ __ZN7Backend20SecurityFlagsMonitor6sharedEv
+ __ZN7Backend20SecurityFlagsMonitorC1Ev
+ __ZN7Backend20SecurityFlagsMonitorC2Ev
+ __ZN7Backend23securityFlagNamesDifferERKNSt3__16vectorINS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS5_IS7_EEEESB_
+ __ZN7Backend29periodicRefreshTaskIdentifierEv
+ __ZN7Backend29securityFlagNamesFromBagValueEP11objc_object
+ __ZN7Backend6Server22handleGetSecurityFlagsEPU24objcproto13OS_xpc_object8NSObject
+ __ZN7BackendL10normalizedENSt3__16vectorINS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS5_IS7_EEEE
+ __ZN7BackendL15sharedServerBagEv
+ __ZN7BackendL15sharedWebKitBagEv
+ __ZN7BackendL34bagFinishedLoadingNotificationNameEv
+ __ZN8Platform4joinIRA3_KcEENSt3__112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEERKNS4_6vectorISA_NS8_ISA_EEEEOT_
+ __ZNK7Backend20SecurityFlagsMonitor15cachedFlagNamesEv
+ __ZNKSt3__110__equal_toclB9fqn220106INS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EEbRKT_RKT0_
+ __ZNSt3__110accumulateB9fqn220106INS_11__wrap_iterIPKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEES7_ZN8Platform4joinIRA3_KcEES7_RKNS_6vectorIS7_NS5_IS7_EEEEOT_EUlS7_S7_E_EET0_SL_SL_SO_T1_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
+ __ZNSt3__130__uninitialized_allocator_copyB9fqn220106INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEPKS6_S9_PS6_EET2_RT_T0_T1_SB_
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__init_with_sizeB9fqn220106IPS6_SA_EEvT_T0_m
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE18__assign_with_sizeB9fqn220106INS_17_ClassicAlgPolicyEPKS6_SC_EEvT0_T1_l
+ __ZNSt3__18__uniqueB9fqn220106INS_17_ClassicAlgPolicyENS_11__wrap_iterIPNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEESA_RNS_10__equal_toEEENS_4pairIT0_SE_EESE_T1_OT2_
+ __ZZN10WebPrivacy3XPC14serializeReplyIL11MessageName13EJNS_12MessageErrorENSt3__16vectorINS4_12basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEENS9_ISB_EEEEEEEPU24objcproto13OS_xpc_object8NSObjectSG_DpOT0_ENKUlvE_clEv
+ __ZZN7Backend20SecurityFlagsMonitor6sharedEvE7monitor
+ __ZZN7Backend20SecurityFlagsMonitor6sharedEvE9onceToken
+ __ZZN7BackendL15sharedServerBagEvE3bag
+ __ZZN7BackendL15sharedServerBagEvE9onceToken
+ __ZZN7BackendL15sharedWebKitBagEvE4lock
+ __ZZN7BackendL15sharedWebKitBagEvE9webKitBag
+ __ZZN7BackendL18flagNameSeparatorsEvE10separators
+ __ZZN7BackendL18flagNameSeparatorsEvE9onceToken
+ __ZZN7BackendL19isPlausibleFlagNameEP8NSStringE20disallowedCharacters
+ __ZZN7BackendL19isPlausibleFlagNameEP8NSStringE9onceToken
+ __ZZN7BackendL23canBuildWebKitBagConfigEP10objc_classE9available
+ __ZZN7BackendL23canBuildWebKitBagConfigEP10objc_classE9onceToken
+ ___ZN7Backend20SecurityFlagsMonitor20beginPeriodicRefreshEP12BGSystemTask_block_invoke
+ ___ZN7BackendL15sharedServerBagEv_block_invoke
+ ____ZL20getIDSServerBagClassv_block_invoke
+ ____ZL24IDSFoundationLibraryCorePPc_block_invoke
+ ____ZL26getIDSServerBagConfigClassv_block_invoke
+ ____ZL29getBGSystemTaskSchedulerClassv_block_invoke
+ ____ZL32BackgroundSystemTasksLibraryCorePPc_block_invoke
+ ____ZL51getIDSServerBagFinishedLoadingNotificationSymbolLocv_block_invoke
+ ____ZN7Backend20SecurityFlagsMonitor15observeBagLoadsEP11objc_objectP8NSString_block_invoke
+ ____ZN7Backend20SecurityFlagsMonitor15observeBagLoadsEP11objc_objectP8NSString_block_invoke_2
+ ____ZN7Backend20SecurityFlagsMonitor15observeBagLoadsEP11objc_objectP8NSString_block_invoke_3
+ ____ZN7Backend20SecurityFlagsMonitor20beginPeriodicRefreshEP12BGSystemTask_block_invoke
+ ____ZN7Backend20SecurityFlagsMonitor20beginPeriodicRefreshEP12BGSystemTask_block_invoke_2
+ ____ZN7Backend20SecurityFlagsMonitor20beginPeriodicRefreshEP12BGSystemTask_block_invoke_3
+ ____ZN7Backend20SecurityFlagsMonitor23registerPeriodicRefreshEv_block_invoke
+ ____ZN7Backend20SecurityFlagsMonitor23registerPeriodicRefreshEv_block_invoke_2
+ ____ZN7Backend20SecurityFlagsMonitor6sharedEv_block_invoke
+ ____ZN7BackendL15sharedServerBagEv_block_invoke
+ ____ZN7BackendL18flagNameSeparatorsEv_block_invoke
+ ____ZN7BackendL19isPlausibleFlagNameEP8NSString_block_invoke
+ ____ZN7BackendL23canBuildWebKitBagConfigEP10objc_class_block_invoke
+ ___block_descriptor_40_e22_v16?0"BGSystemTask"8l
+ ___block_descriptor_40_e24_v16?0"NSNotification"8l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e5_v8?0lu32l8
+ ___block_descriptor_40_ea8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_e5_v8?0l
+ ___block_descriptor_48_ea8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_ea8_32s40s_e5_v8?0ls32l8s40l8
+ __block_literal_global
+ __sl_dlopen
+ _abort_report_np
+ _class_getName
+ _dlerror
+ _dlsym
+ _notify_post
+ _objc_getClass
+ _objc_msgSend$UTF8String
+ _objc_msgSend$addCharactersInString:
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$componentsSeparatedByCharactersInSet:
+ _objc_msgSend$copy
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$initWithConfig:queue:
+ _objc_msgSend$invertedSet
+ _objc_msgSend$isLoading
+ _objc_msgSend$rangeOfCharacterFromSet:
+ _objc_msgSend$registerForTaskWithIdentifier:usingQueue:launchHandler:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$setExpirationHandler:
+ _objc_msgSend$setTaskCompleted
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$sharedScheduler
+ _objc_msgSend$startBagLoad
+ _objc_msgSend$urlWithKey:
+ _objc_msgSend$webKitConfigForURL:
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
+ _objc_opt_respondsToSelector
+ _objc_release_x1
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x28
+ _objc_storeStrong
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _strcmp
- GCC_except_table103
- GCC_except_table104
- GCC_except_table105
- GCC_except_table117
- GCC_except_table137
- GCC_except_table138
- GCC_except_table149
- GCC_except_table150
- GCC_except_table164
- GCC_except_table165
- GCC_except_table166
- GCC_except_table174
- GCC_except_table182
- GCC_except_table189
- GCC_except_table190
- GCC_except_table191
- GCC_except_table201
- GCC_except_table202
- GCC_except_table203
- GCC_except_table214
- GCC_except_table222
- GCC_except_table232
- GCC_except_table236
- GCC_except_table244
- GCC_except_table29
- GCC_except_table37
- GCC_except_table39
- GCC_except_table46
- GCC_except_table77
CStrings:
+ ""
+ "%s"
+ ", "
+ ",;"
+ "<none>"
+ "BGSystemTaskScheduler"
+ "IDSServerBag"
+ "IDSServerBagConfig"
+ "IDSServerBagFinishedLoadingNotification"
+ "Replying with %zu disabled security flag(s)."
+ "Security flag kill switch changed: was %zu disabled flag(s), now %zu: %{public}s. Notifying clients."
+ "Security flag kill switch: BGSystemTaskScheduler is unavailable; no periodic check."
+ "Security flag kill switch: IDSServerBag is unavailable."
+ "Security flag kill switch: IDSServerBagConfig is unavailable."
+ "Security flag kill switch: IDSServerBagFinishedLoadingNotification is unavailable."
+ "Security flag kill switch: a periodic check was already in flight."
+ "Security flag kill switch: bag value for %{public}@ is a %{public}s; expected an array of strings or a delimited string."
+ "Security flag kill switch: cannot observe bag loads; a change will only be seen at the next check."
+ "Security flag kill switch: could not configure a WebKit bag; reading the list from the IDS bag."
+ "Security flag kill switch: could not get the shared server bag."
+ "Security flag kill switch: could not get the shared task scheduler; no periodic check."
+ "Security flag kill switch: failed to notify clients with status: %u"
+ "Security flag kill switch: failed to register %{public}@; no periodic check."
+ "Security flag kill switch: ignoring a %{public}s in the bag value; expected a string."
+ "Security flag kill switch: ignoring implausible flag name in the bag value."
+ "Security flag kill switch: no bag fetch is in flight; ending the periodic check early."
+ "Security flag kill switch: reading the list from the WebKit bag named under %{public}@."
+ "Security flag kill switch: this IdentityServices cannot configure a WebKit bag; reading the list from the IDS bag."
+ "UTF8String"
+ "`"
+ "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
+ "addCharactersInString:"
+ "addObserverForName:object:queue:usingBlock:"
+ "arrayWithCapacity:"
+ "cachedDisabledSecurityFlags"
+ "characterSetWithCharactersInString:"
+ "com.apple.WebPrivacy.security-flags"
+ "com.apple.WebPrivacy.securityFlagsDidChange"
+ "com.apple.WebPrivacy.webkit-server-bag"
+ "com.apple.webprivacyd.security-flags-refresh"
+ "componentsSeparatedByCharactersInSet:"
+ "copy"
+ "defaultCenter"
+ "initWithConfig:queue:"
+ "invertedSet"
+ "isLoading"
+ "rangeOfCharacterFromSet:"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "removeObject:"
+ "removeObserver:"
+ "setExpirationHandler:"
+ "setTaskCompleted"
+ "sharedInstance"
+ "sharedScheduler"
+ "softlink:o:path:/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks"
+ "softlink:o:path:/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation"
+ "startBagLoad"
+ "urlWithKey:"
+ "v16@?0@\"BGSystemTask\"8"
+ "v16@?0@\"NSNotification\"8"
+ "webKitConfigForURL:"
+ "webkit-bag-url"
+ "webkit-bag-url-staging"
+ "webkit-security-flags-disabled"
+ "whitespaceAndNewlineCharacterSet"
```
