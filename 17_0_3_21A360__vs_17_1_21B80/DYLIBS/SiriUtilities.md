## SiriUtilities

> `/System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities`

```diff

-3300.48.1.0.0
-  __TEXT.__text: 0x6340c
-  __TEXT.__auth_stubs: 0x1cb0
-  __TEXT.__objc_methlist: 0x120
-  __TEXT.__const: 0x4180
-  __TEXT.__cstring: 0x2462
-  __TEXT.__oslogstring: 0x69
-  __TEXT.__swift5_typeref: 0x1883
+3301.3.1.0.0
+  __TEXT.__text: 0x64a40
+  __TEXT.__auth_stubs: 0x1d90
+  __TEXT.__objc_methlist: 0x190
+  __TEXT.__const: 0x41b0
+  __TEXT.__cstring: 0x2642
+  __TEXT.__oslogstring: 0x230
+  __TEXT.__swift5_typeref: 0x1897
   __TEXT.__swift5_reflstr: 0xd52
   __TEXT.__swift5_assocty: 0x2c8
-  __TEXT.__constg_swiftt: 0x1f58
-  __TEXT.__swift5_fieldmd: 0x1184
+  __TEXT.__constg_swiftt: 0x1f74
+  __TEXT.__swift5_fieldmd: 0x1194
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x2fc
-  __TEXT.__swift5_types: 0x18c
+  __TEXT.__swift5_types: 0x190
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__swift5_capture: 0x8f8
+  __TEXT.__swift5_capture: 0x908
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x34ac
+  __TEXT.__unwind_info: 0x3508
   __TEXT.__eh_frame: 0x2e80
-  __TEXT.__objc_classname: 0x67
-  __TEXT.__objc_methname: 0x499
-  __TEXT.__objc_methtype: 0xeb
-  __DATA_CONST.__got: 0x598
-  __DATA_CONST.__const: 0x7a8
-  __DATA_CONST.__objc_classlist: 0x88
+  __TEXT.__objc_classname: 0x76
+  __TEXT.__objc_methname: 0x6c4
+  __TEXT.__objc_methtype: 0x11c
+  __TEXT.__objc_stubs: 0x2a0
+  __DATA_CONST.__got: 0x5a8
+  __DATA_CONST.__const: 0x820
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1870
-  __DATA_CONST.__objc_selrefs: 0x158
-  __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x120
-  __AUTH_CONST.__const: 0x4e18
-  __AUTH_CONST.__auth_got: 0xe58
+  __DATA_CONST.__objc_selrefs: 0x1f8
+  __AUTH_CONST.__cfstring: 0x100
+  __AUTH_CONST.__const: 0x4ea8
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__objc_const: 0x1b0
+  __AUTH_CONST.__auth_got: 0xed0
+  __AUTH.__objc_data: 0x158
   __AUTH.__data: 0x740
-  __AUTH.__objc_data: 0x108
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x68
+  __DATA.__objc_classrefs: 0x98
   __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x1380
-  __DATA.__bss: 0x3cc0
+  __DATA.__data: 0x13b0
+  __DATA.__bss: 0x3cd0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x2d0
-  __DATA_DIRTY.__data: 0x1f08
+  __DATA_DIRTY.__data: 0x1f00
   __DATA_DIRTY.__bss: 0x1d00
   __DATA_DIRTY.__common: 0x588
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/libtailspin.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 4B2214AF-E7EA-3AE1-8AC9-692DF7E92F87
-  Functions: 4454
-  Symbols:   10717
-  CStrings:  359
+  UUID: FB565C4A-58E4-3F84-82FF-8834A983874C
+  Functions: 4485
+  Symbols:   10842
+  CStrings:  410
 
Symbols:
+ +[TailSpinHelper getLastSuccessfulTailSpinDate:]
+ +[TailSpinHelper getLogger]
+ +[TailSpinHelper getTailSpinDir:]
+ +[TailSpinHelper isValidToCreateTailSpin:]
+ +[TailSpinHelper isValidToDeleteTailSpinDir:]
+ +[TailSpinHelper setSuccessfulTailSpinDate:date:]
+ -[TailSpinHelper clearDirectory:queue:]
+ -[TailSpinHelper dumpTailSpinOutputToFile:suiteName:options:queue:handler:]
+ -[TailSpinHelper dumpTailSpinOutputToFile:suiteName:options:queue:handler:].cold.1
+ _$s13SiriUtilities15TailSpinManagerO06createcD4File8fileName05suiteI07options10completionySS_SSSDys11AnyHashableVypGSgySb_SSSgtctFZ
+ _$s13SiriUtilities15TailSpinManagerO06createcD4File8fileName05suiteI07options10completionySS_SSSDys11AnyHashableVypGSgySb_SSSgtctFZySb_AMtcfU_
+ _$s13SiriUtilities15TailSpinManagerO06createcD4File8fileName05suiteI07options10completionySS_SSSDys11AnyHashableVypGSgySb_SSSgtctFZySb_AMtcfU_TA
+ _$s13SiriUtilities15TailSpinManagerO06deletecD5Files9suiteNameySS_tFZ
+ _$s13SiriUtilities15TailSpinManagerO20tailspinRequestQueue33_A369BB6ECFF37A4EB79BCE9041611C45LLSo17OS_dispatch_queueCvpZ
+ _$s13SiriUtilities15TailSpinManagerO20tailspinRequestQueue33_A369BB6ECFF37A4EB79BCE9041611C45LL_WZ
+ _$s13SiriUtilities15TailSpinManagerO20tailspinRequestQueue33_A369BB6ECFF37A4EB79BCE9041611C45LL_Wz
+ _$s13SiriUtilities15TailSpinManagerO24tailspinDefaultDirectorySSvgZ
+ _$s13SiriUtilities15TailSpinManagerOMF
+ _$s13SiriUtilities15TailSpinManagerOMa
+ _$s13SiriUtilities15TailSpinManagerOMf
+ _$s13SiriUtilities15TailSpinManagerOMn
+ _$s13SiriUtilities15TailSpinManagerON
+ _$s2os18OSLogInterpolationV06appendC0_6format7privacyySbyXA_AA0B10BoolFormatOAA0B7PrivacyVtFs5Int32Vycfu_
+ _$s2os18OSLogInterpolationV06appendC0_6format7privacyys5Int32VyXA_AA0bG14ExtendedFormatOAA0B7PrivacyVtFAHycfu_
+ _$sSbSSSgIegyg_SbSo8NSStringCSgIeyByy_TR
+ _$sSo17OS_dispatch_queueC8DispatchE10AttributesVAEs9OptionSetACWL
+ _$sSo17OS_dispatch_queueC8DispatchE10AttributesVAEs9OptionSetACWl
+ _$sSo17OS_dispatch_queueC8DispatchE10AttributesVs9OptionSetACMc
+ _$ss5Int32VIegd_ABIegr_TR
+ _$ss9OptionSetP8rawValuex03RawD0Qz_tcfCTj
+ _IsAppleInternalBuild
+ _NSFilePosixPermissions
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_TailSpinHelper
+ _OBJC_METACLASS_$_TailSpinHelper
+ __NSConcreteGlobalBlock
+ __OBJC_$_CLASS_METHODS_TailSpinHelper
+ __OBJC_$_INSTANCE_METHODS_TailSpinHelper
+ __OBJC_CLASS_RO_$_TailSpinHelper
+ __OBJC_METACLASS_RO_$_TailSpinHelper
+ ___27+[TailSpinHelper getLogger]_block_invoke
+ ___39-[TailSpinHelper clearDirectory:queue:]_block_invoke
+ ___39-[TailSpinHelper clearDirectory:queue:]_block_invoke.cold.1
+ ___39-[TailSpinHelper clearDirectory:queue:]_block_invoke.cold.2
+ ___75-[TailSpinHelper dumpTailSpinOutputToFile:suiteName:options:queue:handler:]_block_invoke
+ ___75-[TailSpinHelper dumpTailSpinOutputToFile:suiteName:options:queue:handler:]_block_invoke.cold.1
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_literal_global
+ __os_log_default
+ __os_log_error_impl
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_SiriUtilities
+ _close
+ _dispatch_async
+ _dispatch_once
+ _getLogger._logger
+ _getLogger.onceToken
+ _objc_alloc
+ _objc_alloc_init
+ _objc_msgSend$cStringUsingEncoding:
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$date
+ _objc_msgSend$defaultManager
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$getLastSuccessfulTailSpinDate:
+ _objc_msgSend$getLogger
+ _objc_msgSend$getTailSpinDir:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$isValidToCreateTailSpin:
+ _objc_msgSend$isValidToDeleteTailSpinDir:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setSuccessfulTailSpinDate:date:
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _open
+ _symbolic SbSSSgIegyg_
+ _symbolic _____ 13SiriUtilities15TailSpinManagerO
+ _tailspin_dump_output_with_options_sync
CStrings:
+ " "
+ "-"
+ "/tailspins/siri/%@/"
+ "/var/mobile/tmp/tailspins/siri/"
+ "SiriUtils#TailSpinManager"
+ "SiriUtils_%@_%@.tailspin"
+ "TailSpinHelper"
+ "TailSpinHelper#clearDirectory cleaned up directory: %@"
+ "TailSpinHelper#clearDirectory enforcing minimum time interval (%d s) for deleting directory %@"
+ "TailSpinHelper#clearDirectory failed to clean up directory: %@"
+ "TailSpinHelper#dumpTailSpinOutputToFile dir: %@"
+ "TailSpinHelper#dumpTailSpinOutputToFile enforcing minimum time interval (%d s) between tailspins, not creating new file: %@"
+ "TailSpinHelper#dumpTailSpinOutputToFile unable to create directory %@"
+ "TailSpinManager#createTailSpinFile invalid param(s) passed in"
+ "TailSpinManager#createTailSpinFile refusing to delete tailspin files"
+ "TailSpinManager#createTailSpinFile refusing to generate tailspin file"
+ "TailSpinManager#createTailSpinFile status: %{bool}d, path: %s"
+ "cStringUsingEncoding:"
+ "clearDirectory:queue:"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "date"
+ "dictionaryWithObjects:forKeys:count:"
+ "dumpTailSpinOutputToFile:suiteName:options:queue:handler:"
+ "getLastSuccessfulTailSpinDate:"
+ "getLogger"
+ "getTailSpinDir:"
+ "i"
+ "initWithSuiteName:"
+ "isValidToCreateTailSpin:"
+ "isValidToDeleteTailSpinDir:"
+ "removeItemAtPath:error:"
+ "setDateFormat:"
+ "setSuccessfulTailSpinDate:date:"
+ "siri_tailspin"
+ "stringByAppendingPathComponent:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "stringFromDate:"
+ "stringWithFormat:"
+ "timeIntervalSinceDate:"
+ "v20@?0B8@\"NSString\"12"
+ "v32@0:8@16@24"
+ "v56@0:8@16@24@32@40@?48"
+ "yyyy-MM-dd_HH-mm-ss"

```
