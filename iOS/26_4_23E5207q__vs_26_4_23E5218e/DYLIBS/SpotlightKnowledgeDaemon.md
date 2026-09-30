## SpotlightKnowledgeDaemon

> `/System/Library/PrivateFrameworks/SpotlightKnowledgeDaemon.framework/SpotlightKnowledgeDaemon`

```diff

-2418.4.8.2.100
-  __TEXT.__text: 0x290294
-  __TEXT.__auth_stubs: 0x5040
-  __TEXT.__objc_methlist: 0x98b8
-  __TEXT.__const: 0xce08
-  __TEXT.__oslogstring: 0xcc54
-  __TEXT.__cstring: 0xbd1e
-  __TEXT.__gcc_except_tab: 0x5f30
+2418.4.10.1.0
+  __TEXT.__text: 0x29015c
+  __TEXT.__auth_stubs: 0x5060
+  __TEXT.__objc_methlist: 0x9920
+  __TEXT.__const: 0xcd38
+  __TEXT.__oslogstring: 0xcb24
+  __TEXT.__cstring: 0xbd6e
+  __TEXT.__gcc_except_tab: 0x5f48
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__swift5_typeref: 0x8eec
-  __TEXT.__swift5_fieldmd: 0x4730
-  __TEXT.__constg_swiftt: 0x532c
-  __TEXT.__swift5_capture: 0x1a60
+  __TEXT.__swift5_typeref: 0x8e4c
+  __TEXT.__swift5_fieldmd: 0x475c
+  __TEXT.__constg_swiftt: 0x5320
+  __TEXT.__swift5_capture: 0x1a3c
   __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_reflstr: 0x3ef5
+  __TEXT.__swift5_reflstr: 0x3f55
   __TEXT.__swift5_assocty: 0xe18
   __TEXT.__swift5_protos: 0x158
-  __TEXT.__swift5_proto: 0x91c
-  __TEXT.__swift5_types: 0x4ec
+  __TEXT.__swift5_proto: 0x914
+  __TEXT.__swift5_types: 0x4e8
   __TEXT.__swift_as_entry: 0xe8
   __TEXT.__swift_as_ret: 0x120
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0x7c18
-  __TEXT.__eh_frame: 0x75a8
-  __TEXT.__objc_classname: 0x1f4f
-  __TEXT.__objc_methname: 0x16707
-  __TEXT.__objc_methtype: 0x2cee
-  __TEXT.__objc_stubs: 0x10ce0
-  __DATA_CONST.__got: 0x1a10
+  __TEXT.__unwind_info: 0x7c38
+  __TEXT.__eh_frame: 0x75e0
+  __TEXT.__objc_classname: 0x1f7f
+  __TEXT.__objc_methname: 0x167cd
+  __TEXT.__objc_methtype: 0x2d1e
+  __TEXT.__objc_stubs: 0x10d00
+  __DATA_CONST.__got: 0x1a18
   __DATA_CONST.__const: 0x3bd8
-  __DATA_CONST.__objc_classlist: 0x868
+  __DATA_CONST.__objc_classlist: 0x870
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x160
+  __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ea0
+  __DATA_CONST.__objc_selrefs: 0x4eb8
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x4e8
   __DATA_CONST.__objc_arraydata: 0x828
-  __AUTH_CONST.__auth_got: 0x2838
-  __AUTH_CONST.__const: 0xdbf8
-  __AUTH_CONST.__cfstring: 0x9900
-  __AUTH_CONST.__objc_const: 0x15770
+  __AUTH_CONST.__auth_got: 0x2848
+  __AUTH_CONST.__const: 0xdbb0
+  __AUTH_CONST.__cfstring: 0x99a0
+  __AUTH_CONST.__objc_const: 0x15900
   __AUTH_CONST.__objc_intobj: 0x990
   __AUTH_CONST.__objc_arrayobj: 0x678
   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x2df0
-  __AUTH.__data: 0x2620
-  __DATA.__objc_ivar: 0xb94
-  __DATA.__data: 0x2ce0
-  __DATA.__bss: 0x9c00
+  __AUTH.__objc_data: 0x2e48
+  __AUTH.__data: 0x26a0
+  __DATA.__objc_ivar: 0xba0
+  __DATA.__data: 0x2d70
+  __DATA.__bss: 0x9b40
   __DATA.__common: 0x50
-  __DATA_DIRTY.__objc_data: 0x2518
-  __DATA_DIRTY.__data: 0x61d8
+  __DATA_DIRTY.__objc_data: 0x2520
+  __DATA_DIRTY.__data: 0x6180
   __DATA_DIRTY.__bss: 0x4680
   __DATA_DIRTY.__common: 0x198
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/SpotlightKnowledge.framework/SpotlightKnowledge
   - /System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics
   - /System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D45CA5FA-87A3-3331-B6CA-BE1914A5ED3B
-  Functions: 11419
-  Symbols:   18475
-  CStrings:  8413
+  UUID: C8F6ECFA-9CF7-3620-8E4A-D4938C7F33D2
+  Functions: 11432
+  Symbols:   18534
+  CStrings:  8432
 
Symbols:
+ -[SKDDefaultsProvider initWithSpotlightResourcesProvider:featureFlagsProvider:localeProvider:deviceProvider:]
+ -[SKDDefaultsProvider isGenerativeMLSupported]
+ -[SKDDeviceProvider isGenerativeMLSupported]
+ -[SKDPipelineLogger initWithDomain:].cold.1
+ -[SKDPowerLogger logs].cold.1
+ -[SKDPowerLogger(Internal) setCacheStartTime:]
+ _MGCopyAnswer
+ _OBJC_CLASS_$_SKDDeviceProvider
+ _OBJC_IVAR_$_SKDDefaultsProvider._deviceProvider
+ _OBJC_IVAR_$_SKDPowerLogSender._processorIdentifier
+ _OBJC_IVAR_$_SKDPowerLogger._cacheStartTime
+ _OBJC_METACLASS_$_SKDDeviceProvider
+ _PPSCreateTelemetryIdentifier
+ _PPSSendTelemetry
+ __IVARS_SKDLocaleProvider
+ __OBJC_$_INSTANCE_METHODS_SKDDeviceProvider
+ __OBJC_$_PROP_LIST_SKDDeviceProvider
+ __OBJC_$_PROP_LIST_SKDDeviceProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SKDDeviceProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SKDDeviceProviding
+ __OBJC_CLASS_PROTOCOLS_$_SKDDeviceProvider
+ __OBJC_CLASS_RO_$_SKDDeviceProvider
+ __OBJC_LABEL_PROTOCOL_$_SKDDeviceProviding
+ __OBJC_METACLASS_RO_$_SKDDeviceProvider
+ __OBJC_PROTOCOL_$_SKDDeviceProviding
+ ___22-[SKDPowerLogger logs]_block_invoke
+ ___22-[SKGTaskAgent _setup]_block_invoke.120
+ ___22-[SKGTaskAgent _setup]_block_invoke.128
+ ___22-[SKGTaskAgent _setup]_block_invoke.136
+ ___22-[SKGTaskAgent _setup]_block_invoke.139
+ ___22-[SKGTaskAgent _setup]_block_invoke.144
+ ___22-[SKGTaskAgent _setup]_block_invoke.151
+ ___22-[SKGTaskAgent _setup]_block_invoke.159
+ ___22-[SKGTaskAgent _setup]_block_invoke.162
+ ___22-[SKGTaskAgent _setup]_block_invoke.170
+ ___22-[SKGTaskAgent _setup]_block_invoke.171
+ ___22-[SKGTaskAgent _setup]_block_invoke.47
+ ___22-[SKGTaskAgent _setup]_block_invoke.57
+ ___22-[SKGTaskAgent _setup]_block_invoke.66
+ ___22-[SKGTaskAgent _setup]_block_invoke.66.cold.1
+ ___22-[SKGTaskAgent _setup]_block_invoke.74
+ ___22-[SKGTaskAgent _setup]_block_invoke.74.cold.1
+ ___22-[SKGTaskAgent _setup]_block_invoke.79
+ ___22-[SKGTaskAgent _setup]_block_invoke.98
+ ___22-[SKGTaskAgent _setup]_block_invoke_2.108
+ ___22-[SKGTaskAgent _setup]_block_invoke_2.121
+ ___22-[SKGTaskAgent _setup]_block_invoke_2.129
+ ___22-[SKGTaskAgent _setup]_block_invoke_2.137
+ ___22-[SKGTaskAgent _setup]_block_invoke_2.152
+ ___22-[SKGTaskAgent _setup]_block_invoke_2.158
+ ___22-[SKGTaskAgent _setup]_block_invoke_2.163
+ ___22-[SKGTaskAgent _setup]_block_invoke_2.169
+ ___22-[SKGTaskAgent _setup]_block_invoke_2.174
+ ___22-[SKGTaskAgent _setup]_block_invoke_2.48
+ ___22-[SKGTaskAgent _setup]_block_invoke_2.58
+ ___22-[SKGTaskAgent _setup]_block_invoke_2.65
+ ___22-[SKGTaskAgent _setup]_block_invoke_2.80
+ ___22-[SKGTaskAgent _setup]_block_invoke_3.122
+ ___22-[SKGTaskAgent _setup]_block_invoke_3.130
+ ___22-[SKGTaskAgent _setup]_block_invoke_3.138
+ ___22-[SKGTaskAgent _setup]_block_invoke_3.153
+ ___22-[SKGTaskAgent _setup]_block_invoke_3.177
+ ___22-[SKGTaskAgent _setup]_block_invoke_3.177.cold.1
+ ___22-[SKGTaskAgent _setup]_block_invoke_3.59
+ ___22-[SKGTaskAgent _setup]_block_invoke_3.81
+ ___34-[SKGUpdaterAgent handleDiagnose:]_block_invoke.243
+ ___36-[SKDPipelineLogger initWithDomain:]_block_invoke
+ ___block_literal_global.100
+ ___block_literal_global.110
+ ___block_literal_global.173
+ ___block_literal_global.191
+ ___block_literal_global.194
+ ___block_literal_global.198
+ ___block_literal_global.219
+ ___block_literal_global.240
+ ___block_literal_global.78
+ ___block_literal_global.80
+ ___block_literal_global.87
+ _block_copy_helper.126
+ _block_copy_helper.132
+ _block_copy_helper.138
+ _block_copy_helper.153
+ _block_copy_helper.180
+ _block_copy_helper.61
+ _block_copy_helper.67
+ _block_copy_helper.80
+ _block_copy_helper.89
+ _block_descriptor.128
+ _block_descriptor.134
+ _block_descriptor.140
+ _block_descriptor.155
+ _block_descriptor.182
+ _block_descriptor.63
+ _block_descriptor.69
+ _block_descriptor.82
+ _block_descriptor.91
+ _block_destroy_helper.127
+ _block_destroy_helper.133
+ _block_destroy_helper.139
+ _block_destroy_helper.154
+ _block_destroy_helper.181
+ _block_destroy_helper.62
+ _block_destroy_helper.68
+ _block_destroy_helper.81
+ _block_destroy_helper.90
+ _get_type_metadata 15Synchronization5MutexVy24SpotlightKnowledgeDaemon14LocaleProviderC5StateVG noncopyable.4
+ _initWithDomain:.onceToken
+ _initWithDomain:.sharedAnalyticsLogSender
+ _initWithDomain:.sharedAnalyticsLogger
+ _initWithDomain:.sharedPowerHUDSender
+ _initWithDomain:.sharedPowerLogSender
+ _initWithDomain:.sharedPowerLogger
+ _logs.onceToken
+ _logs.timeFormatter
+ _objc_msgSend$initWithSpotlightResourcesProvider:featureFlagsProvider:localeProvider:deviceProvider:
+ _objc_msgSend$isGenerativeMLSupported
+ _objc_msgSend$localTimeZone
+ _objectdestroy.103Tm
+ _objectdestroy.124Tm
+ _objectdestroy.37Tm
+ _objectdestroy.99Tm
+ _symbolic _____ 10Foundation6LocaleV
+ _symbolic _____ 24SpotlightKnowledgeDaemon14LocaleProviderC5StateV
+ _symbolic _____y_____G 15Synchronization5MutexVAARi_zrlE 24SpotlightKnowledgeDaemon14LocaleProviderC5StateV
+ _symbolic _____y_____G 15Synchronization5_CellVAARi_zrlE 24SpotlightKnowledgeDaemon14LocaleProviderC5StateV
- -[SKDDefaultsProvider initWithSpotlightResourcesProvider:featureFlagsProvider:localeProvider:]
- _PLLogRegisteredEvent
- _PLShouldLogRegisteredEvent
- ___22-[SKGTaskAgent _setup]_block_invoke.116
- ___22-[SKGTaskAgent _setup]_block_invoke.124
- ___22-[SKGTaskAgent _setup]_block_invoke.132
- ___22-[SKGTaskAgent _setup]_block_invoke.137
- ___22-[SKGTaskAgent _setup]_block_invoke.140
- ___22-[SKGTaskAgent _setup]_block_invoke.147
- ___22-[SKGTaskAgent _setup]_block_invoke.155
- ___22-[SKGTaskAgent _setup]_block_invoke.160
- ___22-[SKGTaskAgent _setup]_block_invoke.166
- ___22-[SKGTaskAgent _setup]_block_invoke.169
- ___22-[SKGTaskAgent _setup]_block_invoke.46
- ___22-[SKGTaskAgent _setup]_block_invoke.53
- ___22-[SKGTaskAgent _setup]_block_invoke.62
- ___22-[SKGTaskAgent _setup]_block_invoke.64.cold.1
- ___22-[SKGTaskAgent _setup]_block_invoke.72
- ___22-[SKGTaskAgent _setup]_block_invoke.72.cold.1
- ___22-[SKGTaskAgent _setup]_block_invoke.77
- ___22-[SKGTaskAgent _setup]_block_invoke.96
- ___22-[SKGTaskAgent _setup]_block_invoke_2.106
- ___22-[SKGTaskAgent _setup]_block_invoke_2.117
- ___22-[SKGTaskAgent _setup]_block_invoke_2.125
- ___22-[SKGTaskAgent _setup]_block_invoke_2.133
- ___22-[SKGTaskAgent _setup]_block_invoke_2.148
- ___22-[SKGTaskAgent _setup]_block_invoke_2.156
- ___22-[SKGTaskAgent _setup]_block_invoke_2.161
- ___22-[SKGTaskAgent _setup]_block_invoke_2.167
- ___22-[SKGTaskAgent _setup]_block_invoke_2.172
- ___22-[SKGTaskAgent _setup]_block_invoke_2.47
- ___22-[SKGTaskAgent _setup]_block_invoke_2.54
- ___22-[SKGTaskAgent _setup]_block_invoke_2.63
- ___22-[SKGTaskAgent _setup]_block_invoke_2.78
- ___22-[SKGTaskAgent _setup]_block_invoke_3.120
- ___22-[SKGTaskAgent _setup]_block_invoke_3.128
- ___22-[SKGTaskAgent _setup]_block_invoke_3.136
- ___22-[SKGTaskAgent _setup]_block_invoke_3.151
- ___22-[SKGTaskAgent _setup]_block_invoke_3.175
- ___22-[SKGTaskAgent _setup]_block_invoke_3.175.cold.1
- ___22-[SKGTaskAgent _setup]_block_invoke_3.57
- ___22-[SKGTaskAgent _setup]_block_invoke_3.79
- ___34-[SKGUpdaterAgent handleDiagnose:]_block_invoke.242
- ___36-[SKDPowerLogSender sendLog:domain:]_block_invoke
- ___block_literal_global.108
- ___block_literal_global.176
- ___block_literal_global.178
- ___block_literal_global.190
- ___block_literal_global.197
- ___block_literal_global.200
- ___block_literal_global.218
- ___block_literal_global.239
- ___block_literal_global.75
- ___block_literal_global.79
- ___block_literal_global.82
- ___block_literal_global.85
- ___block_literal_global.98
- _block_copy_helper.136
- _block_copy_helper.142
- _block_copy_helper.148
- _block_copy_helper.163
- _block_copy_helper.190
- _block_copy_helper.40
- _block_copy_helper.49
- _block_copy_helper.90
- _block_copy_helper.99
- _block_descriptor.101
- _block_descriptor.138
- _block_descriptor.144
- _block_descriptor.150
- _block_descriptor.165
- _block_descriptor.192
- _block_descriptor.42
- _block_descriptor.51
- _block_descriptor.92
- _block_destroy_helper.100
- _block_destroy_helper.137
- _block_destroy_helper.143
- _block_destroy_helper.149
- _block_destroy_helper.164
- _block_destroy_helper.191
- _block_destroy_helper.41
- _block_destroy_helper.50
- _block_destroy_helper.91
- _objc_msgSend$initWithSpotlightResourcesProvider:featureFlagsProvider:localeProvider:
- _objc_msgSend$processName
- _objectdestroy.109Tm
- _objectdestroy.113Tm
- _objectdestroy.134Tm
- _symbolic _____ 24SpotlightKnowledgeDaemon010RunAheadOfA13IndexingErrorV
- _symbolic _____ 24SpotlightKnowledgeDaemon0A23SerialNumberFetchFailedV
- _symbolic _____y_____y_____17consumedSerialNum_AC06latestbC0t______pGSgG 15Synchronization5MutexVAARi_zrlE s6ResultOsRi_zRi0_zrlE s5Int64V s5ErrorP
- _symbolic _____y_____y_____17consumedSerialNum_AC06latestbC0t______pGSgG 15Synchronization5_CellVAARi_zrlE s6ResultOsRi_zRi0_zrlE s5Int64V s5ErrorP
- _symbolic _____y_____y_____17consumedSerialNum_AC06latestbC0t______pGSgG_Xx 15Synchronization5MutexVAARi_zrlE s6ResultOsRi_zRi0_zrlE s5Int64V s5ErrorP
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJJDugDBdzHbq-LlCV3nhm71CP3sRReCP7Nr39c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJJDugDBdzHbq-LlCV3nhm71CP3sRReCP7Nr39c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJJDugDBdzHbq-LlCV3nhm71CP3sRReCP7Nr39c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJJDugDBdzHbq-LlCV3nhm71CP3sRReCP7Nr39c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJJDugDBdzHbq-LlCV3nhm71CP3sRReCP7Nr39c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "@\"<SKDDeviceProviding>\""
+ "BundleID"
+ "DeviceSupportsGenerativeModelSystems"
+ "HH:mm:ss"
+ "ProcessorEvents"
+ "ProcessorsCount"
+ "SKDDeviceProvider"
+ "SKDDeviceProviding"
+ "TB,R,N,GisGenerativeMLSupported"
+ "^{PPSTelemetryIdentifier=}"
+ "_cacheStartTime"
+ "_deviceProvider"
+ "_processorIdentifier"
+ "generativeMLSupported"
+ "initWithSpotlightResourcesProvider:featureFlagsProvider:localeProvider:deviceProvider:"
+ "isGenerativeMLSupported"
+ "localTimeZone"
+ "setCacheStartTime:"
+ "timeEnd"
+ "timeStart"
+ "updateLocale"
- "%{public}s Skipping donation with serial number %ld because it's newer than latest consumed serial number %lld"
- "%{public}s Skipping donation with serial number %ld because it's newer than latest serial number %lld"
- "%{public}s job paused due to running ahead of Spotlight indexing."
- "/AppleInternal/Library/BuildRoots/4~CIVGugCpcRPc2I8nJ5PJaiXN-TzE979HA5OuEdc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CIVGugCpcRPc2I8nJ5PJaiXN-TzE979HA5OuEdc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIVGugCpcRPc2I8nJ5PJaiXN-TzE979HA5OuEdc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIVGugCpcRPc2I8nJ5PJaiXN-TzE979HA5OuEdc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CIVGugCpcRPc2I8nJ5PJaiXN-TzE979HA5OuEdc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "initWithSpotlightResourcesProvider:featureFlagsProvider:localeProvider:"
- "processName"
- "timestampEnd"

```
