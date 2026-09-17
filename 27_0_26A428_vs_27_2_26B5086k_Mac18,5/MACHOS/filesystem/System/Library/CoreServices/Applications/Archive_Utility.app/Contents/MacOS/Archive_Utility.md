## Archive Utility

> `/System/Library/CoreServices/Applications/Archive Utility.app/Contents/MacOS/Archive Utility`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-183.0.0.0.0
-  __TEXT.__text: 0x2d9e8
-  __TEXT.__auth_stubs: 0x1100
-  __TEXT.__objc_stubs: 0x44c0
-  __TEXT.__objc_methlist: 0x1ea8
-  __TEXT.__cstring: 0x520e
+184.0.0.0.0
+  __TEXT.__text: 0x2df6c
+  __TEXT.__auth_stubs: 0x1140
+  __TEXT.__objc_stubs: 0x4520
+  __TEXT.__objc_methlist: 0x1ee0
+  __TEXT.__cstring: 0x538e
   __TEXT.__const: 0x14c4
-  __TEXT.__gcc_except_tab: 0x2588
-  __TEXT.__objc_methname: 0x5a24
+  __TEXT.__gcc_except_tab: 0x2678
+  __TEXT.__objc_methname: 0x5a79
   __TEXT.__objc_classname: 0x4fb
   __TEXT.__objc_methtype: 0x11ac
   __TEXT.__ustring: 0xa04
-  __TEXT.__unwind_info: 0xe60
+  __TEXT.__unwind_info: 0xe70
   __DATA_CONST.__const: 0x12b0
-  __DATA_CONST.__cfstring: 0x2e00
+  __DATA_CONST.__cfstring: 0x2f20
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__objc_arraydata: 0xb0
-  __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x898
-  __DATA_CONST.__got: 0x2a0
+  __DATA_CONST.__objc_arraydata: 0xc8
+  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA_CONST.__auth_got: 0x8b8
+  __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0x2fe8
-  __DATA.__objc_selrefs: 0x1858
-  __DATA.__objc_ivar: 0x27c
+  __DATA.__objc_const: 0x3048
+  __DATA.__objc_selrefs: 0x1870
+  __DATA.__objc_ivar: 0x284
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0x468
   __DATA.__common: 0x288

   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/FileProvider.framework/Versions/A/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/Bom.framework/Versions/A/Bom

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 743
-  Symbols:   355
-  CStrings:  2323
+  Functions: 748
+  Symbols:   361
+  CStrings:  2336
 
Symbols:
+ _SecCodeCheckValidity
+ _SecCodeCopyGuestWithAttributes
+ _SecCodeCopySigningInformation
+ _SecRequirementCreateWithString
+ _kSecCodeInfoIdentifier
+ _kSecGuestAttributeAudit
CStrings:
+ " or "
+ "Leaving source in place: open request did not come from a UI agent, so %@ does not apply"
+ "SenderIsUIAgent: could not identify the sender of the open request: %d"
+ "SenderIsUIAgent: open request came from %@, which is not a UI agent"
+ "SenderIsUIAgent: open request carries no usable sender audit token"
+ "TB,V_requestorIsUIAgent"
+ "_requestorIsUIAgent"
+ "anchor apple and (%@)"
+ "canRelocateCopySourceForPref:"
+ "com.apple.coreservices.uiagent"
+ "com.apple.dock"
+ "componentsJoinedByString:"
+ "identifier \"%@\""
+ "requestorIsUIAgent"
+ "setRequestorIsUIAgent:"
- "removeItemAtURL:error:"
- "trashItemAtURL:resultingItemURL:error:"
```
