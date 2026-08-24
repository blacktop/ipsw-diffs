## UIIntelligenceIntents

> `/System/Library/PrivateFrameworks/UIIntelligenceIntents.framework/Versions/A/UIIntelligenceIntents`

```diff

-9127.0.78.0.0
-  __TEXT.__text: 0x2e0c4
-  __TEXT.__objc_methlist: 0x19c
-  __TEXT.__const: 0x4280
+9127.0.84.0.0
+  __TEXT.__text: 0x3054c
+  __TEXT.__objc_methlist: 0x1ac
+  __TEXT.__const: 0x42c0
   __TEXT.__constg_swiftt: 0x998
-  __TEXT.__swift5_typeref: 0x136c
+  __TEXT.__swift5_typeref: 0x138e
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x90e
-  __TEXT.__swift5_fieldmd: 0x808
+  __TEXT.__swift5_reflstr: 0x92e
+  __TEXT.__swift5_fieldmd: 0x820
   __TEXT.__swift5_assocty: 0x510
   __TEXT.__swift5_proto: 0x2f4
   __TEXT.__swift5_types: 0xa0
-  __TEXT.__cstring: 0x1395
+  __TEXT.__cstring: 0x1465
   __TEXT.__swift_as_entry: 0x100
-  __TEXT.__swift_as_ret: 0xc4
-  __TEXT.__swift_as_cont: 0x18c
-  __TEXT.__oslogstring: 0x6aa
+  __TEXT.__swift_as_ret: 0xcc
+  __TEXT.__swift_as_cont: 0x194
+  __TEXT.__oslogstring: 0xa9a
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__swift5_capture: 0xbc
-  __TEXT.__unwind_info: 0xfc0
-  __TEXT.__eh_frame: 0x1bcc
+  __TEXT.__swift5_capture: 0xcc
+  __TEXT.__unwind_info: 0xff0
+  __TEXT.__eh_frame: 0x1c8c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b8
+  __DATA_CONST.__objc_selrefs: 0x2e0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__got: 0x2c8
-  __AUTH_CONST.__const: 0x14f9
-  __AUTH_CONST.__objc_const: 0x298
-  __AUTH_CONST.__auth_got: 0x940
+  __DATA_CONST.__got: 0x2d0
+  __AUTH_CONST.__const: 0x1551
+  __AUTH_CONST.__objc_const: 0x2a0
+  __AUTH_CONST.__auth_got: 0x978
   __AUTH.__data: 0x1b8
-  __DATA.__data: 0xd10
+  __DATA.__data: 0xd20
   __DATA.__bss: 0x5d90
   __DATA.__common: 0x380
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1181
-  Symbols:   737
-  CStrings:  135
+  Functions: 1194
+  Symbols:   749
+  CStrings:  147
 
Symbols:
+ _OBJC_CLASS_$_NSBundle
+ ___swift__destructor
+ ___swift_closure_destructorTm
+ __swift_closure_destructor.5Tm
+ __swift_stdlib_bridgeErrorToNSError
+ _objc_msgSend$attributedSubstringForProposedRange:actualRange:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$mainBundle
+ _objc_msgSend$requestContextsForScope:completion:
+ _objc_msgSend$substringWithRange:
+ _swift_beginAccess
+ _symbolic So11NSResponderCm
+ _symbolic So8NSObjectCSg
- __swift_closure_destructor.21Tm
CStrings:
+ "Bounding frame of the target text field (scene-relative, points). Formatted as a CGRect string. When provided with Target Window Identifier, the intent focuses that field before presenting the result."
+ "Editing context request failed (hasTarget=%{bool,public}d): %{public}s"
+ "No editing context from %{public}s: reconstruction=%{bool,public}d"
+ "No responder to read editing context from (hasTarget=%{bool,public}d, focusedResponder=nil)"
+ "Partial target (targetFrame=%{bool,public}d targetWindowIdentifier=%{bool,public}d) — both must be set for a valid target."
+ "Reconstruction: %{public}s has no NSTextInputClient"
+ "Reconstruction: document read truncated to cap (%{public}ld units)"
+ "Reconstruction: text input returned content starting at offset %{public}ld instead of the document start; cannot map cursor/selection offsets, skipping reconstruction"
+ "Resolved responder %{public}s (viaTarget=%{bool,public}d)"
+ "Text-input reconstruction returned nil for %{public}s; falling back to coordinator/delegate paths"
+ "could not resolve target field by frame; using focused responder: %{public}@"
+ "makeFirstResponder failed for targeted view: %{public}s"
+ "text-input reconstruction: selection not located in full document; falling back to caret"
- "Partial target (targetFrame=%{bool,public}d targetWindowIdentifier=%{bool,public}d) — both must be set"
```
