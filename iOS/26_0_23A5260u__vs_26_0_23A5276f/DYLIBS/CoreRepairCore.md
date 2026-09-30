## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

-921.0.34.0.0
-  __TEXT.__text: 0x7f538
+921.0.65.0.0
+  __TEXT.__text: 0x80e74
   __TEXT.__auth_stubs: 0x1670
-  __TEXT.__objc_methlist: 0x38a4
+  __TEXT.__objc_methlist: 0x396c
   __TEXT.__const: 0x7f0
-  __TEXT.__oslogstring: 0x8aeb
-  __TEXT.__cstring: 0x54f5
-  __TEXT.__gcc_except_tab: 0x14c8
-  __TEXT.__unwind_info: 0x1100
-  __TEXT.__objc_classname: 0x7c8
-  __TEXT.__objc_methname: 0x7bde
-  __TEXT.__objc_methtype: 0x14a7
-  __TEXT.__objc_stubs: 0x60e0
+  __TEXT.__oslogstring: 0x8d80
+  __TEXT.__cstring: 0x567e
+  __TEXT.__gcc_except_tab: 0x1524
+  __TEXT.__unwind_info: 0x1138
+  __TEXT.__objc_classname: 0x7d0
+  __TEXT.__objc_methname: 0x7dd0
+  __TEXT.__objc_methtype: 0x14ba
+  __TEXT.__objc_stubs: 0x62c0
   __DATA_CONST.__got: 0x550
-  __DATA_CONST.__const: 0x870
+  __DATA_CONST.__const: 0x8e0
   __DATA_CONST.__objc_classlist: 0x2b0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ed0
+  __DATA_CONST.__objc_selrefs: 0x1f50
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x1e8
-  __DATA_CONST.__objc_arraydata: 0x890
+  __DATA_CONST.__objc_superrefs: 0x1f0
+  __DATA_CONST.__objc_arraydata: 0x868
   __AUTH_CONST.__auth_got: 0xb48
-  __AUTH_CONST.__const: 0x480
-  __AUTH_CONST.__cfstring: 0x6a00
-  __AUTH_CONST.__objc_const: 0x5788
-  __AUTH_CONST.__objc_arrayobj: 0x588
+  __AUTH_CONST.__const: 0x4a0
+  __AUTH_CONST.__cfstring: 0x6c20
+  __AUTH_CONST.__objc_const: 0x57e8
+  __AUTH_CONST.__objc_arrayobj: 0x570
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH.__objc_data: 0xeb0
-  __DATA.__objc_ivar: 0x2e0
+  __DATA.__objc_ivar: 0x2e8
   __DATA.__data: 0x690
-  __DATA.__bss: 0xb0
+  __DATA.__bss: 0xc8
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__bss: 0x100

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: 05772402-23D0-36D3-BE57-07F1C5998411
-  Functions: 2203
-  Symbols:   7295
-  CStrings:  4561
+  UUID: B3D5332A-B696-3F06-89A7-B41BE0D8AD41
+  Functions: 2228
+  Symbols:   7368
+  CStrings:  4642
 
