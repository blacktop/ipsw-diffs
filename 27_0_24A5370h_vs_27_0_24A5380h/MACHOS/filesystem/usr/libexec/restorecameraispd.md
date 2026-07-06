## restorecameraispd

> `/usr/libexec/restorecameraispd`

```diff

-  __TEXT.__text: 0x1c594
-  __TEXT.__auth_stubs: 0xe60
+  __TEXT.__text: 0x1ce9c
+  __TEXT.__auth_stubs: 0xf90
   __TEXT.__objc_stubs: 0x4a0
-  __TEXT.__const: 0x16c0
-  __TEXT.__cstring: 0x3079
+  __TEXT.__const: 0x16d0
+  __TEXT.__cstring: 0x3203
   __TEXT.__gcc_except_tab: 0x4b8
-  __TEXT.__oslogstring: 0x21c0
+  __TEXT.__oslogstring: 0x2280
   __TEXT.__objc_methname: 0x32c
-  __TEXT.__unwind_info: 0x558
-  __DATA_CONST.__const: 0x79b0
-  __DATA_CONST.__cfstring: 0x1460
+  __TEXT.__unwind_info: 0x570
+  __DATA_CONST.__const: 0x80b0
+  __DATA_CONST.__cfstring: 0x15c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x740
-  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__auth_got: 0x7d8
+  __DATA_CONST.__got: 0x148
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_selrefs: 0x128
   __DATA.__data: 0x3aec00
   __DATA.__common: 0x7
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 411
-  Symbols:   281
-  CStrings:  778
+  Functions: 421
+  Symbols:   301
+  CStrings:  802
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Symbols:
+ _AMFDRSealingMapCopyLocalData
+ _CFArrayApplyFunction
+ _CFDictionaryApplyFunction
+ _CFDictionaryGetTypeID
+ _CFDictionarySetValue
+ _CFNumberGetType
+ _CFPreferencesGetAppBooleanValue
+ _CFStringGetCString
+ __xpc_type_bool
+ _dispatch_once
+ _objc_release_x22
+ _unlink
+ _xpc_array_append_value
+ _xpc_array_create
+ _xpc_bool_create
+ _xpc_bool_get_value
+ _xpc_connection_copy_entitlement_value
+ _xpc_data_create
+ _xpc_double_create
+ _xpc_int64_create
+ _xpc_string_create
- _puts
CStrings:
+ "%s: Failed to create file \"%s\" because of permissions. Deleting it (in case it exists) and trying again"
+ "%s: Failed to create file %s: %s"
+ "/usr/local/share/firmware/isp/dcs_isp_fw.bin"
+ "20.55.3"
+ "<UNKNOWN>"
+ "Audit: XPC peer missing %{public}s (pid %{private}d) — would reject\n"
+ "EnforceClientEntitlement"
+ "ISPServicesRemoteFDRCalDataKey"
+ "PRF1: %s-%s: Unexpected references size (Expected %ld, Got %d)\n"
+ "PRF1: %s-%s: Unexpected references size after compression (Expected %ld, Got %ld)\n"
+ "PRF1: %s-%s: Unknown format %d"
+ "PRF1: Couldn't create reference file %s to write\n"
+ "PRF1: Failed to save plist %@\n"
+ "Rejecting XPC peer missing %{public}s (pid %{private}d)\n"
+ "com.apple.cameraispd"
+ "com.apple.private.cameraispd.client"
+ "createXpcFromType got a dictionary with null value (for key %s)"
+ "fopen_protected"
- "20.50.6"
- "Couldn't create reference file %s to write\n"
- "Failed to save plist"
- "Unexpected references size (Expected %ld, Got %d)\n"
- "Unexpected references size after compression (Expected %ld, Got %ld)\n"

```
