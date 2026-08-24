## CoreLocation

> `/System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation`

```diff

 3077.0.4.0.0
-  __TEXT.__text: 0x1d86b0
+  __TEXT.__text: 0x1d7a74
   __TEXT.__auth_stubs: 0x18d0
-  __TEXT.__objc_methlist: 0x996c
-  __TEXT.__const: 0x3b90
-  __TEXT.__gcc_except_tab: 0xe074
-  __TEXT.__oslogstring: 0x35f96
-  __TEXT.__cstring: 0x22dc2
+  __TEXT.__objc_methlist: 0x980c
+  __TEXT.__const: 0x3b80
+  __TEXT.__gcc_except_tab: 0xe04c
+  __TEXT.__oslogstring: 0x35f34
+  __TEXT.__cstring: 0x22bab
   __TEXT.__ustring: 0x1b0
-  __TEXT.__unwind_info: 0x5060
-  __TEXT.__objc_classname: 0x11cd
-  __TEXT.__objc_methname: 0x1aa45
-  __TEXT.__objc_methtype: 0x4850
-  __TEXT.__objc_stubs: 0xd5c0
-  __DATA_CONST.__got: 0x6e0
+  __TEXT.__unwind_info: 0x5030
+  __TEXT.__objc_classname: 0x119e
+  __TEXT.__objc_methname: 0x1a5f8
+  __TEXT.__objc_methtype: 0x480f
+  __TEXT.__objc_stubs: 0xd4a0
+  __DATA_CONST.__got: 0x6d8
   __DATA_CONST.__const: 0xcc0
-  __DATA_CONST.__objc_classlist: 0x4e8
+  __DATA_CONST.__objc_classlist: 0x4e0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4f28
+  __DATA_CONST.__objc_selrefs: 0x4e78
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x490
+  __DATA_CONST.__objc_superrefs: 0x488
   __DATA_CONST.__objc_arraydata: 0x70
   __AUTH_CONST.__auth_got: 0xc80
-  __AUTH_CONST.__const: 0x4880
-  __AUTH_CONST.__cfstring: 0xac20
-  __AUTH_CONST.__objc_const: 0x10dc0
+  __AUTH_CONST.__const: 0x4860
+  __AUTH_CONST.__cfstring: 0xaae0
+  __AUTH_CONST.__objc_const: 0x10b08
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH.__objc_data: 0x2c10
-  __DATA.__objc_ivar: 0xb54
+  __AUTH.__objc_data: 0x2bc0
+  __DATA.__objc_ivar: 0xb2c
   __DATA.__data: 0x758
   __DATA.__common: 0x60
   __DATA_DIRTY.__objc_ivar: 0x68

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4957
-  Symbols:   1050
-  CStrings:  9384
+  Functions: 4927
+  Symbols:   1046
+  CStrings:  9335
 
Symbols:
- _CFEqual
- _CLClientUpdateSCSessionState
- _OBJC_CLASS_$__CLVLLocalizationAuxiliaryInfo
- _OBJC_METACLASS_$__CLVLLocalizationAuxiliaryInfo
CStrings:
+ "<_CLVLLocalizationResult: %p> {\n%@.timestamp = %f,\n%@.location = {\n%@.coordinate = [%f, %f, %f],\n%@.horizontalAccuracy = %f\n%@},\n%@.transform = [%f, %f, %f, %f;\n%@%f, %f, %f, %f;\n%@%f, %f, %f, %f;\n%@%f, %f, %f, %f],\n%@.covariance = [%f, %f, %f, %f, %f, %f;\n%@%f, %f, %f, %f, %f, %f;\n%@%f, %f, %f, %f, %f, %f;\n%@%f, %f, %f, %f, %f, %f;\n%@%f, %f, %f, %f, %f, %f;\n%@%f, %f, %f, %f, %f, %f],\n%@.confidence = %f,\n%@.debugInfo = %@\n%@}"
- "<_CLVLLocalizationAuxiliaryInfo: %p> {\n%@.sensorLocation = %zd,\n%@.relativeAttitude = [%f, %f, %f, %f],\n%@.relativePosition = [%f, %f, %f],\n%@.relativePositionCovDiag = [%f, %f, %f],\n%@.relativeReferenceFrameId = %zd,\n%@.rotationCameraToImu = [%f, %f, %f, %f],\n%@.positionCameraInImu = [%f, %f, %f],\n%@.rotationImuToImu = [%f, %f, %f, %f]\n%@}"
- "<_CLVLLocalizationResult: %p> {\n%@.timestamp = %f,\n%@.location = {\n%@.coordinate = [%f, %f, %f],\n%@.horizontalAccuracy = %f\n%@},\n%@.transform = [%f, %f, %f, %f;\n%@%f, %f, %f, %f;\n%@%f, %f, %f, %f;\n%@%f, %f, %f, %f],\n%@.covariance = [%f, %f, %f, %f, %f, %f;\n%@%f, %f, %f, %f, %f, %f;\n%@%f, %f, %f, %f, %f, %f;\n%@%f, %f, %f, %f, %f, %f;\n%@%f, %f, %f, %f, %f, %f;\n%@%f, %f, %f, %f, %f, %f],\n%@.confidence = %f,\n%@.debugInfo = %@,\n%@.auxiliaryInfo = %@\n%@}"
- "@\"_CLVLLocalizationAuxiliaryInfo\""
- "@224@0:8q16245688q120128160192"
- "Could not serialize _CLSCSessionState"
- "T,N,V_positionCameraInImu"
- "T,N,V_relativeAttitude"
- "T,N,V_relativePosition"
- "T,N,V_relativePositionCovDiag"
- "T,N,V_rotationCameraToImu"
- "T,N,V_rotationImuToImu"
- "T@\"_CLVLLocalizationAuxiliaryInfo\",C,N,V_auxiliaryInfo"
- "Tq,N,V_relativeReferenceFrameId"
- "Tq,N,V_sensorLocation"
- "T{?=[4]},N,V_transformCameraToImu"
- "_CLSCExtensions"
- "_CLVLLocalizationAuxiliaryInfo"
- "_auxiliaryInfo"
- "_positionCameraInImu"
- "_relativeAttitude"
- "_relativePosition"
- "_relativePositionCovDiag"
- "_relativeReferenceFrameId"
- "_rotationCameraToImu"
- "_rotationImuToImu"
- "_sensorLocation"
- "_transformCameraToImu"
- "_updateSCSessionState:"
- "auxiliaryInfo"
- "initWithSensorLocation:relativeAttitude:relativePosition:relativePositionCovDiag:relativeReferenceFrameId:rotationCameraToImu:positionCameraInImu:rotationImuToImu:"
- "positionCameraInImu"
- "relativeAttitude"
- "relativePosition"
- "relativePositionCovDiag"
- "relativeReferenceFrameId"
- "rotationCameraToImu"
- "rotationImuToImu"
- "sensorLocation"
- "setAuxiliaryInfo:"
- "setPositionCameraInImu:"
- "setRelativeAttitude:"
- "setRelativePosition:"
- "setRelativePositionCovDiag:"
- "setRelativeReferenceFrameId:"
- "setRotationCameraToImu:"
- "setRotationImuToImu:"
- "setSensorLocation:"
- "setTransformCameraToImu:"
- "transformCameraToImu"
- "{\"msg%{public}.0s\":\"Could not serialize _CLSCSessionState\"}"
```
