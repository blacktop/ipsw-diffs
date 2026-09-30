## AudioDSPGraph

> `/System/Library/PrivateFrameworks/AudioDSPGraph.framework/AudioDSPGraph`

```diff

-47.0.0.0.0
-  __TEXT.__text: 0xacb30
-  __TEXT.__auth_stubs: 0x17f0
+48.102.0.0.0
+  __TEXT.__text: 0xacc70
+  __TEXT.__auth_stubs: 0x17e0
   __TEXT.__objc_methlist: 0x15b0
-  __TEXT.__const: 0x3a74
+  __TEXT.__const: 0x3aa4
   __TEXT.__swift5_typeref: 0x8
   __TEXT.__gcc_except_tab: 0xb2a8
   __TEXT.__oslogstring: 0x1e76
-  __TEXT.__cstring: 0xced2
+  __TEXT.__cstring: 0xcee2
   __TEXT.__unwind_info: 0x4138
   __TEXT.__eh_frame: 0x2c8
   __TEXT.__objc_classname: 0x5c3

   __TEXT.__objc_methtype: 0x4383
   __TEXT.__objc_stubs: 0x1ca0
   __DATA_CONST.__got: 0x4b8
-  __DATA_CONST.__const: 0x38d0
+  __DATA_CONST.__const: 0x38b0
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x8f0
   __DATA_CONST.__objc_superrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0xc08
+  __AUTH_CONST.__auth_got: 0xc00
   __AUTH_CONST.__const: 0x8ed0
-  __AUTH_CONST.__cfstring: 0xdc0
+  __AUTH_CONST.__cfstring: 0xde0
   __AUTH_CONST.__objc_const: 0x2b08
   __AUTH.__objc_data: 0xc30
   __AUTH.__data: 0x68
   __DATA.__objc_ivar: 0xd8
   __DATA.__data: 0x408
-  __DATA.__bss: 0x2840
+  __DATA.__bss: 0x2858
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
-  UUID: 781AFEC5-2B10-395C-B177-A71B24A0AEC4
+  UUID: B71375EB-57D2-3D44-92D4-983E134E9551
   Functions: 2963
-  Symbols:   8238
-  CStrings:  1981
+  Symbols:   8231
+  CStrings:  1983
 
Symbols:
+ __ZGVZN2CA3DSP10AUDSPGraph12GetMessengerEvE10sMessenger
+ __ZZN2CA3DSP10AUDSPGraph12GetMessengerEvE10sMessenger
- __ZN5caulk10concurrent9messengerD1Ev
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_AudioDSPGraph
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AudioDSPGraph
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AudioDSPGraph
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AudioDSPGraph
Functions:
~ __ZN2CA3DSP10AUDSPGraphD2Ev : 696 -> 688
~ __ZN5ausdk9APFactoryINS_27AUBaseProcessMultipleLookupEN2CA3DSP10AUDSPGraphEE9ConstructEPvP28OpaqueAudioComponentInstance : 2120 -> 2184
~ -[CADSPGraph initWithModel:error:] : 9316 -> 9328
~ __ZNSt3__110__function6__funcIZN13AudioDSPGraph11BoxRegistryC1EvE4$_29NS_9allocatorIS4_EEFNS_10unique_ptrINS2_3BoxENS_14default_deleteIS8_EEEENS_12basic_stringIcNS_11char_traitsIcEENS5_IcEEEEjjEEclEOSG_OjSK_ : 464 -> 460
~ __ZN13AudioDSPGraph5Boxes21ParameterSmoothingBox7processEj : 372 -> 428
~ __ZN13AudioDSPGraph5Boxes21ParameterSmoothingBox16getParameterInfoEjj : 404 -> 464
~ __ZN13AudioDSPGraph5Boxes21ParameterSmoothingBox16getParameterListEj : 84 -> 180
~ __ZN13AudioDSPGraph5Boxes21ParameterSmoothingBox12getParameterEjjj : 176 -> 192
~ __ZN13AudioDSPGraph5Boxes21ParameterSmoothingBox12setParameterEjjjfj : 176 -> 204
CStrings:
+ "Attack Time (sec)"
+ "Release Time (sec)"
- "Smoothing Time (sec)"

```
