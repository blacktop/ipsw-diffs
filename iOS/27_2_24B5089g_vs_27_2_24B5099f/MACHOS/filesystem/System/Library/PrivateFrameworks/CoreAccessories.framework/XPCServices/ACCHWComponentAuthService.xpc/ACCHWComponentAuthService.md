## ACCHWComponentAuthService

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/XPCServices/ACCHWComponentAuthService.xpc/ACCHWComponentAuthService`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1219.40.7.0.0
-  __TEXT.__text: 0x39974
-  __TEXT.__auth_stubs: 0xe20
-  __TEXT.__objc_stubs: 0xe80
-  __TEXT.__objc_methlist: 0x69c
+1219.40.10.502.1
+  __TEXT.__text: 0x3a74c
+  __TEXT.__auth_stubs: 0xe30
+  __TEXT.__objc_stubs: 0xf80
+  __TEXT.__objc_methlist: 0x704
   __TEXT.__const: 0x1e223
-  __TEXT.__cstring: 0x2050
-  __TEXT.__oslogstring: 0x6768
+  __TEXT.__cstring: 0x20ff
+  __TEXT.__oslogstring: 0x6ae2
   __TEXT.__objc_classname: 0x9b
-  __TEXT.__objc_methname: 0x180b
+  __TEXT.__objc_methname: 0x1880
   __TEXT.__objc_methtype: 0x607
   __TEXT.__gcc_except_tab: 0x270
-  __TEXT.__unwind_info: 0x1028
-  __DATA_CONST.__const: 0x6aa8
-  __DATA_CONST.__cfstring: 0x1780
+  __TEXT.__unwind_info: 0x1060
+  __DATA_CONST.__const: 0x6ab8
+  __DATA_CONST.__cfstring: 0x1860
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x720
-  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__auth_got: 0x728
+  __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x40
   __DATA.__objc_const: 0xb68
-  __DATA.__objc_selrefs: 0x5e8
+  __DATA.__objc_selrefs: 0x5f8
   __DATA.__objc_ivar: 0x64
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x1b8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1234
-  Symbols:   2816
-  CStrings:  1264
+  Functions: 1260
+  Symbols:   2838
+  CStrings:  1287
 
Symbols:
+ -[ACCHWComponentAuthService authenticateBatteryWithChallenge:completionHandler:]
+ -[ACCHWComponentAuthService authenticateLASWithChallenge:completionHandler:updateRegistry:]
+ -[ACCHWComponentAuthService authenticateRCAMWithChallenge:completionHandler:updateRegistry:]
+ -[ACCHWComponentAuthService authenticateTouchControllerWithChallenge:completionHandler:]
+ -[ACCHWComponentAuthService authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]
+ -[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:]
+ -[ACCHWComponentAuthService authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]
+ -[ACCHWComponentAuthService signRCAMChallenge:completionHandler:]
+ -[ACCHWComponentAuthService signVeridianChallenge:completionHandler:]
+ GCC_except_table79
+ _CFDictionaryCreate
+ __createError
+ _kACCInfo_PPIDVersionUID
+ _kCFACCInfo_PPIDVersionUID
+ _kCFErrorUnderlyingErrorKey
+ _objc_msgSend$authenticateBatteryWithChallenge:completionHandler:componentIndex:
+ _objc_msgSend$authenticateLASWithChallenge:completionHandler:updateRegistry:componentIndex:
+ _objc_msgSend$authenticateRCAMWithChallenge:completionHandler:updateRegistry:componentIndex:
+ _objc_msgSend$authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:componentIndex:
+ _objc_msgSend$authenticateVeridianWithChallenge:completionHandler:componentIndex:
+ _objc_msgSend$signRCAMChallenge:completionHandler:componentIndex:
+ _objc_msgSend$signVeridianChallenge:completionHandler:componentIndex:
+ _objc_msgSend$verifyModuleCertificate:forModule:forAuthFlags:forIndex:
- GCC_except_table72
CStrings:
+ "%s: !sendOutgoingHandler"
+ "%s: authSession(%d), keepOpen %d, error %d"
+ "PPIDVersionUID"
+ "authSetupStart: initMessage_RequestAuthSetup failed: %d"
+ "authenticateTouchControllerWithChallenge:completionHandler:"
+ "com.apple.mfi4Auth.decrypt"
+ "com.apple.mfi4Auth.encrypt"
+ "com.apple.mfi4Auth.process"
+ "com.apple.mfi4Auth.protocol"
+ "com.apple.mfi4Auth.receive"
+ "com.apple.mfi4Auth.send"
+ "decryptIncomingData: decryptPayload rc=%d"
+ "decryptIncomingData: failed: %d"
+ "encryptOutgoingData: encryptPayload rc=%d"
+ "failed to handle refresh access state response"
+ "mfi4Auth_protocol_handle_AuthCert: Accessory did NOT provide PrivacyPrefix!"
+ "mfi4Auth_protocol_processIncomingMessage: error: %d"
+ "mfi4Auth_protocol_processIncomingMessageExtra: error: %d"
+ "processIncomingMessageExtra: non-Extra message id 0x%04x — falling through to relay"
+ "processIncomingMessageRelay: error: %d"
+ "processIncomingMessageRelay: non-relay message id 0x%04x — no relay action"
+ "processOutgoingSecureTunnelDataForClient: sendOutgoingData failed"
+ "publicManufacturerNVMRead: initMessage_RequestManufacturerNVMRead failed: %d"
+ "receiveIncomingData: sendOutgoingData failed"
+ "requestRefreshAccessState: !authSession"
+ "requestRefreshAccessState: !outMessage"
+ "requestRefreshAccessState: authSession shutting down"
+ "requestRefreshAccessState: initMessage_RequestRefreshAccessState failed: %d"
+ "userNVMRead: initMessage_RequestUserNVMRead failed: %d"
+ "userNVMWrite: initMessage_RequestUserNVMWrite failed: %d"
+ "verifyModuleCertificate:forModule:forAuthFlags:forIndex:"
- "%s: authSession(%d), keepOpen %d"
- "Data not passed in"
- "decryptIncomingData: failed"
- "encryptOutgoingData: encryptPayload: error: %d"
- "failed to handle auth failed"
- "mfi4Auth_protocol_processIncomingMessage: error"
- "mfi4Auth_protocol_processIncomingMessageExtra: error"
- "processIncomingMessageRelay: error"
```
