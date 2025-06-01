## RemoteTextInput

> `/System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput`

```diff

-139.203.0.0.0
-  __TEXT.__text: 0x1b67c
-  __TEXT.__auth_stubs: 0x670
+139.303.0.0.0
+  __TEXT.__text: 0x1b7dc
+  __TEXT.__auth_stubs: 0x680
   __TEXT.__objc_methlist: 0x2288
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x287a
-  __TEXT.__oslogstring: 0xbaf
+  __TEXT.__cstring: 0x28bc
+  __TEXT.__oslogstring: 0xbed
   __TEXT.__gcc_except_tab: 0x158
   __TEXT.__dlopen_cstrs: 0xb1
-  __TEXT.__unwind_info: 0x758
+  __TEXT.__unwind_info: 0x768
   __TEXT.__objc_classname: 0x3cf
-  __TEXT.__objc_methname: 0x64c8
+  __TEXT.__objc_methname: 0x64dc
   __TEXT.__objc_methtype: 0x14f6
   __TEXT.__objc_stubs: 0x3ac0
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x8e8
+  __DATA_CONST.__const: 0x908
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x5aa8
   __DATA_CONST.__objc_selrefs: 0x1528
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__cfstring: 0x2500
+  __AUTH_CONST.__cfstring: 0x25c0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x348
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x1e0
-  __DATA.__objc_superrefs: 0xc8
+  __AUTH_CONST.__auth_got: 0x350
   __DATA.__objc_ivar: 0x2e0
   __DATA.__data: 0x4b0
   __DATA.__bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 455DF864-A367-3DD8-BB28-65FA7B3D7CCD
-  Functions: 867
-  Symbols:   3149
-  CStrings:  2012
+  UUID: F16E4CEB-750D-38C2-882B-2B9BA0006D77
+  Functions: 870
+  Symbols:   3155
+  CStrings:  2025
 
Symbols:
+ __RTI_NSStringFromRTIInputModality
+ ___51-[RTIInputSystemServiceSession initWithConnection:]_block_invoke.91
+ ___58-[RTIInputSystemClient _configureConnection:withMachName:]_block_invoke.125
+ ___58-[RTIInputSystemClient _configureConnection:withMachName:]_block_invoke.129
+ ___62-[RTIInputSystemClient endAllowingRemoteTextInput:completion:]_block_invoke.136
+ ___65-[RTIInputSystemServiceSession flushOperationsWithResultHandler:]_block_invoke.97
+ ___65-[RTIInputSystemServiceSession flushOperationsWithResultHandler:]_block_invoke.97.cold.1
+ ___66-[RTIInputSystemServiceSession performDocumentRequest:completion:]_block_invoke.99
+ ___66-[RTIInputSystemServiceSession performDocumentRequest:completion:]_block_invoke.99.cold.1
+ ___73-[RTIInputSystemClient _endSessionWithID:forServices:options:completion:]_block_invoke.139
+ ___73-[RTIInputSystemClient _endSessionWithID:forServices:options:completion:]_block_invoke_2.141
+ ___73-[RTIInputSystemClient _endSessionWithID:forServices:options:completion:]_block_invoke_2.141.cold.1
+ ___75-[RTIInputSystemClient endRemoteTextInputSessionWithID:options:completion:]_block_invoke.148
+ _sel_getName
- ___51-[RTIInputSystemServiceSession initWithConnection:]_block_invoke.90
- ___58-[RTIInputSystemClient _configureConnection:withMachName:]_block_invoke.124
- ___58-[RTIInputSystemClient _configureConnection:withMachName:]_block_invoke.128
- ___62-[RTIInputSystemClient endAllowingRemoteTextInput:completion:]_block_invoke.135
- ___65-[RTIInputSystemServiceSession flushOperationsWithResultHandler:]_block_invoke.96
- ___65-[RTIInputSystemServiceSession flushOperationsWithResultHandler:]_block_invoke.96.cold.1
- ___66-[RTIInputSystemServiceSession performDocumentRequest:completion:]_block_invoke.98
- ___66-[RTIInputSystemServiceSession performDocumentRequest:completion:]_block_invoke.98.cold.1
- ___73-[RTIInputSystemClient _endSessionWithID:forServices:options:completion:]_block_invoke.138
- ___73-[RTIInputSystemClient _endSessionWithID:forServices:options:completion:]_block_invoke_2.140
- ___73-[RTIInputSystemClient _endSessionWithID:forServices:options:completion:]_block_invoke_2.140.cold.1
- ___75-[RTIInputSystemClient endRemoteTextInputSessionWithID:options:completion:]_block_invoke.147
CStrings:
+ "%s  perform input operation requires a valid sessionID. inputModality = %@, inputOperation = %s, customInfoType = %@"
+ "; hasText = YES"
+ "Camera"
+ "Dictation"
+ "HardwareKeyboard"
+ "Keyboard"
+ "Pencil"
+ "T@\"NSString\",?,R,C"
- "%s  perform input operation requires a valid sessionID"

```
