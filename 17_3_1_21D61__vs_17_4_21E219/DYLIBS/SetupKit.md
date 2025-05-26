## SetupKit

> `/System/Library/PrivateFrameworks/SetupKit.framework/SetupKit`

```diff

-730.8.3.0.0
-  __TEXT.__text: 0x27440
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_methlist: 0x1d6c
-  __TEXT.__const: 0x180
-  __TEXT.__gcc_except_tab: 0xd50
-  __TEXT.__cstring: 0x72cc
-  __TEXT.__unwind_info: 0x9b0
-  __TEXT.__objc_classname: 0x3d9
-  __TEXT.__objc_methname: 0x362a
+740.14.0.0.0
+  __TEXT.__text: 0x27c88
+  __TEXT.__auth_stubs: 0x7c0
+  __TEXT.__objc_methlist: 0x1e5c
+  __TEXT.__const: 0x192
+  __TEXT.__gcc_except_tab: 0xd58
+  __TEXT.__cstring: 0x7168
+  __TEXT.__oslogstring: 0x113
+  __TEXT.__unwind_info: 0x9cc
+  __TEXT.__objc_classname: 0x3dc
+  __TEXT.__objc_methname: 0x382a
   __TEXT.__objc_methtype: 0xb27
-  __TEXT.__objc_stubs: 0x2b80
+  __TEXT.__objc_stubs: 0x2ca0
   __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0xec8
+  __DATA_CONST.__const: 0xed0
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4698
-  __DATA_CONST.__objc_selrefs: 0xcf0
+  __DATA_CONST.__objc_const: 0x4878
+  __DATA_CONST.__objc_selrefs: 0xd50
+  __DATA_CONST.__objc_classrefs: 0x1c0
+  __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__cfstring: 0xac0
-  __AUTH_CONST.__const: 0x6e0
+  __AUTH_CONST.__cfstring: 0xae0
+  __AUTH_CONST.__const: 0x720
   __AUTH_CONST.__objc_const: 0x9d8
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__auth_got: 0x3c8
+  __AUTH_CONST.__auth_got: 0x3f0
   __AUTH.__objc_data: 0xaa0
-  __DATA.__objc_classrefs: 0x1c0
-  __DATA.__objc_superrefs: 0xb0
-  __DATA.__objc_ivar: 0x44c
+  __DATA.__objc_ivar: 0x474
   __DATA.__data: 0xc90
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 904
-  Symbols:   3042
-  CStrings:  1716
+  Functions: 929
+  Symbols:   3122
+  CStrings:  1747
 
Symbols:
+ -[SKConnection conditionalPersistent]
+ -[SKConnection setConditionalPersistent:]
+ -[SKSetupBase conditionalPersistent]
+ -[SKSetupBase setConditionalPersistent:]
+ -[SKSetupClient clientConfig]
+ -[SKSetupClient setClientConfig:]
+ -[SKSetupClient setSkipWifi:]
+ -[SKSetupClient skipWifi]
+ -[SKSetupServer serverConfig]
+ -[SKSetupServer setServerConfig:]
+ -[SKSetupServer setSkipWifi:]
+ -[SKSetupServer skipWifi]
+ -[SKStepBasicConfigClient clientConfig]
+ -[SKStepBasicConfigClient outServerConfig]
+ -[SKStepBasicConfigClient setClientConfig:]
+ -[SKStepBasicConfigClient setOutServerConfig:]
+ -[SKStepBasicConfigServer outClientConfig]
+ -[SKStepBasicConfigServer serverConfig]
+ -[SKStepBasicConfigServer setOutClientConfig:]
+ -[SKStepBasicConfigServer setServerConfig:]
+ GCC_except_table132
+ GCC_except_table152
+ GCC_except_table154
+ GCC_except_table160
+ GCC_except_table166
+ GCC_except_table171
+ GCC_except_table184
+ GCC_except_table192
+ GCC_except_table221
+ GCC_except_table385
+ GCC_except_table455
+ GCC_except_table497
+ GCC_except_table503
+ GCC_except_table507
+ GCC_except_table551
+ GCC_except_table558
+ GCC_except_table569
+ GCC_except_table576
+ GCC_except_table648
+ GCC_except_table655
+ GCC_except_table662
+ GCC_except_table665
+ GCC_except_table775
+ GCC_except_table844
+ GCC_except_table877
+ GCC_except_table883
+ GCC_except_table887
+ _OBJC_IVAR_$_SKConnection._conditionalPersistent
+ _OBJC_IVAR_$_SKSetupBase._conditionalPersistent
+ _OBJC_IVAR_$_SKSetupClient._clientConfig
+ _OBJC_IVAR_$_SKSetupClient._skipWifi
+ _OBJC_IVAR_$_SKSetupServer._serverConfig
+ _OBJC_IVAR_$_SKSetupServer._skipWifi
+ _OBJC_IVAR_$_SKStepBasicConfigClient._clientConfig
+ _OBJC_IVAR_$_SKStepBasicConfigClient._outServerConfig
+ _OBJC_IVAR_$_SKStepBasicConfigServer._outClientConfig
+ _OBJC_IVAR_$_SKStepBasicConfigServer._serverConfig
+ ___40-[SKSetupClient _prepareStepsOSRecovery]_block_invoke_2
+ ___40-[SKSetupServer _prepareStepsOSRecovery]_block_invoke_2
+ ___48-[SKSetupOSUpdateServer _bleServerEnsureStarted]_block_invoke.13
+ ___73-[SKConnection _sendRequestID:request:options:sendEntry:responseHandler:]_block_invoke.241
+ ___Block_byref_object_copy_.1187
+ ___Block_byref_object_copy_.1604
+ ___Block_byref_object_copy_.2049
+ ___Block_byref_object_copy_.2264
+ ___Block_byref_object_copy_.394
+ ___Block_byref_object_copy_.586
+ ___Block_byref_object_copy_.798
+ ___Block_byref_object_copy_.953
+ ___Block_byref_object_dispose_.1188
+ ___Block_byref_object_dispose_.1605
+ ___Block_byref_object_dispose_.2050
+ ___Block_byref_object_dispose_.2265
+ ___Block_byref_object_dispose_.395
+ ___Block_byref_object_dispose_.587
+ ___Block_byref_object_dispose_.799
+ ___Block_byref_object_dispose_.954
+ ___block_literal_global.1025
+ ___block_literal_global.11
+ ___block_literal_global.1292
+ ___block_literal_global.1350
+ ___block_literal_global.1388
+ ___block_literal_global.1450
+ ___block_literal_global.16.294
+ ___block_literal_global.1684
+ ___block_literal_global.1719
+ ___block_literal_global.1787
+ ___block_literal_global.19.2384
+ ___block_literal_global.21.2386
+ ___block_literal_global.22.1447
+ ___block_literal_global.23.1784
+ ___block_literal_global.23.2388
+ ___block_literal_global.2382
+ ___block_literal_global.251
+ ___block_literal_global.258
+ ___block_literal_global.298
+ ___block_literal_global.302
+ ___block_literal_global.303
+ ___block_literal_global.34.2360
+ ___block_literal_global.391
+ ___block_literal_global.44
+ ___block_literal_global.47.2365
+ ___block_literal_global.494
+ ___block_literal_global.50.2354
+ ___block_literal_global.53.2351
+ ___block_literal_global.55
+ ___block_literal_global.622
+ ___block_literal_global.698
+ ___block_literal_global.8
+ ___block_literal_global.861
+ ___logger_block_invoke
+ ___logger_block_invoke.1740
+ __os_log_error_impl
+ __os_log_impl
+ __unnamed_array_storage.1054
+ _logger
+ _objc_msgSend$clientConfig
+ _objc_msgSend$conditionalPersistent
+ _objc_msgSend$outServerConfig
+ _objc_msgSend$serverConfig
+ _objc_msgSend$setClientConfig:
+ _objc_msgSend$setConditionalPersistent:
+ _objc_msgSend$setOutClientConfig:
+ _objc_msgSend$setOutServerConfig:
+ _objc_msgSend$setServerConfig:
+ _objc_release_x2
+ _os_log_create
+ _os_log_type_enabled
+ _sCUOSLogCreateOnce_logger
+ _sCUOSLogCreateOnce_logger.1720
+ _sCUOSLogHandle_logger
+ _sCUOSLogHandle_logger.1721
- GCC_except_table124
- GCC_except_table148
- GCC_except_table150
- GCC_except_table156
- GCC_except_table162
- GCC_except_table167
- GCC_except_table180
- GCC_except_table188
- GCC_except_table217
- GCC_except_table371
- GCC_except_table441
- GCC_except_table483
- GCC_except_table489
- GCC_except_table493
- GCC_except_table537
- GCC_except_table544
- GCC_except_table555
- GCC_except_table562
- GCC_except_table629
- GCC_except_table636
- GCC_except_table643
- GCC_except_table646
- GCC_except_table751
- GCC_except_table819
- GCC_except_table852
- GCC_except_table858
- GCC_except_table862
- ___48-[SKSetupOSUpdateServer _bleServerEnsureStarted]_block_invoke_2
- ___73-[SKConnection _sendRequestID:request:options:sendEntry:responseHandler:]_block_invoke.239
- ___Block_byref_object_copy_.1110
- ___Block_byref_object_copy_.1519
- ___Block_byref_object_copy_.1950
- ___Block_byref_object_copy_.2163
- ___Block_byref_object_copy_.382
- ___Block_byref_object_copy_.556
- ___Block_byref_object_copy_.756
- ___Block_byref_object_copy_.913
- ___Block_byref_object_dispose_.1111
- ___Block_byref_object_dispose_.1520
- ___Block_byref_object_dispose_.1951
- ___Block_byref_object_dispose_.2164
- ___Block_byref_object_dispose_.383
- ___Block_byref_object_dispose_.557
- ___Block_byref_object_dispose_.757
- ___Block_byref_object_dispose_.914
- ___block_literal_global.1213
- ___block_literal_global.1275
- ___block_literal_global.1314
- ___block_literal_global.1376
- ___block_literal_global.15
- ___block_literal_global.1595
- ___block_literal_global.1630
- ___block_literal_global.1694
- ___block_literal_global.19.2283
- ___block_literal_global.21.2285
- ___block_literal_global.22.1373
- ___block_literal_global.2281
- ___block_literal_global.23.1691
- ___block_literal_global.23.2287
- ___block_literal_global.24.1272
- ___block_literal_global.249
- ___block_literal_global.256
- ___block_literal_global.296
- ___block_literal_global.297
- ___block_literal_global.300
- ___block_literal_global.34.2259
- ___block_literal_global.377
- ___block_literal_global.47.2264
- ___block_literal_global.476
- ___block_literal_global.50.2253
- ___block_literal_global.52
- ___block_literal_global.53.2250
- ___block_literal_global.593
- ___block_literal_global.654
- ___block_literal_global.820
- ___block_literal_global.981
- __unnamed_array_storage.1010
CStrings:
+ "\x03\x15"
+ "\x12\x14&"
+ "\x13\x12"
+ "\x14\x12"
+ "%s: BasicConfig got error %@, ignoring"
+ "-[SKSetupClient _prepareStepsOSRecovery]_block_invoke"
+ "Client error: %@"
+ "OSREXT"
+ "T@\"NSDictionary\",C,N,V_clientConfig"
+ "T@\"NSDictionary\",C,N,V_outClientConfig"
+ "T@\"NSDictionary\",C,N,V_outServerConfig"
+ "T@\"NSDictionary\",C,N,V_serverConfig"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_conditionalPersistent"
+ "TB,N,V_skipWifi"
+ "_clientConfig"
+ "_conditionalPersistent"
+ "_outClientConfig"
+ "_outServerConfig"
+ "_serverConfig"
+ "_skipWifi"
+ "clientConfig"
+ "conditional"
+ "conditionalPersistent"
+ "outClientConfig"
+ "outServerConfig"
+ "persistent %s"
+ "serverConfig"
+ "setClientConfig:"
+ "setConditionalPersistent:"
+ "setOutClientConfig:"
+ "setOutServerConfig:"
+ "setServerConfig:"
+ "setSkipWifi:"
+ "skipWifi"
- "\a"
- "\x12\x14\x15"
- "\x13"
- "\x14"
- "### Client error: %@"
- "-[SKSetupOSUpdateClient _run]"
- "-[SKSetupOSUpdateServer _bleAdvertiserEnsureStarted]"
- "-[SKSetupOSUpdateServer _bleAdvertiserEnsureStarted]_block_invoke"
- "-[SKSetupOSUpdateServer _bleAdvertiserEnsureStopped]"
- "-[SKSetupOSUpdateServer _bleServerAcceptConnecton:]"
- "-[SKSetupOSUpdateServer _bleServerEnsureStarted]"
- "-[SKSetupOSUpdateServer _bleServerEnsureStarted]_block_invoke"
- "-[SKSetupOSUpdateServer _bleServerEnsureStarted]_block_invoke_2"
- "-[SKSetupOSUpdateServer _bleServerEnsureStopped]"

```
