## FamilyControlsObjC

> `/System/Library/PrivateFrameworks/FamilyControlsObjC.framework/Versions/A/FamilyControlsObjC`

```diff

-1204.0.0.0.0
+1204.4.5.0.0
   __TEXT.__text: 0x2868
   __TEXT.__auth_stubs: 0x1b0
-  __TEXT.__objc_methlist: 0x1f4
-  __TEXT.__const: 0x68
+  __TEXT.__objc_methlist: 0x2b0
+  __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x44
   __TEXT.__cstring: 0xeb
   __TEXT.__oslogstring: 0x278

   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x228
+  __DATA_CONST.__objc_selrefs: 0x248
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0xe8
   __AUTH_CONST.__const: 0x170
   __AUTH_CONST.__cfstring: 0x120
-  __AUTH_CONST.__objc_const: 0x698
+  __AUTH_CONST.__objc_const: 0x548
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x120

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 625404E0-0112-3024-A74C-313EB6EE89F1
-  Functions: 74
-  Symbols:   251
+  UUID: E2737A74-2709-3567-8710-23ACCF7F36B0
+  Functions: 75
+  Symbols:   252
   CStrings:  154
 
Symbols:
+ +[FOAuthorizationCenter sharedCenter].cold.1
Functions:
~ +[FOAuthorizationCenter sharedCenter] : 84 -> 68
~ -[FOAuthorizationCenter xpcConnection] : 460 -> 452
~ _OUTLINED_FUNCTION_3 : 28 -> 12
~ -[FOAuthorizationRecord hash] : 196 -> 192
+ +[FOAuthorizationCenter sharedCenter].cold.1
~ __83-[FOAuthorizationCenter requestAuthorizationForRecordIdentifier:completionHandler:]_block_invoke_2.cold.1 : 112 -> 120
~ __81-[FOAuthorizationCenter requestInternalAuthorizationForMember:completionHandler:]_block_invoke_2.cold.1 : 72 -> 68
~ __81-[FOAuthorizationCenter resetAuthorizationForRecordIdentifier:completionHandler:]_block_invoke_2.cold.1 : 112 -> 120
~ __82-[FOAuthorizationCenter revokeAuthorizationForRecordIdentifier:completionHandler:]_block_invoke_2.cold.1 : 112 -> 120
~ __93-[FOAuthorizationCenter revokeAuthorizationForDeletionForRecordIdentifier:completionHandler:]_block_invoke_2.cold.1 : 112 -> 120
~ __74-[FOAuthorizationCenter revokeInternalAuthorizationWithCompletionHandler:]_block_invoke_2.cold.1 : 124 -> 120

```
