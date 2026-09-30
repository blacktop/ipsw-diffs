## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

-3401.13.1.0.0
-  __TEXT.__text: 0x157654
+3401.17.1.0.0
+  __TEXT.__text: 0x157d24
   __TEXT.__auth_stubs: 0x1c20
-  __TEXT.__objc_methlist: 0x13170
+  __TEXT.__objc_methlist: 0x131e8
   __TEXT.__const: 0x5c0
-  __TEXT.__gcc_except_tab: 0x3754
-  __TEXT.__cstring: 0x270d1
-  __TEXT.__oslogstring: 0x1f681
+  __TEXT.__gcc_except_tab: 0x378c
+  __TEXT.__cstring: 0x27177
+  __TEXT.__oslogstring: 0x1f741
   __TEXT.__dlopen_cstrs: 0x197
-  __TEXT.__unwind_info: 0x4ed0
+  __TEXT.__unwind_info: 0x4ee0
   __TEXT.__objc_classname: 0x2f3f
-  __TEXT.__objc_methname: 0x37ea2
+  __TEXT.__objc_methname: 0x380aa
   __TEXT.__objc_methtype: 0x7c85
-  __TEXT.__objc_stubs: 0x1bf00
-  __DATA_CONST.__got: 0x1a80
-  __DATA_CONST.__const: 0x4108
+  __TEXT.__objc_stubs: 0x1bfa0
+  __DATA_CONST.__got: 0x1a88
+  __DATA_CONST.__const: 0x4128
   __DATA_CONST.__objc_classlist: 0x858
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x4a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa660
+  __DATA_CONST.__objc_selrefs: 0xa6b8
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x698
   __DATA_CONST.__objc_arraydata: 0x438
   __AUTH_CONST.__auth_got: 0xe28
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x1e00
-  __AUTH_CONST.__cfstring: 0x8f60
-  __AUTH_CONST.__objc_const: 0x256e8
+  __AUTH_CONST.__const: 0x1e20
+  __AUTH_CONST.__cfstring: 0x8fa0
+  __AUTH_CONST.__objc_const: 0x257d0
   __AUTH_CONST.__objc_intobj: 0xa38
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_floatobj: 0x4c0
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __DATA.__objc_ivar: 0x1a74
+  __DATA.__objc_ivar: 0x1a84
   __DATA.__data: 0x3710
-  __DATA.__bss: 0x670
+  __DATA.__bss: 0x678
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x5370
   __DATA_DIRTY.__data: 0xc0
-  __DATA_DIRTY.__bss: 0x188
+  __DATA_DIRTY.__bss: 0x180
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8285
-  Symbols:   10072
-  CStrings:  14479
+  Functions: 8296
+  Symbols:   10084
+  CStrings:  14502
 
Symbols:
+ _OBJC_CLASS_$_CSPreventSystemSleepPowerAssertion
CStrings:
+ "setNearMissDelayTimeoutInSamples:"
+ "%!s(MISSING) Detected near miss candidate at %!{(MISSING)public}tu, let's wait %!{(MISSING)public}tu samples to log"
+ "%!s(MISSING) Failed to cancel notification (%!@(MISSING)), status: %!u(MISSING)"
+ "com.apple.MobileAsset.AutoAssetNotification^com.apple.MobileAsset.MAAutoAsset^STARTUP_ACTIVATED"
+ "TQ,N,V_nearMissDelayTimeoutInSamples"
+ "%!s(MISSING) Waiting for logging near miss until timeout %!{(MISSING)public}lu samples"
+ "%!s(MISSING) Failed to register for notification (%!@(MISSING)), status: %!u(MISSING)"
+ "initWithTimeOut:"
+ "_nearMissCandidateDetectedSamples"
+ "TQ,N,V_nearMissCandidateDetectedSamples"
+ "-[CSEndpointerAssetManager dealloc]_block_invoke"
+ "setNearMissCandidateDetectedSamples:"
+ "loggingThreshold"
+ "nearMissDelayTimeoutInSamples"
+ "selfTriggerDetector:didDetectNearMiss:"
+ "v32@?0@\"NSString\"8@\"NSNumber\"16^B24"
+ "_hasPendingNearMiss"
+ "TB,N,V_hasPendingNearMiss"
+ "setHasPendingNearMiss:"
+ "hasPendingNearMiss"
+ "-selfTriggerNearMiss"
+ "isSelfTriggerNearMissAudioLoggingEnabled"
+ "_tokenForAssetUpdateNotification"
+ "nearMissCandidateDetectedSamples"
+ "_nearMissDelayTimeoutInSamples"
+ "_logSelfTriggerAudioWithPrefix:result:"
+ "%!s(MISSING) SelfTrigger detected near miss at %!l(MISSING)u samples with score %!f(MISSING)"
- "-[CSEndpointerAssetManager dealloc]"
- "%!s(MISSING) Failed to register for asset update notifications, status: %!u(MISSING)"
- "_assetUpdateNotificationToken"
- "%!s(MISSING) Failed to deregister for asset update notifications, status: %!u(MISSING)"

```
