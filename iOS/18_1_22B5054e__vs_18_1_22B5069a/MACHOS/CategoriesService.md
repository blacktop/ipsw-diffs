## CategoriesService

> `/System/Library/PrivateFrameworks/Categories.framework/XPCServices/CategoriesService.xpc/CategoriesService`

```diff

-44.0.0.0.0
-  __TEXT.__text: 0x4c18
-  __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_stubs: 0xc40
-  __TEXT.__objc_methlist: 0x258
-  __TEXT.__const: 0xa8
-  __TEXT.__objc_methname: 0xc90
-  __TEXT.__oslogstring: 0x485
-  __TEXT.__cstring: 0x55e
-  __TEXT.__objc_classname: 0xd0
-  __TEXT.__objc_methtype: 0x31d
-  __TEXT.__gcc_except_tab: 0x15c
-  __TEXT.__unwind_info: 0x178
-  __DATA_CONST.__auth_got: 0x2e0
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x208
-  __DATA_CONST.__cfstring: 0x920
-  __DATA_CONST.__objc_classlist: 0x40
+44.1.1.0.0
+  __TEXT.__text: 0x49c8
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_stubs: 0xc00
+  __TEXT.__objc_methlist: 0x1f8
+  __TEXT.__const: 0xb8
+  __TEXT.__objc_methname: 0xb9a
+  __TEXT.__oslogstring: 0x4c6
+  __TEXT.__cstring: 0x5a7
+  __TEXT.__objc_classname: 0xb7
+  __TEXT.__objc_methtype: 0x26b
+  __TEXT.__gcc_except_tab: 0x180
+  __TEXT.__unwind_info: 0x158
+  __DATA_CONST.__auth_got: 0x228
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__const: 0x2c8
+  __DATA_CONST.__cfstring: 0x900
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x38
-  __DATA.__objc_const: 0xaf8
-  __DATA.__objc_selrefs: 0x378
-  __DATA.__objc_ivar: 0x38
-  __DATA.__objc_data: 0x280
+  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA.__objc_const: 0x910
+  __DATA.__objc_selrefs: 0x340
+  __DATA.__objc_ivar: 0x20
+  __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x120
-  __DATA.__bss: 0x28
+  __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 78
-  Symbols:   172
-  CStrings:  331
+  Functions: 71
+  Symbols:   141
+  CStrings:  309
 
Symbols:
+ _CTErrorKeyHTTPResponse
+ _MGCopyAnswer
+ _OBJC_CLASS_$_NSCache
+ _OBJC_CLASS_$_NSMutableURLRequest
+ _OBJC_CLASS_$_NSXPCConnection
+ ___NSArray0__struct
+ _dispatch_main
+ _objc_release_x1
- OBJC_IVAR_$_CTCache._file
- OBJC_IVAR_$_CTCache._lock
- OBJC_IVAR_$_CTCache._path
- OBJC_IVAR_$_CTCache._start
- _NSStringFromClass
- _OBJC_CLASS_$_CTCache
- _OBJC_CLASS_$_CTMutableCache
- _OBJC_CLASS_$_NSData
- _OBJC_CLASS_$_NSKeyedArchiver
- _OBJC_CLASS_$_NSKeyedUnarchiver
- _OBJC_CLASS_$_NSRunLoop
- _OBJC_METACLASS_$_CTCache
- _OBJC_METACLASS_$_CTMutableCache
- ___chkstk_darwin
- _fclose
- _feof
- _fflush
- _fgetpos
- _fileno
- _fopen
- _fread
- _fseek
- _fsetpos
- _ftell
- _ftruncate
- _fwrite
- _malloc_type_malloc
- _memcmp
- _objc_retain_x27
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
- _proc_pidpath
- _pthread_mutex_destroy
- _pthread_mutex_init
- _pthread_mutex_lock
- _pthread_mutex_unlock
- _strlen
- _unlink
CStrings:
+ "%!@(MISSING), %!@(MISSING)"
+ "%!@(MISSING)/%!@(MISSING)/%!@(MISSING)/%!@(MISSING)"
+ "-[Categories_Service init]"
+ "-[ServiceDelegate init]"
+ "@40@0:8@16@24^@32"
+ "BuildVersion"
+ "Not performing iTunes lookup for cached bundle IDs: %!{(MISSING)public}@"
+ "Performing iTunes lookup on behalf of %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "T@\"NSCache\",R"
+ "T@\"NSString\",R,V_platform"
+ "User-Agent"
+ "_lookupAppStoreUsing:platform:clientApplication:withCompletionHandler:"
+ "_platform"
+ "appStoreSearchResultsWithResultData:platform:error:"
+ "application-identifier"
+ "componentsSeparatedByString:"
+ "currentConnection"
+ "dataTaskWithRequest:completionHandler:"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "iTunes server is overloaded. Caching empty results for: %!{(MISSING)public}@"
+ "initWithBundleID:platform:"
+ "initWithSearchResultRecord:platform:"
+ "initWithURL:"
+ "mainBundle"
+ "marketing-name"
+ "mutableCopy"
+ "platform"
+ "removeObject:"
+ "resultByBundleID"
+ "setObject:forKeyedSubscript:"
+ "setValue:forHTTPHeaderField:"
+ "userInfo"
+ "v32@?0@\"NSString\"8@\"NSArray\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSError\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSMutableArray\"16^B24"
- "%!@(MISSING), %!@(MISSING), %!@(MISSING)"
- "%!l(MISSING)u"
- "-[Categories_Service initWithCachedData:]"
- "-[ServiceDelegate initWithCachedCategories:]"
- "<%!@(MISSING) %!@(MISSING)>"
- "@\"CTCache\""
- "@32@0:8@16^@24"
- "CALLING PROCESS :: %!@(MISSING)"
- "CTCache"
- "CTMutableCache"
- "Cache file magic number mismatch, expected %!x(MISSING), got %!x(MISSING)"
- "Name must be a NSString. Search result record: %!@(MISSING)"
- "T@\"NSString\",C,V_callingProcessName"
- "T@\"NSString\",R,C,V_name"
- "^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}"
- "_cachedData"
- "_callingProcessName"
- "_file"
- "_lock"
- "_lookupAppStoreUsing:platform:context:withCompletionHandler:"
- "_name"
- "_path"
- "_start"
- "a+"
- "appStoreSearchResultsWithResultData:error:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "bundleWithPath:"
- "bytes"
- "callingProcessName"
- "categoryForBundleId:"
- "currentRunLoop"
- "dataTaskWithURL:completionHandler:"
- "dataWithBytes:length:"
- "https://itunes.apple.com/search"
- "initWithCachedCategories:"
- "initWithCachedData:"
- "initWithPath:version:"
- "initWithSearchResultRecord:"
- "limit"
- "name"
- "processIdentifier"
- "q"
- "r"
- "run"
- "searchForAppsNamed:deviceFamily:resultLimit:completionHandler:"
- "setCallingProcessName:"
- "setCategory:forBundleId:"
- "stringByDeletingLastPathComponent"
- "stringWithUTF8String:"
- "term"
- "trackName"
- "unarchivedObjectOfClass:fromData:error:"
- "v32@0:8@16@24"
- "v48@0:8@16Q24Q32@?40"
- "w+"
- "{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}"
- "\x81"

```
