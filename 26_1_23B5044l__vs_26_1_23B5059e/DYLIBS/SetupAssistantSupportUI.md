## SetupAssistantSupportUI

> `/System/Library/PrivateFrameworks/SetupAssistantSupportUI.framework/SetupAssistantSupportUI`

```diff

-546.0.0.0.0
-  __TEXT.__text: 0x53ec0
-  __TEXT.__auth_stubs: 0x1f40
-  __TEXT.__objc_methlist: 0x1a30
-  __TEXT.__const: 0x3294
-  __TEXT.__cstring: 0x2a7a
-  __TEXT.__gcc_except_tab: 0x1c8
+548.0.0.0.0
+  __TEXT.__text: 0x54d2c
+  __TEXT.__auth_stubs: 0x1ef0
+  __TEXT.__objc_methlist: 0x1a48
+  __TEXT.__const: 0x32a4
+  __TEXT.__cstring: 0x2aca
+  __TEXT.__gcc_except_tab: 0x1e4
   __TEXT.__oslogstring: 0x13d3
   __TEXT.__dlopen_cstrs: 0x130
-  __TEXT.__swift5_typeref: 0x1e7b
-  __TEXT.__swift5_capture: 0x530
+  __TEXT.__swift5_typeref: 0x1e67
+  __TEXT.__swift5_capture: 0x54c
   __TEXT.__swift5_reflstr: 0x13cf
   __TEXT.__swift5_assocty: 0x240
-  __TEXT.__constg_swiftt: 0x23f0
+  __TEXT.__constg_swiftt: 0x23d8
   __TEXT.__swift5_fieldmd: 0x152c
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_proto: 0x190

   __TEXT.__swift5_mpenum: 0x1c
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x64
-  __TEXT.__unwind_info: 0x18a8
+  __TEXT.__unwind_info: 0x18c8
   __TEXT.__eh_frame: 0x1248
   __TEXT.__objc_classname: 0x2b8
-  __TEXT.__objc_methname: 0x4586
+  __TEXT.__objc_methname: 0x45df
   __TEXT.__objc_methtype: 0x2259
-  __TEXT.__objc_stubs: 0x1040
+  __TEXT.__objc_stubs: 0x1080
   __DATA_CONST.__got: 0x4f0
-  __DATA_CONST.__const: 0x3a0
+  __DATA_CONST.__const: 0x3f0
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13d8
+  __DATA_CONST.__objc_selrefs: 0x13e0
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0xfb0
-  __AUTH_CONST.__const: 0x38c8
+  __AUTH_CONST.__auth_got: 0xf88
+  __AUTH_CONST.__const: 0x39d8
   __AUTH_CONST.__cfstring: 0x3c0
-  __AUTH_CONST.__objc_const: 0x8e48
+  __AUTH_CONST.__objc_const: 0x8e78
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x1080
-  __AUTH.__data: 0x2380
-  __DATA.__objc_ivar: 0x7c
-  __DATA.__data: 0x1118
+  __AUTH.__objc_data: 0x1060
+  __AUTH.__data: 0x2398
+  __DATA.__objc_ivar: 0x80
+  __DATA.__data: 0x10f8
   __DATA.__bss: 0x2dd8
   __DATA.__common: 0x108
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6210DF29-84E3-39C0-A499-EEC6EDB39778
-  Functions: 2255
-  Symbols:   2018
-  CStrings:  1507
+  UUID: A44B3CF3-5675-3C09-AE5A-322CD3F95ED1
+  Functions: 2280
+  Symbols:   2055
+  CStrings:  1511
 
Symbols:
+ -[SASCaptureSessionTextureDataSource onTextureQueue_displaySampleBuffer:]
+ -[SASCaptureSessionTextureDataSource onTextureQueue_displaySampleBuffer:].cold.1
+ -[SASCaptureSessionTextureDataSource onTextureQueue_displaySampleBuffer:].cold.2
+ -[SASCaptureSessionTextureDataSource setTextureQueue:]
+ -[SASCaptureSessionTextureDataSource textureQueue]
+ GCC_except_table14
+ _OBJC_IVAR_$_SASCaptureSessionTextureDataSource._textureQueue
+ ___42-[SASCaptureSessionTextureDataSource init]_block_invoke
+ ___42-[SASCaptureSessionTextureDataSource init]_block_invoke.cold.1
+ ___48-[SASCaptureSessionTextureDataSource invalidate]_block_invoke
+ ___52-[SASCaptureSessionTextureDataSource bookendTexture]_block_invoke
+ ___74-[SASCaptureSessionTextureDataSource captureSession:receivedSampleBuffer:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0ls32l8r40l8
+ _block_copy_helper.104
+ _block_copy_helper.132
+ _block_copy_helper.22
+ _block_copy_helper.34
+ _block_copy_helper.36
+ _block_copy_helper.46
+ _block_copy_helper.48
+ _block_copy_helper.55
+ _block_copy_helper.76
+ _block_copy_helper.90
+ _block_descriptor.106
+ _block_descriptor.134
+ _block_descriptor.24
+ _block_descriptor.36
+ _block_descriptor.38
+ _block_descriptor.48
+ _block_descriptor.50
+ _block_descriptor.57
+ _block_descriptor.78
+ _block_descriptor.92
+ _block_destroy_helper.105
+ _block_destroy_helper.133
+ _block_destroy_helper.23
+ _block_destroy_helper.35
+ _block_destroy_helper.37
+ _block_destroy_helper.47
+ _block_destroy_helper.49
+ _block_destroy_helper.56
+ _block_destroy_helper.77
+ _block_destroy_helper.91
+ _objc_msgSend$onTextureQueue_displaySampleBuffer:
+ _objc_msgSend$setTextureQueue:
+ _objc_msgSend$textureQueue
+ _objectdestroy.13Tm
+ _objectdestroy.25Tm
+ _symbolic ______p So10MTLTextureP
- -[SASCaptureSessionTextureDataSource displaySampleBuffer:]
- -[SASCaptureSessionTextureDataSource displaySampleBuffer:].cold.1
- -[SASCaptureSessionTextureDataSource displaySampleBuffer:].cold.2
- -[SASCaptureSessionTextureDataSource init].cold.1
- _block_copy_helper.141
- _block_copy_helper.33
- _block_copy_helper.40
- _block_copy_helper.43
- _block_copy_helper.53
- _block_descriptor.143
- _block_descriptor.35
- _block_descriptor.42
- _block_descriptor.45
- _block_descriptor.55
- _block_destroy_helper.142
- _block_destroy_helper.34
- _block_destroy_helper.41
- _block_destroy_helper.44
- _block_destroy_helper.54
- _dispatch_semaphore_create
- _objc_msgSend$displaySampleBuffer:
- _objectdestroy.31Tm
- _swift_unknownObjectRetain_n
- _symbolic So21OS_dispatch_semaphoreC
CStrings:
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_textureQueue"
+ "_textureQueue"
+ "com.apple.setupassistantsupportui.loadedTextureQueue"
+ "loadedTextureQueue"
+ "onTextureQueue_displaySampleBuffer:"
+ "setTextureQueue:"
+ "setupassistantsupport.textureDataSource.texture"
+ "textureQueue"
- "addCompletedHandler:"
- "displaySampleBuffer:"
- "inflightSemaphore"
- "v16@?0@\"<MTLCommandBuffer>\"8"

```
