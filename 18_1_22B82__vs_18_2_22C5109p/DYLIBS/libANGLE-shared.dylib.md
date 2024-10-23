## libANGLE-shared.dylib

> `/System/Library/PrivateFrameworks/WebCore.framework/Frameworks/libANGLE-shared.dylib`

```diff

-619.2.8.10.7
-  __TEXT.__text: 0x269260
-  __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__const: 0x86410
-  __TEXT.__cstring: 0x479e3
-  __TEXT.__gcc_except_tab: 0x2d7c
+620.1.11.10.8
+  __TEXT.__text: 0x266f94
+  __TEXT.__auth_stubs: 0xe10
+  __TEXT.__const: 0x87db0
+  __TEXT.__cstring: 0x474b4
+  __TEXT.__gcc_except_tab: 0x2e40
   __TEXT.__oslogstring: 0xf
-  __TEXT.__unwind_info: 0x18e0
+  __TEXT.__unwind_info: 0x1960
   __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x1726
-  __TEXT.__objc_stubs: 0x1e20
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x17268
+  __TEXT.__objc_methname: 0x17fd
+  __TEXT.__objc_stubs: 0x1f00
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__const: 0x17248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x788
-  __AUTH_CONST.__auth_got: 0x708
+  __DATA_CONST.__objc_selrefs: 0x7c0
+  __AUTH_CONST.__auth_got: 0x718
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x169e8
+  __AUTH_CONST.__const: 0x16b98
   __AUTH_CONST.__cfstring: 0x9e0
   __DATA.__data: 0x2ee18
-  __DATA.__common: 0x368
-  __DATA.__bss: 0x10
-  __DATA_DIRTY.__data: 0x12f8
+  __DATA.__common: 0x378
+  __DATA.__bss: 0x4
+  __DATA_DIRTY.__data: 0xfd8
   __DATA_DIRTY.__common: 0x4a0
   __DATA_DIRTY.__bss: 0x288
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9506
-  Symbols:   9882
-  CStrings:  8057
+  Functions: 9520
+  Symbols:   9893
+  CStrings:  8055
 
Symbols:
+ __ZNSt3__113random_deviceC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __ZNSt3__113random_deviceD1Ev
+ __ZNSt3__113random_deviceclEv
+ ___cxa_guard_abort
- __ZTTNSt3__114basic_ofstreamIcNS_11char_traitsIcEEEE
- __ZTVNSt3__114basic_ofstreamIcNS_11char_traitsIcEEEE
- _objc_release_x9
- _printf
CStrings:
+ "\ntemplate <typename T, int Cols, int Rows>\nANGLE_ALWAYS_INLINE thread metal::matrix<T, Cols, Rows> &operator/=(thread metal::matrix<T, Cols, Rows> &a, metal::matrix<T, Cols, Rows> b)\n{\n    a = a / b;\n    return a;\n}\n\n"
+ "/Library/Caches/com.apple.xbs/Sources/ANGLE/Source/ThirdParty/ANGLE/src/compiler/translator/IntermNode.cpp"
+ "/dev/urandom"
+ "2.1.23740 git hash: 5a8eab96c6b7"
+ "2b88385687d0f98f9b90956bcbf626b2"
+ "Attempts to detect undefined behavior when in WebGL mode and reject shaders if any detected."
+ "Decompressed data size is zero. Wrong or corrupted data? (compressed size is: "
+ "EGL_ANGLE_platform_angle_d3d_luid"
+ "Emulate DontCare loadAction with Clear loadAction. The clear values will be randomized."
+ "Enable EXT_multisampled_render_to_texture on non tiled GPUs."
+ "Enable multi-draw and base vertex base instance extensions for non-WebGL contexts if they are emulated."
+ "Force flush after drawcall use shadow map for intel device."
+ "Infinite loop detected in the shader"
+ "Replacing a node with a node of invalid type: calling replacement.getAsBlock() should not return nullptr."
+ "Replacing a node with a node of invalid type: calling replacement.getAsFunctionPrototypeNode() should not return nullptr."
+ "Replacing a node with a node of invalid type: calling replacement.getAsSymbolNode() should not return nullptr."
+ "Replacing a node with a node of invalid type: calling replacement.getAsTyped() should not return nullptr."
+ "alwaysEnableEmulatedMultidrawExtensions"
+ "emulateDontCareLoadWithRandomClear"
+ "enableMultisampledRenderToTextureOnNonTilers"
+ "ensureNativeStorageCreated"
+ "forceFlushAfterDrawcallUsingShadowmap"
+ "getRenderTarget"
+ "http://anglebug.com/355645824"
+ "http://anglebug.com/42261786"
+ "http://crbug.com/350528343"
+ "https://issuetracker.google.com/349489248"
+ "loadAction"
+ "memoryBarrierWithResources:count:afterStages:beforeStages:"
+ "memoryBarrierWithScope:afterStages:beforeStages:"
+ "rasterSampleCount"
+ "rejectWebglShadersWithUndefinedBehavior"
+ "replaceChildNode"
+ "setInputPrimitiveTopology:"
+ "setRasterSampleCount:"
+ "supportsBCTextureCompression"
+ "wb"
- "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_div(X x, Y y)\n{\n    auto predicate = X(y) == X(0);\n    if constexpr (metal::is_signed_v<X>)\n    {\n        predicate = predicate || (x == X(metal::numeric_limits<X>::lowest()) && X(y) == X(-1));\n    }\n    return x / metal::select(X(y), X(1), predicate);\n}\n\n"
- "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_ftoi(Y y)\n{\n    auto min = metal::numeric_limits<X>::min();\n    auto max = metal::numeric_limits<X>::max();\n    return X(metal::clamp(y, Y(min), Y(max)));\n}\n\n"
- "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_iadd(X x, Y y)\n{\n    return as_type<X>(as_type<metal::make_unsigned_t<X>>(x) + as_type<metal::make_unsigned_t<Y>>(y));\n}\n\n"
- "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_ilshift(X x, Y y)\n{\n    return as_type<X>(metal::select(metal::make_unsigned_t<X>(0), as_type<metal::make_unsigned_t<X>>(x) << (y & Y(31)), as_type<metal::make_unsigned_t<Y>>(y) < metal::make_unsigned_t<Y>(32)));\n}\n\n"
- "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_imod(X x, Y y)\n{\n    if constexpr (metal::is_signed_v<X>) {\n        X y_or_one = metal::select(X(y), X(1), ((X(y) == X(0)) | ((x == X(metal::numeric_limits<X>::lowest())) & (X(y) == X(-1)))));\n        if (metal::any((X(x | y_or_one) & X(2147483648u)) != X(0u)))\n        {\n            return as_type<X>(\n                as_type<metal::make_unsigned_t<X>>(x) - as_type<metal::make_unsigned_t<X>>(x / y_or_one) * as_type<metal::make_unsigned_t<X>>(y_or_one)\n            );\n        }\n        else\n        {\n            return x %!y(MISSING)_or_one;\n        }\n    }\n    else\n    {\n        return x %!m(MISSING)etal::select(X(y), X(1u), X(y) == X(0u));\n    }\n}\n\n"
- "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_imul(X x, Y y)\n{\n    return as_type<X>(as_type<metal::make_unsigned_t<X>>(x) * as_type<metal::make_unsigned_t<Y>>(y));\n}\n\n"
- "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_isub(X x, Y y)\n{\n    return as_type<X>(as_type<metal::make_unsigned_t<X>>(x) - as_type<metal::make_unsigned_t<Y>>(y));\n}\n\n"
- "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_rshift(X x, Y y)\n{\n    return metal::select(X(0), x >> (y & Y(31)), as_type<metal::make_unsigned_t<Y>>(y) < metal::make_unsigned_t<Y>(32));\n}\n\n"
- "\ntemplate <typename X, typename Y>\nANGLE_ALWAYS_INLINE X ANGLE_ulshift(X x, Y y)\n{\n    return metal::select(X(0), x << (y & Y(31)), as_type<metal::make_unsigned_t<Y>>(y) < metal::make_unsigned_t<Y>(32));\n}\n\n"
- "/Library/Caches/com.apple.xbs/Sources/ANGLE/Source/ThirdParty/ANGLE/src/common/angleutils.cpp"
- "2.1.23377 git hash: 0c7331dfe71d"
- "ANGLECubeMapCoordTransform"
- "ANGLECubeMapCoordTransformImplicit"
- "ANGLE_div"
- "ANGLE_ftoi<"
- "ANGLE_iadd"
- "ANGLE_ilshift"
- "ANGLE_imod"
- "ANGLE_imul"
- "ANGLE_isub"
- "ANGLE_rshift"
- "ANGLE_ulshift"
- "Always automatically resolve MSAA render buffers to single sampled texture."
- "Could not open "
- "Error writing to "
- "P"
- "SaveFileHelper"
- "Saved '%!s(MISSING)'.\n"
- "alwaysResolveMultisampleRenderBuffers"
- "c32b8646369ad2bd36713e112fcf4b76"
- "checkError"
- "dPdx"
- "dPdy"
- "dUVdx"
- "dUVdy"
- "ensureTextureCreated"
- "handleDirtyRenderPass"
- "http://crbug.com/1486094"
- "isARM"

```
