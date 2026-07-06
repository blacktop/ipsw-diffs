## DaemonUtils

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/Versions/A/DaemonUtils`

```diff

-  __TEXT.__text: 0x2c284
-  __TEXT.__objc_methlist: 0x1c44
-  __TEXT.__const: 0x248
-  __TEXT.__cstring: 0x506d
-  __TEXT.__oslogstring: 0x16af
-  __TEXT.__gcc_except_tab: 0xa58
+  __TEXT.__text: 0x2ba34
+  __TEXT.__objc_methlist: 0x1b9c
+  __TEXT.__const: 0x250
+  __TEXT.__cstring: 0x5017
+  __TEXT.__oslogstring: 0x15a8
+  __TEXT.__gcc_except_tab: 0xa50
   __TEXT.__dlopen_cstrs: 0xaa
-  __TEXT.__unwind_info: 0xac0
+  __TEXT.__unwind_info: 0xa80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1d0
+  __DATA_CONST.__const: 0x1b0
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1168
+  __DATA_CONST.__objc_selrefs: 0x1108
   __DATA_CONST.__objc_classrefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__got: 0x2d8
-  __AUTH_CONST.__const: 0x6f0
-  __AUTH_CONST.__cfstring: 0x15a0
+  __DATA_CONST.__got: 0x2f0
+  __AUTH_CONST.__const: 0x630
+  __AUTH_CONST.__cfstring: 0x1540
   __AUTH_CONST.__objc_const: 0x39b0
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x48

   __AUTH.__objc_data: 0x460
   __DATA.__objc_ivar: 0x24c
   __DATA.__data: 0x3d0
-  __DATA.__bss: 0xf1
+  __DATA.__bss: 0xd9
   __DATA_DIRTY.__objc_data: 0x460
-  __DATA_DIRTY.__bss: 0x140
+  __DATA_DIRTY.__bss: 0x138
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1281
-  Symbols:   2544
-  CStrings:  940
+  Functions: 1260
+  Symbols:   2507
+  CStrings:  925
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_classrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ _LACErrorCodeInternal
+ _LACLogPushButton
+ _OBJC_CLASS_$_LACError
+ _OBJC_CLASS_$_LACMobileGestalt
+ _OUTLINED_FUNCTION_69
+ _OUTLINED_FUNCTION_70
+ _objc_msgSend$errorWithCode:debugDescription:
- +[DaemonUtils _enumAllSubrequirements:processingBlock:]
- +[DaemonUtils _updateDFRStatus]
- +[DaemonUtils _updateWithDFRStatus:source:]
- +[DaemonUtils deviceHasAtLeastSimulatedDFR]
- +[DaemonUtils deviceHasDFR]
- +[DaemonUtils deviceHasSecureDFR]
- +[DaemonUtils deviceHasSecureDoublePressHW]
- +[DaemonUtils deviceHasSpecialTouchID]
- +[DaemonUtils deviceHasTouchIDAndSecureDoublePress]
- +[DaemonUtils deviceIsPoseidon]
- +[DaemonUtils deviceSupportsSecureDoubleClick]
- +[DaemonUtils dfrHardwarePresent]
- +[DaemonUtils dfrPresent]
- +[DaemonUtils dfrStatus]
- _DFRRegisterStatusChangeCallback
- __33+[DaemonUtils deviceHasSecureDFR]_block_invoke
- ___31+[DaemonUtils _updateDFRStatus]_block_invoke
- ___31+[DaemonUtils _updateDFRStatus]_block_invoke_2
- ___33+[DaemonUtils deviceHasSecureDFR]_block_invoke
- ___55+[DaemonUtils _enumAllSubrequirements:processingBlock:]_block_invoke
- ___block_descriptor_32_e8_v16?0Q8l
- ___block_descriptor_40_e8_32r_e13_v24?0r^v8Q16l
- ___block_descriptor_48_e8_32bs_e28_v16?0r^{__ACMRequirement=}8l
- __dfrStatus
- _objc_msgSend$_enumAllSubrequirements:processingBlock:
- _objc_msgSend$_updateDFRStatus
- _objc_msgSend$_updateWithDFRStatus:source:
- _objc_msgSend$deviceHasSecureDFR
- _objc_msgSend$deviceHasSecureDoublePressHW
- _objc_msgSend$deviceHasTouchID
- _objc_msgSend$deviceSupportsSecureDoubleClick
- _objc_msgSend$dfrHardwarePresent
- _objc_msgSend$dfrPresent
- _updateDFRStatus.onceToken
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oEmRGu/Sources/LocalAuthenticationSecureIO/LASecureIO/LASecureIO.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oEmRGu/Sources/LocalAuthenticationSecureIO/LASecureIOLocal/LASecureIODisplay.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oEmRGu/Sources/LocalAuthenticationSecureIO/LASecureIOLocal/LASecureIOLocal.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oEmRGu/Sources/LocalAuthenticationSecureIO/LASecureIOd/LASecureIOServer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oEmRGu/Sources/LocalAuthenticationSecureIO/Shared/LASecureIOArchive.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oEmRGu/Sources/LocalAuthenticationSecureIO/Shared/LASecureIOCommunication.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oEmRGu/Sources/LocalAuthenticationSecureIO/Shared/LASecureIOUtils.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "%{public}@ updated DFR status: %x"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6yKJWu/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WlYvIv/Sources/LocalAuthenticationSecureIO/LASecureIO/LASecureIO.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WlYvIv/Sources/LocalAuthenticationSecureIO/LASecureIOLocal/LASecureIODisplay.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WlYvIv/Sources/LocalAuthenticationSecureIO/LASecureIOLocal/LASecureIOLocal.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WlYvIv/Sources/LocalAuthenticationSecureIO/LASecureIOd/LASecureIOServer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WlYvIv/Sources/LocalAuthenticationSecureIO/Shared/LASecureIOArchive.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WlYvIv/Sources/LocalAuthenticationSecureIO/Shared/LASecureIOCommunication.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.WlYvIv/Sources/LocalAuthenticationSecureIO/Shared/LASecureIOUtils.m"
- "DFRGetStatus"
- "StatusChangeCallback"
- "deviceHasAtLeastSimulatedDFR returned %d"
- "deviceHasDFR returned %d"
- "deviceHasSecureDFR returned %d (status:%d)"
- "deviceHasSecureDoublePressHW returned %d"
- "deviceSupportsSecureDoubleClick returned %d"
- "dfrPresent: Invalid data length:%d"
- "v16@?0Q8"
- "v16@?0r^{__ACMRequirement=}8"
- "v24@?0r^v8Q16"

```
