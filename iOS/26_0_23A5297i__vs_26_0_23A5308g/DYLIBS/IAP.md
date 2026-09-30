## IAP

> `/System/Library/PrivateFrameworks/IAP.framework/IAP`

```diff

-2169.0.0.0.0
-  __TEXT.__text: 0x10738
-  __TEXT.__auth_stubs: 0x820
+2169.0.1.0.0
+  __TEXT.__text: 0x1093c
+  __TEXT.__auth_stubs: 0x870
   __TEXT.__objc_methlist: 0x4c4
   __TEXT.__const: 0x184d
-  __TEXT.__cstring: 0x639e
+  __TEXT.__cstring: 0x64da
   __TEXT.__gcc_except_tab: 0x38
   __TEXT.__unwind_info: 0x3b8
   __TEXT.__objc_classname: 0x85
   __TEXT.__objc_methname: 0x14d9
   __TEXT.__objc_methtype: 0x1bb
   __TEXT.__objc_stubs: 0xf80
-  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__got: 0x140
   __DATA_CONST.__const: 0x810
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x4f0
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x428
+  __AUTH_CONST.__auth_got: 0x450
   __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x38e0
+  __AUTH_CONST.__cfstring: 0x3960
   __AUTH_CONST.__objc_const: 0x9f8
   __DATA.__objc_ivar: 0x98
-  __DATA.__data: 0x210
+  __DATA.__data: 0x228
   __DATA.__bss: 0xa8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1e0

   __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F9519BEE-58AF-3B29-B590-174F9D01D9DA
-  Functions: 318
-  Symbols:   1437
-  CStrings:  1285
+  UUID: 4F7FBD13-E1C3-3194-A3A1-42D07EC644C0
+  Functions: 320
+  Symbols:   1450
+  CStrings:  1302
 
Symbols:
+ _SANDBOX_CHECK_NO_REPORT
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ __ZL12__hasSandboxPK8NSString
+ __ZL16__hasEntitlementPK8NSString
+ ___block_literal_global.140
+ ___block_literal_global.171
+ ___block_literal_global.182
+ ___block_literal_global.217
+ ___block_literal_global.219
+ _getpid
+ _nsIap2dServiceName
+ _nsIapdServiceName
+ _nsIaptransportdServiceName
+ _objc_autorelease
+ _sandbox_check
- ___block_literal_global.131
- ___block_literal_global.151
- ___block_literal_global.162
- ___block_literal_global.197
- ___block_literal_global.199
CStrings:
+ "%s: Client %sentitled to %@"
+ "%s: Client %ssandboxed to %@"
+ "%s: Client not entitled to %@"
+ "%s: Client not sandboxed to %@"
+ "%s: Unable to create self task"
+ "NOT "
+ "__hasEntitlement"
+ "__hasSandbox"
+ "com.apple.iap2d.xpc"
+ "com.apple.iapd.xpc"
+ "com.apple.iaptransportd.xpc"
+ "com.apple.security.exception.mach-lookup.global-name"
+ "mach-lookup"

```