Symbols:
+ +[CRDeviceMap getKeysWithSPC:]
+ +[CRFDRUtils isPrimaryDataClassSupported:]
+ +[CRFDRUtils isRepairASIDSupported]
+ +[CRFDRUtils isRepairASIDSupported].cold.1
+ +[CRFDRUtils isRepairASIDSupported].cold.2
+ +[CRFDRUtils isRepairASIDSupported].cold.3
+ +[CRFDRUtils(ComponentState) hasUnsealedComponent:]
+ +[CRFDRUtils(ComponentState) hasUnsealedComponentRequireOSUpdate]
+ +[CRPersonalizationManager(SOCKS) SOCKSInfo]
+ +[CRPersonalizationManager(SOCKS) setSOCKSInfo:]
+ -[CRCCertificate dumpAttestationPayload]
+ -[CRCCertificate setDumpAttestationPayload:]
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.24
+ -[CRFDRGen7DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.7
+ -[CRPersonalizationManager getRepairTicket:useRepairAudience:error:]
+ -[CRPersonalizationManager getRepairTicket:useRepairAudience:error:].cold.1
+ -[CRPreflight componentsWithPrimaryKeys:]
+ -[CRPreflightController _diskImageSupportPreflight]
+ -[CRPreflightController getPreflightEndpoint]
+ -[CRPreflightController init]
+ -[CRPreflightController preflightServiceName]
+ -[CRPreflightController setPreflightServiceName:]
+ -[CRRepairHistory _getCachedCAAData]
+ -[CRRepairHistory getCachedCAA]
+ -[CRUserDefaults _initWithSuiteName:internalOnly:]
+ -[CRUserDefaults _initWithSuiteName:internalOnly:].cold.1
+ GCC_except_table11
+ GCC_except_table15
+ GCC_except_table25
+ GCC_except_table28
+ GCC_except_table31
+ _OBJC_IVAR_$_CRCCertificate._dumpAttestationPayload
+ _OBJC_IVAR_$_CRPreflightController._preflightServiceName
+ _SOCKSProxyInfo
+ __OBJC_$_CLASS_METHODS_CRPersonalizationManager(SOCKS)
+ ___38-[CRPreflightController sign:keyBlob:]_block_invoke.157
+ ___48-[CRPreflightController queryRepairDelta:error:]_block_invoke.203
+ ___49-[CRUserDefaults initWithSuiteName:internalOnly:]_block_invoke
+ ___50-[CRPreflightController verify:signature:keyBlob:]_block_invoke.167
+ ___51-[CRPreflightController _diskImageSupportPreflight]_block_invoke
+ ___51-[CRPreflightController _diskImageSupportPreflight]_block_invoke.164
+ ___55-[CRPreflightController issueRepairCert:keyBlob:error:]_block_invoke.205
+ ___60-[CRFDRBaseDeviceHandler challengeComponentsWith:withReply:]_block_invoke.241
+ ___67-[CRPreflightController challengeStrongComponents:responses:error:]_block_invoke.211
+ ___69-[CRCAttestationManager getStrongComponentsWithError:resultobtained:]_block_invoke.147
+ ___71-[CRCAttestationManager sendChallengeRequestWith:serverResponse:error:]_block_invoke.225
+ ___73-[CRCAttestationManager challengeComponentsWith:challengeResponse:error:]_block_invoke.155
+ ___75-[CRCAttestationManager sendCertIssueRequestWith:serverCertResponse:error:]_block_invoke.244
+ ___92-[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:]_block_invoke.105
+ ___92-[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:]_block_invoke.51
+ ___92-[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:]_block_invoke.51.cold.1
+ ___92-[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:]_block_invoke.51.cold.2
+ ___92-[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:]_block_invoke.57
+ ___block_descriptor_32_e40_"NSDictionary"24?0"NSDictionary"8^16l
+ ___block_descriptor_40_e8_32r_e16_v16?0"NSData"8lr32l8
+ ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_tmp.151
+ ___block_descriptor_tmp.170
+ ___block_literal_global.102
+ ___block_literal_global.153
+ ___block_literal_global.166
+ ___block_literal_global.167
+ ___block_literal_global.169
+ ___block_literal_global.172
+ ___block_literal_global.182
+ ___block_literal_global.184
+ ___block_literal_global.195
+ ___block_literal_global.202
+ ___block_literal_global.205
+ ___block_literal_global.213
+ ___block_literal_global.47
+ ___block_literal_global.69
+ ___block_literal_global.86
+ ___block_literal_global.89
+ _generateRepairTicket_block_invoke_4.cold.8
+ _initWithSuiteName:internalOnly:.instance
+ _initWithSuiteName:internalOnly:.onceToken
+ _objc_msgSend$SOCKSInfo
+ _objc_msgSend$_diskImageSupportPreflight
+ _objc_msgSend$_getCachedCAAData
+ _objc_msgSend$_initWithSuiteName:internalOnly:
+ _objc_msgSend$componentsWithPrimaryKeys:
+ _objc_msgSend$dumpAttestationPayload
+ _objc_msgSend$getCachedCAA
+ _objc_msgSend$getKeysWithSPC:
+ _objc_msgSend$getPreflightEndpoint
+ _objc_msgSend$getRepairTicket:useRepairAudience:error:
+ _objc_msgSend$hasUnsealedComponent:
+ _objc_msgSend$hasUnsealedComponentRequireOSUpdate
+ _objc_msgSend$isPrimaryDataClassSupported:
+ _objc_msgSend$isRepairASIDSupported
+ _objc_msgSend$setDumpAttestationPayload:
+ _objc_msgSend$setSOCKSInfo:
- +[CRFDRUtils hasMesaUnsealedData]
- +[CRFDRUtils hasMesaUnsealedData].cold.1
- -[CRPersonalizationManager getRepairTicket:error:]
- -[CRUserDefaults initWithSuiteName:internalOnly:].cold.1
- GCC_except_table17
- GCC_except_table26
- __OBJC_$_CLASS_METHODS_CRPersonalizationManager
- ___38-[CRPreflightController sign:keyBlob:]_block_invoke.153
- ___48-[CRPreflightController queryRepairDelta:error:]_block_invoke.192
- ___50-[CRPreflightController verify:signature:keyBlob:]_block_invoke.157
- ___55-[CRPreflightController issueRepairCert:keyBlob:error:]_block_invoke.194
- ___60-[CRFDRBaseDeviceHandler challengeComponentsWith:withReply:]_block_invoke.244
- ___67-[CRPreflightController challengeStrongComponents:responses:error:]_block_invoke.200
- ___69-[CRCAttestationManager getStrongComponentsWithError:resultobtained:]_block_invoke.121
- ___71-[CRCAttestationManager sendChallengeRequestWith:serverResponse:error:]_block_invoke.199
- ___73-[CRCAttestationManager challengeComponentsWith:challengeResponse:error:]_block_invoke.129
- ___75-[CRCAttestationManager sendCertIssueRequestWith:serverCertResponse:error:]_block_invoke.218
- ___92-[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:]_block_invoke.37
- ___92-[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:]_block_invoke.37.cold.1
- ___92-[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:]_block_invoke.37.cold.2
- ___92-[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:]_block_invoke.43
- ___92-[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:]_block_invoke.79
- ___block_descriptor_tmp.150
- ___block_descriptor_tmp.169
- ___block_literal_global.152
- ___block_literal_global.156
- ___block_literal_global.159
- ___block_literal_global.161
- ___block_literal_global.174
- ___block_literal_global.176
- ___block_literal_global.190
- ___block_literal_global.192
- ___block_literal_global.200
- ___block_literal_global.208
- ___block_literal_global.46
- ___block_literal_global.61
- ___block_literal_global.78
- ___block_literal_global.81
- ___block_literal_global.94
- _objc_msgSend$getRepairTicket:error:
CStrings:
+ "!"
+ "/tmp/attestRequest.xml"
+ "/tmp/certificatePEM"
+ "/tmp/challengeRequest.xml"
+ "/tmp/challengeResponse.xml"
+ "/tmp/oidDER"
+ "/tmp/parsedCert"
+ "/tmp/serverCertResponse"
+ "@\"NSDictionary\"24@?0@\"NSDictionary\"8^@16"
+ "Adding SrvP to properties"
+ "B36@0:8^@16B24^@28"
+ "BackGlass failed preflight proceeding"
+ "Battery failed preflight"
+ "Cached CAA not found"
+ "Camera failed preflight"
+ "CameraUsingProperty failed preflight proceeding"
+ "Cover Glass failed preflight proceeding"
+ "Display failed preflight"
+ "Dump attestation payload: %@"
+ "DumpAttestationPayload"
+ "Enclosure failed preflight proceeding"
+ "FaceID failed preflight"
+ "Failed to enable SOCKS proxy: %d"
+ "Failed to enable SSO: %d"
+ "Failed to get 'supm' property"
+ "Failed to set TATSU server URL: %d"
+ "Failed to set socks info"
+ "Got reply from %@"
+ "NOT_FOUND"
+ "Overriding useRepairAudience: %d"
+ "PART_LOGIC_BOARD_ASSEM"
+ "Reading CAA from file"
+ "Reading CAA from user defaults"
+ "SOCKS"
+ "SOCKSInfo"
+ "Setting FWKS TATSU server URL"
+ "T@\"NSString\",&,N,V_preflightServiceName"
+ "TB,N,V_dumpAttestationPayload"
+ "TouchID failed preflight"
+ "Unexpected audience"
+ "Updated unsealed: %@"
+ "Use Repair Audience"
+ "Volume Button failed preflight proceeding"
+ "_diskImageSupportPreflight"
+ "_dumpAttestationPayload"
+ "_getCachedCAAData"
+ "_initWithSuiteName:internalOnly:"
+ "_preflightServiceName"
+ "cachedCAACert"
+ "com.apple.diskimagecorerepair.preflightControl"
+ "componentsWithPrimaryKeys:"
+ "dumpAttestationPayload"
+ "getCachedCAA"
+ "getKeysWithSPC:"
+ "getPreflightEndpoint"
+ "getRepairTicket:useRepairAudience:error:"
+ "hasUnsealedComponent:"
+ "hasUnsealedComponentRequireOSUpdate"
+ "https://ac-gs.apple.com:443"
+ "isPrimaryDataClassSupported:"
+ "isRepairASIDSupported"
+ "preflightServiceName"
+ "setDumpAttestationPayload:"
+ "setPreflightServiceName:"
+ "setSOCKSInfo:"
+ "supm"
+ "supm: %@"
+ "useRepairAudience"
- "DumpBAARequest"
- "PART_LOGIC_BOARD"
- "component failed preflight proceeding"
- "getRepairTicket:error:"
- "hasMesaUnsealedData"

```
