## ScreenReaderOutput

> `/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput`

```diff

-346.2.4.0.0
-  __TEXT.__text: 0x39d48
-  __TEXT.__auth_stubs: 0xeb0
-  __TEXT.__objc_methlist: 0x3a7c
-  __TEXT.__cstring: 0x32f9
-  __TEXT.__gcc_except_tab: 0x149c
-  __TEXT.__oslogstring: 0xfed
-  __TEXT.__const: 0x158
+346.2.9.0.0
+  __TEXT.__text: 0x3a3ec
+  __TEXT.__auth_stubs: 0xec0
+  __TEXT.__objc_methlist: 0x3a8c
+  __TEXT.__cstring: 0x3386
+  __TEXT.__gcc_except_tab: 0x14dc
+  __TEXT.__oslogstring: 0x10a0
+  __TEXT.__const: 0x150
   __TEXT.__ustring: 0x9e
-  __TEXT.__unwind_info: 0x1184
+  __TEXT.__unwind_info: 0x11a0
   __TEXT.__objc_classname: 0x6b9
-  __TEXT.__objc_methname: 0x9fce
+  __TEXT.__objc_methname: 0xa010
   __TEXT.__objc_methtype: 0x1bc6
-  __TEXT.__objc_stubs: 0x8160
+  __TEXT.__objc_stubs: 0x81c0
   __DATA_CONST.__got: 0x110
   __DATA_CONST.__const: 0x7c0
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x8da8
-  __DATA_CONST.__objc_selrefs: 0x2620
+  __DATA_CONST.__objc_const: 0x8dc8
+  __DATA_CONST.__objc_selrefs: 0x2628
   __DATA_CONST.__objc_arraydata: 0x200
   __AUTH_CONST.__objc_const: 0x48
   __AUTH_CONST.__cfstring: 0x3560

   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_ptr: 0x38
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x768
+  __AUTH_CONST.__auth_got: 0x770
   __DATA.__objc_protorefs: 0x20
   __DATA.__objc_classrefs: 0x298
   __DATA.__objc_superrefs: 0x120
-  __DATA.__objc_ivar: 0x594
+  __DATA.__objc_ivar: 0x598
   __DATA.__data: 0xb08
   __DATA.__common: 0x10
-  __DATA.__bss: 0x280
+  __DATA.__bss: 0x290
   __DATA_DIRTY.__const: 0x388
   __DATA_DIRTY.__objc_const: 0x1270
   __DATA_DIRTY.__objc_data: 0xd20

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1484
-  Symbols:   5557
-  CStrings:  2590
+  Functions: 1492
+  Symbols:   5582
+  CStrings:  2599
 
Symbols:
+ -[SCROBrailleDisplayAutoDetector _addBLEPeripheral:central:].cold.1
+ -[SCROBrailleDisplayManager _enableAutoDetect].cold.1
+ -[SCROBrailleDisplayManager _updateTactileGraphicsDisplay]
+ GCC_except_table290
+ GCC_except_table31
+ GCC_except_table332
+ GCC_except_table34
+ GCC_except_table39
+ GCC_except_table66
+ _CFNotificationCenterAddObserver
+ _OBJC_IVAR_$_SCROBrailleDisplayAutoDetector._connectedPeripherals
+ _OBJC_IVAR_$_SCROBrailleDisplayManager._tactileGraphicsDisplayIdentifier
+ ___getkAXSVoiceOverTouchTactileGraphicsDisplayChangedNotificationSymbolLoc_block_invoke
+ __handleTactileGraphicsSettingsChange
+ _getkAXSVoiceOverTouchTactileGraphicsDisplayChangedNotificationSymbolLoc.ptr
+ _libAccessibilityLibrary
+ _libAccessibilityLibrary.cold.1
+ _objc_msgSend$_updateTactileGraphicsDisplay
+ _objc_msgSend$isBluetoothLowEnergy
+ _objc_msgSend$removeAutodetectBLEIdentifier:
- GCC_except_table288
- GCC_except_table330
- GCC_except_table37
- GCC_except_table64
- _OBJC_IVAR_$_SCROBrailleDisplayAutoDetector._connectedPeripheral
- ___get_AXSVoiceOverTouchCopyTactileGraphicsDisplaySymbolLoc_block_invoke.cold.1
- ___get_AXSVoiceOverTouchSetTactileGraphicsDisplaySymbolLoc_block_invoke.cold.1
CStrings:
+ "\a\x892\x11"
+ "Auto detect BTLE devices: %@"
+ "Braille display loaded: will notify: %@, will save: %@"
+ "CFStringRef getkAXSVoiceOverTouchTactileGraphicsDisplayChangedNotification(void)"
+ "Checking peripheral %@"
+ "Death timer firing: %@"
+ "Did connect periperhal: %@"
+ "Posting server timeout"
+ "Removing old tactile graphics display: %@"
+ "Updating tactile graphics from notification"
+ "_connectedPeripherals"
+ "_tactileGraphicsDisplayIdentifier"
+ "_updateTactileGraphicsDisplay"
+ "kAXSVoiceOverTouchTactileGraphicsDisplayChangedNotification"
- "\a\x891\x11"
- "Auto detect dot pad: %@"
- "Braille display loaded: will notify: %@"
- "Checking periperhal %@"
- "_connectedPeripheral"

```
