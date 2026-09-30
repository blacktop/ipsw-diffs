## libAppleEXR.dylib

> `/usr/lib/libAppleEXR.dylib`

```diff

-3.1.20.0.0
-  __TEXT.__text: 0x9aa88
-  __TEXT.__auth_stubs: 0x460
+3.1.23.0.0
+  __TEXT.__text: 0x9a864
+  __TEXT.__auth_stubs: 0x440
   __TEXT.__objc_methlist: 0x254
-  __TEXT.__const: 0x210bc
-  __TEXT.__gcc_except_tab: 0x594
+  __TEXT.__const: 0x210ac
+  __TEXT.__gcc_except_tab: 0x4e0
   __TEXT.__cstring: 0x41c1
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x918
+  __TEXT.__unwind_info: 0x8a0
   __TEXT.__eh_frame: 0xf8
   __TEXT.__objc_classname: 0x59
   __TEXT.__objc_methname: 0x20a

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x240
-  __AUTH_CONST.__const: 0x10c0
+  __AUTH_CONST.__auth_got: 0x230
+  __AUTH_CONST.__const: 0x1080
   __AUTH_CONST.__cfstring: 0x400
   __AUTH_CONST.__objc_const: 0x610
   __DATA.__data: 0x240
-  __DATA.__bss: 0x20
-  __DATA.__common: 0xe8
+  __DATA.__bss: 0x18
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__common: 0x1
+  __DATA_DIRTY.__common: 0xd9
+  __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3B5FA21D-2DA9-39C7-999F-83E203DFA166
-  Functions: 735
-  Symbols:   2069
+  UUID: 98E9725A-B2EF-3E49-958A-1F30005E379F
+  Functions: 717
+  Symbols:   2044
   CStrings:  538
 
Symbols:
+ -[OS_axr_data debugDescription].cold.1
+ -[OS_axr_data debugDescription].cold.2
+ -[OS_axr_data debugDescription].cold.3
+ GCC_except_table23
+ GCC_except_table26
+ GCC_except_table34
+ __Z10_YCCtoRGBAIfLj1ELi16EEvRPKT_S3_RPS0_RK9YccMatrixRS1_
+ __Z10_YCCtoRGBAIfLj2ELi16EEvRPKT_S3_RPS0_RK9YccMatrixRS1_
+ __Z11_YCCAtoRGBAIfLj1ELi16EEvRPKT_S3_RPS0_RK9YccMatrixRS1_
+ __Z11_YCCAtoRGBAIfLj2ELi16EEvRPKT_S3_RPS0_RK9YccMatrixRS1_
+ __ZN13EncoderBuffer16GetEncoderBufferEm
+ __ZN19AXRLogicalImageList17LoadDefaultGroupsEPK7AXRDataRb.cold.1
+ __ZN19AXRLogicalImageList17LoadDefaultGroupsEPK7AXRDataRb.cold.2
+ __ZN19AXRLogicalImageList17LoadDefaultGroupsEPK7AXRDataRb.cold.3
+ __ZN19AXRLogicalImageList17LoadDefaultGroupsEPK7AXRDataRb.cold.4
+ __ZN19AXRLogicalImageListC2EPU22objcproto11OS_axr_data8NSObject.cold.1
+ __ZN19AXRLogicalImageListC2EPU22objcproto11OS_axr_data8NSObject.cold.2
+ _axr_data_get_channel_count.cold.1
+ _axr_data_get_channel_info.cold.2
+ _axr_data_get_layer_count.cold.1
+ _axr_data_get_layer_info.cold.2
+ _axr_data_get_level_count.cold.1
+ _axr_data_get_level_size.cold.1
+ _axr_data_get_part_info.cold.2
+ _axr_data_get_property.cold.2
+ _axr_data_get_property_count.cold.1
+ _axr_decoder_append_channel.cold.1
+ _axr_decoder_append_channel.cold.2
+ _axr_decoder_get_info.cold.2
+ _axr_decoder_set_subregion.cold.3
- GCC_except_table21
- GCC_except_table28
- GCC_except_table31
- GCC_except_table39
- GCC_except_table40
- GCC_except_table48
- GCC_except_table49
- __ZL10Encode_v2fP13EncoderStreamPKcff11axr_flags_t
- __ZL11EncodeFloatP13EncoderStreamPKcf11axr_flags_t
- __ZL12EncodeStringP13EncoderStreamPKcS2_11axr_flags_t
- __ZL20EncodeChromaticitiesP13EncoderStreamPKcDv4_fS3_11axr_flags_t
- __ZL9EncodeIntP13EncoderStreamPKci11axr_flags_t
- __ZN11ReadYccArgsD1Ev
- __ZN13AXRBufferPool11FreeBuffersEv
- __ZN13EncoderBuffer16GetEncoderBufferEP18EncoderBufferCachem
- __ZN18EncoderBufferCacheD0Ev
- __ZN18EncoderBufferCacheD1Ev
- __ZN18EncoderBufferCacheD2Ev
- __ZNK7AXRData12GetImageInfoEm
- __ZNK7AXRData12GetImageInfoEm.cold.1
- __ZNK7AXRData12GetImageSizeEmm
- __ZNK7AXRData12GetImageSizeEmm.cold.1
- __ZNK7AXRData12GetLayerInfoEmm
- __ZNK7AXRData12GetLayerInfoEmm.cold.1
- __ZNK7AXRData12GetLevelModeEm
- __ZNK7AXRData12GetLevelModeEm.cold.1
- __ZNK7AXRData12HasLongNamesEm
- __ZNK7AXRData12HasLongNamesEm.cold.1
- __ZNK7AXRData13GetLayerCountEm
- __ZNK7AXRData13GetLayerCountEm.cold.1
- __ZNK7AXRData13GetLevelCountEm
- __ZNK7AXRData13GetLevelCountEm.cold.1
- __ZNK7AXRData13GetSampleTypeEmm11axr_flags_t
- __ZNK7AXRData13GetSampleTypeEmm11axr_flags_t.cold.1
- __ZNK7AXRData14GetChannelTypeEmm11axr_flags_t
- __ZNK7AXRData14GetChannelTypeEmm11axr_flags_t.cold.1
- __ZNK7AXRData15GetChannelCountEm
- __ZNK7AXRData15GetChannelCountEm.cold.1
- __ZNK7AXRData16GetImagePropertyEmm
- __ZNK7AXRData16GetImagePropertyEmm.cold.1
- __ZNK7AXRData21GetImagePropertyCountEm
- __ZNK7AXRData21GetImagePropertyCountEm.cold.1
- __ZTI18EncoderBufferCache
- __ZTS18EncoderBufferCache
- __ZTV18EncoderBufferCache
- _os_unfair_lock_lock
- _os_unfair_lock_unlock

```
