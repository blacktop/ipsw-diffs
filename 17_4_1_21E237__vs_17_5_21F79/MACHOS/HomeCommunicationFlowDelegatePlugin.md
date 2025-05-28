## HomeCommunicationFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/HomeCommunicationFlowDelegatePlugin.bundle/HomeCommunicationFlowDelegatePlugin`

```diff

-3304.19.1.0.0
-  __TEXT.__text: 0x873e4
-  __TEXT.__auth_stubs: 0x2dc0
-  __TEXT.__const: 0x4a04
-  __TEXT.__cstring: 0x7f11
-  __TEXT.__constg_swiftt: 0x2ca8
-  __TEXT.__swift5_typeref: 0x1ef0
-  __TEXT.__swift5_fieldmd: 0x19c4
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x1aa1
-  __TEXT.__swift5_assocty: 0x420
-  __TEXT.__swift5_proto: 0x2c4
-  __TEXT.__swift5_types: 0x1a4
+3305.8.1.0.0
+  __TEXT.__text: 0x90734
+  __TEXT.__auth_stubs: 0x2e40
+  __TEXT.__const: 0x4f34
+  __TEXT.__cstring: 0x8511
+  __TEXT.__constg_swiftt: 0x2dfc
+  __TEXT.__swift5_typeref: 0x1fde
+  __TEXT.__swift5_fieldmd: 0x1ad4
+  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_reflstr: 0x1bd1
+  __TEXT.__swift5_assocty: 0x458
+  __TEXT.__swift5_proto: 0x310
+  __TEXT.__swift5_types: 0x1c0
   __TEXT.__objc_classname: 0xaf
   __TEXT.__objc_methname: 0x8ca
   __TEXT.__objc_methtype: 0x1a8
   __TEXT.__swift5_capture: 0x438
   __TEXT.__swift5_protos: 0x3c
-  __TEXT.__unwind_info: 0x25b4
-  __TEXT.__eh_frame: 0x4180
-  __DATA_CONST.__auth_got: 0x16e0
-  __DATA_CONST.__got: 0x630
-  __DATA_CONST.__auth_ptr: 0x218
-  __DATA_CONST.__const: 0x3d18
-  __DATA_CONST.__objc_classlist: 0xe8
+  __TEXT.__unwind_info: 0x3400
+  __TEXT.__eh_frame: 0x4c38
+  __DATA_CONST.__auth_got: 0x1720
+  __DATA_CONST.__got: 0x638
+  __DATA_CONST.__auth_ptr: 0x220
+  __DATA_CONST.__const: 0x40d0
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_classrefs: 0x180
-  __DATA.__objc_const: 0x2d88
+  __DATA.__objc_const: 0x2e98
   __DATA.__objc_selrefs: 0x300
-  __DATA.__objc_data: 0xba8
-  __DATA.__data: 0x5ed8
+  __DATA.__objc_data: 0xbf8
+  __DATA.__data: 0x61e8
   __DATA.__common: 0x400
-  __DATA.__bss: 0x5180
+  __DATA.__bss: 0x5b00
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3608
+  Functions: 3955
   Symbols:   212
-  CStrings:  847
+  CStrings:  871
 
CStrings:
+ "#SendAnnouncementFlow generating unsupportedFlowProducer for %s"
+ "#SendAnnouncementIntentHandledStrategy Unsupported announcement reason %s"
+ "#SendAnnouncementIntentHandledStrategy Unsupported recipient reason %s"
+ "#SendAnnouncementIntentHandledStrategy dialogExecutionResult is nil - returning generic error"
+ "#SendAnnouncementIntentHandledStrategy makeLaunchAppWithIntentOutput"
+ "#SendAnnouncementIntentHandledStrategy makeUnsupportedValueOutput"
+ "#SendAnnouncementIntentHandledStrategy missing app identifier"
+ "#SendAnnouncementIntentHelper extractSpeechData error=%@. Returning base intent."
+ "#SendAnnouncementIntentHelper extractSpeechData return type is not of type SASExtractSpeechDataCompleted"
+ "#SendAnnouncementIntentHelper sending SASExtractSpeechData async with speechRequestId: %s, startTime in ms: %@, endTime in ms: %@"
+ "#SendAnnouncementIntentHelper speechDataUrl is `nil`"
+ "#SendAnnouncementIntentHelper speechDataUrl unwrapped to %s"
+ "#SendAnnouncementUnsupportedValueFlowStrategy %s: unsupported for %s"
+ ".announcingToSelf"
+ ".intercomDisabledOnAllDevices"
+ ".noAnnouncementToReplyTo"
+ ".speakerGroupsNotSupported"
+ "HomeCommunication#HomeAppLaunch"
+ "OpenApp"
+ "Received ReplyAnnoucement direct invocation, with ID: %s. Fetching announcement ID"
+ "Unknown error code: "
+ "_TtC35HomeCommunicationFlowDelegatePlugin40SendAnnouncementUnsupportedValueStrategy"
+ "announcementID"
+ "extracted speech data url is nil"
+ "makeUpdatedIntentForUnsupportedValue(resolveRecord:)"
- "Received ReplyAnnoucement / Send Announcement direct invocation, with ID: %s"

```
