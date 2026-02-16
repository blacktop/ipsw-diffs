## ExternalAccessory

> `/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory`

```diff

-456.0.0.0.0
-  __TEXT.__text: 0xe424
-  __TEXT.__auth_stubs: 0x940
+458.100.1.0.0
+  __TEXT.__text: 0xe548
+  __TEXT.__auth_stubs: 0x920
   __TEXT.__objc_methlist: 0x15ec
-  __TEXT.__cstring: 0x53b1
+  __TEXT.__cstring: 0x54ec
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x8c
   __TEXT.__dlopen_cstrs: 0x5c
-  __TEXT.__unwind_info: 0x490
+  __TEXT.__unwind_info: 0x498
   __TEXT.__objc_classname: 0x13a
-  __TEXT.__objc_methname: 0x4178
+  __TEXT.__objc_methname: 0x4132
   __TEXT.__objc_methtype: 0x78e
   __TEXT.__objc_stubs: 0x2ae0
   __DATA_CONST.__got: 0x308

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xfb0
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x4b8
+  __AUTH_CONST.__auth_got: 0x4a8
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x3560
   __AUTH_CONST.__objc_const: 0x1f50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 354F639A-9479-3DEE-B5F3-2FC463D0A724
+  UUID: BE642DB6-226B-3B69-8D91-27ACAFB25EA8
   Functions: 468
-  Symbols:   2003
-  CStrings:  1697
+  Symbols:   2001
+  CStrings:  1698
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_setProperty_nonatomic
- _objc_setProperty_nonatomic_copy
CStrings:
+ "/Library/Caches/com.apple.xbs/1FF1DE66-A96C-4CCD-B916-24EC22826794/TemporaryDirectory.bnuv8k/Sources/ExternalAccessory/EAAccessory.mm"
+ "/Library/Caches/com.apple.xbs/1FF1DE66-A96C-4CCD-B916-24EC22826794/TemporaryDirectory.bnuv8k/Sources/ExternalAccessory/EAAccessoryManager.m"
+ "/Library/Caches/com.apple.xbs/1FF1DE66-A96C-4CCD-B916-24EC22826794/TemporaryDirectory.bnuv8k/Sources/ExternalAccessory/EAInputStream.m"
+ "/Library/Caches/com.apple.xbs/1FF1DE66-A96C-4CCD-B916-24EC22826794/TemporaryDirectory.bnuv8k/Sources/ExternalAccessory/EAOutputStream.m"
+ "/Library/Caches/com.apple.xbs/1FF1DE66-A96C-4CCD-B916-24EC22826794/TemporaryDirectory.bnuv8k/Sources/ExternalAccessory/EASession.m"
+ "T@\"<EAAccessoryDelegate>\",V_delegate"
+ "T@\"NSArray\",&,V_cameraComponents"
+ "T@\"NSArray\",&,V_eqNames"
+ "T@\"NSArray\",R"
+ "T@\"NSData\",C,V_certData"
+ "T@\"NSData\",C,V_certSerial"
+ "T@\"NSDictionary\",&,V_audioPorts"
+ "T@\"NSDictionary\",&,V_protocols"
+ "T@\"NSDictionary\",&,V_vehicleInfoInitialData"
+ "T@\"NSDictionary\",&,V_vehicleInfoSupportedTypes"
+ "T@\"NSDictionary\",C,V_protocolDetails"
+ "T@\"NSMutableArray\",&,V_enqueuedNMEASentences"
+ "T@\"NSMutableArray\",&,V_enqueuedNMEATimestamps"
+ "T@\"NSNumber\",&,V_averageFrameworkDelay"
+ "T@\"NSNumber\",&,V_averageXPCDelay"
+ "T@\"NSNumber\",&,V_highestFrameworkDelay"
+ "T@\"NSNumber\",&,V_highestXPCDelay"
+ "T@\"NSString\",C,V_bonjourName"
+ "T@\"NSString\",C,V_coreAccessoryPrimaryUUID"
+ "T@\"NSString\",C,V_dockType"
+ "T@\"NSString\",C,V_firmwareRevisionActive"
+ "T@\"NSString\",C,V_firmwareRevisionPending"
+ "T@\"NSString\",C,V_hardwareRevision"
+ "T@\"NSString\",C,V_macAddress"
+ "T@\"NSString\",C,V_manufacturer"
+ "T@\"NSString\",C,V_modelNumber"
+ "T@\"NSString\",C,V_name"
+ "T@\"NSString\",C,V_ppid"
+ "T@\"NSString\",C,V_preferredApp"
+ "T@\"NSString\",C,V_regionCode"
+ "T@\"NSString\",C,V_serialNumber"
+ "TB,V_connected"
+ "TB,V_hasIPConnection"
+ "TB,V_isAvailableOverBonjour"
+ "TB,V_notPresentInIAPAccessoriesArray"
+ "TI,V_capabilities"
+ "TI,V_connectionID"
+ "TI,V_eqIndex"
+ "TQ,V_nmeaSentenceAddCounter"
+ "TQ,V_nmeaSentenceGetCounter"
+ "Ti,V_classType"
+ "Ti,V_locationSentenceTypesMask"
+ "Tq,V_transportType"
- "/Library/Caches/com.apple.xbs/Sources/ExternalAccessory/EAAccessory.mm"
- "/Library/Caches/com.apple.xbs/Sources/ExternalAccessory/EAAccessoryManager.m"
- "/Library/Caches/com.apple.xbs/Sources/ExternalAccessory/EAInputStream.m"
- "/Library/Caches/com.apple.xbs/Sources/ExternalAccessory/EAOutputStream.m"
- "/Library/Caches/com.apple.xbs/Sources/ExternalAccessory/EASession.m"
- "T@\"<EAAccessoryDelegate>\",N,V_delegate"
- "T@\"NSArray\",&,N,V_cameraComponents"
- "T@\"NSArray\",&,N,V_eqNames"
- "T@\"NSData\",C,N,V_certData"
- "T@\"NSData\",C,N,V_certSerial"
- "T@\"NSDictionary\",&,N,V_audioPorts"
- "T@\"NSDictionary\",&,N,V_protocols"
- "T@\"NSDictionary\",&,N,V_vehicleInfoInitialData"
- "T@\"NSDictionary\",&,N,V_vehicleInfoSupportedTypes"
- "T@\"NSDictionary\",C,N,V_protocolDetails"
- "T@\"NSMutableArray\",&,N,V_enqueuedNMEASentences"
- "T@\"NSMutableArray\",&,N,V_enqueuedNMEATimestamps"
- "T@\"NSNumber\",&,N,V_averageFrameworkDelay"
- "T@\"NSNumber\",&,N,V_averageXPCDelay"
- "T@\"NSNumber\",&,N,V_highestFrameworkDelay"
- "T@\"NSNumber\",&,N,V_highestXPCDelay"
- "T@\"NSString\",C,N,V_bonjourName"
- "T@\"NSString\",C,N,V_coreAccessoryPrimaryUUID"
- "T@\"NSString\",C,N,V_dockType"
- "T@\"NSString\",C,N,V_firmwareRevisionActive"
- "T@\"NSString\",C,N,V_firmwareRevisionPending"
- "T@\"NSString\",C,N,V_hardwareRevision"
- "T@\"NSString\",C,N,V_macAddress"
- "T@\"NSString\",C,N,V_manufacturer"
- "T@\"NSString\",C,N,V_modelNumber"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",C,N,V_ppid"
- "T@\"NSString\",C,N,V_preferredApp"
- "T@\"NSString\",C,N,V_regionCode"
- "T@\"NSString\",C,N,V_serialNumber"
- "TB,N,V_connected"
- "TB,N,V_hasIPConnection"
- "TB,N,V_isAvailableOverBonjour"
- "TB,N,V_notPresentInIAPAccessoriesArray"
- "TI,N,V_capabilities"
- "TI,N,V_connectionID"
- "TI,N,V_eqIndex"
- "TQ,N,V_nmeaSentenceAddCounter"
- "TQ,N,V_nmeaSentenceGetCounter"
- "Ti,N,V_classType"
- "Ti,N,V_locationSentenceTypesMask"
- "Tq,N,V_transportType"

```
