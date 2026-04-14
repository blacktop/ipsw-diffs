## AirPlayOverlaysServer

> `/System/Library/PrivateFrameworks/AirPlayOverlaysServer.framework/AirPlayOverlaysServer`

```diff

-774.19.0.0.0
-  __TEXT.__text: 0x25628
-  __TEXT.__auth_stubs: 0x1060
-  __TEXT.__objc_methlist: 0x2ec
-  __TEXT.__const: 0xf48
+774.23.0.0.0
+  __TEXT.__text: 0x270c8
+  __TEXT.__auth_stubs: 0x10f0
+  __TEXT.__objc_methlist: 0x304
+  __TEXT.__const: 0xf98
   __TEXT.__gcc_except_tab: 0x28
   __TEXT.__cstring: 0x13f
-  __TEXT.__oslogstring: 0x9cc
-  __TEXT.__swift5_typeref: 0x6c9
-  __TEXT.__swift5_capture: 0x55c
-  __TEXT.__constg_swiftt: 0x5e4
-  __TEXT.__swift5_reflstr: 0x537
-  __TEXT.__swift5_fieldmd: 0x434
-  __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_types: 0x68
-  __TEXT.__swift_as_entry: 0x88
-  __TEXT.__swift_as_ret: 0x60
+  __TEXT.__oslogstring: 0xa3c
+  __TEXT.__swift5_typeref: 0x6fb
+  __TEXT.__swift5_capture: 0x56c
+  __TEXT.__constg_swiftt: 0x60c
+  __TEXT.__swift5_reflstr: 0x557
+  __TEXT.__swift5_fieldmd: 0x468
+  __TEXT.__swift5_builtin: 0x64
+  __TEXT.__swift5_types: 0x6c
+  __TEXT.__swift_as_entry: 0x8c
+  __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0x58
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x910
-  __TEXT.__eh_frame: 0xeb8
+  __TEXT.__unwind_info: 0x998
+  __TEXT.__eh_frame: 0xfe8
   __TEXT.__objc_classname: 0x3ef
-  __TEXT.__objc_methname: 0xa6a
-  __TEXT.__objc_methtype: 0x2f3
-  __TEXT.__objc_stubs: 0x5c0
-  __DATA_CONST.__got: 0x2c0
+  __TEXT.__objc_methname: 0xa9a
+  __TEXT.__objc_methtype: 0x303
+  __TEXT.__objc_stubs: 0x620
+  __DATA_CONST.__got: 0x2f0
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x268
+  __DATA_CONST.__objc_selrefs: 0x280
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x840
-  __AUTH_CONST.__const: 0xe68
-  __AUTH_CONST.__objc_const: 0xc68
+  __AUTH_CONST.__auth_got: 0x888
+  __AUTH_CONST.__const: 0xf20
+  __AUTH_CONST.__objc_const: 0xcb8
   __AUTH.__objc_data: 0x420
-  __AUTH.__data: 0xa98
-  __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0x438
+  __AUTH.__data: 0xaa0
+  __DATA.__objc_ivar: 0x8
+  __DATA.__data: 0x460
   __DATA.__bss: 0x870
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2D4777F7-E6BF-34A6-9FA2-AD9DB00D4500
-  Functions: 684
-  Symbols:   558
-  CStrings:  229
+  UUID: E8657774-26D4-3441-872C-7560F15B1094
+  Functions: 717
+  Symbols:   585
+  CStrings:  237
 
Symbols:
+ -[APOOverlaysServer activateOverlaySessionOnEndpoint:figEndpoint:].cold.4
+ -[APOOverlaysServer deactivateOverlaySessionOnEndpoint:].cold.1
+ -[APOOverlaysServer sessionId]
+ -[APOOverlaysServer setSessionId:]
+ _OBJC_IVAR_$_APOOverlaysServer._sessionId
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ ___swift_memcpy16_8
+ _block_copy_helper.202
+ _block_copy_helper.220
+ _block_descriptor.204
+ _block_descriptor.222
+ _block_destroy_helper.203
+ _block_destroy_helper.221
+ _objc_getProperty
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$sessionId
+ _objc_msgSend$setSessionId:
+ _objc_setProperty_atomic
+ _objectdestroy.27Tm
+ _symbolic _____ 12CoreGraphics7CGFloatV
+ _symbolic _____ So6CGSizeV
+ _symbolic _____y_____GSg 21AirPlayOverlaysServer26RenderNodeContainerBuilderV 0aB3Kit0G7ContentV
+ _symbolic _____y_____y_____GSgG s23_ContiguousArrayStorageC 21AirPlayOverlaysServer26RenderNodeContainerBuilderV 0dE3Kit0J7ContentV
+ _type_layout_string So6CGSizeV
- _block_copy_helper.199
- _block_copy_helper.217
- _block_descriptor.201
- _block_descriptor.219
- _block_destroy_helper.200
- _block_destroy_helper.218
- _objectdestroy.23Tm
CStrings:
+ "@\"NSString\""
+ "Overlay session is already active with sessionId %@"
+ "Overlay session is already deactivated with sessionId %@"
+ "T@\"NSString\",&,V_sessionId"
+ "Waiting for display info to create render node"
+ "_sessionId"
+ "barSize"
+ "isEqualToString:"
+ "setSessionId:"
- "Waiting for dispaly info to create render node"

```
