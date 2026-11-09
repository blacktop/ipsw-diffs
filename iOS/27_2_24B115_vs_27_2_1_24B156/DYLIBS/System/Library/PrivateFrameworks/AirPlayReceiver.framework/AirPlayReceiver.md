## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver`

```diff

-1005.13.1.1.0
-  __TEXT.__text: 0x179b44
+1005.13.1.2.0
+  __TEXT.__text: 0x179ce8
   __TEXT.__objc_methlist: 0xaec
   __TEXT.__const: 0x2762b
   __TEXT.__dlopen_cstrs: 0xad
   __TEXT.__gcc_except_tab: 0x890
-  __TEXT.__cstring: 0x33399
+  __TEXT.__cstring: 0x333da
   __TEXT.__oslogstring: 0x2eb
-  __TEXT.__unwind_info: 0x1cc8
+  __TEXT.__unwind_info: 0x1cd0
   __TEXT.__eh_frame: 0x128
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x998
   __AUTH_CONST.__const: 0x9420
-  __AUTH_CONST.__cfstring: 0xbaa0
+  __AUTH_CONST.__cfstring: 0xbac0
   __AUTH_CONST.__objc_const: 0x1550
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1715
-  Symbols:   3610
-  CStrings:  5208
+  Functions: 1716
+  Symbols:   3611
+  CStrings:  5210
 
Symbols:
+ GCC_except_table1015
+ GCC_except_table1128
+ GCC_except_table1147
+ GCC_except_table1198
+ GCC_except_table1202
+ GCC_except_table1255
+ GCC_except_table1263
+ GCC_except_table1265
+ GCC_except_table1309
+ GCC_except_table1372
+ _airplayReqProcessor_ensurePairingServices
- GCC_except_table1014
- GCC_except_table1127
- GCC_except_table1146
- GCC_except_table1197
- GCC_except_table1201
- GCC_except_table1254
- GCC_except_table1262
- GCC_except_table1264
- GCC_except_table1308
- GCC_except_table1371
Functions:
~ _AirPlayReceiverServerControl : 2016 -> 2040
~ __StartOrStopServersIfNeeded : 2008 -> 2076
~ _airplayReqProcessor_requestProcessPairSetupPINStart : 684 -> 744
~ _airplayReqProcessor_requestProcessPairSetupUnauthenticatedLegacy : 848 -> 852
~ _airplayReqProcessor_requestProcessPairSetupPINLegacy : 872 -> 988
~ _airplayReqProcessor_requestProcessPairSetup : 1948 -> 2008
~ _airplayReqProcessor_requestProcessPairVerify : 2432 -> 2136
~ _airplayReqProcessor_copyPasscodeForPairingType : 212 -> 240
+ _airplayReqProcessor_ensurePairingServices
~ _airplayReqProcessor_createPairingParamsDict : 352 -> 388
~ _APPairingServicesCoreUtilsCreate : 348 -> 288
~ _coreUtilsPairing_SetProperty : 456 -> 500
~ _coreUtilsPairing_HandleSetup : 1220 -> 1200
CStrings:
+ "1005.13.1.2"
+ "CoreUtils"
+ "OSStatus APPairingServicesCoreUtilsCreate(CFAllocatorRef, APPairingServicesRef *)"
+ "OSStatus _StartServers(AirPlayReceiverServerRef)"
+ "OSStatus airplayReqProcessor_ensurePairingServices(APReceiverRequestProcessorRef, Boolean, APSTransportMessageProcessingStatus *)"
+ "OSStatus coreUtilsPairing_HandleSetup(APPairingServicesRef, CFStringRef, CFDataRef, CFDataRef *, Boolean *)"
+ "[%{ptr}] APPairingServicesCoreUtils created.\n"
+ "[%{ptr}] Created %s pairing services [%{ptr}]\n"
+ "_StartServers"
+ "airplayReqProcessor_ensurePairingServices"
+ "disablePairSetupThrottling"
+ "legacy"
- "1005.13.1.1"
- "OSStatus APPairingServicesCoreUtilsCreate(CFAllocatorRef, Boolean, APPairingServicesRef *)"
- "OSStatus coreUtilsPairing_HandleSetup(APPairingServicesRef, CFStringRef, APSecurityMode, CFDataRef, CFDataRef *, Boolean *)"
- "[%{ptr}] APPairingServicesCoreUtils (%s) created.\n"
- "[%{ptr}] Created legacy pairing services [%{ptr}]\n"
- "[%{ptr}] Created pairing services [%{ptr}] for pair-setup.\n"
- "[%{ptr}] Created pairing services [%{ptr}] for pair-verify\n"
- "private"
- "public"
- "void _StartServers(AirPlayReceiverServerRef)"
```
