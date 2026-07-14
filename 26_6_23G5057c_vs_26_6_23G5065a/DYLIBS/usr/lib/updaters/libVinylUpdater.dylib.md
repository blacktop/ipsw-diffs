## libVinylUpdater.dylib

> `/usr/lib/updaters/libVinylUpdater.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__DATA.__data`

```diff

-  __TEXT.__text: 0x43240
-  __TEXT.__auth_stubs: 0x1d90
+  __TEXT.__text: 0x42a00
+  __TEXT.__auth_stubs: 0x1d40
   __TEXT.__init_offsets: 0x40
-  __TEXT.__gcc_except_tab: 0x402c
-  __TEXT.__cstring: 0xa1c1
-  __TEXT.__const: 0x5191
+  __TEXT.__gcc_except_tab: 0x400c
+  __TEXT.__cstring: 0x9a40
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
-  Functions: 1253
-  Symbols:   2092
-  CStrings:  1285
+  Functions: 1249
+  Symbols:   2076
+  CStrings:  1207
 
Symbols:
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
- _backtrace
- _backtrace_symbols_fd
- _fprintf
- _getchar
- _sigaction
CStrings:
+ "0x<< SNUM >>"
+ "VinylRestore-146~1227"
- "        %s '%s' - Press [c] to continue ; [q] to quit: "
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
- "VinylRestore-146~1195"
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
