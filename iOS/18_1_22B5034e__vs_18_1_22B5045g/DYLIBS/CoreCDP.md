## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

-383.2.0.0.0
-  __TEXT.__text: 0x4af88
+386.100.4.0.1
+  __TEXT.__text: 0x4b72c
   __TEXT.__auth_stubs: 0x1000
-  __TEXT.__objc_methlist: 0x2aa4
+  __TEXT.__objc_methlist: 0x2ad4
   __TEXT.__const: 0x1124
-  __TEXT.__gcc_except_tab: 0x10f0
+  __TEXT.__gcc_except_tab: 0x10fc
   __TEXT.__oslogstring: 0x81a7
-  __TEXT.__cstring: 0x4ee3
+  __TEXT.__cstring: 0x5073
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x1310
+  __TEXT.__unwind_info: 0x1320
   __TEXT.__objc_classname: 0x6eb
-  __TEXT.__objc_methname: 0x820d
-  __TEXT.__objc_methtype: 0x1968
-  __TEXT.__objc_stubs: 0x4980
+  __TEXT.__objc_methname: 0x8311
+  __TEXT.__objc_methtype: 0x19d3
+  __TEXT.__objc_stubs: 0x49c0
   __DATA_CONST.__got: 0x488
-  __DATA_CONST.__const: 0x2bf0
+  __DATA_CONST.__const: 0x2c60
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d70
+  __DATA_CONST.__objc_selrefs: 0x1d98
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0x810
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x530
-  __AUTH_CONST.__cfstring: 0x32a0
-  __AUTH_CONST.__objc_const: 0x95a0
+  __AUTH_CONST.__cfstring: 0x3320
+  __AUTH_CONST.__objc_const: 0x9670
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x2b0
+  __DATA.__objc_ivar: 0x2b8
   __DATA.__data: 0x1038
   __DATA.__bss: 0x109
   __DATA.__common: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1874
-  Symbols:   2664
-  CStrings:  2959
+  Functions: 1880
+  Symbols:   2674
+  CStrings:  2978
 
Symbols:
+ _kCDPAnalyticsRecoveryCreateSessionEvent
+ _kCDPAnalyticsValidateCustodianRecoveryInfoEvent
+ _kCDPAnalyticsValidateRecoveryCodeEvent
+ _kCDPAnalyticsFetchCustodianRecoveryInfoEvent
CStrings:
+ "setIgnorePasswordCache:"
+ "TB,N,V_ignorePasswordCache"
+ "_ignorePasswordCache"
+ "ignorePasswordCache"
+ "cdpContext:showResetFailedAlertWithUnderlyingError:completion:"
+ "updateWalrusStatus:authenticatedContext:completion:"
+ "com.apple.corecdp.recoveryContact.owner.validateCode"
+ "unlockDeviceWithPasscode:outError:"
+ "TB,R,N,V_isProxSignIn"
+ "isProxSignIn"
+ "com.apple.corecdp.recoveryContact.owner.validateCustodianRecoveryInfo"
+ "Local secret is set and valid"
+ "_isProxSignIn"
+ "Vv40@0:8Q16@\"CDPContext\"24@?<v@?@\"CDPCombinedWalrusStatus\"@\"NSError\">32"
+ "com.apple.corecdp.recoveryContact.owner.fetchCustodianRecoveryInfo"
+ "Local secret is invalid, error: %!s(MISSING)\n"
+ "v40@0:8Q16@24@?32"
+ "Vv40@0:8Q16@24@?32"
+ "-[CDPStateUIProviderProxy cdpContext:showResetFailedAlertWithUnderlyingError:completion:]"
+ "v40@0:8@\"CDPContext\"16@\"NSError\"24@?<v@?Q@\"NSError\">32"
+ "com.apple.corecdp.recoveryContact.owner.createSession"
- "Vv32@0:8Q16@?<v@?@\"CDPCombinedWalrusStatus\"@\"NSError\">24"
- "updateWalrusStatus:completion:"

```
