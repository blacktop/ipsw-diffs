## scrod

> `/System/Library/CoreServices/VoiceOverTouch.app/scrod`

```diff

-283.0.0.0.0
-  __TEXT.__text: 0xaa80
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_stubs: 0x19e0
-  __TEXT.__objc_methlist: 0x5f4
+285.0.2.0.0
+  __TEXT.__text: 0xb878
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_stubs: 0x1a20
+  __TEXT.__objc_methlist: 0x5fc
   __TEXT.__cstring: 0x36c
   __TEXT.__const: 0x20
-  __TEXT.__objc_methname: 0x1bf6
-  __TEXT.__oslogstring: 0x9cb
+  __TEXT.__objc_methname: 0x1c16
+  __TEXT.__oslogstring: 0x1105
   __TEXT.__objc_classname: 0x138
   __TEXT.__objc_methtype: 0x3d7
-  __TEXT.__gcc_except_tab: 0x614
-  __TEXT.__unwind_info: 0x2f0
-  __DATA_CONST.__auth_got: 0x390
+  __TEXT.__gcc_except_tab: 0x6a8
+  __TEXT.__unwind_info: 0x2f8
+  __DATA_CONST.__auth_got: 0x398
   __DATA_CONST.__got: 0x230
   __DATA_CONST.__const: 0x298
   __DATA_CONST.__cfstring: 0x1a0

   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xec8
-  __DATA.__objc_selrefs: 0x828
+  __DATA.__objc_selrefs: 0x838
   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0x100
   __DATA.__objc_superrefs: 0x30

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 37578599-14AC-38C7-9D41-ED04CE2F9A02
-  Functions: 157
-  Symbols:   225
-  CStrings:  500
+  UUID: 9ED28960-F713-34B1-9E98-CC3B6770F597
+  Functions: 158
+  Symbols:   226
+  CStrings:  531
 
Symbols:
+ _objc_retain_x28
CStrings:
+ "Braille driver load succeeded: %@ in _reloadDriver"
+ "Braille driver load succeeded: %@ in processInitiaDeviceConnectionCallback"
+ "Call _removeBluetoothDriverWithIOElement for Display: %@"
+ "Connected and loaded: driverLoadReturn %@, loadSucceeded %@ (BT result: %@) for Display %@"
+ "Disconnecting device %@ because reconnection is not enabled[%@], (HID: %@), (Invalid: %@)"
+ "Display invalid: returning from _processInitialDeviceConnectionCallback"
+ "FAILED: Add device failed: Reset reconnect %@ [%{public}@] - %{public}@"
+ "In _delayedHandleSystemSleep: remove certain drivers in _displays: %@"
+ "In _loadBluetoothDriverFromPreferences: _displays = %@"
+ "Load succeeded and Valid: setting up driver and starting the event processor."
+ "Load succeeded: informing the manager of our progress."
+ "Reconnection enabled: trying again (fail %@) %@ is HID %@, Is invalid: %@"
+ "SUCCESS: Connection success for display [%{public}@] - %{public}@ valid: %@"
+ "Should reload: %@ required service: %@ service connected: %@, connected services: %@, device: %p"
+ "Turning off _isDriverLoading"
+ "_addToDisplays:"
+ "_brailleDriver == nil in _reconnectionEventHandler for Display %p"
+ "_brailleDriver == nil in _reloadDriver for Display %@"
+ "_brailleDriver == nil in _runThread for %p"
+ "_brailleDriver == nil in _setupDriverSupport for Display %p"
+ "_brailleDriver set to %@ in _processDeviceConnectionCallback for Display %p"
+ "_brailleDriver set to %@ in _processInitialDeviceConnectionCallback for Display %p"
+ "_brailleDriver set to %@ in _reloadDriver for Display %p"
+ "_brailleDriver set to nil (from %p) in _reloadDriver for Display %p"
+ "_brailleDriver set to nil in invalidate for Display %p"
+ "_initWithDriver call with driver: %@, driverIdentifier: %@, display: %p"
+ "_isDriverLoading set to NO in _processDeviceConnectionCallback"
+ "_isDriverLoading set to NO in _processInitialDeviceConnectionCallback"
+ "_isDriverLoading set to NO in _reloadDriver"
+ "_isDriverLoading set to YES in _delayedRemoveDeviceNotification"
+ "_isDriverLoading set to YES in _reconnectionEventHandler"
+ "_isDriverLoading set to YES in _reloadDriver"
+ "_isDriverLoading set to YES in _runThread"
+ "brailleDriver == nil in _processDeviceConnectionCallback"
+ "brailleDriver == nil in _processInitialDeviceConnectionCallback for %p"
+ "loadingDisplays"
- "Connected and loaded: %@ = %@ (BT result: %@)"
- "Disconnecting device because reconnection is not enabled[%@], (HID: %@), (Invalid: %@) [%{public}@]"
- "FAILED: Add device failed: Reset reconnect [%{public}@] - %{public}@"
- "Reconnection enabled: trying again (fail %@) %@ is HID %@"
- "SUCCESS: Connection success for display [%{public}@] - %{public}@"

```
