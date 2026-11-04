## trustd

> `/usr/libexec/trustd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-62460.40.78.0.0
-  __TEXT.__text: 0x5b130
-  __TEXT.__auth_stubs: 0x2490
-  __TEXT.__objc_stubs: 0x3520
+62460.60.42.502.1
+  __TEXT.__text: 0x5ccf4
+  __TEXT.__auth_stubs: 0x24f0
+  __TEXT.__objc_stubs: 0x3680
   __TEXT.__objc_methlist: 0xe2c
-  __TEXT.__const: 0xde20
+  __TEXT.__const: 0xde30
   __TEXT.__dlopen_cstrs: 0x54
   __TEXT.__objc_classname: 0x1b4
-  __TEXT.__objc_methname: 0x312e
+  __TEXT.__objc_methname: 0x3201
   __TEXT.__objc_methtype: 0xc6b
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x17
   __TEXT.__swift5_reflstr: 0x4
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0xae0
-  __TEXT.__cstring: 0x6650
-  __TEXT.__oslogstring: 0x6120
-  __TEXT.__unwind_info: 0x13e8
-  __DATA_CONST.__const: 0x3f38
-  __DATA_CONST.__cfstring: 0x6740
+  __TEXT.__gcc_except_tab: 0xbb0
+  __TEXT.__cstring: 0x6901
+  __TEXT.__oslogstring: 0x619b
+  __TEXT.__unwind_info: 0x1420
+  __DATA_CONST.__const: 0x3fd0
+  __DATA_CONST.__cfstring: 0x6ca0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x78
-  __DATA_CONST.__objc_intobj: 0x138
-  __DATA_CONST.__objc_arraydata: 0x100
-  __DATA_CONST.__objc_arrayobj: 0x60
+  __DATA_CONST.__objc_intobj: 0x180
+  __DATA_CONST.__objc_arraydata: 0x110
+  __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_dictobj: 0x190
-  __DATA_CONST.__auth_got: 0x1258
-  __DATA_CONST.__got: 0x908
+  __DATA_CONST.__auth_got: 0x1288
+  __DATA_CONST.__got: 0x928
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x1780
-  __DATA.__objc_selrefs: 0xed0
+  __DATA.__objc_selrefs: 0xf28
   __DATA.__objc_ivar: 0xd4
   __DATA.__objc_data: 0x5b8
   __DATA.__data: 0x400

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 1214
-  Symbols:   897
-  CStrings:  2335
+  Functions: 1225
+  Symbols:   907
+  CStrings:  2392
 
Symbols:
+ _OBJC_CLASS_$_SecAnalyticsAllowlist
+ _OBJC_CLASS_$_SecAnalyticsAllowlistFile
+ _SecAnalyticsAllowlistCodeSignStatusIsPlatformBinary
+ _SecAnalyticsAllowlistCurrentPlatform
+ _SecAnalyticsAllowlistSystemDirectory
+ _SecKeyCopyAttributes
+ _SecKeyGetAlgorithmId
+ _SecKeyGetBlockSize
+ _kSecAttrKeySizeInBits
+ _kSecPolicyCheckQWACTLSBinding
CStrings:
+ "1.3.6.1.5.5.7.3.17"
+ "1.3.6.1.5.5.7.3.5"
+ "1.3.6.1.5.5.7.3.6"
+ "1.3.6.1.5.5.7.3.7"
+ "1.3.6.1.5.5.8.2.2"
+ "AnalyticsAllowlistAppsSource"
+ "AnalyticsAllowlistAppsVersion"
+ "AnalyticsAllowlistDomainsSource"
+ "AnalyticsAllowlistDomainsVersion"
+ "AnalyticsAllowlist_Apps.bin"
+ "AnalyticsAllowlist_Apps_%@.bin"
+ "AnalyticsAllowlist_Domains.bin"
+ "AnyEKU"
+ "CallerRequiredRevocation"
+ "DigestAlg"
+ "IPsecNoEndSystem"
+ "IPsecNoIKE"
+ "IPsecNoIKEIntermediate"
+ "IPsecNoTunnel"
+ "IPsecNoUser"
+ "KeyAlg"
+ "KeySize"
+ "OCSPDigestAlg"
+ "OCSPWeakFallback"
+ "Policies"
+ "PolicyName"
+ "QWACTLSBinding"
+ "RevocationRequired"
+ "S"
+ "SharedAssets"
+ "URLByAppendingPathExtension:"
+ "analytics allowlist %@ is not published: %@"
+ "cannot be opened"
+ "cannot set permissions"
+ "contentVersion"
+ "contentVersionForKind:"
+ "copy failed: %s"
+ "does not verify"
+ "fileAtURL:kind:platform:error:"
+ "iOS"
+ "it is not valid"
+ "lastPathComponent"
+ "localizedDescription"
+ "macOS"
+ "not in the asset"
+ "numberWithChar:"
+ "published analytics allowlist %@"
+ "removing published analytics allowlist %@: %@"
+ "rename failed: %s"
+ "sharedAllowlist"
+ "sourceForKind:"
+ "the OS copy is not older"
+ "tmp"
+ "tvOS"
+ "unsignedShortValue"
+ "verify:"
+ "visionOS"
+ "watchOS"
- "com.apple.trustd.valid.initialize"
```
