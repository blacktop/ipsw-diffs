## VisionKitCore

> `/System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-342.0.0.0.0
-  __TEXT.__text: 0xe70bc
-  __TEXT.__objc_methlist: 0x10624
+344.0.0.0.0
+  __TEXT.__text: 0xe7604
+  __TEXT.__objc_methlist: 0x1063c
   __TEXT.__const: 0x1e80
-  __TEXT.__gcc_except_tab: 0x26e8
+  __TEXT.__gcc_except_tab: 0x2708
   __TEXT.__cstring: 0x829d
-  __TEXT.__oslogstring: 0x41a7
+  __TEXT.__oslogstring: 0x42a7
   __TEXT.__dlopen_cstrs: 0x7f7
   __TEXT.__ustring: 0x4e
   __TEXT.__constg_swiftt: 0x19c8

   __TEXT.__swift_as_cont: 0x18
   __TEXT.__swift5_capture: 0x134
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x4380
+  __TEXT.__unwind_info: 0x4398
   __TEXT.__eh_frame: 0x4c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3c70
+  __DATA_CONST.__const: 0x3c98
   __DATA_CONST.__objc_classlist: 0x680
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9890
+  __DATA_CONST.__objc_selrefs: 0x98a8
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0x2a0
   __DATA_CONST.__got: 0xf70
-  __AUTH_CONST.__const: 0x19c0
+  __AUTH_CONST.__const: 0x1980
   __AUTH_CONST.__cfstring: 0x68c0
-  __AUTH_CONST.__objc_const: 0x311d0
+  __AUTH_CONST.__objc_const: 0x31200
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_doubleobj: 0xe0
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x1088
+  __AUTH_CONST.__auth_got: 0x1090
   __AUTH.__objc_data: 0x43c0
   __AUTH.__data: 0x11e0
   __DATA.__objc_ivar: 0x1140

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6776
-  Symbols:   14210
-  CStrings:  1620
+  Functions: 6780
+  Symbols:   14218
+  CStrings:  1625
 
Symbols:
+ -[VKAVCapture attachSessionToPreviewLayer:completion:]
+ -[VKAVCaptureFrameProvider _sessionAttachedToPreviewLayer]
+ ___54-[VKAVCapture attachSessionToPreviewLayer:completion:]_block_invoke
+ ___54-[VKAVCapture attachSessionToPreviewLayer:completion:]_block_invoke_2
+ ___58-[VKAVCaptureFrameProvider _sessionAttachedToPreviewLayer]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e21_v16?0"VKAVCapture"8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ _dyld_program_sdk_at_least
+ _objc_msgSend$preheatFor:environmentBundleIdentifier:
- ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
CStrings:
+ "%@ preparation complete, attaching session to preview layer"
+ "%@ preparation complete2, startWhenReady=%d"
+ "%@ session attached to preview layer, now connecting sample buffer delegate"
+ "Prewarming with preheat"
+ "Prewarming with preheatFor:environmentBundleIdentifier:"
```
