## H16ISPServices

> `/System/Library/PrivateFrameworks/H16ISPServices.framework/Versions/A/H16ISPServices`

```diff

-3.25.0.0.0
-  __TEXT.__text: 0x1e038
+3.28.0.0.0
+  __TEXT.__text: 0x1f69c
   __TEXT.__auth_stubs: 0x600
-  __TEXT.__cstring: 0x80ae
+  __TEXT.__cstring: 0x82e8
   __TEXT.__gcc_except_tab: 0x594
   __TEXT.__const: 0x8
-  __TEXT.__unwind_info: 0x3f8
+  __TEXT.__unwind_info: 0x450
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0x40
   __AUTH_CONST.__auth_got: 0x308

   - /usr/lib/libIOAccessoryManager.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 395
-  Symbols:   765
-  CStrings:  1465
+  Functions: 423
+  Symbols:   803
+  CStrings:  1469
 
Symbols:
+ __ispirexclavekitmodule_ispirexclavekit_server_start_block_invoke.cold.87
+ __ispirexclavekitmodule_ispirexclavekit_server_start_block_invoke.cold.88
+ __ispirexclavekitmodule_ispirexclavekit_server_start_block_invoke.cold.89
+ __isprgbexclavekitmodule_isprgbexclavekit_server_start_block_invoke.cold.75
+ __isprgbexclavekitmodule_isprgbexclavekit_server_start_block_invoke.cold.76
+ __isprgbexclavekitmodule_isprgbexclavekit_server_start_block_invoke.cold.77
+ __isprgbexclavekitmodule_isprgbexclavekit_server_start_block_invoke.cold.78
+ __isprgbexclavekitmodule_isprgbexclavekit_server_start_block_invoke.cold.79
+ __isprgbexclavekitmodule_isprgbexclavekit_server_start_block_invoke.cold.80
+ _ispirexclavekitmodule_ispexclavecorechinfoset2__decode
+ _ispirexclavekitmodule_ispexclavecorechinfoset2__encode
+ _ispirexclavekitmodule_ispexclavecorechinfoset2__marshal
+ _ispirexclavekitmodule_ispexclavecorechinfoset2__marshal_sizeof
+ _ispirexclavekitmodule_ispexclavecorechinfoset2__unmarshal
+ _ispirexclavekitmodule_ispirexclavekit_sendcmdchinfoset2
+ _isprgbexclavekitmodule_anstfacev150__decode
+ _isprgbexclavekitmodule_anstfacev150__encode
+ _isprgbexclavekitmodule_anstfacev150__marshal
+ _isprgbexclavekitmodule_anstfacev150__marshal_sizeof
+ _isprgbexclavekitmodule_anstfacev150__unmarshal
+ _isprgbexclavekitmodule_anstobjectv150__decode
+ _isprgbexclavekitmodule_anstobjectv150__marshal
+ _isprgbexclavekitmodule_anstobjectv150__marshal_sizeof
+ _isprgbexclavekitmodule_anstobjectv150__unmarshal
+ _isprgbexclavekitmodule_anstresultipcv150__encode
+ _isprgbexclavekitmodule_anstresultipcv150__marshal
+ _isprgbexclavekitmodule_anstresultipcv150__marshal_sizeof
+ _isprgbexclavekitmodule_anstresultipcv150__unmarshal
+ _isprgbexclavekitmodule_ispexclavecorechinfoset2__decode
+ _isprgbexclavekitmodule_ispexclavecorechinfoset2__encode
+ _isprgbexclavekitmodule_ispexclavecorechinfoset2__marshal
+ _isprgbexclavekitmodule_ispexclavecorechinfoset2__marshal_sizeof
+ _isprgbexclavekitmodule_ispexclavecorechinfoset2__unmarshal
+ _isprgbexclavekitmodule_ispexclavecorechrunkitanstrsltv150__marshal
+ _isprgbexclavekitmodule_ispexclavecorechrunkitanstrsltv150__marshal_sizeof
+ _isprgbexclavekitmodule_ispexclavecorechrunkitanstrsltv150__unmarshal
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchinfoset2
+ _isprgbexclavekitmodule_isprgbexclavekit_sendcmdchrunkitanstv150
CStrings:
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Binaries/AppleH16CameraInterface_NoKext/install/TempContent/Objects/AppleH16CameraInterface.build/H16ISPServices.build/DerivedSources/ExclaveKitIRISPMgrInterface_tightbeam.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Binaries/AppleH16CameraInterface_NoKext/install/TempContent/Objects/AppleH16CameraInterface.build/H16ISPServices.build/DerivedSources/ExclaveKitRGBISPMgrInterface_tightbeam.c"
+ "TB_ASSERT: (ispirexclavekitmodule_ispexclavecorechinfoset2__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPIRExclaveKitModule.ISPExclaveCoreChInfoSet2\""
+ "TB_ASSERT: (isprgbexclavekitmodule_ispexclavecorechinfoset2__decode(msg, &cmd) == TB_ERROR_SUCCESS) && \"failed to decode type: ISPRGBExclaveKitModule.ISPExclaveCoreChInfoSet2\""
+ "TB_ASSERT: (server->sendcmdchinfoset2 != NULL) && \"implementation for sendCmdChInfoSet2 is not present\""
+ "TB_ASSERT: (server->sendcmdchrunkitanstv150 != NULL) && \"implementation for sendCmdChRunKitANSTV150 is not present\""
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Binaries/AppleH16CameraInterface_NoKext/install/TempContent/Objects/AppleH16CameraInterface.build/H16ISPServices.build/DerivedSources/ExclaveKitIRISPMgrInterface_tightbeam.c"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Binaries/AppleH16CameraInterface_NoKext/install/TempContent/Objects/AppleH16CameraInterface.build/H16ISPServices.build/DerivedSources/ExclaveKitRGBISPMgrInterface_tightbeam.c"

```
