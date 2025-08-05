## AudioServerDriverTransports_Base

> `/System/Library/PrivateFrameworks/AudioServerDriverTransports_Base.framework/AudioServerDriverTransports_Base`

```diff

-300.70.0.0.0
-  __TEXT.__text: 0x3fb90
+300.71.0.0.0
+  __TEXT.__text: 0x3fd78
   __TEXT.__auth_stubs: 0xe60
-  __TEXT.__objc_methlist: 0x33f4
-  __TEXT.__gcc_except_tab: 0x6370
+  __TEXT.__objc_methlist: 0x3404
+  __TEXT.__gcc_except_tab: 0x63c4
   __TEXT.__const: 0x50e
-  __TEXT.__cstring: 0x1400
-  __TEXT.__oslogstring: 0x2fde
-  __TEXT.__unwind_info: 0x2008
+  __TEXT.__cstring: 0x1413
+  __TEXT.__oslogstring: 0x2fff
+  __TEXT.__unwind_info: 0x1ff8
   __TEXT.__objc_classname: 0x6a1
-  __TEXT.__objc_methname: 0x6e71
+  __TEXT.__objc_methname: 0x6ea1
   __TEXT.__objc_methtype: 0x1013
   __TEXT.__objc_stubs: 0x6560
   __DATA_CONST.__got: 0x2b8
-  __DATA_CONST.__const: 0x758
+  __DATA_CONST.__const: 0x760
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xa8

   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__auth_got: 0x748
   __AUTH_CONST.__const: 0x450
-  __AUTH_CONST.__cfstring: 0x18e0
+  __AUTH_CONST.__cfstring: 0x1900
   __AUTH_CONST.__objc_const: 0x5200
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B2D689AD-369A-3A6F-92E8-BCD1253477BA
+  UUID: 559306A1-A017-3BEE-A3DC-BEF371ED8A41
   Functions: 1681
-  Symbols:   5698
-  CStrings:  2298
+  Symbols:   5697
+  CStrings:  2302
 
Symbols:
+ +[ASDTExclavesStatusProperty config]
+ -[ASDTAudioDevice exclavesSensorName]
+ -[ASDTAudioDevice setExclavesSensorName:]
+ -[NSDictionary(ASDTConfig) asdtExclavesSensorName]
+ _OBJC_IVAR_$_ASDTAudioDevice._exclavesSensorName
+ _kASDTConfigKeyDeviceExclavesSensorName
+ _objc_msgSend$asdtExclavesSensorName
+ _objc_msgSend$exclavesSensorName
+ _objc_msgSend$setExclavesSensorName:
- +[ASDTExclavesSensorManager forMic]
- -[ASDTExclavesStatusProperty initWithConfig:].cold.1
- -[ASDTExclavesStatusProperty sensorName]
- -[ASDTExclavesStatusProperty setSensorName:]
- _OBJC_IVAR_$_ASDTExclavesStatusProperty._sensorName
- _objc_msgSend$forMic
- _objc_msgSend$sensorName
- _objc_msgSend$setSensorName:
CStrings:
+ "%@:%@: Bad sensor name!"
+ "%@:%@: Failed to start with bad sensor name: %@"
+ "%@:%@: Using sensor: %@"
+ "300.71"
+ "ExclavesSensorName"
+ "T@\"NSString\",&,N,V_exclavesSensorName"
+ "_exclavesSensorName"
+ "asdtExclavesSensorName"
+ "exclavesSensorName"
+ "setExclavesSensorName:"
- "300.70"
- "ASDTExclavesStatusProperty: The sensor name must be specified."
- "T@\"NSString\",&,N,V_sensorName"
- "_sensorName"
- "forMic"
- "sensorName"
- "setSensorName:"

```
