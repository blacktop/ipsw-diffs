## diskimagesiod

> `/usr/libexec/diskimagesiod`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-598.40.3.0.0
-  __TEXT.__text: 0x1e3880
+598.40.4.0.0
+  __TEXT.__text: 0x1e35b4
   __TEXT.__auth_stubs: 0x2450
-  __TEXT.__objc_stubs: 0x6860
-  __TEXT.__objc_methlist: 0x3a1c
-  __TEXT.__gcc_except_tab: 0x1be68
-  __TEXT.__const: 0x17647
-  __TEXT.__cstring: 0x173e5
-  __TEXT.__oslogstring: 0x2dab
-  __TEXT.__objc_methname: 0x78e1
+  __TEXT.__objc_stubs: 0x6840
+  __TEXT.__objc_methlist: 0x3a14
+  __TEXT.__gcc_except_tab: 0x1bea0
+  __TEXT.__const: 0x175e7
+  __TEXT.__cstring: 0x1759c
+  __TEXT.__oslogstring: 0x2e04
+  __TEXT.__objc_methname: 0x78d4
   __TEXT.__objc_classname: 0x667
   __TEXT.__objc_methtype: 0x27fa
   __TEXT.__constg_swiftt: 0x60

   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__ustring: 0x13c
-  __TEXT.__unwind_info: 0x10398
+  __TEXT.__unwind_info: 0x10330
   __TEXT.__eh_frame: 0xf0
-  __DATA_CONST.__const: 0x396d8
-  __DATA_CONST.__cfstring: 0x4c40
+  __DATA_CONST.__const: 0x394b8
+  __DATA_CONST.__cfstring: 0x4c60
   __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__got: 0x628
   __DATA_CONST.__auth_ptr: 0x48
   __DATA.__objc_const: 0x5a18
-  __DATA.__objc_selrefs: 0x1f08
+  __DATA.__objc_selrefs: 0x1f00
   __DATA.__objc_ivar: 0x318
   __DATA.__objc_data: 0x1750
   __DATA.__data: 0xde0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/local/lib/libcurl.4.dylib
-  Functions: 11554
+  Functions: 11537
   Symbols:   800
-  CStrings:  4041
+  CStrings:  4052
 
CStrings:
+ " bytes does not fit before the "
+ " bytes image"
+ " bytes is smaller than its trailer"
+ " exceeds the maximum of "
+ " for "
+ "%.*s: Failed to dup stderr: %d"
+ "%.*s: Failed to open /dev/tty: %d, falling back to stderr"
+ "%.*s: SLA resource has no text form, prompting with a warning instead"
+ "%.*s: SLA: unusable LPic resource"
+ "+[DISLAFrontend(Private) redirectStdoutForDisplay]"
+ "Cannot display SLA: no terminal or stderr to write to"
+ "Malformed SLA LPic resource"
+ "UDIF XML at "
+ "UDIF XML length "
+ "UDIF image of "
+ "WARNING: this disk image contains a software license agreement that cannot be displayed as text. To read it, open the disk image in the Finder. Continuing accepts the license agreement without reading it."
+ "bool DIIOManager::checkForPendingSLA(io_connect_t)"
+ "redirectStdoutForDisplay"
+ "std::expected<CFAutoRelease<CFStringRef>, std::errc> udif::sla::extract_sla_text(const DiskImageUDIF &)"
+ "trailer of a "
- "%.*s: Failed to open /dev/tty: %d"
- "%.*s: SLA resource size (%lld bytes) exceeds maximum (%lld), skipping"
- "+[DISLAFrontend(Private) redirectStdoutToTTY]"
- "/dev/null"
- "CFAutoRelease<CFStringRef> udif::sla::extract_sla_text(const DiskImageUDIF &)"
- "Cannot display SLA: not running in a terminal"
- "SLA resource found but text extraction failed"
- "isStdoutQuietMode"
- "redirectStdoutToTTY"
```
