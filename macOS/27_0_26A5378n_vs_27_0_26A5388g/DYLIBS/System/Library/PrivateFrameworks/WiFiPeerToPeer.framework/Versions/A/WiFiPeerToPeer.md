## WiFiPeerToPeer

> `/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/Versions/A/WiFiPeerToPeer`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__oslogstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-875.64.0.0.0
-  __TEXT.__text: 0x42e68
-  __TEXT.__objc_methlist: 0x54a4
+875.71.0.0.0
+  __TEXT.__text: 0x43b48
+  __TEXT.__objc_methlist: 0x565c
   __TEXT.__const: 0x280
   __TEXT.__oslogstring: 0x1bf5
   __TEXT.__swift5_typeref: 0x8c
-  __TEXT.__cstring: 0x9780
+  __TEXT.__cstring: 0x9969
   __TEXT.__constg_swiftt: 0x70
   __TEXT.__swift5_reflstr: 0x7
   __TEXT.__swift5_fieldmd: 0x2c
   __TEXT.__swift5_types: 0x8
   __TEXT.__gcc_except_tab: 0x2f0
-  __TEXT.__unwind_info: 0xf20
+  __TEXT.__unwind_info: 0xf60
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x630
-  __DATA_CONST.__objc_classlist: 0x260
-  __DATA_CONST.__objc_protolist: 0x100
+  __DATA_CONST.__objc_classlist: 0x270
+  __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2238
-  __DATA_CONST.__objc_protorefs: 0xd0
-  __DATA_CONST.__objc_superrefs: 0x240
-  __DATA_CONST.__got: 0x328
-  __AUTH_CONST.__const: 0x1528
-  __AUTH_CONST.__cfstring: 0x6a80
-  __AUTH_CONST.__objc_const: 0x9b88
+  __DATA_CONST.__objc_selrefs: 0x22c8
+  __DATA_CONST.__objc_protorefs: 0xd8
+  __DATA_CONST.__objc_superrefs: 0x250
+  __DATA_CONST.__got: 0x348
+  __AUTH_CONST.__const: 0x1578
+  __AUTH_CONST.__cfstring: 0x6ba0
+  __AUTH_CONST.__objc_const: 0x9ef8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x450
-  __AUTH.__objc_data: 0x48
-  __DATA.__objc_ivar: 0x724
-  __DATA.__data: 0xc80
+  __AUTH.__objc_data: 0xe8
+  __DATA.__objc_ivar: 0x744
+  __DATA.__data: 0xce0
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x1848
   __DATA_DIRTY.__data: 0x60
   __DATA_DIRTY.__common: 0x8
-  __DATA_DIRTY.__bss: 0x70
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1750
-  Symbols:   4161
-  CStrings:  1183
+  Functions: 1782
+  Symbols:   4245
+  CStrings:  1194
 
