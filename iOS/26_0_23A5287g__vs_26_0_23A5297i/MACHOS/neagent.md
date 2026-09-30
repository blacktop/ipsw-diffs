## neagent

> `/usr/libexec/neagent`

```diff

-2186.0.0.0.0
-  __TEXT.__text: 0x1354c
+2191.0.0.0.0
+  __TEXT.__text: 0x13a30
   __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_stubs: 0x1920
-  __TEXT.__objc_methlist: 0xf48
-  __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x278
-  __TEXT.__objc_methname: 0x2301
-  __TEXT.__oslogstring: 0x2b70
-  __TEXT.__cstring: 0xea2
+  __TEXT.__objc_stubs: 0x19c0
+  __TEXT.__objc_methlist: 0xfa8
+  __TEXT.__const: 0xd0
+  __TEXT.__gcc_except_tab: 0x290
+  __TEXT.__objc_methname: 0x2381
+  __TEXT.__oslogstring: 0x2c57
+  __TEXT.__cstring: 0xeb7
   __TEXT.__objc_classname: 0x31b
-  __TEXT.__objc_methtype: 0xd3e
-  __TEXT.__unwind_info: 0x328
+  __TEXT.__objc_methtype: 0xd47
+  __TEXT.__unwind_info: 0x330
   __DATA_CONST.__auth_got: 0x3d0
   __DATA_CONST.__got: 0x178
   __DATA_CONST.__const: 0x4b0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x48
-  __DATA.__objc_const: 0x1c80
-  __DATA.__objc_selrefs: 0x9d8
-  __DATA.__objc_ivar: 0x128
+  __DATA.__objc_const: 0x1cb8
+  __DATA.__objc_selrefs: 0xa10
+  __DATA.__objc_ivar: 0x12c
   __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x840
   __DATA.__bss: 0x90

   - /System/Library/PrivateFrameworks/CipherML.framework/CipherML
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 465C626F-FEDA-3A3C-897C-47A0892AAA85
-  Functions: 284
+  UUID: A2D17CB6-59E3-3781-B662-B07FB7C9EFBB
+  Functions: 290
   Symbols:   174
-  CStrings:  906
+  CStrings:  918
 
Symbols:
+ _unlink
- _objc_release_x9
CStrings:
+ "%@ - initFromFile: retrieved bloom filter data from mmap file %@ tag <%@>"
+ "%@: %s - Deleted file %s"
+ "%@: %s - Failed to delete file %s: [%d] %s"
+ "%@: %s - fetchPreFilterDataWithCompletion - data <%lu bytes>, file %@, sb_extension <%s>, tag <%@> numberOfBits %d, numberOfHashes %d, murmurSeed %d, error %@"
+ "%@: %s - fetchPreFilterDataWithCompletion - data <%lu bytes>, file %@, sb_extension <%s>, tag <%@>,  numberOfBits %d, numberOfHashes  %d, murmurSeed %d, error %@"
+ "%@: %s - savePrefilterData <%u bytes of data> bits %u hashes %u seed %u - using mmap file %@ tag %@"
+ "%s: NEBloomFilter - <pid %d> format version (%llu) does not equal any valid version (%u or %u)"
+ "%s: NEBloomFilter - <pid %d> read from mmap <numberOfBits %d numberOfHashes %d murmurSeed %d bitmapSize %d tagSize %d><%@>"
+ "*56@0:8r*16*24I32I36I40I44@48"
+ "+[NEBloomFilter mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:tag:]"
+ "-[NEAgentURLFilterExtension savePrefilterData:fileURL:sandboxExtension:numberOfBits:numberOfHashes:murmurSeed:tag:]"
+ "3"
+ "@52@0:8@16I24I28I32@36@44"
+ "B32@0:8r*16^{ne_bloom_filter={ne_bloom_filter_header=QQIIII}I^v^v*^vId}24"
+ "T@\"NSData\",&,N,V_tag"
+ "_tag"
+ "dataUsingEncoding:"
+ "fetchPrefilterDataWithTag:completion:"
+ "getFilterTag"
+ "getPrefilterTag"
+ "getTag"
+ "initWithData:encoding:"
+ "initWithData:numberOfBits:numberOfHashes:murmurSeed:mmapFilename:tag:"
+ "mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:tag:"
+ "setTag:"
+ "tag"
+ "v60@?0@\"NSData\"8@\"NSURL\"16@\"NSString\"24@\"NSString\"32I40I44I48@\"NSError\"52"
- "%@ - initFromFile: retrieved bloom filter data from mmap file %@"
- "%@: %s - fetchPreFilterDataWithCompletion - data <%lu bytes>, file %@, sb_extension <%s>, numberOfBits %d, numberOfHashes  %d, murmurSeed %d, error %@"
- "%@: %s - fetchPreFilterDataWithCompletion - data <%lu bytes>, file %@, sb_extension <%s>, numberOfBits %d, numberOfHashes %d, murmurSeed %d, error %@"
- "%@: %s - savePrefilterData <%u bytes of data> bits %u hashes %u seed %u - using mmap file %@"
- "%s: NEBloomFilter - <pid %d> format version (%llu) does not equal the current version (%u)"
- "*48@0:8r*16*24I32I36I40I44"
- "+[NEBloomFilter mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:]"
- "-[NEAgentURLFilterExtension savePrefilterData:fileURL:sandboxExtension:numberOfBits:numberOfHashes:murmurSeed:]"
- "2"
- "@44@0:8@16I24I28I32@36"
- "B32@0:8r*16^{ne_bloom_filter={ne_bloom_filter_header=QQIIII}^v*^vId}24"
- "fetchPrefilterDataWithCompletion:"
- "initWithData:numberOfBits:numberOfHashes:murmurSeed:mmapFilename:"
- "mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:"
- "v52@?0@\"NSData\"8@\"NSURL\"16@\"NSString\"24I32I36I40@\"NSError\"44"

```
