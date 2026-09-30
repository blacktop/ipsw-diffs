## UIIntelligenceIntents

> `/System/Library/PrivateFrameworks/UIIntelligenceIntents.framework/UIIntelligenceIntents`

```diff

-9127.0.78.0.0
-  __TEXT.__text: 0x2bce4
-  __TEXT.__objc_methlist: 0x764
-  __TEXT.__const: 0x3b88
+9127.0.84.0.0
+  __TEXT.__text: 0x2cf04
+  __TEXT.__objc_methlist: 0x774
+  __TEXT.__const: 0x3bb8
   __TEXT.__constg_swiftt: 0x91c
   __TEXT.__swift5_typeref: 0x117a
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x82e
-  __TEXT.__swift5_fieldmd: 0x75c
+  __TEXT.__swift5_reflstr: 0x84e
+  __TEXT.__swift5_fieldmd: 0x774
   __TEXT.__swift5_assocty: 0x458
-  __TEXT.__oslogstring: 0x6aa
+  __TEXT.__oslogstring: 0x9ba
   __TEXT.__swift5_proto: 0x2a0
   __TEXT.__swift5_types: 0x94
   __TEXT.__swift_as_entry: 0xd4
-  __TEXT.__swift_as_ret: 0xbc
-  __TEXT.__swift_as_cont: 0x158
-  __TEXT.__cstring: 0x13a5
-  __TEXT.__swift5_capture: 0xb0
+  __TEXT.__swift_as_ret: 0xb8
+  __TEXT.__swift_as_cont: 0x154
+  __TEXT.__cstring: 0x1435
+  __TEXT.__swift5_capture: 0x80
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0xe80
-  __TEXT.__eh_frame: 0x1ba4
+  __TEXT.__unwind_info: 0xe68
+  __TEXT.__eh_frame: 0x1bac
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x600
+  __DATA_CONST.__objc_selrefs: 0x628
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__got: 0x2c0
-  __AUTH_CONST.__const: 0x1470
-  __AUTH_CONST.__objc_const: 0x30f8
-  __AUTH_CONST.__auth_got: 0x9d8
+  __DATA_CONST.__got: 0x2c8
+  __AUTH_CONST.__const: 0x13b0
+  __AUTH_CONST.__objc_const: 0x43d8
+  __AUTH_CONST.__auth_got: 0x9f0
   __AUTH.__data: 0x1b8
   __DATA.__data: 0xdf8
   __DATA.__bss: 0x5310

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1075
-  Symbols:   737
-  CStrings:  133
+  Functions: 1072
+  Symbols:   748
+  CStrings:  141
 
Symbols:
+ _OBJC_CLASS_$_NSBundle
+ ___swift_closure_destructor.5Tm
+ ___swift_memcpy56_8
+ _objc_msgSend$attributedTextInRange:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$mainBundle
+ _objc_msgSend$offsetFromPosition:toPosition:
+ _objc_msgSend$requestContextsForScope:completion:
+ _objc_msgSend$start
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$textInRange:
+ _swift_retain_x25
+ _swift_unknownObjectRelease_n
- _swift_release_x22
- _swift_retain_x28
CStrings:
+ "Bounding frame of the target text field (scene-relative, points). Formatted as a CGRect string. When provided with Target Window Identifier, the intent focuses that field before presenting the result."
+ "Editing context request failed (hasTarget=%{bool,public}d): %{public}s"
+ "No editing context from %{public}s: isUITextView=%{bool,public}d, reconstruction=%{bool,public}d"
+ "Partial target (targetFrame=%{bool,public}d targetWindowIdentifier=%{bool,public}d) — both must be set for a valid target."
+ "Reconstruction: %{public}s returned neither attributed nor plain text"
+ "Reconstruction: %{public}s returned no document text range"
+ "Reconstruction: document (%{public}ld units) exceeds cap; truncating read to %{public}ld"
+ "Resolved text input %{public}s (viaTarget=%{bool,public}d)"
+ "Text-input reconstruction returned nil for %{public}s; falling back to coordinator/delegate paths"
+ "findTextInput missed target; falling back to %{public}s"
+ "resolved via target frame: %{public}s frame=%{public}s window=%{public}s"
+ "text-input reconstruction: selection not located in full document; falling back to caret"
- "Found editable range %{public}s via coordinator (document length: %{public}ld)"
- "Partial target (targetFrame=%{bool,public}d targetWindowIdentifier=%{bool,public}d) — both must be set"
- "editableRangeForResponder(_:)"
- "requestEditingContext(target:)"
```
