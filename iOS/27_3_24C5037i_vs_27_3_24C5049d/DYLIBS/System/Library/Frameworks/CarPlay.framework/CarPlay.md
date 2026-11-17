## CarPlay

> `/System/Library/Frameworks/CarPlay.framework/CarPlay`

```diff

-553.9.3.0.0
-  __TEXT.__text: 0x6e368
-  __TEXT.__objc_methlist: 0x9b60
+553.14.1.0.0
+  __TEXT.__text: 0x6ecec
+  __TEXT.__objc_methlist: 0x9be8
   __TEXT.__const: 0x562
-  __TEXT.__cstring: 0x5cb6
-  __TEXT.__oslogstring: 0x37c6
+  __TEXT.__cstring: 0x5cc6
+  __TEXT.__oslogstring: 0x37f6
   __TEXT.__gcc_except_tab: 0x934
   __TEXT.__constg_swiftt: 0x1f8
   __TEXT.__swift5_typeref: 0x13d

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_fieldmd: 0x7c
-  __TEXT.__unwind_info: 0x2838
+  __TEXT.__unwind_info: 0x2858
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1fa0
+  __DATA_CONST.__const: 0x2018
   __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4460
+  __DATA_CONST.__objc_selrefs: 0x4498
   __DATA_CONST.__objc_protorefs: 0x168
   __DATA_CONST.__objc_superrefs: 0x350
-  __DATA_CONST.__got: 0x878
-  __AUTH_CONST.__const: 0xbe8
-  __AUTH_CONST.__cfstring: 0x5880
-  __AUTH_CONST.__objc_const: 0x218d0
+  __DATA_CONST.__got: 0x888
+  __AUTH_CONST.__const: 0xc28
+  __AUTH_CONST.__cfstring: 0x58c0
+  __AUTH_CONST.__objc_const: 0x218f8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x7b8
   __AUTH.__objc_data: 0x98
   __DATA.__objc_ivar: 0xa48
-  __DATA.__data: 0x2110
+  __DATA.__data: 0x2120
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x2698
   __DATA_DIRTY.__data: 0x248

   - /System/Library/PrivateFrameworks/UserAlerts.framework/UserAlerts
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3408
-  Symbols:   6405
-  CStrings:  1125
+  Functions: 3422
+  Symbols:   6425
+  CStrings:  1129
 
Symbols:
+ +[CPListImageRowItemCondensedElement _setMaximumImageSize:]
+ +[CPListImageRowItemGridElement _setMaximumImageSize:]
+ +[CPListImageRowItemImageGridElement _setMaximumImageSize:]
+ +[CPListTemplate _setSupportsPlaybackConfirmationBlock:]
+ +[CPSessionConfiguration _setHostSupportsVideoPlayback:]
+ GCC_except_table140
+ GCC_except_table32
+ GCC_except_table40
+ GCC_except_table53
+ GCC_except_table62
+ GCC_except_table82
+ __OBJC_$_CLASS_METHODS_CPSessionConfiguration
+ ___66-[CPInterfaceController _configureTemplateProviderWithCompletion:]_block_invoke_11
+ ___66-[CPInterfaceController _configureTemplateProviderWithCompletion:]_block_invoke_12
+ ___66-[CPInterfaceController _configureTemplateProviderWithCompletion:]_block_invoke_13
+ ___95-[CPListTemplate listTemplateWithIdentifier:didSelectListItemWithIdentifier:completionHandler:]_block_invoke_2
+ ___96-[CPListTemplate listTemplateWithIdentifier:didSelectImageAtIndex:inImageRowItemWithIdentifier:]_block_invoke_2
+ ___96-[CPListTemplate listTemplateWithIdentifier:didSelectImageAtIndex:inImageRowItemWithIdentifier:]_block_invoke_3
+ ___block_descriptor_32_e8_v12?0B8l
+ ___block_descriptor_48_e8_32bs40bs_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ __hostSupportsVideoPlayback
+ __supportsPlaybackConfirmationBlock
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_CarPlay
- GCC_except_table135
- GCC_except_table28
- GCC_except_table31
- GCC_except_table52
- GCC_except_table61
CStrings:
+ "Server %@ playback confirmation block"
+ "Server %@ video playback"
+ "does not support"
+ "supports"
```
