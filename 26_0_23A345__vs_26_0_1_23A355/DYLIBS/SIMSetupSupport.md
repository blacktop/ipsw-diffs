## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-871.3.0.0.0
-  __TEXT.__text: 0xb3bc0
+871.4.0.0.0
+  __TEXT.__text: 0xb4394
   __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0xa00c
+  __TEXT.__objc_methlist: 0xa05c
   __TEXT.__const: 0x1b8
-  __TEXT.__gcc_except_tab: 0x1ca0
-  __TEXT.__cstring: 0xfb5d
-  __TEXT.__oslogstring: 0x65f6
+  __TEXT.__gcc_except_tab: 0x1cc4
+  __TEXT.__cstring: 0xfbe8
+  __TEXT.__oslogstring: 0x6614
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x2530
-  __TEXT.__objc_classname: 0x158c
+  __TEXT.__unwind_info: 0x2548
+  __TEXT.__objc_classname: 0x15b8
   __TEXT.__objc_methname: 0x16622
   __TEXT.__objc_methtype: 0x354f
   __TEXT.__objc_stubs: 0xe1a0
-  __DATA_CONST.__got: 0xa70
+  __DATA_CONST.__got: 0xa78
   __DATA_CONST.__const: 0x1d50
-  __DATA_CONST.__objc_classlist: 0x480
+  __DATA_CONST.__objc_classlist: 0x488
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x50e8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x428
+  __DATA_CONST.__objc_superrefs: 0x430
   __DATA_CONST.__objc_arraydata: 0x68
   __AUTH_CONST.__auth_got: 0x430
   __AUTH_CONST.__const: 0x840
-  __AUTH_CONST.__cfstring: 0x74e0
-  __AUTH_CONST.__objc_const: 0x3d2a8
+  __AUTH_CONST.__cfstring: 0x7520
+  __AUTH_CONST.__objc_const: 0x3d808
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x2cb0
-  __DATA.__objc_ivar: 0xec0
+  __AUTH.__objc_data: 0x2d00
+  __DATA.__objc_ivar: 0xec4
   __DATA.__data: 0xbb0
   __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B0C456A9-6B2D-300B-955A-CA5C4DFF4FCD
-  Functions: 3874
-  Symbols:   14035
-  CStrings:  7376
+  UUID: 80B5E918-747B-38C3-9459-1B05B947FD43
+  Functions: 3883
+  Symbols:   14069
+  CStrings:  7383
 
Symbols:
+ -[SSeSIMCountRestrictionWarningViewController .cxx_destruct]
+ -[SSeSIMCountRestrictionWarningViewController _continueButtonTapped]
+ -[SSeSIMCountRestrictionWarningViewController delegate]
+ -[SSeSIMCountRestrictionWarningViewController init]
+ -[SSeSIMCountRestrictionWarningViewController setDelegate:]
+ -[SSeSIMCountRestrictionWarningViewController viewDidLoad]
+ _OBJC_CLASS_$_SSeSIMCountRestrictionWarningViewController
+ _OBJC_IVAR_$_SSeSIMCountRestrictionWarningViewController._delegate
+ _OBJC_METACLASS_$_SSeSIMCountRestrictionWarningViewController
+ __OBJC_$_INSTANCE_METHODS_SSeSIMCountRestrictionWarningViewController
+ __OBJC_$_INSTANCE_VARIABLES_SSeSIMCountRestrictionWarningViewController
+ __OBJC_$_PROP_LIST_SSeSIMCountRestrictionWarningViewController
+ __OBJC_CLASS_PROTOCOLS_$_SSeSIMCountRestrictionWarningViewController
+ __OBJC_CLASS_RO_$_SSeSIMCountRestrictionWarningViewController
+ __OBJC_METACLASS_RO_$_SSeSIMCountRestrictionWarningViewController
+ ___32-[TSQRCodeScanFlow handleError:]_block_invoke_6
+ ___32-[TSQRCodeScanFlow handleError:]_block_invoke_7
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.103.cold.1
+ ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.104
+ ___72-[TSActivationFlowWithSimSetupFlow _requestCarrierSetupsWithCompletion:]_block_invoke.112
+ ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.106
+ ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.106.cold.1
+ ___block_literal_global.678
+ ___block_literal_global.708
+ ___block_literal_global.768
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.100
- ___64-[TSActivationFlowWithSimSetupFlow _requestPlansWithCompletion:]_block_invoke.100.cold.1
- ___72-[TSActivationFlowWithSimSetupFlow _requestCarrierSetupsWithCompletion:]_block_invoke.111
- ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.105
- ___75-[TSActivationFlowWithSimSetupFlow _requestTransferPlanListWithCompletion:]_block_invoke.105.cold.1
- ___block_literal_global.672
- ___block_literal_global.702
- ___block_literal_global.762
CStrings:
+ "-[TSActivationFlowWithSimSetupFlow _createFirstViewController:]"
+ "ESIM_COUNT_RESTRICTION_WARNING_DETAIL"
+ "ESIM_COUNT_RESTRICTION_WARNING_TITLE"
+ "SSeSIMCountRestrictionWarningViewController"
+ "cannot install more eSIMs @%s"

```
