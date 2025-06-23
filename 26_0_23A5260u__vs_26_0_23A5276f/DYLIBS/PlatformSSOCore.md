## PlatformSSOCore

> `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore`

```diff

-483.0.6.0.1
-  __TEXT.__text: 0x8d8f4
+483.0.19.0.0
+  __TEXT.__text: 0x8de0c
   __TEXT.__auth_stubs: 0x1ae0
-  __TEXT.__objc_methlist: 0x5ea8
-  __TEXT.__const: 0x1704
-  __TEXT.__cstring: 0xa32c
-  __TEXT.__oslogstring: 0x1a07
+  __TEXT.__objc_methlist: 0x5ec0
+  __TEXT.__const: 0x16f4
+  __TEXT.__cstring: 0xa436
+  __TEXT.__oslogstring: 0x19e7
   __TEXT.__gcc_except_tab: 0x7f8
   __TEXT.__dlopen_cstrs: 0xa6
   __TEXT.__swift5_typeref: 0x158

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x34
-  __TEXT.__unwind_info: 0x1fb8
+  __TEXT.__unwind_info: 0x1fc8
   __TEXT.__eh_frame: 0x5b8
   __TEXT.__objc_classname: 0xd3d
-  __TEXT.__objc_methname: 0xc7b2
+  __TEXT.__objc_methname: 0xc7fb
   __TEXT.__objc_methtype: 0x28de
-  __TEXT.__objc_stubs: 0x7000
+  __TEXT.__objc_stubs: 0x7020
   __DATA_CONST.__got: 0x920
-  __DATA_CONST.__const: 0x2420
+  __DATA_CONST.__const: 0x2430
   __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90

   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0xd80
   __AUTH_CONST.__const: 0x780
-  __AUTH_CONST.__cfstring: 0x7300
-  __AUTH_CONST.__objc_const: 0x14188
+  __AUTH_CONST.__cfstring: 0x73a0
+  __AUTH_CONST.__objc_const: 0x141b8
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x3400
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0x610
+  __DATA.__objc_ivar: 0x614
   __DATA.__data: 0x1040
   __DATA.__bss: 0xd31
   __DATA.__common: 0x88

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCryptoTokenKit.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B7CA57D7-F8ED-38A1-8294-B1ABEE04BC87
-  Functions: 3583
-  Symbols:   11910
-  CStrings:  5044
+  UUID: 947C8CE8-0A2B-394B-972B-5F37F8E85C92
+  Functions: 3591
+  Symbols:   11928
+  CStrings:  5056
 
Symbols:
+ -[PODaemonCoreConnection deviceConfigurationForIdentifier:completion:]
+ -[PODaemonCoreConnection loginConfigurationForIdentifier:completion:]
+ -[PODaemonCoreConnection retrievePendingSSOTokenForIdentifier:completion:]
+ -[PODaemonCoreConnection retrieveStashedDecryptionContextForIdentifier:completion:]
+ -[PODaemonCoreConnection retrieveStashedSSOTokenForIdentifier:completion:]
+ -[PODaemonCoreConnection savePendingSSOTokens:identifier:completion:]
+ -[PODaemonCoreConnection saveStashedDecryptionContext:identifier:completion:]
+ -[PODaemonCoreConnection saveStashedSSOTokens:identifier:completion:]
+ -[PODaemonCoreProcess _deviceConfigurationForIdentifier:]
+ -[PODaemonCoreProcess _deviceConfigurationForIdentifier:].cold.1
+ -[PODaemonCoreProcess _loginConfigurationForIdentifier:]
+ -[PODaemonCoreProcess _loginConfigurationForIdentifier:].cold.1
+ -[PODaemonCoreProcess _loginConfigurationForIdentifier:].cold.2
+ -[PODaemonCoreProcess _pendingSSOTokensForIdentifier:error:]
+ -[PODaemonCoreProcess _pendingSSOTokensForIdentifier:error:].cold.1
+ -[PODaemonCoreProcess _stashedSSOTokensForIdentifier:error:]
+ -[PODaemonCoreProcess _stashedSSOTokensForIdentifier:error:].cold.1
+ -[PODaemonCoreProcess _stashedSSOTokensForIdentifier:error:].cold.2
+ -[PODaemonCoreProcess deviceConfigurationForIdentifier:completion:]
+ -[PODaemonCoreProcess loginConfigurationForIdentifier:completion:]
+ -[PODaemonCoreProcess retrievePendingSSOTokenForIdentifier:completion:]
+ -[PODaemonCoreProcess retrieveStashedSSOTokenForIdentifier:completion:]
+ -[PODaemonCoreProcess savePendingSSOTokens:identifier:completion:]
+ -[PODaemonCoreProcess saveStashedDecryptionContext:identifier:completion:]
+ -[PODaemonCoreProcess saveStashedSSOTokens:identifier:completion:]
+ -[PODeviceConfiguration setTemporarySessionQuickLogin:]
+ -[PODeviceConfiguration temporarySessionQuickLogin]
+ _OBJC_IVAR_$_PODeviceConfiguration._temporarySessionQuickLogin
+ ___22-[POKeyWrap wrapBlob:]_block_invoke.11
+ ___22-[POKeyWrap wrapBlob:]_block_invoke.11.cold.1
+ ___22-[POKeyWrap wrapBlob:]_block_invoke.18
+ ___22-[POKeyWrap wrapBlob:]_block_invoke.18.cold.1
+ ___22-[POKeyWrap wrapBlob:]_block_invoke.2
+ ___22-[POKeyWrap wrapBlob:]_block_invoke.2.cold.1
+ ___22-[POKeyWrap wrapBlob:]_block_invoke.24
+ ___22-[POKeyWrap wrapBlob:]_block_invoke.24.cold.1
+ ___22-[POKeyWrap wrapBlob:]_block_invoke.30
+ ___22-[POKeyWrap wrapBlob:]_block_invoke.30.cold.1
+ ___22-[POKeyWrap wrapBlob:]_block_invoke.36
+ ___22-[POKeyWrap wrapBlob:]_block_invoke.36.cold.1
+ ___22-[POKeyWrap wrapBlob:]_block_invoke.7
+ ___22-[POKeyWrap wrapBlob:]_block_invoke.7.cold.1
+ ___24-[POKeyWrap unwrapBlob:]_block_invoke.51
+ ___24-[POKeyWrap unwrapBlob:]_block_invoke.51.cold.1
+ ___24-[POKeyWrap unwrapBlob:]_block_invoke.57
+ ___24-[POKeyWrap unwrapBlob:]_block_invoke.57.cold.1
+ ___24-[POKeyWrap unwrapBlob:]_block_invoke.63
+ ___24-[POKeyWrap unwrapBlob:]_block_invoke.63.cold.1
+ ___24-[POKeyWrap unwrapBlob:]_block_invoke.67
+ ___24-[POKeyWrap unwrapBlob:]_block_invoke.67.cold.1
+ ___24-[POKeyWrap unwrapBlob:]_block_invoke.73
+ ___24-[POKeyWrap unwrapBlob:]_block_invoke.73.cold.1
+ ___24-[POKeyWrap unwrapBlob:]_block_invoke.79
+ ___24-[POKeyWrap unwrapBlob:]_block_invoke.79.cold.1
+ ___38-[PODeviceConfiguration initWithData:]_block_invoke.174
+ ___60-[PODaemonCoreProcess _pendingSSOTokensForIdentifier:error:]_block_invoke
+ ___60-[PODaemonCoreProcess _pendingSSOTokensForIdentifier:error:]_block_invoke.cold.1
+ ___60-[PODaemonCoreProcess _stashedSSOTokensForIdentifier:error:]_block_invoke
+ ___60-[PODaemonCoreProcess _stashedSSOTokensForIdentifier:error:]_block_invoke.cold.1
+ ___66-[PODaemonCoreProcess loginConfigurationForIdentifier:completion:]_block_invoke
+ ___66-[PODaemonCoreProcess loginConfigurationForIdentifier:completion:]_block_invoke.cold.1
+ ___67-[PODaemonCoreProcess deviceConfigurationForIdentifier:completion:]_block_invoke
+ ___67-[PODaemonCoreProcess deviceConfigurationForIdentifier:completion:]_block_invoke.cold.1
+ ___69-[PODaemonCoreConnection loginConfigurationForIdentifier:completion:]_block_invoke
+ ___69-[PODaemonCoreConnection loginConfigurationForIdentifier:completion:]_block_invoke.cold.1
+ ___69-[PODaemonCoreConnection savePendingSSOTokens:identifier:completion:]_block_invoke
+ ___69-[PODaemonCoreConnection savePendingSSOTokens:identifier:completion:]_block_invoke.cold.1
+ ___69-[PODaemonCoreConnection saveStashedSSOTokens:identifier:completion:]_block_invoke
+ ___69-[PODaemonCoreConnection saveStashedSSOTokens:identifier:completion:]_block_invoke.cold.1
+ ___70-[PODaemonCoreConnection deviceConfigurationForIdentifier:completion:]_block_invoke
+ ___70-[PODaemonCoreConnection deviceConfigurationForIdentifier:completion:]_block_invoke.cold.1
+ ___74-[PODaemonCoreConnection retrievePendingSSOTokenForIdentifier:completion:]_block_invoke
+ ___74-[PODaemonCoreConnection retrievePendingSSOTokenForIdentifier:completion:]_block_invoke.cold.1
+ ___74-[PODaemonCoreConnection retrieveStashedSSOTokenForIdentifier:completion:]_block_invoke
+ ___74-[PODaemonCoreConnection retrieveStashedSSOTokenForIdentifier:completion:]_block_invoke.cold.1
+ ___77-[PODaemonCoreConnection saveStashedDecryptionContext:identifier:completion:]_block_invoke
+ ___77-[PODaemonCoreConnection saveStashedDecryptionContext:identifier:completion:]_block_invoke.cold.1
+ ___83-[PODaemonCoreConnection retrieveStashedDecryptionContextForIdentifier:completion:]_block_invoke
+ ___83-[PODaemonCoreConnection retrieveStashedDecryptionContextForIdentifier:completion:]_block_invoke.cold.1
+ ___block_descriptor_tmp.128
+ ___block_descriptor_tmp.141
+ ___block_descriptor_tmp.151
+ ___block_descriptor_tmp.154
+ ___block_descriptor_tmp.170
+ ___block_literal_global.156
+ ___block_literal_global.172
+ ___block_literal_global.447
+ ___block_literal_global.90
+ _objc_msgSend$_deviceConfigurationForIdentifier:
+ _objc_msgSend$_loginConfigurationForIdentifier:
+ _objc_msgSend$_pendingSSOTokensForIdentifier:error:
+ _objc_msgSend$_stashedSSOTokensForIdentifier:error:
+ _objc_msgSend$deviceConfigurationForIdentifier:completion:
+ _objc_msgSend$loginConfigurationForIdentifier:completion:
+ _objc_msgSend$retrievePendingSSOTokenForIdentifier:completion:
+ _objc_msgSend$retrieveStashedDecryptionContextForIdentifier:completion:
+ _objc_msgSend$retrieveStashedSSOTokenForIdentifier:completion:
+ _objc_msgSend$savePendingSSOTokens:identifier:completion:
+ _objc_msgSend$saveStashedDecryptionContext:identifier:completion:
+ _objc_msgSend$saveStashedSSOTokens:identifier:completion:
+ _objc_msgSend$temporarySessionQuickLogin
- -[PODaemonCoreConnection deviceConfigurationForIdentifer:completion:]
- -[PODaemonCoreConnection loginConfigurationForIdentifer:completion:]
- -[PODaemonCoreConnection retrievePendingSSOTokenForIdentifer:completion:]
- -[PODaemonCoreConnection retrieveStashedDecryptionContextForIdentifer:completion:]
- -[PODaemonCoreConnection retrieveStashedSSOTokenForIdentifer:completion:]
- -[PODaemonCoreConnection savePendingSSOTokens:identifer:completion:]
- -[PODaemonCoreConnection saveStashedDecryptionContext:identifer:completion:]
- -[PODaemonCoreConnection saveStashedSSOTokens:identifer:completion:]
- -[PODaemonCoreProcess _deviceConfigurationForIdentifer:]
- -[PODaemonCoreProcess _deviceConfigurationForIdentifer:].cold.1
- -[PODaemonCoreProcess _loginConfigurationForIdentifer:]
- -[PODaemonCoreProcess _loginConfigurationForIdentifer:].cold.1
- -[PODaemonCoreProcess _loginConfigurationForIdentifer:].cold.2
- -[PODaemonCoreProcess _pendingSSOTokensForIdentifer:error:]
- -[PODaemonCoreProcess _pendingSSOTokensForIdentifer:error:].cold.1
- -[PODaemonCoreProcess _stashedSSOTokensForIdentifer:error:]
- -[PODaemonCoreProcess _stashedSSOTokensForIdentifer:error:].cold.1
- -[PODaemonCoreProcess _stashedSSOTokensForIdentifer:error:].cold.2
- -[PODaemonCoreProcess deviceConfigurationForIdentifer:completion:]
- -[PODaemonCoreProcess loginConfigurationForIdentifer:completion:]
- -[PODaemonCoreProcess retrievePendingSSOTokenForIdentifer:completion:]
- -[PODaemonCoreProcess retrieveStashedSSOTokenForIdentifer:completion:]
- -[PODaemonCoreProcess savePendingSSOTokens:identifer:completion:]
- -[PODaemonCoreProcess saveStashedDecryptionContext:identifer:completion:]
- -[PODaemonCoreProcess saveStashedSSOTokens:identifer:completion:]
- ___22-[POKeyWrap wrapBlob:]_block_invoke.3
- ___22-[POKeyWrap wrapBlob:]_block_invoke.3.cold.1
- ___22-[POKeyWrap wrapBlob:]_block_invoke.8
- ___22-[POKeyWrap wrapBlob:]_block_invoke.8.cold.1
- ___24-[POKeyWrap unwrapBlob:]_block_invoke.17
- ___24-[POKeyWrap unwrapBlob:]_block_invoke.17.cold.1
- ___24-[POKeyWrap unwrapBlob:]_block_invoke.23
- ___24-[POKeyWrap unwrapBlob:]_block_invoke.23.cold.1
- ___24-[POKeyWrap unwrapBlob:]_block_invoke.29
- ___24-[POKeyWrap unwrapBlob:]_block_invoke.29.cold.1
- ___24-[POKeyWrap unwrapBlob:]_block_invoke.33
- ___24-[POKeyWrap unwrapBlob:]_block_invoke.33.cold.1
- ___24-[POKeyWrap unwrapBlob:]_block_invoke.39
- ___24-[POKeyWrap unwrapBlob:]_block_invoke.39.cold.1
- ___24-[POKeyWrap unwrapBlob:]_block_invoke.45
- ___24-[POKeyWrap unwrapBlob:]_block_invoke.45.cold.1
- ___38-[PODeviceConfiguration initWithData:]_block_invoke.172
- ___59-[PODaemonCoreProcess _pendingSSOTokensForIdentifer:error:]_block_invoke
- ___59-[PODaemonCoreProcess _pendingSSOTokensForIdentifer:error:]_block_invoke.cold.1
- ___59-[PODaemonCoreProcess _stashedSSOTokensForIdentifer:error:]_block_invoke
- ___59-[PODaemonCoreProcess _stashedSSOTokensForIdentifer:error:]_block_invoke.cold.1
- ___65-[PODaemonCoreProcess loginConfigurationForIdentifer:completion:]_block_invoke
- ___65-[PODaemonCoreProcess loginConfigurationForIdentifer:completion:]_block_invoke.cold.1
- ___66-[PODaemonCoreProcess deviceConfigurationForIdentifer:completion:]_block_invoke
- ___66-[PODaemonCoreProcess deviceConfigurationForIdentifer:completion:]_block_invoke.cold.1
- ___68-[PODaemonCoreConnection loginConfigurationForIdentifer:completion:]_block_invoke
- ___68-[PODaemonCoreConnection loginConfigurationForIdentifer:completion:]_block_invoke.cold.1
- ___68-[PODaemonCoreConnection savePendingSSOTokens:identifer:completion:]_block_invoke
- ___68-[PODaemonCoreConnection savePendingSSOTokens:identifer:completion:]_block_invoke.cold.1
- ___68-[PODaemonCoreConnection saveStashedSSOTokens:identifer:completion:]_block_invoke
- ___68-[PODaemonCoreConnection saveStashedSSOTokens:identifer:completion:]_block_invoke.cold.1
- ___69-[PODaemonCoreConnection deviceConfigurationForIdentifer:completion:]_block_invoke
- ___69-[PODaemonCoreConnection deviceConfigurationForIdentifer:completion:]_block_invoke.cold.1
- ___73-[PODaemonCoreConnection retrievePendingSSOTokenForIdentifer:completion:]_block_invoke
- ___73-[PODaemonCoreConnection retrievePendingSSOTokenForIdentifer:completion:]_block_invoke.cold.1
- ___73-[PODaemonCoreConnection retrieveStashedSSOTokenForIdentifer:completion:]_block_invoke
- ___73-[PODaemonCoreConnection retrieveStashedSSOTokenForIdentifer:completion:]_block_invoke.cold.1
- ___76-[PODaemonCoreConnection saveStashedDecryptionContext:identifer:completion:]_block_invoke
- ___76-[PODaemonCoreConnection saveStashedDecryptionContext:identifer:completion:]_block_invoke.cold.1
- ___82-[PODaemonCoreConnection retrieveStashedDecryptionContextForIdentifer:completion:]_block_invoke
- ___82-[PODaemonCoreConnection retrieveStashedDecryptionContextForIdentifer:completion:]_block_invoke.cold.1
- ___block_descriptor_tmp.127
- ___block_descriptor_tmp.139
- ___block_descriptor_tmp.150
- ___block_descriptor_tmp.153
- ___block_descriptor_tmp.169
- ___block_literal_global.152
- ___block_literal_global.155
- ___block_literal_global.171
- ___block_literal_global.443
- ___block_literal_global.56
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_PlatformSSOCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_PlatformSSOCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_PlatformSSOCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_PlatformSSOCore
- _objc_msgSend$_deviceConfigurationForIdentifer:
- _objc_msgSend$_loginConfigurationForIdentifer:
- _objc_msgSend$_pendingSSOTokensForIdentifer:error:
- _objc_msgSend$_stashedSSOTokensForIdentifer:error:
- _objc_msgSend$deviceConfigurationForIdentifer:completion:
- _objc_msgSend$loginConfigurationForIdentifer:completion:
- _objc_msgSend$retrievePendingSSOTokenForIdentifer:completion:
- _objc_msgSend$retrieveStashedDecryptionContextForIdentifer:completion:
- _objc_msgSend$retrieveStashedSSOTokenForIdentifer:completion:
- _objc_msgSend$savePendingSSOTokens:identifer:completion:
- _objc_msgSend$saveStashedDecryptionContext:identifer:completion:
- _objc_msgSend$saveStashedSSOTokens:identifer:completion:
CStrings:
+ "%s identifier = %{public}@, data = %{public}@ on %@"
+ "-[PODaemonCoreProcess _deviceConfigurationForIdentifier:]"
+ "-[PODaemonCoreProcess _loginConfigurationForIdentifier:]"
+ "-[PODaemonCoreProcess _pendingSSOTokensForIdentifier:error:]"
+ "-[PODaemonCoreProcess _stashedSSOTokensForIdentifier:error:]"
+ "-[PODaemonCoreProcess deviceConfigurationForIdentifier:completion:]"
+ "-[PODaemonCoreProcess loginConfigurationForIdentifier:completion:]"
+ "-[PODaemonCoreProcess retrievePendingSSOTokenForIdentifier:completion:]"
+ "-[PODaemonCoreProcess retrieveStashedSSOTokenForIdentifier:completion:]"
+ "-[PODaemonCoreProcess savePendingSSOTokens:identifier:completion:]"
+ "-[PODaemonCoreProcess saveStashedDecryptionContext:identifier:completion:]"
+ "-[PODaemonCoreProcess saveStashedSSOTokens:identifier:completion:]"
+ "/.exclave"
+ "Failed to allocate memory for wrapped blob"
+ "Failed to get hash for key."
+ "Input blob too large for wrapping"
+ "Integer overflow in blob size calculation"
+ "Invalid input blob with null bytes but non-zero length"
+ "Invalid wrapped key size of 0"
+ "TB,V_temporarySessionQuickLogin"
+ "Wrapped key size exceeds maximum allowed size"
+ "_deviceConfigurationForIdentifier:"
+ "_loginConfigurationForIdentifier:"
+ "_pendingSSOTokensForIdentifier:error:"
+ "_stashedSSOTokensForIdentifier:error:"
+ "_temporarySessionQuickLogin"
+ "deviceConfigurationForIdentifier:completion:"
+ "loginConfigurationForIdentifier:completion:"
+ "retrievePendingSSOTokenForIdentifier:completion:"
+ "retrieveStashedDecryptionContextForIdentifier:completion:"
+ "retrieveStashedSSOTokenForIdentifier:completion:"
+ "savePendingSSOTokens:identifier:completion:"
+ "saveStashedDecryptionContext:identifier:completion:"
+ "saveStashedSSOTokens:identifier:completion:"
+ "setTemporarySessionQuickLogin:"
+ "temporarySessionQuickLogin"
- "%s identifer = %{public}@ on %@"
- "%s identifer = %{public}@, data = %{public}@ on %@"
- "-[PODaemonCoreProcess _deviceConfigurationForIdentifer:]"
- "-[PODaemonCoreProcess _loginConfigurationForIdentifer:]"
- "-[PODaemonCoreProcess _pendingSSOTokensForIdentifer:error:]"
- "-[PODaemonCoreProcess _stashedSSOTokensForIdentifer:error:]"
- "-[PODaemonCoreProcess deviceConfigurationForIdentifer:completion:]"
- "-[PODaemonCoreProcess loginConfigurationForIdentifer:completion:]"
- "-[PODaemonCoreProcess retrievePendingSSOTokenForIdentifer:completion:]"
- "-[PODaemonCoreProcess retrieveStashedSSOTokenForIdentifer:completion:]"
- "-[PODaemonCoreProcess savePendingSSOTokens:identifer:completion:]"
- "-[PODaemonCoreProcess saveStashedDecryptionContext:identifer:completion:]"
- "-[PODaemonCoreProcess saveStashedSSOTokens:identifer:completion:]"
- "Error with wrap key"
- "Falied to get hash for key."
- "_deviceConfigurationForIdentifer:"
- "_loginConfigurationForIdentifer:"
- "_pendingSSOTokensForIdentifer:error:"
- "_stashedSSOTokensForIdentifer:error:"
- "accessKeyReaderGroupIdentifier"
- "allowAccessKeyExpressMode"
- "deviceConfigurationForIdentifer:completion:"
- "loginConfigurationForIdentifer:completion:"
- "retrievePendingSSOTokenForIdentifer:completion:"
- "retrieveStashedDecryptionContextForIdentifer:completion:"
- "retrieveStashedSSOTokenForIdentifer:completion:"
- "savePendingSSOTokens:identifer:completion:"
- "saveStashedDecryptionContext:identifer:completion:"
- "saveStashedSSOTokens:identifer:completion:"

```
