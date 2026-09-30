## appleh16camerad

> `/usr/sbin/appleh16camerad`

```diff

-5.311.0.0.0
-  __TEXT.__text: 0x83c6c
-  __TEXT.__auth_stubs: 0x2030
-  __TEXT.__objc_stubs: 0x1460
-  __TEXT.__init_offsets: 0x14
+5.401.2.0.0
+  __TEXT.__text: 0x7f690
+  __TEXT.__auth_stubs: 0x1f70
+  __TEXT.__objc_stubs: 0x1400
   __TEXT.__objc_methlist: 0x268
-  __TEXT.__gcc_except_tab: 0x233c
-  __TEXT.__const: 0x2e10
-  __TEXT.__cstring: 0x8b7f
+  __TEXT.__gcc_except_tab: 0x2198
+  __TEXT.__const: 0x2db0
+  __TEXT.__cstring: 0x8e73
   __TEXT.__objc_classname: 0x89
-  __TEXT.__oslogstring: 0x5df3
-  __TEXT.__objc_methname: 0x15c5
+  __TEXT.__oslogstring: 0x5dfe
+  __TEXT.__objc_methname: 0x1582
   __TEXT.__objc_methtype: 0x10b3
-  __TEXT.__unwind_info: 0x15d8
-  __DATA_CONST.__auth_got: 0x1028
-  __DATA_CONST.__got: 0xbe0
+  __TEXT.__unwind_info: 0x15b0
+  __DATA_CONST.__auth_got: 0xfc8
+  __DATA_CONST.__got: 0xbc8
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0xb6d0
-  __DATA_CONST.__cfstring: 0x3380
+  __DATA_CONST.__const: 0xb710
+  __DATA_CONST.__cfstring: 0x3360
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA.__objc_const: 0x5a8
-  __DATA.__objc_selrefs: 0x630
+  __DATA.__objc_selrefs: 0x618
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x371d80
-  __DATA.__bss: 0x231
-  __DATA.__common: 0x5c
+  __DATA.__data: 0x371da0
+  __DATA.__common: 0x14
+  __DATA.__bss: 0x91
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 882AE7DC-D6DA-3FB9-B838-C4CF440E8FB0
-  Functions: 1654
-  Symbols:   921
-  CStrings:  2459
+  UUID: 5DFF6D8C-8F58-3DC7-9C1B-ED285084A61D
+  Functions: 1694
+  Symbols:   906
+  CStrings:  2446
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ ___cxa_guard_abort
+ _objc_autoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
- _CFArrayCreate
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev
- __ZNSt3__113basic_filebufIcNS_11char_traitsIcEEE5closeEv
- __ZNSt3__113basic_filebufIcNS_11char_traitsIcEEEC1Ev
- __ZNSt3__113basic_filebufIcNS_11char_traitsIcEEED1Ev
- __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE3putEc
- __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE5flushEv
- __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE5writeEPKcl
- __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEf
- __ZNSt3__114basic_ofstreamIcNS_11char_traitsIcEEE4openERKNS_12basic_stringIcS2_NS_9allocatorIcEEEEj
- __ZNSt3__18ios_base4initEPv
- __ZNSt3__19basic_iosIcNS_11char_traitsIcEEED2Ev
- __ZTTNSt3__114basic_ofstreamIcNS_11char_traitsIcEEEE
- __ZTVNSt3__114basic_ofstreamIcNS_11char_traitsIcEEEE
- ___cxa_atexit
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_storeStrong
CStrings:
+ ".plist"
+ "/AppleInternal/Library/BuildRoots/4~CIU2ugD6nh0yefN3eB1XenYs2P16wqN6VJRpZGM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU2ugD6nh0yefN3eB1XenYs2P16wqN6VJRpZGM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU2ugD6nh0yefN3eB1XenYs2P16wqN6VJRpZGM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "5.401.2"
+ "Jasper Calibration: Cannot run ToF-Color infield calibration on this frame (%d). Will try again on next frame\n"
+ "reference"
- ""
- ","
- ".pb"
- "5.311"
- "ColorF32.bin"
- "Cost grid "
- "Could not open file ["
- "Jasper Calibration: algoExecutorpreProcessInputColorFrame failed with error: %d, trying to recover\n"
- "] for writing.\n"
- "_Debug.plist"
- "defaultCStringEncoding"
- "fileExistsAtPath:isDirectory:"
- "fineGridRes"
- "fullImgGridRes"
- "fullImgGridResPostNormal"
- "fullImgLocalGrid"
- "pathExtension"
- "roiGridRes"
- "roiGridResPostNormal"
- "roiLocalGrid"

```
