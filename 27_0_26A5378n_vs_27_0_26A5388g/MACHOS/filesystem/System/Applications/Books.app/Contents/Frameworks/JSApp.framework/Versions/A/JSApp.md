## JSApp

> `/System/Applications/Books.app/Contents/Frameworks/JSApp.framework/Versions/A/JSApp`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-6643.0.0.0.0
-  __TEXT.__text: 0x872a4
-  __TEXT.__auth_stubs: 0x2910
-  __TEXT.__objc_stubs: 0x6b00
-  __TEXT.__objc_methlist: 0x442c
-  __TEXT.__objc_methname: 0xa0b1
-  __TEXT.__cstring: 0x48f9
+6647.0.0.0.0
+  __TEXT.__text: 0x895ec
+  __TEXT.__auth_stubs: 0x2960
+  __TEXT.__objc_stubs: 0x6ba0
+  __TEXT.__objc_methlist: 0x444c
+  __TEXT.__objc_methname: 0xa171
+  __TEXT.__cstring: 0x49a9
   __TEXT.__objc_classname: 0xd54
   __TEXT.__objc_methtype: 0x2186
-  __TEXT.__const: 0x2b74
-  __TEXT.__oslogstring: 0x3624
+  __TEXT.__const: 0x2b94
+  __TEXT.__oslogstring: 0x3aa4
   __TEXT.__gcc_except_tab: 0xb88
   __TEXT.__swift5_typeref: 0x1058
   __TEXT.__swift5_capture: 0xb5c

   __TEXT.__swift_as_ret: 0xf4
   __TEXT.__swift_as_cont: 0x190
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x2578
-  __TEXT.__eh_frame: 0x27a8
+  __TEXT.__unwind_info: 0x25a0
+  __TEXT.__eh_frame: 0x2828
   __DATA_CONST.__const: 0x5511
   __DATA_CONST.__cfstring: 0x2da0
   __DATA_CONST.__objc_classlist: 0x2b8

   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_arrayobj: 0x78
-  __DATA_CONST.__auth_got: 0x1498
-  __DATA_CONST.__got: 0x910
+  __DATA_CONST.__auth_got: 0x14c0
+  __DATA_CONST.__got: 0x920
   __DATA_CONST.__auth_ptr: 0x5a8
   __DATA.__objc_const: 0x8218
-  __DATA.__objc_selrefs: 0x27c0
+  __DATA.__objc_selrefs: 0x27e8
   __DATA.__objc_ivar: 0x2fc
   __DATA.__objc_data: 0x28c0
-  __DATA.__data: 0x2fb8
+  __DATA.__data: 0x2fc8
   __DATA.__bss: 0x3290
-  __DATA.__common: 0x60
+  __DATA.__common: 0x78
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3156
-  Symbols:   735
-  CStrings:  2994
+  Functions: 3174
+  Symbols:   736
+  CStrings:  3020
 
Symbols:
+ _JSStringGetLength
CStrings:
+ "$bootstrap should return a Runtime object"
+ "-[JSAEnvironment loadScriptFromPackage:completion:]"
+ "-[JSAEnvironment loadScriptFromPackage:completion:]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Febjm2/Sources/Alder/frameworks/JSApp/JSApp/API/Application/JSAApplication.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Febjm2/Sources/Alder/frameworks/JSApp/JSApp/API/Bag/JSAProfileBagManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Febjm2/Sources/Alder/frameworks/JSApp/JSApp/API/Requests/JSAStoreHTTPRequest.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Febjm2/Sources/Alder/frameworks/JSApp/JSApp/API/Requests/StoreContentLookupRequest.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Febjm2/Sources/Alder/frameworks/JSApp/JSApp/API/Store/AccountController.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Febjm2/Sources/Alder/frameworks/JSApp/JSApp/API/URL Parsing/URLParser.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Febjm2/Sources/Alder/frameworks/JSApp/JSApp/Infrastructure/JSABridge+Actor.swift"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Febjm2/Sources/Alder/frameworks/JSApp/JSApp/Infrastructure/JSAEnvironment.m"
+ "Failed to load file from JetPack, path: %s, error: %@"
+ "Failed to load metadata from JetPack, name: %s, error: %@"
+ "Failed to load string from JetPack, path: %s, error: %@"
+ "Failed to persist diagnostics to %{public}s: %@"
+ "Failed to read dir from JetPack, path: %s, error: %@"
+ "JSABridge loadScriptFromPackage: done, success=%@"
+ "JSAEnvironment %{public}s Failed to create folder for diagnostics files for load script failure, script size=%lu, error: %@"
+ "JSAEnvironment %{public}s Failed to save app.js to diagnostics folder, size=%lu, error: %@"
+ "JSAEnvironment %{public}s JS script is empty. Something is wrong with JetPack loading"
+ "JSAEnvironment %{public}s Package is nil!"
+ "JSAEnvironment %{public}s Persisted diagnostic files to %@"
+ "JSAEnvironment %{public}s Persisting diagnostic files due to failure to load script from JetPack, path=%@"
+ "JSAEnvironment %{public}s Saved app.js to diagnostics folder, size=%lu"
+ "JSAEnvironment %{public}s Script is nil!"
+ "JSAEnvironment %{public}s script.length=%lu, name=%@, version=%@, isBundled=%@"
+ "JSAEnvironment %{public}s unable to decode the string using ASCII encoding, something is wrong with javascript app"
+ "JetPackDiagnostics"
+ "Persisted diagnostics to %{public}s"
+ "URLByAppendingPathComponent:isDirectory:"
+ "We should have App in javascript"
+ "We should have config in javascript"
+ "copyItemAtURL:toURL:error:"
+ "createNewDiagnosticsDirAndReturnError:"
+ "persistDiagnosticsTo:"
+ "setDateFormat:"
+ "setLocale:"
+ "writeToURL:options:error:"
+ "yyyy-MM-dd-HHmmss"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M8Qls8/Sources/Alder/frameworks/JSApp/JSApp/API/Application/JSAApplication.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M8Qls8/Sources/Alder/frameworks/JSApp/JSApp/API/Bag/JSAProfileBagManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M8Qls8/Sources/Alder/frameworks/JSApp/JSApp/API/Requests/JSAStoreHTTPRequest.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M8Qls8/Sources/Alder/frameworks/JSApp/JSApp/API/Requests/StoreContentLookupRequest.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M8Qls8/Sources/Alder/frameworks/JSApp/JSApp/API/Store/AccountController.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M8Qls8/Sources/Alder/frameworks/JSApp/JSApp/API/URL Parsing/URLParser.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M8Qls8/Sources/Alder/frameworks/JSApp/JSApp/Infrastructure/JSABridge+Actor.swift"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M8Qls8/Sources/Alder/frameworks/JSApp/JSApp/Infrastructure/JSAEnvironment.m"
- "JSABridge loadScriptFromPackage: done"
- "JSAEnvironment %{public}s"
- "JSAEnvironment %{public}s unable to encode the string using ASCII encoding, something is wrong with javascript app"
- "setPrefersEdgeAttachedInCompactHeight:"
- "sheetPresentationController"
```
