## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

```diff

-3.316.903.0.0
-  __TEXT.__text: 0x1bbe10
+3.319.2.0.0
+  __TEXT.__text: 0x1bdec4
   __TEXT.__auth_stubs: 0x3320
   __TEXT.__init_offsets: 0x18
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__const: 0x228cc
-  __TEXT.__oslogstring: 0x1c1b7
-  __TEXT.__cstring: 0x1a6ba
-  __TEXT.__gcc_except_tab: 0x5cc0
-  __TEXT.__unwind_info: 0x3c40
+  __TEXT.__const: 0x229bc
+  __TEXT.__oslogstring: 0x1c07b
+  __TEXT.__cstring: 0x1961f
+  __TEXT.__gcc_except_tab: 0x5cd0
+  __TEXT.__unwind_info: 0x3c28
   __TEXT.__eh_frame: 0x98
   __TEXT.__objc_classname: 0x89
   __TEXT.__objc_methname: 0x1c61
   __TEXT.__objc_methtype: 0x11fa
   __TEXT.__objc_stubs: 0x1f60
-  __DATA_CONST.__got: 0x3208
-  __DATA_CONST.__const: 0x84d0
+  __DATA_CONST.__got: 0x3210
+  __DATA_CONST.__const: 0x84e8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0x19a0
-  __AUTH_CONST.__auth_ptr: 0xa0
-  __AUTH_CONST.__const: 0x2808
-  __AUTH_CONST.__cfstring: 0x9780
+  __AUTH_CONST.__auth_ptr: 0x98
+  __AUTH_CONST.__const: 0x2828
+  __AUTH_CONST.__cfstring: 0x98c0
   __AUTH_CONST.__objc_const: 0x808
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x48

   __DATA.__common: 0x54
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x110
-  __DATA_DIRTY.__bss: 0x920
-  __DATA_DIRTY.__common: 0x5420
+  __DATA_DIRTY.__bss: 0x924
+  __DATA_DIRTY.__common: 0x54d0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5685
-  Symbols:   9151
-  CStrings:  6395
+  Functions: 5739
+  Symbols:   9264
+  CStrings:  6385
 
Symbols:
+ _CFStringHasPrefix
+ __ZN6H16ISP12H16ISPDevice13SetupConclaveEjPb
+ __ZN6H16ISP12H16ISPDevice16DCS_FPGASyncCtrlEjbt
+ __ZN6H16ISP12H16ISPDevice17GetDriverKextInfoEP18VersionControlInfo
+ __ZN6H16ISP12H16ISPDevice17PowerOnExclaveKitEjPb
+ __ZN6H16ISP12H16ISPDevice18SetDeskViewEnabledEjb
+ __ZN6H16ISP12H16ISPDevice22DCS_FPGASyncOffsetCtrlEjh
+ __ZNK6H16ISP12H16ISPDevice19GetNumCameraConfigsEj
+ _kFigCaptureStreamProperty_DeskViewEnabled
- _CVAFaceTrackingLiteCopyDecodedOutput
- __ZN6H16ISP12H16ISPDevice13SetupConclaveEj
- __ZN6H16ISP12H16ISPDevice17PowerOnExclaveKitEj
- __ZN6H16ISP12H16ISPDevice19GetNumCameraConfigsEj
- __ZN6H16ISP34H16ISPGraphExclaveFaceTrackingNode29AddSecureTrackedFacesMetadataEPNS_24H16ISPFilterGraphMessageE60isprgbexclavekitmodule_ispexclavecorechrunkitfaceprocessrsltb
CStrings:
+ "%!s(MISSING) - %!d(MISSING) configurations detected for channel %!d(MISSING)\n"
+ "%!s(MISSING) - [Exclaves]: Message Drop Timeout!, requestid=0x%!X(MISSING)\n"
+ "%!s(MISSING) - [Exclaves]: Message Drop due to above queue size!, requestid=0x%!X(MISSING)\n"
+ "%!s(MISSING) - [Exclaves]: Sync Node being deconstructed!\n"
+ "%!s(MISSING) - [Exclaves]: Sync Node current message requestID=0x%!X(MISSING), frameID=%!U(MISSING)\n"
+ "%!s(MISSING) - [Exclaves]: Sync node activated!\n"
+ "%!s(MISSING) - [Exclaves]: Sync node being deactivated!\n"
+ "%!s(MISSING) - bad array value at idx=%!l(MISSING)d\n"
+ "%!s(MISSING) - chan: %!d(MISSING), numChannels: %!d(MISSING), index: %!d(MISSING), numConfigs: %!d(MISSING)\n"
+ "%!s(MISSING) - channel=%!u(MISSING) failed to set property=0x%!x(MISSING) value=%!u(MISSING)\n"
+ "%!s(MISSING) - error: 0x%!X(MISSING)\n"
+ "%!s(MISSING) - generic debug property/value pairs must be specified as an array\n"
+ "%!s(MISSING) - invalid preference key for channel=%!u(MISSING)\n"
+ "/usr/local/share/firmware/isp/CmPM-CALm.DAT"
+ "CALm"
+ "DCSDataFileUnload_Private"
+ "DCSFPGASyncControl_Private"
+ "DCSFPGASyncControl_channel_Private"
+ "DCSFPGASyncControl_enable_Private"
+ "DCSFPGASyncControl_frameRate_Private"
+ "DCSFPGASyncOffsetControl_Private"
+ "DCSFPGASyncOffsetControl_channel_Private"
+ "DCSFPGASyncOffsetControl_offset_Private"
+ "ExclavePreferenceApplyFiltrationValues"
+ "ExclavePreferenceApplyGenericValues"
+ "ExclavePreferenceRegisterNotifications"
+ "Front"
+ "FrontInfrared"
+ "FrontSuperWide"
+ "ISPDebug%!s(MISSING)PropertyWrite"
+ "Invalid RGB Conclave Handle\n"
+ "SetDeskViewEnabled"
+ "TB_FATAL: invalid value: unexpected case value, %!l(MISSING)lx"
+ "TB_FATAL: invalid value: unexpected case value, %!l(MISSING)lx (%!s(MISSING):%!d(MISSING))\n"
+ "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[40c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"
- "%!s(MISSING) - Conclave setup failed\n"
- "%!s(MISSING) - Power OFF EK Success\n"
- "%!s(MISSING) - [Exclaves]\n"
- "%!s(MISSING) - [Exclaves]: H16ISPGraphExclaveFaceTrackingNode::%!s(MISSING) index: %!z(MISSING)u AngleInfoRoll: %!f(MISSING) Rect[%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)] Confidence %!f(MISSING) \n"
- "AddSecureTrackedFacesMetadata"
- "ExclaveApplyFiltrationDebugPreferences"
- "ExclaveRegisterPreferenceNotifications"
- "Invalid RGB conclave client handle\n"
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
- "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::%!s(MISSING) CVAFaceTrackingLiteCopyDecodedOutput failed, err=0x%!X(MISSING) \n"
- "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::%!s(MISSING) RunKit FT reqID:0x%!x(MISSING) channel %!d(MISSING)\n"
- "[Exclaves] H16ISPGraphExclaveFaceTrackingNode::%!s(MISSING) Skipped processing secure face tracking algorithm\n"
- "[Exclaves] H16ISPGraphExclaveSyncNode::%!s(MISSING) Message Drop Timeout!, requestid=0x%!X(MISSING)\n"
- "[Exclaves] H16ISPGraphExclaveSyncNode::%!s(MISSING) Message Drop due to above queue size!, requestid=0x%!X(MISSING)\n"
- "[Exclaves] H16ISPGraphExclaveSyncNode::onActivate\n"
- "[Exclaves] H16ISPGraphExclaveSyncNode::onDeactivate\n"
- "[Exclaves]: H16ISPGraphExclaveFaceTrackingNode::%!s(MISSING) EK Face Kit Runkit failed, tberr %!d(MISSING) ipcRet %!d(MISSING)\n"
- "[Exclaves]: RGB Face Tracking: channel=%!u(MISSING)\n"
- "[Exclaves]: Sync Node current message requestID=0x%!X(MISSING), frameID=%!U(MISSING)\n"
- "^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[32c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16"

```
