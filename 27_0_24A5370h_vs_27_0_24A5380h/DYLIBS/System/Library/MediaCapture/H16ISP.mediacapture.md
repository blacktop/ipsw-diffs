## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

```diff

-  __TEXT.__text: 0x1d3150
+  __TEXT.__text: 0x1d31ec
   __TEXT.__objc_methlist: 0x270
-  __TEXT.__gcc_except_tab: 0x63d8
-  __TEXT.__const: 0x2f1c8
-  __TEXT.__cstring: 0x19a11
-  __TEXT.__oslogstring: 0x1dc09
+  __TEXT.__gcc_except_tab: 0x63e4
+  __TEXT.__const: 0x2f208
+  __TEXT.__cstring: 0x19a20
+  __TEXT.__oslogstring: 0x1dbe4
   __TEXT.__unwind_info: 0x3fe0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__got: 0x3518
-  __AUTH_CONST.__const: 0x2dc0
+  __AUTH_CONST.__const: 0x2e38
   __AUTH_CONST.__cfstring: 0xa1c0
   __AUTH_CONST.__objc_const: 0x8a0
   __AUTH_CONST.__weak_auth_got: 0xa0

   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x38
   __DATA.__data: 0x373670
-  __DATA.__bss: 0x139
-  __DATA.__common: 0x34
+  __DATA.__bss: 0x121
+  __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x210
-  __DATA_DIRTY.__bss: 0x998
+  __DATA_DIRTY.__data: 0x218
+  __DATA_DIRTY.__bss: 0x9a8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5946
-  Symbols:   15276
-  CStrings:  7699
+  Functions: 5952
+  Symbols:   15282
+  CStrings:  7701
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ GCC_except_table40
+ __ZN6H16ISP21H16ISPJasperDepthNode18prepareForTeardownEv
+ __ZN6H16ISP33H16ISPGraphExclavePostProcessNode14runPostProcessEj
+ __ZN6H16ISP33H16ISPGraphExclavePostProcessNode19onMessageProcessingEPNS_24H16ISPFilterGraphMessageE
+ __ZN6H16ISP33H16ISPGraphExclavePostProcessNodeC1EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP33H16ISPGraphExclavePostProcessNodeC2EPNS_12H16ISPDeviceEj
+ __ZN6H16ISP33H16ISPGraphExclavePostProcessNodeD0Ev
+ __ZN6H16ISP33H16ISPGraphExclavePostProcessNodeD1Ev
+ __ZN6H16ISP33H16ISPGraphExclavePostProcessNodeD2Ev
+ __ZTIN6H16ISP33H16ISPGraphExclavePostProcessNodeE
+ __ZTSN6H16ISP33H16ISPGraphExclavePostProcessNodeE
+ __ZTVN6H16ISP33H16ISPGraphExclavePostProcessNodeE
+ ____ZN6H16ISP21H16ISPJasperDepthNode18prepareForTeardownEv_block_invoke
+ ___block_descriptor_104_e5_v8?0l
- ____ZN6H16ISP21H16ISPJasperDepthNode12onDeactivateEv_block_invoke
- ___block_descriptor_48_e5_v8?0l
CStrings:
+ "%s - Failed to run post process: err=%d\n"
+ "%s - post process run succeeded ch=%u reqid=0x%08x\n"
+ "%s - running post process ch=%u reqid=0x%08x\n"
+ "runPostProcess"
- "[Exclaves]: H16ISPGraphExclaveISPManagerNode::%s EK RGB ISP Manager POST PROCESS RunKit failed, ret=%d\n"
- "[Exclaves]: ISP POST PROCESS IDL Success: channel=%u, requestid=0x%08X\n"

```
