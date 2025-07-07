## AppSSOCore

> `/System/Library/PrivateFrameworks/AppSSOCore.framework/AppSSOCore`

```diff

-483.0.19.0.0
-  __TEXT.__text: 0x12990
-  __TEXT.__auth_stubs: 0x670
+483.0.24.0.0
+  __TEXT.__text: 0x12a98
+  __TEXT.__auth_stubs: 0x680
   __TEXT.__objc_methlist: 0x1224
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x18bb
-  __TEXT.__oslogstring: 0x1849
+  __TEXT.__cstring: 0x18c1
+  __TEXT.__oslogstring: 0x185d
   __TEXT.__gcc_except_tab: 0x3a0
-  __TEXT.__unwind_info: 0x518
+  __TEXT.__unwind_info: 0x510
   __TEXT.__objc_classname: 0x223
   __TEXT.__objc_methname: 0x2830
   __TEXT.__objc_methtype: 0x7ea
   __TEXT.__objc_stubs: 0x1ba0
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x548
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__const: 0x550
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__auth_got: 0x348
+  __AUTH_CONST.__auth_got: 0x350
   __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0xfa0
+  __AUTH_CONST.__cfstring: 0xfc0
   __AUTH_CONST.__objc_const: 0x2bf8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 80FA6460-7CD3-3D5E-A3FB-0D107C07C67D
-  Functions: 511
-  Symbols:   1845
-  CStrings:  993
+  UUID: 68D867B1-E0E7-31C3-BC97-E966E854B2B8
+  Functions: 512
+  Symbols:   1848
+  CStrings:  997
 
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
