## AppleMIDIBluetoothDriver

> `/System/Library/Audio/MIDI Drivers/AppleMIDIBluetoothDriver.plugin/AppleMIDIBluetoothDriver`

```diff

-315.500.0.0.0
-  __TEXT.__text: 0xf2c8
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_stubs: 0x1160
+319.0.0.0.0
+  __TEXT.__text: 0xf49c
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__objc_stubs: 0x11c0
   __TEXT.__objc_methlist: 0x954
-  __TEXT.__cstring: 0x4e6
-  __TEXT.__gcc_except_tab: 0x498
-  __TEXT.__const: 0xf0
-  __TEXT.__oslogstring: 0x2196
-  __TEXT.__objc_methname: 0x17ce
+  __TEXT.__cstring: 0x4f4
+  __TEXT.__gcc_except_tab: 0x4c0
+  __TEXT.__const: 0xf8
+  __TEXT.__oslogstring: 0x2211
+  __TEXT.__objc_methname: 0x1810
   __TEXT.__objc_classname: 0xb4
-  __TEXT.__objc_methtype: 0xb4d
-  __TEXT.__unwind_info: 0x5a0
-  __DATA_CONST.__auth_got: 0x3f8
-  __DATA_CONST.__got: 0x138
+  __TEXT.__objc_methtype: 0xadf
+  __TEXT.__unwind_info: 0x5b8
+  __DATA_CONST.__auth_got: 0x3e8
+  __DATA_CONST.__got: 0x148
   __DATA_CONST.__const: 0x500
   __DATA_CONST.__cfstring: 0x400
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0xd98
-  __DATA.__objc_selrefs: 0x6b0
+  __DATA.__objc_selrefs: 0x6c8
   __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0x190
-  __DATA.__data: 0x248
+  __DATA.__data: 0x238
   __DATA.__bss: 0xe0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMIDI.framework/CoreMIDI
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/caulk.framework/caulk
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 59AC7464-A506-3DAC-8C90-BE605F55F6C3
-  Functions: 348
-  Symbols:   176
-  CStrings:  603
+  UUID: 178BF197-EDF3-3BCC-8827-6B7EA476409D
+  Functions: 344
+  Symbols:   177
+  CStrings:  609
 
Symbols:
+ _CBConnectPeripheralOptionConnectionUseCase
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSMutableDictionary
- __Znwm
- __os_log_error_impl
CStrings:
+ "%25s:%-5d  CAMutex::CAMutex: Could not init the mutex"
+ "%25s:%-5d  CAMutex::Lock: Could not lock the mutex"
+ "%25s:%-5d  CAMutex::Try: call to pthread_mutex_trylock failed, Error: %d (%s)"
+ "%25s:%-5d  CAMutex::Unlock: A thread is attempting to unlock a Mutex it doesn't own"
+ "%25s:%-5d  CAMutex::Unlock: Could not unlock the mutex"
+ "%25s:%-5d Setting MIDI low latency for peripheral: %@"
+ "%25s:%-5d connectPeripheral: UUID %@ (MIDI low latency)"
+ "CAMutex.cpp"
+ "dictionary"
+ "dictionaryWithObjects:forKeys:count:"
+ "setObject:forKey:"
+ "{BLEMIDIPacketEmitter=\"_vptr$MIDIPacketEmitter\"^^?\"mEmitterProc\"{function<void (const MIDIPacketList *)>=\"__f_\"{__value_func<void (const MIDIPacketList *)>=\"__buf_\"(type=\"__data\"[24C])\"__f_\"^v}}\"mCurPacket\"^{MIDIPacket}\"mBuf\"[1024C]\"mEP\"I\"mIsDirty\"B}"
+ "{vector<std::shared_ptr<BLEIOBuffer>, std::allocator<std::shared_ptr<BLEIOBuffer>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
- " CAMutex::CAMutex: Could not init the mutex"
- " CAMutex::Lock: Could not lock the mutex"
- " CAMutex::Try: call to pthread_mutex_trylock failed, Error: %d (%s)"
- " CAMutex::Unlock: A thread is attempting to unlock a Mutex it doesn't own"
- " CAMutex::Unlock: Could not unlock the mutex"
- "%25s:%-5d connectPeripheral: UUID %@"
- "{BLEMIDIPacketEmitter=\"_vptr$MIDIPacketEmitter\"^^?\"mEmitterProc\"{function<void (const MIDIPacketList *)>=\"__f_\"{__value_func<void (const MIDIPacketList *)>=\"__buf_\"{type=\"__lx\"[24C]}\"__f_\"^v}}\"mCurPacket\"^{MIDIPacket}\"mBuf\"[1024C]\"mEP\"I\"mIsDirty\"B}"
- "{vector<std::shared_ptr<BLEIOBuffer>, std::allocator<std::shared_ptr<BLEIOBuffer>>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::shared_ptr<BLEIOBuffer> *, std::allocator<std::shared_ptr<BLEIOBuffer>>>=\"__value_\"^v}}"

```