Symbols:
+ +[WiFiAwarePairingPasswordVoucher supportsSecureCoding]
+ -[WiFiAwarePairingConfig passwordVoucherToken]
+ -[WiFiAwarePairingConfig setPasswordVoucherToken:]
+ -[WiFiAwarePairingPasswordVoucher .cxx_destruct]
+ -[WiFiAwarePairingPasswordVoucher copyWithZone:]
+ -[WiFiAwarePairingPasswordVoucher description]
+ -[WiFiAwarePairingPasswordVoucher encodeWithCoder:]
+ -[WiFiAwarePairingPasswordVoucher expiration]
+ -[WiFiAwarePairingPasswordVoucher initWithCoder:]
+ -[WiFiAwarePairingPasswordVoucher initWithToken:pairingMode:password:usageCount:expiration:]
+ -[WiFiAwarePairingPasswordVoucher pairingMode]
+ -[WiFiAwarePairingPasswordVoucher password]
+ -[WiFiAwarePairingPasswordVoucher setExpiration:]
+ -[WiFiAwarePairingPasswordVoucher setPairingMode:]
+ -[WiFiAwarePairingPasswordVoucher setPassword:]
+ -[WiFiAwarePairingPasswordVoucher setToken:]
+ -[WiFiAwarePairingPasswordVoucher setUsageCount:]
+ -[WiFiAwarePairingPasswordVoucher token]
+ -[WiFiAwarePairingPasswordVoucher usageCount]
+ -[WiFiAwarePairingPasswordVoucherStore .cxx_destruct]
+ -[WiFiAwarePairingPasswordVoucherStore activate]
+ -[WiFiAwarePairingPasswordVoucherStore deactivate]
+ -[WiFiAwarePairingPasswordVoucherStore generateVoucherForPairingMode:completionHandler:]
+ -[WiFiAwarePairingPasswordVoucherStore init]
+ -[WiFiAwarePairingPasswordVoucherStore remoteObjectInterface]
+ -[WiFiAwarePairingPasswordVoucherStore startConnectionUsingProxy:completionHandler:]
+ -[WiFiAwareStateMonitor realtimeModeUpdatedHandler]
+ -[WiFiAwareStateMonitor setRealtimeModeUpdatedHandler:]
+ -[WiFiAwareStateMonitor updatedNANRealtimeMode:]
+ -[WiFiP2PNANStateMonitor updatedNANRealtimeMode:]
+ GCC_except_table29
+ GCC_except_table33
+ GCC_except_table37
+ GCC_except_table41
+ GCC_except_table45
+ GCC_except_table49
+ OBJC_IVAR_$_WiFiAwarePairingConfig._passwordVoucherToken
+ OBJC_IVAR_$_WiFiAwarePairingPasswordVoucher._expiration
+ OBJC_IVAR_$_WiFiAwarePairingPasswordVoucher._pairingMode
+ OBJC_IVAR_$_WiFiAwarePairingPasswordVoucher._password
+ OBJC_IVAR_$_WiFiAwarePairingPasswordVoucher._token
+ OBJC_IVAR_$_WiFiAwarePairingPasswordVoucher._usageCount
+ OBJC_IVAR_$_WiFiAwarePairingPasswordVoucherStore._xpcConnection
+ OBJC_IVAR_$_WiFiAwareStateMonitor._realtimeModeUpdatedHandler
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSTimeZone
+ _OBJC_CLASS_$_WiFiAwarePairingPasswordVoucher
+ _OBJC_CLASS_$_WiFiAwarePairingPasswordVoucherStore
+ _OBJC_METACLASS_$_WiFiAwarePairingPasswordVoucher
+ _OBJC_METACLASS_$_WiFiAwarePairingPasswordVoucherStore
+ __OBJC_$_CLASS_METHODS_WiFiAwarePairingPasswordVoucher
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwarePairingPasswordVoucher
+ __OBJC_$_INSTANCE_METHODS_WiFiAwarePairingPasswordVoucher
+ __OBJC_$_INSTANCE_METHODS_WiFiAwarePairingPasswordVoucherStore
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwarePairingPasswordVoucher
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwarePairingPasswordVoucherStore
+ __OBJC_$_PROP_LIST_WiFiAwarePairingPasswordVoucher
+ __OBJC_$_PROP_LIST_WiFiAwarePairingPasswordVoucherStore
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WiFiP2PNANStateMonitorXPCDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WiFiAwarePairingPasswordXPC
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WiFiAwarePairingPasswordXPC
+ __OBJC_$_PROTOCOL_REFS_WiFiAwarePairingPasswordXPC
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwarePairingPasswordVoucher
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwarePairingPasswordVoucherStore
+ __OBJC_CLASS_RO_$_WiFiAwarePairingPasswordVoucher
+ __OBJC_CLASS_RO_$_WiFiAwarePairingPasswordVoucherStore
+ __OBJC_LABEL_PROTOCOL_$_WiFiAwarePairingPasswordXPC
+ __OBJC_METACLASS_RO_$_WiFiAwarePairingPasswordVoucher
+ __OBJC_METACLASS_RO_$_WiFiAwarePairingPasswordVoucherStore
+ __OBJC_PROTOCOL_$_WiFiAwarePairingPasswordXPC
+ __OBJC_PROTOCOL_REFERENCE_$_WiFiAwarePairingPasswordXPC
+ ___46-[WiFiAwarePairingPasswordVoucher description]_block_invoke
+ ___88-[WiFiAwarePairingPasswordVoucherStore generateVoucherForPairingMode:completionHandler:]_block_invoke
+ ___block_descriptor_48_e8_32bs_e39_v16?0"<WiFiAwarePairingPasswordXPC>"8l
+ _objc_msgSend$createPasswordVoucherStore:
+ _objc_msgSend$expiration
+ _objc_msgSend$initWithToken:pairingMode:password:usageCount:expiration:
+ _objc_msgSend$issuePasswordVoucherForPairingMode:completion:
+ _objc_msgSend$localTimeZone
+ _objc_msgSend$password
+ _objc_msgSend$passwordVoucherToken
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setExpiration:
+ _objc_msgSend$setPassword:
+ _objc_msgSend$setPasswordVoucherToken:
+ _objc_msgSend$setTimeZone:
+ _objc_msgSend$setToken:
+ _objc_msgSend$setUsageCount:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$token
+ _objc_msgSend$usageCount
- GCC_except_table22
- GCC_except_table26
- GCC_except_table30
- GCC_except_table34
- GCC_except_table38
- GCC_except_table42
- GCC_except_table46
CStrings:
+ "(nil)"
+ "<%@: %p> pairingMode=%@, pairingMetadata=%@, pairSetupMode=%@, userID=%u, passwordVoucherToken=%@"
+ "<%@: %p> token=%@, pairingMode=%@, password=%@, usageCount=%lu, expiration=%@>"
+ "WiFiAwarePairingConfig.passwordVoucherToken"
+ "WiFiAwarePairingPasswordVoucher.expiration"
+ "WiFiAwarePairingPasswordVoucher.pairingMode"
+ "WiFiAwarePairingPasswordVoucher.password"
+ "WiFiAwarePairingPasswordVoucher.token"
+ "WiFiAwarePairingPasswordVoucher.usageCount"
+ "com.apple.wifip2p.WiFiAwarePairingPasswordVoucherStore"
+ "v16@?0@\"<WiFiAwarePairingPasswordXPC>\"8"
+ "yyyy-MM-dd HH:mm:ss zzz"
- "<%@: %p> pairingMode=%@, pairingMetadata=%@, pairSetupMode=%@, userID=%u"
```
