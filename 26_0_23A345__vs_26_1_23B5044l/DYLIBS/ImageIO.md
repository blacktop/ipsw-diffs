## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2773.0.1.2.0
-  __TEXT.__text: 0x3a1fb0
+2781.0.2.0.0
+  __TEXT.__text: 0x3a3740
   __TEXT.__auth_stubs: 0x41e0
   __TEXT.__objc_methlist: 0xd20
-  __TEXT.__const: 0x2ebb8
-  __TEXT.__gcc_except_tab: 0x211a4
-  __TEXT.__cstring: 0x9b48f
+  __TEXT.__const: 0x2ebf8
+  __TEXT.__gcc_except_tab: 0x211e0
+  __TEXT.__cstring: 0x9c08d
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0xd1e0
+  __TEXT.__unwind_info: 0xd230
   __TEXT.__eh_frame: 0x308
   __TEXT.__objc_classname: 0xe0
   __TEXT.__objc_methname: 0x2e13
   __TEXT.__objc_methtype: 0x24c0
   __TEXT.__objc_stubs: 0x2580
   __DATA_CONST.__got: 0x600
-  __DATA_CONST.__const: 0x4c088
+  __DATA_CONST.__const: 0x4c0a8
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH.__objc_data: 0x320
   __AUTH.__data: 0x1d0
   __DATA.__objc_ivar: 0x9c
-  __DATA.__data: 0x2bb0
-  __DATA.__bss: 0x4f20
+  __DATA.__data: 0x2bd0
+  __DATA.__bss: 0x4f60
   __DATA.__common: 0x1e98
   __DATA_DIRTY.__data: 0x168
   __DATA_DIRTY.__crash_info: 0x148

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: C18491E5-FD24-3B83-96C3-B8421D05C760
-  Functions: 13134
-  Symbols:   40985
-  CStrings:  24713
+  UUID: 25D5BC6D-3E7C-354D-ACF7-105B048A0907
+  Functions: 13159
+  Symbols:   41042
+  CStrings:  24775
 
