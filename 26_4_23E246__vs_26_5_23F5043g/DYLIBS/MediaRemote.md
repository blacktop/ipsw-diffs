## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4025.510.1.0.0
-  __TEXT.__text: 0x31471c
-  __TEXT.__auth_stubs: 0x16f0
+4025.600.4.0.0
+  __TEXT.__text: 0x316df4
+  __TEXT.__auth_stubs: 0x16c0
   __TEXT.__objc_methlist: 0x2b430
   __TEXT.__const: 0x5f0
-  __TEXT.__cstring: 0x2c007
+  __TEXT.__cstring: 0x2c6f0
   __TEXT.__oslogstring: 0xdc9e
-  __TEXT.__gcc_except_tab: 0x63b4
-  __TEXT.__dlopen_cstrs: 0x514
+  __TEXT.__gcc_except_tab: 0x6588
+  __TEXT.__dlopen_cstrs: 0x6b1
   __TEXT.__ustring: 0x7b8
-  __TEXT.__unwind_info: 0xcc28
+  __TEXT.__unwind_info: 0xcd40
   __TEXT.__objc_classname: 0x4e1c
   __TEXT.__objc_methname: 0x4dabe
   __TEXT.__objc_methtype: 0x913a
   __TEXT.__objc_stubs: 0x28780
   __DATA_CONST.__got: 0x1450
-  __DATA_CONST.__const: 0xb308
+  __DATA_CONST.__const: 0xb380
   __DATA_CONST.__objc_classlist: 0x11b8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x268

   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0xfe8
   __DATA_CONST.__objc_arraydata: 0x260
-  __AUTH_CONST.__auth_got: 0xb88
-  __AUTH_CONST.__const: 0x3120
-  __AUTH_CONST.__cfstring: 0x23520
+  __AUTH_CONST.__auth_got: 0xb70
+  __AUTH_CONST.__const: 0x3100
+  __AUTH_CONST.__cfstring: 0x23500
   __AUTH_CONST.__objc_const: 0x46188
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x8340
-  __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0x3268
   __DATA.__data: 0x1d40
-  __DATA.__bss: 0x818
+  __DATA.__bss: 0x8c0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2df0
   __DATA_DIRTY.__data: 0x48

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4907BB78-08DA-30B2-A38F-E1B52F3CB9FF
-  Functions: 20441
-  Symbols:   56244
-  CStrings:  24520
+  UUID: F204ED9A-E18F-3CE9-8542-E7420FB8F34B
+  Functions: 20494
+  Symbols:   56383
+  CStrings:  24544
 
