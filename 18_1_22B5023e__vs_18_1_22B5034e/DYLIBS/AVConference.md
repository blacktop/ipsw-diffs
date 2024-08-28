## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2055.64.1.1.2
-  __TEXT.__text: 0x6b6930
-  __TEXT.__auth_stubs: 0x4fc0
-  __TEXT.__objc_methlist: 0x2d8d8
+2085.3.1.0.0
+  __TEXT.__text: 0x6b743c
+  __TEXT.__auth_stubs: 0x4fd0
+  __TEXT.__objc_methlist: 0x2d940
   __TEXT.__const: 0x7dd0
-  __TEXT.__cstring: 0x7f5d4
-  __TEXT.__oslogstring: 0xec3b1
+  __TEXT.__cstring: 0x7f672
+  __TEXT.__oslogstring: 0xec52c
   __TEXT.__gcc_except_tab: 0x253c
   __TEXT.__ustring: 0x144
-  __TEXT.__unwind_info: 0xd130
+  __TEXT.__unwind_info: 0xd140
   __TEXT.__objc_classname: 0x4777
-  __TEXT.__objc_methname: 0x71867
-  __TEXT.__objc_methtype: 0x2455f
-  __TEXT.__objc_stubs: 0x47ba0
+  __TEXT.__objc_methname: 0x7199f
+  __TEXT.__objc_methtype: 0x2456b
+  __TEXT.__objc_stubs: 0x47c40
   __DATA_CONST.__got: 0x18d8
   __DATA_CONST.__const: 0x6128
   __DATA_CONST.__objc_classlist: 0x1178
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x438
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14878
+  __DATA_CONST.__objc_selrefs: 0x148a0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0xfa0
   __DATA_CONST.__objc_arraydata: 0x2070
-  __AUTH_CONST.__auth_got: 0x27f8
+  __AUTH_CONST.__auth_got: 0x2800
   __AUTH_CONST.__auth_ptr: 0xc8
   __AUTH_CONST.__const: 0x3370
   __AUTH_CONST.__cfstring: 0x22580
-  __AUTH_CONST.__objc_const: 0x611c0
+  __AUTH_CONST.__objc_const: 0x61258
   __AUTH_CONST.__objc_intobj: 0x4560
   __AUTH_CONST.__objc_arrayobj: 0x1710
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x160
   __AUTH_CONST.__objc_dictobj: 0x2d0
-  __DATA.__objc_ivar: 0x6350
+  __DATA.__objc_ivar: 0x6360
   __DATA.__data: 0x7430
   __DATA.__bss: 0xb60
   __DATA.__common: 0x55

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 27738
-  Symbols:   32450
-  CStrings:  47155
+  Functions: 27749
+  Symbols:   32461
+  CStrings:  47175
 
Symbols:
+ _os_unfair_lock_assert_owner
CStrings:
+ "-[VCConnectionStatisticsCollector startPeriodicUpdateHistory:withCopyPacketCountCallback:]"
+ " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) Prewarming captions"
+ "+[VCAudioCaptions captionsSupportedWithErrorCode:]"
+ "createNewConnectionStatsCollectorCallback"
+ " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) Speech framework not properly soft linked."
+ " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) Could not register streamToken=%!l(MISSING)d for captions, invalidated=%!{(MISSING)BOOL}d"
+ " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) Failed to prewarm captions with error=%!@(MISSING)"
+ " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) %!@(MISSING)(%!p(MISSING)) Prewarming captions"
+ "releaseAndRemoveConnectionStatsCollectorCallback"
+ " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) invalidate called several times by client"
+ "captionsSupportedWithErrorCode:"
+ "-[VCAudioCaptionsCoordinator invalidate]"
+ "_copyPacketCountCallbackRecv"
+ " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) %!@(MISSING)(%!p(MISSING)) Could not register streamToken=%!l(MISSING)d for captions, invalidated=%!{(MISSING)BOOL}d"
+ " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) Captions is hardware restricted"
+ " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) %!@(MISSING)(%!p(MISSING)) Failed to prewarm captions with error=%!@(MISSING)"
+ "_invalidated"
+ "lockedCaptionsEnabled"
+ "deallocCopyPacketCountCallBack:"
+ "B24@0:8^q16"
+ "2085.3.1"
+ "lockedEnableCaptions:"
+ " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) %!@(MISSING)(%!p(MISSING)) invalidate called several times by client"
+ "-[VCAudioCaptions prewarmCaptions]_block_invoke"
+ "prewarmCaptions"
+ "_isPrewarmed"
+ "startPeriodicUpdateHistory:withCopyPacketCountCallback:"
+ "_copyPacketCountCallbackSend"
+ "_connectionStatsCollectorCallback"
+ "copyCopyPacketCountCallbackForOutgoing:withCallback:"
- "registerCopyPacketCountCallback:"
- "_copyPacketCountCallback"
- " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) %!@(MISSING)(%!p(MISSING)) Could not register streamToken=%!l(MISSING)d for captions"
- " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) Speech framework not loaded for captioning feature"
- "2055.64.1.1.2"
- "-[VCConnectionStatisticsCollector registerCopyPacketCountCallback:]"
- " [%!s(MISSING)] %!s(MISSING):%!d(MISSING) Could not register streamToken=%!l(MISSING)d for captions"
- "deregisterCopyPacketCountCallBack"
- "startPeriodicUpdateHistory:"

```
