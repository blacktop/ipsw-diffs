## CategoriesService

> `/System/Library/PrivateFrameworks/Categories.framework/XPCServices/CategoriesService.xpc/CategoriesService`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-56.0.0.0.0
-  __TEXT.__text: 0x50d4
-  __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_stubs: 0xee0
-  __TEXT.__objc_methlist: 0x394
-  __TEXT.__const: 0xb8
-  __TEXT.__objc_methname: 0xeac
-  __TEXT.__oslogstring: 0x746
-  __TEXT.__cstring: 0x60e
+58.0.1.0.0
+  __TEXT.__text: 0x50b4
+  __TEXT.__auth_stubs: 0x410
+  __TEXT.__objc_stubs: 0xec0
+  __TEXT.__objc_methlist: 0x3cc
+  __TEXT.__const: 0xc0
+  __TEXT.__objc_methname: 0xf12
+  __TEXT.__oslogstring: 0x62c
+  __TEXT.__cstring: 0x61c
   __TEXT.__objc_classname: 0xbb
-  __TEXT.__objc_methtype: 0x2e8
-  __TEXT.__gcc_except_tab: 0x180
-  __TEXT.__unwind_info: 0x178
-  __DATA_CONST.__const: 0x2a0
-  __DATA_CONST.__cfstring: 0x9e0
+  __TEXT.__objc_methtype: 0x2ce
+  __TEXT.__gcc_except_tab: 0x100
+  __TEXT.__unwind_info: 0x188
+  __DATA_CONST.__const: 0x2c0
+  __DATA_CONST.__cfstring: 0xac0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__auth_got: 0x220
-  __DATA_CONST.__got: 0x1c8
-  __DATA.__objc_const: 0x790
-  __DATA.__objc_selrefs: 0x4a0
-  __DATA.__objc_ivar: 0x24
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__objc_arraydata: 0x58
+  __DATA_CONST.__objc_dictobj: 0x50
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0x218
+  __DATA_CONST.__got: 0x1b8
+  __DATA.__objc_const: 0x7c0
+  __DATA.__objc_selrefs: 0x490
+  __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x120
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/Categories.framework/Categories
   - /System/Library/PrivateFrameworks/ContextKit.framework/ContextKit
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 87
+  Functions: 88
   Symbols:   146
-  CStrings:  359
+  CStrings:  356
 
