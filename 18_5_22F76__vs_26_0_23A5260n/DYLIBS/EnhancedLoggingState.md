## EnhancedLoggingState

> `/System/Library/PrivateFrameworks/EnhancedLoggingState.framework/EnhancedLoggingState`

```diff

-70.0.0.0.0
-  __TEXT.__text: 0x85e0
+83.0.0.0.0
+  __TEXT.__text: 0x8eb0
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0xb34
+  __TEXT.__objc_methlist: 0xb9c
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x14c5
+  __TEXT.__cstring: 0x16f7
   __TEXT.__gcc_except_tab: 0xe0
-  __TEXT.__oslogstring: 0x3f6
+  __TEXT.__oslogstring: 0x40b
   __TEXT.__dlopen_cstrs: 0xd8
-  __TEXT.__unwind_info: 0x228
-  __TEXT.__objc_classname: 0xfb
-  __TEXT.__objc_methname: 0x1f67
+  __TEXT.__unwind_info: 0x230
+  __TEXT.__objc_classname: 0xfc
+  __TEXT.__objc_methname: 0x2093
   __TEXT.__objc_methtype: 0x5eb
-  __TEXT.__objc_stubs: 0x1820
+  __TEXT.__objc_stubs: 0x1920
   __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x4b8
+  __DATA_CONST.__const: 0x530
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x890
+  __DATA_CONST.__objc_selrefs: 0x8d8
   __DATA_CONST.__objc_superrefs: 0x38
   __AUTH_CONST.__auth_got: 0x250
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x1be0
-  __AUTH_CONST.__objc_const: 0x1178
+  __AUTH_CONST.__cfstring: 0x1f40
+  __AUTH_CONST.__objc_const: 0x11d8
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0xa8
+  __DATA.__objc_ivar: 0xb0
   __DATA.__data: 0x1e0
   __DATA.__bss: 0xc0
   __DATA_DIRTY.__objc_data: 0xa0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 742D79F2-B1CA-3F76-B3C9-499544E64A73
-  Functions: 223
-  Symbols:   1023
-  CStrings:  943
+  UUID: 639DB4B2-2028-340F-B4A1-F05EF4955105
+  Functions: 232
+  Symbols:   1065
+  CStrings:  1011
 
Symbols:
+ -[ELSManager commitDeviceSelectionMap:]
+ -[ELSManager commitSessionIDTransaction:]
+ -[ELSSnapshot dedSessionIdentifierForRemoteDeviceIdentifier:]
+ -[ELSSnapshot deviceSelection]
+ -[ELSSnapshot refreshDeviceSelectionMap]
+ -[ELSSnapshot refreshSessionID]
+ -[ELSSnapshot sessionID]
+ -[ELSSnapshot setDeviceSelection:]
+ -[ELSSnapshot setSessionID:]
+ GCC_except_table38
+ _ELSDefaultDeviceSelectionMap
+ _ELSDefaultSessionID
+ _ELSDeviceSelectionMapRequirementTypeKey
+ _ELSDeviceSelectionMapSelectionKey
+ _ELSDeviceSelectionMultiple
+ _ELSDeviceSelectionRequirementTypeOptional
+ _ELSDeviceSelectionRequirementTypeRequired
+ _ELSDeviceSelectionRequirementTypeRequiredWhenOrigin
+ _ELSDeviceSelectionSingle
+ _ELSMetadataDeviceClassIdentifier
+ _ELSMetadataOriginDeviceSerialNumber
+ _ELSMetadataOriginDeviceType
+ _ELSParameterDeviceSelection
+ _ELSSessionIdentifierPrefix
+ _OBJC_IVAR_$_ELSSnapshot._deviceSelection
+ _OBJC_IVAR_$_ELSSnapshot._sessionID
+ _objc_msgSend$commitDeviceSelectionMap:
+ _objc_msgSend$commitSessionIDTransaction:
+ _objc_msgSend$deviceSelection
+ _objc_msgSend$refreshDeviceSelectionMap
+ _objc_msgSend$refreshSessionID
+ _objc_msgSend$sessionID
+ _objc_msgSend$setDeviceSelection:
+ _objc_msgSend$setSessionID:
- GCC_except_table36
CStrings:
+ "%@-%@"
+ "ENHANCED_LOGGING_BT_HEADSET"
+ "ENHANCED_LOGGING_HDS"
+ "ENHANCED_LOGGING_HEART_RATE_COORDINATOR"
+ "ENHANCED_LOGGING_MEGAWIFI"
+ "Follow-Up Question"
+ "Snapshot updated: %@"
+ "T@\"NSDictionary\",&,N,V_deviceSelection"
+ "T@\"NSString\",&,N,V_sessionID"
+ "_deviceSelection"
+ "_sessionID"
+ "bt_headset"
+ "com.apple.DiagnosticExtensions.BluetoothHeadset"
+ "com.apple.HDSViewService.HDSDiagnostics"
+ "com.apple.HealthLite.PPGSensorDiagnosticExtension"
+ "com.apple.HeartRateCoordinator.HRCDiagnosticExtension"
+ "com.apple.wifi.WiFiLogCapture.MegaWiFiDiagnosticExtension"
+ "commitDeviceSelectionMap:"
+ "commitSessionIDTransaction:"
+ "dedSessionIdentifierForRemoteDeviceIdentifier:"
+ "deviceClassIdentifier"
+ "deviceSelection"
+ "els"
+ "hdsdiagnose"
+ "hid_heart_rate_coordinator"
+ "megawifi"
+ "multi"
+ "optional"
+ "originDeviceSerialNumber"
+ "originDeviceType"
+ "refreshDeviceSelectionMap"
+ "refreshSessionID"
+ "required"
+ "requiredIfOrigin"
+ "requirementType"
+ "selection"
+ "sessionID"
+ "setDeviceSelection:"
+ "setSessionID:"
+ "single"
- "com.apple.AppleElementsSupport.AppleElementsDiagnostic"

```
