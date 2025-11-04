## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

-1035.3.0.0.0
-  __TEXT.__text: 0xbf480
+1035.4.0.0.0
+  __TEXT.__text: 0xbf4ec
   __TEXT.__auth_stubs: 0x1630
   __TEXT.__objc_methlist: 0x11700
   __TEXT.__const: 0x648
-  __TEXT.__cstring: 0x1ceb7
+  __TEXT.__cstring: 0x1ce78
   __TEXT.__oslogstring: 0x3e14
   __TEXT.__gcc_except_tab: 0x1980
   __TEXT.__dlopen_cstrs: 0x56

   __DATA_CONST.__objc_selrefs: 0x9aa8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x438
-  __DATA_CONST.__objc_arraydata: 0xac0
+  __DATA_CONST.__objc_arraydata: 0xae0
   __AUTH_CONST.__auth_got: 0xb30
   __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__cfstring: 0x19300
+  __AUTH_CONST.__cfstring: 0x192e0
   __AUTH_CONST.__objc_const: 0x217f0
   __AUTH_CONST.__objc_intobj: 0x1848
   __AUTH_CONST.__objc_arrayobj: 0x3a8
-  __AUTH_CONST.__objc_dictobj: 0xf0
+  __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x7a8
   __DATA.__objc_ivar: 0x215c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4AEC08C2-BD53-3D05-A159-E55D848EE452
+  UUID: EDD0F5BC-F53F-3DD3-A45B-3D87041B4D67
   Functions: 6170
   Symbols:   20139
-  CStrings:  16708
+  CStrings:  16706
 
Symbols:
+ ___47-[WiFiSoftError updateHUDWithHost:messageDict:]_block_invoke.137
+ ___47-[WiFiSoftError updateHUDWithHost:messageDict:]_block_invoke.137.cold.1
+ ___49-[WiFiSoftError submitABCReportWithReason:event:]_block_invoke.105
+ ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.158
+ ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.158.cold.1
+ ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.369
+ ___block_literal_global.114
- ___47-[WiFiSoftError updateHUDWithHost:messageDict:]_block_invoke.125
- ___47-[WiFiSoftError updateHUDWithHost:messageDict:]_block_invoke.125.cold.1
- ___49-[WiFiSoftError submitABCReportWithReason:event:]_block_invoke.93
- ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.147
- ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.147.cold.1
- ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.372
- ___block_literal_global.102
Functions:
~ -[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:] : 888 -> 856
~ -[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:] : 1736 -> 1748
~ ___49-[WiFiSoftError submitABCReportWithReason:event:]_block_invoke : 624 -> 752
CStrings:
- "%s Rejected due to [WiFiUsagePrivacyFilter isInternalInstall]\n"

```
