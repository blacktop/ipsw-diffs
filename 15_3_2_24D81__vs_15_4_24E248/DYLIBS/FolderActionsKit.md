## FolderActionsKit

> `/System/Library/PrivateFrameworks/FolderActionsKit.framework/Versions/A/FolderActionsKit`

```diff

 38.1.0.0.0
-  __TEXT.__text: 0x7864
+  __TEXT.__text: 0x783c
   __TEXT.__auth_stubs: 0x2c0
-  __TEXT.__objc_methlist: 0x7f4
+  __TEXT.__objc_methlist: 0xab4
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0xa8
   __TEXT.__cstring: 0x489
   __TEXT.__oslogstring: 0x205
-  __TEXT.__unwind_info: 0x2d8
+  __TEXT.__unwind_info: 0x2e0
   __TEXT.__objc_classname: 0x13b
   __TEXT.__objc_methname: 0x1d39
   __TEXT.__objc_methtype: 0x53f

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x768
+  __DATA_CONST.__objc_selrefs: 0x808
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x170
   __AUTH_CONST.__const: 0x2c0
   __AUTH_CONST.__cfstring: 0x4a0
-  __AUTH_CONST.__objc_const: 0x14b8
+  __AUTH_CONST.__objc_const: 0xf98
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x70
   __DATA.__data: 0x240

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1436876B-6200-36F9-B612-F2EB7C7D8E7F
-  Functions: 219
-  Symbols:   679
+  UUID: 1230452F-1D69-39E4-8FFB-96BB93BE4D0F
+  Functions: 220
+  Symbols:   680
   CStrings:  504
 
Functions:
~ -[FolderActionsDispatcher updateFolderActionsInfo:] : 268 -> 264
~ ___51-[FolderActionsDispatcher updateFolderActionsInfo:]_block_invoke : 868 -> 852
~ ___51-[FolderActionsDispatcher updateFolderActionsInfo:]_block_invoke_2 : 264 -> 260
~ -[FolderActionsDispatcher hasFolderActionWithURL:] : 412 -> 420
+ _OUTLINED_FUNCTION_0
~ -[FAFolderAction hasScriptWithURL:] : 412 -> 420
~ ___37-[FAScriptableObject objectSpecifier]_block_invoke : 336 -> 332
~ __37-[FAScriptableObject objectSpecifier]_block_invoke.16 : 336 -> 332
~ -[FAScript url] : 1184 -> 1192
~ -[FAXPCDelegate listener:shouldAcceptNewConnection:] : 744 -> 720
~ FAFolderActionDispatcherSetLaunchDaemonEnabled.cold.1 : 144 -> 216
~ FAFolderActionDispatcherSetLaunchDaemonEnabled.cold.2 : 216 -> 140
~ -[FolderActionsDispatcher dealloc].cold.1 : 172 -> 168
~ -[FolderActionsDispatcher addFrontEnd:].cold.1 : 128 -> 124
~ -[FolderActionsDispatcher updateFolderActionsInfo:].cold.1 : 72 -> 68
~ +[FolderActionsDispatcher _enableFolderActionsDispatcherLaunchDJobIfNeeded].cold.1 : 72 -> 68

```
