## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

 992.1.0.0.0
-  __TEXT.__text: 0xb95fc
+  __TEXT.__text: 0xb9610
   __TEXT.__auth_stubs: 0x15f0
   __TEXT.__objc_methlist: 0x11108
   __TEXT.__const: 0x638
-  __TEXT.__cstring: 0x1c06c
+  __TEXT.__cstring: 0x1c0ab
   __TEXT.__oslogstring: 0x3b16
   __TEXT.__gcc_except_tab: 0x18f0
   __TEXT.__dlopen_cstrs: 0x56

   __DATA_CONST.__objc_arraydata: 0xa58
   __AUTH_CONST.__auth_got: 0xb10
   __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x187a0
+  __AUTH_CONST.__cfstring: 0x187c0
   __AUTH_CONST.__objc_const: 0x20b40
   __AUTH_CONST.__objc_intobj: 0x1740
   __AUTH_CONST.__objc_arrayobj: 0x390

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3AB9C8FF-EBF6-34E8-BEA7-DD0D87E971E7
+  UUID: 28A5F38E-C2B1-33F9-8FC6-487B025AD1DF
   Functions: 6017
   Symbols:   19661
-  CStrings:  16313
+  CStrings:  16315
 
Functions:
~ -[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:] : 856 -> 888
~ -[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:] : 1708 -> 1696
CStrings:
+ "%s Rejected due to [WiFiUsagePrivacyFilter isInternalInstall]\n"

```
