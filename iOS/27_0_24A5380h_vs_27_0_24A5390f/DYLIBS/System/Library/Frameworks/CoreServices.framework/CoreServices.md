## CoreServices

> `/System/Library/Frameworks/CoreServices.framework/CoreServices`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__lazy_load_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1507.0.0.0.0
-  __TEXT.__text: 0x1c63f8
+1512.0.0.0.0
+  __TEXT.__text: 0x1c6f38
   __TEXT.__delay_helper: 0x1b8
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0xe16c
+  __TEXT.__objc_methlist: 0xe1d4
   __TEXT.__const: 0x990
-  __TEXT.__cstring: 0x28c92
-  __TEXT.__oslogstring: 0x16286
-  __TEXT.__gcc_except_tab: 0x29414
+  __TEXT.__cstring: 0x28cce
+  __TEXT.__oslogstring: 0x1650f
+  __TEXT.__gcc_except_tab: 0x2955c
   __TEXT.__ustring: 0x23c
-  __TEXT.__unwind_info: 0xc598
+  __TEXT.__unwind_info: 0xc5d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6510
+  __DATA_CONST.__objc_selrefs: 0x6540
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x640
   __DATA_CONST.__objc_arraydata: 0x990
   __DATA_CONST.__got: 0xbb8
   __AUTH_CONST.__const: 0x3b90
-  __AUTH_CONST.__cfstring: 0x179c0
-  __AUTH_CONST.__objc_const: 0x15660
+  __AUTH_CONST.__cfstring: 0x17a00
+  __AUTH_CONST.__objc_const: 0x156e0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x7f8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x150
-  __AUTH_CONST.__auth_got: 0x1960
+  __AUTH_CONST.__auth_got: 0x1968
   __AUTH.__objc_data: 0x33b8
   __AUTH.__data: 0x318
-  __DATA.__objc_ivar: 0xbe8
+  __DATA.__objc_ivar: 0xbf0
   __DATA.__data: 0x15c4
   __DATA.__bss: 0xf30
   __DATA.__common: 0x40

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 9514
-  Symbols:   16458
-  CStrings:  6019
+  Functions: 9533
+  Symbols:   16473
+  CStrings:  6034
 
