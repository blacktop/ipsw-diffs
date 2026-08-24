## JSApp

> `/System/Applications/Books.app/Contents/Frameworks/JSApp.framework/Versions/A/JSApp`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-6647.0.0.0.0
-  __TEXT.__text: 0x895ec
+6655.0.0.0.0
+  __TEXT.__text: 0x8a108
   __TEXT.__auth_stubs: 0x2960
-  __TEXT.__objc_stubs: 0x6ba0
-  __TEXT.__objc_methlist: 0x444c
-  __TEXT.__objc_methname: 0xa171
-  __TEXT.__cstring: 0x49a9
+  __TEXT.__objc_stubs: 0x6be0
+  __TEXT.__objc_methlist: 0x4474
+  __TEXT.__objc_methname: 0xa1e1
+  __TEXT.__cstring: 0x4a49
   __TEXT.__objc_classname: 0xd54
-  __TEXT.__objc_methtype: 0x2186
+  __TEXT.__objc_methtype: 0x2196
   __TEXT.__const: 0x2b94
-  __TEXT.__oslogstring: 0x3aa4
+  __TEXT.__oslogstring: 0x3b04
   __TEXT.__gcc_except_tab: 0xb88
-  __TEXT.__swift5_typeref: 0x1058
+  __TEXT.__swift5_typeref: 0x1062
   __TEXT.__swift5_capture: 0xb5c
   __TEXT.__swift5_fieldmd: 0xc88
   __TEXT.__constg_swiftt: 0x133c

   __TEXT.__swift_as_ret: 0xf4
   __TEXT.__swift_as_cont: 0x190
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x25a0
+  __TEXT.__unwind_info: 0x25b0
   __TEXT.__eh_frame: 0x2828
-  __DATA_CONST.__const: 0x5511
-  __DATA_CONST.__cfstring: 0x2da0
+  __DATA_CONST.__const: 0x5549
+  __DATA_CONST.__cfstring: 0x2e00
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x220

   __DATA_CONST.__auth_got: 0x14c0
   __DATA_CONST.__got: 0x920
   __DATA_CONST.__auth_ptr: 0x5a8
-  __DATA.__objc_const: 0x8218
-  __DATA.__objc_selrefs: 0x27e8
+  __DATA.__objc_const: 0x8230
+  __DATA.__objc_selrefs: 0x2800
   __DATA.__objc_ivar: 0x2fc
   __DATA.__objc_data: 0x28c0
-  __DATA.__data: 0x2fc8
+  __DATA.__data: 0x2fe8
   __DATA.__bss: 0x3290
   __DATA.__common: 0x78
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3174
+  Functions: 3185
   Symbols:   736
-  CStrings:  3020
+  CStrings:  3029
 
CStrings:
+ "-[JSAEnvironment _loadScript:name:version:isBundled:completion:]"
+ "-[JSAEnvironment _loadScript:name:version:isBundled:completion:]_block_invoke"
+ "-[JSAEnvironment _loadScriptFromPackage:retryCount:completion:]"
+ "-[JSAEnvironment _loadScriptFromPackage:retryCount:completion:]_block_invoke"
+ "BKScriptEvaluationRetryCount"
+ "JS script is empty"
+ "JSAEnvironment %{public}s Retrying loading script due to corrupted script. Remaining tries: %ld"
+ "Loading script caused an exception"
+ "Unable to decode the string using ASCII encoding"
+ "_loadScript:name:version:isBundled:completion:"
+ "_loadScriptFromPackage:retryCount:completion:"
+ "scriptEvaluationRetryCount"
+ "setScriptEvaluationRetryCount:"
+ "v40@0:8@16q24@?32"
+ "yyyy-MM-dd-HHmmss.SSS"
- "-[JSAEnvironment loadScript:name:version:isBundled:completion:]"
- "-[JSAEnvironment loadScript:name:version:isBundled:completion:]_block_invoke"
- "-[JSAEnvironment loadScriptFromPackage:completion:]"
- "-[JSAEnvironment loadScriptFromPackage:completion:]_block_invoke"
- "loadScript:name:version:isBundled:completion:"
- "yyyy-MM-dd-HHmmss"
```
