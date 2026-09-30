## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-774.14.0.0.0
-  __TEXT.__text: 0x5e054
-  __TEXT.__auth_stubs: 0xff0
-  __TEXT.__objc_methlist: 0x625c
-  __TEXT.__const: 0x41a
+774.19.0.0.0
+  __TEXT.__text: 0x5f0f0
+  __TEXT.__auth_stubs: 0x1000
+  __TEXT.__objc_methlist: 0x63a4
+  __TEXT.__const: 0x45a
   __TEXT.__gcc_except_tab: 0xa20
-  __TEXT.__oslogstring: 0x660a
-  __TEXT.__cstring: 0x54ad
+  __TEXT.__oslogstring: 0x67ba
+  __TEXT.__cstring: 0x54fd
   __TEXT.__dlopen_cstrs: 0x15e
-  __TEXT.__swift5_typeref: 0x7e
-  __TEXT.__constg_swiftt: 0xd8
-  __TEXT.__swift5_reflstr: 0x23
-  __TEXT.__swift5_fieldmd: 0x28
-  __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_types: 0x10
+  __TEXT.__swift5_typeref: 0x8a
+  __TEXT.__constg_swiftt: 0xf8
+  __TEXT.__swift5_reflstr: 0x4a
+  __TEXT.__swift5_fieldmd: 0x5c
+  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x10
-  __TEXT.__unwind_info: 0x1ca8
+  __TEXT.__unwind_info: 0x1cf8
   __TEXT.__eh_frame: 0x80
-  __TEXT.__objc_classname: 0xbc3
-  __TEXT.__objc_methname: 0x11161
-  __TEXT.__objc_methtype: 0x2613
-  __TEXT.__objc_stubs: 0x9680
-  __DATA_CONST.__got: 0x7b8
-  __DATA_CONST.__const: 0x1f58
-  __DATA_CONST.__objc_classlist: 0x258
+  __TEXT.__objc_classname: 0xc13
+  __TEXT.__objc_methname: 0x11361
+  __TEXT.__objc_methtype: 0x26d3
+  __TEXT.__objc_stubs: 0x97e0
+  __DATA_CONST.__got: 0x7c0
+  __DATA_CONST.__const: 0x1fd0
+  __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x170
+  __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3560
-  __DATA_CONST.__objc_protorefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_selrefs: 0x35d0
+  __DATA_CONST.__objc_protorefs: 0x108
+  __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x808
-  __AUTH_CONST.__const: 0x1a28
-  __AUTH_CONST.__cfstring: 0x57c0
-  __AUTH_CONST.__objc_const: 0xfa10
+  __AUTH_CONST.__auth_got: 0x810
+  __AUTH_CONST.__const: 0x1b08
+  __AUTH_CONST.__cfstring: 0x5800
+  __AUTH_CONST.__objc_const: 0x105c0
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x11d8
+  __AUTH.__objc_data: 0x1280
   __AUTH.__data: 0xb8
-  __DATA.__objc_ivar: 0x77c
-  __DATA.__data: 0x10c0
-  __DATA.__bss: 0x690
+  __DATA.__objc_ivar: 0x78c
+  __DATA.__data: 0x1130
+  __DATA.__bss: 0x6a0
   __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__bss: 0x108
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4C5B357D-0718-3D36-9334-11B592857ACD
-  Functions: 2918
-  Symbols:   9502
-  CStrings:  5052
+  UUID: 7601D892-7C2B-3A0D-88E5-7D31D93DE974
+  Functions: 2962
+  Symbols:   9644
+  CStrings:  5094
 
