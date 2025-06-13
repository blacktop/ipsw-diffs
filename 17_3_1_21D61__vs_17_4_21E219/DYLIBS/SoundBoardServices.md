## SoundBoardServices

> `/System/Library/PrivateFrameworks/SoundBoardServices.framework/SoundBoardServices`

```diff

-741.30.4.0.0
-  __TEXT.__text: 0x12fb8
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0x16ac
+741.40.21.0.0
+  __TEXT.__text: 0x13ac8
+  __TEXT.__auth_stubs: 0x470
+  __TEXT.__objc_methlist: 0x1774
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x1197
+  __TEXT.__cstring: 0x11d7
   __TEXT.__constg_swiftt: 0x2c
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x69c
-  __TEXT.__oslogstring: 0x9a9
-  __TEXT.__unwind_info: 0x8d4
-  __TEXT.__objc_classname: 0x2f7
-  __TEXT.__objc_methname: 0x2cdb
-  __TEXT.__objc_methtype: 0x74a
-  __TEXT.__objc_stubs: 0x2720
+  __TEXT.__gcc_except_tab: 0x694
+  __TEXT.__oslogstring: 0xa31
+  __TEXT.__unwind_info: 0x924
+  __TEXT.__objc_classname: 0x314
+  __TEXT.__objc_methname: 0x2f09
+  __TEXT.__objc_methtype: 0x7fd
+  __TEXT.__objc_stubs: 0x2880
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x438
+  __DATA_CONST.__const: 0x4b0
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x0
-  __DATA_CONST.__objc_protolist: 0x90
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2480
-  __DATA_CONST.__objc_selrefs: 0xbd8
+  __DATA_CONST.__objc_const: 0x25c0
+  __DATA_CONST.__objc_selrefs: 0xc38
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0x88
   __AUTH_CONST.__const: 0x510
   __AUTH_CONST.__objc_const: 0x678
-  __AUTH_CONST.__cfstring: 0x11c0
-  __AUTH_CONST.__auth_got: 0x238
+  __AUTH_CONST.__cfstring: 0x11e0
+  __AUTH_CONST.__auth_got: 0x248
   __AUTH.__objc_data: 0x500
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0xd0
-  __DATA.__objc_superrefs: 0x88
-  __DATA.__objc_ivar: 0xe8
-  __DATA.__data: 0x6c8
+  __DATA.__objc_ivar: 0xec
+  __DATA.__data: 0x728
   __DATA.__bss: 0xa0
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
-  UUID: 2A641B23-3E5D-3869-804F-D814FAA831A7
-  Functions: 588
-  Symbols:   2052
-  CStrings:  984
+  UUID: 77F5C1CB-FF2A-3808-82A7-91C795992A2E
+  Functions: 615
+  Symbols:   2132
+  CStrings:  1014
 
Symbols:
+ +[SBSUtils connectionWithExportedObject:]
+ -[SBSRemoteDeviceSender airDropSysdiagnose:airDropID:completionHandler:]
+ -[SBSRemoteDeviceSender createSysdiagnose:]
+ -[SBSRemoteDeviceSender fetchLatestEvents:completionHandler:]
+ -[SBSServer airDropSysdiagnose:airDropID:completionHandler:]
+ -[SBSServer airdropServiceDelegate]
+ -[SBSServer cancelCurrentSysdiagnose:]
+ -[SBSServer createSysdiagnose:]
+ -[SBSServer setAirdropServiceDelegate:]
+ -[SBSServer(Internal) airDropSysdiagnoseInternal:airDropID:completionHandler:]
+ -[SBSServer(Internal) cancelSysdiagnoseInternal:]
+ -[SBSServer(Internal) createSysdiagnoseInternal:]
+ -[SBSSysdiagnoseInterface airDropSysdiagnose:airDropID:completionHandler:]
+ -[SBSSysdiagnoseInterface cancelSysdiagnose:]
+ -[SBSSysdiagnoseInterface createSysdiagnose:]
+ -[SBSSysdiagnoseInterface sbConnection]
+ -[SBSSysdiagnoseInterface sbProxy]
+ GCC_except_table204
+ GCC_except_table209
+ GCC_except_table210
+ GCC_except_table211
+ GCC_except_table212
+ GCC_except_table213
+ GCC_except_table267
+ GCC_except_table268
+ GCC_except_table443
+ GCC_except_table446
+ GCC_except_table449
+ GCC_except_table452
+ GCC_except_table455
+ GCC_except_table459
+ GCC_except_table467
+ GCC_except_table471
+ GCC_except_table475
+ GCC_except_table478
+ GCC_except_table481
+ GCC_except_table484
+ GCC_except_table487
+ GCC_except_table490
+ GCC_except_table493
+ GCC_except_table497
+ GCC_except_table500
+ GCC_except_table503
+ GCC_except_table507
+ GCC_except_table510
+ GCC_except_table513
+ GCC_except_table516
+ GCC_except_table519
+ GCC_except_table541
+ GCC_except_table544
+ GCC_except_table547
+ GCC_except_table550
+ GCC_except_table553
+ GCC_except_table556
+ GCC_except_table562
+ GCC_except_table565
+ GCC_except_table569
+ GCC_except_table572
+ GCC_except_table575
+ GCC_except_table578
+ GCC_except_table582
+ GCC_except_table586
+ GCC_except_table590
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSURL
+ _OBJC_IVAR_$_SBSServer._airdropServiceDelegate
+ _SBSErrorDomain
+ __OBJC_$_PROP_LIST_SBSSysdiagnoseInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSAirDropServiceImplementer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSAirDropServiceImplementer
+ __OBJC_$_PROTOCOL_REFS_SBSAirDropServiceImplementer
+ __OBJC_LABEL_PROTOCOL_$_SBSAirDropServiceImplementer
+ __OBJC_PROTOCOL_$_SBSAirDropServiceImplementer
+ ___31-[SBSServer createSysdiagnose:]_block_invoke
+ ___38-[SBSServer cancelCurrentSysdiagnose:]_block_invoke
+ ___41+[SBSUtils connectionWithExportedObject:]_block_invoke
+ ___41+[SBSUtils connectionWithExportedObject:]_block_invoke.156
+ ___45-[SBSSysdiagnoseInterface cancelSysdiagnose:]_block_invoke
+ ___45-[SBSSysdiagnoseInterface createSysdiagnose:]_block_invoke
+ ___49-[SBSServer(Internal) cancelSysdiagnoseInternal:]_block_invoke
+ ___49-[SBSServer(Internal) createSysdiagnoseInternal:]_block_invoke
+ ___49-[SBSSysdiagnoseInterface sysdiagnoseHasStarted:]_block_invoke
+ ___60-[SBSServer airDropSysdiagnose:airDropID:completionHandler:]_block_invoke
+ ___74-[SBSSysdiagnoseInterface airDropSysdiagnose:airDropID:completionHandler:]_block_invoke
+ ___78-[SBSServer(Internal) airDropSysdiagnoseInternal:airDropID:completionHandler:]_block_invoke
+ ___block_descriptor_33_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32bs_e27_v24?0"NSURL"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_literal_global.1029
+ ___block_literal_global.1169
+ ___block_literal_global.151
+ ___block_literal_global.153
+ ___block_literal_global.155
+ ___block_literal_global.157
+ ___block_literal_global.159
+ ___block_literal_global.541
+ ___block_literal_global.863
+ _objc_msgSend$airDropSysdiagnose:airDropID:completionHandler:
+ _objc_msgSend$airDropSysdiagnoseInternal:airDropID:completionHandler:
+ _objc_msgSend$airdropServiceDelegate
+ _objc_msgSend$cancelCurrentSysdiagnose:
+ _objc_msgSend$cancelSysdiagnoseInternal:
+ _objc_msgSend$connectionWithExportedObject:
+ _objc_msgSend$createSysdiagnose:
+ _objc_msgSend$createSysdiagnoseInternal:
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$sbConnection
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_retain
+ _objc_retain_x4
- GCC_except_table187
- GCC_except_table192
- GCC_except_table193
- GCC_except_table194
- GCC_except_table195
- GCC_except_table196
- GCC_except_table244
- GCC_except_table245
- GCC_except_table413
- GCC_except_table416
- GCC_except_table419
- GCC_except_table422
- GCC_except_table425
- GCC_except_table428
- GCC_except_table432
- GCC_except_table436
- GCC_except_table444
- GCC_except_table448
- GCC_except_table451
- GCC_except_table454
- GCC_except_table457
- GCC_except_table460
- GCC_except_table466
- GCC_except_table470
- GCC_except_table473
- GCC_except_table476
- GCC_except_table480
- GCC_except_table483
- GCC_except_table486
- GCC_except_table489
- GCC_except_table492
- GCC_except_table496
- GCC_except_table499
- GCC_except_table502
- GCC_except_table505
- GCC_except_table508
- GCC_except_table511
- GCC_except_table514
- GCC_except_table517
- GCC_except_table520
- GCC_except_table542
- GCC_except_table545
- GCC_except_table548
- GCC_except_table551
- GCC_except_table555
- GCC_except_table563
- ___69+[SBSUtils createProxyConnectionForXPCWithExportedObject:connection:]_block_invoke
- ___69+[SBSUtils createProxyConnectionForXPCWithExportedObject:connection:]_block_invoke.146
- ___block_literal_global.1002
- ___block_literal_global.1135
- ___block_literal_global.148
- ___block_literal_global.150
- ___block_literal_global.152
- ___block_literal_global.154
- ___block_literal_global.156
- ___block_literal_global.528
- ___block_literal_global.834
CStrings:
+ "+[SBSUtils connectionWithExportedObject:]_block_invoke"
+ "@\"<SBSAirDropServiceImplementer>\""
+ "Failed to set sysdiagnose started to %d, %@"
+ "J"
+ "Missing Entitlement for cancelling sysdiagnose"
+ "Missing Entitlement for starting sysdiagnose"
+ "SBSAirDropServiceImplementer"
+ "T@\"<SBSAirDropServiceImplementer>\",W,N,V_airdropServiceDelegate"
+ "T@\"<SBSImplementer>\",R,N,V_sbProxy"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSXPCConnection\",R,N,V_sbConnection"
+ "_airdropServiceDelegate"
+ "airDropSysdiagnose:airDropID:completionHandler:"
+ "airDropSysdiagnoseInternal:airDropID:completionHandler:"
+ "airdropServiceDelegate"
+ "cancelCurrentSysdiagnose:"
+ "cancelSysdiagnose:"
+ "cancelSysdiagnoseInternal:"
+ "com.apple.soundboardservices"
+ "connectionWithExportedObject:"
+ "createSysdiagnose:"
+ "createSysdiagnoseInternal:"
+ "initWithDomain:code:userInfo:"
+ "setAirdropServiceDelegate:"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSURL\"@\"NSError\">16"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"
+ "v40@0:8@\"NSURL\"16@\"NSString\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@16@24@?32"
- "+[SBSUtils createProxyConnectionForXPCWithExportedObject:connection:]_block_invoke"
- "I"

```
