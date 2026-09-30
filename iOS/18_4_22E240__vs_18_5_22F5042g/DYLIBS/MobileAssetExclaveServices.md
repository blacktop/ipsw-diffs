## MobileAssetExclaveServices

> `/System/Library/PrivateFrameworks/MobileAssetExclaveServices.framework/MobileAssetExclaveServices`

```diff

-1487.102.2.0.0
-  __TEXT.__text: 0x7ed4
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_methlist: 0x1e4
-  __TEXT.__const: 0x340
+1487.120.46.0.0
+  __TEXT.__text: 0x96e8
+  __TEXT.__auth_stubs: 0x900
+  __TEXT.__objc_methlist: 0x1f4
+  __TEXT.__const: 0x3b8
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__cstring: 0x58e
-  __TEXT.__oslogstring: 0x48e
-  __TEXT.__swift5_typeref: 0x153
-  __TEXT.__constg_swiftt: 0x1e0
-  __TEXT.__swift5_reflstr: 0x1b1
-  __TEXT.__swift5_fieldmd: 0x1bc
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_types: 0x18
+  __TEXT.__cstring: 0x73e
+  __TEXT.__oslogstring: 0x60e
+  __TEXT.__swift5_typeref: 0x166
+  __TEXT.__constg_swiftt: 0x224
+  __TEXT.__swift5_reflstr: 0x1c1
+  __TEXT.__swift5_fieldmd: 0x1e4
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_types: 0x20
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x1c
-  __TEXT.__unwind_info: 0x210
-  __TEXT.__eh_frame: 0x3d0
-  __TEXT.__objc_classname: 0x51
-  __TEXT.__objc_methname: 0x282
-  __TEXT.__objc_methtype: 0x1a1
+  __TEXT.__unwind_info: 0x238
+  __TEXT.__eh_frame: 0x470
+  __TEXT.__objc_classname: 0x7e
+  __TEXT.__objc_methname: 0x2c7
+  __TEXT.__objc_methtype: 0x1f5
   __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__got: 0xe0
+  __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x78
   __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x110
-  __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x478
-  __AUTH_CONST.__auth_ptr: 0x128
-  __AUTH_CONST.__const: 0xb0
-  __AUTH_CONST.__objc_const: 0x4b0
+  __DATA_CONST.__objc_protorefs: 0x18
+  __AUTH_CONST.__auth_got: 0x490
+  __AUTH_CONST.__auth_ptr: 0x130
+  __AUTH_CONST.__const: 0x150
+  __AUTH_CONST.__objc_const: 0x4c8
   __AUTH.__objc_data: 0x170
-  __AUTH.__data: 0x218
-  __DATA.__data: 0x1a0
+  __AUTH.__data: 0x210
+  __DATA.__data: 0x208
   __DATA.__bss: 0x390
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 120
-  Symbols:   115
-  CStrings:  123
+  Functions: 133
+  Symbols:   121
+  CStrings:  135
 
Symbols:
+ _objc_release_x28
+ _objc_retain_x24
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _objc_release_x24
- _objc_retain_x20
CStrings:
+ "%s Sending activateCommittedManifestForSelector request..."
+ "%s Sending checkManifestForSelector request..."
+ "%s Sending commitStagedManifestForSelectors request..."
+ "%s Sending invalidateManifestForSelector request..."
+ "%s Sending stageManifestForSelector request..."
+ "%s activateCommittedManifestForSelector request failed: %@"
+ "%s activateCommittedManifestForSelector request succeeded."
+ "%s checkManifestForSelector request failed: %@"
+ "%s checkManifestForSelector request succeeded."
+ "%s checkState=%s is invalid"
+ "%s commitStagedManifestForSelectors request failed: %@"
+ "%s commitStagedManifestForSelectors request succeeded."
+ "%s commitStagedManifestForSelectors:\nfsTags=%s\nspecifiers=%s"
+ "%s commitStagedManifestForSelectors: fsTags and specifiers have unequal count"
+ "%s invalidateManifestForSelector request failed: %@"
+ "%s invalidateManifestForSelector request succeeded."
+ "%s stageManifestForSelector request failed: %@"
+ "%s stageManifestForSelector request succeeded."
+ ": incorrect fixed-sized array length, expected 32, got "
+ "B36@0:8I16@\"NSString\"20^@28"
+ "B36@0:8I16@20^@28"
+ "B40@0:8@\"NSArray\"16@\"NSArray\"24^@32"
+ "B40@0:8@16@24^@32"
+ "B60@0:8I16@\"NSString\"20@\"NSData\"28@\"NSData\"36@\"NSData\"44^@52"
+ "B60@0:8I16@20@28@36@44^@52"
+ "B72@0:8I16@\"NSString\"20I28@\"NSData\"32@\"NSData\"40@\"NSData\"48^B56^@64"
+ "B72@0:8I16@20I28@32@40@48^B56^@64"
+ "Invalid key value while decoding result type for activateCommittedManifestForSelector"
+ "Invalid key value while decoding result type for checkManifestForSelector"
+ "Invalid key value while decoding result type for commitStagedManifestForSelectors"
+ "Invalid key value while decoding result type for invalidateManifestForSelector"
+ "Invalid key value while decoding result type for stageManifestForSelector"
+ "MAExclaveManifestStorageServiceBaseProtocol"
+ "MAExclaveManifestStorageServiceProtocol2"
+ "activateCommittedManifestForFSTag:specifier:error:"
+ "activateCommittedManifestForSelector threw an unexpected error type"
+ "checkManifestForFSTag:specifier:state:manifest:infoPlist:catalog:isValid:error:"
+ "checkManifestForSelector threw an unexpected error type"
+ "commitStagedManifestForFSTags:specifiers:error:"
+ "commitStagedManifestForSelectors threw an unexpected error type"
+ "invalid rawValue for SecureMobileAssetManifestState: "
+ "invalidateManifestForFSTag:specifier:error:"
+ "invalidateManifestForSelector threw an unexpected error type"
+ "stageManifestForFSTag:specifier:manifest:infoPlist:catalog:error:"
+ "stageManifestForSelector threw an unexpected error type"
- "%s Sending checkManifest request..."
- "%s Sending commitStagedManifestForFSTags request..."
- "%s Sending invalidateManifestForFSTag request..."
- "%s Sending storeManifest request..."
- "%s checkManifest request failed: %@"
- "%s checkManifest request succeeded."
- "%s commitStagedManifestForFSTags request failed: %@"
- "%s commitStagedManifestForFSTags request succeeded."
- "%s invalidateManifestForFSTag request failed: %@"
- "%s invalidateManifestForFSTag request succeeded."
- "%s storeManifest request failed: %@"
- "%s storeManifest request succeeded."
- "B28@0:8I16^@20"
- "B32@0:8@\"NSArray\"16^@24"
- "B32@0:8@16^@24"
- "B48@0:8@\"NSData\"16@\"NSData\"24@\"NSData\"32^@40"
- "B48@0:8@16@24@32^@40"
- "B64@0:8I16B20@\"NSData\"24@\"NSData\"32@\"NSData\"40^B48^@56"
- "B64@0:8I16B20@24@32@40^B48^@56"
- "Invalid key value while decoding result type for checkManifest"
- "Invalid key value while decoding result type for commitStagedManifestForFSTags"
- "Invalid key value while decoding result type for invalidateManifestForFSTag"
- "Invalid key value while decoding result type for storeManifest"
- "MAExclaveManifestStorageServiceProtocol"
- "checkManifest threw an unexpected error type"
- "checkManifestForFSTag:staged:manifest:infoPlist:catalog:isValid:error:"
- "commitStagedManifestForFSTags threw an unexpected error type"
- "commitStagedManifestForFSTags:error:"
- "invalidateManifestForFSTag threw an unexpected error type"
- "invalidateManifestForFSTag:error:"
- "stageManifest:infoPlist:catalog:error:"
- "storeManifest threw an unexpected error type"
- "storeManifest:infoPlist:catalog:error:"

```
