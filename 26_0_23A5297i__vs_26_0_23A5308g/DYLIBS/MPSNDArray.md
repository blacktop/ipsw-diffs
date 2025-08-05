## MPSNDArray

> `/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNDArray.framework/MPSNDArray`

```diff

-129.0.15.0.0
-  __TEXT.__text: 0xe89e8
-  __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_methlist: 0x6a14
+129.0.18.0.0
+  __TEXT.__text: 0xe8fdc
+  __TEXT.__auth_stubs: 0xa60
+  __TEXT.__objc_methlist: 0x6a84
   __TEXT.__const: 0x44900
-  __TEXT.__gcc_except_tab: 0x38d0
-  __TEXT.__cstring: 0xb9e9
-  __TEXT.__unwind_info: 0x1788
+  __TEXT.__gcc_except_tab: 0x38d8
+  __TEXT.__cstring: 0xbb81
+  __TEXT.__unwind_info: 0x17a0
   __TEXT.__eh_frame: 0x68
-  __TEXT.__objc_classname: 0x1c3b
-  __TEXT.__objc_methname: 0x6944
-  __TEXT.__objc_methtype: 0x1e33
-  __TEXT.__objc_stubs: 0x2f00
-  __DATA_CONST.__got: 0x2a0
+  __TEXT.__objc_classname: 0x1c59
+  __TEXT.__objc_methname: 0x6b34
+  __TEXT.__objc_methtype: 0x1e7e
+  __TEXT.__objc_stubs: 0x3160
+  __DATA_CONST.__got: 0x2d8
   __DATA_CONST.__const: 0xe9f0
-  __DATA_CONST.__objc_classlist: 0x840
+  __DATA_CONST.__objc_classlist: 0x848
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1458
+  __DATA_CONST.__objc_selrefs: 0x14f8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x818
-  __AUTH_CONST.__auth_got: 0x528
-  __AUTH_CONST.__const: 0x3c00
-  __AUTH_CONST.__cfstring: 0x5bc0
-  __AUTH_CONST.__objc_const: 0xe6d8
-  __DATA.__objc_ivar: 0x68c
+  __DATA_CONST.__objc_superrefs: 0x820
+  __AUTH_CONST.__auth_got: 0x540
+  __AUTH_CONST.__const: 0x3be0
+  __AUTH_CONST.__cfstring: 0x5d00
+  __AUTH_CONST.__objc_const: 0xe888
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x6a8
   __DATA.__data: 0x9c0
   __DATA.__bss: 0x450
   __DATA_DIRTY.__objc_data: 0x5280

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EAF75D1F-EE58-33D8-BEAB-E9B5860617AF
-  Functions: 2179
-  Symbols:   7300
-  CStrings:  3294
+  UUID: 305C6D11-A4E2-37D3-93D3-F436FBFA8625
+  Functions: 2189
+  Symbols:   7362
+  CStrings:  3347
 
Symbols:
+ -[MPSNDArrayAutoTuneRecorderObj dealloc]
+ -[MPSNDArrayAutoTuneRecorderObj getKernelNodesForKernelID:]
+ -[MPSNDArrayAutoTuneRecorderObj init]
+ -[MPSNDArrayAutoTuneRecorderObj recordNode:kernelID:]
+ -[MPSNDArrayMatrixMultiplication advanceAutoTuneIteration]
+ -[MPSNDArrayMatrixMultiplication autoTuneIteration]
+ -[MPSNDArrayMatrixMultiplication logNextAutoTuneParams]
+ -[MPSNDArrayMatrixMultiplication setAutoTuneIteration:]
+ -[MPSNDArrayMatrixMultiplication setLogNextAutoTuneParams:]
+ GCC_except_table91
+ OBJC_IVAR_$_MPSNDArrayMatrixMultiplication._autoTuneIteration
+ OBJC_IVAR_$_MPSNDArrayMatrixMultiplication._logNextAutoTuneParams
+ OBJC_IVAR_$_MPSNDArrayMatrixMultiplication._nextAutoTuneIteration
+ _NSLog
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_MPSNDArrayAutoTuneRecorderObj
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSURL
+ _OBJC_IVAR_$_MPSNDArrayAutoTuneRecorderObj._autoTuneNodesDirURL
+ _OBJC_IVAR_$_MPSNDArrayAutoTuneRecorderObj._fileManager
+ _OBJC_IVAR_$_MPSNDArrayAutoTuneRecorderObj._modelFileArchivePath
+ _OBJC_IVAR_$_MPSNDArrayAutoTuneRecorderObj._nodeDictionary
+ _OBJC_METACLASS_$_MPSNDArrayAutoTuneRecorderObj
+ __OBJC_$_INSTANCE_METHODS_MPSNDArrayAutoTuneRecorderObj
+ __OBJC_$_INSTANCE_VARIABLES_MPSNDArrayAutoTuneRecorderObj
+ __OBJC_CLASS_PROTOCOLS_$_MPSNDArrayMatrixMultiplication
+ __OBJC_CLASS_RO_$_MPSNDArrayAutoTuneRecorderObj
+ __OBJC_METACLASS_RO_$_MPSNDArrayAutoTuneRecorderObj
+ __ZL17MPSKernel_LogInfo24MPSKernelOptionVerbositymPKcz
+ _getpid
+ _objc_msgSend$URLByAppendingPathComponent:
+ _objc_msgSend$allObjects
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$containsObject:
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$date
+ _objc_msgSend$defaultManager
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$getKernelNodesForKernelID:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$localizedFailureReason
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$path
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$writeToURL:error:
- GCC_except_table86
CStrings:
+ "%@%@"
+ "%@%@/mpsndarray_autotune-%d-%@-%u/"
+ "%s/"
+ ".h"
+ ".nsarray"
+ "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShaders/MPSNDArray/AutoTune/MPSNDArrayAutoTune.mm"
+ "/tmp/"
+ "@\"NSFileManager\""
+ "@\"NSMutableDictionary\""
+ "@\"NSString\""
+ "@\"NSURL\""
+ "Error creating directory \n %s %s"
+ "Error unexpectedly %@ is not a directory \n %s %s"
+ "MPSNDARRAY_AUTO_TUNE_FILE_PATH"
+ "MPSNDArray Auto Tuning Error: unrecognized auto tune keys"
+ "MPSNDArray Auto Tuning: Writing found nodes to %s\n"
+ "MPSNDArrayAutoTuneRecorderObj"
+ "URLByAppendingPathComponent:"
+ "_autoTuneNodesDirURL"
+ "_fileManager"
+ "_modelFileArchivePath"
+ "_nodeDictionary"
+ "allObjects"
+ "bundleForClass:"
+ "bundleIdentifier"
+ "containsObject:"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "date"
+ "defaultManager"
+ "fileExistsAtPath:isDirectory:"
+ "fileURLWithPath:"
+ "getKernelNodesForKernelID:"
+ "localizedDescription"
+ "localizedFailureReason"
+ "objectForKeyedSubscript:"
+ "path"
+ "recordNode:kernelID:"
+ "setDateFormat:"
+ "setObject:forKeyedSubscript:"
+ "stringFromDate:"
+ "v32@0:8@16Q24"
+ "writeToURL:error:"
+ "yyyy-MM-dd_HH_mm_ss"

```
