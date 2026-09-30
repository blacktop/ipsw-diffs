## TextGeneration

> `/System/Library/PrivateFrameworks/TextGeneration.framework/TextGeneration`

```diff

   __TEXT.__gcc_except_tab: 0x298
   __TEXT.__oslogstring: 0x294
   __TEXT.__dlopen_cstrs: 0x6c
-  __TEXT.__unwind_info: 0x1f8
+  __TEXT.__unwind_info: 0x1f0
   __TEXT.__objc_classname: 0x1f6
   __TEXT.__objc_methname: 0xe5a
-  __TEXT.__objc_methtype: 0x5e6
+  __TEXT.__objc_methtype: 0x4fc
   __TEXT.__objc_stubs: 0xac0
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x138

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8A791F86-C6A1-3451-9CE7-2D0EBCD2C9DE
+  UUID: A90AAD24-8E88-3F17-BE1E-F70730BACB3F
   Functions: 152
   Symbols:   688
   CStrings:  310
Symbols:
+ __ZN44TGITextGenerationInferenceModelConfigurationD2Ev
- __ZN44TGITextGenerationInferenceModelConfigurationD1Ev
Functions:
~ __ZN44TGITextGenerationInferenceModelConfigurationD1Ev -> -[TGTextGenerationConfiguration uuid] : 84 -> 12
~ -[TGTextGenerationConfiguration decodingPolicy] -> -[TGTextGenerationConfiguration setDecodingPolicy:] : 12 -> 8
~ -[TGTextGenerationConfiguration setDecodingPolicy:] -> -[TGTextGenerationConfiguration resources] : 8 -> 12
~ -[TGTextGenerationConfiguration resources] -> -[TGTextGenerationConfiguration .cxx_destruct] : 12 -> 80
~ -[TGTextGenerationConfiguration .cxx_destruct] -> __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17__assign_externalEPKcm : 80 -> 188
~ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17__assign_externalEPKcm -> __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17__assign_externalEPKc : 188 -> 72
~ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17__assign_externalEPKc -> __ZN44TGITextGenerationInferenceModelConfigurationD2Ev : 72 -> 84
CStrings:
+ "{TGITextGenerationInferenceModelConfiguration={basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16@0:8"
- "{TGITextGenerationInferenceModelConfiguration={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}16@0:8"

```
