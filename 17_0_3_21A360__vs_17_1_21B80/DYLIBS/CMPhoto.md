## CMPhoto

> `/System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto`

```diff

-239.0.0.0.0
-  __TEXT.__text: 0xd9f70
-  __TEXT.__auth_stubs: 0x2ed0
-  __TEXT.__objc_methlist: 0x340
-  __TEXT.__const: 0xa550
-  __TEXT.__cstring: 0x4b8e
+244.6.0.0.0
+  __TEXT.__text: 0xdbdc0
+  __TEXT.__auth_stubs: 0x2f60
+  __TEXT.__objc_methlist: 0x390
+  __TEXT.__const: 0xa5d0
+  __TEXT.__cstring: 0x4efe
   __TEXT.__gcc_except_tab: 0x104
   __TEXT.__oslogstring: 0x168
-  __TEXT.__unwind_info: 0x18b8
+  __TEXT.__unwind_info: 0x18e0
   __TEXT.__eh_frame: 0x88
-  __TEXT.__objc_classname: 0x35
-  __TEXT.__objc_methname: 0x1731
-  __TEXT.__objc_methtype: 0x9ac
-  __TEXT.__objc_stubs: 0x16c0
+  __TEXT.__objc_classname: 0x54
+  __TEXT.__objc_methname: 0x1b3f
+  __TEXT.__objc_methtype: 0xa63
+  __TEXT.__objc_stubs: 0x1b00
   __DATA_CONST.__got: 0xff0
-  __DATA_CONST.__const: 0x1de0
-  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__const: 0x1e00
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x830
-  __DATA_CONST.__objc_selrefs: 0x610
+  __DATA_CONST.__objc_const: 0xaa0
+  __DATA_CONST.__objc_selrefs: 0x720
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__cfstring: 0x49c0
+  __AUTH_CONST.__cfstring: 0x4b40
   __AUTH_CONST.__auth_ptr: 0x78
   __AUTH_CONST.__const: 0x7d8
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__objc_const: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1780
-  __DATA.__objc_classrefs: 0xc8
-  __DATA.__objc_superrefs: 0x18
-  __DATA.__objc_ivar: 0xcc
+  __AUTH_CONST.__auth_got: 0x17c8
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_classrefs: 0xf8
+  __DATA.__objc_superrefs: 0x20
+  __DATA.__objc_ivar: 0x110
   __DATA.__data: 0x330
-  __DATA.__bss: 0x430
+  __DATA.__bss: 0x438
   __DATA.__common: 0x40
-  __DATA_DIRTY.__const: 0xa48
+  __DATA_DIRTY.__const: 0xa68
   __DATA_DIRTY.__objc_const: 0x120
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x830

   - /System/Library/PrivateFrameworks/AppleJPEGXL.framework/AppleJPEGXL
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
+  - /System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2120
-  Symbols:   6230
-  CStrings:  1048
+  Functions: 2145
+  Symbols:   6353
+  CStrings:  1138
 
Symbols:
+ -[CMPhotoInterchangeCompactMetal initWithDevice:encode:bayer:quadra:depth:]
+ -[CMPhotoInterchangeCompactMetal prepareData]
+ -[CMPhotoInterchangeCompactMetal prepareDst:]
+ -[CMPhotoInterchangeCompactMetal prepareDst:].cold.1
+ -[CMPhotoInterchangeCompactMetal prepareDst:].cold.2
+ -[CMPhotoInterchangeCompactMetal prepareDst:].cold.3
+ -[CMPhotoInterchangeCompactMetal prepareDst:].cold.4
+ -[CMPhotoInterchangeCompactMetal prepareSrc:]
+ -[CMPhotoInterchangeCompactMetal prepareSrc:].cold.1
+ -[CMPhotoInterchangeCompactMetal prepareTexture:usage:]
+ -[CMPhotoInterchangeCompactMetal sendRenderCommand]
+ -[CMPhotoInterchangeCompactMetal sendRenderCommand].cold.1
+ -[CMPhotoInterchangeCompactMetal sendRenderCommand].cold.2
+ -[CMPhotoInterchangeCompactMetal sendRenderCommand].cold.3
+ -[CMPhotoInterchangeCompactMetal sendRenderCommand].cold.4
+ _CMPhotoHEIFFileWriterCompareReservedImageHandleWithOptions.onceToken
+ _CMPhotoInterchangeCompactDecode
+ _CMPhotoInterchangeCompactDecode.cold.1
+ _CMPhotoInterchangeCompactEncode
+ _CMPhotoInterchangeCompactEncode.cold.1
+ _IOSurfaceGetBaseAddressOfCompressedTileDataRegionOfPlane
+ _IOSurfaceGetBaseAddressOfCompressedTileHeaderRegionOfPlane
+ _IOSurfaceGetBytesPerTileDataOfPlane
+ _IOSurfaceGetCompressedTileHeightOfPlane
+ _IOSurfaceGetCompressedTileWidthOfPlane
+ _IOSurfaceGetCompressionTypeOfPlane
+ _IOSurfaceGetHeightInCompressedTilesOfPlane
+ _IOSurfaceGetWidthInCompressedTilesOfPlane
+ _IntcDecodeFrame
+ _IntcEncodeFrame
+ _OBJC_CLASS_$_CMPhotoInterchangeCompactMetal
+ _OBJC_CLASS_$_MTLComputePipelineDescriptor
+ _OBJC_CLASS_$_MTLFunctionConstantValues
+ _OBJC_CLASS_$_MTLRenderPassDescriptor
+ _OBJC_CLASS_$_MTLRenderPipelineDescriptor
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_IVAR_$_CMPhotoInterchangeCompactMetal._mBufferA
+ _OBJC_IVAR_$_CMPhotoInterchangeCompactMetal._mBufferB
+ _OBJC_IVAR_$_CMPhotoInterchangeCompactMetal._mBufferResult
+ _OBJC_IVAR_$_CMPhotoInterchangeCompactMetal._mCommandQueue
+ _OBJC_IVAR_$_CMPhotoInterchangeCompactMetal._mCompactMetadataPSO
+ _OBJC_IVAR_$_CMPhotoInterchangeCompactMetal._mDevice
+ _OBJC_IVAR_$_CMPhotoInterchangeCompactMetal._mDstBuf
+ _OBJC_IVAR_$_CMPhotoInterchangeCompactMetal._mDstMetaOffset
+ _OBJC_IVAR_$_CMPhotoInterchangeCompactMetal._mDstTex
+ _OBJC_IVAR_$_CMPhotoInterchangeCompactMetal._mSrcTex
+ _OBJC_IVAR_$_CMPhotoInterchangeCompactMetal._mask
+ _OBJC_IVAR_$_CMPhotoInterchangeCompactMetal._renderPipeline
+ _OBJC_IVAR_$_CMPhotoInterchangeCompactMetal._renderToTextureRenderPassDescriptor
+ _OBJC_IVAR_$_CMPhotoInterchangeCompactMetal.mb_height
+ _OBJC_IVAR_$_CMPhotoInterchangeCompactMetal.mb_width
+ _OBJC_IVAR_$_CMPhotoInterchangeCompactMetal.meta_length
+ _OBJC_IVAR_$_CMPhotoInterchangeCompactMetal.meta_size
+ _OBJC_METACLASS_$_CMPhotoInterchangeCompactMetal
+ _SlimVideoDecoder_SessionIsSlimIntc
+ __OBJC_$_INSTANCE_METHODS_CMPhotoInterchangeCompactMetal
+ __OBJC_$_INSTANCE_VARIABLES_CMPhotoInterchangeCompactMetal
+ __OBJC_CLASS_RO_$_CMPhotoInterchangeCompactMetal
+ __OBJC_METACLASS_RO_$_CMPhotoInterchangeCompactMetal
+ ___CMPhotoHEIFFileWriterCompareReservedImageHandleWithOptions_block_invoke
+ __agxXBiasedTwiddle
+ __configureJXLColor
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$colorAttachments
+ _objc_msgSend$drawPrimitives:vertexStart:vertexCount:
+ _objc_msgSend$endEncoding
+ _objc_msgSend$initWithDevice:encode:bayer:quadra:depth:
+ _objc_msgSend$iosurface
+ _objc_msgSend$iosurfacePlane
+ _objc_msgSend$newBufferWithIOSurface:
+ _objc_msgSend$newBufferWithLength:options:
+ _objc_msgSend$newComputePipelineStateWithDescriptor:options:reflection:error:
+ _objc_msgSend$newDefaultLibraryWithBundle:error:
+ _objc_msgSend$newFunctionWithName:
+ _objc_msgSend$newFunctionWithName:constantValues:error:
+ _objc_msgSend$newRenderPipelineStateWithDescriptor:error:
+ _objc_msgSend$prepareData
+ _objc_msgSend$prepareDst:
+ _objc_msgSend$prepareSrc:
+ _objc_msgSend$prepareTexture:usage:
+ _objc_msgSend$renderCommandEncoderWithDescriptor:
+ _objc_msgSend$sendRenderCommand
+ _objc_msgSend$setClearColor:
+ _objc_msgSend$setComputeFunction:
+ _objc_msgSend$setConstantValue:type:atIndex:
+ _objc_msgSend$setFragmentFunction:
+ _objc_msgSend$setFragmentTexture:atIndex:
+ _objc_msgSend$setLabel:
+ _objc_msgSend$setLoadAction:
+ _objc_msgSend$setPixelFormat:
+ _objc_msgSend$setRenderPipelineState:
+ _objc_msgSend$setStoreAction:
+ _objc_msgSend$setTexture:
+ _objc_msgSend$setVertexBytes:length:atIndex:
+ _objc_msgSend$setVertexFunction:
+ _objc_msgSend$waitUntilCompleted
+ _objc_opt_new
+ _sendRenderCommand.quadVertices
CStrings:
+ "(IOSurfaceGetCompressionTypeOfPlane(_mDstTex.iosurface, _mDstTex.iosurfacePlane) == kIOSurfaceCompressionTypeInterchange) || (IOSurfaceGetCompressionTypeOfPlane(_mSrcTex.iosurface, _mSrcTex.iosurfacePlane) == kIOSurfaceCompressionTypeInterchange)"
+ "-[CMPhotoInterchangeCompactMetal prepareDst:]"
+ "-[CMPhotoInterchangeCompactMetal prepareSrc:]"
+ "-[CMPhotoInterchangeCompactMetal sendRenderCommand]"
+ "@\"<MTLBuffer>\""
+ "@\"<MTLComputePipelineState>\""
+ "@\"<MTLDevice>\""
+ "@\"<MTLRenderPipelineState>\""
+ "@\"<MTLTexture>\""
+ "@\"MTLRenderPassDescriptor\""
+ "@32@0:8^{__IOSurface=}16Q24"
+ "@40@0:8@16B24B28B32c36"
+ "CMPhotoInterchangeCompact.m"
+ "CMPhotoInterchangeCompactMetal"
+ "CMPhotoInterchangeCompactMetal.m"
+ "Command Buffer"
+ "Compact Metadata Compute Pipeline"
+ "Interchange Compact Repack Pipeline"
+ "Interchange Compact Unpack Pipeline"
+ "Offscreen Render Pass"
+ "S"
+ "_compact"
+ "_expand"
+ "_mBufferA"
+ "_mBufferB"
+ "_mBufferResult"
+ "_mCommandQueue"
+ "_mCompactMetadataPSO"
+ "_mDevice"
+ "_mDstBuf"
+ "_mDstBuf != nil"
+ "_mDstMetaOffset"
+ "_mDstTex"
+ "_mDstTex != nil"
+ "_mSrcTex"
+ "_mSrcTex != nil"
+ "_mask"
+ "_mask == mask"
+ "_renderPipeline"
+ "_renderToTextureRenderPassDescriptor"
+ "bayer_repack_fs"
+ "bayer_unpack_fs"
+ "bundleForClass:"
+ "colorAttachments"
+ "commandBuffer != nil"
+ "compact_metadata_cs"
+ "deviceSPI != nil"
+ "drawPrimitives:vertexStart:vertexCount:"
+ "endEncoding"
+ "initWithDevice:encode:bayer:quadra:depth:"
+ "iosurface"
+ "iosurfacePlane"
+ "mb_height"
+ "mb_width"
+ "meta_length"
+ "meta_size"
+ "newBufferWithIOSurface:"
+ "newBufferWithLength:options:"
+ "newComputePipelineStateWithDescriptor:options:reflection:error:"
+ "newDefaultLibraryWithBundle:error:"
+ "newFunctionWithName:"
+ "newFunctionWithName:constantValues:error:"
+ "newRenderPipelineStateWithDescriptor:error:"
+ "prepareData"
+ "prepareDst:"
+ "prepareSrc:"
+ "prepareTexture:usage:"
+ "quadra_repack_fs"
+ "quadra_unpack_fs"
+ "renderCommandEncoderWithDescriptor:"
+ "renderEncoder != nil"
+ "renderPipeline != nil"
+ "sendRenderCommand"
+ "setClearColor:"
+ "setComputeFunction:"
+ "setConstantValue:type:atIndex:"
+ "setFragmentFunction:"
+ "setFragmentTexture:atIndex:"
+ "setLabel:"
+ "setLoadAction:"
+ "setPixelFormat:"
+ "setRenderPipelineState:"
+ "setStoreAction:"
+ "setTexture:"
+ "setVertexBytes:length:atIndex:"
+ "setVertexFunction:"
+ "simple_fs"
+ "simple_vs"
+ "size == dataLength"
+ "waitUntilCompleted"

```
