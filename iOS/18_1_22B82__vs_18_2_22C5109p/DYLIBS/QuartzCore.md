## QuartzCore

> `/System/Library/Frameworks/QuartzCore.framework/QuartzCore`

```diff

-1149.20.0.0.0
-  __TEXT.__text: 0x3171c4
-  __TEXT.__auth_stubs: 0x5210
-  __TEXT.__objc_methlist: 0x955c
-  __TEXT.__const: 0x15b20
-  __TEXT.__gcc_except_tab: 0x6db8
-  __TEXT.__cstring: 0x2b1d3
-  __TEXT.__oslogstring: 0xebdc
+1150.9.0.0.0
+  __TEXT.__text: 0x31bdc0
+  __TEXT.__auth_stubs: 0x5240
+  __TEXT.__objc_methlist: 0x95bc
+  __TEXT.__const: 0x15d10
+  __TEXT.__gcc_except_tab: 0x6e84
+  __TEXT.__cstring: 0x2b441
+  __TEXT.__oslogstring: 0xece9
   __TEXT.__dlopen_cstrs: 0xe0
-  __TEXT.__unwind_info: 0x7d60
+  __TEXT.__unwind_info: 0x7dc0
   __TEXT.__eh_frame: 0x108
   __TEXT.__objc_classname: 0xcbb
-  __TEXT.__objc_methname: 0xef14
-  __TEXT.__objc_methtype: 0x3567
-  __TEXT.__objc_stubs: 0xc360
-  __DATA_CONST.__got: 0xd58
-  __DATA_CONST.__const: 0xe758
+  __TEXT.__objc_methname: 0xf070
+  __TEXT.__objc_methtype: 0x3568
+  __TEXT.__objc_stubs: 0xc420
+  __DATA_CONST.__got: 0xd68
+  __DATA_CONST.__const: 0xe778
   __DATA_CONST.__objc_classlist: 0x3c8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e18
+  __DATA_CONST.__objc_selrefs: 0x4ea0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_arraydata: 0x37d0
-  __AUTH_CONST.__auth_got: 0x2920
+  __AUTH_CONST.__auth_got: 0x2938
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x13f20
-  __AUTH_CONST.__cfstring: 0x15080
-  __AUTH_CONST.__objc_const: 0xd6d0
+  __AUTH_CONST.__const: 0x14060
+  __AUTH_CONST.__cfstring: 0x15120
+  __AUTH_CONST.__objc_const: 0xd740
   __AUTH_CONST.__objc_dictobj: 0x320
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_intobj: 0x4278

   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1130
   __AUTH.__data: 0x40
-  __DATA.__objc_ivar: 0x55c
+  __DATA.__objc_ivar: 0x564
   __DATA.__data: 0x1390
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x3e40
+  __DATA.__bss: 0x6500
   __DATA.__common: 0xc
   __DATA_DIRTY.__objc_data: 0x14a0
   __DATA_DIRTY.__data: 0x580
-  __DATA_DIRTY.__bss: 0x2f78
+  __DATA_DIRTY.__bss: 0x2fd8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 10924
-  Symbols:   13202
-  CStrings:  11634
+  Functions: 10955
+  Symbols:   13237
+  CStrings:  11675
 
Symbols:
+ _CAXPCImageQueueSampleIsLowLatency
+ _CGImageGetContentHeadroom
+ _IOMobileFramebufferSwapSetIndicatorBrightnessLimit
+ _IOMobileFramebufferSwapSetSecureAnimation
+ _SILManagerIndicatorValidPositions
+ _SILManagerSwapEnd
- _SILManagerRelease
- _objc_release_x28
- _objc_retain_x25
CStrings:
+ "\tcurrent EDR: %!g(MISSING), potential EDR: %!g(MISSING)\n"
+ "!indicators.empty ()"
+ "%!g(MISSING), %!g(MISSING), "
+ "%!g(MISSING), %!g(MISSING)]\n"
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)"
+ "22C5109h"
+ "CASecureIndicatorLayerInvalidName"
+ "CASecureIndicatorLayerValidPositionsForIndicator: name can't be nil"
+ "CA_COLOR_SECURE_INDICATOR_VALID_REGIONS"
+ "CA_RECORD_SECURE_INDICATOR_POSITIONS"
+ "CA_TRACE_CLIENT_INFO"
+ "Display %!u(MISSING) setting indicator brightness limit to %!g(MISSING) return: 0x%!x(MISSING)\n"
+ "Failed to turn off all regions !"
+ "IOMFBHotplugKeysChangedKey"
+ "Invalid indicator name %!@(MISSING)"
+ "Ramp %!d(MISSING): Setting SDR brightness to %!g(MISSING) nits, headroom to %!g(MISSING), limit to %!g(MISSING), contrast enhancer to %!g(MISSING), low_amb_str to %!g(MISSING), high_amb_str to %!g(MISSING) indicator_nits to %!g(MISSING) indicator_limit to %!g(MISSING)"
+ "Recorded indicator positions for device of size [%!u(MISSING)x%!u(MISSING)]\n"
+ "SIL failed to query bounding boxes for valid indicator '%!s(MISSING)'"
+ "SIL failed to query display size from client"
+ "SILMgr::swap_region_private region: %!u(MISSING) indicator %!u(MISSING) pos: [%!f(MISSING) %!f(MISSING)] opacity: %!f(MISSING) rotation: %!f(MISSING)"
+ "Td,V_indicatorLimitBegin"
+ "Td,V_indicatorLimitEnd"
+ "Unsupported filter %!s(MISSING) for SIL"
+ "^{CAWindowServerDisplayImpl={Mutex={_opaque_pthread_mutex_t=q[56c]}}^{Server}{CABrightnessTransaction=fffffffffff{?=[9f]}fBBI}@?@@@@BB}"
+ "_indicatorLimitBegin"
+ "_indicatorLimitEnd"
+ "can_purge ()"
+ "forceTransitionToState:"
+ "getValue:"
+ "indicator %!u(MISSING) (normalized) : ["
+ "indicator %!u(MISSING) : ["
+ "indicatorLimitBegin"
+ "indicatorLimitEnd"
+ "purge_pipeline_state"
+ "setAllowsDynamicSystemOOTF:"
+ "setIndicatorBrightnessLimit:"
+ "setIndicatorLimitBegin:"
+ "setIndicatorLimitEnd:"
+ "setMaximum:"
+ "setMinimum:"
+ "setRectangle:"
+ "setStateTransitions:"
+ "validPositions"
- "%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)"
- "-[CASecureIndicatorLayer _copyRenderLayer:layerFlags:commitFlags:]"
- "22B71"
- "Ramp %!d(MISSING): Setting SDR brightness to %!g(MISSING) nits, headroom to %!g(MISSING), limit to %!g(MISSING), contrast enhancer to %!g(MISSING), low_amb_str to %!g(MISSING), high_amb_str to %!g(MISSING) indicator_nits to %!g(MISSING)"
- "SILMgr::swap_region_private region: %!u(MISSING) indicator %!u(MISSING) pos: [%!f(MISSING) %!f(MISSING)] opacity: %!f(MISSING)"
- "T@\"NSString\",&"
- "^{CAWindowServerDisplayImpl={Mutex={_opaque_pthread_mutex_t=q[56c]}}^{Server}{CABrightnessTransaction=ffffffffff{?=[9f]}fBBI}@?@@@@BB}"
- "_regions[region].opacity == 0.0f"
- "face id"
- "indicator_id_from_name"
- "indicators"

```
