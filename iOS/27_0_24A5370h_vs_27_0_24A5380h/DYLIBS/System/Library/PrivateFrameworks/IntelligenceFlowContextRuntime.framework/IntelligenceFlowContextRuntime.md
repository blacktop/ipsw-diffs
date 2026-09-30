## IntelligenceFlowContextRuntime

> `/System/Library/PrivateFrameworks/IntelligenceFlowContextRuntime.framework/IntelligenceFlowContextRuntime`

```diff

-  __TEXT.__text: 0x1022e0
+  __TEXT.__text: 0x1087bc
   __TEXT.__objc_methlist: 0x6cc
-  __TEXT.__const: 0x4a90
-  __TEXT.__swift5_typeref: 0x2b2c
-  __TEXT.__swift5_fieldmd: 0x124c
-  __TEXT.__constg_swiftt: 0x1a9c
+  __TEXT.__const: 0x4930
+  __TEXT.__swift5_typeref: 0x2b10
+  __TEXT.__swift5_fieldmd: 0x1204
+  __TEXT.__constg_swiftt: 0x1a6c
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_reflstr: 0xd8a
+  __TEXT.__swift5_reflstr: 0xcf1
   __TEXT.__swift5_assocty: 0x220
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__swift5_proto: 0x204
-  __TEXT.__swift5_types: 0x1e8
-  __TEXT.__cstring: 0x1ccc
-  __TEXT.__oslogstring: 0x3457
-  __TEXT.__swift_as_entry: 0x38c
-  __TEXT.__swift_as_ret: 0x3b4
-  __TEXT.__swift_as_cont: 0x64c
-  __TEXT.__swift5_capture: 0x162c
+  __TEXT.__swift5_proto: 0x1f8
+  __TEXT.__swift5_types: 0x1e4
+  __TEXT.__cstring: 0x1cec
+  __TEXT.__oslogstring: 0x3a00
+  __TEXT.__swift_as_entry: 0x394
+  __TEXT.__swift_as_ret: 0x3c0
+  __TEXT.__swift_as_cont: 0x65c
+  __TEXT.__swift5_capture: 0x172c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x2ef0
-  __TEXT.__eh_frame: 0x8270
+  __TEXT.__unwind_info: 0x2fa8
+  __TEXT.__eh_frame: 0x8598
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xab8
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__got: 0xfd0
-  __AUTH_CONST.__const: 0x50a0
+  __DATA_CONST.__got: 0x1030
+  __AUTH_CONST.__const: 0x5230
   __AUTH_CONST.__cfstring: 0xc0
-  __AUTH_CONST.__objc_const: 0x1d80
-  __AUTH_CONST.__auth_got: 0x25b0
-  __AUTH.__objc_data: 0x398
-  __AUTH.__data: 0x640
-  __DATA.__data: 0xe70
-  __DATA.__bss: 0x1670
+  __AUTH_CONST.__objc_const: 0x1d60
+  __AUTH_CONST.__auth_got: 0x2658
+  __AUTH.__objc_data: 0x348
+  __AUTH.__data: 0x558
+  __DATA.__data: 0xc90
+  __DATA.__bss: 0x13f0
   __DATA.__common: 0x30
-  __DATA_DIRTY.__objc_data: 0x4a0
-  __DATA_DIRTY.__data: 0x2dc0
-  __DATA_DIRTY.__bss: 0xc80
+  __DATA_DIRTY.__objc_data: 0x4f0
+  __DATA_DIRTY.__data: 0x3168
+  __DATA_DIRTY.__bss: 0xd80
   __DATA_DIRTY.__common: 0x88
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4780
+  Functions: 4846
   Symbols:   327
-  CStrings:  375
+  CStrings:  389
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__cfstring : content changed
Symbols:
+ _OBJC_CLASS_$_NSError
+ _swift_deallocBox
- _swift_runtimeSupportsNoncopyableTypes
- _swift_willThrowTypedImpl
CStrings:
+ "[UserContextFetcher] Context menu source element: appIntentsPayloadCount=%ld, hasExportableData=%{bool}d"
+ "[UserContextFetcher] Context menu: direct entities excluded, falling back to exportable data (hasExportableData=%{bool}d)"
+ "[UserContextFetcher] Context menu: extracted %ld direct entities from source element"
+ "[UserContextFetcher] Direct fetch %s for targetWindow=%{public}s, bundle=%{public}s"
+ "[UserContextFetcher] Direct fetch for targetWindow=%{public}s returned no content"
+ "[UserContextFetcher] Direct window fetch without process-pinning (pid or pidVersion missing)"
+ "[UserContextFetcher] Layout scan returned window element with missing identifier or processInfo"
+ "[UserContextFetcher] No usable target window after retries for bundle=%{public}s; marking layout-scan target foreground"
+ "[UserContextFetcher] Screenshot requested for window %s but not received"
+ "[UserContextFetcher] Window %{public}s (bundle=%{public}s) found in layout scan but returned no content in detailed fetch."
+ "[UserContextFetcher] Window %{public}s (bundle=%{public}s) is access-excluded; returning content-free skeleton without scraping"
+ "[UserContextFetcher] fetch(screenshotActiveWindow: %{bool,public}d, invocationContext: %{public}s)"
+ "[UserContextFetcher] fetchWindow(%{public}s) — UIIS returned %ld root(s) but no usable window content"
+ "[UserContextFetcher] fetchWindow(%{public}s) — UIIS returned empty hierarchy (no roots). processInfo=%{public}s"
+ "fetchUserContext starting for %{public}s, screenshot=%{bool}d, invocationContext=%{public}s"
+ "fetchUserContext: failed to decode request: %@"
+ "skeleton (access-excluded)"
- "[UserContextFetcher] No usable target window after retries for bundle=%{public}s"
- "[UserContextFetcher] Screenshot was requested for window %s but not received"
- "fetchUserContext starting for %{public}s, screenshot=%{bool}d"

```
