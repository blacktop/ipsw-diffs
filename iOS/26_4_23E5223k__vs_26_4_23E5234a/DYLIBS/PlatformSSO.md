## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO`

```diff

-483.100.72.0.0
-  __TEXT.__text: 0x5b99c
+483.100.73.0.0
+  __TEXT.__text: 0x5bbf0
   __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_methlist: 0x3314
+  __TEXT.__objc_methlist: 0x331c
   __TEXT.__const: 0x2e2
-  __TEXT.__cstring: 0x7e76
+  __TEXT.__cstring: 0x7e96
   __TEXT.__oslogstring: 0x2271
   __TEXT.__gcc_except_tab: 0x152c
   __TEXT.__dlopen_cstrs: 0x110

   __TEXT.__unwind_info: 0x1448
   __TEXT.__eh_frame: 0x600
   __TEXT.__objc_classname: 0x3e5
-  __TEXT.__objc_methname: 0x9d6e
-  __TEXT.__objc_methtype: 0x1548
-  __TEXT.__objc_stubs: 0x7140
+  __TEXT.__objc_methname: 0x9dd4
+  __TEXT.__objc_methtype: 0x1558
+  __TEXT.__objc_stubs: 0x7180
   __DATA_CONST.__got: 0x428
-  __DATA_CONST.__const: 0xea8
+  __DATA_CONST.__const: 0xeb0
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21f0
+  __DATA_CONST.__objc_selrefs: 0x2200
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x710
   __AUTH_CONST.__const: 0xc08
-  __AUTH_CONST.__cfstring: 0x37e0
+  __AUTH_CONST.__cfstring: 0x3800
   __AUTH_CONST.__objc_const: 0x83a0
-  __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xa00

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: ABFED0AC-128F-3BCE-A7F5-2134C18F12E8
-  Functions: 2062
-  Symbols:   7323
-  CStrings:  3140
+  UUID: CFC93406-01CC-3322-A89D-9599795BAD14
+  Functions: 2064
+  Symbols:   7332
+  CStrings:  3145
 
Symbols:
+ -[PODaemonConnection changeTempSessionAccountWithCompletion:]
+ -[PODaemonConnection currentTempSessionAccountWithCompletion:]
+ -[PODaemonConnection resetTemporaryAccountWithName:completion:]
+ -[PODaemonConnection updateTemporaryAccountWithName:fullName:altSecurityIdentity:completion:]
+ GCC_except_table113
+ ___54-[PODaemonProcess saveAppSSOConfiguration:completion:]_block_invoke.104
+ ___61-[PODaemonConnection changeTempSessionAccountWithCompletion:]_block_invoke
+ ___61-[PODaemonConnection changeTempSessionAccountWithCompletion:]_block_invoke.cold.1
+ ___62-[PODaemonConnection currentTempSessionAccountWithCompletion:]_block_invoke
+ ___62-[PODaemonConnection currentTempSessionAccountWithCompletion:]_block_invoke.cold.1
+ ___63-[PODaemonConnection resetTemporaryAccountWithName:completion:]_block_invoke
+ ___63-[PODaemonConnection resetTemporaryAccountWithName:completion:]_block_invoke.cold.1
+ ___93-[PODaemonConnection updateTemporaryAccountWithName:fullName:altSecurityIdentity:completion:]_block_invoke
+ ___93-[PODaemonConnection updateTemporaryAccountWithName:fullName:altSecurityIdentity:completion:]_block_invoke.cold.1
+ ___block_literal_global.144
+ ___block_literal_global.279
+ _kPOCurrentTempSessionKey
+ _objc_msgSend$changeTempSessionAccountWithCompletion:
+ _objc_msgSend$currentTempSessionAccountWithCompletion:
+ _objc_msgSend$registerDefaults:
+ _objc_msgSend$resetTemporaryAccountWithName:completion:
+ _objc_msgSend$updateTemporaryAccountWithName:fullName:altSecurityIdentity:completion:
- -[PODaemonConnection createTempUserHomeDirectory:]
- -[PODaemonConnection resetTemporaryAccount:]
- -[PODaemonConnection updateTemporaryAccountName:altSecurityIdentity:completion:]
- ___44-[PODaemonConnection resetTemporaryAccount:]_block_invoke
- ___44-[PODaemonConnection resetTemporaryAccount:]_block_invoke.cold.1
- ___50-[PODaemonConnection createTempUserHomeDirectory:]_block_invoke
- ___50-[PODaemonConnection createTempUserHomeDirectory:]_block_invoke.cold.1
- ___54-[PODaemonProcess saveAppSSOConfiguration:completion:]_block_invoke.97
- ___80-[PODaemonConnection updateTemporaryAccountName:altSecurityIdentity:completion:]_block_invoke
- ___80-[PODaemonConnection updateTemporaryAccountName:altSecurityIdentity:completion:]_block_invoke.cold.1
- ___block_literal_global.142
- ___block_literal_global.274
- _objc_msgSend$createTempUserHomeDirectory:
- _objc_msgSend$resetTemporaryAccount:
- _objc_msgSend$updateTemporaryAccountName:altSecurityIdentity:completion:
CStrings:
+ "changeTempSessionAccountWithCompletion:"
+ "com.apple.TempSession"
+ "currentTempSessionAccountWithCompletion:"
+ "registerDefaults:"
+ "resetTemporaryAccountWithName:completion:"
+ "updateTemporaryAccountWithName:fullName:altSecurityIdentity:completion:"
+ "v48@0:8@16@24@32@?40"
- "createTempUserHomeDirectory:"
- "resetTemporaryAccount:"
- "updateTemporaryAccountName:altSecurityIdentity:completion:"

```
