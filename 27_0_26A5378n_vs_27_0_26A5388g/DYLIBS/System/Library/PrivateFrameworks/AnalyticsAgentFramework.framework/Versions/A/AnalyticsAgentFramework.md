## AnalyticsAgentFramework

> `/System/Library/PrivateFrameworks/AnalyticsAgentFramework.framework/Versions/A/AnalyticsAgentFramework`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__objc_const`

```diff

-559.0.0.0.0
-  __TEXT.__text: 0x1bd14
+564.0.0.0.0
+  __TEXT.__text: 0x1b9fc
   __TEXT.__objc_methlist: 0xd74
-  __TEXT.__const: 0x6c8
-  __TEXT.__gcc_except_tab: 0xa28
+  __TEXT.__const: 0x6d8
+  __TEXT.__gcc_except_tab: 0xa34
   __TEXT.__swift5_typeref: 0x57a
   __TEXT.__cstring: 0x481
-  __TEXT.__oslogstring: 0x124b
+  __TEXT.__oslogstring: 0x127b
   __TEXT.__constg_swiftt: 0x35c
   __TEXT.__swift5_reflstr: 0x21c
   __TEXT.__swift5_fieldmd: 0x230

   __TEXT.__swift_as_entry: 0x38
   __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift_as_cont: 0x88
-  __TEXT.__swift5_capture: 0x154
+  __TEXT.__swift5_capture: 0x140
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x780
+  __TEXT.__unwind_info: 0x770
   __TEXT.__eh_frame: 0x1bf8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0xaf0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x748
+  __AUTH_CONST.__const: 0x6f8
   __AUTH_CONST.__objc_const: 0x1938
-  __AUTH_CONST.__auth_got: 0x660
-  __AUTH.__data: 0x3c0
-  __DATA.__data: 0x538
-  __DATA.__bss: 0x80
-  __DATA.__common: 0x90
+  __AUTH_CONST.__auth_got: 0x670
+  __AUTH.__data: 0x80
+  __DATA.__data: 0x1c0
+  __DATA.__common: 0x18
+  __DATA_DIRTY.__data: 0x6a0
+  __DATA_DIRTY.__bss: 0x80
+  __DATA_DIRTY.__common: 0x78
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 331
-  Symbols:   412
-  CStrings:  101
+  Functions: 327
+  Symbols:   414
+  CStrings:  102
 
Symbols:
+ _AnalyticsIsEventUsed
+ _AnalyticsSendEventSync
CStrings:
+ "Event not enabled. { eventName=%s }"
+ "Failed to send event %{public}s, skipping %{public}s duration=%u collectedDate=%{public}s"
- "Event %{public}s not enabled, skipping %{public}s duration=%u collectedDate=%{public}s"
```
