## bluetoothd

> `/usr/sbin/bluetoothd`

```diff

-185.4.0.0.0
-  __TEXT.__text: 0x7c5a6c
+185.6.1.1.1
+  __TEXT.__text: 0x7c71a4
   __TEXT.__auth_stubs: 0x4620
-  __TEXT.__objc_stubs: 0x13120
+  __TEXT.__objc_stubs: 0x13140
   __TEXT.__init_offsets: 0x54
   __TEXT.__objc_methlist: 0x655c
   __TEXT.__const: 0xa77c
-  __TEXT.__gcc_except_tab: 0x619a4
-  __TEXT.__cstring: 0xa2c16
+  __TEXT.__gcc_except_tab: 0x61ab4
+  __TEXT.__cstring: 0xa2fa5
   __TEXT.__objc_classname: 0x7eb
-  __TEXT.__objc_methname: 0x15eb3
+  __TEXT.__objc_methname: 0x15ebb
   __TEXT.__objc_methtype: 0x44e7
-  __TEXT.__oslogstring: 0xa1884
+  __TEXT.__oslogstring: 0xa1bb7
   __TEXT.__ustring: 0x34
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__unwind_info: 0x1fbb0
+  __TEXT.__unwind_info: 0x1fbe8
   __TEXT.__eh_frame: 0x60
   __DATA_CONST.__auth_got: 0x2328
   __DATA_CONST.__got: 0xc90
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x2c6e0
-  __DATA_CONST.__cfstring: 0x1f7c0
+  __DATA_CONST.__const: 0x2c7a0
+  __DATA_CONST.__cfstring: 0x1f940
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb0

   __DATA_CONST.__objc_arrayobj: 0x1c8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0xb4d0
-  __DATA.__objc_selrefs: 0x5600
+  __DATA.__objc_selrefs: 0x5608
   __DATA.__objc_ivar: 0xbb4
   __DATA.__objc_data: 0x14f0
   __DATA.__data: 0x4668
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x19f9a
+  __DATA.__bss: 0x19fda
   __DATA.__common: 0x6f00
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 30477
+  Functions: 30494
   Symbols:   1547
-  CStrings:  35622
+  CStrings:  35664
 
CStrings:
+ "22:17:25"
+ "Apr 10 2025"
+ "CBClassicMsgIdAppTCCCheckComplete"
+ "CBClassicMsgIdCheckAppTCC"
+ "CBClassicMsgIdPairingAgentRemoveGlobalLTK"
+ "CBClassicMsgIdPairingAgentSetGlobalLTK"
+ "CBLePipeMsgIdAppTCCCheckComplete"
+ "CBLePipeMsgIdCheckAppTCC"
+ "CBMsgIdAppTCCCheckComplete"
+ "CBMsgIdCheckAppTCC"
+ "CBMsgIdPairingAgentRemoveGlobalLTK"
+ "CBMsgIdPairingAgentSetGlobalLTK"
+ "ChipBootFailureChipBootFailureOperationNotSupported"
+ "ChipBootFailureDeviceFatalError"
+ "ChipBootFailureInvalidExtension"
+ "ChipBootFailureInvalidFilePointer"
+ "ChipBootFailureInvalidFileSize"
+ "ChipBootFailureUnableToAllocateMemory"
+ "ChipBootFailureUnableToFLR"
+ "ChipBootFailureUnableToFindService"
+ "ChipBootFailureUnableToOpenFile"
+ "ChipBootFailureUnableToReadFile"
+ "ChipBootFailureUnableToSendFWImage"
+ "Clearing default LTK security keys"
+ "Failed to configureRSSIIntentforAOP for handle:0x%02X - device not yet added"
+ "Found %lu paired LE device%{public}s in synced keychain, total paired LE devices %lu"
+ "Invalid Handle, allow %d"
+ "LPMSU params not set"
+ "New client to SPUBluetooth 0x%llx - enumerated before AOPInterfaceManager was initialized"
+ "OverrideMaxLESyncedDevices"
+ "Session \"%{public}s\" is asking to clear LTK"
+ "Session \"%{public}s\" is asking to set LTK size %d useCase %s result %d"
+ "Setting default LTK security keys (lengh:%d)"
+ "TCC Done session:%s fDeviceAccessForMediaSession:%d fDeviceAccessForMediaExtension:%d fDeviceAccessPerAccessorySession:%d fDeviceAccessPerAccessoryExtension:%d sessionType:%d"
+ "Warning: Setting default LTK security keys twice"
+ "We can have up to %d paired devices, %d synced LE devices"
+ "deviceIdLength invalid: %d"
+ "findResponseByHCIHandle response is NULL, lmHandle invalid"
+ "findResponseByHCIHandle session is NULL, lmHandle invalid"
+ "init cloud - found %lu paired LE device%{public}s in local keychain"
+ "kCBGlobalTemporaryLTK"
+ "kCBMsgArgFakeLeDeviceIgnoreMaxLimit"
+ "kCBMsgArgFakeLeDeviceSynced"
+ "lpmFlag1 or lpmFlag2 not supported for this platform."
+ "prkLength invalid: %d"
+ "statedump: Default Temporary LTK:"
+ "statedump: Usecase %lld, TemporaryLTK %{private}.16P"
+ "using default temporary keys for device \"%{public}@\", keyLen %d"
+ "vseLpmDebugDeviceIdEvent - DeviceId: %@, prk: %@, timestamp: 0x%08X"
- "20:56:28"
- "Found %lu paired LE device%{public}s in local keychain, loaded %lu"
- "Invalid Handle"
- "Mar 24 2025"
- "We can have up to %d paired devices"
- "handleTCCDone fDeviceAccessForMediaSession:%d fDeviceAccessForMediaExtension:%d fDeviceAccessPerAccessorySession:%d fDeviceAccessPerAccessoryExtension:%d sessionType:%d"
- "kCBMsgArgTCCLEDevicesAroundDetails"
- "kCBMsgArgTCCLELocalizedCenterLabel"

```
