## com.apple.driver.AppleMobileApNonce

> `com.apple.driver.AppleMobileApNonce`

```diff

-44.0.0.0.0
-  __TEXT.__cstring: 0x10bc
+47.0.0.0.0
+  __TEXT.__cstring: 0x1861
   __TEXT.__const: 0x12
-  __TEXT_EXEC.__text: 0x3844
+  __TEXT_EXEC.__text: 0x3fdc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
   __DATA.__bss: 0x8
   __DATA_CONST.__auth_got: 0x1a8
   __DATA_CONST.__got: 0x50
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x1470
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: D441A6C3-EC31-3BD6-9DE5-D049B14F2D69
-  Functions: 102
-  Symbols:   504
-  CStrings:  109
+  UUID: F771CA88-8BBF-3E53-AEE7-65A2074B4255
+  Functions: 101
+  Symbols:   507
+  CStrings:  154
 
Symbols:
+ _ZN18AppleMobileApNonce18_printNonceAndHashEyPKvm.cold.1
+ ___chkstk_darwin
+ ___chkstk_darwin_probe
Functions:
~ __ZN28AppleMobileApNonceUserClient5startEP9IOService : 172 -> 232
~ __ZN28AppleMobileApNonceUserClient11clientCloseEv : 72 -> 116
~ __ZN28AppleMobileApNonceUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv : 452 -> 432
- sub_fffffe0009c74710
~ __ZN18AppleMobileApNonce5startEP9IOService : 1788 -> 1952
~ __ZN18AppleMobileApNonce15registerServiceEj : 220 -> 240
~ __ZN18AppleMobileApNonce14_generateNonceEPvPm : 1012 -> 1084
~ __ZN18AppleMobileApNonce22_getBootedSlotAndStateEPhS0_ : 616 -> 620
~ __ZN18AppleMobileApNonce13retrieveNonceEPvPm : 160 -> 260
~ __ZN18AppleMobileApNonce14_retrieveNonceEPy : 1016 -> 1112
~ __ZN18AppleMobileApNonce18_printNonceAndHashEyPKvm : 8 -> 360
~ __ZN18AppleMobileApNonce17_pickNewNonceSlotEPh : 268 -> 264
~ __ZN18AppleMobileApNonce19_waitForSandcatInitEv : 100 -> 104
~ __ZN18AppleMobileApNonce18_generateNonceHashEyPh : 1300 -> 1356
~ __ZN18AppleMobileApNonce10_readNonceEPP8OSString : 460 -> 876
~ __ZN18AppleMobileApNonce21_waitForNVRAMReadableEv : 76 -> 152
~ __ZN18AppleMobileApNonce21_waitForNVRAMWritableEv : 76 -> 156
~ __ZN18AppleMobileApNonce15_saveNonceGatedEPKc : 132 -> 236
~ __ZN18AppleMobileApNonce21_saveNonceInfoInNVRAMEPKc : 572 -> 612
~ __ZN18AppleMobileApNonce16_clearNonceGatedEv : 116 -> 220
~ __ZN18AppleMobileApNonce24_clearNonceInfoFromNVRAMEv : 312 -> 368
~ __ZN18AppleMobileApNonce15_readNonceGatedEPP8OSString : 132 -> 236
~ __ZN18AppleMobileApNonce19_readNonceFromNVRAMEPP8OSString : 296 -> 364
+ ___chkstk_darwin
CStrings:
+ "%s%s:\n%s    Got IODTNVRAM\n"
+ "%s%s:\n%s    Got IONVRAM\n"
+ "%s%s:\n%s    Hash: %s\n"
+ "%s%s:\n%s    Nonce: 0x%016llX\n"
+ "%s%s:\n%s    Waiting for IODTNVRAM\n"
+ "%s%s:\n%s    Waiting for IONVRAM\n"
+ "%s%s:\n%s    _clearNonceInfoFromNVRAM done: 0x%X\n"
+ "%s%s:\n%s    _readNonce call _getCommandGate action: 0x%X\n"
+ "%s%s:\n%s    _readNonce done: 0x%X (%s)\n\n"
+ "%s%s:\n%s    _readNonce get slot info: current_slot_state=%d, _nonce_slot_id=%d\n"
+ "%s%s:\n%s    _readNonce: _sandcatSupported=%d\n"
+ "%s%s:\n%s    _readNonce: failed because SEP is not up\n"
+ "%s%s:\n%s    _readNonce: nonce(bncn) 0x%016llX\n"
+ "%s%s:\n%s    _readNonce: return string %p, nonce_string %s\n"
+ "%s%s:\n%s    _readNonceFromNVRAM done: 0x%X\n"
+ "%s%s:\n%s    _saveNonceInfoInNVRAM done: 0x%X\n"
+ "%s%s:\n%s    called _clearNonceInfoFromNVRAM\n"
+ "%s%s:\n%s    called _readNonceFromNVRAM\n"
+ "%s%s:\n%s    called _saveNonceInfoInNVRAM\n"
+ "%s%s:\n%s    calling _clearNonceInfoFromNVRAM\n"
+ "%s%s:\n%s    calling _readNonceFromNVRAM\n"
+ "%s%s:\n%s    calling _saveNonceInfoInNVRAM\n"
+ "%s%s:\n%s    closed\n"
+ "%s%s:\n%s    entering\n"
+ "%s%s:\n%s    leaving: 0x%X\n"
+ "%s%s:\n%s    leaving: 0x%X %p\n"
+ "%s%s:\n%s    raw nonce: 0x%016llx  ciphertext 0x%016llx%016llx\n"
+ "%s%s:\n%s    raw nonce: 0x%016llx  plaintext 0x%016llx%016llx\n"
+ "%s%s:\n%s    retrieveNonce _allowApNonceRetrieval: %d\n"
+ "%s%s:\n%s    retrieveNonce assign result to kIOReturnNotPermitted\n"
+ "%s%s:\n%s    retrieveNonce done: 0x%X\n"
+ "%s%s:\n%s    start: _allowApNonceRetrieval=%d\n"
+ "%s%s:\n%s    start: _cryptoHashMethod=%d\n"
+ "%s%s:\n%s    start: _entangleNonce=%d\n"
+ "%s%s:\n%s    start: _sandcatSupported=%d\n"
+ "%s%s:\n%s    start: aes-service-publish-timeout %llu seconds\n"
+ "%s%s:\n%s    started\n"
+ "CLIENT: "
+ "IOReturn AppleMobileApNonce::_clearNonceGated()"
+ "IOReturn AppleMobileApNonce::_readNonceGated(OSString **)"
+ "IOReturn AppleMobileApNonce::_saveNonceGated(const char *)"
+ "SPEW: "
+ "static void AppleMobileApNonce::_printNonceAndHash(uint64_t, const void *, size_t)"
+ "virtual IOReturn AppleMobileApNonceUserClient::clientClose()"
+ "void AppleMobileApNonce::_waitForNVRAMWritable()"

```