Symbols:
+ _AMSErrorDomain
+ _AMSMediaTaskPlatformAppleTV
+ _AMSMediaTaskPlatformMac
+ _AMSMediaTaskPlatformiPad
+ _AMSMediaTaskPlatformiPhone
+ _OBJC_CLASS_$_AMSMediaTask
+ _OBJC_CLASS_$_AMSProcessInfo
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _objc_retain_x25
- _CTErrorKeyHTTPResponse
- _CTErrorKeyHTTPResponseData
- _MGCopyAnswer
- _OBJC_CLASS_$_NSBundle
- _OBJC_CLASS_$_NSJSONSerialization
- _OBJC_CLASS_$_NSLocale
- _OBJC_CLASS_$_NSMutableURLRequest
- _OBJC_CLASS_$_NSURLComponents
- _OBJC_CLASS_$_NSURLQueryItem
- _OBJC_CLASS_$_NSURLSession
- _objc_autorelease
CStrings:
+ "1"
+ "55"
+ "56"
+ "App Store category: %{private}@ = %@ -> %@"
+ "Corrupt response data item: %{private}@"
+ "Could not resolve app from response data item: %{private}@"
+ "Media API server is overloaded. Caching empty results for: %{private}@"
+ "Not performing Media API lookup for cached bundle IDs: %{private}@"
+ "Performing Media API lookup on behalf of %{private}@: %{private}@"
+ "Q"
+ "Q24@0:8@16"
+ "Response data item is missing a bundle identifier: %{private}@"
+ "Response data item is missing attributes: %{private}@"
+ "SOCIAL_MEDIA"
+ "SOCIAL_MEDIA_AGE_RESTRICTED"
+ "START: Media API lookup on behalf of %{private}@: %{private}@"
+ "TQ,R,V_contentDescriptors"
+ "_bundleIdentifierFromAttributes:"
+ "_contentDescriptorKindToCTContentDescriptorsMap"
+ "_contentDescriptors"
+ "_contentDescriptorsFromAttributes:"
+ "_errorIndicatesServerOverloaded:"
+ "_genreIDsFromResponseDataItem:"
+ "addFinishBlock:"
+ "ageRating"
+ "appStoreSearchResultsWithResponseDataItems:platform:"
+ "appletvos"
+ "attributes"
+ "contentDescriptors"
+ "contentLevels"
+ "createBagForSubProfile"
+ "data"
+ "extend"
+ "genres"
+ "handleMediaResult:error:platform:completionHandler:"
+ "id"
+ "identifier"
+ "initWithBundleIdentifier:"
+ "initWithPrimary:secondary:contentDescriptors:"
+ "initWithResponseDataItem:platform:"
+ "initWithType:clientIdentifier:clientVersion:bag:"
+ "ios"
+ "kind"
+ "osx"
+ "perform"
+ "performMediaAPIQueryWithBundleIDs:deviceFamily:completionHandler:"
+ "platformAttributes"
+ "relationships"
+ "responseDataItems"
+ "secondaryGenreIdentifier"
+ "setAdditionalPlatforms:"
+ "setAdditionalQueryParams:"
+ "setBundleIdentifiers:"
+ "setClientInfo:"
+ "unsignedIntegerValue"
+ "v24@?0@\"AMSMediaResult\"8@\"NSError\"16"
+ "watchos"
+ "xros"
- "%@,%@"
- "%@/%@/%@/%@"
- "@40@0:8@16@24^@32"
- "BuildVersion"
- "Bundle ID must be a NSString. Search result record: %@"
- "CTAppStoreSearchResult results: %{private}@"
- "CTAppStoreSearchResult searchResult: %{private}@"
- "Corrupt result record: %{private}@"
- "Corrupt search record: %{private}@"
- "Corrupt search results: %{private}@"
- "Could not resolve app from search result record: %{private}@"
- "Could not serialize result data with error: %@"
- "Genre ID must be a NSString. Search result record: %@"
- "Genre IDs must be a NSArray. Search result record: %@"
- "JSONObjectWithData:options:error:"
- "Not performing iTunes lookup for cached bundle IDs: %{public}@"
- "Performing iTunes lookup on behalf of %{public}@: %{public}@"
- "START: %{private}@"
- "STORELOOKUP END: %{private}@"
- "STORELOOKUP LOOKUP FAILED: %{private}@"
- "URL"
- "User-Agent"
- "appStoreSearchResultsWithResultData:platform:error:"
- "bundleIdentifier"
- "configuration"
- "country"
- "countryCode"
- "currentLocale"
- "dataTaskWithRequest:completionHandler:"
- "entity"
- "genreIds"
- "handleSearchResultsWithTaskData:platform:error:completionHandler:"
- "https://itunes.apple.com/lookup"
- "iPadSoftware"
- "iTunes server is overloaded. Caching empty results for: %{public}@"
- "initWithDomain:code:userInfo:"
- "initWithFormat:"
- "initWithName:value:"
- "initWithPrimary:secondary:"
- "initWithSearchResultRecord:platform:"
- "initWithString:"
- "initWithURL:"
- "itunes.apple.com AppStore category: %{private}@ = %@ -> %@"
- "macSoftware"
- "mainBundle"
- "marketing-name"
- "media"
- "performiTunesQueryWithURLComponents:queryItems:deviceFamily:completionHandler:"
- "results"
- "setQueryItems:"
- "setTimeoutIntervalForRequest:"
- "setTimeoutIntervalForResource:"
- "setValue:forHTTPHeaderField:"
- "set_sourceApplicationBundleIdentifier:"
- "sharedSession"
- "software"
- "statusCode"
- "tvSoftware"
- "userInfo"
- "v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24"
- "v48@0:8@16@24Q32@?40"
```
