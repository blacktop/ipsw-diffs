## bluetoothd

> `/usr/sbin/bluetoothd`

```diff

-192.7.0.0.0
-  __TEXT.__text: 0x87c680
+193.5.1.0.0
+  __TEXT.__text: 0x87fd08
   __TEXT.__auth_stubs: 0x4990
-  __TEXT.__objc_stubs: 0x173a0
-  __TEXT.__init_offsets: 0x58
-  __TEXT.__objc_methlist: 0x8b4c
+  __TEXT.__objc_stubs: 0x17380
+  __TEXT.__init_offsets: 0x5c
+  __TEXT.__objc_methlist: 0x8b44
   __TEXT.__const: 0x2504c
-  __TEXT.__gcc_except_tab: 0x6c83c
-  __TEXT.__cstring: 0xb4ed5
+  __TEXT.__gcc_except_tab: 0x6c9d0
+  __TEXT.__cstring: 0xb51ff
   __TEXT.__objc_classname: 0xa07
-  __TEXT.__objc_methname: 0x1be95
-  __TEXT.__objc_methtype: 0x49af
-  __TEXT.__oslogstring: 0xae013
+  __TEXT.__objc_methname: 0x1be5f
+  __TEXT.__objc_methtype: 0x4993
+  __TEXT.__oslogstring: 0xae105
   __TEXT.__ustring: 0x34
   __TEXT.__dlopen_cstrs: 0xd4
-  __TEXT.__unwind_info: 0x22fd8
+  __TEXT.__unwind_info: 0x230b0
   __TEXT.__eh_frame: 0x60
   __DATA_CONST.__auth_got: 0x24e0
   __DATA_CONST.__got: 0xdc8
   __DATA_CONST.__auth_ptr: 0x220
-  __DATA_CONST.__const: 0x30500
-  __DATA_CONST.__cfstring: 0x236e0
+  __DATA_CONST.__const: 0x306e8
+  __DATA_CONST.__cfstring: 0x23780
   __DATA_CONST.__objc_classlist: 0x2a8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd0

   __DATA_CONST.__objc_arrayobj: 0x1f8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0xf0b0
-  __DATA.__objc_selrefs: 0x6b50
+  __DATA.__objc_selrefs: 0x6b48
   __DATA.__objc_ivar: 0x1018
   __DATA.__objc_data: 0x1a90
-  __DATA.__data: 0x4a78
+  __DATA.__data: 0x4a80
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x72b4a
+  __DATA.__bss: 0x72b92
   __DATA.__common: 0x6fb8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: B84A1836-20F1-3494-BB7F-27D2F2762BF9
-  Functions: 33417
+  UUID: B3A01B27-9D28-3916-944B-EC54D0C86363
+  Functions: 33465
   Symbols:   1640
-  CStrings:  44127
+  CStrings:  44159
 
CStrings:
+ "%s:%06u: unable to check if profile is installed"
+ "-[LeDeviceCache readDeviceFromDatabase:statement:]"
+ "01:01:48"
+ "2c1877ad4ff80c066ea059b6fa73641767e9cd390213e77850886054489440cc"
+ "2d1739b4abd6fa985199c458d11afbffabba96bca06a0db3e4fd16a6f2a76835"
+ "39b1613448e7c989527265da99dce616dc77bad533d33f020b63c722a4b1733d"
+ "7817522da74b3aead8649e502aa25cfb5cbb3bbf0fd7944747ab14b4457afa60"
+ "7bbbb2c52336dbcf81115a1c87788a8c8eec2716033f5dab935c5f7bbf32f1ea"
+ "Checking for installed profiles\n"
+ "Dec  6 2025"
+ "Device %@ allowed to drop 0 IRK IRKSize:%zu"
+ "Disconnect OI_HCI_LM_HANDLE: 0x%x (%d) wakeUp: %s SNR: %{public}s RSSI: %{public}s\nRetransmission Rx: %{public}s Retransmission Tx: %{public}s Packet Type Rx: %{public}s Packet Type Tx: %{public}s"
+ "DropZeroIRK"
+ "Dropping 0 IRK for device %@"
+ "EventLogs"
+ "FeiZhiAPEX"
+ "FwLogs"
+ "Invalid AESSIV Key Count"
+ "Invalid AESSIV/Ratchet Key Count"
+ "Invalid MPS value %d, minimum required is 23"
+ "Invalid Ratchet Key Count"
+ "Invalid number of parameter = %d or length = %d"
+ "LEInstanceUpdatelist"
+ "LEInstanceUpdatelist: set tag for %s"
+ "LEInstanceUpdatelist: set tag for VID = 0x%04x, PID = 0x%04x"
+ "No change in profile configuration\n"
+ "Override %s Coex 0x%x connection scan timeout %d extended by %f percent"
+ "SRS PCIe failed to create profile monitor queue\n"
+ "Unable to create dict"
+ "cannot create xpc connection"
+ "cannot create xpc message"
+ "com.apple.KalBluetooth_driver"
+ "eventstream"
+ "fwloggerstream"
- "-[LeDeviceCache readDeviceFromDatabase:statement:readResolvedAddress:]"
- "21:27:22"
- "Disconnect connection handle: 0x%x (%d) wakeUp: %s SNR: %{public}s RSSI: %{public}s\nRetransmission Rx: %{public}s Retransmission Tx: %{public}s Packet Type Rx: %{public}s Packet Type Tx: %{public}s"
- "Invalid number of paramerter = %d"
- "Nov 18 2025"
- "^v36@0:8^{sqlite3=}16@24B32"
- "readDeviceFromDatabase:statement:readResolvedAddress:"

```
