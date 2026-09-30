## trustd

> `/usr/libexec/trustd`

```diff

-61439.81.1.0.0
-  __TEXT.__text: 0x60f2c
-  __TEXT.__auth_stubs: 0x22e0
-  __TEXT.__objc_stubs: 0x2b60
-  __TEXT.__objc_methlist: 0x920
-  __TEXT.__const: 0x4658
-  __TEXT.__gcc_except_tab: 0xd14
-  __TEXT.__cstring: 0x62cc
-  __TEXT.__oslogstring: 0x588b
-  __TEXT.__objc_classname: 0x183
-  __TEXT.__objc_methname: 0x2adc
-  __TEXT.__objc_methtype: 0xab8
+61439.101.1.0.0
+  __TEXT.__text: 0x6375c
+  __TEXT.__auth_stubs: 0x2370
+  __TEXT.__objc_stubs: 0x2d80
+  __TEXT.__objc_methlist: 0xbf4
+  __TEXT.__const: 0x4668
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0x1050
-  __DATA_CONST.__auth_got: 0x1180
-  __DATA_CONST.__got: 0x6e0
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x5090
-  __DATA_CONST.__cfstring: 0x58e0
-  __DATA_CONST.__objc_classlist: 0x68
+  __TEXT.__gcc_except_tab: 0xd24
+  __TEXT.__cstring: 0x63b7
+  __TEXT.__oslogstring: 0x5993
+  __TEXT.__objc_classname: 0x194
+  __TEXT.__objc_methname: 0x2cf6
+  __TEXT.__objc_methtype: 0xae6
+  __TEXT.__unwind_info: 0x10a8
+  __DATA_CONST.__auth_got: 0x11c8
+  __DATA_CONST.__got: 0x758
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0x5168
+  __DATA_CONST.__cfstring: 0x5a80
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x50
-  __DATA_CONST.__objc_intobj: 0xf0
+  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_intobj: 0x120
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x16e0
-  __DATA.__objc_selrefs: 0xb98
-  __DATA.__objc_ivar: 0xa4
-  __DATA.__objc_data: 0x410
-  __DATA.__data: 0x3c4
-  __DATA.__bss: 0x4b8
+  __DATA.__objc_const: 0x1450
+  __DATA.__objc_selrefs: 0xd30
+  __DATA.__objc_ivar: 0xb4
+  __DATA.__objc_data: 0x460
+  __DATA.__data: 0x3dc
+  __DATA.__bss: 0x4e8
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 8EEBD231-F77E-359F-84C8-3F7E84CEB48E
-  Functions: 1293
-  Symbols:   791
-  CStrings:  2795
+  UUID: ECAD5DEC-E0A0-3FE5-91C6-6D68729C8325
+  Functions: 1322
+  Symbols:   817
+  CStrings:  2859
 
Symbols:
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
+ "stringByAppendingPathComponent:"
+ "stringByAppendingPathExtension:"
+ "type"
- "Failed to allocate buffer for %lld values"
- "Failed to get CFArray type in values, skipping item"
- "Unable to allocate anchor array"
- "Unable to retrieve anchor lookup table"
- "Unable to retrieve current OTAPKIRef"
- "Unexpected system store count: %lld"
- "invalid transaction type %d"

```
