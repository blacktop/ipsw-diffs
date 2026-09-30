## libAppleArchive.dylib

> `/usr/lib/libAppleArchive.dylib`

```diff

-423.100.6.0.0
-  __TEXT.__text: 0x82628
-  __TEXT.__auth_stubs: 0xed0
-  __TEXT.__cstring: 0x1155b
-  __TEXT.__const: 0x9b0
-  __TEXT.__oslogstring: 0x21
-  __TEXT.__unwind_info: 0xd28
-  __TEXT.__eh_frame: 0x48
+443.0.0.0.0
+  __TEXT.__text: 0x83620
+  __TEXT.__auth_stubs: 0xf20
+  __TEXT.__cstring: 0x11978
+  __TEXT.__const: 0x990
+  __TEXT.__oslogstring: 0x31
+  __TEXT.__unwind_info: 0xd58
+  __TEXT.__eh_frame: 0x90
   __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0xd8
-  __AUTH_CONST.__auth_got: 0x768
+  __DATA_CONST.__const: 0x148
+  __AUTH_CONST.__auth_got: 0x790
   __AUTH_CONST.__const: 0x70
   __AUTH_CONST.__cfstring: 0x40
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/libbz2.1.0.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/liblzma.5.dylib
-  UUID: DE634A07-85AE-3178-9A7B-46796E725DD1
-  Functions: 1054
-  Symbols:   2160
-  CStrings:  2835
+  UUID: 62EBFBF4-E4CD-372C-BB89-AA690E41F59C
+  Functions: 1059
+  Symbols:   2169
+  CStrings:  2888
 
Symbols:
+ _CCCryptorCreateWithMode
+ _CCCryptorFinal
+ _CCCryptorGetOutputLength
+ _CCCryptorRelease
+ _CCCryptorUpdate
+ _CCDeriveKey
+ _CCHmacFinal
+ _CCHmacInit
+ _CCHmacUpdate
+ _CCKDFParametersCreateHkdf
+ _CCKDFParametersDestroy
+ _aaCreateArchString
+ _aaEntryMCOStringCreateWithPath
+ _aaGetBinaryTypeString
+ _aaGetMagic
+ _aaPReadExpected
+ _aaParseARSection
+ _aaParseMachOSection
+ _rawimg_allocate_header_and_footer
- _bxdiff5Alloc
- _ccaes_ctr_crypt_mode
- _cchkdf
- _cchmac_final
- _cchmac_init
- _cchmac_update
- _ccsha256_di
- _decodeStreamDiscard
- _getHeader
CStrings:
+ "\t<%s>\n"
+ " (0x%x %i %i %u %llu %llu %u)"
+ " [%s, %s, %s]"
+ "%s (N=%u)"
+ "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AAFieldMCO.c"
+ "1 0x%x %u"
+ "?"
+ "A file composed of other Mach-Os"
+ "AAEntryMCOBlobInitWithFD"
+ "AEAD can't operate in-place"
+ "CCDeriveKey"
+ "CCKDFParametersCreateHkdf"
+ "Can't allocate header/footer"
+ "Can't init MCO"
+ "Companion file with only debug sections"
+ "Core file"
+ "Cryptor creation"
+ "Demand paged executable file"
+ "Dynamic link editor"
+ "Dynamically bound bundle file"
+ "Dynamically bound shared library"
+ "Encryption"
+ "Fat GPU binary"
+ "Fat GPU binary BE"
+ "Fat binary"
+ "Fat binary 64-bit"
+ "Fat binary 64-bit BE"
+ "Fat binary BE"
+ "Fixed VM shared library file"
+ "Fork missing header/footer"
+ "GPU program"
+ "GPU support functions"
+ "MCO creation failed"
+ "Mach-O"
+ "Mach-O 64-bit"
+ "Mach-O 64-bit BE"
+ "Mach-O BE"
+ "No more data"
+ "Object archive"
+ "Object archive BE"
+ "Preloaded executable file"
+ "Refill buffer failed"
+ "Relocatable object file"
+ "Shared library stub for static linking only"
+ "String overflow"
+ "Too many arches"
+ "Too much fork padding: %zu"
+ "[0x%08x] %{public}s"
+ "[0x%08x](warning) %{public}s"
+ "aaCreateArchString"
+ "aaEntryMCOStringCreateWithPath"
+ "aaPReadExpected"
+ "aaParseFatFile"
+ "arm"
+ "arm64"
+ "arm64_32"
+ "arm64e"
+ "fetching Mach-O information: %s"
+ "fstat failed"
+ "inserting MCO: %s"
+ "pread failed"
+ "x86"
+ "x86_64"
+ "x86_64 kexts"
+ "x86_64h"
- "HKDF"
- "HMACDerive_SHA256"
- "[0x%08x] %s"
- "[0x%08x](warning) %s"
- "decodeStreamDiscard"
- "discard data failed"
- "encryption"
- "init"
- "load header failed"
- "refill buffer failed"
- "too much padding"
- "updating buffer"

```
