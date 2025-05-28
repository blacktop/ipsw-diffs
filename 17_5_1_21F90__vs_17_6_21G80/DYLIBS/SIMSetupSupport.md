## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-668.0.0.0.0
-  __TEXT.__text: 0x70e4c
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x5c8c
+673.0.0.0.0
+  __TEXT.__text: 0x71378
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__objc_methlist: 0x5cf4
   __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x936b
-  __TEXT.__oslogstring: 0x3f71
-  __TEXT.__gcc_except_tab: 0xd98
+  __TEXT.__cstring: 0x948f
+  __TEXT.__oslogstring: 0x3fa5
+  __TEXT.__gcc_except_tab: 0xd94
   __TEXT.__dlopen_cstrs: 0x1b6
-  __TEXT.__unwind_info: 0x1908
+  __TEXT.__unwind_info: 0x1920
   __TEXT.__objc_classname: 0xe80
-  __TEXT.__objc_methname: 0xfd51
+  __TEXT.__objc_methname: 0xfddd
   __TEXT.__objc_methtype: 0x2df6
-  __TEXT.__objc_stubs: 0xa600
+  __TEXT.__objc_stubs: 0xa620
   __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x1378
+  __DATA_CONST.__const: 0x1380
   __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x247e8
-  __DATA_CONST.__objc_selrefs: 0x35e0
+  __DATA_CONST.__objc_const: 0x24828
+  __DATA_CONST.__objc_selrefs: 0x3600
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0x688
   __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__cfstring: 0x4220
+  __AUTH_CONST.__cfstring: 0x4260
   __AUTH_CONST.__const: 0x580
   __AUTH_CONST.__objc_const: 0x2258
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x3f0
-  __AUTH_CONST.__auth_got: 0x3f0
+  __AUTH_CONST.__auth_got: 0x3f8
   __AUTH.__objc_data: 0x1e50
-  __DATA.__objc_ivar: 0x958
+  __DATA.__objc_ivar: 0x95c
   __DATA.__data: 0xa90
   __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2576
-  Symbols:   9408
-  CStrings:  4472
+  Functions: 2585
+  Symbols:   9430
+  CStrings:  4485
 
Symbols:
+ -[TSSinglePlanTransferViewController _userDisagreedTermsAndConditions]
+ -[TSTransferCloudFlow _updateSourceProxCardState:]
+ -[TSTransferCloudFlow isSourceProxCardVisible]
+ -[TSTransferCloudFlow setIsSourceProxCardVisible:]
+ -[TSTransferCloudFlow userDidTapCancel]
+ -[TSTransferCloudFlowModel clearCarrierSetupItemsCache]
+ -[TSTransferFlowModel areTransferPlansReady]
+ -[TSTransferFlowModel clearCarrierSetupItemsCache]
+ -[TSTransferFlowModel setAreTransferPlansReady:]
+ GCC_except_table60
+ GCC_except_table72
+ GCC_except_table73
+ _OBJC_IVAR_$_TSTransferCloudFlow._isSourceProxCardVisible
+ _TSNotificationUserDisagreedTermsAndConditions
+ ___39-[TSTransferFlow _firstViewController:]_block_invoke
+ ___82-[TSSinglePlanTransferViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.281
+ ___82-[TSSinglePlanTransferViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.285
+ ___block_literal_global.256
+ ___block_literal_global.287
+ ___block_literal_global.294
+ ___block_literal_global.434
+ ___block_literal_global.47
+ ___block_literal_global.487
+ _dispatch_get_current_queue
+ _objc_msgSend$clearCarrierSetupItemsCache
- -[TSTransferCloudFlow _userDidTapCancel]
- GCC_except_table22
- GCC_except_table27
- GCC_except_table57
- GCC_except_table68
- GCC_except_table69
- ___82-[TSSinglePlanTransferViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.279
- ___82-[TSSinglePlanTransferViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.283
- ___block_literal_global.254
- ___block_literal_global.285
- ___block_literal_global.292
- ___block_literal_global.431
- ___block_literal_global.484
CStrings:
+ "\x01!"
+ "-[TSSinglePlanTransferViewController _userDisagreedTermsAndConditions]"
+ "-[TSTransferCloudFlow _updateSourceProxCardState:]"
+ "-[TSTransferCloudFlowModel clearCarrierSetupItemsCache]"
+ "-[TSTransferFlowModel clearCarrierSetupItemsCache]"
+ "Clear carrier setup items cache @%s"
+ "Hide button tray! @%s"
+ "TB,N,V_areTransferPlansReady"
+ "TERMS_AND_CONDITIONS_TITLE"
+ "Transferrable plan %@ will be removed from the list @%s"
+ "_userDisagreedTermsAndConditions"
+ "areTransferPlansReady"
+ "clearCarrierSetupItemsCache"
+ "setAreTransferPlansReady:"
+ "user.disagreed.terms.and.conditions"
- "\x01\x11"
- "Account member plan %@ will be removed from transfer list @%s"

```
