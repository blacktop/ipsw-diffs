## ChronoCore

> `/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore`

```diff

-740.0.0.0.0
-  __TEXT.__text: 0x42417c
-  __TEXT.__objc_methlist: 0x1f10
-  __TEXT.__const: 0x14908
-  __TEXT.__cstring: 0x6e4b
-  __TEXT.__oslogstring: 0x15b47
+749.0.1.0.0
+  __TEXT.__text: 0x424350
+  __TEXT.__objc_methlist: 0x1f20
+  __TEXT.__const: 0x148d8
+  __TEXT.__cstring: 0x6e5b
+  __TEXT.__oslogstring: 0x15c47
   __TEXT.__gcc_except_tab: 0x70
   __TEXT.__dlopen_cstrs: 0x7a
-  __TEXT.__constg_swiftt: 0xbc94
-  __TEXT.__swift5_typeref: 0xc457
-  __TEXT.__swift5_reflstr: 0xa9f3
-  __TEXT.__swift5_fieldmd: 0x7f68
+  __TEXT.__constg_swiftt: 0xbc98
+  __TEXT.__swift5_typeref: 0xc393
+  __TEXT.__swift5_reflstr: 0xaa03
+  __TEXT.__swift5_fieldmd: 0x7f58
   __TEXT.__swift5_builtin: 0x1b8
   __TEXT.__swift5_assocty: 0x6e8
   __TEXT.__swift5_proto: 0xb74
-  __TEXT.__swift5_types: 0x684
+  __TEXT.__swift5_types: 0x680
   __TEXT.__swift5_protos: 0x230
-  __TEXT.__swift5_capture: 0x558c
+  __TEXT.__swift5_capture: 0x556c
   __TEXT.__swift_as_entry: 0x180
   __TEXT.__swift_as_ret: 0x16c
   __TEXT.__swift_as_cont: 0x33c
   __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__unwind_info: 0x7750
-  __TEXT.__eh_frame: 0xc640
+  __TEXT.__unwind_info: 0x7758
+  __TEXT.__eh_frame: 0xc6a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x2c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1960
+  __DATA_CONST.__objc_selrefs: 0x1968
   __DATA_CONST.__objc_protorefs: 0x178
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__got: 0x1dd8
-  __AUTH_CONST.__const: 0x138c8
+  __DATA_CONST.__got: 0x1df0
+  __AUTH_CONST.__const: 0x13868
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x187c0
-  __AUTH_CONST.__auth_got: 0x4540
+  __AUTH_CONST.__objc_const: 0x187c8
+  __AUTH_CONST.__auth_got: 0x4548
   __AUTH.__objc_data: 0x1138
   __AUTH.__data: 0x16d8
   __DATA.__objc_ivar: 0x14

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11046
-  Symbols:   5061
-  CStrings:  1989
+  Functions: 11048
+  Symbols:   5055
+  CStrings:  1990
 
Symbols:
+ ___swift_closure_destructor.220Tm
+ ___swift_memcpy33_8
+ ___swift_project_boxed_opaque_existential_0Tm
+ _symbolic ___________p 9ChronoKit15ExtensionHidingP AA0C8ManagingP
- ___swift_closure_destructor.216Tm
- ___swift_closure_destructor.35Tm
- _objc_msgSend$reloadWidget:reason:
- _symbolic _____ 10ChronoCore21MobileTimelineServiceC19ReloadBehaviorState33_FA00F2730F9D79EF75DE399C5A05AFB0LLV23ResolvedRefreshStrategyV
- _symbolic _____Sg 10ChronoCore21MobileTimelineServiceC19ReloadBehaviorState33_FA00F2730F9D79EF75DE399C5A05AFB0LLV23ResolvedRefreshStrategyV
- _symbolic ______p 10ChronoCore25TimelineRendererServicingP
- _symbolic _____y______y__________GG 7Combine10PublishersO6FilterV AA12AnyPublisherV 9ChronoKit28WidgetDescriptorsChangeEventV s5NeverO
- _symbolic _____y______y______y__________GG_____ySo19CHSWidgetDescriptorCGG 7Combine10PublishersO3MapV AC6FilterV AA12AnyPublisherV 9ChronoKit28WidgetDescriptorsChangeEventV s5NeverO AJ20DescriptorCollectionC
- _symbolic _____y______y______y______y__________GG_____ySo19CHSWidgetDescriptorCGGSo17OS_dispatch_queueCG 7Combine10PublishersO9ReceiveOnV AC3MapV AC6FilterV AA12AnyPublisherV 9ChronoKit28WidgetDescriptorsChangeEventV s5NeverO AL20DescriptorCollectionC
- _type_layout_string 10ChronoCore21MobileTimelineServiceC19ReloadBehaviorState33_FA00F2730F9D79EF75DE399C5A05AFB0LLV23ResolvedRefreshStrategyV
CStrings:
+ "Asked to reload placeholder widget: %{public}s for reason: %{public}s, but that's not currently supported."
+ "Setting extension hidden: %{bool,public}d for extensions: %{public}s"
+ "[%{public}@] Reload widget for reason: %{public}s, contentType: %{public}s"
+ "[%{public}@] Reload widget ignored because content type %{public}s is unhandled."
+ "[%{public}s] Received message to reload %{public}@ for reason: %{public}s, contentType: %{public}s"
+ "[%{public}s] Received message to reload if failed %{public}@ for reason: %{public}s, contentType: %{public}s"
+ "going from not disabled -> disabled"
+ "going from once/disabled -> not disabled/once"
+ "setExtensionHidden: Empty extension bundle identifiers array"
- "Failed to reload relevances for %{public}@: %{public}@"
- "Got updated descriptor collection with identities %{public}s"
- "Reloaded relevances for %{public}@"
- "[%{public}@] Reload widget for reason: %{public}s"
- "[%{public}@] Reload widget ignored because service doesn't support reloading."
- "[%{public}s] Received message to reload %{public}@ for reason: %{public}s"
- "once/disabled refresh strategy suppression"
- "refreshStrategySuppression"
```
