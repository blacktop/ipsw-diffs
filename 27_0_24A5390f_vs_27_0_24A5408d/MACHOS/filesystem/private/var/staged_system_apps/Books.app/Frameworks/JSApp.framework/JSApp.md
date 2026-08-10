## JSApp

> `/private/var/staged_system_apps/Books.app/Frameworks/JSApp.framework/JSApp`

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
-  __TEXT.__text: 0x87094
+6655.0.0.0.0
+  __TEXT.__text: 0x87bb0
   __TEXT.__auth_stubs: 0x2960
-  __TEXT.__objc_stubs: 0x6a20
-  __TEXT.__objc_methlist: 0x448c
-  __TEXT.__objc_methname: 0xa0d1
-  __TEXT.__cstring: 0x4719
+  __TEXT.__objc_stubs: 0x6a60
+  __TEXT.__objc_methlist: 0x44b4
+  __TEXT.__objc_methname: 0xa151
+  __TEXT.__cstring: 0x47b9
   __TEXT.__objc_classname: 0xd84
-  __TEXT.__objc_methtype: 0x2176
+  __TEXT.__objc_methtype: 0x2186
   __TEXT.__const: 0x2be4
-  __TEXT.__oslogstring: 0x3964
+  __TEXT.__oslogstring: 0x39c4
   __TEXT.__gcc_except_tab: 0xb88
-  __TEXT.__swift5_typeref: 0x10a0
+  __TEXT.__swift5_typeref: 0x10aa
   __TEXT.__swift5_capture: 0xb78
   __TEXT.__swift5_fieldmd: 0xcac
   __TEXT.__constg_swiftt: 0x133c

   __TEXT.__swift_as_ret: 0xe0
   __TEXT.__swift_as_cont: 0x178
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x2588
+  __TEXT.__unwind_info: 0x2590
   __TEXT.__eh_frame: 0x2758
-  __DATA_CONST.__const: 0x56f9
-  __DATA_CONST.__cfstring: 0x2da0
+  __DATA_CONST.__const: 0x5731
+  __DATA_CONST.__cfstring: 0x2e00
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x230

   __DATA_CONST.__auth_got: 0x14c0
   __DATA_CONST.__got: 0x940
   __DATA_CONST.__auth_ptr: 0x5b0
-  __DATA.__objc_const: 0x8260
-  __DATA.__objc_selrefs: 0x27b8
+  __DATA.__objc_const: 0x8278
+  __DATA.__objc_selrefs: 0x27d0
   __DATA.__objc_ivar: 0x2f8
   __DATA.__objc_data: 0x2990
-  __DATA.__data: 0x2fc8
+  __DATA.__data: 0x2fe8
   __DATA.__bss: 0x3380
   __DATA.__common: 0x78
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3166
+  Functions: 3177
   Symbols:   744
-  CStrings:  3008
+  CStrings:  3017
 
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
