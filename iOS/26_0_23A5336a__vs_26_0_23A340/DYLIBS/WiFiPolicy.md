## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

 1026.80.0.0.0
-  __TEXT.__text: 0xbf154
+  __TEXT.__text: 0xbf168
   __TEXT.__auth_stubs: 0x1620
   __TEXT.__objc_methlist: 0x11700
   __TEXT.__const: 0x648
-  __TEXT.__cstring: 0x1ce0b
+  __TEXT.__cstring: 0x1ce4a
   __TEXT.__oslogstring: 0x3d90
   __TEXT.__gcc_except_tab: 0x1980
   __TEXT.__dlopen_cstrs: 0x56

   __DATA_CONST.__objc_arraydata: 0xac0
   __AUTH_CONST.__auth_got: 0xb28
   __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__cfstring: 0x192a0
+  __AUTH_CONST.__cfstring: 0x192c0
   __AUTH_CONST.__objc_const: 0x217f0
   __AUTH_CONST.__objc_intobj: 0x1848
   __AUTH_CONST.__objc_arrayobj: 0x3a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C6D8A5AD-68E6-34F3-ADDD-A7A398E159F8
+  UUID: E232BD9E-9974-3D1D-94DC-C409BD59950F
   Functions: 6168
   Symbols:   20133
-  CStrings:  16698
+  CStrings:  16700
 
Symbols:
+ ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.372
- ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.369
Functions:
~ -[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:] : 856 -> 888
~ -[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:] : 1748 -> 1736
CStrings:
+ "%s Rejected due to [WiFiUsagePrivacyFilter isInternalInstall]\n"

```
