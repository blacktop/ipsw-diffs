## HomeCommunicationFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/HomeCommunicationFlowDelegatePlugin.bundle/HomeCommunicationFlowDelegatePlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

 3605.8.1.0.0
-  __TEXT.__text: 0x89950
-  __TEXT.__auth_stubs: 0x2f80
-  __TEXT.__objc_stubs: 0xce0
+  __TEXT.__text: 0x91e54
+  __TEXT.__auth_stubs: 0x3090
+  __TEXT.__objc_stubs: 0xd00
   __TEXT.__objc_methlist: 0x26c
-  __TEXT.__const: 0x73f8
+  __TEXT.__const: 0x7dd8
   __TEXT.__objc_methname: 0xed4
   __TEXT.__objc_methtype: 0x1a9
-  __TEXT.__constg_swiftt: 0x2fac
-  __TEXT.__swift5_typeref: 0x2680
-  __TEXT.__swift5_reflstr: 0x2178
-  __TEXT.__swift5_fieldmd: 0x1f80
+  __TEXT.__constg_swiftt: 0x3064
+  __TEXT.__swift5_typeref: 0x28be
+  __TEXT.__swift5_reflstr: 0x2408
+  __TEXT.__swift5_fieldmd: 0x20f4
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__cstring: 0x2932
-  __TEXT.__swift5_assocty: 0x648
-  __TEXT.__swift5_proto: 0x544
-  __TEXT.__swift5_types: 0x220
+  __TEXT.__cstring: 0x2be2
+  __TEXT.__swift5_assocty: 0x720
+  __TEXT.__swift5_proto: 0x5e0
+  __TEXT.__swift5_types: 0x238
   __TEXT.__objc_classname: 0x1168
-  __TEXT.__oslogstring: 0x593e
+  __TEXT.__oslogstring: 0x605e
   __TEXT.__swift5_protos: 0x48
-  __TEXT.__swift5_capture: 0x578
-  __TEXT.__swift_as_entry: 0x2c0
-  __TEXT.__swift_as_ret: 0x364
-  __TEXT.__swift_as_cont: 0x458
-  __TEXT.__unwind_info: 0x3298
-  __TEXT.__eh_frame: 0x5520
-  __DATA_CONST.__const: 0x55b0
+  __TEXT.__swift5_capture: 0x628
+  __TEXT.__swift_as_entry: 0x2d4
+  __TEXT.__swift_as_ret: 0x3b0
+  __TEXT.__swift_as_cont: 0x4bc
+  __TEXT.__unwind_info: 0x3640
+  __TEXT.__eh_frame: 0x5c70
+  __DATA_CONST.__const: 0x5c10
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__auth_got: 0x17c8
-  __DATA_CONST.__got: 0x7b0
-  __DATA_CONST.__auth_ptr: 0xe68
+  __DATA_CONST.__auth_got: 0x1850
+  __DATA_CONST.__got: 0x7d8
+  __DATA_CONST.__auth_ptr: 0xec0
   __DATA.__objc_const: 0x2948
   __DATA.__objc_selrefs: 0x450
   __DATA.__objc_data: 0xa40
-  __DATA.__data: 0x4680
-  __DATA.__common: 0x340
+  __DATA.__data: 0x48c0
+  __DATA.__common: 0x358
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3844
-  Symbols:   245
-  CStrings:  974
+  Functions: 4098
+  Symbols:   248
+  CStrings:  1011
 
Symbols:
+ _OBJC_CLASS_$_SAUIDelayedActionCommand
+ _OBJC_CLASS_$_SAUIPerformAppIntent
+ _swift_getTupleTypeMetadata
CStrings:
+ "#CommandHelper failed to make SAUIPerformAPpIntent for PlayAnnouncementSoundIntent."
+ "#CommandHelper failed to make SAUIPerformAppIntent for DismissIntercomIntent."
+ "#CommandHelper failed to make SAUIPerformAppIntent for DismissIntercomIntent. Error=%@"
+ "#CommandHelper has prompted for announcement: %{bool}d."
+ "#CommandHelper making SAUIPerformAppIntent with wrapped %s."
+ "#CommandHelper wrapping SAUIPerformAppIntent with aceId=%s in SAUIDelayedActionCommand with aceId=%s"
+ "#SendAnnouncementFlow using UnsupportedValueAndCancelIntentFlowProducer (HomeAccessory or CarPlay)"
+ "#SendAnnouncementIntentHandlerStrategy adding PlayAnnouncementSoundAction"
+ "#SendAnnouncementNeedsValueStrategy adding dismissIntercomDelayedAction"
+ "#SendAnnouncementNeedsValueStrategy sending DismissIntercomIntent in delayedAction with aceId=%s"
+ "#SendAnnouncementPreflightGuardFlow - makePreflightFailureResponse: success response code is not a failure"
+ "#SendAnnouncementPreflightGuardFlow CheckTargetSupportIntent returned a non-successful preflight check: %s"
+ "#SendAnnouncementPreflightGuardFlow failed to create CheckTargetSupportIntent"
+ "#SendAnnouncementPreflightGuardFlow failed to get nlIntent from parse. Returning generic error flow"
+ "#SendAnnouncementPreflightGuardFlow failed to perform preflight check: %@"
+ "#SendAnnouncementPreflightGuardFlow makeFailureHandlingIntentResponseAsync"
+ "#SendAnnouncementPreflightGuardFlow preflight check successful. Guard flow passed."
+ "#SendAnnouncementPreflightGuardFlow sending preflight intent"
+ "#SendAnnouncementPreflightGuardFlow skipping preflight check for non-homeAccessory"
+ "#Transformer<HomeCommunicationNLIntent, CheckTargetSupportIntent?> CheckTargetSupportIntent=%s"
+ "#Transformer<HomeCommunicationNLIntent, CheckTargetSupportIntent?> converting %s"
+ "AppIntentDispatcherError("
+ "CheckTargetSupportIntent"
+ "CheckTargetSupportIntent(home="
+ "Error while making AppIntent "
+ "Failed to perform "
+ "Got .success response code from CheckTargetSupportIntent instead of a failure"
+ "HomeCommunicationFlowDelegatePlugin/CommandHelper.swift"
+ "HomeCommunicationFlowDelegatePlugin/SendAnnouncementPreflightGuardFlow.swift"
+ "ShouldNeverBeLogged"
+ "actionName error fileName methodName line "
+ "announcementSent"
+ "cancelled"
+ "completed"
+ "failed to transform input"
+ "failureAnnouncingToSelf"
+ "failureTargetNotFound"
+ "makeSAUIPerformAppIntent(for:performOptions:dialogPhase:)"
- "#SendAnnouncementPreflightGuardFlow bypassing preflight check. Guard flow passed."
```
