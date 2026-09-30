## AskToViewExtension

> `/System/iOSSupport/System/Library/ExtensionKit/Extensions/AskToViewExtension.appex/Contents/MacOS/AskToViewExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_data`

```diff

-93.0.0.0.0
-  __TEXT.__text: 0xf534
-  __TEXT.__auth_stubs: 0xeb0
+96.0.0.0.0
+  __TEXT.__text: 0x16674
+  __TEXT.__auth_stubs: 0xf30
   __TEXT.__objc_stubs: 0xe0
-  __TEXT.__objc_methlist: 0x50
-  __TEXT.__const: 0x5a8
-  __TEXT.__constg_swiftt: 0x1f8
-  __TEXT.__swift5_typeref: 0x6bd
-  __TEXT.__swift5_fieldmd: 0x128
-  __TEXT.__swift5_protos: 0x4
+  __TEXT.__objc_methlist: 0x34
+  __TEXT.__const: 0x8d8
+  __TEXT.__constg_swiftt: 0x27c
+  __TEXT.__swift5_typeref: 0x7f6
+  __TEXT.__cstring: 0x357
+  __TEXT.__swift5_reflstr: 0x2a3
+  __TEXT.__swift5_fieldmd: 0x20c
+  __TEXT.__swift5_assocty: 0x78
+  __TEXT.__swift5_capture: 0x3e0
+  __TEXT.__oslogstring: 0x45f
+  __TEXT.__swift5_proto: 0x1c
+  __TEXT.__swift5_types: 0x1c
+  __TEXT.__swift_as_entry: 0x40
+  __TEXT.__swift_as_ret: 0x40
+  __TEXT.__swift_as_cont: 0x64
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_reflstr: 0x1b3
-  __TEXT.__swift5_assocty: 0x48
-  __TEXT.__cstring: 0x288
-  __TEXT.__oslogstring: 0x37f
-  __TEXT.__swift5_proto: 0x14
-  __TEXT.__swift5_types: 0x10
-  __TEXT.__swift_as_entry: 0x34
-  __TEXT.__swift_as_ret: 0x30
-  __TEXT.__swift_as_cont: 0x48
   __TEXT.__objc_classname: 0xa2
-  __TEXT.__objc_methname: 0x170
-  __TEXT.__objc_methtype: 0xb9
-  __TEXT.__swift5_capture: 0x180
-  __TEXT.__unwind_info: 0x370
-  __TEXT.__eh_frame: 0x744
-  __DATA_CONST.__const: 0x408
+  __TEXT.__objc_methname: 0x140
+  __TEXT.__objc_methtype: 0x59
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__unwind_info: 0x4b0
+  __TEXT.__eh_frame: 0x8ac
+  __DATA_CONST.__const: 0x9b0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__auth_got: 0x760
-  __DATA_CONST.__got: 0x258
-  __DATA_CONST.__auth_ptr: 0x278
-  __DATA.__objc_const: 0x1e8
-  __DATA.__objc_selrefs: 0x50
+  __DATA_CONST.__auth_got: 0x7a0
+  __DATA_CONST.__got: 0x298
+  __DATA_CONST.__auth_ptr: 0x2a0
+  __DATA.__objc_const: 0x1e0
+  __DATA.__objc_selrefs: 0x48
   __DATA.__objc_data: 0x100
-  __DATA.__data: 0x3f8
-  __DATA.__bss: 0x2d0
+  __DATA.__data: 0x5a0
+  __DATA.__bss: 0x3f0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/Versions/A/ExtensionFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 211
-  Symbols:   151
-  CStrings:  63
+  Functions: 305
+  Symbols:   153
+  CStrings:  67
 
Symbols:
+ _objc_release_x28
+ _objc_retain_x25
+ _objc_retain_x26
+ _swift_release_x27
+ _swift_retain_x21
+ _swift_retain_x23
- _objc_retain_x20
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