Symbols:
+ -[LSApplicationRecord(MobileInstall) _LSRecord_resolve_installBuildVersion]
+ -[LSApplicationRecord(MobileInstall) _LSRecord_resolve_originalInstallDate]
+ -[LSApplicationRecord(MobileInstall) installBuildVersionWithContext:tableID:unitID:unitBytes:]
+ -[LSApplicationRecord(MobileInstall) installBuildVersion]
+ -[LSApplicationRecord(MobileInstall) originalInstallDateWithContext:tableID:unitID:unitBytes:]
+ -[LSApplicationRecord(MobileInstall) originalInstallDate]
+ -[LSBundleRecordBuilder installBuildVersion]
+ -[LSBundleRecordBuilder originalInstallDate]
+ -[_LSStackBacktrace replacementObjectForCoder:]
+ GCC_except_table166
+ GCC_except_table359
+ GCC_except_table378
+ GCC_except_table385
+ GCC_except_table386
+ GCC_except_table390
+ GCC_except_table397
+ GCC_except_table398
+ GCC_except_table412
+ GCC_except_table413
+ GCC_except_table417
+ _OBJC_IVAR_$_LSBundleRecordBuilder._installBuildVersion
+ _OBJC_IVAR_$_LSBundleRecordBuilder._originalInstallDate
+ ___block_descriptor_32_e387_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiII}20l
+ ___block_descriptor_40_ea8_32s_e387_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiII}20ls32l8
+ ___block_descriptor_40_ea8_32s_e387_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiII}20ls32l8
+ ___block_descriptor_44_e387_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiII}20l
+ ___block_descriptor_48_e8_32s40s_e387_v28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiII}20ls32l8s40l8
+ ___block_descriptor_48_ea8_32bs_e384_v28?0"NSString"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiII}20ls32l8
+ ___block_descriptor_52_e8_32s40n6_8_8_s0_e387_v28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiII}20l
+ ___block_descriptor_56_ea8_32bs40bs_e374_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiII}12*20ls32l8s40l8
+ ___block_descriptor_56_ea8_32r40r_e374_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiII}12*20lr32l8r40l8
+ ___block_descriptor_56_ea8_32s40bs_e374_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiII}12*20ls32l8s40l8
+ ___block_descriptor_632_ea8_32s_e19_v32?0I8r^v12I20*24ls32l8
+ ___block_descriptor_632_ea8_32s_e37_v40?0q8"NSString"16"NSString"24*32ls32l8
+ ___block_descriptor_64_ea8_32s40r48r_e44_v32?0"NSDictionary"8"NSSet"16"NSError"24lr40l8s32l8r48l8
+ ___block_descriptor_68_ea8_32s40s48s_e374_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiII}12*20ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32bs40r48r_e374_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiII}12*20ls32l8r40l8r48l8
+ ___block_descriptor_72_ea8_32s40s48r_e374_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiII}12*20ls32l8s40l8r48l8
+ ___block_descriptor_80_e8_32s40s48s56s64n6_8_8_s0_e387_v28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiII}20l
+ _copyProcessNameString
+ _objc_msgSend$installBuildVersion
+ _objc_msgSend$originalInstallDate
+ _proc_name
+ _processNameString
- GCC_except_table353
- GCC_except_table372
- GCC_except_table373
- GCC_except_table380
- GCC_except_table383
- GCC_except_table384
- GCC_except_table388
- GCC_except_table391
- GCC_except_table392
- GCC_except_table406
- GCC_except_table407
- GCC_except_table411
- ___block_descriptor_32_e385_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20l
- ___block_descriptor_40_ea8_32s_e385_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20ls32l8
- ___block_descriptor_40_ea8_32s_e385_B28?0^{LSContext=}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20ls32l8
- ___block_descriptor_44_e385_B28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20l
- ___block_descriptor_48_e8_32s40s_e385_v28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20ls32l8s40l8
- ___block_descriptor_48_ea8_32bs_e382_v28?0"NSString"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20ls32l8
- ___block_descriptor_52_e8_32s40n6_8_8_s0_e385_v28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20l
- ___block_descriptor_56_ea8_32bs40bs_e372_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}12*20ls32l8s40l8
- ___block_descriptor_56_ea8_32r40r_e372_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}12*20lr32l8r40l8
- ___block_descriptor_56_ea8_32r40r_e44_v32?0"NSDictionary"8"NSSet"16"NSError"24lr32l8r40l8
- ___block_descriptor_56_ea8_32s40bs_e372_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}12*20ls32l8s40l8
- ___block_descriptor_624_ea8_32s_e19_v32?0I8r^v12I20*24ls32l8
- ___block_descriptor_624_ea8_32s_e37_v40?0q8"NSString"16"NSString"24*32ls32l8
- ___block_descriptor_68_ea8_32s40s48s_e372_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}12*20ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32bs40r48r_e372_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}12*20ls32l8r40l8r48l8
- ___block_descriptor_72_ea8_32s40s48r_e372_v28?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}12*20ls32l8s40l8r48l8
- ___block_descriptor_80_e8_32s40s48s56s64n6_8_8_s0_e385_v28?0"_LSDatabase"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20l
CStrings:
+ "%s: Success canonicalizing %@ produced no result."
+ "%s: could not canonicalize %@: %@"
+ "B28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiII}20"
+ "B28@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiII}20"
+ "Could not create bundle node from %@: %@"
+ "Couldn't construct relative path for executable: %@ %@ %@ %@"
+ "Failed to get keys remotely, but got no error: %@"
+ "Failed to get keys remotely, but keeping original error. Remote error: %@"
+ "Stopping lsd %{public}d/%{public}@ uid %{public}d on request; letting databases complete in-flight operations."
+ "_LSGetMainBundleURL_block_invoke"
+ "failed to get node for %@ but had no error"
+ "failed to get populator for %@ but had no error"
+ "failed to prepare mimic for %@ but had no error"
+ "failed to prepare value for %@ but had no error"
+ "install build version"
+ "mimic selector %{public}@ returned false without setting an error"
+ "mimic selector %{public}@ returned nil without setting an error"
+ "original install date"
+ "pid %{public}ld/%{public}@ requests to open URL with scheme %{private}@"
+ "platform default"
+ "system placeholder (prioritized)"
+ "v28@?0@\"NSString\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiII}20"
+ "v28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiII}20"
+ "v28@?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIIiII}12*20"
+ "vendor (prioritized)"
- "Apple default"
- "B28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20"
- "B28@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20"
- "Stopping lsd %{public}d uid %{public}d on request; letting databases complete in-flight operations."
- "pid %{public}ld requests to open URL with scheme %{private}@"
- "system placeholder (prioritized is-Apple check)"
- "v28@?0@\"NSString\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20"
- "v28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}20"
- "v28@?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIIii{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIICCIII{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}II{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQQIIIQIIIIIIIIIIIIIIIICCC[1I]II{LSAppClipFields=I}iIIIIIIII}12*20"
- "vendor (prioritized is-Apple check)"
```
