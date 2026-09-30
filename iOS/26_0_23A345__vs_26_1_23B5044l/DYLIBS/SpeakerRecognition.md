## SpeakerRecognition

> `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`

```diff

-3500.122.2.0.0
-  __TEXT.__text: 0x8bf84
-  __TEXT.__auth_stubs: 0x1240
-  __TEXT.__objc_methlist: 0x6530
+3505.14.3.0.0
+  __TEXT.__text: 0x8df30
+  __TEXT.__auth_stubs: 0x1250
+  __TEXT.__objc_methlist: 0x6658
   __TEXT.__const: 0x4c8
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__cstring: 0xfc2a
+  __TEXT.__cstring: 0x1005e
   __TEXT.__swift5_typeref: 0xea
   __TEXT.__constg_swiftt: 0x320
   __TEXT.__swift5_fieldmd: 0x128
   __TEXT.__swift5_reflstr: 0x18a
   __TEXT.__swift5_types: 0x10
-  __TEXT.__gcc_except_tab: 0x2d34
-  __TEXT.__oslogstring: 0xc5bb
-  __TEXT.__unwind_info: 0x18b0
-  __TEXT.__objc_classname: 0xda6
-  __TEXT.__objc_methname: 0x11afc
-  __TEXT.__objc_methtype: 0x24a3
-  __TEXT.__objc_stubs: 0xa520
-  __DATA_CONST.__got: 0x938
-  __DATA_CONST.__const: 0x1cd8
-  __DATA_CONST.__objc_classlist: 0x2c0
+  __TEXT.__gcc_except_tab: 0x2d38
+  __TEXT.__oslogstring: 0xc814
+  __TEXT.__unwind_info: 0x18e8
+  __TEXT.__objc_classname: 0xe2e
+  __TEXT.__objc_methname: 0x11c16
+  __TEXT.__objc_methtype: 0x253e
+  __TEXT.__objc_stubs: 0xa660
+  __DATA_CONST.__got: 0x948
+  __DATA_CONST.__const: 0x1d40
+  __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x140
+  __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b40
-  __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x200
-  __DATA_CONST.__objc_arraydata: 0x3c0
-  __AUTH_CONST.__auth_got: 0x938
-  __AUTH_CONST.__const: 0x4d0
-  __AUTH_CONST.__cfstring: 0x51c0
-  __AUTH_CONST.__objc_const: 0xaa70
-  __AUTH_CONST.__objc_dictobj: 0x960
+  __DATA_CONST.__objc_selrefs: 0x3b78
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x218
+  __DATA_CONST.__objc_arraydata: 0x3e0
+  __AUTH_CONST.__auth_got: 0x940
+  __AUTH_CONST.__const: 0x4f0
+  __AUTH_CONST.__cfstring: 0x5260
+  __AUTH_CONST.__objc_const: 0xae10
+  __AUTH_CONST.__objc_dictobj: 0x9b0
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x18d8
+  __AUTH.__objc_data: 0x19c8
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0x820
-  __DATA.__data: 0x1000
-  __DATA.__bss: 0xf0
+  __DATA.__objc_ivar: 0x834
+  __DATA.__data: 0x1060
+  __DATA.__bss: 0x100
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0x6b8
   __DATA_DIRTY.__bss: 0x48

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8F2773C3-DBDB-3E7D-8D97-300EA944617E
-  Functions: 2382
-  Symbols:   8169
-  CStrings:  6044
+  UUID: 91C7FE0B-6DEE-39C8-9382-9DB8717375EF
+  Functions: 2414
+  Symbols:   8286
+  CStrings:  6096
 
Symbols:
+ +[SSRVoiceProfileManagerXPCClient createVoiceProfileManagerXPCConnection]
+ +[SSRVoiceProfileManagerXPCClient sharedClient]
+ -[SSREnrollmentUtterance approximateGenerationDate]
+ -[SSREnrollmentUtterance description]
+ -[SSREnrollmentUtterance parseMetadataFromDictionary:]
+ -[SSREnrollmentUtterance productType]
+ -[SSREnrollmentUtterance productVersion]
+ -[SSRVoiceProfileManager addUtterances:toProfile:withContext:doUtteranceDonation:withCompletion:]
+ -[SSRVoiceProfileManagerXPCClient .cxx_destruct]
+ -[SSRVoiceProfileManagerXPCClient importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]
+ -[SSRVoiceProfileManagerXPCClient init]
+ -[SSRVoiceProfileManagerXPCClient markSATEnrollmentSuccessForVoiceProfile:completion:]
+ -[SSRVoiceProfileManagerXPCClient queue]
+ -[SSRVoiceProfileManagerXPCClient setQueue:]
+ -[SSRVoiceProfileManagerXPCListener .cxx_destruct]
+ -[SSRVoiceProfileManagerXPCListener init]
+ -[SSRVoiceProfileManagerXPCListener listen]
+ -[SSRVoiceProfileManagerXPCListener listener:shouldAcceptNewConnection:]
+ -[SSRVoiceProfileManagerXPCListener setXpcListener:]
+ -[SSRVoiceProfileManagerXPCListener xpcListener]
+ -[SSRVoiceProfileManagerXPCService importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]
+ -[SSRVoiceProfileManagerXPCService init]
+ -[SSRVoiceProfileManagerXPCService markSATEnrollmentSuccessForVoiceProfile:completion:]
+ GCC_except_table1261
+ GCC_except_table1265
+ GCC_except_table1274
+ GCC_except_table1279
+ GCC_except_table1283
+ GCC_except_table1344
+ GCC_except_table1350
+ GCC_except_table1354
+ GCC_except_table1358
+ GCC_except_table1361
+ GCC_except_table1367
+ GCC_except_table1396
+ GCC_except_table1445
+ GCC_except_table1460
+ GCC_except_table1476
+ GCC_except_table1483
+ GCC_except_table1553
+ GCC_except_table1657
+ GCC_except_table1663
+ GCC_except_table1678
+ GCC_except_table1688
+ GCC_except_table1698
+ GCC_except_table1719
+ GCC_except_table1723
+ GCC_except_table1727
+ GCC_except_table1733
+ GCC_except_table1741
+ GCC_except_table1805
+ GCC_except_table1809
+ GCC_except_table1851
+ GCC_except_table1886
+ GCC_except_table1951
+ GCC_except_table1960
+ GCC_except_table1969
+ GCC_except_table1980
+ GCC_except_table1989
+ GCC_except_table2008
+ GCC_except_table2070
+ _CSLogInitIfNeeded
+ _OBJC_CLASS_$_CSRemoteAssetManagerFactory
+ _OBJC_CLASS_$_SSRVoiceProfileManagerXPCClient
+ _OBJC_CLASS_$_SSRVoiceProfileManagerXPCListener
+ _OBJC_CLASS_$_SSRVoiceProfileManagerXPCService
+ _OBJC_IVAR_$_SSREnrollmentUtterance._approximateGenerationDate
+ _OBJC_IVAR_$_SSREnrollmentUtterance._productType
+ _OBJC_IVAR_$_SSREnrollmentUtterance._productVersion
+ _OBJC_IVAR_$_SSRVoiceProfileManagerXPCClient._queue
+ _OBJC_IVAR_$_SSRVoiceProfileManagerXPCListener._xpcListener
+ _OBJC_METACLASS_$_SSRVoiceProfileManagerXPCClient
+ _OBJC_METACLASS_$_SSRVoiceProfileManagerXPCListener
+ _OBJC_METACLASS_$_SSRVoiceProfileManagerXPCService
+ _SSRVoiceProfileManagerXPCEntitlement
+ _SSRVoiceProfileManagerXPCServiceName
+ _SSRVoiceRetrainingSecureAssetKey
+ __OBJC_$_CLASS_METHODS_SSRVoiceProfileManagerXPCClient
+ __OBJC_$_INSTANCE_METHODS_SSRVoiceProfileManagerXPCClient
+ __OBJC_$_INSTANCE_METHODS_SSRVoiceProfileManagerXPCListener
+ __OBJC_$_INSTANCE_METHODS_SSRVoiceProfileManagerXPCService
+ __OBJC_$_INSTANCE_VARIABLES_SSRVoiceProfileManagerXPCClient
+ __OBJC_$_INSTANCE_VARIABLES_SSRVoiceProfileManagerXPCListener
+ __OBJC_$_PROP_LIST_SSRVoiceProfileManagerXPCClient
+ __OBJC_$_PROP_LIST_SSRVoiceProfileManagerXPCListener
+ __OBJC_$_PROP_LIST_SSRVoiceProfileManagerXPCService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRVoiceProfileManagerXPCProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVoiceProfileManagerXPCProtocol
+ __OBJC_$_PROTOCOL_REFS_SSRVoiceProfileManagerXPCProtocol
+ __OBJC_CLASS_PROTOCOLS_$_SSRVoiceProfileManagerXPCListener
+ __OBJC_CLASS_PROTOCOLS_$_SSRVoiceProfileManagerXPCService
+ __OBJC_CLASS_RO_$_SSRVoiceProfileManagerXPCClient
+ __OBJC_CLASS_RO_$_SSRVoiceProfileManagerXPCListener
+ __OBJC_CLASS_RO_$_SSRVoiceProfileManagerXPCService
+ __OBJC_LABEL_PROTOCOL_$_SSRVoiceProfileManagerXPCProtocol
+ __OBJC_METACLASS_RO_$_SSRVoiceProfileManagerXPCClient
+ __OBJC_METACLASS_RO_$_SSRVoiceProfileManagerXPCListener
+ __OBJC_METACLASS_RO_$_SSRVoiceProfileManagerXPCService
+ __OBJC_PROTOCOL_$_SSRVoiceProfileManagerXPCProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_SSRVoiceProfileManagerXPCProtocol
+ ___148-[SSRVoiceProfileManagerXPCClient importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke
+ ___148-[SSRVoiceProfileManagerXPCClient importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke.70
+ ___148-[SSRVoiceProfileManagerXPCClient importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke.71
+ ___148-[SSRVoiceProfileManagerXPCClient importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke.76
+ ___148-[SSRVoiceProfileManagerXPCClient importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke.81
+ ___149-[SSRVoiceProfileManagerXPCService importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke
+ ___149-[SSRVoiceProfileManagerXPCService importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke.10
+ ___149-[SSRVoiceProfileManagerXPCService importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke.25
+ ___47+[SSRVoiceProfileManagerXPCClient sharedClient]_block_invoke
+ ___86-[SSRVoiceProfileManagerXPCClient markSATEnrollmentSuccessForVoiceProfile:completion:]_block_invoke
+ ___86-[SSRVoiceProfileManagerXPCClient markSATEnrollmentSuccessForVoiceProfile:completion:]_block_invoke.51
+ ___86-[SSRVoiceProfileManagerXPCClient markSATEnrollmentSuccessForVoiceProfile:completion:]_block_invoke.53
+ ___86-[SSRVoiceProfileManagerXPCClient markSATEnrollmentSuccessForVoiceProfile:completion:]_block_invoke.60
+ ___86-[SSRVoiceProfileManagerXPCClient markSATEnrollmentSuccessForVoiceProfile:completion:]_block_invoke.68
+ ___87-[SSRVoiceProfileManagerXPCService markSATEnrollmentSuccessForVoiceProfile:completion:]_block_invoke
+ ___97-[SSRVoiceProfileManager addUtterances:toProfile:withContext:doUtteranceDonation:withCompletion:]_block_invoke
+ ___97-[SSRVoiceProfileManager addUtterances:toProfile:withContext:doUtteranceDonation:withCompletion:]_block_invoke_2
+ ___97-[SSRVoiceProfileManager addUtterances:toProfile:withContext:doUtteranceDonation:withCompletion:]_block_invoke_3
+ ___Block_byref_object_copy_.5510
+ ___Block_byref_object_copy_.5702
+ ___Block_byref_object_copy_.5906
+ ___Block_byref_object_copy_.6714
+ ___Block_byref_object_copy_.7161
+ ___Block_byref_object_copy_.7275
+ ___Block_byref_object_copy_.7501
+ ___Block_byref_object_copy_.7847
+ ___Block_byref_object_copy_.8659
+ ___Block_byref_object_dispose_.5511
+ ___Block_byref_object_dispose_.5703
+ ___Block_byref_object_dispose_.5907
+ ___Block_byref_object_dispose_.6715
+ ___Block_byref_object_dispose_.7162
+ ___Block_byref_object_dispose_.7276
+ ___Block_byref_object_dispose_.7502
+ ___Block_byref_object_dispose_.7848
+ ___Block_byref_object_dispose_.8660
+ ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72s80bs_e5_v8?0ls80l8s32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.5991
+ ___block_literal_global.6193
+ ___block_literal_global.6768
+ ___block_literal_global.7285
+ ___block_literal_global.7535
+ ___block_literal_global.7724
+ ___block_literal_global.7999
+ ___block_literal_global.8188
+ ___block_literal_global.8499
+ ___block_literal_global.8961
+ ___block_literal_global.9330
+ _objc_msgSend$addUtterances:toProfile:withContext:doUtteranceDonation:withCompletion:
+ _objc_msgSend$approximateGenerationDate
+ _objc_msgSend$createVoiceProfileManagerXPCConnection
+ _objc_msgSend$enrollmentUtteranceUrl
+ _objc_msgSend$needRetrainingForExclaveOnly
+ _objc_msgSend$parseMetadataFromDictionary:
+ _objc_msgSend$productType
+ _objc_msgSend$productVersion
+ _objc_msgSend$remoteAssetManager
+ _objc_msgSend$secureAsset
+ _objc_msgSend$sharedClient
+ _objc_msgSend$triggerPhrase
+ _sharedClient.onceToken
+ _sharedClient.sharedClient
+ _sharedInstance.onceToken.7998
+ _sharedInstance.onceToken.8498
+ _sharedManager.onceToken.7534
- +[SSRUtils needProfileEmbeddingsForDarwin]
- -[SSRVoiceProfileManager _addUtterances:toProfile:withContext:doUtteranceDonation:withCompletion:]
- -[SSRVoiceProfileManager _updateUserProfileAndAddVoiceProfile:withCompletion:]
- -[SSRVoiceProfileManager updateVoiceProfileIdInUserProfile:personaId:completion:]
- GCC_except_table1262
- GCC_except_table1266
- GCC_except_table1275
- GCC_except_table1280
- GCC_except_table1284
- GCC_except_table1345
- GCC_except_table1351
- GCC_except_table1355
- GCC_except_table1359
- GCC_except_table1362
- GCC_except_table1368
- GCC_except_table1397
- GCC_except_table1446
- GCC_except_table1461
- GCC_except_table1477
- GCC_except_table1484
- GCC_except_table1554
- GCC_except_table1662
- GCC_except_table1668
- GCC_except_table1683
- GCC_except_table1693
- GCC_except_table1708
- GCC_except_table1724
- GCC_except_table1728
- GCC_except_table1732
- GCC_except_table1738
- GCC_except_table1746
- GCC_except_table1810
- GCC_except_table1814
- GCC_except_table1856
- GCC_except_table1891
- GCC_except_table1956
- GCC_except_table1965
- GCC_except_table1974
- GCC_except_table1985
- GCC_except_table1994
- GCC_except_table2013
- GCC_except_table2043
- _OBJC_CLASS_$_CSRemoteAssetManager
- ___139-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke.335
- ___139-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke.349
- ___98-[SSRVoiceProfileManager _addUtterances:toProfile:withContext:doUtteranceDonation:withCompletion:]_block_invoke
- ___98-[SSRVoiceProfileManager _addUtterances:toProfile:withContext:doUtteranceDonation:withCompletion:]_block_invoke_2
- ___98-[SSRVoiceProfileManager _addUtterances:toProfile:withContext:doUtteranceDonation:withCompletion:]_block_invoke_3
- ___Block_byref_object_copy_.5506
- ___Block_byref_object_copy_.5700
- ___Block_byref_object_copy_.5904
- ___Block_byref_object_copy_.6741
- ___Block_byref_object_copy_.7167
- ___Block_byref_object_copy_.7281
- ___Block_byref_object_copy_.7507
- ___Block_byref_object_copy_.7857
- ___Block_byref_object_copy_.8357
- ___Block_byref_object_dispose_.5507
- ___Block_byref_object_dispose_.5701
- ___Block_byref_object_dispose_.5905
- ___Block_byref_object_dispose_.6742
- ___Block_byref_object_dispose_.7168
- ___Block_byref_object_dispose_.7282
- ___Block_byref_object_dispose_.7508
- ___Block_byref_object_dispose_.7858
- ___Block_byref_object_dispose_.8358
- ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_literal_global.5989
- ___block_literal_global.6191
- ___block_literal_global.6776
- ___block_literal_global.7291
- ___block_literal_global.7541
- ___block_literal_global.7733
- ___block_literal_global.8009
- ___block_literal_global.8197
- ___block_literal_global.8612
- ___block_literal_global.8981
- _objc_msgSend$_addUtterances:toProfile:withContext:doUtteranceDonation:withCompletion:
- _objc_msgSend$needProfileEmbeddingsForDarwin
- _sharedInstance.onceToken.8008
- _sharedInstance.onceToken.8196
- _sharedManager.onceToken.7540
CStrings:
+ "%s Audio file does not exist at path: %@"
+ "%s Completion called with error: %@"
+ "%s Completion called with result: %i, error: %@"
+ "%s ERR: Retraining context failed to init with error: %@"
+ "%s Failed to extract phId from metadata, using default trigger phrase"
+ "%s Failed to parse grainedDate string: %@, setting to nil"
+ "%s Remote object proxy error: %@"
+ "%s SSRVoiceProfileManagerXPCListener: Connection accepted and resumed"
+ "%s SSRVoiceProfileManagerXPCListener: New connection request"
+ "%s SSRVoiceProfileManagerXPCListener: Starting to listen"
+ "%s XPC connection established"
+ "%s enrollmentUtteranceUrl cannot be nil"
+ "-[SSREnrollmentUtterance parseMetadataFromDictionary:]"
+ "-[SSRVoiceProfileManager addUtterances:toProfile:withContext:doUtteranceDonation:withCompletion:]"
+ "-[SSRVoiceProfileManager addUtterances:toProfile:withContext:doUtteranceDonation:withCompletion:]_block_invoke"
+ "-[SSRVoiceProfileManager addUtterances:toProfile:withContext:doUtteranceDonation:withCompletion:]_block_invoke_3"
+ "-[SSRVoiceProfileManagerXPCClient importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke"
+ "-[SSRVoiceProfileManagerXPCClient markSATEnrollmentSuccessForVoiceProfile:completion:]_block_invoke"
+ "-[SSRVoiceProfileManagerXPCListener listen]"
+ "-[SSRVoiceProfileManagerXPCListener listener:shouldAcceptNewConnection:]"
+ "-[SSRVoiceProfileManagerXPCService importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]"
+ "-[SSRVoiceProfileManagerXPCService importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]_block_invoke"
+ "-[SSRVoiceProfileManagerXPCService markSATEnrollmentSuccessForVoiceProfile:completion:]"
+ "-[SSRVoiceProfileManagerXPCService markSATEnrollmentSuccessForVoiceProfile:completion:]_block_invoke"
+ "SSREnrollmentUtterance: URL=%@, isExplicit=%@, triggerPhrase=%lu, productType=%@, productVersion=%@, approximateGenerationDate=%@"
+ "SSRVoiceProfileManagerXPCClient"
+ "SSRVoiceProfileManagerXPCListener"
+ "SSRVoiceProfileManagerXPCProtocol"
+ "SSRVoiceProfileManagerXPCService"
+ "SSRVoiceRetrainingSecureAsset"
+ "T@\"NSDate\",R,N,V_approximateGenerationDate"
+ "T@\"NSString\",R,N,V_productType"
+ "T@\"NSString\",R,N,V_productVersion"
+ "T@\"NSXPCListener\",&,N,V_xpcListener"
+ "XPC Connection interrupted"
+ "XPC Connection invalidated"
+ "_approximateGenerationDate"
+ "_productType"
+ "_productVersion"
+ "_xpcListener"
+ "addUtterances:toProfile:withContext:doUtteranceDonation:withCompletion:"
+ "approximateGenerationDate"
+ "com.apple.siri.voiceprofilemanager.xpc"
+ "com.apple.siri.voiceprofilemanager.xpc.client"
+ "createVoiceProfileManagerXPCConnection"
+ "needRetrainingForExclaveOnly"
+ "parseMetadataFromDictionary:"
+ "private.corespeech.voiceprofiles"
+ "remoteAssetManager"
+ "setXpcListener:"
+ "sharedClient"
+ "v32@0:8@\"SSRVoiceProfile\"16@?<v@?B@\"NSError\">24"
+ "v76@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"CSAsset\"56B64@?<v@?@\"NSError\">68"
+ "xpcListener"
- "-[SSRVoiceProfileManager _addUtterances:toProfile:withContext:doUtteranceDonation:withCompletion:]"
- "-[SSRVoiceProfileManager _addUtterances:toProfile:withContext:doUtteranceDonation:withCompletion:]_block_invoke"
- "-[SSRVoiceProfileManager _addUtterances:toProfile:withContext:doUtteranceDonation:withCompletion:]_block_invoke_3"
- "-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withPersonaId:withLocale:withAsset:trainWithPayload:withCompletion:]"
- "Platform or device doesn't support User Profiles"
- "_addUtterances:toProfile:withContext:doUtteranceDonation:withCompletion:"
- "_updateUserProfileAndAddVoiceProfile:withCompletion:"
- "needProfileEmbeddingsForDarwin"
- "updateVoiceProfileIdInUserProfile:personaId:completion:"

```
