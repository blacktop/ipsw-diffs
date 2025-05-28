## CoreMediaIO

> `/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO`

```diff

-5510.0.0.0.0
-  __TEXT.__text: 0x43c90
-  __TEXT.__auth_stubs: 0xdc0
+5514.7.0.0.0
+  __TEXT.__text: 0x43efc
+  __TEXT.__auth_stubs: 0xdd0
   __TEXT.__objc_methlist: 0x1bf4
   __TEXT.__const: 0x7c
   __TEXT.__gcc_except_tab: 0x126c
-  __TEXT.__cstring: 0x804e
-  __TEXT.__oslogstring: 0x3cb0
+  __TEXT.__cstring: 0x80d9
+  __TEXT.__oslogstring: 0x3d49
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__unwind_info: 0xbc4
   __TEXT.__objc_classname: 0x395

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x3148
   __DATA_CONST.__objc_selrefs: 0xee8
-  __AUTH_CONST.__cfstring: 0x1da0
+  __AUTH_CONST.__cfstring: 0x1dc0
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__auth_got: 0x6f0
+  __AUTH_CONST.__auth_got: 0x6f8
   __DATA.__objc_classrefs: 0x150
   __DATA.__objc_superrefs: 0xd0
   __DATA.__objc_ivar: 0x354
   __DATA.__data: 0x4b8
   __DATA.__bss: 0x70
-  __DATA.__common: 0x9
+  __DATA.__common: 0x15
   __DATA_DIRTY.__const: 0x280
   __DATA_DIRTY.__objc_const: 0xdc8
   __DATA_DIRTY.__objc_data: 0x820

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1343
-  Symbols:   4094
-  CStrings:  1876
+  Symbols:   4097
+  CStrings:  1880
 
Symbols:
+ _FigGetUpTimeNanoseconds
+ ___63-[CMIOExtensionProvider startStreamForClientID:streamID:reply:]_block_invoke.434
+ ___63-[CMIOExtensionProvider startStreamForClientID:streamID:reply:]_block_invoke.436
+ ___67-[CMIOExtensionProvider consumeSampleBufferForStream:client:reply:]_block_invoke.450
+ ___81-[CMIOExtensionProvider setPluginPropertyValuesForClientID:propertyValues:reply:]_block_invoke.415
+ ___86-[CMIOExtensionProvider enqueueReactionEffectForClientID:streamID:reactionType:reply:]_block_invoke.444
+ ___90-[CMIOExtensionProvider setDevicePropertyValuesForClientID:deviceID:propertyValues:reply:]_block_invoke.426
+ ___90-[CMIOExtensionProvider setStreamPropertyValuesForClientID:streamID:propertyValues:reply:]_block_invoke.430
+ ___91-[CMIOExtensionProvider captureAsyncStillImageForClientID:streamID:uniqueID:options:reply:]_block_invoke.441
+ ___98-[CMIOExtensionProvider _performDeferredStreamStartsForClient:streamID:requestVideo:requestAudio:]_block_invoke.437
+ ___98-[CMIOExtensionProvider _performDeferredStreamStartsForClient:streamID:requestVideo:requestAudio:]_block_invoke.437.cold.1
+ _sMostRecentProprietaryDefaultDomainLookupTimeByPID
+ _sPostTerminationTimoutForClearingEntryFromProprietaryDefaultsDomainsByPID
- ___63-[CMIOExtensionProvider startStreamForClientID:streamID:reply:]_block_invoke.431
- ___63-[CMIOExtensionProvider startStreamForClientID:streamID:reply:]_block_invoke.433
- ___67-[CMIOExtensionProvider consumeSampleBufferForStream:client:reply:]_block_invoke.447
- ___81-[CMIOExtensionProvider setPluginPropertyValuesForClientID:propertyValues:reply:]_block_invoke.412
- ___86-[CMIOExtensionProvider enqueueReactionEffectForClientID:streamID:reactionType:reply:]_block_invoke.441
- ___90-[CMIOExtensionProvider setDevicePropertyValuesForClientID:deviceID:propertyValues:reply:]_block_invoke.423
- ___90-[CMIOExtensionProvider setStreamPropertyValuesForClientID:streamID:propertyValues:reply:]_block_invoke.427
- ___91-[CMIOExtensionProvider captureAsyncStillImageForClientID:streamID:uniqueID:options:reply:]_block_invoke.438
- ___98-[CMIOExtensionProvider _performDeferredStreamStartsForClient:streamID:requestVideo:requestAudio:]_block_invoke.434
- ___98-[CMIOExtensionProvider _performDeferredStreamStartsForClient:streamID:requestVideo:requestAudio:]_block_invoke.434.cold.1
CStrings:
+ "%s:%d:%s [%{private}d] dropping stale pid; last accessed %lld seconds ago"
+ "%s:%d:%s [%{private}d] keeping stale pid because it was accessed %lld seconds ago"
+ "%s:%d:%s stale pid timeout: %d seconds"
+ "+[CMIOExtensionProvider proprietaryDefaultsDomainForAuditToken:]_block_invoke"
+ "proprietary_default_domain_most_recent_pid_lookup_time_limit"
- "%s:%d:%s [%{private}d] dropping stale pid"

```
