## libamsupport.dylib

> `/usr/lib/libamsupport.dylib`

```diff

-432.0.0.0.1
-  __TEXT.__text: 0x12920
-  __TEXT.__auth_stubs: 0xca0
+434.0.4.0.0
+  __TEXT.__text: 0x13508
+  __TEXT.__auth_stubs: 0xd50
   __TEXT.__objc_methlist: 0x36c
-  __TEXT.__const: 0x7268
-  __TEXT.__cstring: 0x2a13
+  __TEXT.__const: 0x88d8
+  __TEXT.__cstring: 0x2b6c
   __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__unwind_info: 0x4e8
+  __TEXT.__unwind_info: 0x510
   __TEXT.__objc_classname: 0x89
   __TEXT.__objc_methname: 0xa7d
   __TEXT.__objc_methtype: 0x4c0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x360
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x660
-  __AUTH_CONST.__const: 0x690
+  __AUTH_CONST.__auth_got: 0x6b8
+  __AUTH_CONST.__const: 0x7a8
   __AUTH_CONST.__cfstring: 0xf80
   __AUTH_CONST.__objc_const: 0x588
   __DATA.__objc_ivar: 0x2c

   - /usr/lib/libReverseProxyDevice.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B52E0B17-26A9-3A38-B0DE-2D95CCD4F3C3
-  Functions: 497
-  Symbols:   1487
-  CStrings:  736
+  UUID: FD46DC86-CA1B-39C9-97A4-67D1C5CC0F3B
+  Functions: 512
+  Symbols:   1536
+  CStrings:  743
 
Symbols:
+ _AMSupportCreatePathForPeerExecutable
+ _CFArrayAppendValue
+ _CFArrayCreateMutable
+ _CFURLCreateCopyDeletingLastPathComponent
+ _CFURLCreateFilePathURL
+ _CFURLGetByteRangeForComponent
+ _Img4DecodeHybridScheme3Sha384IM4C
+ _Img4DecodeHybridScheme3Sha384IM4CNoPQC
+ _Img4DecodeLocalHybridScheme3Sha384IM4C
+ _Img4DecodeLocalHybridScheme3Sha384IM4CNoPQC
+ _Img4DecodeLocalMLDSA87Sha384IM4C
+ _LocalHybridScheme3Sha384IM4C
+ _LocalHybridScheme3Sha384IM4C_len
+ _LocalMLDSA87Sha384IM4C
+ _LocalMLDSA87Sha384IM4C_len
+ __AMSupportPlatformTempDirCString
+ __NSGetExecutablePath
+ _ccmldsa87
+ _ccmldsa_import_pubkey
+ _ccmldsa_verify
+ _ccrsa_pub_init
+ _confstr
+ _dladdr
+ _hybrid_scheme3_pubkey_cast
+ _hybrid_scheme3_signature_cast
+ _kImg4DecodeHybridScheme3Sha384IM4C
+ _kImg4DecodeHybridScheme3Sha384IM4CNoPQC
+ _kImg4DecodeLocalHybridScheme3Sha384IM4C
+ _kImg4DecodeLocalHybridScheme3Sha384IM4CNoPQC
+ _kImg4DecodeLocalMLDSA87Sha384IM4C
+ _verify_signature_hybrid_scheme3
+ _verify_signature_hybrid_scheme3_no_pqc
+ _verify_signature_ml_dsa_87
+ _verify_signature_rsa4096_fixed
CStrings:
+ "%@/%@"
+ "%s/%s"
+ "(No copy of executable located at %@)"
+ "AMSupportCreatePathForPeerExecutable"
+ "Found executable at %@"
+ "NULL parameter passed to _create_peer_executable_for_ancestors()"
+ "Searched for %@ relative to %@ and its ancestors, found %@"
+ "_NSGetExecutablePath failed to get path of current executable"
+ "_create_peer_executable_for_ancestors"
+ "dladdr failed to get info about running framework"
+ "failed to create %s: %s"
- "/tmp"
- "/tmp/%s"
- "failed to create tmp dir: %s"
- "tmp dir template: %s"

```
