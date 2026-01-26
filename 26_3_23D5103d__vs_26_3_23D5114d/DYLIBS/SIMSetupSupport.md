## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-883.7.0.0.0
-  __TEXT.__text: 0xb9858
+883.9.0.0.0
+  __TEXT.__text: 0xba4fc
   __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0xa3b4
+  __TEXT.__objc_methlist: 0xa3fc
   __TEXT.__const: 0x1d0
-  __TEXT.__gcc_except_tab: 0x1dc0
-  __TEXT.__cstring: 0x107a6
-  __TEXT.__oslogstring: 0x6c1f
+  __TEXT.__gcc_except_tab: 0x1dcc
+  __TEXT.__cstring: 0x10a02
+  __TEXT.__oslogstring: 0x6d7b
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x2640
+  __TEXT.__unwind_info: 0x2658
   __TEXT.__objc_classname: 0x15de
-  __TEXT.__objc_methname: 0x16f1d
+  __TEXT.__objc_methname: 0x16fb0
   __TEXT.__objc_methtype: 0x35f7
-  __TEXT.__objc_stubs: 0xe680
+  __TEXT.__objc_stubs: 0xe6e0
   __DATA_CONST.__got: 0xa78
   __DATA_CONST.__const: 0x1db0
   __DATA_CONST.__objc_classlist: 0x488
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x52c8
+  __DATA_CONST.__objc_selrefs: 0x52e8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x430
   __DATA_CONST.__objc_arraydata: 0x1a8
   __AUTH_CONST.__auth_got: 0x430
-  __AUTH_CONST.__const: 0x8e0
-  __AUTH_CONST.__cfstring: 0x79a0
-  __AUTH_CONST.__objc_const: 0x3dfb8
+  __AUTH_CONST.__const: 0x900
+  __AUTH_CONST.__cfstring: 0x7ac0
+  __AUTH_CONST.__objc_const: 0x3e008
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH.__objc_data: 0x2d00
-  __DATA.__objc_ivar: 0xf00
+  __DATA.__objc_ivar: 0xf08
   __DATA.__data: 0xbb0
   __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 766EB3CD-0698-3FE9-AF40-9892D7406728
-  Functions: 3973
-  Symbols:   14335
-  CStrings:  7579
+  UUID: 53294ED0-8638-38E3-87BB-F133E849DFA9
+  Functions: 3982
+  Symbols:   14357
+  CStrings:  7613
 
Symbols:
+ -[CrossPlatformTransferSourceSelectionWarningViewController _cancelButtonTapped]
+ -[CrossPlatformTransferSourceSelectionWarningViewController isCancelTapped]
+ -[CrossPlatformTransferSourceSelectionWarningViewController setIsCancelTapped:]
+ -[TSCrossPlatformSourceTransferFlow _showCancelAlert:withMessage:]
+ -[TSNoPlanForTransferViewController initShowCarrierNotSupportCrossPlatformTransfer]
+ _OBJC_IVAR_$_CrossPlatformTransferSourceSelectionWarningViewController._client
+ _OBJC_IVAR_$_CrossPlatformTransferSourceSelectionWarningViewController._isCancelTapped
+ ___66-[TSCrossPlatformSourceTransferFlow _showCancelAlert:withMessage:]_block_invoke
+ ___66-[TSCrossPlatformSourceTransferFlow _showCancelAlert:withMessage:]_block_invoke_2
+ ___80-[CrossPlatformTransferSourceSelectionWarningViewController _cancelButtonTapped]_block_invoke
+ ___80-[CrossPlatformTransferSourceSelectionWarningViewController _cancelButtonTapped]_block_invoke.cold.1
+ ___block_literal_global.101
+ _objc_msgSend$declineCrossPlatformTransfer:
+ _objc_msgSend$initShowCarrierNotSupportCrossPlatformTransfer
+ _objc_msgSend$isCancelTapped
CStrings:
+ "-[CrossPlatformTransferSourceSelectionWarningViewController _cancelButtonTapped]"
+ "-[CrossPlatformTransferSourceSelectionWarningViewController _cancelButtonTapped]_block_invoke"
+ "-[SSCrossPlatformTransferSourceSelectionViewController _continueButtonTapped:]"
+ "CROSSPLATFORM_TRANSFER_CARRIER_LOCK"
+ "CROSSPLATFORM_TRANSFER_CARRIER_LOCK_DETAIL"
+ "CROSSPLATFORM_TRANSFER_CARRIER_NOT_SUPPORT"
+ "CROSSPLATFORM_TRANSFER_CARRIER_NOT_SUPPORT_DETAIL"
+ "CROSSTRANSFER_CONN_LOST_GENERAL"
+ "CROSSTRANSFER_CONN_LOST_GENERAL_MSG"
+ "CROSSTRANSFER_ERROR_NO_SCREEN_LOCK_DETAIL"
+ "CROSSTRANSFER_ERROR_NO_SCREEN_LOCK_TITLE"
+ "GreenTea Capable device, disable Cross Platform transfer @%s"
+ "GreenTea Capable device, no cross platform transfer suppported @%s"
+ "Select Plan %@ Carrier Name: %@ @%s"
+ "TB,V_isCancelTapped"
+ "UI is in terminal state, wait for user to dismiss @%s"
+ "[E]declineCrossPlatformTransfer fail @%s"
+ "_isCancelTapped"
+ "cancel button tapped, cancel the flow @%s"
+ "declineCrossPlatformTransfer:"
+ "initShowCarrierNotSupportCrossPlatformTransfer"
+ "isCancelTapped"
+ "kCrossTransferConnected = 0, not connected @%s"
+ "kCrossTransferTargetDenied"
+ "setIsCancelTapped:"

```
