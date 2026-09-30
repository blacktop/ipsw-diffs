## fpassetmanagerd

> `/usr/libexec/fpassetmanagerd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`

```diff

-1.5.0.0.0
-  __TEXT.__text: 0x2052c
-  __TEXT.__auth_stubs: 0xd30
+2.0.0.0.0
+  __TEXT.__text: 0x26d9c
+  __TEXT.__auth_stubs: 0xd90
   __TEXT.__objc_stubs: 0x460
-  __TEXT.__objc_methlist: 0x1b4
-  __TEXT.__const: 0x668
-  __TEXT.__cstring: 0xb3f
+  __TEXT.__objc_methlist: 0x1f8
+  __TEXT.__const: 0x7c8
+  __TEXT.__cstring: 0xdff
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__oslogstring: 0x1978
-  __TEXT.__objc_methtype: 0x1e4
-  __TEXT.__swift5_typeref: 0x35a
-  __TEXT.__swift5_capture: 0x204
+  __TEXT.__swift5_typeref: 0x3e6
+  __TEXT.__oslogstring: 0x1a78
+  __TEXT.__swift5_capture: 0x288
+  __TEXT.__objc_methtype: 0x274
   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x30
   __TEXT.__swift_as_cont: 0x34
-  __TEXT.__constg_swiftt: 0x220
-  __TEXT.__swift5_reflstr: 0x174
-  __TEXT.__swift5_fieldmd: 0x224
-  __TEXT.__swift5_proto: 0x24
-  __TEXT.__swift5_types: 0x24
+  __TEXT.__constg_swiftt: 0x298
+  __TEXT.__swift5_reflstr: 0x2b4
+  __TEXT.__swift5_fieldmd: 0x304
+  __TEXT.__swift5_proto: 0x3c
+  __TEXT.__swift5_types: 0x30
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__swift5_builtin: 0x14
   __TEXT.__objc_classname: 0xde
-  __TEXT.__objc_methname: 0x5f8
-  __TEXT.__unwind_info: 0x4c0
-  __TEXT.__eh_frame: 0xb74
-  __DATA_CONST.__const: 0x920
+  __TEXT.__objc_methname: 0x648
+  __TEXT.__unwind_info: 0x528
+  __TEXT.__eh_frame: 0xb94
+  __DATA_CONST.__const: 0xa78
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0x6a0
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__auth_ptr: 0x188
-  __DATA.__objc_const: 0x3b0
-  __DATA.__objc_selrefs: 0x1e8
-  __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x570
-  __DATA.__common: 0x80
-  __DATA.__bss: 0x480
+  __DATA_CONST.__auth_got: 0x6d0
+  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__auth_ptr: 0x1b8
+  __DATA.__objc_const: 0x3c8
+  __DATA.__objc_selrefs: 0x200
+  __DATA.__objc_data: 0x1f8
+  __DATA.__data: 0x660
+  __DATA.__common: 0x68
+  __DATA.__bss: 0x780
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/Versions/A/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 342
-  Symbols:   335
-  CStrings:  297
+  Functions: 384
+  Symbols:   350
+  CStrings:  316
 
Symbols:
+ _$s8RawValueSYTl
+ _$sBi64_WV
+ _$sSY8rawValue03RawB0QzvgTq
+ _$sSY8rawValuexSg03RawB0Qz_tcfCTq
+ _$sSYMp
+ _$sSdN
+ _$sShMa
+ _$ss10_HashTableV12previousHole6beforeAB6BucketVAF_tF
+ _$ss11_SetStorageC8allocate8capacityAByxGSi_tFZ
+ _$ss11_SetStorageCMn
+ _$ss32_diagnoseUnexpectedEnumCaseValue4type03rawE0s5NeverOxm_q_tr0_lF
+ _$ss5NeverOMn
+ _$ss6HasherV5_hash4seed5bytes5countS2i_s6UInt64VSitFZ
+ _$ss6HasherV8_combineyys6UInt32VF
+ _$ss6UInt32VSHsWP
CStrings:
+ " not supported in this bundle"
+ "/private/var/db/fpsd/dvp/fpassetmanager/fps/cert_info/"
+ "/private/var/db/fpsd/dvp/fpassetmanager/fps/cert_info/bundle_metadata.plist"
+ "/private/var/db/fpsd/dvp/fpassetmanager/fps/cert_info/current_bundle.dat"
+ "/private/var/db/fpsd/dvp/fpassetmanager/fps/cert_info/staging_bundle.dat"
+ "/private/var/db/fpsd/dvp/fpassetmanager/fps/cert_info/staging_metadata.plist"
+ "Asset %s in index but type mismatch or read failed"
+ "Asset %s... type mismatch: requested 0x%s, found 0x%s"
+ "Asset request: bundle=%ld, type=0x%s, id=%s..."
+ "Asset type 0x%s not supported in bundle %ld"
+ "Background tasks registered for %ld bundles"
+ "Boot refresh cancelled due to expiration for %s"
+ "Boot refresh failed for %s: %s"
+ "Built index for %s: %ld assets"
+ "Checking remote ETag at %s"
+ "Daemon initialized with %ld bundle indexes (%ld total assets, ~%ld bytes)"
+ "Failed to build index for %s: %s"
+ "Force refresh requested for bundle %ld"
+ "Indexed %s - ID: %s..., Offset: %ld, Size: %ld bytes"
+ "Loaded bundle: %ld bytes from %s"
+ "Metadata inconsistency detected for bundle %s"
+ "No bundle available yet for %s"
+ "No bundle file exists at %s - nothing to validate"
+ "No bundle installed for %s, attempting initial download"
+ "On-boot check triggered for %s"
+ "Periodic refresh cancelled due to expiration for %s"
+ "Periodic refresh failed for %s: %s"
+ "Periodic refresh triggered for %s"
+ "Periodic task expired by system for %s, cancelling async work"
+ "Rebuilt index for %s: %ld assets"
+ "Signature verification failed before asset read - possible tampering!"
+ "Signature verification failed for on-disk bundle!"
+ "Starting asset bundle refresh for %s (trigger: %s)"
+ "Using internal asset URLs"
+ "Using production asset URLs"
+ "Using production asset URLs (non-internal OS)"
+ "Version request for bundle %ld"
+ "bundleIndexes"
+ "com.apple.fpassetmanagerd.retrievecertinfoonboot"
+ "com.apple.fpassetmanagerd.retrievecertinfoperiodic"
+ "fetchAssetFromBundle:assetType:assetID:reply:"
+ "forceRefreshForBundle:reply:"
+ "getCurrentBundleVersionForBundle:reply:"
+ "https://silverbullet-external.itunes.apple.com/content/fp-assets/fps/cert_info"
+ "https://silverbullet-itms7.itunes.apple.com/content/fp-assets/fps/cert_info"
+ "v32@0:8q16@?24"
+ "v32@0:8q16@?<v@?@\"NSError\">24"
+ "v32@0:8q16@?<v@?I>24"
+ "v44@0:8q16I24@\"NSData\"28@?<v@?@\"NSData\"@\"NSError\">36"
+ "v44@0:8q16I24@28@?36"
- "Asset %s in index but failed to read"
- "Asset request: %s..."
- "Background tasks registered"
- "Boot refresh cancelled due to expiration"
- "Boot refresh failed: %s"
- "Built index for %ld assets"
- "Daemon initialized with asset index (%ld assets, ~%ld bytes)"
- "Daemon started with no asset bundle available"
- "Failed to build index: %s"
- "Force refresh requested"
- "Indexed CA blob - ID: %s..., Offset: %ld, Size: %ld bytes"
- "Loaded bundle: %ld bytes"
- "Metadata inconsistency detected"
- "No bundle available yet"
- "No bundle file exists - nothing to validate"
- "No bundle installed, attempting initial download for asset request"
- "On-boot asset check triggered"
- "Periodic asset refresh triggered"
- "Periodic refresh cancelled due to expiration"
- "Periodic refresh failed: %s"
- "Periodic task expired by system, cancelling async work"
- "Rebuilt index for %ld assets"
- "Starting asset bundle refresh (trigger: %s)"
- "Storage directory does not exist: %s"
- "Using internal asset URL: %s"
- "Using production asset URL (non-internal OS)"
- "Using production asset URL: %s"
- "Version request"
- "assetIndex"
- "❌ Signature verification failed before asset read - possible tampering!"
- "❌ Signature verification failed for on-disk bundle!"
```
