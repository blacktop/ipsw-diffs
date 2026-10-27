## diskimagesiod

> `/usr/libexec/diskimagesiod`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__info_plist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
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

-598.0.1.0.0
-  __TEXT.__text: 0x202c0c
+598.40.4.0.0
+  __TEXT.__text: 0x203c3c
   __TEXT.__auth_stubs: 0x2580
-  __TEXT.__objc_stubs: 0x6f00
-  __TEXT.__objc_methlist: 0x3d5c
-  __TEXT.__const: 0x17e47
-  __TEXT.__gcc_except_tab: 0x1e134
-  __TEXT.__objc_methname: 0x8121
-  __TEXT.__oslogstring: 0x3c3d
-  __TEXT.__cstring: 0x159b7
+  __TEXT.__objc_stubs: 0x6ee0
+  __TEXT.__objc_methlist: 0x3d54
+  __TEXT.__const: 0x17e97
+  __TEXT.__gcc_except_tab: 0x1e23c
+  __TEXT.__objc_methname: 0x8114
+  __TEXT.__oslogstring: 0x3c96
+  __TEXT.__cstring: 0x15b6e
   __TEXT.__objc_classname: 0x6e0
   __TEXT.__objc_methtype: 0x2ca7
   __TEXT.__constg_swiftt: 0x60

   __TEXT.__swift5_types: 0x4
   __TEXT.__ustring: 0x13c
   __TEXT.__info_plist: 0x40e
-  __TEXT.__unwind_info: 0x10f10
+  __TEXT.__unwind_info: 0x10f80
   __TEXT.__eh_frame: 0xf0
-  __DATA_CONST.__const: 0x3ac10
-  __DATA_CONST.__cfstring: 0x54a0
+  __DATA_CONST.__const: 0x3aed0
+  __DATA_CONST.__cfstring: 0x54c0
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__got: 0x718
   __DATA_CONST.__auth_ptr: 0x50
   __DATA.__objc_const: 0x5f20
-  __DATA.__objc_selrefs: 0x20b0
+  __DATA.__objc_selrefs: 0x20a8
   __DATA.__objc_ivar: 0x340
   __DATA.__objc_data: 0x1890
   __DATA.__data: 0xe40

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 12040
+  Functions: 12057
   Symbols:   850
-  CStrings:  4354
+  CStrings:  4365
 
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
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
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
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "/dev/null"
- "CFAutoRelease<CFStringRef> udif::sla::extract_sla_text(const DiskImageUDIF &)"
- "Cannot display SLA: not running in a terminal"
- "SLA resource found but text extraction failed"
- "isStdoutQuietMode"
- "redirectStdoutToTTY"
```
