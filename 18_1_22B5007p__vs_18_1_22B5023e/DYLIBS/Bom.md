## Bom

> `/System/Library/PrivateFrameworks/Bom.framework/Bom`

```diff

-262.0.0.0.0
-  __TEXT.__text: 0x551e0
+264.0.0.0.0
+  __TEXT.__text: 0x55ea0
   __TEXT.__auth_stubs: 0x1840
-  __TEXT.__cstring: 0x11265
+  __TEXT.__cstring: 0x1156c
   __TEXT.__const: 0x14f8
   __TEXT.__oslogstring: 0xfbb
-  __TEXT.__unwind_info: 0xb58
+  __TEXT.__unwind_info: 0xb68
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0x9a8
   __AUTH_CONST.__auth_got: 0xc20

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1085
-  Symbols:   1471
-  CStrings:  2246
+  Functions: 1091
+  Symbols:   1477
+  CStrings:  2267
 
Symbols:
+ _BOMStreamAdvance
+ _BOMStreamReadUInt64
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/Bom/Copier/data_archive/data_archive_decoder.c"
+ "Could not create byte stream"
+ "Could not extract PKZip central directory header from entry"
+ "Could not extract PKZip local header from entry"
+ "Could not initialize the PKZip cipher"
+ "Could not parse NFTS extra field"
+ "Could not parse the PKZip NTFS extra field"
+ "Could not parse the PKZip digital signature"
+ "Could not read %!l(MISSING)u bytes from non-deterministic source"
+ "Could not read %!l(MISSING)u bytes from source"
+ "Could not read encrypted data"
+ "Could not read from the underlying origin"
+ "Could not set NTFS extra field"
+ "Format entry callback failed"
+ "Invalid PKZip archive digital signature signature: %!x(MISSING)"
+ "Jul 31 2024"
+ "PKZip archive digital signature"
+ "The extra buffer is not empty"
+ "The extra buffer is not large enough"
+ "Unknown NTFS tag value: %!u(MISSING)"
+ "data_archive_decoder_read_data"
+ "data_archive_decoder_read_entry"
+ "data_archive_decoder_rewind_data"
+ "data_archive_decoder_set_stream"
+ "decompress_streamed_data"
+ "decrypt_streamed_data"
+ "init_pkzip_cipher"
+ "parse_entry_pkzip_digital_signature"
+ "parse_entry_pkzip_extra_field_ntfs"
+ "pkzip extra field NTFS"
+ "read_streamed_data"
- "/Library/Caches/com.apple.xbs/Sources/Bom/Copier/data_archive/data_decoder.c"
- "Could not read %!l(MISSING)u bytes from source, only read %!l(MISSING)d"
- "Jul 10 2024"
- "PKZIP_SIGNATURE_DIGITAL_SIGNATURE\n"
- "Unsupported compression method: %!d(MISSING)"
- "data_decoder_read_data"
- "data_decoder_read_entry"
- "data_decoder_rewind_data"
- "data_decoder_set_stream"
- "decompress_data_blind"

```
