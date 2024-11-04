## H16ISPServices

> `/System/Library/PrivateFrameworks/H16ISPServices.framework/H16ISPServices`

```diff

-3.316.903.0.0
-  __TEXT.__text: 0x1e0ac
+3.319.2.0.0
+  __TEXT.__text: 0x1ff24
   __TEXT.__auth_stubs: 0x680
   __TEXT.__gcc_except_tab: 0x594
-  __TEXT.__cstring: 0x8e3f
+  __TEXT.__cstring: 0x7c0e
   __TEXT.__const: 0x58
-  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__unwind_info: 0x2a0
   __DATA_CONST.__got: 0x168
   __DATA_CONST.__const: 0x40
   __AUTH_CONST.__auth_got: 0x348

   - /usr/lib/libIOAccessoryManager.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 351
-  Symbols:   628
-  CStrings:  1500
+  Functions: 397
+  Symbols:   732
+  CStrings:  1476
 
CStrings:
+ "TB_FATAL: invalid value: unexpected case value, %!l(MISSING)lx"
+ "TB_FATAL: invalid value: unexpected case value, %!l(MISSING)lx (%!s(MISSING):%!d(MISSING))\n"
+ "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[40c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
- "TB_ASSERT: (ispirexclavekitmodule_ispexclavecoreadsettings__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreAdSettings\""
- "TB_ASSERT: (ispirexclavekitmodule_ispexclavecorechdpcset__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreChDPCSet\""
- "TB_ASSERT: (ispirexclavekitmodule_ispexclavecorechinfoset2__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreChInfoSet2\""
- "TB_ASSERT: (ispirexclavekitmodule_ispexclavecorechinfoset__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreChInfoSet\""
- "TB_ASSERT: (ispirexclavekitmodule_ispexclavecorechrunkit__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreChRunKit\""
- "TB_ASSERT: (ispirexclavekitmodule_ispexclavecorechrunkitalgo__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreChRunKitAlgo\""
- "TB_ASSERT: (ispirexclavekitmodule_ispexclavecorechsensormetadata2__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreChSensorMetadata2\""
- "TB_ASSERT: (ispirexclavekitmodule_ispexclavecorechsensormetadata__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreChSensorMetadata\""
- "TB_ASSERT: (ispirexclavekitmodule_ispexclavecorechsensormetadatav3__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreChSensorMetadataV3\""
- "TB_ASSERT: (ispirexclavekitmodule_ispexclavecoreexclavebootarg__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreExclaveBootArg\""
- "TB_ASSERT: (ispirexclavekitmodule_ispexclavecoreexclavechconfigurationstatusread__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreExclaveChConfigurationStatusRead\""
- "TB_ASSERT: (ispirexclavekitmodule_ispexclavecoreexclavechpropertyread__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreExclaveChPropertyRead\""
- "TB_ASSERT: (ispirexclavekitmodule_ispexclavecoreexclavechpropertywrite__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreExclaveChPropertyWrite\""
- "TB_ASSERT: (ispirexclavekitmodule_ispexclavecorefiltration__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreFiltration\""
- "TB_ASSERT: (isprgbexclavekitmodule_ispexclavecorechdpcset__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPRGBExclaveKitModule.ISPExclaveCoreChDPCSet\""
- "TB_ASSERT: (isprgbexclavekitmodule_ispexclavecorechinfoset2__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPRGBExclaveKitModule.ISPExclaveCoreChInfoSet2\""
- "TB_ASSERT: (isprgbexclavekitmodule_ispexclavecorechinfoset__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPRGBExclaveKitModule.ISPExclaveCoreChInfoSet\""
- "TB_ASSERT: (isprgbexclavekitmodule_ispexclavecorechrunkit__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPRGBExclaveKitModule.ISPExclaveCoreChRunKit\""
- "TB_ASSERT: (isprgbexclavekitmodule_ispexclavecorechrunkitalgo__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPRGBExclaveKitModule.ISPExclaveCoreChRunKitAlgo\""
- "TB_ASSERT: (isprgbexclavekitmodule_ispexclavecorechsensormetadata2__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPRGBExclaveKitModule.ISPExclaveCoreChSensorMetadata2\""
- "TB_ASSERT: (isprgbexclavekitmodule_ispexclavecorechsensormetadata__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPRGBExclaveKitModule.ISPExclaveCoreChSensorMetadata\""
- "TB_ASSERT: (isprgbexclavekitmodule_ispexclavecorechsensormetadatav3__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPRGBExclaveKitModule.ISPExclaveCoreChSensorMetadataV3\""
- "TB_ASSERT: (isprgbexclavekitmodule_ispexclavecoreexclavebootarg__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPRGBExclaveKitModule.ISPExclaveCoreExclaveBootArg\""
- "TB_ASSERT: (isprgbexclavekitmodule_ispexclavecoreexclavechpropertyread__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPRGBExclaveKitModule.ISPExclaveCoreExclaveChPropertyRead\""
- "TB_ASSERT: (isprgbexclavekitmodule_ispexclavecoreexclavechpropertywrite__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPRGBExclaveKitModule.ISPExclaveCoreExclaveChPropertyWrite\""
- "TB_ASSERT: (isprgbexclavekitmodule_ispexclavecorefiltration__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPRGBExclaveKitModule.ISPExclaveCoreFiltration\""
- "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[32c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"

```
