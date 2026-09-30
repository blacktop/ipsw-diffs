## cloudphotod

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/Support/cloudphotod`

```diff

-720.1.111.0.0
-  __TEXT.__text: 0x1d0d94
-  __TEXT.__auth_stubs: 0x1a10
-  __TEXT.__objc_stubs: 0x1aea0
-  __TEXT.__objc_methlist: 0xc2d4
-  __TEXT.__const: 0x78e0
-  __TEXT.__cstring: 0x1a7f4
-  __TEXT.__objc_classname: 0x27c6
-  __TEXT.__objc_methname: 0x271d4
-  __TEXT.__objc_methtype: 0x82e5
-  __TEXT.__gcc_except_tab: 0x3148
+720.4.101.0.0
+  __TEXT.__text: 0x1d13ac
+  __TEXT.__auth_stubs: 0x1a20
+  __TEXT.__objc_stubs: 0x1af00
+  __TEXT.__objc_methlist: 0xc3d4
+  __TEXT.__cstring: 0x1a7b4
+  __TEXT.__objc_classname: 0x27ec
+  __TEXT.__objc_methname: 0x27610
+  __TEXT.__objc_methtype: 0x834b
+  __TEXT.__const: 0x78a0
+  __TEXT.__gcc_except_tab: 0x3134
   __TEXT.__oslogstring: 0x10292
   __TEXT.__swift5_typeref: 0x182f
   __TEXT.__swift5_reflstr: 0x1ef7

   __TEXT.__swift5_types: 0x158
   __TEXT.__swift5_capture: 0x348
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x6668
+  __TEXT.__unwind_info: 0x6680
   __TEXT.__eh_frame: 0x1700
-  __DATA_CONST.__auth_got: 0xd18
-  __DATA_CONST.__got: 0xc08
+  __DATA_CONST.__auth_got: 0xd20
+  __DATA_CONST.__got: 0xc10
   __DATA_CONST.__auth_ptr: 0x390
-  __DATA_CONST.__const: 0x9dd8
-  __DATA_CONST.__cfstring: 0x10ea0
-  __DATA_CONST.__objc_classlist: 0x688
+  __DATA_CONST.__const: 0x9e98
+  __DATA_CONST.__cfstring: 0x10e60
+  __DATA_CONST.__objc_classlist: 0x690
   __DATA_CONST.__objc_catlist: 0x180
   __DATA_CONST.__objc_protolist: 0x438
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x608
+  __DATA_CONST.__objc_superrefs: 0x610
   __DATA_CONST.__objc_intobj: 0x588
   __DATA_CONST.__objc_arraydata: 0xa38
   __DATA_CONST.__objc_arrayobj: 0x17a0
   __DATA_CONST.__objc_floatobj: 0x60
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x21e90
-  __DATA.__objc_selrefs: 0x8208
-  __DATA.__objc_ivar: 0x11cc
-  __DATA.__objc_data: 0x42f8
+  __DATA.__objc_const: 0x222a0
+  __DATA.__objc_selrefs: 0x8260
+  __DATA.__objc_ivar: 0x11f0
+  __DATA.__objc_data: 0x4348
   __DATA.__data: 0x6998
-  __DATA.__bss: 0xdd80
+  __DATA.__bss: 0xdd90
   __DATA.__common: 0x778
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9192
-  Symbols:   936
-  CStrings:  11291
+  Functions: 9216
+  Symbols:   938
+  CStrings:  11315
 
