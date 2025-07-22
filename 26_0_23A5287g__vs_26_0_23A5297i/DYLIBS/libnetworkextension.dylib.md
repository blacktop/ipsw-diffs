## libnetworkextension.dylib

> `/usr/lib/libnetworkextension.dylib`

```diff

-2186.0.0.0.0
-  __TEXT.__text: 0x324ac
-  __TEXT.__auth_stubs: 0x1980
-  __TEXT.__objc_methlist: 0x228
-  __TEXT.__const: 0x24c
-  __TEXT.__cstring: 0x2932
-  __TEXT.__oslogstring: 0x7dcc
-  __TEXT.__unwind_info: 0x728
+2191.0.0.0.0
+  __TEXT.__text: 0x32710
+  __TEXT.__auth_stubs: 0x1970
+  __TEXT.__objc_methlist: 0x24c
+  __TEXT.__const: 0x25c
+  __TEXT.__cstring: 0x2936
+  __TEXT.__oslogstring: 0x7e54
+  __TEXT.__unwind_info: 0x730
   __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methname: 0x871
-  __TEXT.__objc_methtype: 0x205
-  __TEXT.__objc_stubs: 0x740
+  __TEXT.__objc_methname: 0x8d6
+  __TEXT.__objc_methtype: 0x20e
+  __TEXT.__objc_stubs: 0x780
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__const: 0x1b58
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a0
+  __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xcc8
+  __AUTH_CONST.__auth_got: 0xcc0
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__cfstring: 0x6e0
-  __AUTH_CONST.__objc_const: 0x518
+  __AUTH_CONST.__objc_const: 0x548
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x28
+  __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x50
-  __DATA.__bss: 0xb68
+  __DATA.__bss: 0xb78
   __DATA.__common: 0x3d
   __DATA_DIRTY.__data: 0xc
   __DATA_DIRTY.__bss: 0x2c0

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7C43F487-B88D-3B8D-A0A2-39F14334A396
-  Functions: 601
-  Symbols:   1753
-  CStrings:  1174
+  UUID: 92D31D91-EB74-3AD7-83B8-C208CF6FC3EF
+  Functions: 604
+  Symbols:   1761
+  CStrings:  1182
 
Symbols:
+ +[NEBloomFilter mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:tag:]
+ -[NEBloomFilter getFilterTag]
+ -[NEBloomFilter initWithData:numberOfBits:numberOfHashes:murmurSeed:mmapFilename:tag:]
+ -[NEBloomFilter setTag:]
+ -[NEBloomFilter tag]
+ _OBJC_IVAR_$_NEBloomFilter._tag
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:tag:
- +[NEBloomFilter mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:]
- -[NEBloomFilter initWithData:numberOfBits:numberOfHashes:murmurSeed:mmapFilename:]
- _objc_msgSend$mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:
- _objc_release_x9
CStrings:
+ "%@ - initFromFile: retrieved bloom filter data from mmap file %@ tag <%@>"
+ "%s: NEBloomFilter - <pid %d> format version (%llu) does not equal any valid version (%u or %u)"
+ "%s: NEBloomFilter - <pid %d> read from mmap <numberOfBits %d numberOfHashes %d murmurSeed %d bitmapSize %d tagSize %d><%@>"
+ "*56@0:8r*16*24I32I36I40I44@48"
+ "+[NEBloomFilter mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:tag:]"
+ "3"
+ "@52@0:8@16I24I28I32@36@44"
+ "B32@0:8r*16^{ne_bloom_filter={ne_bloom_filter_header=QQIIII}I^v^v*^vId}24"
+ "T@\"NSData\",&,N,V_tag"
+ "_tag"
+ "dataUsingEncoding:"
+ "getFilterTag"
+ "initWithData:encoding:"
+ "initWithData:numberOfBits:numberOfHashes:murmurSeed:mmapFilename:tag:"
+ "mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:tag:"
+ "setTag:"
+ "tag"
- "%@ - initFromFile: retrieved bloom filter data from mmap file %@"
- "%s: NEBloomFilter - <pid %d> format version (%llu) does not equal the current version (%u)"
- "*48@0:8r*16*24I32I36I40I44"
- "+[NEBloomFilter mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:]"
- "2"
- "@44@0:8@16I24I28I32@36"
- "B32@0:8r*16^{ne_bloom_filter={ne_bloom_filter_header=QQIIII}^v*^vId}24"
- "initWithData:numberOfBits:numberOfHashes:murmurSeed:mmapFilename:"
- "mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:"

```
