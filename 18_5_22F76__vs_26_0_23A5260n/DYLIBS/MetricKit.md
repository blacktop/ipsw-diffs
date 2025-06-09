## MetricKit

> `/System/Library/Frameworks/MetricKit.framework/MetricKit`

```diff

-261.0.0.0.0
-  __TEXT.__text: 0xf160
+291.0.0.0.1
+  __TEXT.__text: 0xfec0
   __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_methlist: 0x1ab8
+  __TEXT.__objc_methlist: 0x1bb8
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0xdee
+  __TEXT.__cstring: 0xeb3
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__oslogstring: 0x21e
-  __TEXT.__unwind_info: 0x460
-  __TEXT.__objc_classname: 0x320
-  __TEXT.__objc_methname: 0x4f07
-  __TEXT.__objc_methtype: 0x60c
-  __TEXT.__objc_stubs: 0x1060
-  __DATA_CONST.__got: 0x218
+  __TEXT.__unwind_info: 0x480
+  __TEXT.__objc_classname: 0x33b
+  __TEXT.__objc_methname: 0x535f
+  __TEXT.__objc_methtype: 0x646
+  __TEXT.__objc_stubs: 0x1080
+  __DATA_CONST.__got: 0x228
   __DATA_CONST.__const: 0xc8
-  __DATA_CONST.__objc_classlist: 0x130
+  __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb90
+  __DATA_CONST.__objc_selrefs: 0xc00
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x120
+  __DATA_CONST.__objc_superrefs: 0x128
   __AUTH_CONST.__auth_got: 0x218
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x1360
-  __AUTH_CONST.__objc_const: 0x4208
-  __DATA.__objc_ivar: 0x284
+  __AUTH_CONST.__cfstring: 0x14a0
+  __AUTH_CONST.__objc_const: 0x4488
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x2ac
   __DATA.__data: 0x180
   __DATA_DIRTY.__objc_data: 0xbe0
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CB77E0D3-BE41-37C3-8E2C-76CB849F50AE
-  Functions: 508
-  Symbols:   1863
-  CStrings:  1106
+  UUID: 0D001FCB-7A06-36FB-9EA6-F89F6400C3B3
+  Functions: 527
+  Symbols:   1921
+  CStrings:  1163
 
Symbols:
+ +[MXDiskSpaceUsageMetric supportsSecureCoding]
+ -[MXAnimationMetric hitchTimeRatio]
+ -[MXAnimationMetric initWithHitchTimeRatio:perceivedHitchTimeRatio:]
+ -[MXAppResponsivenessMetric initWithAppResponsivenessHangData:spinData:]
+ -[MXDiskSpaceUsageMetric .cxx_destruct]
+ -[MXDiskSpaceUsageMetric encodeWithCoder:]
+ -[MXDiskSpaceUsageMetric initWithCoder:]
+ -[MXDiskSpaceUsageMetric initWithTotalBinaryFileSize:totalBinaryFileCount:totalDataFileSize:totalDataFileCount:totalCacheFolderSize:totalCloneSize:totalDiskSpaceUsedSize:totalDiskSpaceCapacity:]
+ -[MXDiskSpaceUsageMetric toDictionary]
+ -[MXDiskSpaceUsageMetric totalBinaryFileCount]
+ -[MXDiskSpaceUsageMetric totalBinaryFileSize]
+ -[MXDiskSpaceUsageMetric totalCacheFolderSize]
+ -[MXDiskSpaceUsageMetric totalCloneSize]
+ -[MXDiskSpaceUsageMetric totalDataFileCount]
+ -[MXDiskSpaceUsageMetric totalDataFileSize]
+ -[MXDiskSpaceUsageMetric totalDiskSpaceCapacity]
+ -[MXDiskSpaceUsageMetric totalDiskSpaceUsedSize]
+ -[MXMetaData bundleIdentifier]
+ -[MXMetaData setBundleIdentifier:]
+ -[MXMetricPayload diskSpaceUsageMetrics]
+ -[MXMetricPayload setDiskSpaceUsageMetrics:]
+ _OBJC_CLASS_$_MXDiskSpaceUsageMetric
+ _OBJC_CLASS_$_NSUnitInformationStorage
+ _OBJC_IVAR_$_MXAnimationMetric._hitchTimeRatio
+ _OBJC_IVAR_$_MXDiskSpaceUsageMetric._totalBinaryFileCount
+ _OBJC_IVAR_$_MXDiskSpaceUsageMetric._totalBinaryFileSize
+ _OBJC_IVAR_$_MXDiskSpaceUsageMetric._totalCacheFolderSize
+ _OBJC_IVAR_$_MXDiskSpaceUsageMetric._totalCloneSize
+ _OBJC_IVAR_$_MXDiskSpaceUsageMetric._totalDataFileCount
+ _OBJC_IVAR_$_MXDiskSpaceUsageMetric._totalDataFileSize
+ _OBJC_IVAR_$_MXDiskSpaceUsageMetric._totalDiskSpaceCapacity
+ _OBJC_IVAR_$_MXDiskSpaceUsageMetric._totalDiskSpaceUsedSize
+ _OBJC_IVAR_$_MXMetaData._bundleIdentifier
+ _OBJC_IVAR_$_MXMetricPayload._diskSpaceUsageMetrics
+ _OBJC_METACLASS_$_MXDiskSpaceUsageMetric
+ __OBJC_$_CLASS_METHODS_MXDiskSpaceUsageMetric
+ __OBJC_$_INSTANCE_METHODS_MXDiskSpaceUsageMetric
+ __OBJC_$_INSTANCE_VARIABLES_MXDiskSpaceUsageMetric
+ __OBJC_$_PROP_LIST_MXDiskSpaceUsageMetric
+ __OBJC_CLASS_RO_$_MXDiskSpaceUsageMetric
+ __OBJC_METACLASS_RO_$_MXDiskSpaceUsageMetric
+ _objc_msgSend$kilobytes
- -[MXMetaData bundleID]
- -[MXMetaData setBundleID:]
- _OBJC_IVAR_$_MXMetaData._bundleID
CStrings:
+ "@\"MXDiskSpaceUsageMetric\""
+ "@80@0:8@16Q24@32Q40@48@56@64@72"
+ "MXDiskSpaceUsageMetric"
+ "T@\"MXDiskSpaceUsageMetric\",&,V_diskSpaceUsageMetrics"
+ "T@\"NSMeasurement\",R,V_hitchTimeRatio"
+ "T@\"NSMeasurement\",R,V_totalBinaryFileSize"
+ "T@\"NSMeasurement\",R,V_totalCacheFolderSize"
+ "T@\"NSMeasurement\",R,V_totalCloneSize"
+ "T@\"NSMeasurement\",R,V_totalDataFileSize"
+ "T@\"NSMeasurement\",R,V_totalDiskSpaceCapacity"
+ "T@\"NSMeasurement\",R,V_totalDiskSpaceUsedSize"
+ "T@\"NSString\",&,V_bundleIdentifier"
+ "Tq,R,V_totalBinaryFileCount"
+ "Tq,R,V_totalDataFileCount"
+ "_bundleIdentifier"
+ "_diskSpaceUsageMetrics"
+ "_hitchTimeRatio"
+ "_totalBinaryFileCount"
+ "_totalBinaryFileSize"
+ "_totalCacheFolderSize"
+ "_totalCloneSize"
+ "_totalDataFileCount"
+ "_totalDataFileSize"
+ "_totalDiskSpaceCapacity"
+ "_totalDiskSpaceUsedSize"
+ "diskSpaceUsageMetrics"
+ "hitchTimeRatio"
+ "initWithAppResponsivenessHangData:spinData:"
+ "initWithHitchTimeRatio:perceivedHitchTimeRatio:"
+ "initWithTotalBinaryFileSize:totalBinaryFileCount:totalDataFileSize:totalDataFileCount:totalCacheFolderSize:totalCloneSize:totalDiskSpaceUsedSize:totalDiskSpaceCapacity:"
+ "kilobytes"
+ "setBundleIdentifier:"
+ "setDiskSpaceUsageMetrics:"
+ "totalBinaryFileCount"
+ "totalBinaryFileSize"
+ "totalCacheFolderSize"
+ "totalCloneSize"
+ "totalDataFileCount"
+ "totalDataFileSize"
+ "totalDiskSpaceCapacity"
+ "totalDiskSpaceUsedSize"
- "T@\"NSString\",&,V_bundleID"
- "_bundleID"
- "setBundleID:"

```
