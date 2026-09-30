## trustd

> `/usr/libexec/trustd`

```diff

-61439.100.285.0.1
-  __TEXT.__text: 0x5d9fc
-  __TEXT.__auth_stubs: 0x2360
-  __TEXT.__objc_stubs: 0x2c40
-  __TEXT.__objc_methlist: 0xbec
+61439.100.301.0.0
+  __TEXT.__text: 0x5ea9c
+  __TEXT.__auth_stubs: 0x23b0
+  __TEXT.__objc_stubs: 0x2d00
+  __TEXT.__objc_methlist: 0xbf4
   __TEXT.__const: 0x4771
   __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__gcc_except_tab: 0xcfc
-  __TEXT.__cstring: 0x66ba
-  __TEXT.__oslogstring: 0x57ce
+  __TEXT.__cstring: 0x66ff
+  __TEXT.__oslogstring: 0x5879
   __TEXT.__objc_classname: 0x194
-  __TEXT.__objc_methname: 0x2c03
+  __TEXT.__objc_methname: 0x2c72
   __TEXT.__objc_methtype: 0xae6
-  __TEXT.__unwind_info: 0x1030
-  __DATA_CONST.__auth_got: 0x11c0
-  __DATA_CONST.__got: 0x730
+  __TEXT.__unwind_info: 0x1058
+  __DATA_CONST.__auth_got: 0x11e8
+  __DATA_CONST.__got: 0x788
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x4900
-  __DATA_CONST.__cfstring: 0x5cc0
+  __DATA_CONST.__const: 0x4950
+  __DATA_CONST.__cfstring: 0x5d60
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x1450
-  __DATA.__objc_selrefs: 0xce8
+  __DATA.__objc_selrefs: 0xd10
   __DATA.__objc_ivar: 0xb4
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x3b0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1233
-  Symbols:   812
-  CStrings:  2141
+  Functions: 1241
+  Symbols:   828
+  CStrings:  2150
 
Symbols:
+ _OBJC_CLASS_$_NSFileManager
+ _SecCertificateCopyAnchorLookupKey
+ _SecCertificateCopyExtensionValue
+ _SecPolicyGetCompatibilityOidString
+ _SecPolicyUsesAppleAnchors
+ _SecPolicyUsesConstrainedAnchors
+ _kSecPolicyAppleEAP
+ _kSecPolicyAppleEAPClient
+ _kSecPolicyAppleEAPServer
+ _kSecPolicyAppleIPSecClient
+ _kSecPolicyAppleIPSecServer
+ _kSecPolicyAppleIPsec
+ _kSecPolicyAppleSSL
+ _kSecPolicyAppleSSLClient
+ _kSecPolicyAppleSSLServer
+ _kSecPolicyAppleX509Basic
CStrings:
+ "1.2.840.113635.100.1"
+ "2.5.29.30"
+ "ConstrainedTestAnchors.plist"
+ "Found ConstrainedTestAnchors.plist in incorrect format. Skipping."
+ "Found ConstrainedTestAnchors.plist key in incorrect format (%@). Skipping."
+ "Found ConstrainedTestAnchors.plist unparseable cert for %@. Skipping."
+ "Found ConstrainedTestAnchors.plist value in incorrect format for %@. Skipping."
+ "Found test anchor would replace a production anchor lookup key (%@). Skipping."
+ "anchorsForPolicyId:"
+ "arrayWithObject:"
+ "defaultManager"
+ "failed to load constrained test anchors"
+ "initWithBase64EncodedString:options:"
+ "isReadableFileAtPath:"
+ "platform"
- "Failed to allocate buffer for %lld values"
- "Failed to get CFArray type in values, skipping item"
- "Unable to allocate anchor array"
- "Unable to retrieve anchor lookup table"
- "Unable to retrieve current OTAPKIRef"
- "Unexpected system store count: %lld"

```
