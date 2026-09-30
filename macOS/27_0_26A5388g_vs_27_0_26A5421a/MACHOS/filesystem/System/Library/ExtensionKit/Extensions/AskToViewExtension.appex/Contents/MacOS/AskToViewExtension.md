## AskToViewExtension

> `/System/Library/ExtensionKit/Extensions/AskToViewExtension.appex/Contents/MacOS/AskToViewExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_data`

```diff

-93.0.0.0.0
-  __TEXT.__text: 0x11254
-  __TEXT.__auth_stubs: 0xe80
+96.0.0.0.0
+  __TEXT.__text: 0x18610
+  __TEXT.__auth_stubs: 0xea0
   __TEXT.__objc_stubs: 0x100
-  __TEXT.__objc_methlist: 0x50
-  __TEXT.__const: 0x6b0
-  __TEXT.__constg_swiftt: 0x230
-  __TEXT.__swift5_typeref: 0x721
-  __TEXT.__swift5_fieldmd: 0x144
+  __TEXT.__objc_methlist: 0x34
+  __TEXT.__const: 0xa08
+  __TEXT.__constg_swiftt: 0x2b4
+  __TEXT.__swift5_typeref: 0x85a
+  __TEXT.__cstring: 0x387
+  __TEXT.__swift5_reflstr: 0x283
+  __TEXT.__swift5_fieldmd: 0x21c
+  __TEXT.__swift5_assocty: 0x78
+  __TEXT.__swift5_capture: 0x3e0
+  __TEXT.__oslogstring: 0x45f
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x1a3
-  __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_proto: 0x1c
-  __TEXT.__swift5_types: 0x14
+  __TEXT.__swift5_proto: 0x24
+  __TEXT.__swift5_types: 0x20
+  __TEXT.__swift_as_entry: 0x40
+  __TEXT.__swift_as_ret: 0x44
+  __TEXT.__swift_as_cont: 0x6c
+  __TEXT.__objc_methtype: 0x89
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_assocty: 0x48
-  __TEXT.__cstring: 0x2bc
-  __TEXT.__oslogstring: 0x37f
-  __TEXT.__swift_as_entry: 0x34
-  __TEXT.__swift_as_ret: 0x34
-  __TEXT.__swift_as_cont: 0x50
   __TEXT.__objc_classname: 0xa2
-  __TEXT.__objc_methname: 0x190
-  __TEXT.__objc_methtype: 0xe3
-  __TEXT.__swift5_capture: 0x180
-  __TEXT.__unwind_info: 0x398
-  __TEXT.__eh_frame: 0x7b4
-  __DATA_CONST.__const: 0x460
+  __TEXT.__objc_methname: 0x160
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__unwind_info: 0x4c8
+  __TEXT.__eh_frame: 0x8d0
+  __DATA_CONST.__const: 0xa08
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__auth_got: 0x748
-  __DATA_CONST.__got: 0x288
-  __DATA_CONST.__auth_ptr: 0x2c0
-  __DATA.__objc_const: 0x1e8
-  __DATA.__objc_selrefs: 0x58
+  __DATA_CONST.__auth_got: 0x758
+  __DATA_CONST.__got: 0x2d0
+  __DATA_CONST.__auth_ptr: 0x2e8
+  __DATA.__objc_const: 0x1e0
+  __DATA.__objc_selrefs: 0x50
   __DATA.__objc_data: 0x100
-  __DATA.__data: 0x430
-  __DATA.__bss: 0x3d0
+  __DATA.__data: 0x5d8
+  __DATA.__bss: 0x4f0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 227
-  Symbols:   136
-  CStrings:  66
+  Functions: 319
+  Symbols:   133
+  CStrings:  70
 
Symbols:
- _swift_cvw_allocateGenericValueMetadataWithLayoutString
- _swift_getExistentialTypeMetadata
- _swift_getGenericMetadata
CStrings:
+ "%s Could not construct URL to launch Messages"
+ "%s didLaunchApp %{bool}d"
+ "Approve in person flow completed with answerChoice == %s. error: %s"
+ "AskToViewExtension/ApproveInPersonFlowView.swift"
+ "AskToViewExtension/AskToApproveFlowView.swift"
+ "Attempting to open url to launch Messages %{private}s"
+ "Direct Approve in person flow completed with answerChoice == %s. error: %s"
+ "Error finishing AskToViewExtension with result: %@"
+ "Failed to launch Messages with error: %@"
+ "Presenting direct approve in person"
+ "Presenting direct ask to approve"
+ "View.task @ AskToViewExtension/ApproveInPersonFlowView.swift:"
+ "View.task @ AskToViewExtension/AskToApproveFlowView.swift:"
+ "launchMessagesAndStagePayload(result:)"
- "%s Error calling acknowledgmentAlertButtonTapped: %@"
- "Approve in person flow completed with success == %@. error: %@"
- "Attempting to open url to launch Messages %s"
- "Failed to launch Messages on macOS with error: %@"
- "_launchMessagesAndStagePayload(result:)"
- "acknowledgmentAlertButtonTappedWithQuestion:action:reply:"
- "notifyDaemonOfAlertAction(_:)"
- "presentMessageCompose didLaunchApp %{bool}d"
- "v40@0:8@\"_TtC5AskTo10ATQuestion\"16q24@?<v@?@\"NSError\">32"
- "v40@0:8@16q24@?32"
```
