## modelmanagerd

> `/usr/libexec/modelmanagerd`

```diff

-122.40.11.0.0
-  __TEXT.__text: 0x1135e8
-  __TEXT.__auth_stubs: 0x2d80
-  __TEXT.__const: 0x24c0
-  __TEXT.__cstring: 0x25dc
-  __TEXT.__swift5_typeref: 0x1932
-  __TEXT.__swift5_capture: 0xa70
+122.40.14.0.0
+  __TEXT.__text: 0x1149dc
+  __TEXT.__auth_stubs: 0x2cf0
+  __TEXT.__const: 0x2578
+  __TEXT.__cstring: 0x2584
+  __TEXT.__swift5_typeref: 0x1938
+  __TEXT.__swift5_capture: 0xa84
   __TEXT.__objc_methname: 0x418
-  __TEXT.__oslogstring: 0x5e25
+  __TEXT.__oslogstring: 0x6145
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1c04
+  __TEXT.__constg_swiftt: 0x1c50
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x1372
-  __TEXT.__swift5_fieldmd: 0x11d8
-  __TEXT.__swift5_types: 0x100
+  __TEXT.__swift5_reflstr: 0x13f3
+  __TEXT.__swift5_fieldmd: 0x1224
+  __TEXT.__swift5_types: 0x104
   __TEXT.__swift5_protos: 0x50
-  __TEXT.__swift5_proto: 0x1f0
+  __TEXT.__swift5_proto: 0x1fc
   __TEXT.__swift5_assocty: 0xd0
   __TEXT.__objc_classname: 0x5b
   __TEXT.__objc_methtype: 0x191
-  __TEXT.__unwind_info: 0x4bd0
-  __TEXT.__eh_frame: 0xf4ec
-  __DATA_CONST.__auth_got: 0x16c0
-  __DATA_CONST.__got: 0xbf0
-  __DATA_CONST.__auth_ptr: 0x8e8
-  __DATA_CONST.__const: 0x28f0
+  __TEXT.__unwind_info: 0x4c00
+  __TEXT.__eh_frame: 0xf598
+  __DATA_CONST.__auth_got: 0x1678
+  __DATA_CONST.__got: 0xbd0
+  __DATA_CONST.__auth_ptr: 0x928
+  __DATA_CONST.__const: 0x29b0
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA.__objc_const: 0x2990
+  __DATA.__objc_const: 0x29d0
   __DATA.__objc_selrefs: 0x138
   __DATA.__objc_data: 0x4b0
-  __DATA.__data: 0x4cc8
-  __DATA.__common: 0x498
-  __DATA.__bss: 0x36c8
+  __DATA.__data: 0x4d18
+  __DATA.__common: 0x4a8
+  __DATA.__bss: 0x3820
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5115
-  Symbols:   1262
-  CStrings:  743
+  Functions: 5125
+  Symbols:   1250
+  CStrings:  747
 
Symbols:
+ _$sSo18OS_dispatch_sourceC8DispatchE19MemoryPressureEventV8rawValueAESu_tcfC
+ _$s6Darwin5errnos5Int32Vvg
+ _sysctlbyname
+ _$ss10SetAlgebraP10isSuperset2ofSbx_tFTj
- _dispatch_once_f
- _swift_unexpectedError
- _$sSo18OS_dispatch_sourceC8DispatchE19MemoryPressureEventVSQACMc
- __availability_version_check
- _fseek
- _fread
- _fclose
- _sscanf
- _$sSo18OS_dispatch_sourceC8DispatchE19MemoryPressureEventVSYACMc
- _$sScG4next9isolationxSgScA_pSgYi_tYaF
- _$sScG4next9isolationxSgScA_pSgYi_tYaFTu
- _swift_taskGroup_wait_next_throwing
- _dlsym
- _ftell
- _rewind
- _fopen
CStrings:
+ "Critical Memory Pressure Event Loop"
+ "kern.memorystatus_vm_pressure_level: %!l(MISSING)u"
+ "Dispatch memory pressure source cancelled"
+ "Failed to query current kernel memory pressure. Assuming non-critical."
+ "Cancelling critical memory pressure watchdog"
+ "Critical memory pressure watchdog fired, but no assertion found."
+ "kernel memory pressure unknown!"
+ "sysctlbyname(\"kern.memorystatus_vm_pressure_level\") failed: %!{(MISSING)darwin.errno}d"
+ "kern.memorystatus_vm_pressure_level contains system memory pressure: %!l(MISSING)u"
+ "Unknown memory pressure event"
+ "criticalMemoryPressureWatchdogTask"
+ "criticalMemoryPressureWatchdogInterval"
+ "Received dispatch memory pressure event: %!s(MISSING)"
+ "Fetched memory pressure directly from kernel: %!s(MISSING)"
+ "kern.memorystatus_vm_pressure_level"
+ "Memory pressure events ended"
+ "Critical Memory Pressure Watchdog"
+ "Kernel memory pressure (%!s(MISSING)) no longer critical when watchdog fired."
+ "Dispatch memory pressure event stream cancelled"
- "CFPropertyListCreateFromXMLData"
- "/System/Library/CoreServices/SystemVersion.plist"
- "CFRelease"
- "_Concurrency/TaskGroup.swift"
- "CFStringGetTypeID"
- "r"
- "CFDictionaryGetValue"
- "CFStringCreateWithCStringNoCopy"
- "CFDataCreateWithBytesNoCopy"
- "CFGetTypeID"
- "ProductVersion"
- "%!d(MISSING).%!d(MISSING).%!d(MISSING)"
- "CFStringGetCString"
- "kCFAllocatorNull"
- "CFPropertyListCreateWithData"

```
