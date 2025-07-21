## AppSSOCore

> `/System/Library/PrivateFrameworks/AppSSOCore.framework/AppSSOCore`

```diff

-417.140.2.0.0
-  __TEXT.__text: 0x11f54
-  __TEXT.__auth_stubs: 0x660
+417.140.3.0.0
+  __TEXT.__text: 0x1205c
+  __TEXT.__auth_stubs: 0x670
   __TEXT.__objc_methlist: 0x11fc
   __TEXT.__const: 0x118
-  __TEXT.__cstring: 0x17d7
-  __TEXT.__oslogstring: 0x1849
+  __TEXT.__cstring: 0x17dd
+  __TEXT.__oslogstring: 0x185d
   __TEXT.__gcc_except_tab: 0x388
   __TEXT.__unwind_info: 0x500
   __TEXT.__objc_classname: 0x223
   __TEXT.__objc_methname: 0x26e8
   __TEXT.__objc_methtype: 0x7bd
   __TEXT.__objc_stubs: 0x1b20
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x458
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__const: 0x460
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__auth_got: 0x340
+  __AUTH_CONST.__auth_got: 0x348
   __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0xf80
+  __AUTH_CONST.__cfstring: 0xfa0
   __AUTH_CONST.__objc_const: 0x2bf8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A7459D27-91A2-38E2-8253-4F81859AEEEF
-  Functions: 497
-  Symbols:   1815
-  CStrings:  981
+  UUID: DCFD7F5F-F9F2-3DBC-A7E2-96423AF69CE1
+  Functions: 498
+  Symbols:   1818
+  CStrings:  985
 
Symbols:
+ +[SOUtils bundleIdentifierFromAuditToken:].cold.2
+ _SecTaskGetCodeSignStatus
+ ___block_literal_global.10
+ ___block_literal_global.7
+ ___block_literal_global.81
+ _kApplePlatformBinaryTeamIdentifier
- ___block_literal_global.6
- ___block_literal_global.78
- ___block_literal_global.9
- _kCFAllocatorDefault
Functions (modified):
~ +[SOUtils bundleIdentifierFromAuditToken:] : 572 -> 652
~ +[SOUtils teamIdentifierFromAuditToken:] : 504 -> 620

Functions (added):
+ +[SOUtils bundleIdentifierFromAuditToken:].cold.2
CStrings:
+ "Apple"
+ "bundleIdentifier: CPCopyBundleIdentifierAndTeamFromAuditToken() failed"
+ "bundleIdentifier: The entitlements are not valid."
+ "bundleIdentifier: using SecTaskCopySigningIdentifier()"
+ "teamIdentifier: CPCopyBundleIdentifierAndTeamFromAuditToken() failed"
+ "teamIdentifier: The entitlements are not valid."
+ "teamIdentifier: using SecTaskCopyTeamIdentifier()"
- "bundleIdentifier: CPCopyBundleIdentifierAndTeamFromAuditToken() failed, trying SecTaskCopySigningIdentifier()"
- "bundleIdentifier: SecTaskCreateWithAuditToken() failed"
- "teamIdentifier: CPCopyBundleIdentifierAndTeamFromAuditToken() failed, trying SecTaskCopyTeamIdentifier()"
- "teamIdentifier: SecTaskCreateWithAuditToken() failed"

```
