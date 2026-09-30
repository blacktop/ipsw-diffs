## CMImaging

> `/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__oslogstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-758.0.0.122.2
-  __TEXT.__text: 0x1da208
+761.0.0.0.3
+  __TEXT.__text: 0x1da510
   __TEXT.__objc_methlist: 0xd3bc
   __TEXT.__const: 0x2e40
   __TEXT.__oslogstring: 0x1551e
-  __TEXT.__cstring: 0x28b23
+  __TEXT.__cstring: 0x28bdb
   __TEXT.__gcc_except_tab: 0x154c
   __TEXT.__unwind_info: 0x31e0
   __TEXT.__eh_frame: 0x6e8

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x410
-  __DATA_CONST.__got: 0xc48
+  __DATA_CONST.__got: 0xc58
   __AUTH_CONST.__const: 0x810
-  __AUTH_CONST.__cfstring: 0x6be0
-  __AUTH_CONST.__objc_const: 0x1f118
+  __AUTH_CONST.__cfstring: 0x6c20
+  __AUTH_CONST.__objc_const: 0x1f158
   __AUTH_CONST.__objc_intobj: 0xba0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x1130
   __AUTH_CONST.__auth_got: 0xc00
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x17d4
+  __DATA.__objc_ivar: 0x17dc
   __DATA.__data: 0x12d90
   __DATA.__common: 0x1e0
   __DATA.__bss: 0x70

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 7597
-  Symbols:   10392
-  CStrings:  5293
+  Symbols:   10396
+  CStrings:  5295
 
Symbols:
+ _OBJC_IVAR_$_CMIStyleEngineApplyStyle._skinMaskPurpose
+ _OBJC_IVAR_$_CMIStyleEngineProcessor._skinMaskPurpose
+ _kFigCaptureSampleBufferMetadata_IntermediateZoomDstRect
+ _kFigCaptureSampleBufferMetadata_IntermediateZoomSrcRect
CStrings:
+ "%@ColorPrimaries:%@, YCbCrMatrix:%@, TransferFunction:%@"
+ "( inputTexture.pixelFormat == outputTexture.pixelFormat ) || ( [CMIGuidedFilter isSingleChannelTexture:inputTexture] && [CMIGuidedFilter isSingleChannelTexture:outputTexture] )"
+ "N/A"
+ "err = FigSignalErrorAt3(\"%s%s%s signalled err=%d (%s) (%s) at %s:%d\", gStyleEngineProcessorTrace.note.emitter, (CMIStyleEngineStatusResourcesNotReleased), \"CMIStyleEngineStatusResourcesNotReleased\", (\"FigMetalAllocator resources not correctly released\"), \"<<<< StyleEngineProcessor >>>>\", __FUNCTION__, \"CMIStyleEngineProcessor.m\", 3625, __builtin_return_address(0), 0) == 0 "
- "err = FigSignalErrorAt3(\"%s%s%s signalled err=%d (%s) (%s) at %s:%d\", gStyleEngineProcessorTrace.note.emitter, (CMIStyleEngineStatusResourcesNotReleased), \"CMIStyleEngineStatusResourcesNotReleased\", (\"FigMetalAllocator resources not correctly released\"), \"<<<< StyleEngineProcessor >>>>\", __FUNCTION__, \"CMIStyleEngineProcessor.m\", 3586, __builtin_return_address(0), 0) == 0 "
- "inputTexture.pixelFormat == outputTexture.pixelFormat"
```
