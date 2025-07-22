## MechanismBase

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase`

```diff

-2005.0.40.0.0
-  __TEXT.__text: 0x17fd4
+2005.0.49.0.0
+  __TEXT.__text: 0x18078
   __TEXT.__auth_stubs: 0x5f0
   __TEXT.__objc_methlist: 0x1da8
   __TEXT.__const: 0x128
-  __TEXT.__gcc_except_tab: 0x3b4
+  __TEXT.__gcc_except_tab: 0x410
   __TEXT.__cstring: 0x1070
-  __TEXT.__oslogstring: 0x14e1
+  __TEXT.__oslogstring: 0x14f0
   __TEXT.__unwind_info: 0x780
   __TEXT.__objc_classname: 0x404
-  __TEXT.__objc_methname: 0x4dc2
-  __TEXT.__objc_methtype: 0xebe
+  __TEXT.__objc_methname: 0x4dc9
+  __TEXT.__objc_methtype: 0xed3
   __TEXT.__objc_stubs: 0x3a20
   __DATA_CONST.__got: 0x288
-  __DATA_CONST.__const: 0x948
+  __DATA_CONST.__const: 0x920
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 818CFE34-7EE5-3875-9A3A-934645B03F05
+  UUID: CB7343AF-AF9C-34DF-81CF-459AC23050CA
   Functions: 629
-  Symbols:   2517
-  CStrings:  1469
+  Symbols:   2516
+  CStrings:  1470
 
Symbols:
+ -[RemoteUIActivator _processParams:interface:]
+ -[RemoteUIManager didSuccessfullyFinishForRequestIdentifier:]
+ -[_RemoteUIManager didSuccessfullyFinishForRequestIdentifier:]
+ ___46-[RemoteUIActivator _processParams:interface:]_block_invoke
+ ___46-[RemoteUIActivator _processParams:interface:]_block_invoke.cold.1
+ ___61-[RemoteUIManager didSuccessfullyFinishForRequestIdentifier:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48w_e17_v16?0"NSError"8ls32l8w48l8s40l8
+ _objc_msgSend$_processParams:interface:
+ _objc_msgSend$didSuccessfullyFinishForRequestIdentifier:
- -[RemoteUIActivator _processRequest:interface:]
- -[RemoteUIManager didSuccessfullyFinishForRequestId:]
- -[_RemoteUIManager didSuccessfullyFinishForRequestId:]
- ___47-[RemoteUIActivator _processRequest:interface:]_block_invoke
- ___47-[RemoteUIActivator _processRequest:interface:]_block_invoke.cold.1
- ___53-[RemoteUIManager didSuccessfullyFinishForRequestId:]_block_invoke
- ___block_descriptor_44_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_48_e8_32s40w_e17_v16?0"NSError"8ls32l8w40l8
- _objc_msgSend$_processRequest:interface:
- _objc_msgSend$didSuccessfullyFinishForRequestId:
Functions:
~ -[RemoteUIManager didSuccessfullyFinishForRequestId:] -> -[RemoteUIManager didSuccessfullyFinishForRequestIdentifier:] : 180 -> 204
~ -[_RemoteUIManager connectionToViewServiceInvalidatedForIdentifier:reply:] : 480 -> 492
~ -[_RemoteUIManager didSuccessfullyFinishForRequestId:] -> -[_RemoteUIManager didSuccessfullyFinishForRequestIdentifier:] : 244 -> 276
~ -[RemoteUIActivator _activateUserInterface:withParams:] : 896 -> 544
~ -[RemoteUIActivator _processRequest:interface:] -> -[RemoteUIActivator _processParams:interface:] : 248 -> 684
~ ___47-[RemoteUIActivator _processRequest:interface:]_block_invoke -> ___46-[RemoteUIActivator _processParams:interface:]_block_invoke : 540 -> 552
CStrings:
+ "Activator did successfully finish request identifier: %{public}@"
+ "Current request identifier: %@ is different from the connection identifier: %@"
+ "_processParams:interface:"
+ "didSuccessfullyFinishForRequestIdentifier:"
+ "v24@0:8@\"NSString\"16"
- "Activator did successfully finish request rid: %u"
- "Current request identifier: %u is different from the connection identifier: %@"
- "_processRequest:interface:"
- "didSuccessfullyFinishForRequestId:"

```
