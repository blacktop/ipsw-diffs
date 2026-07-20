## BulkSymbolication

> `/System/Library/PrivateFrameworks/BulkSymbolication.framework/Versions/A/BulkSymbolication`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-436.0.0.0.0
-  __TEXT.__text: 0xc868
-  __TEXT.__objc_methlist: 0x914
-  __TEXT.__const: 0x90
-  __TEXT.__cstring: 0xb95
-  __TEXT.__gcc_except_tab: 0x3d4
-  __TEXT.__oslogstring: 0x6b6
-  __TEXT.__unwind_info: 0x2e8
+438.0.0.0.0
+  __TEXT.__text: 0xd858
+  __TEXT.__objc_methlist: 0x98c
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0xc01
+  __TEXT.__gcc_except_tab: 0x430
+  __TEXT.__oslogstring: 0x783
+  __TEXT.__unwind_info: 0x330
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__const: 0xb0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x758
+  __DATA_CONST.__objc_selrefs: 0x820
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__got: 0x118
-  __AUTH_CONST.__const: 0x4f0
-  __AUTH_CONST.__cfstring: 0xd80
-  __AUTH_CONST.__objc_const: 0x1750
+  __DATA_CONST.__got: 0x140
+  __AUTH_CONST.__const: 0x570
+  __AUTH_CONST.__cfstring: 0xde0
+  __AUTH_CONST.__objc_const: 0x17e0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x154
+  __DATA.__objc_ivar: 0x160
   __DATA.__data: 0x60
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x40
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 274
-  Symbols:   749
-  CStrings:  162
+  Functions: 293
+  Symbols:   811
+  CStrings:  167
 
Symbols:
+ +[BKSJob _caseInsensitiveHeader:inHeaders:]
+ +[BKSJob _delayForRateLimitedResponse:attempt:]
+ +[BKSJob _parseRetryAfterValue:]
+ -[BKSACOAuthCredentials initWithServiceClientID:oauthIDToken:oauthAccessToken:]
+ -[BKSJob _dispatchAttemptWithRequest:session:deadline:attempt:completionHandler:]
+ -[BKSJob _rateLimitAwareDataTaskWithRequest:session:completionHandler:]
+ -[BKSJob completionBlockFired]
+ -[BKSJob retryDataTasks]
+ -[BKSJob setCompletionBlockFired:]
+ -[BKSResult error]
+ -[BKSResult initWithResponse:request:symbolOwner:error:]
+ GCC_except_table129
+ GCC_except_table131
+ GCC_except_table149
+ GCC_except_table160
+ GCC_except_table184
+ GCC_except_table193
+ GCC_except_table196
+ OBJC_IVAR_$_BKSJob._completionBlockFired
+ OBJC_IVAR_$_BKSJob._retryDataTasks
+ OBJC_IVAR_$_BKSResult._error
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSScanner
+ _OBJC_CLASS_$_NSTimeZone
+ __81-[BKSJob _dispatchAttemptWithRequest:session:deadline:attempt:completionHandler:]_block_invoke
+ ___32+[BKSJob _parseRetryAfterValue:]_block_invoke
+ ___81-[BKSJob _dispatchAttemptWithRequest:session:deadline:attempt:completionHandler:]_block_invoke
+ ___81-[BKSJob _dispatchAttemptWithRequest:session:deadline:attempt:completionHandler:]_block_invoke_2
+ ___block_descriptor_104_e8_32s40s48s56s64s72bs80w_e5_v8?0l
+ ___block_descriptor_80_e8_32s40s48bs56w_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24l
+ ___copy_helper_block_e8_32s40s48b56w
+ ___copy_helper_block_e8_32s40s48s56s64s72b80w
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80w
+ ___destroy_helper_block_e8_32s40s48s56w
+ _dispatch_after
+ _dispatch_get_global_queue
+ _exp2
+ _kBKSRequestErrorHTTPHeadersKey
+ _kBKSRequestErrorHTTPStatusCodeKey
+ _objc_alloc_init
+ _objc_msgSend$_caseInsensitiveHeader:inHeaders:
+ _objc_msgSend$_delayForRateLimitedResponse:attempt:
+ _objc_msgSend$_dispatchAttemptWithRequest:session:deadline:attempt:completionHandler:
+ _objc_msgSend$_parseRetryAfterValue:
+ _objc_msgSend$_rateLimitAwareDataTaskWithRequest:session:completionHandler:
+ _objc_msgSend$allHeaderFields
+ _objc_msgSend$caseInsensitiveCompare:
+ _objc_msgSend$completionBlockFired
+ _objc_msgSend$dateFromString:
+ _objc_msgSend$description
+ _objc_msgSend$initWithLocaleIdentifier:
+ _objc_msgSend$initWithResponse:request:symbolOwner:error:
+ _objc_msgSend$initWithServiceClientID:oauthIDToken:oauthAccessToken:
+ _objc_msgSend$isAtEnd
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$retryDataTasks
+ _objc_msgSend$scanDouble:
+ _objc_msgSend$scannerWithString:
+ _objc_msgSend$setCompletionBlockFired:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$setTimeZone:
+ _objc_msgSend$stringByTrimmingCharactersInSet:
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$timeZoneWithAbbreviation:
+ _objc_msgSend$timeoutInterval
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
+ _parseRetryAfterValue:.httpDateFormatter
+ _parseRetryAfterValue:.onceToken
- -[BKSJob _newBoundaryString]
- GCC_except_table147
- GCC_except_table159
- GCC_except_table168
- GCC_except_table179
- _OBJC_CLASS_$_NSMutableData
- _objc_msgSend$_newBoundaryString
- _objc_msgSend$appendData:
- _objc_msgSend$data
CStrings:
+ ""
+ "%llu offsets encountered, finalizing current request"
+ "BKS got HTTP 429; retry after %.2fs would exceed task budget (%.2fs remaining) — surfacing 429 to caller"
+ "BKS got HTTP 429; retrying after %.2fs (attempt %lu of %lu)"
+ "BKSRequestErrorHTTPHeaders"
+ "BKSRequestErrorHTTPStatusCode"
+ "BulkSymbolication will need to make %lu requests"
+ "EEE, dd MMM yyyy HH:mm:ss 'GMT'"
+ "GMT"
+ "Generating offsetsByUuid requests"
+ "Retry-After"
+ "Symbolication endpoint rate-limited the request (HTTP status code %ld). Inspect %@ in NSError.userInfo to decide how to back off."
+ "Using DAW Token to authenticate with SpeedTracer (deprecated, migrate to OAuth)"
+ "Using OD Credentials to authenticate with SpeedTracer (deprecated, migrate to OAuth)"
+ "application/json"
+ "en_US_POSIX"
+ "https://speedtracer.apple.com/api/v3/atos_batches"
- "%llu offsets encoutered, finalizing current request"
- "--%@\r\n"
- "--%@--\r\n"
- "Boundary-%@"
- "BulkSymbolication will need to make %lu more requests"
- "Content-Disposition: form-data; name=\"file\"; filename=\"file.txt\"\r\n"
- "Content-Type: text/plain\r\n\r\n"
- "UUID+offset dictionary available, generating requests"
- "Using DAW Token to authenticate with SpeedTracer"
- "Using OD Credentials to authenticate with SpeedTracer"
- "https://speedtracer.apple.com/api/v2/atos_batches"
- "multipart/form-data; boundary=%@"
```
