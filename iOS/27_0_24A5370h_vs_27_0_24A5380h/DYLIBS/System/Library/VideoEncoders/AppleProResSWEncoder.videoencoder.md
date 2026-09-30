## AppleProResSWEncoder.videoencoder

> `/System/Library/VideoEncoders/AppleProResSWEncoder.videoencoder`

```diff

-  __TEXT.__text: 0x21224
+  __TEXT.__text: 0x2150c
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0xf990
-  __TEXT.__cstring: 0x40e
+  __TEXT.__cstring: 0x58a
   __TEXT.__oslogstring: 0xbc
-  __TEXT.__gcc_except_tab: 0x158
-  __TEXT.__unwind_info: 0x258
+  __TEXT.__gcc_except_tab: 0x174
+  __TEXT.__unwind_info: 0x290
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x88
+  __DATA_CONST.__const: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__objc_selrefs: 0x10
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x440
+  __AUTH_CONST.__const: 0x380
+  __AUTH_CONST.__cfstring: 0x4c0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x2a8
+  __AUTH_CONST.__auth_got: 0x300
   __DATA.__data: 0x36
-  __DATA.__bss: 0x80
+  __DATA.__bss: 0x140
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 160
-  Symbols:   559
-  CStrings:  80
+  Functions: 171
+  Symbols:   602
+  CStrings:  95
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
Symbols:
+ GCC_except_table3
+ _CFArrayGetCount
+ _CFArrayGetTypeID
+ _CFArrayGetValues
+ _CFPreferencesCopyAppValue
+ _CFStringGetCString
+ _CFStringGetLength
+ _CFStringGetTypeID
+ __ZL21getQuantizationMatrixPKvPKcPh
+ __ZN10Macroblock31getCustomQuantizationMatrixLumaEi
+ __ZN10Macroblock33getCustomQuantizationMatrixChromaEi
+ __ZN23DiscreteCosineTransform8quantizeIstfEEvPKT_PT0_PKT1_
+ ____ZL24getUserDefinedQuantIndexv_block_invoke
+ ____ZL46getUserDefinedMaxCompressionSizeExcludingAlphav_block_invoke
+ ____ZN10Macroblock31getCustomQuantizationMatrixLumaEi_block_invoke
+ ____ZN10Macroblock33getCustomQuantizationMatrixChromaEi_block_invoke
+ _malloc_type_posix_memalign
+ _printf
+ _putchar
+ _strtol
- __ZN23DiscreteCosineTransform8quantizeIstEEvPKT_PT0_S3_
CStrings:
+ "%4d"
+ "ProRes user-defined %s matrix:\n"
+ "ProRes user-defined max compression size excluding alpha: %d\n"
+ "ProRes user-defined quantization index: %d\n"
+ "ProResUserDefinedChromaMatrix"
+ "ProResUserDefinedLumaMatrix"
+ "ProResUserDefinedMaxCompressionSizeExcludingAlpha"
+ "ProResUserDefinedMaxCompressionSizeExcludingAlpha is too small, using %d instead!\n"
+ "ProResUserDefinedQuantizationIndex"
+ "chroma"
+ "luma"

```
