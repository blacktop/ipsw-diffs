## MechanismBase

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase`

```diff

-2005.0.31.0.0
-  __TEXT.__text: 0x1848c
+2005.0.40.0.0
+  __TEXT.__text: 0x17fd4
   __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_methlist: 0x1e10
+  __TEXT.__objc_methlist: 0x1da8
   __TEXT.__const: 0x128
-  __TEXT.__gcc_except_tab: 0x404
-  __TEXT.__cstring: 0x108b
+  __TEXT.__gcc_except_tab: 0x3b4
+  __TEXT.__cstring: 0x1070
   __TEXT.__oslogstring: 0x14e1
-  __TEXT.__unwind_info: 0x7b0
-  __TEXT.__objc_classname: 0x407
-  __TEXT.__objc_methname: 0x4e87
-  __TEXT.__objc_methtype: 0xf33
-  __TEXT.__objc_stubs: 0x3a40
+  __TEXT.__unwind_info: 0x780
+  __TEXT.__objc_classname: 0x404
+  __TEXT.__objc_methname: 0x4dc2
+  __TEXT.__objc_methtype: 0xebe
+  __TEXT.__objc_stubs: 0x3a20
   __DATA_CONST.__got: 0x288
-  __DATA_CONST.__const: 0x970
+  __DATA_CONST.__const: 0x948
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1228
+  __DATA_CONST.__objc_selrefs: 0x1218
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x308
-  __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x1000
-  __AUTH_CONST.__objc_const: 0x54c8
+  __AUTH_CONST.__const: 0x220
+  __AUTH_CONST.__cfstring: 0xfe0
+  __AUTH_CONST.__objc_const: 0x53f0
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x25c
+  __DATA.__objc_ivar: 0x254
   __DATA.__data: 0x720
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__bss: 0x48

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6BE83D20-2FAC-3A5F-84ED-83C16260ECB9
-  Functions: 641
-  Symbols:   2550
-  CStrings:  1478
+  UUID: 818CFE34-7EE5-3875-9A3A-934645B03F05
+  Functions: 629
+  Symbols:   2517
+  CStrings:  1469
 
Symbols:
+ GCC_except_table34
+ GCC_except_table39
+ GCC_except_table45
+ GCC_except_table49
+ ___52-[_RemoteUIManager connectRemoteUI:requestID:reply:]_block_invoke.131
+ ___79-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:shouldIdle:reply:]_block_invoke.98
+ _objc_msgSend$authenticationSuccessfulForEvent:
- -[RemoteUIActivator notificationManager]
- -[RemoteUIActivator setNotificationManager:]
- -[RemoteUIActivator_Legacy notificationManager]
- -[RemoteUIActivator_Legacy setNotificationManager:]
- -[RemoteUIManager setNotificationManager:]
- -[_RemoteUIManager setNotificationManager:]
- GCC_except_table37
- GCC_except_table4
- GCC_except_table42
- GCC_except_table48
- GCC_except_table5
- GCC_except_table55
- GCC_except_table7
- _OBJC_IVAR_$_RemoteUIActivator._notificationManager
- _OBJC_IVAR_$_RemoteUIActivator_Legacy._notificationManager
- ___100-[RemoteUIActivator_Legacy _postNotificationsAndActivateRemoteAlertHandle:activationContext:params:]_block_invoke
- ___42-[RemoteUIManager setNotificationManager:]_block_invoke
- ___47-[RemoteUIActivator _processRequest:interface:]_block_invoke.12
- ___52-[_RemoteUIManager connectRemoteUI:requestID:reply:]_block_invoke.133
- ___55-[RemoteUIActivator _activateUserInterface:withParams:]_block_invoke
- ___59-[RemoteUIActivator_Legacy remoteAlertHandleDidDeactivate:]_block_invoke
- ___79-[_RemoteUIManager dismissRemoteUI:uiMechanism:uiDisappeared:shouldIdle:reply:]_block_invoke.100
- ___80-[RemoteUIActivator_Legacy _activateRemoteAlertHandle:activationContext:params:]_block_invoke
- ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
- ___block_literal_global.37
- _objc_msgSend$postNotificationOfClassNamed:newValue:oldValue:completionHandler:
- _objc_msgSend$setNotificationManager:
CStrings:
+ "#"
+ "authenticationSuccessfulForEvent:"
- "@\"<LACLegacyNotificationPosting>\""
- "@\"<LACLegacyNotificationPosting>\"16@0:8"
- "LANotificationUIAppearance"
- "T@\"<LACLegacyNotificationPosting>\",&,N"
- "T@\"<LACLegacyNotificationPosting>\",&,N,V_notificationManager"
- "_notificationManager"
- "notificationManager"
- "postNotificationOfClassNamed:newValue:oldValue:completionHandler:"
- "setNotificationManager:"
- "v24@0:8@\"<LACLegacyNotificationPosting>\"16"

```
