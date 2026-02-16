## libnfshared.dylib

> `/usr/lib/libnfshared.dylib`

```diff

-363.10.0.0.0
-  __TEXT.__text: 0x20880
-  __TEXT.__auth_stubs: 0xb50
+364.20.0.0.0
+  __TEXT.__text: 0x206ac
+  __TEXT.__auth_stubs: 0xaf0
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x1e24
-  __TEXT.__const: 0x220
-  __TEXT.__cstring: 0x3a11
-  __TEXT.__oslogstring: 0x16d8
-  __TEXT.__unwind_info: 0x5e0
-  __TEXT.__objc_classname: 0x326
-  __TEXT.__objc_methname: 0x3f82
-  __TEXT.__objc_methtype: 0x96b
-  __TEXT.__objc_stubs: 0x2500
-  __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x518
-  __DATA_CONST.__objc_classlist: 0xf0
+  __TEXT.__objc_methlist: 0x1ff4
+  __TEXT.__const: 0x210
+  __TEXT.__cstring: 0x4005
+  __TEXT.__oslogstring: 0x133a
+  __TEXT.__unwind_info: 0x6b8
+  __TEXT.__objc_classname: 0x354
+  __TEXT.__objc_methname: 0x4323
+  __TEXT.__objc_methtype: 0x9bd
+  __TEXT.__objc_stubs: 0x2660
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__const: 0x560
+  __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1150
+  __DATA_CONST.__objc_selrefs: 0x11f8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xb8
-  __DATA_CONST.__objc_arraydata: 0x3e8
-  __AUTH_CONST.__auth_got: 0x5b8
-  __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x3b00
-  __AUTH_CONST.__objc_const: 0x3520
+  __DATA_CONST.__objc_superrefs: 0xc0
+  __DATA_CONST.__objc_arraydata: 0x420
+  __AUTH_CONST.__auth_got: 0x588
+  __AUTH_CONST.__const: 0x200
+  __AUTH_CONST.__cfstring: 0x3d40
+  __AUTH_CONST.__objc_const: 0x3820
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0x218
-  __DATA.__data: 0x3d8
+  __AUTH.__objc_data: 0x460
+  __DATA.__objc_ivar: 0x228
+  __DATA.__data: 0x3d0
   __DATA.__bss: 0x10
-  __DATA.__common: 0x28
+  __DATA.__common: 0x68
+  __DATA_DIRTY.__objc_ivar: 0x10
   __DATA_DIRTY.__objc_data: 0x5a0
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0x120
-  __DATA_DIRTY.__common: 0x78
+  __DATA_DIRTY.__bss: 0xf8
+  __DATA_DIRTY.__common: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
-  - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0E8DCE28-E447-36DC-9383-4DBBFCE795EE
-  Functions: 640
-  Symbols:   379
-  CStrings:  2168
+  UUID: BC39017C-40FB-3A7E-A2A4-F8F59E85D5AD
+  Functions: 673
+  Symbols:   377
+  CStrings:  2301
 
Symbols:
+ _NFProductCopyName
+ _OBJC_CLASS_$_NFAssertionInternalWrapper
+ _OBJC_CLASS_$_NFCoreNFCPollConfig
+ _OBJC_METACLASS_$_NFAssertionInternalWrapper
+ _OBJC_METACLASS_$_NFCoreNFCPollConfig
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x25
+ _objc_retain_x26
+ _snprintf
- _NFProductGetName
- ___sprintf_chk
- _class_isMetaClass
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x4
- _objc_retain_x7
- _objc_retain_x8
- _object_getClassName
- _sprintf
CStrings:
+ "\t"
+ "%@-%@ { Tech=%@ Type=%@ ID=%@ silentType=%d SAK=%@ ATQA=%@ sfgi=0x%X %@ %@}"
+ "%s:%i %{public}@ Expected %{public}@, got %{public}@"
+ "%s:%i %{public}@ does not hold assertion"
+ "%s:%i 0 record type length; unable to decode"
+ "%s:%i Cannot create SecTaskRef with XPC Connection: %{public}@"
+ "%s:%i Could not create the Publisher!!!"
+ "%s:%i Disabled"
+ "%s:%i Expected length is too large."
+ "%s:%i Failed to get entitlements: %{public}@"
+ "%s:%i Failed to get power assertion - system already going to sleep"
+ "%s:%i Failed to recurse children of constructed (?) tag 0x%x, returning as simple"
+ "%s:%i Failed to register for PM notifications"
+ "%s:%i Failed to send event to XPC event stream %{public}@ for token %{public}@: %s"
+ "%s:%i Failed with 0x%x"
+ "%s:%i Have not received initial barrier; not sending %@"
+ "%s:%i Identifier string does not meet the minimum required length, %{public}@"
+ "%s:%i Identifier string exceeds the maximum length, %{public}@"
+ "%s:%i Incorrect length field"
+ "%s:%i Invalid AID entry: %{public}@"
+ "%s:%i Invalid URI; dropping message"
+ "%s:%i Invalid character found, skipping"
+ "%s:%i Invalid extended response length : %{public}@"
+ "%s:%i Invalid language code length; dropping message"
+ "%s:%i Invalid payload character; dropping message"
+ "%s:%i Invalid payload encoding; dropping message"
+ "%s:%i Invalid payload length; dropping message"
+ "%s:%i Minimum length requirement not met"
+ "%s:%i Missing or invalid entitlement %{public}@ to be of type <string>, ignoring"
+ "%s:%i More than one TLV detected"
+ "%s:%i No TLV detected"
+ "%s:%i Radio %s."
+ "%s:%i Require definite encoding, but got zero tag and len"
+ "%s:%i Restricted mode for eSE is NOT set!"
+ "%s:%i Returned %x"
+ "%s:%i System already sent a will sleep message ! Ignoring will sleep."
+ "%s:%i System never went to sleep ! Ignoring will not sleep message."
+ "%s:%i System never went to sleep ! Ignoring will power on message."
+ "%s:%i System not ready.  Abort"
+ "%s:%i Tag value overflows"
+ "%s:%i Unable to create event dictionary; dropping event"
+ "%s:%i Underflow: tag=0x%x len=%u have=%lu offset=%lu"
+ "%s:%i Unexpected %u len on tag 0"
+ "%s:%i Unexpected error from XPC event publisher for stream %{public}@: %s"
+ "%s:%i Unexpected length did you mean to use extended length ?"
+ "%s:%i Unrecognized tag: 0x%X"
+ "%s:%i Unregistering Power notifications"
+ "%s:%i Unsupported length 0x%X"
+ "%s:%i Value too large: %{public}@"
+ "%s:%i XPC Sanitizer : Unexpected class %{public}@, expecting %{public}@"
+ "%s:%i XPC Sanitizer : Unexpected key %{public}@, class %{public}@, expecting %{public}@"
+ "%s:%i XPC event publisher for stream %@ received initial barrier"
+ "%s:%i XPC event publisher for stream %@ with action = %d"
+ "%s:%i [NFTLV TLVWithTag:children:] failed!"
+ "%s:%i [Tag 0x%X] Unexpected data length: 0x%X"
+ "%s:%i [Tag 0x11] Unexpected data length: 0x%X"
+ "%s:%i [Tag 0x12] Unexpected data length: 0x%X"
+ "%s:%i all assertions: %{public}@"
+ "%s:%i com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes={public}%@"
+ "%s:%i opened assertion: counter: %lu id: %{public}@"
+ "%s:%i released assertion: counter: %lu id: %{public}@"
+ "%{public}s:%i %{public}@ Expected %{public}@, got %{public}@"
+ "%{public}s:%i %{public}@ does not hold assertion"
+ "%{public}s:%i 0 record type length; unable to decode"
+ "%{public}s:%i Cannot create SecTaskRef with XPC Connection: %{public}@"
+ "%{public}s:%i Could not create the Publisher!!!"
+ "%{public}s:%i Disabled"
+ "%{public}s:%i Expected length is too large."
+ "%{public}s:%i Failed to get entitlements: %{public}@"
+ "%{public}s:%i Failed to get power assertion - system already going to sleep"
+ "%{public}s:%i Failed to recurse children of constructed (?) tag 0x%x, returning as simple"
+ "%{public}s:%i Failed to register for PM notifications"
+ "%{public}s:%i Failed to send event to XPC event stream %{public}@ for token %{public}@: %s"
+ "%{public}s:%i Failed with 0x%x"
+ "%{public}s:%i Have not received initial barrier; not sending %@"
+ "%{public}s:%i Identifier string does not meet the minimum required length, %{public}@"
+ "%{public}s:%i Identifier string exceeds the maximum length, %{public}@"
+ "%{public}s:%i Incorrect length field"
+ "%{public}s:%i Invalid AID entry: %{public}@"
+ "%{public}s:%i Invalid URI; dropping message"
+ "%{public}s:%i Invalid character found, skipping"
+ "%{public}s:%i Invalid extended response length : %{public}@"
+ "%{public}s:%i Invalid language code length; dropping message"
+ "%{public}s:%i Invalid payload character; dropping message"
+ "%{public}s:%i Invalid payload encoding; dropping message"
+ "%{public}s:%i Invalid payload length; dropping message"
+ "%{public}s:%i Minimum length requirement not met"
+ "%{public}s:%i Missing or invalid entitlement %{public}@ to be of type <string>, ignoring"
+ "%{public}s:%i More than one TLV detected"
+ "%{public}s:%i No TLV detected"
+ "%{public}s:%i Radio %s."
+ "%{public}s:%i Require definite encoding, but got zero tag and len"
+ "%{public}s:%i Restricted mode for eSE is NOT set!"
+ "%{public}s:%i Returned %x"
+ "%{public}s:%i System already sent a will sleep message ! Ignoring will sleep."
+ "%{public}s:%i System never went to sleep ! Ignoring will not sleep message."
+ "%{public}s:%i System never went to sleep ! Ignoring will power on message."
+ "%{public}s:%i System not ready.  Abort"
+ "%{public}s:%i Tag value overflows"
+ "%{public}s:%i Unable to create event dictionary; dropping event"
+ "%{public}s:%i Underflow: tag=0x%x len=%u have=%lu offset=%lu"
+ "%{public}s:%i Unexpected %u len on tag 0"
+ "%{public}s:%i Unexpected error from XPC event publisher for stream %{public}@: %s"
+ "%{public}s:%i Unexpected length did you mean to use extended length ?"
+ "%{public}s:%i Unrecognized tag: 0x%X"
+ "%{public}s:%i Unregistering Power notifications"
+ "%{public}s:%i Unsupported length 0x%X"
+ "%{public}s:%i Value too large: %{public}@"
+ "%{public}s:%i XPC Sanitizer : Unexpected class %{public}@, expecting %{public}@"
+ "%{public}s:%i XPC Sanitizer : Unexpected key %{public}@, class %{public}@, expecting %{public}@"
+ "%{public}s:%i XPC event publisher for stream %@ received initial barrier"
+ "%{public}s:%i XPC event publisher for stream %@ with action = %d"
+ "%{public}s:%i [NFTLV TLVWithTag:children:] failed!"
+ "%{public}s:%i [Tag 0x%X] Unexpected data length: 0x%X"
+ "%{public}s:%i [Tag 0x11] Unexpected data length: 0x%X"
+ "%{public}s:%i [Tag 0x12] Unexpected data length: 0x%X"
+ "%{public}s:%i all assertions: %{public}@"
+ "%{public}s:%i com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes={public}%@"
+ "%{public}s:%i opened assertion: counter: %lu id: %{public}@"
+ "%{public}s:%i released assertion: counter: %lu id: %{public}@"
+ "+[NFCommandAPDU appendExpectedLength:usingExtendedLength:toAPDU:]"
+ "+[NFCommandAPDU buildAPDUHeaderWithClass:instruction:p1:p2:len:useExtendedLength:]"
+ "+[NFMSEIParser parseResponseAPDU:]"
+ "+[NFNSCheckedDecoder coder:decodeArrayOfArrayOfClass:forKey:]"
+ "+[NFNSCheckedDecoder coder:decodeArrayOfArrayOfClass:forKey:]_block_invoke"
+ "+[NFNSCheckedDecoder coder:decodeArrayOfClass:forKey:]"
+ "+[NFNSCheckedDecoder coder:decodeArrayOfClass:forKey:]_block_invoke"
+ "+[NFNSCheckedDecoder coder:decodeDictOfClass:forKey:]"
+ "+[NFNSCheckedDecoder coder:decodeDictOfClass:forKey:]_block_invoke"
+ "+[NFNdefRecordInternal _decodeTextRecord:]"
+ "+[NFNdefRecordInternal _decodeTextRecordLanguage:]"
+ "+[NFNdefRecordInternal _decodeTextRecordText:]"
+ "+[NFNdefRecordInternal _decodeURIRecord:]"
+ "+[NFNdefRecordInternal decodeFromRecord:]"
+ "+[NFTLV TLVWithData:]"
+ "+[NFTLV _parseTLVs:end:simple:definite:]"
+ ", %@"
+ "-[NFAccessoryTagI2CBridge(NTAG5Boost) _bridgeType0ReadMultipleSRAMPagesWithBuffer:]"
+ "-[NFAccessoryTagI2CBridge(NTAG5Boost) _readFromBridgeType0:fragmentationSupport:]"
+ "-[NFAccessoryTagI2CBridge(NTAG5Boost) _writeToBridgeType0:fragmentationSupport:]"
+ "-[NFCALogger removeRestrictedMode]"
+ "-[NFCoreNFCPollConfig initPollConfigWithOption:sessionConfig:iso7816SelectIdentifiers:felicaSystemCodes:]"
+ "-[NFPowerAssertion holdPowerAssertion:onBehalfOf:behaviourWhenSleepStarted:]"
+ "-[NFPowerAssertion releasePowerAssertion:logFaultOnOverRelease:]"
+ "-[NFPowerObserver _powerNotificationMessage:argument:]"
+ "-[NFPowerObserver allowSleep]"
+ "-[NFPowerObserver registerForEvents]"
+ "-[NFPowerObserver unregisterForEvents]"
+ "-[NFResponseAPDU decodeUnderlyingAppletError:]"
+ "-[NFServiceWhitelistChecker _copyValueOfEntitlement:secTask:]"
+ "-[NFServiceWhitelistChecker _initCardSessionEntitlementsWithSecTask:]"
+ "-[NFServiceWhitelistChecker _isAIDStringValid:]"
+ "-[NFServiceWhitelistChecker initWithConnection:coreNFCConnection:]"
+ "-[NFServiceWhitelistChecker sessionTimeLimit]"
+ "-[NFTLV valueAsUnsignedLongLong]"
+ "-[NFTLV valueAsUnsignedLong]"
+ "-[NFTLV valueAsUnsignedShort]"
+ "-[NFTagInternal _setSupportsPACE:]"
+ "-[NFXPCEventPublisher handleEventWithAction:token:descriptor:]"
+ "-[NFXPCEventPublisher initWithStreamName:queue:]"
+ "-[NFXPCEventPublisher initWithStreamName:queue:]_block_invoke_2"
+ "-[NFXPCEventPublisher sendXpcNotificationEvent:]_block_invoke"
+ "-[NFXPCEventPublisher sendXpcNotificationEventWithDictionary:]"
+ "-[NSDictionary(NFExtension) NF_objectForKey:expectedClass:]"
+ "2"
+ "@\"NFAssertionInternal\""
+ "@\"NFTimer\""
+ "@32@0:8Q16Q24"
+ "@52@0:8Q16Q24@32@40B48"
+ "A`"
+ "AccessoryRF"
+ "Critical error : this device should have NFC !!! cache = %d, MG = %d, EDT = %d"
+ "NFAssertionInternalWrapper"
+ "NFCoreNFCPollConfig"
+ "NFCoreNFCPollConfig.m"
+ "NFTagInternal.m"
+ "PACE=Y"
+ "RF"
+ "T@\"NFAssertionInternal\",&,N,V_assertion"
+ "T@\"NFTimer\",&,N,V_releaseTimer"
+ "T@\"NSArray\",&,N,V_felicaSystemCodes"
+ "T@\"NSArray\",&,N,V_iso7816SelectIdentifiers"
+ "TB,N,V_queryTypeFSystemCodes"
+ "TB,R,N,V_delayConnectionHandoverRestart"
+ "TQ,N,V_pollingOption"
+ "TQ,N,V_sessionConfig"
+ "_NFPlatformSupportsSecureTimersInOff"
+ "_NFProductHasNFCRadio"
+ "_assertion"
+ "_bucketizeOverCurrentCount:"
+ "_delayConnectionHandoverRestart"
+ "_felicaSystemCodes"
+ "_iso7816SelectIdentifiers"
+ "_pollingOption"
+ "_queryTypeFSystemCodes"
+ "_releaseTimer"
+ "_sessionConfig"
+ "_setSupportsPACE:"
+ "_supportsPACE"
+ "absent"
+ "assertion"
+ "assertionTimeString"
+ "com.apple.nfc.rf"
+ "delayConnectionHandoverRestart"
+ "false"
+ "felicaSystemCodes"
+ "isEqualToArray:"
+ "iso7816SelectIdentifiers"
+ "mode=%lu, type=%@, delayCHRestart=%d"
+ "nfcWithRadio"
+ "nil != self"
+ "overCurrentErrorCount"
+ "pollConfigWithOption:sessionConfig:"
+ "pollConfigWithOption:sessionConfig:iso7816SelectIdentifiers:felicaSystemCodes:"
+ "pollingOption"
+ "present"
+ "q24@0:8q16"
+ "queryTypeFSystemCodes"
+ "releaseTimer"
+ "se-lpem-enabled"
+ "sessionConfig"
+ "sessionConfigOverride"
+ "sessionConfigWithUIMode:sessionType:initialScanText:vasPass:delayConnectionHandoverRestart:"
+ "setAssertion:"
+ "setFelicaSystemCodes:"
+ "setIso7816SelectIdentifiers:"
+ "setPollingOption:"
+ "setQueryTypeFSystemCodes:"
+ "setReleaseTimer:"
+ "setSessionConfig:"
+ "stockholm"
+ "supportsPACE"
+ "totalCoreNFCConnectionDuration"
+ "totalCoreNFCPollingDuration"
+ "totalCoreNFCSession"
+ "totalCoreNFCSessionBurnout"
+ "totalReaderSession"
- "%02X"
- "%@-%@ { Tech=%@ Type=%@ ID=%@ silentType=%d SAK=%@ ATQA=%@ sfgi=0x%X %@}"
- "%c[%{public}s %{public}s]:%i %{public}@ Expected %{public}@, got %{public}@"
- "%c[%{public}s %{public}s]:%i %{public}@ does not hold assertion"
- "%c[%{public}s %{public}s]:%i 0 record type length; unable to decode"
- "%c[%{public}s %{public}s]:%i Cannot create SecTaskRef with XPC Connection: %{public}@"
- "%c[%{public}s %{public}s]:%i Could not create the Publisher!!!"
- "%c[%{public}s %{public}s]:%i Disabled"
- "%c[%{public}s %{public}s]:%i Expected length is too large."
- "%c[%{public}s %{public}s]:%i Failed to get entitlements: %{public}@"
- "%c[%{public}s %{public}s]:%i Failed to get power assertion - system already going to sleep"
- "%c[%{public}s %{public}s]:%i Failed to recurse children of constructed (?) tag 0x%x, returning as simple"
- "%c[%{public}s %{public}s]:%i Failed to register for PM notifications"
- "%c[%{public}s %{public}s]:%i Failed to send event to XPC event stream %{public}@ for token %{public}@: %s"
- "%c[%{public}s %{public}s]:%i Failed with 0x%x"
- "%c[%{public}s %{public}s]:%i Have not received initial barrier; not sending %@"
- "%c[%{public}s %{public}s]:%i Identifier string does not meet the minimum required length, %{public}@"
- "%c[%{public}s %{public}s]:%i Identifier string exceeds the maximum length, %{public}@"
- "%c[%{public}s %{public}s]:%i Incorrect length field"
- "%c[%{public}s %{public}s]:%i Invalid AID entry: %{public}@"
- "%c[%{public}s %{public}s]:%i Invalid URI; dropping message"
- "%c[%{public}s %{public}s]:%i Invalid character found, skipping"
- "%c[%{public}s %{public}s]:%i Invalid extended response length : %{public}@"
- "%c[%{public}s %{public}s]:%i Invalid language code length; dropping message"
- "%c[%{public}s %{public}s]:%i Invalid payload character; dropping message"
- "%c[%{public}s %{public}s]:%i Invalid payload encoding; dropping message"
- "%c[%{public}s %{public}s]:%i Invalid payload length; dropping message"
- "%c[%{public}s %{public}s]:%i Minimum length requirement not met"
- "%c[%{public}s %{public}s]:%i Missing or invalid entitlement %{public}@ to be of type <string>, ignoring"
- "%c[%{public}s %{public}s]:%i More than one TLV detected"
- "%c[%{public}s %{public}s]:%i No TLV detected"
- "%c[%{public}s %{public}s]:%i Require definite encoding, but got zero tag and len"
- "%c[%{public}s %{public}s]:%i Restricted mode for eSE is NOT set!"
- "%c[%{public}s %{public}s]:%i Returned %x"
- "%c[%{public}s %{public}s]:%i System already sent a will sleep message ! Ignoring will sleep."
- "%c[%{public}s %{public}s]:%i System never went to sleep ! Ignoring will not sleep message."
- "%c[%{public}s %{public}s]:%i System never went to sleep ! Ignoring will power on message."
- "%c[%{public}s %{public}s]:%i System not ready.  Abort"
- "%c[%{public}s %{public}s]:%i Tag value overflows"
- "%c[%{public}s %{public}s]:%i Unable to create event dictionary; dropping event"
- "%c[%{public}s %{public}s]:%i Underflow"
- "%c[%{public}s %{public}s]:%i Underflow: tag=0x%x"
- "%c[%{public}s %{public}s]:%i Underflow: tag=0x%x len=%u have=%lu offset=%lu"
- "%c[%{public}s %{public}s]:%i Unexpected %u len on tag 0"
- "%c[%{public}s %{public}s]:%i Unexpected error from XPC event publisher for stream %{public}@: %s"
- "%c[%{public}s %{public}s]:%i Unexpected length did you mean to use extended length ?"
- "%c[%{public}s %{public}s]:%i Unrecognized tag: 0x%X"
- "%c[%{public}s %{public}s]:%i Unregistering Power notifications"
- "%c[%{public}s %{public}s]:%i Unsupported length 0x%X"
- "%c[%{public}s %{public}s]:%i Value too large: %{public}@"
- "%c[%{public}s %{public}s]:%i XPC Sanitizer : Unexpected class %{public}@, expecting %{public}@"
- "%c[%{public}s %{public}s]:%i XPC Sanitizer : Unexpected key %{public}@, class %{public}@, expecting %{public}@"
- "%c[%{public}s %{public}s]:%i XPC event publisher for stream %@ received initial barrier"
- "%c[%{public}s %{public}s]:%i XPC event publisher for stream %@ with action = %d"
- "%c[%{public}s %{public}s]:%i [NFTLV TLVWithTag:children:] failed!"
- "%c[%{public}s %{public}s]:%i [Tag 0x%X] Unexpected data length: 0x%X"
- "%c[%{public}s %{public}s]:%i [Tag 0x11] Unexpected data length: 0x%X"
- "%c[%{public}s %{public}s]:%i [Tag 0x12] Unexpected data length: 0x%X"
- "%c[%{public}s %{public}s]:%i all assertions: %{public}@"
- "%c[%{public}s %{public}s]:%i com.apple.developer.nfc.hce.iso7816.select-identifier-prefixes={public}%@"
- "%c[%{public}s %{public}s]:%i opened assertion: counter: %lu id: %{public}@"
- "%c[%{public}s %{public}s]:%i released assertion: counter: %lu id: %{public}@"
- "0x%02X "
- "A!`"
- "Critical error : this device should have NFC !!! cache = %d, new = $%d"
- "NFAssertionTimeString"
- "_assertionTimeString"
- "sessionConfigWithUIMode:sessionType:initialScanText:vasPass:"
- "synchronize"

```
