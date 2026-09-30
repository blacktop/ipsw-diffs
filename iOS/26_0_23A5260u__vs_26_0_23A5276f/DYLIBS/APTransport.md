## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/APTransport`

```diff

-890.61.4.11.2
-  __TEXT.__text: 0xa3d54
-  __TEXT.__auth_stubs: 0x31e0
-  __TEXT.__objc_methlist: 0x12d8
-  __TEXT.__cstring: 0x2ab77
+890.66.3.0.0
+  __TEXT.__text: 0xa4760
+  __TEXT.__auth_stubs: 0x3200
+  __TEXT.__objc_methlist: 0x1368
+  __TEXT.__cstring: 0x2ae64
   __TEXT.__const: 0x328
   __TEXT.__gcc_except_tab: 0x4cc
   __TEXT.__oslogstring: 0x16e
   __TEXT.__dlopen_cstrs: 0x18b
-  __TEXT.__unwind_info: 0x2658
-  __TEXT.__objc_classname: 0x1db
-  __TEXT.__objc_methname: 0x46b1
-  __TEXT.__objc_methtype: 0xf03
-  __TEXT.__objc_stubs: 0x3ee0
-  __DATA_CONST.__got: 0x3d8
-  __DATA_CONST.__const: 0x3588
-  __DATA_CONST.__objc_classlist: 0x50
+  __TEXT.__unwind_info: 0x2670
+  __TEXT.__objc_classname: 0x1f5
+  __TEXT.__objc_methname: 0x48b3
+  __TEXT.__objc_methtype: 0xf40
+  __TEXT.__objc_stubs: 0x4080
+  __DATA_CONST.__got: 0x3e0
+  __DATA_CONST.__const: 0x35a0
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1378
-  __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__objc_selrefs: 0x13e8
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x1900
+  __AUTH_CONST.__auth_got: 0x1910
   __AUTH_CONST.__const: 0x2b48
-  __AUTH_CONST.__cfstring: 0x5ec0
-  __AUTH_CONST.__objc_const: 0x1b40
+  __AUTH_CONST.__cfstring: 0x5f20
+  __AUTH_CONST.__objc_const: 0x1c90
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x140
+  __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x278
-  __DATA.__objc_ivar: 0x15c
+  __DATA.__objc_ivar: 0x16c
   __DATA.__data: 0x1190
   __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0x1e0

   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 40A80443-D0DB-371A-8DA1-422B3527AB2A
-  Functions: 4478
-  Symbols:   11612
-  CStrings:  5798
+  UUID: A00987C9-A128-3B2A-A06F-0493A000B6BF
+  Functions: 4496
+  Symbols:   11679
+  CStrings:  5838
 
Symbols:
+ +[APBonjourCacheHomeKitItem itemWithDeviceInfo:userInfo:]
+ -[APBonjourCacheHomeKit canCacheDevice:]
+ -[APBonjourCacheHomeKit realDeviceFound:userInfo:]
+ -[APBonjourCacheHomeKit requireDeviceNetworkSignature]
+ -[APBonjourCacheHomeKit setRequireDeviceNetworkSignature:]
+ -[APBonjourCacheHomeKitItem dealloc]
+ -[APBonjourCacheHomeKitItem deviceInfo]
+ -[APBonjourCacheHomeKitItem setDeviceInfo:]
+ -[APBonjourCacheHomeKitItem setUserInfo:]
+ -[APBonjourCacheHomeKitItem userInfo]
+ -[APTNANPairingDelegate initWithHandleAuthorizationRequestBlock:logContext:]
+ -[APTNANPairingDelegate initWithHandleAuthorizationRequestBlock:logContext:].cold.1
+ -[APTNANPairingDelegate initWithHandleAuthorizationRequestBlock:logContext:].cold.2
+ GCC_except_table105
+ GCC_except_table21
+ _APBrowserCreate.cold.25
+ _APBrowserCreate.cold.26
+ _APSCopyDeviceName
+ _OBJC_CLASS_$_APBonjourCacheHomeKitItem
+ _OBJC_CLASS_$_WiFiAwarePairingMetadata
+ _OBJC_IVAR_$_APBonjourCacheHomeKit._requireDeviceNetworkSignature
+ _OBJC_IVAR_$_APBonjourCacheHomeKitItem._deviceInfo
+ _OBJC_IVAR_$_APBonjourCacheHomeKitItem._userInfo
+ _OBJC_IVAR_$_APTNANPairingDelegate._logContext
+ _OBJC_METACLASS_$_APBonjourCacheHomeKitItem
+ __APTNANDataSessionSetProperty.cold.7
+ __APTNANDataSessionSetProperty.cold.8
+ __OBJC_$_CLASS_METHODS_APBonjourCacheHomeKitItem
+ __OBJC_$_INSTANCE_METHODS_APBonjourCacheHomeKitItem
+ __OBJC_$_INSTANCE_VARIABLES_APBonjourCacheHomeKitItem
+ __OBJC_$_PROP_LIST_APBonjourCacheHomeKitItem
+ __OBJC_CLASS_RO_$_APBonjourCacheHomeKitItem
+ __OBJC_METACLASS_RO_$_APBonjourCacheHomeKitItem
+ ___50-[APBonjourCacheHomeKit realDeviceFound:userInfo:]_block_invoke
+ ___block_descriptor_88_e8_32r40r48r_e5_v8?0lr32l8r40l8r48l8
+ ___block_literal_global.371
+ _kAPBrowserDeviceInfoKey_NetworkSignature
+ _kAPTNANDataSessionProperty_AuthorizationLogContext
+ _kAPTransportSessionOption_NANAuthorizationLogContext
+ _objc_autorelease
+ _objc_msgSend$canCacheDevice:
+ _objc_msgSend$deviceInfo
+ _objc_msgSend$initWithBundleID:selfPairingName:peerDeviceName:storageClass:lifetime:pairingClient:
+ _objc_msgSend$initWithHandleAuthorizationRequestBlock:logContext:
+ _objc_msgSend$itemWithDeviceInfo:userInfo:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$realDeviceFound:userInfo:
+ _objc_msgSend$requireDeviceNetworkSignature
+ _objc_msgSend$setDeviceInfo:
+ _objc_msgSend$setUserInfo:
+ _objc_msgSend$setWfaConnectionMode:
+ _objc_msgSend$setWfaPairingMetadata:
+ _objc_msgSend$userInfo
+ _objc_msgSend$valueForKey:
- -[APTNANPairingDelegate initWithHandleAuthorizationRequestBlock:]
- -[APTNANPairingDelegate initWithHandleAuthorizationRequestBlock:].cold.1
- -[APTNANPairingDelegate initWithHandleAuthorizationRequestBlock:].cold.2
- GCC_except_table95
- ___41-[APBonjourCacheHomeKit realDeviceFound:]_block_invoke
- ___block_descriptor_64_e8_32r40r48r_e5_v8?0lr32l8r40l8r48l8
- ___block_literal_global.339
- _objc_msgSend$initWithHandleAuthorizationRequestBlock:
- _udpconnection_setPropertyInternal.cold.10
CStrings:
+ "-[APBonjourCacheHomeKit canCacheDevice:]"
+ "-[APTNANPairingDelegate initWithHandleAuthorizationRequestBlock:logContext:]"
+ "2"
+ "890.66.3"
+ "@\"NSDictionary\""
+ "@32@0:8@16@24"
+ "@32@0:8@?16^{__CFString=}24"
+ "APBonjourCacheHomeKitItem"
+ "APTNANDataSessionProperty_AuthorizationLogContext"
+ "NANAuthorizationLogContext"
+ "NANDS [%{ptr}] Receiver is denying interruptions. Translating error to hijack failed error."
+ "NANDS [%{ptr}] set connection mode to any pairing"
+ "NANDS [%{ptr}] set pairing metadata"
+ "T@\"NSDictionary\",&,N,V_deviceInfo"
+ "T@\"NSDictionary\",&,N,V_userInfo"
+ "TB,N,V_requireDeviceNetworkSignature"
+ "[%{ptr}] Device %@ missing required network signature for new entry"
+ "[%{ptr}] Device %@ network signature: %'@ does not match current network signature: %'@"
+ "[%{ptr}] Device %@ no longer present on Infra"
+ "[%{ptr}] Device %@ seen over Infra with network signature %'@"
+ "[%{ptr}] Failed to remove cache file: %@ %@%?{end} URL: %@"
+ "[%{ptr}] Found cache with incompatible version %'@ (expected %'@). Existing contents may be overridden."
+ "[%{ptr}] Pairing delegate received %@ pairing request for session %@. Running pairing block [%{ptr}]."
+ "^{__CFString=}"
+ "_deviceInfo"
+ "_requireDeviceNetworkSignature"
+ "_userInfo"
+ "canCacheDevice:"
+ "initWithBundleID:selfPairingName:peerDeviceName:storageClass:lifetime:pairingClient:"
+ "initWithHandleAuthorizationRequestBlock:logContext:"
+ "itemWithDeviceInfo:userInfo:"
+ "localizedDescription"
+ "realDeviceFound:userInfo:"
+ "requireDeviceNetworkSignature"
+ "setDeviceInfo:"
+ "setRequireDeviceNetworkSignature:"
+ "setUserInfo:"
+ "setWfaConnectionMode:"
+ "setWfaPairingMetadata:"
+ "userInfo"
+ "valueForKey:"
+ "void browser_updateDeviceInfraNetworkSignature(APBrowserRef, CFNumberRef, Boolean)"
- "-[APTNANPairingDelegate initWithHandleAuthorizationRequestBlock:]"
- "890.61.4.11.2"
- "@24@0:8@?16"
- "[%{ptr}] Failed to load cache with incompatible file version %'@ (expected %'@)"
- "[%{ptr}] Pairing delegate received %s pairing request. Running pairing block [%{ptr}]."
- "initWithHandleAuthorizationRequestBlock:"

```
