## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

 1041.25.0.0.0
-  __TEXT.__text: 0xd7be4
+  __TEXT.__text: 0xd7bfc
   __TEXT.__auth_stubs: 0x1730
   __TEXT.__objc_methlist: 0x12450
   __TEXT.__const: 0x6e8
-  __TEXT.__cstring: 0x2028d
+  __TEXT.__cstring: 0x202cc
   __TEXT.__oslogstring: 0x4862
   __TEXT.__gcc_except_tab: 0x1920
   __TEXT.__dlopen_cstrs: 0xf3

   __DATA_CONST.__objc_arraydata: 0xb50
   __AUTH_CONST.__auth_got: 0xbb0
   __AUTH_CONST.__const: 0x4e0
-  __AUTH_CONST.__cfstring: 0x1b260
+  __AUTH_CONST.__cfstring: 0x1b280
   __AUTH_CONST.__objc_const: 0x22e00
   __AUTH_CONST.__objc_intobj: 0x19f8
   __AUTH_CONST.__objc_arrayobj: 0x3f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 27D6028A-0EA2-3F5C-9826-ECB0CA298B06
+  UUID: 3E9D6C37-D44E-392C-8340-F5084E82A296
   Functions: 6559
   Symbols:   21402
-  CStrings:  17701
+  CStrings:  17703
 
Symbols:
+ ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.376
- ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.373
Functions:
~ -[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:] : 892 -> 924
~ -[WFMeasure initWithType:andReason:prevTestedOptions:andInterfaceName:] : 1756 -> 1744
~ -[WiFiUsageSession _generateState] : 1044 -> 1048
CStrings:
+ "%s Rejected due to [WiFiUsagePrivacyFilter isInternalInstall]\n"

```
