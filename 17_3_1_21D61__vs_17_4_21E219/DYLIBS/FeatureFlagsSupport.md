## FeatureFlagsSupport

> `/System/Library/PrivateFrameworks/FeatureFlagsSupport.framework/FeatureFlagsSupport`

```diff

-85.0.0.0.0
-  __TEXT.__text: 0xb6e8
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_methlist: 0xb1c
+86.0.0.0.0
+  __TEXT.__text: 0xbd30
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_methlist: 0xbcc
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0xadc
-  __TEXT.__unwind_info: 0x2b8
-  __TEXT.__objc_classname: 0x1f5
-  __TEXT.__objc_methname: 0x1fd5
-  __TEXT.__objc_methtype: 0x500
-  __TEXT.__objc_stubs: 0x1860
+  __TEXT.__cstring: 0xaf8
+  __TEXT.__unwind_info: 0x2dc
+  __TEXT.__objc_classname: 0x226
+  __TEXT.__objc_methname: 0x2279
+  __TEXT.__objc_methtype: 0x58d
+  __TEXT.__objc_stubs: 0x19a0
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x268
-  __DATA_CONST.__objc_classlist: 0x80
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x0
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1068
-  __DATA_CONST.__objc_selrefs: 0x7a0
+  __DATA_CONST.__objc_const: 0x1150
+  __DATA_CONST.__objc_selrefs: 0x810
+  __DATA_CONST.__objc_classrefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__objc_const: 0x48
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__cfstring: 0x920
+  __AUTH_CONST.__cfstring: 0x940
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x1b0
-  __DATA.__objc_classrefs: 0xd8
-  __DATA.__objc_superrefs: 0x58
-  __DATA.__objc_ivar: 0xb0
-  __DATA.__data: 0x298
+  __AUTH_CONST.__auth_got: 0x1c8
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0xb8
+  __DATA.__data: 0x2f8
   __DATA.__crash_info: 0x40
   __DATA_DIRTY.__const: 0x20
   __DATA_DIRTY.__objc_const: 0x5e8

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4B840EB0-3C51-3398-BB53-71E30E714506
-  Functions: 268
-  Symbols:   1016
-  CStrings:  616
+  UUID: 98E3E8CE-1259-3CD9-BF33-C0D13181F585
+  Functions: 283
+  Symbols:   1067
+  CStrings:  646
 
Symbols:
+ +[FFConfiguration _configurationForTestingWithFileReader:fileWriter:buildVersionGetter:parseErrorReporter:safeModeChecker:]
+ +[FFConfiguration configurationForTestingWithFileReader:fileWriter:buildVersionGetter:]
+ -[FFConfiguration buildVersionGetter]
+ -[FFConfiguration disableFeature:domain:level:transient:]
+ -[FFConfiguration disableFeature:domain:levelIndex:transient:]
+ -[FFConfiguration enableFeature:domain:level:transient:]
+ -[FFConfiguration enableFeature:domain:levelIndex:transient:]
+ -[FFConfiguration setBuildVersionGetter:]
+ -[FFConfiguration setValue:feature:domain:levelIndex:buildVersion:]
+ -[FFConfiguration setValue:feature:domain:levelIndex:buildVersion:].cold.1
+ -[FFConfiguration setValue:feature:domain:levelIndex:buildVersion:].cold.2
+ -[FFDefaultBuildVersionGetter getBuildVersion]
+ -[FFFeatureState buildVersion]
+ -[FFFeatureState initWithDomain:feature:value:buildVersion:]
+ -[FFFeatureState initWithDomain:feature:value:phase:disclosureRequired:attributes:buildVersion:]
+ -[FFFeatureState setBuildVersion:]
+ _OBJC_CLASS_$_FFDefaultBuildVersionGetter
+ _OBJC_IVAR_$_FFConfiguration._buildVersionGetter
+ _OBJC_IVAR_$_FFFeatureState._buildVersion
+ _OBJC_METACLASS_$_FFDefaultBuildVersionGetter
+ __OBJC_$_INSTANCE_METHODS_FFDefaultBuildVersionGetter
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FFBuildVersionGetter
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FFBuildVersionGetter
+ __OBJC_CLASS_PROTOCOLS_$_FFDefaultBuildVersionGetter
+ __OBJC_CLASS_RO_$_FFDefaultBuildVersionGetter
+ __OBJC_LABEL_PROTOCOL_$_FFBuildVersionGetter
+ __OBJC_METACLASS_RO_$_FFDefaultBuildVersionGetter
+ __OBJC_PROTOCOL_$_FFBuildVersionGetter
+ __unnamed_array_storage.337
+ __unnamed_array_storage.339
+ __unnamed_array_storage.340
+ __unnamed_array_storage.346
+ __unnamed_array_storage.347
+ _objc_msgSend$_configurationForTestingWithFileReader:fileWriter:buildVersionGetter:parseErrorReporter:safeModeChecker:
+ _objc_msgSend$buildVersion
+ _objc_msgSend$buildVersionGetter
+ _objc_msgSend$disableFeature:domain:levelIndex:transient:
+ _objc_msgSend$enableFeature:domain:levelIndex:transient:
+ _objc_msgSend$getBuildVersion
+ _objc_msgSend$initWithDomain:feature:value:buildVersion:
+ _objc_msgSend$initWithDomain:feature:value:phase:disclosureRequired:attributes:buildVersion:
+ _objc_msgSend$setBuildVersion:
+ _objc_msgSend$setBuildVersionGetter:
+ _objc_msgSend$setValue:feature:domain:levelIndex:buildVersion:
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_retain_x5
+ _objc_retain_x7
+ _sysctlbyname
- +[FFConfiguration _configurationForTestingWithFileReader:fileWriter:parseErrorReporter:safeModeChecker:]
- -[FFConfiguration setValue:feature:domain:levelIndex:].cold.1
- -[FFConfiguration setValue:feature:domain:levelIndex:].cold.2
- __unnamed_array_storage.324
- __unnamed_array_storage.326
- __unnamed_array_storage.327
- __unnamed_array_storage.333
- __unnamed_array_storage.334
- _objc_msgSend$_configurationForTestingWithFileReader:fileWriter:parseErrorReporter:safeModeChecker:
- _objc_msgSend$initWithDomain:feature:value:
CStrings:
+ "\x03\x13"
+ "\x1f\x0f\x0f\x0f\x0f\b"
+ "@\"<FFBuildVersionGetter>\""
+ "@48@0:8@16@24q32@40"
+ "@56@0:8@16@24@32@40@48"
+ "@72@0:8@16@24q32@40@48@56@64"
+ "BuildVersion"
+ "FFBuildVersionGetter"
+ "FFDefaultBuildVersionGetter"
+ "T@\"<FFBuildVersionGetter>\",&,N,V_buildVersionGetter"
+ "T@\"NSString\",&,N,V_buildVersion"
+ "T@\"NSString\",?,R,C"
+ "_buildVersion"
+ "_buildVersionGetter"
+ "_configurationForTestingWithFileReader:fileWriter:buildVersionGetter:parseErrorReporter:safeModeChecker:"
+ "buildVersion"
+ "buildVersionGetter"
+ "configurationForTestingWithFileReader:fileWriter:buildVersionGetter:"
+ "disableFeature:domain:level:transient:"
+ "disableFeature:domain:levelIndex:transient:"
+ "enableFeature:domain:level:transient:"
+ "enableFeature:domain:levelIndex:transient:"
+ "getBuildVersion"
+ "initWithDomain:feature:value:buildVersion:"
+ "initWithDomain:feature:value:phase:disclosureRequired:attributes:buildVersion:"
+ "kern.osversion"
+ "setBuildVersion:"
+ "setBuildVersionGetter:"
+ "setValue:feature:domain:levelIndex:buildVersion:"
+ "stringWithCString:encoding:"
+ "v44@0:8@16@24Q32B40"
+ "v44@0:8@16@24q32B40"
+ "v56@0:8q16@24@32Q40@48"
- "\x03\x12"
- "\x1f\x0f\x0f\x0f\x0f\a"
- "@48@0:8@16@24@32@40"
- "_configurationForTestingWithFileReader:fileWriter:parseErrorReporter:safeModeChecker:"

```
