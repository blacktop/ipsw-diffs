## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

```diff

-  __TEXT.__text: 0x18ff6c
-  __TEXT.__const: 0x2dce8
-  __TEXT.__oslogstring: 0x182ee
-  __TEXT.__cstring: 0x153c2
-  __TEXT.__gcc_except_tab: 0x4654
+  __TEXT.__text: 0x18ff30
+  __TEXT.__const: 0x2dd28
+  __TEXT.__oslogstring: 0x182c9
+  __TEXT.__cstring: 0x153d1
+  __TEXT.__gcc_except_tab: 0x4660
   __TEXT.__unwind_info: 0x3040
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_selrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x24d8
+  __AUTH_CONST.__const: 0x2550
   __AUTH_CONST.__cfstring: 0x7260
   __AUTH_CONST.__weak_auth_got: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x1370
   __DATA.__data: 0x373408
-  __DATA.__bss: 0x121
+  __DATA.__bss: 0x119
   __DATA.__common: 0x14
-  __DATA_DIRTY.__data: 0x1a0
-  __DATA_DIRTY.__bss: 0x918
+  __DATA_DIRTY.__data: 0x1a8
+  __DATA_DIRTY.__bss: 0x920
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4929
-  Symbols:   9213
-  CStrings:  6296
+  Functions: 4934
+  Symbols:   9222
+  CStrings:  6298
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
Symbols:
+ _ZN6H16ISP33H16ISPGraphExclavePostProcessNode14runPostProcessEj
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
CStrings:
+ "%s - Failed to run post process: err=%d\n"
+ "%s - post process run succeeded ch=%u reqid=0x%08x\n"
+ "%s - running post process ch=%u reqid=0x%08x\n"
+ "runPostProcess"
- "[Exclaves]: H16ISPGraphExclaveISPManagerNode::%s EK RGB ISP Manager POST PROCESS RunKit failed, ret=%d\n"
- "[Exclaves]: ISP POST PROCESS IDL Success: channel=%u, requestid=0x%08X\n"

```
