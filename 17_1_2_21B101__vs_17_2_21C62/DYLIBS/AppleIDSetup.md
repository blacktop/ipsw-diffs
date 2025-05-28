## AppleIDSetup

> `/System/Library/PrivateFrameworks/AppleIDSetup.framework/AppleIDSetup`

```diff

-23.0.0.0.0
-  __TEXT.__text: 0xfd68
-  __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_methlist: 0x1e8
-  __TEXT.__const: 0xa52
-  __TEXT.__cstring: 0xe70
-  __TEXT.__constg_swiftt: 0x724
-  __TEXT.__swift5_typeref: 0x50f
-  __TEXT.__swift5_fieldmd: 0x3b8
-  __TEXT.__swift5_types: 0x48
-  __TEXT.__swift5_reflstr: 0x367
+23.2.0.0.0
+  __TEXT.__text: 0x121ec
+  __TEXT.__auth_stubs: 0xb30
+  __TEXT.__objc_methlist: 0x220
+  __TEXT.__const: 0xc22
+  __TEXT.__cstring: 0x1070
+  __TEXT.__oslogstring: 0x8b
+  __TEXT.__constg_swiftt: 0x820
+  __TEXT.__swift5_typeref: 0x585
+  __TEXT.__swift5_fieldmd: 0x404
+  __TEXT.__swift5_types: 0x54
+  __TEXT.__swift5_reflstr: 0x397
   __TEXT.__swift5_capture: 0xf8
-  __TEXT.__swift5_protos: 0x1c
-  __TEXT.__swift5_proto: 0x4c
-  __TEXT.__swift5_assocty: 0x48
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x6b8
-  __TEXT.__eh_frame: 0x970
-  __TEXT.__objc_classname: 0x21
-  __TEXT.__objc_methname: 0x5b1
-  __TEXT.__objc_methtype: 0xeb
-  __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x210
-  __DATA_CONST.__objc_classlist: 0x68
-  __DATA_CONST.__objc_protolist: 0x50
+  __TEXT.__swift5_protos: 0x24
+  __TEXT.__swift5_proto: 0x60
+  __TEXT.__swift5_assocty: 0x60
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__unwind_info: 0x12fc
+  __TEXT.__eh_frame: 0xb58
+  __TEXT.__objc_classname: 0x5b
+  __TEXT.__objc_methname: 0x787
+  __TEXT.__objc_methtype: 0x167
+  __TEXT.__objc_stubs: 0xa0
+  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__const: 0x258
+  __DATA_CONST.__objc_classlist: 0x80
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1200
-  __DATA_CONST.__objc_selrefs: 0x1e8
-  __AUTH_CONST.__const: 0x730
-  __AUTH_CONST.__auth_ptr: 0x30
-  __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__auth_got: 0x518
-  __AUTH.__data: 0x640
-  __AUTH.__objc_data: 0x738
-  __DATA.__objc_protorefs: 0x38
-  __DATA.__objc_classrefs: 0x60
+  __DATA_CONST.__objc_const: 0x1760
+  __DATA_CONST.__objc_selrefs: 0x240
+  __AUTH_CONST.__const: 0x800
+  __AUTH_CONST.__objc_const: 0xd0
+  __AUTH_CONST.__auth_ptr: 0x38
+  __AUTH_CONST.__auth_got: 0x5a0
+  __AUTH.__objc_data: 0x788
+  __AUTH.__data: 0x7a0
+  __DATA.__objc_protorefs: 0x40
+  __DATA.__objc_classrefs: 0x80
   __DATA.__objc_data: 0xb0
-  __DATA.__data: 0x4f0
-  __DATA.__common: 0x60
-  __DATA.__bss: 0x600
+  __DATA.__data: 0x590
+  __DATA.__bss: 0x790
+  __DATA.__common: 0x68
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
-  - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
+  - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP
   - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 590
-  Symbols:   425
-  CStrings:  220
+  Functions: 661
+  Symbols:   495
+  CStrings:  260
 
Symbols:
+ +[AISChildSetupBiomeEventFactory biomeEventWithIsNewChildAccount:startDate:endDate:completedSetup:lastViewedScreen:appUsage:askToBuy:commSafety:screenDistance:age:flowType:]
+ +[AISChildSetupBiomeEventFactory biomeEventWithIsNewChildAccount:startDate:endDate:completedSetup:lastViewedScreen:appUsage:askToBuy:commSafety:screenDistance:age:flowType:].cold.1
+ +[AISChildSetupBiomeEventFactory log]
+ +[BMStreams(ForwardDeclare) ais_appleIDChildSetupSource]
+ +[BMStreams(ForwardDeclare) ais_appleIDChildSetupSource].cold.1
+ _BiomeLibrary
+ _OBJC_CLASS_$_AISChildSetupBiomeEventFactory
+ _OBJC_CLASS_$_BMAppleIDChildSetup
+ _OBJC_CLASS_$_BMStreams
+ _OBJC_CLASS_$_FAFetchFamilyCircleRequest
+ _OBJC_METACLASS_$_AISChildSetupBiomeEventFactory
+ __DATA__TtC12AppleIDSetup20FamilyCircleProvider
+ __DATA__TtC12AppleIDSetup8AISBiome
+ __METACLASS_DATA__TtC12AppleIDSetup20FamilyCircleProvider
+ __METACLASS_DATA__TtC12AppleIDSetup8AISBiome
+ __NSConcreteGlobalBlock
+ __OBJC_$_CATEGORY_BMStreams_$_ForwardDeclare
+ __OBJC_$_CLASS_METHODS_AISChildSetupBiomeEventFactory
+ __OBJC_$_CLASS_METHODS_BMStreams(ForwardDeclare)
+ __OBJC_$_PROP_LIST_BMStoreData
+ __OBJC_$_PROTOCOL_CLASS_METHODS_BMStoreData
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BMStoreData
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BMStoreData
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BMStoreData
+ __OBJC_$_PROTOCOL_REFS_BMStoreData
+ __OBJC_CLASS_RO_$_AISChildSetupBiomeEventFactory
+ __OBJC_LABEL_PROTOCOL_$_BMStoreData
+ __OBJC_METACLASS_RO_$_AISChildSetupBiomeEventFactory
+ __OBJC_PROTOCOL_$_BMStoreData
+ ___37+[AISChildSetupBiomeEventFactory log]_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_literal_global
+ __os_log_debug_impl
+ _associated conformance 12AppleIDSetup24AISAppleIDSignInFlowTypeOSHAASQ
+ _dispatch_once
+ _log.log
+ _log.onceToken
+ _objc_alloc
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$AppleID
+ _objc_msgSend$ChildSetup
+ _objc_msgSend$initWithIsNewChildAccount:startDate:endDate:completedSetup:lastViewedScreen:appUsage:askToBuy:commSafety:screenDistance:age:flowType:
+ _objc_msgSend$log
+ _objc_msgSend$source
+ _objc_release_x1
+ _objc_release_x26
+ _objc_retain_x1
+ _objc_retain_x22
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x27
+ _os_log_create
+ _swift_dynamicCastObjCProtocolConditional
+ _symbolic $s12AppleIDSetup16AISBiomeProtocolP
+ _symbolic $s12AppleIDSetup28FamilyCircleProviderProtocolP
+ _symbolic _____ 12AppleIDSetup20FamilyCircleProviderC
+ _symbolic _____ 12AppleIDSetup24AISAppleIDSignInFlowTypeO
+ _symbolic _____ 12AppleIDSetup8AISBiomeC
+ _symbolic _____Sg 12AppleIDSetup24AISAppleIDSignInFlowTypeO
CStrings:
+ "@\"NSData\"16@0:8"
+ "@\"NSDictionary\"16@0:8"
+ "@104@0:8@16@24@32@40q48@56@64@72@80@88q96"
+ "@28@0:8@\"NSData\"16I24"
+ "@28@0:8@16I24"
+ "AISBiomeController biomeEvent is not the correct type"
+ "AISBiomeController failed to get biome source"
+ "AISBiomeController wrote biome event for child setup"
+ "AISBiomeEventProvider childMember == nil. This should not happen"
+ "AISBiomeEventProvider error fetching family %@"
+ "AISBiomeEventProvider setup aborted not fetching family"
+ "AISChildSetupBiomeEventFactory"
+ "AISChildSetupBiomeEventFactory - Creating BMAppleIDChildSetup biome event"
+ "AISChildSetupBiomeEventFactory - Loaded appleIDChildSetup stream"
+ "AppleID"
+ "BMStoreData"
+ "ChildSetup"
+ "ForwardDeclare"
+ "I16@0:8"
+ "T@\"BMSource\",R"
+ "TI,R,N"
+ "_TtC12AppleIDSetup20FamilyCircleProvider"
+ "_TtC12AppleIDSetup8AISBiome"
+ "age"
+ "ais_appleIDChildSetupSource"
+ "biome"
+ "biomeEventWithIsNewChildAccount:startDate:endDate:completedSetup:lastViewedScreen:appUsage:askToBuy:commSafety:screenDistance:age:flowType:"
+ "dataVersion"
+ "eventWithData:dataVersion:"
+ "flowType"
+ "initWithIsNewChildAccount:startDate:endDate:completedSetup:lastViewedScreen:appUsage:askToBuy:commSafety:screenDistance:age:flowType:"
+ "json"
+ "jsonDict"
+ "lastViewedScreen"
+ "log"
+ "me"
+ "sendEvent:"
+ "serialize"
+ "source"
+ "startRequestWithCompletionHandler:"
+ "v24@?0@\"FAFamilyCircle\"8@\"NSError\"16"
- "lasViewedSrceen"

```
