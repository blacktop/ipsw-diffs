## PosterFoundation

> `/System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation`

```diff

-276.105.0.0.0
-  __TEXT.__text: 0x41850
+280.101.0.0.0
+  __TEXT.__text: 0x41f98
   __TEXT.__auth_stubs: 0x1020
-  __TEXT.__objc_methlist: 0x3110
+  __TEXT.__objc_methlist: 0x3168
   __TEXT.__const: 0x176
-  __TEXT.__cstring: 0x39d2
+  __TEXT.__cstring: 0x3b1d
   __TEXT.__oslogstring: 0x2d1a
   __TEXT.__gcc_except_tab: 0xf18
-  __TEXT.__unwind_info: 0x11e8
-  __TEXT.__objc_classname: 0x715
-  __TEXT.__objc_methname: 0x72bd
-  __TEXT.__objc_methtype: 0x124b
-  __TEXT.__objc_stubs: 0x5500
-  __DATA_CONST.__got: 0x4d0
-  __DATA_CONST.__const: 0x12f8
-  __DATA_CONST.__objc_classlist: 0x1a0
+  __TEXT.__unwind_info: 0x1200
+  __TEXT.__objc_classname: 0x728
+  __TEXT.__objc_methname: 0x73e7
+  __TEXT.__objc_methtype: 0x1273
+  __TEXT.__objc_stubs: 0x55c0
+  __DATA_CONST.__got: 0x4d8
+  __DATA_CONST.__const: 0x1330
+  __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d00
+  __DATA_CONST.__objc_selrefs: 0x1d48
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x178
-  __DATA_CONST.__objc_arraydata: 0xc8
+  __DATA_CONST.__objc_superrefs: 0x180
+  __DATA_CONST.__objc_arraydata: 0x120
   __AUTH_CONST.__auth_got: 0x820
-  __AUTH_CONST.__const: 0x8c0
-  __AUTH_CONST.__cfstring: 0x3860
-  __AUTH_CONST.__objc_const: 0x8078
-  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__const: 0x8e0
+  __AUTH_CONST.__cfstring: 0x39e0
+  __AUTH_CONST.__objc_const: 0x8180
+  __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x2d4
+  __AUTH.__objc_data: 0x500
+  __DATA.__objc_ivar: 0x2e0
   __DATA.__data: 0x850
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0xb90
   __DATA_DIRTY.__bss: 0x1e0
   __DATA_DIRTY.__common: 0xc

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9DC9DE35-1F76-3CCB-84E8-5FE9A9D89819
-  Functions: 1566
-  Symbols:   5502
-  CStrings:  2735
+  UUID: 0CC8E9D4-AD4F-3285-A1E0-A912860650D6
+  Functions: 1576
+  Symbols:   5535
+  CStrings:  2776
 
Symbols:
+ +[NSKeyedUnarchiver(PosterFoundation) pf_unarchivedObjectOfClasses:fromData:strict:classReplacementBlock:error:]
+ +[RBSAssertion(PosterFoundation) pf_extendRenderSessionWithReason:]
+ +[RBSAssertion(PosterFoundation) pf_extendRenderSessionWithReason:].cold.1
+ -[NSError(PosterFoundation) pf_jetsamReason]
+ -[PFDebounceFilter .cxx_destruct]
+ -[PFDebounceFilter allowEvent]
+ -[PFDebounceFilter initWithDebounceAfterEvents:withinTimeInterval:]
+ _OBJC_CLASS_$_PFDebounceFilter
+ _OBJC_IVAR_$_PFDebounceFilter._debounceAfterEvents
+ _OBJC_IVAR_$_PFDebounceFilter._eventTimestamps
+ _OBJC_IVAR_$_PFDebounceFilter._interval
+ _OBJC_METACLASS_$_PFDebounceFilter
+ __OBJC_$_INSTANCE_METHODS_PFDebounceFilter
+ __OBJC_$_INSTANCE_VARIABLES_PFDebounceFilter
+ __OBJC_CLASS_RO_$_PFDebounceFilter
+ __OBJC_METACLASS_RO_$_PFDebounceFilter
+ ___103+[NSKeyedUnarchiver(PosterFoundation) pf_unarchivedObjectOfClasses:fromData:classReplacementMap:error:]_block_invoke_2
+ ___30-[PFDebounceFilter allowEvent]_block_invoke
+ ___67+[RBSAssertion(PosterFoundation) pf_extendRenderSessionWithReason:]_block_invoke
+ ___block_descriptor_40_e8_32s_e27_v16?0"NSKeyedUnarchiver"8ls32l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ _kPRStaticDescriptorRenderingConfigurationKey
+ _objc_msgSend$_enableStrictSecureDecodingMode
+ _objc_msgSend$block:
+ _objc_msgSend$bundleID
+ _objc_msgSend$insertObject:atIndex:
+ _objc_msgSend$now
+ _objc_msgSend$pf_unarchivedObjectOfClasses:fromData:strict:classReplacementBlock:error:
+ _pf_extendRenderSessionWithReason:.onceToken
+ _pf_extendRenderSessionWithReason:.shouldUseFinishRenderEntitledAttribute
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_PosterFoundation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_PosterFoundation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_PosterFoundation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_PosterFoundation
CStrings:
+ "!"
+ "@32@0:8Q16d24"
+ "@52@0:8@16@24B32@?36o^@44"
+ "ENT"
+ "Entitled-"
+ "FinishRender"
+ "FinishRender-%@-%@"
+ "FinishRenderEntitled"
+ "PFDebounceFilter"
+ "PRPreferredRenderingConfiguration"
+ "_debounceAfterEvents"
+ "_enableStrictSecureDecodingMode"
+ "_eventTimestamps"
+ "_interval"
+ "allowEvent"
+ "bundleID"
+ "com.apple.MercuryPoster"
+ "com.apple.PosterKit"
+ "com.apple.WatchFacesWallpaperSupport.Unity2025Poster"
+ "com.apple.posterkit.entitled-finish-render"
+ "com.apple.transcriptBackgroundPoster.GradientExtension"
+ "initWithDebounceAfterEvents:withinTimeInterval:"
+ "insertObject:atIndex:"
+ "jetsam"
+ "now"
+ "pf_extendRenderSessionWithReason:"
+ "pf_jetsamReason"
+ "pf_unarchivedObjectOfClasses:fromData:strict:classReplacementBlock:error:"
+ "v16@?0@\"NSKeyedUnarchiver\"8"

```
