## NearbyInteraction

> `/System/Library/Frameworks/NearbyInteraction.framework/Versions/A/NearbyInteraction`

```diff

-568.0.0.0.0
-  __TEXT.__text: 0x3716c
-  __TEXT.__objc_methlist: 0x4208
-  __TEXT.__gcc_except_tab: 0x57b4
-  __TEXT.__cstring: 0x5275
+575.0.5.0.0
+  __TEXT.__text: 0x36924
+  __TEXT.__objc_methlist: 0x4220
+  __TEXT.__gcc_except_tab: 0x5798
+  __TEXT.__cstring: 0x5116
   __TEXT.__const: 0x500
   __TEXT.__oslogstring: 0xf2d
   __TEXT.__swift5_typeref: 0x83

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x2250
-  __TEXT.__eh_frame: 0x108
+  __TEXT.__unwind_info: 0x2228
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ea8
+  __DATA_CONST.__objc_selrefs: 0x1eb8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__got: 0x2b8
   __AUTH_CONST.__const: 0xb88
-  __AUTH_CONST.__cfstring: 0x5a20
-  __AUTH_CONST.__objc_const: 0x7d00
+  __AUTH_CONST.__cfstring: 0x5a60
+  __AUTH_CONST.__objc_const: 0x7d30
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x3d0
+  __AUTH_CONST.__auth_got: 0x370
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x4fc
+  __DATA.__objc_ivar: 0x500
   __DATA.__data: 0x4f0
   __DATA.__common: 0x12d
   __DATA_DIRTY.__objc_data: 0x10e0
-  __DATA_DIRTY.__bss: 0x68
+  __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1553
-  Symbols:   3540
-  CStrings:  930
+  Functions: 1549
+  Symbols:   3524
+  CStrings:  915
 
Symbols:
+ -[NINearbyObject setSuggestedNearbyThreshold:]
+ -[NINearbyObject suggestedNearbyThreshold]
+ GCC_except_table107
+ OBJC_IVAR_$_NINearbyObject._suggestedNearbyThreshold
+ _objc_msgSend$suggestedNearbyThreshold
- __MergedGlobals
- ___isOSVersionAtLeast
- ___isPlatformOrVariantPlatformVersionAtLeast
- ___isPlatformVersionAtLeast
- __availability_version_check
- __initializeAvailabilityCheck
- __isPlatformOrVariantPlatformVersionAtLeast
- _compatibilityInitializeAvailabilityCheck
- _dispatch_once_f
- _dlsym
- _fclose
- _fopen
- _fread
- _free
- _fseek
- _ftell
- _initializeAvailabilityCheck
- _malloc
- _objc_msgSend$initWithAnchorAddress:measurementType:coordinatesType:transmitTime:receiveTime:signalStrength:carrierFrequencyOffset:coordinates:
- _rewind
- _sscanf
CStrings:
+ ", Suggested Nearby Threshold: %@"
+ "suggestedNearbyThreshold"
- "%d.%d.%d"
- "/System/Library/CoreServices/SystemVersion.plist"
- "CFDataCreateWithBytesNoCopy"
- "CFDictionaryGetValue"
- "CFGetTypeID"
- "CFPropertyListCreateFromXMLData"
- "CFPropertyListCreateWithData"
- "CFRelease"
- "CFStringCreateWithCStringNoCopy"
- "CFStringGetCString"
- "CFStringGetTypeID"
- "Platform2 == PLATFORM_MACOS && \"unexpected platform\""
- "ProductVersion"
- "__isPlatformOrVariantPlatformVersionAtLeast"
- "kCFAllocatorNull"
- "os_version_check.c"
- "r"
```
