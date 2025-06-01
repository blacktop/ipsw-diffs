## Ninepoint Systems Driver

> `/System/Library/ScreenReader/BrailleDrivers/Ninepoint Systems Driver.brailledriver/Ninepoint Systems Driver`

```diff

-283.0.0.0.0
-  __TEXT.__text: 0x2d58
-  __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0x214
-  __TEXT.__cstring: 0x68e
+285.0.2.0.0
+  __TEXT.__text: 0x1604
+  __TEXT.__auth_stubs: 0x320
+  __TEXT.__objc_stubs: 0x4c0
+  __TEXT.__objc_methlist: 0x104
+  __TEXT.__cstring: 0x362
   __TEXT.__oslogstring: 0xc0
-  __TEXT.__objc_methname: 0x5dd
-  __TEXT.__objc_classname: 0xb9
+  __TEXT.__objc_methname: 0x5cf
+  __TEXT.__objc_classname: 0xa2
   __TEXT.__objc_methtype: 0x224
-  __TEXT.__unwind_info: 0xd0
-  __DATA_CONST.__auth_got: 0x1d0
-  __DATA_CONST.__got: 0x40
-  __DATA_CONST.__cfstring: 0x360
-  __DATA_CONST.__objc_classlist: 0x10
+  __TEXT.__unwind_info: 0x98
+  __DATA_CONST.__auth_got: 0x198
+  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__cfstring: 0x1e0
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x11b0
-  __DATA.__objc_selrefs: 0x1d0
+  __DATA.__objc_const: 0x8d8
+  __DATA.__objc_selrefs: 0x1c8
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x50
-  __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x60
-  __DATA.__objc_data: 0xa0
+  __DATA.__objc_superrefs: 0x8
+  __DATA.__objc_ivar: 0x30
+  __DATA.__objc_data: 0x50
   __DATA.__data: 0x240
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2331DC4A-570A-37A3-A34D-944DBAF1179E
-  Functions: 46
-  Symbols:   112
-  CStrings:  202
+  UUID: 95D3D87E-2F53-34DC-AB2D-CD44F3F1A1D3
+  Functions: 24
+  Symbols:   90
+  CStrings:  176
 
Symbols:
- OBJC_IVAR_$_MSCROHIMSBrailleDriver._bluetoothChannelIsLost
- OBJC_IVAR_$_MSCROHIMSBrailleDriver._comPort
- OBJC_IVAR_$_MSCROHIMSBrailleDriver._device
- OBJC_IVAR_$_MSCROHIMSBrailleDriver._driverDelegate
- OBJC_IVAR_$_MSCROHIMSBrailleDriver._hasBeenUnloaded
- OBJC_IVAR_$_MSCROHIMSBrailleDriver._isDriverLoaded
- OBJC_IVAR_$_MSCROHIMSBrailleDriver._mainSize
- OBJC_IVAR_$_MSCROHIMSBrailleDriver._modelIdentifier
- OBJC_IVAR_$_MSCROHIMSBrailleDriver._readBuffer
- OBJC_IVAR_$_MSCROHIMSBrailleDriver._readBufferLock
- OBJC_IVAR_$_MSCROHIMSBrailleDriver._readerThread
- OBJC_IVAR_$_MSCROHIMSBrailleDriver._safeReadBuffer
- _CFRunLoopRunInMode
- _OBJC_CLASS_$_MSCROHIMSBrailleDriver
- _OBJC_METACLASS_$_MSCROHIMSBrailleDriver
- _SCRDAdvanceBufferToPacketStart
- _SCRDHIMSBrailleEDGEExtractEventsFromBuffer
- _SCRDHIMSCreateRequest
- _SCRDHIMSFillPacket
- _SCRDHIMSIsPacketValid
- _free
- _kCFRunLoopDefaultMode
CStrings:
- "Failed to load HIMS braille driver - Unexpected transport [%ld], conforms to protocol [%ld]"
- "Failed to load HIMS braille driver because the device is no longer connected over bluetooth."
- "Failed to load HIMS braille driver because we found no matching paired device"
- "Failed to load HIMS braille driver because we have no bundle identifier"
- "Failed to load HIMS braille driver, Missing model identifier from info plist [%{public}@]"
- "Failed to load HIMS braille driver, Unknown model identifier [%{public}@]"
- "Failed to load HIMS braille driver, bluetoothChannelIsLost [%ld], unloaded [%ld], runLoopStatus [%ld]"
- "Failed to write to com port for cellCountRequest"
- "Loading HIMS braille driver"
- "MSCROHIMSBrailleDriver"
- "Unloading HIMS Braille Driver"
- "_himsDeviceId"
- "com.apple.scrod.braille.driver.hims.braille.edge.20"
- "com.apple.scrod.braille.driver.hims.braille.edge.40"

```
