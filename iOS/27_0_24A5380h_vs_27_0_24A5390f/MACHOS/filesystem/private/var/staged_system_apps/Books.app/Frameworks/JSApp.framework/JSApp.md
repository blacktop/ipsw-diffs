## JSApp

> `/private/var/staged_system_apps/Books.app/Frameworks/JSApp.framework/JSApp`

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
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-6643.0.0.0.0
-  __TEXT.__text: 0x84d80
-  __TEXT.__auth_stubs: 0x2910
-  __TEXT.__objc_stubs: 0x6980
-  __TEXT.__objc_methlist: 0x446c
-  __TEXT.__objc_methname: 0xa031
-  __TEXT.__cstring: 0x4669
+6647.0.0.0.0
+  __TEXT.__text: 0x87094
+  __TEXT.__auth_stubs: 0x2960
+  __TEXT.__objc_stubs: 0x6a20
+  __TEXT.__objc_methlist: 0x448c
+  __TEXT.__objc_methname: 0xa0d1
+  __TEXT.__cstring: 0x4719
   __TEXT.__objc_classname: 0xd84
   __TEXT.__objc_methtype: 0x2176
-  __TEXT.__const: 0x2bf4
-  __TEXT.__oslogstring: 0x34e4
+  __TEXT.__const: 0x2be4
+  __TEXT.__oslogstring: 0x3964
   __TEXT.__gcc_except_tab: 0xb88
   __TEXT.__swift5_typeref: 0x10a0
   __TEXT.__swift5_capture: 0xb78

   __TEXT.__swift_as_ret: 0xe0
   __TEXT.__swift_as_cont: 0x178
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x2560
-  __TEXT.__eh_frame: 0x26d8
+  __TEXT.__unwind_info: 0x2588
+  __TEXT.__eh_frame: 0x2758
   __DATA_CONST.__const: 0x56f9
   __DATA_CONST.__cfstring: 0x2da0
   __DATA_CONST.__objc_classlist: 0x2b8

   __DATA_CONST.__objc_dictobj: 0xf0
   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_arrayobj: 0x78
-  __DATA_CONST.__auth_got: 0x1498
-  __DATA_CONST.__got: 0x930
+  __DATA_CONST.__auth_got: 0x14c0
+  __DATA_CONST.__got: 0x940
   __DATA_CONST.__auth_ptr: 0x5b0
   __DATA.__objc_const: 0x8260
-  __DATA.__objc_selrefs: 0x2790
+  __DATA.__objc_selrefs: 0x27b8
   __DATA.__objc_ivar: 0x2f8
   __DATA.__objc_data: 0x2990
   __DATA.__data: 0x2fc8
   __DATA.__bss: 0x3380
-  __DATA.__common: 0x60
+  __DATA.__common: 0x78
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3148
-  Symbols:   743
-  CStrings:  2982
+  Functions: 3166
+  Symbols:   744
+  CStrings:  3008
 
Symbols:
+ _JSStringGetLength
CStrings:
+ "$bootstrap should return a Runtime object"
+ "-[JSAEnvironment loadScriptFromPackage:completion:]"
+ "-[JSAEnvironment loadScriptFromPackage:completion:]_block_invoke"
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
- "JSABridge loadScriptFromPackage: done"
- "JSAEnvironment %{public}s"
- "JSAEnvironment %{public}s unable to encode the string using ASCII encoding, something is wrong with javascript app"
- "setPrefersEdgeAttachedInCompactHeight:"
- "sheetPresentationController"
```
