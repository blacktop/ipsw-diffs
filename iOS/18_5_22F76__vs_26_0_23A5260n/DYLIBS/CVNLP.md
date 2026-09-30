## CVNLP

> `/System/Library/PrivateFrameworks/CVNLP.framework/CVNLP`

```diff

 119.0.0.0.0
-  __TEXT.__text: 0xcc120
-  __TEXT.__auth_stubs: 0x1670
+  __TEXT.__text: 0xce4c0
+  __TEXT.__auth_stubs: 0x1650
   __TEXT.__objc_methlist: 0x1a1c
   __TEXT.__const: 0x1e01
-  __TEXT.__gcc_except_tab: 0xe364
-  __TEXT.__cstring: 0x64c4
+  __TEXT.__gcc_except_tab: 0xe494
+  __TEXT.__cstring: 0x64f4
   __TEXT.__oslogstring: 0x7ec
   __TEXT.__dlopen_cstrs: 0xc9
-  __TEXT.__unwind_info: 0x40d8
+  __TEXT.__unwind_info: 0x4178
   __TEXT.__objc_classname: 0x440
-  __TEXT.__objc_methname: 0x6159
-  __TEXT.__objc_methtype: 0x2d5e
+  __TEXT.__objc_methname: 0x5d4c
+  __TEXT.__objc_methtype: 0x21f7
   __TEXT.__objc_stubs: 0x2f00
-  __DATA_CONST.__got: 0x3a0
+  __DATA_CONST.__got: 0x3a8
   __DATA_CONST.__const: 0x8d8
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1168
   __DATA_CONST.__objc_superrefs: 0x118
-  __AUTH_CONST.__auth_got: 0xb50
-  __AUTH_CONST.__const: 0x31e0
+  __AUTH_CONST.__auth_got: 0xb40
+  __AUTH_CONST.__const: 0x3248
   __AUTH_CONST.__cfstring: 0x10c0
   __AUTH_CONST.__objc_const: 0x3cf8
   __AUTH_CONST.__objc_doubleobj: 0x20

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  UUID: 8AD2227B-AE98-3F19-B9E3-58382FB0EABA
-  Functions: 2622
-  Symbols:   633
-  CStrings:  2077
+  UUID: B00FE1BD-D954-3964-8907-F9193452D78C
+  Functions: 2662
+  Symbols:   632
+  CStrings:  2079
 
Symbols:
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
CStrings:
+ "@96@0:8@16@?24^{CVNLPLanguageModelWithState=}32{vector<unsigned int, std::allocator<unsigned int>>=^I^I^I}40{vector<unsigned int, std::allocator<unsigned int>>=^I^I^I}64B88B92"
+ "Models/word_lm"
+ "T{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}},N,V_stateInputEspressoBuffers"
+ "T{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}},N,V_stateOutputEspressoBuffers"
+ "T{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}},N,V_stateInputEspressoBuffersShape"
+ "T{vector<std::string, std::allocator<std::string>>=^v^v^v},N,V_decoderInputNames"
+ "f88@0:8@16@24{vector<unsigned int, std::allocator<unsigned int>>=^I^I^I}32@56{vector<unsigned int, std::allocator<unsigned int>>=^I^I^I}64"
+ "norm_to_orig"
+ "normalized"
+ "v40@0:8{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}16"
+ "v40@0:8{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}16"
+ "v40@0:8{vector<std::string, std::allocator<std::string>>=^v^v^v}16"
+ "{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}16@0:8"
+ "{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}16@0:8"
+ "{vector<const _LXCursor *, std::allocator<const _LXCursor *>>=\"__begin_\"^^{_LXCursor}\"__end_\"^^{_LXCursor}\"__cap_\"^^{_LXCursor}}"
+ "{vector<double, std::allocator<double>>=\"__begin_\"^d\"__end_\"^d\"__cap_\"^d}"
+ "{vector<std::string, std::allocator<std::string>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
+ "{vector<std::string, std::allocator<std::string>>=^v^v^v}16@0:8"
+ "{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__cap_\"^I}"
+ "{vector<unsigned int, std::allocator<unsigned int>>=^I^I^I}24@0:8@16"
+ "{vector<unsigned int, std::allocator<unsigned int>>=^I^I^I}32@0:8@16^@24"
+ "{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"__cap_\"^Q}"
- "@96@0:8@16@?24^{CVNLPLanguageModelWithState=}32{vector<unsigned int, std::allocator<unsigned int>>=^I^I{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=^I}}40{vector<unsigned int, std::allocator<unsigned int>>=^I^I{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=^I}}64B88B92"
- "OK"
- "T{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::vector<float>>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>>=Q}}},N,V_stateInputEspressoBuffers"
- "T{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::vector<float>>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>>=Q}}},N,V_stateOutputEspressoBuffers"
- "T{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::vector<unsigned long>>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>>=Q}}},N,V_stateInputEspressoBuffersShape"
- "T{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}},N,V_decoderInputNames"
- "f88@0:8@16@24{vector<unsigned int, std::allocator<unsigned int>>=^I^I{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=^I}}32@56{vector<unsigned int, std::allocator<unsigned int>>=^I^I{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=^I}}64"
- "v40@0:8{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::vector<float>>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>>=Q}}}16"
- "v40@0:8{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::vector<unsigned long>>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>>=Q}}}16"
- "v40@0:8{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}}16"
- "{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::vector<float>>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>>=\"__value_\"Q}}}"
- "{map<std::string, std::vector<float>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<float>>>>={__tree<std::__value_type<std::string, std::vector<float>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<float>>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::vector<float>>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<float>>, std::less<std::string>>>=Q}}}16@0:8"
- "{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>=\"__tree_\"{__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::vector<unsigned long>>, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>>=\"__value_\"Q}}}"
- "{map<std::string, std::vector<unsigned long>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<unsigned long>>>>={__tree<std::__value_type<std::string, std::vector<unsigned long>>, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>, std::allocator<std::__value_type<std::string, std::vector<unsigned long>>>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<std::__value_type<std::string, std::vector<unsigned long>>, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::__map_value_compare<std::string, std::__value_type<std::string, std::vector<unsigned long>>, std::less<std::string>>>=Q}}}16@0:8"
- "{vector<const _LXCursor *, std::allocator<const _LXCursor *>>=\"__begin_\"^^{_LXCursor}\"__end_\"^^{_LXCursor}\"__end_cap_\"{__compressed_pair<const _LXCursor **, std::allocator<const _LXCursor *>>=\"__value_\"^^{_LXCursor}}}"
- "{vector<double, std::allocator<double>>=\"__begin_\"^d\"__end_\"^d\"__end_cap_\"{__compressed_pair<double *, std::allocator<double>>=\"__value_\"^d}}"
- "{vector<std::string, std::allocator<std::string>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::string *, std::allocator<std::string>>=\"__value_\"^v}}"
- "{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}}16@0:8"
- "{vector<unsigned int, std::allocator<unsigned int>>=\"__begin_\"^I\"__end_\"^I\"__end_cap_\"{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=\"__value_\"^I}}"
- "{vector<unsigned int, std::allocator<unsigned int>>=^I^I{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=^I}}24@0:8@16"
- "{vector<unsigned int, std::allocator<unsigned int>>=^I^I{__compressed_pair<unsigned int *, std::allocator<unsigned int>>=^I}}32@0:8@16^@24"
- "{vector<unsigned long, std::allocator<unsigned long>>=\"__begin_\"^Q\"__end_\"^Q\"__end_cap_\"{__compressed_pair<unsigned long *, std::allocator<unsigned long>>=\"__value_\"^Q}}"

```
