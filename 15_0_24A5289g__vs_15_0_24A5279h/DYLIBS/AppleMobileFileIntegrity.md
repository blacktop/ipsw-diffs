## AppleMobileFileIntegrity

> `/System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/Versions/A/AppleMobileFileIntegrity`

```diff

-938.0.19.0.0
-  __TEXT.__text: 0xff14
+938.0.16.0.0
+  __TEXT.__text: 0xf740
   __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x4e0
+  __TEXT.__objc_methlist: 0x4c4
   __TEXT.__const: 0x220
-  __TEXT.__cstring: 0x1bf2
-  __TEXT.__oslogstring: 0x13d9
-  __TEXT.__gcc_except_tab: 0x278
-  __TEXT.__unwind_info: 0x3e8
-  __TEXT.__objc_classname: 0x96
-  __TEXT.__objc_methname: 0x1288
+  __TEXT.__cstring: 0x1b7c
+  __TEXT.__oslogstring: 0x1288
+  __TEXT.__gcc_except_tab: 0x24c
+  __TEXT.__unwind_info: 0x400
+  __TEXT.__objc_classname: 0x98
+  __TEXT.__objc_methname: 0x1263
   __TEXT.__objc_methtype: 0x451
-  __TEXT.__objc_stubs: 0xe00
+  __TEXT.__objc_stubs: 0xdc0
   __DATA_CONST.__got: 0x208
   __DATA_CONST.__const: 0x650
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x450
+  __DATA_CONST.__objc_selrefs: 0x448
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __AUTH_CONST.__auth_got: 0x330

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 362
-  Symbols:   828
-  CStrings:  202
+  Functions: 352
+  Symbols:   817
+  CStrings:  197
 
Symbols:
+ -[amfidConnection .cxx_destruct]
+ -[amfidConnection commitProfile:]
+ -[amfidConnection dealloc]
+ -[amfidConnection getACMUPPStateWithError:]
+ -[amfidConnection getStagedProfilewithError:]
+ -[amfidConnection init]
+ -[amfidConnection initiateDataMigration]
+ -[amfidConnection removeManagedState]
+ -[amfidConnection removeTrustforUuid:]
+ -[amfidConnection setDemoState:]
+ -[amfidConnection setManagedState:]
+ -[amfidConnection setSupervisedState:]
+ -[amfidConnection setTrustforUuid:withSignature:andSignType:]
+ -[amfidConnection signTeamId:withSignType:withLAContext:withError:]
+ -[amfidConnection stageProfile:]
+ AMFIGetSEPDeviceState.cold.1
+ GCC_except_table14
+ GCC_except_table17
+ GCC_except_table2
+ GCC_except_table20
+ GCC_except_table23
+ GCC_except_table26
+ GCC_except_table29
+ GCC_except_table32
+ GCC_except_table35
+ GCC_except_table38
+ GCC_except_table41
+ GCC_except_table8
+ GCC_except_table9
+ OBJC_IVAR_$_amfidConnection.connection
+ _OBJC_CLASS_$_amfidConnection
+ _OBJC_METACLASS_$_amfidConnection
+ __32-[amfidConnection setDemoState:]_block_invoke.36
+ __32-[amfidConnection setDemoState:]_block_invoke.cold.1
+ __32-[amfidConnection stageProfile:]_block_invoke.44
+ __32-[amfidConnection stageProfile:]_block_invoke.cold.1
+ __33-[amfidConnection commitProfile:]_block_invoke.49
+ __33-[amfidConnection commitProfile:]_block_invoke.cold.1
+ __35-[amfidConnection setManagedState:]_block_invoke.37
+ __35-[amfidConnection setManagedState:]_block_invoke.cold.1
+ __37-[amfidConnection removeManagedState]_block_invoke.34
+ __37-[amfidConnection removeManagedState]_block_invoke.cold.1
+ __38-[amfidConnection removeTrustforUuid:]_block_invoke.35
+ __38-[amfidConnection removeTrustforUuid:]_block_invoke.cold.1
+ __38-[amfidConnection setSupervisedState:]_block_invoke.38
+ __38-[amfidConnection setSupervisedState:]_block_invoke.cold.1
+ __40-[amfidConnection initiateDataMigration]_block_invoke.30
+ __40-[amfidConnection initiateDataMigration]_block_invoke.30.cold.1
+ __40-[amfidConnection initiateDataMigration]_block_invoke.cold.1
+ __43-[amfidConnection getACMUPPStateWithError:]_block_invoke.32
+ __43-[amfidConnection getACMUPPStateWithError:]_block_invoke.cold.1
+ __45-[amfidConnection getStagedProfilewithError:]_block_invoke.45
+ __45-[amfidConnection getStagedProfilewithError:]_block_invoke.cold.1
+ __61-[amfidConnection setTrustforUuid:withSignature:andSignType:]_block_invoke.39
+ __61-[amfidConnection setTrustforUuid:withSignature:andSignType:]_block_invoke.cold.1
+ __67-[amfidConnection signTeamId:withSignType:withLAContext:withError:]_block_invoke.40
+ __67-[amfidConnection signTeamId:withSignType:withLAContext:withError:]_block_invoke.cold.1
+ __OBJC_$_INSTANCE_METHODS_amfidConnection
+ __OBJC_$_INSTANCE_VARIABLES_amfidConnection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_amfidProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_amfidProtocol
+ __OBJC_CLASS_RO_$_amfidConnection
+ __OBJC_LABEL_PROTOCOL_$_amfidProtocol
+ __OBJC_METACLASS_RO_$_amfidConnection
+ __OBJC_PROTOCOL_$_amfidProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_amfidProtocol
+ ___32-[amfidConnection setDemoState:]_block_invoke
+ ___32-[amfidConnection stageProfile:]_block_invoke
+ ___33-[amfidConnection commitProfile:]_block_invoke
+ ___35-[amfidConnection setManagedState:]_block_invoke
+ ___37-[amfidConnection removeManagedState]_block_invoke
+ ___38-[amfidConnection removeTrustforUuid:]_block_invoke
+ ___38-[amfidConnection setSupervisedState:]_block_invoke
+ ___40-[amfidConnection initiateDataMigration]_block_invoke
+ ___43-[amfidConnection getACMUPPStateWithError:]_block_invoke
+ ___45-[amfidConnection getStagedProfilewithError:]_block_invoke
+ ___61-[amfidConnection setTrustforUuid:withSignature:andSignType:]_block_invoke
+ ___67-[amfidConnection signTeamId:withSignType:withLAContext:withError:]_block_invoke
+ __getAuxiliarySignature
+ _nsErrorToAMFIReturn
+ _objc_msgSend$commitProfile:
+ _objc_msgSend$commitProfile:withReply:
+ _objc_msgSend$getACMUPPStateWithError:
+ _objc_msgSend$getACMUPPStateWithReply:
+ _objc_msgSend$getStagedProfilewithError:
+ _objc_msgSend$getStagedProfilewithReply:
+ _objc_msgSend$setTrustforUuid:withSignature:andSignType:
+ _objc_msgSend$setTrustforUuid:withSignature:withSignType:withReply:
+ _objc_msgSend$signTeamId:withSignType:withLAContext:withError:
+ _objc_msgSend$stageProfile:withReply:
- +[AMFIConnection newConnection]
- -[AMFIConnection .cxx_destruct]
- -[AMFIConnection commitProfileForUuid:]
- -[AMFIConnection dealloc]
- -[AMFIConnection getSEPStateWithError:]
- -[AMFIConnection getStagedProfileWithError:]
- -[AMFIConnection init]
- -[AMFIConnection initiateDataMigration]
- -[AMFIConnection removeManagedState]
- -[AMFIConnection removeTrustforUuid:]
- -[AMFIConnection setDemoState:]
- -[AMFIConnection setManagedState:]
- -[AMFIConnection setSupervisedState:]
- -[AMFIConnection setTrustForUuid:withSignature:withSignType:]
- -[AMFIConnection signTeamID:withSignType:withLAContext:withError:]
- -[AMFIConnection stageProfileForUuid:]
- AMFIDemoModeSetState.cold.1
- AMFIMDMModeEnroll.cold.1
- AMFIMDMModeRemove.cold.1
- AMFIProfileRequiresReboot.cold.2
- AMFIProfileScheduleTrust.cold.3
- AMFIProfileScheduleTrust.cold.4
- AMFIProfileSetTrustWithOptions.cold.5
- AMFIProfileSetTrustWithOptions.cold.6
- AMFISupervisedModeSetState.cold.1
- GCC_except_table10
- GCC_except_table15
- GCC_except_table18
- GCC_except_table21
- GCC_except_table24
- GCC_except_table27
- GCC_except_table30
- GCC_except_table33
- GCC_except_table36
- GCC_except_table39
- GCC_except_table42
- OBJC_IVAR_$_AMFIConnection.connection
- _NSErrorToAMFIReturn
- _OBJC_CLASS_$_AMFIConnection
- _OBJC_METACLASS_$_AMFIConnection
- __31-[AMFIConnection setDemoState:]_block_invoke.48
- __31-[AMFIConnection setDemoState:]_block_invoke.cold.1
- __34-[AMFIConnection setManagedState:]_block_invoke.49
- __34-[AMFIConnection setManagedState:]_block_invoke.cold.1
- __36-[AMFIConnection removeManagedState]_block_invoke.50
- __36-[AMFIConnection removeManagedState]_block_invoke.cold.1
- __37-[AMFIConnection removeTrustforUuid:]_block_invoke.46
- __37-[AMFIConnection removeTrustforUuid:]_block_invoke.cold.1
- __37-[AMFIConnection setSupervisedState:]_block_invoke.47
- __37-[AMFIConnection setSupervisedState:]_block_invoke.cold.1
- __38-[AMFIConnection stageProfileForUuid:]_block_invoke.39
- __38-[AMFIConnection stageProfileForUuid:]_block_invoke.cold.1
- __39-[AMFIConnection commitProfileForUuid:]_block_invoke.44
- __39-[AMFIConnection commitProfileForUuid:]_block_invoke.cold.1
- __39-[AMFIConnection getSEPStateWithError:]_block_invoke.33
- __39-[AMFIConnection getSEPStateWithError:]_block_invoke.cold.1
- __39-[AMFIConnection initiateDataMigration]_block_invoke.31
- __39-[AMFIConnection initiateDataMigration]_block_invoke.31.cold.1
- __39-[AMFIConnection initiateDataMigration]_block_invoke.cold.1
- __44-[AMFIConnection getStagedProfileWithError:]_block_invoke.40
- __44-[AMFIConnection getStagedProfileWithError:]_block_invoke.cold.1
- __61-[AMFIConnection setTrustForUuid:withSignature:withSignType:]_block_invoke.45
- __61-[AMFIConnection setTrustForUuid:withSignature:withSignType:]_block_invoke.cold.1
- __66-[AMFIConnection signTeamID:withSignType:withLAContext:withError:]_block_invoke.35
- __66-[AMFIConnection signTeamID:withSignType:withLAContext:withError:]_block_invoke.cold.1
- __OBJC_$_CLASS_METHODS_AMFIConnection
- __OBJC_$_INSTANCE_METHODS_AMFIConnection
- __OBJC_$_INSTANCE_VARIABLES_AMFIConnection
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AMFIProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_AMFIProtocol
- __OBJC_CLASS_RO_$_AMFIConnection
- __OBJC_LABEL_PROTOCOL_$_AMFIProtocol
- __OBJC_METACLASS_RO_$_AMFIConnection
- __OBJC_PROTOCOL_$_AMFIProtocol
- __OBJC_PROTOCOL_REFERENCE_$_AMFIProtocol
- ___31-[AMFIConnection setDemoState:]_block_invoke
- ___34-[AMFIConnection setManagedState:]_block_invoke
- ___36-[AMFIConnection removeManagedState]_block_invoke
- ___37-[AMFIConnection removeTrustforUuid:]_block_invoke
- ___37-[AMFIConnection setSupervisedState:]_block_invoke
- ___38-[AMFIConnection stageProfileForUuid:]_block_invoke
- ___39-[AMFIConnection commitProfileForUuid:]_block_invoke
- ___39-[AMFIConnection getSEPStateWithError:]_block_invoke
- ___39-[AMFIConnection initiateDataMigration]_block_invoke
- ___44-[AMFIConnection getStagedProfileWithError:]_block_invoke
- ___61-[AMFIConnection setTrustForUuid:withSignature:withSignType:]_block_invoke
- ___66-[AMFIConnection signTeamID:withSignType:withLAContext:withError:]_block_invoke
- _objc_msgSend$commitProfileForUuid:
- _objc_msgSend$commitProfileForUuid:withReply:
- _objc_msgSend$getSEPStateWithError:
- _objc_msgSend$getSEPStateWithReply:
- _objc_msgSend$getStagedProfileWithError:
- _objc_msgSend$getStagedProfileWithReply:
- _objc_msgSend$newConnection
- _objc_msgSend$setTrustForUuid:withSignature:withSignType:
- _objc_msgSend$setTrustForUuid:withSignature:withSignType:withReply:
- _objc_msgSend$signTeamID:withSignType:withLAContext:withError:
- _objc_msgSend$stageProfileForUuid:
- _objc_msgSend$stageProfileForUuid:withReply:
CStrings:
+ "-[amfidConnection commitProfile:]_block_invoke"
+ "-[amfidConnection getACMUPPStateWithError:]_block_invoke"
+ "-[amfidConnection getStagedProfilewithError:]_block_invoke"
+ "-[amfidConnection initiateDataMigration]_block_invoke"
+ "-[amfidConnection removeManagedState]_block_invoke"
+ "-[amfidConnection removeTrustforUuid:]_block_invoke"
+ "-[amfidConnection setDemoState:]_block_invoke"
+ "-[amfidConnection setManagedState:]_block_invoke"
+ "-[amfidConnection setSupervisedState:]_block_invoke"
+ "-[amfidConnection setTrustforUuid:withSignature:andSignType:]_block_invoke"
+ "-[amfidConnection signTeamId:withSignType:withLAContext:withError:]_block_invoke"
+ "-[amfidConnection stageProfile:]_block_invoke"
+ "AMFIGetSEPDeviceState"
- "-[AMFIConnection commitProfileForUuid:]_block_invoke"
- "-[AMFIConnection getSEPStateWithError:]_block_invoke"
- "-[AMFIConnection getStagedProfileWithError:]_block_invoke"
- "-[AMFIConnection initiateDataMigration]_block_invoke"
- "-[AMFIConnection removeManagedState]_block_invoke"
- "-[AMFIConnection removeTrustforUuid:]_block_invoke"
- "-[AMFIConnection setDemoState:]_block_invoke"
- "-[AMFIConnection setManagedState:]_block_invoke"
- "-[AMFIConnection setSupervisedState:]_block_invoke"
- "-[AMFIConnection setTrustForUuid:withSignature:withSignType:]_block_invoke"
- "-[AMFIConnection signTeamID:withSignType:withLAContext:withError:]_block_invoke"
- "-[AMFIConnection stageProfileForUuid:]_block_invoke"
- "AMFIDemoModeSetState"
- "AMFIMDMModeEnroll"
- "AMFIMDMModeRemove"
- "AMFISupervisedModeSetState"
- "_createAuxiliarySignature"
- "_getProfileAuxiliarySignature"

```
