## IntelligenceFlowContextRuntime

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/IntelligenceFlowContextRuntime`

```diff

-3610.18.2.501.3
-  __TEXT.__text: 0x115614
+3610.25.4.551.4
+  __TEXT.__text: 0x120f88
   __TEXT.__objc_methlist: 0x6d4
-  __TEXT.__const: 0x4d80
-  __TEXT.__swift5_typeref: 0x2cbe
-  __TEXT.__swift5_fieldmd: 0x1348
-  __TEXT.__constg_swiftt: 0x1c10
+  __TEXT.__const: 0x5170
+  __TEXT.__swift5_typeref: 0x2f54
+  __TEXT.__swift5_fieldmd: 0x14a4
+  __TEXT.__constg_swiftt: 0x1cd0
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_reflstr: 0xdca
+  __TEXT.__swift5_reflstr: 0xea2
   __TEXT.__swift5_assocty: 0x220
   __TEXT.__swift5_protos: 0x44
-  __TEXT.__swift5_proto: 0x204
-  __TEXT.__swift5_types: 0x204
-  __TEXT.__cstring: 0x20ac
-  __TEXT.__oslogstring: 0x46a2
-  __TEXT.__swift_as_entry: 0x3ac
-  __TEXT.__swift_as_ret: 0x40c
-  __TEXT.__swift_as_cont: 0x6c4
-  __TEXT.__swift5_capture: 0x18c4
+  __TEXT.__swift5_proto: 0x218
+  __TEXT.__swift5_types: 0x21c
+  __TEXT.__cstring: 0x20bc
+  __TEXT.__oslogstring: 0x49b2
+  __TEXT.__swift_as_entry: 0x3d0
+  __TEXT.__swift_as_ret: 0x434
+  __TEXT.__swift_as_cont: 0x6f0
+  __TEXT.__swift5_capture: 0x19e8
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x3c40
-  __TEXT.__eh_frame: 0x8edc
+  __TEXT.__unwind_info: 0x3ed8
+  __TEXT.__eh_frame: 0x941c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb20
+  __DATA_CONST.__objc_selrefs: 0xb58
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__got: 0x1190
-  __AUTH_CONST.__const: 0x5b10
+  __DATA_CONST.__got: 0x11b0
+  __AUTH_CONST.__const: 0x5f60
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0x1ff8
-  __AUTH_CONST.__auth_got: 0x28f0
+  __AUTH_CONST.__auth_got: 0x2958
   __AUTH.__objc_data: 0x288
-  __AUTH.__data: 0x550
-  __DATA.__data: 0xcd8
-  __DATA.__common: 0x38
+  __AUTH.__data: 0x788
+  __DATA.__data: 0xe60
+  __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x5b0
-  __DATA_DIRTY.__data: 0x3548
+  __DATA_DIRTY.__data: 0x33d8
   __DATA_DIRTY.__bss: 0xe80
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/PrivateFrameworks/ProactiveDaemonSupport.framework/ProactiveDaemonSupport
   - /System/Library/PrivateFrameworks/SiriEntityMatcher.framework/SiriEntityMatcher
   - /System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities
+  - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/ToolKit.framework/ToolKit
   - /System/Library/PrivateFrameworks/UIIntelligenceSupport.framework/UIIntelligenceSupport
   - /System/Library/PrivateFrameworks/UIIntelligenceSupportAgent.framework/UIIntelligenceSupportAgent
   - /System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5348
-  Symbols:   338
-  CStrings:  441
+  Functions: 5615
+  Symbols:   343
+  CStrings:  448
 
Symbols:
+ _CGRectIntersection
+ _CGRectIsEmpty
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_deviceClassNumber
+ _OBJC_CLASS_$_FBSDisplayIdentity
+ _OBJC_CLASS_$_FBSDisplayMonitor
- _CVPixelBufferGetIOSurface
CStrings:
+ "EditingContextFetcher.getResults"
+ "Skipping HAL media entity: no media type from %{public}s, state %{public}ld"
+ "Skipping HAL media entity: peer has no IDS device identifier"
+ "Using video for HAL media entity with no media type from %{public}s, state %{public}ld"
+ "[UserContextFetcher] %{public}ld panes of %{private}s have a focused field; editing context discarded"
+ "[UserContextFetcher] Active target returned no content; not promoting another app's window"
+ "[UserContextFetcher] All candidates excluded; falling back to first excluded window"
+ "[UserContextFetcher] No usable target window after retries for %{private}s; marking layout-scan target foreground"
+ "[UserContextFetcher] Pane returned no content; not falling back to its app's other windows"
+ "[UserContextFetcher] Split screen supported: %{bool,public}d (iPad: %{bool,public}d, always-connected displays: %{public}ld)"
+ "[UserContextFetcher] Split screen: fetching panes [%{private}s], used last first (from SpringBoard: %{bool,public}d); %{public}ld by bundle id"
+ "[UserContextFetcher] Window %{private}s hosts excluded RemoteProcess; trying next candidate"
+ "[UserContextFetcher] Window %{private}s returned no content in detailed fetch."
+ "execute(frameworkIdentifier:actionIdentifier:targetAppBundleIdentifier:processInstanceIdentifier:parameters:timeout:)"
- "EditingContextFetcher.getResult"
- "[UserContextFetcher] All candidates excluded; falling back to window %s"
- "[UserContextFetcher] No usable target window after retries for bundle=%{private}s; marking layout-scan target foreground"
- "[UserContextFetcher] Window %s hosts excluded RemoteProcess; trying next candidate"
- "[UserContextFetcher] Window %{public}s (bundle=%{private}s) found in layout scan but returned no content in detailed fetch."
- "execute(frameworkIdentifier:actionIdentifier:targetAppBundleIdentifier:parameters:timeout:)"
- "iOS System Interface"
```
