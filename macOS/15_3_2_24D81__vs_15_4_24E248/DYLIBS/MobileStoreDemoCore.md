## MobileStoreDemoCore

> `/System/Library/PrivateFrameworks/MobileStoreDemoCore.framework/Versions/A/MobileStoreDemoCore`

```diff

-1445.81.1.0.0
-  __TEXT.__text: 0xea64
+1445.100.92.0.0
+  __TEXT.__text: 0xed34
   __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_methlist: 0xae8
+  __TEXT.__objc_methlist: 0xd44
   __TEXT.__const: 0x128
   __TEXT.__gcc_except_tab: 0x250
   __TEXT.__cstring: 0xfd6
   __TEXT.__oslogstring: 0x157a
   __TEXT.__dlopen_cstrs: 0xca
-  __TEXT.__unwind_info: 0x300
-  __TEXT.__objc_classname: 0x118
-  __TEXT.__objc_methname: 0x2e6e
+  __TEXT.__unwind_info: 0x348
+  __TEXT.__objc_classname: 0x126
+  __TEXT.__objc_methname: 0x2e86
   __TEXT.__objc_methtype: 0xb57
-  __TEXT.__objc_stubs: 0x2680
+  __TEXT.__objc_stubs: 0x26a0
   __DATA_CONST.__got: 0x240
   __DATA_CONST.__const: 0xd8
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc28
+  __DATA_CONST.__objc_selrefs: 0xd38
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__auth_got: 0x2e0
   __AUTH_CONST.__const: 0x420
   __AUTH_CONST.__cfstring: 0x1000
-  __AUTH_CONST.__objc_const: 0x1600
+  __AUTH_CONST.__objc_const: 0x1258
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0x230
+  __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x9c
   __DATA.__data: 0x980
   __DATA.__bss: 0xe0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 00639043-641C-328E-B625-000B1BA83451
-  Functions: 331
-  Symbols:   1028
-  CStrings:  1033
+  UUID: A8AA666B-9C81-3221-8335-4A5A0DFFF39F
+  Functions: 351
+  Symbols:   1052
+  CStrings:  1035
 
Symbols:
+ +[AluminiumAuthenticator _defaultIncludedHeaders].cold.1
+ +[MSDBAAInterface sharedInstance].cold.1
+ +[MSDCDemoState isSecureDemoModeEnabled]
+ +[MSDCDemoUnitConnection sharedConnection].cold.1
+ +[MSDCHelper sharedInstance].cold.1
+ +[MSDCOnDemandUpdateController sharedInstance].cold.1
+ +[MSDLogModel sharedInstance].cold.1
+ +[MSDTestPreferences sharedInstance].cold.1
+ -[AluminiumAuthenticator addAuthenticationHeadersToRequest:includedHeaders:body:algorithm:error:].cold.1
+ -[AluminiumAuthenticator verifyAuthenticationWithRequest:includedHeaders:algorithm:error:].cold.1
+ -[MSDCDemoUnitConnection trustDAServer:].cold.3
+ -[MSDCDemoUnitConnection validateAccountsArrayFromDU:].cold.1
+ -[MSDCDemoUnitConnection validateUserEnteredPassword:getRetryCount:forDeviceID:].cold.5
+ -[MSDCHelper validatePasswordEnteredByUser:skipScreen:].cold.2
+ -[MSDCOnDemandUpdateController createCookieFileWithExpectedOSBuild:error:].cold.2
+ _OBJC_CLASS_$_MSDCDemoState
+ _OBJC_METACLASS_$_MSDCDemoState
+ _OUTLINED_FUNCTION_5
+ __OBJC_$_CLASS_METHODS_MSDCDemoState
+ __OBJC_CLASS_RO_$_MSDCDemoState
+ __OBJC_METACLASS_RO_$_MSDCDemoState
+ _objc_msgSend$isDeviceEnrolledOnAlbert
+ defaultLogHandle.cold.1
+ messageLogHandle.cold.1
+ screenSaverLogHandle.cold.1
+ signpostLogHandle.cold.1
CStrings:
+ "MSDCDemoState"
+ "isSecureDemoModeEnabled"

```
