## SiriAudioSupport

> `/System/Library/PrivateFrameworks/SiriAudioSupport.framework/SiriAudioSupport`

```diff

-3401.14.1.0.0
-  __TEXT.__text: 0x21b454
-  __TEXT.__auth_stubs: 0x3850
-  __TEXT.__objc_methlist: 0x808
+3401.19.1.0.0
+  __TEXT.__text: 0x21af00
+  __TEXT.__auth_stubs: 0x37c0
+  __TEXT.__objc_methlist: 0x81c
   __TEXT.__const: 0x93c8
-  __TEXT.__cstring: 0xb1d5
+  __TEXT.__cstring: 0xb090
   __TEXT.__swift5_typeref: 0x3fa5
   __TEXT.__swift5_fieldmd: 0x4268
   __TEXT.__constg_swiftt: 0x5954

   __TEXT.__swift5_proto: 0x548
   __TEXT.__swift5_types: 0x408
   __TEXT.__swift5_capture: 0x54e4
-  __TEXT.__oslogstring: 0x1fede
+  __TEXT.__oslogstring: 0x1fdce
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4600
-  __TEXT.__eh_frame: 0x259c
-  __TEXT.__objc_classname: 0x180
-  __TEXT.__objc_methname: 0x61b8
+  __TEXT.__unwind_info: 0x45e8
+  __TEXT.__eh_frame: 0x2524
+  __TEXT.__objc_classname: 0x19c
+  __TEXT.__objc_methname: 0x61d2
   __TEXT.__objc_methtype: 0x5c5
-  __DATA_CONST.__got: 0x10f0
+  __DATA_CONST.__got: 0x10f8
   __DATA_CONST.__const: 0x810
-  __DATA_CONST.__objc_classlist: 0x2d8
+  __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cc0
+  __DATA_CONST.__objc_selrefs: 0x1cc8
   __DATA_CONST.__objc_protorefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x1c28
-  __AUTH_CONST.__auth_ptr: 0x1588
-  __AUTH_CONST.__const: 0x14f30
+  __AUTH_CONST.__auth_got: 0x1be0
+  __AUTH_CONST.__auth_ptr: 0x15a0
+  __AUTH_CONST.__const: 0x14f80
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0xb198
-  __AUTH.__objc_data: 0xfb8
-  __AUTH.__data: 0x5a08
-  __DATA.__data: 0x2c00
-  __DATA.__bss: 0x6f38
+  __AUTH_CONST.__objc_const: 0xb228
+  __AUTH.__objc_data: 0x1008
+  __AUTH.__data: 0x5a00
+  __DATA.__data: 0x2c18
+  __DATA.__bss: 0x6f10
   __DATA.__common: 0x270
   __DATA_DIRTY.__objc_data: 0xd0
   __DATA_DIRTY.__data: 0x28

   - /System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers
   - /System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals
   - /System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities
+  - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8439
-  Symbols:   1009
-  CStrings:  4097
+  Functions: 8437
+  Symbols:   1001
+  CStrings:  4080
 
Symbols:
+ _OBJC_METACLASS_$_SiriAudioSpringBoardService
+ _SBSIsSystemApertureAvailable
+ _OBJC_CLASS_$_SiriAudioSpringBoardService
- _swift_taskGroup_wait_next_throwing
- _dlsym
- _fseek
- _fclose
- _rewind
- _sscanf
- _fread
- _ftell
- _fopen
- _dispatch_once_f
- __availability_version_check
CStrings:
+ "isSystemApertureAvailable"
+ "SiriEnvironmentWrapper#mockSystemAperture This should only happen in unit tests."
+ "SiriAudioSpringBoardService"
+ "SiriEnvironmentWrapper#mockSystemAperture This should only be called in unit tests."
- "CFPropertyListCreateFromXMLData"
- "CFPropertyListCreateWithData"
- "SystemApertureCachedValue#update count is now: %!l(MISSING)d"
- "SystemApertureCachedValue#start persisting value for the next request as: %!{(MISSING)bool}d"
- "kCFAllocatorNull"
- "r"
- "CFStringGetCString"
- "ProductVersion"
- "CFRelease"
- "%!d(MISSING).%!d(MISSING).%!d(MISSING)"
- "CFDictionaryGetValue"
- "SystemApertureCachedValue#update updating SystemAperture cached value."
- "CFStringGetTypeID"
- "SystemApertureCachedValue#isSystemApertureEnabled returning value from current request."
- "CFStringCreateWithCStringNoCopy"
- "CFDataCreateWithBytesNoCopy"
- "CFGetTypeID"
- "_Concurrency/TaskGroup.swift"
- "SystemApertureCachedValue#isSystemApertureEnabled returning cached Value"
- "/System/Library/CoreServices/SystemVersion.plist"
- "SystemApertureCachedValue#update value expired"

```
