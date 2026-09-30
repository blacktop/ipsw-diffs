## WebGPU

> `/System/Library/PrivateFrameworks/WebGPU.framework/WebGPU`

```diff

-622.1.19.10.4
-  __TEXT.__text: 0x21b3e0
+622.1.21.10.3
+  __TEXT.__text: 0x21b624
   __TEXT.__auth_stubs: 0xd40
   __TEXT.__objc_methlist: 0x1f0
   __TEXT.__const: 0x11e0
-  __TEXT.__gcc_except_tab: 0x7b3c
-  __TEXT.__cstring: 0x3d8a7
-  __TEXT.__unwind_info: 0x1eb0
+  __TEXT.__gcc_except_tab: 0x7b28
+  __TEXT.__cstring: 0x3dc93
+  __TEXT.__unwind_info: 0x1eb8
   __TEXT.__objc_classname: 0x54
   __TEXT.__objc_methname: 0x298e
   __TEXT.__objc_methtype: 0x1c9d

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7E0A1926-949D-315C-B041-C1A41A820E99
-  Functions: 2673
-  Symbols:   6853
-  CStrings:  3375
+  UUID: 163E35D8-111F-3DBF-9D8F-A5420C1B6D6C
+  Functions: 2674
+  Symbols:   6857
+  CStrings:  3379
 
Symbols:
+ __ZN3WTF37tryMakeStringImplFromAdaptersInternalIJNS_17StringTypeAdapterINS_12ASCIILiteralEvEENS1_IjvEES3_S4_EEENS_6RefPtrINS_10StringImplENS_12RawPtrTraitsIS6_EENS_21DefaultRefDerefTraitsIS6_EEEEjbDpT_
+ __ZN3WTF9HashTableINS_6RefPtrIKN6WebGPU9BindGroupENS_12RawPtrTraitsIS4_EENS_21DefaultRefDerefTraitsIS4_EEEES9_NS_17IdentityExtractorENS_11DefaultHashIS9_EENS_10HashTraitsIS9_EESE_NS_10FastMallocEED2Ev
Functions:
~ __ZN3WTF7HashSetIyNS_11DefaultHashIyEENS_29UnsignedWithZeroKeyHashTraitsIyEENS_15HashTableTraitsELNS_17ShouldValidateKeyE1EEC2ESt16initializer_listIyE : 124 -> 368
+ __ZN3WTF6VectorIjLm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE4fillERKjm
~ __Z33wgpuComputePassEncoderSetPipelineP26WGPUComputePassEncoderImplP23WGPUComputePipelineImpl : 1064 -> 900
- __ZN3WTF6VectorIjLm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE4fillERKjm
~ __ZZN6WebGPUL23rawHardwareCapabilitiesEPU19objcproto9MTLDevice11objc_objectENK3$_0clERKNS_20HardwareCapabilitiesE : 1576 -> 1444
~ __ZN6WebGPU12RenderBundleC2EP7NSArrayIP28RenderBundleICBWithResourcesEON3WTF6VectorINS_17BindableResourcesELm0ENS6_15CrashOnOverflowELm16ENS6_10FastMallocEEENS6_6RefPtrINS_19RenderBundleEncoderENS6_12RawPtrTraitsISE_EENS6_21DefaultRefDerefTraitsISE_EEEERK33WGPURenderBundleEncoderDescriptorybONS6_7HashSetINSD_IKNS_9BindGroupENSF_ISP_EENSH_ISP_EEEENS6_11DefaultHashISS_EENS6_10HashTraitsISS_EENS6_15HashTableTraitsELNS6_17ShouldValidateKeyE1EEERNS_6DeviceE : 1236 -> 1508
+ __ZN3WTF9HashTableINS_6RefPtrIKN6WebGPU9BindGroupENS_12RawPtrTraitsIS4_EENS_21DefaultRefDerefTraitsIS4_EEEES9_NS_17IdentityExtractorENS_11DefaultHashIS9_EENS_10HashTraitsIS9_EESE_NS_10FastMallocEED2Ev
+ __ZN3WTF9HashTableINS_6RefPtrIKN6WebGPU9BindGroupENS_12RawPtrTraitsIS4_EENS_21DefaultRefDerefTraitsIS4_EEEES9_NS_17IdentityExtractorENS_11DefaultHashIS9_EENS_10HashTraitsIS9_EESE_NS_10FastMallocEE6rehashEjPS9_
- __ZN3WTF7HashSetINS_6RefPtrIKN6WebGPU9BindGroupENS_12RawPtrTraitsIS4_EENS_21DefaultRefDerefTraitsIS4_EEEENS_11DefaultHashIS9_EENS_10HashTraitsIS9_EENS_15HashTableTraitsELNS_17ShouldValidateKeyE1EED1Ev
- __ZN3WTF9HashTableINS_6RefPtrIKN6WebGPU9BindGroupENS_12RawPtrTraitsIS4_EENS_21DefaultRefDerefTraitsIS4_EEEES9_NS_17IdentityExtractorENS_11DefaultHashIS9_EENS_10HashTraitsIS9_EESE_NS_10FastMallocEE6rehashEjPS9_
~ __ZN6WebGPU17RenderPassEncoder11setPipelineERKNS_14RenderPipelineE : 1764 -> 1436
~ __ZN6WebGPU7Texture11pixelFormatE17WGPUTextureFormat : 700 -> 812
~ __ZN4WGSL22RewriteGlobalVariables15insertParameterERKNS_10SourceSpanERKNS_3AST8FunctionEjONS4_10IdentifierEPNS4_10ExpressionENS4_13ParameterRoleE : 1268 -> 1272
+ __ZN3WTF37tryMakeStringImplFromAdaptersInternalIJNS_17StringTypeAdapterINS_12ASCIILiteralEvEENS1_IjvEES3_S4_EEENS_6RefPtrINS_10StringImplENS_12RawPtrTraitsIS6_EENS_21DefaultRefDerefTraitsIS6_EEEEjbDpT_
~ __ZN4WGSL5Metal17generateMetalCodeERNS_12ShaderModuleERNS_13PrepareResultERKN3WTF7HashMapINS5_6StringENS_13ConstantValueENS5_11DefaultHashIS7_EENS5_10HashTraitsIS7_EENSB_IS8_EENS5_15HashTableTraitsELNS5_17ShouldValidateKeyE1ENS5_10FastMallocEEEONS_11DeviceStateE : 456 -> 460
~ __ZZN4WGSL5Metal24FunctionDefinitionWriter5visitEPKNS_4TypeERNS_3AST14CallExpressionEEN4$_298__invokeERNS0_15HelperGeneratorE : 16 -> 72
~ __ZZN4WGSL5Metal24FunctionDefinitionWriter5visitEPKNS_4TypeERNS_3AST14CallExpressionEEN4$_308__invokeERNS0_15HelperGeneratorE : 16 -> 72
~ __ZZN4WGSL5Metal24FunctionDefinitionWriter5visitEPKNS_4TypeERNS_3AST14CallExpressionEEN4$_318__invokeERNS0_15HelperGeneratorE : 16 -> 72
~ __ZZN4WGSL5Metal24FunctionDefinitionWriter5visitEPKNS_4TypeERNS_3AST14CallExpressionEEN4$_328__invokeERNS0_15HelperGeneratorE : 16 -> 72
~ __ZZN4WGSL11prepareImplERNS_12ShaderModuleERKN3WTF7HashMapINS2_6StringEPNS_14PipelineLayoutENS2_11DefaultHashIS4_EENS2_10HashTraitsIS4_EENS9_IS6_EENS2_15HashTableTraitsELNS2_17ShouldValidateKeyE1ENS2_10FastMallocEEEENKUlvE_clEv : 892 -> 924
CStrings:
+ "'atomic' requires 1 template argument"
+ "'ptr' requires at least 2 template arguments"
+ "'ptr' requires at most 3 template arguments"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugBt3avYGGG4rvNW6lGp7hvnQUj97A38lfg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugBt3avYGGG4rvNW6lGp7hvnQUj97A38lfg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/HashTable.h"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugBt3avYGGG4rvNW6lGp7hvnQUj97A38lfg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/Markable.h"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugBt3avYGGG4rvNW6lGp7hvnQUj97A38lfg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/RefCounted.h"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugBt3avYGGG4rvNW6lGp7hvnQUj97A38lfg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugBt3avYGGG4rvNW6lGp7hvnQUj97A38lfg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/TrailingArray.h"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugBt3avYGGG4rvNW6lGp7hvnQUj97A38lfg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugBt3avYGGG4rvNW6lGp7hvnQUj97A38lfg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugBt3avYGGG4rvNW6lGp7hvnQUj97A38lfg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
+ "/AppleInternal/Library/BuildRoots/4~B6jBugBt3avYGGG4rvNW6lGp7hvnQUj97A38lfg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "T &WTF::Markable<unsigned int>::operator*() & [T = unsigned int, Traits = WTF::MarkableTraits<unsigned int>]"
+ "__wgslPackFloatToSnorm2x16"
+ "__wgslPackFloatToSnorm4x8"
+ "__wgslPackFloatToUnorm2x16"
+ "__wgslPackFloatToUnorm4x8"
+ "template <typename T>\n auto __wgslPackFloatToSnorm2x16(T value)\n {\n if constexpr(__wgslMetalAppleGPUFamily < 9) { \n volatile auto result = pack_float_to_snorm2x16(value);\n return result;\n } else { \n auto result = pack_float_to_snorm2x16(value);\n return result;\n }\n }\n"
+ "template <typename T>\n auto __wgslPackFloatToSnorm4x8(T value)\n {\n if constexpr(__wgslMetalAppleGPUFamily < 9) { \n volatile auto result = pack_float_to_snorm4x8(value);\n return result;\n } else { \n auto result = pack_float_to_snorm4x8(value);\n return result;\n }\n }\n"
+ "template <typename T>\n auto __wgslPackFloatToUnorm2x16(T value)\n {\n if constexpr(__wgslMetalAppleGPUFamily < 9) { \n volatile auto result = pack_float_to_unorm2x16(value);\n return result;\n } else { \n auto result = pack_float_to_unorm2x16(value);\n return result;\n }\n }\n"
+ "template <typename T>\n auto __wgslPackFloatToUnorm4x8(T value)\n {\n if constexpr(__wgslMetalAppleGPUFamily < 9) { \n volatile auto result = pack_float_to_unorm4x8(value);\n return result;\n } else { \n auto result = pack_float_to_unorm4x8(value);\n return result;\n }\n }\n"
- "'atomic' requires 1 template arguments"
- "'ptr' requires at least 2 template argument"
- "'ptr' requires at most 3 template argument"
- "/AppleInternal/Library/BuildRoots/4~B5heugByL5381y80qXQpXj79MimwekqJibBXljU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/CompletionHandler.h"
- "/AppleInternal/Library/BuildRoots/4~B5heugByL5381y80qXQpXj79MimwekqJibBXljU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/HashTable.h"
- "/AppleInternal/Library/BuildRoots/4~B5heugByL5381y80qXQpXj79MimwekqJibBXljU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/Markable.h"
- "/AppleInternal/Library/BuildRoots/4~B5heugByL5381y80qXQpXj79MimwekqJibBXljU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/RefCounted.h"
- "/AppleInternal/Library/BuildRoots/4~B5heugByL5381y80qXQpXj79MimwekqJibBXljU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/4~B5heugByL5381y80qXQpXj79MimwekqJibBXljU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/TrailingArray.h"
- "/AppleInternal/Library/BuildRoots/4~B5heugByL5381y80qXQpXj79MimwekqJibBXljU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/TypeCasts.h"
- "/AppleInternal/Library/BuildRoots/4~B5heugByL5381y80qXQpXj79MimwekqJibBXljU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
- "/AppleInternal/Library/BuildRoots/4~B5heugByL5381y80qXQpXj79MimwekqJibBXljU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
- "/AppleInternal/Library/BuildRoots/4~B5heugByL5381y80qXQpXj79MimwekqJibBXljU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "T &WTF::Markable<unsigned int, WTF::IntegralMarkableTraits<unsigned int, 4294967295>>::operator*() & [T = unsigned int, Traits = WTF::IntegralMarkableTraits<unsigned int, 4294967295>]"
- "pack_float_to_snorm2x16"
- "pack_float_to_snorm4x8"
- "pack_float_to_unorm2x16"
- "pack_float_to_unorm4x8"

```
