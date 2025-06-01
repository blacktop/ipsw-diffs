## HealthAppServices

> `/System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices`

```diff

-4146.3.2.0.0
-  __TEXT.__text: 0x19828
-  __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__objc_methlist: 0x418
-  __TEXT.__const: 0xd92
-  __TEXT.__cstring: 0xbd2
+4146.4.18.0.0
+  __TEXT.__text: 0x1bbd4
+  __TEXT.__auth_stubs: 0xc40
+  __TEXT.__objc_methlist: 0x540
+  __TEXT.__const: 0xd32
+  __TEXT.__cstring: 0x1082
   __TEXT.__oslogstring: 0x55
   __TEXT.__swift5_typeref: 0x2c6
   __TEXT.__swift5_reflstr: 0x44e

   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x668
+  __TEXT.__unwind_info: 0x6fc
   __TEXT.__eh_frame: 0x110
-  __TEXT.__objc_classname: 0x111
-  __TEXT.__objc_methname: 0x10d5
-  __TEXT.__objc_methtype: 0x12a
-  __TEXT.__objc_stubs: 0xa20
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0xd0
-  __DATA_CONST.__objc_classlist: 0x50
+  __TEXT.__objc_classname: 0x1d4
+  __TEXT.__objc_methname: 0x15d6
+  __TEXT.__objc_methtype: 0x2e9
+  __TEXT.__objc_stubs: 0xd40
+  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__const: 0x1d0
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x468
-  __DATA_CONST.__objc_selrefs: 0x448
+  __DATA_CONST.__objc_const: 0xaf8
+  __DATA_CONST.__objc_selrefs: 0x550
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0xd0
+  __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__cfstring: 0x640
-  __AUTH_CONST.__objc_const: 0x358
+  __AUTH_CONST.__cfstring: 0x740
+  __AUTH_CONST.__objc_const: 0x478
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__const: 0xab0
-  __AUTH_CONST.__auth_got: 0x5e0
-  __AUTH.__objc_data: 0x328
+  __AUTH_CONST.__auth_got: 0x628
+  __AUTH.__objc_data: 0x3c8
   __AUTH.__data: 0x178
-  __DATA.__objc_classrefs: 0xa0
-  __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x6b0
+  __DATA.__objc_ivar: 0x24
+  __DATA.__data: 0xb40
   __DATA.__bss: 0x1000
+  __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0xb8
   __DATA_DIRTY.__data: 0x1c0
   __DATA_DIRTY.__common: 0x18

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1CA5BAE1-C57D-3EF1-A582-C781BCDC27A3
-  Functions: 673
-  Symbols:   533
-  CStrings:  347
+  UUID: A01DF85D-FE35-323C-BC37-EED79A71CA6A
+  Functions: 729
+  Symbols:   706
+  CStrings:  493
 
Symbols:
+ +[HealthAppAnalyticsAcceptance supportsSecureCoding]
+ +[HealthAppAnalyticsStore setUserDidAccept:currentAgreement:completion:]
+ -[HealthAppAnalyticsAcceptance .cxx_destruct]
+ -[HealthAppAnalyticsAcceptance accepted]
+ -[HealthAppAnalyticsAcceptance agreement]
+ -[HealthAppAnalyticsAcceptance copyWithZone:]
+ -[HealthAppAnalyticsAcceptance encodeWithCoder:]
+ -[HealthAppAnalyticsAcceptance hash]
+ -[HealthAppAnalyticsAcceptance initForAgreement:version:accepted:modificationDate:]
+ -[HealthAppAnalyticsAcceptance initWithCoder:]
+ -[HealthAppAnalyticsAcceptance init]
+ -[HealthAppAnalyticsAcceptance isEqual:]
+ -[HealthAppAnalyticsAcceptance modificationDate]
+ -[HealthAppAnalyticsAcceptance version]
+ -[HealthAppAnalyticsStore .cxx_destruct]
+ -[HealthAppAnalyticsStore connectionInvalidated]
+ -[HealthAppAnalyticsStore exportedInterface]
+ -[HealthAppAnalyticsStore initWithHealthStore:]
+ -[HealthAppAnalyticsStore remoteInterface]
+ -[HealthAppAnalyticsStore setUserDidAccept:agreement:version:completion:]
+ -[HealthAppAnalyticsStore setUserDidAccept:currentAgreement:completion:]
+ _AllHealthAppAnalyticsAgreements
+ _HealthAppAnalyticsAgreementImproveHealthAndAnalytics
+ _HealthAppAnalyticsAgreementImproveHealthRecords
+ _HealthAppAnalyticsStoreTaskServerIdentifier
+ _NSInvalidArgumentException
+ _NSStringFromSelector
+ _OBJC_CLASS_$_HKHealthStore
+ _OBJC_CLASS_$_HKTaskServerProxyProvider
+ _OBJC_CLASS_$_HealthAppAnalyticsAcceptance
+ _OBJC_CLASS_$_HealthAppAnalyticsStore
+ _OBJC_CLASS_$_NSException
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_IVAR_$_HealthAppAnalyticsAcceptance._accepted
+ _OBJC_IVAR_$_HealthAppAnalyticsAcceptance._agreement
+ _OBJC_IVAR_$_HealthAppAnalyticsAcceptance._modificationDate
+ _OBJC_IVAR_$_HealthAppAnalyticsAcceptance._version
+ _OBJC_IVAR_$_HealthAppAnalyticsStore._healthStore
+ _OBJC_IVAR_$_HealthAppAnalyticsStore._proxyProvider
+ _OBJC_METACLASS_$_HealthAppAnalyticsAcceptance
+ _OBJC_METACLASS_$_HealthAppAnalyticsStore
+ __NSConcreteStackBlock
+ __OBJC_$_CLASS_METHODS_HealthAppAnalyticsAcceptance
+ __OBJC_$_CLASS_METHODS_HealthAppAnalyticsStore
+ __OBJC_$_CLASS_PROP_LIST_HealthAppAnalyticsAcceptance
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_INSTANCE_METHODS_HealthAppAnalyticsAcceptance
+ __OBJC_$_INSTANCE_METHODS_HealthAppAnalyticsStore
+ __OBJC_$_INSTANCE_VARIABLES_HealthAppAnalyticsAcceptance
+ __OBJC_$_INSTANCE_VARIABLES_HealthAppAnalyticsStore
+ __OBJC_$_PROP_LIST_HealthAppAnalyticsAcceptance
+ __OBJC_$_PROP_LIST_HealthAppAnalyticsStore
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HealthAppAnalyticsStoreServerInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__HKXPCExportable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__HKXPCExportable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HealthAppAnalyticsStoreServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES__HKXPCExportable
+ __OBJC_$_PROTOCOL_REFS_HealthAppAnalyticsStoreClientInterface
+ __OBJC_$_PROTOCOL_REFS_HealthAppAnalyticsStoreServerInterface
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS__HKXPCExportable
+ __OBJC_CLASS_PROTOCOLS_$_HealthAppAnalyticsAcceptance
+ __OBJC_CLASS_PROTOCOLS_$_HealthAppAnalyticsStore
+ __OBJC_CLASS_RO_$_HealthAppAnalyticsAcceptance
+ __OBJC_CLASS_RO_$_HealthAppAnalyticsStore
+ __OBJC_LABEL_PROTOCOL_$_HealthAppAnalyticsStoreClientInterface
+ __OBJC_LABEL_PROTOCOL_$_HealthAppAnalyticsStoreServerInterface
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_LABEL_PROTOCOL_$__HKXPCExportable
+ __OBJC_METACLASS_RO_$_HealthAppAnalyticsAcceptance
+ __OBJC_METACLASS_RO_$_HealthAppAnalyticsStore
+ __OBJC_PROTOCOL_$_HealthAppAnalyticsStoreClientInterface
+ __OBJC_PROTOCOL_$_HealthAppAnalyticsStoreServerInterface
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ __OBJC_PROTOCOL_$__HKXPCExportable
+ __OBJC_PROTOCOL_REFERENCE_$_HealthAppAnalyticsStoreClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_HealthAppAnalyticsStoreServerInterface
+ ___72+[HealthAppAnalyticsStore setUserDidAccept:currentAgreement:completion:]_block_invoke
+ ___72-[HealthAppAnalyticsStore setUserDidAccept:currentAgreement:completion:]_block_invoke
+ ___72-[HealthAppAnalyticsStore setUserDidAccept:currentAgreement:completion:]_block_invoke_2
+ ___72-[HealthAppAnalyticsStore setUserDidAccept:currentAgreement:completion:]_block_invoke_3
+ ___72-[HealthAppAnalyticsStore setUserDidAccept:currentAgreement:completion:]_block_invoke_4
+ ___72-[HealthAppAnalyticsStore setUserDidAccept:currentAgreement:completion:]_block_invoke_5
+ ___73-[HealthAppAnalyticsStore setUserDidAccept:agreement:version:completion:]_block_invoke
+ ___73-[HealthAppAnalyticsStore setUserDidAccept:agreement:version:completion:]_block_invoke_2
+ ___73-[HealthAppAnalyticsStore setUserDidAccept:agreement:version:completion:]_block_invoke_3
+ ___73-[HealthAppAnalyticsStore setUserDidAccept:agreement:version:completion:]_block_invoke_4
+ ___73-[HealthAppAnalyticsStore setUserDidAccept:agreement:version:completion:]_block_invoke_5
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_57_e8_32s40s48bs_e50_v16?0"<HealthAppAnalyticsStoreServerInterface>"8ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48bs_e50_v16?0"<HealthAppAnalyticsStoreServerInterface>"8ls32l8s40l8s48l8
+ _dispatch_async
+ _objc_msgSend$UUID
+ _objc_msgSend$accepted
+ _objc_msgSend$agreement
+ _objc_msgSend$clientQueue
+ _objc_msgSend$copy
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$fetchProxyWithHandler:errorHandler:
+ _objc_msgSend$hash
+ _objc_msgSend$initForAgreement:version:accepted:modificationDate:
+ _objc_msgSend$initWithHealthStore:
+ _objc_msgSend$initWithHealthStore:taskIdentifier:exportedObject:taskUUID:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$isEqualToDate:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$modificationDate
+ _objc_msgSend$raise:format:
+ _objc_msgSend$remote_setAccepted:agreement:version:completion:
+ _objc_msgSend$remote_setAccepted:currentAgreement:completion:
+ _objc_msgSend$setUserDidAccept:currentAgreement:completion:
+ _objc_msgSend$version
+ _objc_opt_isKindOfClass
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x9
+ _swift_deallocClassInstance
- _objc_retain_x27
CStrings:
+ "\x02"
+ "\x11"
+ "#16@0:8"
+ "@\"HKHealthStore\""
+ "@\"HKTaskServerProxyProvider\""
+ "@\"NSDate\""
+ "@\"NSString\"16@0:8"
+ "@\"NSXPCInterface\"16@0:8"
+ "@24@0:8:16"
+ "@24@0:8@\"NSCoder\"16"
+ "@24@0:8^{_NSZone=}16"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "@44@0:8@16q24B32@36"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "Division by zero"
+ "Division results in an overflow"
+ "Fatal error"
+ "HealthAppAnalyticsAcceptance"
+ "HealthAppAnalyticsStore"
+ "HealthAppAnalyticsStoreClientInterface"
+ "HealthAppAnalyticsStoreServerInterface"
+ "ImproveHealthAndAnalytics"
+ "ImproveHealthRecords"
+ "Insufficient space allocated to copy string contents"
+ "Must take zero or more splits"
+ "NSCoding"
+ "NSCopying"
+ "NSObject"
+ "NSSecureCoding"
+ "Q16@0:8"
+ "Range requires lowerBound <= upperBound"
+ "Swift/Collection.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/Range.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T#,R"
+ "T@\"NSDate\",R,N,V_modificationDate"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@\"NSString\",R,C,N,V_agreement"
+ "TB,R"
+ "TB,R,N,V_accepted"
+ "TQ,R"
+ "The -%@ method is not available on %@"
+ "Tq,R,N,V_version"
+ "UUID"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "_HKXPCExportable"
+ "_accepted"
+ "_agreement"
+ "_healthStore"
+ "_modificationDate"
+ "_proxyProvider"
+ "_version"
+ "accepted"
+ "agreement"
+ "autorelease"
+ "class"
+ "clientQueue"
+ "conformsToProtocol:"
+ "connectionConfigured"
+ "connectionInterrupted"
+ "connectionInvalidated"
+ "copy"
+ "copyWithZone:"
+ "debugDescription"
+ "decodeBoolForKey:"
+ "decodeIntegerForKey:"
+ "decodeObjectOfClass:forKey:"
+ "description"
+ "encodeBool:forKey:"
+ "encodeInteger:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "exportedInterface"
+ "fetchProxyWithHandler:errorHandler:"
+ "hash"
+ "initForAgreement:version:accepted:modificationDate:"
+ "initWithCoder:"
+ "initWithHealthStore:taskIdentifier:exportedObject:taskUUID:"
+ "interfaceWithProtocol:"
+ "invalid Collection: less than 'count' elements in collection"
+ "isEqual:"
+ "isEqualToDate:"
+ "isEqualToString:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "modificationDate"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "q"
+ "q16@0:8"
+ "raise:format:"
+ "release"
+ "remoteInterface"
+ "remote_setAccepted:agreement:version:completion:"
+ "remote_setAccepted:currentAgreement:completion:"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "self"
+ "setUserDidAccept:agreement:version:completion:"
+ "setUserDidAccept:currentAgreement:completion:"
+ "superclass"
+ "supportsSecureCoding"
+ "v16@?0@\"<HealthAppAnalyticsStoreServerInterface>\"8"
+ "v16@?0@\"NSError\"8"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@\"NSCoder\"16"
+ "v36@0:8B16@\"NSString\"20@?<v@?B@\"NSError\">28"
+ "v36@0:8B16@20@?28"
+ "v44@0:8B16@\"NSString\"20q28@?<v@?B@\"NSError\">36"
+ "v44@0:8B16@20q28@?36"
+ "v8@?0"
+ "version"
+ "zone"

```
