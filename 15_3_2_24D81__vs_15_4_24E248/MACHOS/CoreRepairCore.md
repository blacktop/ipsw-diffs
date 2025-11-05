## CoreRepairCore

> `/System/Library/Templates/Data/Library/Frameworks/CoreRepairCore.framework/Versions/A/CoreRepairCore`

```diff

-645.80.16.0.0
-  __TEXT.__text: 0x36ca4
-  __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_stubs: 0x2f60
-  __TEXT.__objc_methlist: 0x18a0
+696.100.57.0.0
+  __TEXT.__text: 0x39668
+  __TEXT.__auth_stubs: 0xd10
+  __TEXT.__objc_stubs: 0x30a0
+  __TEXT.__objc_methlist: 0x1a3c
   __TEXT.__const: 0x458
-  __TEXT.__oslogstring: 0x4eb8
-  __TEXT.__cstring: 0x2133
-  __TEXT.__objc_methname: 0x48ea
-  __TEXT.__objc_classname: 0x29f
-  __TEXT.__objc_methtype: 0xc0f
-  __TEXT.__gcc_except_tab: 0x528
-  __TEXT.__unwind_info: 0x618
-  __DATA_CONST.__auth_got: 0x650
-  __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x468
-  __DATA_CONST.__cfstring: 0x2e60
-  __DATA_CONST.__objc_classlist: 0xe8
+  __TEXT.__oslogstring: 0x50f6
+  __TEXT.__cstring: 0x2264
+  __TEXT.__objc_methname: 0x49c1
+  __TEXT.__objc_classname: 0x2c9
+  __TEXT.__objc_methtype: 0xc35
+  __TEXT.__gcc_except_tab: 0x6b4
+  __TEXT.__unwind_info: 0x720
+  __DATA_CONST.__auth_got: 0x698
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__const: 0x498
+  __DATA_CONST.__cfstring: 0x2fe0
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x80
-  __DATA_CONST.__objc_arraydata: 0x340
-  __DATA_CONST.__objc_arrayobj: 0x258
+  __DATA_CONST.__objc_superrefs: 0x88
+  __DATA_CONST.__objc_arraydata: 0x3c8
+  __DATA_CONST.__objc_arrayobj: 0x2d0
   __DATA_CONST.__objc_intobj: 0x90
-  __DATA.__objc_const: 0x2748
-  __DATA.__objc_selrefs: 0x10f0
+  __DATA_CONST.__objc_dictobj: 0xa0
+  __DATA.__objc_const: 0x2608
+  __DATA.__objc_selrefs: 0x11a8
   __DATA.__objc_ivar: 0x1a4
-  __DATA.__objc_data: 0x910
+  __DATA.__objc_data: 0x9b0
   __DATA.__data: 0x150
   __DATA.__common: 0x8
   __DATA.__bss: 0xa8

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/ServiceManagement.framework/Versions/A/ServiceManagement
   - /System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/Versions/A/AppleDeviceQuerySupport
+  - /System/Library/PrivateFrameworks/CoreAccessories.framework/Versions/A/CoreAccessories
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/Versions/A/DeviceIdentity
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/Versions/A/MSUDataAccessor
   - /usr/lib/libFDR.dylib

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 03991495-0724-37B7-9EBC-69C101D16727
-  Functions: 977
-  Symbols:   302
-  CStrings:  2302
+  UUID: 146C0590-02CA-301D-880F-30401606D700
+  Functions: 1039
+  Symbols:   315
+  CStrings:  2358
 
Symbols:
+ _AMFDRRegisterModuleChallengeCallback
+ _CFDataCreateWithBytesNoCopy
+ _DEREncoderAddData
+ _DEREncoderAddSequenceFromEncoder
+ _DEREncoderCreate
+ _DEREncoderCreateEncodedBuffer
+ _DEREncoderDestroy
+ _OBJC_CLASS_$_ACCHWComponentAuth
+ _OBJC_CLASS_$_CRComponentSigning
+ _OBJC_CLASS_$_NSConstantDictionary
+ __set_user_dir_suffix
+ _ccrng
+ _kCFAllocatorMalloc
CStrings:
+ "%s failed"
+ "%s failed to create DER file"
+ "*outDerData is NULL"
+ "*outDerDataLength is 0"
+ "*outDeviceNonce is NULL"
+ "*outSignature is NULL"
+ "@\"NSData\"24@?0@\"NSDictionary\"8^@16"
+ "@\"NSDictionary\"24@?0@\"NSData\"8^@16"
+ "@\"NSDictionary\"24@?0@\"NSMutableDictionary\"8^@16"
+ "@\"NSDictionary\"24@?0@\"NSString\"8^@16"
+ "@24@?0@\"NSDictionary\"8^@16"
+ "AMFDRDataCreatePermissionString failed"
+ "AMFDRPermissionRequest error: %@"
+ "AMFDRPermissionRequest successful"
+ "AlsC"
+ "CRComponentSigning"
+ "CRFDRMac5DeviceHandler"
+ "Cleanup %@, error: %@"
+ "CoverGlass"
+ "DEREncoderAddData failed"
+ "DEREncoderAddSequenceFromEncoder failed"
+ "DEREncoderCreateEncodedBuffer failed"
+ "Empty measurementDict, error: %@"
+ "Failed to _set_user_dir_suffix"
+ "Failed to allocate memmory for nonce"
+ "Failed to create FDR permission string"
+ "Failed to generate random nonce\n"
+ "Failed to get KBB %@, error: %@"
+ "Failed to get fCfg dataInstance from FDR sealing map"
+ "Failed to parse response"
+ "Failed to parse response, error: %@"
+ "Failed to read live MSRk dataInstance"
+ "IONVRAM-DELETEWRET-PROPERTY"
+ "IPAD COVER GLASS"
+ "IPAD VOLUME BUTTON"
+ "KBB FSC2 instance: %@ doesn't match live MSRk instance: %@"
+ "KBB fCfg doesn't contain LASC"
+ "LASC"
+ "Missing FDR data path: %@"
+ "Patch not supported, skipping"
+ "Repair"
+ "SECURE MODULE"
+ "Unable to create FDR permission string to copy KBB info"
+ "VolumeButton"
+ "activeFDRDataPathStr: %@"
+ "appendData:"
+ "authenticateBatteryWithChallenge:completionHandler:"
+ "authenticateTouchControllerWithChallenge:completionHandler:"
+ "bcrtSign:outSignature:outDeviceNonce:outError:"
+ "ccrngNonce is NULL"
+ "createECDSADerData"
+ "errorCode detected"
+ "fCfg"
+ "failed to allocate dstEncoder"
+ "failed to allocate encoder"
+ "getUnsealedSPCWithDataClass:"
+ "isEqualTo:"
+ "outSignature is NULL"
+ "prpcSign:outSignature:outDeviceNonce:outError:"
+ "sharedManager"
+ "signChallenge"
+ "signing timed out"
+ "tcrtSign:outSignature:outDeviceNonce:outError:"
+ "tmpFDRDataPathStr: %@"
+ "v24@0:8^{__AMFDR=}16"
+ "v36@?0B8@\"NSData\"12@\"NSData\"20B28i32"
+ "v48@0:8^{__CFData=}16r^^{__CFData}24r^^{__CFData}32^i40"
+ "vcrtSign:outSignature:outDeviceNonce:outError:"
- "/private/var/hardware/FactoryData/System/Library/Caches/Repair"
- "/private/var/tmp/com.apple.corerepaird/FactoryData"
- "@\"NSData\"16@?0@\"NSDictionary\"8"
- "@\"NSDictionary\"16@?0@\"NSData\"8"
- "@\"NSDictionary\"16@?0@\"NSMutableDictionary\"8"
- "@\"NSDictionary\"16@?0@\"NSString\"8"
- "@16@?0@\"NSDictionary\"8"
- "AMFDRDataCreatePermissionsString failed"
- "AMFDRPermisisonRequest error: %@"
- "AMFDRPermisisonRequest successful"
- "Delete %@, error: %@"
- "Empty measurementDict"
- "FDR data Real path is %@ (%ld)"
- "FDR data path is %@"
- "Failed to create FDR persmission string"
- "IONVRAM-DELETE-PROPERTY"
- "Missing FDR data path"
- "Unable to create FDR persmission string to copy KBB info"
- "challengeStrongComponents:withReply:"
- "issueRepairCert:withReply:"
- "queryRepairDeltaWithReply:"
- "sign:keyBlob:withReply:"
- "v40@0:8@16@24@?32"
- "v48@0:8@16@24@32@?40"
- "verify:signature:keyBlob:withReply:"

```
