## ISPKit

> `/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`

```diff

-  __TEXT.__text: 0x1ff04
-  __TEXT.__objc_methlist: 0x1f9c
+  __TEXT.__text: 0x200f8
+  __TEXT.__objc_methlist: 0x1fac
   __TEXT.__const: 0x280
   __TEXT.__gcc_except_tab: 0x620
   __TEXT.__cstring: 0x1764
-  __TEXT.__oslogstring: 0x2ece
+  __TEXT.__oslogstring: 0x2f60
   __TEXT.__dlopen_cstrs: 0xa6
   __TEXT.__unwind_info: 0x660
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12a0
+  __DATA_CONST.__objc_selrefs: 0x12a8
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0x70
-  __DATA_CONST.__got: 0x0
+  __DATA_CONST.__got: 0x1f0
   __AUTH_CONST.__const: 0x30
   __AUTH_CONST.__cfstring: 0x16a0
-  __AUTH_CONST.__objc_const: 0x6f98
+  __AUTH_CONST.__objc_const: 0x6fb8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x5b8
+  __DATA.__objc_ivar: 0x5bc
   __DATA.__data: 0x180
   __DATA.__bss: 0x78
-  __DATA_DIRTY.__objc_data: 0xdc0
+  __DATA_DIRTY.__objc_data: 0x1040
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 938
-  Symbols:   3595
-  CStrings:  723
+  Functions: 942
+  Symbols:   3605
+  CStrings:  726
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
Symbols:
+ -[LLVProcessorBufferManager emptyHumanFullBodiesMask]
+ _OBJC_IVAR_$_LLVProcessorBufferManager._emptyHumanFullBodiesMask
+ _objc_msgSend$emptyHumanFullBodiesMask
Functions:
~ -[ABDLookupTable getValueFor:] : 656 -> 660
~ -[LLVProcessorBufferManager prepareAllBuffersWithInput:inputHumanFullBodiesMask:output:scale1Width:scale1Height:opticalFlowWidth:opticalFlowHeight:] : 804 -> 812
+ -[LLVProcessorBufferManager emptyHumanFullBodiesMask]
~ -[LLVProcessorBufferManager .cxx_destruct] : 248 -> 260
+ -[LLVProcessorBufferManager emptyHumanFullBodiesMask].cold.2
- -[LLVProcessorBufferManager dumpAllBuffersToDirectory:frameIndex:].cold.2
+ -[LLVProcessorBufferManager dumpAllBuffersToDirectory:frameIndex:].cold.1
+ -[LLVProcessorBufferManager dumpAllBuffersToDirectory:frameIndex:].cold.23
+ -[LLVProcessorBufferManager dumpAllBuffersToDirectory:frameIndex:].cold.25
CStrings:
+ "1x1 emptyHumanFullBodiesMask created"
+ "Failed to create empty human full bodies mask"
+ "Failed to get base address for emptyHumanFullBodiesMask"
+ "Failed to lock base address for emptyHumanFullBodiesMask"
- "Input human full bodies mask pixel buffer not set"

```
