## com.apple.DriverKit-IOUserDockChannelSerial

> `/System/Library/DriverExtensions/com.apple.DriverKit-IOUserDockChannelSerial.dext/com.apple.DriverKit-IOUserDockChannelSerial`

```diff

-205.0.0.0.0
-  __TEXT.__text: 0x2038
-  __TEXT.__auth_stubs: 0x2b0
+208.120.5.0.0
+  __TEXT.__text: 0x260c
+  __TEXT.__auth_stubs: 0x330
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x229
-  __TEXT.__unwind_info: 0xd8
-  __TEXT.__oslogstring: 0x34e
-  __DATA_CONST.__auth_got: 0x158
-  __DATA_CONST.__got: 0x30
+  __TEXT.__cstring: 0x23c
+  __TEXT.__unwind_info: 0xf0
+  __TEXT.__oslogstring: 0x37f
+  __DATA_CONST.__auth_got: 0x198
+  __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x390
   __DATA_CONST.__osclassinfo: 0x10
   __DATA.__common: 0x10
   - /System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit
   - /System/DriverKit/System/Library/Frameworks/SerialDriverKit.framework/SerialDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 37
-  Symbols:   107
-  CStrings:  36
+  Functions: 45
+  Symbols:   125
+  CStrings:  38
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _ZN23IOUserDockChannelSerial21DestroyPseudoTerminalEP29IOUserDockChannelSerialClientR35DockChannelPseudoTerminalProperties.cold.1
+ _ZN23IOUserDockChannelSerial23DestroyPseudoTerminalV2EP29IOUserDockChannelSerialClientR37DockChannelPseudoTerminalPropertiesV2.cold.1
+ __ZN23IOUserDockChannelSerial19ErasePseudoTerminalEP29IOUserDockChannelSerialClientP8OSStringb
+ __ZN23IOUserDockChannelSerial20CreatePseudoTerminalEP29IOUserDockChannelSerialClientR35DockChannelPseudoTerminalProperties
+ __ZN23IOUserDockChannelSerial20InsertPseudoTerminalEP29IOUserDockChannelSerialClientP8OSStringP18IOUserPseudoSerial
+ __ZN23IOUserDockChannelSerial21DestroyPseudoTerminalEP29IOUserDockChannelSerialClientR35DockChannelPseudoTerminalProperties
+ __ZN23IOUserDockChannelSerial22CreatePseudoTerminalV2EP29IOUserDockChannelSerialClientR37DockChannelPseudoTerminalPropertiesV2
+ __ZN23IOUserDockChannelSerial23DestroyPseudoTerminalV2EP29IOUserDockChannelSerialClientR37DockChannelPseudoTerminalPropertiesV2
+ __ZN23IOUserDockChannelSerial25CheckForTerminalExistenceEP29IOUserDockChannelSerialClientP8OSString
+ __ZN23IOUserDockChannelSerial26ExterminatePseudoTerminalsEP29IOUserDockChannelSerialClient
+ __ZN23IOUserDockChannelSerial35ExterminatePseudoAllClientTerminalsEv
+ __ZN29IOUserDockChannelSerialClient18ClientCrashed_ImplEP9IOServicey
+ __ZN7OSArray12removeObjectEj
+ __ZN7OSArray12withCapacityEj
+ __ZN7OSArray9setObjectEPK15OSMetaClassBase
+ __ZN7OSArray9setObjectEjPK15OSMetaClassBase
+ __ZN9IOService20ClientCrashed_InvokeE5IORPCP15OSMetaClassBasePFiS2_PS_yE
+ __ZNK7OSArray13getLastObjectEv
+ __ZNK7OSArray20getNextIndexOfObjectEPK15OSMetaClassBasej
+ __ZNK7OSArray9getObjectEj
+ ____ZN23IOUserDockChannelSerial19ErasePseudoTerminalEP29IOUserDockChannelSerialClientP8OSStringb_block_invoke
+ _gOSDictionaryMetaClass
- __ZN23IOUserDockChannelSerial20CreatePseudoTerminalER35DockChannelPseudoTerminalProperties
- __ZN23IOUserDockChannelSerial21DestroyPseudoTerminalER35DockChannelPseudoTerminalProperties
- __ZN23IOUserDockChannelSerial22CreatePseudoTerminalV2ER37DockChannelPseudoTerminalPropertiesV2
- __ZN23IOUserDockChannelSerial23DestroyPseudoTerminalV2ER37DockChannelPseudoTerminalPropertiesV2
- __ZN23IOUserDockChannelSerial26ExterminatePseudoTerminalsEv
- ____ZN23IOUserDockChannelSerial26ExterminatePseudoTerminalsEv_block_invoke
CStrings:
+ "ClientCrashed_Impl"
+ "IOUserDockChannelSerialClient::%s client crashed"

```