Symbols:
+ -[MRCoreUtilsPairingSession _delegateDidEnterPasscode:].cold.1
+ -[MRCoreUtilsPairingSession _onQueueInitializePairingSessionWithState:].cold.1
+ -[MRCoreUtilsPairingSession _onQueueInitializePairingSessionWithState:].cold.2
+ -[MRCoreUtilsPairingSession _onQueueInitializePairingSessionWithState:].cold.3
+ -[MRCoreUtilsPairingSession _onQueuePerformPairingExchangeWithInputData:error:].cold.1
+ -[MRCoreUtilsPairingSession initializePairingSession:].cold.1
+ -[MRCoreUtilsPairingSession setPairingFlags:].cold.1
+ -[MRStreamTransportConnection _setQOSPropertiesOnStream:].cold.1
+ _AVFoundationLibrary
+ _AVFoundationLibrary.cold.1
+ _AVFoundationLibraryCore.frameworkLibrary
+ _AirPlaySupportLibraryCore
+ _CoreUtilsLibrary
+ _CoreUtilsLibrary.cold.1
+ _ProximityControlLibrary
+ _ProximityControlLibrary.cold.1
+ _ProximityControlLibraryCore.frameworkLibrary
+ ___41-[MRCoreUtilsPairingSession openInState:]_block_invoke.9
+ ___51-[MRCoreUtilsPairingSession decryptData:withError:]_block_invoke.cold.1
+ ___51-[MRCoreUtilsPairingSession encryptData:withError:]_block_invoke.cold.1
+ ___AVFoundationLibraryCore_block_invoke
+ ___ProximityControlLibraryCore_block_invoke
+ ___block_literal_global.619
+ ___block_literal_global.649
+ ___block_literal_global.74
+ ___getAVAudioCompressedBufferClass_block_invoke
+ ___getAVAudioCompressedBufferClass_block_invoke.cold.1
+ ___getAVAudioFormatClass_block_invoke
+ ___getAVAudioFormatClass_block_invoke.cold.1
+ ___getCUPairingManagerClass_block_invoke
+ ___getCUPairingManagerClass_block_invoke.cold.1
+ ___getPCMediaRemoteDisplayContextClass_block_invoke
+ ___getPCMediaRemoteDisplayContextClass_block_invoke.cold.1
+ ___getPCProgressEventClass_block_invoke
+ ___getPCProgressEventClass_block_invoke.cold.1
+ ___getPairingSessionCopyPeerIdentifierSymbolLoc_block_invoke
+ ___getPairingSessionCopyPeersSymbolLoc_block_invoke
+ ___getPairingSessionCreateSymbolLoc_block_invoke
+ ___getPairingSessionDeleteIdentitySymbolLoc_block_invoke
+ ___getPairingSessionDeletePeerSymbolLoc_block_invoke
+ ___getPairingSessionDeriveKeySymbolLoc_block_invoke
+ ___getPairingSessionExchangeSymbolLoc_block_invoke
+ ___getPairingSessionSetACLSymbolLoc_block_invoke
+ ___getPairingSessionSetFlagsSymbolLoc_block_invoke
+ ___getPairingSessionSetKeychainInfoSymbolLoc_block_invoke
+ ___getPairingSessionSetSetupCodeSymbolLoc_block_invoke
+ ___getPairingSessionUpdatePeerInfoSymbolLoc_block_invoke
+ ___getSocketSetQoSSymbolLoc_block_invoke
+ ___getSocketSetQoSSymbolLoc_block_invoke.cold.1
+ ___getchacha20_poly1305_decrypt_all_64x64SymbolLoc_block_invoke
+ ___getchacha20_poly1305_encrypt_all_64x64SymbolLoc_block_invoke
+ _audit_stringAVFoundation
+ _audit_stringProximityControl
+ _getAPSCopyDefaultGroupUUIDSymbolLoc
+ _getAVAudioCompressedBufferClass.softClass
+ _getAVAudioFormatClass.softClass
+ _getCUPairingManagerClass.softClass
+ _getPCMediaRemoteDisplayContextClass.softClass
+ _getPCProgressEventClass.softClass
+ _getPairingSessionCopyPeerIdentifierSymbolLoc.ptr
+ _getPairingSessionCopyPeersSymbolLoc.ptr
+ _getPairingSessionCreateSymbolLoc.ptr
+ _getPairingSessionDeleteIdentitySymbolLoc.ptr
+ _getPairingSessionDeletePeerSymbolLoc.ptr
+ _getPairingSessionDeriveKeySymbolLoc.ptr
+ _getPairingSessionExchangeSymbolLoc.ptr
+ _getPairingSessionSetACLSymbolLoc.ptr
+ _getPairingSessionSetFlagsSymbolLoc.ptr
+ _getPairingSessionSetKeychainInfoSymbolLoc.ptr
+ _getPairingSessionSetSetupCodeSymbolLoc.ptr
+ _getPairingSessionUpdatePeerInfoSymbolLoc.ptr
+ _getSocketSetQoSSymbolLoc.ptr
+ _getchacha20_poly1305_decrypt_all_64x64SymbolLoc.ptr
+ _getchacha20_poly1305_encrypt_all_64x64SymbolLoc.ptr
+ _soft_PairingSessionCopyPeerIdentifier
+ _soft_PairingSessionCopyPeerIdentifier.cold.1
+ _soft_PairingSessionCopyPeers
+ _soft_PairingSessionCopyPeers.cold.1
+ _soft_PairingSessionDeletePeer
+ _soft_PairingSessionDeletePeer.cold.1
+ _soft_PairingSessionDeriveKey
+ _soft_PairingSessionDeriveKey.cold.1
+ _soft_PairingSessionUpdatePeerInfo
+ _soft_PairingSessionUpdatePeerInfo.cold.1
- GCC_except_table109
- _MSVWeakLinkClass
- _MSVWeakLinkSymbol
- _PCMediaRemoteDisplayContextFunction
- _PCProgressEventFunction
- _ProximityControlLibrary.sLib
- _ProximityControlLibrary.sOnce
- ___41-[MRCoreUtilsPairingSession openInState:]_block_invoke.15
- ___ProximityControlLibrary_block_invoke
- ___block_literal_global.625
- ___block_literal_global.652
- ___block_literal_global.90
- _classPCMediaRemoteDisplayContext
- _classPCProgressEvent
- _dlopen
- _initPCMediaRemoteDisplayContext
- _initPCMediaRemoteDisplayContext.cold.1
- _initPCProgressEvent
- _initPCProgressEvent.cold.1
CStrings:
+ "CFArrayRef soft_PairingSessionCopyPeers(PairingSessionRef, OSStatus *)"
+ "Class getAVAudioCompressedBufferClass(void)_block_invoke"
+ "Class getAVAudioFormatClass(void)_block_invoke"
+ "Class getCUPairingManagerClass(void)_block_invoke"
+ "Class getPCMediaRemoteDisplayContextClass(void)_block_invoke"
+ "Class getPCProgressEventClass(void)_block_invoke"
+ "MRAudio.m"
+ "MRCoreUtilsSoftLinking.h"
+ "MRProximityProvider.m"
+ "MRStreamTransportConnection.m"
+ "OSStatus soft_PairingSessionCreate(PairingSessionRef *, const PairingDelegate *, PairingSessionType)"
+ "OSStatus soft_PairingSessionDeleteIdentity(PairingSessionRef)"
+ "OSStatus soft_PairingSessionDeletePeer(PairingSessionRef, const void *, size_t)"
+ "OSStatus soft_PairingSessionDeriveKey(PairingSessionRef, const void *, size_t, const void *, size_t, size_t, uint8_t *)"
+ "OSStatus soft_PairingSessionExchange(PairingSessionRef, const void *, size_t, uint8_t **, size_t *, Boolean *)"
+ "OSStatus soft_PairingSessionSetSetupCode(PairingSessionRef, const void *, size_t)"
+ "OSStatus soft_PairingSessionUpdatePeerInfo(PairingSessionRef, const void *, size_t, CFDictionaryRef)"
+ "OSStatus soft_SocketSetQoS(SocketRef, int)"
+ "OSStatus soft_chacha20_poly1305_decrypt_all_64x64(const uint8_t *, const uint8_t *, const void *, size_t, const void *, size_t, void *, const uint8_t *)"
+ "char *soft_PairingSessionCopyPeerIdentifier(PairingSessionRef, size_t *, OSStatus *)"
+ "softlink:r:path:/System/Library/Frameworks/AVFoundation.framework/AVFoundation"
+ "softlink:r:path:/System/Library/PrivateFrameworks/ProximityControl.framework/ProximityControl"
+ "void *AVFoundationLibrary(void)"
+ "void *ProximityControlLibrary(void)"
+ "void soft_PairingSessionSetACL(PairingSessionRef, CFDictionaryRef)"
+ "void soft_PairingSessionSetFlags(PairingSessionRef, PairingFlags)"
+ "void soft_PairingSessionSetKeychainInfo(PairingSessionRef, CFStringRef, uint32_t, CFStringRef, CFStringRef, uint32_t, CFStringRef, CFStringRef, PairingKeychainFlags)"
+ "void soft_chacha20_poly1305_encrypt_all_64x64(const uint8_t *, const uint8_t *, const void *, size_t, const void *, size_t, void *, uint8_t *)"
- "/System/Library/PrivateFrameworks/ProximityControl.framework/ProximityControl"
- "AVFoundation"
- "CoreUtils"

```
