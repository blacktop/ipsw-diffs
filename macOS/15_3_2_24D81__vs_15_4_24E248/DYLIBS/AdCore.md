## AdCore

> `/System/Library/PrivateFrameworks/AdCore.framework/Versions/A/AdCore`

```diff

-632.0.0.0.0
-  __TEXT.__text: 0x2b4c4
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x38f8
+636.4.0.0.0
+  __TEXT.__text: 0x2cf94
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__objc_methlist: 0x3d44
   __TEXT.__const: 0x188
-  __TEXT.__cstring: 0x3ab3
-  __TEXT.__gcc_except_tab: 0x444
+  __TEXT.__cstring: 0x3b23
+  __TEXT.__gcc_except_tab: 0x448
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0x53
-  __TEXT.__unwind_info: 0xb10
-  __TEXT.__objc_classname: 0x378
-  __TEXT.__objc_methname: 0x6aa5
-  __TEXT.__objc_methtype: 0xa67
-  __TEXT.__objc_stubs: 0x3b20
-  __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0x3c0
-  __DATA_CONST.__objc_classlist: 0x130
+  __TEXT.__unwind_info: 0xb68
+  __TEXT.__objc_classname: 0x3a1
+  __TEXT.__objc_methname: 0x6e0e
+  __TEXT.__objc_methtype: 0xa9f
+  __TEXT.__objc_stubs: 0x3c20
+  __DATA_CONST.__got: 0x348
+  __DATA_CONST.__const: 0x3d8
+  __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cb8
+  __DATA_CONST.__objc_selrefs: 0x1e20
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x130
+  __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0x188
-  __AUTH_CONST.__auth_got: 0x3b8
+  __AUTH_CONST.__auth_got: 0x3a8
   __AUTH_CONST.__const: 0x6e0
-  __AUTH_CONST.__cfstring: 0x4740
+  __AUTH_CONST.__cfstring: 0x4820
   __AUTH_CONST.__objc_const: 0x5700
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x390
+  __AUTH.__objc_data: 0x730
+  __DATA.__objc_ivar: 0x3b0
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0x550

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3B99CF31-D621-34FF-9BE2-C159643DBF9F
-  Functions: 1296
-  Symbols:   2780
-  CStrings:  2654
+  UUID: 0DDEA4AA-2412-3A12-B041-0F743A09C797
+  Functions: 1362
+  Symbols:   2889
+  CStrings:  2713
 
Symbols:
+ +[ADAnalyticsEvent options].cold.1
+ +[ADAttributionRequest options].cold.1
+ +[ADAttributionResponse options].cold.1
+ +[ADBackgroundTaskScheduler registerTaskDelegate:forRequestID:].cold.1
+ +[ADClientSettingsRequest options].cold.1
+ +[ADConfigurationRequest options].cold.1
+ +[ADKeyedParameterList options].cold.1
+ +[ADLogAnalyticsRequest options].cold.1
+ +[ADLogAnalyticsResponse options].cold.1
+ +[ADOptOutRequest options].cold.1
+ +[ADOptOutResponse options].cold.1
+ +[ADParameter options].cold.1
+ +[ADRotatingIdentifiers experimentBucketsType]
+ +[ADSegmentUpdateRequest options].cold.1
+ +[ADSegmentUpdateResponse options].cold.1
+ +[ADSponsoredSearchRequest options].cold.1
+ +[ADUserTransparencyRequest options].cold.1
+ -[ADCoreSettings adprivacydBag].cold.1
+ -[ADCoreSettings unitTesting].cold.1
+ -[ADExperimentBucket .cxx_destruct]
+ -[ADExperimentBucket bucketId]
+ -[ADExperimentBucket bucketNamespace]
+ -[ADExperimentBucket copyTo:]
+ -[ADExperimentBucket copyWithZone:]
+ -[ADExperimentBucket description]
+ -[ADExperimentBucket dictionaryRepresentation]
+ -[ADExperimentBucket generation]
+ -[ADExperimentBucket hasBucketId]
+ -[ADExperimentBucket hasBucketNamespace]
+ -[ADExperimentBucket hasGeneration]
+ -[ADExperimentBucket hash]
+ -[ADExperimentBucket isEqual:]
+ -[ADExperimentBucket mergeFrom:]
+ -[ADExperimentBucket readFrom:]
+ -[ADExperimentBucket setBucketId:]
+ -[ADExperimentBucket setBucketNamespace:]
+ -[ADExperimentBucket setGeneration:]
+ -[ADExperimentBucket setHasBucketId:]
+ -[ADExperimentBucket setHasGeneration:]
+ -[ADExperimentBucket writeTo:]
+ -[ADRotatingIdentifiers .cxx_destruct]
+ -[ADRotatingIdentifiers addExperimentBuckets:]
+ -[ADRotatingIdentifiers anonymousSessionId]
+ -[ADRotatingIdentifiers clearExperimentBuckets]
+ -[ADRotatingIdentifiers copyTo:]
+ -[ADRotatingIdentifiers copyWithZone:]
+ -[ADRotatingIdentifiers description]
+ -[ADRotatingIdentifiers dictionaryRepresentation]
+ -[ADRotatingIdentifiers experimentBucketsAtIndex:]
+ -[ADRotatingIdentifiers experimentBucketsCount]
+ -[ADRotatingIdentifiers experimentBuckets]
+ -[ADRotatingIdentifiers hasAnonymousSessionId]
+ -[ADRotatingIdentifiers hasRotatedAnonymousId]
+ -[ADRotatingIdentifiers hash]
+ -[ADRotatingIdentifiers isEqual:]
+ -[ADRotatingIdentifiers mergeFrom:]
+ -[ADRotatingIdentifiers readFrom:]
+ -[ADRotatingIdentifiers rotatedAnonymousId]
+ -[ADRotatingIdentifiers setAnonymousSessionId:]
+ -[ADRotatingIdentifiers setExperimentBuckets:]
+ -[ADRotatingIdentifiers setRotatedAnonymousId:]
+ -[ADRotatingIdentifiers writeTo:]
+ -[ADSponsoredSearchRequest hasRotatingIdentifiers]
+ -[ADSponsoredSearchRequest rotatingIdentifiers]
+ -[ADSponsoredSearchRequest setRotatingIdentifiers:]
+ ADAdsOptions.cold.1
+ ADEncryptString.cold.1
+ ClientTypeToString.cold.1
+ OBJC_IVAR_$_ADExperimentBucket._bucketId
+ OBJC_IVAR_$_ADExperimentBucket._bucketNamespace
+ OBJC_IVAR_$_ADExperimentBucket._generation
+ OBJC_IVAR_$_ADExperimentBucket._has
+ OBJC_IVAR_$_ADRotatingIdentifiers._anonymousSessionId
+ OBJC_IVAR_$_ADRotatingIdentifiers._experimentBuckets
+ OBJC_IVAR_$_ADRotatingIdentifiers._rotatedAnonymousId
+ OBJC_IVAR_$_ADSponsoredSearchRequest._rotatingIdentifiers
+ _ADExperimentBucketReadFrom
+ _ADLog.cold.1
+ _ADLogQueue.cold.1
+ _ADRotatingIdentifiersReadFrom
+ _OBJC_CLASS_$_ADExperimentBucket
+ _OBJC_CLASS_$_ADRotatingIdentifiers
+ _OBJC_METACLASS_$_ADExperimentBucket
+ _OBJC_METACLASS_$_ADRotatingIdentifiers
+ _TransactionQueue.cold.1
+ _TransactionsByReason.cold.1
+ __OBJC_$_CLASS_METHODS_ADRotatingIdentifiers
+ __OBJC_$_INSTANCE_METHODS_ADExperimentBucket
+ __OBJC_$_INSTANCE_METHODS_ADRotatingIdentifiers
+ __OBJC_$_INSTANCE_VARIABLES_ADExperimentBucket
+ __OBJC_$_INSTANCE_VARIABLES_ADRotatingIdentifiers
+ __OBJC_$_PROP_LIST_ADExperimentBucket
+ __OBJC_$_PROP_LIST_ADRotatingIdentifiers
+ __OBJC_CLASS_PROTOCOLS_$_ADExperimentBucket
+ __OBJC_CLASS_PROTOCOLS_$_ADRotatingIdentifiers
+ __OBJC_CLASS_RO_$_ADExperimentBucket
+ __OBJC_CLASS_RO_$_ADRotatingIdentifiers
+ __OBJC_METACLASS_RO_$_ADExperimentBucket
+ __OBJC_METACLASS_RO_$_ADRotatingIdentifiers
+ _objc_msgSend$addExperimentBuckets:
+ _objc_msgSend$clearExperimentBuckets
+ _objc_msgSend$experimentBucketsAtIndex:
+ _objc_msgSend$experimentBucketsCount
+ _objc_msgSend$setAnonymousSessionId:
+ _objc_msgSend$setBucketNamespace:
+ _objc_msgSend$setRotatedAnonymousId:
+ _objc_msgSend$setRotatingIdentifiers:
- _fmod
- _fmodf
CStrings:
+ "@\"ADRotatingIdentifiers\""
+ "ADExperimentBucket"
+ "ADRotatingIdentifiers"
+ "T@\"ADRotatingIdentifiers\",&,N,V_rotatingIdentifiers"
+ "T@\"NSMutableArray\",&,N,V_experimentBuckets"
+ "T@\"NSString\",&,N,V_anonymousSessionId"
+ "T@\"NSString\",&,N,V_bucketNamespace"
+ "T@\"NSString\",&,N,V_rotatedAnonymousId"
+ "Ti,N,V_bucketId"
+ "Ti,N,V_generation"
+ "_anonymousSessionId"
+ "_bucketId"
+ "_bucketNamespace"
+ "_experimentBuckets"
+ "_generation"
+ "_rotatedAnonymousId"
+ "_rotatingIdentifiers"
+ "addExperimentBuckets:"
+ "anonymousSessionId"
+ "bucketId"
+ "bucketNamespace"
+ "clearExperimentBuckets"
+ "experimentBuckets"
+ "experimentBucketsAtIndex:"
+ "experimentBucketsCount"
+ "experimentBucketsType"
+ "generation"
+ "hasAnonymousSessionId"
+ "hasBucketId"
+ "hasBucketNamespace"
+ "hasGeneration"
+ "hasRotatedAnonymousId"
+ "hasRotatingIdentifiers"
+ "rotatedAnonymousId"
+ "rotatingIdentifiers"
+ "setAnonymousSessionId:"
+ "setBucketId:"
+ "setBucketNamespace:"
+ "setExperimentBuckets:"
+ "setGeneration:"
+ "setHasBucketId:"
+ "setHasGeneration:"
+ "setRotatedAnonymousId:"
+ "setRotatingIdentifiers:"
+ "{?=\"bucketId\"b1\"generation\"b1}"

```