Symbols:
+ _OBJC_CLASS_$_CPLFingerprintContext
+ _realpath$DARWIN_EXTSN
CStrings:
+ "\x03\x11\x18\x13\x15\x18"
+ "\x04S"
+ "@\"<CPLCloudKitZoneManager>\""
+ "@\"CPLFingerprintContext\""
+ "@\"CPLFingerprintContext\"16@0:8"
+ "@40@0:8Q16@24@32"
+ "@48@0:8@16^B24@32@40"
+ "@56@0:8Q16@24@32^B40@48"
+ "@72@0:8@16@24@32@40@48@56@64"
+ "A\x13\x14"
+ "B52@0:8@16B24@28@36^@44"
+ "CPLCloudKitCreateSparsePrivateAssetTask"
+ "CPLDontAddBoundaryKeyToCKAssetReferences"
+ "Missing required shared scope"
+ "T@\"<CPLCloudKitZoneManager>\",&,N,V_zoneManager"
+ "T@\"CPLFingerprintContext\",&,V_fingerprintContext"
+ "T@\"CPLFingerprintContext\",R"
+ "T@\"CPLFingerprintContext\",R,N,V_fingerprintContext"
+ "T@\"CPLFingerprintContext\",R,V_fingerprintContext"
+ "T@\"CPLScopedIdentifier\",R,N,V_privateScopedIdentifier"
+ "T@\"CPLScopedIdentifier\",R,N,V_sharedScopedIdentifier"
+ "T@?,C,N,V_configureEngineBeforeOpeningBlock"
+ "_configureEngineBeforeOpeningBlock"
+ "_fingerprintContext"
+ "_privateScopedIdentifier"
+ "_sharedScopedIdentifier"
+ "_zoneManager"
+ "configureAssetTransferOptionsForCKAsset:fromReference:scopeProvider:"
+ "configureAssetTransferOptionsForCKAsset:scopeProvider:"
+ "configureEngineBeforeOpeningBlock"
+ "cplResourceWithType:scopedIdentifier:forRecord:isCoherent:scopeProvider:"
+ "cplResourcesWithScopedIdentifier:coherent:forRecord:scopeProvider:"
+ "fillCKRecord:scopeProvider:"
+ "fillCKRecordBuilder:scopeProvider:"
+ "fillCKRecordBuilderWithResourceChange:resourceCountAndSize:scopeProvider:error:"
+ "fillResourcesOfCKRecordBuilder:clearMissing:resourceCountAndSize:scopeProvider:error:"
+ "fillWithCKRecord:missingResourceProperties:scopeProvider:"
+ "fingerprintContext"
+ "fingerprintSchemeWithContext:"
+ "initWithController:scope:sharedScope:transportScopeMapping:privateScopedIdentifier:sharedScopedIdentifier:completionHandler:"
+ "initWithResourceType:defaultSourceBundleIdentifier:fingerprintContext:"
+ "initWithTask:scopedIdentifiers:destinationZoneIdentification:sharedZoneIdentification:targetMapping:propertyMapping:fingerprintContext:"
+ "isReference"
+ "prepareWithCKRecordBuilder:resourceCountAndSize:scopeProvider:error:"
+ "privateScopedIdentifier"
+ "setConfigureEngineBeforeOpeningBlock:"
+ "setFingerprintContext:"
+ "setSystemTask:"
+ "setZoneManager:"
+ "sharedContext"
+ "sharedScopedIdentifier"
+ "shouldUseEncryptedPropertiesIfPossibleWithContext:"
+ "supportsDeletionOfRecord:scopeProvider:"
+ "supportsDirectDeletionOfRecord:scopeProvider:"
+ "supportsDownloadOfChange:scopeProvider:"
+ "supportsUploadOfChange:scopeProvider:"
+ "v40@0:8@16^@24@32"
+ "zoneManager"
- "\x03\x11\x18\x13\x15\x16"
- "\x04R"
- "\v"
- "@32@0:8Q16@24"
- "@40@0:8@16^B24@32"
- "@48@0:8Q16@24@32^B40"
- "@64@0:8@16@24@32@40@48@56"
- "A\x13\x13"
- "B44@0:8@16B24@28^@36"
- "CloudKit operation has been cancelled because of an XPC activity bug"
- "CloudKit operation has been deferred by the system"
- "_attachedOperations"
- "_statusForConfiguration:"
- "activity"
- "configureAssetTransferOptionsForCKAsset:"
- "configureAssetTransferOptionsForCKAsset:fromReference:"
- "cplResourceWithType:scopedIdentifier:forRecord:isCoherent:"
- "cplResourcesWithScopedIdentifier:coherent:forRecord:"
- "fillCKRecord:"
- "fillCKRecordBuilder:"
- "fillCKRecordBuilderWithResourceChange:resourceCountAndSize:error:"
- "fillResourcesOfCKRecordBuilder:clearMissing:resourceCountAndSize:error:"
- "fillWithCKRecord:missingResourceProperties:"
- "fingerprintScheme"
- "hasXPCActivity"
- "initWithResourceType:defaultSourceBundleIdentifier:"
- "initWithTask:scopedIdentifiers:destinationZoneIdentification:sharedZoneIdentification:targetMapping:propertyMapping:"
- "prepareWithCKRecordBuilder:resourceCountAndSize:error:"
- "supportsDeletionOfRecord:"
- "supportsDirectDeletionOfRecord:"
- "supportsDownloadOfChange:"
- "supportsUploadOfChange:"
- "v32@0:8@16^@24"
- "xpc activity"

```
