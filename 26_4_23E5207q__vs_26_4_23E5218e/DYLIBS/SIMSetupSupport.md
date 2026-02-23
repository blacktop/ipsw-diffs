## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-892.0.0.0.0
-  __TEXT.__text: 0xc0654
+894.1.0.0.0
+  __TEXT.__text: 0xc15c8
   __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_methlist: 0xa4ac
+  __TEXT.__objc_methlist: 0xa4cc
   __TEXT.__const: 0x1d8
   __TEXT.__gcc_except_tab: 0x1d80
-  __TEXT.__cstring: 0x10bc6
-  __TEXT.__oslogstring: 0x6e32
+  __TEXT.__cstring: 0x10d0b
+  __TEXT.__oslogstring: 0x6eea
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x2868
+  __TEXT.__unwind_info: 0x2870
   __TEXT.__objc_classname: 0x15de
-  __TEXT.__objc_methname: 0x1747f
-  __TEXT.__objc_methtype: 0x36fd
-  __TEXT.__objc_stubs: 0xe900
-  __DATA_CONST.__got: 0xa88
+  __TEXT.__objc_methname: 0x174ed
+  __TEXT.__objc_methtype: 0x3700
+  __TEXT.__objc_stubs: 0xe960
+  __DATA_CONST.__got: 0xa90
   __DATA_CONST.__const: 0x1db8
   __DATA_CONST.__objc_classlist: 0x488
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5390
+  __DATA_CONST.__objc_selrefs: 0x53a0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x430
   __DATA_CONST.__objc_arraydata: 0x1a8
   __AUTH_CONST.__auth_got: 0x418
-  __AUTH_CONST.__const: 0x8e0
-  __AUTH_CONST.__cfstring: 0x7bc0
+  __AUTH_CONST.__const: 0x920
+  __AUTH_CONST.__cfstring: 0x7c00
   __AUTH_CONST.__objc_const: 0x3e140
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F9F6DFEB-B21F-3472-84F6-7088B3FAA5B9
-  Functions: 4026
-  Symbols:   14665
-  CStrings:  7671
+  UUID: EEF5D19E-D489-34D5-848C-42A90B1C83F5
+  Functions: 4031
+  Symbols:   14680
+  CStrings:  7685
 
Symbols:
+ +[TSUtilities FormattedCarrierListFromSet:conjunction:]
+ -[TSCrossPlatformSourceTransferFlow appForegrounded]
+ -[TSCrossPlatformTargetTransferFlow appForegrounded]
+ -[TSTransferListViewController _maybeDisplayPhysicalPlanConversionAlert:showServiceImpact:phoneNumber:completion:]
+ -[TSTransferListViewController _maybeDisplayPhysicalPlanConversionAlert:showServiceImpact:phoneNumber:completion:].cold.1
+ _OBJC_IVAR_$_TSTransferListViewController._serviceImpact
+ ___114-[TSTransferListViewController _maybeDisplayPhysicalPlanConversionAlert:showServiceImpact:phoneNumber:completion:]_block_invoke
+ ___114-[TSTransferListViewController _maybeDisplayPhysicalPlanConversionAlert:showServiceImpact:phoneNumber:completion:]_block_invoke_2
+ ___52-[TSCrossPlatformSourceTransferFlow appForegrounded]_block_invoke
+ ___52-[TSCrossPlatformTargetTransferFlow appForegrounded]_block_invoke
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.234
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.236
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke_2.235
+ ___block_literal_global.105
+ ___block_literal_global.238
+ ___block_literal_global.309
+ ___block_literal_global.325
+ _objc_msgSend$FormattedCarrierListFromSet:conjunction:
+ _objc_msgSend$_maybeDisplayPhysicalPlanConversionAlert:showServiceImpact:phoneNumber:completion:
+ _objc_msgSend$hasProvisioningServiceImpact
+ _objc_msgSend$resumeCrossPlatformTransferSession:
- -[TSTransferListViewController _maybeDisplayPhysicalPlanConversionAlert:phoneNumber:completion:]
- -[TSTransferListViewController _maybeDisplayPhysicalPlanConversionAlert:phoneNumber:completion:].cold.1
- _OBJC_IVAR_$_TSSinglePlanTransferViewController._hasProvisioningServiceImpact
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.218
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.220
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke_2.219
- ___96-[TSTransferListViewController _maybeDisplayPhysicalPlanConversionAlert:phoneNumber:completion:]_block_invoke
- ___96-[TSTransferListViewController _maybeDisplayPhysicalPlanConversionAlert:phoneNumber:completion:]_block_invoke_2
- ___block_literal_global.222
- ___block_literal_global.306
- ___block_literal_global.322
- _objc_msgSend$_maybeDisplayPhysicalPlanConversionAlert:phoneNumber:completion:
CStrings:
+ "-[TSCrossPlatformSourceTransferFlow appForegrounded]"
+ "-[TSCrossPlatformSourceTransferFlow appForegrounded]_block_invoke"
+ "-[TSCrossPlatformTargetTransferFlow appForegrounded]"
+ "-[TSCrossPlatformTargetTransferFlow appForegrounded]_block_invoke"
+ "-[TSTransferListViewController _maybeDisplayPhysicalPlanConversionAlert:showServiceImpact:phoneNumber:completion:]"
+ "App entering foreground, resuming cross platform transfer session @%s"
+ "Failed to resume cross platform transfer session: %@ @%s"
+ "FormattedCarrierListFromSet:conjunction:"
+ "SERVICE_IMPACT_MESSAGE_%@"
+ "SERVICE_IMPACT_MESSAGE_NO_CARRIER"
+ "SERVICE_IMPACT_SPEED_BUMP_TITLE"
+ "Successfully resumed cross platform transfer session @%s"
+ "_maybeDisplayPhysicalPlanConversionAlert:showServiceImpact:phoneNumber:completion:"
+ "_serviceImpact"
+ "resumeCrossPlatformTransferSession:"
+ "v40@0:8B16B20@24@?32"
+ "\xf0!"
- "-[TSTransferListViewController _maybeDisplayPhysicalPlanConversionAlert:phoneNumber:completion:]"
- "SERVICE_IMPACT_MESSAGE"
- "_maybeDisplayPhysicalPlanConversionAlert:phoneNumber:completion:"
- "v36@0:8B16@20@?28"
- "\xf01"

```
