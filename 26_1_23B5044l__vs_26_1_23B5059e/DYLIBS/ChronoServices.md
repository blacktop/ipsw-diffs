## ChronoServices

> `/System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices`

```diff

-664.1.12.1.100
-  __TEXT.__text: 0xe88e4
-  __TEXT.__auth_stubs: 0x2680
-  __TEXT.__objc_methlist: 0x7c84
+664.1.20.0.0
+  __TEXT.__text: 0xe9e4c
+  __TEXT.__auth_stubs: 0x26b0
+  __TEXT.__objc_methlist: 0x7e14
   __TEXT.__const: 0x66d8
-  __TEXT.__gcc_except_tab: 0xaab0
-  __TEXT.__cstring: 0x78d4
-  __TEXT.__oslogstring: 0x463e
+  __TEXT.__gcc_except_tab: 0xab30
+  __TEXT.__cstring: 0x79c4
+  __TEXT.__oslogstring: 0x469e
   __TEXT.__dlopen_cstrs: 0x182
-  __TEXT.__swift5_typeref: 0x2288
-  __TEXT.__swift5_capture: 0xa40
-  __TEXT.__swift5_reflstr: 0x17d5
+  __TEXT.__swift5_typeref: 0x228c
+  __TEXT.__swift5_capture: 0xa58
+  __TEXT.__swift5_reflstr: 0x1805
   __TEXT.__swift5_assocty: 0x470
-  __TEXT.__constg_swiftt: 0x29a4
-  __TEXT.__swift5_fieldmd: 0x1564
+  __TEXT.__constg_swiftt: 0x29c4
+  __TEXT.__swift5_fieldmd: 0x157c
   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_proto: 0x4d0
   __TEXT.__swift5_types: 0x1d8

   __TEXT.__swift_as_entry: 0x54
   __TEXT.__swift_as_ret: 0x54
   __TEXT.__swift5_protos: 0x44
-  __TEXT.__unwind_info: 0x6588
+  __TEXT.__unwind_info: 0x6600
   __TEXT.__eh_frame: 0x3160
   __TEXT.__objc_classname: 0x13b1
-  __TEXT.__objc_methname: 0xdce2
-  __TEXT.__objc_methtype: 0x23e1
-  __TEXT.__objc_stubs: 0x61c0
-  __DATA_CONST.__got: 0xa58
-  __DATA_CONST.__const: 0x1d08
-  __DATA_CONST.__objc_classlist: 0x5c8
+  __TEXT.__objc_methname: 0xde1f
+  __TEXT.__objc_methtype: 0x2463
+  __TEXT.__objc_stubs: 0x61e0
+  __DATA_CONST.__got: 0xa68
+  __DATA_CONST.__const: 0x1d38
+  __DATA_CONST.__objc_classlist: 0x5d0
   __DATA_CONST.__objc_nlclslist: 0x8
-  __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x250
+  __DATA_CONST.__objc_catlist: 0x20
+  __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f40
-  __DATA_CONST.__objc_protorefs: 0xe8
+  __DATA_CONST.__objc_selrefs: 0x2f90
+  __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x328
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x1358
-  __AUTH_CONST.__const: 0x54b8
-  __AUTH_CONST.__cfstring: 0x4ea0
-  __AUTH_CONST.__objc_const: 0x1ee60
+  __AUTH_CONST.__auth_got: 0x1370
+  __AUTH_CONST.__const: 0x5548
+  __AUTH_CONST.__cfstring: 0x4ec0
+  __AUTH_CONST.__objc_const: 0x1f098
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH.__objc_data: 0x3008
-  __AUTH.__data: 0x2328
-  __DATA.__objc_ivar: 0x720
-  __DATA.__data: 0x2d20
-  __DATA.__bss: 0x8ab0
+  __AUTH.__objc_data: 0x3078
+  __AUTH.__data: 0x2388
+  __DATA.__objc_ivar: 0x728
+  __DATA.__data: 0x2d50
+  __DATA.__bss: 0x8aa0
   __DATA.__common: 0x150
   __DATA_DIRTY.__objc_data: 0xcd0
   __DATA_DIRTY.__data: 0x278

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BBB334C8-5E16-3B33-A895-8EA54574975A
-  Functions: 6643
-  Symbols:   12269
-  CStrings:  4945
+  UUID: 14B942AC-C0B5-3B84-A851-1430F6277398
+  Functions: 6721
+  Symbols:   12329
+  CStrings:  4972
 
Symbols:
+ +[NSProcessInfo(ChronoServices) chs_isWatchFacesWidgetRendererProcess]
+ +[NSProcessInfo(ChronoServices) chs_isWatchFacesWidgetRendererProcess].cold.1
+ -[CHSChronoServicesConnection acquireLifetimeAssertionForWidget:metrics:prewarm:timeout:completion:]
+ -[CHSMutableWidgetConfiguration setExpirationTimeout:]
+ -[CHSToolServiceConnection subscribeToTaskServiceStateWithDelegate:completion:]
+ -[CHSToolServiceConnection taskServiceStateDidChange:]
+ -[CHSWidgetConfiguration expirationTimeout]
+ GCC_except_table85
+ GCC_except_table87
+ OBJC_IVAR_$_CHSWidgetConfiguration._expirationTimeout
+ _OBJC_CLASS_$_CHSMutableControlConfiguration
+ _OBJC_IVAR_$_CHSToolServiceConnection._calloutQueue
+ _OBJC_METACLASS_$_CHSMutableControlConfiguration
+ __DATA_CHSMutableControlConfiguration
+ __INSTANCE_METHODS_CHSMutableControlConfiguration
+ __METACLASS_DATA_CHSMutableControlConfiguration
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSProcessInfo_$_ChronoServices
+ __OBJC_$_CATEGORY_NSProcessInfo_$_ChronoServices
+ __OBJC_$_CLASS_PROP_LIST_NSProcessInfo_$_ChronoServices
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CHSToolServiceClientInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CHSToolServiceClient
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CHSToolServiceClient
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CHSToolServiceClientInterface
+ __PROPERTIES_CHSMutableControlConfiguration
+ __PROTOCOLS_CHSWidgetRelevanceService.48
+ __PROTOCOLS__TtCE14ChronoServicesCSo25CHSWidgetRelevanceService16ConnectionClient.52
+ ___100-[CHSChronoServicesConnection acquireLifetimeAssertionForWidget:metrics:prewarm:timeout:completion:]_block_invoke
+ ___100-[CHSChronoServicesConnection acquireLifetimeAssertionForWidget:metrics:prewarm:timeout:completion:]_block_invoke.cold.1
+ ___34-[CHSWidgetConfiguration isEqual:]_block_invoke_6
+ ___51-[CHSToolServiceConnection _queue_createConnection]_block_invoke.42
+ ___54-[CHSToolServiceConnection taskServiceStateDidChange:]_block_invoke
+ ___54-[CHSToolServiceConnection taskServiceStateDidChange:]_block_invoke_2
+ ___70+[NSProcessInfo(ChronoServices) chs_isWatchFacesWidgetRendererProcess]_block_invoke
+ ___79-[CHSToolServiceConnection subscribeToTaskServiceStateWithDelegate:completion:]_block_invoke
+ ___79-[CHSToolServiceConnection subscribeToTaskServiceStateWithDelegate:completion:]_block_invoke.cold.1
+ ___block_descriptor_80_ea8_32s40s48s56s64s72bs_e5_v8?0ls32l8s72l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.44
+ __dispatch_queue_attr_concurrent
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_ChronoServices
+ _block_copy_helper.105
+ _block_copy_helper.117
+ _block_copy_helper.120
+ _block_copy_helper.44
+ _block_copy_helper.63
+ _block_copy_helper.69
+ _block_copy_helper.86
+ _block_copy_helper.93
+ _block_copy_helper.99
+ _block_descriptor.101
+ _block_descriptor.107
+ _block_descriptor.119
+ _block_descriptor.122
+ _block_descriptor.46
+ _block_descriptor.65
+ _block_descriptor.71
+ _block_descriptor.88
+ _block_descriptor.95
+ _block_destroy_helper.100
+ _block_destroy_helper.106
+ _block_destroy_helper.118
+ _block_destroy_helper.121
+ _block_destroy_helper.45
+ _block_destroy_helper.64
+ _block_destroy_helper.70
+ _block_destroy_helper.87
+ _block_destroy_helper.94
+ _chs_isWatchFacesWidgetRendererProcess.isWatchFacesWidgetRendererProcess
+ _chs_isWatchFacesWidgetRendererProcess.onceToken
+ _keypath_get.15Tm
+ _keypath_set.96Tm
+ _objc_msgSend$acquireLifetimeAssertionForWidget:metrics:prewarm:timeout:completion:
+ _objc_msgSend$chs_isWatchFacesWidgetRendererProcess
+ _objc_msgSend$doubleValue
+ _objc_msgSend$subscribeToTaskServiceStateWithCompletion:
+ _objc_msgSend$taskServiceStateDidChange:
+ _objectdestroy.91Tm
+ _symbolic Sd
- +[CHSWidgetMetrics use32BitFloats].cold.1
- -[CHSChronoServicesConnection acquireLifetimeAssertionForWidget:metrics:completion:]
- GCC_except_table68
- __PROTOCOLS_CHSWidgetRelevanceService.45
- __PROTOCOLS__TtCE14ChronoServicesCSo25CHSWidgetRelevanceService16ConnectionClient.49
- ___34+[CHSWidgetMetrics use32BitFloats]_block_invoke
- ___51-[CHSToolServiceConnection _queue_createConnection]_block_invoke.36
- ___84-[CHSChronoServicesConnection acquireLifetimeAssertionForWidget:metrics:completion:]_block_invoke
- ___84-[CHSChronoServicesConnection acquireLifetimeAssertionForWidget:metrics:completion:]_block_invoke.cold.1
- ___block_literal_global.35
- _block_copy_helper.101
- _block_copy_helper.107
- _block_copy_helper.110
- _block_copy_helper.57
- _block_copy_helper.76
- _block_copy_helper.83
- _block_copy_helper.89
- _block_copy_helper.95
- _block_descriptor.103
- _block_descriptor.109
- _block_descriptor.112
- _block_descriptor.59
- _block_descriptor.78
- _block_descriptor.85
- _block_descriptor.91
- _block_descriptor.97
- _block_destroy_helper.102
- _block_destroy_helper.108
- _block_destroy_helper.111
- _block_destroy_helper.58
- _block_destroy_helper.77
- _block_destroy_helper.84
- _block_destroy_helper.90
- _block_destroy_helper.96
- _keypath_get.41Tm
- _keypath_get_selector_controlItems
- _keypath_set.94Tm
- _objc_msgSend$acquireLifetimeAssertionForWidget:metrics:completion:
- _objc_msgSend$automaticallyOrphaned
- _objc_msgSend$rateLimitPolicies
- _objc_msgSend$replicationPredicate
- _objectdestroy.81Tm
- _use32BitFloats.__use32BitFloats
- _use32BitFloats.onceToken
CStrings:
+ "CHSMutableControlConfiguration"
+ "T@\"CHSRemoteDevicePredicate\",N,&"
+ "Td,N"
+ "Td,N,R"
+ "Td,R,N,V_expirationTimeout"
+ "Tq,N"
+ "Unable to subscribe to task service state; unable to obtain the remote target"
+ "Vv24@0:8@\"NSDictionary\"16"
+ "Vv24@0:8@?<v@?@\"NSDictionary\"@\"BSAction\"@\"NSError\">16"
+ "Vv56@0:8@\"CHSWidget\"16@\"CHSWidgetMetrics\"24@\"NSNumber\"32@\"NSNumber\"40@?<v@?@\"BSAction\"@\"NSError\">48"
+ "_controlItems"
+ "_expirationTimeout"
+ "_secondHandFPS"
+ "acquireLifetimeAssertionForWidget:metrics:prewarm:timeout:completion:"
+ "chs_isWatchFacesWidgetRendererProcess"
+ "com.apple.chronoservices.CHSChronoServicesToolConnection.callout"
+ "doubleValue"
+ "expirationTimeout"
+ "initWithDouble:"
+ "initWithItem:"
+ "setExpirationTimeout:"
+ "setLocation:"
+ "subscribeToTaskServiceStateWithCompletion:"
+ "subscribeToTaskServiceStateWithDelegate:completion:"
+ "taskServiceStateDidChange:"
+ "v24@?0@\"<BSInvalidatable>\"8@\"NSError\"16"
+ "v52@0:8@16@24B32d36@?44"
+ "v56@0:8@16@24@32@40@?48"
+ "xpc: acquireLifetimeAssertionForWidget:metrics:prewarm:timeout:completion:"
- "<Unknown CHSControlConfiguration>"
- "T@\"CHSRemoteDevicePredicate\",N,R,VreplicationPredicate"
- "TB,N,R,VautomaticallyOrphaned"
- "Tq,N,R,Vlocation"
- "Vv40@0:8@\"CHSWidget\"16@\"CHSWidgetMetrics\"24@?<v@?@\"BSAction\"@\"NSError\">32"
- "acquireLifetimeAssertionForWidget:metrics:completion:"
- "xpc: acquireLifetimeAssertionForWidget:metrics:completion:"

```
