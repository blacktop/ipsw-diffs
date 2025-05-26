## APConfigurationSystem

> `/System/Library/PrivateFrameworks/APConfigurationSystem.framework/APConfigurationSystem`

```diff

-485.0.0.0.0
-  __TEXT.__text: 0x4208
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_methlist: 0x46c
-  __TEXT.__const: 0x68
-  __TEXT.__oslogstring: 0x8c1
-  __TEXT.__cstring: 0x5d0
-  __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x128
-  __TEXT.__objc_classname: 0x1c0
-  __TEXT.__objc_methname: 0x10d7
-  __TEXT.__objc_methtype: 0x2d1
-  __TEXT.__objc_stubs: 0xe20
+500.2.0.0.0
+  __TEXT.__text: 0x4c84
+  __TEXT.__auth_stubs: 0x3c0
+  __TEXT.__objc_methlist: 0x5fc
+  __TEXT.__const: 0x78
+  __TEXT.__oslogstring: 0x93b
+  __TEXT.__cstring: 0x653
+  __TEXT.__gcc_except_tab: 0x2c
+  __TEXT.__unwind_info: 0x16c
+  __TEXT.__objc_classname: 0x274
+  __TEXT.__objc_methname: 0x133e
+  __TEXT.__objc_methtype: 0x2c7
+  __TEXT.__objc_stubs: 0xf80
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x100
-  __DATA_CONST.__objc_classlist: 0x70
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__const: 0x128
+  __DATA_CONST.__objc_classlist: 0xb0
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf28
-  __DATA_CONST.__objc_selrefs: 0x410
-  __AUTH_CONST.__cfstring: 0x660
-  __AUTH_CONST.__objc_const: 0x510
-  __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x1b8
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_classrefs: 0xb8
-  __DATA.__objc_superrefs: 0x20
-  __DATA.__objc_ivar: 0x28
-  __DATA.__data: 0x1e0
+  __DATA_CONST.__objc_const: 0x1438
+  __DATA_CONST.__objc_selrefs: 0x478
+  __AUTH_CONST.__cfstring: 0x700
+  __AUTH_CONST.__objc_const: 0x828
+  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__auth_got: 0x1f0
+  __AUTH.__objc_data: 0x460
+  __DATA.__objc_classrefs: 0xc8
+  __DATA.__objc_superrefs: 0x38
+  __DATA.__objc_ivar: 0x30
+  __DATA.__data: 0x240
   __DATA_DIRTY.__objc_data: 0x280
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 78
-  Symbols:   142
-  CStrings:  371
+  Functions: 104
+  Symbols:   165
+  CStrings:  411
 
Symbols:
+ _OBJC_CLASS_$_APCSIntegrityReport
+ _OBJC_CLASS_$_APCSReports
+ _OBJC_CLASS_$_APECObservabilityConfig
+ _OBJC_CLASS_$_APECObservabilityPurposeConfig
+ _OBJC_CLASS_$_APECReportsPurposeConfig
+ _OBJC_CLASS_$_APVersionData
+ _OBJC_CLASS_$_APVersionHelper
+ _OBJC_CLASS_$_APVersionTestData
+ _OBJC_CLASS_$_NSArray
+ _OBJC_METACLASS_$_APCSIntegrityReport
+ _OBJC_METACLASS_$_APCSReports
+ _OBJC_METACLASS_$_APECObservabilityConfig
+ _OBJC_METACLASS_$_APECObservabilityPurposeConfig
+ _OBJC_METACLASS_$_APECReportsPurposeConfig
+ _OBJC_METACLASS_$_APVersionData
+ _OBJC_METACLASS_$_APVersionHelper
+ _OBJC_METACLASS_$_APVersionTestData
+ __Block_object_dispose
+ ___NSArray0__struct
+ _objc_destroyWeak
+ _objc_loadWeakRetained
+ _objc_moveWeak
+ _objc_retainBlock
+ _objc_retain_x1
+ _objc_storeWeak
- _APDefaultsBundleID
- _OBJC_CLASS_$_NSUserDefaults
CStrings:
+ "@\"<APVersionDatasource>\""
+ "@\"NSArray\""
+ "@\"NSArray\"24@0:8@\"NSURL\"16"
+ "@24@0:8^@16"
+ "APCSIntegrityReport"
+ "APCSReports"
+ "APECObservabilityConfig"
+ "APECObservabilityPurposeConfig"
+ "APECReportsPurposeConfig"
+ "APVersionData"
+ "APVersionDatasource"
+ "APVersionHelper"
+ "APVersionTestData"
+ "EventCollection/Observability"
+ "EventCollection/Purposes/103"
+ "EventCollection/Purposes/8501"
+ "Reports"
+ "Reports/Integrity"
+ "T@\"<APVersionDatasource>\",&,N,V_datasource"
+ "T@\"NSArray\",&,N,V_directoryURLs"
+ "T@\"NSArray\",&,N,V_testURLS"
+ "T@\"NSArray\",R,D,N"
+ "T@\"NSArray\",R,N"
+ "T@\"NSFileManager\",&,N,V_fileManager"
+ "T@\"NSNumber\",R,N"
+ "T@\"NSString\",R,D,N"
+ "[%{private}@] Error: Unable to create Enumerator from URL."
+ "[%{private}@] Error: Unable to create URL from directory path."
+ "_datasource"
+ "_directoryURLs"
+ "_getVersionForNodesAtDirectoryPath:"
+ "_resourcesBundleDirectoryPathError:"
+ "_testURLS"
+ "_versionInDirectoryWithURLs:"
+ "allObjects"
+ "array"
+ "bufferedTimeHistogram"
+ "communicationReportClientCodeBuckets"
+ "communicationReportServerCodeBuckets"
+ "createdToBufferedTimeHistogram"
+ "dailyReportClientCodeBuckets"
+ "dailyReportServerCodeBuckets"
+ "datasource"
+ "defaultManager"
+ "deliveryLeeway"
+ "directoryURLs"
+ "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
+ "initWithDatasource:"
+ "regularJobDaemonStartDelay"
+ "removeDataAfterDays"
+ "reportingFrequency"
+ "reportingPurposes"
+ "resourcesBundleDirectoryPath"
+ "setDatasource:"
+ "setDirectoryURLs:"
+ "setFileManager:"
+ "setTestURLS:"
+ "subdirectoriesAtURL:"
+ "systemVersion"
+ "testURLS"
+ "v16@?0@\"NSURL\"8"
+ "xpcTimerGracePeriod"
+ "xpcTimerPriority"
- "@\"NSNumber\""
- "T@\"NSArray\",&,D,N"
- "T@\"NSArray\",&,N"
- "T@\"NSNumber\",&,N"
- "T@\"NSNumber\",&,N,V_purpose"
- "T@\"NSString\",&,N"
- "_purpose"
- "initWithSuiteName:"
- "integerForKey:"
- "saveConfigurationVersion:"
- "setAllowedPurposes:"
- "setAllowedSources:"
- "setCollectionType:"
- "setDestination:"
- "setDisallowedEvents:"
- "setInteger:forKey:"
- "setPurpose:"
- "setSamplePercentage:"
- "setSamplePeriod:"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSNumber\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8q16"

```
