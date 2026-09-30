## liblog_geo.dylib

> `/usr/lib/log/liblog_geo.dylib`

```diff

-2027.33.11.13.3
-  __TEXT.__text: 0x2cec
-  __TEXT.__auth_stubs: 0x380
+2031.34.7.17.30
+  __TEXT.__text: 0x2e44
+  __TEXT.__auth_stubs: 0x340
   __TEXT.__objc_methlist: 0x16c
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x4c

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x230
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1d0
+  __AUTH_CONST.__auth_got: 0x1b0
   __AUTH_CONST.__const: 0xc8
   __AUTH_CONST.__cfstring: 0xbcc0
   __AUTH_CONST.__objc_const: 0x218

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A4AA4E51-3186-3422-AED7-59E6C7A61088
+  UUID: DAAFF5C9-F122-3351-B6ED-E96444829AD7
   Functions: 47
-  Symbols:   289
+  Symbols:   285
   CStrings:  3128
 
Symbols:
+ _objc_retain_x19
+ _objc_retain_x23
+ _objc_retain_x25
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[GEOLogFormatter(PropertyList) descriptionForPropertyListData:capturedStateType:] : 124 -> 132
~ -[GEOLogFormatter(Struct) formattedStringForStructType:data:] : 428 -> 432
~ _formatDataRequestKind : 72 -> 76
~ _formatTileKey : 736 -> 744
~ _StringsCaseInsensitiveEqual : 200 -> 196
~ ___StringsCaseInsensitiveEqual_block_invoke : 72 -> 76
~ -[GEOLogFormatter formattedStringForStateType:data:] : 200 -> 208
~ -[GEOLogFormatter formattedAttributedStringForType:value:] : 264 -> 280
~ -[GEOLogFormatter init] : 128 -> 132
~ +[GEOLogFormatter sharedFormatter] : 160 -> 176
~ -[GEOLogFormatter(Protobuf) formattedStringForProtobufType:data:] : 392 -> 420
~ _OSLogCopyFormattedString : 156 -> 168
~ _OSStateCreateStringWithData : 188 -> 204
~ -[Multipart isEqualToMultipart:] : 100 -> 104
~ -[Multipart copyWithZone:] : 4 -> 40
~ -[GEOLogFormatter(RequestResponse) formattedStringForRequestResponseMultipart:partData:className:compressed:] : 716 -> 752
~ _decompress : 388 -> 392
~ _formattedStringFromProtobuf : 748 -> 788
~ _scanDict : 604 -> 628
~ _scanArr : 496 -> 516
~ _getNameAndRemainderAtOffset : 308 -> 324
~ -[GEOLogFormatter(RequestResponse) formattedStringForRequestResponse:] : 196 -> 208
~ -[GEOLogFormatter(RequestResponse) formattedStringForRequestResponseType:value:] : 500 -> 496
~ ___80-[GEOLogFormatter(RequestResponse) formattedStringForRequestResponseType:value:]_block_invoke : 80 -> 84
~ -[GEOLogFormatter(Enum) formattedStringForEnumType:number:] : 160 -> 164
~ _formattedGEOTileSetStyleForNumber : 1500 -> 1504
~ _formattedTileLoadOptionsForNumber : 400 -> 416
~ -[GEOLogFormatter(Enum) formattedStringForEnumType:value:] : 192 -> 196

```
