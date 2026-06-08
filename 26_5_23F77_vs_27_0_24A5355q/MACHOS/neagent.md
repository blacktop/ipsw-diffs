## neagent

> `/usr/libexec/neagent`

```diff

-2226.120.19.0.0
-  __TEXT.__text: 0x1645c
-  __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_stubs: 0x1aa0
-  __TEXT.__objc_methlist: 0x1040
-  __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x3a4
-  __TEXT.__objc_methname: 0x24ad
-  __TEXT.__oslogstring: 0x31a3
-  __TEXT.__cstring: 0x10d0
-  __TEXT.__objc_classname: 0x32d
-  __TEXT.__objc_methtype: 0xdda
-  __TEXT.__unwind_info: 0x3b8
-  __DATA_CONST.__auth_got: 0x3e8
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x550
-  __DATA_CONST.__cfstring: 0x460
-  __DATA_CONST.__objc_classlist: 0x80
-  __DATA_CONST.__objc_protolist: 0xb0
+2303.0.0.0.2
+  __TEXT.__text: 0x1adc8
+  __TEXT.__auth_stubs: 0x950
+  __TEXT.__objc_stubs: 0x25a0
+  __TEXT.__objc_methlist: 0x1210
+  __TEXT.__const: 0xf0
+  __TEXT.__gcc_except_tab: 0x6bc
+  __TEXT.__objc_methname: 0x2db5
+  __TEXT.__oslogstring: 0x3ebe
+  __TEXT.__cstring: 0x18d3
+  __TEXT.__objc_classname: 0x354
+  __TEXT.__objc_methtype: 0xef8
+  __TEXT.__unwind_info: 0x430
+  __DATA_CONST.__const: 0x690
+  __DATA_CONST.__cfstring: 0xb00
+  __DATA_CONST.__objc_classlist: 0x98
+  __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x58
-  __DATA.__objc_const: 0x1e28
-  __DATA.__objc_selrefs: 0xa58
-  __DATA.__objc_ivar: 0x144
-  __DATA.__objc_data: 0x500
-  __DATA.__data: 0x840
-  __DATA.__bss: 0x90
+  __DATA_CONST.__objc_superrefs: 0x68
+  __DATA_CONST.__objc_intobj: 0x90
+  __DATA_CONST.__auth_got: 0x4b8
+  __DATA_CONST.__got: 0x1d8
+  __DATA.__objc_const: 0x21e8
+  __DATA.__objc_selrefs: 0xd30
+  __DATA.__objc_ivar: 0x174
+  __DATA.__objc_data: 0x5f0
+  __DATA.__data: 0x8a0
+  __DATA.__bss: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/AppSSO.framework/AppSSO
   - /System/Library/PrivateFrameworks/CipherML.framework/CipherML
+  - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FD2FB604-ABA9-3441-ACE6-3A411F4C3AB5
-  Functions: 310
-  Symbols:   178
-  CStrings:  968
+  UUID: C6A0513C-428B-32C2-B853-968505F12D69
+  Functions: 361
+  Symbols:   218
+  CStrings:  1269
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFRelease
+ _NEIsValidCFType
+ _NSLocalizedDescriptionKey
+ _NSLog
+ _OBJC_CLASS_$_CMLPrivacyPassToken
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_NSMutableURLRequest
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$_NSURLSession
+ _OBJC_CLASS_$_NSURLSessionConfiguration
+ _OBJC_CLASS_$_PBCodable
+ _OBJC_METACLASS_$_PBCodable
+ _PBDataWriterWriteStringField
+ _PBReaderReadString
+ _PBReaderSkipValueWithTag
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ ___NSArray0__struct
+ ___kCFBooleanFalse
+ ___strlcpy_chk
+ __dispatch_source_type_timer
+ _dispatch_activate
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _dispatch_time
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_release_x9
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_setProperty_nonatomic_copy
+ _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "#"
+ "%*"
+ "%@"
+ "%@ %@"
+ "%@%@%@"
+ "%@%@%@=%@"
+ "%@/"
+ "%@/%@"
+ "%@: %s - Canceling reporting timer"
+ "%@: %s - Failed to create reporting timer source"
+ "%@: %s - Failed to retrieve privacy token for report: %@"
+ "%@: %s - Failed to send blocked URLs report: %@"
+ "%@: %s - Filter not active, skipping report"
+ "%@: %s - No reporting URL configured, skipping report"
+ "%@: %s - Report interval is %f, not setting up reporting timer"
+ "%@: %s - Sending blocked URLs report in protobuf format to %@"
+ "%@: %s - Setting up reporting timer with interval %f seconds"
+ "%@: %s - Successfully created repeating reporting timer with %f second interval"
+ "%@: %s - Successfully sent blocked URLs report"
+ "%@: %s - Using test report endpoint %@"
+ "%@: %s - init report using mmap file %@"
+ "%@: Added Authorization header with PrivateToken + base64 token (length: %lu)"
+ "%@: Bloom filter has no mmap data to post"
+ "%@: Bloom filter has no mmap memory content to clear"
+ "%@: Bundle ID truncated from %d to %d characters: %s"
+ "%@: Cannot reinitialize - mmap not properly set up"
+ "%@: Clearing mmap memory content (%u entries)"
+ "%@: Collected %lu unique URLs for JSON serialization"
+ "%@: Collected %lu unique URLs for protobuf serialization"
+ "%@: Corrupted file - currentCount (%u) > maxEntries (%u). Reinitializing file."
+ "%@: Creating new mmap file"
+ "%@: Existing file has invalid magic number (0x%llx), reinitializing"
+ "%@: Extending existing mmap file from %zu to %zu bytes"
+ "%@: Failed to create JSON data: %@"
+ "%@: Failed to mmap file: %s"
+ "%@: Failed to open mmap file %@: %s"
+ "%@: Failed to post mmap data: %@"
+ "%@: Failed to process binary auth token data (raw length: %lu)"
+ "%@: Failed to resize mmap file: %s"
+ "%@: Failed to serialize protobuf data"
+ "%@: Failed to sync cleared mmap data to disk: %s"
+ "%@: Failed to sync reinitialized mmap data to disk: %s"
+ "%@: Found existing mmap file with size %zu bytes (expected: %zu bytes)"
+ "%@: Found valid existing mmap file with %u entries (max: %u, version: %u)"
+ "%@: Generated JSON data with %lu URLs (%lu bytes)"
+ "%@: Generated protobuf data with %lu URLs (%lu bytes) using ProtocolBuffer framework"
+ "%@: Initialized mmap file %@ with %u max entries, current count: %u"
+ "%@: Invalid mmap magic number, file may be corrupted"
+ "%@: Invalid mmap magic number, returning empty JSON data"
+ "%@: Invalid mmap magic number, skipping mmap entries"
+ "%@: Max entries mismatch - file has %u, expected %u. Reinitializing file."
+ "%@: No auth token provided for request"
+ "%@: No mmap data to post"
+ "%@: Posting %lu bytes of %@ data to %@ using %@ protocol (privacyProxyFailClosed %d)"
+ "%@: Processing auth token with length: %lu bytes"
+ "%@: Reinitializing mmap file content"
+ "%@: Server returned error code: %ld"
+ "%@: Successfully cleared mmap memory content and synced to disk"
+ "%@: Successfully posted mmap data. Response code: %ld"
+ "%@: URL truncated from %d to %d characters"
+ "%@: Unsupported mmap version %u, expected %u"
+ "%@: Version mismatch - file has version %u, expected %u. Reinitializing file."
+ "%@: WARNING: Existing file is larger than expected (%zu > %zu bytes). This may indicate version mismatch or corruption."
+ "%@: handleNewRequest - Allow neagent requests"
+ "%@: handleNewRequest - regular expression parse result is nil - allow <parsed groupnames %@>"
+ "%@: mmap file is full (%u entries), will overwrite latest entry (LIFO)"
+ "%@: mmap not initialized, cannot clear content"
+ "%@: mmap not initialized, cannot write blocked URL"
+ "%@: mmap not initialized, returning empty JSON data"
+ "%@: msync warning: %s"
+ "%@:%@"
+ "%@://"
+ "%lu"
+ "&"
+ "-[NEPIRChecker initializeMmapFile]"
+ "-[NEURLFilterEngine cancelReportingTimer]"
+ "-[NEURLFilterEngine sendBlockedURLsReport:]"
+ "-[NEURLFilterEngine sendBlockedURLsReport:]_block_invoke"
+ "-[NEURLFilterEngine sendBlockedURLsReport:]_block_invoke_2"
+ "-[NEURLFilterEngine setConfiguration:completionHandler:]_block_invoke_2"
+ "-[NEURLFilterEngine setupReportingTimer]"
+ "-[NEURLFilterEngine startFilterWithCompletionHandler:]_block_invoke_2"
+ "/([^/]+)"
+ "/private/var/db/urlPrefilter/com.apple.networkextension.url-prefilter-data.report."
+ ":"
+ "="
+ "?"
+ "@\"NSDate\""
+ "@24@0:8^{_NSZone=}16"
+ "@36@0:8@16@24i32"
+ "@40@0:8@16Q24@32"
+ "@48@0:8@16@24@32@40"
+ "@88@0:8@16Q24q32q40@48@56@64@72@80"
+ "Authorization"
+ "Content-Length"
+ "Content-Type"
+ "Failed to compile URL regex: %@"
+ "Failed to compile path components regex: %@"
+ "Invalid URL scheme. Only HTTP and HTTPS are supported"
+ "Invalid format. Use 'json' or 'protobuf'"
+ "NEBlockedURLEntry"
+ "NERegexURLParser"
+ "NEURLFilterReport"
+ "NSCopying"
+ "POST"
+ "PrivateToken token=%@"
+ "Q"
+ "Server returned status %ld"
+ "T@\"NSDate\",&,N,V_timestamp"
+ "T@\"NSString\",C,N,V_sourceBundleId"
+ "T@\"NSString\",C,N,V_url"
+ "Ti,N,V_sourcePID"
+ "URLWithString:relativeToURL:"
+ "["
+ "[]"
+ "]"
+ "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
+ "^(?:(?<scheme>[a-zA-Z][a-zA-Z0-9+.-]*):)?(?://)?(?:(?<userinfo>[^@/\\?#]*+)@)?(?<host>\\[[0-9a-fA-F:]+\\]|[^:/\\?#]*+)(?::(?<port>\\d+))?(?<path>/[^\\?#]*+)?(?:\\?(?<query>[^#]*+))?(?:#(?<fragment>.*))?$"
+ "^(?:[0-9a-fA-F]{1,4}:){1,7}[0-9a-fA-F]{1,4}$|^(?:[0-9a-fA-F]{1,4}:){1,7}:$|^:(?::[0-9a-fA-F]{1,4}){1,7}$|^::$|^::1$"
+ "^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$|^(?:[0-9a-fA-F]{1,4}:){1,7}:$|^(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}$|^(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}$|^(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}$|^(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}$|^(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}$|^[0-9a-fA-F]{1,4}:(?::[0-9a-fA-F]{1,4}){1,6}$|^:(?::[0-9a-fA-F]{1,4}){1,7}$|^::$|^::1$|^(?:[0-9a-fA-F]{1,4}:){6}(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
+ "^v"
+ "^{ne_pir_blocked_url_entry=[512c][128c]iSSQ}"
+ "^{ne_pir_blocked_url_header=QIIII}"
+ "_mmapEntries"
+ "_mmapFileDescriptor"
+ "_mmapFilePath"
+ "_mmapFileSize"
+ "_mmapHeader"
+ "_mmapMemory"
+ "_reportingTimer"
+ "_setError"
+ "_setPrivacyProxyFailClosed:"
+ "_sourceBundleId"
+ "_sourcePID"
+ "_timestamp"
+ "_url"
+ "_urls"
+ "absoluteURL"
+ "allocWithZone:"
+ "application/json"
+ "application/x-protobuf"
+ "arrayWithCapacity:"
+ "base64EncodedStringWithOptions:"
+ "clearMmapMemoryContent"
+ "com.apple.private.neagent"
+ "compare:"
+ "copyWithZone:"
+ "data"
+ "dataTaskWithRequest:completionHandler:"
+ "dataWithJSONObject:options:error:"
+ "date"
+ "dateWithTimeIntervalSince1970:"
+ "dictionary"
+ "dictionaryRepresentation"
+ "ephemeralSessionConfiguration"
+ "fetchPrivacyPassTokenForGroup:dispatchQueue:completionHandler:"
+ "file-read*"
+ "finishTasksAndInvalidate"
+ "firstMatchInString:options:range:"
+ "firstObject"
+ "ftp"
+ "ftps"
+ "getBytes:range:"
+ "getCachedBlockedURLs"
+ "hasError"
+ "http"
+ "https"
+ "i16@0:8"
+ "initWithBytes:length:encoding:"
+ "initWithDictionary:copyItems:"
+ "initWithObjects:"
+ "initWithURL:sourceBundleId:sourcePID:"
+ "lowercaseString"
+ "matchesInString:options:range:"
+ "matchingStringsForDomain:options:port:"
+ "matchingStringsForURLString:"
+ "matchingStringsForURLString:options:domainLevels:pathSegments:queryParameters:componentPlaceHolder:parsePattern:parseGroupNames:parseDelimitor:"
+ "mutableCopy"
+ "parseQueryParameters:"
+ "parseURLComponents:"
+ "parseURLWithPattern:groupNames:url:delimiter:"
+ "parsingCaseSensitive"
+ "parsingDomainLevels"
+ "parsingEnumerateDomainHierarchy"
+ "parsingEnumeratePathHierarchy"
+ "parsingExcludeDomain"
+ "parsingExcludeFragment"
+ "parsingExcludeIntermediates"
+ "parsingExcludePath"
+ "parsingExcludeQuery"
+ "parsingExcludeScheme"
+ "parsingExcludeWWW"
+ "parsingGroupNames"
+ "parsingPathSegments"
+ "parsingQueryNames"
+ "parsingRegularExpression"
+ "port"
+ "position"
+ "postMmapDataToEndpoint:format:authorizationToken:completionHandler:"
+ "queryParameters"
+ "rangeAtIndex:"
+ "rangeWithName:"
+ "readFrom:"
+ "regularExpressionWithPattern:options:error:"
+ "reportEndpoint"
+ "reportFormat"
+ "reportInterval"
+ "requestWithURL:cachePolicy:timeoutInterval:"
+ "scheme"
+ "sessionWithConfiguration:"
+ "set"
+ "setHTTPBody:"
+ "setHTTPMethod:"
+ "setObject:forKey:"
+ "setPosition:"
+ "setSourceBundleId:"
+ "setSourcePID:"
+ "setTimeoutIntervalForRequest:"
+ "setTimeoutIntervalForResource:"
+ "setTimestamp:"
+ "setUrl:"
+ "setValue:forHTTPHeaderField:"
+ "sortedArrayUsingSelector:"
+ "sourceBundleId"
+ "sourcePID"
+ "ssh"
+ "statusCode"
+ "stringByRemovingPercentEncoding"
+ "stringValue"
+ "substringToIndex:"
+ "substringWithRange:"
+ "telnet"
+ "testReportURL"
+ "timeIntervalSince1970"
+ "timestamp"
+ "unionSet:"
+ "unknown"
+ "uppercaseString"
+ "url"
+ "urls"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24"
+ "v48@0:8@\"NSURL\"16q24@\"NSData\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8@16q24@32@?40"
+ "writeTo:"
- "file-read-data"
- "file-read-metadata"
- "numberWithBool:"

```
