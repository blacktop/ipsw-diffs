## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

-210.3.1.0.0
-  __TEXT.__text: 0x26d238
+210.5.1.0.0
+  __TEXT.__text: 0x26d800
   __TEXT.__auth_stubs: 0x1ef0
-  __TEXT.__objc_methlist: 0x464c
-  __TEXT.__cstring: 0x3b6fe
-  __TEXT.__const: 0x1aa8
+  __TEXT.__objc_methlist: 0x467c
+  __TEXT.__cstring: 0x3b7c8
+  __TEXT.__const: 0x1ab8
   __TEXT.__gcc_except_tab: 0x22d0
-  __TEXT.__oslogstring: 0x59b20
+  __TEXT.__oslogstring: 0x59cd8
   __TEXT.__dlopen_cstrs: 0x5bd
   __TEXT.__unwind_info: 0x4320
   __TEXT.__objc_classname: 0x4d1
-  __TEXT.__objc_methname: 0x1209b
+  __TEXT.__objc_methname: 0x121b0
   __TEXT.__objc_methtype: 0x1b96
-  __TEXT.__objc_stubs: 0xb200
+  __TEXT.__objc_stubs: 0xb280
   __DATA_CONST.__got: 0xa08
-  __DATA_CONST.__const: 0x63d0
+  __DATA_CONST.__const: 0x63e0
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3020
+  __DATA_CONST.__objc_selrefs: 0x3040
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0xf90
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x3988
-  __AUTH_CONST.__cfstring: 0x17660
-  __AUTH_CONST.__objc_const: 0x7a78
+  __AUTH_CONST.__cfstring: 0x17740
+  __AUTH_CONST.__objc_const: 0x7ad8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x460
   __AUTH.__data: 0x510
-  __DATA.__objc_ivar: 0x710
-  __DATA.__data: 0xed8
+  __DATA.__objc_ivar: 0x718
+  __DATA.__data: 0xee8
   __DATA.__bss: 0x18d0
   __DATA.__common: 0x598
   __DATA_DIRTY.__objc_data: 0x910

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5314
-  Symbols:   7829
-  CStrings:  13802
+  Functions: 5318
+  Symbols:   7837
+  CStrings:  13820
 
Symbols:
+ _kMXSessionProperty_PrefersNoInterruptions
+ _AVSystemController_VolumeButtonDeltaDidChangeNotificationParameter_VolumeDelta
+ _AVSystemController_VolumeButtonDeltaDidChangeNotification
+ _kMXSessionAudioMode_SpatialCapture
CStrings:
+ "hasEntitlementToSetPrefersNoInterruptions ="
+ "-[MXSessionManager(Utilities) getVolumeButtonDelta:outVolumeDelta:]"
+ "TB,N,V_hasEntitlementToSetPrefersNoInterruptions"
+ "_prefersNoInterruptions"
+ "_hasEntitlementToSetPrefersNoInterruptions"
+ "non-CFBoolean PrefersNoInterruptions"
+ "-CMSessionMgr- %!s(MISSING): Client '%!{(MISSING)public}@' does not have entitlement to set PrefersNoInterruptions"
+ "SpatialCapture"
+ "PrefersNoInterruptions"
+ "-CMSessionMgr- %!s(MISSING): Session '%!{(MISSING)public}@' setting PrefersNoInterruptions to %!{(MISSING)BOOL}u"
+ "PrefersNoInterruptions ="
+ "Aug 29 2024"
+ "setPrefersNoInterruptions:"
+ "systemController_GetVolumeButtonDelta"
+ "VolumeButtonDeltaDidChange"
+ "TB,N,V_prefersNoInterruptions"
+ "23:32:15"
+ "-CMSessionMgr- %!s(MISSING): Session '%!{(MISSING)public}@' cannot change PrefersNoInterruptions because it is active"
+ "-CMSUtilities- %!s(MISSING): NOT going to interrupt because: interruptor '%!{(MISSING)public}@' prefersNoInterruptions = %!{(MISSING)BOOL}u, victim '%!{(MISSING)public}@' prefersNoInterruptions = %!{(MISSING)BOOL}u"
+ "setHasEntitlementToSetPrefersNoInterruptions:"
+ "-MXSessionManagerUtilities- %!s(MISSING): Volume button client session: %!{(MISSING)public}@, category: %!{(MISSING)public}@, isActive: %!{(MISSING)BOOL}u, outVolumeDelta = %!f(MISSING)"
+ "getVolumeButtonDelta:outVolumeDelta:"
+ "hasEntitlementToSetPrefersNoInterruptions"
+ "remoteSystemController_GetVolumeButtonDelta"
+ "com.apple.private.mediaexperience.prefersnointerruptions.allow"
+ "prefersNoInterruptions"
- "VolumeChange"
- "getVolumeButtonChangeValue:outVolumeChange:"
- "00:40:40"
- "systemController_GetVolumeButtonChangeValue"
- "remoteSystemController_GetVolumeButtonChangeValue"
- "-[MXSessionManager(Utilities) getVolumeButtonChangeValue:outVolumeChange:]"
- "Aug 16 2024"
- "-MXSessionManagerUtilities- %!s(MISSING): Volume button client session: %!{(MISSING)public}@, category: %!{(MISSING)public}@, isActive: %!{(MISSING)BOOL}u, outVolumeChange = %!f(MISSING)"

```
