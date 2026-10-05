## DVTInstrumentsUtilities

> `/System/Library/PrivateFrameworks/DVTInstrumentsUtilities.framework/DVTInstrumentsUtilities`

```diff

-64578.160.1.0.0
-  __TEXT.__text: 0x30d28
-  __TEXT.__objc_methlist: 0x2fdc
-  __TEXT.__const: 0x177c
-  __TEXT.__gcc_except_tab: 0x14b8
-  __TEXT.__cstring: 0x5cda
-  __TEXT.__oslogstring: 0x799
+64578.209.1.0.0
+  __TEXT.__text: 0x30ed0
+  __TEXT.__objc_methlist: 0x2fcc
+  __TEXT.__const: 0x1770
+  __TEXT.__gcc_except_tab: 0x14c4
+  __TEXT.__cstring: 0x5da7
+  __TEXT.__oslogstring: 0x7d1
   __TEXT.__ustring: 0x34
-  __TEXT.__swift5_typeref: 0x343
-  __TEXT.__constg_swiftt: 0x374
-  __TEXT.__swift5_reflstr: 0x175
+  __TEXT.__swift5_typeref: 0x345
+  __TEXT.__constg_swiftt: 0x354
+  __TEXT.__swift5_reflstr: 0x181
   __TEXT.__swift5_fieldmd: 0x2b8
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x40
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x18
-  __TEXT.__swift_as_cont: 0x1c
+  __TEXT.__swift_as_cont: 0x8
   __TEXT.__swift5_capture: 0x38
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x80
   __TEXT.__swift5_types2: 0x4
   __TEXT.__swift5_assocty: 0x68
-  __TEXT.__unwind_info: 0x18b8
-  __TEXT.__eh_frame: 0x530
+  __TEXT.__unwind_info: 0x18a8
+  __TEXT.__eh_frame: 0x580
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x18c0
+  __DATA_CONST.__objc_selrefs: 0x18a8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x148
   __DATA_CONST.__objc_arraydata: 0x120
   __DATA_CONST.__got: 0x588
   __AUTH_CONST.__const: 0x11b8
-  __AUTH_CONST.__cfstring: 0x8a40
+  __AUTH_CONST.__cfstring: 0x8b20
   __AUTH_CONST.__objc_const: 0x6360
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__auth_got: 0xbb0
+  __AUTH_CONST.__auth_got: 0xbd0
   __AUTH.__objc_data: 0x1c88
   __AUTH.__data: 0x178
   __DATA.__objc_ivar: 0x318
   __DATA.__data: 0xbf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1533
-  Symbols:   619
-  CStrings:  1286
+  Functions: 1531
+  Symbols:   624
+  CStrings:  1292
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFGetTypeID
+ _CFRelease
+ _DVTAuditedCodeValidlyHoldsEntitlement
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ _os_variant_allows_internal_security_policies
+ _swift_release_x27
- _CC_MD5_Final
- _CC_MD5_Init
- _CC_MD5_Update
- _swift_release_x26
CStrings:
+ "\"\\"
+ "DVTEntitlementCheck"
+ "invalid entitlement name: contains a quote or backslash"
+ "the audited process does not hold %@"
+ "the audited process holds %@ but is neither a platform binary nor debuggable (%#x)"
+ "the entitlement name was missing or malformed"
+ "unable to inspect the audited process"
+ "unable to read the audited process' code signing status"
- "-[XREngineeringTypeDefinitions checksum]"
- "chunk.length <= chunkSizeTarget"
```
