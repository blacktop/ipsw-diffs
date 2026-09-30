## libZhuGeArmory.dylib

> `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/libZhuGeArmory.dylib`

```diff

-396.0.4.0.0
-  __TEXT.__text: 0x222e8
-  __TEXT.__auth_stubs: 0x990
-  __TEXT.__objc_methlist: 0x80c
+396.0.8.0.0
+  __TEXT.__text: 0x22a60
+  __TEXT.__auth_stubs: 0x9a0
+  __TEXT.__objc_methlist: 0x81c
   __TEXT.__const: 0x4b8
-  __TEXT.__cstring: 0xa021
+  __TEXT.__cstring: 0xa01c
   __TEXT.__gcc_except_tab: 0x18c
   __TEXT.__oslogstring: 0x1af
   __TEXT.__unwind_info: 0x3d8
   __TEXT.__objc_classname: 0x181
-  __TEXT.__objc_methname: 0x1caf
+  __TEXT.__objc_methname: 0x1cd2
   __TEXT.__objc_methtype: 0x32c
   __TEXT.__objc_stubs: 0x1bc0
   __DATA_CONST.__got: 0x198

   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x848
+  __DATA_CONST.__objc_selrefs: 0x850
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_arraydata: 0xa40
-  __AUTH_CONST.__auth_got: 0x4d8
+  __DATA_CONST.__objc_arraydata: 0x748
+  __AUTH_CONST.__auth_got: 0x4e0
   __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x8020
+  __AUTH_CONST.__cfstring: 0x7fc0
   __AUTH_CONST.__objc_const: 0xe68
   __AUTH_CONST.__objc_intobj: 0x1f8
-  __AUTH_CONST.__objc_dictobj: 0xb18
-  __AUTH_CONST.__objc_arrayobj: 0x930
+  __AUTH_CONST.__objc_dictobj: 0x758
+  __AUTH_CONST.__objc_arrayobj: 0x7f8
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x60
   __DATA.__data: 0xa24

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnfrestore.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 77FE23E8-C78A-3860-A270-16258D46FC55
-  Functions: 333
-  Symbols:   1397
-  CStrings:  2613
+  UUID: F2AD8B41-9AE3-3C4C-A8EF-EF4468F7DEE4
+  Functions: 335
+  Symbols:   1402
+  CStrings:  2610
 
Symbols:
+ +[ZhuGeKeysActionArmory queryVinylEUICCCSNbyKey:withError:]
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table45
+ GCC_except_table47
+ GCC_except_table49
+ GCC_except_table51
+ _VinyleUICCPerformOperationWithLogSync
+ _logCallBackForVinylEUICCWithLevelFormat
- GCC_except_table39
- GCC_except_table41
- GCC_except_table44
- GCC_except_table46
- GCC_except_table48
- GCC_except_table50
Functions:
~ -[ZhuGeArmory convertReturnValue:toFormat:] : 2208 -> 2240
+ _logCallBackForVinylEUICCWithLevelFormat
+ +[ZhuGeKeysActionArmory queryVinylEUICCCSNbyKey:withError:]
~ ___getConfigDict_block_invoke : 32516 -> 33120
CStrings:
+ "+[ZhuGeKeysActionArmory queryVinylEUICCCSNbyKey:withError:]"
+ "-l 0xFFFFFFFF -v 99"
+ "8jvikGIcqTbQS4FdgY3t6160TElV+a3nnrgv6KQmmRbsc"
+ "BasebandUpdater"
+ "DSp557sXEG12LTRMsGdoP0DnK4Tq6SBvsLPV6rag2VVVQ"
+ "DebugArgs"
+ "Did not find config of key %@"
+ "Didn't find EID from response of eUICC operation!"
+ "EID"
+ "Failed to get response from eUICC operation! Error code: %@"
+ "Failed to weak link libVinylNonUpdater.dylib, VinyleUICCPerformOperationWithLogSync isn't available!"
+ "UpdateBaseband"
+ "Vinyl error code: %@"
+ "ZhuGeBasebandFirmwareUpdateInfo query:%@ isCachable:%s"
+ "kVinylFwUpdateCsn"
+ "logCallBackForVinylEUICCWithLevelFormat"
+ "queryVinylEUICCCSNbyKey:withError:"
- "AppleBasebandUserClient"
- "AppleBiometricServicesUserClient"
- "AppleTCONControlUserClient"
- "IOAVDisplayMemoryUserClient"
- "IOAppleConvergedIPCBBUserClient"
- "IOPortTransportAIDBusUserClient"
- "com.apple.CommCenter.fine-grained"
- "com.apple.aop.user-client.full-access"
- "com.apple.keystore.sik.access"
- "com.apple.nfcd.hwmanager"
- "com.apple.nvmetunnel.allow"
- "com.apple.private.IOPortTransportAIDBusUserClient.access"
- "com.apple.private.MobileGestalt.AllowedProtectedKeys"
- "com.apple.private.ioavfamily.user-access-displaymemory"
- "com.apple.security.exception.iokit-user-client-class"
- "com.apple.security.iokit-user-client-class"
- "com.apple.stockholm.kext.entitlement"
- "spi"

```
