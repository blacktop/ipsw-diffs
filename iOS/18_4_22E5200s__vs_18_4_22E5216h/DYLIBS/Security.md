## Security

> `/System/Library/Frameworks/Security.framework/Security`

```diff

-61439.100.285.0.1
-  __TEXT.__text: 0x1712b8
+61439.100.301.0.0
+  __TEXT.__text: 0x172b68
   __TEXT.__auth_stubs: 0x3e50
   __TEXT.__objc_methlist: 0x5fd8
-  __TEXT.__const: 0xa410
+  __TEXT.__const: 0xa3e8
   __TEXT.__dlopen_cstrs: 0x359
-  __TEXT.__cstring: 0x17c7d
+  __TEXT.__cstring: 0x17d66
   __TEXT.__gcc_except_tab: 0x8bfc
-  __TEXT.__oslogstring: 0xef72
+  __TEXT.__oslogstring: 0xef8b
   __TEXT.__ustring: 0x406
   __TEXT.__dof_codesign: 0x1ffd
   __TEXT.__dof_security_: 0x325
-  __TEXT.__unwind_info: 0x5d60
+  __TEXT.__unwind_info: 0x5d80
   __TEXT.__objc_classname: 0xae3
   __TEXT.__objc_methname: 0xb894
   __TEXT.__objc_methtype: 0x354a
   __TEXT.__objc_stubs: 0x8920
   __DATA_CONST.__got: 0x718
-  __DATA_CONST.__const: 0x11d00
+  __DATA_CONST.__const: 0x11d68
   __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf8

   __AUTH_CONST.__auth_got: 0x1f40
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x4320
-  __AUTH_CONST.__cfstring: 0x15780
+  __AUTH_CONST.__cfstring: 0x158c0
   __AUTH_CONST.__objc_const: 0x98f8
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x138

   - /usr/lib/libcoretls_cfhelpers.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 6791
-  Symbols:   9502
-  CStrings:  8164
+  Functions: 6801
+  Symbols:   9520
+  CStrings:  8175
 
Symbols:
+ _SecCertificateCopyAnchorLookupKey
+ _SecPolicyCreate3PMobileAsset
+ _SecPolicyGetCompatibilityOidString
+ _SecPolicyUsesAppleAnchors
+ _SecPolicyUsesConstrainedAnchors
+ _SecTrustStoreCopyAnchors
+ _kSecPolicyApple3PMobileAsset
+ _kSecPolicyAppleEAPClient
+ _kSecPolicyAppleEAPServer
+ _kSecPolicyAppleIPSecClient
+ _kSecPolicyAppleIPSecServer
+ _kSecPolicyAppleSSLClient
+ _kSecPolicyAppleSSLServer
+ _kSecPolicyNameAppleIssuedTransparent
CStrings:
+ "1.2.840.113635.100.1.11.1"
+ "1.2.840.113635.100.1.11.2"
+ "1.2.840.113635.100.1.122"
+ "1.2.840.113635.100.1.3.1"
+ "1.2.840.113635.100.1.3.2"
+ "1.2.840.113635.100.1.9.1"
+ "1.2.840.113635.100.1.9.2"
+ "1.3.6.1.5.5.7.3.36"
+ "3PMobileAsset"
+ "AppleIssuedTransparent"
+ "SecTrustStoreCopyAnchors"

```
