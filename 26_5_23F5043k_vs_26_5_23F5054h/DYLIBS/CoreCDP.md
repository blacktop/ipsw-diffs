## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

-416.575.3.0.0
-  __TEXT.__text: 0x51edc
+416.575.6.0.0
+  __TEXT.__text: 0x52220
   __TEXT.__auth_stubs: 0x1020
-  __TEXT.__objc_methlist: 0x39ec
+  __TEXT.__objc_methlist: 0x3a34
   __TEXT.__const: 0x139c
-  __TEXT.__gcc_except_tab: 0x131c
+  __TEXT.__gcc_except_tab: 0x130c
   __TEXT.__oslogstring: 0x919a
-  __TEXT.__cstring: 0x6111
+  __TEXT.__cstring: 0x6189
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__ustring: 0x28
   __TEXT.__unwind_info: 0x1680
-  __TEXT.__objc_classname: 0x71d
-  __TEXT.__objc_methname: 0x917c
+  __TEXT.__objc_classname: 0x71e
+  __TEXT.__objc_methname: 0x91af
   __TEXT.__objc_methtype: 0x1c0f
-  __TEXT.__objc_stubs: 0x4f60
+  __TEXT.__objc_stubs: 0x4fc0
   __DATA_CONST.__got: 0x4e0
-  __DATA_CONST.__const: 0x2f98
+  __DATA_CONST.__const: 0x2f88
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2188
+  __DATA_CONST.__objc_selrefs: 0x2198
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0x820
   __AUTH_CONST.__const: 0x610
-  __AUTH_CONST.__cfstring: 0x3c00
-  __AUTH_CONST.__objc_const: 0x8778
+  __AUTH_CONST.__cfstring: 0x3c80
+  __AUTH_CONST.__objc_const: 0x87e8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x2f4
+  __DATA.__objc_ivar: 0x2fc
   __DATA.__data: 0x1118
   __DATA.__bss: 0x121
   __DATA.__common: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A6FA851B-0F0F-3C32-91B3-46A3C4308920
-  Functions: 2346
-  Symbols:   7849
-  CStrings:  3812
+  UUID: 636C80BF-BA51-3C1A-9C63-42B8732E3B6F
+  Functions: 2352
+  Symbols:   7868
+  CStrings:  3822
 
Symbols:
+ -[CDPContext isActivePDPState]
+ -[CDPFollowUpContext applyTelemetryFromCDPContext:]
+ -[CDPFollowUpContext pdpHealth]
+ -[CDPFollowUpContext pdpState]
+ -[CDPFollowUpContext setPdpHealth:]
+ -[CDPFollowUpContext setPdpState:]
+ -[CDPProtectedCloudStorageProxyImpl _callHealWalrusSPIWithAccountIdentifier:parameters:error:]
+ -[CDPProtectedCloudStorageProxyImpl _callHealWalrusSPIWithAccountIdentifier:parameters:error:].cold.1
+ GCC_except_table51
+ _OBJC_IVAR_$_CDPFollowUpContext._pdpHealth
+ _OBJC_IVAR_$_CDPFollowUpContext._pdpState
+ ___block_descriptor_48_e8_32s40bs_e45_v24?0"CDPCombinedWalrusStatus"8"NSError"16ls32l8s40l8
+ _kCDPAnalyticsADPHealingPCSEvent
+ _kCDPAnalyticsPDPBlobGenerationEvent
+ _kCDPAnalyticsPDPBlobGenerationStartEvent
+ _objc_msgSend$_callHealWalrusSPIWithAccountIdentifier:parameters:error:
+ _objc_msgSend$applyTelemetryFromCDPContext:
+ _objc_msgSend$setPdpHealth:
+ _objc_msgSend$setPdpState:
- +[AAFAnalyticsEvent(CDP) analyticsEventWithFollowUpContext:eventName:category:]
- -[CDPProtectedCloudStorageProxyImpl healBrokenADPEnablementWithAccountIdentifier:parameters:completion:].cold.2
- GCC_except_table47
- ___block_descriptor_56_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs_e45_v24?0"CDPCombinedWalrusStatus"8"NSError"16ls32l8s40l8
- _objc_msgSend$_makeAnalyticsEvent:state:error:
CStrings:
+ "#!"
+ "_callHealWalrusSPIWithAccountIdentifier:parameters:error:"
+ "applyTelemetryFromCDPContext:"
+ "com.apple.corecdp.adpHealingPCS"
+ "com.apple.corecdp.pdpBlobGeneration"
+ "com.apple.corecdp.pdpBlobGenerationStart"
+ "isActivePDPState"
- "$"
- "analyticsEventWithFollowUpContext:eventName:category:"

```
