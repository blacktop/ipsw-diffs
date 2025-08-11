## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver`

```diff

-890.77.2.0.0
-  __TEXT.__text: 0x14ccd4
+890.79.1.1.0
+  __TEXT.__text: 0x14cd2c
   __TEXT.__auth_stubs: 0x3820
   __TEXT.__objc_methlist: 0xad4
   __TEXT.__const: 0x32335
   __TEXT.__dlopen_cstrs: 0xad
   __TEXT.__gcc_except_tab: 0x7e8
-  __TEXT.__cstring: 0x2f813
-  __TEXT.__unwind_info: 0x1470
+  __TEXT.__cstring: 0x2f832
+  __TEXT.__unwind_info: 0x1478
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0x144
   __TEXT.__objc_methname: 0x2756

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 793E8235-57CD-3E10-8A1B-81524D08939F
+  UUID: CE4874F2-FB5E-3182-BF71-64DE1490697F
   Functions: 1591
   Symbols:   5091
-  CStrings:  6869
+  CStrings:  6871
 
Symbols:
+ _APReceiverRequestProcessorCopyProperty.7553
+ ___block_descriptor_tmp.42.7138
+ ___block_descriptor_tmp.52.7478
+ ___block_descriptor_tmp.7141
+ ___block_descriptor_tmp.7471
+ ___block_literal_global.44
+ ___block_literal_global.7124
+ ___block_literal_global.7469
- _APReceiverRequestProcessorCopyProperty.7550
- ___block_descriptor_tmp.40
- ___block_descriptor_tmp.52.7475
- ___block_descriptor_tmp.7138
- ___block_descriptor_tmp.7468
- ___block_literal_global.42
- ___block_literal_global.7122
- ___block_literal_global.7466
Functions:
~ _airplayReqProcessor_requestProcessPairSetup : 1676 -> 1684
~ _airplayReqProcessor_requestProcessPairVerify : 2260 -> 2272
~ _APPairingServicesCoreUtilsCreate : 288 -> 348
~ _coreUtilsPairing_HandleSetup : 1212 -> 1220
CStrings:
+ "890.79.1.1"
+ "OSStatus APPairingServicesCoreUtilsCreate(CFAllocatorRef, Boolean, APPairingServicesRef *)"
+ "[%{ptr}] APPairingServicesCoreUtils (%s) created.\n"
+ "private"
+ "public"
- "890.77.2"
- "OSStatus APPairingServicesCoreUtilsCreate(CFAllocatorRef, APPairingServicesRef *)"
- "[%{ptr}] APPairingServicesCoreUtils created.\n"

```
