## NearbyInteraction

> `/System/Library/Frameworks/NearbyInteraction.framework/Versions/A/NearbyInteraction`

```diff

-568.0.0.0.0
-  __TEXT.__text: 0x38260
-  __TEXT.__objc_methlist: 0x4208
-  __TEXT.__gcc_except_tab: 0x57b4
-  __TEXT.__cstring: 0x5275
+575.0.10.0.0
+  __TEXT.__text: 0x37f9c
+  __TEXT.__objc_methlist: 0x4278
+  __TEXT.__gcc_except_tab: 0x5834
+  __TEXT.__cstring: 0x5175
   __TEXT.__const: 0x500
-  __TEXT.__oslogstring: 0xf2d
+  __TEXT.__oslogstring: 0xfc5
   __TEXT.__swift5_typeref: 0x83
   __TEXT.__swift5_reflstr: 0x4b
   __TEXT.__swift5_assocty: 0x48

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x20a8
-  __TEXT.__eh_frame: 0x100
+  __TEXT.__unwind_info: 0x20c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5a0
+  __DATA_CONST.__const: 0x5b8
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ea8
+  __DATA_CONST.__objc_selrefs: 0x1ef0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__got: 0x2b8
   __AUTH_CONST.__const: 0xb88
-  __AUTH_CONST.__cfstring: 0x5a20
-  __AUTH_CONST.__objc_const: 0x7d00
+  __AUTH_CONST.__cfstring: 0x5a80
+  __AUTH_CONST.__objc_const: 0x7da8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x3d0
+  __AUTH_CONST.__auth_got: 0x370
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x4fc
-  __DATA.__data: 0x4f0
+  __DATA.__objc_ivar: 0x500
+  __DATA.__data: 0xd0
   __DATA.__common: 0x12d
   __DATA.__bss: 0x580
-  __DATA_DIRTY.__objc_data: 0x10e0
-  __DATA_DIRTY.__bss: 0x68
+  __DATA_DIRTY.__objc_data: 0x1180
+  __DATA_DIRTY.__data: 0x428
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
+  Functions: 1554
+  Symbols:   3541
+  CStrings:  920
 
Symbols:
+ +[NIPlatformInfo supportsDeviceCVPerception]
+ -[NINearbyObject setSuggestedNearbyThreshold:]
+ -[NINearbyObject suggestedNearbyThreshold]
+ -[NISession didUpdateDeviceAssociationStatus:]
+ -[NISession object:didUpdateCVDistance:]
+ -[NISession object:didUpdateCVRegion:previousRegion:]
+ GCC_except_table107
+ GCC_except_table118
+ GCC_except_table149
+ GCC_except_table154
+ GCC_except_table163
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table179
+ GCC_except_table181
+ GCC_except_table184
+ GCC_except_table186
+ GCC_except_table201
+ GCC_except_table202
+ GCC_except_table203
+ GCC_except_table204
+ GCC_except_table205
+ GCC_except_table217
+ GCC_except_table218
+ GCC_except_table221
+ GCC_except_table234
+ GCC_except_table237
+ GCC_except_table250
+ GCC_except_table253
+ GCC_except_table257
+ GCC_except_table258
+ GCC_except_table260
+ GCC_except_table268
+ GCC_except_table282
+ GCC_except_table289
+ GCC_except_table291
+ GCC_except_table296
+ GCC_except_table301
+ GCC_except_table310
+ GCC_except_table320
+ GCC_except_table323
+ GCC_except_table324
+ GCC_except_table338
+ GCC_except_table341
+ GCC_except_table345
+ GCC_except_table346
+ GCC_except_table348
+ GCC_except_table349
+ GCC_except_table359
+ GCC_except_table80
+ GCC_except_table81
+ OBJC_IVAR_$_NINearbyObject._suggestedNearbyThreshold
+ ___40-[NISession object:didUpdateCVDistance:]_block_invoke
+ ___46-[NISession didUpdateDeviceAssociationStatus:]_block_invoke
+ ___53-[NISession object:didUpdateCVRegion:previousRegion:]_block_invoke
+ _objc_msgSend$session:didUpdateDeviceAssociationStatus:
+ _objc_msgSend$session:object:didUpdateCVDistance:
+ _objc_msgSend$session:object:didUpdateCVRegion:previousRegion:
+ _objc_msgSend$suggestedNearbyThreshold
- GCC_except_table124
- GCC_except_table125
- GCC_except_table155
- GCC_except_table160
- GCC_except_table175
- GCC_except_table193
- GCC_except_table195
- GCC_except_table196
- GCC_except_table197
- GCC_except_table198
- GCC_except_table206
- GCC_except_table207
- GCC_except_table208
- GCC_except_table209
- GCC_except_table210
- GCC_except_table211
- GCC_except_table223
- GCC_except_table230
- GCC_except_table233
- GCC_except_table252
- GCC_except_table262
- GCC_except_table266
- GCC_except_table267
- GCC_except_table276
- GCC_except_table280
- GCC_except_table283
- GCC_except_table288
- GCC_except_table295
- GCC_except_table297
- GCC_except_table299
- GCC_except_table308
- GCC_except_table322
- GCC_except_table326
- GCC_except_table335
- GCC_except_table336
- GCC_except_table337
- GCC_except_table347
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
+ "DelegateProxy: updated cv distance: %.3f. Object: %{private}@"
+ "DelegateProxy: updated cv region %{private}@ (previous: %{private}@). Object: %{private}@"
+ "HomeKit Accessory Control Devices"
+ "HomeKit Accessory Control Devices | Known Devices"
+ "Perception"
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
