## MLRuntime

> `/System/Library/PrivateFrameworks/MLRuntime.framework/MLRuntime`

```diff

-101.1.0.0.0
-  __TEXT.__text: 0xcfa0
+101.4.0.0.0
+  __TEXT.__text: 0xd984
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0xc30
+  __TEXT.__objc_methlist: 0xc98
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0xacc
+  __TEXT.__cstring: 0xb87
+  __TEXT.__oslogstring: 0xcad
   __TEXT.__gcc_except_tab: 0x360
-  __TEXT.__oslogstring: 0xbbc
-  __TEXT.__unwind_info: 0x3b4
-  __TEXT.__objc_classname: 0x2db
-  __TEXT.__objc_methname: 0x2a06
-  __TEXT.__objc_methtype: 0x6c7
-  __TEXT.__objc_stubs: 0x2100
+  __TEXT.__unwind_info: 0x3cc
+  __TEXT.__objc_classname: 0x2ee
+  __TEXT.__objc_methname: 0x2ab2
+  __TEXT.__objc_methtype: 0x6df
+  __TEXT.__objc_stubs: 0x2140
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x218
-  __DATA_CONST.__objc_classlist: 0xa0
+  __DATA_CONST.__const: 0x240
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2c58
-  __DATA_CONST.__objc_selrefs: 0xa38
-  __AUTH_CONST.__objc_const: 0xa00
-  __AUTH_CONST.__cfstring: 0xcc0
-  __AUTH_CONST.__const: 0x80
+  __DATA_CONST.__objc_const: 0x2c98
+  __DATA_CONST.__objc_selrefs: 0xa58
+  __AUTH_CONST.__objc_const: 0xa90
+  __AUTH_CONST.__cfstring: 0xd80
+  __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__auth_got: 0x240
-  __AUTH.__objc_data: 0x370
+  __AUTH.__objc_data: 0x3c0
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x1c0
-  __DATA.__objc_superrefs: 0x88
-  __DATA.__objc_ivar: 0xf0
+  __DATA.__objc_classrefs: 0x1c8
+  __DATA.__objc_superrefs: 0x90
+  __DATA.__objc_ivar: 0xf4
   __DATA.__data: 0x4e0
-  __DATA.__bss: 0x40
+  __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0x2d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 354
-  Symbols:   1507
-  CStrings:  773
+  Functions: 369
+  Symbols:   1552
+  CStrings:  793
 
Symbols:
+ +[MLRDonationManager defaultManager]
+ -[MLRDonationManager .cxx_destruct]
+ -[MLRDonationManager encodeAndUploadToDediscoWithIdentifier:measurements:withEncodingSchemas:metadata:completion:]
+ -[MLRDonationManager encodeAndUploadToDediscoWithIdentifier:measurements:withEncodingSchemas:metadata:completion:].cold.1
+ -[MLRDonationManager encodeAndUploadToDediscoWithIdentifier:measurements:withEncodingSchemas:metadata:completion:].cold.2
+ -[MLRDonationManager encodeAndUploadToDediscoWithIdentifier:measurements:withEncodingSchemas:metadata:completion:].cold.3
+ -[MLRDonationManager init]
+ -[MLRDonationManager queue]
+ -[MLRDonationManager record:data:encodingSchema:metadata:errorOut:]
+ -[MLRDonationManager record:data:encodingSchema:metadata:errorOut:].cold.1
+ -[MLRDonationManager setQueue:]
+ _OBJC_CLASS_$_MLRDonationManager
+ _OBJC_IVAR_$_MLRDonationManager._queue
+ _OBJC_METACLASS_$_MLRDonationManager
+ __OBJC_$_CLASS_METHODS_MLRDonationManager
+ __OBJC_$_INSTANCE_METHODS_MLRDonationManager
+ __OBJC_$_INSTANCE_VARIABLES_MLRDonationManager
+ __OBJC_$_PROP_LIST_MLRDonationManager
+ __OBJC_CLASS_RO_$_MLRDonationManager
+ __OBJC_METACLASS_RO_$_MLRDonationManager
+ ___114-[MLRDonationManager encodeAndUploadToDediscoWithIdentifier:measurements:withEncodingSchemas:metadata:completion:]_block_invoke
+ ___114-[MLRDonationManager encodeAndUploadToDediscoWithIdentifier:measurements:withEncodingSchemas:metadata:completion:]_block_invoke.cold.1
+ ___36+[MLRDonationManager defaultManager]_block_invoke
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ _defaultManager.donationManagerClient
+ _defaultManager.onceToken
+ _objc_msgSend$UTF8String
+ _objc_msgSend$queue
CStrings:
+ "MLRDonationManager"
+ "Recording key=%@, data=%@, encodingSchema=%@, metadata=%@"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "The encodingSchema type has to be either %@ or %@."
+ "The encodingSchema type has to be either decimal or fedstats."
+ "The identifier must not be nil."
+ "UTF8String"
+ "_queue"
+ "dedisco donation hit error: %@"
+ "encodeAndUploadToDediscoWithIdentifier:measurements:withEncodingSchemas:metadata:completion:"
+ "encodingParameters"
+ "encodingSchemas must be not be nil."
+ "fedstats"
+ "identifier must not be nil."
+ "measurements must be not be nil."
+ "queue"
+ "setQueue:"
+ "v56@0:8@16@24@32@40@?48"

```
