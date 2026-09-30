## CloudAttestation

> `/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation`

```diff

-171.0.0.0.0
-  __TEXT.__text: 0xfd974
-  __TEXT.__auth_stubs: 0x2150
+178.0.0.0.0
+  __TEXT.__text: 0x106164
+  __TEXT.__auth_stubs: 0x21d0
   __TEXT.__objc_methlist: 0x2c
-  __TEXT.__const: 0x8b20
-  __TEXT.__cstring: 0x255f
-  __TEXT.__constg_swiftt: 0x223c
-  __TEXT.__swift5_typeref: 0x1e17
-  __TEXT.__swift5_reflstr: 0x21b2
-  __TEXT.__swift5_fieldmd: 0x29f4
-  __TEXT.__swift5_assocty: 0x390
-  __TEXT.__swift5_proto: 0x840
-  __TEXT.__swift5_types: 0x334
+  __TEXT.__const: 0x96b0
+  __TEXT.__cstring: 0x26ef
+  __TEXT.__constg_swiftt: 0x231c
+  __TEXT.__swift5_typeref: 0x1fa5
+  __TEXT.__swift5_reflstr: 0x22f2
+  __TEXT.__swift5_fieldmd: 0x2c2c
+  __TEXT.__swift5_assocty: 0x480
+  __TEXT.__swift5_proto: 0x8f0
+  __TEXT.__swift5_types: 0x350
   __TEXT.__swift5_capture: 0xe0
   __TEXT.__oslogstring: 0x1cdb
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_mpenum: 0x94
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__unwind_info: 0x3908
-  __TEXT.__eh_frame: 0x64d8
+  __TEXT.__unwind_info: 0x3b70
+  __TEXT.__eh_frame: 0x6540
   __TEXT.__objc_classname: 0x1e
-  __TEXT.__objc_methname: 0x36a
+  __TEXT.__objc_methname: 0x388
   __TEXT.__objc_methtype: 0x16c
-  __DATA_CONST.__got: 0x590
+  __DATA_CONST.__got: 0x5b8
   __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa0
+  __DATA_CONST.__objc_selrefs: 0xa8
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x10a8
-  __AUTH_CONST.__auth_ptr: 0x960
-  __AUTH_CONST.__const: 0x4d00
+  __AUTH_CONST.__auth_got: 0x10e8
+  __AUTH_CONST.__auth_ptr: 0x9c8
+  __AUTH_CONST.__const: 0x4fe8
   __AUTH_CONST.__objc_const: 0x738
   __AUTH.__objc_data: 0x1b0
-  __AUTH.__data: 0x25b8
-  __DATA.__data: 0x27a0
-  __DATA.__common: 0x758
-  __DATA.__bss: 0xf500
-  __DATA_DIRTY.__data: 0xf8
+  __AUTH.__data: 0x2770
+  __DATA.__data: 0x2998
+  __DATA.__common: 0x820
+  __DATA.__bss: 0x10b00
+  __DATA_DIRTY.__data: 0x100
   __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4494
-  Symbols:   271
-  CStrings:  460
+  Functions: 4713
+  Symbols:   273
+  CStrings:  488
 
Symbols:
+ _SecPolicyCreateDCAttestation
+ _NSUnderlyingErrorKey
+ _SecPolicyCreateRevocation
- _SecPolicyCreateBasicX509
CStrings:
+ "digestAlg"
+ "ASSET_TYPE_PCS"
+ "ASSET_TYPE_OS"
+ "DIGEST_ALG_SHA256"
+ "com.apple.CloudAttestation.TransparencyLogError"
+ "PRODUCTION"
+ "ASSET_TYPE_MODEL"
+ "QA1_INTERNAL"
+ "com.apple.CloudAttestation.AttestationProtocolError"
+ "QA"
+ "STAGING"
+ "initWithDomain:code:userInfo:"
+ "variant"
+ "serverEventInfo"
+ "DIGEST_ALG_SHA384"
+ "QA2_PRIMARY"
+ "insertData"
+ "permittedEnvironments"
+ "timestamp"
+ "PrivateCloudCompute.ReleaseMetadata"
+ "ASSET_TYPE_DEBUG_SHELL"
+ "SCHEMA_VERSION_V1"
+ "com.apple.CloudAttestation.CloudAttestationError"
+ "DIGEST_ALG_UNSPECIFIED"
+ "UNSPECIFIED"
+ "DEV"
+ "SCHEMA_VERSION_UNSPECIFIED"
+ "url"
+ "assets"
+ "releaseHash"
+ "ASSET_TYPE_HOST_TOOLS"
+ "value"
+ "QA2_INTERNAL"
+ "QA1_PRIMARY"
+ "CARRY"
+ "schemaVersion"
+ "darwin_init"
+ "ASSET_TYPE_UNSPECIFIED"
+ "EPHEMERAL"
+ "PERF"
+ "ticket"
- "ENVIRONMENT_UNSPECIFIED"
- "ENVIRONMENT_STAGING"
- "ENVIRONMENT_DEV"
- "ENVIRONMENT_QA2PRIMARY"
- "ENVIRONMENT_CARRY"
- "ENVIRONMENT_EPHEMERAL"
- "permitted_environments"
- "PrivateCloudCompute.TransparencyLogEntry"
- "ENVIRONMENT_PRODUCTION"
- "cloudAttestationTraceDirectory"
- "ENVIRONMENT_QA"
- "ENVIRONMENT_PERF"
- "ENVIRONMENT_QA2INTERNAL"

```
