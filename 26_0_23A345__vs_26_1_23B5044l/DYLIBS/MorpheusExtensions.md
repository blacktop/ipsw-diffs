## MorpheusExtensions

> `/System/Library/PrivateFrameworks/MorpheusExtensions.framework/MorpheusExtensions`

```diff

-62.0.0.0.0
-  __TEXT.__text: 0x1f310
-  __TEXT.__auth_stubs: 0xd50
-  __TEXT.__const: 0x7e8
-  __TEXT.__cstring: 0x4f2
-  __TEXT.__swift5_typeref: 0x3d6
-  __TEXT.__swift5_capture: 0x194
-  __TEXT.__constg_swiftt: 0x2e8
-  __TEXT.__swift5_fieldmd: 0x2ac
-  __TEXT.__oslogstring: 0x3
-  __TEXT.__swift5_proto: 0x6c
-  __TEXT.__swift5_types: 0x24
-  __TEXT.__swift5_reflstr: 0x512
+70.0.0.0.0
+  __TEXT.__text: 0x22384
+  __TEXT.__auth_stubs: 0xf60
+  __TEXT.__objc_methlist: 0x1e4
+  __TEXT.__const: 0x880
+  __TEXT.__cstring: 0x669
+  __TEXT.__oslogstring: 0x9f
+  __TEXT.__swift5_typeref: 0x430
+  __TEXT.__swift5_capture: 0x184
+  __TEXT.__constg_swiftt: 0x33c
+  __TEXT.__swift5_fieldmd: 0x2f8
+  __TEXT.__swift5_proto: 0x70
+  __TEXT.__swift5_types: 0x28
+  __TEXT.__swift5_reflstr: 0x587
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_assocty: 0x50
-  __TEXT.__unwind_info: 0x560
-  __TEXT.__eh_frame: 0xfe0
-  __TEXT.__objc_methname: 0x128
-  __DATA_CONST.__got: 0x208
-  __DATA_CONST.__const: 0xd0
-  __DATA_CONST.__objc_classlist: 0x18
+  __TEXT.__unwind_info: 0x610
+  __TEXT.__eh_frame: 0x10e8
+  __TEXT.__objc_classname: 0x2c
+  __TEXT.__objc_methname: 0x43d
+  __TEXT.__objc_methtype: 0x11c
+  __TEXT.__objc_stubs: 0x200
+  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__const: 0xe8
+  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x6a8
-  __AUTH_CONST.__const: 0x1a10
-  __AUTH_CONST.__objc_const: 0x328
-  __AUTH.__data: 0x340
-  __DATA.__data: 0x2e0
-  __DATA.__bss: 0x900
-  __DATA.__common: 0x8
+  __DATA_CONST.__objc_selrefs: 0x208
+  __AUTH_CONST.__auth_got: 0x7b8
+  __AUTH_CONST.__const: 0x1af8
+  __AUTH_CONST.__cfstring: 0x20
+  __AUTH_CONST.__objc_const: 0x708
+  __AUTH.__objc_data: 0xa0
+  __AUTH.__data: 0x400
+  __DATA.__data: 0x3e0
+  __DATA.__bss: 0x990
+  __DATA.__common: 0x20
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/Morpheus.framework/Morpheus
   - /System/Library/PrivateFrameworks/PrivateFederatedLearning.framework/PrivateFederatedLearning

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 234759A8-61E0-363E-86C0-2DC521F552D3
-  Functions: 395
-  Symbols:   257
-  CStrings:  60
+  UUID: AD63E2D0-3338-3C2F-8C69-B9564CD5FA92
+  Functions: 447
+  Symbols:   369
+  CStrings:  161
 
Symbols:
+ +[AnyEvent eventWithData:dataVersion:]
+ +[StreamHelpers eventOfType:jsonDictionary:error:]
+ +[StreamHelpers logger]
+ +[StreamHelpers logger].cold.1
+ +[StreamHelpers lookupStream:]
+ +[StreamHelpers lookupStream:].cold.1
+ +[StreamHelpers lookupStream:].cold.2
+ +[StreamHelpers lookupStreamBase:]
+ -[AnyEvent dataVersion]
+ -[AnyEvent serialize]
+ _BiomeLibraryNode
+ _OBJC_CLASS_$_AnyEvent
+ _OBJC_CLASS_$_NSISO8601DateFormatter
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_StreamHelpers
+ _OBJC_METACLASS_$_AnyEvent
+ _OBJC_METACLASS_$_NSObject
+ _OBJC_METACLASS_$_StreamHelpers
+ __DATA__TtC18MorpheusExtensions11BiomeWriter
+ __IVARS__TtC18MorpheusExtensions11BiomeWriter
+ __METACLASS_DATA__TtC18MorpheusExtensions11BiomeWriter
+ __NSConcreteGlobalBlock
+ __OBJC_$_CLASS_METHODS_AnyEvent
+ __OBJC_$_CLASS_METHODS_StreamHelpers
+ __OBJC_$_CLASS_PROP_LIST_AnyEvent
+ __OBJC_$_CLASS_PROP_LIST_BMStoreData
+ __OBJC_$_INSTANCE_METHODS_AnyEvent
+ __OBJC_$_PROP_LIST_AnyEvent
+ __OBJC_$_PROP_LIST_BMStoreData
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_CLASS_METHODS_BMStoreData
+ __OBJC_$_PROTOCOL_CLASS_METHODS_OPT_BMStoreData
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BMStoreData
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BMStoreData
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BMStoreData
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_BMStoreData
+ __OBJC_CLASS_PROTOCOLS_$_AnyEvent
+ __OBJC_CLASS_RO_$_AnyEvent
+ __OBJC_CLASS_RO_$_StreamHelpers
+ __OBJC_LABEL_PROTOCOL_$_BMStoreData
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_AnyEvent
+ __OBJC_METACLASS_RO_$_StreamHelpers
+ __OBJC_PROTOCOL_$_BMStoreData
+ __OBJC_PROTOCOL_$_NSObject
+ ___23+[StreamHelpers logger]_block_invoke
+ ___CFConstantStringClassReference
+ ___assert_rtn
+ ___block_descriptor_32_e5_v8?0l
+ ___block_literal_global
+ ___swift_allocate_boxed_opaque_existential_0
+ ___swift_allocate_value_buffer
+ ___swift_project_value_buffer
+ __os_log_default
+ __os_log_error_impl
+ __swift_stdlib_strtod_clocale
+ _dispatch_once
+ _logger._framework
+ _logger.onceToken
+ _objc_alloc
+ _objc_claimAutoreleasedReturnValue
+ _objc_enumerationMutation
+ _objc_msgSend$UUIDString
+ _objc_msgSend$allStreams
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$configuration
+ _objc_msgSend$containsObject:
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$firstObject
+ _objc_msgSend$identifier
+ _objc_msgSend$initWithJSONDictionary:error:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$legacyNames
+ _objc_msgSend$logger
+ _objc_msgSend$lookupStream:
+ _objc_msgSend$streamUUID
+ _objc_msgSend$streamWithIdentifier:error:
+ _objc_release_x1
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x3
+ _os_log_create
+ _swift_getObjCClassFromMetadata
+ _swift_getObjectType
+ _swift_unknownObjectRetain
+ _symbolic SDySSypG
+ _symbolic SDy_____ypG s11AnyHashableV
+ _symbolic So8BMSourceCyyXlG
+ _symbolic _____ 18MorpheusExtensions11BiomeWriterC
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y_____ypG s18_DictionaryStorageC s11AnyHashableV
+ _symbolic yXlXp
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_MorpheusExtensions
CStrings:
+ "#16@0:8"
+ "+[AnyEvent eventWithData:dataVersion:]"
+ "-[AnyEvent dataVersion]"
+ "-[AnyEvent serialize]"
+ "0"
+ ":"
+ "@\"NSData\"16@0:8"
+ "@\"NSDictionary\"16@0:8"
+ "@\"NSString\"16@0:8"
+ "@16@0:8"
+ "@24@0:8:16"
+ "@24@0:8@16"
+ "@28@0:8@\"NSData\"16I24"
+ "@28@0:8@16I24"
+ "@32@0:8:16@24"
+ "@40@0:8#16@24^@32"
+ "@40@0:8:16@24@32"
+ "AnyEvent"
+ "B16@0:8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "BMSQLResultSet.as_records"
+ "BMStoreData"
+ "I16@0:8"
+ "Invalid stream ID %@"
+ "MorpheusExtension"
+ "MorpheusExtensions"
+ "NSObject"
+ "Q16@0:8"
+ "StreamHelpers"
+ "StreamHelpers.m"
+ "T#,R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TI,?,R,N"
+ "TI,R,N"
+ "TQ,R"
+ "UUIDString"
+ "Unable to convert %s into Date"
+ "Unable to convert %s into Double"
+ "Vv16@0:8"
+ "WARNING: '%@' is the legacy name for '%@'"
+ "^{_NSZone=}16@0:8"
+ "_TtC18MorpheusExtensions11BiomeWriter"
+ "allStreams"
+ "autorelease"
+ "biome.database.Database"
+ "biome.writer.BiomeWriter"
+ "class"
+ "com.apple.priml.pfl.Morpheus"
+ "componentsSeparatedByString:"
+ "configuration"
+ "conformsToProtocol:"
+ "containsObject:"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "dataVersion"
+ "dateFromString:"
+ "debugDescription"
+ "description"
+ "eventClass"
+ "eventOfType:jsonDictionary:error:"
+ "eventWithData:dataVersion:"
+ "firstObject"
+ "hash"
+ "identifier"
+ "init"
+ "initWithJSONDictionary:error:"
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "json"
+ "jsonDict"
+ "latestDataVersion"
+ "legacyNames"
+ "logger"
+ "lookupStream:"
+ "lookupStreamBase:"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "release"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "self"
+ "sendEvent:"
+ "sendEvent:date:"
+ "serialize"
+ "source"
+ "streamUUID"
+ "streamWithIdentifier:error:"
+ "superclass"
+ "v8@?0"
+ "zone"

```
