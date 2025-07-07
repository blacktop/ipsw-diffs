## heartratecoordinatord

> `/usr/libexec/heartratecoordinatord`

```diff

-17.0.0.0.0
-  __TEXT.__text: 0x1b728
-  __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_stubs: 0x2de0
-  __TEXT.__objc_methlist: 0x1414
+19.0.0.0.0
+  __TEXT.__text: 0x1bfb0
+  __TEXT.__auth_stubs: 0x7a0
+  __TEXT.__objc_stubs: 0x2e40
+  __TEXT.__objc_methlist: 0x13fc
   __TEXT.__const: 0x330
-  __TEXT.__oslogstring: 0x2f03
-  __TEXT.__cstring: 0xd51
-  __TEXT.__gcc_except_tab: 0x2528
-  __TEXT.__objc_methname: 0x3cbd
+  __TEXT.__oslogstring: 0x30af
+  __TEXT.__cstring: 0xde8
+  __TEXT.__gcc_except_tab: 0x285c
+  __TEXT.__objc_methname: 0x3d01
   __TEXT.__objc_classname: 0x387
-  __TEXT.__objc_methtype: 0x1541
-  __TEXT.__unwind_info: 0xd78
-  __DATA_CONST.__auth_got: 0x3c8
+  __TEXT.__objc_methtype: 0x1535
+  __TEXT.__unwind_info: 0xe00
+  __DATA_CONST.__auth_got: 0x3e0
   __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0xa38
-  __DATA_CONST.__cfstring: 0x980
+  __DATA_CONST.__const: 0xa70
+  __DATA_CONST.__cfstring: 0xaa0
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x24c0
-  __DATA.__objc_selrefs: 0xd50
-  __DATA.__objc_ivar: 0x1e4
+  __DATA.__objc_const: 0x24d0
+  __DATA.__objc_selrefs: 0xd60
+  __DATA.__objc_ivar: 0x1e8
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0x5a0
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x68
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/HeartRateCoordinator.framework/HeartRateCoordinator
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
+  - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D420D4DA-DABD-3B29-9751-9E40C60EE432
-  Functions: 721
-  Symbols:   192
-  CStrings:  1154
+  UUID: 58F9138A-1AD0-3C6F-86EA-390C347D35AB
+  Functions: 726
+  Symbols:   195
+  CStrings:  1178
 
Symbols:
+ _PPSCreateTelemetryIdentifier
+ _PPSSendTelemetry
+ _objc_retain_x4
CStrings:
+ "%{public}@ with uuid : %{public}@ requested opportunistic updates enabled : %d"
+ "%{public}@ with uuid : %{public}@ requested streaming mode : %lu"
+ "%{public}@ with uuid : %{public}@ updated workoutActivityType : %lu, locationType : %lu"
+ "@\"NSUUID\""
+ "HeartRateCoordinator"
+ "UUIDString"
+ "_clientIdentifier"
+ "a"
+ "clientConnection"
+ "clientState"
+ "collatedState"
+ "connection-identifier"
+ "numberWithBool:"
+ "opportunistic-mode"
+ "power telemetry :: client connection with name : %{public}@ , uuid : %{public}@, process-connected : %{public}d"
+ "power telemetry :: client snapshot with name : %{public}@ , uuid : %{public}@, streaming-mode : %{public}lu , opportunistic-mode : %{public}d"
+ "power telemetry :: collated snapshot with streaming-mode : %{public}lu , opportunistic-mode : %{public}d"
+ "process-connected"
+ "process-name"
+ "reportClientConnectionUpdate:"
+ "reportClientSnapshot"
+ "reportCollatedStateSnapshot"
+ "streaming-mode"
- "%{public}@ requested opportunistic updates enabled : %d"
- "%{public}@ requested streaming mode : %ld"
- "%{public}@ updated workoutActivityType : %lu, locationType : %lu"
- "_requestRemoval"
- "requestRemoval"
- "requestRemovalForClient:"
- "v24@0:8@\"HRCClient\"16"

```
