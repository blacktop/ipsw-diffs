## sensorkitd

> `/usr/libexec/sensorkitd`

```diff

-707.0.47.0.0
-  __TEXT.__text: 0x40040
+756.0.25.0.0
+  __TEXT.__text: 0x407b4
   __TEXT.__auth_stubs: 0xc40
-  __TEXT.__objc_stubs: 0x36e0
-  __TEXT.__objc_methlist: 0x1694
-  __TEXT.__objc_methname: 0x57df
-  __TEXT.__objc_classname: 0x894
-  __TEXT.__objc_methtype: 0x254b
-  __TEXT.__cstring: 0x2bf7
+  __TEXT.__objc_stubs: 0x37a0
+  __TEXT.__objc_methlist: 0x179c
+  __TEXT.__objc_methname: 0x5963
+  __TEXT.__objc_classname: 0x8de
+  __TEXT.__objc_methtype: 0x2617
+  __TEXT.__cstring: 0x2c91
   __TEXT.__oslogstring: 0x6a15
   __TEXT.__const: 0x34
   __TEXT.__gcc_except_tab: 0x618
-  __TEXT.__unwind_info: 0x9c0
+  __TEXT.__unwind_info: 0x9f0
   __DATA_CONST.__auth_got: 0x630
   __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0xfd0
-  __DATA_CONST.__cfstring: 0x2fc0
-  __DATA_CONST.__objc_classlist: 0x1b8
-  __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x168
+  __DATA_CONST.__const: 0xfb8
+  __DATA_CONST.__cfstring: 0x3080
+  __DATA_CONST.__objc_classlist: 0x1c0
+  __DATA_CONST.__objc_catlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x4c8
+  __DATA_CONST.__objc_protorefs: 0x60
+  __DATA_CONST.__objc_classrefs: 0x330
+  __DATA_CONST.__objc_superrefs: 0x198
+  __DATA_CONST.__objc_intobj: 0x4b0
   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA.__objc_const: 0x7008
-  __DATA.__objc_selrefs: 0x1020
-  __DATA.__objc_protorefs: 0x60
-  __DATA.__objc_classrefs: 0x328
-  __DATA.__objc_superrefs: 0x190
-  __DATA.__objc_ivar: 0x3ec
-  __DATA.__objc_data: 0x1130
-  __DATA.__data: 0x10e8
-  __DATA.__bss: 0x1c8
+  __DATA.__objc_const: 0x72c0
+  __DATA.__objc_selrefs: 0x1080
+  __DATA.__objc_ivar: 0x3fc
+  __DATA.__objc_data: 0x1180
+  __DATA.__data: 0x11a8
+  __DATA.__bss: 0x1e0
   __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 788
+  Functions: 806
   Symbols:   324
-  CStrings:  2160
+  CStrings:  2200
 
CStrings:
+ "%@ (%p)"
+ "%@ (%p): from: %f, to: %f, cursor: %@, %@"
+ "%@ (%p): name: %@, authService: %@, writer: %@, relatedSettings: %@, publicEntitlement: %@, sampleClass: %@, exportingSampleClass: %@, additions: %@, onDemandWriterId: %@, writerAuthService: %@, supportedPlatforms: %@, auth store cohort: %@, legacyName: %@, filters: %@, legacySampleClass: %@, legacySampleClassLinkedBefore: %u, roundingInterval: %f, eligibleDaemons: %@, storageBackend: %ld"
+ "@\"NSData\""
+ "@\"NSString\"24@0:8@\"NSXPCConnection\"16"
+ "@\"SRCursor\""
+ "@\"SRCursor\"16@0:8"
+ "@24@0:8^{_NSZone=}16"
+ "@32@0:8#16^@24"
+ "@32@0:8@\"NSString\"16@\"NSXPCConnection\"24"
+ "Cursor"
+ "NSCopying"
+ "NSXPCConnection+Valdiation"
+ "SRConnectionValueProving"
+ "SRCursor"
+ "StorageBackend"
+ "T@\"NSString\",?,R,C"
+ "T@\"SRCursor\",&,N"
+ "T@\"SRCursor\",&,N,V_cursor"
+ "Tq,R,N,V_datastoreBackend"
+ "Validation"
+ "_PayloadInspection"
+ "_cursor"
+ "_datastoreBackend"
+ "_hmac"
+ "_payload"
+ "_payloadOfClass:error:"
+ "_sr_hasEntitlement:sensor:valueProvider:"
+ "com.apple.SensorKit.ECG"
+ "com.apple.SensorKit.PPG"
+ "com.apple.private.sensorkit.auth.request.arbitrary_bundle"
+ "copyWithZone:"
+ "cursor"
+ "datastoreBackend"
+ "fetchAllDevices:reply:"
+ "fetchDeviceInformationForDeviceIdentifiers:reply:"
+ "hmac"
+ "isAuthorizedForSensor:bundleIdentifier:"
+ "isEqualToData:"
+ "new"
+ "payload"
+ "setCursor:"
+ "sr_hasHoldingPeriodBypassEntitlement:"
+ "v24@0:8@\"SRCursor\"16"
+ "v32@0:8@\"<SRRequestReading>\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "%@ (%p): from: %f, to: %f, %@"
- "%@ (%p): name: %@, authService: %@, writer: %@, relatedSettings: %@, publicEntitlement: %@, sampleClass: %@, exportingSampleClass: %@, additions: %@, onDemandWriterId: %@, writerAuthService: %@, supportedPlatforms: %@, auth store cohort: %@, legacyName: %@, filters: %@, legacySampleClass: %@, legacySampleClassLinkedBefore: %u, roundingInterval: %f, eligibleDaemons; %@"
- "com.apple.private.SensorKit.ECG"
- "com.apple.private.SensorKit.PPG"
- "fetchAllDevices:idOnly:reply:"
- "v36@0:8@\"<SRRequestReading>\"16B24@?<v@?@\"NSArray\"@\"NSError\">28"
- "v36@0:8@16B24@?28"

```
