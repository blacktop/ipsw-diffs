## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

 1035.3.0.0.0
-  __TEXT.__text: 0xbf46c
+  __TEXT.__text: 0xbf480
   __TEXT.__auth_stubs: 0x1630
   __TEXT.__objc_methlist: 0x11700
   __TEXT.__const: 0x648
-  __TEXT.__cstring: 0x1ce78
+  __TEXT.__cstring: 0x1ceb7
   __TEXT.__oslogstring: 0x3e14
   __TEXT.__gcc_except_tab: 0x1980
   __TEXT.__dlopen_cstrs: 0x56

   __DATA_CONST.__objc_arraydata: 0xac0
   __AUTH_CONST.__auth_got: 0xb30
   __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__cfstring: 0x192e0
+  __AUTH_CONST.__cfstring: 0x19300
   __AUTH_CONST.__objc_const: 0x217f0
   __AUTH_CONST.__objc_intobj: 0x1848
   __AUTH_CONST.__objc_arrayobj: 0x3a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 10653EAD-8D06-3AC5-9492-34A1D0B4D315
+  UUID: 4AEC08C2-BD53-3D05-A159-E55D848EE452
   Functions: 6170
   Symbols:   20139
-  CStrings:  16706
+  CStrings:  16708
 
Symbols:
+ ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.372
- ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.369
Functions:
~ -[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:] : 856 -> 888
~ -[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:] : 1748 -> 1736
CStrings:
+ "%s Rejected due to [WiFiUsagePrivacyFilter isInternalInstall]\n"

```
