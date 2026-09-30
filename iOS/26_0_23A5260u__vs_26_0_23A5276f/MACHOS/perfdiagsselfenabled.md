## perfdiagsselfenabled

> `/usr/libexec/perfdiagsselfenabled`

```diff

-375.0.0.0.0
-  __TEXT.__text: 0xc828
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_stubs: 0xea0
-  __TEXT.__objc_methlist: 0xaa8
-  __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x15ba
-  __TEXT.__oslogstring: 0x1eaf
+378.0.0.0.0
+  __TEXT.__text: 0xc53c
+  __TEXT.__auth_stubs: 0x590
+  __TEXT.__objc_stubs: 0xe80
+  __TEXT.__objc_methlist: 0xa78
+  __TEXT.__const: 0x108
+  __TEXT.__cstring: 0x13bf
+  __TEXT.__oslogstring: 0x1fd0
   __TEXT.__objc_classname: 0xda
-  __TEXT.__objc_methtype: 0x55e
-  __TEXT.__objc_methname: 0x328d
+  __TEXT.__objc_methtype: 0x553
+  __TEXT.__objc_methname: 0x31b2
   __TEXT.__gcc_except_tab: 0x18
   __TEXT.__unwind_info: 0x270
-  __DATA_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__auth_got: 0x2d8
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x668
-  __DATA_CONST.__cfstring: 0x1720
+  __DATA_CONST.__const: 0x658
+  __DATA_CONST.__cfstring: 0x1560
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x1b10
-  __DATA.__objc_selrefs: 0x740
-  __DATA.__objc_ivar: 0x1b8
+  __DATA.__objc_const: 0x1ab0
+  __DATA.__objc_selrefs: 0x720
+  __DATA.__objc_ivar: 0x1b0
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x30
   __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/MetricKitSource.framework/MetricKitSource

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 79591D6F-E2FE-32C0-888B-11CEF5113501
-  Functions: 311
-  Symbols:   123
-  CStrings:  1019
+  UUID: 76D84733-475E-3B3B-895D-D522AD62CA1B
+  Functions: 306
+  Symbols:   121
+  CStrings:  985
 
Symbols:
- _ADClientAddValueForScalarKey
- _ADClientSetValueForScalarKey
CStrings:
+ "ConfigureTailspinForSelfEnableConfig: EPL is ACTIVE, do not attempt to configure tailspin"
+ "ConfigureTailspinForSelfEnableConfig: Failed to configure tailspin with desired configs."
+ "ConfigureTailspinForSelfEnableConfig: ThirdPartyDevEnablement is ACTIVE, do not attempt to configure tailspin"
+ "\xf0\xf0A!V!"
- "HangTracerEnableMemoryLogging"
- "HangTracerMemoryLoggingInterval"
- "TB,R,V_memoryLoggingEnabled"
- "TI,V_memoryLoggingIntervalSec"
- "_memoryLoggingEnabled"
- "_memoryLoggingIntervalSec"
- "com.apple.hangtracer.HTSE.EnabledToday"
- "com.apple.pdse.%@.DisableToDisable"
- "com.apple.pdse.%@.DisableToEnable"
- "com.apple.pdse.%@.DisableToEnable.Failed"
- "com.apple.pdse.%@.EnableToDisable"
- "com.apple.pdse.%@.EnableToDisable.Failed"
- "com.apple.pdse.%@.EnableToEnable"
- "com.apple.pdse.%@.EnableToday"
- "com.apple.pdse.%@.TimeoutForceDisable"
- "com.apple.pdse.AttemptConfigureTailspin"
- "com.apple.pdse.FailConfigureTailspin"
- "com.apple.pdse.NoConfigureTailspinDueToEPL"
- "initPropertyMemoryLoggingIntervalSec:"
- "memoryLoggingEnabled"
- "memoryLoggingIntervalSec"
- "setMemoryLoggingIntervalSec:"
- "v20@0:8I16"
- "\xf0\xf0Q!V!"

```
