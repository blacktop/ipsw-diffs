## ScreenReaderOutput

> `/System/Library/PrivateFrameworks/ScreenReaderOutput.framework/ScreenReaderOutput`

```diff

-467.3.1.0.0
-  __TEXT.__text: 0x998ac
-  __TEXT.__objc_methlist: 0x9208
-  __TEXT.__const: 0x183c
-  __TEXT.__cstring: 0x5c0c
+467.3.3.0.0
+  __TEXT.__text: 0x99e14
+  __TEXT.__objc_methlist: 0x9248
+  __TEXT.__const: 0x184c
+  __TEXT.__cstring: 0x5bf5
   __TEXT.__swift5_typeref: 0xeec
   __TEXT.__constg_swiftt: 0x960
   __TEXT.__swift5_builtin: 0xb4

   __TEXT.__swift_as_ret: 0x5c
   __TEXT.__swift_as_cont: 0x9c
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__gcc_except_tab: 0x194c
+  __TEXT.__gcc_except_tab: 0x1964
   __TEXT.__ustring: 0x9e
-  __TEXT.__unwind_info: 0x3418
+  __TEXT.__unwind_info: 0x3428
   __TEXT.__eh_frame: 0xa30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4858
+  __DATA_CONST.__objc_selrefs: 0x4878
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x380
   __DATA_CONST.__got: 0x790
   __AUTH_CONST.__const: 0x3280
-  __AUTH_CONST.__cfstring: 0x5740
-  __AUTH_CONST.__objc_const: 0xbd48
+  __AUTH_CONST.__cfstring: 0x5720
+  __AUTH_CONST.__objc_const: 0xbda0
   __AUTH_CONST.__objc_intobj: 0xa68
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH_CONST.__auth_got: 0x10a8
   __AUTH.__objc_data: 0x360
   __AUTH.__data: 0x80
-  __DATA.__objc_ivar: 0x8d4
+  __DATA.__objc_ivar: 0x8dc
   __DATA.__data: 0x1690
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x1d10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4011
-  Symbols:   5813
-  CStrings:  1081
+  Functions: 4015
+  Symbols:   5820
+  CStrings:  1080
 
Symbols:
+ -[SCROBrailleClientXPC handleBrailleDidPanLeft:elementToken:appToken:lineOffset:displayToken:]
+ -[SCROBrailleClientXPC handleBrailleDidPanRight:elementToken:appToken:lineOffset:displayToken:]
+ -[SCROBrailleHandler handleBrailleDidPanLeft:elementToken:appToken:lineOffset:displayToken:]
+ -[SCROBrailleHandler handleBrailleDidPanRight:elementToken:appToken:lineOffset:displayToken:]
+ -[SCROBrailleHandlerXPC handleBrailleDidPanLeft:elementToken:appToken:lineOffset:displayToken:]
+ -[SCROBrailleHandlerXPC handleBrailleDidPanRight:elementToken:appToken:lineOffset:displayToken:]
+ -[SCROMobileBrailleDisplayInputManager _storedUserDefaultsForModelIdentifier:]
+ -[SCROMobileBrailleDisplayInputManager _userDefaultsForDisplayWithToken:]
+ -[SCROMobileBrailleDisplayInputManager userDefaultsForModelIdentifier:productName:driverIdentifier:]
+ -[SCROMobileBrailleDisplayInputManagerCacheObject modelIdentifierForPlist]
+ -[SCROMobileBrailleDisplayInputManagerCacheObject setModelIdentifierForPlist:]
+ GCC_except_table2931
+ GCC_except_table2947
+ GCC_except_table2966
+ GCC_except_table2967
+ GCC_except_table2968
+ GCC_except_table3033
+ GCC_except_table3035
+ GCC_except_table3038
+ GCC_except_table3040
+ OBJC_IVAR_$_SCROBrailleDisplay._driverModelIdentifierForAnalytics
+ _OBJC_IVAR_$_SCROMobileBrailleDisplayInputManagerCacheObject._modelIdentifierForPlist
+ ___95-[SCROBrailleHandlerXPC handleBrailleDidPanLeft:elementToken:appToken:lineOffset:displayToken:]_block_invoke
+ ___96-[SCROBrailleHandlerXPC handleBrailleDidPanRight:elementToken:appToken:lineOffset:displayToken:]_block_invoke
+ ___block_descriptor_72_e8_32s40s48s56s64s_e41_v16?0"<SCROBrailleClientCallbacksXPC>"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ _kSCROBrailleDisplayModelIdentifierForAnalytics
- -[SCROBrailleClientXPC handleBrailleDidPanLeft:elementToken:appToken:lineOffset:]
- -[SCROBrailleClientXPC handleBrailleDidPanRight:elementToken:appToken:lineOffset:]
- -[SCROBrailleHandler handleBrailleDidPanLeft:elementToken:appToken:lineOffset:]
- -[SCROBrailleHandler handleBrailleDidPanRight:elementToken:appToken:lineOffset:]
- -[SCROBrailleHandlerXPC handleBrailleDidPanLeft:elementToken:appToken:lineOffset:]
- -[SCROBrailleHandlerXPC handleBrailleDidPanRight:elementToken:appToken:lineOffset:]
- -[SCROMobileBrailleDisplayInputManager userDefaultsForModelIdentifier:]
- GCC_except_table2927
- GCC_except_table2943
- GCC_except_table2962
- GCC_except_table2963
- GCC_except_table2964
- GCC_except_table3027
- GCC_except_table3029
- GCC_except_table3032
- GCC_except_table3034
- ___82-[SCROBrailleHandlerXPC handleBrailleDidPanLeft:elementToken:appToken:lineOffset:]_block_invoke
- ___83-[SCROBrailleHandlerXPC handleBrailleDidPanRight:elementToken:appToken:lineOffset:]_block_invoke
- ___block_descriptor_64_e8_32s40s48s56s_e41_v16?0"<SCROBrailleClientCallbacksXPC>"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
CStrings:
+ "BrailleDisplayModelIdentifierForAnalytics"
- "NLS eReader Humanware"
- "com.apple.scrod.braille.driver.nls.ereader"
```
