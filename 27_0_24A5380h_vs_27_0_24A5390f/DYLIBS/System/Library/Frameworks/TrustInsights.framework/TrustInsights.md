## TrustInsights

> `/System/Library/Frameworks/TrustInsights.framework/TrustInsights`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`

```diff

-27.0.49.0.0
-  __TEXT.__text: 0x1972c
-  __TEXT.__const: 0x1d94
-  __TEXT.__cstring: 0x721
-  __TEXT.__constg_swiftt: 0x680
-  __TEXT.__swift5_typeref: 0x70e
+27.0.52.0.0
+  __TEXT.__text: 0x1a870
+  __TEXT.__const: 0x1e04
+  __TEXT.__cstring: 0x861
+  __TEXT.__constg_swiftt: 0x6b8
+  __TEXT.__swift5_typeref: 0x742
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x43b
-  __TEXT.__swift5_fieldmd: 0x620
+  __TEXT.__swift5_reflstr: 0x4cb
+  __TEXT.__swift5_fieldmd: 0x67c
   __TEXT.__swift5_types: 0x8c
-  __TEXT.__oslogstring: 0x2eb
-  __TEXT.__swift5_capture: 0x78
+  __TEXT.__oslogstring: 0x42f
+  __TEXT.__swift5_capture: 0xa0
   __TEXT.__swift5_assocty: 0x80
   __TEXT.__swift5_proto: 0x18c
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x2c
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift_as_cont: 0x58
-  __TEXT.__unwind_info: 0x698
+  __TEXT.__unwind_info: 0x6a8
   __TEXT.__eh_frame: 0xa80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60
+  __DATA_CONST.__objc_selrefs: 0x70
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xef8
+  __AUTH_CONST.__const: 0xf70
   __AUTH_CONST.__objc_const: 0x3d0
-  __AUTH_CONST.__auth_got: 0x740
+  __AUTH_CONST.__auth_got: 0x788
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x2f0
   __DATA.__data: 0x6a8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 564
-  Symbols:   364
-  CStrings:  62
+  Functions: 570
+  Symbols:   377
+  CStrings:  74
 
Symbols:
+ ___swift__destructor
+ ___swift_destroy_boxed_opaque_existential_0
+ _objc_msgSend$developerType
+ _objc_msgSend$teamIdentifier
+ _objc_retain
+ _objc_retain_x20
+ _swift_beginAccess
+ _swift_release_x25
+ _swift_retain_x19
+ _symbolic SDySSSo8NSObjectCG
+ _symbolic So14LSBundleRecordC
+ _symbolic _____ 13TrustInsights18EntitlementCheckerV
+ _symbolic _____ 13TrustInsights18EntitlementCheckerV11ApiEndpointO
CStrings:
+ "Call to %{public}s"
+ "Call to %{public}s | operationCategory: %{public}s | requestID: %{public}s | requestedInsight: %{public}s"
+ "Call to %{public}s | status: %{public}s | insightIDsUsed: %{public}s"
+ "Could not validate the app bundle record for the \"com.apple.developer.trustinsights.base\" entitlement"
+ "Initializing InsightEvaluator"
+ "Sending CoreAnalytics event for entitlementChecked: %s"
+ "authorizationStatus(for:)"
+ "com.apple.TrustInsights.entitlementChecked"
+ "com.apple.odi.trustinsights"
+ "reportConsumption(_:insightIDsUsed:)"
+ "requestAuthorization(for:)"
+ "requestEvaluation(context:)"
```
