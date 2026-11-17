## AppSSOCore

> `/System/Library/PrivateFrameworks/AppSSOCore.framework/AppSSOCore`

```diff

-643.60.12.0.0
-  __TEXT.__text: 0x10ffc
-  __TEXT.__objc_methlist: 0x1214
+643.60.14.0.0
+  __TEXT.__text: 0x110e8
+  __TEXT.__objc_methlist: 0x121c
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x18de
-  __TEXT.__oslogstring: 0x185d
+  __TEXT.__cstring: 0x1908
+  __TEXT.__oslogstring: 0x18a0
   __TEXT.__gcc_except_tab: 0x1b8
-  __TEXT.__unwind_info: 0x730
+  __TEXT.__unwind_info: 0x738
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9a0
+  __DATA_CONST.__objc_selrefs: 0x9a8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x108

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 513
-  Symbols:   904
-  CStrings:  319
+  Functions: 515
+  Symbols:   905
+  CStrings:  321
 
Symbols:
+ +[SOUtils shouldTrustSuppliedAuditTokenFromPeerBundleIdentifier:suppliedTokenData:peerIsSocketDelegate:]
Functions:
+ +[SOUtils shouldTrustSuppliedAuditTokenFromPeerBundleIdentifier:suppliedTokenData:peerIsSocketDelegate:]
+ +[SOUtils shouldTrustSuppliedAuditTokenFromPeerBundleIdentifier:suppliedTokenData:peerIsSocketDelegate:].cold.1
CStrings:
+ "%{public}@ supplied an audit token without %{public}s, ignoring it"
+ "com.apple.private.network.socket-delegate"
```
