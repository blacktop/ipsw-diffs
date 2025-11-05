## com.apple.DriverKit-IOUserDockChannelSerial

> `/System/Library/DriverExtensions/com.apple.DriverKit-IOUserDockChannelSerial.dext/com.apple.DriverKit-IOUserDockChannelSerial`

```diff

-178.60.8.0.0
-  __TEXT.__text: 0x16fc
-  __TEXT.__auth_stubs: 0x260
+205.0.0.0.0
+  __TEXT.__text: 0x2038
+  __TEXT.__auth_stubs: 0x2b0
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x137
-  __TEXT.__unwind_info: 0xc0
+  __TEXT.__cstring: 0x229
+  __TEXT.__unwind_info: 0xd8
   __TEXT.__oslogstring: 0x34e
-  __DATA_CONST.__auth_got: 0x130
+  __DATA_CONST.__auth_got: 0x158
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x350
+  __DATA_CONST.__const: 0x390
   __DATA_CONST.__osclassinfo: 0x10
   __DATA.__common: 0x10
   - /System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit
   - /System/DriverKit/System/Library/Frameworks/SerialDriverKit.framework/SerialDriverKit
   - /System/DriverKit/usr/lib/libc++.dylib
-  UUID: E4D1CBB1-4481-3F0E-941F-12C54EEDDDBE
-  Functions: 32
-  Symbols:   97
-  CStrings:  28
+  UUID: 3E3A97E1-C224-3937-B3EB-2E5069E83CAD
+  Functions: 37
+  Symbols:   107
+  CStrings:  36
 
Symbols:
+ _OSDictionarySetValue
+ __ZN18IOUserPseudoSerial17withNameAndSuffixEP9IOServicePKcS3_hh
+ __ZN23IOUserDockChannelSerial22CreatePseudoTerminalV2ER37DockChannelPseudoTerminalPropertiesV2
+ __ZN23IOUserDockChannelSerial23DestroyPseudoTerminalV2ER37DockChannelPseudoTerminalPropertiesV2
+ __ZN23IOUserDockChannelSerial28CombinedNameFromPropertiesV2ER37DockChannelPseudoTerminalPropertiesV2
+ __ZN29IOUserDockChannelSerialClient16CreateTerminalV2EP8OSObjectPvP27IOUserClientMethodArguments
+ __ZN29IOUserDockChannelSerialClient17DestroyTerminalV2EP8OSObjectPvP27IOUserClientMethodArguments
+ __ZN8OSNumber10withNumberEym
+ __ZN9IOService13SetPropertiesEP12OSDictionaryPFiP15OSMetaClassBase5IORPCE
+ _strlcat
+ _strlcpy
- __ZN18IOUserPseudoSerial8withNameEP9IOServicePKchh
CStrings:
+ "CreateTerminalV2"
+ "DestroyTerminalV2"
+ "IOUserDockChannelSerialMajorVersion"
+ "IOUserDockChannelSerialMinorVersion"
+ "IOUserDockChannelSerialNexusID"
+ "IOUserDockChannelSerialNexusLocation"
+ "IOUserDockChannelSerialPortID"
+ "IOUserDockChannelSerialPortLocation"

```
