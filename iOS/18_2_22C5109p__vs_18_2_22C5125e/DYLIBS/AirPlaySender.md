## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-835.13.1.11.1
-  __TEXT.__text: 0x1c91cc
-  __TEXT.__auth_stubs: 0x5070
+835.16.1.0.0
+  __TEXT.__text: 0x1c9efc
+  __TEXT.__auth_stubs: 0x50a0
   __TEXT.__objc_methlist: 0x340
-  __TEXT.__cstring: 0x72681
+  __TEXT.__cstring: 0x72b5b
   __TEXT.__const: 0xfd70
-  __TEXT.__gcc_except_tab: 0x3fc
+  __TEXT.__gcc_except_tab: 0x41c
   __TEXT.__oslogstring: 0x69f
-  __TEXT.__unwind_info: 0x2ad0
+  __TEXT.__unwind_info: 0x2ae8
   __TEXT.__eh_frame: 0xaa8
   __TEXT.__objc_classname: 0x174
   __TEXT.__objc_methname: 0x19a5

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x680
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x2848
+  __AUTH_CONST.__auth_got: 0x2860
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x7a20
-  __AUTH_CONST.__cfstring: 0x10c60
+  __AUTH_CONST.__const: 0x7a60
+  __AUTH_CONST.__cfstring: 0x10d00
   __AUTH_CONST.__objc_const: 0x1178
   __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x738
   __DATA.__objc_ivar: 0x64
-  __DATA.__data: 0x18448
-  __DATA.__bss: 0x9b0
+  __DATA.__data: 0x183d8
+  __DATA.__bss: 0x9d0
   __DATA.__common: 0xa08
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0xcc0
+  __DATA_DIRTY.__data: 0xd30
   __DATA_DIRTY.__bss: 0x2d0
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3349
-  Symbols:   6287
-  CStrings:  9768
+  Functions: 3357
+  Symbols:   6298
+  CStrings:  9797
 
Symbols:
+ _APSGetAirPlayNonSystemPeersCount
+ _APSRemoveAirPlayNonSystemPeers
+ _CFPrefs_SetValue
CStrings:
+ " with new value"
+ "835.16.1"
+ "Boolean coreUtilsPairing_IsPeerKnown(APPairingClientRef)"
+ "Failed to remove"
+ "Non-System (mostly CarPlay) peers"
+ "OSStatus APPairingClientCoreUtilsCreate(CFAllocatorRef, CFStringRef, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, CFStringRef, CFStringRef, CFDataRef, FigTransportStreamRef, CFStringRef, APPairingClientRef *)"
+ "OSStatus coreUtilsPairingPeerCache_SavePeer(const void *, size_t, const uint8_t *, void *)"
+ "OSStatus coreUtilsPairingPeerCache_SavePeer(const void *, size_t, const uint8_t *, void *)_block_invoke_2"
+ "Peer Cache"
+ "PeerIdentifier"
+ "PeerPublicKey"
+ "Stored new"
+ "Successfully removed"
+ "Updated"
+ "[%!{(MISSING)ptr}] %!s(MISSING) %!s(MISSING) from the Keychain (took %!l(MISSING)lu ms)%!?(MISSING){end}, error: %!m(MISSING)\n"
+ "[%!{(MISSING)ptr}] %!s(MISSING) item in %!s(MISSING)%!s(MISSING):\n\"%!@(MISSING)\" :\n%!@(MISSING)"
+ "[%!{(MISSING)ptr}] %!s(MISSING)[%!u(MISSING)]:\n%!@(MISSING) :\n%!@(MISSING)"
+ "[%!{(MISSING)ptr}] APPairingClientCoreUtils created %!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING).\n"
+ "[%!{(MISSING)ptr}] All items in %!s(MISSING):"
+ "[%!{(MISSING)ptr}] Forcing coreUtilsPairing_IsPeerKnown to return false\n"
+ "[%!{(MISSING)ptr}] Forcing coreUtilsPairing_IsPeerKnown to return true\n"
+ "[%!{(MISSING)ptr}] Is peer known: %!d(MISSING), peerIdentifier: %!s(MISSING) (processing time: %!l(MISSING)lu ms, err: %!d(MISSING))\n"
+ "[%!{(MISSING)ptr}] Number of %!s(MISSING) in the Keychain: %!l(MISSING)lu (excessive peers cleanup is %!s(MISSING), threshold for cleanup: %!d(MISSING))."
+ "[%!{(MISSING)ptr}] Number of items in %!s(MISSING): %!d(MISSING)"
+ "[%!{(MISSING)ptr}] PairingSessionCopyPeerIdentifier returned %!s(MISSING) (err: %!d(MISSING)) \n"
+ "[%!{(MISSING)ptr}] Removing random item from %!s(MISSING):\n\"%!@(MISSING)\" :\n%!@(MISSING)"
+ "[%!{(MISSING)ptr}] Using %!s(MISSING) with size: %!d(MISSING)\n"
+ "coreUtilsPairingPeerCache_SavePeer"
+ "disableCarPlayPeersCleanup"
+ "forcePeerKnown"
+ "forcePeerUnknown"
+ "void carManager_cleanupCarPlayPeersInKeychainIfNeeded(FigEndpointManagerRef)"
- "835.13.1.11.1"
- "OSStatus APPairingClientCoreUtilsCreate(CFAllocatorRef, CFStringRef, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, CFStringRef, CFStringRef, CFDataRef, FigTransportStreamRef, APPairingClientRef *)"
- "[%!{(MISSING)ptr}] APPairingClientCoreUtils created %!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING).\n"

```
