## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO`

```diff

-483.100.68.0.0
-  __TEXT.__text: 0x5b8f0
+483.100.71.0.1
+  __TEXT.__text: 0x5b99c
   __TEXT.__auth_stubs: 0xe00
   __TEXT.__objc_methlist: 0x3314
   __TEXT.__const: 0x2e2
   __TEXT.__cstring: 0x7e76
   __TEXT.__oslogstring: 0x2271
-  __TEXT.__gcc_except_tab: 0x1520
+  __TEXT.__gcc_except_tab: 0x152c
   __TEXT.__dlopen_cstrs: 0x110
   __TEXT.__swift5_typeref: 0xc2
   __TEXT.__swift5_capture: 0x118

   __TEXT.__objc_methtype: 0x1548
   __TEXT.__objc_stubs: 0x7140
   __DATA_CONST.__got: 0x428
-  __DATA_CONST.__const: 0xea0
+  __DATA_CONST.__const: 0xea8
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FC3EB1EA-4E75-31D7-B193-433D271669D1
+  UUID: 8FB7BC77-8F45-36F3-BEDA-525FFC3F247A
   Functions: 2062
-  Symbols:   7321
+  Symbols:   7323
   CStrings:  3140
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftSpatial_$_PlatformSSO
Functions:
~ -[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:] : 2656 -> 2716
~ -[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:] : 1576 -> 1632
~ -[POAgentAuthenticationProcess handlePreviousRefreshTokens] : 656 -> 712

```
