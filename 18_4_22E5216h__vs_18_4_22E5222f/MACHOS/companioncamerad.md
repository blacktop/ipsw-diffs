## companioncamerad

> `/System/Library/PrivateFrameworks/CompanionCamera.framework/Support/companioncamerad`

```diff

-2022.300.9.0.0
-  __TEXT.__text: 0x1ff48
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__objc_stubs: 0x1de0
-  __TEXT.__objc_methlist: 0x2fdc
-  __TEXT.__cstring: 0x118f
-  __TEXT.__objc_methname: 0x34dc
+2022.300.12.0.0
+  __TEXT.__text: 0x20360
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_stubs: 0x1e00
+  __TEXT.__objc_methlist: 0x2fec
+  __TEXT.__cstring: 0x11cf
+  __TEXT.__objc_methname: 0x352c
   __TEXT.__objc_classname: 0x4bb
   __TEXT.__objc_methtype: 0x1183
   __TEXT.__const: 0xf0
-  __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__oslogstring: 0x60b
+  __TEXT.__gcc_except_tab: 0xe0
+  __TEXT.__oslogstring: 0x741
   __TEXT.__dlopen_cstrs: 0x4f
-  __TEXT.__unwind_info: 0x8a0
-  __DATA_CONST.__auth_got: 0x388
+  __TEXT.__unwind_info: 0x8b8
+  __DATA_CONST.__auth_got: 0x390
   __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0xa60
+  __DATA_CONST.__const: 0xad0
   __DATA_CONST.__cfstring: 0xca0
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x4c78
-  __DATA.__objc_selrefs: 0xef0
-  __DATA.__objc_ivar: 0x294
+  __DATA.__objc_const: 0x4c98
+  __DATA.__objc_selrefs: 0xef8
+  __DATA.__objc_ivar: 0x298
   __DATA.__objc_data: 0xe10
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x50

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1008
-  Symbols:   161
-  CStrings:  1057
+  Functions: 1012
+  Symbols:   162
+  CStrings:  1065
 
Symbols:
+ _notify_register_dispatch
CStrings:
+ "(connectionDidTearDown) Companion camera closed, sending open state change"
+ "Active camera reset, not starting preview endpoint or sending open message."
+ "Camera completed setup. Enqueuing finalization after XPC connection settle interval."
+ "Camera setup finalized. Sending open state change. (willStartPreviewEndpoint=%d)"
+ "[lifecycle] cameraPreviewIDSSocketCreationFailed"
+ "_cameraPreviewIDSSocketCreationFailedToken"
+ "cameraPreviewIDSSocketCreationFailed"
+ "com.apple.fignero.CameraPreviewIDSSocketCreationFailed"
+ "connectionDidTearDown"
+ "v12@?0i8"
- "Companion camera closed, sending open state change"
- "Sending open state change."

```
