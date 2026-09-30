## AssistantServices

> `/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices`

```diff

-3401.26.2.0.0
-  __TEXT.__text: 0x1a2424
-  __TEXT.__auth_stubs: 0x1530
-  __TEXT.__objc_methlist: 0x199fc
+3401.29.5.11.1
+  __TEXT.__text: 0x1a2884
+  __TEXT.__auth_stubs: 0x1540
+  __TEXT.__objc_methlist: 0x199dc
   __TEXT.__const: 0x458
   __TEXT.__gcc_except_tab: 0x2570
-  __TEXT.__cstring: 0x3b6bc
-  __TEXT.__oslogstring: 0xffca
+  __TEXT.__cstring: 0x3b77c
+  __TEXT.__oslogstring: 0xffe5
   __TEXT.__dlopen_cstrs: 0x42e
-  __TEXT.__unwind_info: 0x7a28
+  __TEXT.__unwind_info: 0x7a20
   __TEXT.__objc_classname: 0x4e2f
-  __TEXT.__objc_methname: 0x3a4e6
-  __TEXT.__objc_methtype: 0xa8ea
+  __TEXT.__objc_methname: 0x3a4e3
+  __TEXT.__objc_methtype: 0xa8d4
   __TEXT.__objc_stubs: 0x23e60
   __DATA_CONST.__got: 0x1610
   __DATA_CONST.__const: 0x8120

   __DATA_CONST.__objc_catlist: 0x290
   __DATA_CONST.__objc_protolist: 0x550
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbe68
+  __DATA_CONST.__objc_selrefs: 0xbe60
   __DATA_CONST.__objc_protorefs: 0x140
   __DATA_CONST.__objc_superrefs: 0xdb8
   __DATA_CONST.__objc_arraydata: 0x1fa8
-  __AUTH_CONST.__auth_got: 0xaa8
+  __AUTH_CONST.__auth_got: 0xab0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x3880
-  __AUTH_CONST.__cfstring: 0x268a0
-  __AUTH_CONST.__objc_const: 0x39cb8
+  __AUTH_CONST.__const: 0x38c0
+  __AUTH_CONST.__cfstring: 0x269c0
+  __AUTH_CONST.__objc_const: 0x39c98
   __AUTH_CONST.__objc_intobj: 0x2328
   __AUTH_CONST.__objc_dictobj: 0xb90
   __AUTH_CONST.__objc_arrayobj: 0x588
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x73f0
   __AUTH.__data: 0x2f0
-  __DATA.__objc_ivar: 0x2538
+  __DATA.__objc_ivar: 0x2534
   __DATA.__data: 0x4108
-  __DATA.__bss: 0x1300
+  __DATA.__bss: 0x1318
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x14a0
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11613
-  Symbols:   13808
-  CStrings:  18893
+  Functions: 11614
+  Symbols:   13810
+  CStrings:  18900
 
Symbols:
+ _AFHasOSEligibilityEntitlement
+ _AFIsChinaSKU
+ _AFSiriHeadphonesMonitorGetCurrentlySelectedAudioRoute
+ _os_eligibility_get_domain_answer
CStrings:
+ "!\x1e"
+ "%!s(MISSING) #DisableServerFallbackWhenMissingAsset: deviceSupportsSAE=%!u(MISSING), result=%!u(MISSING)"
+ "%!s(MISSING) Missing entitlements for os_eligibility lookup"
+ "%!s(MISSING) initializing AVSystemController's subscriptions due to: %!@(MISSING)"
+ "-[AFSiriHeadphonesMonitor initializeAVSystemControllerSubscriptions:]_block_invoke"
+ "AFDeviceSupportsDisablingServerFallbackWhenMissingAsset"
+ "AFIsChinaSKU_block_invoke"
+ "ExecuteOnRemoteRequest"
+ "Head Gestures Accept Gesture"
+ "Head Gestures Configuration"
+ "Head Gestures Enabled"
+ "Head Gestures Reject Gesture"
+ "Head Gestures Supported"
+ "InitiateHandoffOnCompanion"
+ "StartHandoffRequest"
+ "com.apple.private.security.storage.os_eligibility.readonly"
+ "initializeAVSystemControllerSubscriptions:"
+ "setStoredHeadGestureConfigurationForDevice:"
+ "storedHeadGestureConfigurationForDevice"
+ "yue"
+ "zh"
- "!\x1f"
- "%!s(MISSING) AVSystemController died, updating route availability"
- "%!s(MISSING) AVSystemController subscription complete"
- "%!s(MISSING) Extending request timeout to %!f(MISSING) seconds as IE is enabled"
- "-[AFSiriHeadphonesMonitor _init]_block_invoke_2"
- "-[AFSiriHeadphonesMonitor systemControllerDied:]_block_invoke"
- "@\"AVSystemController\""
- "_avSystemController"
- "_getCurrentAudioRoute:ringerSwitchState:"
- "_handleRingerStateChanged"
- "getCurrentAudioRoute"
- "init is not allowed, use +[AFSiriHeadphonesMonitor sharedMonitor]"
- "new is not allowed, use +[AFSiriHeadphonesMonitor sharedMonitor]"
- "systemControllerDied:"

```
