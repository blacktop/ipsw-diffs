## DaemonUtils

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/Versions/A/DaemonUtils`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_classrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2319.0.33.0.1
-  __TEXT.__text: 0x2ba34
+2319.0.46.0.0
+  __TEXT.__text: 0x2b938
   __TEXT.__objc_methlist: 0x1b9c
-  __TEXT.__const: 0x250
-  __TEXT.__cstring: 0x5017
-  __TEXT.__oslogstring: 0x15a8
+  __TEXT.__const: 0x238
+  __TEXT.__cstring: 0x4ff3
+  __TEXT.__oslogstring: 0x157e
   __TEXT.__gcc_except_tab: 0xa50
   __TEXT.__dlopen_cstrs: 0xaa
-  __TEXT.__unwind_info: 0xa80
+  __TEXT.__unwind_info: 0xa88
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classrefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__got: 0x2f0
-  __AUTH_CONST.__const: 0x630
+  __DATA_CONST.__got: 0x2f8
+  __AUTH_CONST.__const: 0x5e0
   __AUTH_CONST.__cfstring: 0x1540
-  __AUTH_CONST.__objc_const: 0x39b0
-  __AUTH_CONST.__objc_intobj: 0x1e0
+  __AUTH_CONST.__objc_const: 0x39d0
+  __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x410
+  __AUTH_CONST.__auth_got: 0x408
   __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x24c
+  __DATA.__objc_ivar: 0x250
   __DATA.__data: 0x3d0
   __DATA.__bss: 0xd9
   __DATA_DIRTY.__objc_data: 0x460
-  __DATA_DIRTY.__bss: 0x138
+  __DATA_DIRTY.__bss: 0x128
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1260
-  Symbols:   2023
-  CStrings:  752
+  Functions: 1257
+  Symbols:   2022
+  CStrings:  747
 
Symbols:
+ -[LAAnalytics initWithEventName:reporter:]
+ OBJC_IVAR_$_LAAnalytics._reporter
+ _OBJC_CLASS_$_LACAnalyticsReporter
+ _objc_msgSend$initWithEventName:reporter:
+ _objc_msgSend$sendEventWithName:payload:
- -[LAAnalytics logLevel]
- _AnalyticsSendEventLazy
- ___23-[LAAnalytics _collect]_block_invoke
- ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0l
- _objc_msgSend$intValue
- _objc_msgSend$logLevel
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YiEnDf/Sources/LocalAuthenticationSecureIO/LASecureIO/LASecureIO.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YiEnDf/Sources/LocalAuthenticationSecureIO/LASecureIOLocal/LASecureIODisplay.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YiEnDf/Sources/LocalAuthenticationSecureIO/LASecureIOLocal/LASecureIOLocal.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YiEnDf/Sources/LocalAuthenticationSecureIO/LASecureIOd/LASecureIOServer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YiEnDf/Sources/LocalAuthenticationSecureIO/Shared/LASecureIOArchive.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YiEnDf/Sources/LocalAuthenticationSecureIO/Shared/LASecureIOCommunication.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YiEnDf/Sources/LocalAuthenticationSecureIO/Shared/LASecureIOUtils.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "%{public}s analytics event %{public}@: %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oEmRGu/Sources/LocalAuthenticationSecureIO/LASecureIO/LASecureIO.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oEmRGu/Sources/LocalAuthenticationSecureIO/LASecureIOLocal/LASecureIODisplay.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oEmRGu/Sources/LocalAuthenticationSecureIO/LASecureIOLocal/LASecureIOLocal.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oEmRGu/Sources/LocalAuthenticationSecureIO/LASecureIOd/LASecureIOServer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oEmRGu/Sources/LocalAuthenticationSecureIO/Shared/LASecureIOArchive.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oEmRGu/Sources/LocalAuthenticationSecureIO/Shared/LASecureIOCommunication.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oEmRGu/Sources/LocalAuthenticationSecureIO/Shared/LASecureIOUtils.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "@\"NSDictionary\"8@?0"
- "C"
- "didn't send"
- "sent"
```
