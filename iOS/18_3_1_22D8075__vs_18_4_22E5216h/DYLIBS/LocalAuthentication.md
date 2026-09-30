## LocalAuthentication

> `/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`

```diff

-1656.80.6.0.0
-  __TEXT.__text: 0x35720
-  __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x3020
-  __TEXT.__const: 0x2d4
-  __TEXT.__gcc_except_tab: 0xfd8
-  __TEXT.__cstring: 0x19aa
+1656.100.222.0.0
+  __TEXT.__text: 0x36728
+  __TEXT.__auth_stubs: 0xae0
+  __TEXT.__objc_methlist: 0x37e8
+  __TEXT.__const: 0x2e4
+  __TEXT.__gcc_except_tab: 0xfe8
+  __TEXT.__cstring: 0x19e6
   __TEXT.__dlopen_cstrs: 0x1cd
-  __TEXT.__oslogstring: 0x2526
+  __TEXT.__oslogstring: 0x2748
   __TEXT.__swift5_typeref: 0x6e
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1230
+  __TEXT.__unwind_info: 0x12f8
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0xa46
-  __TEXT.__objc_methname: 0x6d89
-  __TEXT.__objc_methtype: 0x1cd6
-  __TEXT.__objc_stubs: 0x48e0
-  __DATA_CONST.__got: 0x510
-  __DATA_CONST.__const: 0x1ba8
+  __TEXT.__objc_classname: 0xa42
+  __TEXT.__objc_methname: 0x6f26
+  __TEXT.__objc_methtype: 0x1d73
+  __TEXT.__objc_stubs: 0x49e0
+  __DATA_CONST.__got: 0x500
+  __DATA_CONST.__const: 0x1c48
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ab8
+  __DATA_CONST.__objc_selrefs: 0x1bd0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1f8
-  __AUTH_CONST.__auth_got: 0x570
+  __AUTH_CONST.__auth_got: 0x580
   __AUTH_CONST.__auth_ptr: 0x98
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x1980
-  __AUTH_CONST.__objc_const: 0x95a0
+  __AUTH_CONST.__cfstring: 0x19c0
+  __AUTH_CONST.__objc_const: 0x8988
   __AUTH_CONST.__objc_intobj: 0x1f8
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x2b0
+  __AUTH.__objc_data: 0x550
+  __DATA.__objc_ivar: 0x2b8
   __DATA.__data: 0xbe8
-  __DATA.__bss: 0x400
-  __DATA_DIRTY.__objc_data: 0x18b0
-  __DATA_DIRTY.__bss: 0xe8
+  __DATA.__bss: 0x420
+  __DATA_DIRTY.__objc_data: 0x15e0
+  __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1429
-  Symbols:   1825
-  CStrings:  2048
+  Functions: 1471
+  Symbols:   1872
+  CStrings:  2077
 
Symbols:
+ _OBJC_CLASS_$_LACCachedExternalizedContext
+ _os_unfair_lock_assert_owner
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- _LACPolicyOptionAllowEnablementGracePeriod
- _OBJC_CLASS_$_LACDTORatchetState
- _OBJC_CLASS_$_LACachedExternalizedContext
- _dispatch_assert_queue$V2
CStrings:
+ "\x05\x11"
+ "@\"LACCachedExternalizedContext\""
+ "Helper context invalidated"
+ "LACContextCallbackXPC"
+ "LACContextExternalizing"
+ "LAEnvironment notification queue"
+ "T@\"LACCachedExternalizedContext\",&,V_cachedExternalizedContext"
+ "_handleDarwinNotification"
+ "_notificationQueue"
+ "_stateLock"
+ "analyticsAction:%d dismissing:%d on %{public}@ cid:%u"
+ "analyticsAction:%d on %{public}@ cid:%u returned %{public}@"
+ "analyticsAction:dismissing:"
+ "analyticsAction:dismissing:reply:"
+ "analyticsMechanism:%d result: %{public}@ on %{public}@ cid:%u returned %{public}@"
+ "analyticsMechanism:%d result:%{public}@ on %{public}@ cid:%u"
+ "analyticsMechanism:%d starting:%d on %{public}@ cid:%u"
+ "analyticsMechanism:%d starting:%d on %{public}@ cid:%u returned %{public}@"
+ "analyticsMechanism:result:"
+ "analyticsMechanism:result:reply:"
+ "analyticsMechanism:starting:"
+ "analyticsMechanism:starting:reply:"
+ "analyticsSessionStarting:%d dialogID:%{public}@ bundleID:%{private}@ on %{public}@ cid:%u"
+ "analyticsSessionStarting:%d on %{public}@ cid:%u returned %{public}@"
+ "analyticsSessionStarting:dialogID:bundleID:"
+ "analyticsSessionStarting:dialogID:bundleID:reply:"
+ "dictionaryForKey:"
+ "dictionaryForKey:completionHandler:"
+ "dictionaryForKey:error:"
+ "setDictionary:forKey:completionHandler:"
+ "setDictionary:forKey:error:"
+ "v28@0:8q16B24"
+ "v36@0:8B16@20@28"
+ "v44@0:8B16@\"NSString\"20@\"NSString\"28@?<v@?B@\"NSError\">36"
+ "v44@0:8B16@20@28@?36"
+ "v48@0:8@\"NSData\"16@\"<LACContextCallbackXPC>\"24Q32@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">40"
+ "v64@0:8@\"NSUUID\"16@\"<LACContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "\x04\x11"
- "@\"LACachedExternalizedContext\""
- "LAContextCallbackXPC"
- "LAContextExternalizationProt"
- "T@\"LACachedExternalizedContext\",&,V_cachedExternalizedContext"
- "optionAllowEnablementGracePeriod"
- "setOptionAllowEnablementGracePeriod:"
- "v48@0:8@\"NSData\"16@\"<LAContextCallbackXPC>\"24Q32@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">40"
- "v64@0:8@\"NSUUID\"16@\"<LAContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56"

```
