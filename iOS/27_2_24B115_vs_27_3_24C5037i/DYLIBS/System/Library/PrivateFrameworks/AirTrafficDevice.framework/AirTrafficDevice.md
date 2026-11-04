## AirTrafficDevice

> `/System/Library/PrivateFrameworks/AirTrafficDevice.framework/AirTrafficDevice`

```diff

-4026.200.21.0.0
-  __TEXT.__text: 0x1f0488
+4026.300.13.0.0
+  __TEXT.__text: 0x1f06d8
   __TEXT.__objc_methlist: 0x37d0
   __TEXT.__dlopen_cstrs: 0x202
   __TEXT.__const: 0x1e1e8
-  __TEXT.__gcc_except_tab: 0xad8
-  __TEXT.__cstring: 0x2b36
-  __TEXT.__oslogstring: 0x7260
+  __TEXT.__gcc_except_tab: 0xaf8
+  __TEXT.__cstring: 0x2b90
+  __TEXT.__oslogstring: 0x72ac
   __TEXT.__unwind_info: 0x1888
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29e0
+  __DATA_CONST.__objc_selrefs: 0x29f0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__got: 0x888
   __AUTH_CONST.__const: 0x118a8
-  __AUTH_CONST.__cfstring: 0x2e40
+  __AUTH_CONST.__cfstring: 0x2ee0
   __AUTH_CONST.__objc_const: 0x6258
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x650
+  __AUTH_CONST.__auth_got: 0x658
   __DATA.__objc_ivar: 0x4b0
   __DATA.__data: 0x1750
   __DATA.__common: 0xb20
   __DATA_DIRTY.__objc_data: 0x11d0
   __DATA_DIRTY.__data: 0xc0
-  __DATA_DIRTY.__bss: 0xc0
+  __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/BackgroundTasks.framework/BackgroundTasks

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1679
-  Symbols:   3037
-  CStrings:  986
+  Symbols:   3040
+  CStrings:  992
 
Symbols:
+ _MSVBundleIDForAuditToken
+ __ReportMissingEntitlementOnce.lock
+ __ReportMissingEntitlementOnce.reportedBundleIDs
Functions:
~ -[ATXPCListener listener:shouldAcceptNewConnection:] : 832 -> 1424
CStrings:
+ "MissingATCPrivateEntitlement"
+ "bundleID"
+ "com.apple.atc.private"
+ "entitlement"
+ "pid %i (%{public}@) connected without %{public}@ (alreadyReported=%{BOOL}u)"
+ "processIdentifier"
```
