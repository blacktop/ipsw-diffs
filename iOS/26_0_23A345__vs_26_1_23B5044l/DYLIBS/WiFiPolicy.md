## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

-1026.80.0.0.0
-  __TEXT.__text: 0xbf168
+1035.2.0.0.0
+  __TEXT.__text: 0xbf21c
   __TEXT.__auth_stubs: 0x1620
   __TEXT.__objc_methlist: 0x11700
   __TEXT.__const: 0x648
-  __TEXT.__cstring: 0x1ce4a
+  __TEXT.__cstring: 0x1ce0b
   __TEXT.__oslogstring: 0x3d90
   __TEXT.__gcc_except_tab: 0x1980
   __TEXT.__dlopen_cstrs: 0x56

   __DATA_CONST.__objc_arraydata: 0xac0
   __AUTH_CONST.__auth_got: 0xb28
   __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__cfstring: 0x192c0
+  __AUTH_CONST.__cfstring: 0x192a0
   __AUTH_CONST.__objc_const: 0x217f0
   __AUTH_CONST.__objc_intobj: 0x1848
   __AUTH_CONST.__objc_arrayobj: 0x3a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E232BD9E-9974-3D1D-94DC-C409BD59950F
-  Functions: 6168
-  Symbols:   20133
-  CStrings:  16700
+  UUID: 7194E63D-897C-3CB6-B946-BC282B901797
+  Functions: 6169
+  Symbols:   20135
+  CStrings:  16698
 
Symbols:
+ GCC_except_table43
+ GCC_except_table46
+ ___24-[WiFiSoftError dealloc]_block_invoke
+ ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.369
- GCC_except_table42
- GCC_except_table45
- ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.372
Functions:
~ -[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:] : 888 -> 856
~ -[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:] : 1736 -> 1748
~ ___31-[WFMeasure doULThroughputTest]_block_invoke_2 : 632 -> 656
~ ___39-[WFMeasure start:withCompletionQueue:]_block_invoke : 248 -> 280
~ -[WiFiSoftError dealloc] : 528 -> 568
+ ___24-[WiFiSoftError dealloc]_block_invoke
CStrings:
- "%s Rejected due to [WiFiUsagePrivacyFilter isInternalInstall]\n"

```
