## DeviceDiscoveryUICore

> `/System/Library/PrivateFrameworks/DeviceDiscoveryUICore.framework/DeviceDiscoveryUICore`

```diff

-2086.10.3.2.2
-  __TEXT.__text: 0x3b924
+2088.10.21.0.0
+  __TEXT.__text: 0x3bd14
   __TEXT.__auth_stubs: 0x1970
-  __TEXT.__objc_methlist: 0x159c
-  __TEXT.__const: 0x29c8
+  __TEXT.__objc_methlist: 0x15a4
+  __TEXT.__const: 0x29d8
   __TEXT.__cstring: 0x2077
-  __TEXT.__oslogstring: 0x2f50
+  __TEXT.__oslogstring: 0x2f40
   __TEXT.__gcc_except_tab: 0x284
   __TEXT.__swift5_typeref: 0xce6
   __TEXT.__constg_swiftt: 0xb18

   __TEXT.__swift5_assocty: 0xb8
   __TEXT.__swift5_proto: 0x22c
   __TEXT.__swift5_types: 0xd4
-  __TEXT.__swift5_capture: 0x1ec
+  __TEXT.__swift5_capture: 0x1fc
   __TEXT.__swift_as_entry: 0x5c
   __TEXT.__swift_as_ret: 0x70
   __TEXT.__swift5_acfuncs: 0x28
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1188
-  __TEXT.__eh_frame: 0x18e0
+  __TEXT.__unwind_info: 0x1198
+  __TEXT.__eh_frame: 0x1930
   __TEXT.__objc_classname: 0x3fc
-  __TEXT.__objc_methname: 0x4071
+  __TEXT.__objc_methname: 0x409a
   __TEXT.__objc_methtype: 0xde8
-  __TEXT.__objc_stubs: 0x25e0
+  __TEXT.__objc_stubs: 0x2600
   __DATA_CONST.__got: 0x510
   __DATA_CONST.__const: 0x988
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1008
+  __DATA_CONST.__objc_selrefs: 0x1010
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x68
   __AUTH_CONST.__auth_got: 0xcc8
-  __AUTH_CONST.__const: 0x1838
+  __AUTH_CONST.__const: 0x1840
   __AUTH_CONST.__cfstring: 0x12a0
   __AUTH_CONST.__objc_const: 0x2dc8
   __AUTH_CONST.__objc_intobj: 0x60

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9E23F0CA-F30D-363A-B640-A84A189E8C31
-  Functions: 1456
-  Symbols:   2475
-  CStrings:  1493
+  UUID: F3A5CE38-59BA-3DD3-B119-DE14E976535A
+  Functions: 1462
+  Symbols:   2477
+  CStrings:  1494
 
Symbols:
+ -[DDUICoreAgent _setupDDUIServiceIfNeededWithCompletion:]
+ GCC_except_table27
+ ___30-[DDUICoreAgent _startOnQueue]_block_invoke_3
+ ___54-[DDUICoreAgent _setupListenerIfNeededWithCompletion:]_block_invoke.11
+ ___54-[DDUICoreAgent _setupListenerIfNeededWithCompletion:]_block_invoke.13
+ ___57-[DDUICoreAgent _setupDDUIServiceIfNeededWithCompletion:]_block_invoke
+ ___61-[DDUICoreAgent _handleIncomingContinuityCameraConfirmation:]_block_invoke.24
+ ___61-[DDUICoreAgent _handleIncomingContinuityCameraConfirmation:]_block_invoke.29
+ ___61-[DDUICoreAgent _handleIncomingContinuityCameraConfirmation:]_block_invoke.33
+ ___61-[DDUICoreAgent _handleIncomingContinuityCameraConfirmation:]_block_invoke.37
+ ___62-[DDUICoreAgent _handleIncomingPairingSession:pairingMessage:]_block_invoke.17
+ ___block_literal_global.9
+ _block_copy_helper.66
+ _block_copy_helper.80
+ _block_copy_helper.83
+ _block_descriptor.68
+ _block_descriptor.82
+ _block_descriptor.85
+ _block_destroy_helper.67
+ _block_destroy_helper.81
+ _block_destroy_helper.84
+ _objc_msgSend$_setupDDUIServiceIfNeededWithCompletion:
- GCC_except_table25
- ___30-[DDUICoreAgent _startOnQueue]_block_invoke.12
- ___30-[DDUICoreAgent _startOnQueue]_block_invoke.12.cold.1
- ___54-[DDUICoreAgent _setupListenerIfNeededWithCompletion:]_block_invoke.16
- ___54-[DDUICoreAgent _setupListenerIfNeededWithCompletion:]_block_invoke.18
- ___61-[DDUICoreAgent _handleIncomingContinuityCameraConfirmation:]_block_invoke.26
- ___61-[DDUICoreAgent _handleIncomingContinuityCameraConfirmation:]_block_invoke.31
- ___61-[DDUICoreAgent _handleIncomingContinuityCameraConfirmation:]_block_invoke.35
- ___61-[DDUICoreAgent _handleIncomingContinuityCameraConfirmation:]_block_invoke.39
- ___62-[DDUICoreAgent _handleIncomingPairingSession:pairingMessage:]_block_invoke.21
- ___block_literal_global.14
- ___block_literal_global.8
- _block_copy_helper.61
- _block_copy_helper.75
- _block_copy_helper.78
- _block_descriptor.63
- _block_descriptor.77
- _block_descriptor.80
- _block_destroy_helper.62
- _block_destroy_helper.76
- _block_destroy_helper.79
CStrings:
+ "Creating DDUI service"
+ "DDUI service started."
+ "_setupDDUIServiceIfNeededWithCompletion:"
- "Creating listener for modern DDUI here"
- "DDUI actor exited."

```
