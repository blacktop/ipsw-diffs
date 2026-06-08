## libnetworkextension.dylib

> `/usr/lib/libnetworkextension.dylib`

```diff

-2226.120.19.0.0
-  __TEXT.__text: 0x3386c
-  __TEXT.__auth_stubs: 0x1bf0
-  __TEXT.__objc_methlist: 0x24c
+2303.0.0.0.2
+  __TEXT.__text: 0x34a8c
+  __TEXT.__objc_methlist: 0x2ac
   __TEXT.__const: 0x25c
-  __TEXT.__cstring: 0x2a4a
+  __TEXT.__cstring: 0x2ed4
   __TEXT.__oslogstring: 0x803e
-  __TEXT.__unwind_info: 0x750
-  __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methname: 0x8d6
-  __TEXT.__objc_methtype: 0x20e
-  __TEXT.__objc_stubs: 0x780
-  __DATA_CONST.__got: 0x180
+  __TEXT.__unwind_info: 0x778
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1c08
-  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c8
+  __DATA_CONST.__objc_selrefs: 0x3a0
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xe00
-  __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x6e0
-  __AUTH_CONST.__objc_const: 0x548
-  __AUTH.__objc_data: 0x1e0
+  __DATA_CONST.__got: 0x1c0
+  __AUTH_CONST.__const: 0x3c0
+  __AUTH_CONST.__cfstring: 0xb20
+  __AUTH_CONST.__objc_const: 0x5d8
+  __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH_CONST.__auth_got: 0xe48
+  __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x2c
-  __DATA.__data: 0x58
-  __DATA.__bss: 0xb90
+  __DATA.__data: 0x60
+  __DATA.__bss: 0xce0
   __DATA.__common: 0x3d
-  __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x2b8
+  __DATA_DIRTY.__data: 0x8
+  __DATA_DIRTY.__bss: 0x1b8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 404D50D4-8E75-3C3B-8B02-B258CD5430B8
-  Functions: 614
-  Symbols:   1825
-  CStrings:  1192
+  UUID: CC4B62ED-5B63-3370-9BA4-DE6DA13E6BE0
+  Functions: 629
+  Symbols:   1919
+  CStrings:  1112
 
Symbols:
+ +[NERegexURLParser addQueryAndFragmentFromComponents:queryParameters:toDomain:options:matchingStrings:componentPlaceHolder:]
+ +[NERegexURLParser appendURLComponent:withPrefix:toDomain:options:excludeOption:addIntermediateResult:matchingStrings:componentPlaceHolder:]
+ +[NERegexURLParser extractNamedGroup:fromMatch:inString:]
+ +[NERegexURLParser matchingStringsForDomain:options:port:]
+ +[NERegexURLParser matchingStringsForURL:]
+ +[NERegexURLParser matchingStringsForURLString:]
+ +[NERegexURLParser matchingStringsForURLString:options:domainLevels:pathSegments:queryParameters:componentPlaceHolder:parsePattern:parseGroupNames:parseDelimitor:]
+ +[NERegexURLParser parseQueryParameters:]
+ +[NERegexURLParser parseURLComponents:]
+ +[NERegexURLParser parseURLWithPattern:groupNames:url:delimiter:]
+ _NSLog
+ _OBJC_CLASS_$_NERegexURLParser
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$_NSSet
+ _OBJC_METACLASS_$_NERegexURLParser
+ __OBJC_$_CLASS_METHODS_NERegexURLParser
+ __OBJC_CLASS_RO_$_NERegexURLParser
+ __OBJC_METACLASS_RO_$_NERegexURLParser
+ ___32+[NERegexURLParser isIPAddress:]_block_invoke
+ ___32+[NERegexURLParser isIPAddress:]_block_invoke_2
+ ___32+[NERegexURLParser isIPAddress:]_block_invoke_3
+ ___40+[NERegexURLParser urlRegularExpression]_block_invoke
+ ___51+[NERegexURLParser pathComponentsRegularExpression]_block_invoke
+ ___Block_byref_object_copy_.584
+ ___Block_byref_object_dispose_.585
+ ___NSArray0__struct
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_tmp.102.302
+ ___block_descriptor_tmp.12.514
+ ___block_descriptor_tmp.13.515
+ ___block_descriptor_tmp.14.501
+ ___block_descriptor_tmp.14.719
+ ___block_descriptor_tmp.158.375
+ ___block_descriptor_tmp.165
+ ___block_descriptor_tmp.168
+ ___block_descriptor_tmp.17.721
+ ___block_descriptor_tmp.171
+ ___block_descriptor_tmp.172.384
+ ___block_descriptor_tmp.173.165
+ ___block_descriptor_tmp.178.179
+ ___block_descriptor_tmp.182.171
+ ___block_descriptor_tmp.185
+ ___block_descriptor_tmp.186.168
+ ___block_descriptor_tmp.188
+ ___block_descriptor_tmp.19.573
+ ___block_descriptor_tmp.19.611
+ ___block_descriptor_tmp.192
+ ___block_descriptor_tmp.197
+ ___block_descriptor_tmp.198.223
+ ___block_descriptor_tmp.20.612
+ ___block_descriptor_tmp.200.224
+ ___block_descriptor_tmp.203
+ ___block_descriptor_tmp.204.237
+ ___block_descriptor_tmp.205.240
+ ___block_descriptor_tmp.21.613
+ ___block_descriptor_tmp.223
+ ___block_descriptor_tmp.226
+ ___block_descriptor_tmp.229
+ ___block_descriptor_tmp.233
+ ___block_descriptor_tmp.237
+ ___block_descriptor_tmp.241
+ ___block_descriptor_tmp.244
+ ___block_descriptor_tmp.250
+ ___block_descriptor_tmp.255
+ ___block_descriptor_tmp.29.490
+ ___block_descriptor_tmp.3.520
+ ___block_descriptor_tmp.30.570
+ ___block_descriptor_tmp.33.655
+ ___block_descriptor_tmp.35.654
+ ___block_descriptor_tmp.36.586
+ ___block_descriptor_tmp.36.637
+ ___block_descriptor_tmp.4.522
+ ___block_descriptor_tmp.403
+ ___block_descriptor_tmp.42.529
+ ___block_descriptor_tmp.42.621
+ ___block_descriptor_tmp.468
+ ___block_descriptor_tmp.47.710
+ ___block_descriptor_tmp.48.542
+ ___block_descriptor_tmp.48.691
+ ___block_descriptor_tmp.49.534
+ ___block_descriptor_tmp.49.662
+ ___block_descriptor_tmp.518
+ ___block_descriptor_tmp.55.596
+ ___block_descriptor_tmp.58.587
+ ___block_descriptor_tmp.599
+ ___block_descriptor_tmp.60.589
+ ___block_descriptor_tmp.88
+ ___block_literal_global.160
+ ___block_literal_global.175
+ ___block_literal_global.180
+ ___block_literal_global.192
+ ___block_literal_global.225
+ ___block_literal_global.228
+ ___block_literal_global.23
+ ___block_literal_global.239
+ ___block_literal_global.38.207
+ ___block_literal_global.401
+ ___block_literal_global.470
+ ___block_literal_global.521
+ ___block_literal_global.55
+ ___block_literal_global.597
+ ___block_literal_global.6
+ ___block_literal_global.60
+ ___block_literal_global.65
+ ___block_literal_global.73
+ ___get_flow_divert_token_from_session_manager_block_invoke.248
+ ___ne_session_get_info_with_parameters_block_invoke.196
+ ___ne_session_get_info_with_parameters_block_invoke_2.199
+ ___notify_client_block_invoke.191
+ _isIPAddress:.bracketedIPv6Regex
+ _isIPAddress:.bracketedIPv6Token
+ _isIPAddress:.ipv4Regex
+ _isIPAddress:.ipv4Token
+ _isIPAddress:.unbracketedIPv6Regex
+ _isIPAddress:.unbracketedIPv6Token
+ _ne_session_trim_domain.domain_buffer.297
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$array
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$dictionary
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$firstObject
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithDictionary:copyItems:
+ _objc_msgSend$initWithObjects:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$matchesInString:options:range:
+ _objc_msgSend$matchingStringsForDomain:options:port:
+ _objc_msgSend$matchingStringsForURLString:
+ _objc_msgSend$matchingStringsForURLString:options:domainLevels:pathSegments:queryParameters:componentPlaceHolder:parsePattern:parseGroupNames:parseDelimitor:
+ _objc_msgSend$parseQueryParameters:
+ _objc_msgSend$parseURLComponents:
+ _objc_msgSend$parseURLWithPattern:groupNames:url:delimiter:
+ _objc_msgSend$rangeAtIndex:
+ _objc_msgSend$rangeWithName:
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$set
+ _objc_msgSend$stringByRemovingPercentEncoding
+ _objc_msgSend$stringValue
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$unionSet:
+ _objc_release_x1
+ _objc_release_x9
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _pathComponentsRegularExpression.onceToken
+ _pathComponentsRegularExpression.pathRegex
+ _urlRegularExpression.onceToken
+ _urlRegularExpression.urlRegex
- ___Block_byref_object_copy_.514
- ___Block_byref_object_dispose_.515
- ___block_descriptor_tmp
- ___block_descriptor_tmp.102.238
- ___block_descriptor_tmp.12.444
- ___block_descriptor_tmp.13.445
- ___block_descriptor_tmp.14.431
- ___block_descriptor_tmp.14.649
- ___block_descriptor_tmp.148
- ___block_descriptor_tmp.159.304
- ___block_descriptor_tmp.167
- ___block_descriptor_tmp.169.312
- ___block_descriptor_tmp.17.651
- ___block_descriptor_tmp.172.313
- ___block_descriptor_tmp.173.314
- ___block_descriptor_tmp.174.120
- ___block_descriptor_tmp.179
- ___block_descriptor_tmp.184
- ___block_descriptor_tmp.186.125
- ___block_descriptor_tmp.187
- ___block_descriptor_tmp.189
- ___block_descriptor_tmp.19.503
- ___block_descriptor_tmp.19.541
- ___block_descriptor_tmp.198.176
- ___block_descriptor_tmp.199
- ___block_descriptor_tmp.20.542
- ___block_descriptor_tmp.202
- ___block_descriptor_tmp.204.179
- ___block_descriptor_tmp.205.186
- ___block_descriptor_tmp.206
- ___block_descriptor_tmp.21.543
- ___block_descriptor_tmp.224
- ___block_descriptor_tmp.227
- ___block_descriptor_tmp.230
- ___block_descriptor_tmp.234
- ___block_descriptor_tmp.238
- ___block_descriptor_tmp.243
- ___block_descriptor_tmp.245
- ___block_descriptor_tmp.251
- ___block_descriptor_tmp.256
- ___block_descriptor_tmp.29.420
- ___block_descriptor_tmp.3.450
- ___block_descriptor_tmp.30.500
- ___block_descriptor_tmp.33.585
- ___block_descriptor_tmp.333
- ___block_descriptor_tmp.35.584
- ___block_descriptor_tmp.36.516
- ___block_descriptor_tmp.36.567
- ___block_descriptor_tmp.398
- ___block_descriptor_tmp.4.452
- ___block_descriptor_tmp.42.459
- ___block_descriptor_tmp.42.551
- ___block_descriptor_tmp.448
- ___block_descriptor_tmp.45
- ___block_descriptor_tmp.47.640
- ___block_descriptor_tmp.48.472
- ___block_descriptor_tmp.48.621
- ___block_descriptor_tmp.49.464
- ___block_descriptor_tmp.49.592
- ___block_descriptor_tmp.529
- ___block_descriptor_tmp.55.526
- ___block_descriptor_tmp.58.517
- ___block_descriptor_tmp.60.519
- ___block_literal_global.145
- ___block_literal_global.16
- ___block_literal_global.161
- ___block_literal_global.176.118
- ___block_literal_global.181
- ___block_literal_global.226
- ___block_literal_global.229
- ___block_literal_global.240
- ___block_literal_global.30
- ___block_literal_global.331
- ___block_literal_global.400
- ___block_literal_global.451
- ___block_literal_global.527
- ___get_flow_divert_token_from_session_manager_block_invoke.249
- ___ne_session_get_info_with_parameters_block_invoke.197
- ___ne_session_get_info_with_parameters_block_invoke_2.200
- ___notify_client_block_invoke.192
- _ne_session_trim_domain.domain_buffer.235
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "#"
+ "%*"
+ "%@%@%@"
+ "%@%@%@=%@"
+ "%@/"
+ "%@:%@"
+ "%@://"
+ "&"
+ "/([^/]+)"
+ ":"
+ "="
+ "?"
+ "Failed to compile URL regex: %@"
+ "Failed to compile path components regex: %@"
+ "["
+ "]"
+ "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
+ "^(?:(?<scheme>[a-zA-Z][a-zA-Z0-9+.-]*):)?(?://)?(?:(?<userinfo>[^@/\\?#]*+)@)?(?<host>\\[[0-9a-fA-F:]+\\]|[^:/\\?#]*+)(?::(?<port>\\d+))?(?<path>/[^\\?#]*+)?(?:\\?(?<query>[^#]*+))?(?:#(?<fragment>.*))?$"
+ "^(?:[0-9a-fA-F]{1,4}:){1,7}[0-9a-fA-F]{1,4}$|^(?:[0-9a-fA-F]{1,4}:){1,7}:$|^:(?::[0-9a-fA-F]{1,4}){1,7}$|^::$|^::1$"
+ "^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$|^(?:[0-9a-fA-F]{1,4}:){1,7}:$|^(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}$|^(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}$|^(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}$|^(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:(?::[0-9a-fA-F]{1,4}){1,6}$|^:(?::[0-9a-fA-F]{1,4}){1,7}$|^::$|^::1$|^(?:[0-9a-fA-F]{1,4}:){6}(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
+ "file-read*"
+ "ftp"
+ "ftps"
+ "http"
+ "https"
+ "i"
+ "path"
+ "port"
+ "queryParameters"
+ "scheme"
+ "ssh"
+ "telnet"
- "*"
- "*56@0:8r*16*24I32I36I40I44@48"
- ".cxx_destruct"
- "@\"NEBitVector\""
- "@\"NSData\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8r*16"
- "@28@0:8I16d20"
- "@32@0:8*16I24I28"
- "@52@0:8@16I24I28I32@36@44"
- "B24@0:8@16"
- "B24@0:8q16"
- "B32@0:8r*16^{ne_bloom_filter={ne_bloom_filter_header=QQIIII}I^v^v*^vId}24"
- "B36@0:8*16I24q28"
- "B44@0:8*16I24I28I32r*36"
- "I"
- "I16@0:8"
- "I20@0:8I16"
- "I24@0:8@16"
- "I24@0:8r*16"
- "I28@0:8@16I24"
- "I28@0:8r*16I24"
- "NEBitVector"
- "NEBloomFilter"
- "NEDiagnosticReport"
- "NEFNVHash"
- "NEMurmurHash3"
- "NEURLParser"
- "T@\"NSData\",&,N,V_bitVectorBuffer"
- "T@\"NSData\",&,N,V_tag"
- "TI,N,V_murmurSeed"
- "TI,N,V_numberOfBits"
- "TI,N,V_numberOfHashes"
- "TI,N,V_numberOfItems"
- "Td,N,V_falsePositiveTolerance"
- "UTF8String"
- "_bitCount"
- "_bitVector"
- "_bitVectorBuffer"
- "_bitmap"
- "_bitmapSize"
- "_falsePositiveTolerance"
- "_murmurSeed"
- "_numberOfBits"
- "_numberOfHashes"
- "_numberOfItems"
- "_tag"
- "addObject:"
- "addObjectsFromArray:"
- "allObjects"
- "appendFormat:"
- "appendString:"
- "bitVectorBuffer"
- "bytes"
- "clearAllBits"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "contains:"
- "containsWithBitmap:numberOfBits:numberOfHashes:murmurSeed:value:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d"
- "d16@0:8"
- "d28@0:8I16I20I24"
- "dataUsingEncoding:"
- "dataWithLength:"
- "date"
- "falsePositiveTolerance"
- "file-read-data"
- "file-read-metadata"
- "getBitAtIndex:"
- "getBitAtIndexWithBitmap:bitCount:index:"
- "getByteCount:"
- "getFalsePositiveProbability:numberOfBits:numberOfHashes:"
- "getFilterTag"
- "getNumberOfBits:falsePositiveTolerance:"
- "getNumberOfHashes:numberOfBits:"
- "hasPrefix:"
- "hasSuffix:"
- "hash:"
- "hash:seed:"
- "hashWithString:"
- "hashWithString:seed:"
- "i24@0:8I16i20"
- "i28@0:8I16d20"
- "init"
- "initFromFile:"
- "initWithBitMap:bitmapSize:bitCount:"
- "initWithBytes:length:"
- "initWithData:encoding:"
- "initWithData:numberOfBits:numberOfHashes:murmurSeed:mmapFilename:tag:"
- "initWithFormat:"
- "initWithNumberOfItems:falsePositiveTolerance:"
- "initWithString:"
- "initWithUTF8String:"
- "insert:"
- "insertWithBitmap:numberOfBits:numberOfHashes:murmurSeed:value:"
- "intValue"
- "length"
- "lengthOfBytesUsingEncoding:"
- "logInternalError:subType:context:"
- "matchingStringsForURL:"
- "mmapFromFile:bloomFilter:"
- "mmapToFile:data:dataLength:numberOfBits:numberOfHashes:murmurSeed:tag:"
- "murmurSeed"
- "numberOfBits"
- "numberOfHashes"
- "numberOfItems"
- "objectForKeyedSubscript:"
- "printBits"
- "processInfo"
- "processName"
- "rangeOfString:"
- "setBitAtIndex:toValue:"
- "setBitAtIndexWithBitmap:bitCount:index:toValue:"
- "setBitVectorBuffer:"
- "setFalsePositiveTolerance:"
- "setMurmurSeed:"
- "setNumberOfBits:"
- "setNumberOfHashes:"
- "setNumberOfItems:"
- "setObject:forKeyedSubscript:"
- "setTag:"
- "setWithCapacity:"
- "signatureWithDomain:type:subType:detectedProcess:triggerThresholdValues:"
- "snapshotWithSignature:delay:events:payload:actions:reply:"
- "string"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subarrayWithRange:"
- "substringFromIndex:"
- "tag"
- "timeIntervalSinceNow"
- "v16@0:8"
- "v20@0:8I16"
- "v24@0:8@16"
- "v24@0:8d16"
- "v28@0:8q16B24"
- "v40@0:8*16I24q28B36"
- "v40@0:8@16@24@32"
- "v44@0:8*16I24I28I32r*36"

```
