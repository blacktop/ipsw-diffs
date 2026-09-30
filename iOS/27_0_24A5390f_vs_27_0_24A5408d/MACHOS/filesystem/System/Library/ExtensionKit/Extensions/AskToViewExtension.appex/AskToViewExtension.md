## AskToViewExtension

> `/System/Library/ExtensionKit/Extensions/AskToViewExtension.appex/AskToViewExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`

```diff

-93.0.0.0.0
-  __TEXT.__text: 0x11b98
-  __TEXT.__auth_stubs: 0x1060
+96.0.0.0.0
+  __TEXT.__text: 0x19ca0
+  __TEXT.__auth_stubs: 0x10e0
   __TEXT.__objc_stubs: 0x220
-  __TEXT.__objc_methlist: 0x1a0
-  __TEXT.__const: 0x6c2
-  __TEXT.__constg_swiftt: 0x26c
-  __TEXT.__swift5_typeref: 0x753
-  __TEXT.__swift5_fieldmd: 0x15c
+  __TEXT.__objc_methlist: 0x184
+  __TEXT.__const: 0xa58
+  __TEXT.__constg_swiftt: 0x2f0
+  __TEXT.__swift5_typeref: 0x8a2
+  __TEXT.__cstring: 0x487
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x1df
-  __TEXT.__swift5_assocty: 0x60
-  __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_proto: 0x1c
-  __TEXT.__swift5_types: 0x18
+  __TEXT.__swift5_reflstr: 0x32f
+  __TEXT.__swift5_fieldmd: 0x258
+  __TEXT.__swift5_assocty: 0x90
+  __TEXT.__swift5_capture: 0x4f4
+  __TEXT.__oslogstring: 0x58f
+  __TEXT.__swift5_proto: 0x24
+  __TEXT.__swift5_types: 0x24
+  __TEXT.__swift_as_entry: 0x48
+  __TEXT.__swift_as_ret: 0x48
+  __TEXT.__swift_as_cont: 0x74
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x388
-  __TEXT.__oslogstring: 0x4af
-  __TEXT.__swift_as_entry: 0x38
-  __TEXT.__swift_as_ret: 0x34
-  __TEXT.__swift_as_cont: 0x54
   __TEXT.__objc_classname: 0x112
-  __TEXT.__objc_methname: 0x401
-  __TEXT.__objc_methtype: 0x1a9
-  __TEXT.__swift5_capture: 0x1e8
-  __TEXT.__unwind_info: 0x3e0
-  __TEXT.__eh_frame: 0x864
-  __DATA_CONST.__const: 0x538
+  __TEXT.__objc_methname: 0x4a1
+  __TEXT.__objc_methtype: 0x149
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__unwind_info: 0x540
+  __TEXT.__eh_frame: 0x9b4
+  __DATA_CONST.__const: 0xc48
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0x838
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__auth_ptr: 0x2c0
-  __DATA.__objc_const: 0x3a0
-  __DATA.__objc_selrefs: 0x150
-  __DATA.__objc_data: 0x1c8
-  __DATA.__data: 0x530
-  __DATA.__bss: 0x3d0
+  __DATA_CONST.__auth_got: 0x878
+  __DATA_CONST.__got: 0x2e8
+  __DATA_CONST.__auth_ptr: 0x2f0
+  __DATA.__objc_const: 0x3b8
+  __DATA.__objc_selrefs: 0x148
+  __DATA.__objc_data: 0x1d0
+  __DATA.__data: 0x6f0
+  __DATA.__bss: 0x4f0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 245
-  Symbols:   170
-  CStrings:  130
+  Functions: 357
+  Symbols:   173
+  CStrings:  135
 
Symbols:
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x27
+ _swift_release_x27
+ _swift_retain_x19
+ _swift_retain_x22
+ _swift_retain_x25
+ _swift_retain_x26
- _objc_retain_x28
- _swift_cvw_allocateGenericValueMetadataWithLayoutString
- _swift_getExistentialTypeMetadata
- _swift_getGenericMetadata
- _swift_retain_x27
CStrings:
+ "%s Could not construct URL to launch Messages"
+ "%s didLaunchApp %{bool}d"
+ "Approve in person flow completed with answerChoice == %s. error: %s"
+ "AskToViewExtension/ApproveInPersonFlowView.swift"
+ "AskToViewExtension/AskFlowCoordinator.swift"
+ "AskToViewExtension/AskToApproveFlowView.swift"
+ "Attempting to open url to launch Messages %{private}s"
+ "Direct Approve in person flow completed with answerChoice == %s. error: %s"
+ "Error broadcasting messagesComposeDidFinish: %@"
+ "Error finishing AskToViewExtension with result: %@"
+ "Failed to launch Messages with error: %@"
+ "Presenting direct approve in person"
+ "Presenting direct ask to approve"
+ "View.task @ AskToViewExtension/ApproveInPersonFlowView.swift:"
+ "View.task @ AskToViewExtension/AskToApproveFlowView.swift:"
+ "launchMessagesAndStagePayload(result:)"
+ "messagesComposeDidFinish"
+ "presentMessageCompose(result:delegateBinding:withCurrentHostingController:)"
- "%s Error calling acknowledgmentAlertButtonTapped: %@"
- "%s Error calling messagesComposeDidFinish: %@"
- "Approve in person flow completed with success == %@. error: %@"
- "Attempting to open url to launch Messages %s"
- "Failed to launch Messages on macOS with error: %@"
- "_launchMessagesAndStagePayload(result:)"
- "_presentMessageCompose(result:)"
- "acknowledgmentAlertButtonTappedWithQuestion:action:reply:"
- "messageComposeViewController(_:didFinishWith:)"
- "notifyDaemonOfAlertAction(_:)"
- "presentMessageCompose didLaunchApp %{bool}d"
- "v40@0:8@\"_TtC5AskTo10ATQuestion\"16q24@?<v@?@\"NSError\">32"
- "v40@0:8@16q24@?32"
```
