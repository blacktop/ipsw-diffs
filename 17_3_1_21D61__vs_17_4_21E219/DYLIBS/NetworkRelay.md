## NetworkRelay

> `/System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay`

```diff

-454.40.3.0.0
-  __TEXT.__text: 0x3fb98
+471.100.3.0.0
+  __TEXT.__text: 0x4ed0c
   __TEXT.__auth_stubs: 0xc10
   __TEXT.__objc_methlist: 0xf54
   __TEXT.__const: 0x1c0
-  __TEXT.__gcc_except_tab: 0x148
-  __TEXT.__cstring: 0x9ec8
-  __TEXT.__oslogstring: 0x115a
-  __TEXT.__unwind_info: 0x5a0
-  __TEXT.__objc_classname: 0x259
-  __TEXT.__objc_methname: 0x321c
+  __TEXT.__gcc_except_tab: 0x154
+  __TEXT.__cstring: 0xa23b
+  __TEXT.__oslogstring: 0x1197
+  __TEXT.__unwind_info: 0x610
+  __TEXT.__objc_classname: 0x257
+  __TEXT.__objc_methname: 0x327e
   __TEXT.__objc_methtype: 0x679
-  __TEXT.__objc_stubs: 0x1c20
+  __TEXT.__objc_stubs: 0x1cc0
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x9e0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2b48
-  __DATA_CONST.__objc_selrefs: 0x960
+  __DATA_CONST.__objc_const: 0x2b88
+  __DATA_CONST.__objc_selrefs: 0x988
+  __DATA_CONST.__objc_classrefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__cfstring: 0x35e0
+  __AUTH_CONST.__cfstring: 0x3620
   __AUTH_CONST.__objc_const: 0x948
-  __AUTH_CONST.__const: 0x190
+  __AUTH_CONST.__const: 0x390
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__auth_got: 0x618
   __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_classrefs: 0xe8
-  __DATA.__objc_superrefs: 0xb8
-  __DATA.__objc_ivar: 0x370
+  __DATA.__objc_ivar: 0x378
   __DATA.__data: 0x208
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x1
-  __DATA.__bss: 0xa0
+  __DATA.__bss: 0x1b0
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__common: 0x1
-  __DATA_DIRTY.__bss: 0x58
+  __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A35C82C9-99E1-34C4-876F-FD3109388CDC
-  Functions: 546
-  Symbols:   2046
-  CStrings:  2432
+  UUID: 91F70DB5-A2B8-309D-872B-D1845C0094C6
+  Functions: 590
+  Symbols:   2185
+  CStrings:  2453
 
Symbols:
+ -[NRBluetoothPacketParser handleIncomingIKEData:linkPriority:]
+ -[NRBluetoothPacketParser teardown]
+ -[NRDevicePreferences removeQuickRelayRequestLocked:]
+ -[NRDevicePreferencesQuickRelay setAssertCount:]
+ GCC_except_table102
+ GCC_except_table104
+ GCC_except_table225
+ GCC_except_table278
+ GCC_except_table42
+ GCC_except_table53
+ GCC_except_table90
+ _NRTLVAdd
+ _NRTLVAddData
+ _NRTLVParse
+ _OBJC_CLASS_$_NSCountedSet
+ _OBJC_IVAR_$_NRBluetoothPacketParser._nrUUID
+ _OBJC_IVAR_$_NRXPCComm._nrUUID
+ __NRAddEligibleNRUUIDForLogObject
+ __NRCopyEventLogObjectForNRUUID
+ __NRCopyLogObjectForNRUUID
+ __NRRemoveEligibleNRUUIDForLogObject
+ __NRUpdateNRUUIDsEligibleForLogObjects
+ ___Block_byref_object_copy_.1558
+ ___Block_byref_object_dispose_.1559
+ ___block_literal_global.1035
+ ___block_literal_global.1066
+ ___block_literal_global.1087
+ ___block_literal_global.139
+ ___block_literal_global.1539
+ ___block_literal_global.1666
+ ___block_literal_global.239
+ ___block_literal_global.327
+ ___block_literal_global.338
+ ___block_literal_global.339
+ ___block_literal_global.356
+ ___block_literal_global.37
+ ___block_literal_global.400
+ ___block_literal_global.41
+ ___block_literal_global.422
+ ___block_literal_global.499
+ ___block_literal_global.545
+ ___block_literal_global.55
+ ___block_literal_global.55.295
+ ___block_literal_global.611
+ ___block_literal_global.64
+ ___block_literal_global.697
+ ___block_literal_global.70
+ ___block_literal_global.886
+ ___nrCopyLogObj_block_invoke.1075
+ ___nrCopyLogObj_block_invoke.1098
+ ___nrCopyLogObj_block_invoke.147
+ ___nrCopyLogObj_block_invoke.1550
+ ___nrCopyLogObj_block_invoke.1670
+ ___nrCopyLogObj_block_invoke.243
+ ___nrCopyLogObj_block_invoke.299
+ ___nrCopyLogObj_block_invoke.35
+ ___nrCopyLogObj_block_invoke.360
+ ___nrCopyLogObj_block_invoke.427
+ ___nrCopyLogObj_block_invoke.549
+ ___nrCopyLogObj_block_invoke.618
+ ___nrCopyLogObj_block_invoke.691
+ ___nrCopyLogObj_block_invoke.890
+ ___nrCopyLogObj_block_invoke.97
+ ___nrCopyLogObj_block_invoke.995
+ __os_log_impl
+ __unnamed_array_storage.230
+ __unnamed_array_storage.235
+ __unnamed_array_storage.238
+ __unnamed_array_storage.241
+ __unnamed_array_storage.244
+ _checkAndCapValue
+ _isNextHeaderValidESP
+ _nrCopyLogObj.1078
+ _nrCopyLogObj.1232
+ _nrCopyLogObj.148
+ _nrCopyLogObj.1541
+ _nrCopyLogObj.1661
+ _nrCopyLogObj.231
+ _nrCopyLogObj.27
+ _nrCopyLogObj.305
+ _nrCopyLogObj.350
+ _nrCopyLogObj.420
+ _nrCopyLogObj.530
+ _nrCopyLogObj.631
+ _nrCopyLogObj.66
+ _nrCopyLogObj.684
+ _nrCopyLogObj.880
+ _nrCopyLogObj.986
+ _nrCopyLogObj.onceToken.1065
+ _nrCopyLogObj.onceToken.1086
+ _nrCopyLogObj.onceToken.138
+ _nrCopyLogObj.onceToken.1547
+ _nrCopyLogObj.onceToken.1665
+ _nrCopyLogObj.onceToken.238
+ _nrCopyLogObj.onceToken.294
+ _nrCopyLogObj.onceToken.32
+ _nrCopyLogObj.onceToken.355
+ _nrCopyLogObj.onceToken.424
+ _nrCopyLogObj.onceToken.544
+ _nrCopyLogObj.onceToken.610
+ _nrCopyLogObj.onceToken.63
+ _nrCopyLogObj.onceToken.688
+ _nrCopyLogObj.onceToken.885
+ _nrCopyLogObj.onceToken.990
+ _nrCopyLogObj.sNRLogObj.1067
+ _nrCopyLogObj.sNRLogObj.1088
+ _nrCopyLogObj.sNRLogObj.140
+ _nrCopyLogObj.sNRLogObj.1548
+ _nrCopyLogObj.sNRLogObj.1667
+ _nrCopyLogObj.sNRLogObj.240
+ _nrCopyLogObj.sNRLogObj.296
+ _nrCopyLogObj.sNRLogObj.33
+ _nrCopyLogObj.sNRLogObj.357
+ _nrCopyLogObj.sNRLogObj.425
+ _nrCopyLogObj.sNRLogObj.546
+ _nrCopyLogObj.sNRLogObj.612
+ _nrCopyLogObj.sNRLogObj.65
+ _nrCopyLogObj.sNRLogObj.689
+ _nrCopyLogObj.sNRLogObj.887
+ _nrCopyLogObj.sNRLogObj.991
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$allKeys
+ _objc_msgSend$appendBytes:length:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeObject:
+ _sNRUUIDToEventLogObject
+ _sNRUUIDToLogObject
+ _sNRUUIDsEligibleForLogObject
- -[NRBluetoothPacketParser handleIncomingIKEData:]
- -[NRBluetoothPacketParser invalidateParser]
- GCC_except_table201
- GCC_except_table250
- GCC_except_table38
- GCC_except_table47
- GCC_except_table82
- GCC_except_table84
- GCC_except_table95
- ___Block_byref_object_copy_.1445
- ___Block_byref_object_dispose_.1446
- ___block_literal_global.1433
- ___block_literal_global.280
- ___block_literal_global.29
- ___block_literal_global.33
- ___block_literal_global.337
- ___block_literal_global.433
- ___block_literal_global.629
- ___block_literal_global.938
- __unnamed_array_storage.229
- __unnamed_array_storage.234
- __unnamed_array_storage.237
- __unnamed_array_storage.240
- __unnamed_array_storage.243
- _objc_retainAutorelease
CStrings:
+ "#\x14\xf0\xcd!\xf0\xd1"
+ "%@"
+ "%@.events"
+ "%s called with null block"
+ "%s called with null tlvData"
+ "%s%.30s:%-4d "
+ "%s%.30s:%-4d %@ adding prefer Wi-Fi request (count is now %llu)"
+ "%s%.30s:%-4d %@ cancelling connection %@"
+ "%s%.30s:%-4d %@ cancelling connection because not needed %@"
+ "%s%.30s:%-4d %@ failed to send device preferences: %@, error %@"
+ "%s%.30s:%-4d %@ interrupted, resubmitting device preferences"
+ "%s%.30s:%-4d %@ link Write context staging buffer allocated: %u bytes"
+ "%s%.30s:%-4d %@ not removing prefer Wi-Fi request because count is 0"
+ "%s%.30s:%-4d %@ policy traffic classifiers already set to %@"
+ "%s%.30s:%-4d %@ received XPC error invalid"
+ "%s%.30s:%-4d %@ received unexpected XPC message %@"
+ "%s%.30s:%-4d %@ received unknown XPC error: %@"
+ "%s%.30s:%-4d %@ removing all quick relay requests (count is now %llu)"
+ "%s%.30s:%-4d %@ removing prefer Wi-Fi request (count is now %llu)"
+ "%s%.30s:%-4d %@ removing quick relay request (count is now %llu)"
+ "%s%.30s:%-4d %@ restarting connection %@"
+ "%s%.30s:%-4d %@ sending device preferences: %@"
+ "%s%.30s:%-4d %@ sent device preferences: %@"
+ "%s%.30s:%-4d %@ setting Bluetooth link preferences from %@ to %@"
+ "%s%.30s:%-4d %@ setting link preferences from %@ to %@"
+ "%s%.30s:%-4d %@ setting policy traffic classifiers from %@ to %@"
+ "%s%.30s:%-4d %lld > UINT32_MAX, capping"
+ "%s%.30s:%-4d %s received XPC_ERROR_CONNECTION_INTERRUPTED, retrying (%u)"
+ "%s%.30s:%-4d %s: No data to write"
+ "%s%.30s:%-4d %s: canWriteMore: %d bufferHandled=%u/%u"
+ "%s%.30s:%-4d %s: done with NtL fast-path"
+ "%s%.30s:%-4d %s: ignoring NtL fast-path for %u, as waiting for link output available"
+ "%s%.30s:%-4d %s: invoking send callback w/ written %u"
+ "%s%.30s:%-4d %s: memmoving filledIn=%u, bufferHandled=%u"
+ "%s%.30s:%-4d %s: not enough room %u to fit maxTLVLen %u"
+ "%s%.30s:%-4d %s: not memmoving filledIn=%u, bufferHandled=%u"
+ "%s%.30s:%-4d %s: nothing to read from nexus"
+ "%s%.30s:%-4d %s: out of NtL inner loop"
+ "%s%.30s:%-4d %s: out of NtL outer loop"
+ "%s%.30s:%-4d %s: performing RX sync (%u packets, %u bytes, %u pending, %0.2f msec, canWriteMore %d, memmove %u)"
+ "%s%.30s:%-4d %s: starting NtL inner loop"
+ "%s%.30s:%-4d %s: starting NtL outer loop"
+ "%s%.30s:%-4d %s: wrote %u (%u/%u) bytes from linkWriteBuffer"
+ "%s%.30s:%-4d %s: wrote %u bytes from nexus for ESP seq: %u (spi: %u)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (dstAddr) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (ioVecs) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (nrXPCQueue) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (outBuffer) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (packetBuffer) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (propertiesCopy.outOfBandKey) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (retNum) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (self.queue) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (srcAddr) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (xpcDict) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: (xpcKey) != ((void*)0)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: bytesWritten == length"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: bytesWritten == length; bytesWritten (%u) != length (%u), offset: %u, ioVec: %@"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: computedBytes == writtenLength"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: dataLen <= 65535"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: dataLen > 0"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: ioVecs[0].len == 1; %@"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: ioVecs[1].len == 1; %@"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: iovecIndex + 1 < numIOVecs; %@, iovecIndex=%u bytesToCheckThisIOVec=%u"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: iovecs[iovecIndex + 1].len >= 1; %@, iovecIndex=%u bytesToCheckThisIOVec=%u"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: iovecs[iovecIndex].len >= bytesToCheckThisIOVec + 1; %@, iovecIndex=%u bytesToCheckThisIOVec=%u"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: numIOVecs > 0"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: numIOVecs > 1"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: numIOVecs > 1; %@"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: numIOVecs > 2; %@"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: packetLength > 0"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: packetLength >= sizeof(NRIPv6Hdr_s)"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: propertiesCopy.outOfBandKey.length == 34"
+ "%s%.30s:%-4d ABORTING: Assertion Failed: tlvLen > 0"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with Device pairing bluetoothMACAddress length %lu != 6"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with Device pairing properties has pairWithSPPLink but no bluetoothMACAddress"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with Device pairing properties must either have wasInitiallySetupUsingIDSPairing or outOfBandKey"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with Device pairing protocol version %llu is too large"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL bluetoothUUID"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL completionBlock"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL dataProtectionClass == NRDataProtectionClassC || dataProtectionClass == NRDataProtectionClassD"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL delegate"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL deviceID"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL deviceIdentifier"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL directoryPath"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL directoryPath.length"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL directoryPathC"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL filePath"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL filePath.length"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL filePathC"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL idsDeviceID"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL nrDeviceIdentifier"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL nrUUID"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL operationalproperties"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL portString"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL properties"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL queue"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with all-zero bluetoothUUID"
+ "%s%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with all-zero nrDeviceIdentifier"
+ "%s%.30s:%-4d ABORTING: [super initWithCoder:] failed"
+ "%s%.30s:%-4d ABORTING: [super init] failed"
+ "%s%.30s:%-4d ABORTING: _strict_reallocf called with size 0"
+ "%s%.30s:%-4d ABORTING: _strict_reallocf(%zu) failed"
+ "%s%.30s:%-4d ABORTING: dispatch_queue_create(%s) failed"
+ "%s%.30s:%-4d ABORTING: strict_calloc(%zu, %zu) failed"
+ "%s%.30s:%-4d ABORTING: strict_malloc called with size 0"
+ "%s%.30s:%-4d ABORTING: strict_malloc(%zu) failed"
+ "%s%.30s:%-4d ABORTING: xpc_array_create(%p, %u) failed"
+ "%s%.30s:%-4d ABORTING: xpc_dictionary_create(%p, %p, %u) failed"
+ "%s%.30s:%-4d ABORTING: xpc_string_create(%s) failed"
+ "%s%.30s:%-4d Advancing linkReadBuffer handled by %u handled=%u filledIn=%u"
+ "%s%.30s:%-4d All clients of prefer Wi-Fi went away"
+ "%s%.30s:%-4d All clients of quick relay went away"
+ "%s%.30s:%-4d All-zero nrUUID in response from daemon"
+ "%s%.30s:%-4d Avoiding compression of strange length payload %u expected %u"
+ "%s%.30s:%-4d Cancel"
+ "%s%.30s:%-4d Cancel: %@ %@"
+ "%s%.30s:%-4d Changing state: %@ -> %@"
+ "%s%.30s:%-4d Checkin could not deliver message %@, error %@, retrying"
+ "%s%.30s:%-4d Checkin received XPC dict: %@"
+ "%s%.30s:%-4d Checkin received unexpected XPC object: %@"
+ "%s%.30s:%-4d Clearing NREndpoint cache"
+ "%s%.30s:%-4d Created (%p)"
+ "%s%.30s:%-4d Created read context (%p) for %@ (total: %llu)"
+ "%s%.30s:%-4d Created temporary directory at \"%@\""
+ "%s%.30s:%-4d Created write context (%p) for %@"
+ "%s%.30s:%-4d Creating %@ for ephemeral pairing"
+ "%s%.30s:%-4d Creating temporary directory at \"%@\""
+ "%s%.30s:%-4d Dealloc"
+ "%s%.30s:%-4d Dealloc %@ for %@"
+ "%s%.30s:%-4d Dealloc: %@"
+ "%s%.30s:%-4d Decompressed 6LoWPAN data from %u to %u, %@ to %@"
+ "%s%.30s:%-4d Device supports restricted ports: %s"
+ "%s%.30s:%-4d Disabled device %@"
+ "%s%.30s:%-4d Disabling device %@"
+ "%s%.30s:%-4d Enabled device %@"
+ "%s%.30s:%-4d Enabling device %@"
+ "%s%.30s:%-4d Ended linkInputSlot on a Pad0 handled=%u filledIn=%u"
+ "%s%.30s:%-4d Ended linkReadBuffer on a Pad0 handled=%u filledIn=%u"
+ "%s%.30s:%-4d Failed to archive operational properties %@"
+ "%s%.30s:%-4d Failed to create directory at \"%@\": %@"
+ "%s%.30s:%-4d Failed to disable device %@: %@"
+ "%s%.30s:%-4d Failed to enable device %@: %@"
+ "%s%.30s:%-4d Failed to get agent UUID"
+ "%s%.30s:%-4d Failed to register device %@ with properties %@: %@"
+ "%s%.30s:%-4d Failed to resolve endpoint for %@ %@"
+ "%s%.30s:%-4d Failed to save diagnostic status to directory \"%s\""
+ "%s%.30s:%-4d Failed to start %@ for %@"
+ "%s%.30s:%-4d Failed to unregister all devices: %@"
+ "%s%.30s:%-4d Failed to unregister device %@: %@"
+ "%s%.30s:%-4d Found %@ for bluetoothUUID %@"
+ "%s%.30s:%-4d Found %@ for idsDeviceID %@"
+ "%s%.30s:%-4d Got NRUUID %@ from cache for bluetoothUUID %@"
+ "%s%.30s:%-4d Got NRUUID %@ from cache for idsDeviceID %@"
+ "%s%.30s:%-4d Got NRUUID %@ from daemon for bluetoothUUID %@"
+ "%s%.30s:%-4d Got NRUUID %@ from daemon for idsDeviceID %@"
+ "%s%.30s:%-4d Got [%@] total len %u"
+ "%s%.30s:%-4d Handling Pad0 in linkInputSlot alreadyRead=%u"
+ "%s%.30s:%-4d Handling Pad0 in linkReadBuffer"
+ "%s%.30s:%-4d Handling PadN %u"
+ "%s%.30s:%-4d Ignoring path evaluator update for a stale evaluator: old: %@, new: %@"
+ "%s%.30s:%-4d Ignoring setting prefer Wi-Fi to %d"
+ "%s%.30s:%-4d Incomplete tlv buffer (%u < %zu)"
+ "%s%.30s:%-4d Informing client that %@ %shasUnpairedBluetooth"
+ "%s%.30s:%-4d Informing client that %@ has link type %@"
+ "%s%.30s:%-4d Informing client that %@ has link type %@ subtype %@"
+ "%s%.30s:%-4d Informing client that %@ has proxy svc interface name %@"
+ "%s%.30s:%-4d Informing client that %@ has thermal pressure level %@"
+ "%s%.30s:%-4d Informing client that %@ is %s"
+ "%s%.30s:%-4d Informing client that %@ is %sabled"
+ "%s%.30s:%-4d Informing client that %@ is %sclassCConnected"
+ "%s%.30s:%-4d Informing client that %@ is %scloudConnected"
+ "%s%.30s:%-4d Informing client that %@ is %sconnected"
+ "%s%.30s:%-4d Informing client that %@ is %snearby"
+ "%s%.30s:%-4d Informing client that %@ is %sregistered"
+ "%s%.30s:%-4d Init for %@"
+ "%s%.30s:%-4d Init: %@"
+ "%s%.30s:%-4d Invalid checksum detected in Isoch loop len %u filledIn=%u handled=%u ioVecContentLen=%u alreadyRead=%zu "
+ "%s%.30s:%-4d Invalid link-read context ptr for prio %@"
+ "%s%.30s:%-4d Invalid link-write context ptr for prio %@"
+ "%s%.30s:%-4d Invalid read context %sptr for prio %@"
+ "%s%.30s:%-4d Invalid tlv buffer (%u < %zu + %u)"
+ "%s%.30s:%-4d Invalid write context %sptr for prio %@"
+ "%s%.30s:%-4d Link Read context: %p"
+ "%s%.30s:%-4d Link input available - %@"
+ "%s%.30s:%-4d Link output available - %@"
+ "%s%.30s:%-4d Looking into incoming TLV %@ len=%u%s"
+ "%s%.30s:%-4d Looking into incoming TLV o1 %@ len=%u handled=%u filledIn=%u"
+ "%s%.30s:%-4d Looking into incoming TLV o2 %@ len=%u handled=%u filledIn=%u slotLen=%u alreadyRead=%u"
+ "%s%.30s:%-4d Looking into incoming TLV o3 %@"
+ "%s%.30s:%-4d Looking into incoming TLV o4 %@ len=%u handled=%u filledIn=%u slotLen=%u"
+ "%s%.30s:%-4d Looking into incoming TLV o5 %@"
+ "%s%.30s:%-4d LtN not enough input bytes from linkInputSlot %u to fit %@ tlvLen %u"
+ "%s%.30s:%-4d M=0 DAC=1 DAM=00 is reserved"
+ "%s%.30s:%-4d M=1 DAC=1 DAM!=00 is reserved"
+ "%s%.30s:%-4d Marking as completed"
+ "%s%.30s:%-4d Marking as completed (no nexusOutputSlot) alreadyRead=%u"
+ "%s%.30s:%-4d Marking as completed (not enough input bytes) alreadyRead=%u"
+ "%s%.30s:%-4d Missing address"
+ "%s%.30s:%-4d Missing nrUUID in response from daemon"
+ "%s%.30s:%-4d NREndpoint cache generation changed: %llu -> %llu"
+ "%s%.30s:%-4d Nexus input available - %@"
+ "%s%.30s:%-4d Nexus output available - %@"
+ "%s%.30s:%-4d No delegate found"
+ "%s%.30s:%-4d No netagents to retrieve agent UUID"
+ "%s%.30s:%-4d No path to retrieve agent UUID"
+ "%s%.30s:%-4d No path to retrieve agent data"
+ "%s%.30s:%-4d No path to update agent UUID"
+ "%s%.30s:%-4d Not marking as completed (all in linkReadBuffer)"
+ "%s%.30s:%-4d Packet too short for determining address family"
+ "%s%.30s:%-4d Packet too short for determining next header"
+ "%s%.30s:%-4d Placing in ioVec[%u] buf=%p len=%u alreadyRead=%u += %u"
+ "%s%.30s:%-4d Placing linkReadBuffer handled=%u filledIn=%u in ioVec[%u] buf=%p len=%u"
+ "%s%.30s:%-4d Querying NRUUID for IDSDeviceID %@"
+ "%s%.30s:%-4d Querying NRUUID for bluetoothUUID %@"
+ "%s%.30s:%-4d Querying whether companion link is enabled"
+ "%s%.30s:%-4d Querying whether device supports restricted ports"
+ "%s%.30s:%-4d Read context: %p"
+ "%s%.30s:%-4d Reading from buf=%p len=%u alreadyRead=%u handled=%u filledIn=%u"
+ "%s%.30s:%-4d Reading link input, setting filledIn=%u (linkChannelPriority=%u)"
+ "%s%.30s:%-4d Ready to handle %@ len %u in %@ ioVecContentLen=%u alreadyRead=%u"
+ "%s%.30s:%-4d Reasserting the agent"
+ "%s%.30s:%-4d Received %supdate %sregistered %sabled %snearby %sconnected %scloudConnected %sclassCConnected %shasUnpairedBluetooth %s %@(%@) prx %@ thermal %@ for %@"
+ "%s%.30s:%-4d Received XPC dict: %@"
+ "%s%.30s:%-4d Received XPC error: %@, retrying"
+ "%s%.30s:%-4d Received empty out of band key, using generic key for device %@ with properties %@"
+ "%s%.30s:%-4d Received invalid TLV len %u for %@ (max=%u) %@"
+ "%s%.30s:%-4d Received notification: %@"
+ "%s%.30s:%-4d Received path: %@"
+ "%s%.30s:%-4d Received unexpected XPC object: %@"
+ "%s%.30s:%-4d Refresh generation response %lld (%@)"
+ "%s%.30s:%-4d Registered device %@ with properties %@"
+ "%s%.30s:%-4d Registering device %@ with properties %@"
+ "%s%.30s:%-4d Reinjecting %@ packet len %u to nexusOutputSlot=%p buf=%p len=%u: %@, buflet: %d"
+ "%s%.30s:%-4d Resetting context for priority: %@ (%d)"
+ "%s%.30s:%-4d Resetting state"
+ "%s%.30s:%-4d Resolved properties: %@"
+ "%s%.30s:%-4d Response of invalid length %zu"
+ "%s%.30s:%-4d Response of invalid type"
+ "%s%.30s:%-4d Returning that companion link is %sabled"
+ "%s%.30s:%-4d Saved diagnostic status to directory \"%s\""
+ "%s%.30s:%-4d Saved diagnostic status to file \"%s\""
+ "%s%.30s:%-4d Saving diagnostic status to directory \"%s\""
+ "%s%.30s:%-4d Saving diagnostic status to file \"%s\""
+ "%s%.30s:%-4d Saving diagnostic status to temp directory"
+ "%s%.30s:%-4d Setting prefer Wi-Fi assert count: %ld -> %ld"
+ "%s%.30s:%-4d Setting quick relay assert count: %ld -> %ld"
+ "%s%.30s:%-4d Setup nexus channels: %@"
+ "%s%.30s:%-4d Shrinking ioVecs[%u] down by %u - %@ ioVecContentLen=%u alreadyRead=%u"
+ "%s%.30s:%-4d Shrunk ioVecs[%u] down by %u - %@ ioVecContentLen=%u alreadyRead=%u"
+ "%s%.30s:%-4d Started %@ for %@"
+ "%s%.30s:%-4d Teardown"
+ "%s%.30s:%-4d Tried to sync nexus output but _nexusOutputRing is NULL"
+ "%s%.30s:%-4d Unregistered all devices"
+ "%s%.30s:%-4d Unregistered device %@"
+ "%s%.30s:%-4d Unregistering all devices"
+ "%s%.30s:%-4d Unregistering device %@"
+ "%s%.30s:%-4d Used 6LowPAN IPHC to compress %@, %u to %u - %@ %@ %@"
+ "%s%.30s:%-4d Using new nexusOutputSlot=%p"
+ "%s%.30s:%-4d Write context: %p"
+ "%s%.30s:%-4d adding quick relay request (count is now %ld)"
+ "%s%.30s:%-4d can't handle M=1 DAC=1 DAM=00 yet"
+ "%s%.30s:%-4d can't handle NH=1 yet"
+ "%s%.30s:%-4d checksum failed disjoint IOVec received 0x%02x%02x != computed 0x%02x%02x"
+ "%s%.30s:%-4d checksum failed same IOVec received 0x%02x%02x != computed 0x%02x%02x"
+ "%s%.30s:%-4d end of LtN inner loop alreadyRead=%u splen=%u"
+ "%s%.30s:%-4d failed to reinject %@ tlvLen=%u slotLen=%u"
+ "%s%.30s:%-4d failed to send %@ due to error %@"
+ "%s%.30s:%-4d handling uIKE packet of %llu bytes"
+ "%s%.30s:%-4d hasUnpairedBluetooth: %d -> %d"
+ "%s%.30s:%-4d highestNexusOutputSlotWrittenTo is NULL"
+ "%s%.30s:%-4d internal error: %@"
+ "%s%.30s:%-4d invalid link channel priority"
+ "%s%.30s:%-4d isAsleep: %d -> %d"
+ "%s%.30s:%-4d isClassCConnected: %d -> %d"
+ "%s%.30s:%-4d isCloudConnected: %d -> %d"
+ "%s%.30s:%-4d isConnected: %d -> %d"
+ "%s%.30s:%-4d isEnabled: %d -> %d"
+ "%s%.30s:%-4d isNearby: %d -> %d"
+ "%s%.30s:%-4d isRegistered: %d -> %d"
+ "%s%.30s:%-4d link Write context: %p"
+ "%s%.30s:%-4d link subtype: %@ -> %@"
+ "%s%.30s:%-4d link type: %@ -> %@"
+ "%s%.30s:%-4d memmoving the linkReadBuffer by handled=%u (filledIn=%u) thresh=%u"
+ "%s%.30s:%-4d merged properties: %@"
+ "%s%.30s:%-4d no 6lo compression - IPv4 - %@"
+ "%s%.30s:%-4d no 6lo compression - not IPv6 - v=%u"
+ "%s%.30s:%-4d no 6lo compression - too short %u"
+ "%s%.30s:%-4d no curNexusOutputSlot, dropping %@ tlvLen=%u slotLen=%u"
+ "%s%.30s:%-4d no nexusOutputSlot - consolidating %u bytes from linkInputSlot ioVecs[%u].buf=%p to linkReadBuffer filledIn=%u handled=%u"
+ "%s%.30s:%-4d no nexusOutputSlot - tail consolidating %zu bytes from linkInputSlot to linkReadBuffer filledIn=%u handled=%u and marking as completed"
+ "%s%.30s:%-4d no nexusOutputSlot and everything in linkReadBuffer alreadyRead=%zu"
+ "%s%.30s:%-4d no nexusOutputSlot and linkReadBuffer is full %@ filledIn=%u handled=%u"
+ "%s%.30s:%-4d no nexusOutputSlot highestSlot=%p %@ filledIn=%u handled=%u"
+ "%s%.30s:%-4d not activating as cancelled"
+ "%s%.30s:%-4d not memmoving the linkReadBuffer thresh handled=%u filledIn=%u thresh=%u"
+ "%s%.30s:%-4d not memmoving the linkReadBuffer zero handled=%u filledIn=%u thresh=%u"
+ "%s%.30s:%-4d not ready to accept data"
+ "%s%.30s:%-4d not sending message as cancelled"
+ "%s%.30s:%-4d not shrinking len %u%s ioVecContentLen=%u alreadyRead=%u"
+ "%s%.30s:%-4d out of LtN fast path inner loop"
+ "%s%.30s:%-4d out of LtN fast path loop (%llu/%llu bytes)"
+ "%s%.30s:%-4d packet too big %@ tlvLen=%u payloadLength=%u packetLength=%u"
+ "%s%.30s:%-4d partial TLV - consolidating %u bytes from linkInputSlot buf %p to linkReadBuffer filledIn=%u handled=%u"
+ "%s%.30s:%-4d proxy-svc intf name: %@ -> %@"
+ "%s%.30s:%-4d read all of len=%u alreadyRead=%u nexusOutputAvailable=%d"
+ "%s%.30s:%-4d received 6LoWPAN TLV too short %u"
+ "%s%.30s:%-4d received XPC error invalid"
+ "%s%.30s:%-4d received XPC_ERROR_CONNECTION_INVALID"
+ "%s%.30s:%-4d received internal failure result code: [%lld] %@"
+ "%s%.30s:%-4d received more data than moveOffset (%u > %u), off %d"
+ "%s%.30s:%-4d received unexpected XPC message %@"
+ "%s%.30s:%-4d received unknown 6LoWPAN dispatch %u"
+ "%s%.30s:%-4d received unknown XPC error: %@"
+ "%s%.30s:%-4d resetting the linkReadBuffer (filledIn=%u)"
+ "%s%.30s:%-4d reusing existing len=%u alreadyRead=%u"
+ "%s%.30s:%-4d sending datapath report: %@"
+ "%s%.30s:%-4d sending packets over medium pipe"
+ "%s%.30s:%-4d sent %@"
+ "%s%.30s:%-4d source-%s: High"
+ "%s%.30s:%-4d source-%s: Isochronous"
+ "%s%.30s:%-4d source-%s: Medium"
+ "%s%.30s:%-4d source-resume: NexusBEInput"
+ "%s%.30s:%-4d source-resume: NexusBEOutput"
+ "%s%.30s:%-4d source-resume: NexusBKInput"
+ "%s%.30s:%-4d source-resume: NexusBKOutput"
+ "%s%.30s:%-4d source-resume: NexusVIInput"
+ "%s%.30s:%-4d source-resume: NexusVIOutput"
+ "%s%.30s:%-4d source-resume: NexusVOInput"
+ "%s%.30s:%-4d source-resume: NexusVOOutput"
+ "%s%.30s:%-4d source-suspend: NexusBEInput"
+ "%s%.30s:%-4d source-suspend: NexusBEOutput"
+ "%s%.30s:%-4d source-suspend: NexusBKInput"
+ "%s%.30s:%-4d source-suspend: NexusVIInput"
+ "%s%.30s:%-4d source-suspend: NexusVIOutput"
+ "%s%.30s:%-4d source-suspend: NexusVOInput"
+ "%s%.30s:%-4d source-suspend: NexusVOOutput"
+ "%s%.30s:%-4d start LtN fast path inner loop"
+ "%s%.30s:%-4d start LtN fast path outer loop"
+ "%s%.30s:%-4d starting NtL fast-path for %u"
+ "%s%.30s:%-4d syncing nexus output (%u packets)"
+ "%s%.30s:%-4d thermal pressure level: %@ -> %@"
+ "%s%.30s:%-4d truncated packet received %u != %u"
+ "%s%.30s:%-4d xpc connection interrupted"
+ "-[NRBluetoothPacketParser handleIncomingIKEData:linkPriority:]"
+ "NRTLVAdd"
+ "NRTLVParse"
+ "T@\"NSString\",?,R,C"
+ "addObjectsFromArray:"
+ "adding event log object for %@"
+ "adding log object for %@"
+ "allKeys"
+ "appendBytes:length:"
+ "invalid tlv length and value"
+ "removeAllObjects"
+ "removeObject:"
+ "removing event log object for %@"
+ "removing log object for %@"
+ "tlv buffer full"
+ "tlv buffer larger than expected"
- "\x14"
- "\"\x14\xf0\xcd!\xf0\xd1"
- "%.30s:%-4d "
- "%.30s:%-4d %@ Cancel"
- "%.30s:%-4d %@ Changing state: %@ -> %@"
- "%.30s:%-4d %@ Created (%p)"
- "%.30s:%-4d %@ Created read context (%p) for %@ (total: %llu)"
- "%.30s:%-4d %@ Created write context (%p) for %@"
- "%.30s:%-4d %@ Dealloc"
- "%.30s:%-4d %@ Init"
- "%.30s:%-4d %@ Invalid link-read context ptr for prio %@"
- "%.30s:%-4d %@ Invalid link-write context ptr for prio %@"
- "%.30s:%-4d %@ Invalid read context %sptr for prio %@"
- "%.30s:%-4d %@ Invalid write context %sptr for prio %@"
- "%.30s:%-4d %@ Received XPC dict: %@"
- "%.30s:%-4d %@ Received notification: %@"
- "%.30s:%-4d %@ Resetting context for priority: %@ (%d)"
- "%.30s:%-4d %@ Setup nexus channels: %@"
- "%.30s:%-4d %@ Teardown"
- "%.30s:%-4d %@ adding prefer Wi-Fi request (count is now %llu)"
- "%.30s:%-4d %@ cancelling connection %@"
- "%.30s:%-4d %@ cancelling connection because not needed %@"
- "%.30s:%-4d %@ failed to send %@ due to error %@"
- "%.30s:%-4d %@ failed to send device preferences: %@, error %@"
- "%.30s:%-4d %@ internal error: %@"
- "%.30s:%-4d %@ interrupted, resubmitting device preferences"
- "%.30s:%-4d %@ link Write context staging buffer allocated: %u bytes"
- "%.30s:%-4d %@ not activating as cancelled"
- "%.30s:%-4d %@ not removing prefer Wi-Fi request because count is 0"
- "%.30s:%-4d %@ not sending message as cancelled"
- "%.30s:%-4d %@ policy traffic classifiers already set to %@"
- "%.30s:%-4d %@ received XPC error invalid"
- "%.30s:%-4d %@ received unexpected XPC message %@"
- "%.30s:%-4d %@ received unknown XPC error: %@"
- "%.30s:%-4d %@ removing all quick relay requests (count is now %llu)"
- "%.30s:%-4d %@ removing prefer Wi-Fi request (count is now %llu)"
- "%.30s:%-4d %@ removing quick relay request (count is now %llu)"
- "%.30s:%-4d %@ restarting connection %@"
- "%.30s:%-4d %@ sending datapath report: %@"
- "%.30s:%-4d %@ sending device preferences: %@"
- "%.30s:%-4d %@ sent %@"
- "%.30s:%-4d %@ sent device preferences: %@"
- "%.30s:%-4d %@ setting Bluetooth link preferences from %@ to %@"
- "%.30s:%-4d %@ setting link preferences from %@ to %@"
- "%.30s:%-4d %@ setting policy traffic classifiers from %@ to %@"
- "%.30s:%-4d %@ xpc connection interrupted"
- "%.30s:%-4d %lld > UINT32_MAX, capping"
- "%.30s:%-4d %s received XPC_ERROR_CONNECTION_INTERRUPTED, retrying (%u)"
- "%.30s:%-4d %s: No data to write"
- "%.30s:%-4d %s: canWriteMore: %d bufferHandled=%u/%u"
- "%.30s:%-4d %s: done with NtL fast-path"
- "%.30s:%-4d %s: ignoring NtL fast-path for %u, as waiting for link output available"
- "%.30s:%-4d %s: invoking send callback w/ written %u"
- "%.30s:%-4d %s: memmoving filledIn=%u, bufferHandled=%u"
- "%.30s:%-4d %s: not enough room %u to fit maxTLVLen %u"
- "%.30s:%-4d %s: not memmoving filledIn=%u, bufferHandled=%u"
- "%.30s:%-4d %s: nothing to read from nexus"
- "%.30s:%-4d %s: out of NtL inner loop"
- "%.30s:%-4d %s: out of NtL outer loop"
- "%.30s:%-4d %s: performing RX sync (%u packets, %u bytes, %u pending, %0.2f msec, canWriteMore %d, memmove %u)"
- "%.30s:%-4d %s: starting NtL inner loop"
- "%.30s:%-4d %s: starting NtL outer loop"
- "%.30s:%-4d %s: wrote %u (%u/%u) bytes from linkWriteBuffer"
- "%.30s:%-4d %s: wrote %u bytes from nexus for ESP seq: %u (spi: %u)"
- "%.30s:%-4d ABORTING: Assertion Failed: (dstAddr) != ((void*)0)"
- "%.30s:%-4d ABORTING: Assertion Failed: (ioVecs) != ((void*)0)"
- "%.30s:%-4d ABORTING: Assertion Failed: (nrXPCQueue) != ((void*)0)"
- "%.30s:%-4d ABORTING: Assertion Failed: (outBuffer) != ((void*)0)"
- "%.30s:%-4d ABORTING: Assertion Failed: (packetBuffer) != ((void*)0)"
- "%.30s:%-4d ABORTING: Assertion Failed: (propertiesCopy.outOfBandKey) != ((void*)0)"
- "%.30s:%-4d ABORTING: Assertion Failed: (retNum) != ((void*)0)"
- "%.30s:%-4d ABORTING: Assertion Failed: (sNRLogObj) != ((void*)0)"
- "%.30s:%-4d ABORTING: Assertion Failed: (self.queue) != ((void*)0)"
- "%.30s:%-4d ABORTING: Assertion Failed: (srcAddr) != ((void*)0)"
- "%.30s:%-4d ABORTING: Assertion Failed: (xpcDict) != ((void*)0)"
- "%.30s:%-4d ABORTING: Assertion Failed: (xpcKey) != ((void*)0)"
- "%.30s:%-4d ABORTING: Assertion Failed: bytesWritten == length"
- "%.30s:%-4d ABORTING: Assertion Failed: bytesWritten == length; bytesWritten (%u) != length (%u), offset: %u, ioVec: %@"
- "%.30s:%-4d ABORTING: Assertion Failed: computedBytes == writtenLength"
- "%.30s:%-4d ABORTING: Assertion Failed: dataLen <= 65535"
- "%.30s:%-4d ABORTING: Assertion Failed: dataLen > 0"
- "%.30s:%-4d ABORTING: Assertion Failed: ioVecs[0].len == 1; %@"
- "%.30s:%-4d ABORTING: Assertion Failed: ioVecs[1].len == 1; %@"
- "%.30s:%-4d ABORTING: Assertion Failed: iovecIndex + 1 < numIOVecs; %@, iovecIndex=%u bytesToCheckThisIOVec=%u"
- "%.30s:%-4d ABORTING: Assertion Failed: iovecs[iovecIndex + 1].len >= 1; %@, iovecIndex=%u bytesToCheckThisIOVec=%u"
- "%.30s:%-4d ABORTING: Assertion Failed: iovecs[iovecIndex].len >= bytesToCheckThisIOVec + 1; %@, iovecIndex=%u bytesToCheckThisIOVec=%u"
- "%.30s:%-4d ABORTING: Assertion Failed: numIOVecs > 0"
- "%.30s:%-4d ABORTING: Assertion Failed: numIOVecs > 1"
- "%.30s:%-4d ABORTING: Assertion Failed: numIOVecs > 1; %@"
- "%.30s:%-4d ABORTING: Assertion Failed: numIOVecs > 2; %@"
- "%.30s:%-4d ABORTING: Assertion Failed: packetLength > 0"
- "%.30s:%-4d ABORTING: Assertion Failed: packetLength >= sizeof(NRIPv6Hdr_s)"
- "%.30s:%-4d ABORTING: Assertion Failed: propertiesCopy.outOfBandKey.length == 34"
- "%.30s:%-4d ABORTING: Assertion Failed: tlvLen > 0"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with Device pairing bluetoothMACAddress length %lu != 6"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with Device pairing properties has pairWithSPPLink but no bluetoothMACAddress"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with Device pairing properties must either have wasInitiallySetupUsingIDSPairing or outOfBandKey"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with Device pairing protocol version %llu is too large"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL bluetoothUUID"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL completionBlock"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL dataProtectionClass == NRDataProtectionClassC || dataProtectionClass == NRDataProtectionClassD"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL delegate"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL deviceID"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL deviceIdentifier"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL directoryPath"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL directoryPath.length"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL directoryPathC"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL filePath"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL filePath.length"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL filePathC"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL idsDeviceID"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL nrDeviceIdentifier"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL nrUUID"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL operationalproperties"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL portString"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL properties"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with NULL queue"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with all-zero bluetoothUUID"
- "%.30s:%-4d ABORTING: BUG IN CLIENT OF NetworkRelay: %s called with all-zero nrDeviceIdentifier"
- "%.30s:%-4d ABORTING: [super initWithCoder:] failed"
- "%.30s:%-4d ABORTING: [super init] failed"
- "%.30s:%-4d ABORTING: _strict_reallocf called with size 0"
- "%.30s:%-4d ABORTING: _strict_reallocf(%zu) failed"
- "%.30s:%-4d ABORTING: dispatch_queue_create(%s) failed"
- "%.30s:%-4d ABORTING: strict_calloc(%zu, %zu) failed"
- "%.30s:%-4d ABORTING: strict_malloc called with size 0"
- "%.30s:%-4d ABORTING: strict_malloc(%zu) failed"
- "%.30s:%-4d ABORTING: xpc_array_create(%p, %u) failed"
- "%.30s:%-4d ABORTING: xpc_dictionary_create(%p, %p, %u) failed"
- "%.30s:%-4d ABORTING: xpc_string_create(%s) failed"
- "%.30s:%-4d Advancing linkReadBuffer handled by %u handled=%u filledIn=%u"
- "%.30s:%-4d All clients of prefer Wi-Fi went away"
- "%.30s:%-4d All clients of quick relay went away"
- "%.30s:%-4d All-zero nrUUID in response from daemon"
- "%.30s:%-4d Avoiding compression of strange length payload %u expected %u"
- "%.30s:%-4d Cancel: %@ %@"
- "%.30s:%-4d Checkin could not deliver message %@, error %@, retrying"
- "%.30s:%-4d Checkin received XPC dict: %@"
- "%.30s:%-4d Checkin received unexpected XPC object: %@"
- "%.30s:%-4d Clearing NREndpoint cache"
- "%.30s:%-4d Created temporary directory at \"%@\""
- "%.30s:%-4d Creating %@ for ephemeral pairing"
- "%.30s:%-4d Creating temporary directory at \"%@\""
- "%.30s:%-4d Dealloc %@ for %@"
- "%.30s:%-4d Dealloc: %@"
- "%.30s:%-4d Decompressed 6LoWPAN data from %u to %u, %@ to %@"
- "%.30s:%-4d Device supports restricted ports: %s"
- "%.30s:%-4d Disabled device %@"
- "%.30s:%-4d Disabling device %@"
- "%.30s:%-4d Enabled device %@"
- "%.30s:%-4d Enabling device %@"
- "%.30s:%-4d Ended linkInputSlot on a Pad0 handled=%u filledIn=%u"
- "%.30s:%-4d Ended linkReadBuffer on a Pad0 handled=%u filledIn=%u"
- "%.30s:%-4d Failed to archive operational properties %@"
- "%.30s:%-4d Failed to create directory at \"%@\": %@"
- "%.30s:%-4d Failed to disable device %@: %@"
- "%.30s:%-4d Failed to enable device %@: %@"
- "%.30s:%-4d Failed to get agent UUID"
- "%.30s:%-4d Failed to register device %@ with properties %@: %@"
- "%.30s:%-4d Failed to resolve endpoint for %@ %@"
- "%.30s:%-4d Failed to save diagnostic status to directory \"%s\""
- "%.30s:%-4d Failed to start %@ for %@"
- "%.30s:%-4d Failed to unregister all devices: %@"
- "%.30s:%-4d Failed to unregister device %@: %@"
- "%.30s:%-4d Found %@ for bluetoothUUID %@"
- "%.30s:%-4d Found %@ for idsDeviceID %@"
- "%.30s:%-4d Got NRUUID %@ from cache for bluetoothUUID %@"
- "%.30s:%-4d Got NRUUID %@ from cache for idsDeviceID %@"
- "%.30s:%-4d Got NRUUID %@ from daemon for bluetoothUUID %@"
- "%.30s:%-4d Got NRUUID %@ from daemon for idsDeviceID %@"
- "%.30s:%-4d Got [%@] total len %u"
- "%.30s:%-4d Handling Pad0 in linkInputSlot alreadyRead=%u"
- "%.30s:%-4d Handling Pad0 in linkReadBuffer"
- "%.30s:%-4d Handling PadN %u"
- "%.30s:%-4d Ignoring path evaluator update for a stale evaluator: old: %@, new: %@"
- "%.30s:%-4d Ignoring setting prefer Wi-Fi to %d"
- "%.30s:%-4d Informing client that %@ %shasUnpairedBluetooth"
- "%.30s:%-4d Informing client that %@ has link type %@"
- "%.30s:%-4d Informing client that %@ has link type %@ subtype %@"
- "%.30s:%-4d Informing client that %@ has proxy svc interface name %@"
- "%.30s:%-4d Informing client that %@ has thermal pressure level %@"
- "%.30s:%-4d Informing client that %@ is %s"
- "%.30s:%-4d Informing client that %@ is %sabled"
- "%.30s:%-4d Informing client that %@ is %sclassCConnected"
- "%.30s:%-4d Informing client that %@ is %scloudConnected"
- "%.30s:%-4d Informing client that %@ is %sconnected"
- "%.30s:%-4d Informing client that %@ is %snearby"
- "%.30s:%-4d Informing client that %@ is %sregistered"
- "%.30s:%-4d Init: %@"
- "%.30s:%-4d Invalid checksum detected in Isoch loop len %u filledIn=%u handled=%u ioVecContentLen=%u alreadyRead=%zu "
- "%.30s:%-4d Link Read context: %p"
- "%.30s:%-4d Link input available - %@"
- "%.30s:%-4d Link output available - %@"
- "%.30s:%-4d Looking into incoming TLV %@ len=%u%s"
- "%.30s:%-4d Looking into incoming TLV o1 %@ len=%u handled=%u filledIn=%u"
- "%.30s:%-4d Looking into incoming TLV o2 %@ len=%u handled=%u filledIn=%u slotLen=%u alreadyRead=%u"
- "%.30s:%-4d Looking into incoming TLV o3 %@"
- "%.30s:%-4d Looking into incoming TLV o4 %@ len=%u handled=%u filledIn=%u slotLen=%u"
- "%.30s:%-4d Looking into incoming TLV o5 %@"
- "%.30s:%-4d LtN not enough input bytes from linkInputSlot %u to fit %@ tlvLen %u"
- "%.30s:%-4d M=0 DAC=1 DAM=00 is reserved"
- "%.30s:%-4d M=1 DAC=1 DAM!=00 is reserved"
- "%.30s:%-4d Marking as completed"
- "%.30s:%-4d Marking as completed (no nexusOutputSlot) alreadyRead=%u"
- "%.30s:%-4d Marking as completed (not enough input bytes) alreadyRead=%u"
- "%.30s:%-4d Missing address"
- "%.30s:%-4d Missing nrUUID in response from daemon"
- "%.30s:%-4d NREndpoint cache generation changed: %llu -> %llu"
- "%.30s:%-4d Nexus input available - %@"
- "%.30s:%-4d Nexus output available - %@"
- "%.30s:%-4d No delegate found"
- "%.30s:%-4d No netagents to retrieve agent UUID"
- "%.30s:%-4d No path to retrieve agent UUID"
- "%.30s:%-4d No path to retrieve agent data"
- "%.30s:%-4d No path to update agent UUID"
- "%.30s:%-4d Not marking as completed (all in linkReadBuffer)"
- "%.30s:%-4d Packet too short for determining address family"
- "%.30s:%-4d Packet too short for determining next header"
- "%.30s:%-4d Placing in ioVec[%u] buf=%p len=%u alreadyRead=%u += %u"
- "%.30s:%-4d Placing linkReadBuffer handled=%u filledIn=%u in ioVec[%u] buf=%p len=%u"
- "%.30s:%-4d Querying NRUUID for IDSDeviceID %@"
- "%.30s:%-4d Querying NRUUID for bluetoothUUID %@"
- "%.30s:%-4d Querying whether companion link is enabled"
- "%.30s:%-4d Querying whether device supports restricted ports"
- "%.30s:%-4d Read context: %p"
- "%.30s:%-4d Reading from buf=%p len=%u alreadyRead=%u handled=%u filledIn=%u"
- "%.30s:%-4d Reading link input, setting filledIn=%u (linkChannelPriority=%u)"
- "%.30s:%-4d Ready to handle %@ len %u in %@ ioVecContentLen=%u alreadyRead=%u"
- "%.30s:%-4d Reasserting the agent"
- "%.30s:%-4d Received %supdate %sregistered %sabled %snearby %sconnected %scloudConnected %sclassCConnected %shasUnpairedBluetooth %s %@(%@) prx %@ thermal %@ for %@"
- "%.30s:%-4d Received XPC dict: %@"
- "%.30s:%-4d Received XPC error: %@, retrying"
- "%.30s:%-4d Received empty out of band key, using generic key for device %@ with properties %@"
- "%.30s:%-4d Received invalid TLV len %u for %@ (max=%u) %@"
- "%.30s:%-4d Received path: %@"
- "%.30s:%-4d Received unexpected XPC object: %@"
- "%.30s:%-4d Refresh generation response %lld (%@)"
- "%.30s:%-4d Registered device %@ with properties %@"
- "%.30s:%-4d Registering device %@ with properties %@"
- "%.30s:%-4d Reinjecting %@ packet len %u to nexusOutputSlot=%p buf=%p len=%u: %@, buflet: %d"
- "%.30s:%-4d Resetting state"
- "%.30s:%-4d Resolved properties: %@"
- "%.30s:%-4d Response of invalid length %zu"
- "%.30s:%-4d Response of invalid type"
- "%.30s:%-4d Returning that companion link is %sabled"
- "%.30s:%-4d Saved diagnostic status to directory \"%s\""
- "%.30s:%-4d Saved diagnostic status to file \"%s\""
- "%.30s:%-4d Saving diagnostic status to directory \"%s\""
- "%.30s:%-4d Saving diagnostic status to file \"%s\""
- "%.30s:%-4d Saving diagnostic status to temp directory"
- "%.30s:%-4d Setting prefer Wi-Fi assert count: %ld -> %ld"
- "%.30s:%-4d Setting quick relay assert count: %ld -> %ld"
- "%.30s:%-4d Shrinking ioVecs[%u] down by %u - %@ ioVecContentLen=%u alreadyRead=%u"
- "%.30s:%-4d Shrunk ioVecs[%u] down by %u - %@ ioVecContentLen=%u alreadyRead=%u"
- "%.30s:%-4d Started %@ for %@"
- "%.30s:%-4d Tried to sync nexus output but _nexusOutputRing is NULL"
- "%.30s:%-4d Unregistered all devices"
- "%.30s:%-4d Unregistered device %@"
- "%.30s:%-4d Unregistering all devices"
- "%.30s:%-4d Unregistering device %@"
- "%.30s:%-4d Used 6LowPAN IPHC to compress %@, %u to %u - %@ %@ %@"
- "%.30s:%-4d Using new nexusOutputSlot=%p"
- "%.30s:%-4d Write context: %p"
- "%.30s:%-4d adding quick relay request (count is now %ld)"
- "%.30s:%-4d can't handle M=1 DAC=1 DAM=00 yet"
- "%.30s:%-4d can't handle NH=1 yet"
- "%.30s:%-4d checksum failed disjoint IOVec received 0x%02x%02x != computed 0x%02x%02x"
- "%.30s:%-4d checksum failed same IOVec received 0x%02x%02x != computed 0x%02x%02x"
- "%.30s:%-4d end of LtN inner loop alreadyRead=%u splen=%u"
- "%.30s:%-4d failed to reinject %@ tlvLen=%u slotLen=%u"
- "%.30s:%-4d handling uIKE packet of %llu bytes"
- "%.30s:%-4d hasUnpairedBluetooth: %d -> %d"
- "%.30s:%-4d highestNexusOutputSlotWrittenTo is NULL"
- "%.30s:%-4d invalid link channel priority"
- "%.30s:%-4d isAsleep: %d -> %d"
- "%.30s:%-4d isClassCConnected: %d -> %d"
- "%.30s:%-4d isCloudConnected: %d -> %d"
- "%.30s:%-4d isConnected: %d -> %d"
- "%.30s:%-4d isEnabled: %d -> %d"
- "%.30s:%-4d isNearby: %d -> %d"
- "%.30s:%-4d isRegistered: %d -> %d"
- "%.30s:%-4d link Write context: %p"
- "%.30s:%-4d link subtype: %@ -> %@"
- "%.30s:%-4d link type: %@ -> %@"
- "%.30s:%-4d memmoving the linkReadBuffer by handled=%u (filledIn=%u) thresh=%u"
- "%.30s:%-4d merged properties: %@"
- "%.30s:%-4d no 6lo compression - IPv4 - %@"
- "%.30s:%-4d no 6lo compression - not IPv6 - v=%u"
- "%.30s:%-4d no 6lo compression - too short %u"
- "%.30s:%-4d no curNexusOutputSlot, dropping %@ tlvLen=%u slotLen=%u"
- "%.30s:%-4d no nexusOutputSlot - consolidating %u bytes from linkInputSlot ioVecs[%u].buf=%p to linkReadBuffer filledIn=%u handled=%u"
- "%.30s:%-4d no nexusOutputSlot - tail consolidating %zu bytes from linkInputSlot to linkReadBuffer filledIn=%u handled=%u and marking as completed"
- "%.30s:%-4d no nexusOutputSlot and everything in linkReadBuffer alreadyRead=%zu"
- "%.30s:%-4d no nexusOutputSlot and linkReadBuffer is full %@ filledIn=%u handled=%u"
- "%.30s:%-4d no nexusOutputSlot highestSlot=%p %@ filledIn=%u handled=%u"
- "%.30s:%-4d not memmoving the linkReadBuffer thresh handled=%u filledIn=%u thresh=%u"
- "%.30s:%-4d not memmoving the linkReadBuffer zero handled=%u filledIn=%u thresh=%u"
- "%.30s:%-4d not ready to accept data"
- "%.30s:%-4d not shrinking len %u%s ioVecContentLen=%u alreadyRead=%u"
- "%.30s:%-4d out of LtN fast path inner loop"
- "%.30s:%-4d out of LtN fast path loop (%llu/%llu bytes)"
- "%.30s:%-4d packet too big %@ tlvLen=%u payloadLength=%u packetLength=%u"
- "%.30s:%-4d partial TLV - consolidating %u bytes from linkInputSlot buf %p to linkReadBuffer filledIn=%u handled=%u"
- "%.30s:%-4d proxy-svc intf name: %@ -> %@"
- "%.30s:%-4d read all of len=%u alreadyRead=%u nexusOutputAvailable=%d"
- "%.30s:%-4d received 6LoWPAN TLV too short %u"
- "%.30s:%-4d received XPC_ERROR_CONNECTION_INVALID"
- "%.30s:%-4d received internal failure result code: [%lld] %@"
- "%.30s:%-4d received more data than moveOffset (%u > %u), off %d"
- "%.30s:%-4d received unknown 6LoWPAN dispatch %u"
- "%.30s:%-4d resetting the linkReadBuffer (filledIn=%u)"
- "%.30s:%-4d reusing existing len=%u alreadyRead=%u"
- "%.30s:%-4d sending packets over medium pipe"
- "%.30s:%-4d source-%s: High"
- "%.30s:%-4d source-%s: Isochronous"
- "%.30s:%-4d source-%s: Medium"
- "%.30s:%-4d source-resume: NexusBEInput"
- "%.30s:%-4d source-resume: NexusBEOutput"
- "%.30s:%-4d source-resume: NexusBKInput"
- "%.30s:%-4d source-resume: NexusBKOutput"
- "%.30s:%-4d source-resume: NexusVIInput"
- "%.30s:%-4d source-resume: NexusVIOutput"
- "%.30s:%-4d source-resume: NexusVOInput"
- "%.30s:%-4d source-resume: NexusVOOutput"
- "%.30s:%-4d source-suspend: NexusBEInput"
- "%.30s:%-4d source-suspend: NexusBEOutput"
- "%.30s:%-4d source-suspend: NexusBKInput"
- "%.30s:%-4d source-suspend: NexusVIInput"
- "%.30s:%-4d source-suspend: NexusVIOutput"
- "%.30s:%-4d source-suspend: NexusVOInput"
- "%.30s:%-4d source-suspend: NexusVOOutput"
- "%.30s:%-4d start LtN fast path inner loop"
- "%.30s:%-4d start LtN fast path outer loop"
- "%.30s:%-4d starting NtL fast-path for %u"
- "%.30s:%-4d syncing nexus output (%u packets)"
- "%.30s:%-4d thermal pressure level: %@ -> %@"
- "%.30s:%-4d truncated packet received %u != %u"
- "%{public}s Assertion Failed: (sNRLogObj) != ((void*)0)"
- "-[NRBluetoothPacketParser handleIncomingIKEData:]"
- "nrCopyLogObj_block_invoke"

```