Symbols:
+ _IsKeyFrame
+ _WebPAnimDecoderRestoreCanvas
+ _WebPAnimDecoderSkipFrame
+ _ZeroFillFrameRect
+ _ZeroFillFrameRect.cold.1
+ __Z13ParseUnormDFDPjjRjS0_Rb
+ __Z17GetKtx2FormatInfoP11ktxTexture2RP14Ktx2FormatInfo
+ __Z17ValidateKTXHeaderRK10_KTXHeadery
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.1
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.10
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.2
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.3
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.4
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.5
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.6
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.7
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.8
+ __Z17ValidateKTXHeaderRK10_KTXHeadery.cold.9
+ __Z18ParseCompressedDFDPjjjRP14Ktx2FormatInfo
+ __Z19GetKtx2VKFormatInfo8VkFormatRP14Ktx2FormatInfo
+ __Z20ExtractFormatFromDFDP11ktxTexture2RP14Ktx2FormatInfo
+ __Z21HandleZlibCompressionP11ktxTexture2RP14Ktx2FormatInfo
+ __Z21HandleZstdCompressionP11ktxTexture2RP14Ktx2FormatInfo
+ __Z28HandleSupercompressionSchemeP11ktxTexture2RP14Ktx2FormatInfo
+ __ZL21releaseGlobalWebPInfoPv
+ __ZN11OFDTemplate8parseXMLEPK8__CFData.cold.1
+ __ZN14GlobalWebPInfo14setFrameBufferEPhmjjj
+ __ZN14WebPReadPlugin24copyDecodedFrameToBufferEPhS0_jjji
+ __ZN14WebPReadPlugin27decodeAnimatedWebPOptimizedEP8WebPDataPhm
+ __ZN15IIO_Reader_KTX214validateHeaderERK11_KTX2Headerj
+ __ZNSt3__16vectorIZN15IIO_Reader_KTX214validateHeaderERK11_KTX2HeaderjE7SectionNS_9allocatorIS5_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIZN15IIO_Reader_KTX214validateHeaderERK11_KTX2HeaderjE7SectionNS_9allocatorIS5_EEE9push_backB8ne200100EOS5_
+ __ZZ18ParseCompressedDFDPjjjRP14Ktx2FormatInfoE14compressedInfo
+ __ZZ20ExtractFormatFromDFDP11ktxTexture2RP14Ktx2FormatInfoE7dfdInfo
+ __ZZ28HandleSupercompressionSchemeP11ktxTexture2RP14Ktx2FormatInfoE9basisInfo
+ __ZZN12IIOXPCClient12replyIsValidEPvE9validChar
+ ___block_descriptor_tmp.93
- _WebPAnimDecoderGetNext.cold.2
- __Z17GetKtx2FormatInfo8VkFormatRP14Ktx2FormatInfo
- __Z17ValidateKTXHeaderP10_KTXHeadery
- __ZN10siz_params8finalizeEb.cold.1
- __ZN13JP2ReadPlugin11validateJP2EP10IIOScanner.cold.1
- __ZN13JP2ReadPlugin11validateJP2EP10IIOScanner.cold.2
- __ZN13JP2ReadPlugin11validateJP2EP10IIOScanner.cold.3
- __ZN13JP2ReadPlugin11validateJP2EP10IIOScanner.cold.4
- __ZN14WebPReadPlugin18decodeAnimatedWebPEP8WebPDataPhm
- ___block_descriptor_tmp.92
CStrings:
+ "*** ERROR: BASIS_LZ supercompression requires SGD (Supercompression Global Data)"
+ "*** ERROR: Cubemaps cannot have depth\n"
+ "*** ERROR: DFD extends beyond file size\n"
+ "*** ERROR: DFD offset and length must both be 0 or both be non-zero\n"
+ "*** ERROR: DFD offset overlaps with header\n"
+ "*** ERROR: DFD too small: %d bytes\n"
+ "*** ERROR: GetKtx2FormatInfo: Unknown vkFormat %d\n"
+ "*** ERROR: KTX2 3D textures cannot have layers (%d)\n"
+ "*** ERROR: KTX2 numberOfFaces (%d) must be 1 or 6 (cubemap)\n"
+ "*** ERROR: KTX2 numberOfFaces must be greater than 0\n"
+ "*** ERROR: KTX2 numberOfMipmapLevels must be greater than 0\n"
+ "*** ERROR: KTX2 pixelHeight must be greater than 0\n"
+ "*** ERROR: KTX2 pixelWidth must be greater than 0\n"
+ "*** ERROR: KV extends beyond file size\n"
+ "*** ERROR: KVD extends beyond file size\n"
+ "*** ERROR: KVD length is non-zero but offset is 0"
+ "*** ERROR: KVD offset overlaps with header\n"
+ "*** ERROR: No DFD available for Zlib compressed texture\n"
+ "*** ERROR: No DFD available for Zstd compressed texture\n"
+ "*** ERROR: No DFD available for format extraction\n"
+ "*** ERROR: No texture data present in file"
+ "*** ERROR: Non-Khronos DFD not supported: %d\n"
+ "*** ERROR: SGD extends beyond file size\n"
+ "*** ERROR: SGD length is non-zero but offset is 0"
+ "*** ERROR: SGD offset overlaps with header\n"
+ "*** ERROR: SGD present but supercompression scheme is NONE"
+ "*** ERROR: Unsupported DFD color model: %d\n"
+ "*** ERROR: Unsupported supercompression scheme: %d\n"
+ "*** ERROR: bad 'COD ycb/ycb' (%d+%d)>12\n"
+ "*** ERROR: decodeAnimatedWebPOptimized failed\n"
+ "*** ERROR: duplicate FTYP File Type Box (count: %u)\n"
+ "*** ERROR: duplicate JP Signature Box (count: %u)\n"
+ "*** ERROR: duplicate JP2C Continuous Codestream Box (count: %u)\n"
+ "*** ERROR: duplicate JP2H Header Box (count: %u)\n"
+ "*** ERROR: failed to get _structure from XMLDictionaryCreateWithData\n"
+ "*** ERROR: format is 0 but no DFD present\n"
+ "*** ERROR: glFormat must be non-zero for uncompressed textures\n"
+ "*** ERROR: glInternalFormat must be non-zero\n"
+ "*** ERROR: glInternalFormat must be non-zero for compressed textures\n"
+ "*** ERROR: glType must be non-zero for uncompressed textures\n"
+ "*** ERROR: glTypeSize (%d) must be 1 for compressed textures\n"
+ "*** ERROR: glTypeSize must be non-zero for uncompressed textures\n"
+ "*** ERROR: invalid KTX2 identifier\n"
+ "*** ERROR: invalid xcb - failing 'COD xcb' check:  2 <= %d <= 10\n"
+ "*** ERROR: invalid ycb - failing 'COD ycb' check:  2 <= %d <= 10\n"
+ "*** ERROR: marker '%c%c%c%c' length (%llu) at offset (%llu [0x%llX]) larger than fileSize(%llu)\n"
+ "*** ERROR: missing or invalid ContinuousCodestreamBox count (%u)\n"
+ "*** ERROR: missing or invalid FileTypeBox count (%u)\n"
+ "*** ERROR: missing or invalid JP2HeaderBox count (%u)\n"
+ "*** ERROR: missing or invalid SignatureBox count (%u)\n"
+ "*** ERROR: numberOfFaces (%d) must be 1 or 6 (cubemap)\n"
+ "*** ERROR: numberOfMipmapLevels (%d) exceeds maximum possible mipmap levels (%d)\n"
+ "*** ERROR: numberOfMipmapLevels must be at least 1"
+ "*** ERROR: pixelWidth must be greater than 0\n"
+ "*** ERROR: sections overlap ['%c%c%c%c' [%llu,%llu) - '%c%c%c%c' [%llu,%llu)\n"
+ "*** ERROR: too many boxes (%u)\n"
+ "*** ERROR: unknown supercompressionScheme (%d)\n"
+ "*** KTX2: Handling supercompressed texture with scheme: %s\n"
+ "*** NOTE: Cubemap faces should be square"
+ "*** NOTE: Key-value data size not aligned to 4 bytes"
+ "*** NOTE: extended range image is inside sRGB -- converting to 8-bit\n"
+ "Basis Universal"
+ "ExtractFormatFromDFD"
+ "GetKtx2FormatInfo"
+ "GetKtx2VKFormatInfo"
+ "HandleSupercompressionScheme"
+ "HandleZlibCompression"
+ "HandleZstdCompression"
+ "ValidateKTXHeader"
+ "Zlib"
+ "Zstandard"
+ "parseXML"
+ "validateHeader"
+ "☀️  %s - updating <IOSurface: %p>  maxContentLightLevel: %d, maxFrameAverageLightLevel: %d\n"
- "*** ERROR: bad 'COD CodeBlockWidth' (%d)\n"
- "*** ERROR: decodeAnimatedWebP failed\n"
- "*** ERROR: marker '%c%c%c%c' length (%d) at offset (%d [0x%04X]) larger than fileSize(%d)\n"
- "*** ERROR: no ContinousCodestreamBox\n"
- "*** ERROR: no FileTypeBox\n"
- "*** ERROR: no JP2HeaderBox\n"
- "*** ERROR: no SignatureBox\n"
- "*** invalid KTX2 file: bytesOfKeyValueData: %d (fileSize: %d)\n"
- "COL extended range image is inside sRGB -- converting to 8-bit\n"
- "abcdefghijklmnopqrstuvwxyz0123456789_"
- "have_dims && have_size"
- "☀️  %s - updating <IOSurface: %p>  maxContentLightLevel: %d\n"

```
