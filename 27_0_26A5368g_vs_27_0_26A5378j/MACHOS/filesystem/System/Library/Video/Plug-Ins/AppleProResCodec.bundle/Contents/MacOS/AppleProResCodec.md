## AppleProResCodec

> `/System/Library/Video/Plug-Ins/AppleProResCodec.bundle/Contents/MacOS/AppleProResCodec`

```diff

-  __TEXT.__text: 0x725c0
-  __TEXT.__auth_stubs: 0x800
+  __TEXT.__text: 0x7de38
+  __TEXT.__auth_stubs: 0x890
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x743f0
-  __TEXT.__gcc_except_tab: 0x3b4
-  __TEXT.__cstring: 0x3fb
+  __TEXT.__gcc_except_tab: 0x47c
+  __TEXT.__cstring: 0x577
   __TEXT.__oslogstring: 0x79
-  __TEXT.__unwind_info: 0x618
-  __TEXT.__eh_frame: 0x4a0
-  __DATA_CONST.__const: 0x1008
-  __DATA_CONST.__cfstring: 0x360
+  __TEXT.__unwind_info: 0x6a0
+  __TEXT.__eh_frame: 0x350
+  __DATA_CONST.__const: 0xb08
+  __DATA_CONST.__cfstring: 0x3e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x408
+  __DATA_CONST.__auth_got: 0x450
   __DATA_CONST.__got: 0x2b8
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__data: 0xfe
-  __DATA.__bss: 0xc30
+  __DATA.__bss: 0xff0
   __DATA.__common: 0x1
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 871
-  Symbols:   223
-  CStrings:  72
+  Functions: 1051
+  Symbols:   232
+  CStrings:  87
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__const : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__data : content changed
Symbols:
+ _CFArrayGetValues
+ _CFPreferencesCopyAppValue
+ _CFStringGetCString
+ _CFStringGetLength
+ _CFStringGetTypeID
+ _malloc_type_posix_memalign
+ _printf
+ _putchar
+ _strtol
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
