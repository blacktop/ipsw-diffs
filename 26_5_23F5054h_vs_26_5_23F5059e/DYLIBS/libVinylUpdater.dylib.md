## libVinylUpdater.dylib

> `/usr/lib/updaters/libVinylUpdater.dylib`

```diff

 146.0.0.0.0
-  __TEXT.__text: 0x43240
-  __TEXT.__auth_stubs: 0x1d90
+  __TEXT.__text: 0x42a00
+  __TEXT.__auth_stubs: 0x1d40
   __TEXT.__init_offsets: 0x40
-  __TEXT.__gcc_except_tab: 0x402c
-  __TEXT.__cstring: 0xa1c0
-  __TEXT.__const: 0x5191
+  __TEXT.__gcc_except_tab: 0x400c
+  __TEXT.__cstring: 0x9a3f
+  __TEXT.__const: 0x5171
   __TEXT.__oslogstring: 0x7c
-  __TEXT.__unwind_info: 0x18f0
+  __TEXT.__unwind_info: 0x18d0
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__const: 0x9a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0xed0
+  __AUTH_CONST.__auth_got: 0xea8
   __AUTH_CONST.__const: 0x1910
   __AUTH_CONST.__cfstring: 0xec0
   __DATA.__data: 0x460

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: C5E2E3D1-8275-386E-AB2B-CCF7D2C7345E
-  Functions: 1253
-  Symbols:   3968
-  CStrings:  1402
+  UUID: 5D071214-27B2-3E0F-AA06-15B71B2637EF
+  Functions: 1249
+  Symbols:   3951
+  CStrings:  1324
 
Symbols:
+ ___block_descriptor_tmp.110
+ ___block_descriptor_tmp.12
+ ___block_descriptor_tmp.16
+ ___block_descriptor_tmp.18
+ ___block_descriptor_tmp.20
+ ___block_descriptor_tmp.8
+ ___block_literal_global.112
+ ___cxx_global_var_init.109
+ ___cxx_global_var_init.21
+ ___cxx_global_var_init.23
+ ___cxx_global_var_init.53
+ ___cxx_global_var_init.75
- GCC_except_table65
- GCC_except_table66
- GCC_except_table68
- GCC_except_table70
- __ZN15BBUpdaterCommon17BBUPrintBackTraceEv
- __ZN15BBUpdaterCommon23BBURegisterDebugSignalsEv
- __ZN15BBUpdaterCommonL18handleDebugSignalsEiP9__siginfoPv
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIPvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__16vectorIPvNS_9allocatorIS1_EEE11__vallocateB9nqe210106Em
- __ZNSt3__16vectorIPvNS_9allocatorIS1_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIPvNS_9allocatorIS1_EEEC2B9nqe210106Em
- ___block_descriptor_tmp.10
- ___block_descriptor_tmp.109
- ___block_descriptor_tmp.15
- ___block_descriptor_tmp.17
- ___block_descriptor_tmp.19
- ___block_descriptor_tmp.7
- ___block_literal_global.111
- ___cxx_global_var_init.108
- ___cxx_global_var_init.20
- ___cxx_global_var_init.22
- ___cxx_global_var_init.47
- ___cxx_global_var_init.74
- _backtrace
- _backtrace_symbols_fd
- _fprintf
- _getchar
- _sigaction
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CNX3ugA4HN7HKUM_f2sp-P34-Wy-R3Uhumkxj-U/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "0x<< SNUM >>"
+ "VinylRestore-146~951"
- "        %s '%s' - Press [c] to continue ; [q] to quit: "
- "/AppleInternal/Library/BuildRoots/4~CMtvugBpmnT28UB1JaG_cY3MRH48WzxBXKHj87k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/CommandDrivers/eUICCVinylICEValve.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/Communication/Eureka/VinylETLEUICC.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/Support/BBUPurpleReverseProxy.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/VinylRestore/Update/Perso/eUICCPerso.cpp"
- "AuthPerso"
- "AuthenticatePersoDevice"
- "BBUCreateCFError"
- "BBUFDRLogHandler"
- "BBULogPrintBinaryDelegate"
- "BBUReadNVRAM"
- "BBUReadNVRAM_block_invoke"
- "CreateDictionaryFromPlistData"
- "CreateValidationBlob"
- "DeleteProfile"
- "FinalizePerso"
- "FinalizePersoDevice"
- "ForcePerso"
- "GetData"
- "GetData_EoS"
- "GetNonceServer"
- "GetSIMSKUString"
- "GetVinylType"
- "GetWrapKeyServer"
- "HardwareHasESIM_block_invoke"
- "HowToProceed"
- "InitPerso"
- "InitPersoDevice"
- "InitPersoServer"
- "InstallPairingMSM"
- "InstallTicket"
- "LETOEnableEUICC"
- "ManagePairingAuthenticate"
- "ManagePairingGetNonce"
- "Perform"
- "PostDataSync"
- "PowerDownSE"
- "PowerUpSE"
- "Refurb"
- "ResetCard"
- "ReverseProxyGetSettings"
- "ReverseProxyGetSettings_block_invoke"
- "Run"
- "SendReceiptServer"
- "SerializeKeyValuePairsIntoPlistData"
- "SetCardMode"
- "Step"
- "StoreData"
- "StreamFirmware"
- "ValidatePerso"
- "ValidatePersoDevice"
- "VinylControllerObjDestroy"
- "VinylRestore-146~868"
- "bbupdater_log"
- "caught signal %d\n"
- "checkEOSDev"
- "collectCoreDump"
- "createTransportNoEvents"
- "createTransport_block_invoke_2"
- "freeTransport"
- "freeTransportSync"
- "freeTransportSync_block_invoke"
- "freeTransportSync_block_invoke_2"
- "getECID_block_invoke"
- "getEID"
- "getPairingIdentifier"
- "getParamUpdateOperation"
- "get_info"
- "inRestoreOS_block_invoke"
- "inRestoreOS_block_invoke_2"
- "isAbsentOkay"
- "isNVRAMKeyPresent"
- "logEUICCData"
- "openChannel"
- "operator()"
- "startRouterServer"
- "statusCallback"
- "stopRouterServer"
- "supportsVinylUpdate"
- "waitForeSIMBoot"

```
