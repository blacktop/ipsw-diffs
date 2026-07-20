## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/Versions/A/MediaExperience`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__lazy_load_got`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-360.66.1.0.0
-  __TEXT.__text: 0xbb098
+360.70.2.0.0
+  __TEXT.__text: 0xbb4d4
   __TEXT.__delay_helper: 0xdc
   __TEXT.__lazy_helpers: 0xa8
   __TEXT.__objc_methlist: 0x1e14
   __TEXT.__const: 0x1e8
-  __TEXT.__cstring: 0x17245
-  __TEXT.__oslogstring: 0x17bc2
+  __TEXT.__cstring: 0x17252
+  __TEXT.__oslogstring: 0x17d19
   __TEXT.__gcc_except_tab: 0x1340
   __TEXT.__dlopen_cstrs: 0x16e
-  __TEXT.__unwind_info: 0x1bb0
+  __TEXT.__unwind_info: 0x1bc8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2758
+  __DATA_CONST.__const: 0x2760
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1338
+  __DATA_CONST.__objc_selrefs: 0x1340
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__got: 0x7d8
   __AUTH_CONST.__const: 0x23c0
-  __AUTH_CONST.__cfstring: 0xafe0
+  __AUTH_CONST.__cfstring: 0xb000
   __AUTH_CONST.__objc_const: 0x3308
   __AUTH_CONST.__lazy_load_got: 0x8
   __AUTH_CONST.__objc_dictobj: 0x118

   __DATA.__objc_ivar: 0x2b4
   __DATA.__data: 0x3b4
   __DATA.__common: 0x220
-  __DATA.__bss: 0x3a0
+  __DATA.__bss: 0x3b0
   __DATA_DIRTY.__objc_data: 0x528
-  __DATA_DIRTY.__bss: 0x74c
+  __DATA_DIRTY.__bss: 0x73c
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3007
-  Symbols:   5293
-  CStrings:  3870
+  Functions: 3014
+  Symbols:   5301
+  CStrings:  3874
 
Symbols:
+ _FigXPCCommonServerTimeoutHandler
+ _figXPC_ServerTimeout_EndpointUIAgent
+ _figXPC_ServerTimeout_FigSystemController
+ _figXPC_ServerTimeout_FigVolumeController
+ _figXPC_ServerTimeout_RouteDiscoverer
+ _figXPC_ServerTimeout_RoutingContext
+ _kFigEndpointUIAgentPromptInfo_FailureDetails_MediaAppName
+ _objc_msgSend$setWithArray:
Functions:
~ _FigEndpointUIAgentStartServer : 464 -> 488
+ _figXPC_ServerTimeout_EndpointUIAgent
~ ___FigRoutingManagerContextUtilities_ResetCurrentlyActivatingSubEndpointsInfo_block_invoke : 732 -> 1056
~ __routingContextUtilities_checkActivationTimeout : 744 -> 1104
+ _figXPC_ServerTimeout_FigSystemController
~ _FigRoutingContextStartServer : 272 -> 296
+ _figXPC_ServerTimeout_RoutingContext
~ _FigVolumeControllerStartServer : 524 -> 548
+ _figXPC_ServerTimeout_FigVolumeController
~ _FigRouteDiscovererStartServer : 300 -> 324
+ _figXPC_ServerTimeout_RouteDiscoverer
~ _OUTLINED_FUNCTION_6 : 40 -> 20
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_19
- _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_32
~ _FigSystemControllerStartServer : 432 -> 452
~ -[MXCoreSession updateDeviceUUIDs:] : 1380 -> 1552
~ -[MXCoreSession updateInterruptionStyle:] : 852 -> 828
CStrings:
+ "-FigRoutingManagerContextUtilities- %s: Activation timeout - removing stale entry and posting EndedFailed for uuid=%{public}@"
+ "-FigRoutingManagerContextUtilities- %s: Posting coalesced notification for original SET operation (entryOptions=%{public}@)"
+ "-FigRoutingManagerContextUtilities- %s: picking timer fired for '%@' '%@' (pickingState=%u)"
+ "-MXCoreSession- %s: deviceUUIDs unchanged (%@), skipping update and hijack"
+ "22:02:36"
+ "Jul 10 2026"
+ "MediaAppName"
- "-FigRoutingManagerContextUtilities- %s: picking timer fired for '%@' '%@'"
- "23:32:22"
- "Jun 25 2026"
```
