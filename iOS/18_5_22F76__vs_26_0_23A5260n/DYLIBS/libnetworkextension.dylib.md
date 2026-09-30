## libnetworkextension.dylib

> `/usr/lib/libnetworkextension.dylib`

```diff

-2063.120.19.0.0
-  __TEXT.__text: 0x2d384
-  __TEXT.__auth_stubs: 0x17f0
-  __TEXT.__objc_methlist: 0x14
-  __TEXT.__const: 0x20c
-  __TEXT.__cstring: 0x2526
-  __TEXT.__oslogstring: 0x6fb9
-  __TEXT.__unwind_info: 0x670
-  __TEXT.__objc_classname: 0x13
-  __TEXT.__objc_methname: 0x116
-  __TEXT.__objc_methtype: 0x11
-  __TEXT.__objc_stubs: 0x140
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x1808
-  __DATA_CONST.__objc_classlist: 0x8
+2167.0.0.0.2
+  __TEXT.__text: 0x3291c
+  __TEXT.__auth_stubs: 0x1990
+  __TEXT.__objc_methlist: 0x228
+  __TEXT.__const: 0x24c
+  __TEXT.__cstring: 0x2932
+  __TEXT.__oslogstring: 0x7e08
+  __TEXT.__unwind_info: 0x730
+  __TEXT.__objc_classname: 0x53
+  __TEXT.__objc_methname: 0x871
+  __TEXT.__objc_methtype: 0x205
+  __TEXT.__objc_stubs: 0x740
+  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__const: 0x1b58
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x50
-  __AUTH_CONST.__auth_got: 0xc00
-  __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x5c0
-  __AUTH_CONST.__objc_const: 0x90
-  __DATA.__data: 0x4c
-  __DATA.__bss: 0xa90
+  __DATA_CONST.__objc_selrefs: 0x2a0
+  __DATA_CONST.__objc_superrefs: 0x10
+  __AUTH_CONST.__auth_got: 0xcd0
+  __AUTH_CONST.__const: 0x300
+  __AUTH_CONST.__cfstring: 0x6e0
+  __AUTH_CONST.__objc_const: 0x518
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x28
+  __DATA.__data: 0x50
+  __DATA.__bss: 0xb68
   __DATA.__common: 0x3d
-  __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x300
+  __DATA_DIRTY.__data: 0xc
+  __DATA_DIRTY.__bss: 0x2c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libicucore.A.dylib
-  - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D386B923-773E-352C-99DC-6C47C650DF0B
-  Functions: 527
-  Symbols:   1463
-  CStrings:  936
+  UUID: 089B4064-ADBC-3145-846E-D1423B52FC18
+  Functions: 607
+  Symbols:   1760
+  CStrings:  1175
 
Symbols:
+ +[NEBitVector getBitAtIndexWithBitmap:bitCount:index:]
+ +[NEBitVector getByteCount:]
+ +[NEBitVector setBitAtIndexWithBitmap:bitCount:index:toValue:]
+ +[NEBloomFilter containsWithBitmap:numberOfBits:numberOfHashes:murmurSeed:value:]
+ +[NEBloomFilter getFalsePositiveProbability:numberOfBits:numberOfHashes:]
+ +[NEBloomFilter getNumberOfBits:falsePositiveTolerance:]
+ +[NEBloomFilter getNumberOfHashes:numberOfBits:]
+ +[NEBloomFilter insertWithBitmap:numberOfBits:numberOfHashes:murmurSeed:value:]
+ +[NEBloomFilter mmapCleanup:]
+ +[NEBloomFilter mmapFromFile:bloomFilter:]
+ +[NEBloomFilter mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:]
+ +[NEFNVHash hash:]
+ +[NEFNVHash hashWithString:]
+ +[NEMurmurHash3 digest32BitX86:length:seed:]
+ +[NEMurmurHash3 hash:seed:]
+ +[NEMurmurHash3 hashWithString:seed:]
+ +[NEURLParser matchingStringsForURL:]
+ -[NEBitVector clearAllBits]
+ -[NEBitVector getBitAtIndex:]
+ -[NEBitVector initWithBitMap:bitmapSize:bitCount:]
+ -[NEBitVector printBits]
+ -[NEBitVector setBitAtIndex:toValue:]
+ -[NEBloomFilter .cxx_destruct]
+ -[NEBloomFilter bitVectorBuffer]
+ -[NEBloomFilter contains:]
+ -[NEBloomFilter falsePositiveTolerance]
+ -[NEBloomFilter initFromFile:]
+ -[NEBloomFilter initWithData:numberOfBits:numberOfHashes:murmurSeed:mmapFilename:]
+ -[NEBloomFilter initWithNumberOfItems:falsePositiveTolerance:]
+ -[NEBloomFilter insert:]
+ -[NEBloomFilter murmurSeed]
+ -[NEBloomFilter numberOfBits]
+ -[NEBloomFilter numberOfHashes]
+ -[NEBloomFilter numberOfItems]
+ -[NEBloomFilter setBitVectorBuffer:]
+ -[NEBloomFilter setFalsePositiveTolerance:]
+ -[NEBloomFilter setMurmurSeed:]
+ -[NEBloomFilter setNumberOfBits:]
+ -[NEBloomFilter setNumberOfHashes:]
+ -[NEBloomFilter setNumberOfItems:]
+ _CFAllocatorAllocateTyped
+ _OBJC_CLASS_$_NEBitVector
+ _OBJC_CLASS_$_NEBloomFilter
+ _OBJC_CLASS_$_NEFNVHash
+ _OBJC_CLASS_$_NEMurmurHash3
+ _OBJC_CLASS_$_NEURLParser
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSURL
+ _OBJC_IVAR_$_NEBitVector._bitCount
+ _OBJC_IVAR_$_NEBitVector._bitmap
+ _OBJC_IVAR_$_NEBitVector._bitmapSize
+ _OBJC_IVAR_$_NEBloomFilter._bitVector
+ _OBJC_IVAR_$_NEBloomFilter._bitVectorBuffer
+ _OBJC_IVAR_$_NEBloomFilter._falsePositiveTolerance
+ _OBJC_IVAR_$_NEBloomFilter._murmurSeed
+ _OBJC_IVAR_$_NEBloomFilter._numberOfBits
+ _OBJC_IVAR_$_NEBloomFilter._numberOfHashes
+ _OBJC_IVAR_$_NEBloomFilter._numberOfItems
+ _OBJC_METACLASS_$_NEBitVector
+ _OBJC_METACLASS_$_NEBloomFilter
+ _OBJC_METACLASS_$_NEFNVHash
+ _OBJC_METACLASS_$_NEMurmurHash3
+ _OBJC_METACLASS_$_NEURLParser
+ __OBJC_$_CLASS_METHODS_NEBitVector
+ __OBJC_$_CLASS_METHODS_NEBloomFilter
+ __OBJC_$_CLASS_METHODS_NEFNVHash
+ __OBJC_$_CLASS_METHODS_NEMurmurHash3
+ __OBJC_$_CLASS_METHODS_NEURLParser
+ __OBJC_$_INSTANCE_METHODS_NEBitVector
+ __OBJC_$_INSTANCE_METHODS_NEBloomFilter
+ __OBJC_$_INSTANCE_VARIABLES_NEBitVector
+ __OBJC_$_INSTANCE_VARIABLES_NEBloomFilter
+ __OBJC_$_PROP_LIST_NEBloomFilter
+ __OBJC_CLASS_RO_$_NEBitVector
+ __OBJC_CLASS_RO_$_NEBloomFilter
+ __OBJC_CLASS_RO_$_NEFNVHash
+ __OBJC_CLASS_RO_$_NEMurmurHash3
+ __OBJC_CLASS_RO_$_NEURLParser
+ __OBJC_METACLASS_RO_$_NEBitVector
+ __OBJC_METACLASS_RO_$_NEBloomFilter
+ __OBJC_METACLASS_RO_$_NEFNVHash
+ __OBJC_METACLASS_RO_$_NEMurmurHash3
+ __OBJC_METACLASS_RO_$_NEURLParser
+ ___Block_byref_object_copy_.504
+ ___Block_byref_object_dispose_.505
+ ___block_descriptor_tmp.102.233
+ ___block_descriptor_tmp.103
+ ___block_descriptor_tmp.104
+ ___block_descriptor_tmp.12.436
+ ___block_descriptor_tmp.13.437
+ ___block_descriptor_tmp.13.633
+ ___block_descriptor_tmp.144
+ ___block_descriptor_tmp.159.298
+ ___block_descriptor_tmp.166
+ ___block_descriptor_tmp.167
+ ___block_descriptor_tmp.169
+ ___block_descriptor_tmp.172.305
+ ___block_descriptor_tmp.173.306
+ ___block_descriptor_tmp.174
+ ___block_descriptor_tmp.179
+ ___block_descriptor_tmp.18.493
+ ___block_descriptor_tmp.18.521
+ ___block_descriptor_tmp.184
+ ___block_descriptor_tmp.186
+ ___block_descriptor_tmp.19.522
+ ___block_descriptor_tmp.194.123
+ ___block_descriptor_tmp.198.174
+ ___block_descriptor_tmp.20.399
+ ___block_descriptor_tmp.20.523
+ ___block_descriptor_tmp.201.172
+ ___block_descriptor_tmp.202
+ ___block_descriptor_tmp.204
+ ___block_descriptor_tmp.205.183
+ ___block_descriptor_tmp.206
+ ___block_descriptor_tmp.21
+ ___block_descriptor_tmp.226
+ ___block_descriptor_tmp.229
+ ___block_descriptor_tmp.233
+ ___block_descriptor_tmp.237
+ ___block_descriptor_tmp.24
+ ___block_descriptor_tmp.241
+ ___block_descriptor_tmp.242
+ ___block_descriptor_tmp.250
+ ___block_descriptor_tmp.255
+ ___block_descriptor_tmp.27
+ ___block_descriptor_tmp.29.490
+ ___block_descriptor_tmp.3.442
+ ___block_descriptor_tmp.30.405
+ ___block_descriptor_tmp.32.570
+ ___block_descriptor_tmp.325
+ ___block_descriptor_tmp.34.569
+ ___block_descriptor_tmp.35.506
+ ___block_descriptor_tmp.35.552
+ ___block_descriptor_tmp.36
+ ___block_descriptor_tmp.390
+ ___block_descriptor_tmp.4.444
+ ___block_descriptor_tmp.41.451
+ ___block_descriptor_tmp.41.531
+ ___block_descriptor_tmp.440
+ ___block_descriptor_tmp.45.623
+ ___block_descriptor_tmp.46.624
+ ___block_descriptor_tmp.47.464
+ ___block_descriptor_tmp.47.610
+ ___block_descriptor_tmp.48.456
+ ___block_descriptor_tmp.48.577
+ ___block_descriptor_tmp.516
+ ___block_descriptor_tmp.54.513
+ ___block_descriptor_tmp.57.507
+ ___block_descriptor_tmp.59.508
+ ___block_literal_global.141
+ ___block_literal_global.16
+ ___block_literal_global.161
+ ___block_literal_global.176
+ ___block_literal_global.181
+ ___block_literal_global.225
+ ___block_literal_global.228
+ ___block_literal_global.239
+ ___block_literal_global.30
+ ___block_literal_global.323
+ ___block_literal_global.392
+ ___block_literal_global.443
+ ___block_literal_global.514
+ ___block_literal_global.56
+ ___get_flow_divert_token_from_session_manager_block_invoke.248
+ ___ne_session_fetch_server_parameters_block_invoke
+ ___ne_session_get_info_with_parameters_block_invoke.197
+ ___ne_session_get_info_with_parameters_block_invoke_2.200
+ ___ne_session_get_type_block_invoke
+ ___ne_session_reset_cache_block_invoke
+ ___ne_url_filter_check_block_invoke
+ ___ne_url_filter_check_block_invoke.33
+ ___ne_url_filter_check_block_invoke_2
+ ___ne_url_filter_connection_queue_block_invoke
+ ___ne_url_filter_globals_block_invoke
+ ___ne_url_filter_handle_request_block_invoke
+ ___ne_url_filter_handle_request_block_invoke.17
+ ___ne_url_filter_handle_request_block_invoke.20
+ ___ne_url_filter_handle_request_block_invoke.23
+ ___ne_url_filter_handle_request_block_invoke.26
+ ___ne_url_filter_request_connection_block_invoke
+ ___ne_url_filter_request_connection_block_invoke_2
+ ___ne_url_filter_request_connection_block_invoke_3
+ ___ne_url_filter_request_connections_block_invoke
+ ___ne_url_filter_request_connections_block_invoke_2
+ ___ne_url_filter_request_xpc_connection_block_invoke
+ ___ne_url_filter_request_xpc_connection_block_invoke.44
+ ___ne_url_filter_request_xpc_connection_block_invoke.46
+ ___notify_client_block_invoke.192
+ __xpc_error_connection_invalid
+ _arc4random
+ _closedir
+ _ftruncate
+ _g_bloom_filter_ready
+ _g_bloom_filters
+ _g_waitingForXPCConnections
+ _log
+ _mmap
+ _msync
+ _munmap
+ _ne_bit_vector_get
+ _ne_bloom_filter_cleanup
+ _ne_bloom_filter_contains
+ _ne_bloom_filter_from_mmap
+ _ne_fnvhash
+ _ne_murmurHash3
+ _ne_parse_url_and_check
+ _ne_session_fetch_server_parameters
+ _ne_session_get_type
+ _ne_session_reset_cache
+ _ne_session_trim_domain.domain_buffer.230
+ _ne_session_urlfilter_configs_present
+ _ne_url_filter_check
+ _ne_url_filter_connection_queue.onceToken
+ _ne_url_filter_connection_queue.url_filter_queue
+ _ne_url_filter_copy_connection
+ _ne_url_filter_globals.globals
+ _ne_url_filter_globals.onceToken
+ _ne_url_filter_handle_request
+ _ne_url_filter_request_connection
+ _ne_url_filter_send_message
+ _ne_url_prefilter_check_info_changed
+ _ne_url_prefilter_check_info_changed.current_info_token
+ _ne_url_prefilter_check_info_changed.current_timestamp
+ _ne_url_prefilter_contains
+ _ne_url_prefilter_lock
+ _objc_alloc
+ _objc_autoreleaseReturnValue
+ _objc_enumerationMutation
+ _objc_msgSend$UTF8String
+ _objc_msgSend$addObject:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$allObjects
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$bytes
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$containsWithBitmap:numberOfBits:numberOfHashes:murmurSeed:value:
+ _objc_msgSend$copy
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$fragment
+ _objc_msgSend$getBitAtIndexWithBitmap:bitCount:index:
+ _objc_msgSend$getByteCount:
+ _objc_msgSend$getNumberOfBits:falsePositiveTolerance:
+ _objc_msgSend$getNumberOfHashes:numberOfBits:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$hashWithString:
+ _objc_msgSend$hashWithString:seed:
+ _objc_msgSend$host
+ _objc_msgSend$initWithBitMap:bitmapSize:bitCount:
+ _objc_msgSend$initWithBytes:length:
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$initWithString:
+ _objc_msgSend$initWithUTF8String:
+ _objc_msgSend$insertWithBitmap:numberOfBits:numberOfHashes:murmurSeed:value:
+ _objc_msgSend$length
+ _objc_msgSend$lengthOfBytesUsingEncoding:
+ _objc_msgSend$matchingStringsForURL:
+ _objc_msgSend$mmapFromFile:bloomFilter:
+ _objc_msgSend$mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:
+ _objc_msgSend$pathComponents
+ _objc_msgSend$query
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$setBitAtIndexWithBitmap:bitCount:index:toValue:
+ _objc_msgSend$setWithCapacity:
+ _objc_msgSend$string
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSendSuper2
+ _objc_opt_self
+ _objc_release
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x9
+ _objc_retain
+ _objc_retainAutorelease
+ _objc_retain_x19
+ _objc_retain_x25
+ _objc_retain_x8
+ _objc_storeStrong
+ _opendir
+ _pow
+ _readdir
- _CFAllocatorAllocate
- ___block_descriptor_tmp.100
- ___block_descriptor_tmp.12.432
- ___block_descriptor_tmp.13.433
- ___block_descriptor_tmp.13.545
- ___block_descriptor_tmp.143
- ___block_descriptor_tmp.155
- ___block_descriptor_tmp.162
- ___block_descriptor_tmp.163.305
- ___block_descriptor_tmp.165
- ___block_descriptor_tmp.168.111
- ___block_descriptor_tmp.173.127
- ___block_descriptor_tmp.177.118
- ___block_descriptor_tmp.178
- ___block_descriptor_tmp.18.443
- ___block_descriptor_tmp.180
- ___block_descriptor_tmp.181
- ___block_descriptor_tmp.188.117
- ___block_descriptor_tmp.19.444
- ___block_descriptor_tmp.192
- ___block_descriptor_tmp.196.171
- ___block_descriptor_tmp.198.175
- ___block_descriptor_tmp.20.395
- ___block_descriptor_tmp.20.445
- ___block_descriptor_tmp.200.187
- ___block_descriptor_tmp.217
- ___block_descriptor_tmp.220
- ___block_descriptor_tmp.227
- ___block_descriptor_tmp.231
- ___block_descriptor_tmp.235
- ___block_descriptor_tmp.236
- ___block_descriptor_tmp.238
- ___block_descriptor_tmp.249
- ___block_descriptor_tmp.30.401
- ___block_descriptor_tmp.324
- ___block_descriptor_tmp.35.477
- ___block_descriptor_tmp.37.478
- ___block_descriptor_tmp.386
- ___block_descriptor_tmp.41.453
- ___block_descriptor_tmp.438
- ___block_descriptor_tmp.46.534
- ___block_descriptor_tmp.47.524
- ___block_descriptor_tmp.48.501
- ___block_descriptor_tmp.99
- ___block_literal_global.140
- ___block_literal_global.157
- ___block_literal_global.170
- ___block_literal_global.175.109
- ___block_literal_global.219
- ___block_literal_global.22
- ___block_literal_global.222
- ___block_literal_global.233
- ___block_literal_global.322
- ___block_literal_global.388
- ___block_literal_global.436
- ___block_literal_global.7
- ___get_flow_divert_token_from_session_manager_block_invoke.242
- ___ne_session_get_info_with_parameters_block_invoke.191
- ___ne_session_get_info_with_parameters_block_invoke_2.194
- ___notify_client_block_invoke.186
- _ne_session_trim_domain.domain_buffer.232
- _set_status
CStrings:
+ "#%@"
+ "%@ - initFromFile: Invalid params"
+ "%@ - initFromFile: failed to get bloom filter data from mmap file %@"
+ "%@ - initFromFile: retrieved bloom filter data from mmap file %@"
+ "%@ - initWithBitMap: Invalid params"
+ "%@ - initWithData: Invalid params"
+ "%@ - initWithData: failed to save bloom filter data to mmap file"
+ "%@ - initWithData: saved bloom filter data to mmap file"
+ "%@ - initWithNumberOfItems: Invalid params"
+ "%@%@"
+ "%@/%@"
+ "%s: Checking file %@"
+ "%s: Cleaning up bloom filter for %s"
+ "%s: FINAL RESULT for <%s> - PREFILTER ALLOWED"
+ "%s: Failed to init bloom filter from directory %s"
+ "%s: Failed to read mmap directory"
+ "%s: Failed to read mmap files from directory <%s>"
+ "%s: Got an error in reply <%lld>"
+ "%s: Got an error on the URL Filter XPC connection"
+ "%s: Got an error on the XPC connection when sending a url filter request: %s"
+ "%s: Got an invalid url filter reply"
+ "%s: NEBloomFilter - <pid %d> Failed to get file stats for file %s: [%d] %s"
+ "%s: NEBloomFilter - <pid %d> Failed to open file %s: [%d] %s"
+ "%s: NEBloomFilter - <pid %d> No read permission to file %s"
+ "%s: NEBloomFilter - <pid %d> format version (%llu) does not equal the current version (%u)"
+ "%s: NEBloomFilter - <pid %d> invalid file size %lld for file %s"
+ "%s: NEBloomFilter - <pid %d> invalid mmap file size <%d> <bitmapSize %d data_memory_offset %d>"
+ "%s: NEBloomFilter - <pid %d> magic number (%llx) does not equal the expected value (%llx)"
+ "%s: NEBloomFilter - <pid %d> mmap failed for file %s: [%d] %s"
+ "%s: NEBloomFilter - <pid %d> mmap failed to malloc for filename %s: [%d] %s"
+ "%s: NEBloomFilter - <pid %d> no update needed for %s"
+ "%s: NEBloomFilter - <pid %d> read from mmap <numberOfBits %d numberOfHashes %d murmurSeed %d bitmapSize %d>"
+ "%s: NEBloomFilter - <pid %d> read mmap <fd %d, size %lld> for file %s"
+ "%s: NEBloomFilter - <pid %d> update done for %s"
+ "%s: NEBloomFilter - Failed mmap file <%s> <fd %d, size %d>"
+ "%s: NEBloomFilter - Failed msync: [%d] %s"
+ "%s: NEBloomFilter - done msync"
+ "%s: NEBloomFilter - failed to ftruncate mmap file <%s> to %d bytes <errno %d - %s>"
+ "%s: NEBloomFilter - failed to open mmap file %s <errno %d - %s>"
+ "%s: Prefilter info timestamp changed from %llu to %llu"
+ "%s: Session manager not running, cannot filter"
+ "%s: URL Filter failed to create connection: %s"
+ "%s: URL Filter failed to get endpoint: %s"
+ "%s: URL Filter falling back to Mach service %s"
+ "%s: URL Filter got an error on the XPC connection when requesting endpoint: %s"
+ "%s: URL Filter requesting xpc connection"
+ "%s: URLCHECK: CHECKING URL - %{sensitive, mask.hash, networkextension:string}.*P (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: CHECKING URL - <%d : %{private}s> (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: FILTER ALLOWED - %{sensitive, mask.hash, networkextension:string}.*P (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: FILTER ALLOWED - <%d : %{private}s> (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: FILTER DENIED - %{sensitive, mask.hash, networkextension:string}.*P (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: FINAL RESULT: FILTER DENIED - <%d : %{private}s> (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: Failed url request - %{sensitive, mask.hash, networkextension:string}.*P (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: Failed url request - <%d : %{private}s> (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: SENDING URL CHECK REQ - %{sensitive, mask.hash, networkextension:string}.*P (app bundleid <%s> pid <%d>)"
+ "%s: URLCHECK: SENDING URL CHECK REQ - <%d : %{private}s> (app bundleid <%s> pid <%d>)"
+ "%s: Updated file %@ into bloomFilter[%d]"
+ "%s: Updating file %@ into bloomFilter[%d]"
+ "%s: all url filter provider connection requests complete with success: %d"
+ "%s: checking prefilter for url <%s>"
+ "%s: received url filter xpc reply"
+ "*"
+ "*48@0:8r*16*24I32I36I40I44"
+ "+[NEBloomFilter mmapCleanup:]"
+ "+[NEBloomFilter mmapFromFile:bloomFilter:]"
+ "+[NEBloomFilter mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:]"
+ "."
+ ".cxx_destruct"
+ "/"
+ "/private/var/db/urlPrefilter"
+ "2"
+ "://"
+ "<nil url>"
+ "<nil>"
+ "?%@"
+ "@\"NEBitVector\""
+ "@\"NSData\""
+ "@16@0:8"
+ "@24@0:8@16"
+ "@24@0:8r*16"
+ "@28@0:8I16d20"
+ "@32@0:8*16I24I28"
+ "@44@0:8@16I24I28I32@36"
+ "B24@0:8@16"
+ "B24@0:8q16"
+ "B32@0:8r*16^{ne_bloom_filter={ne_bloom_filter_header=QQIIII}^v*^vId}24"
+ "B36@0:8*16I24q28"
+ "B44@0:8*16I24I28I32r*36"
+ "Flow gone away"
+ "I"
+ "I16@0:8"
+ "I20@0:8I16"
+ "I24@0:8@16"
+ "I24@0:8r*16"
+ "I28@0:8@16I24"
+ "I28@0:8r*16I24"
+ "NEBitVector"
+ "NEBloomFilter"
+ "NEFNVHash"
+ "NEMurmurHash3"
+ "NEURLParser"
+ "PID"
+ "T@\"NSData\",&,N,V_bitVectorBuffer"
+ "TI,N,V_murmurSeed"
+ "TI,N,V_numberOfBits"
+ "TI,N,V_numberOfHashes"
+ "TI,N,V_numberOfItems"
+ "Td,N,V_falsePositiveTolerance"
+ "URL"
+ "URL Filter establish connections queue"
+ "URL Filter provider connection waiter queue"
+ "URLPrefiltered"
+ "UTF8String"
+ "_bitCount"
+ "_bitVector"
+ "_bitVectorBuffer"
+ "_bitmap"
+ "_bitmapSize"
+ "_falsePositiveTolerance"
+ "_murmurSeed"
+ "_numberOfBits"
+ "_numberOfHashes"
+ "_numberOfItems"
+ "addObject:"
+ "addObjectsFromArray:"
+ "allObjects"
+ "appendFormat:"
+ "appendString:"
+ "bitVectorBuffer"
+ "bundleIdentifier"
+ "bytes"
+ "clearAllBits"
+ "com.apple.nesessionmanager.prefilter-ready"
+ "com.apple.networkextension.url-prefilter-data."
+ "com.apple.networkextension.url-prefilter-data.temp."
+ "componentsJoinedByString:"
+ "componentsSeparatedByString:"
+ "contains:"
+ "containsWithBitmap:numberOfBits:numberOfHashes:murmurSeed:value:"
+ "copy"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "d"
+ "d16@0:8"
+ "d28@0:8I16I20I24"
+ "dataWithLength:"
+ "falsePositiveTolerance"
+ "fragment"
+ "getBitAtIndex:"
+ "getBitAtIndexWithBitmap:bitCount:index:"
+ "getByteCount:"
+ "getFalsePositiveProbability:numberOfBits:numberOfHashes:"
+ "getNumberOfBits:falsePositiveTolerance:"
+ "getNumberOfHashes:numberOfBits:"
+ "hasPrefix:"
+ "hasSuffix:"
+ "hash:"
+ "hash:seed:"
+ "hashWithString:"
+ "hashWithString:seed:"
+ "host"
+ "hotspot-authentication"
+ "hotspot-evaluation"
+ "hotspot-provider"
+ "i24@0:8I16i20"
+ "i28@0:8I16d20"
+ "init"
+ "initFromFile:"
+ "initWithBitMap:bitmapSize:bitCount:"
+ "initWithBytes:length:"
+ "initWithData:numberOfBits:numberOfHashes:murmurSeed:mmapFilename:"
+ "initWithFormat:"
+ "initWithNumberOfItems:falsePositiveTolerance:"
+ "initWithString:"
+ "initWithUTF8String:"
+ "insert:"
+ "insertWithBitmap:numberOfBits:numberOfHashes:murmurSeed:value:"
+ "length"
+ "lengthOfBytesUsingEncoding:"
+ "matchingStringsForURL:"
+ "mmapFromFile:bloomFilter:"
+ "mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:"
+ "murmurSeed"
+ "ne.urlfilter"
+ "ne_bloom_filter_from_mmap"
+ "ne_url_filter_check"
+ "ne_url_filter_check_block_invoke"
+ "ne_url_filter_handle_request"
+ "ne_url_filter_handle_request_block_invoke"
+ "ne_url_filter_handle_request_block_invoke_2"
+ "ne_url_filter_request_connections_block_invoke_2"
+ "ne_url_filter_request_xpc_connection"
+ "ne_url_filter_request_xpc_connection_block_invoke"
+ "ne_url_prefilter_check_info_changed"
+ "ne_url_prefilter_contains"
+ "numberOfBits"
+ "numberOfHashes"
+ "numberOfItems"
+ "pathComponents"
+ "printBits"
+ "query"
+ "rangeOfString:"
+ "redactSensitiveLogs"
+ "setBitAtIndex:toValue:"
+ "setBitAtIndexWithBitmap:bitCount:index:toValue:"
+ "setBitVectorBuffer:"
+ "setFalsePositiveTolerance:"
+ "setMurmurSeed:"
+ "setNumberOfBits:"
+ "setNumberOfHashes:"
+ "setNumberOfItems:"
+ "setWithCapacity:"
+ "string"
+ "stringByAppendingPathComponent:"
+ "stringByAppendingString:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "stringWithFormat:"
+ "stringWithUTF8String:"
+ "subarrayWithRange:"
+ "substringFromIndex:"
+ "url-filter-provider"
+ "urlfilter"
+ "v16@0:8"
+ "v20@0:8I16"
+ "v24@0:8@16"
+ "v24@0:8d16"
+ "v28@0:8q16B24"
+ "v40@0:8*16I24q28B36"
+ "v44@0:8*16I24I28I32r*36"
+ "verdict"
+ "www."
- "filter is null"

```
