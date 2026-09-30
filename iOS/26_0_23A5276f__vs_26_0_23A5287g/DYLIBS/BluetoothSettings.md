## BluetoothSettings

> `/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings`

```diff

-450.36.0.0.0
-  __TEXT.__text: 0x2277c
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0x18bc
-  __TEXT.__cstring: 0x1791
+450.38.0.0.0
+  __TEXT.__text: 0x22b04
+  __TEXT.__auth_stubs: 0xcd0
+  __TEXT.__objc_methlist: 0x18ec
+  __TEXT.__cstring: 0x1801
   __TEXT.__const: 0x762
   __TEXT.__gcc_except_tab: 0x328
-  __TEXT.__oslogstring: 0x1e02
+  __TEXT.__oslogstring: 0x1e42
   __TEXT.__swift5_typeref: 0x296
   __TEXT.__constg_swiftt: 0x17c
   __TEXT.__swift5_fieldmd: 0xb0

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0x778
+  __TEXT.__unwind_info: 0x780
   __TEXT.__eh_frame: 0x2b8
   __TEXT.__objc_classname: 0x1c3
-  __TEXT.__objc_methname: 0x4f53
+  __TEXT.__objc_methname: 0x4fa9
   __TEXT.__objc_methtype: 0x106e
-  __TEXT.__objc_stubs: 0x4300
-  __DATA_CONST.__got: 0x5e8
+  __TEXT.__objc_stubs: 0x4380
+  __DATA_CONST.__got: 0x5f8
   __DATA_CONST.__const: 0x578
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1728
+  __DATA_CONST.__objc_selrefs: 0x1748
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x670
-  __AUTH_CONST.__const: 0x2c8
-  __AUTH_CONST.__cfstring: 0x1ac0
+  __AUTH_CONST.__auth_got: 0x678
+  __AUTH_CONST.__const: 0x2e8
+  __AUTH_CONST.__cfstring: 0x1b60
   __AUTH_CONST.__objc_const: 0x25e8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28

   __DATA.__objc_ivar: 0x198
   __DATA.__data: 0x5d0
   __DATA.__common: 0x30
-  __DATA.__bss: 0x720
+  __DATA.__bss: 0x730
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DCD5823C-225A-3500-A663-F3AA5D9E25C3
-  Functions: 634
-  Symbols:   2275
-  CStrings:  1697
+  UUID: 9F809CE9-0CDC-37B6-9C44-2EABB288F5F4
+  Functions: 640
+  Symbols:   2298
+  CStrings:  1715
 
Symbols:
+ -[BTSDevice isLEAudioSupported]
+ -[BTSDeviceLE isLEAudioSupported]
+ -[BTSDevicesController isLEAudioLiveOnEnabled]
+ -[BTSDevicesController isLEAudioLiveOnEnabled].cold.1
+ -[BTSDevicesController markLEAudioDevice:]
+ GCC_except_table207
+ _CBUUIDCommonAudioServiceString
+ _CBUUIDTelephonyMediaAudioServiceString
+ _CFPreferencesCopyAppValue
+ ___46-[BTSDevicesController isLEAudioLiveOnEnabled]_block_invoke
+ ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.775
+ ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.775.cold.1
+ ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.779
+ ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.779.cold.1
+ ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.780
+ ___block_literal_global.751
+ _isLEAudioLiveOnEnabled.flagExists
+ _isLEAudioLiveOnEnabled.onceTokenLEAudio
+ _isLEAudioLiveOnEnabled.osFeatureLEAudioEnabled
+ _objc_msgSend$isLEAudioLiveOnEnabled
+ _objc_msgSend$isLEAudioSupported
+ _objc_msgSend$markLEAudioDevice:
+ _objc_msgSend$stringByAppendingString:
- GCC_except_table204
- ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.759
- ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.759.cold.1
- ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.763
- ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.763.cold.1
- ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.764
CStrings:
+ "Accessibility"
+ "LE"
+ "LEAudio - liveOnEnabled: %d, featureEnabled: %d"
+ "LEAudioLiveOnEnable"
+ "LeAudio"
+ "Mark LEAudio device"
+ "[LEAudio]"
+ "_LEAUDIO_DEVICE_"
+ "com.apple.MobileBluetooth.debug"
+ "isLEAudioLiveOnEnabled"
+ "isLEAudioSupported"
+ "markLEAudioDevice:"
+ "stringByAppendingString:"

```
