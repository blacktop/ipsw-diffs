## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation`

```diff

-760.2.1.0.0
-  __TEXT.__text: 0x56b14
+767.3.3.0.0
+  __TEXT.__text: 0x56f28
   __TEXT.__auth_stubs: 0x1380
-  __TEXT.__objc_methlist: 0x68a8
+  __TEXT.__objc_methlist: 0x68f8
   __TEXT.__const: 0x140
   __TEXT.__gcc_except_tab: 0x1470
-  __TEXT.__oslogstring: 0x4133
-  __TEXT.__cstring: 0x2d5b
+  __TEXT.__oslogstring: 0x4186
+  __TEXT.__cstring: 0x2d97
   __TEXT.__dlopen_cstrs: 0xf8
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x1dd4
+  __TEXT.__unwind_info: 0x1de0
   __TEXT.__objc_classname: 0x1054
-  __TEXT.__objc_methname: 0xb9ce
+  __TEXT.__objc_methname: 0xba7c
   __TEXT.__objc_methtype: 0x259a
-  __TEXT.__objc_stubs: 0x8520
+  __TEXT.__objc_stubs: 0x85a0
   __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0x13b0
+  __DATA_CONST.__const: 0x13b8
   __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xaae0
-  __DATA_CONST.__objc_selrefs: 0x2c08
-  __AUTH_CONST.__const: 0xa38
-  __AUTH_CONST.__cfstring: 0x4b60
+  __DATA_CONST.__objc_const: 0xab48
+  __DATA_CONST.__objc_selrefs: 0x2c38
+  __AUTH_CONST.__const: 0xa78
+  __AUTH_CONST.__cfstring: 0x4bc0
   __AUTH_CONST.__objc_const: 0x3f88
   __AUTH_CONST.__auth_got: 0x9d0
   __AUTH.__objc_data: 0x1040

   __DATA.__objc_classrefs: 0x560
   __DATA.__objc_superrefs: 0x378
   __DATA.__objc_ivar: 0x19c
-  __DATA.__data: 0x1f50
+  __DATA.__data: 0x1fb0
   __DATA.__thread_vars: 0x18
   __DATA.__thread_bss: 0x8
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_ivar: 0x580
   __DATA_DIRTY.__objc_data: 0x19a0
-  __DATA_DIRTY.__bss: 0x4b8
+  __DATA_DIRTY.__bss: 0x4d8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 95D042D7-8CBF-3C49-9886-26DD61177FEF
-  Functions: 2436
-  Symbols:   8484
-  CStrings:  4421
+  UUID: 1781F215-31D4-3D0A-B50A-A399DCE3C812
+  Functions: 2445
+  Symbols:   8514
+  CStrings:  4435
 
Symbols:
+ +[HMFSoftwareVersion isValidVersionString:]
+ +[HMFSoftwareVersion logCategory]
+ +[HMFSoftwareVersion versionRegex]
+ +[HMFVersion logCategory]
+ +[NSUUID(Version5) hmf_UUIDWithNamespace:data:salts:]
+ -[HMFMessage untrustedClientIdentifier]
+ -[HMFMutableMessage setUntrustedClientIdentifier:]
+ _HMFMessageUntrustedClientIdentifierHeader
+ _HMFProductInfoDawnCOSVersion
+ _HMFProductInfoLighthouseCOSVersion
+ _HMFProductInfoStarlightCOSVersion
+ _HMFProductInfoSunburstCOSVersion
+ ___25+[HMFVersion logCategory]_block_invoke
+ ___33+[HMFSoftwareVersion logCategory]_block_invoke
+ ___block_literal_global.129
+ _objc_msgSend$hmf_UUIDWithNamespace:data:salts:
+ _objc_msgSend$lengthOfBytesUsingEncoding:
+ _objc_msgSend$setHeaderValue:forKey:
+ _objc_msgSend$versionRegex
CStrings:
+ "%{public}@HMFSoftwareVersion: Failed to create version string regex with error: %@"
+ "HMF.untrustedClientIdentifier"
+ "T@\"NSString\",&,D,N"
+ "hmf_UUIDWithNamespace:data:salts:"
+ "isValidVersionString:"
+ "lengthOfBytesUsingEncoding:"
+ "setUntrustedClientIdentifier:"
+ "untrustedClientIdentifier"
+ "versionRegex"

```
