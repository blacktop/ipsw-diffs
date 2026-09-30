## trustd

> `/usr/libexec/trustd`

```diff

-61439.82.1.0.0
-  __TEXT.__text: 0x5c458
-  __TEXT.__auth_stubs: 0x2320
-  __TEXT.__objc_stubs: 0x2b00
-  __TEXT.__objc_methlist: 0x920
+61439.100.301.0.0
+  __TEXT.__text: 0x5ea9c
+  __TEXT.__auth_stubs: 0x23b0
+  __TEXT.__objc_stubs: 0x2d00
+  __TEXT.__objc_methlist: 0xbf4
   __TEXT.__const: 0x4771
-  __TEXT.__gcc_except_tab: 0xcec
-  __TEXT.__cstring: 0x6614
-  __TEXT.__oslogstring: 0x5771
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__objc_classname: 0x183
-  __TEXT.__objc_methname: 0x2a89
-  __TEXT.__objc_methtype: 0xab8
-  __TEXT.__unwind_info: 0x1000
-  __DATA_CONST.__auth_got: 0x11a0
-  __DATA_CONST.__got: 0x708
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x4890
-  __DATA_CONST.__cfstring: 0x5bc0
-  __DATA_CONST.__objc_classlist: 0x68
+  __TEXT.__gcc_except_tab: 0xcfc
+  __TEXT.__cstring: 0x66ff
+  __TEXT.__oslogstring: 0x5879
+  __TEXT.__objc_classname: 0x194
+  __TEXT.__objc_methname: 0x2c72
+  __TEXT.__objc_methtype: 0xae6
+  __TEXT.__unwind_info: 0x1058
+  __DATA_CONST.__auth_got: 0x11e8
+  __DATA_CONST.__got: 0x788
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0x4950
+  __DATA_CONST.__cfstring: 0x5d60
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x50
-  __DATA_CONST.__objc_intobj: 0xd8
+  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x16e0
-  __DATA.__objc_selrefs: 0xb80
-  __DATA.__objc_ivar: 0xa4
-  __DATA.__objc_data: 0x410
-  __DATA.__data: 0x398
-  __DATA.__bss: 0x498
+  __DATA.__objc_const: 0x1450
+  __DATA.__objc_selrefs: 0xd10
+  __DATA.__objc_ivar: 0xb4
+  __DATA.__objc_data: 0x460
+  __DATA.__data: 0x3b0
+  __DATA.__bss: 0x4c8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1213
-  Symbols:   801
-  CStrings:  2099
+  Functions: 1241
+  Symbols:   828
+  CStrings:  2150
 
Symbols:
+ _OBJC_CLASS_$_NSFileManager
+ _SecCertificateCopyAnchorLookupKey
+ _SecCertificateCopyExtensionValue
+ _SecCertificateCopyQualifiedCertificateStatements
+ _SecCertificateIsSelfSignedCA
+ _SecFrameworkCopyLocalizedString
+ _SecPolicyGetCompatibilityOidString
+ _SecPolicyUsesAppleAnchors
+ _SecPolicyUsesConstrainedAnchors
+ _ccsha1_di
+ _kSecPolicyAppleEAP
+ _kSecPolicyAppleEAPClient
+ _kSecPolicyAppleEAPServer
+ _kSecPolicyAppleIPSecClient
+ _kSecPolicyAppleIPSecServer
+ _kSecPolicyAppleIPsec
+ _kSecPolicyAppleQWAC
+ _kSecPolicyAppleSSL
+ _kSecPolicyAppleSSLClient
+ _kSecPolicyAppleSSLServer
+ _kSecPolicyAppleX509Basic
+ _kSecPolicyCheckQWAC
+ _kSecQCStatementCompliance
+ _kSecQCStatementType
+ _kSecQCStatementTypeWeb
+ _kSecTrustInfoQCStatementsKey
+ _kSecTrustInfoQWACValidationKey
CStrings:
+ "\x13"
+ "%s is %s (via feature flags)"
+ "1.2.840.113635.100.1"
+ "2.5.29.30"
+ "@\"NSDictionary\""
+ "Anchors"
+ "Anchors.plist is wrong type."
+ "B32@?0@\"NSString\"8Q16^B24"
+ "Certificate"
+ "ConstrainedTestAnchors.plist"
+ "Found ConstrainedTestAnchors.plist in incorrect format. Skipping."
+ "Found ConstrainedTestAnchors.plist key in incorrect format (%@). Skipping."
+ "Found ConstrainedTestAnchors.plist unparseable cert for %@. Skipping."
+ "Found ConstrainedTestAnchors.plist value in incorrect format for %@. Skipping."
+ "Found test anchor would replace a production anchor lookup key (%@). Skipping."
+ "QWACValidation"
+ "RootConstraints"
+ "SecAnchorCache"
+ "SecAnchorCache failed to copy anchor table"
+ "Security"
+ "T@\"NSDictionary\",&,V_anchor_table"
+ "T@\"NSMutableArray\",&,V_cache_list"
+ "T@\"NSMutableDictionary\",&,V_cache"
+ "T{os_unfair_lock_s=I},V_cache_lock"
+ "Using built-in constrained anchors"
+ "Web Authentication"
+ "^{__SecCertificate=}24@0:8@16"
+ "_anchor_table"
+ "_cache"
+ "_cache_list"
+ "_cache_lock"
+ "anchor_table"
+ "anchorsForKey:"
+ "anchorsForPolicyId:"
+ "arrayWithObject:"
+ "cache"
+ "cache_list"
+ "cache_lock"
+ "cer"
+ "copyAnchorAssetForKey:"
+ "defaultManager"
+ "disabled"
+ "enabled"
+ "failed to load constrained test anchors"
+ "indexOfObjectPassingTest:"
+ "initWithBase64EncodedString:options:"
+ "isReadableFileAtPath:"
+ "oids"
+ "platform"
+ "preheatCache"
+ "removeObjectAtIndex:"
+ "setAnchor_table:"
+ "setCache:"
+ "setCache_list:"
+ "setCache_lock:"
+ "sha2"
+ "spki-sha2"
+ "type"
- "Failed to allocate buffer for %lld values"
- "Failed to get CFArray type in values, skipping item"
- "Unable to allocate anchor array"
- "Unable to retrieve anchor lookup table"
- "Unable to retrieve current OTAPKIRef"
- "Unexpected system store count: %lld"
- "invalid transaction type %d"

```
