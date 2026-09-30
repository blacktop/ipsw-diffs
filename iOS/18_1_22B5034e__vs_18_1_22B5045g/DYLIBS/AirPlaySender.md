## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-830.4.1.0.0
-  __TEXT.__text: 0x1c71e0
-  __TEXT.__auth_stubs: 0x5020
+830.6.1.0.0
+  __TEXT.__text: 0x1c8464
+  __TEXT.__auth_stubs: 0x5060
   __TEXT.__objc_methlist: 0x340
-  __TEXT.__cstring: 0x71f43
-  __TEXT.__const: 0xfd30
-  __TEXT.__gcc_except_tab: 0x3d8
+  __TEXT.__cstring: 0x72429
+  __TEXT.__const: 0xfd80
+  __TEXT.__gcc_except_tab: 0x3fc
   __TEXT.__oslogstring: 0x69f
-  __TEXT.__unwind_info: 0x2a88
+  __TEXT.__unwind_info: 0x2ab0
   __TEXT.__eh_frame: 0xaa8
   __TEXT.__objc_classname: 0x174
   __TEXT.__objc_methname: 0x19a5
   __TEXT.__objc_methtype: 0xa56
   __TEXT.__objc_stubs: 0x1760
   __DATA_CONST.__got: 0x1d20
-  __DATA_CONST.__const: 0x5e78
+  __DATA_CONST.__const: 0x5f08
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x680
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x2820
+  __AUTH_CONST.__auth_got: 0x2840
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x79c0
-  __AUTH_CONST.__cfstring: 0x10bc0
+  __AUTH_CONST.__const: 0x79e0
+  __AUTH_CONST.__cfstring: 0x10c20
   __AUTH_CONST.__objc_const: 0x1178
   __AUTH.__objc_data: 0xf0
-  __AUTH.__data: 0x608
+  __AUTH.__data: 0x720
   __DATA.__objc_ivar: 0x64
-  __DATA.__data: 0x18390
+  __DATA.__data: 0x18440
   __DATA.__bss: 0x9b0
   __DATA.__common: 0xa04
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3331
-  Symbols:   6262
-  CStrings:  9730
+  Functions: 3343
+  Symbols:   6279
+  CStrings:  9759
 
Symbols:
+ _FigInstallSysdiagnoseBlock
+ _CFStringAppendV
+ _APSHierarchyReporterProtocolGetProtocolID
+ _CFStringCreateV
+ _kAPEndpointManagerProperty_HierarchyDump
CStrings:
+ "Sysdiagnose signal detected: Dumping APEndpoint Hierarchy..."
+ "OSStatus manager_create(CFDictionaryRef, FigEndpointManagerRef *)_block_invoke_3"
+ "830.6.1"
+ "Endpoint:[%!{(MISSING)ptr}] (Local) %!'(MISSING)'@ Parent:[%!{(MISSING)ptr}]\n"
+ "manager_copyHierarchy"
+ "airPlayDebugIPC_showEndpointManagerHierarchy"
+ "manager_DumpHierarchy"
+ "apsession_DumpHierarchy"
+ "endpoint_DumpHierarchy"
+ "+-+ APEndpoint Hierarchy Dump +-+\n\n"
+ "Endpoint:[%!{(MISSING)ptr}] (%!s(MISSING)) %!'(MISSING)'@ Parent:[%!{(MISSING)ptr}]\n"
+ "APEndpointManagerDump"
+ "void endpoint_reportPlaybackMetrics(FigEndpointRef, FigEndpointPlaybackSessionRef, APSRTCReportingAgentRef, CFDictionaryRef)"
+ "[Error] Object:[%!{(MISSING)ptr}]%!?(MISSING)s%!?(MISSING)''@ cannot be dumped (error %!m(MISSING)) Parent:[%!{(MISSING)ptr}]\n"
+ "endpointLocal_DumpHierarchy"
+ "ClusterEndpoint:[%!{(MISSING)ptr}] (%!s(MISSING) %!@(MISSING)) %!'(MISSING)'@ Parent:[%!{(MISSING)ptr}]\n"
+ "manager_copyHierarchy_block_invoke"
+ "EndpointManager:[%!{(MISSING)ptr}] (AirPlay)\n"
+ "%!(BADWIDTH)%!s(MISSING)"
+ "APEndpointHierarchy"
+ "SenderSession:[%!{(MISSING)ptr}] Parent:[%!{(MISSING)ptr}]\n"
+ "void endpoint_invalidatePlaybackSession(FigEndpointPlaybackSessionRef, FigEndpointRef, APSRTCReportingAgentRef, CFDictionaryRef)"
+ "i24@?0q8r*16"
+ "[%!{(MISSING)ptr}] ### Get IsActivated for endpoint [%!{(MISSING)ptr}] failed (%!m(MISSING))\n"
+ "endpointCluster_DumpHierarchy"
+ "%!(BADWIDTH)%!s(MISSING)%!@(MISSING)"
+ "manager_create_block_invoke_4"
+ "hierarchy"
+ "OSStatus manager_create(CFDictionaryRef, FigEndpointManagerRef *)_block_invoke_4"
+ "OSStatus manager_DumpHierarchy(APSHierarchyReporterRef, void *, CFIndex, CFStringRef, APSHierarchyReporterDumpCallback)"
+ "HierarchyDump"
+ "[%!{(MISSING)ptr}] Failed to copy property %!@(MISSING) with error %!m(MISSING)"
- "void endpoint_reportPlaybackMetrics(FigEndpointRef, FigEndpointPlaybackSessionRef)"
- "void endpoint_invalidatePlaybackSession(const void *, void *)"
- "830.4.1"

```
