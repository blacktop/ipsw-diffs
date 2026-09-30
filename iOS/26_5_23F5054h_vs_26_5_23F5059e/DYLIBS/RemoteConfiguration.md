## RemoteConfiguration

> `/System/Library/PrivateFrameworks/RemoteConfiguration.framework/RemoteConfiguration`

```diff

-400.0.0.0.0
-  __TEXT.__text: 0x2e9e8
+401.0.0.0.0
+  __TEXT.__text: 0x2f40c
   __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_methlist: 0x2f7c
+  __TEXT.__objc_methlist: 0x2fb4
   __TEXT.__const: 0x200
-  __TEXT.__gcc_except_tab: 0x4f4
+  __TEXT.__gcc_except_tab: 0x7c8
   __TEXT.__oslogstring: 0x1d1d
   __TEXT.__cstring: 0x4b23
   __TEXT.__swift5_typeref: 0x180
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0xe80
+  __TEXT.__unwind_info: 0xed8
   __TEXT.__eh_frame: 0x138
   __TEXT.__objc_classname: 0x566
-  __TEXT.__objc_methname: 0x83c7
+  __TEXT.__objc_methname: 0x84c8
   __TEXT.__objc_methtype: 0x1465
-  __TEXT.__objc_stubs: 0x5060
+  __TEXT.__objc_stubs: 0x50c0
   __DATA_CONST.__got: 0x318
-  __DATA_CONST.__const: 0xff0
+  __DATA_CONST.__const: 0x1068
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b18
+  __DATA_CONST.__objc_selrefs: 0x1b40
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x118
   __AUTH_CONST.__auth_got: 0x4c8
   __AUTH_CONST.__const: 0x3d0
   __AUTH_CONST.__cfstring: 0x2280
-  __AUTH_CONST.__objc_const: 0x5798
+  __AUTH_CONST.__objc_const: 0x57f8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x3c8
+  __DATA.__objc_ivar: 0x3d0
   __DATA.__data: 0x708
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x780

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  UUID: 319C65EF-EC1F-37CE-9860-606D03D5D357
-  Functions: 1393
-  Symbols:   4576
-  CStrings:  2364
+  UUID: 32AE78E3-356E-3ABC-A1B7-DF5A63BE7A88
+  Functions: 1408
+  Symbols:   4618
+  CStrings:  2373
 
Symbols:
+ -[RCConfigurationManager _lockedConfigResourceForKey:]
+ -[RCConfigurationManager configResourceLock]
+ -[RCConfigurationManager networkEventHandlerLock]
+ -[RCConfigurationManager setConfigResourceLock:]
+ -[RCConfigurationManager setNetworkEventHandlerLock:]
+ GCC_except_table15
+ GCC_except_table41
+ GCC_except_table54
+ GCC_except_table57
+ GCC_except_table67
+ _OBJC_IVAR_$_RCConfigurationManager._configResourceLock
+ _OBJC_IVAR_$_RCConfigurationManager._networkEventHandlerLock
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.100
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.109
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.130
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.131
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.132
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.138
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.110
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.129
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.137
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.137.cold.1
+ ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.139
+ ___130-[RCConfigurationManager _fetchMultiConfigurationFromEndpointURL:settings:networkActivityBlock:changeTagsByRequestKey:completion:]_block_invoke.162
+ ___183-[RCConfigurationManager _processConfigurationCompletionWithResources:configurationSettings:processedConfigurationDataByRequestKey:processedTreatmentIDs:processedSegmentSetIDs:error:]_block_invoke
+ ___45-[RCConfigurationManager networkEventHandler]_block_invoke
+ ___49-[RCConfigurationManager setNetworkEventHandler:]_block_invoke
+ ___53-[RCConfigurationManager _saveConfigurationResource:]_block_invoke
+ ___54-[RCConfigurationManager _lockedConfigResourceForKey:]_block_invoke
+ ___68-[RCConfigurationManager _removeConfigurationResourceForRequestKey:]_block_invoke
+ ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.169
+ ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.172
+ ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_2.170.cold.1
+ ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_2.174
+ ___98-[RCConfigurationManager _isAllowedToReachEndpointWithSettings:configurationResource:endpointURL:]_block_invoke.157
+ ___98-[RCConfigurationManager _isAllowedToReachEndpointWithSettings:configurationResource:endpointURL:]_block_invoke.160
+ ___Block_byref_object_copy_.107
+ ___Block_byref_object_dispose_.108
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56r64r72r_e5_v8?0lr56l8s32l8s40l8r64l8s48l8r72l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72r_e5_v8?0lr72l8s32l8s40l8s48l8s64l8s56l8
+ ___block_literal_global.113
+ ___block_literal_global.116
+ ___block_literal_global.118
+ ___block_literal_global.123
+ ___block_literal_global.126
+ ___block_literal_global.135
+ ___block_literal_global.167
+ ___block_literal_global.99
+ _objc_msgSend$_lockedConfigResourceForKey:
+ _objc_msgSend$configResourceLock
+ _objc_msgSend$networkEventHandlerLock
- GCC_except_table45
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.123
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.124
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.126
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.134
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke.99
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.125
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.133
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.133.cold.1
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_2.135
- ___110-[RCConfigurationManager fetchMultiConfigurationWithSettings:networkActivityBlock:completionQueue:completion:]_block_invoke_8
- ___130-[RCConfigurationManager _fetchMultiConfigurationFromEndpointURL:settings:networkActivityBlock:changeTagsByRequestKey:completion:]_block_invoke.158
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.161
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke.168
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_2.166
- ___84-[RCConfigurationManager _fetchConfigurationFromFallbackURLWithSettings:completion:]_block_invoke_2.166.cold.1
- ___98-[RCConfigurationManager _isAllowedToReachEndpointWithSettings:configurationResource:endpointURL:]_block_invoke.153
- ___98-[RCConfigurationManager _isAllowedToReachEndpointWithSettings:configurationResource:endpointURL:]_block_invoke.156
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s72l8s64l8
- ___block_literal_global.109
- ___block_literal_global.112
- ___block_literal_global.114
- ___block_literal_global.119
- ___block_literal_global.122
- ___block_literal_global.131
- ___block_literal_global.163
- ___block_literal_global.98
CStrings:
+ "\r"
+ "T@\"RCUnfairLock\",&,N,V_configResourceLock"
+ "T@\"RCUnfairLock\",&,N,V_networkEventHandlerLock"
+ "_configResourceLock"
+ "_lockedConfigResourceForKey:"
+ "_networkEventHandlerLock"
+ "configResourceLock"
+ "networkEventHandlerLock"
+ "setConfigResourceLock:"
+ "setNetworkEventHandlerLock:"
- "\v"

```
