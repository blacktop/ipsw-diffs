## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

 1050.2.0.0.0
-  __TEXT.__text: 0xd7f10
+  __TEXT.__text: 0xd7f28
   __TEXT.__auth_stubs: 0x1730
   __TEXT.__objc_methlist: 0x124d0
   __TEXT.__const: 0x6e8
-  __TEXT.__cstring: 0x202c5
+  __TEXT.__cstring: 0x20304
   __TEXT.__oslogstring: 0x4862
   __TEXT.__gcc_except_tab: 0x1920
   __TEXT.__dlopen_cstrs: 0xf3

   __DATA_CONST.__objc_arraydata: 0xb50
   __AUTH_CONST.__auth_got: 0xbb0
   __AUTH_CONST.__const: 0x4e0
-  __AUTH_CONST.__cfstring: 0x1b2a0
+  __AUTH_CONST.__cfstring: 0x1b2c0
   __AUTH_CONST.__objc_const: 0x22ef0
   __AUTH_CONST.__objc_intobj: 0x19f8
   __AUTH_CONST.__objc_arrayobj: 0x3f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BA8B664B-2FF0-33FB-B29F-1240D5F3C1B2
+  UUID: 8E486B50-1323-3DD9-B460-D46304203EED
   Functions: 6570
   Symbols:   21430
-  CStrings:  17726
+  CStrings:  17728
 
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