Symbols:
+ +[CARVehicleStatisticsSession _vehicleStatisticsServiceInterface]
+ +[CARVehicleStatisticsSession _vehicleStatisticsServiceInterface].cold.1
+ -[CARScreenInfo(CRDisplayScaling) isViewAreaPixelSizeAcceptable:]
+ -[CARStatisticsObservation .cxx_destruct]
+ -[CARStatisticsObservation dealloc]
+ -[CARStatisticsObservation didReceiveStatistics:]
+ -[CARStatisticsObservation handler]
+ -[CARStatisticsObservation setHandler:]
+ -[CARStatisticsObservation setStore:]
+ -[CARStatisticsObservation store]
+ -[CARVehicleStatisticsSession .cxx_destruct]
+ -[CARVehicleStatisticsSession _removeObservation:]
+ -[CARVehicleStatisticsSession _removeObservation:].cold.1
+ -[CARVehicleStatisticsSession _setupConnection]
+ -[CARVehicleStatisticsSession _xpcFetchWithServiceBlock:errorHandler:]
+ -[CARVehicleStatisticsSession _xpcFetchWithServiceBlock:errorHandler:].cold.1
+ -[CARVehicleStatisticsSession connection]
+ -[CARVehicleStatisticsSession currentObservation]
+ -[CARVehicleStatisticsSession dealloc]
+ -[CARVehicleStatisticsSession init]
+ -[CARVehicleStatisticsSession observeStatistics:completion:]
+ -[CARVehicleStatisticsSession observeStatistics:completion:].cold.1
+ -[CARVehicleStatisticsSession setConnection:]
+ -[CARVehicleStatisticsSession setCurrentObservation:]
+ _CARVehicleStatisticsSessionErrorDomain
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_CARStatisticsObservation
+ _OBJC_CLASS_$_CARVehicleStatisticsSession
+ _OBJC_IVAR_$_CARStatisticsObservation._handler
+ _OBJC_IVAR_$_CARStatisticsObservation._store
+ _OBJC_IVAR_$_CARVehicleStatisticsSession._connection
+ _OBJC_IVAR_$_CARVehicleStatisticsSession._currentObservation
+ _OBJC_METACLASS_$_CARStatisticsObservation
+ _OBJC_METACLASS_$_CARVehicleStatisticsSession
+ __OBJC_$_CLASS_METHODS_CARVehicleStatisticsSession
+ __OBJC_$_INSTANCE_METHODS_CARStatisticsObservation
+ __OBJC_$_INSTANCE_METHODS_CARVehicleStatisticsSession
+ __OBJC_$_INSTANCE_VARIABLES_CARStatisticsObservation
+ __OBJC_$_INSTANCE_VARIABLES_CARVehicleStatisticsSession
+ __OBJC_$_PROP_LIST_CARStatisticsObservation
+ __OBJC_$_PROP_LIST_CARVehicleStatisticsSession
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRVehicleStatisticsObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRVehicleStatisticsObserver
+ __OBJC_$_PROTOCOL_REFS_CRVehicleStatisticsObserver
+ __OBJC_CLASS_PROTOCOLS_$_CARStatisticsObservation
+ __OBJC_CLASS_RO_$_CARStatisticsObservation
+ __OBJC_CLASS_RO_$_CARVehicleStatisticsSession
+ __OBJC_LABEL_PROTOCOL_$_CRVehicleStatisticsObserver
+ __OBJC_METACLASS_RO_$_CARStatisticsObservation
+ __OBJC_METACLASS_RO_$_CARVehicleStatisticsSession
+ __OBJC_PROTOCOL_$_CRVehicleStatisticsObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CRVehicleStatisticsObserver
+ ___49-[CARStatisticsObservation didReceiveStatistics:]_block_invoke
+ ___50-[CARVehicleStatisticsSession _removeObservation:]_block_invoke
+ ___50-[CARVehicleStatisticsSession _removeObservation:]_block_invoke_2
+ ___50-[CARVehicleStatisticsSession _removeObservation:]_block_invoke_2.cold.1
+ ___60-[CARVehicleStatisticsSession observeStatistics:completion:]_block_invoke
+ ___60-[CARVehicleStatisticsSession observeStatistics:completion:]_block_invoke.213
+ ___60-[CARVehicleStatisticsSession observeStatistics:completion:]_block_invoke.213.cold.1
+ ___60-[CARVehicleStatisticsSession observeStatistics:completion:]_block_invoke_2
+ ___60-[CARVehicleStatisticsSession observeStatistics:completion:]_block_invoke_2.cold.1
+ ___60-[CARVehicleStatisticsSession observeStatistics:completion:]_block_invoke_2.cold.2
+ ___65+[CARVehicleStatisticsSession _vehicleStatisticsServiceInterface]_block_invoke
+ ___70-[CARVehicleStatisticsSession _xpcFetchWithServiceBlock:errorHandler:]_block_invoke
+ ___70-[CARVehicleStatisticsSession _xpcFetchWithServiceBlock:errorHandler:]_block_invoke.cold.1
+ ___CRCollectCarPlayDiagnostics_block_invoke.168
+ ___CRCollectVehicleLogs_block_invoke.172
+ ___CRIsPreflightThemeAssetEnabled_block_invoke.176
+ ___CRIsPreflightThemeAssetEnabled_block_invoke.176.cold.1
+ ___CRPostBannerToPhone_block_invoke.160
+ ___CRServiceConnectionPerform_block_invoke.124
+ ___CRSetPreflightThemeAssetEnabled_block_invoke.186
+ ___CRSetPreflightThemeAssetEnabled_block_invoke.186.cold.1
+ ___block_descriptor_32_e27_v16?0"<CRCarKitService>"8l
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e27_v16?0"<CRCarKitService>"8ls32l8s48l8s40l8
+ ___block_literal_global.167
+ ___block_literal_global.171
+ ___block_literal_global.185
+ ___block_literal_global.201
+ ___block_literal_global.206
+ ___block_literal_global.207
+ ___swift_memcpy16_8
+ ___swift_noop_void_return
+ __vehicleStatisticsServiceInterface.__interface
+ __vehicleStatisticsServiceInterface.onceToken
+ _objc_msgSend$_removeObservation:
+ _objc_msgSend$_vehicleStatisticsServiceInterface
+ _objc_msgSend$currentObservation
+ _objc_msgSend$handler
+ _objc_msgSend$minAcceptableViewAreaSize
+ _objc_msgSend$setCurrentObservation:
+ _objc_msgSend$setHandler:
+ _objc_msgSend$setInterface:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setStore:
+ _objc_msgSend$setVehicleStatisticsObserver:reply:
+ _objc_msgSend$store
+ _symbolic _____ 12CoreGraphics7CGFloatV
+ _symbolic _____ So6CGSizeV
+ _type_layout_string So6CGSizeV
- ___CRCollectCarPlayDiagnostics_block_invoke.166
- ___CRCollectVehicleLogs_block_invoke.170
- ___CRIsPreflightThemeAssetEnabled_block_invoke.174
- ___CRIsPreflightThemeAssetEnabled_block_invoke.174.cold.1
- ___CRPostBannerToPhone_block_invoke.158
- ___CRServiceConnectionPerform_block_invoke.122
- ___CRSetPreflightThemeAssetEnabled_block_invoke.184
- ___CRSetPreflightThemeAssetEnabled_block_invoke.184.cold.1
- ___block_literal_global.169
- ___block_literal_global.173
- ___block_literal_global.183
- ___block_literal_global.199
CStrings:
+ "@\"CARStatisticsObservation\""
+ "@\"CARVehicleStatisticsSession\""
+ "@32@0:8@?16@?24"
+ "An observation handler is required"
+ "B32@0:8{CGSize=dd}16"
+ "CARStatisticsObservation"
+ "CARVehicleStatisticsSession"
+ "CARVehicleStatisticsSession: Connecting to CarKit service"
+ "CARVehicleStatisticsSession: Failed to remove observer: %@"
+ "CARVehicleStatisticsSession: Failed to start observation: %@"
+ "CARVehicleStatisticsSession: Removing observation"
+ "CARVehicleStatisticsSession: Successfully started observation"
+ "CARVehicleStatisticsSession: XPC error: %@"
+ "CARVehicleStatisticsSession: XPC service error: %@"
+ "CARVehicleStatisticsSession: handler is required"
+ "CARVehicleStatisticsSessionErrorDomain"
+ "CRVehicleStatisticsObserver"
+ "T@\"CARStatisticsObservation\",&,N,V_currentObservation"
+ "T@\"CARVehicleStatisticsSession\",W,N,V_store"
+ "T@?,C,N,V_handler"
+ "T{CGSize=dd},N,R,VminAcceptableViewAreaSize"
+ "_currentObservation"
+ "_handler"
+ "_removeObservation:"
+ "_store"
+ "_vehicleStatisticsServiceInterface"
+ "currentObservation"
+ "didReceiveStatistics:"
+ "handler"
+ "isViewAreaPixelSizeAcceptable:"
+ "minAcceptableViewAreaSize"
+ "observeStatistics:completion:"
+ "setCurrentObservation:"
+ "setHandler:"
+ "setInterface:forSelector:argumentIndex:ofReply:"
+ "setStore:"
+ "setVehicleStatisticsObserver:reply:"
+ "store"
+ "v32@0:8@\"<CRVehicleStatisticsObserver>\"16@?<v@?B@\"NSError\">24"
+ "{CGSize=dd}"

```
