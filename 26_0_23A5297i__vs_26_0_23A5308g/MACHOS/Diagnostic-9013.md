## Diagnostic-9013

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-9013.appex/Diagnostic-9013`

```diff

-921.0.98.0.0
-  __TEXT.__text: 0x11f4
-  __TEXT.__auth_stubs: 0x210
-  __TEXT.__objc_stubs: 0x220
-  __TEXT.__objc_methlist: 0x98
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x46
-  __TEXT.__oslogstring: 0x229
-  __TEXT.__objc_classname: 0x18
-  __TEXT.__objc_methname: 0x1d3
-  __TEXT.__objc_methtype: 0x9f
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0x110
-  __DATA_CONST.__got: 0x50
+921.0.119.0.0
+  __TEXT.__text: 0x360
+  __TEXT.__auth_stubs: 0x120
+  __TEXT.__objc_stubs: 0xe0
+  __TEXT.__objc_methlist: 0x2c
+  __TEXT.__const: 0x48
+  __TEXT.__cstring: 0x3d
+  __TEXT.__oslogstring: 0x1a
+  __TEXT.__objc_classname: 0xa
+  __TEXT.__objc_methname: 0x89
+  __TEXT.__objc_methtype: 0x13
+  __TEXT.__unwind_info: 0x78
+  __DATA_CONST.__auth_got: 0x98
+  __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0x20
-  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xd0
-  __DATA.__objc_selrefs: 0xb8
-  __DATA.__objc_data: 0x50
+  __DATA.__objc_const: 0x40
+  __DATA.__objc_selrefs: 0x48
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CA3F7EEF-2119-354C-82C8-A924B5FB69DA
-  Functions: 23
-  Symbols:   56
-  CStrings:  55
+  UUID: F66C62CC-61C5-391B-AF38-E769F17AAB67
+  Functions: 6
+  Symbols:   31
+  CStrings:  20
 
Symbols:
- _IOConnectCallScalarMethod
- _IOConnectCallStructMethod
- _IOObjectRelease
- _IOServiceClose
- _IOServiceGetMatchingService
- _IOServiceMatching
- _IOServiceOpen
- _OBJC_CLASS_$_NSNumber
- _OBJC_CLASS_$_NSObject
- _OBJC_CLASS_$_NSThread
- _OBJC_CLASS_$_SmcController
- _OBJC_METACLASS_$_NSObject
- _OBJC_METACLASS_$_SmcController
- ___stack_chk_fail
- ___stack_chk_guard
- __objc_empty_cache
- __os_log_impl
- _kIOMainPortDefault
- _mach_task_self_
- _memcpy
- _objc_alloc
- _objc_autorelease
- _objc_release_x21
- _objc_release_x25
- _objc_retain_x3
CStrings:
- "AppleSMC"
- "B28@0:8I16@20"
- "Failed to covert from valueBuffer to byteData"
- "Failed to open SMC, error: %d, retrying..."
- "Failed to read SMC key %@, error: %d"
- "Failed to write data to key %@, error: 0x%x"
- "No info found for key '%s' (0x%X, 0x%X)\n"
- "Read failed for key '%s' (0x%X, 0x%X)\n"
- "SMC key(%@) reading failed, error: 0x%x"
- "SmcController"
- "UTF8String"
- "Write failed for key '%s' (0x%X, 0x%X)\n"
- "Write succeed for key '%s', value returned = 0x%X"
- "buffer overflow on string/key conversion"
- "closeAppleSMC:"
- "destination for key read does not match expected size (Key: '%s', Expected Size: %u, Supplied Size: %lu)\n"
- "i20@0:8I16"
- "i28@0:8^I16S24"
- "i28@0:8i16^I20"
- "i36@0:8I16@20^@28"
- "i40@0:8I16I20^v24Q32"
- "i44@0:8I16@20^v28Q36"
- "i48@0:8I16I20^v24Q32^I40"
- "initWithBytes:length:"
- "isSMCKeyAvalible:keyName:"
- "lengthOfBytesUsingEncoding:"
- "numberWithChar:"
- "numberWithInt:"
- "openAppleSMC:port:"
- "openAppleSMC:withRetry:"
- "readSMCKey:key:readData:dataSize:oSize:"
- "readSMCKey:keyName:rval:"
- "sleepForTimeInterval:"
- "writeSMCKey:key:writeData:dataSize:"
- "writeSMCKey:keyName:data:size:"

```
