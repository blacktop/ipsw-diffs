## DeviceDiscoveryUICore

> `/System/Library/PrivateFrameworks/DeviceDiscoveryUICore.framework/Versions/A/DeviceDiscoveryUICore`

```diff

-2060.40.21.0.0
-  __TEXT.__text: 0xd448
+2060.50.171.1.2
+  __TEXT.__text: 0xd40c
   __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_methlist: 0xb34
+  __TEXT.__objc_methlist: 0xe24
   __TEXT.__const: 0xca
   __TEXT.__cstring: 0x8ce
   __TEXT.__oslogstring: 0x1bb9
   __TEXT.__gcc_except_tab: 0x208
-  __TEXT.__unwind_info: 0x3c0
+  __TEXT.__unwind_info: 0x3d0
   __TEXT.__objc_classname: 0x298
   __TEXT.__objc_methname: 0x252e
   __TEXT.__objc_methtype: 0x78f

   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x848
+  __DATA_CONST.__objc_selrefs: 0x8d8
   __DATA_CONST.__objc_superrefs: 0x58
   __AUTH_CONST.__auth_got: 0x198
   __AUTH_CONST.__const: 0x700
   __AUTH_CONST.__cfstring: 0xa60
-  __AUTH_CONST.__objc_const: 0x20f0
+  __AUTH_CONST.__objc_const: 0x1b80
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x4b0
   __DATA.__objc_ivar: 0x100

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 0363DF00-9FCE-3BD2-886A-679EC8D4E4D5
-  Functions: 331
-  Symbols:   956
+  UUID: 2D7E1A51-0C22-3E55-AFCC-76D74137B7AB
+  Functions: 333
+  Symbols:   958
   CStrings:  808
 
Symbols:
+ DDUICorePrimaryQueue.cold.1
+ _DDUIEndpointPairingSessionStateString
Functions:
~ _DDUICorePrimaryQueue : 84 -> 68
~ -[DDUIApplicationInfo initWithDictionaryRepresentation:] : 348 -> 352
~ -[_DDUIRapportPairingTransport setAvailableDevicesChangedHandler:] : 608 -> 596
~ -[_DDUIRapportPairingTransport _setupListeningForResponseMessagesIfNeeded] : 228 -> 220
~ -[_DDUIRapportPairingTransport setupListeningForSessionsWithHandler:] : 580 -> 572
~ -[DDUICoreAgent _setupListenerIfNeededWithCompletion:] : 676 -> 672
~ -[DDUICoreAgent _showNotificationForPairingSession:pairingMessage:] : 440 -> 432
~ -[DDUIPairInitiateMessage initWithDictionaryRepresentation:] : 144 -> 148
~ -[_DDUIRapportOutgoingTransportSession activateWithErrorHandler:messageHandler:completion:] : 828 -> 816
~ -[DDUIEndpointPairingSession _activateWithErrorHandler:completionHandler:] : 548 -> 532
~ -[DDUIEndpointPairingSession _pairWithInfo:] : 296 -> 288
~ -[DDUIEndpointPairingSession _handleIncomingMessage:] : 1124 -> 1112
+ _DDUIEndpointPairingSessionStateString
~ -[DDUIRapportPeopleDiscovery initWithRemoteDisplayDiscovery:deviceSelectedHandler:] : 548 -> 528
~ -[DDUIRapportPeopleDiscovery activateDiscoveryWithCompletion:] : 256 -> 248
~ -[DDUIRapportPeopleDiscovery setAvailablePeopleChangedHandler:] : 736 -> 720
~ -[DDUIRapportPeopleDiscovery setPersonDeclinedHandler:] : 120 -> 112
~ -[DDUIPairCompleteMessage initWithDictionaryRepresentation:] : 316 -> 320
+ DDUICorePrimaryQueue.cold.1
~ -[DDUIEndpointPairingSession _handleIncomingMessage:].cold.1 : 204 -> 232

```
