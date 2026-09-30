## AnalyticsAgentFramework

> `/System/Library/PrivateFrameworks/AnalyticsAgentFramework.framework/AnalyticsAgentFramework`

```diff

-  __TEXT.__text: 0x1b520
+  __TEXT.__text: 0x1b200
   __TEXT.__objc_methlist: 0xd8c
-  __TEXT.__const: 0x6b8
-  __TEXT.__gcc_except_tab: 0xa50
+  __TEXT.__const: 0x6c8
+  __TEXT.__gcc_except_tab: 0xa5c
   __TEXT.__swift5_typeref: 0x57a
   __TEXT.__cstring: 0x481
-  __TEXT.__oslogstring: 0x124b
+  __TEXT.__oslogstring: 0x127b
   __TEXT.__constg_swiftt: 0x35c
   __TEXT.__swift5_reflstr: 0x21c
   __TEXT.__swift5_fieldmd: 0x230

   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x64
   __TEXT.__swift_as_cont: 0x88
-  __TEXT.__swift5_capture: 0x154
+  __TEXT.__swift5_capture: 0x140
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x788
+  __TEXT.__unwind_info: 0x780
   __TEXT.__eh_frame: 0x1bf0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0xb00
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x748
+  __AUTH_CONST.__const: 0x6f8
   __AUTH_CONST.__objc_const: 0x1968
-  __AUTH_CONST.__auth_got: 0x788
+  __AUTH_CONST.__auth_got: 0x798
   __AUTH.__data: 0x3c0
   __DATA.__data: 0x538
   __DATA.__bss: 0x80

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 329
-  Symbols:   591
-  CStrings:  102
+  Functions: 325
+  Symbols:   586
+  CStrings:  103
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ _AnalyticsIsEventUsed
+ _AnalyticsSendEventSync
CStrings:
+ "Event not enabled. { eventName=%s }"
+ "Failed to send event %{public}s, skipping %{public}s duration=%u collectedDate=%{public}s"
- "Event %{public}s not enabled, skipping %{public}s duration=%u collectedDate=%{public}s"

```
