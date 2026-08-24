## fpassetmanagerd

> `/usr/libexec/fpassetmanagerd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-2.0.0.0.0
-  __TEXT.__text: 0x26d9c
-  __TEXT.__auth_stubs: 0xd90
+2.1.0.0.0
+  __TEXT.__text: 0x26d00
+  __TEXT.__auth_stubs: 0xda0
   __TEXT.__objc_stubs: 0x460
   __TEXT.__objc_methlist: 0x1f8
   __TEXT.__const: 0x7c8
   __TEXT.__cstring: 0xdff
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_typeref: 0x3e6
-  __TEXT.__oslogstring: 0x1a78
+  __TEXT.__oslogstring: 0x1b18
   __TEXT.__swift5_capture: 0x288
   __TEXT.__objc_methtype: 0x274
   __TEXT.__swift_as_entry: 0x28

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__objc_classname: 0xde
-  __TEXT.__objc_methname: 0x648
-  __TEXT.__unwind_info: 0x528
-  __TEXT.__eh_frame: 0xb94
+  __TEXT.__objc_methname: 0x638
+  __TEXT.__unwind_info: 0x538
+  __TEXT.__eh_frame: 0xb84
   __DATA_CONST.__const: 0xa78
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0x6d0
-  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__auth_got: 0x6d8
+  __DATA_CONST.__got: 0x218
   __DATA_CONST.__auth_ptr: 0x1b8
   __DATA.__objc_const: 0x3c8
   __DATA.__objc_selrefs: 0x200
   __DATA.__objc_data: 0x1f8
-  __DATA.__data: 0x660
+  __DATA.__data: 0x670
   __DATA.__common: 0x68
   __DATA.__bss: 0x780
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 384
-  Symbols:   350
+  Functions: 387
+  Symbols:   352
   CStrings:  316
 
Symbols:
+ _$sSo7NSErrorCs5Error10FoundationMc
+ _$ss24_getErrorEmbeddedNSErroryyXlSgxs0B0RzlF
+ _swift_allocError
- _$ss5ErrorP10FoundationE20localizedDescriptionSSvg
CStrings:
+ "Asset %{public}s in index but type mismatch or read failed"
+ "Asset %{public}s... found after update: %ld bytes"
+ "Asset %{public}s... not found in index, checking for bundle updates..."
+ "Asset %{public}s... not found in initial bundle"
+ "Asset %{public}s... still not found after update"
+ "Asset request: bundle=%ld, type=0x%{public}s, id=%{public}s..."
+ "Boot refresh failed for %s"
+ "Bundle already up-to-date, asset %{public}s... does not exist"
+ "Bundle version unchanged, asset %{public}s... does not exist"
+ "Error reading asset: %{public}s"
+ "Failed to build index for %s: %{public}s"
+ "Failed to check for bundle updates: %{public}s"
+ "Failed to create metadata: %{public}s"
+ "Failed to download initial bundle: %{public}s"
+ "Failed to import public key: %{public}s"
+ "Failed to recover metadata: %{public}s"
+ "Force refresh failed: %{public}s"
+ "Force refresh rate limited: %{public}s"
+ "Periodic refresh failed for %s"
+ "Serving asset %{public}s... from fallback: %ld bytes"
+ "Serving asset %{public}s... from initial bundle: %ld bytes"
+ "Serving asset %{public}s...: %ld bytes"
+ "Signature verification error: %{public}s"
+ "Starting asset bundle refresh for %s (trigger: %{public}s)"
+ "domain"
- "Asset %s in index but type mismatch or read failed"
- "Asset %s... found after update: %ld bytes"
- "Asset %s... not found in index, checking for bundle updates..."
- "Asset %s... not found in initial bundle"
- "Asset %s... still not found after update"
- "Asset request: bundle=%ld, type=0x%s, id=%s..."
- "Boot refresh failed for %s: %s"
- "Bundle already up-to-date, asset %s... does not exist"
- "Bundle version unchanged, asset %s... does not exist"
- "Error reading asset: %s"
- "Failed to build index for %s: %s"
- "Failed to check for bundle updates: %s"
- "Failed to create metadata: %s"
- "Failed to download initial bundle: %s"
- "Failed to import public key: %s"
- "Failed to recover metadata: %s"
- "Force refresh failed: %s"
- "Force refresh rate limited: %s"
- "Periodic refresh failed for %s: %s"
- "Serving asset %s... from fallback: %ld bytes"
- "Serving asset %s... from initial bundle: %ld bytes"
- "Serving asset %s...: %ld bytes"
- "Signature verification error: %s"
- "Starting asset bundle refresh for %s (trigger: %s)"
- "localizedDescription"
```
